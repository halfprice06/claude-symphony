// Plays a timed MIDI event list through Apple's built-in General MIDI synth (DLSMusicDevice,
// gs_instruments.dls) and writes a float WAV. Offline, so nothing is heard while it runs.
// Usage: gmrender events.txt out.wav        (events.txt from midi2events.py)
import AVFoundation
import AudioToolbox

let args = CommandLine.arguments
struct Ev { let t: Double; let s: UInt8; let a: UInt8; let b: UInt8 }
var evs: [Ev] = []
var length = 0.0
for line in try! String(contentsOfFile: args[1], encoding: .utf8).split(separator: "\n") {
  let f = line.split(separator: " ")
  if f[0] == "len" { length = Double(f[1])! }
  else { evs.append(Ev(t: Double(f[0])!, s: UInt8(f[1])!, a: UInt8(f[2])!, b: UInt8(f[3])!)) }
}
let sr = 44100.0
let quantum: AVAudioFrameCount = 64   // events land within 1.5 ms of their time
let lead = 0.1
let engine = AVAudioEngine()
let fmt = AVAudioFormat(standardFormatWithSampleRate: sr, channels: 2)!
try! engine.enableManualRenderingMode(.offline, format: fmt, maximumFrameCount: quantum)
let desc = AudioComponentDescription(componentType: kAudioUnitType_MusicDevice,
                                     componentSubType: kAudioUnitSubType_DLSSynth,
                                     componentManufacturer: kAudioUnitManufacturer_Apple,
                                     componentFlags: 0, componentFlagsMask: 0)
let synth = AVAudioUnitMIDIInstrument(audioComponentDescription: desc)
engine.attach(synth)
engine.connect(synth, to: engine.mainMixerNode, format: fmt)
try! engine.start()
let file = try! AVAudioFile(forWriting: URL(fileURLWithPath: args[2]), settings: fmt.settings)
let buf = AVAudioPCMBuffer(pcmFormat: engine.manualRenderingFormat, frameCapacity: quantum)!
let total = AVAudioFramePosition((length + lead) * sr)
var k = 0
while engine.manualRenderingSampleTime < total {
  let t = Double(engine.manualRenderingSampleTime) / sr - lead
  while k < evs.count && evs[k].t <= t {
    let e = evs[k]
    if e.s & 0xf0 == 0xc0 || e.s & 0xf0 == 0xd0 { synth.sendMIDIEvent(e.s, data1: e.a) }
    else { synth.sendMIDIEvent(e.s, data1: e.a, data2: e.b) }
    k += 1
  }
  let n = AVAudioFrameCount(min(AVAudioFramePosition(quantum), total - engine.manualRenderingSampleTime))
  if try! engine.renderOffline(n, to: buf) == .success { try! file.write(from: buf) }
}
print("wrote", args[2], evs.count, "events")
