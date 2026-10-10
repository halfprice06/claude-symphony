"""r04 (critic 3, plan 8): a staff name with no entry in config.stems falls back to the config of the instrument its
name names (family words), instead of aborting the render. resolve(cfg, staff) -> (config key, stem config)."""
import re

RULES = [  # first match wins; patterns on the lower-case staff name
    (r"piccolo|flute|flauto", "Flutes 12"), (r"cor anglais|english horn|corno inglese", "Cor anglais"),
    (r"oboe", "Oboes 12"), (r"bass clarinet|clarinetto basso", "Bass clarinet"), (r"clarinet", "Clarinets 12"),
    (r"contrabassoon|contrafagotto|double bassoon", "Contrabassoon"), (r"bassoon|fagott", "Bassoons 12"),
    (r"horn|corno", "Horns 12"), (r"trumpet|tromba|cornet", "Trumpets 12"), (r"bass trombone", "Bass trombone"),
    (r"trombone", "Trombones 12"), (r"tuba", "Tuba"), (r"timpani|timp", "Timpani"), (r"harp|arpa", "Harp RH"),
    (r"violins? ?(ii|2)\b|second violin", "Violins II"), (r"violin", "Violins I"), (r"viola", "Violas"),
    (r"violoncell|cello", "Violoncellos"), (r"contrabass|double bass|basses|bass", "Double basses"),
]


def resolve(cfg, st):
    S = cfg["stems"]
    if st in S:
        return st, S[st]
    low = st.lower()
    for pat, k in RULES:
        if re.search(pat, low) and k in S:
            return k, S[k]
    return None, None


def fill(cfg, staves):
    """Add a fallback entry to cfg['stems'] for every staff name in staves that has none; returns {staff: source key}."""
    used = {}
    for st in staves:
        if st not in cfg["stems"] and st != "drums":
            k, sc = resolve(cfg, st)
            if sc is not None:
                cfg["stems"][st] = dict(sc); used[st] = k
    return used
