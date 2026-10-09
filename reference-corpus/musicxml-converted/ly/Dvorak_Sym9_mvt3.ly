\version "2.24.3"
% automatically converted by musicxml2ly from ../xml/Dvorak_Sym9_mvt3.musicxml
\pointAndClickOff

%% additional definitions required by the score:
ffz = #(make-dynamic-script "ffz")
fpp = #(make-dynamic-script "fpp")
fz = #(make-dynamic-script "fz")

\header {
    title =  "Symphony No. 9"
    composer =  "Antonin Dvořák"
    encodingsoftware =  "MuseScore 4.2.1"
    encodingdate =  "2024-06-26"
    source =  "https://musescore.com/score/4602736"
    subtitle =  "III - Molto Vivace"
    }

#(set-global-staff-size 13.714285714285715)
\paper {
    
    paper-width = 21.01\cm
    paper-height = 39.85\cm
    top-margin = 1.0\cm
    bottom-margin = 1.0\cm
    left-margin = 0.5\cm
    right-margin = 0.5\cm
    indent = 2.0471282051282054\cm
    short-indent = 1.6161538461538465\cm
    }
\layout {
    \context { \Score
        skipBars = ##t
        }
    }
PartPOneVoiceOne =  \relative e''' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key g \major | % 1
        \tempo "Molto vivace" 2.=80 \stemDown e8 ^ "a 2" _\f \stemDown e8
        \stemDown e2 ~ | % 2
        \stemDown e2. | % 3
        \stemDown b8 \stemDown b8 \stemDown b2 ~ | % 4
        \stemDown b2. \bar "||"
        R2.*3 \pageBreak | % 8
        R2.*5 | % 13
        r4 \stemDown b8 _. _\p \stemDown b8 _. \stemDown b4 _. | % 14
        \stemDown e,4 _. \stemDown e4 _. r4 \pageBreak | % 15
        r4 \stemDown fis4 -. \stemDown a4 -. | % 16
        \stemDown g8 ( \stemDown fis8 \stemDown e4 ) r4 | % 17
        r4 \stemDown b'8 -. \stemDown b8 -. \stemDown b4 -. | % 18
        \stemDown e,4 _. \stemDown e4 _. r4 | % 19
        r4 \stemDown fis4 -. \stemDown a4 -. | \barNumberCheck #20
        \stemDown g8 ( \stemDown fis8 \stemDown e4 ) r4 \pageBreak | % 21
        R2.*5 \pageBreak | % 26
        R2.*5 \pageBreak | % 31
        R2.*5 \pageBreak | % 36
        R2.*6 \pageBreak | % 42
        r4 \stemDown b'8 ^ "a 2" _\ff \stemDown b8 \stemDown b4 | % 43
        \stemDown e,4 \stemDown e4 r4 | % 44
        r4 \stemDown g4 -. \stemDown b4 -. | % 45
        \stemDown g8 ( \stemDown fis8 \stemDown e4 ) r4 | % 46
        r4 \stemDown b'8 \stemDown b8 \stemDown b4 \pageBreak | % 47
        \stemDown e,4 ^ "a 2" \stemDown e4 r4 | % 48
        r4 \stemDown g4 -. \stemDown b4 -. | % 49
        \mark \markup { 1 } \stemDown g8 ( \stemDown fis8 \stemDown e4 )
        \stemDown e'4 | \barNumberCheck #50
        \stemDown d2 -> \stemDown cis4 ~ -> | % 51
        \stemDown cis4 \stemDown c2 -> | % 52
        \stemDown b2 -> \stemDown e,4 ~ \pageBreak | % 53
        \stemDown e4 \stemDown e'2 -> | % 54
        \stemDown d2 -> \stemDown cis4 ~ -> | % 55
        \stemDown cis4 \stemDown c2 -> | % 56
        \stemDown b8 ( \stemDown e8 ) \stemDown e4 -. \stemDown e8 (
        \stemDown c8 ) | % 57
        \stemDown b8 ( \stemDown e8 ) \stemDown e4 -. \stemDown e8 (
        \stemDown c8 ) | % 58
        \stemDown b8 ( \stemDown e8 ) \stemDown e4 -. \stemDown e8 (
        \stemDown c8 ) | % 59
        \stemDown e4 -. r4 r4 }
    \pageBreak | \barNumberCheck #60
    R2.*7 \pageBreak | % 67
    R2. \bar "||"
    \key e \major \stemDown gis,8 ( ^\p ^\markup{ \large {Poco
            sostenuto} } \stemDown b8 ) \stemDown b2 ~ | % 69
    \stemDown b2 \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 \stemDown b8 \stemDown fis8 }
    | \barNumberCheck #70
    \stemDown e2 \stemDown fis4 | % 71
    \stemDown gis8 ( \stemDown b8 ) \stemDown b2 ~ \pageBreak | % 72
    \stemUp b8 \stemUp e8 ( \stemUp dis8 \stemUp cis8 \stemDown b4 ~ | % 73
    \stemDown b8 ) \stemDown cis8 ( \stemDown b8 \stemDown gis8
    \stemDown b4 ~ | % 74
    \stemDown b8 \stemDown gis8 \stemDown fis8 \stemDown gis8 \stemDown
    b8 \stemDown gis8 | % 75
    \stemDown fis8 \stemDown gis8 \stemDown e2 ~ | % 76
    \stemDown e4 ) r4 r4 \pageBreak | % 77
    R2.*5 \pageBreak | % 82
    R2.*2 | % 84
    r4 \stemDown cis'8 ( _\f _\< \stemDown e8 \stemDown e4 ~ | % 85
    \stemDown e2 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 ( _\! \stemDown e8 \stemDown cis8 }
    | % 86
    \stemDown b8 \stemDown gis8 _\> \stemDown b2 ~ \pageBreak | % 87
    \stemDown b2. ) | % 88
    r4 _\! \stemDown cis8 ( _\< \stemDown e8 \stemDown e4 ~ | % 89
    \stemDown e2 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 ( _\! \stemDown e8 \stemDown cis8 }
    | \barNumberCheck #90
    \stemDown b8 \stemDown gis8 _\> \stemDown b2 ~ | % 91
    \stemDown b2 ) r4 \pageBreak | % 92
    \stemDown b8 _\! ^ "a 2" _\p \stemDown b8 \stemDown b8 \stemDown b8
    \stemDown b8 \stemDown b8 | % 93
    \stemDown b8 \stemDown b8 \stemDown b8 \stemDown b8 \stemDown b8
    \stemDown b8 | % 94
    \stemDown b8 _\markup{ \italic {cresc.} } \stemDown b8 \stemDown b8
    \stemDown b8 \stemDown b8 \stemDown b8 | % 95
    \stemDown b8 _\< \stemDown b8 \stemDown b8 \stemDown b8 \stemDown b8
    \stemDown b8 | % 96
    \stemDown b8 _\! _\f \stemDown b8 \stemDown b8 \stemDown b8
    \stemDown b8 \stemDown b8 | % 97
    \stemDown b8 \stemDown b8 \stemDown b8 \stemDown b8 \stemDown b8
    _\markup{ \italic {dim.} } _\> \stemDown b8 | % 98
    \stemDown b8 \stemDown b8 \stemDown b8 \stemDown b8 \stemDown b8
    \stemDown b8 \pageBreak | % 99
    \mark \markup { 2 } R2.*8 \pageBreak ^\markup{ \large {in tempo
            [Tempo I.]} } | % 107
    R2.*6 \pageBreak | % 113
    R2.*4 | % 117
    r4 _\! \stemDown dis2 ~ ^ "a 2" _\f | % 118
    \stemDown dis2 \stemDown dis4 \pageBreak | % 119
    \stemDown dis4 ^ "a 2" \stemDown dis4 \stemDown fis4 |
    \barNumberCheck #120
    \stemDown fis2. ~ _\markup{ \italic {cresc.} } | % 121
    \stemDown fis2. | % 122
    \stemDown dis2. \bar "||"
    \key g \major \mark \markup { 3 } \stemDown e2 ^ "a 2" _\ff
    \stemDown e4 ~ | % 124
    \stemDown e4 \stemDown e2 | % 125
    \stemDown e2 \stemDown e4 ~ \pageBreak | % 126
    \stemDown e4 ^ "a 2" \stemDown e2 | % 127
    \stemDown e2 \stemDown e4 ~ | % 128
    \stemDown e4 \stemDown e2 | % 129
    \stemDown e2 \stemDown e4 | \barNumberCheck #130
    \stemDown e4 r4 \stemDown e4 | % 131
    \stemDown e4 r4 \stemDown e4 | % 132
    \stemDown e4 r4 \stemDown e4 \pageBreak | % 133
    \stemDown e4 r4 \stemDown e4 | % 134
    \stemDown e4 r4 r4 | % 135
    \stemDown e4 r4 r4 | % 136
    \stemDown e4 r4 r4 | % 137
    \stemDown e4 r4 r4 | % 138
    \stemDown e4 r4 r4 | % 139
    R2. | \barNumberCheck #140
    \stemDown e4 r4 r4 | % 141
    R2. ^ "al Coda <font size=" 20"/><sym>coda</sym>" \bar "||"
    \pageBreak | % 142
    \stemDown g,2. ~ ^\fp ^\> | % 143
    \stemDown g4 r4 ^\! r4 | % 144
    R2.*6 \pageBreak | \barNumberCheck #150
    R2.*4 | % 154
    \mark \markup { 4 } R2.*3 | % 157
    r4 r4 \stemUp e'4 ( ^\p \pageBreak | % 158
    \stemDown dis4 \stemDown g,4 ) r4 | % 159
    R2.*7 \pageBreak | % 166
    R2.*3 | % 169
    r4 r4 \stemDown as'4 ( ^\p | \barNumberCheck #170
    \stemDown g4 \stemDown b,4 ) r4 | % 171
    R2.*3 \pageBreak | % 174
    R2. | % 175
    r4 r4 \stemDown c,4 ^ "a 2" _\p \repeat volta 2 {
        | % 176
        \stemDown c4. \stemDown c8 \stemDown e8 -. r8 | % 177
        \stemDown e4. \stemDown e8 \stemDown g8 -. r8 | % 178
        \stemDown g2. ~ | % 179
        \stemDown g2 \stemDown g4 \pageBreak | \barNumberCheck #180
        \stemDown g4. \stemDown g8 \stemDown c4 | % 181
        \stemDown b4. \stemDown b8 \stemDown a4 | % 182
        \stemDown g2. ~ | % 183
        \stemDown g2 \stemDown c,4 | % 184
        \stemDown c4. \stemDown c8 \stemDown e8 r8 | % 185
        \stemDown e4. \stemDown e8 \stemDown g8 r8 \pageBreak | % 186
        \stemDown g2. ~ ^ "a 2" | % 187
        \stemDown g2 \stemDown g4 | % 188
        \stemDown g4. _\< \stemDown g8 \stemDown e'4 | % 189
        \stemDown d2 _\! _\f \stemDown c4 _\> | \barNumberCheck #190
        \stemDown c2. ~ }
    \alternative { {
            | % 191
            \stemDown c4 ~ _\! _\p r4 \stemDown c,4 }
        {
            | % 192
            \stemDown c'4 r2 }
        } \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
        \mark \markup { 5 } R2.*7 \pageBreak | \barNumberCheck #200
        R2. | % 201
        \stemDown b8 ( _\p \stemDown g'8 \stemDown b,8 ) r8 \stemDown a8
        r8 | % 202
        \stemDown g2. \startTrillSpan \stopTrillSpan ^ "[♮]" _\fp | % 203
        \stemDown fis8 ( \stemDown d'8 \stemDown fis,8 ) r8 \stemDown e8
        r8 | % 204
        \stemDown d2. \startTrillSpan \stopTrillSpan _\fp | % 205
        \stemDown e8 ( \stemDown c'8 \stemDown e,8 ) r8 \stemDown d8 r8
        \pageBreak | % 206
        \stemDown c2. \startTrillSpan \stopTrillSpan | % 207
        \stemDown b8 ( \stemDown g'8 \stemDown b,8 ) r8 \stemUp a8 r8 | % 208
        \stemUp g2 ~ \startTrillSpan \stopTrillSpan \stemUp g8 r8 | % 209
        R2.*4 \pageBreak | % 213
        R2.*4 | % 217
        \stemDown e'2 ~ \startTrillSpan \stopTrillSpan _\p \stemDown e8
        r8 | % 218
        R2. | % 219
        \stemDown e2 ~ \startTrillSpan \stopTrillSpan \stemDown e8 r8 |
        \barNumberCheck #220
        R2. \pageBreak | % 221
        \stemDown f2 ~ \startTrillSpan \stopTrillSpan \stemDown f8 r8 | % 222
        R2. | % 223
        \stemDown f2 ~ \startTrillSpan \stopTrillSpan \stemDown f8 r8 | % 224
        \stemDown c4. ^ "a 2" _\p \stemDown c8 \stemDown e8 r8 | % 225
        \stemDown e4. \stemDown e8 \stemDown g8 r8 | % 226
        \stemDown g2. ~ \pageBreak | % 227
        \stemDown g2 ^ "a 2" \stemDown g4 | % 228
        \stemDown g4. \stemDown g8 \stemDown c8 r8 | % 229
        \stemDown b4. \stemDown b8 \stemDown a8 r8 | \barNumberCheck
        #230
        \stemDown g2. ~ | % 231
        \stemDown g2 \stemDown c,4 \pageBreak | % 232
        \stemDown c4. ^ "a 2" ^\markup{ \italic {cresc.} }
        \startTrillSpan \stemDown c8 \stemDown e8 r8 | % 233
        \stemDown e4. \stemDown e8 \stemDown g8 r8 | % 234
        \stemDown g2. ~ | % 235
        \stemDown g2 \stemDown g4 | % 236
        \stemDown g4. \stemDown g8 \stemDown e'4 \pageBreak | % 237
        \stemDown d2 ^ "a 2" \stemDown c4 | % 238
        \stemDown c2. ~ \stopTrillSpan _\fz | % 239
        \stemDown c4 r4 r4 }
    | \barNumberCheck #240
    \mark \markup { 6 } R2.*3 \pageBreak | % 243
    R2.*6 ^ "<i><font size=" 14"/>D. C. Scherzo e poi la Coda</i>" \bar
    "||"
    \pageBreak | % 249
    \mark \markup { \musicglyph "scripts.coda" } R2.*8 ^ "CODA" | % 257
    r4 \stemDown g8 ^\p \stemDown g8 \stemDown g4 _. \pageBreak | % 258
    \stemDown c,4 _. \stemDown c4 _. r4 | % 259
    r4 \stemDown g'8 \stemDown g8 \stemDown g4 _. | \barNumberCheck #260
    \stemDown c,4 _. \stemDown c4 _. r4 | % 261
    R2.*4 \pageBreak | % 265
    r4 \stemDown gis'8 _\p \stemDown gis8 \stemDown gis4 _. | % 266
    \stemDown cis,4 _. \stemDown cis4 _. r4 | % 267
    r4 \stemDown gis'8 \stemDown gis8 \stemDown gis4 _. | % 268
    \stemDown cis,4 _. \stemDown cis4 _. r4 | % 269
    R2.*2 | % 271
    \mark \markup { 7 } R2. \pageBreak | % 272
    R2. ^\markup{ \italic {cresc.} } | % 273
    \stemDown fis2 ^ "a 2" _\f _\< \stemDown a4 -. | % 274
    \stemDown cis4 -. \stemDown fis2 -> | % 275
    \stemDown a2 -> _\! _\ff \stemDown fis4 -. | % 276
    \stemDown cis4 -. \stemDown a2 -> \pageBreak | % 277
    \stemDown dis8 ^ "a 2" \stemDown dis8 \stemDown dis4 -. \stemDown a4
    -. | % 278
    \stemDown a4 -. \stemDown dis8 \stemDown dis8 \stemDown dis4 | % 279
    \stemDown a4 -. \stemDown a4 -. \stemDown dis8 \stemDown dis8 |
    \barNumberCheck #280
    \stemDown dis4 -. \stemDown a4 -. \stemDown a4 -. | % 281
    \stemDown gis'2. ~ _\fff | % 282
    \stemDown gis2. ~ \pageBreak | % 283
    \stemDown gis2. ~ _\markup{ \italic {dim.} } | % 284
    \stemDown gis2. ~ | % 285
    \stemDown gis4 r4 r4 | % 286
    R2.*2 \pageBreak | % 288
    R2.*6 \pageBreak | % 294
    R2.*5 | % 299
    R2. ^\markup{ \bold {G. P.} } | \barNumberCheck #300
    \stemDown e4 _\ff r4 r4 \bar "|."
    }

PartPTwoVoiceOne =  \relative e''' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key g \major | % 1
        \stemDown e8 ^ "a 2" _\f \stemDown e8 \stemDown e2 ~ | % 2
        \stemDown e2. | % 3
        \stemDown b8 \stemDown b8 \stemDown b2 ~ | % 4
        \stemDown b2. \bar "||"
        R2.*3 \pageBreak | % 8
        R2.*5 | % 13
        r4 \stemDown b8 _. _\p \stemDown b8 _. \stemDown b4 _. | % 14
        \stemDown e,4 _. \stemDown e4 _. r4 \pageBreak | % 15
        r4 \stemDown fis4 -. \stemDown a4 -. | % 16
        \stemDown g8 ( \stemDown fis8 \stemDown e4 ) r4 | % 17
        r4 \stemDown b'8 -. \stemDown b8 -. \stemDown b4 -. | % 18
        \stemDown e,4 _. \stemDown e4 _. r4 | % 19
        r4 \stemDown fis4 -. \stemDown a4 -. | \barNumberCheck #20
        \stemDown g8 ( \stemDown fis8 \stemDown e4 ) r4 \pageBreak | % 21
        R2.*5 \pageBreak | % 26
        R2.*5 \pageBreak | % 31
        R2.*5 \pageBreak | % 36
        R2.*6 \pageBreak | % 42
        r4 \stemDown b'8 ^ "a 2" _\ff \stemDown b8 \stemDown b4 | % 43
        \stemDown e,4 \stemDown e4 r4 | % 44
        r4 \stemDown g4 -. \stemDown b4 -. | % 45
        \stemDown g8 ( \stemDown fis8 \stemDown e4 ) r4 | % 46
        r4 \stemDown b'8 \stemDown b8 \stemDown b4 \pageBreak | % 47
        \stemDown e,4 ^ "a 2" \stemDown e4 r4 | % 48
        r4 \stemDown g4 -. \stemDown b4 -. | % 49
        \stemDown g8 ( \stemDown fis8 \stemDown e4 ) \stemDown e'4 |
        \barNumberCheck #50
        \stemDown d2 -> \stemDown cis4 ~ -> | % 51
        \stemDown cis4 \stemDown c2 -> | % 52
        \stemDown b2 -> \stemDown e,4 ~ \pageBreak | % 53
        \stemDown e4 \stemDown e'2 -> | % 54
        \stemDown d2 -> \stemDown cis4 ~ -> | % 55
        \stemDown cis4 \stemDown c2 -> | % 56
        \stemDown b8 ( \stemDown e8 ) \stemDown e4 -. \stemDown e8 (
        \stemDown c8 ) | % 57
        \stemDown b8 ( \stemDown e8 ) \stemDown e4 -. \stemDown e8 (
        \stemDown c8 ) | % 58
        \stemDown b8 ( \stemDown e8 ) \stemDown e4 -. \stemDown e8 (
        \stemDown c8 ) | % 59
        \stemDown e4 -. r4 r4 }
    \pageBreak | \barNumberCheck #60
    R2.*7 \pageBreak | % 67
    R2. \bar "||"
    \key e \major \stemDown gis,8 ( ^\p \stemDown b8 ) \stemDown b2 ~ | % 69
    \stemDown b2 \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 \stemDown b8 \stemDown fis8 }
    | \barNumberCheck #70
    \stemDown e2 \stemDown fis4 | % 71
    \stemDown gis8 ( \stemDown b8 ) \stemDown b2 ~ \pageBreak | % 72
    \stemUp b8 \stemUp e8 ( \stemUp dis8 \stemUp cis8 \stemDown b4 ~ | % 73
    \stemDown b8 ) \stemDown cis8 ( \stemDown b8 \stemDown gis8
    \stemDown b4 ~ | % 74
    \stemDown b8 \stemDown gis8 \stemDown fis8 \stemDown gis8 \stemDown
    b8 \stemDown gis8 | % 75
    \stemDown fis8 \stemDown gis8 \stemDown e2 ~ | % 76
    \stemDown e4 ) r4 r4 \pageBreak | % 77
    R2.*5 \pageBreak | % 82
    R2.*2 | % 84
    r4 \stemDown a8 ( _\f _\< \stemDown cis8 \stemDown cis4 ~ | % 85
    \stemDown cis2 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown dis8 ( _\! \stemDown cis8 \stemDown a8 }
    | % 86
    \stemDown gis8 \stemDown e8 _\> \stemDown gis2 ~ \pageBreak | % 87
    \stemDown gis2. ) | % 88
    r4 _\! \stemDown a8 ( _\< \stemDown cis8 \stemDown cis4 ~ | % 89
    \stemDown cis2 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown dis8 ( _\! \stemDown cis8 \stemDown a8 }
    | \barNumberCheck #90
    \stemDown gis8 \stemDown e8 _\> \stemDown gis2 ~ | % 91
    \stemDown gis2 ) r4 \pageBreak | % 92
    \stemDown b8 _\! ^ "a 2" _\p \stemDown b8 \stemDown b8 \stemDown b8
    \stemDown b8 \stemDown b8 | % 93
    \stemDown b8 \stemDown b8 \stemDown b8 \stemDown b8 \stemDown b8
    \stemDown b8 | % 94
    \stemDown b8 _\markup{ \italic {cresc.} } \stemDown b8 \stemDown b8
    \stemDown b8 \stemDown b8 \stemDown b8 | % 95
    \stemDown b8 _\< \stemDown b8 \stemDown b8 \stemDown b8 \stemDown b8
    \stemDown b8 | % 96
    \stemDown b8 _\! _\f \stemDown b8 \stemDown b8 \stemDown b8
    \stemDown b8 \stemDown b8 | % 97
    \stemDown b8 \stemDown b8 \stemDown b8 \stemDown b8 \stemDown b8
    _\markup{ \italic {dim.} } _\> \stemDown b8 | % 98
    \stemDown b8 \stemDown b8 \stemDown b8 \stemDown b8 \stemDown b8
    \stemDown b8 \pageBreak | % 99
    R2.*8 \pageBreak | % 107
    R2.*6 \pageBreak | % 113
    R2.*4 | % 117
    r4 _\! \stemDown dis2 ~ ^ "a 2" _\f | % 118
    \stemDown dis2 \stemDown dis4 \pageBreak | % 119
    \stemDown dis4 ^ "a 2" \stemDown dis4 \stemDown fis4 |
    \barNumberCheck #120
    \stemDown fis2. ~ _\markup{ \italic {cresc.} } | % 121
    \stemDown fis2. | % 122
    \stemDown b,2. \bar "||"
    \key g \major \stemDown e2 ^ "a 2" _\ff \stemDown e4 ~ | % 124
    \stemDown e4 \stemDown e2 | % 125
    \stemDown e2 \stemDown e4 ~ \pageBreak | % 126
    \stemDown e4 ^ "a 2" \stemDown e2 | % 127
    \stemDown e2 \stemDown e4 ~ | % 128
    \stemDown e4 \stemDown e2 | % 129
    \stemDown e2 \stemDown e4 | \barNumberCheck #130
    \stemDown e4 r4 \stemDown c4 | % 131
    \stemDown b4 r4 \stemDown c4 | % 132
    \stemDown b4 r4 \stemDown c4 \pageBreak | % 133
    \stemDown b4 r4 \stemDown c4 | % 134
    \stemDown b4 r4 r4 | % 135
    \stemDown c4 r4 r4 | % 136
    \stemDown b4 r4 r4 | % 137
    \stemDown c4 r4 r4 | % 138
    \stemDown b4 r4 r4 | % 139
    R2. | \barNumberCheck #140
    \stemDown b4 r4 r4 | % 141
    R2. \bar "||"
    \pageBreak | % 142
    \stemDown g2. ~ ^\fp ^\> | % 143
    \stemDown g4 r4 ^\! r4 | % 144
    R2.*6 \pageBreak | \barNumberCheck #150
    R2.*7 | % 157
    r4 r4 \stemUp e'4 ( ^\p \pageBreak | % 158
    \stemDown dis4 \stemDown g,4 ) r4 | % 159
    R2.*7 \pageBreak | % 166
    R2.*3 | % 169
    r4 r4 \stemDown as'4 ( ^\p | \barNumberCheck #170
    \stemDown g4 \stemDown b,4 ) r4 | % 171
    R2.*3 \pageBreak | % 174
    R2. | % 175
    r4 r4 \stemDown c,4 ^ "a 2" _\p \repeat volta 2 {
        | % 176
        \stemDown c4. \stemDown c8 \stemDown e8 -. r8 | % 177
        \stemDown e4. \stemDown e8 \stemDown g8 -. r8 | % 178
        \stemDown g2. ~ | % 179
        \stemDown g2 \stemDown g4 \pageBreak | \barNumberCheck #180
        \stemDown g4. \stemDown g8 \stemDown c4 | % 181
        \stemDown b4. \stemDown b8 \stemDown a4 | % 182
        \stemDown g2. ~ | % 183
        \stemDown g2 \stemDown c,4 | % 184
        \stemDown c4. \stemDown c8 \stemDown e8 r8 | % 185
        \stemDown e4. \stemDown e8 \stemDown g8 r8 \pageBreak | % 186
        \stemDown g2. ~ ^ "a 2" | % 187
        \stemDown g2 \stemDown g4 | % 188
        \stemDown g4. _\< \stemDown g8 \stemDown e'4 | % 189
        \stemDown d2 _\! _\f \stemDown c4 _\> | \barNumberCheck #190
        \stemDown c2. ~ | % 191
        \stemDown c4 ~ _\! _\p r4 \stemDown c,4 }
    | % 192
    \stemDown c'4 r2 \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
        R2.*7 \pageBreak | \barNumberCheck #200
        R2. | % 201
        \stemDown g8 ( _\p \stemDown b8 \stemDown g8 ) r8 \stemDown f8 r8
        | % 202
        \stemDown e2. \startTrillSpan \stopTrillSpan ^ "[♮]" _\fp | % 203
        \stemDown d8 ( \stemDown fis8 \stemDown d8 ) r8 \stemDown c8 r8
        | % 204
        \stemDown b2. \startTrillSpan \stopTrillSpan _\fp | % 205
        \stemDown c8 ( \stemDown e8 \stemDown c8 ) r8 \stemDown b8 r8
        \pageBreak | % 206
        \stemUp a2. \startTrillSpan \stopTrillSpan | % 207
        \stemUp g8 ( \stemUp b8 \stemUp g8 ) r8 \stemUp fis8 r8 | % 208
        \stemUp e2 ~ \startTrillSpan \stopTrillSpan \stemUp e8 r8 | % 209
        R2.*4 \pageBreak | % 213
        R2.*4 | % 217
        \stemUp gis2 ~ \startTrillSpan \stopTrillSpan _\p \stemUp gis8 r8
        | % 218
        R2. | % 219
        \stemUp gis2 ~ \startTrillSpan \stopTrillSpan \stemUp gis8 r8 |
        \barNumberCheck #220
        R2. \pageBreak | % 221
        \stemUp a2 ~ \startTrillSpan \stopTrillSpan \stemUp a8 r8 | % 222
        R2. | % 223
        \stemUp a2 ~ \startTrillSpan \stopTrillSpan \stemUp a8 r8 | % 224
        \stemDown c4. ^ "a 2" _\p \stemDown c8 \stemDown e8 r8 | % 225
        \stemDown e4. \stemDown e8 \stemDown g8 r8 | % 226
        \stemDown g2. ~ \pageBreak | % 227
        \stemDown g2 ^ "a 2" \stemDown g4 | % 228
        \stemDown g4. \stemDown g8 \stemDown c8 r8 | % 229
        \stemDown b4. \stemDown b8 \stemDown a8 r8 | \barNumberCheck
        #230
        \stemDown g2. ~ | % 231
        \stemDown g2 \stemDown c,4 \pageBreak | % 232
        \stemDown c4. ^ "a 2" ^\markup{ \italic {cresc.} }
        \startTrillSpan \stemDown c8 \stemDown e8 r8 | % 233
        \stemDown e4. \stemDown e8 \stemDown g8 r8 | % 234
        \stemDown g2. ~ | % 235
        \stemDown g2 \stemDown g4 | % 236
        \stemDown g4. \stemDown g8 \stemDown e'4 \pageBreak | % 237
        \stemDown d2 ^ "a 2" \stemDown c4 | % 238
        \stemDown c2. ~ \stopTrillSpan _\fz | % 239
        \stemDown c4 r4 r4 }
    | \barNumberCheck #240
    R2.*3 \pageBreak | % 243
    R2.*6 \bar "||"
    \pageBreak | % 249
    R2.*8 ^ "CODA" | % 257
    r4 \stemDown g8 ^\p \stemDown g8 \stemDown g4 _. \pageBreak | % 258
    \stemDown c,4 _. \stemDown c4 _. r4 | % 259
    r4 \stemDown g'8 \stemDown g8 \stemDown g4 _. | \barNumberCheck #260
    \stemDown c,4 _. \stemDown c4 _. r4 | % 261
    R2.*4 \pageBreak | % 265
    r4 \stemDown gis'8 _\p \stemDown gis8 \stemDown gis4 _. | % 266
    \stemDown cis,4 _. \stemDown cis4 _. r4 | % 267
    r4 \stemDown gis'8 \stemDown gis8 \stemDown gis4 _. | % 268
    \stemDown cis,4 _. \stemDown cis4 _. r4 | % 269
    R2.*3 \pageBreak | % 272
    R2. ^\markup{ \italic {cresc.} } | % 273
    \stemDown fis2 ^ "a 2" _\f _\< \stemDown a4 -. | % 274
    \stemDown cis4 -. \stemDown fis2 -> | % 275
    \stemDown a2 -> _\! _\ff \stemDown fis4 -. | % 276
    \stemDown cis4 -. \stemDown a2 -> \pageBreak | % 277
    \stemDown dis8 ^ "a 2" \stemDown dis8 \stemDown dis4 -. \stemDown a4
    -. | % 278
    \stemDown a4 -. \stemDown dis8 \stemDown dis8 \stemDown dis4 | % 279
    \stemDown a4 -. \stemDown a4 -. \stemDown dis8 \stemDown dis8 |
    \barNumberCheck #280
    \stemDown dis4 -. \stemDown a4 -. \stemDown a4 -. | % 281
    \stemDown e'2. ~ _\fff | % 282
    \stemDown e2. ~ \pageBreak | % 283
    \stemDown e2. ~ _\markup{ \italic {dim.} } | % 284
    \stemDown e2. ~ | % 285
    \stemDown e4 r4 r4 | % 286
    R2.*2 \pageBreak | % 288
    R2.*6 \pageBreak | % 294
    R2.*5 | % 299
    R2. ^\markup{ \bold {G. P.} } | \barNumberCheck #300
    \stemDown e4 _\ff r4 r4 \bar "|."
    }

PartPThreeVoiceOne =  \relative e'' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key g \major | % 1
        \stemDown e8 ^ "a 2" _\f \stemDown e8 \stemDown e2 ~ | % 2
        \stemDown e2. | % 3
        \stemDown b8 \stemDown b8 \stemDown b2 ~ | % 4
        \stemDown b2. \bar "||"
        R2.*3 \pageBreak | % 8
        R2.*5 | % 13
        r4 \stemUp b'8 ^. ^\p \stemUp b8 ^. \stemUp b4 ^. | % 14
        \stemUp e,4 ^. \stemUp e4 ^. r4 \pageBreak | % 15
        r4 \stemUp fis4 ^. \stemUp a4 ^. | % 16
        \stemUp g8 ( \stemUp fis8 \stemUp e4 ) r4 | % 17
        r4 \stemUp b'8 ^. \stemUp b8 ^. \stemUp b4 ^. | % 18
        \stemUp e,4 ^. \stemUp e4 ^. r4 | % 19
        r4 \stemUp fis4 ^. \stemUp a4 ^. | \barNumberCheck #20
        \stemUp g8 ( \stemUp fis8 \stemUp e4 ) r4 \pageBreak | % 21
        R2.*5 \pageBreak | % 26
        R2.*5 \pageBreak | % 31
        R2.*5 \pageBreak | % 36
        R2.*6 \pageBreak | % 42
        r4 \stemDown b'8 _\ff \stemDown b8 \stemDown b4 | % 43
        \stemDown e,4 \stemDown e4 r4 | % 44
        r4 \stemDown g4 -. \stemDown b4 -. | % 45
        \stemDown g8 ( \stemDown fis8 \stemDown e4 ) r4 | % 46
        r4 \stemDown b'8 \stemDown b8 \stemDown b4 \pageBreak | % 47
        \stemDown e,4 \stemDown e4 r4 | % 48
        r4 \stemDown g4 -. \stemDown b4 -. | % 49
        \stemDown g8 ( \stemDown fis8 \stemDown e4 ) \stemDown e'4 |
        \barNumberCheck #50
        \stemDown d2 -> \stemDown cis4 ~ -> | % 51
        \stemDown cis4 \stemDown c2 -> | % 52
        \stemDown b2 -> \stemDown e,4 ~ \pageBreak | % 53
        \stemDown e4 \stemDown e'2 -> | % 54
        \stemDown d2 -> \stemDown cis4 ~ -> | % 55
        \stemDown cis4 \stemDown c2 -> | % 56
        \stemDown b8 \stemDown e,8 \stemDown e4 -. \stemDown e8 ( ^
        "a 2" \stemDown c8 ) | % 57
        \stemDown b8 ( \stemDown e8 ) \stemDown e4 -. \stemDown e8 (
        \stemDown c8 ) | % 58
        \stemDown b8 ( \stemDown e8 ) \stemDown e4 -. \stemDown e8 (
        \stemDown c8 ) | % 59
        \stemDown e4 -. r4 r4 }
    \pageBreak | \barNumberCheck #60
    R2.*7 \pageBreak | % 67
    R2. \bar "||"
    \key e \major \stemUp gis,8 ( ^\p \stemUp b8 ) \stemDown b2 ~ | % 69
    \stemDown b2 \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis8 \stemUp b8 \stemUp fis8 }
    | \barNumberCheck #70
    \stemUp e2 \stemUp fis4 | % 71
    \stemUp gis8 ( \stemUp b8 ) \stemDown b2 ~ \pageBreak | % 72
    \stemUp b8 \stemUp e8 ( \stemUp dis8 \stemUp cis8 \stemDown b4 ~ | % 73
    \stemUp b8 ) \stemUp cis8 ( \stemUp b8 \stemUp gis8 \stemDown b4 ~ | % 74
    \stemUp b8 ) \stemUp gis8 ( \stemUp fis8 \stemUp gis8 \stemUp b8
    \stemUp gis8 | % 75
    \stemUp fis8 \stemUp gis8 \stemUp e2 ~ | % 76
    \stemUp e4 ) r4 r4 \pageBreak | % 77
    R2.*5 \pageBreak | % 82
    R2.*2 | % 84
    r4 \stemDown cis'8 ( _\f _\< \stemDown e8 \stemDown e4 ~ | % 85
    \stemDown e2 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 ( _\! \stemDown e8 \stemDown cis8 }
    | % 86
    \stemUp b8 \stemUp gis8 _\> \stemDown b2 ~ \pageBreak | % 87
    \stemDown b2. ) | % 88
    r4 _\! \stemDown cis8 ( _\< \stemDown e8 \stemDown e4 ~ | % 89
    \stemDown e2 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 ( _\! \stemDown e8 \stemDown cis8 }
    | \barNumberCheck #90
    \stemUp b8 \stemUp gis8 _\> \stemDown b2 ~ | % 91
    \stemDown b2 ) r4 \pageBreak | % 92
    \stemDown gis'8 _\! _\p \stemDown gis8 \stemDown gis8 \stemDown gis8
    \stemDown a8 \stemDown a8 | % 93
    \stemDown gis8 \stemDown gis8 \stemDown gis8 \stemDown gis8
    \stemDown a8 \stemDown a8 | % 94
    \stemDown gis8 _\markup{ \italic {cresc.} } \stemDown gis8 \stemDown
    gis8 \stemDown gis8 \stemDown a8 \stemDown a8 | % 95
    \stemDown gis8 _\< \stemDown gis8 \stemDown gis8 \stemDown gis8
    \stemDown a8 \stemDown a8 | % 96
    \stemDown gis8 _\! _\f \stemDown gis8 \stemDown gis8 \stemDown gis8
    \stemDown gis8 \stemDown gis8 | % 97
    \stemDown gis8 \stemDown gis8 \stemDown gis8 \stemDown gis8
    \stemDown gis8 _\markup{ \italic {dim.} } _\> \stemDown gis8 | % 98
    \stemDown a8 \stemDown a8 \stemDown gis8 \stemDown gis8 \stemDown
    gis8 \stemDown gis8 \pageBreak | % 99
    R2.*8 \pageBreak | % 107
    R2.*6 \pageBreak | % 113
    R2.*4 | % 117
    r4 _\! \stemDown a2 ~ _\f | % 118
    \stemDown a2 \stemDown gis4 \pageBreak | % 119
    \stemDown gis4 \stemDown fis4 \stemDown a4 | \barNumberCheck #120
    \stemDown a2. ~ _\markup{ \italic {cresc.} } | % 121
    \stemDown a2. | % 122
    \stemDown fis2 \stemDown a4 \bar "||"
    \key g \major \stemDown g2 _\ff \stemDown g4 ~ | % 124
    \stemDown g4 \stemDown g2 | % 125
    \stemDown fis2 \stemDown fis4 ~ \pageBreak | % 126
    \stemDown fis4 \stemDown g2 | % 127
    \stemDown g2 \stemDown g4 ~ | % 128
    \stemDown g4 \stemDown g2 | % 129
    \stemDown fis2 \stemDown fis4 | \barNumberCheck #130
    \stemDown b4 r4 \stemDown c4 | % 131
    \stemDown b4 r4 \stemDown c4 | % 132
    \stemDown b4 r4 \stemDown c4 \pageBreak | % 133
    \stemDown b4 r4 \stemDown c4 | % 134
    \stemDown b4 r4 r4 | % 135
    \stemDown g4 r4 r4 | % 136
    \stemDown b4 r4 r4 | % 137
    \stemDown g4 r4 r4 | % 138
    \stemDown g4 r4 r4 | % 139
    R2. | \barNumberCheck #140
    \stemDown g4 r4 r4 | % 141
    R2. \bar "||"
    \pageBreak | % 142
    \stemDown e2. ( ~ _\fp _\> | % 143
    \stemDown e4 ) r2 _\! | % 144
    R2.*6 \pageBreak | \barNumberCheck #150
    R2.*8 \pageBreak | % 158
    R2.*8 \pageBreak | % 166
    R2.*4 | \barNumberCheck #170
    r4 r4 \stemDown as4 ( ^\p | % 171
    \stemDown g4 \stemDown b,4 ) r4 | % 172
    R2.*2 \pageBreak | % 174
    R2. | % 175
    r4 r4 \stemDown c4 _\p \repeat volta 2 {
        | % 176
        \stemDown c4. \stemDown c8 \stemDown e8 ^. r8 | % 177
        \stemDown e4. \stemDown e8 \stemDown g8 -. r8 | % 178
        \stemDown e2. ~ | % 179
        \stemDown e2 \stemDown e4 \pageBreak | \barNumberCheck #180
        \stemDown e4. \stemDown e8 \stemDown g4 | % 181
        \stemDown g4. \stemDown g8 \stemDown f4 | % 182
        \stemDown e2. ~ | % 183
        \stemDown e2 \stemDown c4 | % 184
        \stemDown c4. \stemDown c8 \stemDown e8 r8 | % 185
        \stemDown e4. \stemDown e8 \stemDown g8 r8 \pageBreak | % 186
        \stemDown g2. ~ | % 187
        \stemDown g2 \stemDown g4 | % 188
        \stemDown g4. _\< \stemDown g8 \stemDown g4 | % 189
        \stemDown f2 _\! _\f \stemDown e4 _\> | \barNumberCheck #190
        \stemDown e2. ~ | % 191
        \stemDown e4 ~ _\! _\p r4 \stemDown c4 }
    | % 192
    \stemDown e4 r4 r4 \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
        R2.*7 \pageBreak | \barNumberCheck #200
        R2. | % 201
        \stemDown g8 ( ^\p \stemDown b8 \stemDown g8 ) r8 \stemDown f8 r8
        | % 202
        \stemUp e2. \startTrillSpan ^ "[♮]" _\fp | % 203
        \stemDown d8 ( \stemDown fis8 \stemDown d8 ) r8 \stemDown c8 r8
        | % 204
        \stemDown b2. \startTrillSpan \stopTrillSpan _\fp | % 205
        \stemDown e8 ( _\p \stemDown c'8 \stemDown e,8 ) r8 \stemDown d8
        r8 \pageBreak | % 206
        \stemDown c2. \startTrillSpan \stopTrillSpan | % 207
        \stemDown b8 ( \stemDown g'8 \stemDown b,8 ) r8 \stemUp a8 r8 | % 208
        \stemUp g2 ~ \startTrillSpan \stopTrillSpan \stemUp g8 r8 | % 209
        R2.*4 \pageBreak | % 213
        R2.*8 \pageBreak | % 221
        R2.*3 | % 224
        \stemDown c4. _\p \stemDown c8 \stemDown e8 r8 | % 225
        \stemDown e4. \stemDown e8 \stemDown g8 r8 | % 226
        \stemDown g2. ~ \pageBreak | % 227
        \stemDown g2 \stemDown g4 | % 228
        \stemDown g4. \stemDown g8 \stemDown c8 r8 | % 229
        \stemDown b4. \stemDown b8 \stemDown a8 r8 | \barNumberCheck
        #230
        \stemDown g2. ~ | % 231
        \stemDown g2 \stemDown c,4 \pageBreak | % 232
        \stemDown c4. \stemDown c8 \stemDown e8 r8 | % 233
        \stemDown e4. \stemDown e8 \stemDown g8 r8 | % 234
        \stemDown g2. ~ | % 235
        \stemDown g2 \stemDown g4 | % 236
        \stemDown g4. \stemDown g8 \stemDown g4 \pageBreak | % 237
        \stemDown f2 \stemDown e4 | % 238
        \stemDown e2. ~ _\fz | % 239
        \stemDown e4 r4 r4 }
    | \barNumberCheck #240
    R2.*3 \pageBreak | % 243
    R2.*6 \bar "||"
    \pageBreak | % 249
    R2.*8 | % 257
    r4 \stemUp g8 ^\p \stemUp g8 \stemUp g4 ^. \pageBreak | % 258
    \stemUp c,4 ^. \stemUp c4 ^. r4 | % 259
    r4 \stemUp g'8 \stemUp g8 \stemUp g4 ^. | \barNumberCheck #260
    \stemUp c,4 ^. \stemUp c4 ^. r4 | % 261
    R2.*4 \pageBreak | % 265
    r4 \stemUp gis'8 ^\p \stemUp gis8 \stemUp gis4 ^. | % 266
    \stemUp cis,4 ^. \stemUp cis4 ^. r4 | % 267
    r4 \stemUp gis'8 \stemUp gis8 \stemUp gis4 ^. | % 268
    \stemUp cis,4 ^. \stemUp cis4 ^. r4 | % 269
    R2.*2 | % 271
    \stemUp fis,2 _\f ^ "a 2" \stemUp a4 -. \pageBreak | % 272
    \stemDown cis4 ^ "a 2" \stemDown fis2 -> | % 273
    \stemDown fis2 _\f _\< \stemDown a4 -. | % 274
    \stemDown cis4 -. \stemDown fis,2 -> | % 275
    \stemDown a2 -> _\! _\ff \stemDown fis4 -. | % 276
    \stemDown cis'4 -. \stemDown a2 -> \pageBreak | % 277
    \stemDown dis,8 ^ "a 2" \stemDown dis8 \stemDown dis4 -. \stemUp a4
    -. | % 278
    \stemUp a4 -. \stemDown dis8 \stemDown dis8 \stemDown dis4 | % 279
    \stemUp a4 -. \stemUp a4 -. \stemDown dis8 \stemDown dis8 |
    \barNumberCheck #280
    \stemDown dis4 -. \stemUp a4 -. \stemUp a4 -. | % 281
    \stemDown b'2. ~ _\fff | % 282
    \stemDown b2. ~ \pageBreak | % 283
    \stemDown b2. ~ _\markup{ \italic {dim.} } | % 284
    \stemDown b2. ~ | % 285
    \stemDown b4 r4 r4 | % 286
    R2.*2 \pageBreak | % 288
    R2.*6 \pageBreak | % 294
    R2.*6 | \barNumberCheck #300
    \stemDown b4 _\ff r4 r4 \bar "|."
    }

PartPThreeVoiceThree =  \relative c' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key g \major s1*3 \bar "||"
        s4*9 \pageBreak s4*21 \pageBreak s2*9 \pageBreak s4*15
        \pageBreak s4*15 \pageBreak s4*15 \pageBreak s2*9 \pageBreak
        s4*15 \pageBreak s2*9 \pageBreak s4*21 }
    \pageBreak s4*21 \pageBreak s2. \bar "||"
    \key e \major s1*3 \pageBreak s4*15 \pageBreak s4*15 \pageBreak
    s4*15 \pageBreak s4*15 \pageBreak s4*21 \pageBreak s1*6 \pageBreak
    s2*9 \pageBreak s2*9 \pageBreak s1*3 \bar "||"
    \key g \major s4*9 \pageBreak s4*21 \pageBreak s4*27 \bar "||"
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*6
    \pageBreak s1. \repeat volta 2 {
        s1*3 \pageBreak s2*9 \pageBreak s2*9 }
    s2. \bar "||"
    \pageBreak \repeat volta 2 {
        s4*21 \pageBreak s1. | % 202
        R2. s4*9 \pageBreak s4*21 \pageBreak s1*6 \pageBreak s2*9
        \pageBreak s4*15 \pageBreak s4*15 \pageBreak s4*9 }
    s4*9 \pageBreak s2*9 \bar "||"
    \pageBreak s4*27 \pageBreak s4*21 \pageBreak s4*21 \pageBreak s4*15
    \pageBreak s2*9 \pageBreak s4*15 \pageBreak s2*9 \pageBreak s4*21
    \bar "|."
    }

PartPFourVoiceOne =  \relative e'' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key g \major | % 1
        \stemDown e8 ^ "a 2" _\f \stemDown e8 \stemDown e2 ~ | % 2
        \stemDown e2. | % 3
        \stemDown b8 \stemDown b8 \stemDown b2 ~ | % 4
        \stemDown b2. \bar "||"
        R2.*3 \pageBreak | % 8
        R2.*5 | % 13
        r4 \stemUp b'8 ^. ^\p \stemUp b8 ^. \stemUp b4 ^. | % 14
        \stemUp e,4 ^. \stemUp e4 ^. r4 \pageBreak | % 15
        r4 \stemUp fis4 ^. \stemUp a4 ^. | % 16
        \stemUp g8 ( \stemUp fis8 \stemUp e4 ) r4 | % 17
        r4 \stemUp b'8 ^. \stemUp b8 ^. \stemUp b4 ^. | % 18
        \stemUp e,4 ^. \stemUp e4 ^. r4 | % 19
        r4 \stemUp fis4 ^. \stemUp a4 ^. | \barNumberCheck #20
        \stemUp g8 ( \stemUp fis8 \stemUp e4 ) r4 \pageBreak | % 21
        R2.*5 \pageBreak | % 26
        R2.*5 \pageBreak | % 31
        R2.*5 \pageBreak | % 36
        R2.*6 \pageBreak | % 42
        r4 \stemDown b8 _\ff \stemDown b8 \stemDown b4 | % 43
        \stemUp e,4 \stemUp e4 r4 | % 44
        r4 \stemUp g4 -. \stemDown b4 -. | % 45
        \stemUp g8 ( \stemUp fis8 \stemUp e4 ) r4 | % 46
        r4 \stemDown b'8 \stemDown b8 \stemDown b4 \pageBreak | % 47
        \stemUp e,4 \stemUp e4 r4 | % 48
        r4 \stemUp g4 -. \stemDown b4 -. | % 49
        \stemUp g8 ( \stemUp fis8 \stemUp e4 ) \stemDown e'4 |
        \barNumberCheck #50
        \stemDown d2 -> \stemDown cis4 ~ -> | % 51
        \stemDown cis4 \stemDown c2 -> | % 52
        \stemDown b2 -> \stemUp e,4 ~ \pageBreak | % 53
        \stemUp e4 \stemDown e'2 -> | % 54
        \stemDown d2 -> \stemDown cis4 ~ -> | % 55
        \stemDown cis4 \stemDown c2 -> | % 56
        \stemDown b'8 \stemDown e,8 \stemDown e4 -. \stemDown e8 ( ^
        "a 2" \stemDown c8 ) | % 57
        \stemDown b8 ( \stemDown e8 ) \stemDown e4 -. \stemDown e8 (
        \stemDown c8 ) | % 58
        \stemDown b8 ( \stemDown e8 ) \stemDown e4 -. \stemDown e8 (
        \stemDown c8 ) | % 59
        \stemDown e4 -. r4 r4 }
    \pageBreak | \barNumberCheck #60
    R2.*7 \pageBreak | % 67
    R2. \bar "||"
    \key e \major \stemUp gis,8 ( ^\p \stemUp b8 ) \stemDown b2 ~ | % 69
    \stemDown b2 \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis8 \stemUp b8 \stemUp fis8 }
    | \barNumberCheck #70
    \stemUp e2 \stemUp fis4 | % 71
    \stemUp gis8 ( \stemUp b8 ) \stemDown b2 ~ \pageBreak | % 72
    \stemUp b8 \stemUp e8 ( \stemUp dis8 \stemUp cis8 \stemDown b4 ~ | % 73
    \stemUp b8 ) \stemUp cis8 ( \stemUp b8 \stemUp gis8 \stemDown b4 ~ | % 74
    \stemUp b8 ) \stemUp gis8 ( \stemUp fis8 \stemUp gis8 \stemUp b8
    \stemUp gis8 | % 75
    \stemUp fis8 \stemUp gis8 \stemUp e2 ~ | % 76
    \stemUp e4 ) r4 r4 \pageBreak | % 77
    R2.*5 \pageBreak | % 82
    R2.*2 | % 84
    r4 \stemDown a8 ( _\f _\< \stemDown cis8 \stemDown cis4 ~ | % 85
    \stemDown cis2 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown dis8 ( _\! \stemDown cis8 \stemDown a8 }
    | % 86
    \stemUp gis8 \stemUp e8 _\> \stemUp gis2 ~ \pageBreak | % 87
    \stemUp gis2. ) | % 88
    r4 _\! \stemDown a8 ( _\< \stemDown cis8 \stemDown cis4 ~ | % 89
    \stemDown cis2 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown dis8 ( _\! \stemDown cis8 \stemDown a8 }
    | \barNumberCheck #90
    \stemUp gis8 \stemUp e8 _\> \stemUp gis2 ~ | % 91
    \stemUp gis2 ) r4 \pageBreak | % 92
    \stemDown e'8 _\! _\p \stemDown e8 \stemDown e8 \stemDown e8
    \stemDown dis8 \stemDown dis8 | % 93
    \stemDown e8 \stemDown e8 \stemDown e8 \stemDown e8 \stemDown dis8
    \stemDown dis8 | % 94
    \stemDown e8 _\markup{ \italic {cresc.} } \stemDown e8 \stemDown e8
    \stemDown e8 \stemDown dis8 \stemDown dis8 | % 95
    \stemDown e8 _\< \stemDown e8 \stemDown e8 \stemDown e8 \stemDown
    dis8 \stemDown dis8 | % 96
    \stemDown e8 _\! _\f \stemDown e8 \stemDown e8 \stemDown e8
    \stemDown dis8 \stemDown dis8 | % 97
    \stemDown e8 \stemDown e8 \stemDown e8 \stemDown e8 \stemDown dis8
    _\markup{ \italic {dim.} } _\> \stemDown dis8 | % 98
    \stemDown dis8 \stemDown dis8 \stemDown e8 \stemDown e8 \stemDown
    dis8 \stemDown dis8 \pageBreak | % 99
    R2.*8 \pageBreak | % 107
    R2.*6 \pageBreak | % 113
    R2.*4 | % 117
    r4 _\! \stemDown dis2 ~ _\f | % 118
    \stemDown dis2 \stemDown dis4 \pageBreak | % 119
    \stemDown dis4 \stemDown dis4 \stemDown fis4 | \barNumberCheck #120
    \stemDown fis2. ~ _\markup{ \italic {cresc.} } | % 121
    \stemDown fis2. | % 122
    \stemDown dis2 \stemDown dis4 \bar "||"
    \key g \major \stemDown e2 _\ff \stemDown e4 ~ | % 124
    \stemDown e4 \stemDown e2 | % 125
    \stemDown e2 \stemDown e4 ~ \pageBreak | % 126
    \stemDown e4 \stemDown e2 | % 127
    \stemDown e2 \stemDown e4 ~ | % 128
    \stemDown e4 \stemDown e2 | % 129
    \stemDown e2 \stemDown e4 | \barNumberCheck #130
    \stemDown g4 r4 \stemDown fis4 | % 131
    \stemDown g4 r4 \stemDown fis4 | % 132
    \stemDown g4 r4 \stemDown fis4 \pageBreak | % 133
    \stemDown g4 r4 \stemDown fis4 | % 134
    \stemDown g4 r4 r4 | % 135
    \stemDown e4 r4 r4 | % 136
    \stemDown g4 r4 r4 | % 137
    \stemDown e4 r4 r4 | % 138
    \stemDown e4 r4 r4 | % 139
    R2. | \barNumberCheck #140
    \stemDown e4 r4 r4 | % 141
    R2. \bar "||"
    \pageBreak | % 142
    \stemDown c2. ( _\fp _\> | % 143
    \stemDown b4 ) r2 _\! | % 144
    R2.*6 \pageBreak | \barNumberCheck #150
    R2.*8 \pageBreak | % 158
     \once \override NoteHead.style = ##f \stemDown cis4 s2 | % 159
    R2.*7 \pageBreak | % 166
    R2.*4 | \barNumberCheck #170
    r4 r4 \stemDown as'4 ( ^\p | % 171
    \stemDown g4 \stemDown b,4 ) r4 | % 172
    R2.*2 \pageBreak | % 174
    R2. | % 175
    r4 r4 \stemDown c4 _\p \repeat volta 2 {
        | % 176
        \stemDown c4. \stemDown c8 \stemDown c8 ^. r8 | % 177
        \stemDown c4. \stemDown c8 \stemDown e8 -. r8 | % 178
        \stemDown c2. ~ | % 179
        \stemDown c2 \stemDown c4 \pageBreak | \barNumberCheck #180
        \stemDown c4. \stemDown c8 \stemDown e4 | % 181
        \stemDown b4. \stemDown b8 \stemDown b4 | % 182
        \stemDown c2. ~ | % 183
        \stemDown c2 \stemDown c4 | % 184
        \stemDown c4. \stemDown c8 \stemDown e8 r8 | % 185
        \stemDown c4. \stemDown c8 \stemDown e8 r8 \pageBreak | % 186
        \stemDown e2. ~ | % 187
        \stemDown e2 \stemDown e4 | % 188
        \stemDown e4. _\< \stemDown e8 \stemDown e4 | % 189
        \stemDown d2 _\! _\f \stemDown c4 _\> | \barNumberCheck #190
        \stemDown c2. ~ | % 191
        \stemDown c4 ~ _\! _\p r4 \stemDown c4 }
    | % 192
    \stemDown c4 r4 r4 \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
        R2.*7 \pageBreak | \barNumberCheck #200
        R2. | % 201
        \stemDown g'8 ( ^\p \stemDown b8 \stemDown g8 ) r8 \stemDown f8
        r8 | % 202
        \stemUp e2. \startTrillSpan ^ "[♮]" _\fp | % 203
        \stemDown d8 ( \stemDown fis8 \stemDown d8 ) r8 \stemDown c8 r8
        | % 204
        \stemDown b2. \startTrillSpan \stopTrillSpan _\fp | % 205
        \stemDown c8 ( _\p \stemDown e8 \stemDown c8 ) r8 \stemDown b8 r8
        \pageBreak | % 206
        \stemUp a2. \startTrillSpan \stopTrillSpan | % 207
        \stemUp g8 ( \stemUp b8 \stemUp g8 ) r8 \stemUp fis8 r8 | % 208
        \stemUp e2 ~ \startTrillSpan \stopTrillSpan \stemUp e8 r8 | % 209
        R2.*4 \pageBreak | % 213
        R2.*8 \pageBreak | % 221
        R2.*3 | % 224
        \stemDown c'4. _\p \stemDown c8 \stemDown c8 r8 | % 225
        \stemDown c4. \stemDown c8 \stemDown e8 r8 | % 226
        \stemDown e2. ~ \pageBreak | % 227
        \stemDown e2 \stemDown e4 | % 228
        \stemDown e4. \stemDown e8 \stemDown e8 r8 | % 229
        \stemDown g4. \stemDown g8 \stemDown f8 r8 | \barNumberCheck
        #230
        \stemDown e2. ~ | % 231
        \stemDown e2 \stemDown c4 \pageBreak | % 232
        \stemDown c4. \stemDown c8 \stemDown e8 r8 | % 233
        \stemDown c4. \stemDown c8 \stemDown e8 r8 | % 234
        \stemDown e2. ~ | % 235
        \stemDown e2 \stemDown e4 | % 236
        \stemDown e4. \stemDown e8 \stemDown e4 \pageBreak | % 237
        \stemDown d2 \stemDown c4 | % 238
        \stemDown c2. ~ _\fz | % 239
        \stemDown c4 r4 r4 }
    | \barNumberCheck #240
    R2.*3 \pageBreak | % 243
     \once \override NoteHead.style = ##f \stemDown cis4 s2 | % 244
    R2.*5 \bar "||"
    \pageBreak | % 249
    R2.*8 | % 257
    r4 \stemUp g'8 ^\p \stemUp g8 \stemUp g4 ^. \pageBreak | % 258
    \stemUp c,4 ^. \stemUp c4 ^. r4 | % 259
    r4 \stemUp g'8 \stemUp g8 \stemUp g4 ^. | \barNumberCheck #260
    \stemUp c,4 ^. \stemUp c4 ^. r4 | % 261
    R2.*4 \pageBreak | % 265
    r4 \stemUp gis'8 ^\p \stemUp gis8 \stemUp gis4 ^. | % 266
    \stemUp cis,4 ^. \stemUp cis4 ^. r4 | % 267
    r4 \stemUp gis'8 \stemUp gis8 \stemUp gis4 ^. | % 268
    \stemUp cis,4 ^. \stemUp cis4 ^. r4 | % 269
    R2.*2 | % 271
    \stemUp fis,2 _\f ^ "a 2" \stemUp a4 -. \pageBreak | % 272
    \stemDown cis4 ^ "a 2" \stemDown fis2 -> | % 273
    \stemUp fis,2 _\f _\< \stemUp a4 -. | % 274
    \stemDown cis4 -. \stemDown fis2 -> | % 275
    \stemDown a2 -> _\! _\ff \stemDown fis4 -. | % 276
    \stemDown cis4 -. \stemUp a2 -> \pageBreak | % 277
    \stemDown dis8 ^ "a 2" \stemDown dis8 \stemDown dis4 -. \stemUp a4
    -. | % 278
    \stemUp a4 -. \stemDown dis8 \stemDown dis8 \stemDown dis4 | % 279
    \stemUp a4 -. \stemUp a4 -. \stemDown dis8 \stemDown dis8 |
    \barNumberCheck #280
    \stemDown dis4 -. \stemUp a4 -. \stemUp a4 -. | % 281
    \stemDown gis'2. ~ _\fff | % 282
    \stemDown gis2. ~ \pageBreak | % 283
    \stemDown gis2. ~ _\markup{ \italic {dim.} } | % 284
    \stemDown gis2. ~ | % 285
    \stemDown gis4 r4 r4 | % 286
    R2.*2 \pageBreak | % 288
     \once \override NoteHead.style = ##f \stemDown cis,4 s2 | % 289
    R2.*5 \pageBreak | % 294
    R2.*6 | \barNumberCheck #300
    \stemDown g'4 _\ff r4 r4 \bar "|."
    }

PartPFourVoiceThree =  \relative c' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key g \major s1*3 \bar "||"
        s4*9 \pageBreak s4*21 \pageBreak s2*9 \pageBreak s4*15
        \pageBreak s4*15 \pageBreak s4*15 \pageBreak s2*9 \pageBreak
        s4*15 \pageBreak s2*9 \pageBreak s4*21 }
    \pageBreak s4*21 \pageBreak s2. \bar "||"
    \key e \major s1*3 \pageBreak s4*15 \pageBreak s4*15 \pageBreak
    s4*15 \pageBreak s4*15 \pageBreak s4*21 \pageBreak s1*6 \pageBreak
    s2*9 \pageBreak s2*9 \pageBreak s1*3 \bar "||"
    \key g \major s4*9 \pageBreak s4*21 \pageBreak s4*27 \bar "||"
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*6
    \pageBreak s1. \repeat volta 2 {
        s1*3 \pageBreak s2*9 \pageBreak s2*9 }
    s2. \bar "||"
    \pageBreak \repeat volta 2 {
        s4*21 \pageBreak s1. | % 202
        R2. s4*9 \pageBreak s4*21 \pageBreak s1*6 \pageBreak s2*9
        \pageBreak s4*15 \pageBreak s4*15 \pageBreak s4*9 }
    s4*9 \pageBreak s2*9 \bar "||"
    \pageBreak s4*27 \pageBreak s4*21 \pageBreak s4*21 \pageBreak s4*15
    \pageBreak s2*9 \pageBreak s4*15 \pageBreak s2*9 \pageBreak s4*21
    \bar "|."
    }

PartPFiveVoiceOne =  \relative g'' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key bes \major \transposition a | % 1
        \stemDown g8 _\f ^ "a 2" \stemDown g8 \stemDown g2 ~ | % 2
        \stemDown g2. | % 3
        \stemDown d8 \stemDown d8 \stemDown d2 ~ | % 4
        \stemDown d2. \bar "||"
        R2.*3 \pageBreak | % 8
        R2.*6 | % 14
        r4 \stemUp d8 ^. ^\p \stemUp d8 ^. \stemUp d4 ^. \pageBreak | % 15
        \stemUp g,4 -. \stemUp g4 -. r4 | % 16
        r4 \stemDown bes4 -. \stemDown d4 -. | % 17
        \stemUp bes8 ( \stemUp a8 \stemUp g4 ) r4 | % 18
        r4 \stemUp d'8 ^. \stemUp d8 ^. \stemUp d4 ^. | % 19
        \stemUp g,4 -. \stemUp g4 -. r4 | \barNumberCheck #20
        r4 \stemDown bes4 -. \stemDown d4 -. \pageBreak | % 21
        \stemUp g,2. -> ^ "a 2" _\fz | % 22
        \stemUp g2. -> _\fz | % 23
        \stemUp g2. -> _\fz | % 24
        \stemUp g4. _\fz \stemUp d8 ( \stemUp bes8 \stemUp d8 | % 25
        \stemUp g2. ) _\fz \pageBreak | % 26
        \stemUp g2. _\fz ^ "a 2" | % 27
        \stemUp g2. _\fz | % 28
        \stemUp g4. ( _\fz \stemUp d8 \stemUp bes8 \stemUp d8 | % 29
        \stemUp g,8 ) r8 r4 r4 | \barNumberCheck #30
        R2. \pageBreak | % 31
        R2.*5 \pageBreak | % 36
        R2.*6 \pageBreak | % 42
        r4 \stemDown d'''8 _\ff \stemDown d8 \stemDown d4 | % 43
        \stemDown g,4 \stemDown g4 r4 | % 44
        r4 \stemDown bes4 -. \stemDown d4 -. | % 45
        \stemDown bes8 ( \stemDown a8 \stemDown g4 ) r4 | % 46
        r4 \stemDown d'8 \stemDown d8 \stemDown d4 \pageBreak | % 47
        \stemDown g,4 \stemDown g4 r4 | % 48
        r4 \stemDown bes4 -. \stemDown d4 -. | % 49
        \stemDown bes8 ( \stemDown a8 \stemDown g4 ) \stemDown g4 |
        \barNumberCheck #50
        \stemDown f2 -> \stemDown e4 ~ -> | % 51
        \stemDown e4 \stemDown es2 -> | % 52
        \stemDown d2 -> \stemUp g,4 ~ \pageBreak | % 53
        \stemUp g4 \stemDown g'2 -> | % 54
        \stemDown f2 -> \stemDown e4 ~ -> | % 55
        \stemDown e4 \stemDown es2 -> | % 56
        \stemDown d8 ( \stemDown g8 ) \stemDown g4 -. \stemDown g8 (
        \stemDown es8 ) | % 57
        \stemDown d8 ( \stemDown g8 ) \stemDown g4 -. \stemDown g8 (
        \stemDown es8 ) | % 58
        \stemDown d8 ( \stemDown g8 ) \stemUp g,4 -. \stemUp g8 (
        \stemUp es8 ) | % 59
        \stemDown g'4 -. r4 r4 }
    \pageBreak | \barNumberCheck #60
    R2.*7 \pageBreak | % 67
    R2. \bar "||"
    \key g \major R2.*4 \pageBreak | % 72
    R2.*4 | % 76
    \stemDown b8 ( _\mp _\< \stemDown d8 \stemDown d2 ~ \pageBreak | % 77
    \stemDown d2 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( _\! _\mf \stemDown d8 \stemDown a8 }
    | % 78
    \stemDown g2 \stemDown a4 ) | % 79
    \stemDown b8 ( _\< \stemDown d8 ) \stemDown d2 ~ | \barNumberCheck
    #80
    \stemDown d8 \stemDown g8 ( _\! \stemDown fis8 \stemDown e8 )
    \stemDown d4 ~ | % 81
    \stemDown d8 \stemDown e8 ( \stemDown d8 \stemDown b8 ) \stemDown d4
    ~ \pageBreak | % 82
    \stemDown d8 \stemDown b8 ( \stemDown a8 \stemDown b8 _\> \stemDown
    d8 \stemDown b8 | % 83
    \stemDown a8 \stemDown b8 \stemDown g2 ) | % 84
    R2.*3 \pageBreak | % 87
    R2.*5 \pageBreak | % 92
    \stemDown b,8 _\! _\p \stemDown b8 \stemDown b8 \stemDown b8
    \stemDown c8 \stemDown c8 | % 93
    \stemDown b8 \stemDown b8 \stemDown b8 \stemDown b8 \stemDown c8
    \stemDown c8 | % 94
    \stemDown b8 _\markup{ \italic {cresc.} } \stemDown b8 \stemDown b8
    \stemDown b8 \stemDown c8 \stemDown c8 | % 95
    \stemDown b8 _\< \stemDown b8 \stemDown b8 \stemDown b8 \stemDown c8
    \stemDown c8 | % 96
    \stemDown d8 _\! _\f \stemDown d8 \stemDown d8 \stemDown d8
    \stemDown d8 \stemDown d8 | % 97
    \stemDown d8 \stemDown d8 \stemDown d8 \stemDown d8 \stemDown d8
    _\markup{ \italic {dim.} } _\> \stemDown d8 | % 98
    \stemDown c8 \stemDown c8 \stemDown b8 \stemDown b8 \stemDown b8
    \stemDown b8 \pageBreak | % 99
    R2.*8 \pageBreak | % 107
    R2.*6 \pageBreak | % 113
    R2.*6 \pageBreak | % 119
    R2.*3 | % 122
    \stemDown fis'2 _\! _\f _\< \stemDown fis4 \bar "||"
    \key bes \major \stemDown g2 _\! _\ff \stemDown g4 ~ | % 124
    \stemDown g4 \stemDown g2 | % 125
    \stemDown g2 \stemDown g4 ~ \pageBreak | % 126
    \stemDown g4 \stemDown g2 | % 127
    \stemDown g2 \stemDown g4 ~ | % 128
    \stemDown g4 \stemDown g2 | % 129
    \stemDown a2 \stemDown a4 | \barNumberCheck #130
    \stemDown bes4 r4 \stemDown a4 | % 131
    \stemDown bes4 r4 \stemDown a4 | % 132
    \stemDown bes4 r4 \stemDown a4 \pageBreak | % 133
    \stemDown bes4 r4 \stemDown a4 | % 134
    \stemDown bes4 r4 r4 | % 135
    \stemDown g4 r4 r4 | % 136
    \stemDown bes4 r4 r4 | % 137
    \stemDown g4 r4 r4 | % 138
    \stemDown bes4 r4 r4 | % 139
    R2. | \barNumberCheck #140
    \stemDown bes4 r4 r4 | % 141
    R2. \bar "||"
    \pageBreak | % 142
    R2.*2 | % 144
    \stemDown bes,2. ~ -> _\p _\> | % 145
    \stemDown bes4 r2 _\! | % 146
    \stemUp bes,2. ~ -> _\pp _\> | % 147
    \stemUp bes4 r4 _\! r4 | % 148
    \stemUp g2. ~ _> _\> | % 149
    \stemUp g4 r4 _\! r4 \pageBreak | \barNumberCheck #150
    \stemUp bes2. ~ _\pp | % 151
    \stemUp bes2. ~ | % 152
    \stemUp bes2. ~ | % 153
    \stemUp bes2. ~ | % 154
    \stemUp bes4 r2 | % 155
    R2.*3 \pageBreak | % 158
    r4 r4 \stemDown g''4 ( ^\pp | % 159
    \stemDown fis4 \stemDown bes,4 ) r4 | \barNumberCheck #160
    R2.*6 \pageBreak | % 166
    R2.*8 \pageBreak | % 174
    R2.*2 \repeat volta 2 {
        | % 176
        \stemDown bes4. _\p \stemDown bes8 \stemDown bes8 -. r8 | % 177
        \stemDown bes4. \stemDown bes8 \stemDown bes8 -. r8 | % 178
        \stemDown bes2. ~ | % 179
        \stemDown bes2 \stemDown bes4 \pageBreak | \barNumberCheck #180
        \stemDown bes4. \stemDown bes8 \stemDown es4 | % 181
        \stemDown d4. \stemDown d8 \stemDown c4 | % 182
        \stemDown bes2. ~ | % 183
        \stemDown bes2 \stemDown bes4 | % 184
        \stemDown bes4. \stemDown bes8 \stemDown es8 r8 | % 185
        \stemDown es4. \stemDown es8 \stemDown es8 r8 \pageBreak | % 186
        \stemDown es2. ~ | % 187
        \stemDown es2 \stemDown es4 | % 188
        \stemDown d4. _\< \stemDown d8 \stemDown d4 | % 189
        \stemDown d2 _\! _\f \stemDown es4 _\> | \barNumberCheck #190
        \stemDown es2. ~ | % 191
        \stemDown es4 ~ _\! _\p r4 r4 }
    | % 192
    \stemDown es4 r4 r4 \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
        R2.*7 \pageBreak | \barNumberCheck #200
        R2. | % 201
        \stemDown d8 ( _\p \stemDown bes'8 \stemDown d,8 ) r8 \stemDown
        c8 r8 | % 202
        \stemDown bes2. \startTrillSpan \stopTrillSpan ^ "[♭]" _\fp | % 203
        \stemDown a8 ( \stemDown f'8 \stemUp a,8 ) r8 \stemUp g8 r8 | % 204
        \stemUp f2. \startTrillSpan \stopTrillSpan _\fp | % 205
        \stemDown g8 ( \stemDown es'8 \stemUp g,8 ) r8 \stemUp f8 r8
        \pageBreak | % 206
        \stemUp es2. \startTrillSpan \stopTrillSpan | % 207
        \stemUp d8 ( \stemUp bes'8 \stemUp d,8 ) r8 \stemUp c8 r8 | % 208
        \stemUp bes2 ~ \startTrillSpan \stopTrillSpan \stemUp bes8 r8 | % 209
        R2.*4 \pageBreak | % 213
        R2.*4 | % 217
        \stemUp d2 ~ \startTrillSpan \stopTrillSpan _\p \stemUp d8 r8 | % 218
        R2. | % 219
        \stemUp d2 ~ \startTrillSpan \stopTrillSpan \stemUp d8 r8 |
        \barNumberCheck #220
        R2. \pageBreak | % 221
        \once \omit TupletBracket
        \times 4/6  {
            \stemUp f2. :16 }
        \stemUp f8 r8 | % 222
        R2. | % 223
        \once \omit TupletBracket
        \times 4/6  {
            \stemUp f2. :16 }
        \stemUp f8 r8 | % 224
        \stemDown bes4. _\p \stemDown bes8 \stemDown bes8 r8 | % 225
        \stemDown bes4. \stemDown bes8 \stemDown bes8 r8 | % 226
        \stemDown bes2. ~ \pageBreak | % 227
        \stemDown bes2 \stemDown bes4 | % 228
        \stemDown bes4. \stemDown bes8 \stemDown es8 r8 | % 229
        \stemDown d4. \stemDown d8 \stemDown c8 r8 | \barNumberCheck
        #230
        \stemDown bes2. ~ | % 231
        \stemUp bes2 \stemDown bes4 \pageBreak | % 232
        \stemDown bes4. \stemDown bes8 \stemDown bes8 r8 | % 233
        \stemDown bes4. \stemDown bes8 \stemDown bes8 r8 | % 234
        \stemDown bes2. ~ | % 235
        \stemDown bes2 \stemDown es4 | % 236
        \stemDown d4. \stemDown d8 \stemDown d4 \pageBreak | % 237
        \stemDown d2 \stemDown es4 | % 238
        \stemDown es2. ~ _\fz | % 239
        \stemDown es4 r4 r4 }
    | \barNumberCheck #240
    R2.*3 \pageBreak | % 243
    R2.*6 \bar "||"
    \pageBreak | % 249
    R2.*9 \pageBreak | % 258
    R2.*7 \pageBreak | % 265
    R2.*6 | % 271
    \stemUp a,2 _\f \stemDown c4 -. \pageBreak | % 272
    \stemDown e4 -. \stemDown a2 -> | % 273
    \stemUp a,2 ^ "a 2" _\f _\< \stemDown c4 -. | % 274
    \stemDown e4 -. \stemDown a2 -> | % 275
    \stemDown c2 -> _\! _\ff \stemDown a4 -. | % 276
    \stemDown e4 -. \stemDown c2 -> \pageBreak | % 277
    \stemDown fis8 \stemDown fis8 \stemDown fis4 -. \stemDown c4 -. | % 278
    \stemDown c4 -. \stemDown fis8 \stemDown fis8 \stemDown fis4 | % 279
    \stemDown c4 -. \stemDown c4 -. \stemDown fis8 \stemDown fis8 |
    \barNumberCheck #280
    \stemDown fis4 -. \stemDown c4 -. \stemDown c4 -. | % 281
    \stemDown g'2. ~ _\fff | % 282
    \stemDown g2. ~ \pageBreak | % 283
    \stemDown g2. ~ _\markup{ \italic {dim.} } | % 284
    \stemDown g2. ~ | % 285
    \stemDown g4 r4 r4 | % 286
    R2.*2 \pageBreak | % 288
    R2. | % 289
    \stemUp bes,,2. ~ _\p | \barNumberCheck #290
    \stemUp bes2. ~ | % 291
    \stemUp bes2. ~ | % 292
    \stemUp bes2. | % 293
    \stemUp bes2. ~ _\pp \pageBreak | % 294
    \stemUp bes2. ~ | % 295
    \stemUp bes2. ~ | % 296
    \stemUp bes2. ~ | % 297
    \stemUp bes2. ~ | % 298
    \stemUp bes4 r4 r4 | % 299
    R2. | \barNumberCheck #300
    \stemDown d'4 _\ff r4 r4 \bar "|."
    }

PartPSixVoiceOne =  \relative g'' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key bes \major \transposition a | % 1
        \stemDown g8 _\f ^ "a 2" \stemDown g8 \stemDown g2 ~ | % 2
        \stemDown g2. | % 3
        \stemDown d8 \stemDown d8 \stemDown d2 ~ | % 4
        \stemDown d2. \bar "||"
        R2.*3 \pageBreak | % 8
        R2.*6 | % 14
        r4 \stemUp d8 ^. ^\p \stemUp d8 ^. \stemUp d4 ^. \pageBreak | % 15
        \stemUp g,4 -. \stemUp g4 -. r4 | % 16
        r4 \stemDown bes4 -. \stemDown d4 -. | % 17
        \stemUp bes8 ( \stemUp a8 \stemUp g4 ) r4 | % 18
        r4 \stemUp d'8 ^. \stemUp d8 ^. \stemUp d4 ^. | % 19
        \stemUp g,4 -. \stemUp g4 -. r4 | \barNumberCheck #20
        r4 \stemDown bes4 -. \stemDown d4 -. \pageBreak | % 21
        \stemUp g,2. -> ^ "a 2" _\fz | % 22
        \stemUp g2. -> _\fz | % 23
        \stemUp g2. -> _\fz | % 24
        \stemUp g4. _\fz \stemUp d8 ( \stemUp bes8 \stemUp d8 | % 25
        \stemUp g2. ) _\fz \pageBreak | % 26
        \stemUp g2. _\fz ^ "a 2" | % 27
        \stemUp g2. _\fz | % 28
        \stemUp g4. ( _\fz \stemUp d8 \stemUp bes8 \stemUp d8 | % 29
        \stemUp g,8 ) r8 r4 r4 | \barNumberCheck #30
        R2. \pageBreak | % 31
        R2.*5 \pageBreak | % 36
        R2.*6 \pageBreak | % 42
        r4 \stemDown d''8 _\ff \stemDown d8 \stemDown d4 | % 43
        \stemUp g,4 \stemUp g4 r4 | % 44
        r4 \stemDown bes4 -. \stemDown d4 -. | % 45
        \stemUp bes8 ( \stemUp a8 \stemUp g4 ) r4 | % 46
        r4 \stemDown d'8 \stemDown d8 \stemDown d4 \pageBreak | % 47
        \stemUp g,4 \stemUp g4 r4 | % 48
        r4 \stemDown bes4 -. \stemDown d4 -. | % 49
        \stemUp bes8 ( \stemUp a8 \stemUp g4 ) \stemUp g4 |
        \barNumberCheck #50
        \stemUp f2 -> \stemUp e4 ~ -> | % 51
        \stemUp e4 \stemUp es2 -> | % 52
        \stemUp d2 -> \stemUp g,4 ~ \pageBreak | % 53
        \stemUp g4 \stemUp g'2 -> | % 54
        \stemUp f2 -> \stemUp e4 ~ -> | % 55
        \stemUp e4 \stemUp es2 -> | % 56
        \stemUp d8 ( \stemUp g8 ) \stemUp g4 -. \stemUp g8 ( \stemUp es8
        ) | % 57
        \stemUp d8 ( \stemUp g8 ) \stemUp g4 -. \stemUp g8 ( \stemUp es8
        ) | % 58
        \stemUp d8 ( \stemUp g8 ) \stemUp g4 -. \stemUp g8 ( \stemUp es8
        ) | % 59
        \stemUp g4 -. r4 r4 }
    \pageBreak | \barNumberCheck #60
    R2.*7 \pageBreak | % 67
    R2. \bar "||"
    \key g \major R2.*4 \pageBreak | % 72
    R2.*4 | % 76
    \stemDown b8 ( _\mp _\< \stemDown d8 \stemDown d2 ~ \pageBreak | % 77
    \stemDown d2 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( _\! _\mf \stemDown d8 \stemDown a8 }
    | % 78
    \stemUp g2 \stemUp a4 ) | % 79
    \stemDown b8 ( _\< \stemDown d8 ) \stemDown d2 ~ | \barNumberCheck
    #80
    \stemDown d8 \stemDown g8 ( _\! \stemDown fis8 \stemDown e8 )
    \stemDown d4 ~ | % 81
    \stemDown d8 \stemDown e8 ( \stemDown d8 \stemDown b8 ) \stemDown d4
    ~ \pageBreak | % 82
    \stemDown d8 \stemDown b8 ( \stemDown a8 \stemDown b8 _\> \stemDown
    d8 \stemDown b8 | % 83
    \stemUp a8 \stemUp b8 \stemUp g2 ) | % 84
    R2.*3 \pageBreak | % 87
    R2.*5 \pageBreak | % 92
    \stemDown b8 _\! _\p \stemDown b8 \stemDown b8 \stemDown b8
    \stemDown c8 \stemDown c8 | % 93
    \stemDown b8 \stemDown b8 \stemDown b8 \stemDown b8 \stemDown c8
    \stemDown c8 | % 94
    \stemDown b8 \stemDown b8 \stemDown b8 \stemDown b8 \stemDown c8
    \stemDown c8 | % 95
    \stemDown b8 _\< \stemDown b8 \stemDown b8 \stemDown b8 \stemDown c8
    \stemDown c8 | % 96
    \stemDown b8 _\! _\f \stemDown b8 \stemDown b8 \stemDown b8
    \stemDown b8 \stemDown b8 | % 97
    \stemDown b8 \stemDown b8 \stemDown b8 \stemDown b8 \stemDown b8
    _\markup{ \italic {dim.} } _\> \stemDown b8 | % 98
    \stemDown c8 \stemDown c8 \stemDown b8 \stemDown b8 \stemDown b8
    \stemDown b8 \pageBreak | % 99
    R2.*8 \pageBreak | % 107
    R2.*6 \pageBreak | % 113
    R2.*6 \pageBreak | % 119
    R2.*3 | % 122
    \stemUp a2 _\! _\f _\< \stemUp a4 \bar "||"
    \key bes \major \stemDown bes2 _\! _\ff \stemDown bes4 ~ | % 124
    \stemDown bes4 \stemDown bes2 | % 125
    \stemUp a2 \stemUp a4 ~ \pageBreak | % 126
    \stemUp a4 \stemDown bes2 | % 127
    \stemDown bes2 \stemDown bes4 ~ | % 128
    \stemDown bes4 \stemDown bes2 | % 129
    \stemDown g'2 \stemDown g4 | \barNumberCheck #130
    \stemDown g4 r4 \stemDown g4 | % 131
    \stemDown g4 r4 \stemDown g4 | % 132
    \stemDown g4 r4 \stemDown g4 \pageBreak | % 133
    \stemDown g4 r4 \stemDown g4 | % 134
    \stemDown g4 r4 r4 | % 135
    \stemDown es4 r4 r4 | % 136
    \stemDown g4 r4 r4 | % 137
    \stemDown es4 r4 r4 | % 138
    \stemDown g4 r4 r4 | % 139
    R2. | \barNumberCheck #140
    \stemDown g4 r4 r4 | % 141
    R2. \bar "||"
    \pageBreak | % 142
    R2.*2 | % 144
    \stemUp g,2. ~ -> _\p _\> | % 145
    \stemUp g4 r2 _\! | % 146
    \stemUp bes,2. ~ -> _\pp _\> | % 147
    \stemUp bes4 r4 _\! r4 | % 148
    \stemUp g2. ~ _> _\> | % 149
    \stemUp g4 r4 _\! r4 \pageBreak | \barNumberCheck #150
    \stemUp g2. ~ _\pp | % 151
    \stemUp g2. ~ | % 152
    \stemUp g2. ~ | % 153
    \stemUp g2. ~ | % 154
    \stemUp g4 r2 | % 155
    R2.*3 \pageBreak | % 158
    r4 r4 \stemDown g''4 ( ^\pp | % 159
    \stemDown fis4 \stemDown bes,4 ) r4 | \barNumberCheck #160
    R2.*6 \pageBreak | % 166
    R2.*8 \pageBreak | % 174
    R2.*2 \repeat volta 2 {
        | % 176
        \stemUp g4. _\p \stemUp g8 \stemUp g8 -. r8 | % 177
        \stemUp g4. \stemUp g8 \stemUp g8 -. r8 | % 178
        \stemUp g2. ~ | % 179
        \stemUp g2 \stemUp g4 \pageBreak | \barNumberCheck #180
        \stemUp g4. \stemUp g8 \stemDown bes4 | % 181
        \stemDown bes4. \stemDown bes8 \stemUp as4 | % 182
        \stemUp g2. ~ | % 183
        \stemUp g2 \stemUp g4 | % 184
        \stemUp g4. \stemUp g8 \stemDown bes8 r8 | % 185
        \stemDown bes4. \stemDown bes8 \stemDown bes8 r8 \pageBreak | % 186
        \stemDown bes2. ~ | % 187
        \stemDown bes2 \stemDown bes4 | % 188
        \stemDown bes4. _\< \stemDown bes8 \stemDown bes4 | % 189
        \stemDown bes2 _\! _\f \stemDown bes4 _\> | \barNumberCheck #190
        \stemDown bes2. ~ | % 191
        \stemDown bes4 ~ _\! _\p r4 r4 }
    | % 192
    \stemDown bes4 r4 r4 \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
        R2.*7 \pageBreak | \barNumberCheck #200
        R2. | % 201
        \stemDown bes8 ( _\p \stemDown d8 \stemDown bes8 ) r8 \stemUp as8
        r8 | % 202
        \stemUp g2. \startTrillSpan \stopTrillSpan ^ "[♭]" _\fp | % 203
        \stemUp f8 ( \stemUp a8 \stemUp f8 ) r8 \stemUp es8 r8 | % 204
        \stemUp d2. \startTrillSpan \stopTrillSpan _\fp | % 205
        \stemUp es8 ( \stemUp g8 \stemUp es8 ) r8 \stemUp d8 r8
        \pageBreak | % 206
        \stemUp c2. \startTrillSpan \stopTrillSpan | % 207
        \stemUp bes8 ( \stemUp d8 \stemUp bes8 ) r8 \stemUp a8 r8 | % 208
        \stemUp g2 ~ \startTrillSpan \stopTrillSpan \stemUp g8 r8 | % 209
        R2.*4 \pageBreak | % 213
        R2.*4 | % 217
        \stemUp g2 ~ \startTrillSpan \stopTrillSpan _\p \stemUp g8 r8 | % 218
        R2. | % 219
        \stemUp g2 ~ \startTrillSpan \stopTrillSpan \stemUp g8 r8 |
        \barNumberCheck #220
        R2. \pageBreak | % 221
        \once \omit TupletBracket
        \times 4/6  {
            \stemUp f2. :16 }
        \stemUp f8 r8 | % 222
        R2. | % 223
        \once \omit TupletBracket
        \times 4/6  {
            \stemUp f2. :16 }
        \stemUp f8 r8 | % 224
        \stemUp g'4. _\p \stemUp g8 \stemUp g8 r8 | % 225
        \stemUp g4. \stemUp g8 \stemUp g8 r8 | % 226
        \stemUp g2. ~ \pageBreak | % 227
        \stemUp g2 \stemUp g4 | % 228
        \stemUp g4. \stemUp g8 \stemUp g8 r8 | % 229
        \stemDown bes4. \stemDown bes8 \stemUp as8 r8 | \barNumberCheck
        #230
        \stemUp g2. ~ | % 231
        \stemUp g2 \stemUp g4 \pageBreak | % 232
        \stemUp g4. \stemUp g8 \stemUp g8 r8 | % 233
        \stemUp g4. \stemUp g8 \stemUp g8 r8 | % 234
        \stemUp g2. ~ | % 235
        \stemUp g2 \stemDown es'4 | % 236
        \stemDown d4. \stemDown d8 \stemDown d4 \pageBreak | % 237
        \stemDown d2 \stemDown es4 | % 238
        \stemDown es2. ~ _\fz | % 239
        \stemDown es4 r4 r4 }
    | \barNumberCheck #240
    R2.*3 \pageBreak | % 243
    R2.*6 \bar "||"
    \pageBreak | % 249
    R2.*9 \pageBreak | % 258
    R2.*7 \pageBreak | % 265
    R2.*6 | % 271
    \stemUp a,,2 _\f \stemUp c4 -. \pageBreak | % 272
    \stemUp e4 -. \stemUp a2 -> | % 273
    \stemUp a2 ^ "a 2" _\f _\< \stemDown c4 -. | % 274
    \stemDown e4 -. \stemDown a2 -> | % 275
    \stemDown c2 -> _\! _\ff \stemDown a4 -. | % 276
    \stemDown e4 -. \stemDown c2 -> \pageBreak | % 277
    \stemUp fis,8 \stemUp fis8 \stemUp fis4 -. \stemUp c4 -. | % 278
    \stemUp c4 -. \stemUp fis8 \stemUp fis8 \stemUp fis4 | % 279
    \stemUp c4 -. \stemUp c4 -. \stemUp fis8 \stemUp fis8 |
    \barNumberCheck #280
    \stemUp fis4 -. \stemUp c4 -. \stemUp c4 -. | % 281
    \stemDown d'2. ~ _\fff | % 282
    \stemDown d2. ~ \pageBreak | % 283
    \stemDown d2. ~ | % 284
    \stemDown d2. ~ | % 285
    \stemDown d4 r4 r4 | % 286
    R2.*2 \pageBreak | % 288
    R2. | % 289
    \stemUp g,,2. ~ _\p | \barNumberCheck #290
    \stemUp g2. ~ | % 291
    \stemUp g2. ~ | % 292
    \stemUp g2. | % 293
    \stemUp g2. ~ _\pp \pageBreak | % 294
    \stemUp g2. ~ | % 295
    \stemUp g2. ~ | % 296
    \stemUp g2. ~ | % 297
    \stemUp g2. ~ | % 298
    \stemUp g4 r4 r4 | % 299
    R2. | \barNumberCheck #300
    \stemDown bes'4 _\ff r4 r4 \bar "|."
    }

PartPSevenVoiceOne =  \relative e {
    \repeat volta 2 {
        \clef "bass" \time 3/4 \key g \major | % 1
        r8 \stemDown e8 _\f \stemDown e2 ~ | % 2
        \stemDown e2. | % 3
        r8 \stemUp b8 \stemUp b2 ~ | % 4
        \stemUp b2. \bar "||"
        R2.*3 \pageBreak | % 8
        R2.*7 \pageBreak | % 15
        R2.*6 \pageBreak | % 21
        R2.*5 \pageBreak | % 26
        R2.*5 \pageBreak | % 31
        R2.*5 \pageBreak | % 36
        R2.*5 | % 41
        r4 \stemUp g2 -> _\ff \pageBreak | % 42
        \stemUp g2 -> \stemUp g4 | % 43
        \stemUp a2 -> \stemUp a4 | % 44
        \stemUp g2 -> \stemUp g4 | % 45
        \stemUp g2 -> \stemUp g4 | % 46
        \stemUp g2 -> \stemUp g4 \pageBreak | % 47
        \stemUp a2 -> \stemUp a4 | % 48
        \stemUp g2 -> \stemUp g4 | % 49
        \stemUp g4 \stemDown e''2 -> ^ "a 2" | \barNumberCheck #50
        \stemDown d2 -> \stemDown cis4 ~ -> | % 51
        \stemDown cis4 \stemDown c2 -> | % 52
        \stemDown b2 -> \stemDown e,4 ~ \pageBreak | % 53
        \stemDown e4 ^ "a 2" \stemDown e'2 -> | % 54
        \stemDown d2 -> \stemDown cis4 ~ -> | % 55
        \stemDown cis4 \stemDown c2 -> | % 56
        \stemDown b8 \stemDown a8 \stemDown g4 \stemDown c4 | % 57
        \stemDown b8 \stemDown a8 \stemDown g4 \stemDown c4 | % 58
        \stemDown b8 \stemDown a8 \stemDown g4 \stemDown c4 | % 59
        \stemDown b8 \stemDown a8 \stemDown g4 r4 }
    \pageBreak | \barNumberCheck #60
    R2.*4 | % 64
    r4 \stemDown e'8 ( ^\p \stemDown c8 \stemDown b8 ) r8 | % 65
    r4 \stemDown e8 ( \stemDown c8 \stemDown b8 ) r8 | % 66
    r4 \stemDown e8 ( \stemDown c8 \stemDown b8 ) r8 \pageBreak | % 67
    r4 \stemDown e8 ( \stemDown cis8 \stemDown b8 ) r8 \bar "||"
    \key e \major r4 \stemDown e8 ( ^\pp \stemDown cis8 \stemDown b4 ~ | % 69
    \stemDown b2. ) ~ | \barNumberCheck #70
    \stemDown b2. ~ | % 71
    \stemDown b4 r4 r4 \pageBreak | % 72
    R2.*4 | % 76
    r4 \stemDown e8 ( ^\p \stemDown cis8 ) \stemDown b4 ~
    \pageBreak | % 77
    \stemDown b2. ~ | % 78
    \stemDown b2. ~ | % 79
    \stemDown b2. ~ | \barNumberCheck #80
    \stemDown b4 r4 r4 | % 81
    R2. \pageBreak | % 82
    R2.*5 \pageBreak | % 87
    R2.*5 \pageBreak | % 92
    \stemDown gis8 ( ^ "a 2" _\p \stemDown b8 ) \stemDown b2 ~ | % 93
    \stemDown b2 \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( \stemDown b8 _\< \stemDown fis8 }
    | % 94
    \stemDown e2 \stemDown fis4 ) | % 95
    \stemDown gis8 ( \stemDown b8 \stemDown b2 ~ | % 96
    \stemDown b8 ) _\! \stemDown e8 ( _\f \stemDown dis8 \stemDown cis8
    ) \stemDown b4 ~ | % 97
    \stemDown b8 \stemDown gis8 ( \stemDown fis8 \stemDown gis8
    \stemDown b8 _\markup{ \italic {dim.} } _\> \stemDown gis8 | % 98
    \stemDown fis8 \stemDown gis8 \stemDown e2 ) \pageBreak | % 99
    R2.*8 \pageBreak | % 107
    \stemDown d'2. ~ _\! _\p | % 108
    \stemDown d2. | % 109
    \stemDown c2. ~ | \barNumberCheck #110
    \stemDown c2 \stemDown es4 | % 111
    \stemDown des2. ~ | % 112
    \stemDown des2 \stemDown e4 \pageBreak | % 113
    \stemDown d2. ( | % 114
    \stemDown dis2. ) _\markup{ \italic {cresc.} } | % 115
    \stemDown e2. _\< | % 116
    \stemDown f2. | % 117
    \stemDown fis8 _\! r8 \stemUp b,,2 ~ ^^ _\f | % 118
    \stemUp b2. \pageBreak | % 119
    \stemUp b4. \stemUp c8 _ "[" _\< \stemDown dis4 | \barNumberCheck
    #120
    \stemDown fis4 \stemDown a2 -> | % 121
    \stemDown e'4. -> _\! _ "]" \stemDown dis8 \stemDown c4 | % 122
    \stemDown b4 -. \stemDown fis4 -. \stemDown b4 -. \bar "||"
    \key g \major \stemDown e2 -> _\ff ^ "[" ^ "]" \stemDown d4 ~ -> | % 124
    \stemDown d4 \stemDown cis2 -> | % 125
    \stemDown c2 \stemDown fis,4 -. \pageBreak | % 126
    \stemDown b4 \stemDown g4 \stemDown e4 | % 127
    \stemDown e'2 -> \stemDown d4 ~ -> | % 128
    \stemDown d4 \stemDown cis2 -> | % 129
    \stemDown c2 \stemDown a4 | \barNumberCheck #130
    \stemDown e4 \stemDown e4 \stemDown a4 | % 131
    \stemDown e4 \stemDown e4 \stemDown a4 | % 132
    \stemDown e4 \stemDown e4 \stemDown a4 \pageBreak | % 133
    \stemDown e4 \stemDown e4 \stemDown a4 | % 134
    \stemDown e4 r4 r4 | % 135
    \stemDown a4 r4 r4 | % 136
    \stemDown e4 r4 r4 | % 137
    \stemDown a4 r4 r4 | % 138
    \stemDown e4 r4 r4 | % 139
    R2. | \barNumberCheck #140
    \stemDown e4 r4 r4 | % 141
    R2. \bar "||"
    \pageBreak | % 142
    R2.*2 | % 144
    \stemDown c'2. ( -> ^\p ^\> | % 145
    \stemDown b4 ) r4 ^\! r4 | % 146
    \stemDown e,2. ~ _\pp _\> | % 147
    \stemDown e4 r4 _\! r4 | % 148
    \stemUp c2. ( | % 149
    \stemUp b4 ) r4 r4 \pageBreak | \barNumberCheck #150
    R2.*8 \pageBreak | % 158
    R2.*2 | \barNumberCheck #160
    r4 \stemDown as'2 ~ ^\p | % 161
    \stemDown as2. ~ | % 162
    \stemDown as2 r4 | % 163
    R2.*3 \pageBreak | % 166
    R2.*8 \pageBreak | % 174
    R2.*2 \repeat volta 2 {
        | % 176
        \clef "tenor" \stemDown e'4. _\p \stemDown e8 \stemDown e8 -. r8
        | % 177
        \stemDown e4. \stemDown e8 \stemDown e8 -. r8 | % 178
        \stemDown e2. ~ | % 179
        \stemDown e2 \stemDown e4 \pageBreak | \barNumberCheck #180
        \stemDown e4. \stemDown e8 \stemDown e4 | % 181
        \stemDown f4. \stemDown f8 \stemDown f4 | % 182
        \stemDown e2. ~ | % 183
        \stemDown e2 \stemDown e4 | % 184
        \stemDown e4. \stemDown e8 \stemDown e8 r8 | % 185
        \stemDown e4. \stemDown e8 \stemDown e8 r8 \pageBreak | % 186
        \stemDown e2. ~ | % 187
        \stemDown e2 \stemDown e4 | % 188
        \stemDown e4. _\< \stemDown e8 \stemDown e4 | % 189
        \stemDown f2 _\! _\f \stemDown e4 _\> | \barNumberCheck #190
        \stemDown e2. ~ | % 191
        \stemDown e4 ~ _\! _\p r4 r4 }
    | % 192
    \stemDown e4 r4 r4 \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
        R2.*7 \pageBreak | \barNumberCheck #200
        R2.*6 \pageBreak | % 206
        R2.*7 \pageBreak | % 213
        R2.*8 \pageBreak | % 221
        R2.*3 | % 224
        \clef "bass" \stemDown e4. _\p \stemDown e8 \stemDown e8 r8 | % 225
        \stemDown e4. \stemDown e8 \stemDown e8 r8 | % 226
        \stemDown e2. ~ \pageBreak | % 227
        \stemDown e2 \stemDown e4 | % 228
        \stemDown e4. \stemDown e8 \stemDown e8 r8 | % 229
        \stemDown f4. \stemDown f8 \stemDown f8 r8 | \barNumberCheck
        #230
        \stemDown e2. ~ | % 231
        \stemDown e2 \stemDown e4 \pageBreak | % 232
        \stemDown e4. \stemDown e8 \stemDown e8 r8 | % 233
        \stemDown e4. \stemDown e8 \stemDown e8 r8 | % 234
        \stemDown e2. ~ | % 235
        \stemDown e2 \stemDown e4 | % 236
        \stemDown e4. \stemDown e8 \stemDown e4 \pageBreak | % 237
        \stemDown d2 \stemDown e4 | % 238
        \stemDown e2. ~ _\fz | % 239
        \stemDown e4 r4 r4 }
    | \barNumberCheck #240
    R2.*3 \pageBreak | % 243
    R2.*6 \bar "||"
    \pageBreak | % 249
    R2.*9 \pageBreak | % 258
    R2.*7 \pageBreak | % 265
    R2.*6 | % 271
    \stemDown fis,2 _\f ^ "a 2" \stemDown a4 -. \pageBreak | % 272
    \stemDown cis4 -. ^ "a 2" \stemDown fis2 -> | % 273
    R2.*4 \pageBreak | % 277
    \stemDown dis8 ^ "a 2" \stemDown dis8 \stemDown dis4 -. \stemDown a4
    -. | % 278
    \stemDown a4 -. \stemDown dis8 \stemDown dis8 \stemDown dis4 | % 279
    \stemDown a4 -. \stemDown a4 -. \stemDown dis8 \stemDown dis8 |
    \barNumberCheck #280
    \stemDown dis4 -. \stemDown a4 -. \stemDown a4 -. | % 281
    \stemDown e2. ~ _\fff | % 282
    \stemDown e2. ~ \pageBreak | % 283
    \stemDown e2. ~ | % 284
    \stemDown e2. ~ | % 285
    \stemDown e2. ~ _\mf | % 286
    \stemDown e2. ~ | % 287
    \stemDown e2. ~ _\p _\> \pageBreak | % 288
    \stemDown e2. ~ _\! _\pp | % 289
    \stemDown e4 r4 r4 | \barNumberCheck #290
    R2.*4 \pageBreak | % 294
    R2.*6 | \barNumberCheck #300
    \stemDown e4 _\ff r4 r4 \bar "|."
    }

PartPEightVoiceOne =  \relative e, {
    \repeat volta 2 {
        \clef "bass" \time 3/4 \key g \major | % 1
        r8 \stemUp e8 _\f \stemUp e2 ~ | % 2
        \stemUp e2. | % 3
        r8 \stemUp b8 \stemUp b2 ~ | % 4
        \stemUp b2. \bar "||"
        R2.*3 \pageBreak | % 8
        R2.*7 \pageBreak | % 15
        R2.*6 \pageBreak | % 21
        R2.*5 \pageBreak | % 26
        R2.*5 \pageBreak | % 31
        R2.*5 \pageBreak | % 36
        R2.*5 | % 41
        r4 \stemUp e2 -> _\ff \pageBreak | % 42
        \stemUp e2 -> \stemUp e4 | % 43
        \stemUp e2 -> \stemUp e4 | % 44
        \stemUp e2 -> \stemUp e4 | % 45
        \stemUp e2 -> \stemUp e4 | % 46
        \stemUp e2 -> \stemUp e4 \pageBreak | % 47
        \stemUp e2 -> \stemUp e4 | % 48
        \stemUp e2 -> \stemUp e4 | % 49
        \stemUp e4 \stemDown e''2 -> ^ "a 2" | \barNumberCheck #50
        \stemDown d2 -> \stemDown cis4 ~ -> | % 51
        \stemDown cis4 \stemDown c2 -> | % 52
        \stemDown b2 -> \stemDown e,4 ~ \pageBreak | % 53
        \stemDown e4 ^ "a 2" \stemDown e'2 -> | % 54
        \stemDown d2 -> \stemDown cis4 ~ -> | % 55
        \stemDown cis4 \stemDown c2 -> | % 56
        \stemDown g8 \stemDown fis8 \stemDown e4 \stemDown a4 | % 57
        \stemDown g8 \stemDown fis8 \stemDown e4 \stemDown a4 | % 58
        \stemDown g8 \stemDown fis8 \stemDown e4 \stemDown a4 | % 59
        \stemDown g8 \stemDown fis8 \stemDown e4 r4 }
    \pageBreak | \barNumberCheck #60
    R2.*4 | % 64
    r4 \stemDown e'8 ( ^\p \stemDown c8 \stemDown b8 ) r8 | % 65
    r4 \stemDown e8 ( \stemDown c8 \stemDown b8 ) r8 | % 66
    r4 \stemDown e8 ( \stemDown c8 \stemDown b8 ) r8 \pageBreak | % 67
    r4 \stemDown e8 ( \stemDown cis8 \stemDown b8 ) r8 \bar "||"
    \key e \major r4 \stemDown e8 ( ^\pp \stemDown cis8 \stemDown b4 ~ | % 69
    \stemDown b2. ) ~ | \barNumberCheck #70
    \stemDown b2. ~ | % 71
    \stemDown b4 r4 r4 \pageBreak | % 72
    R2.*4 | % 76
    r4 \stemDown e8 ( ^\p \stemDown cis8 ) \stemDown b4 ~
    \pageBreak | % 77
    \stemDown b2. ~ | % 78
    \stemDown b2. ~ | % 79
    \stemDown b2. ~ | \barNumberCheck #80
    \stemDown b4 r4 r4 | % 81
    R2. \pageBreak | % 82
    R2.*5 \pageBreak | % 87
    R2.*5 \pageBreak | % 92
    \stemDown gis8 ( ^ "a 2" _\p \stemDown b8 ) \stemDown b2 ~ | % 93
    \stemDown b2 \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( \stemDown b8 _\< \stemDown fis8 }
    | % 94
    \stemDown e2 \stemDown fis4 ) | % 95
    \stemDown gis8 ( \stemDown b8 \stemDown b2 ~ | % 96
    \stemDown b8 ) _\! \stemDown e8 ( _\f \stemDown dis8 \stemDown cis8
    ) \stemDown b4 ~ | % 97
    \stemDown b8 \stemDown gis8 ( \stemDown fis8 \stemDown gis8
    \stemDown b8 _\markup{ \italic {dim.} } _\> \stemDown gis8 | % 98
    \stemDown fis8 \stemDown gis8 \stemDown e2 ) \pageBreak | % 99
    R2.*8 \pageBreak | % 107
    \stemDown gis2. ~ _\! _\p | % 108
    \stemDown gis2. | % 109
    \stemDown a2. ~ | \barNumberCheck #110
    \stemDown a2 \stemDown a4 | % 111
    \stemDown bes2. ~ | % 112
    \stemDown bes2 \stemDown ais4 \pageBreak | % 113
    \stemDown b2. ( | % 114
    \stemDown bis2. ) _\markup{ \italic {cresc.} } | % 115
    \stemDown cis2. _\< | % 116
    \stemDown d2. | % 117
    \stemDown dis8 _\! r8 \stemUp b,,2 ~ ^^ _\f | % 118
    \stemUp b2. \pageBreak | % 119
    \stemUp b4. \stemUp c8 _ "[" _\< \stemUp dis4 | \barNumberCheck #120
    \stemUp fis4 \stemUp a2 -> | % 121
    \stemDown e'4. -> _\! _ "]" \stemDown dis8 \stemUp c4 | % 122
    \stemUp b4 -. \stemUp fis4 -. \stemUp b4 -. \bar "||"
    \key g \major \stemDown e2 -> _\ff ^ "[" ^ "]" \stemDown d4 ~ -> | % 124
    \stemDown d4 \stemUp cis2 -> | % 125
    \stemUp c2 \stemUp fis,4 -. \pageBreak | % 126
    \stemUp b4 \stemUp g4 \stemUp e4 | % 127
    \stemDown e'2 -> \stemDown d4 ~ -> | % 128
    \stemDown d4 \stemUp cis2 -> | % 129
    \stemUp c2 \stemUp a4 | \barNumberCheck #130
    \stemUp e4 \stemUp e4 \stemUp a4 | % 131
    \stemUp e4 \stemUp e4 \stemUp a4 | % 132
    \stemUp e4 \stemUp e4 \stemUp a4 \pageBreak | % 133
    \stemUp e4 \stemUp e4 \stemUp a4 | % 134
    \stemUp e4 r4 r4 | % 135
    \stemUp a4 r4 r4 | % 136
    \stemUp e4 r4 r4 | % 137
    \stemUp a4 r4 r4 | % 138
    \stemUp e4 r4 r4 | % 139
    R2. | \barNumberCheck #140
    \stemUp e4 r4 r4 | % 141
    R2. \bar "||"
    \pageBreak | % 142
    R2.*2 | % 144
    \stemDown c''2. ( -> ^\p ^\> | % 145
    \stemDown b4 ) r4 ^\! r4 | % 146
    \stemDown e,2. ~ _\pp _\> | % 147
    \stemDown e4 r4 _\! r4 | % 148
    \stemUp c2. ( | % 149
    \stemUp b4 ) r4 r4 \pageBreak | \barNumberCheck #150
    R2.*8 \pageBreak | % 158
    R2.*2 | \barNumberCheck #160
    r4 \stemDown as'2 ~ ^\p | % 161
    \stemDown as2. ~ | % 162
    \stemDown as2 r4 | % 163
    R2.*3 \pageBreak | % 166
    R2.*8 \pageBreak | % 174
    R2.*2 \repeat volta 2 {
        | % 176
        \clef "tenor" \stemDown c4. _\p \stemDown c8 \stemDown c8 -. r8
        | % 177
        \stemDown c4. \stemDown c8 \stemDown c8 -. r8 | % 178
        \stemDown c2. ~ | % 179
        \stemDown c2 \stemDown c4 \pageBreak | \barNumberCheck #180
        \stemDown c4. \stemDown c8 \stemDown c4 | % 181
        \stemDown d4. \stemDown d8 \stemDown d4 | % 182
        \stemDown c2. ~ | % 183
        \stemDown c2 \stemDown c4 | % 184
        \stemDown c4. \stemDown c8 \stemDown c8 r8 | % 185
        \stemDown c4. \stemDown c8 \stemDown c8 r8 \pageBreak | % 186
        \stemDown c2. ~ | % 187
        \stemDown c2 \stemDown c4 | % 188
        \stemDown b4. _\< \stemDown b8 \stemDown b4 | % 189
        \stemDown b2 _\! _\f \stemDown c4 _\> | \barNumberCheck #190
        \stemDown c2. ~ | % 191
        \stemDown c4 ~ _\! _\p r4 r4 }
    | % 192
    \stemDown c4 r4 r4 \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
        R2.*7 \pageBreak | \barNumberCheck #200
        R2.*6 \pageBreak | % 206
        R2.*7 \pageBreak | % 213
        R2.*8 \pageBreak | % 221
        R2.*3 | % 224
        \clef "bass" \stemDown c4. _\p \stemDown c8 \stemDown c8 r8 | % 225
        \stemDown c4. \stemDown c8 \stemDown c8 r8 | % 226
        \stemDown c2. ~ \pageBreak | % 227
        \stemDown c2 \stemDown c4 | % 228
        \stemDown c4. \stemDown c8 \stemDown c8 r8 | % 229
        \stemDown d4. \stemDown d8 \stemDown b8 r8 | \barNumberCheck
        #230
        \stemDown c2. ~ | % 231
        \stemDown c2 \stemDown c4 \pageBreak | % 232
        \stemDown c4. \stemDown c8 \stemDown c8 r8 | % 233
        \stemDown c4. \stemDown c8 \stemDown c8 r8 | % 234
        \stemDown c2. ~ | % 235
        \stemDown c2 \stemDown c4 | % 236
        \stemDown e,4. \stemDown e8 \stemDown e4 \pageBreak | % 237
        \stemDown g2 \stemDown c4 | % 238
        \stemDown c2. ~ _\fz | % 239
        \stemDown c4 r4 r4 }
    | \barNumberCheck #240
    R2.*3 \pageBreak | % 243
    R2.*6 \bar "||"
    \pageBreak | % 249
    R2.*9 \pageBreak | % 258
    R2.*7 \pageBreak | % 265
    R2.*6 | % 271
    \stemDown fis,2 _\f ^ "a 2" \stemDown a4 -. \pageBreak | % 272
    \stemDown cis4 -. ^ "a 2" \stemDown fis2 -> | % 273
    R2.*4 \pageBreak | % 277
    \stemDown dis8 ^ "a 2" \stemDown dis8 \stemDown dis4 -. \stemDown a4
    -. | % 278
    \stemDown a4 -. \stemDown dis8 \stemDown dis8 \stemDown dis4 | % 279
    \stemDown a4 -. \stemDown a4 -. \stemDown dis8 \stemDown dis8 |
    \barNumberCheck #280
    \stemDown dis4 -. \stemDown a4 -. \stemDown a4 -. | % 281
    \stemUp e,2. ~ _\fff | % 282
    \stemUp e2. ~ \pageBreak | % 283
    \stemUp e2. ~ | % 284
    \stemUp e2. ~ | % 285
    \stemUp e2. ~ _\mf | % 286
    \stemUp e2. ~ | % 287
    \stemUp e2. ~ _\p _\> \pageBreak | % 288
    \stemUp e2. ~ _\! _\pp | % 289
    \stemUp e4 r4 r4 | \barNumberCheck #290
    R2.*4 \pageBreak | % 294
    R2.*6 | \barNumberCheck #300
    \stemUp e4 _\ff r4 r4 \bar "|."
    }

PartPNineVoiceOne =  \relative c'' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key c \none \transposition e | % 1
        r8 \stemDown c8 _\f \stemDown c2 ~ | % 2
        \stemDown c2. | % 3
        r8 \stemUp g8 \stemUp g2 ~ | % 4
        \stemUp g2. \bar "||"
        R2.*3 \pageBreak | % 8
        R2.*7 \pageBreak | % 15
        R2.*6 \pageBreak | % 21
        R2.*5 \pageBreak | % 26
        R2.*5 \pageBreak | % 31
        R2.*5 \pageBreak | % 36
        R2.*5 | % 41
        r4 ^ "a 2" \stemDown c2 -> _\ff \pageBreak | % 42
        \stemDown bes2 -> ^ "a 2" \stemUp a4 ~ -> | % 43
        \stemUp a4 \stemUp as2 -> | % 44
        \stemUp g2 -> \stemUp c,4 ~ | % 45
        \stemUp c4 \stemDown c'2 -> | % 46
        \stemDown bes2 -> \stemUp a4 ~ -> \pageBreak | % 47
        \stemUp a4 ^ "a 2" \stemUp as2 -> | % 48
        \stemUp g2 \stemUp c,4 ~ | % 49
        \stemUp c4 \stemDown es'2 -> | \barNumberCheck #50
        \stemDown es2 \stemDown f4 ~ | % 51
        \stemDown f4 \stemDown f2 | % 52
        \stemDown es2 \stemDown es4 ~ \pageBreak | % 53
        \stemDown es4 \stemDown es2 | % 54
        \stemDown es2 \stemDown f4 ~ | % 55
        \stemDown f4 \stemDown f2 | % 56
        \stemDown c8 \stemDown c8 \stemDown c4 \stemDown d4 | % 57
        \stemDown c8 \stemDown c8 \stemDown c4 \stemDown d4 | % 58
        \stemDown c8 \stemDown c8 \stemDown c4 \stemDown d4 | % 59
        \stemDown c4 r4 r4 }
    \pageBreak | \barNumberCheck #60
    R2.*7 \pageBreak | % 67
    R2. \bar "||"
    \key c \major R2.*4 \pageBreak | % 72
    R2.*5 \pageBreak | % 77
    R2.*5 \pageBreak | % 82
    R2.*5 \pageBreak | % 87
    R2.*5 \pageBreak | % 92
    \stemDown c8 ^\p \stemDown c8 \stemDown c8 \stemDown c8 \stemDown b8
    \stemDown b8 | % 93
    \stemDown c8 \stemDown c8 \stemDown c8 \stemDown c8 \stemDown b8
    \stemDown b8 | % 94
    \stemDown c8 \stemDown c8 \stemDown c8 \stemDown c8 \stemDown b8
    \stemDown b8 | % 95
    \stemDown c8 \stemDown c8 \stemDown c8 \stemDown c8 \stemDown b8
    \stemDown b8 | % 96
    \stemDown c8 ^\mf \stemDown c8 \stemDown c8 \stemDown c8 \stemDown b8
    \stemDown b8 | % 97
    \stemDown c8 \stemDown c8 \stemDown c8 \stemDown c8 \stemDown b8
    ^\markup{ \italic {dim.} } ^\> \stemDown b8 | % 98
    \stemDown b8 \stemDown b8 \stemDown c8 \stemDown c8 \stemDown c8
    \stemDown c8 \pageBreak | % 99
    R2.*8 \pageBreak | % 107
    R2.*6 \pageBreak | % 113
    \stemDown bes2 ^\! _\mf \stemDown des4 | % 114
    \stemDown b2 _\< \stemDown d4 | % 115
    \stemDown c2 \stemDown es4 | % 116
    \stemDown cis2 \stemDown e4 _\! | % 117
    \stemDown d4 \stemDown f2 ~ ^^ _\f | % 118
    \stemDown f2 \stemDown e4 ~ \pageBreak | % 119
    \stemDown e4 \stemDown d4 _\< \stemDown f8 \stemDown f8 |
    \barNumberCheck #120
    \stemDown f4 \stemDown f8 \stemDown f8 \stemDown f4 | % 121
    \stemDown f8 _\! \stemDown f8 \stemDown f4 \stemDown f8 \stemDown f8
    | % 122
    \stemDown f4 \stemDown f8 \stemDown f8 \stemDown f4 \bar "||"
    \key c \none \stemDown es4 _\ff \stemDown c2 -> | % 124
    \stemDown c2 -> \stemDown c4 ~ -> | % 125
    \stemDown c4 \stemDown c2 -> \pageBreak | % 126
    \stemDown c2 \stemDown c4 ~ | % 127
    \stemDown c4 \stemDown c2 -> | % 128
    \stemDown c2 -> \stemDown c4 ~ | % 129
    \stemDown c4 -> \stemDown c2 -> | \barNumberCheck #130
    \stemDown es4 r4 \stemDown d4 | % 131
    \stemDown es4 r4 \stemDown d4 | % 132
    \stemDown es4 r4 \stemDown d4 \pageBreak | % 133
    \stemDown es4 r4 \stemDown d4 | % 134
    \stemDown es4 r4 r4 | % 135
    \stemDown es4 r4 r4 | % 136
    \stemDown es4 r4 r4 | % 137
    \stemDown es4 r4 r4 | % 138
    \stemDown es4 r4 r4 | % 139
    R2. | \barNumberCheck #140
    \stemDown es4 r4 r4 | % 141
    R2. \bar "||"
    \pageBreak | % 142
    R2.*8 \pageBreak | \barNumberCheck #150
    R2.*8 \pageBreak | % 158
    R2.*8 \pageBreak | % 166
    R2.*8 \pageBreak | % 174
    R2.*2 \repeat volta 2 {
        | % 176
        R2.*4 \pageBreak | \barNumberCheck #180
        R2.*6 \pageBreak | % 186
        R2.*6 }
    | % 192
    R2. \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
        R2.*7 \pageBreak | \barNumberCheck #200
        R2.*6 \pageBreak | % 206
        R2.*7 \pageBreak | % 213
        R2.*8 \pageBreak | % 221
        R2.*3 | % 224
        \stemDown es4. _\p \stemDown es8 \stemDown es8 r8 | % 225
        \stemDown es4. \stemDown es8 \stemDown es8 r8 | % 226
        \stemDown es2. ~ \pageBreak | % 227
        \stemDown es2 \stemDown es4 | % 228
        \stemDown es4. \stemDown es8 \stemDown es8 r8 | % 229
        \stemDown es4. \stemDown es8 \stemDown es8 r8 | \barNumberCheck
        #230
        \stemDown es2. ~ | % 231
        \stemUp es2 \stemDown es4 \pageBreak | % 232
        \stemDown es4. \stemDown es8 \stemDown es4 | % 233
        \stemDown es4. \stemDown es8 \stemDown es4 | % 234
        \stemDown es2. ~ | % 235
        \stemDown es2 \stemDown es4 | % 236
        \stemDown es4. \stemDown es8 \stemDown es4 \pageBreak | % 237
        \stemDown es2 \stemDown es4 | % 238
        \stemDown es2. ~ _\fz | % 239
        \stemDown es4 r4 r4 }
    | \barNumberCheck #240
    R2.*3 \pageBreak | % 243
    R2.*2 | % 245
    \stemDown b2. _\p _\< | % 246
    \stemDown d2. _\! _\fz _\< | % 247
    \stemDown d2 \stemDown f4 -. _\! _\f | % 248
    \stemDown f2. \bar "||"
    \pageBreak | % 249
    R2.*9 \pageBreak | % 258
    R2.*3 | % 261
    \stemUp cis,2 _\f ^ "a 2" _\< \stemUp e4 -. | % 262
    \stemUp a4 -. \stemDown cis2 | % 263
    \stemDown e2 -> _\! _\ff \stemDown cis4 -. | % 264
    \stemDown b4 -. \stemUp a2 \pageBreak | % 265
    R2.*4 | % 269
    \stemUp d,2 _\ff ^ "a 2" _\< \stemUp f4 -. | \barNumberCheck #270
    \stemUp a4 -. \stemDown d2 | % 271
    R2. \pageBreak | % 272
    R2. | % 273
    \stemUp d,2 _\! _\f ^ "a 2" _\< \stemUp f4 -. | % 274
    \stemUp a4 -. \stemDown d2 -> | % 275
    \stemDown f2 -> _\! \stemDown d4 -. | % 276
    \stemUp a4 -. \stemUp f2 -> \pageBreak | % 277
    \stemDown f'2. ~ -> _\ff | % 278
    \stemDown f2. | % 279
    \stemDown f2. ~ | \barNumberCheck #280
    \stemDown f2. | % 281
    \stemDown e2. ~ _\fff | % 282
    \stemDown e2. ~ \pageBreak | % 283
    \stemDown e2. ~ | % 284
    \stemDown e2. | % 285
    \stemUp g,2. ~ _\mf | % 286
    \stemUp g2. ~ | % 287
    \stemUp g2. ~ _\p _\> \pageBreak | % 288
    \stemUp g2. ~ _\! _\pp | % 289
    \stemUp g4 r4 r4 | \barNumberCheck #290
    R2.*4 \pageBreak | % 294
    R2.*6 | \barNumberCheck #300
    \stemDown es'4 _\ff r4 r4 \bar "|."
    }

PartPOneZeroVoiceOne =  \relative c' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key es \major \transposition e | % 1
        r8 \stemUp c8 _\f \stemUp c2 ~ | % 2
        \stemUp c2. | % 3
        r8 \stemUp g8 \stemUp g2 ~ | % 4
        \stemUp g2. \bar "||"
        R2.*3 \pageBreak | % 8
        R2.*7 \pageBreak | % 15
        R2.*6 \pageBreak | % 21
        R2.*5 \pageBreak | % 26
        R2.*5 \pageBreak | % 31
        R2.*5 \pageBreak | % 36
        R2.*5 | % 41
        r4 ^ "a 2" \stemDown c'2 -> _\ff \pageBreak | % 42
        \stemDown bes2 -> ^ "a 2" \stemUp a4 ~ -> | % 43
        \stemUp a4 \stemUp as2 -> | % 44
        \stemUp g2 -> \stemUp c,4 ~ | % 45
        \stemUp c4 \stemDown c'2 -> | % 46
        \stemDown bes2 -> \stemUp a4 ~ -> \pageBreak | % 47
        \stemUp a4 ^ "a 2" \stemUp as2 -> | % 48
        \stemUp g2 \stemUp c,4 ~ | % 49
        \stemUp c4 \stemDown c'2 -> | \barNumberCheck #50
        \stemDown c2 \stemDown c4 ~ | % 51
        \stemDown c4 \stemDown c2 | % 52
        \stemDown c2 \stemDown c4 ~ \pageBreak | % 53
        \stemDown c4 \stemDown c2 | % 54
        \stemDown c2 \stemDown c4 ~ | % 55
        \stemDown c4 \stemDown c2 | % 56
        \stemDown c8 \stemDown c8 \stemDown c4 \stemDown d4 | % 57
        \stemDown c8 \stemDown c8 \stemDown c4 \stemDown d4 | % 58
        \stemDown c8 \stemDown c8 \stemDown c4 \stemDown d4 | % 59
        \stemDown c4 r4 r4 }
    \pageBreak | \barNumberCheck #60
    R2.*7 \pageBreak | % 67
    R2. \bar "||"
    \key c \major R2.*4 \pageBreak | % 72
    R2.*5 \pageBreak | % 77
    R2.*5 \pageBreak | % 82
    R2.*5 \pageBreak | % 87
    R2.*5 \pageBreak | % 92
    \stemDown c8 ^\p \stemDown c8 \stemDown c8 \stemDown c8 \stemDown b8
    \stemDown b8 | % 93
    \stemDown c8 \stemDown c8 \stemDown c8 \stemDown c8 \stemDown b8
    \stemDown b8 | % 94
    \stemDown c8 \stemDown c8 \stemDown c8 \stemDown c8 \stemDown b8
    \stemDown b8 | % 95
    \stemDown c8 \stemDown c8 \stemDown c8 \stemDown c8 \stemDown b8
    \stemDown b8 | % 96
    \stemDown c8 ^\mf \stemDown c8 \stemDown c8 \stemDown c8 \stemDown b8
    \stemDown b8 | % 97
    \stemDown c8 \stemDown c8 \stemDown c8 \stemDown c8 \stemDown b8
    ^\markup{ \italic {dim.} } ^\> \stemDown b8 | % 98
    \stemDown b8 \stemDown b8 \stemDown c8 \stemDown c8 \stemDown c8
    \stemDown c8 \pageBreak | % 99
    R2.*8 \pageBreak | % 107
    R2.*6 \pageBreak | % 113
    \stemUp g2 ^\! _\mf \stemUp g4 | % 114
    \stemUp gis2 _\< \stemUp gis4 | % 115
    \stemUp a2 \stemUp a4 | % 116
    \stemUp ais2 \stemUp ais4 _\! | % 117
    \stemDown b4 \stemDown b2 ~ ^^ _\f | % 118
    \stemDown b2 \stemDown b4 ~ \pageBreak | % 119
    \stemDown b4 \stemDown b4 _\< \stemDown d8 \stemDown d8 |
    \barNumberCheck #120
    \stemDown d4 \stemDown d8 \stemDown d8 \stemDown d4 | % 121
    \stemDown d8 _\! \stemDown d8 \stemDown d4 \stemDown d8 \stemDown d8
    | % 122
    \stemDown d4 \stemDown d8 \stemDown d8 \stemDown d4 \bar "||"
    \key es \major \stemDown c4 _\ff \stemUp c,2 -> | % 124
    \stemUp c2 -> \stemUp c4 ~ -> | % 125
    \stemUp c4 \stemUp c2 -> \pageBreak | % 126
    \stemUp c2 \stemUp c4 ~ | % 127
    \stemUp c4 \stemUp c2 -> | % 128
    \stemUp c2 -> \stemUp c4 ~ | % 129
    \stemUp c4 -> \stemUp c2 -> | \barNumberCheck #130
    \stemDown c'4 r4 \stemDown c4 | % 131
    \stemDown c4 r4 \stemDown c4 | % 132
    \stemDown c4 r4 \stemDown c4 \pageBreak | % 133
    \stemDown c4 r4 \stemDown c4 | % 134
    \stemDown c4 r4 r4 | % 135
    \stemDown c4 r4 r4 | % 136
    \stemDown c4 r4 r4 | % 137
    \stemDown c4 r4 r4 | % 138
    \stemDown c4 r4 r4 | % 139
    R2. | \barNumberCheck #140
    \stemDown c4 r4 r4 | % 141
    R2. \bar "||"
    \pageBreak | % 142
    R2.*8 \pageBreak | \barNumberCheck #150
    R2.*8 \pageBreak | % 158
    R2.*8 \pageBreak | % 166
    R2.*8 \pageBreak | % 174
    R2.*2 \repeat volta 2 {
        | % 176
        R2.*4 \pageBreak | \barNumberCheck #180
        R2.*6 \pageBreak | % 186
        R2.*6 }
    | % 192
    R2. \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
        R2.*7 \pageBreak | \barNumberCheck #200
        R2.*6 \pageBreak | % 206
        R2.*7 \pageBreak | % 213
        R2.*8 \pageBreak | % 221
        R2.*3 | % 224
        \stemUp es,4. _\p \stemUp es8 \stemUp es8 r8 | % 225
        \stemUp es4. \stemUp es8 \stemUp es8 r8 | % 226
        \stemUp es2. ~ \pageBreak | % 227
        \stemUp es2 \stemUp es4 | % 228
        \stemUp es4. \stemUp es8 \stemUp es8 r8 | % 229
        \stemUp es4. \stemUp es8 \stemUp es8 r8 | \barNumberCheck #230
        \stemUp es2. ~ | % 231
        \stemUp es2 \stemUp es4 \pageBreak | % 232
        \stemUp es4. \stemUp es8 \stemUp es4 | % 233
        \stemUp es4. \stemUp es8 \stemUp es4 | % 234
        \stemUp es2. ~ | % 235
        \stemUp es2 \stemUp es4 | % 236
        \stemUp es4. \stemUp es8 \stemUp es4 \pageBreak | % 237
        \stemUp es2 \stemUp es4 | % 238
        \stemUp es2. ~ _\fz | % 239
        \stemUp es4 r4 r4 }
    | \barNumberCheck #240
    R2.*3 \pageBreak | % 243
    R2.*2 | % 245
    \stemUp g2. _\p _\< | % 246
    \stemDown b2. _\! _\fz _\< | % 247
    \stemDown b2 \stemDown d4 -. _\! _\f | % 248
    \stemDown d2. \bar "||"
    \pageBreak | % 249
    R2.*9 \pageBreak | % 258
    R2.*3 | % 261
    \stemUp cis,2 _\f ^ "a 2" _\< \stemUp e4 -. | % 262
    \stemUp a4 -. \stemDown cis2 | % 263
    \stemDown e2 -> _\! _\ff \stemDown cis4 -. | % 264
    \stemDown b4 -. \stemUp a2 \pageBreak | % 265
    R2.*4 | % 269
    \stemUp d,2 _\ff ^ "a 2" _\< \stemUp f4 -. | \barNumberCheck #270
    \stemUp a4 -. \stemDown d2 | % 271
    R2. \pageBreak | % 272
    R2. | % 273
    \stemUp d,2 _\! _\f ^ "a 2" _\< \stemUp f4 -. | % 274
    \stemUp a4 -. \stemDown d2 -> | % 275
    \stemDown f2 -> _\! \stemDown d4 -. | % 276
    \stemUp a4 -. \stemUp f2 -> \pageBreak | % 277
    \stemDown b2. ~ -> _\ff | % 278
    \stemDown b2. | % 279
    \stemDown b2. ~ | \barNumberCheck #280
    \stemDown b2. | % 281
    \stemDown c2. ~ _\fff | % 282
    \stemDown c2. ~ \pageBreak | % 283
    \stemDown c2. ~ | % 284
    \stemDown c2. | % 285
    \stemUp e,2. ~ _\mf | % 286
    \stemUp e2. ~ | % 287
    \stemUp e2. ~ _\p _\> \pageBreak | % 288
    \stemUp e2. ~ _\! _\pp | % 289
    \stemUp e4 r4 r4 | \barNumberCheck #290
    R2.*4 \pageBreak | % 294
    R2.*6 | \barNumberCheck #300
    \stemDown c'4 _\ff r4 r4 \bar "|."
    }

PartPOneOneVoiceOne =  \relative c' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key c \none \transposition e | % 1
        r8 \stemUp c8 _\f \stemUp c2 ~ | % 2
        \stemUp c2. | % 3
        r8 \stemUp g8 \stemUp g2 ~ | % 4
        \stemUp g2. \bar "||"
        R2.*3 \pageBreak | % 8
        R2.*7 \pageBreak | % 15
        R2.*6 \pageBreak | % 21
        \stemUp c'2. ~ -> ^\p | % 22
        \stemUp c4 r4 r4 | % 23
        R2.*2 | % 25
        \stemDown c2. ~ -> ^\p \pageBreak | % 26
        \stemUp c4 r4 r4 | % 27
        R2.*4 \pageBreak | % 31
        R2.*5 \pageBreak | % 36
        R2.*5 | % 41
        r4 \stemDown c2 -> _\ff \pageBreak | % 42
        \stemDown bes2 -> \stemUp a4 ~ -> | % 43
        \stemUp a4 \stemUp as2 -> | % 44
        \stemUp g2 _> \stemUp c,4 ~ | % 45
        \stemUp c4 \stemDown c'2 -> | % 46
        \stemDown bes2 -> \stemUp a4 ~ -> \pageBreak | % 47
        \stemUp a4 \stemUp as2 -> | % 48
        \stemUp g2 \stemUp c,4 ~ ^ "a 2" | % 49
        \stemUp c4 \stemUp g'8 \stemUp g8 \stemUp g4 | \barNumberCheck
        #50
        \stemUp c,4 -. \stemUp c4 -. r4 | % 51
        r4 \stemUp d4 -. \stemUp f4 -. | % 52
        \stemUp es8 \stemUp d8 \stemUp c4 r4 \pageBreak | % 53
        r4 ^ "a 2" \stemUp g'8 \stemUp g8 \stemUp g4 | % 54
        \stemUp c,4 -. \stemUp c4 -. r4 | % 55
        r4 \stemUp d4 -. \stemUp f4 -. | % 56
        \stemUp c8 \stemUp c8 \stemUp c4 \stemUp c4 | % 57
        \stemUp c8 \stemUp c8 \stemUp c4 \stemUp c4 | % 58
        \stemUp c8 \stemUp c8 \stemUp c4 \stemUp c4 | % 59
        \stemUp c4 r4 r4 }
    \pageBreak | \barNumberCheck #60
    R2.*7 \pageBreak | % 67
    R2. \bar "||"
    \key c \major R2.*4 \pageBreak | % 72
    R2.*5 \pageBreak | % 77
    R2.*5 \pageBreak | % 82
    R2.*5 \pageBreak | % 87
    R2.*5 \pageBreak | % 92
    \stemDown c'8 ^\p \stemDown c8 \stemDown c8 \stemDown c8 \stemDown b8
    \stemDown b8 | % 93
    \stemDown c8 \stemDown c8 \stemDown c8 \stemDown c8 \stemDown b8
    \stemDown b8 | % 94
    \stemDown c8 \stemDown c8 \stemDown c8 \stemDown c8 \stemDown b8
    \stemDown b8 | % 95
    \stemDown c8 \stemDown c8 \stemDown c8 \stemDown c8 \stemDown b8
    \stemDown b8 | % 96
    \stemDown c8 ^\mf \stemDown c8 \stemDown c8 \stemDown c8 \stemDown b8
    \stemDown b8 | % 97
    \stemDown c8 \stemDown c8 \stemDown c8 \stemDown c8 \stemDown b8
    ^\markup{ \italic {dim.} } ^\> \stemDown b8 | % 98
    \stemDown b8 \stemDown b8 \stemDown c8 \stemDown c8 \stemDown c8
    \stemDown c8 \pageBreak | % 99
    R2.*8 \pageBreak | % 107
    R2.*6 \pageBreak | % 113
    R2.*4 | % 117
    \stemUp g2. ~ -> ^\! _\f | % 118
    \stemUp g2. \pageBreak | % 119
    \stemUp g4. \stemUp as8 \stemDown b4 _\< | \barNumberCheck #120
    \stemDown d4 \stemDown f2 -> | % 121
    \stemDown c'4. ^^ _\! _\ffz \stemDown b8 \stemDown as4 -. | % 122
    \stemDown g4 -. \stemDown d4 -. \stemUp g,4 -. \bar "||"
    \key c \none \stemDown c2 -> _\ff \stemDown bes4 ~ -> | % 124
    \stemDown bes4 \stemUp a2 -> | % 125
    \stemUp as2 \stemUp d,4 -. \pageBreak | % 126
    \stemUp g4 -. \stemUp es4 -. \stemUp c4 | % 127
    \stemDown c'2 -> \stemDown bes4 ~ -> | % 128
    \stemDown bes4 \stemUp a2 -> | % 129
    \stemUp as2 \stemUp f4 -. | \barNumberCheck #130
    \stemDown c'4 r4 \stemDown c4 | % 131
    \stemDown c4 r4 \stemDown c4 | % 132
    \stemDown c4 r4 \stemDown c4 \pageBreak | % 133
    \stemDown c4 r4 \stemDown c4 | % 134
    \stemDown c4 r4 r4 | % 135
    \stemDown c4 r4 r4 | % 136
    \stemDown c4 r4 r4 | % 137
    \stemDown c4 r4 r4 | % 138
    \stemDown c4 r4 r4 | % 139
    R2. | \barNumberCheck #140
    \stemDown c4 r4 r4 | % 141
    R2. \bar "||"
    \pageBreak | % 142
    \clef "bass" \stemUp c,,2. ~ _\p | % 143
    \stemUp c2. ~ | % 144
    \stemUp c2. ~ _\markup{ \italic {dim.} } | % 145
    \stemUp c2. ~ | % 146
    \stemUp c2. ~ _\pp | % 147
    \stemUp c2. ~ | % 148
    \stemUp c2. ~ | % 149
    \stemUp c2. \pageBreak | \barNumberCheck #150
    \stemUp c4 r4 r4 | % 151
    \clef "treble" R2.*7 \pageBreak | % 158
    R2.*8 \pageBreak | % 166
    R2.*8 \pageBreak | % 174
    R2.*2 \repeat volta 2 {
        | % 176
        \stemDown es''4. _\p \stemDown es8 \stemDown es8 -. r8 | % 177
        \stemDown es4. \stemDown es8 \stemDown es8 -. r8 | % 178
        \stemDown es2. ~ | % 179
        \stemDown es2 \stemDown es4 \pageBreak | \barNumberCheck #180
        \stemDown es4. \stemDown es8 \stemDown es4 | % 181
        \stemDown es4. \stemDown es8 \stemDown es4 | % 182
        \stemDown es2. ~ | % 183
        \stemDown es2 \stemDown es4 | % 184
        \stemDown es4. \stemDown es8 \stemDown es4 | % 185
        \stemDown es4. \stemDown es8 \stemDown es4 \pageBreak | % 186
        \stemDown es2. ~ | % 187
        \stemDown es2 \stemDown es4 | % 188
        \stemDown es4. _\< \stemDown es8 \stemDown es4 | % 189
        \stemDown es2 _\! _\f \stemDown es4 _\> | \barNumberCheck #190
        \stemDown es2. ~ | % 191
        \stemUp es4 ~ _\! ^\p r4 r4 }
    | % 192
    \stemUp es4 r4 r4 \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
        R2.*7 \pageBreak | \barNumberCheck #200
        R2.*6 \pageBreak | % 206
        R2.*7 \pageBreak | % 213
        R2.*8 \pageBreak | % 221
        R2.*6 \pageBreak | % 227
        R2.*5 \pageBreak | % 232
        R2.*5 \pageBreak | % 237
        R2.*3 }
    | \barNumberCheck #240
    R2.*3 \pageBreak | % 243
    R2.*6 \bar "||"
    \pageBreak | % 249
    \clef "treble_8" R2.*4 ^\markup{ \bold {muta in C} } | % 253
    \stemUp e,,2 ^ "a 2" _\f _\< \stemUp g4 -. | % 254
    \stemDown c4 -. \stemDown e2 | % 255
    \stemDown g2 ^^ _\! _\ff \stemDown e4 -. | % 256
    \stemDown d4 -. \stemDown c2 | % 257
    \transposition e R2. \pageBreak ^\markup{ \bold {muta in E} } | % 258
    \clef "treble" R2.*7 \pageBreak | % 265
    R2.*7 \pageBreak | % 272
    R2.*5 \pageBreak | % 277
    \stemUp g'2. ~ -> _\ff | % 278
    \stemUp g2 \stemUp g8 \stemUp g8 | % 279
    \stemUp g2. ~ | \barNumberCheck #280
    \stemUp g2 \stemUp g8 \stemUp g8 | % 281
    \stemDown c2. ~ _\fff | % 282
    \stemDown c2. ~ \pageBreak | % 283
    \stemDown c2. ~ | % 284
    \stemDown c2. ~ | % 285
    \stemDown c4 r4 r4 | % 286
    R2.*2 \pageBreak | % 288
    R2.*6 \pageBreak | % 294
    R2.*6 | \barNumberCheck #300
    \stemUp g4 _\ff r4 r4 \bar "|."
    }

PartPOneOneVoiceTwo =  \relative a' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key c \none \transposition e | % 1
         \once \override NoteHead.style = ##f \stemUp a4 s4*11 \bar "||"
        s4*9 \pageBreak | % 8
         \once \override NoteHead.style = ##f \stemUp a4 s1*5 \pageBreak
        | % 15
         \once \override NoteHead.style = ##f \stemUp a4 s4*17
        \pageBreak | % 21
        R2.*2 s4*9 \pageBreak s4*15 \pageBreak s4*15 \pageBreak s2*9
        \pageBreak s4*15 \pageBreak s2*9 \pageBreak s4*21 }
    \pageBreak s4*21 \pageBreak s2. \bar "||"
    \key c \major s1*3 \pageBreak s4*15 \pageBreak s4*15 \pageBreak
    s4*15 \pageBreak s4*15 \pageBreak | % 92
     \once \override NoteHead.style = ##f \stemUp a4 s1*5 \pageBreak | % 99
    R2.*8 \pageBreak | % 107
    R2. s4*15 \pageBreak s2*9 \pageBreak s1*3 \bar "||"
    \key c \none s4*9 \pageBreak s4*21 \pageBreak s4*27 \bar "||"
    \pageBreak | % 142
    \clef "bass" s1*6 \pageBreak s2. | % 151
    \clef "treble" s4*21 \pageBreak | % 158
     \once \override NoteHead.style = ##f \stemUp a4 s4*23 \pageBreak | % 166
     \once \override NoteHead.style = ##f \stemUp a4 s4*23 \pageBreak
    s1. \repeat volta 2 {
        s1*3 \pageBreak s2*9 \pageBreak s2*9 }
    s2. \bar "||"
    \pageBreak \repeat volta 2 {
        s4*21 \pageBreak s2*9 \pageBreak s4*21 \pageBreak s1*6
        \pageBreak | % 221
         \once \override NoteHead.style = ##f \stemUp a4 s4*17
        \pageBreak | % 227
         \once \override NoteHead.style = ##f \stemUp a4 s2*7 \pageBreak
        | % 232
         \once \override NoteHead.style = ##f \stemUp a4 s2*7 \pageBreak
        | % 237
         \once \override NoteHead.style = ##f \stemUp a4 s1*2 }
    s4*9 \pageBreak | % 243
     \once \override NoteHead.style = ##f \stemUp a4 s4*17 \bar "||"
    \pageBreak | % 249
    \clef "treble_8" s1*6 | % 257
    \transposition e s2. \pageBreak | % 258
    \clef "treble" \once \override NoteHead.style = ##f \stemUp a4 s1*5
    \pageBreak | % 265
     \once \override NoteHead.style = ##f \stemUp a4 s1*5 \pageBreak | % 272
     \once \override NoteHead.style = ##f \stemUp a4 s2*7 \pageBreak
    s2*9 \pageBreak s4*15 \pageBreak | % 288
     \once \override NoteHead.style = ##f \stemUp a4 s4*17 \pageBreak
    s4*21 \bar "|."
    }

PartPOneTwoVoiceOne =  \relative c'' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key es \major \transposition e | % 1
        R2.*4 \bar "||"
        R2.*3 \pageBreak | % 8
        R2.*7 \pageBreak | % 15
        R2.*6 \pageBreak | % 21
        \stemUp c2. ~ -> ^\p | % 22
        \stemUp c4 r4 r4 | % 23
        R2.*2 | % 25
        \stemDown c2. ~ -> ^\p \pageBreak | % 26
        \stemUp c4 r4 r4 | % 27
        R2.*4 \pageBreak | % 31
        R2.*5 \pageBreak | % 36
        R2.*5 | % 41
        r4 \stemUp c,2 -> _\ff \pageBreak | % 42
        \stemUp c2 -> \stemUp c4 -> | % 43
        \stemUp c4 \stemUp c2 -> | % 44
        \stemUp c2 _> \stemUp c4 ~ | % 45
        \stemUp c4 \stemDown c'2 -> | % 46
        \stemUp c,2 -> \stemUp c4 ~ -> \pageBreak | % 47
        \stemUp c4 \stemUp c2 -> | % 48
        \stemUp c2 \stemUp c4 ~ ^ "a 2" | % 49
        \stemUp c4 \stemUp g'8 \stemUp g8 \stemUp g4 | \barNumberCheck
        #50
        \stemUp c,4 -. \stemUp c4 -. r4 | % 51
        r4 \stemUp d4 -. \stemUp f4 -. | % 52
        \stemUp es8 \stemUp d8 \stemUp c4 r4 \pageBreak | % 53
        r4 ^ "a 2" \stemUp g'8 \stemUp g8 \stemUp g4 | % 54
        \stemUp c,4 -. \stemUp c4 -. r4 | % 55
        r4 \stemUp d4 -. \stemUp f4 -. | % 56
        \stemUp c8 \stemUp c8 \stemUp c4 \stemUp c4 | % 57
        \stemUp c8 \stemUp c8 \stemUp c4 \stemUp c4 | % 58
        \stemUp c8 \stemUp c8 \stemUp c4 \stemUp c4 | % 59
        \stemUp c4 r4 r4 }
    \pageBreak | \barNumberCheck #60
    R2.*7 \pageBreak | % 67
    R2. \bar "||"
    \key c \major R2.*4 \pageBreak | % 72
    R2.*5 \pageBreak | % 77
    R2.*5 \pageBreak | % 82
    R2.*5 \pageBreak | % 87
    R2.*5 \pageBreak | % 92
    R2.*7 \pageBreak | % 99
    \stemUp c'2. ~ ^\ppp | \barNumberCheck #100
    \stemUp c2. ~ | % 101
    \stemUp c2. ~ | % 102
    \stemUp c2. ~ | % 103
    \stemUp c2. ~ | % 104
    \stemUp c2. ~ | % 105
    \stemUp c2. ~ | % 106
    \stemUp c2. ~ \pageBreak | % 107
    \stemUp c4 r4 r4 | % 108
    R2.*5 \pageBreak | % 113
    R2.*4 | % 117
    \stemUp g,2. ~ -> _\f | % 118
    \stemUp g2. \pageBreak | % 119
    \stemUp g4. \stemUp as8 \stemUp b4 _\< | \barNumberCheck #120
    \stemUp d4 \stemUp f2 -> | % 121
    \stemDown c'4. ^^ _\! _\ffz \stemDown b8 \stemUp as4 -. | % 122
    \stemUp g4 -. \stemUp d4 -. \stemUp g,4 -. \bar "||"
    \key es \major \stemUp c2 -> _\ff \stemUp bes4 ~ -> | % 124
    \stemUp bes4 \stemUp a2 -> | % 125
    \stemUp as2 \stemUp d,4 -. \pageBreak | % 126
    \stemUp g4 -. \stemUp es4 -. \stemUp c4 | % 127
    \stemUp c'2 -> \stemUp bes4 ~ -> | % 128
    \stemUp bes4 \stemUp a2 -> | % 129
    \stemUp as2 \stemUp f4 -. | \barNumberCheck #130
    \stemUp c'4 r4 \stemUp c4 | % 131
    \stemUp c4 r4 \stemUp c4 | % 132
    \stemUp c4 r4 \stemUp c4 \pageBreak | % 133
    \stemUp c4 r4 \stemUp c4 | % 134
    \stemUp c4 r4 r4 | % 135
    \stemUp c4 r4 r4 | % 136
    \stemUp c4 r4 r4 | % 137
    \stemUp c4 r4 r4 | % 138
    \stemUp c4 r4 r4 | % 139
    R2. | \barNumberCheck #140
    \stemUp c4 r4 r4 | % 141
    R2. \bar "||"
    \pageBreak | % 142
    \clef "bass" \stemUp c,2. ~ | % 143
    \stemUp c2. ~ | % 144
    \stemUp c2. ~ | % 145
    \stemUp c2. ~ | % 146
    \stemUp c2. ~ | % 147
    \stemUp c2. ~ | % 148
    \stemUp c2. ~ | % 149
    \stemUp c2. ~ \pageBreak | \barNumberCheck #150
    R2.*8 \pageBreak | % 158
    R2.*8 \pageBreak | % 166
    R2.*8 \pageBreak | % 174
    R2.*2 \repeat volta 2 {
        | % 176
        \stemUp es'4. _\p \stemUp es8 \stemUp es8 -. r8 | % 177
        \stemUp es4. \stemUp es8 \stemUp es8 -. r8 | % 178
        \stemUp es2. ~ | % 179
        \stemUp es2 \stemUp es4 \pageBreak | \barNumberCheck #180
        \stemUp es4. \stemUp es8 \stemUp es4 | % 181
        \stemUp es4. \stemUp es8 \stemUp es4 | % 182
        \stemUp es2. ~ | % 183
        \stemUp es2 \stemUp es4 | % 184
        \stemUp es4. \stemUp es8 \stemUp es4 | % 185
        \stemUp es4. \stemUp es8 \stemUp es4 \pageBreak | % 186
        \stemUp es2. ~ | % 187
        \stemUp es2 \stemUp es4 | % 188
        \stemUp es4. _\< \stemUp es8 \stemUp es4 | % 189
        \stemUp es2 _\! _\f \stemUp es4 _\> | \barNumberCheck #190
        \stemUp es2. ~ | % 191
        \stemUp es4 ~ _\! ^\p r4 r4 }
    | % 192
    \stemUp es4 r4 r4 \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
        R2.*7 \pageBreak | \barNumberCheck #200
        R2.*6 \pageBreak | % 206
        R2.*7 \pageBreak | % 213
        R2.*8 \pageBreak | % 221
        R2.*6 \pageBreak | % 227
        R2.*5 \pageBreak | % 232
        R2.*5 \pageBreak | % 237
        R2.*3 }
    | \barNumberCheck #240
    R2.*3 \pageBreak | % 243
    R2.*6 \bar "||"
    \pageBreak | % 249
    R2.*4 | % 253
    \stemUp c2 ^ "a 2" _\f _\< \stemUp es4 -. | % 254
    \stemUp as4 -. \stemDown c2 | % 255
    \stemDown es2 ^^ _\! _\ff \stemDown c4 -. | % 256
    \stemDown bes4 -. \stemUp as2 | % 257
    R2. \pageBreak | % 258
    \clef "treble" R2.*7 \pageBreak | % 265
    R2.*7 \pageBreak | % 272
    R2.*5 \pageBreak | % 277
    \stemUp g,2. ~ -> _\ff | % 278
    \stemUp g2 \stemUp g8 \stemUp g8 | % 279
    \stemUp g2. ~ | \barNumberCheck #280
    \stemUp g2 \stemUp g8 \stemUp g8 | % 281
    \stemUp c2. ~ _\fff | % 282
    \stemUp c2. ~ \pageBreak | % 283
    \stemUp c2. ~ | % 284
    \stemUp c2. ~ | % 285
    \stemUp c4 r4 r4 | % 286
    R2.*2 \pageBreak | % 288
    R2.*6 \pageBreak | % 294
    R2.*6 | \barNumberCheck #300
    \stemUp g4 _\ff r4 r4 \bar "|."
    }

PartPOneTwoVoiceTwo =  \relative a' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key es \major \transposition e s1*3
        \bar "||"
        s4*9 \pageBreak s4*21 \pageBreak s2*9 \pageBreak | % 21
        R2.*2 s4*9 \pageBreak s4*15 \pageBreak s4*15 \pageBreak s2*9
        \pageBreak s4*15 \pageBreak s2*9 \pageBreak s4*21 }
    \pageBreak s4*21 \pageBreak s2. \bar "||"
    \key c \major s1*3 \pageBreak s4*15 \pageBreak s4*15 \pageBreak
    s4*15 \pageBreak s4*15 \pageBreak | % 92
     \once \override NoteHead.style = ##f \stemUp a4 s1*5 \pageBreak | % 99
    R2.*8 \pageBreak | % 107
    R2. s4*15 \pageBreak s2*9 \pageBreak s1*3 \bar "||"
    \key es \major s4*9 \pageBreak s4*21 \pageBreak s4*27 \bar "||"
    \pageBreak | % 142
    \clef "bass" s1*6 \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*6
    \pageBreak s1. \repeat volta 2 {
        s1*3 \pageBreak s2*9 \pageBreak s2*9 }
    s2. \bar "||"
    \pageBreak \repeat volta 2 {
        s4*21 \pageBreak s2*9 \pageBreak s4*21 \pageBreak s1*6
        \pageBreak s2*9 \pageBreak s4*15 \pageBreak s4*15 \pageBreak
        s4*9 }
    s4*9 \pageBreak s2*9 \bar "||"
    \pageBreak s4*27 \pageBreak | % 258
    \clef "treble" \once \override NoteHead.style = ##f \stemUp a4 s1*5
    \pageBreak | % 265
     \once \override NoteHead.style = ##f \stemUp a4 s1*5 \pageBreak | % 272
     \once \override NoteHead.style = ##f \stemUp a4 s2*7 \pageBreak
    s2*9 \pageBreak s4*15 \pageBreak s2*9 \pageBreak s4*21 \bar "|."
    }

PartPOneThreeVoiceOne =  \relative c' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key c \none \transposition fes' | % 1
        R2.*4 \bar "||"
        R2.*3 \pageBreak | % 8
        R2.*7 \pageBreak | % 15
        R2.*6 \pageBreak | % 21
        R2.*5 \pageBreak | % 26
        R2.*5 \pageBreak | % 31
        R2.*5 \pageBreak | % 36
        R2.*6 \pageBreak | % 42
        R2.*5 \pageBreak | % 47
        R2.*2 | % 49
        \stemUp <c c'>4 _\ff r4 \stemUp <c c'>4 | \barNumberCheck #50
        r4 \stemUp <c c'>8 -. \stemUp <c c'>8 -. \stemUp <c c'>4 -. | % 51
        \stemUp <c c'>4 r4 \stemUp <c c'>4 | % 52
        r4 \stemUp <c c'>8 -. \stemUp <c c'>8 -. \stemUp <c c'>4 -.
        \pageBreak | % 53
        \stemUp <c c'>4 r4 \stemUp <c c'>4 | % 54
        r4 \stemUp <c c'>8 -. \stemUp <c c'>8 -. \stemUp <c c'>4 -. | % 55
        \stemUp <c c'>4 r4 \stemUp <c c'>4 | % 56
        \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>4 \stemUp <c c'>4
        | % 57
        \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>4 \stemUp <c c'>4
        | % 58
        \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>4 \stemUp <c c'>4
        | % 59
        \stemUp <c c'>4 r4 r4 }
    \pageBreak | \barNumberCheck #60
    R2.*7 \pageBreak | % 67
    R2. \bar "||"
    \key c \major R2.*4 \pageBreak | % 72
    R2.*5 \pageBreak | % 77
    R2.*5 \pageBreak | % 82
    R2.*5 \pageBreak | % 87
    R2.*5 \pageBreak | % 92
    r4 \stemUp <g g'>4 _\pp r4 | % 93
    r4 \stemUp <g g'>4 r4 | % 94
    r4 \stemUp <g g'>4 r4 | % 95
    r4 \stemUp <g g'>4 r4 | % 96
    r4 \stemUp <g g'>4 r4 | % 97
    r4 \stemUp <g g'>4 r4 | % 98
    r4 \stemUp <g g'>4 r4 \pageBreak | % 99
    R2.*8 \pageBreak | % 107
    R2. | % 108
    r4 \stemUp c8 _\p ^ "a 2" \stemUp c8 \stemUp c4 | % 109
    \stemUp b4 -. \stemUp b4 -. r4 | \barNumberCheck #110
    r4 \stemUp des8 \stemUp des8 \stemUp des4 | % 111
    \stemUp c4 -. \stemUp c4 -. r4 | % 112
    r4 \stemUp d8 \stemUp d8 \stemUp d4 \pageBreak | % 113
    \stemUp cis4 _\f r4 \stemUp g'8 -. \stemUp g8 -. | % 114
    \stemUp d4 -. _\markup{ \italic {cresc.} } r4 \stemUp as'8 -.
    \stemUp as8 -. | % 115
    \stemUp es4 -. r4 \stemUp a8 -. \stemUp a8 -. | % 116
    \stemUp e4 -. r4 \stemDown bes'8 -. \stemDown bes8 -. | % 117
    \stemUp f2. ^^ _\f | % 118
    \stemUp g2. ~ ^^ _\< \pageBreak | % 119
    \stemUp g8 _\! ^ "a 2" r8 \stemUp <d d'>2 ~ -> ~ _\ff |
    \barNumberCheck #120
    \stemUp <d d'>2. ~ ~ | % 121
    \stemUp <d d'>4 r4 r4 | % 122
    \stemUp g4 \stemUp g8 \stemUp g8 \stemUp g4 \bar "||"
    \key c \none \stemUp <c, c'>2. _\ff | % 124
    r4 \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>4 | % 125
    \stemUp <c c'>4 \stemUp <c c'>4 r4 \pageBreak | % 126
    r4 \stemUp <c c'>4 \stemUp <c c'>4 | % 127
    \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>4 r4 | % 128
    r4 \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>4 | % 129
    \stemUp <c c'>4 \stemUp <c c'>4 r4 | \barNumberCheck #130
    \stemUp <c c'>4 \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>4 | % 131
    \stemUp <c c'>4 \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>4 | % 132
    \stemUp <c c'>4 \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>4
    \pageBreak | % 133
    \stemUp <c c'>4 \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>4 | % 134
    \stemUp <c c'>4 r4 r4 | % 135
    \stemUp <c c'>4 r4 r4 | % 136
    \stemUp <c c'>4 r4 r4 | % 137
    \stemUp <c c'>4 r4 r4 | % 138
    \stemUp <c c'>4 r4 r4 | % 139
    R2. | \barNumberCheck #140
    \stemUp <c c'>4 r4 r4 | % 141
    R2. ^\markup{ \bold {muta} } \bar "||"
    \pageBreak ^ "in C" | % 142
    R2.*8 \pageBreak | \barNumberCheck #150
    R2.*8 \pageBreak | % 158
    R2.*8 \pageBreak | % 166
    R2.*8 \pageBreak | % 174
    R2.*2 \repeat volta 2 {
        | % 176
        R2.*4 \pageBreak | \barNumberCheck #180
        R2.*6 \pageBreak | % 186
        R2.*6 }
    | % 192
    R2. \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
        R2.*7 \pageBreak | \barNumberCheck #200
        R2.*6 \pageBreak | % 206
        R2.*7 \pageBreak | % 213
        R2.*8 \pageBreak | % 221
        R2.*3 | % 224
        \stemUp <c c'>4. _\p \stemUp <c c'>8 \stemUp <c c'>8 r8 | % 225
        \stemUp <c c'>4. \stemUp <c c'>8 \stemUp <c c'>8 r8 | % 226
        \stemUp <c c'>2. ~ ~ \pageBreak | % 227
        \stemUp <c c'>4. \stemUp <c c'>8 \stemUp <c c'>8 r8 | % 228
        \stemUp <c c'>4. \stemUp <c c'>8 \stemUp <c c'>8 r8 | % 229
        \stemUp <g g'>4. \stemUp <g g'>8 \stemUp <g g'>8 r8 |
        \barNumberCheck #230
        \stemUp <c c'>4. \stemUp <c c'>8 \stemUp <c c'>4 | % 231
        \stemUp <c c'>4. \stemUp <c c'>8 \stemUp <c c'>4 \pageBreak | % 232
        \stemUp <c c'>4. \stemUp <c c'>8 \stemUp <c c'>4 | % 233
        \stemUp <c c'>4. \stemUp <c c'>8 \stemUp <c c'>4 | % 234
        \stemUp <c c'>4. \stemUp <c c'>8 \stemUp <c c'>4 | % 235
        \stemUp <c c'>4. \stemUp <c c'>8 \stemUp <c c'>4 | % 236
        \stemUp <g g'>4. \stemUp <g g'>8 \stemUp <g g'>4 \pageBreak | % 237
        \stemDown <g' d'>2 \stemUp <e c'>4 | % 238
        \stemUp <e c'>2. ~ ~ _\fz | % 239
        \stemUp <e c'>4 r4 r4 }
    | \barNumberCheck #240
    \transposition fes' R2.*3 \pageBreak ^\markup{ \bold {muta in E} } | % 243
    R2.*6 \bar "||"
    \pageBreak | % 249
    R2.*9 \pageBreak | % 258
    R2.*7 \pageBreak | % 265
    R2.*7 \pageBreak | % 272
    R2.*5 \pageBreak | % 277
    \stemUp g2. ~ _\ff ^ "a 2" | % 278
    \stemUp g2 \stemUp g8 \stemUp g8 | % 279
    \stemUp g2. ~ | \barNumberCheck #280
    \stemUp g2 \stemUp g8 \stemUp g8 | % 281
    \stemUp c,2. ~ -> _\fff | % 282
    \stemUp c2 \stemUp c4 -. \pageBreak | % 283
    \stemUp a4 ^ "a 2" \stemUp g2 ~ | % 284
    \stemUp g2. | % 285
    \stemUp c2 _\mf _\> \stemUp e4 | % 286
    \stemUp g2 _\! \stemUp g4 | % 287
    \stemUp g2. ~ _\fp _\> \pageBreak | % 288
    \stemUp g2. ~ ^ "a 2" | % 289
    \stemUp g2. ~ _\! _\pp | \barNumberCheck #290
    \stemUp g2. ~ | % 291
    \stemUp g4 r4 r4 | % 292
    R2.*2 \pageBreak | % 294
    R2.*6 | \barNumberCheck #300
    \stemUp <c, c'>4 _\ff r4 r4 \bar "|."
    }

PartPOneThreeVoiceTwo =  \relative gisis' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key c \none \transposition fes' | % 1
         \once \override NoteHead.style = ##f \stemUp gisis4 s4*11 \bar
        "||"
        s4*9 \pageBreak | % 8
         \once \override NoteHead.style = ##f \stemUp gisis4 s1*5
        \pageBreak | % 15
         \once \override NoteHead.style = ##f \stemUp gisis4 s4*17
        \pageBreak s4*15 \pageBreak s4*15 \pageBreak s4*15 \pageBreak
        s2*9 \pageBreak | % 42
         \once \override NoteHead.style = ##f \stemUp gisis4 s2*7
        \pageBreak s2*9 \pageBreak s4*21 }
    \pageBreak s4*21 \pageBreak s2. \bar "||"
    \key c \major s1*3 \pageBreak s4*15 \pageBreak s4*15 \pageBreak
    s4*15 \pageBreak s4*15 \pageBreak s4*21 \pageBreak | % 99
     \once \override NoteHead.style = ##f \stemUp gisis4 s4*23
    \pageBreak s2*9 \pageBreak s2*9 \pageBreak s4*9 | % 122
    \stemDown g4 \stemDown g8 \stemDown g8 \stemDown g4 \bar "||"
    \key c \none s4*9 \pageBreak s4*21 \pageBreak s4*27 \bar "||"
    \pageBreak | % 142
     \once \override NoteHead.style = ##f \stemDown cis'4 s4*23
    \pageBreak | \barNumberCheck #150
     \once \override NoteHead.style = ##f \stemDown cis4 s4*23
    \pageBreak | % 158
     \once \override NoteHead.style = ##f \stemDown cis,4 s4*23
    \pageBreak | % 166
     \once \override NoteHead.style = ##f \stemDown cis4 s4*23
    \pageBreak | % 174
     \once \override NoteHead.style = ##f \stemDown cis4 s4*5 \repeat
    volta 2 {
        s1*3 \pageBreak | \barNumberCheck #180
         \once \override NoteHead.style = ##f \stemDown cis4 s4*17
        \pageBreak | % 186
         \once \override NoteHead.style = ##f \stemDown cis4 s4*17 }
    s2. \bar "||"
    \pageBreak \repeat volta 2 {
        s4*21 \pageBreak s2*9 \pageBreak s4*21 \pageBreak s1*6
        \pageBreak s2*9 \pageBreak s4*15 \pageBreak s4*15 \pageBreak
        s4*9 }
    | \barNumberCheck #240
    \transposition fes' s4*9 \pageBreak | % 243
     \once \override NoteHead.style = ##f \stemUp gisis4 s4*17 \bar "||"
    \pageBreak | % 249
     \once \override NoteHead.style = ##f \stemUp gisis4 s2*13
    \pageBreak | % 258
     \once \override NoteHead.style = ##f \stemUp gisis4 s1*5 \pageBreak
    | % 265
     \once \override NoteHead.style = ##f \stemUp gisis4 s1*5 \pageBreak
    | % 272
     \once \override NoteHead.style = ##f \stemUp gisis4 s2*7 \pageBreak
    s2*9 \pageBreak s4*15 \pageBreak s2*9 \pageBreak s4*21 \bar "|."
    }

PartPOneFourVoiceOne =  \relative c' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key es \major \transposition e' | % 1
        R2.*4 \bar "||"
        R2.*3 \pageBreak | % 8
        R2.*7 \pageBreak | % 15
        R2.*6 \pageBreak | % 21
        R2.*5 \pageBreak | % 26
        R2.*5 \pageBreak | % 31
        R2.*5 \pageBreak | % 36
        R2.*6 \pageBreak | % 42
        R2.*5 \pageBreak | % 47
        R2.*6 \pageBreak | % 53
        R2.*7 }
    \pageBreak | \barNumberCheck #60
    R2.*7 \pageBreak | % 67
    R2. \bar "||"
    \key c \major R2.*4 \pageBreak | % 72
    R2.*5 \pageBreak | % 77
    R2.*5 \pageBreak | % 82
    R2.*5 \pageBreak | % 87
    R2.*5 \pageBreak | % 92
    R2.*7 \pageBreak | % 99
    R2.*8 \pageBreak | % 107
    R2.*6 \pageBreak | % 113
    R2.*6 \pageBreak | % 119
    R2.*4 \bar "||"
    \key es \major R2.*3 \pageBreak | % 126
    R2.*7 \pageBreak | % 133
    R2.*9 \bar "||"
    \pageBreak | % 142
    R2.*8 \pageBreak | \barNumberCheck #150
    R2.*8 \pageBreak | % 158
    R2.*8 \pageBreak | % 166
    R2.*8 \pageBreak | % 174
    R2.*2 \repeat volta 2 {
        | % 176
        R2.*4 \pageBreak | \barNumberCheck #180
        R2.*6 \pageBreak | % 186
        R2.*6 }
    | % 192
    R2. \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
        R2.*7 \pageBreak | \barNumberCheck #200
        R2.*6 \pageBreak | % 206
        R2.*7 \pageBreak | % 213
        R2.*8 \pageBreak | % 221
        R2.*6 \pageBreak | % 227
        R2.*5 \pageBreak | % 232
        R2.*5 \pageBreak | % 237
        R2.*3 }
    | \barNumberCheck #240
    R2.*3 \pageBreak | % 243
    R2.*6 \bar "||"
    \pageBreak | % 249
    R2.*9 \pageBreak | % 258
    R2.*7 \pageBreak | % 265
    R2.*7 \pageBreak | % 272
    R2.*5 \pageBreak | % 277
    R2.*6 \pageBreak | % 283
    R2.*5 \pageBreak | % 288
    R2.*6 \pageBreak | % 294
    R2.*7 \bar "|."
    }

PartPOneFiveVoiceOne =  \relative e {
    \repeat volta 2 {
        \clef "bass" \time 3/4 \key c \none | % 1
        r4 \stemDown e8 _\f \stemDown e8 \stemDown e4 | % 2
        \stemDown e4 r4 r4 | % 3
        r4 \stemUp b8 \stemUp b8 \stemUp b4 | % 4
        \stemUp b4 r4 r4 \bar "||"
        R2.*3 \pageBreak | % 8
        R2.*7 \pageBreak | % 15
        R2.*6 \pageBreak | % 21
        R2. | % 22
        r4 \stemDown e8 ^ "Solo" _\pp \stemDown e8 \stemDown e4 | % 23
        \stemDown e4 \stemDown e4 r4 | % 24
        r4 \stemDown e4 \stemDown e4 | % 25
        r4 \stemDown e8 \stemDown e8 \stemDown e4 \pageBreak | % 26
        r4 \stemDown e8 \stemDown e8 \stemDown e4 | % 27
        \stemDown e4 \stemDown e4 r4 | % 28
        r4 \stemDown e8 \stemDown e8 \stemDown e4 | % 29
        \stemDown e4 r4 r4 | \barNumberCheck #30
        R2. \pageBreak | % 31
        R2.*2 | % 33
        \stemUp b8 _\ff \stemUp b8 \stemUp b4 r4 | % 34
        R2.*2 \pageBreak | % 36
        R2. | % 37
        \stemUp b8 _\ff \stemUp b8 \stemUp b4 r4 | % 38
        R2.*4 \pageBreak | % 42
        R2.*5 \pageBreak | % 47
        R2.*2 | % 49
        \stemDown e8 _\ff \stemDown e8 r4 \stemDown e4 | \barNumberCheck
        #50
        r4 \stemDown e8 \stemDown e8 \stemDown e4 | % 51
        \stemDown e8 \stemDown e8 r4 \stemDown e4 | % 52
        r4 \stemDown e8 \stemDown e8 \stemDown e4 \pageBreak | % 53
        \stemDown e8 \stemDown e8 r4 \stemDown e4 | % 54
        r4 \stemDown e8 \stemDown e8 \stemDown e4 | % 55
        \stemDown e8 \stemDown e8 r4 \stemDown e4 | % 56
        \stemDown e8 \stemDown e8 \stemDown e4 \stemDown e4 | % 57
        \stemDown e8 \stemDown e8 \stemDown e4 \stemDown e4 | % 58
        \stemDown e8 \stemDown e8 \stemDown e4 \stemDown e4 | % 59
        \stemDown e4 r4 r4 }
    \pageBreak | \barNumberCheck #60
    R2.*7 \pageBreak | % 67
    R2. \bar "||"
    \key c \none R2.*4 \pageBreak | % 72
    R2.*5 \pageBreak | % 77
    R2.*5 \pageBreak | % 82
    R2.*5 \pageBreak | % 87
    R2.*5 \pageBreak | % 92
    \stemDown e4 _\pp r4 \stemUp b4 | % 93
    \stemDown e4 r4 \stemUp b4 | % 94
    \stemDown e4 r4 \stemUp b4 | % 95
    \stemDown e4 r4 \stemUp b4 | % 96
    \stemDown e4 r4 \stemUp b4 | % 97
    \stemDown e4 r4 \stemUp b4 | % 98
    \stemUp b4 \stemUp b8 \stemUp b8 \stemDown e4 \pageBreak | % 99
    R2. | \barNumberCheck #100
    r4 _\ppp \stemDown e8 \stemDown e8 \stemDown e4 | % 101
    \stemDown e4 \stemDown e4 r4 | % 102
    r4 \stemDown e4 \stemDown e4 | % 103
    \stemDown e8 \stemDown e8 \stemDown e4 r4 | % 104
    r4 \stemDown e8 \stemDown e8 \stemDown e4 | % 105
    \stemDown e4 \stemDown e4 r4 | % 106
    r4 \stemDown e4 \stemDown e4 \pageBreak | % 107
    \stemDown e8 \stemDown e8 \stemDown e4 r4 | % 108
    R2.*5 \pageBreak | % 113
    R2.*4 | % 117
    \stemUp b2. :16 _\p | % 118
    \stemUp b2. :16 _\< \pageBreak | % 119
    \key c \none \stemUp b2. :16 | \barNumberCheck #120
    \stemUp b2. :16 _\! | % 121
    \stemUp b2. :16 _\markup{ \italic {cresc.} } _\< | % 122
    \stemUp b2. :16 \bar "||"
    \key c \none \stemDown e2. :16 _\! _\ff | % 124
    \stemDown e2. :16 | % 125
    \stemDown e2. :16 \pageBreak | % 126
    \stemDown e2. :16 | % 127
    \stemDown e2. :16 | % 128
    \stemDown e2. :16 | % 129
    \stemDown e2. :16 | \barNumberCheck #130
    \stemDown e4 \stemDown e4 \stemDown e8 \stemDown e8 | % 131
    \stemDown e4 \stemDown e4 \stemDown e8 \stemDown e8 | % 132
    \stemDown e4 \stemDown e4 \stemDown e8 \stemDown e8 \pageBreak | % 133
    \stemDown e4 \stemDown e4 \stemDown e8 \stemDown e8 | % 134
    \stemDown e8 _\ff \stemDown e8 r4 r4 | % 135
    \stemDown e8 \stemDown e8 r4 r4 | % 136
    \stemDown e8 \stemDown e8 r4 r4 | % 137
    \stemDown e8 \stemDown e8 r4 r4 | % 138
    \stemDown e8 ^^ \stemDown e8 ^^ r4 r4 | % 139
    R2. | \barNumberCheck #140
    \stemDown e8 ^^ \stemDown e8 ^^ r4 r4 | % 141
    R2. \bar "||"
    \pageBreak | % 142
    \stemDown e2. :16 _\fpp | % 143
    \stemDown e2. :16 | % 144
    \stemDown e2. :16 | % 145
    \stemDown e2. :16 | % 146
    \stemDown e2. :16 | % 147
    \stemDown e2. :16 | % 148
    \stemDown e2. :16 | % 149
    \stemDown e2. :16 \pageBreak | \barNumberCheck #150
    \stemDown e2. :16 | % 151
    \stemDown e2. :16 | % 152
    \stemDown e2. :16 | % 153
    \stemDown e2. :16 | % 154
    \stemDown e4 r4 r4 | % 155
    R2.*3 \pageBreak ^\markup{ \bold {muta in C, G} } | % 158
    R2.*8 \pageBreak | % 166
    R2.*8 \pageBreak | % 174
    R2.*2 \repeat volta 2 {
        | % 176
        \stemUp c4 _\p r4 r4 | % 177
        R2. | % 178
        r4 r4 r8 \stemUp c8 _\pp | % 179
        \stemUp c4 r4 r4 \pageBreak | \barNumberCheck #180
        R2.*2 | % 182
        r4 r4 r8 \stemUp c8 _\pp | % 183
        \stemUp c4 r4 r4 | % 184
        R2.*2 \pageBreak | % 186
        r4 r4 r8 \stemUp c8 _\pp | % 187
        \stemUp c4 r4 r4 | % 188
        R2.*2 | \barNumberCheck #190
        r4 r4 r8 \stemUp c8 _\pp | % 191
        \stemUp c4 r4 r4 }
    | % 192
    \stemUp c4 r4 r4 \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
        R2.*7 \pageBreak | \barNumberCheck #200
        R2.*6 \pageBreak | % 206
        R2.*7 \pageBreak | % 213
        R2.*8 \pageBreak | % 221
        R2.*5 | % 226
        r4 r8 \stemUp c8 _\p \stemUp g4 \pageBreak | % 227
        \stemUp c4 \stemUp c4 r4 | % 228
        R2.*2 | \barNumberCheck #230
        r4 r8 \stemUp c8 \stemUp g4 | % 231
        \stemUp c4 \stemUp c4 r4 \pageBreak | % 232
        R2.*2 | % 234
        r4 r8 \stemUp c8 _\mf \stemUp g4 | % 235
        \stemUp c4 \stemUp c4 r4 | % 236
        R2. \pageBreak | % 237
        R2. | % 238
        r4 r8 \stemUp c8 _\f \stemUp g4 | % 239
        \stemUp c4 \stemUp c4 r4 }
    | \barNumberCheck #240
    R2.*3 \pageBreak ^\markup{ \bold {muta in E, H} } | % 243
    R2.*6 \bar "||"
    \pageBreak | % 249
    R2.*9 \pageBreak | % 258
    R2.*7 \pageBreak | % 265
    R2.*7 \pageBreak | % 272
    R2.*5 \pageBreak | % 277
    \stemUp b2. :16 _\ff | % 278
    \stemUp b2. :16 | % 279
    \stemUp b2. :16 | \barNumberCheck #280
    \stemUp b2. :16 | % 281
    \stemDown e2. :16 _\fff | % 282
    \stemDown e2. :16 \pageBreak | % 283
    \stemDown e2. :16 | % 284
    \stemDown e2. :16 | % 285
    \stemDown e2. :16 _\mf _\> | % 286
    \stemDown e2. :16 _\! | % 287
    \stemDown e2. :16 _\p _\> \pageBreak | % 288
    \stemDown e2. :16 | % 289
    \stemDown e4 _\! _\pp r4 r4 | \barNumberCheck #290
    r4 \stemDown e8 \stemDown e8 \stemDown e4 | % 291
    \stemDown e4 r4 r4 | % 292
    r4 \stemDown e8 \stemDown e8 \stemDown e4 | % 293
    \stemDown e4 r4 r4 \pageBreak | % 294
    r4 \stemDown e8 \stemDown e8 \stemDown e4 | % 295
    \stemDown e4 r4 r4 | % 296
    R2.*4 | \barNumberCheck #300
    \stemDown e4 _\ff r4 r4 \bar "|."
    }

PartPOneFiveVoiceTwo =  \relative cis {
    \repeat volta 2 {
        \clef "bass" \time 3/4 \key c \none s1*3 \bar "||"
        s4*9 \pageBreak | % 8
         \once \override NoteHead.style = ##f \stemUp cis4 s1*5
        \pageBreak | % 15
         \once \override NoteHead.style = ##f \stemUp cis4 s4*17
        \pageBreak s4*15 \pageBreak s4*15 \pageBreak s4*15 \pageBreak
        s2*9 \pageBreak | % 42
         \once \override NoteHead.style = ##f \stemUp cis4 s2*7
        \pageBreak s2*9 \pageBreak s4*21 }
    \pageBreak s4*21 \pageBreak s2. \bar "||"
    \key c \none s1*3 \pageBreak s4*15 \pageBreak s4*15 \pageBreak s4*15
    \pageBreak s4*15 \pageBreak s4*21 \pageBreak s1*6 \pageBreak s2*9
    \pageBreak s2*9 \pageBreak | % 119
    \key c \none s1*3 \bar "||"
    \key c \none s4*9 \pageBreak s4*21 \pageBreak s4*27 \bar "||"
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak | % 158
     \once \override NoteHead.style = ##f \stemUp cis4 s4*23 \pageBreak
    | % 166
     \once \override NoteHead.style = ##f \stemUp cis4 s4*23 \pageBreak
    s1. \repeat volta 2 {
        s1*3 \pageBreak s2*9 \pageBreak s2*9 }
    s2. \bar "||"
    \pageBreak \repeat volta 2 {
        s4*21 \pageBreak s2*9 \pageBreak s4*21 \pageBreak s1*6
        \pageBreak s2*9 \pageBreak s4*15 \pageBreak s4*15 \pageBreak
        s4*9 }
    s4*9 \pageBreak | % 243
     \once \override NoteHead.style = ##f \stemUp cis4 s4*17 \bar "||"
    \pageBreak | % 249
     \once \override NoteHead.style = ##f \stemUp cis4 s2*13 \pageBreak
    | % 258
     \once \override NoteHead.style = ##f \stemUp cis4 s1*5 \pageBreak | % 265
     \once \override NoteHead.style = ##f \stemUp cis4 s1*5 \pageBreak | % 272
     \once \override NoteHead.style = ##f \stemUp cis4 s2*7 \pageBreak
    s2*9 \pageBreak s4*15 \pageBreak s2*9 \pageBreak s4*21 \bar "|."
    }

PartPOneSixVoiceOne =  \relative e' {
    \repeat volta 2 {
        \clef "percussion" \time 3/4 \key c \major \stopStaff \override
        Staff.StaffSymbol.line-count = #1 \startStaff | % 1
        \stemUp e2. :16 _\f | % 2
        \stemUp e2. :16 | % 3
        \stemUp e2. :16 | % 4
        \stemUp e2. :16 \bar "||"
        R2.*3 \pageBreak | % 8
        R2.*7 \pageBreak | % 15
        R2.*6 \pageBreak | % 21
        R2.*5 \pageBreak | % 26
        R2.*5 \pageBreak | % 31
        R2.*5 \pageBreak | % 36
        R2.*6 \pageBreak | % 42
        R2.*5 \pageBreak | % 47
        R2.*6 \pageBreak | % 53
        R2.*7 }
    \pageBreak | \barNumberCheck #60
    R2.*7 \pageBreak | % 67
    R2. \bar "||"
    R2.*4 \pageBreak | % 72
    R2.*4 | % 76
    r4 \stemUp e4 _\pp r4 \pageBreak | % 77
    r4 \stemUp e4 r4 | % 78
    r4 \stemUp e4 r4 | % 79
    r4 \stemUp e4 r4 | \barNumberCheck #80
    r4 \stemUp e4 r4 | % 81
    r4 \stemUp e4 r4 \pageBreak | % 82
    r4 \stemUp e4 r4 | % 83
    r4 \stemUp e4 r4 | % 84
    R2.*3 \pageBreak | % 87
    R2.*5 \pageBreak | % 92
    r4 \stemUp e4 _\p r4 | % 93
    r4 \stemUp e4 r4 | % 94
    r4 \stemUp e4 r4 | % 95
    r4 \stemUp e4 r4 | % 96
    r4 \stemUp e4 r4 | % 97
    r4 \stemUp e4 r4 | % 98
    r4 \stemUp e4 r4 \pageBreak | % 99
    R2.*8 \pageBreak | % 107
    R2.*6 \pageBreak | % 113
    R2.*6 \pageBreak | % 119
    R2.*4 \bar "||"
    R2.*3 \pageBreak | % 126
    R2.*7 \pageBreak | % 133
    R2.*9 \bar "||"
    \pageBreak | % 142
    R2.*8 \pageBreak | \barNumberCheck #150
    R2.*8 \pageBreak | % 158
    R2.*8 \pageBreak | % 166
    R2.*8 \pageBreak | % 174
    R2.*2 \repeat volta 2 {
        | % 176
        R2.*2 | % 178
        \stemUp e2. :16 _\pp | % 179
        \stemUp e4 r4 r4 \pageBreak | \barNumberCheck #180
        R2.*2 | % 182
        \stemUp e2. :16 | % 183
        \stemUp e4 r4 r4 | % 184
        R2.*2 \pageBreak | % 186
        \stemUp e2. :16 | % 187
        \stemUp e4 r4 r4 | % 188
        R2.*2 | \barNumberCheck #190
        \stemUp e2. :16 | % 191
        \stemUp e4 r4 r4 }
    | % 192
    \stemUp e4 r4 r4 \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
        R2.*7 \pageBreak | \barNumberCheck #200
        R2.*6 \pageBreak | % 206
        R2.*7 \pageBreak | % 213
        R2.*8 \pageBreak | % 221
        R2.*3 | % 224
        \once \omit TupletBracket
        \times 4/6  {
            \stemUp e2. :8 _\pp }
        \stemUp e8 r8 | % 225
        \once \omit TupletBracket
        \times 4/6  {
            \stemUp e2. :16 }
        \stemUp e8 r8 | % 226
        \once \omit TupletBracket
        \times 4/6  {
            \stemUp e2. :16 }
        \stemUp e8 r8 \pageBreak | % 227
        \once \omit TupletBracket
        \times 4/6  {
            \stemUp e2. :16 }
        \stemUp e8 r8 | % 228
        \once \omit TupletBracket
        \times 4/6  {
            \stemUp e2. :16 }
        \stemUp e8 r8 | % 229
        \once \omit TupletBracket
        \times 4/6  {
            \stemUp e2. :16 }
        \stemUp e8 r8 | \barNumberCheck #230
        \once \omit TupletBracket
        \times 4/6  {
            \stemUp e2. :16 }
        \stemUp e8 r8 | % 231
        \once \omit TupletBracket
        \times 4/6  {
            \stemUp e2. :16 }
        \stemUp e8 r8 \pageBreak | % 232
        \once \omit TupletBracket
        \times 4/6  {
            \stemUp e2. :16 }
        \stemUp e8 r8 | % 233
        \once \omit TupletBracket
        \times 4/6  {
            \stemUp e2. :16 }
        \stemUp e8 r8 | % 234
        \once \omit TupletBracket
        \times 4/6  {
            \stemUp e2. :16 }
        \stemUp e8 r8 | % 235
        \once \omit TupletBracket
        \times 4/6  {
            \stemUp e2. :16 }
        \stemUp e8 r8 | % 236
        \once \omit TupletBracket
        \times 4/6  {
            \stemUp e2. :16 }
        \stemUp e8 r8 \pageBreak | % 237
        \once \omit TupletBracket
        \times 4/6  {
            \stemUp e2. :16 }
        \stemUp e8 r8 | % 238
        \stemUp e2. \startTrillSpan \stopTrillSpan _\fz | % 239
        \stemUp e4 r4 r4 }
    | \barNumberCheck #240
    R2.*3 \pageBreak | % 243
    R2.*6 \bar "||"
    \pageBreak | % 249
    R2.*9 \pageBreak | % 258
    R2.*7 \pageBreak | % 265
    R2.*7 \pageBreak | % 272
    R2.*5 \pageBreak | % 277
    R2.*6 \pageBreak | % 283
    R2.*5 \pageBreak | % 288
    R2.*6 \pageBreak | % 294
    R2.*7 \bar "|."
    }

PartPOneSixVoiceTwo =  \relative e' {
    \repeat volta 2 {
        \clef "percussion" \time 3/4 \key c \major \stopStaff \override
        Staff.StaffSymbol.line-count = #1 \startStaff s1*3 \bar "||"
        s4*9 \pageBreak | % 8
         \once \override NoteHead.style = ##f \stemDown e4 s1*5
        \pageBreak | % 15
         \once \override NoteHead.style = ##f \stemDown e4 s4*17
        \pageBreak s4*15 \pageBreak s4*15 \pageBreak s4*15 \pageBreak
        s2*9 \pageBreak | % 42
         \once \override NoteHead.style = ##f \stemDown e4 s2*7
        \pageBreak | % 47
         \once \override NoteHead.style = ##f \stemDown e4 s4*17
        \pageBreak | % 53
         \once \override NoteHead.style = ##f \stemDown e4 s1*5 }
    \pageBreak s4*21 \pageBreak s2. \bar "||"
    s1*3 \pageBreak s4*15 \pageBreak s4*15 \pageBreak s4*15 \pageBreak
    s4*15 \pageBreak s4*21 \pageBreak | % 99
     \once \override NoteHead.style = ##f \stemDown e4 s4*23 \pageBreak
    | % 107
     \once \override NoteHead.style = ##f \stemDown e4 s4*17 \pageBreak
    | % 113
     \once \override NoteHead.style = ##f \stemDown e4 s4*17 \pageBreak
    | % 119
     \once \override NoteHead.style = ##f \stemDown e4 s4*11 \bar "||"
    s4*9 \pageBreak | % 126
     \once \override NoteHead.style = ##f \stemDown e4 s1*5 \pageBreak | % 133
     \once \override NoteHead.style = ##f \stemDown e4 s2*13 \bar "||"
    \pageBreak | % 142
     \once \override NoteHead.style = ##f \stemDown e4 s4*23 \pageBreak
    | \barNumberCheck #150
     \once \override NoteHead.style = ##f \stemDown e4 s4*23 \pageBreak
    | % 158
     \once \override NoteHead.style = ##f \stemDown e4 s4*23 \pageBreak
    | % 166
     \once \override NoteHead.style = ##f \stemDown e4 s4*23 \pageBreak
    s1. \repeat volta 2 {
        s1*3 \pageBreak s2*9 \pageBreak s2*9 }
    s2. \bar "||"
    \pageBreak \repeat volta 2 {
        s4*21 \pageBreak s2*9 \pageBreak s4*21 \pageBreak s1*6
        \pageBreak s2*9 \pageBreak s4*15 \pageBreak s4*15 \pageBreak
        s4*9 }
    s4*9 \pageBreak | % 243
     \once \override NoteHead.style = ##f \stemDown e4 s4*17 \bar "||"
    \pageBreak | % 249
     \once \override NoteHead.style = ##f \stemDown e4 s2*13 \pageBreak
    | % 258
     \once \override NoteHead.style = ##f \stemDown e4 s1*5 \pageBreak | % 265
     \once \override NoteHead.style = ##f \stemDown e4 s1*5 \pageBreak | % 272
     \once \override NoteHead.style = ##f \stemDown e4 s2*7 \pageBreak | % 277
     \once \override NoteHead.style = ##f \stemDown e4 s4*17 \pageBreak
    | % 283
     \once \override NoteHead.style = ##f \stemDown e4 s2*7 \pageBreak | % 288
     \once \override NoteHead.style = ##f \stemDown e4 s4*17 \pageBreak
    | % 294
     \once \override NoteHead.style = ##f \stemDown e4 s1*5 \bar "|."
    }

PartPOneSevenVoiceOne =  \relative e''' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key g \major | % 1
        \stemDown e4 _\f r4 r4 | % 2
        R2. | % 3
        \stemDown b4 r4 r4 | % 4
        R2. \bar "||"
        R2.*3 \pageBreak | % 8
        \stemUp d,,8 _\f _\> \stemUp d8 \stemUp d2 ~ | % 9
        \stemUp d4 _\! \stemUp d4 ( -. _\p ^\markup{ \italic {spiccato}
            } \stemUp d4 ) -. | \barNumberCheck #10
        \stemUp d4 ( -. \stemUp d4 -. \stemUp d4 ) -. | % 11
        \stemUp d4 -. _\pp ^\markup{ \italic {simile} } \stemUp d4 -.
        \stemUp d4 -. | % 12
        \stemUp d4 -. _\> \stemUp d4 -. \stemUp d4 -. | % 13
        \stemUp d4 -. _\! _\ppp \stemUp d4 -. \stemUp d4 -. | % 14
        \stemUp d4 -. \stemUp d4 -. \stemUp d4 -. \pageBreak | % 15
        \stemUp d4 -. \stemUp d4 -. \stemUp d4 -. | % 16
        \stemUp d4 -. \stemUp d4 -. \stemUp d4 -. | % 17
        \stemUp d4 -. \stemUp d4 -. \stemUp d4 -. | % 18
        \stemUp d4 -. \stemUp d4 -. \stemUp d4 -. | % 19
        \stemUp d4 -. \stemUp d4 -. \stemUp d4 -. | \barNumberCheck #20
        \stemDown b'4 -. \stemUp g8 ( \stemUp b8 \stemUp g4 ) \pageBreak
        | % 21
        \stemUp e8 r8 \stemDown b''8 ( -. _\pp \stemDown b8 -. \stemDown
        b4 ) -. | % 22
        \stemDown e,4 ( -. \stemDown e4 ) -. r4 | % 23
        r4 \stemDown fis4 -. \stemDown a4 -. | % 24
        \stemDown g8 ( -. \stemDown fis8 -. \stemDown e4 ) -. r4 | % 25
        r4 \stemDown b'8 ( -. \stemDown b8 -. \stemDown b4 ) -.
        \pageBreak | % 26
        \stemDown e,4 ( -. \stemDown e4 ) -. r4 | % 27
        r4 \stemDown fis4 -. \stemDown a4 -. | % 28
        \stemDown g8 ( -. \stemDown fis8 -. \stemDown e4 ) -. r4 | % 29
        r4 \stemDown e4 -. _\mf \stemDown g4 -. | \barNumberCheck #30
        \stemDown e8 \stemDown d8 \stemDown b4 -. \stemDown d8 \stemDown
        b8 \pageBreak | % 31
        \stemUp g4 -. _\f _\< \stemUp g8 \stemUp e8 \stemUp d8
        \stemUp g8 | % 32
        \stemUp e8 \stemUp d8 \stemUp b8 \stemUp e8 \stemUp d8 \stemUp b8
        | % 33
        r4 _\! \stemUp g'8 -. _\ff \stemUp g8 -. \stemUp e4 -. | % 34
        \stemUp g4 -. \stemUp g4 -. \stemUp e4 -. | % 35
        \stemUp g8 -. \stemUp g8 -. \stemUp e4 -. \stemDown b'4 -.
        \pageBreak | % 36
        \stemUp g4 -. \stemDown b4 -. \stemUp g4 -. | % 37
        \stemDown b4 -. \stemDown g'8 -. \stemDown g8 -. \stemDown e4 -.
        | % 38
        \stemDown g4 -. \stemDown g4 -. \stemDown e4 -. | % 39
        \stemDown g8 -. \stemDown g8 -. \stemDown e4 -. \stemDown b'4 -.
        | \barNumberCheck #40
        \stemDown g4 -. \stemDown b4 -. \stemDown g4 -. | % 41
        \stemDown b4 -. \stemDown b'8 \stemDown b8 \stemDown b4
        \pageBreak | % 42
        \stemDown e,4 -. \stemDown e4 -. r4 | % 43
        r4 \stemDown fis4 -. \stemDown a4 -. | % 44
        \stemDown g8 \stemDown fis8 \stemDown e4 r4 | % 45
        r4 \stemDown b'8 \stemDown b8 \stemDown b4 | % 46
        \stemDown e,4 -. \stemDown e4 -. r4 \pageBreak | % 47
        r4 \stemDown fis4 -. \stemDown a4 -. | % 48
        \stemDown g8 \stemDown fis8 \stemDown e4 \stemDown e8 \stemDown
        b8 | % 49
        \stemDown e2. :32 | \barNumberCheck #50
        \stemDown e2. :32 | % 51
        \stemDown e2. :32 | % 52
        \stemDown e2. :32 \pageBreak | % 53
        \stemDown e2. :32 | % 54
        \stemDown e2. :32 | % 55
        \stemDown e2. :32 | % 56
        \stemDown e8 \stemDown e8 \stemDown e4 \stemDown e4 | % 57
        \stemDown e8 \stemDown e8 \stemDown e4 \stemDown e4 | % 58
        \stemDown e8 \stemDown e8 \stemDown e4 \stemDown e4 | % 59
        \stemDown e8 \stemDown e8 \stemDown e4 r4 }
    \pageBreak | \barNumberCheck #60
    \stemDown e8 _\f \stemDown c8 \stemDown b4 -. _\p r4 | % 61
    R2. | % 62
    \stemUp e,,8 _\p _\markup{ \italic {dim.} } \stemUp c8 \stemUp b4 -.
    r4 | % 63
    \stemUp e8 _\markup{ \italic {dim.} } \stemUp c8 \stemUp b4 -. r4 | % 64
    R2.*3 \pageBreak | % 67
    R2. \bar "||"
    \key e \major R2.*4 \pageBreak | % 72
    R2.*5 \pageBreak | % 77
    R2.*5 \pageBreak | % 82
    R2.*5 \pageBreak | % 87
    R2.*5 \pageBreak | % 92
    R2.*7 \pageBreak | % 99
    r4 \stemDown b''8 ( -. _\ppp \stemDown b8 -. \stemDown b4 ) -. |
    \barNumberCheck #100
    \stemDown e,4 -. \stemDown e4 -. r4 | % 101
    r4 \stemDown fis4 -. \stemDown a4 -. | % 102
    \stemDown gis8 -. \stemDown fis8 -. \stemDown e4 -. r4 | % 103
    r4 \stemDown b'8 ( -. \stemDown b8 -. \stemDown b4 ) -. | % 104
    \stemDown e,4 -. \stemDown e4 -. r4 | % 105
    r4 \stemDown fis4 -. \stemDown a4 -. | % 106
    \stemDown gis8 -. \stemDown fis8 -. \stemDown e4 -. r4 \pageBreak | % 107
    r4 \stemDown b'8 _\pp \stemDown b8 \stemDown b4 | % 108
    \stemDown e,4 -. \stemDown e4 -. r4 | % 109
    r4 \stemDown c'8 \stemDown c8 \stemDown c4 | \barNumberCheck #110
    \stemDown f,4 -. _\< \stemDown f4 -. r4 _\! | % 111
    r4 \stemDown cis'8 \stemDown cis8 \stemDown cis4 | % 112
    \stemDown fis,4 -. \stemDown fis4 -. r4 \pageBreak | % 113
    r4 \stemDown d'8 _\mf _\< \stemDown d8 \stemDown d4 | % 114
    r4 \stemDown dis8 \stemDown dis8 \stemDown dis4 | % 115
    r4 \stemDown e8 \stemDown e8 \stemDown e4 | % 116
    r4 _\! \stemDown f8 _\f \stemDown f8 \stemDown f4 | % 117
    r4 _\markup{ \italic {più} } \stemDown fis8 _\f \stemDown fis8
    \stemDown fis4 | % 118
    \stemDown g8 _\< \stemDown g8 \stemDown g4 \stemDown gis8 \stemDown
    gis8 \pageBreak | % 119
    \stemDown gis4 \stemDown a8 _\! \stemDown a8 \stemDown a4 |
    \barNumberCheck #120
    \stemDown a8 \stemDown a8 \stemDown a4 \stemDown a8 \stemDown a8 | % 121
    \stemDown a4 \stemDown a8 \stemDown a8 \stemDown a4 | % 122
    \stemDown a8 \stemDown a8 \stemDown a8 \stemDown ais8 \stemDown b8
    \stemDown b,8 \bar "||"
    \key g \major \stemDown e8 _\fff r8 \stemDown b'8 \stemDown b8
    \stemDown b4 | % 124
    \stemDown e,4 -. \stemDown e4 -. r4 | % 125
    r4 \stemDown fis4 -. \stemDown a4 -. \pageBreak | % 126
    \stemDown g8 \stemDown fis8 \stemDown e4 r4 | % 127
    r4 \stemDown b'8 \stemDown b8 \stemDown b4 | % 128
    \stemDown e,4 -. \stemDown e4 -. r4 | % 129
    r4 \stemDown fis4 -. \stemDown a4 -. | \barNumberCheck #130
    \stemDown g8 \stemDown fis8 \stemDown e4 \stemDown a4 | % 131
    \stemDown g8 \stemDown fis8 \stemDown e4 \stemDown a4 | % 132
    \stemDown g8 \stemDown fis8 \stemDown e4 \stemDown a4 \pageBreak | % 133
    \stemDown g8 \stemDown fis8 \stemDown e4 \stemDown a4 | % 134
    \stemDown g8 \stemDown fis8 \stemDown e4 r4 | % 135
    \stemDown g8 \stemDown fis8 \stemDown e4 r4 | % 136
    \stemDown g8 \stemDown fis8 \stemDown e4 r4 | % 137
    \stemDown g8 \stemDown fis8 \stemDown e4 r4 | % 138
    \stemDown g8 _\ffz \stemDown fis8 \stemDown e2 ~ _\> | % 139
    \stemDown e2. | \barNumberCheck #140
    \stemDown g8 _\! _\ffz \stemDown fis8 \stemDown e2 ~ _\> | % 141
    \stemDown e2. \bar "||"
    \pageBreak | % 142
    R2. | % 143
    r4 _\! \stemDown b8 _\p \stemDown b8 \stemDown b4 | % 144
    \stemDown e,4 -. \stemDown e4 -. r4 | % 145
    R2.*5 \pageBreak | \barNumberCheck #150
    R2.*8 \pageBreak | % 158
    R2.*8 \pageBreak | % 166
    R2.*5 | % 171
    r4 r4 \stemDown as4 ( _\ppp | % 172
    \stemDown g4 \stemDown c,4 \stemDown a'4 | % 173
    \stemDown g4 \stemDown c,4 \stemDown a'4 \pageBreak | % 174
    \stemDown g4 \stemDown c,4 ) \stemDown a'4 ( | % 175
    \stemDown g4 \stemDown c,4 \stemDown a'4 \repeat volta 2 {
        | % 176
        \stemDown g4 \stemDown c,4 ) \stemDown a'4 ( | % 177
        \stemDown g4 \stemDown c,4 \stemDown a'4 | % 178
        \stemDown g4 \stemDown c,4 ) \stemDown a'4 ( | % 179
        \stemDown g4 \stemDown c,4 \stemDown a'4 \pageBreak |
        \barNumberCheck #180
        \stemDown g4 \stemDown c,4 ) \stemDown a'4 ( | % 181
        \stemDown g4 \stemUp g,4 \stemDown f'4 | % 182
        \stemDown e4 \stemDown c4 ) \stemDown d'4 ( | % 183
        \stemDown c4 \stemDown e,4 \stemDown a4 | % 184
        \stemDown g4 \stemDown c,4 ) \stemDown a'4 ( | % 185
        \stemDown g4 \stemDown c,4 \stemDown a'4 \pageBreak | % 186
        \stemDown g4 \stemDown c,4 ) \stemDown a'4 ( | % 187
        \stemDown g4 \stemDown c,4 \stemDown a'4 | % 188
        \stemDown g4 \stemDown b,4 ) \stemDown g'4 ( | % 189
        \stemDown f4 \stemDown g4 \stemDown e4 ) | \barNumberCheck #190
        \stemDown e4 ( \stemDown c4 \stemDown d4 | % 191
        \stemUp g,4 \stemDown c4 ) \stemDown a'4 ( }
    | % 192
    \stemUp g,4 ) \stemDown c4 \stemDown c'4 -. \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
        \stemDown b8 ( _\mf \stemDown g'8 \stemDown b,8 ) r8 \stemDown a8
        r8 | % 194
        \stemDown g2. \startTrillSpan \stopTrillSpan | % 195
        \stemDown fis8 ( \stemDown d'8 \stemDown fis,8 ) r8 \stemDown e8
        r8 | % 196
        \stemDown d2. \startTrillSpan \stopTrillSpan | % 197
        \stemDown c8 ( _\p \stemDown a'8 \stemDown c,8 ) r8 \stemDown b8
        r8 | % 198
        \stemUp a2. \startTrillSpan \stopTrillSpan _\> | % 199
        \stemDown g8 ( _\! _\pp \stemDown e'8 \stemUp g,8 ) r8 \stemUp
        fis8 r8 \pageBreak | \barNumberCheck #200
        \stemUp g2. \startTrillSpan \stopTrillSpan | % 201
        R2.*5 \pageBreak | % 206
        R2.*3 | % 209
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown b8 ( _\p \stemDown g'8 \stemDown b,8 }
        \stemDown g'8 ) r8 \stemDown fis8 r8 | \barNumberCheck #210
        \stemDown e2. \startTrillSpan \stopTrillSpan | % 211
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown b8 ( _\p \stemDown g'8 \stemDown b,8 }
        \stemDown g'8 ) r8 \stemDown fis8 r8 | % 212
        \stemDown e2. \startTrillSpan \stopTrillSpan \pageBreak | % 213
        \acciaccatura { \stemUp b8 ( } \stemDown b'2. ) ~ | % 214
        \stemDown b2. ~ | % 215
        \stemDown b2 ( \stemDown b,4 ) | % 216
        \stemDown b2 ~ \startTrillSpan ^ "♯" _\pp \stemDown b8 r8 | % 217
        R2. | % 218
        \stemDown e2 ~ \startTrillSpan \stemDown e8 r8 | % 219
        R2. | \barNumberCheck #220
        \stemDown f2 ~ \startTrillSpan \stemDown f8 r8 \pageBreak | % 221
        R2. | % 222
        \stemDown f2 ~ \startTrillSpan \stemDown f8 r8 | % 223
        R2. | % 224
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown g8 ( _\pp \stemDown a8 \stemDown g8 }
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown a8 \stemDown g8 \stemDown a8 ) }
        \stemDown g8 r8 | % 225
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown g8 ( \stemDown a8 \stemDown g8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown a8 \stemDown g8 \stemDown a8 ) }
        \stemDown g8 r8 | % 226
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown g8 ( \stemDown a8 \stemDown g8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown a8 \stemDown g8 \stemDown a8 ) }
        \stemDown g8 r8 \pageBreak | % 227
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown g8 ( \stemDown a8 \stemDown g8 }
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown a8 \stemDown g8 \stemDown a8 ) }
        \stemDown g8 r8 | % 228
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown g8 ( \stemDown a8 \stemDown g8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown a8 \stemDown g8 \stemDown a8 ) }
        \stemDown g8 r8 | % 229
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown g8 ( \stemDown a8 \stemDown g8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown a8 \stemDown g8 \stemDown a8 ) }
        \stemDown g8 r8 | \barNumberCheck #230
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown g8 ( \stemDown a8 \stemDown g8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown a8 \stemDown g8 \stemDown a8 ) }
        \stemDown g8 r8 | % 231
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown g8 ( \stemDown a8 \stemDown g8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown a8 \stemDown g8 \stemDown a8 ) }
        \stemDown g8 r8 \pageBreak | % 232
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown g8 ( \stemDown a8 \stemDown g8 }
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown a8 \stemDown g8 \stemDown a8 ) }
        \stemDown g8 r8 | % 233
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown g8 ( \stemDown a8 \stemDown g8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown a8 \stemDown g8 \stemDown a8 ) }
        \stemDown g8 r8 | % 234
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown g8 ( \stemDown a8 \stemDown g8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown a8 \stemDown g8 \stemDown a8 ) }
        \stemDown g8 r8 | % 235
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown g8 ( \stemDown a8 \stemDown g8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown a8 \stemDown g8 \stemDown a8 ) }
        \stemDown g8 r8 | % 236
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown g8 ( \stemDown a8 \stemDown g8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown a8 \stemDown g8 \stemDown a8 ) }
        \stemDown g8 r8 \pageBreak | % 237
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown g8 ( \stemDown a8 \stemDown g8 }
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown a8 \stemDown g8 \stemDown a8 ) }
        \stemDown g8 r8 | % 238
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown g8 ( _\fz \stemDown a8 \stemDown g8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown a8 \stemDown g8 \stemDown a8 ) }
        \stemDown g8 r8 | % 239
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown g8 ( \stemDown a8 \stemDown g8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown a8 \stemDown g8 \stemDown a8 ) }
        \stemDown g8 r8 }
    | \barNumberCheck #240
    r4 \stemDown g8 _\pp \stemDown g8 \stemDown g4 | % 241
    \stemDown c,4 \stemDown c4 r4 | % 242
    r4 \stemDown as'8 \stemDown as8 \stemDown as4 \pageBreak | % 243
    \stemDown ces,4 \stemDown ces4 r4 | % 244
    r4 \stemDown gis'8 \stemDown gis8 \stemDown gis4 | % 245
    r4 \stemDown a8 \stemDown a8 \stemDown a4 | % 246
    r4 \stemDown ais8 _\< \stemDown ais8 \stemDown ais4 | % 247
    \stemDown ais8 \stemDown ais8 \stemDown b4 \stemDown c8 \stemDown c8
    | % 248
    \stemDown cis4 _\! _\f _\< \stemDown d8 \stemDown d8 \stemDown dis4
    \bar "||"
    \pageBreak | % 249
    \stemUp e,,2. :16 _\! _\ff | \barNumberCheck #250
    \stemUp e2. :16 _\markup{ \italic {dim.} } _\> | % 251
    \stemUp e2. :16 _\! _\p _\> | % 252
    \stemUp e2. :16 _\! | % 253
    \stemUp e2. :16 _\pp | % 254
    \stemUp e2. :16 | % 255
    \stemUp e2. :16 | % 256
    \stemUp e2. :16 | % 257
    \stemUp e2. :16 \pageBreak | % 258
    \stemUp e2. :16 | % 259
    \stemUp e2. :16 | \barNumberCheck #260
    \stemUp e2. :16 | % 261
    \stemUp f2. :16 _\pp | % 262
    \stemUp f2. :16 | % 263
    \stemUp f2. :16 | % 264
    \stemUp f2. :16 \pageBreak | % 265
    \stemUp f2. :16 _\< | % 266
    \stemUp f2. :16 | % 267
    \stemUp f2. :16 | % 268
    \stemUp f2. :16 | % 269
    \stemUp <fis a>2. :16 _\! _\fz | \barNumberCheck #270
    \stemUp <fis a>2. :16 | % 271
    \stemDown cis'2. :16 _\p \pageBreak | % 272
    \stemDown cis2. :16 _\< | % 273
    \stemDown fis2. :16 | % 274
    \stemDown a2. :16 _\! | % 275
    \stemDown cis2. :16 _\f _\< | % 276
    \stemDown fis2. :16 \pageBreak | % 277
    \stemDown b2. :16 _\! _\fff | % 278
    \stemDown b2. :16 | % 279
    \stemDown b2. :16 | \barNumberCheck #280
    \stemDown b2. :16 | % 281
    \stemDown b8 r8 \stemDown b8 \stemDown b8 \stemDown b4 | % 282
    \stemDown e,4 -. \stemDown e4 -. r4 \pageBreak | % 283
    r4 \stemDown b8 \stemDown b8 \stemDown b4 _\> | % 284
    \stemDown e,4 -. \stemDown e4 -. r4 _\! | % 285
    r4 \stemDown b8 _\mf \stemDown b8 \stemDown b4 | % 286
    \stemUp e,4 -. \stemUp e4 -. r4 | % 287
    r4 \stemDown b'8 _\p \stemDown b8 \stemDown b4 \pageBreak | % 288
    \stemUp e,4 -. \stemUp e4 -. r4 | % 289
    r4 \stemDown b'8 _\p \stemDown b8 \stemDown b4 | \barNumberCheck
    #290
    \stemUp e,4 r4 r4 | % 291
    R2.*3 \pageBreak | % 294
    R2. | % 295
    \stemDown b'4 _\ppp ^ "pizz." r4 r4 | % 296
    \stemUp e,4 r4 r4 | % 297
    R2.*3 | \barNumberCheck #300
    \stemDown e''4 _\ff ^ "arco" r4 r4 \bar "|."
    }

PartPOneSevenVoiceTwo =  \relative cis'' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key g \major s1*3 \bar "||"
        s4*9 \pageBreak s4*21 \pageBreak s2*9 \pageBreak s4*15
        \pageBreak s4*15 \pageBreak s4*15 \pageBreak s2*9 \pageBreak
        s4*15 \pageBreak s2*9 \pageBreak s4*21 }
    \pageBreak s4*21 \pageBreak | % 67
     \once \override NoteHead.style = ##f \stemDown cis4 s2 \bar "||"
    \key e \major s1*3 \pageBreak | % 72
     \once \override NoteHead.style = ##f \stemDown cis4 s2*7 \pageBreak
    | % 77
     \once \override NoteHead.style = ##f \stemDown cis4 s2*7 \pageBreak
    | % 82
     \once \override NoteHead.style = ##f \stemDown cis4 s2*7 \pageBreak
    | % 87
     \once \override NoteHead.style = ##f \stemDown cis4 s2*7 \pageBreak
    | % 92
     \once \override NoteHead.style = ##f \stemDown cis4 s1*5 \pageBreak
    s1*6 \pageBreak s2*9 \pageBreak s2*9 \pageBreak s1*3 \bar "||"
    \key g \major s4*9 \pageBreak s4*21 \pageBreak s4*27 \bar "||"
    \pageBreak s1*6 \pageBreak | \barNumberCheck #150
     \once \override NoteHead.style = ##f \stemDown cis4 s4*23
    \pageBreak | % 158
     \once \override NoteHead.style = ##f \stemDown cis4 s4*23
    \pageBreak s1*6 \pageBreak s1. \repeat volta 2 {
        s1*3 \pageBreak s2*9 \pageBreak s2*9 }
    s2. \bar "||"
    \pageBreak \repeat volta 2 {
        s4*21 \pageBreak s2*9 \pageBreak s4*21 \pageBreak s4*9 | % 216
         \once \override NoteHead.style = ##f \stemNeutral b2*1/2 \once
        \override NoteHead.style = ##f \stemNeutral cis2*1/2 \once
        \override NoteHead.style = ##f \stemNeutral b16 \stopTrillSpan
        \once \override NoteHead.style = ##f \stemNeutral cis16 s8*7 | % 218
         \once \override NoteHead.style = ##f \stemNeutral e2*1/2 \once
        \override NoteHead.style = ##f \stemNeutral fis2*1/2 \once
        \override NoteHead.style = ##f \stemNeutral e16 \stopTrillSpan
        \once \override NoteHead.style = ##f \stemNeutral fis16 s8*7 |
        \barNumberCheck #220
         \once \override NoteHead.style = ##f \stemNeutral f2*1/2 \once
        \override NoteHead.style = ##f \stemNeutral g2*1/2 \once
        \override NoteHead.style = ##f \stemNeutral f16 \stopTrillSpan
        \once \override NoteHead.style = ##f \stemNeutral g16 s8
        \pageBreak s2. | % 222
         \once \override NoteHead.style = ##f \stemNeutral f2*1/2 \once
        \override NoteHead.style = ##f \stemNeutral g2*1/2 \once
        \override NoteHead.style = ##f \stemNeutral f16 \stopTrillSpan
        \once \override NoteHead.style = ##f \stemNeutral g16 s8*25
        \pageBreak s4*15 \pageBreak s4*15 \pageBreak s4*9 }
    s4*9 \pageBreak s2*9 \bar "||"
    \pageBreak s4*27 \pageBreak s4*21 \pageBreak s4*21 \pageBreak s4*15
    \pageBreak s2*9 \pageBreak s4*15 \pageBreak s2*9 \pageBreak s4*21
    \bar "|."
    }

PartPOneEightVoiceOne =  \relative e'' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key g \major | % 1
        \stemDown e4 _\f r4 r4 | % 2
        R2. | % 3
        \stemDown b4 r4 r4 | % 4
        R2. \bar "||"
        R2.*3 \pageBreak | % 8
        R2. | % 9
        \stemUp b,4 _\p ^ "pizz." r4 r4 | \barNumberCheck #10
        \stemUp b4 r4 r4 | % 11
        \stemUp b4 _\pp r4 r4 | % 12
        \stemUp b4 _\> r4 r4 | % 13
        \stemUp b4 _\! _\ppp r4 r4 | % 14
        \stemUp b4 r4 r4 \pageBreak | % 15
        \stemUp b4 r4 r4 | % 16
        \stemUp b4 r4 r4 | % 17
        \stemUp b4 r4 r4 | % 18
        \stemUp b4 r4 r4 | % 19
        \stemUp b4 r4 r4 | \barNumberCheck #20
        \stemUp b4 r4 r4 \pageBreak | % 21
        \stemUp e8 ( _\pp ^ "arco" \stemUp fis8 \stemUp g8 \stemUp fis8
        _\< \stemUp g8 \stemUp a8 | % 22
        \stemDown b8 \stemDown d8 _\! \stemDown c8 _\> \stemDown b8
        \stemDown a8 \stemDown g8 ) | % 23
        \stemUp fis8 ( _\! \stemUp g8 \stemUp a8 \stemUp b8 \stemUp c8
        \stemUp d8 | % 24
        \stemUp b8 \stemUp a8 \stemUp g8 \stemUp fis8 \stemUp e8 \stemUp
        fis8 ) | % 25
        \stemUp e8 ( \stemUp fis8 \stemUp g8 \stemUp fis8 _\< \stemUp g8
        \stemUp a8 \pageBreak | % 26
        \stemUp b8 \stemUp d8 _\! \stemUp c8 _\> \stemUp b8 \stemUp a8
        \stemUp g8 ) | % 27
        \stemUp fis8 ( _\! \stemUp g8 \stemUp a8 \stemUp b8 \stemUp c8
        \stemUp d8 | % 28
        \stemUp b8 \stemUp a8 \stemUp g8 \stemUp fis8 \stemUp e8 \stemUp
        fis8 ) | % 29
        \stemUp e8 r8 r4 r4 | \barNumberCheck #30
        R2. \pageBreak | % 31
        R2.*2 | % 33
        r4 \stemUp dis8 -. _\ff \stemUp dis8 -. \stemUp e4 -. | % 34
        \stemUp dis4 -. \stemUp dis4 -. \stemUp e4 -. | % 35
        \stemUp dis8 -. \stemUp dis8 -. \stemUp e4 -. \stemUp b4 -.
        \pageBreak | % 36
        \stemUp b4 -. \stemUp b4 -. \stemUp b4 -. | % 37
        \stemUp b4 -. \stemDown dis'8 -. \stemDown dis8 -. \stemDown b4
        -. | % 38
        \stemDown dis4 -. \stemDown dis4 -. \stemDown b4 -. | % 39
        \stemDown dis8 -. \stemDown dis8 -. \stemDown b4 -. \stemDown g'4
        -. | \barNumberCheck #40
        \stemDown e4 -. \stemDown g4 -. \stemDown e4 -. | % 41
        \stemDown g4 -. \stemDown b8 \stemDown b8 \stemDown b4
        \pageBreak | % 42
        \stemDown e,4 -. \stemDown e4 -. r4 | % 43
        r4 \stemDown fis4 -. \stemDown a4 -. | % 44
        \stemDown g8 \stemDown fis8 \stemDown e4 r4 | % 45
        r4 \stemDown b'8 \stemDown b8 \stemDown b4 | % 46
        \stemDown e,4 -. \stemDown e4 -. r4 \pageBreak | % 47
        r4 \stemDown fis4 -. \stemDown a4 -. | % 48
        \stemDown g8 \stemDown fis8 \stemDown e4 \stemDown e8 \stemDown
        b8 | % 49
        \stemDown g'2. :32 | \barNumberCheck #50
        \stemDown g2 :16 \stemDown a4 :16 | % 51
        \stemDown a2. :16 | % 52
        \stemDown b8 \stemDown a8 \stemDown g2 :16 \pageBreak | % 53
        \stemDown g2. :16 | % 54
        \stemDown g2 :16 \stemDown a4 :16 | % 55
        \stemDown a2. :16 | % 56
        \stemDown b8 \stemDown a8 \stemDown g4 \stemDown fis4 | % 57
        \stemDown b8 \stemDown a8 \stemDown g4 \stemDown fis4 | % 58
        \stemDown b8 \stemDown a8 \stemDown g4 \stemDown fis4 | % 59
        \stemDown b8 \stemDown a8 \stemDown g4 r4 }
    \pageBreak | \barNumberCheck #60
    \stemDown e4 -. _\fp \stemDown g4 -. r4 | % 61
    \stemDown e8 _\f \stemDown c8 \stemDown b4 -. _\p r4 | % 62
    R2.*2 | % 64
    \stemUp g8 _\p \stemUp g16 r16 r4 \stemUp fis8 \stemUp fis16 r16 | % 65
    \stemUp g8 \stemUp g16 r16 r4 \stemUp fis8 \stemUp fis16 r16 | % 66
    \stemUp g8 \stemUp g16 r16 r4 \stemUp fis8 \stemUp fis16 r16
    \pageBreak | % 67
    \stemUp gis8 \stemUp gis16 r16 r4 \stemUp fis8 \stemUp fis16 r16
    \bar "||"
    \key e \major \stemUp <b, gis'>8 _\pp \stemUp <b gis'>16 r16 r4
    \stemUp <b fis'>8 \stemUp <b fis'>16 r16 | % 69
    \stemUp <b gis'>8 \stemUp <b gis'>16 r16 r4 \stemUp <b fis'>8
    \stemUp <b fis'>16 r16 | \barNumberCheck #70
    \stemUp <b gis'>8 \stemUp <b gis'>16 r16 r4 \stemUp <b fis'>8
    \stemUp <b fis'>16 r16 | % 71
    \stemUp <b gis'>8 \stemUp <b gis'>16 r16 r4 \stemUp <b fis'>8
    \stemUp <b fis'>16 r16 \pageBreak | % 72
    \stemUp <b gis'>8 \stemUp <b gis'>16 r16 r4 \stemDown b'8 \stemDown
    b16 r16 | % 73
    \stemUp <b, gis'>8 \stemUp <b gis'>16 r16 r4 \stemDown b'8 \stemDown
    b16 r16 | % 74
    \stemUp <b, gis'>8 \stemUp <b gis'>16 r16 r4 \stemDown b'8 \stemDown
    b16 r16 | % 75
    \stemUp fis8 \stemUp fis16 r16 r4 \stemUp <b, gis'>8 \stemUp <b
        gis'>16 r16 | % 76
    \stemUp <b gis'>8 \stemUp <b gis'>16 r16 r4 \stemUp <b fis'>8
    \stemUp <b fis'>16 r16 \pageBreak | % 77
    \stemUp <b gis'>8 \stemUp <b gis'>16 r16 r4 \stemUp <b fis'>8
    \stemUp <b fis'>16 r16 | % 78
    \stemUp <b gis'>8 \stemUp <b gis'>16 r16 r4 \stemUp <b fis'>8
    \stemUp <b fis'>16 r16 | % 79
    \stemUp <b gis'>8 \stemUp <b gis'>16 r16 r4 \stemUp <b fis'>8
    \stemUp <b fis'>16 r16 | \barNumberCheck #80
    \stemUp <b gis'>8 \stemUp <b gis'>16 r16 r4 \stemDown b'8 \stemDown
    b16 r16 | % 81
    \stemUp <b, gis'>8 \stemUp <b gis'>16 r16 r4 \stemDown b'8 \stemDown
    b16 r16 \pageBreak | % 82
    \stemUp <b, gis'>8 \stemUp <b gis'>16 r16 r4 \stemDown b'8 \stemDown
    b16 r16 | % 83
    \stemUp fis4 r4 \stemUp <b, gis'>8 \stemUp <b gis'>16 r16 | % 84
    \stemUp <cis a'>8 _\fz \stemUp <cis a'>16 r16 r4 \stemUp <cis a'>8
    \stemUp <cis a'>16 r16 | % 85
    \stemUp <cis a'>8 _\fz \stemUp <cis a'>16 r16 r4 \stemUp <cis a'>8
    \stemUp <cis a'>16 r16 | % 86
    \stemUp <b gis'>8 _\fz \stemUp <b gis'>16 r16 r4 \stemDown b'8 _\pp
    \stemDown b16 r16 \pageBreak | % 87
    \stemUp <b, gis'>8 \stemUp <b gis'>16 r16 r4 \stemUp <gis' b>8
    \stemUp <gis b>16 r16 | % 88
    \stemUp <cis, a'>8 _\fp \stemUp <cis a'>16 r16 r4 \stemUp <cis a'>8
    \stemUp <cis a'>16 r16 | % 89
    \stemUp <cis a'>8 _\fp \stemUp <cis a'>16 r16 r4 \stemUp <cis a'>8
    \stemUp <cis a'>16 r16 | \barNumberCheck #90
    \stemUp <b gis'>8 _\fp \stemUp <b gis'>16 r16 r4 \stemDown b'8 _\pp
    \stemDown b16 r16 | % 91
    \stemUp <b, gis'>8 \stemUp <b gis'>16 r16 r4 \stemUp <b gis'>8
    \stemUp <b gis'>16 r16 \pageBreak | % 92
    \stemUp <b gis'>4 r4 r4 | % 93
    R2.*6 \pageBreak | % 99
    \stemUp d4 ( -. _\ppp \stemUp d4 -. \stemUp d4 ) -. |
    \barNumberCheck #100
    \stemUp d4 ( -. \stemUp d4 -. \stemUp d4 ) -. | % 101
    \stemUp d4 ( -. \stemUp d4 -. \stemUp d4 ) -. | % 102
    \stemUp d4 ( -. \stemUp d4 -. \stemUp d4 ) -. | % 103
    \stemUp d4 ( -. \stemUp d4 -. \stemUp d4 ) -. | % 104
    \stemUp d4 ( -. \stemUp d4 -. \stemUp d4 ) -. | % 105
    \stemUp d4 ( -. \stemUp d4 -. \stemUp d4 ) -. | % 106
    \stemUp d4 ( -. \stemUp d4 -. \stemUp d4 ) -. \pageBreak | % 107
    r4 \stemDown b'8 _\pp \stemDown b8 \stemDown b4 | % 108
    \stemUp e,4 -. \stemUp e4 -. r4 | % 109
    r4 \stemDown c'8 \stemDown c8 \stemDown c4 | \barNumberCheck #110
    \stemUp f,4 -. _\< \stemUp f4 -. r4 _\! | % 111
    r4 \stemDown cis'8 \stemDown cis8 \stemDown cis4 | % 112
    \stemUp fis,4 -. \stemUp fis4 -. r4 \pageBreak | % 113
    r4 \stemDown d'8 _\mf _\< \stemDown d8 \stemDown d4 | % 114
    r4 \stemDown dis8 \stemDown dis8 \stemDown dis4 | % 115
    r4 \stemDown e8 \stemDown e8 \stemDown e4 | % 116
    r4 _\! \stemDown f8 _\f \stemDown f8 \stemDown f4 | % 117
    r4 _\markup{ \italic {più} } \stemDown fis8 _\f \stemDown fis8
    \stemDown fis4 | % 118
    \stemDown g8 _\< \stemDown g8 \stemDown g4 \stemDown gis8 \stemDown
    gis8 \pageBreak | % 119
    \stemDown gis4 \stemDown a8 _\! \stemDown a8 \stemDown a4 |
    \barNumberCheck #120
    \stemDown a8 \stemDown a8 \stemDown a4 \stemDown a8 \stemDown a8 | % 121
    \stemDown a4 \stemDown a8 \stemDown a8 \stemDown a4 | % 122
    \stemDown a8 \stemDown a8 \stemDown a8 \stemDown ais8 \stemDown b8
    \stemDown b,8 \bar "||"
    \key g \major \stemDown e8 _\fff r8 \stemDown b'8 \stemDown b8
    \stemDown b4 | % 124
    \stemDown e,4 -. \stemDown e4 -. r4 | % 125
    r4 \stemDown fis4 -. \stemDown a4 -. \pageBreak | % 126
    \stemDown g8 \stemDown fis8 \stemDown e4 r4 | % 127
    r4 \stemDown b'8 \stemDown b8 \stemDown b4 | % 128
    \stemDown e,4 -. \stemDown e4 -. r4 | % 129
    r4 \stemDown fis4 -. \stemDown a4 -. | \barNumberCheck #130
    \stemDown g8 \stemDown fis8 \stemDown e4 \stemDown a4 | % 131
    \stemDown g8 \stemDown fis8 \stemDown e4 \stemDown a4 | % 132
    \stemDown g8 \stemDown fis8 \stemDown e4 \stemDown a4 \pageBreak | % 133
    \stemDown g8 \stemDown fis8 \stemDown e4 \stemDown a4 | % 134
    \stemDown g8 \stemDown fis8 \stemDown e4 r4 | % 135
    \stemDown g8 \stemDown fis8 \stemDown e4 r4 | % 136
    \stemDown g8 \stemDown fis8 \stemDown e4 r4 | % 137
    \stemDown g8 \stemDown fis8 \stemDown e4 r4 | % 138
    \stemDown g8 _\ffz \stemDown fis8 \stemDown e2 ~ _\> | % 139
    \stemDown e2. | \barNumberCheck #140
    \stemDown g8 _\! _\ffz \stemDown fis8 \stemDown e2 ~ _\> | % 141
    \stemDown e2. \bar "||"
    \pageBreak | % 142
    R2.*3 | % 145
    r4 _\! \stemDown b8 _\p \stemDown b8 \stemDown b4 | % 146
    \stemUp e,4 -. \stemUp e4 -. r4 | % 147
    R2.*3 \pageBreak | \barNumberCheck #150
    R2.*8 \pageBreak | % 158
    R2.*2 | \barNumberCheck #160
    r4 r4 \stemUp f4 ( _\pp | % 161
    \stemUp es4 \stemUp as,4 ) \stemUp f'4 ( | % 162
    \stemUp es4 \stemUp as,4 \stemUp as'4 ) | % 163
    \stemUp f2. ( | % 164
    \stemUp es2. ~ | % 165
    \stemUp es4 ) r2 \pageBreak | % 166
    R2.*6 | % 172
    r4 \stemDown c'2 ~ _\ppp | % 173
    \stemDown c2. ~ \pageBreak | % 174
    \stemDown c2 r4 | % 175
    r4 r4 \stemUp a4 ( \repeat volta 2 {
        | % 176
        \stemUp g4 \stemUp c,4 \stemUp a'4 | % 177
        \stemUp g4 \stemUp c,4 ) \stemUp a'4 ( | % 178
        \stemUp g4 \stemUp c,4 ) \stemUp a'4 ( | % 179
        \stemUp g4 \stemUp c,4 \stemUp a'4 \pageBreak | \barNumberCheck
        #180
        \stemUp g4 \stemUp c,4 ) \stemUp a'4 ( | % 181
        \stemUp g4 \stemUp g,4 \stemUp f'4 | % 182
        \stemUp e4 \stemUp c4 ) \stemDown d'4 ( | % 183
        \stemDown c4 \stemUp e,4 \stemUp a4 | % 184
        \stemUp g4 \stemUp c,4 ) \stemUp a'4 ( | % 185
        \stemUp g4 \stemUp c,4 \stemUp a'4 \pageBreak | % 186
        \stemUp g4 \stemUp c,4 ) \stemUp a'4 ( | % 187
        \stemUp g4 \stemUp c,4 \stemUp a'4 | % 188
        \stemUp g4 \stemUp b,4 ) \stemUp g'4 ( | % 189
        \stemUp f4 \stemUp g4 \stemUp e4 ) | \barNumberCheck #190
        \stemUp e4 ( \stemUp c4 \stemUp d4 | % 191
        \stemUp g,4 \stemUp c4 ) \stemUp a'4 ( }
    | % 192
    \stemUp g,4 ) \stemUp c4 \stemDown c'4 -. \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
        \stemDown g'8 ( _\mf \stemDown b8 \stemDown g8 ) r8 \stemDown f8
        r8 | % 194
        \stemDown e2. \startTrillSpan ^ "[♮]" | % 195
        \stemDown d8 ( \stemDown fis8 \stemDown d8 ) r8 \stemDown c8 r8
        | % 196
        \stemDown b2. \startTrillSpan \stopTrillSpan | % 197
        \stemDown a8 ( _\p \stemDown c8 \stemUp a8 ) r8 \stemUp g8 r8 | % 198
        \stemUp fis2. \startTrillSpan \stopTrillSpan _\> | % 199
        \stemUp e8 ( _\! _\pp \stemUp g8 \stemUp e8 ) r8 \stemUp dis8 r8
        \pageBreak | \barNumberCheck #200
        \stemUp e2. \startTrillSpan \stopTrillSpan | % 201
        R2.*5 \pageBreak | % 206
        R2.*3 | % 209
        \stemUp b'2 _\pp \stemUp b8 r8 | \barNumberCheck #210
        \stemUp b2 \stemUp b8 r8 | % 211
        \stemUp b2 \stemUp b8 r8 | % 212
        \stemUp b2 \stemUp b8 r8 \pageBreak | % 213
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown b8 ( \stemDown gis'8 \stemDown b,8 }
        \stemDown gis'8 ) r8 \stemDown fis8 r8 | % 214
        \stemDown e2. \startTrillSpan \stopTrillSpan | % 215
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown b8 ( \stemDown gis'8 \stemDown b,8 }
        \stemDown gis'8 ) r8 \stemDown fis8 r8 | % 216
        \stemDown e2 ~ \startTrillSpan _\pp \stemDown e8 r8 | % 217
        R2. | % 218
        \stemDown b2 ~ \startTrillSpan ^ "♯" \stemDown b8 r8 | % 219
        R2. | \barNumberCheck #220
        \stemDown d2 ~ \startTrillSpan \stemDown d8 r8 \pageBreak | % 221
        R2. | % 222
        \stemDown d2 ~ \startTrillSpan \stemDown d8 r8 | % 223
        R2. | % 224
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown e8 ( _\pp \stemDown c8 \stemDown e8 }
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown c8 \stemDown e8 \stemDown c8 }
        \stemDown e8 ) r8 | % 225
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown e8 ( \stemDown c8 \stemDown e8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown c8 \stemDown e8 \stemDown c8 }
        \stemDown e8 ) r8 | % 226
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown e8 ( \stemDown c8 \stemDown e8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown c8 \stemDown e8 \stemDown c8 }
        \stemDown e8 ) r8 \pageBreak | % 227
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown e8 ( \stemDown c8 \stemDown e8 }
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown c8 \stemDown e8 \stemDown c8 }
        \stemDown e8 ) r8 | % 228
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown e8 ( \stemDown c8 \stemDown e8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown c8 \stemDown e8 \stemDown c8 }
        \stemDown e8 ) r8 | % 229
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown f8 ( \stemDown b,8 \stemDown f'8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown b,8 \stemDown f'8 \stemDown b,8 }
        \stemDown f'8 ) r8 | \barNumberCheck #230
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown e8 ( \stemDown c8 \stemDown e8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown c8 \stemDown e8 \stemDown c8 }
        \stemDown e8 ) r8 | % 231
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown e8 ( \stemDown c8 \stemDown e8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown c8 \stemDown e8 \stemDown c8 }
        \stemDown e8 ) r8 \pageBreak | % 232
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown e8 ( \stemDown c8 \stemDown e8 }
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown c8 \stemDown e8 \stemDown c8 }
        \stemDown e8 ) r8 | % 233
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown e8 ( \stemDown c8 \stemDown e8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown c8 \stemDown e8 \stemDown c8 }
        \stemDown e8 ) r8 | % 234
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown e8 ( \stemDown c8 \stemDown e8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown c8 \stemDown e8 \stemDown c8 }
        \stemDown e8 ) r8 | % 235
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown e8 ( \stemDown c8 \stemDown e8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown c8 \stemDown e8 \stemDown c8 }
        \stemDown e8 ) r8 | % 236
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown e8 ( \stemDown c8 \stemDown e8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown c8 \stemDown e8 \stemDown c8 }
        \stemDown e8 ) r8 \pageBreak | % 237
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown f8 ( \stemDown b,8 \stemDown f'8 }
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown b,8 \stemDown f'8 \stemDown b,8 }
        \stemDown g'8 ) r8 | % 238
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown e8 ( _\fz \stemDown c8 \stemDown e8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown c8 \stemDown e8 \stemDown c8 }
        \stemDown e8 ) r8 | % 239
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown e8 ( \stemDown c8 \stemDown e8 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown c8 \stemDown e8 \stemDown c8 }
        \stemDown e8 ) r8 }
    | \barNumberCheck #240
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp g,2. :16 _\pp }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp g4. :16 }
    | % 241
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp g2. :16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp g4. :16 }
    | % 242
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp as2. :16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp as4. :16 }
    \pageBreak | % 243
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp as2. :16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp as4. :16 }
    | % 244
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp <dis, b'>2. :16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp <dis b'>4. :16 }
    | % 245
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp <dis b'>2. :16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp <dis b'>4. :16 }
    | % 246
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp <fis dis'>2. :16 }
    _\< \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp <fis dis'>4. :16 }
    | % 247
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp <fis dis'>2. :16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown <a fis'>4. :16 }
    | % 248
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown <a fis'>2. :16 }
    _\! _\f _\< \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown <a fis'>4. :16 }
    \bar "||"
    \pageBreak | % 249
    \stemUp c,2. :32 _\! _\ff | \barNumberCheck #250
    \stemUp c2. :32 _\markup{ \italic {dim.} } _\> | % 251
    \stemUp c2. :32 _\! _\p _\> | % 252
    \stemUp c2. :32 _\! | % 253
    \stemUp c2. :32 _\pp | % 254
    \stemUp c2. :32 | % 255
    \stemUp c2. :32 | % 256
    \stemUp c2. :32 | % 257
    \stemUp c2. :32 \pageBreak | % 258
    \stemUp c2. :32 | % 259
    \stemUp c2. :32 | \barNumberCheck #260
    \stemUp c2. :32 | % 261
    \stemUp des2. :32 _\pp | % 262
    \stemUp des2. :32 | % 263
    \stemUp des2. :32 | % 264
    \stemUp des2. :32 \pageBreak | % 265
    \stemUp des2. :32 _\< | % 266
    \stemUp des2. :32 | % 267
    \stemUp des2. :32 | % 268
    \stemUp des2. :32 | % 269
    \stemUp <cis fis>2. :32 _\! _\fz | \barNumberCheck #270
    \stemUp <cis fis>2. :32 | % 271
    \stemUp <fis a>2. :32 _\p \pageBreak | % 272
    \stemUp <fis a>2. :32 _\< | % 273
    \stemDown cis'2. :32 | % 274
    \stemDown fis2. :32 _\! | % 275
    \stemDown a2. :32 _\f _\< | % 276
    \stemDown cis2. :32 \pageBreak | % 277
    \stemDown dis2. :32 _\! _\fff | % 278
    \stemDown dis2. :32 | % 279
    \stemDown dis2. :32 | \barNumberCheck #280
    \stemDown dis2. :32 | % 281
    \stemDown e8 r8 \stemDown b8 \stemDown b8 \stemDown b4 | % 282
    \stemDown e,4 -. \stemDown e4 -. r4 \pageBreak | % 283
    r4 \stemDown b8 \stemDown b8 \stemDown b4 _\> | % 284
    \stemUp e,4 -. \stemUp e4 -. r4 _\! | % 285
    R2.*3 \pageBreak | % 288
    R2.*6 \pageBreak | % 294
    R2.*6 | \barNumberCheck #300
    \stemDown <e b' g'>4 _\ff r4 r4 \bar "|."
    }

PartPOneEightVoiceTwo =  \relative cis'' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key g \major s1*3 \bar "||"
        s4*9 \pageBreak s4*21 \pageBreak s2*9 \pageBreak s4*15
        \pageBreak s4*15 \pageBreak s4*15 \pageBreak s2*9 \pageBreak
        s4*15 \pageBreak s2*9 \pageBreak s4*21 }
    \pageBreak s4*21 \pageBreak s2. \bar "||"
    \key e \major s1*3 \pageBreak s4*15 \pageBreak s4*15 \pageBreak
    s4*15 \pageBreak s4*15 \pageBreak s4*21 \pageBreak s1*6 \pageBreak
    s2*9 \pageBreak s2*9 \pageBreak s1*3 \bar "||"
    \key g \major s4*9 \pageBreak s4*21 \pageBreak s4*27 \bar "||"
    \pageBreak s1*6 \pageBreak | \barNumberCheck #150
     \once \override NoteHead.style = ##f \stemDown cis4 s4*23
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1. \repeat volta 2 {
        s1*3 \pageBreak s2*9 \pageBreak s2*9 }
    s2. \bar "||"
    \pageBreak \repeat volta 2 {
        s2. | % 194
         \once \override NoteHead.style = ##f \stemNeutral e2.*1/2 \once
        \override NoteHead.style = ##f \stemNeutral f2.*1/2
        \stopTrillSpan s4*15 \pageBreak s2*9 \pageBreak s4*9 | % 209
        \stemDown a,2 \stemDown a8 s8 | \barNumberCheck #210
        \stemDown g2 \stemDown g8 s8 | % 211
        \stemDown a2 \stemDown a8 s8 | % 212
        \stemDown g2 \stemDown g8 s8 \pageBreak s4*9 | % 216
         \once \override NoteHead.style = ##f \stemNeutral e'2*1/2 \once
        \override NoteHead.style = ##f \stemNeutral fis2*1/2 \once
        \override NoteHead.style = ##f \stemNeutral e16 \stopTrillSpan
        \once \override NoteHead.style = ##f \stemNeutral fis16 s8*7 | % 218
         \once \override NoteHead.style = ##f \stemNeutral b,2*1/2 \once
        \override NoteHead.style = ##f \stemNeutral cis2*1/2 \once
        \override NoteHead.style = ##f \stemNeutral b8*1/2
        \stopTrillSpan \once \override NoteHead.style = ##f \stemNeutral
        cis8*1/2 s8*7 | \barNumberCheck #220
         \once \override NoteHead.style = ##f \stemNeutral d2*1/2 \once
        \override NoteHead.style = ##f \stemNeutral e2*1/2 \once
        \override NoteHead.style = ##f \stemNeutral d16 \stopTrillSpan
        \once \override NoteHead.style = ##f \stemNeutral e16 s8
        \pageBreak s2. | % 222
         \once \override NoteHead.style = ##f \stemNeutral d2*1/2 \once
        \override NoteHead.style = ##f \stemNeutral e2*1/2 \once
        \override NoteHead.style = ##f \stemNeutral d16 \stopTrillSpan
        \once \override NoteHead.style = ##f \stemNeutral e16 s8*25
        \pageBreak s4*15 \pageBreak s4*15 \pageBreak s4*9 }
    s4*9 \pageBreak s2*9 \bar "||"
    \pageBreak s4*27 \pageBreak s4*21 \pageBreak s4*21 \pageBreak s4*15
    \pageBreak s2*9 \pageBreak s4*15 \pageBreak | % 288
     \once \override NoteHead.style = ##f \stemDown cis4 s4*17
    \pageBreak s4*21 \bar "|."
    }

PartPOneNineVoiceOne =  \relative e' {
    \repeat volta 2 {
        \clef "alto" \time 3/4 \key g \major | % 1
        \stemDown e4 _\f r4 r4 | % 2
        R2. | % 3
        \stemUp b4 r4 r4 | % 4
        R2. \bar "||"
        R2.*2 | % 7
        \stemUp g8 _\f \stemUp g8 \stemUp g2 \pageBreak | % 8
        \stemUp g2. ~ _\fz _\> | % 9
        \stemUp g2. ~ _\! _\p | \barNumberCheck #10
        \stemUp g2. ~ | % 11
        \stemUp g2. ~ _\pp | % 12
        \stemUp g2. ~ _\> | % 13
        \stemUp g2. ~ _\! _\ppp | % 14
        \stemUp g2. ~ \pageBreak | % 15
        \stemUp g2. ~ | % 16
        \stemUp g2. ~ | % 17
        \stemUp g2. ~ | % 18
        \stemUp g2. ~ | % 19
        \stemUp g2. ~ | \barNumberCheck #20
        \stemUp g2. \pageBreak | % 21
        \stemDown e'4 _\p ^ "pizz." \stemUp e,4 r4 | % 22
        R2. | % 23
        \stemDown e'4 \stemUp e,4 r4 | % 24
        R2. | % 25
        \stemDown e'4 \stemUp e,4 r4 \pageBreak | % 26
        R2. | % 27
        \stemDown e'4 \stemUp e,4 r4 | % 28
        R2. | % 29
        r4 \stemDown e'4 -. _\mf ^ "arco" \stemDown g4 -. |
        \barNumberCheck #30
        \stemDown e8 \stemDown d8 \stemUp b4 -. \stemDown d8 \stemDown b8
        \pageBreak | % 31
        \stemUp g4 -. _\f _\< \stemDown g'8 \stemDown e8
        \stemDown d8 \stemDown g8 | % 32
        \stemDown e8 \stemDown d8 \stemDown b8 \stemDown e8 \stemDown d8
        \stemDown b8 | % 33
        r4 _\! \stemUp b8 -. _\ff \stemUp b8 -. \stemUp b4 -. | % 34
        \stemUp b4 -. \stemUp b4 -. \stemUp b4 -. | % 35
        \stemUp b8 -. \stemUp b8 -. \stemUp b4 -. \stemDown g'8 -.
        \stemDown g8 -. \pageBreak | % 36
        \stemDown e4 -. \stemDown g4 -. \stemDown e4 -. | % 37
        \stemDown g4 -. \stemDown b8 -. \stemDown b8 -. \stemDown g4 -.
        | % 38
        \stemDown b4 -. \stemDown b4 -. \stemDown g4 -. | % 39
        \stemDown b8 -. \stemDown b8 -. \stemDown g4 -. \stemDown b4 -.
        | \barNumberCheck #40
        \stemDown b4 -. \stemDown b4 -. \stemDown b4 -. | % 41
        \stemDown b4 -. \stemUp g,8 \stemUp e8 \stemUp g8 \stemUp e8
        \pageBreak | % 42
        \stemUp g8 \stemUp e8 \stemUp g8 \stemUp e8 \stemUp g8 \stemUp e8
        | % 43
        \stemUp a8 \stemUp e8 \stemUp a8 \stemUp e8 \stemUp a8 \stemUp e8
        | % 44
        \stemUp b'8 \stemUp e,8 \stemUp g8 \stemUp e8 \stemUp g8 \stemUp
        e8 | % 45
        \stemUp g8 \stemUp e8 \stemUp g8 \stemUp e8 \stemUp g8 \stemUp e8
        | % 46
        \stemUp g8 \stemUp e8 \stemUp g8 \stemUp e8 \stemUp g8 \stemUp e8
        \pageBreak | % 47
        \stemUp a8 \stemUp e8 \stemUp a8 \stemUp e8 \stemUp a8 \stemUp e8
        | % 48
        \stemUp b'8 \stemUp e,8 \stemUp g8 \stemUp e8 \stemUp g8 \stemUp
        b8 | % 49
        \stemDown e8 r8 \stemDown g2 :16 | \barNumberCheck #50
        \stemDown g2 :16 \stemDown a4 :16 | % 51
        \stemDown a2. :16 | % 52
        \stemDown b8 \stemDown a8 \stemDown g2 :16 \pageBreak | % 53
        \stemDown g2. :16 | % 54
        \stemDown g2 :16 \stemDown a4 :16 | % 55
        \stemDown a2. | % 56
        \stemDown e'8 \stemDown e8 \stemDown e4 \stemDown e4 | % 57
        \stemDown e8 \stemDown e8 \stemDown e4 \stemDown e4 | % 58
        \stemDown e8 \stemDown e8 \stemDown e4 \stemDown e4 | % 59
        \stemDown e8 \stemDown e8 \stemDown e4 r4 }
    \pageBreak | \barNumberCheck #60
    R2. | % 61
    \stemDown e,4 -. _\fp \stemDown g4 -. r4 | % 62
    R2.*2 | % 64
    \stemUp b,8 _\p \stemUp b16 r16 r4 \stemDown dis8 \stemDown dis16 r16
    | % 65
    \stemUp b8 \stemUp b16 r16 r4 \stemDown dis8 \stemDown dis16 r16 | % 66
    \stemUp b8 \stemUp b16 r16 r4 \stemDown dis8 \stemDown dis16 r16
    \pageBreak | % 67
    \stemUp b8 \stemUp b16 r16 r4 \stemDown dis8 \stemDown dis16 r16
    \bar "||"
    \key e \major \stemDown e8 _\pp \stemDown e16 r16 r4 \stemDown dis8
    \stemDown dis16 r16 | % 69
    \stemDown e8 \stemDown e16 r16 r4 \stemDown dis8 \stemDown dis16 r16
    | \barNumberCheck #70
    \stemDown e8 \stemDown e16 r16 r4 \stemDown dis8 \stemDown dis16 r16
    | % 71
    \stemDown e8 \stemDown e16 r16 r4 \stemDown dis8 \stemDown dis16 r16
    \pageBreak | % 72
    \stemDown e8 \stemDown e16 r16 r4 \stemDown <b dis>8 \stemDown <b
        dis>16 r16 | % 73
    \stemDown e8 \stemDown e16 r16 r4 \stemDown <b dis>8 \stemDown <b
        dis>16 r16 | % 74
    \stemDown e8 \stemDown e16 r16 r4 \stemDown <b dis>8 \stemDown <b
        dis>16 r16 | % 75
    \stemDown <b dis>8 \stemDown <b dis>16 r16 r4 \stemDown e8 \stemDown
    e16 r16 | % 76
    \stemDown e8 \stemDown e16 r16 r4 \stemDown dis8 \stemDown dis16 r16
    \pageBreak | % 77
    \stemDown e8 \stemDown e16 r16 r4 \stemDown dis8 \stemDown dis16 r16
    | % 78
    \stemDown e8 \stemDown e16 r16 r4 \stemDown dis8 \stemDown dis16 r16
    | % 79
    \stemDown e8 \stemDown e16 r16 r4 \stemDown dis8 \stemDown dis16 r16
    | \barNumberCheck #80
    \stemDown e8 \stemDown e16 r16 r4 \stemDown <b dis>8 \stemDown <b
        dis>16 r16 | % 81
    \stemDown e8 \stemDown e16 r16 r4 \stemDown <b dis>8 \stemDown <b
        dis>16 r16 \pageBreak | % 82
    \stemDown e8 \stemDown e16 r16 r4 \stemDown <b dis>8 \stemDown <b
        dis>16 r16 | % 83
    \stemDown <b dis>4 r4 \stemDown e8 \stemDown e16 r16 | % 84
    \stemDown <cis e>8 _\fz \stemDown <cis e>16 r16 r4 \stemDown <cis e>8
    \stemDown <cis e>16 r16 | % 85
    \stemDown <cis e>8 _\fz \stemDown <cis e>16 r16 r4 \stemDown <cis e>8
    \stemDown <cis e>16 r16 | % 86
    \stemDown <b e>8 _\fz \stemDown <b e>16 r16 r4 \stemDown <b dis>8
    _\pp \stemDown <b dis>16 r16 \pageBreak | % 87
    \stemDown <b e>8 \stemDown <b e>16 r16 r4 \stemDown <e gis>8
    \stemDown <e gis>16 r16 | % 88
    \stemDown <cis e>8 _\fp \stemDown <cis e>16 r16 r4 \stemDown <cis e>8
    \stemDown <cis e>16 r16 | % 89
    \stemDown <cis e>8 _\fp \stemDown <cis e>16 r16 r4 \stemDown <cis e>8
    \stemDown <cis e>16 r16 | \barNumberCheck #90
    \stemDown <b e>8 _\fp \stemDown <b e>16 r16 r4 \stemDown <b dis>8
    _\pp \stemDown <b dis>16 r16 | % 91
    \stemDown <b e>8 \stemDown <b e>16 r16 r4 \stemDown <b e>8 \stemDown
    <b e>16 r16 \pageBreak | % 92
    \stemDown <b e>4 r4 r4 | % 93
    R2.*6 \pageBreak | % 99
    \stemUp gis4 ( -. _\ppp \stemUp gis4 -. \stemUp gis4 ) -. |
    \barNumberCheck #100
    \stemUp gis4 ( -. \stemUp gis4 -. \stemUp gis4 ) -. | % 101
    \stemUp a4 ( -. \stemUp a4 -. \stemUp fis4 ) -. | % 102
    \stemUp b4 ( -. \stemUp gis4 -. \stemUp gis4 ) -. | % 103
    \stemUp gis4 ( -. \stemUp gis4 -. \stemUp gis4 ) -. | % 104
    \stemUp gis4 ( -. \stemUp gis4 -. \stemUp gis4 ) -. | % 105
    \stemUp a4 ( -. \stemUp a4 -. \stemUp fis4 ) -. | % 106
    \stemUp b4 ( -. \stemUp gis4 -. \stemUp gis4 ) -. \pageBreak | % 107
    \stemUp d'8 _\pp \stemUp d8 \stemUp d8 \stemUp d8 \stemUp d8
    \stemUp d8 | % 108
    \stemUp d8 \stemUp d8 \stemUp d8 \stemUp d8 \stemUp d8 \stemUp d8 | % 109
    \stemUp c8 \stemUp c8 \stemUp c8 \stemUp c8 \stemUp c8 \stemUp c8 |
    \barNumberCheck #110
    \stemUp c8 _\< \stemUp c8 \stemUp c8 \stemUp c8 \stemUp es8 \stemUp
    es8 | % 111
    \stemUp cis8 \stemUp cis8 \stemUp cis8 \stemUp cis8 \stemUp cis8
    \stemUp cis8 | % 112
    \stemUp cis8 \stemUp cis8 \stemUp cis8 \stemUp cis8 \stemUp e8 _\!
    \stemUp e8 \pageBreak | % 113
    \stemUp d8 _\mf \stemUp d8 \stemUp d8 \stemUp d8 \stemUp f8 \stemUp
    f8 | % 114
    \stemUp dis8 _\< \stemUp dis8 \stemUp dis8 \stemUp dis8 \stemUp fis8
    \stemUp fis8 | % 115
    \stemUp e8 \stemUp e8 \stemUp e8 \stemUp e8 \stemUp g8 \stemUp g8 | % 116
    \stemUp f8 _\! _\f \stemUp f8 \stemUp f8 \stemUp f8 \stemUp as8
    \stemUp as8 | % 117
    \stemDown <dis, fis>8 _\f _\markup{ \italic {più} } \stemDown <dis
        a'>8 \stemDown <dis a'>8 \stemDown <dis a'>8 _\markup{ \italic
        {cresc.} } _\< \stemDown <dis a'>8 \stemDown <dis a'>8 | % 118
    \stemDown <dis a'>8 \stemDown <dis a'>8 \stemDown <dis a'>8
    \stemDown <dis a'>8 \stemDown <dis gis>8 \stemDown <dis gis>8
    \pageBreak | % 119
    \stemDown <dis gis>8 _\! \stemDown <dis gis>8 \stemDown <dis fis>8
    \stemDown <fis a>8 \stemDown <fis a>8 \stemDown <fis a>8 |
    \barNumberCheck #120
    \stemDown <fis a>8 \stemDown <fis a>8 \stemDown <fis a>8 \stemDown
    <fis a>8 \stemDown <fis a>8 \stemDown <fis a>8 | % 121
    \stemDown <fis a>8 \stemDown <fis a>8 \stemDown <fis a>8 \stemDown
    <fis a>8 \stemDown <fis a>8 \stemDown <fis a>8 | % 122
    \stemDown <dis fis>8 \stemDown <dis fis>8 \stemDown <dis fis>8
    \stemDown <dis fis>8 \stemDown <dis fis>8 \stemDown <dis fis>8 \bar
    "||"
    \key g \major \stemUp g2. :16 _\fff | % 124
    \stemUp g2. :16 | % 125
    \stemUp fis2. :16 \pageBreak | % 126
    \stemUp fis4 :8 \stemUp g2 :8 | % 127
    \stemUp g2. :8 | % 128
    \stemUp g2. :8 | % 129
    \stemUp fis2. :8 | \barNumberCheck #130
    \stemDown <b, e>8 \stemDown <b e>8 \stemDown <e g>8 \stemDown <e g>8
    \stemDown <fis c'>8 \stemDown <fis c'>8 | % 131
    \stemDown <g b>8 \stemDown <g b>8 \stemDown <e g>8 \stemDown <e g>8
    \stemDown <c fis>8 \stemDown <c fis>8 | % 132
    \stemDown <b e>8 \stemDown <b e>8 \stemDown <e g>8 \stemDown <e g>8
    \stemDown <fis c'>8 \stemDown <fis c'>8 \pageBreak | % 133
    \stemDown <g b>8 \stemDown <g b>8 \stemDown <e g>8 \stemDown <e g>8
    \stemDown <c fis>8 \stemDown <c fis>8 | % 134
    \stemDown <b g'>8 \stemDown fis'8 \stemDown e4 r4 | % 135
    \stemDown <b g'>8 \stemDown fis'8 \stemDown e4 r4 | % 136
    \stemDown <b g'>8 \stemDown fis'8 \stemDown e4 r4 | % 137
    \stemDown <b g'>8 \stemDown fis'8 \stemDown e4 r4 | % 138
    \stemDown <b g'>8 _\ffz \stemDown fis'8 \stemDown e2 ~ _\> | % 139
    \stemDown e2. | \barNumberCheck #140
    \stemDown <b g'>8 _\! _\ffz \stemDown fis'8 \stemDown e2 ~ _\> | % 141
    \stemDown e2. \bar "||"
    \pageBreak | % 142
    R2.*5 | % 147
    r4 _\! \stemUp b8 _\pp \stemUp b8 \stemUp b4 | % 148
    \stemUp e,4 -. \stemUp e4 -. r4 | % 149
    R2. \pageBreak | \barNumberCheck #150
    r4 \stemUp b'8 _\ppp \stemUp b8 \stemUp b4 | % 151
    \stemUp e,4 r4 r4 | % 152
    r4 \stemUp b'8 \stemUp b8 \stemUp b4 | % 153
    \stemUp e,4 r4 r4 | % 154
    R2.*4 \pageBreak | % 158
    R2. | % 159
    r4 r4 \stemDown e'4 ( _\pp | \barNumberCheck #160
    \stemDown es4 \stemUp as,4 ) r4 | % 161
    R2.*4 | % 165
    r4 r4 \stemUp as4 _\pp \pageBreak | % 166
    \stemUp as2 ( \stemDown ces4 | % 167
    \stemDown es4 _\< \stemDown as2 ) | % 168
    \stemDown ces2 ( \stemDown as4 _\! _\> | % 169
    \stemDown g4 \stemDown es2 ) ~ -> | \barNumberCheck #170
    \stemDown es2. ~ _\! _\markup{ \italic {dim.} } _\> | % 171
    \stemDown es2. | % 172
    \stemDown e2. ~ _\! _\ppp | % 173
    \stemDown e2. ~ \pageBreak | % 174
    \stemDown e2 r4 | % 175
    R2. \repeat volta 2 {
        | % 176
        R2.*4 \pageBreak | \barNumberCheck #180
        R2.*6 \pageBreak | % 186
        R2.*6 }
    | % 192
    R2. \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
        R2.*7 \pageBreak | \barNumberCheck #200
        R2. | % 201
        \times 2/3  {
            \stemDown g8 _\pp \stemDown g8 \stemDown g8 }
        \times 2/3  {
            \stemDown a8 \stemDown a8 \stemDown a8 }
        \times 2/3  {
            \stemDown b8 \stemDown b8 \stemDown b8 }
        | % 202
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown c4. :16 }
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown c,4. :16 }
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown c'4. :16 }
        | % 203
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown a4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown d,4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown fis4. :16 }
        | % 204
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown g4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemUp g,4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown g'4. :16 }
        | % 205
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown c,4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown d4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown e4. :16 }
        \pageBreak | % 206
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown f4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemUp f,4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown f'4. :16 }
        | % 207
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown dis4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemUp b4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown dis4. :16 }
        | % 208
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown e4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemUp b4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemUp e,4. :16 }
        | % 209
        \stemDown dis'2 _\pp \stemDown dis8 r8 | \barNumberCheck #210
        \stemDown e2 \stemDown e8 r8 | % 211
        \stemDown dis2 \stemDown dis8 r8 | % 212
        \stemDown e2 \stemDown e8 r8 \pageBreak | % 213
        \stemDown <dis a'>2 ^ "div." \stemDown <dis a'>8 r8 | % 214
        \stemDown <e gis>2 \stemDown <e gis>8 r8 | % 215
        \stemDown <dis a'>2 \stemDown <dis a'>8 r8 | % 216
        \stemDown <e gis>2 ~ \startTrillSpan ~ _\pp \stemDown <e gis>8 r8
        | % 217
        R2. | % 218
        \stemDown gis2 ~ \startTrillSpan \stemDown gis8 r8 | % 219
        R2. | \barNumberCheck #220
        \stemDown a2 ~ \startTrillSpan \stemDown a8 r8 \pageBreak | % 221
        R2. | % 222
        \stemDown a2 ~ \startTrillSpan \stemDown a8 r8 | % 223
        R2. | % 224
        \stemDown g8 _\pp \stemDown g8 \stemDown c,8 \stemDown c8
        \stemDown a'8 \stemDown a8 | % 225
        \stemDown g8 \stemDown g8 \stemDown c,8 \stemDown c8 \stemDown
        a'8 \stemDown a8 | % 226
        \stemDown g8 \stemDown g8 \stemDown c,8 \stemDown c8 \stemDown
        a'8 \stemDown a8 \pageBreak | % 227
        \stemDown g8 \stemDown g8 \stemDown c,8 \stemDown c8 \stemDown
        a'8 \stemDown a8 | % 228
        \stemDown g8 \stemDown g8 \stemDown c,8 \stemDown c8 \stemDown
        a'8 \stemDown a8 | % 229
        \stemDown g8 \stemDown g8 \stemUp g,8 \stemUp g8 \stemDown f'8
        \stemDown f8 | \barNumberCheck #230
        \stemDown e8 \stemDown e8 \stemUp g,8 \stemUp g8 \stemDown d'8
        \stemDown d8 | % 231
        \stemDown c8 \stemDown c8 \stemDown e8 \stemDown e8 \stemDown c8
        \stemDown c8 \pageBreak | % 232
        \stemDown g'8 \stemDown g8 \stemDown c,8 \stemDown c8 \stemDown
        a'8 \stemDown a8 | % 233
        \stemDown g8 \stemDown g8 \stemDown c,8 \stemDown c8 \stemDown
        a'8 \stemDown a8 | % 234
        \stemDown g8 \stemDown g8 \stemDown c,8 \stemDown c8 \stemDown
        a'8 \stemDown a8 | % 235
        \stemDown g8 \stemDown g8 \stemDown c,8 \stemDown c8 \stemDown
        c'8 \stemDown c8 | % 236
        \stemDown b8 \stemDown b8 \stemDown e,8 \stemDown e8 \stemDown g8
        \stemDown g8 \pageBreak | % 237
        \stemDown b8 \stemDown b8 \stemDown g8 \stemDown g8 \stemDown e'8
        \stemDown e8 | % 238
        \stemDown c8 _\fz \stemDown c8 \stemDown g'8 \stemDown g8
        \stemDown e8 \stemDown e8 | % 239
        \stemDown c8 \stemDown c8 \stemDown g8 \stemDown g8 \stemDown e8
        \stemDown c8 }
    | \barNumberCheck #240
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown <c es>2. :16 _\pp }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <c es>4. :16 }
    | % 241
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown <c es>2. :16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown <c es>4. :16 }
    | % 242
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown <ces es>2. :16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown <ces es>4. :16 }
    \pageBreak | % 243
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown <ces es>2. :16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown <ces es>4. :16 }
    | % 244
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown <b dis>2. :16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown <b dis>4. :16 }
    | % 245
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown <b dis>2. :16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown <b dis>4. :16 }
    | % 246
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown <dis fis>2. :16 }
    _\< \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown <dis fis>4. :16 }
    | % 247
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown <dis fis>2. :16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown <fis a>4. :16 }
    | % 248
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown <fis a>2. :16 }
    _\! _\f _\< \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown <fis a>4. :16 }
    \bar "||"
    \pageBreak | % 249
    \stemUp g,2. :32 _\! _\ff | \barNumberCheck #250
    \stemUp g2. :32 _\markup{ \italic {dim.} } _\> | % 251
    \stemUp g2. :32 _\! _\p _\> | % 252
    \stemUp g2. :32 _\! | % 253
    \stemUp g2. :32 _\pp | % 254
    \stemUp g2. :32 | % 255
    \stemUp g2. :32 | % 256
    \stemUp g2. :32 | % 257
    \stemUp g2. :32 \pageBreak | % 258
    \stemUp g2. :32 | % 259
    \stemUp g2. :32 | \barNumberCheck #260
    \stemUp g2. :32 | % 261
    \stemUp <f as>2. :32 _\pp | % 262
    \stemUp <f as>2. :32 | % 263
    \stemUp <f as>2. :32 | % 264
    \stemUp <f as>2. :32 \pageBreak | % 265
    \stemUp <f as>2. :32 _\< | % 266
    \stemUp <f as>2. :32 | % 267
    \stemUp <f as>2. :32 | % 268
    \stemUp <f as>2. :32 | % 269
    \stemUp <fis a>2. :32 _\! _\fz | \barNumberCheck #270
    \stemUp <fis a>2. :32 | % 271
    \stemUp cis'2. :32 _\p \pageBreak | % 272
    \stemUp cis2. :32 _\< | % 273
    \clef "treble" \stemUp a'2. :32 | % 274
    \stemDown cis2. :32 _\! | % 275
    \stemDown fis2. :32 _\f _\< | % 276
    \stemDown a2. :32 \pageBreak | % 277
    \stemDown a2. :32 _\! _\fff | % 278
    \stemDown a2. :32 | % 279
    \stemDown a2. :32 | \barNumberCheck #280
    \stemDown a2. :32 | % 281
    \stemDown gis8 r8 \clef "alto" \once \omit TupletBracket
    \times 2/3  {
        \stemUp gis,,8 ( \stemUp b8 \stemUp gis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp gis8 \stemUp b8 }
    | % 282
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp gis8 \stemUp b8 \stemUp gis8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 \stemUp gis8 \stemUp b8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp gis8 \stemUp b8 \stemUp gis8 ) }
    \pageBreak | % 283
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 ( \stemUp gis8 \stemUp b8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp gis8 _\markup{ \italic {dim.} } _\> \stemUp b8 \stemUp
        gis8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 \stemUp gis8 \stemUp b8 }
    | % 284
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp gis8 \stemUp b8 \stemUp gis8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 \stemUp gis8 \stemUp b8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp gis8 \stemUp b8 \stemUp gis8 ) }
    | % 285
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 ( _\! _\mf \stemUp gis8 \stemUp b8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp gis8 \stemUp b8 \stemUp gis8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 \stemUp gis8 \stemUp b8 }
    | % 286
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp gis8 \stemUp b8 \stemUp gis8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 \stemUp gis8 \stemUp b8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp gis8 \stemUp b8 \stemUp gis8 ) }
    | % 287
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 ( _\p \stemUp g8 \stemUp b8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp g8 \stemUp b8 \stemUp g8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 \stemUp g8 \stemUp b8 }
    \pageBreak | % 288
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp g8 _\markup{ \italic {dim.} } \stemUp b8 \stemUp g8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 \stemUp g8 \stemUp b8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp g8 \stemUp b8 \stemUp g8 ) }
    | % 289
    \stemUp <e g>2. :32 _\p | \barNumberCheck #290
    \stemUp <e g>2. :32 _\markup{ \italic {dim.} } _\> | % 291
    \stemUp <e g>2. :32 | % 292
    \stemUp <e g>2. :32 _\! | % 293
    \stemUp <e g>8 _\pp \stemUp <e g>8 \stemUp <e g>8 \stemUp <e g>8
    \stemUp <e g>8 \stemUp <e g>8 \pageBreak | % 294
    \stemUp <e g>8 _\> \stemUp <e g>8 \stemUp <e g>8 \stemUp <e g>8
    \stemUp <e g>8 \stemUp <e g>8 | % 295
    \times 6/5  {
        \stemUp <e g>8 _\! _\ppp \stemUp <e g>8 \stemUp <e g>8 \stemUp
        <e g>8 \stemUp <e g>8 }
    | % 296
    \times 3/4  {
        \stemUp <e g>4 \stemUp <e g>4 \stemUp <e g>4 \stemUp <e g>4 }
    | % 297
    \stemUp <e g>4 ( -. \stemUp <e g>4 -. \stemUp <e g>4 ) -. | % 298
    \stemUp <e g>4 r4 r4 | % 299
    R2. | \barNumberCheck #300
    \stemDown <g e' b'>4 _\ff r4 r4 \bar "|."
    }

PartPOneNineVoiceTwo =  \relative gis {
    \repeat volta 2 {
        \clef "alto" \time 3/4 \key g \major s1*3 \bar "||"
        s4*9 \pageBreak s4*21 \pageBreak s2*9 \pageBreak s4*15
        \pageBreak s4*15 \pageBreak s4*15 \pageBreak s2*9 \pageBreak
        s4*15 \pageBreak s2*9 \pageBreak s4*21 }
    \pageBreak s4*21 \pageBreak s2. \bar "||"
    \key e \major s1*3 \pageBreak s4*15 \pageBreak s4*15 \pageBreak
    s4*15 \pageBreak s4*15 \pageBreak s4*21 \pageBreak s1*6 \pageBreak | % 107
    \stemDown gis8 \stemDown gis8 \stemDown gis8 \stemDown gis8
    \stemDown gis8 \stemDown gis8 | % 108
    \stemDown gis8 \stemDown gis8 \stemDown gis8 \stemDown gis8
    \stemDown gis8 \stemDown gis8 | % 109
    \stemDown a8 \stemDown a8 \stemDown a8 \stemDown a8 \stemDown a8
    \stemDown a8 | \barNumberCheck #110
    \stemDown a8 \stemDown a8 \stemDown a8 \stemDown a8 \stemDown a8
    \stemDown a8 | % 111
    \stemDown ais8 \stemDown ais8 \stemDown ais8 \stemDown ais8
    \stemDown ais8 \stemDown ais8 | % 112
    \stemDown ais8 \stemDown ais8 \stemDown ais8 \stemDown ais8
    \stemDown ais8 \stemDown ais8 \pageBreak | % 113
    \stemDown b8 \stemDown b8 \stemDown b8 \stemDown b8 \stemDown b8
    \stemDown b8 | % 114
    \stemDown bis8 \stemDown bis8 \stemDown bis8 \stemDown bis8
    \stemDown bis8 \stemDown bis8 | % 115
    \stemDown cis8 \stemDown cis8 \stemDown cis8 \stemDown cis8
    \stemDown cis8 \stemDown cis8 | % 116
    \stemDown d8 \stemDown d8 \stemDown d8 \stemDown d8 \stemDown d8
    \stemDown d8 s1. \pageBreak s1*3 \bar "||"
    \key g \major \stemDown e2. :16 | % 124
    \stemDown e2. :16 | % 125
    \stemDown e2. :16 \pageBreak | % 126
    \stemDown e4 :8 \stemDown e2 :8 | % 127
    \stemDown e2. :8 | % 128
    \stemDown e2. :8 | % 129
    \stemDown e2. :8 s4*9 \pageBreak s4*27 \bar "||"
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*6
    \pageBreak s1. \repeat volta 2 {
        s1*3 \pageBreak | \barNumberCheck #180
         \once \override NoteHead.style = ##f \stemDown cis4 s4*17
        \pageBreak | % 186
         \once \override NoteHead.style = ##f \stemDown cis4 s4*17 }
    s2. \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
         \once \override NoteHead.style = ##f \stemDown cis4 s1*5
        \pageBreak s2*9 \pageBreak s4*21 \pageBreak s4*9 | % 216
        \stemNeutral <\tweak style ##f e \tweak style ##f gis>2*1/2
        \stemNeutral <\tweak style ##f fis \tweak style ##f a>2*1/2
        \stemNeutral <\tweak style ##f e \tweak style ##f gis>16
        \stopTrillSpan \stemNeutral <\tweak style ##f fis \tweak style
            ##f a>16 s8*7 | % 218
         \once \override NoteHead.style = ##f \stemNeutral gis2*1/2
        \once \override NoteHead.style = ##f \stemNeutral a2*1/2 \once
        \override NoteHead.style = ##f \stemNeutral gis16 \stopTrillSpan
        \once \override NoteHead.style = ##f \stemNeutral a16 s8*7 |
        \barNumberCheck #220
         \once \override NoteHead.style = ##f \stemNeutral a2*1/2 \once
        \override NoteHead.style = ##f \stemNeutral b2*1/2 \once
        \override NoteHead.style = ##f \stemNeutral a16 \stopTrillSpan
        \once \override NoteHead.style = ##f \stemNeutral b16 s8
        \pageBreak s2. | % 222
         \once \override NoteHead.style = ##f \stemNeutral a2*1/2 \once
        \override NoteHead.style = ##f \stemNeutral b2*1/2 \once
        \override NoteHead.style = ##f \stemNeutral a16 \stopTrillSpan
        \once \override NoteHead.style = ##f \stemNeutral b16 s8*25
        \pageBreak s4*15 \pageBreak s4*15 \pageBreak s4*9 }
    s4*9 \pageBreak s2*9 \bar "||"
    \pageBreak s4*27 \pageBreak s4*21 \pageBreak s2*9 | % 271
    \stemDown a,2. :64 \pageBreak | % 272
    \stemDown a2. :64 | % 273
    \clef "treble" s1*3 \pageBreak s4*13 \clef "alto" s4*5 \pageBreak
    s4*15 \pageBreak s2*9 \pageBreak s4*21 \bar "|."
    }

PartPTwoZeroVoiceOne =  \relative e' {
    \repeat volta 2 {
        \clef "bass" \time 3/4 \key g \major | % 1
        \stemDown e4 _\f r4 r4 | % 2
        R2. | % 3
        \stemDown b4 r4 r4 | % 4
        R2. \bar "||"
        R2.*3 \pageBreak | % 8
        \stemUp e,,8 _\f _\> \stemUp e8 \stemUp e2 ~ | % 9
        \stemUp e4 _\! \stemUp e4 ( -. _\p \stemUp e4 ) -. |
        \barNumberCheck #10
        \stemUp e4 ( -. \stemUp e4 -. \stemUp e4 ) -. | % 11
        \stemUp e4 -. ^\markup{ \italic {simile} } \stemUp e4 -. \stemUp
        e4 -. | % 12
        \stemUp e4 -. _\> \stemUp e4 -. \stemUp e4 -. | % 13
        \stemUp e4 -. _\! _\ppp \stemUp e4 -. \stemUp e4 -. | % 14
        \stemUp e4 -. \stemUp e4 -. \stemUp e4 -. \pageBreak | % 15
        \stemUp e4 -. \stemUp e4 -. \stemUp e4 -. | % 16
        \stemUp e4 -. \stemUp e4 -. \stemUp e4 -. | % 17
        \stemUp e4 -. \stemUp e4 -. \stemUp e4 -. | % 18
        \stemUp e4 -. \stemUp e4 -. \stemUp e4 -. | % 19
        \stemUp e4 -. \stemUp e4 -. \stemUp e4 -. | \barNumberCheck #20
        \stemUp e4 -. \stemUp e4 -. \stemUp e4 -. \pageBreak | % 21
        R2.*5 \pageBreak | % 26
        R2.*5 \pageBreak | % 31
        r4 \stemDown g'8 _\f _\< \stemDown e8 \stemDown d8 \stemDown g8
        | % 32
        \stemDown e8 \stemDown d8 \stemDown b8 \stemDown e8 \stemDown d8
        \stemDown b8 | % 33
        r4 _\! \stemUp b8 -. _\ff \stemUp b8 -. \stemUp g4 -. | % 34
        \stemUp b4 -. \stemUp b4 -. \stemUp g4 -. | % 35
        \stemUp b8 -. \stemUp b8 -. \stemUp g4 -. \stemDown dis'4 -.
        \pageBreak | % 36
        \stemDown e4 -. \stemDown dis4 -. \stemDown e4 -. | % 37
        \stemDown g4 -. \stemDown b8 -. \stemDown b8 -. \stemDown g4 -.
        | % 38
        \stemDown b4 -. \stemDown b4 -. \stemDown g4 -. | % 39
        \stemDown b8 -. \stemDown b8 -. \stemDown g4 -. \stemDown dis'4
        -. | \barNumberCheck #40
        \stemDown b4 -. \stemDown dis4 -. \stemDown b4 -. | % 41
        \stemDown dis4 -. \stemDown e4 -. \stemUp g,,8 \stemUp e8
        \pageBreak | % 42
        \stemUp g8 \stemUp e8 \stemUp g8 \stemUp e8 \stemUp g8 \stemUp e8
        | % 43
        \stemUp a8 \stemUp e8 \stemUp a8 \stemUp e8 \stemUp a8 \stemUp e8
        | % 44
        \stemUp b'8 \stemUp e,8 \stemUp g8 \stemUp e8 \stemUp g8 \stemUp
        e8 | % 45
        \stemUp g8 \stemUp e8 \stemUp g8 \stemUp e8 \stemUp g8 \stemUp e8
        | % 46
        \stemUp g8 \stemUp e8 \stemUp g8 \stemUp e8 \stemUp g8 \stemUp e8
        \pageBreak | % 47
        \stemUp a8 \stemUp e8 \stemUp a8 \stemUp e8 \stemUp a8 \stemUp e8
        | % 48
        \stemUp b'8 \stemUp e,8 \stemUp g8 \stemUp e8 \stemUp g8 \stemUp
        b8 | % 49
        \stemDown e8 r8 \stemDown b'8 \stemDown b8 \stemDown b4 |
        \barNumberCheck #50
        \stemDown e,4 -. \stemDown e4 -. r4 | % 51
        r4 \stemDown fis4 -. \stemDown a4 -. | % 52
        \stemDown g8 \stemDown fis8 \stemDown e4 r4 \pageBreak | % 53
        r4 \stemDown b'8 \stemDown b8 \stemDown b4 | % 54
        \stemDown e,4 -. \stemDown e4 -. r4 | % 55
        r4 \stemDown fis4 -. \stemDown a4 -. | % 56
        \stemDown g8 \stemDown fis8 \stemDown e4 \stemDown a4 | % 57
        \stemDown g8 \stemDown fis8 \stemDown e4 \stemDown a4 | % 58
        \stemDown g8 \stemDown fis8 \stemDown e4 \stemDown a4 | % 59
        \stemDown g8 \stemDown fis8 \stemDown e4 r4 }
    \pageBreak | \barNumberCheck #60
    R2.*2 | % 62
    \stemDown e4 -. _\p \stemDown g4 -. r4 | % 63
    \stemDown e4 -. _\markup{ \italic {dim.} } \stemDown g4 -. r4 | % 64
    \stemDown e8 _\p \stemDown e16 r16 r4 \stemUp b8 \stemUp b16 r16 | % 65
    \stemDown e8 \stemDown e16 r16 r4 \stemUp b8 \stemUp b16 r16 | % 66
    \stemDown e8 \stemDown e16 r16 r4 \stemUp b8 \stemUp b16 r16
    \pageBreak | % 67
    \stemDown e8 \stemDown e16 r16 r4 \stemUp b8 \stemUp b16 r16 \bar
    "||"
    \key e \major \stemDown e8 _\pp \stemDown e16 r16 r4 \stemUp b8
    \stemUp b16 r16 | % 69
    \stemDown e8 \stemDown e16 r16 r4 \stemUp b8 \stemUp b16 r16 |
    \barNumberCheck #70
    \stemDown e8 \stemDown e16 r16 r4 \stemUp b8 \stemUp b16 r16 | % 71
    \stemDown e8 \stemDown e16 r16 r4 \stemUp b8 \stemUp b16 r16
    \pageBreak | % 72
    \stemDown e8 \stemDown e16 r16 r4 \stemDown gis8 \stemDown gis16 r16
    | % 73
    \stemDown e8 \stemDown e16 r16 r4 \stemDown gis8 \stemDown gis16 r16
    | % 74
    \stemDown e8 \stemDown e16 r16 r4 \stemDown gis8 \stemDown gis16 r16
    | % 75
    \stemDown b4 -. \stemUp b,4 -. \stemDown e8 \stemDown e16 r16 | % 76
    \stemDown e8 \stemDown e16 r16 r4 \stemUp b8 \stemUp b16 r16
    \pageBreak | % 77
    \stemDown e8 \stemDown e16 r16 r4 \stemUp b8 \stemUp b16 r16 | % 78
    \stemDown e8 \stemDown e16 r16 r4 \stemUp b8 \stemUp b16 r16 | % 79
    \stemDown e8 \stemDown e16 r16 r4 \stemUp b8 \stemUp b16 r16 |
    \barNumberCheck #80
    \stemDown e8 \stemDown e16 r16 r4 \stemDown gis8 \stemDown gis16 r16
    | % 81
    \stemDown e8 \stemDown e16 r16 r4 \stemDown gis8 \stemDown gis16 r16
    \pageBreak | % 82
    \stemDown e8 \stemDown e16 r16 r4 \stemDown gis8 \stemDown gis16 r16
    | % 83
    \stemDown b4 -. \stemUp b,4 -. \stemDown e8 \stemDown e16 r16 | % 84
    \stemUp a,8 _\fz \stemUp a16 r16 r4 \stemUp cis8 \stemUp cis16 r16 | % 85
    \stemUp a8 _\fz \stemUp a16 r16 r4 \stemUp cis8 \stemUp cis16 r16 | % 86
    \stemDown e8 _\fz \stemDown e16 r16 r4 \stemDown gis8 _\pp \stemDown
    gis16 r16 \pageBreak | % 87
    \stemDown e8 \stemDown e16 r16 r4 \stemUp e,8 \stemUp e16 r16 | % 88
    \stemUp a8 _\fp \stemUp a16 r16 r4 \stemUp cis8 \stemUp cis16 r16 | % 89
    \stemUp a8 _\fp \stemUp a16 r16 r4 \stemUp cis8 \stemUp cis16 r16 |
    \barNumberCheck #90
    \stemDown e8 _\fp \stemDown e16 r16 r4 \stemDown gis8 _\pp \stemDown
    gis16 r16 | % 91
    \stemDown e8 \stemDown e16 r16 r4 \stemDown e8 \stemDown e16 r16
    \pageBreak | % 92
    \stemDown gis8 ( _\p \stemDown b8 ) \stemDown b2 ~ | % 93
    \stemDown b2 \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( \stemDown b8 \stemDown fis8 }
    | % 94
    \stemDown e2 _\< \stemDown fis4 ) | % 95
    \stemDown gis8 ( \stemDown b8 ) \stemDown b2 ~ | % 96
    \stemDown b8 _\! _\mf \stemDown e8 ( \stemDown dis8 \stemDown cis8
    \stemDown b4 ~ | % 97
    \stemDown b8 ) \stemDown gis8 ( \stemDown fis8 \stemDown gis8
    \stemDown b8 _\> \stemDown gis8 ) | % 98
    \stemDown fis8 ( \stemDown gis8 \stemDown e2 ) \pageBreak | % 99
    \stemDown e4 -. _\! _\ppp \stemDown e4 -. \stemDown e4 -. |
    \barNumberCheck #100
    \stemDown e4 -. \stemDown e4 -. \stemDown e4 -. | % 101
    \stemDown e4 -. \stemDown e4 -. \stemDown e4 -. | % 102
    \stemDown e4 -. \stemDown e4 -. \stemDown e4 -. | % 103
    \stemDown e4 -. \stemDown e4 -. \stemDown e4 -. | % 104
    \stemDown e4 -. \stemDown e4 -. \stemDown e4 -. | % 105
    \stemDown e4 -. \stemDown e4 -. \stemDown e4 -. | % 106
    \stemDown e4 -. \stemDown e4 -. \stemDown e4 -. \pageBreak | % 107
    \stemUp e,2. -> _ "[" _ "]" _\p | % 108
    \stemDown e'2. -> ^ "[" ^ "]" | % 109
    \stemDown f2. _\fz | \barNumberCheck #110
    \stemUp f,2. | % 111
    \stemUp fis2. _\< | % 112
    \stemDown fis'2. \pageBreak | % 113
    \stemDown g4 ( _\! _\mf \stemDown as4 \stemUp as,4 ) | % 114
    \stemDown gis'4 ( _\< \stemDown a4 \stemUp a,4 ) | % 115
    \stemDown a'4 ( \stemDown bes4 \stemUp bes,4 ) | % 116
    \stemDown bes'4 ( _\! _\f \stemDown b4 \stemUp b,4 ) | % 117
    \stemUp b8 _\f _\markup{ \italic {più} } \stemUp b8 \stemUp b8
    \stemUp b8 _\markup{ \italic {cresc.} } _\< \stemUp b8 \stemUp b8 | % 118
    \stemUp b8 \stemUp b8 \stemUp b8 \stemUp b8 \stemUp b8 \stemUp b8
    \pageBreak | % 119
    \stemUp b4. _\! \stemUp c8 \stemDown dis4 | \barNumberCheck #120
    \stemDown fis4 \stemDown a2 -> | % 121
    \stemDown e'4. -> \stemDown dis8 \stemDown c4 | % 122
    \stemDown b4 \stemDown fis'4 \stemDown b,4 \bar "||"
    \key g \major \stemDown e2 -> _\fff \stemDown d4 ~ -> | % 124
    \stemDown d4 \stemDown cis2 -> | % 125
    \stemDown c2 \stemDown fis,4 -. \pageBreak | % 126
    \stemDown b4 -. \stemDown g4 -. \stemDown e4 -. | % 127
    \stemDown e'2 -> \stemDown d4 ~ -> | % 128
    \stemDown d4 \stemDown cis2 -> | % 129
    \stemDown c2 \stemDown a4 -. | \barNumberCheck #130
    \stemDown e4 \stemDown e4 \stemDown a4 | % 131
    \stemDown e4 \stemDown e4 \stemUp a,4 | % 132
    \stemDown e'4 \stemDown e4 \stemDown a4 \pageBreak | % 133
    \stemDown e4 \stemDown e4 \stemUp a,4 | % 134
    \stemDown e'4 r4 r4 | % 135
    \stemUp a,4 r4 r4 | % 136
    \stemDown e'4 r4 r4 | % 137
    \stemUp a,4 r4 r4 | % 138
    \stemUp e4 r4 r4 | % 139
    R2. | \barNumberCheck #140
    \stemUp e4 r4 r4 | % 141
    R2. \bar "||"
    \pageBreak | % 142
    R2.*7 | % 149
    r4 \stemUp b'8 _\ppp \stemUp b8 \stemUp b4 \pageBreak |
    \barNumberCheck #150
    \stemUp e,4 r4 r4 | % 151
    r4 \stemUp b'8 \stemUp b8 \stemUp b4 | % 152
    \stemUp e,4 r2 | % 153
    r4 \stemUp b'8 \stemUp b8 \stemUp b4 | % 154
    \stemUp e,2 ( _\pp \stemUp g4 | % 155
    \stemUp b4 _\< \stemDown e2 ) | % 156
    \stemDown g2 ( \stemDown e4 _\! _\> | % 157
    \stemDown es4 \stemUp g,2 ~ _\! \pageBreak | % 158
    \stemUp g2. ) ( | % 159
    \stemUp b2. | \barNumberCheck #160
    \stemUp c2. ) ~ | % 161
    \stemUp c2. ~ | % 162
    \stemUp c2 r4 | % 163
    R2.*3 \pageBreak | % 166
    R2.*8 \pageBreak | % 174
    R2.*2 \repeat volta 2 {
        | % 176
        \stemUp c4 _\pp r4 r4 | % 177
        R2. | % 178
        r4 r8 \stemDown g'8 _\pp \stemUp c,4 -. | % 179
        \stemUp c4 -. r4 r4 \pageBreak | \barNumberCheck #180
        R2.*2 | % 182
        r4 r8 \stemDown g'8 _\pp \stemUp c,4 -. | % 183
        \stemUp c4 -. r4 r4 | % 184
        R2.*2 \pageBreak | % 186
        r4 r8 \stemDown g'8 _\pp \stemUp c,4 -. | % 187
        \stemUp c4 -. r4 r4 | % 188
        \stemDown e4 r4 r4 | % 189
        \stemDown g4 r4 r4 | \barNumberCheck #190
        r4 r8 \stemDown g8 _\pp \stemUp c,4 -. | % 191
        \stemUp c4 -. r4 r4 }
    | % 192
    \stemUp c4 -. r4 r4 \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
        \stemDown g'4 -. _\mf \stemDown a4 -. \stemDown b4 -. | % 194
        \stemDown c4 -. \stemUp c,4 -. \stemDown c'4 -. | % 195
        \stemDown a4 -. \stemDown d,4 -. \stemDown fis4 -. | % 196
        \stemDown g4 -. \stemUp g,4 -. \stemDown g'4 -. | % 197
        \stemUp a,4 -. _\p r4 \stemUp c4 -. | % 198
        \stemDown d4 -. _\> \stemDown d'4 -. \stemDown d,4 -. | % 199
        \stemDown e4 -. _\! _\pp r4 \stemUp b4 -. \pageBreak |
        \barNumberCheck #200
        \stemDown e4 -. \stemDown e'4 -. \stemDown e,4 -. | % 201
        \times 2/3  {
            \stemDown g8 _\pp \stemDown g8 \stemDown g8 }
        \times 2/3  {
            \stemDown a8 \stemDown a8 \stemDown a8 }
        \times 2/3  {
            \stemDown b8 \stemDown b8 \stemDown b8 }
        | % 202
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown c4. :16 }
        \once \omit TupletBracket
        \times 2/3  {
            \stemUp c,4. :16 }
        \once \omit TupletBracket
        \times 2/3  {
            \stemDown c'4. :16 }
        | % 203
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown a4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown d,4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown fis4. :16 }
        | % 204
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown g4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemUp g,4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown g'4. :16 }
        | % 205
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemUp c,4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown d4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown e4. :16 }
        \pageBreak | % 206
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown f4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemUp f,4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown f'4. :16 }
        | % 207
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown dis4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemUp b4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown dis4. :16 }
        | % 208
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemDown e4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemUp b4. :16 }
        \once \omit TupletBracket
        \once \omit TupletNumber
        \times 2/3  {
            \stemUp e,4. :16 }
        | % 209
        \stemUp b'8 r8 \stemDown b'2 -> _\pp | \barNumberCheck #210
        \stemDown b2 \stemDown b8 r8 | % 211
        \stemUp b,8 r8 \stemDown b'2 -> | % 212
        \stemDown b2 \stemDown b8 r8 \pageBreak | % 213
        \stemUp b,8 r8 \stemDown b'2 -> | % 214
        \stemDown b2 \stemDown b8 r8 | % 215
        \stemUp b,8 r8 \stemDown b'2 -> | % 216
        \stemDown e2 ~ _\pp \stemDown e8 r8 | % 217
        R2. | % 218
        \stemDown e2 ~ \stemDown e8 r8 | % 219
        R2. | \barNumberCheck #220
        \stemDown d2 ~ \stemDown d8 r8 \pageBreak | % 221
        R2. | % 222
        \stemDown d2 ~ \stemDown d8 r8 | % 223
        R2. | % 224
        \stemDown g,8 _\pp \stemDown g8 \stemUp c,8 \stemUp c8 \stemDown
        a'8 \stemDown a8 | % 225
        \stemDown g8 \stemDown g8 \stemUp c,8 \stemUp c8 \stemDown a'8
        \stemDown a8 | % 226
        \stemDown g8 \stemDown g8 \stemUp c,8 \stemUp c8 \stemDown a'8
        \stemDown a8 \pageBreak | % 227
        \stemDown g8 \stemDown g8 \stemUp c,8 \stemUp c8 \stemDown a'8
        \stemDown a8 | % 228
        \stemDown g8 \stemDown g8 \stemUp c,8 \stemUp c8 \stemDown a'8
        \stemDown a8 | % 229
        \stemDown g8 \stemDown g8 \stemUp g,8 \stemUp g8 \stemDown f'8
        \stemDown f8 | \barNumberCheck #230
        \stemDown e8 \stemDown e8 \stemUp g,8 \stemUp g8 \stemDown d'8
        \stemDown d8 | % 231
        \stemUp c8 \stemUp c8 \stemDown e8 \stemDown e8 \stemUp c8
        \stemUp c8 \pageBreak | % 232
        \stemDown g'8 \stemDown g8 \stemUp c,8 \stemUp c8 \stemDown a'8
        \stemDown a8 | % 233
        \stemDown g8 \stemDown g8 \stemUp c,8 \stemUp c8 \stemDown a'8
        \stemDown a8 | % 234
        \stemDown g8 \stemDown g8 \stemUp c,8 \stemUp c8 \stemDown a'8
        \stemDown a8 | % 235
        \stemDown g8 \stemDown g8 \stemUp c,8 \stemUp c8 \stemDown c'8
        \stemDown c8 | % 236
        \stemDown b8 \stemDown b8 \stemDown e,8 \stemDown e8 \stemDown g8
        \stemDown g8 \pageBreak | % 237
        \stemDown b8 \stemDown b8 \stemDown g8 \stemDown g8 \stemDown e'8
        \stemDown e8 | % 238
        \stemDown c8 _\fz \stemDown c8 \stemDown g'8 \stemDown g8
        \stemDown e8 \stemDown e8 | % 239
        \stemDown c8 \stemDown c8 \stemDown g8 \stemDown g8 \stemDown e8
        \stemDown c8 }
    | \barNumberCheck #240
    \stemUp c4 r4 r4 | % 241
    R2.*2 \pageBreak | % 243
    R2. | % 244
    r4 r4 \stemDown gis'8 _\pp \stemDown gis8 | % 245
    \stemDown a4 r4 \stemDown a8 \stemDown a8 | % 246
    \stemDown ais4 _\< r4 \stemDown ais8 \stemDown ais8 | % 247
    \stemDown b4. \stemDown c8 \stemDown cis4 ~ | % 248
    \stemDown cis8 _\! _\f \stemDown d8 \stemDown dis4. \stemDown e8
    \bar "||"
    \pageBreak | % 249
    \stemUp bes,2. :32 _\ff | \barNumberCheck #250
    \stemUp bes2. :32 _\markup{ \italic {dim.} } _\> | % 251
    \stemUp bes2. :32 _\! _\p _\> | % 252
    \stemUp bes2. :32 _\! | % 253
    \stemUp bes2. :32 _\pp | % 254
    \stemUp bes2. :32 | % 255
    \stemUp bes2. :32 | % 256
    \stemUp bes2. :32 | % 257
    \stemUp bes2. :32 \pageBreak | % 258
    \stemUp bes2. :32 | % 259
    \stemUp bes2. :32 | \barNumberCheck #260
    \stemUp bes2. :32 | % 261
    \stemUp as2. :32 _\pp | % 262
    \stemUp as2. :32 | % 263
    \stemUp as2. :32 | % 264
    \stemUp as2. :32 \pageBreak | % 265
    \stemUp as2. :32 _\< | % 266
    \stemUp as2. :32 | % 267
    \stemUp as2. :32 | % 268
    \stemUp as2. :32 | % 269
    \stemUp fis2. :32 _\! _\fz | \barNumberCheck #270
    \stemUp fis2. :32 | % 271
    \stemUp a8 _\p \stemUp gis8 \stemUp fis8 \stemUp gis8 \stemUp a8
    \stemUp gis8 \pageBreak | % 272
    \stemUp fis8 _\< \stemUp gis8 \stemUp a8 \stemUp gis8 \stemUp fis8
    \stemUp gis8 | % 273
    \stemUp a8 \stemUp gis8 \stemUp fis8 \stemUp gis8 \stemUp a8 \stemUp
    gis8 | % 274
    \stemUp fis8 _\! \stemUp gis8 \stemUp a8 \stemUp gis8 \stemUp fis8
    \stemUp gis8 | % 275
    \stemUp a8 _\f _\< \stemUp gis8 \stemUp fis8 \stemUp gis8 \stemUp a8
    \stemUp gis8 | % 276
    \stemUp fis8 \stemUp gis8 \stemUp a8 \stemUp gis8 \stemUp fis8
    \stemUp gis8 \pageBreak | % 277
    \stemUp f2. :32 _\! _\fff | % 278
    \stemUp f2. :32 | % 279
    \stemUp f2. :32 | \barNumberCheck #280
    \stemUp f2. :32 | % 281
    \stemUp e8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp gis8 ( \stemUp b8 \stemUp gis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp gis8 \stemUp b8 }
    | % 282
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp gis8 \stemUp b8 \stemUp gis8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 \stemUp gis8 \stemUp b8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp gis8 \stemUp b8 \stemUp gis8 ) }
    \pageBreak | % 283
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 ( \stemUp gis8 \stemUp b8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp gis8 _\markup{ \italic {dim.} } _\> \stemUp b8 \stemUp
        gis8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 \stemUp gis8 \stemUp b8 }
    | % 284
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp gis8 \stemUp b8 \stemUp gis8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 \stemUp gis8 \stemUp b8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp gis8 \stemUp b8 \stemUp gis8 ) }
    | % 285
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 ( _\! _\mf \stemUp gis8 \stemUp b8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp gis8 \stemUp b8 \stemUp gis8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 \stemUp gis8 \stemUp b8 }
    | % 286
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp gis8 \stemUp b8 \stemUp gis8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 \stemUp gis8 \stemUp b8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp gis8 \stemUp b8 \stemUp gis8 ) }
    | % 287
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 ( _\p \stemUp g8 \stemUp b8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp g8 \stemUp b8 \stemUp g8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 \stemUp g8 \stemUp b8 }
    \pageBreak | % 288
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp g8 _\markup{ \italic {dim.} } \stemUp b8 \stemUp g8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 \stemUp g8 \stemUp b8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp g8 \stemUp b8 \stemUp g8 ) }
    | % 289
    \stemUp e4 r4 r4 | \barNumberCheck #290
    R2. | % 291
    r4 \stemDown b''8 _\p \stemDown b8 \stemDown b4 | % 292
    \stemDown e,4 r4 r4 | % 293
    R2. \pageBreak | % 294
    R2.*6 | \barNumberCheck #300
    \stemUp <e, b' g'>4 _\ff r4 r4 \bar "|."
    }

PartPTwoZeroVoiceTwo =  \relative cis {
    \repeat volta 2 {
        \clef "bass" \time 3/4 \key g \major s1*3 \bar "||"
        s4*9 \pageBreak s4*21 \pageBreak s2*9 \pageBreak | % 21
         \once \override NoteHead.style = ##f \stemUp cis4 s2*7
        \pageBreak | % 26
         \once \override NoteHead.style = ##f \stemUp cis4 s2*7
        \pageBreak s4*15 \pageBreak s2*9 \pageBreak s4*15 \pageBreak
        s2*9 \pageBreak s4*21 }
    \pageBreak s4*21 \pageBreak s2. \bar "||"
    \key e \major s1*3 \pageBreak s4*15 \pageBreak s4*15 \pageBreak
    s4*15 \pageBreak s4*15 \pageBreak s4*21 \pageBreak s1*6 \pageBreak
    s2*9 \pageBreak s2*9 \pageBreak s1*3 \bar "||"
    \key g \major s4*9 \pageBreak s4*21 \pageBreak s4*27 \bar "||"
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*6 \pageBreak | % 166
     \once \override NoteHead.style = ##f \stemUp cis4 s4*23 \pageBreak
    s1. \repeat volta 2 {
        s1*3 \pageBreak s2*9 \pageBreak s2*9 }
    s2. \bar "||"
    \pageBreak \repeat volta 2 {
        s4*21 \pageBreak s2*9 \pageBreak s4*21 \pageBreak s1*6
        \pageBreak s2*9 \pageBreak s4*15 \pageBreak s4*15 \pageBreak
        s4*9 }
    s4*9 \pageBreak s2*9 \bar "||"
    \pageBreak s4*27 \pageBreak s4*21 \pageBreak s4*21 \pageBreak s4*15
    \pageBreak s2*9 \pageBreak s4*15 \pageBreak s2*9 \pageBreak s4*21
    \bar "|."
    }

PartPTwoOneVoiceOne =  \relative e' {
    \repeat volta 2 {
        \clef "bass" \time 3/4 \key g \major \transposition c | % 1
        \stemDown e4 _\f r4 r4 | % 2
        R2. | % 3
        \stemDown b4 r4 r4 | % 4
        R2. \bar "||"
        \stemDown e8 _\f \stemDown e8 \stemDown e2 | % 6
        \stemDown b8 _\fz \stemDown b8 \stemDown b2 ~ | % 7
        \stemDown b2. \pageBreak | % 8
        \stemDown b2. ~ _\fz _\> | % 9
        \stemDown b2. ~ _\! _\p | \barNumberCheck #10
        \stemDown b2. ~ | % 11
        \stemDown b2. ~ _\pp | % 12
        \stemDown b2. ~ _\> | % 13
        \stemDown b2. ~ _\! _\ppp | % 14
        \stemDown b2. ~ \pageBreak | % 15
        \stemDown b2. ~ | % 16
        \stemDown b2. ~ | % 17
        \stemDown b2. ~ | % 18
        \stemDown b2. ~ | % 19
        \stemDown b2. ~ | \barNumberCheck #20
        \stemDown b2. \pageBreak | % 21
        R2.*5 \pageBreak | % 26
        R2.*5 \pageBreak | % 31
        R2.*2 | % 33
        r4 \stemUp b,8 -. _\ff \stemUp b8 -. \stemUp g4 -. | % 34
        \stemUp b4 -. \stemUp b4 -. \stemUp g4 -. | % 35
        \stemUp b8 -. \stemUp b8 -. \stemUp g4 -. \stemDown dis'4 -.
        \pageBreak | % 36
        \stemDown e4 -. \stemDown dis4 -. \stemDown e4 -. | % 37
        \stemDown g4 -. \stemDown b8 -. \stemDown b8 -. \stemDown g4 -.
        | % 38
        \stemDown b4 -. \stemDown b4 -. \stemDown g4 -. | % 39
        \stemDown b8 -. \stemDown b8 -. \stemDown g4 -. \stemDown dis'4
        -. | \barNumberCheck #40
        \stemDown b4 -. \stemDown dis4 -. \stemDown b4 -. | % 41
        \stemDown dis4 ^. \stemDown e4 ^. \stemUp e,4 ^ "div."
        \pageBreak | % 42
        \stemUp e4 \stemUp e4 \stemUp e4 | % 43
        \stemUp e4 \stemUp e'4 \stemUp e,4 | % 44
        \stemUp e4 \stemUp e4 \stemUp e4 | % 45
        \stemUp e4 \stemUp e'4 \stemUp e,4 | % 46
        \stemUp e4 \stemUp e4 \stemUp e4 \pageBreak | % 47
        \stemUp e4 \stemUp e'4 \stemUp e,4 | % 48
        \stemUp e4 \stemUp e4 \stemUp e4 | % 49
        r4 \stemDown b'8 \stemDown b8 \stemDown b4 | \barNumberCheck #50
        \stemDown e,4 -. \stemDown e4 -. r4 | % 51
        r4 \stemDown fis4 -. \stemDown a4 -. | % 52
        \stemDown g8 \stemDown fis8 \stemDown e4 r4 \pageBreak | % 53
        r4 \stemDown b'8 \stemDown b8 \stemDown b4 | % 54
        \stemDown e,4 -. \stemDown e4 -. r4 | % 55
        r4 \stemDown fis4 -. \stemDown a4 -. | % 56
        \stemDown g8 \stemDown fis8 \stemDown e4 \stemDown a4 | % 57
        \stemDown g8 \stemDown fis8 \stemDown e4 \stemDown a4 | % 58
        \stemDown g8 \stemDown fis8 \stemDown e4 \stemDown a4 | % 59
        \stemDown g8 \stemDown fis8 \stemDown e4 r4 }
    \pageBreak | \barNumberCheck #60
    R2.*7 \pageBreak | % 67
    R2. \bar "||"
    \key e \major R2.*4 \pageBreak | % 72
    R2.*5 \pageBreak | % 77
    R2.*5 \pageBreak | % 82
    R2.*5 \pageBreak | % 87
    R2.*5 \pageBreak | % 92
    \stemDown e4 _\p ^ "pizz." r4 \stemUp b4 | % 93
    \stemDown e4 r4 \stemUp b4 | % 94
    \stemDown e4 _\< r4 \stemUp b4 | % 95
    \stemDown e4 r4 \stemUp b4 | % 96
    \stemDown e4 _\! _\mf r4 \stemDown gis4 | % 97
    \stemDown e4 r4 \stemDown gis4 _\> | % 98
    \stemDown b4 \stemUp b,4 \stemDown e4 \pageBreak | % 99
    r4 _\! \stemUp e,2 ~ _\ppp ^ "arco" | \barNumberCheck #100
    \stemUp e2. ~ | % 101
    \stemUp e2. ~ | % 102
    \stemUp e2. ~ | % 103
    \stemUp e2. ~ | % 104
    \stemUp e2. ~ | % 105
    \stemUp e2. ~ | % 106
    \stemUp e2. \pageBreak | % 107
    \stemUp e2. -> _\p | % 108
    \stemDown e'2. -> | % 109
    \stemDown f2. -> _\fz | \barNumberCheck #110
    \stemUp f,2. | % 111
    \stemUp fis2. _\< | % 112
    \stemDown fis'2. \pageBreak | % 113
    \stemDown g4 ( _\! _\mf \stemDown as4 \stemUp as,4 ) | % 114
    \stemDown gis'4 ( _\< \stemDown a4 \stemUp a,4 ) | % 115
    \stemDown a'4 ( \stemDown bes4 \stemUp bes,4 ) | % 116
    \stemDown bes'4 ( _\! _\f \stemDown b4 \stemUp b,4 ) | % 117
    \stemUp b8 _\f _\markup{ \italic {più} } \stemUp b8 \stemUp b8
    \stemUp b8 _\markup{ \italic {cresc.} } _\< \stemUp b8 \stemUp b8 | % 118
    \stemUp b8 \stemUp b8 \stemUp b8 \stemUp b8 \stemUp b8 \stemUp b8
    \pageBreak | % 119
    \stemUp b4. _\! \stemUp c8 \stemDown dis4 | \barNumberCheck #120
    \stemDown fis4 \stemDown a2 -> ^ "[" ^ "]" | % 121
    \stemDown e'4. -> \stemDown dis8 \stemDown c4 | % 122
    \stemDown b4 \stemDown fis'4 \stemDown b,4 \bar "||"
    \key g \major \stemDown e2 -> _\fff \stemDown d4 ~ -> | % 124
    \stemDown d4 \stemDown cis2 -> | % 125
    \stemDown c2 \stemDown fis,4 -. \pageBreak | % 126
    \stemDown b4 -. \stemDown g4 -. \stemDown e4 -. | % 127
    \stemDown e'2 -> \stemDown d4 ~ -> | % 128
    \stemDown d4 \stemDown cis2 -> | % 129
    \stemDown c2 \stemDown a4 -. | \barNumberCheck #130
    \stemDown e4 \stemDown e4 \stemDown a4 | % 131
    \stemDown e4 \stemDown e4 \stemUp a,4 | % 132
    \stemDown e'4 \stemDown e4 \stemDown a4 \pageBreak | % 133
    \stemDown e4 \stemDown e4 \stemUp a,4 | % 134
    \stemDown e'4 r4 r4 | % 135
    \stemUp a,4 r4 r4 | % 136
    \stemDown e'4 r4 r4 | % 137
    \stemUp a,4 r4 r4 | % 138
    \stemUp e4 r4 r4 | % 139
    R2. | \barNumberCheck #140
    \stemUp e4 r4 r4 | % 141
    R2. \bar "||"
    \pageBreak | % 142
    R2.*8 \pageBreak | \barNumberCheck #150
    R2.*8 \pageBreak | % 158
    R2.*8 \pageBreak | % 166
    R2.*8 \pageBreak | % 174
    R2.*2 \repeat volta 2 {
        | % 176
        \stemUp c'4 _\pp r4 r4 | % 177
        R2. | % 178
        r4 r8 \stemDown g'8 _\pp \stemUp c,4 -. | % 179
        \stemUp c4 -. r4 r4 \pageBreak | \barNumberCheck #180
        R2.*2 | % 182
        r4 r8 \stemDown g'8 _\pp \stemUp c,4 -. | % 183
        \stemUp c4 -. r4 r4 | % 184
        R2.*2 \pageBreak | % 186
        r4 r8 \stemDown g'8 _\pp \stemUp c,4 -. | % 187
        \stemUp c4 -. r4 r4 | % 188
        \stemDown e4 r4 r4 | % 189
        \stemDown g4 r4 r4 | \barNumberCheck #190
        r4 r8 \stemDown g8 _\pp \stemUp c,4 -. | % 191
        \stemUp c4 -. r4 r4 }
    | % 192
    \stemUp c4 -. r4 r4 \bar "||"
    \pageBreak \repeat volta 2 {
        | % 193
        \stemDown g'4 -. _\mf \stemDown a4 -. \stemDown b4 -. | % 194
        \stemDown c4 -. \stemUp c,4 -. \stemDown c'4 -. | % 195
        \stemDown a4 -. \stemDown d,4 -. \stemDown fis4 -. | % 196
        \stemDown g4 -. \stemUp g,4 -. \stemDown g'4 -. | % 197
        \stemUp a,4 -. _\p r4 \stemUp c4 -. | % 198
        \stemDown d4 -. _\> \stemDown d'4 -. \stemDown d,4 -. | % 199
        \stemDown e4 -. _\! _\pp r4 \stemUp b4 -. \pageBreak |
        \barNumberCheck #200
        \stemDown e4 -. \stemDown e'4 -. \stemDown e,4 -. | % 201
        \stemDown g4 _\p r4 \stemDown g4 | % 202
        \stemUp c,4 r4 \stemUp c4 | % 203
        \stemDown d4 r4 \stemDown d4 | % 204
        \stemUp g,4 r4 \stemUp g4 | % 205
        \stemUp c4 r4 \stemUp c4 \pageBreak | % 206
        \stemDown f4 r4 r4 | % 207
        \stemUp b,4 r4 \stemUp b4 | % 208
        \stemDown e4 r4 r4 | % 209
        R2.*4 \pageBreak | % 213
        R2.*8 \pageBreak | % 221
        R2.*3 | % 224
        \stemUp c4 _\pp ^ "pizz." \stemDown c'4 r4 | % 225
        \stemUp c,4 \stemDown c'4 r4 | % 226
        \stemUp c,4 \stemDown c'4 r4 \pageBreak | % 227
        \stemUp c,4 \stemDown c'4 r4 | % 228
        \stemUp c,4 \stemDown c'4 r4 | % 229
        \stemUp g,4 \stemDown g'4 r4 | \barNumberCheck #230
        \stemUp c,4 \stemDown c'4 r4 | % 231
        \stemUp c,4 \stemDown c'4 r4 \pageBreak | % 232
        \stemUp c,4 \stemDown c'4 r4 | % 233
        \stemUp c,4 \stemDown c'4 r4 | % 234
        \stemUp c,4 \stemDown c'4 r4 | % 235
        \stemUp c,4 \stemDown c'4 r4 | % 236
        \stemDown e,4 \stemDown e'4 r4 \pageBreak | % 237
        \stemDown g,4 \stemDown g'4 r4 | % 238
        \stemUp c,,4 _\fz \stemDown c'4 r4 | % 239
        \stemUp c,4 \stemDown c'4 r4 }
    | \barNumberCheck #240
    R2.*3 \pageBreak | % 243
    R2. | % 244
    r4 r4 \stemDown gis8 _\pp ^ "arco" \stemDown gis8 | % 245
    \stemDown a4 r4 \stemDown a8 \stemDown a8 | % 246
    \stemDown ais4 _\< r4 \stemDown ais8 \stemDown ais8 | % 247
    \stemDown b4. \stemDown c8 \stemDown cis4 ~ | % 248
    \stemDown cis8 _\! _\f \stemDown d8 \stemDown dis4. \stemDown e8
    \bar "||"
    \pageBreak | % 249
    \stemUp bes,2. :32 _\ff | \barNumberCheck #250
    \stemUp bes2. :32 _\markup{ \italic {dim.} } _\> | % 251
    \stemUp bes2. :32 _\! _\p _\> | % 252
    \stemUp bes2. :32 _\! | % 253
    \stemUp bes2. :32 _\pp | % 254
    \stemUp bes2. :32 | % 255
    \stemUp bes2. :32 | % 256
    \stemUp bes2. :32 | % 257
    \stemUp bes2. :32 \pageBreak | % 258
    \stemUp bes2. :32 | % 259
    \stemUp bes2. :32 | \barNumberCheck #260
    \stemUp bes2. :32 | % 261
    \stemUp as2. :32 _\pp | % 262
    \stemUp as2. :32 | % 263
    \stemUp as2. :32 | % 264
    \stemUp as2. :32 \pageBreak | % 265
    \stemUp as2. :32 _\< | % 266
    \stemUp as2. :32 | % 267
    \stemUp as2. :32 | % 268
    \stemUp as2. :32 | % 269
    \stemUp fis2. :32 _\! _\fz | \barNumberCheck #270
    \stemUp fis2. :32 | % 271
    \stemUp a8 _\p \stemUp gis8 \stemUp fis8 \stemUp gis8 \stemUp a8
    \stemUp gis8 \pageBreak | % 272
    \stemUp fis8 _\< \stemUp gis8 \stemUp a8 \stemUp gis8 \stemUp fis8
    \stemUp gis8 | % 273
    \stemUp a8 \stemUp gis8 \stemUp fis8 \stemUp gis8 \stemUp a8 \stemUp
    gis8 | % 274
    \stemUp fis8 _\! \stemUp gis8 \stemUp a8 \stemUp gis8 \stemUp fis8
    \stemUp gis8 | % 275
    \stemUp a8 _\f _\< \stemUp gis8 \stemUp fis8 \stemUp gis8 \stemUp a8
    \stemUp gis8 | % 276
    \stemUp fis8 \stemUp gis8 \stemUp a8 \stemUp gis8 \stemUp fis8
    \stemUp gis8 \pageBreak | % 277
    \stemUp f2. :32 _\! _\fff | % 278
    \stemUp f2. :32 | % 279
    \stemUp f2. :32 | \barNumberCheck #280
    \stemUp f2. :32 | % 281
    \stemUp e2. ~ -> | % 282
    \stemUp e2. ~ \pageBreak | % 283
    \stemUp e2. ~ _\markup{ \italic {dim.} } _\> | % 284
    \stemUp e2. | % 285
    \stemUp e2. ~ _\! _\mf | % 286
    \stemUp e2. ~ | % 287
    \stemUp e2. ~ _\p \pageBreak | % 288
    \stemUp e2. ~ | % 289
    \stemUp e2. ~ | \barNumberCheck #290
    \stemUp e2. | % 291
    R2.*2 | % 293
    r4 \stemDown b''8 _\ppp \stemDown b8 \stemDown b4 \pageBreak | % 294
    \stemDown e,4 r4 r4 | % 295
    R2.*2 | % 297
    \stemDown b'4 ^ "pizz." r4 r4 | % 298
    \stemDown e,4 r4 r4 | % 299
    R2. | \barNumberCheck #300
    \stemDown e4 _\ff ^ "arco" r4 r4 \bar "|."
    }

PartPTwoOneVoiceTwo =  \relative cis {
    \repeat volta 2 {
        \clef "bass" \time 3/4 \key g \major \transposition c s1*3 \bar
        "||"
        s4*9 \pageBreak s4*21 \pageBreak s2*9 \pageBreak | % 21
         \once \override NoteHead.style = ##f \stemUp cis4 s2*7
        \pageBreak | % 26
         \once \override NoteHead.style = ##f \stemUp cis4 s2*7
        \pageBreak s4*15 \pageBreak s4*17 \stemDown e,4 \pageBreak | % 42
        \stemDown e4 \stemDown e4 \stemDown e4 | % 43
        \stemDown e4 \stemDown e'4 \stemDown e,4 | % 44
        \stemDown e4 \stemDown e4 \stemDown e4 | % 45
        \stemDown e4 \stemDown e'4 \stemDown e,4 | % 46
        \stemDown e4 \stemDown e4 \stemDown e4 \pageBreak | % 47
        \stemDown e4 \stemDown e'4 \stemDown e,4 | % 48
        \stemDown e4 \stemDown e4 \stemDown e4 s1*3 \pageBreak s4*21 }
    \pageBreak | \barNumberCheck #60
     \once \override NoteHead.style = ##f \stemUp cis'4 s1*5 \pageBreak
    | % 67
     \once \override NoteHead.style = ##f \stemUp cis4 s2 \bar "||"
    \key e \major s1*3 \pageBreak | % 72
     \once \override NoteHead.style = ##f \stemUp cis4 s2*7 \pageBreak | % 77
     \once \override NoteHead.style = ##f \stemUp cis4 s2*7 \pageBreak | % 82
     \once \override NoteHead.style = ##f \stemUp cis4 s2*7 \pageBreak | % 87
     \once \override NoteHead.style = ##f \stemUp cis4 s2*7 \pageBreak
    s4*21 \pageBreak s1*6 \pageBreak s2*9 \pageBreak s2*9 \pageBreak
    s1*3 \bar "||"
    \key g \major s4*9 \pageBreak s4*21 \pageBreak s4*27 \bar "||"
    \pageBreak | % 142
     \once \override NoteHead.style = ##f \stemUp cis4 s4*23 \pageBreak
    | \barNumberCheck #150
     \once \override NoteHead.style = ##f \stemUp cis4 s4*23 \pageBreak
    | % 158
     \once \override NoteHead.style = ##f \stemUp cis4 s4*23 \pageBreak
    | % 166
     \once \override NoteHead.style = ##f \stemUp cis4 s4*23 \pageBreak
    s1. \repeat volta 2 {
        s1*3 \pageBreak s2*9 \pageBreak s2*9 }
    s2. \bar "||"
    \pageBreak \repeat volta 2 {
        s4*21 \pageBreak s2*9 \pageBreak s4*21 \pageBreak | % 213
         \once \override NoteHead.style = ##f \stemUp cis4 s4*23
        \pageBreak s2*9 \pageBreak s4*15 \pageBreak s4*15 \pageBreak
        s4*9 }
    s4*9 \pageBreak s2*9 \bar "||"
    \pageBreak s4*27 \pageBreak s4*21 \pageBreak s4*21 \pageBreak s4*15
    \pageBreak s2*9 \pageBreak s4*15 \pageBreak s2*9 \pageBreak s4*21
    \bar "|."
    }


% The score definition
\score {
    <<
        
        \new StaffGroup
        <<
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = \markup { \center-column { \line {"Flauti"} \line {"I. II."} } }
                    \set Staff.shortInstrumentName = "Fl. I. II."
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneVoiceOne" {  \PartPOneVoiceOne }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Flute 2"
                    \set Staff.shortInstrumentName = "Fl. 2"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPTwoVoiceOne" {  \PartPTwoVoiceOne }
                        >>
                    >>
                
                >>
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = \markup { \center-column { \line {"Oboi"} \line {"I. II."} } }
                    \set Staff.shortInstrumentName = "Ob. I. II."
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPThreeVoiceOne" {  \voiceOne \PartPThreeVoiceOne }
                        \context Voice = "PartPThreeVoiceThree" {  \voiceTwo \PartPThreeVoiceThree }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Oboe 2"
                    \set Staff.shortInstrumentName = "Ob. 2"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPFourVoiceOne" {  \voiceOne \PartPFourVoiceOne }
                        \context Voice = "PartPFourVoiceThree" {  \voiceTwo \PartPFourVoiceThree }
                        >>
                    >>
                
                >>
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = \markup { \center-column { \line {"Clarinetti"} \line {"I. II. A"} } }
                    \set Staff.shortInstrumentName = "Cl. I. II."
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPFiveVoiceOne" {  \PartPFiveVoiceOne }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Clarinet in A 2"
                    \set Staff.shortInstrumentName = "Cl. in A 2"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPSixVoiceOne" {  \PartPSixVoiceOne }
                        >>
                    >>
                
                >>
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = \markup { \center-column { \line {"Fagotti"} \line {"I. II."} } }
                    \set Staff.shortInstrumentName = "Fag. I. II."
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPSevenVoiceOne" {  \PartPSevenVoiceOne }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Bassoon 2"
                    \set Staff.shortInstrumentName = "Bsn. 2"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPEightVoiceOne" {  \PartPEightVoiceOne }
                        >>
                    >>
                
                >>
            
            >>
        \new StaffGroup
        <<
            \new StaffGroup \with { }
            
            <<
                \new StaffGroup \with { systemStartDelimiter =
                    #'SystemStartBrace }
                
                <<
                    \new Staff
                    <<
                        \set Staff.instrumentName = \markup { \center-column { \line {"Corni"} \line {"I. II. E"} } }
                        \set Staff.shortInstrumentName = \markup { \center-column { \line {"Cor."} \line {"I. II. E"} } }
                        
                        \context Staff << 
                            \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                            \context Voice = "PartPNineVoiceOne" {  \PartPNineVoiceOne }
                            >>
                        >>
                    \new Staff
                    <<
                        \set Staff.instrumentName = "Horn in E 3"
                        \set Staff.shortInstrumentName = "Hn. in E 3"
                        
                        \context Staff << 
                            \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                            \context Voice = "PartPOneZeroVoiceOne" {  \PartPOneZeroVoiceOne }
                            >>
                        >>
                    
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = \markup { \center-column { \line {"Corni"} \line {"III. IV. E"} } }
                    \set Staff.shortInstrumentName = \markup { \center-column { \line {"Cor."} \line {"III. IV. E"} } }
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneOneVoiceOne" {  \voiceOne \PartPOneOneVoiceOne }
                        \context Voice = "PartPOneOneVoiceTwo" {  \voiceTwo \PartPOneOneVoiceTwo }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Horn in E 4"
                    \set Staff.shortInstrumentName = "Hn. in E 4"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneTwoVoiceOne" {  \voiceOne \PartPOneTwoVoiceOne }
                        \context Voice = "PartPOneTwoVoiceTwo" {  \voiceTwo \PartPOneTwoVoiceTwo }
                        >>
                    >>
                
                >>
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = \markup { \center-column { \line {"Trombe"} \line {"I. II. E"} } }
                    \set Staff.shortInstrumentName = \markup { \center-column { \line {"Trbe."} \line {"I. II."} } }
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneThreeVoiceOne" {  \voiceOne \PartPOneThreeVoiceOne }
                        \context Voice = "PartPOneThreeVoiceTwo" {  \voiceTwo \PartPOneThreeVoiceTwo }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Trumpet in E 2"
                    \set Staff.shortInstrumentName = "Tpt. in E 2"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneFourVoiceOne" {  \PartPOneFourVoiceOne }
                        >>
                    >>
                
                >>
            
            >>
        \new Staff
        <<
            \set Staff.instrumentName = "Timpani"
            \set Staff.shortInstrumentName = "Timp."
            
            \context Staff << 
                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                \context Voice = "PartPOneFiveVoiceOne" {  \voiceOne \PartPOneFiveVoiceOne }
                \context Voice = "PartPOneFiveVoiceTwo" {  \voiceTwo \PartPOneFiveVoiceTwo }
                >>
            >>
        \new RhythmicStaff
        <<
            \set RhythmicStaff.instrumentName = "Triangolo"
            \set RhythmicStaff.shortInstrumentName = "Trgl."
            
            \context RhythmicStaff << 
                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                \context Voice = "PartPOneSixVoiceOne" {  \voiceOne \PartPOneSixVoiceOne }
                \context Voice = "PartPOneSixVoiceTwo" {  \voiceTwo \PartPOneSixVoiceTwo }
                >>
            >>
        \new StaffGroup \with { systemStartDelimiter =
            #'SystemStartBrace }
        
        <<
            \new Staff
            <<
                \set Staff.instrumentName = \markup { \center-column { \line {"Violini"} \line {"I."} } }
                \set Staff.shortInstrumentName = "Viol. I."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneSevenVoiceOne" {  \voiceOne \PartPOneSevenVoiceOne }
                    \context Voice = "PartPOneSevenVoiceTwo" {  \voiceTwo \PartPOneSevenVoiceTwo }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = \markup { \center-column { \line {"Violini"} \line {"II."} } }
                \set Staff.shortInstrumentName = "Viol. II."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneEightVoiceOne" {  \voiceOne \PartPOneEightVoiceOne }
                    \context Voice = "PartPOneEightVoiceTwo" {  \voiceTwo \PartPOneEightVoiceTwo }
                    >>
                >>
            
            >>
        \new Staff
        <<
            \set Staff.instrumentName = "Viole"
            \set Staff.shortInstrumentName = "Vle"
            
            \context Staff << 
                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                \context Voice = "PartPOneNineVoiceOne" {  \voiceOne \PartPOneNineVoiceOne }
                \context Voice = "PartPOneNineVoiceTwo" {  \voiceTwo \PartPOneNineVoiceTwo }
                >>
            >>
        \new Staff
        <<
            \set Staff.instrumentName = "Violoncelli"
            \set Staff.shortInstrumentName = "Vcl."
            
            \context Staff << 
                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                \context Voice = "PartPTwoZeroVoiceOne" {  \voiceOne \PartPTwoZeroVoiceOne }
                \context Voice = "PartPTwoZeroVoiceTwo" {  \voiceTwo \PartPTwoZeroVoiceTwo }
                >>
            >>
        \new Staff
        <<
            \set Staff.instrumentName = "Contrabassi"
            \set Staff.shortInstrumentName = "Cb."
            
            \context Staff << 
                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                \context Voice = "PartPTwoOneVoiceOne" {  \voiceOne \PartPTwoOneVoiceOne }
                \context Voice = "PartPTwoOneVoiceTwo" {  \voiceTwo \PartPTwoOneVoiceTwo }
                >>
            >>
        
        >>
    \layout {}
    % To create MIDI output, uncomment the following line:
    %  \midi {\tempo 4 = 240 }
    }

