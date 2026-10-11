export const meta = {
  name: 'mockup-actor-critic',
  description: 'Movement II REAPER mockup: actor-critic cycles (3 parallel critics, then one actor who edits, rebuilds and renders)',
  phases: [{ title: 'Critique' }, { title: 'Act' }],
}
const ROOT = '/Users/gooby/sandbox/claude_composes/symphony/mvt2/reaper'
const LENS_A = 'Articulation and phrasing, instrument by instrument against the score: legato transitions (are slurred lines connected, do legato patches get overlapping notes, are chords ever sent to a monophonic legato patch), note lengths and releases, keyswitch correctness and timing, pizzicato, tremolo, tenuto, accents (Dan: soft, 2-4 dB), breath marks, ties, harp and timpani technique. Also whether a better Hollywood Orchestra patch exists for a passage (e.g. individual articulation patches, divisi patches, con sordino, portamento legato, solo vs section).'
const LENS_B = 'Balance and levels: every stem against its printed dynamic and its role (melody and solos above accompaniment, the bass solid but not boomy, timpani and brass not covering), consistency of the dynamic mapping between instruments (does p sound like p in every family), section balance by orchestration norms (Rimsky-Korsakov and Adler in reference-books), track volumes and the CC11/velocity mapping that produces the levels.'
const LENS_C = [
  'Blend and space: one room. Reverb, seating and panning, mic positions (Close/Main/Surround column volumes in the patches), tone matching between sample sets, the low-end build-up versus the reference recording spectrum.',
  'Dynamics over time: the shape of every hairpin and phrase, the loudness arc of the whole movement against the score (climax at bars 59-63, the return at 65, the coda), loudness range, swells on long notes, decays, and comparison with the reference recording of a real orchestra.',
  'Tempo, timing and transitions: the tempo map against the printed tempos and rit./allargando/fermata steps in global.ily, the attack latency of legato and sustain samples (notes that sound late against the beat, especially slow-attack strings and brass; lead compensation), keyswitch lead times, note starts against each other between sections, endings of phrases and the final fermata.',
  'Holistic comparison: listen through the data as a conductor would. Compare the current render with cycle 0 and with the render five cycles back (if it exists) and with the reference recording. Which passages are now the weakest? What still sounds like a machine? Name the three to six changes that would most improve the next render, across any area.',
]
const pad = n => String(n).padStart(2, '0')
const start = args.start, end = args.end
let prev = args.prev
const results = []
for (let N = start; N <= end; N++) {
  const lensC = LENS_C[(N - 1) % LENS_C.length]
  const slots = [['A', LENS_A], ['B', LENS_B], ['C', lensC]]
  if (N !== args.skipCritics) {
    const critique = (slot, lens) => `Read /Users/gooby/sandbox/claude_composes/symphony/mvt2/reaper/loop/critic_prompt.md and carry it out exactly, with these values substituted: {SLOT}=${slot}, {N}=${N}, {N2}=${pad(N)}, {PREV}=${prev}, {PREV2}=${pad(prev)}, {LENS}=${lens}`
    const reports = await parallel(slots.map(([slot, lens]) => () =>
      agent(critique(slot, lens), { label: `c${pad(N)} critic ${slot}`, phase: 'Critique', agentType: 'general-purpose' })))
    const got = reports.filter(Boolean).length
    log(`cycle ${N}: ${got}/3 critic reports`)
    if (got === 0) { log(`cycle ${N}: no reports, stopping`); break }
  } else {
    log(`cycle ${N}: critic reports already written before the interruption; going straight to the actor`)
  }
  const actorPrompt = `Read ${ROOT}/loop/actor_prompt.md and carry it out exactly, with these values substituted: {N}=${N}, {N2}=${pad(N)}, {PREV}=${prev}.`
  const SCHEMA = { type: 'object', properties: {
    ok: { type: 'boolean', description: 'true if cycle render finished and metrics were written' },
    mp3: { type: 'string' }, summary: { type: 'string' },
    lufs: { type: 'number' }, lra: { type: 'number' }, true_peak: { type: 'number' } }, required: ['ok', 'summary'] }
  let act = await agent(actorPrompt, { label: `c${pad(N)} actor`, phase: 'Act', agentType: 'general-purpose', schema: SCHEMA })
  if (!act || !act.ok) {
    log(`cycle ${N}: actor failed (${act ? act.summary.slice(0, 200) : 'no result'}), retrying once`)
    act = await agent(actorPrompt + ' A previous actor attempt for this cycle failed or stopped partway; inspect cycles/c' + pad(N) + '/ and the state of REAPER, finish or redo the work, and render.', { label: `c${pad(N)} actor retry`, phase: 'Act', agentType: 'general-purpose', schema: SCHEMA })
  }
  results.push({ cycle: N, actor: act })
  if (!act || !act.ok) { log(`cycle ${N}: actor failed twice, stopping`); break }
  log(`cycle ${N} done: ${act.lufs} LUFS, LRA ${act.lra}, TP ${act.true_peak}`)
  prev = N
}
return { last_good: prev, results }
