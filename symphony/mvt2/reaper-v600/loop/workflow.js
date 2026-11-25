export const meta = {
  name: 'mvt2-mockup-actor-critic',
  description: 'Movement II REAPER mockup, series 2 (v600): actor-critic cycles (3 parallel critics, then one actor who edits, rebuilds and renders under the shared REAPER lock)',
  phases: [{ title: 'Critique' }, { title: 'Act' }],
}
const ROOT = '/Users/gooby/sandbox/claude_composes/symphony/mvt2/reaper-v600'
const LENS_A = 'Articulation and phrasing, instrument by instrument against the score: legato transitions (are slurred lines connected, do legato patches get overlapping notes, are chords ever sent to a monophonic legato patch), note lengths and releases, keyswitch correctness and timing, tenuto and portato (the violas\' sotto voce portato eighths, bars 48-51; the molto sostenuto tenutos of bars 61-62), accents (Dan: weight, not bite; Trombone 1\'s marcato quotation, bars 63-64; measure 2-5 kHz attack against the body), tremolo (bars 61-64), pizzicato (bars 37-44), sul tasto (Violins II, bars 37-40), con sordino and the coda\'s mutes, the re-bows of long string notes (the opening chord, bar 66, the 4 soli pedals, the final chord: dips, level steps, any audible pulse), breath marks, ties, the harp\'s arpeggios and harmonics, the timpani rolls and strokes. Also whether a better Hollywood Orchestra patch exists for a passage (individual articulation patches, divisi patches for the div. and 4 soli passages, con sordino, portamento legato, solo vs section for the bars 17-22 violin solo, 2-player or a2 patches).'
const LENS_B = 'Balance and levels: every stem against its printed dynamic and its role (the solos above their accompaniment: Horn 1 bars 7-14, Oboe 1 and the solo violin bars 15-22, the bass clarinet bars 31-36, Flute 1 and the cor anglais bars 37-50, Clarinet 1 in the coda; the bass solid but not boomy; timpani and low brass not covering at the bar 61-64 climax and bars 79-82), consistency of the dynamic mapping between instruments (does p sound like p in every family; the half-section divisi and 4 soli tracks against the full sections), section balance by orchestration norms (Rimsky-Korsakov and Adler in reference-books), track gains, soft trims and the CC11/velocity mapping that produces the levels.'
const LENS_C = [
  'Blend and space: one room. Reverb, seating and panning, mic positions (Close/Main/Mid column volumes in the patches), tone matching between sample sets (the DIV A/DIV B half-section tracks against their sections, the harp harmonics, muted against open strings), the low-end build-up against several reference recordings.',
  'Dynamics over time: the shape of every hairpin and phrase, the loudness arc of the whole movement against the score (the bar 47 fp, the animando crescendo of bars 53-60 into the Largamente climax of bars 61-64, the niente of bar 66, the ff cadence of bars 79-82, the ppp coda and the morendo of bar 91), loudness range of the master and the delivered mp3 (BRIEF item 6), swells and loop pulsing on long notes (BRIEF item 8), decays, and comparison with real recordings.',
  'Tempo, timing and transitions: the tempo map against the printed tempos and the rit./allargando/animando/sostenuto steps in global.ily (score_config.py RAMP_SPANS, PHRASE_ARCS, TEMPO_PUSH, CAESURA), the Adagio / Poco più mosso / Largamente / Tempo I changes, attack latency of legato and sustain samples (soft string entries and slow legato arrivals that sound late against the beat; lead compensation; Dan\'s S2), keyswitch lead times, note starts against each other between sections, endings of phrases, the tutti breaths before bars 59, 61 and 82 (qn 196, 204, 268; CAESURA at 204 and 268), and the final fermata.',
  'Holistic comparison: listen through the data as a conductor would. Compare the current render with the c27 port baseline, with the render five cycles back (if it exists), with series 1\'s c26 render of v77 on unchanged passages, and with real recordings. Which passages are now the weakest? What still sounds like a machine? Name the three to six changes that would most improve the next render, across any area.',
]
const pad = n => String(n).padStart(2, '0')
const start = args.start, end = args.end
let prev = args.prev
const results = []
for (let N = start; N <= end; N++) {
  const lensC = LENS_C[(N - 1) % LENS_C.length]
  const slots = [['A', LENS_A], ['B', LENS_B], ['C', lensC]]
  if (N !== args.skipCritics) {
    const critique = (slot, lens) => `Read ${ROOT}/loop/critic_prompt.md and carry it out exactly, with these values substituted: {SLOT}=${slot}, {N}=${N}, {N2}=${pad(N)}, {PREV}=${prev}, {PREV2}=${pad(prev)}, {LENS}=${lens}`
    const reports = await parallel(slots.map(([slot, lens]) => () =>
      agent(critique(slot, lens), { label: `mvt2 c${pad(N)} critic ${slot}`, phase: 'Critique', agentType: 'general-purpose' })))
    const got = reports.filter(Boolean).length
    log(`cycle ${N}: ${got}/3 critic reports`)
    if (got === 0) { log(`cycle ${N}: no reports, stopping`); break }
  } else {
    log(`cycle ${N}: critic reports already written; going straight to the actor`)
  }
  const actorPrompt = `Read ${ROOT}/loop/actor_prompt.md and carry it out exactly, with these values substituted: {N}=${N}, {N2}=${pad(N)}, {PREV}=${prev}.`
  const SCHEMA = { type: 'object', properties: {
    ok: { type: 'boolean', description: 'true if the cycle render finished and metrics were written' },
    mp3: { type: 'string' }, summary: { type: 'string' },
    lufs: { type: 'number' }, lra: { type: 'number' }, true_peak: { type: 'number' } }, required: ['ok', 'summary'] }
  let act = await agent(actorPrompt, { label: `mvt2 c${pad(N)} actor`, phase: 'Act', agentType: 'general-purpose', schema: SCHEMA })
  if (!act || !act.ok) {
    log(`cycle ${N}: actor failed (${act ? act.summary.slice(0, 200) : 'no result'}), retrying once`)
    act = await agent(actorPrompt + ' A previous actor attempt for this cycle failed or stopped partway; inspect cycles/c' + pad(N) + '/, the REAPER lock (~/.rpr-bridge/REAPER.lock: release it only if it is this thread\'s, owner "mvt2") and the state of REAPER, finish or redo the work, and render.', { label: `mvt2 c${pad(N)} actor retry`, phase: 'Act', agentType: 'general-purpose', schema: SCHEMA })
  }
  results.push({ cycle: N, actor: act })
  if (!act || !act.ok) { log(`cycle ${N}: actor failed twice, stopping`); break }
  log(`cycle ${N} done: ${act.lufs} LUFS, LRA ${act.lra}, TP ${act.true_peak}`)
  prev = N
}
return { last_good: prev, results }
