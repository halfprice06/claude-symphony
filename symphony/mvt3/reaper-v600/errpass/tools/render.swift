import AVFoundation
let a = CommandLine.arguments
let lines = try! String(contentsOfFile: a[1], encoding: .utf8).split(separator: "\n")
let bank = URL(fileURLWithPath: "/System/Library/Components/CoreAudio.component/Contents/Resources/gs_instruments.dls")
let engine = AVAudioEngine()
let fmt = AVAudioFormat(standardFormatWithSampleRate: 44100, channels: 2)!
try! engine.enableManualRenderingMode(.offline, format: fmt, maximumFrameCount: 256)
var samplers: [Int: AVAudioUnitSampler] = [:]
var progs: [Int: UInt8] = [:]
var events: [(Double, Int, Bool, UInt8, UInt8)] = []
var length = 10.0
for l in lines {
  let f = l.split(separator: " ")
  if f[0] == "inst" {
    let s = AVAudioUnitSampler(); engine.attach(s)
    engine.connect(s, to: engine.mainMixerNode, format: fmt)
    s.pan = Float(f[3])!; s.overallGain = -14
    samplers[Int(f[1])!] = s; progs[Int(f[1])!] = UInt8(f[2])!
  } else if f[0] == "len" { length = Double(f[1])! }
  else if f[0] == "ev" { events.append((Double(f[1])!, Int(f[2])!, f[3] == "on", UInt8(f[4])!, UInt8(f[5])!)) }
}
try! engine.start()
for (i, s) in samplers {
  try! s.loadSoundBankInstrument(at: bank, program: progs[i]!, bankMSB: 0x79, bankLSB: 0)
}
let file = try! AVAudioFile(forWriting: URL(fileURLWithPath: a[2]), settings: fmt.settings)
let buf = AVAudioPCMBuffer(pcmFormat: engine.manualRenderingFormat, frameCapacity: 256)!
let total = AVAudioFramePosition(length * 44100)
var k = 0
let lead = 0.25
while engine.manualRenderingSampleTime < total {
  let t = Double(engine.manualRenderingSampleTime) / 44100.0 - lead
  while k < events.count && events[k].0 <= t {
    let e = events[k]; let s = samplers[e.1]!
    if e.2 { s.startNote(e.3, withVelocity: e.4, onChannel: 0) } else { s.stopNote(e.3, onChannel: 0) }
    k += 1
  }
  let n = AVAudioFrameCount(min(256, total - engine.manualRenderingSampleTime))
  if try! engine.renderOffline(n, to: buf) == .success { try! file.write(from: buf) }
}
print("wrote", a[2])
