# Featured lines for the movement II score video (v77 bar numbers (the mockup's score version), bars inclusive).
# role "p" = main line (red), "s" = counter-melody (blue).
FEATURES = [
    # (first bar, last bar, [(staff, role), ...], caption)
    (1, 2, [("Violins I", "p")], "Movement I's last chord: the violins hold its C"),
    (3, 5, [("Horns 3·4", "p")], "The winds take the chord; horn 3 turns C–D♭–C"),
    (6, 14, [("Horns 1·2", "p")], "Theme A in horn 1, without strings"),
    (15, 21, [("Oboes 1·2", "p"), ("Violins I", "p")], "Oboe and first violins answer each other"),
    (22, 22, [("Oboes 1·2", "p"), ("Violins I", "p"), ("Violins II", "p")], "Oboe and first violins answer each other"),
    (23, 30, [("Violins I", "p"), ("Violins II", "p"), ("Violoncellos", "s")], "Theme A in the violins, cello counter-melody"),
    (31, 36, [("Bass clarinet", "p")], "Bass clarinet solo over an A♭ pedal"),
    (37, 40, [("Flutes 1·2", "p")], "Poco più mosso: theme B in flute 1"),
    (41, 43, [("Flutes 1·2", "p"), ("Cor anglais", "p")], "Theme B: cor anglais and flute in tenths"),
    (44, 44, [("Flutes 1·2", "p"), ("Cor anglais", "p"), ("Oboes 1·2", "p")], "Theme B: cor anglais and flute in tenths"),
    (45, 46, [("Oboes 1·2", "p"), ("Violoncellos", "p")], "Theme B in B♭ minor: oboe, cellos an octave lower"),
    (47, 47, [("Cor anglais", "p"), ("Oboes 1·2", "p"), ("Violoncellos", "p")], "Movement I's second theme, in F♯ minor: cor anglais"),
    (48, 51, [("Cor anglais", "p")], "Movement I's second theme, in F♯ minor: cor anglais"),
    (52, 56, [("Violins I", "p"), ("Violins II", "p"), ("Horns 1·2", "s"), ("Clarinets 1·2", "s")], "Theme B in the violins; horn and clarinet counter-melody"),
    (57, 60, [("Violins I", "p"), ("Violins II", "p"), ("Horns 1·2", "s"), ("Violoncellos", "s")], "Poco a poco animando, toward the climax"),
    (61, 62, [("Flutes 1·2", "p"), ("Violins I", "p")], "Largamente: the climax on D♭"),
    (63, 64, [("Trombones 1·2", "p")], "Movement I's first theme, ff in A minor: trombone 1"),
    (65, 70, [("Horns 1·2", "p")], "Tempo I: horn 1 alone, the motto's tail"),
    (70, 70, [("Violins I", "p"), ("Violins II", "p")], "Tempo I: horn 1 alone, the motto's tail"),
    (71, 78, [("Violins I", "p"), ("Violins II", "p"), ("Violoncellos", "s"), ("Horns 1·2", "s")], "Theme A returns in the violins; cellos and horns counter-melody"),
    (79, 82, [("Violins I", "p"), ("Violins II", "p")], "The peak (F6, ff) and the full close"),
    (83, 83, [("Harp RH", "p")], "Coda: harp harmonics, theme A's head"),
    (84, 84, [("Timpani", "p")], "The timpani answer"),
    (85, 85, [("Timpani", "p"), ("Clarinets 1·2", "p")], "Clarinet 1: the motto's tail, one last time"),
    (86, 88, [("Clarinets 1·2", "p")], "Clarinet 1: the motto's tail, one last time"),
    (89, 90, [("Violins I", "p"), ("Clarinets 1·2", "p")], "The violins take over the clarinet's C"),
    (91, 92, [("Violins I", "p")], "The violins end on C, the note the movement began with"),
]

# First bar of each video system.
BREAKS = [1, 4, 7, 11, 15, 19, 23, 27, 31, 34, 37, 41, 45, 49, 53, 57, 61, 65, 68, 71, 75, 79, 83, 87, 90]

COLORS = {"p": (0.69, 0.09, 0.20), "s": (0.10, 0.36, 0.62)}
