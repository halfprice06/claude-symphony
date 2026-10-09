\version "2.24.3"
% automatically converted by musicxml2ly from ../xml/Tchaikovsky_Sym6_mvt1.musicxml
\pointAndClickOff

%% additional definitions required by the score:
più  = #(make-dynamic-script "più ")
pppppp = #(make-dynamic-script "pppppp")
sfff = #(make-dynamic-script "sfff")

\header {
    title =  "Symphony No. 6, Pathétique"
    composer =  \markup \column {
        \line { "Pyotr Ilyich Tchaikovsky"}
        \line { ""} }
    
    poet =  "Пётр Ильич Чайкoвский"
    encodingsoftware =  "MuseScore 4.1.0"
    encodingdate =  "2023-07-21"
    source =  "http://musescore.com/user/19710/scores/7569779"
    subtitle =  \markup \column {
        \line { "1"}
        \line { ""} }
    
    }

#(set-global-staff-size 17.714285714285715)
\paper {
    
    paper-width = 42.01\cm
    paper-height = 59.41\cm
    top-margin = 1.0\cm
    bottom-margin = 2.0\cm
    left-margin = 1.0\cm
    right-margin = 1.0\cm
    indent = 3.7417813765182184\cm
    short-indent = 1.8708906882591092\cm
    }
\layout {
    \context { \Score
        skipBars = ##t
        }
    }
PartPOneVoiceOne =  \relative cis''' {
    \clef "treble" \time 4/4 \key d \major \transposition c'' | % 1
    R1*11 \break ^\markup{ \bold {Adagio} } | % 12
    R1*5 | % 17
    R1*2 ^\markup{ \italic {ritenuto} } \bar "||"
    R1*5 \pageBreak ^\markup{ \bold {Allegro non troppo} } | % 24
    R1*6 | \barNumberCheck #30
    \time 2/4  R2 \break | % 31
    \time 4/4  R1*6 \break | % 37
    R1*7 \pageBreak | % 44
    R1*4 | % 48
    r2 r8 \stemDown cis8 ( _\p \stemDown b8 \stemDown a8 | % 49
    \stemDown gis8 ) r8 r4 r2 \break | \barNumberCheck #50
    R1*4 \pageBreak | % 54
    R1*5 \break | % 59
    R1*5 \pageBreak | % 64
    R1*2 | % 66
    r2 r16 \stemDown dis16 -. _\f ^\markup{ \italic {solo} } \stemDown
    dis16 -. \stemDown dis16 -. \stemDown dis16 ( \stemDown fis16 )
    \stemDown eis16 -. \stemDown dis16 -. | % 67
    \stemDown cisis2 ( ^\markup{ \bold {Un poco animando} } \stemDown
    dis8 ) r8 r4 | % 68
    r2 r16 \stemDown fis16 -. _\ff \stemDown fis16 -. \stemDown fis16 -.
    \stemDown fis16 ( \stemDown a16 ) \stemDown gis16 -. \stemDown fis16
    -. \pageBreak | % 69
    \stemDown eis2 ( \stemDown fis8 ) r8 r4 | \barNumberCheck #70
    r2 r16 \stemDown a16 -. \stemDown a16 -. \stemDown a16 -. \stemDown
    a16 ( \stemDown c16 ) \stemDown b16 -. \stemDown a16 -. | % 71
    \stemDown f16 ( \stemDown e16 \stemDown d16 \stemDown c16 ) \stemUp
    b16 ( \stemUp a16 \stemUp f16 \stemUp e16 ) r16 \stemDown a'16 -.
    \stemDown a16 -. \stemDown a16 -. \stemDown a16 ( \stemDown c16 )
    \stemDown b16 -. \stemDown a16 -. | % 72
    \stemDown f16 ( \stemDown e16 \stemDown d16 \stemDown c16 ) \stemUp
    b16 ( \stemUp a16 \stemUp f16 \stemUp e16 ) r16 \stemDown a'16 -.
    \stemDown a16 -. \stemDown a16 -. \stemDown a16 ( \stemDown c16 )
    \stemDown b16 -. \stemDown a16 -. | % 73
    r16 ^\markup{ \bold {Un poco più animato} } \stemUp a,16 -. \stemUp
    a16 -. \stemUp a16 -. \stemUp a16 ( \stemUp c16 \stemUp b16 \stemUp
    a16 ) r16 \stemDown a'16 -. \stemDown a16 -. \stemDown a16 -.
    \stemDown a16 ( \stemDown c16 \stemDown b16 \stemDown a16 )
    \pageBreak | % 74
    r16 \stemUp a,16 -. \stemUp a16 -. \stemUp a16 -. \stemUp a16 (
    \stemUp c16 \stemUp b16 \stemUp a16 ) r16 \stemUp a16 -. \stemUp a16
    -. \stemUp a16 -. \stemUp a16 ( \stemUp c16 \stemUp b16 \stemUp a16
    ) | % 75
    r16 \stemUp a16 -. \stemUp a16 -. \stemUp a16 -. \stemUp a16 (
    \stemUp c16 \stemUp b16 \stemUp a16 ) r16 \stemUp a16 -. \stemUp a16
    -. \stemUp a16 -. \stemUp a16 ( \stemUp cis16 \stemUp b16 \stemUp a16
    ) | % 76
    r16 \stemUp a16 -. \stemUp a16 -. \stemUp a16 -. \stemUp a16 (
    \stemUp cis16 \stemUp b16 \stemUp a16 ) r2 ^\markup{ \italic {Große
            Flöte} } ^ "vorbereiten" ^ "" | % 77
    R1 \break | % 78
    R1*5 \pageBreak | % 83
    R1 | % 84
    R1*3 ^\markup{ \italic {ritardando molto} } | % 87
    R1*2 ^\markup{ \bold {Adagio} } \bar "||"
    R1*4 ^\markup{ \bold {Andante} } | % 93
    R1 \break ^\markup{ \italic {incalzando} } | % 94
    R1 | % 95
    R1*2 ^\markup{ \italic {ritenuto} } | % 97
    R1*2 ^\markup{ \italic {come prima} } | % 99
    R1*2 ^\markup{ \italic {ritenuto} } \bar "||"
    R1*2 \pageBreak ^\markup{ \bold {Moderato mosso} } | % 103
    R1*5 \break | % 108
    R1*4 \pageBreak | % 112
    R1*4 \break | % 116
    R1*4 \pageBreak | \barNumberCheck #120
    R1*5 \break | % 125
    R1*2 | % 127
    R1*3 ^\markup{ \italic {ritenuto} } \bar "||"
    R1*2 \pageBreak ^\markup{ \bold {Andante} } | % 132
    R1*2 | % 134
    R1*2 ^\markup{ \italic {incalzando} } | % 136
    R1*2 \pageBreak ^\markup{ \italic {ritenuto} } | % 138
    R1*2 ^\markup{ \italic {incalzando} } | \barNumberCheck #140
    R1*2 ^\markup{ \italic {ritenuto} } \bar "||"
    R1*3 \break ^\markup{ \bold {Moderato assai} } | % 145
    R1*7 | % 152
    R1*2 ^\markup{ \italic {rallentando} } | % 154
    R1*2 \pageBreak ^\markup{ \bold {Adagio mosso} } | % 156
    R1*2 | % 158
    R1*3 ^\markup{ \italic {ritardando molto} } \bar "||"
    \key c \major R1*4 \pageBreak ^\markup{ \bold {Allegro vivo} } | % 165
    R1*7 \pageBreak | % 172
    R1*6 \pageBreak | % 178
    R1*5 \break | % 183
    R1*5 \pageBreak | % 188
    R1*4 \break | % 192
    R1*4 \pageBreak | % 196
    R1*5 \break | % 201
    R1*6 \pageBreak | % 207
    R1*6 \pageBreak | % 213
    R1*4 \break | % 217
    R1*4 \pageBreak | % 221
    R1*5 \break | % 226
    R1*5 \break | % 231
    R1*6 \pageBreak | % 237
    R1*5 \pageBreak | % 242
    r2 r4 \stemUp a16 ( _\ff \stemUp ais16 \stemUp b16 \stemUp ais16 ) | % 243
    \stemDown cis16 ( \stemDown b16 ) \stemDown b8 \stemDown ais16 (
    \stemDown b16 \stemDown cis16 \stemDown b16 ) \stemDown d16 (
    \stemDown cis16 ) \stemDown cis8 \stemDown bis16 ( \stemDown cis16
    \stemDown d16 \stemDown cis16 ) | % 244
    \stemDown e16 ( \stemDown d16 ) \stemDown d8 \stemDown fis16 (
    \stemDown e16 ) \stemDown e8 \stemDown g16 ( \stemDown fis16 )
    \stemDown fis8 r4 | % 245
    r4 r16 \stemDown fis16 ( _\fff \stemDown eis16 \stemDown fis16 )
    \stemDown g16 ( \stemDown fis16 ) \stemDown fis8 r4 \pageBreak | % 246
    r4 r16 \stemDown fis16 ( \stemDown eis16 \stemDown fis16 ) \stemDown
    g16 ( \stemDown fis16 ) \stemDown fis8 \stemDown fis16 ( \stemDown e16
    ) \stemDown e8 | % 247
    \stemDown g16 ( \stemDown fis16 ) \stemDown fis8 \stemUp b,16 (
    \stemUp ais16 ) \stemUp ais8 \stemDown cis16 ( \stemDown b16 )
    \stemDown b8 r4 | % 248
    R1 | % 249
    r4 \stemDown cis8 _\ff \stemDown d8 \stemDown e4 -> \stemDown d8 r8
    | \barNumberCheck #250
    r4 \stemDown cis16 ( \stemDown fis16 ) \stemDown fis16 ( \stemDown d16
    ) \stemDown e4 -> \stemDown d8 r8 | % 251
    r4 \stemDown e8 \stemDown fis8 \stemDown g4 -> \stemDown fis8 r8
    \break | % 252
    r4 \stemDown e16 ( \stemDown a16 ) \stemDown a16 ( \stemDown fis16 )
    \stemDown g4 -> \stemDown fis8 r8 | % 253
    r4 \stemDown fis8 \stemDown gis8 \stemDown a8 ( -> \stemDown gis8 )
    r4 | % 254
    r4 \stemDown fis16 ( \stemDown gis16 ) \stemDown a16 ( \stemDown fis16
    ) \stemDown a8 ( -> \stemDown gis8 ) r4 | % 255
    r4 \stemDown cis16 ( _\ff \stemDown b16 ) \stemDown b16 -. \stemDown
    b16 -. \stemDown d16 ( \stemDown cis16 ) \stemDown cis16 -.
    \stemDown cis16 -. r4 | % 256
    r4 \stemDown fis16 ( \stemDown a,16 ) \stemDown a16 -. \stemDown a16
    -. \stemDown a16 ( \stemDown gis16 ) \stemDown gis16 -. \stemDown
    gis16 -. r4 \pageBreak | % 257
    r4 \stemDown b16 ( \stemDown a16 ) \stemDown a16 -. \stemDown a16 -.
    \stemDown cis16 ( \stemDown b16 ) \stemDown b16 -. \stemDown b16 -.
    r4 | % 258
    r4 \stemDown e16 ( \stemDown gis,16 ) \stemDown gis16 -. \stemDown
    gis16 -. \stemDown gis16 ( \stemDown fis16 ) \stemDown fis16 -.
    \stemDown fis16 -. r4 | % 259
    R1*2 | % 261
    r2 r4 \stemDown a,8 ( _ "" _\markup{ \italic {cresc.} } \stemDown b8
    | % 262
    \stemDown c8 \stemDown a8 ) \stemDown c8 ( \stemDown d8 \stemDown es8
    \stemDown c8 ) \stemDown es8 _\ff \stemDown f8 \pageBreak | % 263
    \stemDown ges8 r8 \stemDown es8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown es8 \stemDown f8 \stemDown ges8 }
    | % 264
    \stemDown ges8 r8 \stemDown es8 r8 r4 \stemDown fis8 \stemDown gis8
    | % 265
    \stemDown a8 r8 \stemDown fis8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown gis8 \stemDown a8 }
    | % 266
    \stemDown a8 r8 \stemDown fis8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown gis8 \stemDown a8 }
    | % 267
    \stemDown a16 ( _\fff \stemDown gis16 \stemDown a16 \stemDown gis16
    \stemDown a16 \stemDown gis16 \stemDown a16 \stemDown gis16 )
    \stemDown a16 ( \stemDown gis16 \stemDown a16 \stemDown eis16 )
    \stemDown fis16 ( \stemDown eis16 \stemDown fis16 \stemDown d16 )
    \pageBreak | % 268
    \stemDown es16 ( \stemDown d16 \stemDown es16 \stemDown d16
    \stemDown es16 \stemDown d16 \stemDown es16 \stemDown d16 )
    \stemDown es16 ( \stemDown d16 \stemDown es16 \stemDown b16 )
    \stemDown c16 ( \stemDown b16 \stemDown c8 ) | % 269
    R1*4 \pageBreak ^\markup{ \italic {Gr. Flöte vorbereiten} } | % 273
    R1*12 \pageBreak | % 285
    R1*17 \break | % 302
    R1*3 \bar "||"
    \pageBreak | % 305
    \key b \major R1*4 ^\markup{ \bold {Andante come prima} } | % 309
    R1*2 \pageBreak ^\markup{ \italic {incalzando} } | % 311
    R1*2 ^\markup{ \italic {ritenuto} } | % 313
    R1*2 ^\markup{ \italic {incalzando} } | % 315
    R1*2 \pageBreak ^\markup{ \italic {ritenuto} } | % 317
    R1*8 ^\markup{ \bold {Tempo I} } | % 325
    R1 \break ^\markup{ \italic {ritenuto} } | % 326
    R1*3 ^\markup{ \bold {Meno} } | % 329
    R1*2 ^\markup{ \italic {animando} } | % 331
    R1*3 \pageBreak ^\markup{ \italic {rallentando} } | % 334
    R1 ^\markup{ \bold {quasi adagio} } \bar "||"
    R1*8 \pageBreak ^\markup{ \bold {Andante mosso} } | % 343
    R1*12 \bar "|."
    }

PartPTwoVoiceOne =  \relative fis' {
    \clef "treble" \time 4/4 \key d \major | % 1
    R1*11 \break | % 12
    R1*7 \bar "||"
    R1*4 | % 23
    r2 r16 \stemUp fis16 -. ^ "I." _\p \stemUp gis16 -. \stemUp ais16 -.
    \stemUp <fis b>8 ( -. _\< \stemUp <g cis>8 ) -. \pageBreak | % 24
    \stemDown <gis d'>4 ( _\! _\> \stemDown <ais cis>8 ) r8 _\! r4
    \stemDown <fis b>16 ( _\p _\< \stemDown <g e'>16 \stemDown <fis d'>16
    \stemDown <g b>16 ) | % 25
    \stemDown <gis d'>4 ( _\! _\> \stemDown <ais cis>8 ) r8 _\! r4
    \stemUp fis'16 ( _\p \stemUp e16 ) \stemUp e16 -. \stemUp e16 -. | % 26
    \stemUp g16 ( \stemUp fis16 ) \stemUp fis16 -. \stemUp fis16 -.
    \stemUp b16 ( -> \stemUp d,16 ) \stemUp d16 -. \stemUp d16 -.
    \stemUp d16 ( \stemUp cis16 ) \stemUp cis16 -. \stemUp cis16 -.
    \stemUp a'16 ( -> \stemUp cis,16 ) \stemUp cis16 -. \stemUp cis16 -.
    | % 27
    \stemUp cis16 ( \stemUp b16 ) \stemUp b16 -. \stemUp b16 -. \stemUp
    g'16 ( -> \stemUp fis16 ) \stemUp e16 -. \stemUp d16 -. \stemUp cis16
    -. \stemUp b16 -. \stemUp a16 -. \stemUp g16 -. r4 | % 28
    R1*2 | \barNumberCheck #30
    \time 2/4  R2 \break | % 31
    \time 4/4  R1*6 \break | % 37
    R1*7 \pageBreak | % 44
    r2 r8 \stemDown fis''8 ( _\pp ^ "I." \stemDown e8 \stemDown d8 | % 45
    \stemDown cis8 ) \stemDown b8 ( \stemDown a8 \stemDown gis8
    \stemDown fis8 ) \stemDown e8 ( \stemDown d8 \stemDown cis8 ) | % 46
    \stemDown cis'16 ( \stemDown d16 \stemDown cis16 \stemDown d16
    \stemDown cis16 \stemDown d16 \stemDown cis16 \stemDown d16
    \stemDown cis8 ) r8 r4 | % 47
    R1 | % 48
    r2 r8 \stemDown cis8 ( ^ "II." _\p \stemDown b8 \stemDown a8 | % 49
    \stemDown gis8 ) \stemDown <fis fis'>8 ( _\p \stemDown <e e'>8
    \stemDown <dis dis'>8 \stemDown <cis cis'>8 ) \stemDown <b b'>8 (
    \stemDown <a a'>8 \stemDown <gis gis'>8 ) \break | \barNumberCheck
    #50
    \stemDown <gis' gis'>16 ( \stemDown <a a'>16 \stemDown <gis gis'>16
    \stemDown <a a'>16 \stemDown <gis gis'>16 \stemDown <a a'>16
    \stemDown <gis gis'>16 \stemDown <a a'>16 \stemDown <gis gis'>8 ) r8
    r4 | % 51
    r2 r8 \stemUp cis,8 ( _\mp _\< \stemUp e8 \stemUp gis8 ) | % 52
    \stemDown <bis, bis'>8 ( -. \stemDown <dis dis'>8 ) -. \stemDown
    <gis gis'>4 ~ ~ _\! _\> \stemDown <gis gis'>8 r8 _\! r4 | % 53
    r2 r8 \stemUp cis,8 ( _\mp _\< \stemUp e8 \stemUp gis8 ) \pageBreak
    | % 54
    \stemDown <bis, bis'>8 ( -. \stemDown <dis dis'>8 ) -. \stemDown
    <gis gis'>4 ~ ~ _\! _\> \stemDown <gis gis'>8 r8 _\! r4 | % 55
    R1 | % 56
    r2 r16 \stemDown <b e>16 -. _\p _\< \stemDown <b e>16 -. \stemDown
    <b e>16 -. \stemDown <b e>16 ( \stemDown <b dis>16 ) \stemDown <gis
        cis>16 -. \stemDown <gis b>16 -. | % 57
    \stemDown <fisis b>8 -- _\! r8 r4 r16 \stemUp fisis,16 -. _\p
    ^\markup{ \bold\small {a. 2} } _\< \stemUp fisis16 -. \stemUp fisis16
    -. \stemUp fisis16 -. \stemUp fisis16 -. r8 _\! | % 58
    R1 \break | % 59
    R1*5 \pageBreak | % 64
    R1*2 | % 66
    r2 r16 ^\markup{ \italic {solo} } \stemDown dis''16 -. _\f ^\markup{
        \bold\small {a. 2} } \stemDown dis16 -. \stemDown dis16 -.
    \stemDown dis16 ( \stemDown fis16 ) \stemDown eis16 -. \stemDown dis16
    -. | % 67
    \stemDown cisis2 ( \stemDown dis8 ) r8 r4 | % 68
    r2 r16 \stemDown fis16 -. _\ff \stemDown fis16 -. \stemDown fis16 -.
    \stemDown fis16 ( \stemDown a16 ) \stemDown gis16 -. \stemDown fis16
    -. \pageBreak | % 69
    \stemDown eis2 ( \stemDown fis8 ) r8 r4 | \barNumberCheck #70
    r2 r16 \stemUp a16 -. \stemUp a16 -. \stemUp a16 -. \stemUp a16 (
    \stemUp c,16 ) \stemUp b16 -. \stemUp a16 -. | % 71
    \stemUp f'16 ( \stemUp e16 \stemUp d16 \stemUp c16 ) \stemUp b16 (
    \stemUp a16 \stemUp f16 \stemUp e16 ) r16 \stemUp a'16 -. \stemUp a16
    -. \stemUp a16 -. \stemUp a16 ( \stemUp c,16 ) \stemUp b16 -.
    \stemUp a16 -. | % 72
    \stemUp f'16 ( \stemUp e16 \stemUp d16 \stemUp c16 ) \stemUp b16 (
    \stemUp a16 \stemUp f16 \stemUp e16 ) r16 \stemUp a'16 -. \stemUp a16
    -. \stemUp a16 -. \stemUp a16 ( \stemUp c,16 ) \stemUp b16 -.
    \stemUp a16 -. | % 73
    r16 \stemUp a16 -. \stemUp a16 -. \stemUp a16 -. \stemUp a16 (
    \stemUp c16 \stemUp b16 \stemUp a16 ) r16 \stemUp a'16 -. \stemUp a16
    -. \stemUp a16 -. \stemUp a16 ( \stemUp c,16 \stemUp b16 \stemUp a16
    ) \pageBreak | % 74
    r16 \stemDown a16 -. ^\markup{ \bold\small {a. 2} } \stemDown a16 -.
    \stemDown a16 -. \stemDown a16 ( \stemDown c16 \stemDown b16
    \stemDown a16 ) r16 \stemDown a16 -. \stemDown a16 -. \stemDown a16
    -. \stemDown a16 ( \stemDown c16 \stemDown b16 \stemDown a16 ) | % 75
    r16 \stemDown a16 -. \stemDown a16 -. \stemDown a16 -. \stemDown a16
    ( \stemDown c16 \stemDown b16 \stemDown a16 ) r16 \stemDown a16 -.
    \stemDown a16 -. \stemDown a16 -. \stemDown a16 ( \stemDown cis16
    \stemDown b16 \stemDown a16 ) | % 76
    r16 \stemDown a16 -. \stemDown a16 -. \stemDown a16 -. \stemDown a16
    ( \stemDown cis16 \stemDown b16 \stemDown a16 ) r2 | % 77
    R1 \break | % 78
    R1*5 \pageBreak | % 83
    R1*6 \bar "||"
    R1*5 \break | % 94
    R1*7 \bar "||"
    \stemUp a,4 ~ _\p ^ "I." _\< \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown b8 ( \stemDown cis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 ) \stemDown d8 ( -- \stemDown e8 -- }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 -- \stemDown g8 -- \stemDown a8 ) -- }
    | % 102
    \stemDown b4 ( ~ -> _\! _\> \stemDown b16 \stemDown fis16 \stemDown
    d16 \stemDown cis16 \stemDown b4 ~ \stemDown b8 ) r8 \pageBreak | % 103
    \stemDown e4 ~ _\! _\p _\< \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 ( \stemDown fis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 ) \stemDown g8 ( -- \stemDown a8 -- }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 -- \stemDown cis8 -- \stemDown d8 ) -- }
    | % 104
    \stemDown e4 ( ~ -> _\! _\> \stemDown e16 \stemDown cis16 \stemDown
    a16 \stemDown e16 \stemDown cis8 ) r8 _\! r4 | % 105
    r4 \stemDown fis'2 ^ "I.II." ^\markup{ \bold\small {a. 2} } _ ""
    _\markup{ \italic {espress.} } \stemDown e4 -- | % 106
    \stemDown e4 ~ -> \stemDown e8. \stemDown d16 \stemDown d2 _\< | % 107
    r4 _\! \stemDown cis2 _\f _\> \stemDown b4 -- \break | % 108
    \stemDown b4 ~ -> _\! _\mf \stemDown b8. _\> \stemDown a16 \stemDown
    a4 ~ \stemDown a8 r8 _\! | % 109
    R1*3 \pageBreak | % 112
    R1 | % 113
    r4 \stemDown <cis, cis'>2 _ "" _\markup{ \italic {espress.} } ^
    "I." ^ "II." ^ "" \stemDown <b b'>4 -- | % 114
    \stemDown <b b'>4 ~ -> ~ \stemDown <b b'>8. \stemDown <a a'>16
    \stemDown <a a'>2 _\< | % 115
    r4 _\! \stemDown <gis gis'>2 _\f _\> \stemDown <fis fis'>4 -- \break
    | % 116
    \stemDown <fis fis'>4 ~ -> ~ _\! _\mf _\> \stemDown <fis fis'>8.
    \stemDown <e e'>16 \stemUp <e e'>4 ~ ~ \stemUp <e e'>8 r8 _\! | % 117
    \stemDown b'4 ~ ^\markup{ \bold\small {a. 3} } _\p \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown b8 _\< \stemDown cis8 ( \stemDown dis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ) \stemDown e8 ( -- \stemDown fis8 -- }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown gis8 -- \stemDown a8 -- \stemDown ais8 ) -- }
    | % 118
    \stemDown b4 ( ~ -> _\! _\> \stemDown b16 \stemDown gis16 \stemDown
    e16 \stemDown b16 \stemUp gis8 ) r8 _\! r4 | % 119
    \stemDown b4 ~ _\markup{ \italic {più} } _ "" \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown b8 \stemDown cis8 ( \stemDown dis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ) \stemDown e8 ( -- \stemDown fis8 -- }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 -- \stemDown a8 -- \stemDown ais8 ) -- }
    \pageBreak | \barNumberCheck #120
    \stemDown b4 ( ~ -> ^ "I." \stemDown b16 \stemDown g16 \stemDown e16
    \stemDown b16 \stemUp g8 ) r8 r4 | % 121
    r4 \stemDown e''2 _\f \stemDown d4 -- | % 122
    \stemDown d4 ~ -> \stemDown d8. \stemDown cis16 \stemDown cis4 ~
    \stemDown cis8 r8 | % 123
    r4 \stemDown cis2 _\ff \stemDown b4 -- | % 124
    \stemDown b4 ~ -> \stemDown b8. \stemDown a16 \stemDown a2 ~ \break
    | % 125
    \stemDown a8 r8 \stemDown b2 \stemDown a4 ~ | % 126
    \stemDown a8 r8 \stemDown b2 ( \stemDown a4 ) | % 127
    r4 \stemDown g4 ( _\ff \stemDown fis4 \stemDown e4 ) | % 128
    \stemDown d4 ( \stemDown cis2 ) \stemDown b4 ( | % 129
    \stemDown bes2 _\sff _\> \stemUp a4 ~ \stemUp a8 ) r8 ^\fermata _\!
    \bar "||"
    R1*2 \pageBreak | % 132
    R1*2 | % 134
    r4 r32 \stemDown a'32 ( _\f \stemDown b32 \stemDown cis32 \stemDown
    d32 \stemDown e32 \stemDown fis32 \stemDown g32 ) \stemDown a4 --
    \stemDown g8 ( \stemDown fis8 ) | % 135
    \stemDown fis4 ( \stemDown e4 ) \stemDown g4 -- \stemDown fis8 (
    \stemDown e8 ) | % 136
    \stemDown e4 ( \stemDown d4 ) r8 \stemDown fis8 ( _\> \stemDown e8
    \stemDown d8 ) | % 137
    \stemDown a8 ( _\! _\mf _\< \stemDown fis8 \stemDown d8 \stemDown
    fis8 ) \stemDown b4. ( _\! _\> \stemDown a8 ) \pageBreak | % 138
    r4 _\! r32 \stemDown a32 ( _\f \stemDown b32 \stemDown cis32
    \stemDown d32 \stemDown e32 \stemDown fis32 \stemDown g32 )
    \stemDown a4 -- \stemDown g8 ( \stemDown fis8 ) | % 139
    \stemDown fis4 ( \stemDown e4 ) \stemDown g4 -- \stemDown fis8 (
    \stemDown e8 ) | \barNumberCheck #140
    \stemDown e4 ( \stemDown d4 ) r8 \stemDown fis8 ( _\> \stemDown e8
    \stemDown d8 ) | % 141
    \stemDown a8 ( _\! _\mf _\< \stemDown fis8 \stemDown d8 \stemDown
    fis8 ) \stemDown b4. ( _\! _\f _\> \stemDown a8 ) s2 _\! \bar "||"
    r2 | % 143
    R1*2 \break | % 145
    R1*11 \pageBreak | % 156
    R1*5 \bar "||"
    \key c \major \stemDown es'8 _\ff ^\markup{ \bold\small {a. 3} } r8
    r4 r2 | % 162
    R1*2 | % 164
    r2 r4 \stemDown es,16 ( \stemDown g16 ) \stemDown g16 ( \stemDown
    es'16 ) \pageBreak | % 165
    \stemDown e8 ^ "I.II." ^\markup{ \bold\small {a. 2} } r8 r4 r2 | % 166
    R1*2 | % 168
    r2 r4 \stemDown e,16 ( _\ff \stemDown g16 ) \stemDown g16 (
    \stemDown e'16 ) | % 169
    \stemDown f8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown f16 _\sff \stemDown f16 \stemDown f16 }
    \stemDown f8 ~ \stemDown f4 ~ | \barNumberCheck #170
    \stemDown f8 \stemDown g8 -> \stemDown f8 -> \stemDown g8 ->
    \stemDown gis8 -> \stemDown a8 -> r4 | % 171
    R1 \pageBreak | % 172
    r2 r4 r8 \stemDown d,8 ~ _\f | % 173
    \stemDown d4. \stemDown d8 ~ \stemDown d4. \stemDown d8 ~ | % 174
    \stemDown d8 r8 r4 r2 | % 175
    R1 | % 176
    r2 r4 r8 \stemDown a'8 ~ _\f | % 177
    \stemDown a4. \stemDown a8 ~ \stemDown a4. \stemDown a8 ~ \pageBreak
    | % 178
    \stemDown a8 r8 r4 r2 | % 179
    r4 \stemDown e8 -. _\mf \stemDown fis8 ( \stemDown b,8 ) \stemDown e8
    -. r4 | \barNumberCheck #180
    r2 r4 r8 \stemDown e8 ~ _\f ^ "I." | % 181
    \stemDown e4. \stemDown e8 ~ \stemDown e4. \stemDown e8 ~ | % 182
    \stemDown e8 r8 r4 r2 \break | % 183
    R1*2 | % 185
    r2 r4 \stemDown a,16 ( _\ff ^\markup{ \bold\small {a. 3} } \stemDown
    d16 \stemDown cis16 \stemDown a16 ) | % 186
    \stemDown b16 ( \stemDown e16 \stemDown d16 \stemDown b16 )
    \stemDown cis16 ( \stemDown fis16 \stemDown e16 \stemDown cis16 )
    \stemDown d16 ( \stemDown g16 \stemDown fis16 \stemDown d16
    \stemDown cis8 ) r8 | % 187
    r2 r4 \stemDown fis,16 ( _\fff \stemDown b16 \stemDown a16 \stemDown
    fis16 ) \pageBreak | % 188
    \stemDown g16 ( \stemDown cis16 \stemDown b16 \stemDown g16 )
    \stemDown a16 ( \stemDown d16 \stemDown cis16 \stemDown a16 )
    \stemDown b16 ( \stemDown e16 \stemDown d16 \stemDown b16 )
    \stemDown bes16 ( \stemDown f'16 \stemDown es16 \stemDown bes16 ) | % 189
    \stemDown bes16 ( \stemDown f'16 \stemDown es16 \stemDown bes16 )
    \stemDown bes16 ( \stemDown f'16 \stemDown es16 \stemDown bes16 )
    \stemDown bes16 ( \stemDown f'16 \stemDown es16 \stemDown bes16 )
    \stemDown bes16 ( \stemDown f'16 \stemDown es16 \stemDown bes16 ) |
    \barNumberCheck #190
    \stemDown bes16 ( \stemDown f'16 \stemDown es16 \stemDown bes16 )
    \stemDown bes16 ( \stemDown f'16 \stemDown es16 \stemDown bes16 )
    \stemDown bes16 ( \stemDown f'16 \stemDown es16 \stemDown bes16 )
    \stemDown bes16 ( \stemDown f'16 \stemDown es16 \stemDown bes16 ) | % 191
    \stemDown bes16 ( \stemDown f'16 \stemDown es16 \stemDown bes16 )
    \stemDown bes16 ( \stemDown f'16 \stemDown es16 \stemDown bes16 )
    \stemDown bes16 ( \stemDown f'16 \stemDown es16 \stemDown bes16 )
    \stemDown bes16 ( \stemDown f'16 \stemDown es16 \stemDown bes16 )
    \break | % 192
    \stemDown es16 ( \stemDown as16 \stemDown g16 \stemDown es16 )
    \stemDown es16 ( \stemDown as16 \stemDown g16 \stemDown es16 )
    \stemDown es16 ( \stemDown as16 \stemDown g16 \stemDown es16 )
    \stemDown es16 ( \stemDown as16 \stemDown g16 \stemDown es16 ) | % 193
    \stemDown es16 ( \stemDown as16 \stemDown g16 \stemDown es16 )
    \stemDown es16 ( \stemDown as16 \stemDown g16 \stemDown es16 )
    \stemDown es16 ( \stemDown as16 \stemDown g16 \stemDown es16 )
    \stemDown d16 ( \stemDown g16 \stemDown f16 \stemDown d16 ) | % 194
    \stemDown d16 ( \stemDown g16 \stemDown f16 \stemDown d16 )
    \stemDown d16 ( \stemDown g16 \stemDown f16 \stemDown d16 )
    \stemDown d16 ( \stemDown g16 \stemDown f16 \stemDown d16 )
    \stemDown d16 ( \stemDown g16 \stemDown f16 \stemDown d16 ) | % 195
    \stemDown f16 ( \stemDown bes16 \stemDown a16 \stemDown f16 )
    \stemDown f16 ( \stemDown bes16 \stemDown a16 \stemDown f16 )
    \stemDown f16 ( \stemDown bes16 \stemDown a16 \stemDown f16 )
    \stemDown f16 ( \stemDown bes16 \stemDown a16 \stemDown f16 )
    \pageBreak | % 196
    \stemDown d16 ( \stemDown g16 \stemDown f16 \stemDown d16 )
    \stemDown d16 ( \stemDown g16 \stemDown f16 \stemDown d16 )
    \stemDown a16 ( \stemDown e'16 \stemDown d16 \stemDown a16 )
    \stemDown a16 ( \stemDown e'16 \stemDown d16 \stemDown a16 ) | % 197
    \stemDown f16 ( \stemDown bes16 \stemDown a16 \stemDown f16 )
    \stemDown f16 ( \stemDown bes16 \stemDown a16 \stemDown f16 )
    \stemDown d16 ( \stemDown g16 \stemDown f16 \stemDown d16 )
    \stemDown a16 ( \stemDown e'16 \stemDown d16 \stemDown a16 ) | % 198
    \stemUp f16 ( \stemUp bes16 \stemUp a16 \stemUp f16 ) \stemUp d16 (
    \stemUp g16 \stemUp f16 \stemUp d16 ) r2 | % 199
    R1*2 \break | % 201
    R1*4 | % 205
    r2 \once \omit TupletBracket
    \times 4/7  {
        \stemDown a''16*161/160 ( _\p ^\markup{ \bold\small {a. 3} } _\<
        \stemDown bes16*161/160 \stemDown cis16*161/160 \stemDown d16*161/160
        \stemDown e16*161/160 \stemDown f16*161/160 \stemDown g16*161/160
        }
    \stemDown a8 ) _\! r8 | % 206
    R1 \pageBreak ^\markup{ \italic {Kleine Flöte vorbereiten} } | % 207
    R1*6 \pageBreak | % 213
    r2 r4 r8 \stemDown b,8 ~ _\ff \stemDown b'8 ~ | % 214
    \stemDown b,8 \stemDown b'8 \stemDown a,8 ~ \stemDown a'8 ~
    \stemDown a,8 \stemDown a'8 \stemDown gis,8 ~ \stemDown gis'8 ~
    \stemDown gis,8 \stemDown gis'8 \stemDown fis,8 ~ \stemDown fis'8 ~
    \stemDown fis,8 \stemDown fis'8 \stemDown e,8 ~ \stemDown e'8 ~ | % 215
    \stemDown e,8 \stemDown e'8 \stemDown d,8 ~ \stemDown d'8 ~
    \stemDown d,8 \stemDown d'8 \stemDown bis,8 ~ \stemDown bis'8 ~
    \stemDown bis,8 \stemDown bis'8 \stemDown cis,8 ~ \stemDown cis'8 ~
    \stemDown cis,8 \stemDown cis'8 \stemDown ais,8 ~ \stemDown ais'8 ~
    | % 216
    \stemDown ais,8 _\markup{ \italic {dim. un poco} } \stemDown ais'8
    \stemDown b,8 ~ \stemDown b'8 ~ \stemDown b,8 \stemDown b'8
    \stemDown gis,8 ~ \stemDown gis'8 ~ \stemDown gis,8 \stemDown gis'8
    \stemDown a,8 ~ \stemDown a'8 ~ \stemDown a,8 \stemDown a'8
    \stemDown eis,8 ~ \stemDown eis'8 ~ \break | % 217
    \stemDown eis,8 \stemDown eis'8 \stemDown fis,8 ~ \stemDown fis'8 ~
    \stemDown fis,8 \stemDown fis'8 \stemDown e,8 ~ \stemDown e'8 ~
    \stemUp e,8 \stemUp e'8 \stemUp eis,8 ~ \stemUp eis'8 ~ \stemUp eis,8
    \stemUp eis'8 r8 | % 218
    R1*3 \pageBreak | % 221
    R1*5 \break | % 226
    R1*5 \break | % 231
    R1*6 \pageBreak | % 237
    R1 | % 238
    r2 r4 \stemUp a,8 ( -. _\mp ^ "I." \stemUp bes8 ) -. | % 239
    \stemDown des8 ( -> _\markup{ \italic {cresc.} } \stemDown c8 )
    \stemDown b16 ( \stemDown c16 \stemDown des16 \stemDown b16 )
    \stemDown des8 ( -> \stemDown c8 ) \stemDown b8 ( -. \stemDown c8 )
    -. | \barNumberCheck #240
    \stemDown es8 ( -> \stemDown des8 ) \stemDown c16 ( \stemDown des16
    \stemDown es16 \stemDown des16 ) \stemDown f8 ( -> \stemDown es8 )
    \stemDown d16 ( \stemDown es16 \stemDown f16 \stemDown es16 ) | % 241
    \stemDown ges8 ( \stemDown f8 ) \stemDown e16 ( _\f ^\markup{
        \bold\small {a. 2} } \stemDown f16 \stemDown ges16 \stemDown e16
    ) \stemDown ges8 ( _\markup{ \italic {cresc.} } \stemDown f8 )
    \stemDown e16 ( \stemDown f16 \stemDown ges16 \stemDown f16 )
    \pageBreak | % 242
    \stemDown as16 ( \stemDown ges16 ) \stemDown ges8 \stemDown bes16 (
    \stemDown as16 \stemDown as8 ) \stemDown ces16 ( \stemDown bes16 )
    \stemDown bes8 \stemDown a16 ( \stemDown ais16 \stemDown b16
    \stemDown ais16 ) | % 243
    \stemDown cis16 ( _\ff \stemDown b16 ) \stemDown b8 \stemDown ais16
    ( \stemDown b16 \stemDown cis16 \stemDown b16 ) \stemDown d16 (
    \stemDown cis16 ) \stemDown cis8 \stemDown bis16 ( \stemDown cis16
    \stemDown d16 \stemDown cis16 ) | % 244
    \stemDown e16 ( \stemDown d16 ) \stemDown d8 \stemDown fis16 (
    \stemDown e16 ) \stemDown e8 \stemDown g16 ( \stemDown fis16 )
    \stemDown fis8 r4 | % 245
    r4 r16 \stemDown fis16 ( _\fff \stemDown eis16 \stemDown fis16 )
    \stemDown g16 ( \stemDown fis16 ) \stemDown fis8 r4 \pageBreak | % 246
    r4 r16 \stemDown fis16 ( \stemDown eis16 \stemDown fis16 ) \stemDown
    g16 ( \stemDown fis16 ) \stemDown fis8 \stemDown fis16 ( \stemDown e16
    ) \stemDown e8 | % 247
    \stemDown g16 ( \stemDown fis16 ) \stemDown fis8 \stemDown b,16 (
    \stemDown ais16 ) \stemDown ais8 \stemDown cis16 ( \stemDown b16 )
    \stemDown b8 \stemDown fis16 ( \stemDown e16 ) \stemDown e8 | % 248
    \stemDown g16 ( \stemDown fis16 \stemDown e16 \stemDown d16 )
    \stemDown cis16 ( \stemDown d16 \stemDown cis16 \stemDown b16 )
    \stemUp ais16 ( \stemUp g16 \stemUp fis16 \stemUp eis16 \stemUp fis8
    ) r8 | % 249
    r4 \stemDown cis''8 _\ff \stemDown d8 \stemDown e4 -> \stemDown d8 r8
    | \barNumberCheck #250
    r4 \stemDown cis16 ( \stemDown fis16 ) \stemDown fis16 ( \stemDown d16
    ) \stemDown e4 -> \stemDown d8 r8 | % 251
    r4 \stemDown e8 \stemDown fis8 \stemDown g4 -> \stemDown fis8 r8
    \break | % 252
    r4 \stemDown e16 ( \stemDown a16 ) \stemDown a16 ( \stemDown fis16 )
    \stemDown g4 -> \stemDown fis8 r8 | % 253
    r4 \stemDown fis8 \stemDown gis8 \stemDown a8 ( -> \stemDown gis8 )
    r4 | % 254
    r4 \stemDown fis16 ( \stemDown gis16 ) \stemDown a16 ( \stemDown fis16
    ) \stemDown a8 ( -> \stemDown gis8 ) r4 | % 255
    r4 \stemDown cis,16 ( _\ff \stemDown b16 ) \stemDown b16 -.
    \stemDown b16 -. \stemDown d16 ( \stemDown cis16 ) \stemDown cis16
    -. \stemDown cis16 -. r4 | % 256
    r4 \stemDown fis16 ( \stemDown a,16 ) \stemDown a16 -. \stemDown a16
    -. \stemDown a16 ( \stemDown gis16 ) \stemDown gis16 -. \stemDown
    gis16 -. r4 \pageBreak | % 257
    r4 \stemDown b16 ( \stemDown a16 ) \stemDown a16 -. \stemDown a16 -.
    \stemDown cis16 ( \stemDown b16 ) \stemDown b16 -. \stemDown b16 -.
    r4 | % 258
    r4 \stemDown e16 ( \stemDown gis,16 ) \stemDown gis16 -. \stemDown
    gis16 -. \stemDown gis16 ( \stemDown fis16 ) \stemDown fis16 -.
    \stemDown fis16 -. \stemUp fis,8 ( _\pp \stemUp gis8 | % 259
    \stemUp a8 \stemUp f8 ) \stemDown a8 ( _\markup{ \italic {cresc.} }
    \stemDown b8 \stemDown c8 \stemDown a8 ) \stemDown c8 ( \stemDown d8
    | \barNumberCheck #260
    \stemDown es8 \stemDown c8 ) \stemDown es8 ( \stemDown f8 \stemDown
    ges8 \stemDown es8 ) \stemDown es8 ( \stemDown f8 | % 261
    \stemDown ges8 \stemDown es8 ) \stemDown fis8 ( \stemDown gis8
    \stemDown a8 \stemDown fis8 ) \stemDown a8 ( \stemDown b8 | % 262
    \stemDown c8 \stemDown a8 ) \stemDown c8 ( \stemDown d8 \stemDown es8
    \stemDown c8 ) \stemDown es8 _\ff \stemDown f8 \pageBreak | % 263
    \stemDown ges8 r8 \stemDown es8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown es8 \stemDown f8 \stemDown ges8 }
    | % 264
    \stemDown ges8 r8 \stemDown es8 r8 r4 \stemDown fis8 \stemDown gis8
    | % 265
    \stemDown a8 r8 \stemDown fis8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown gis8 \stemDown a8 }
    | % 266
    \stemDown a8 r8 \stemDown fis8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown gis8 \stemDown a8 }
    | % 267
    \stemDown a16 ( _\fff \stemDown gis16 \stemDown a16 \stemDown gis16
    \stemDown a16 \stemDown gis16 \stemDown a16 \stemDown gis16 )
    \stemDown a16 ( \stemDown gis16 \stemDown a16 \stemDown eis16 )
    \stemDown fis16 ( \stemDown eis16 \stemDown fis16 \stemDown d16 )
    \pageBreak | % 268
    \stemDown es16 ( \stemDown d16 \stemDown es16 \stemDown d16
    \stemDown es16 \stemDown d16 \stemDown es16 \stemDown d16 )
    \stemDown es16 ( \stemDown d16 \stemDown es16 \stemDown b16 )
    \stemDown c16 ( \stemDown b16 \stemDown c16 \stemDown gis16 ) | % 269
    \stemDown a16 ( \stemDown gis16 \stemDown a16 \stemDown gis16
    \stemDown a16 \stemDown gis16 \stemDown a16 \stemDown eis16 )
    \stemDown fis16 ( \stemDown eis16 \stemDown fis16 \stemDown eis16
    \stemDown fis16 \stemDown eis16 \stemDown fis16 \stemDown d16 |
    \barNumberCheck #270
    \stemDown es8 ) r8 r4 r4 r8 \stemDown es32 ( _\ff \stemDown f32
    \stemDown fis32 \stemDown gis32 ) | % 271
    \stemDown a16 ( \stemDown gis16 \stemDown a16 \stemDown gis16
    \stemDown a16 \stemDown gis16 \stemDown a16 \stemDown gis16 )
    \stemDown a16 ( \stemDown gis16 \stemDown a16 \stemDown eis16 )
    \stemDown fis16 ( \stemDown eis16 \stemDown fis16 \stemDown d16 ) | % 272
    \stemDown es16 ( \stemDown d16 \stemDown es16 \stemDown d16
    \stemDown es16 \stemDown d16 \stemDown es16 \stemDown d16 )
    \stemDown es16 ( \stemDown d16 \stemDown es16 \stemDown b16 )
    \stemUp c16 ( \stemUp b16 \stemUp c16 \stemUp gis16 ) \pageBreak | % 273
    \stemUp a16 ( \stemUp gis16 \stemUp a16 \stemUp gis16 \stemUp a16
    \stemUp gis16 \stemUp a16 \stemUp eis16 ) \stemUp fis16 ( \stemUp
    eis16 \stemUp fis16 \stemUp eis16 \stemUp fis16 \stemUp eis16
    \stemUp fis16 \stemUp d16 | % 274
    \stemUp es8 ) r8 r4 r2 | % 275
    R1*9 | % 284
    r2 r4 \stemDown fis''4 ^\markup{ \bold\small {a. 3} } _\fff
    \pageBreak | % 285
    \stemDown e2 \stemDown d2 ~ | % 286
    \stemDown d2. \stemDown d4 | % 287
    \stemDown cis2 \stemDown b2 ~ | % 288
    \stemDown b2. \stemDown a4 | % 289
    \stemDown g2 \stemDown fis2 ~ | \barNumberCheck #290
    \stemDown fis2. \stemDown e4 | % 291
    \stemDown d2 \stemDown cis2 ~ | % 292
    \stemDown cis2. \stemDown cis4 | % 293
    \stemDown b2 \stemUp ais2 ~ | % 294
    ais1 | % 295
    \stemUp g2 \stemUp fis2 ~ | % 296
    fis1 | % 297
    R1*5 \break | % 302
    R1*3 \bar "||"
    \pageBreak | % 305
    \key b \major r2 r8 \stemDown dis''8 ( _\p ^ "I.II." ^\markup{
        \bold\small {a. 2} } ^\markup{ \italic {con dolcezza} }
    \stemDown cis8 \stemDown b8 ) | % 306
    \stemDown gis8 ( _\< \stemDown fis8 \stemDown dis8 \stemDown fis8 )
    \stemDown b4. ( _\! _\> \stemDown gis8 ) | % 307
    \stemDown fis4 ~ _\! \stemDown fis8 r8 r8 \stemDown dis'8 (
    \stemDown cis8 \stemDown b8 ) | % 308
    \stemDown fis8 ( _\< \stemDown dis8 \stemDown b8 \stemDown dis8 )
    \stemDown gis4. ( _\! _\> \stemDown fis8 ) | % 309
    \stemDown fis2 _\! _\< \stemDown fis'4 -- _\! _\mf \stemDown e8. (
    \stemDown dis16 ) | \barNumberCheck #310
    \stemDown dis4 ( -> _\markup{ \italic {poco cresc.} } \stemDown cis4
    ) \stemDown e4 -- \stemDown dis8. ( \stemDown cis16 ) \pageBreak | % 311
    \stemDown cis4 ( -> \stemDown b4 ) r8 \stemDown dis8 ( _\mf _\>
    \stemDown cis8 \stemDown b8 ) | % 312
    \stemDown fis8 ( _\! _\p _\< \stemDown dis8 \stemDown b8 \stemDown
    dis8 ) \stemDown gis4.. ( _\! _\> \stemDown fis16 ) | % 313
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis16 -. _\! _\p _\< \stemDown fis16 ( \stemDown g16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown gis16 \stemDown a16 \stemDown ais16 ) }
    \stemDown b32 ( \stemDown bis32 \stemDown cis32 \stemDown d32
    \stemDown dis32 \stemDown e32 \stemDown eis32 \stemDown fis32 )
    \stemDown fis4 -- _\! _\fff \stemDown e8. ( \stemDown dis16 ) | % 314
    \stemDown dis4 ( -> \stemDown cis4 ) \stemDown e4 -- \stemDown dis8.
    ( \stemDown cis16 ) | % 315
    \stemDown cis4 ( -> \stemDown b4 ) r8 \stemDown dis8 ( _\> \stemDown
    cis8 \stemDown b8 ) | % 316
    \stemDown fis8 ( _\! _\mf _\< \stemDown dis8 \stemDown b8 \stemDown
    dis8 ) \stemDown gis4.. ( _\! _\ff _\> \stemDown fis16 ) \pageBreak
    | % 317
    \stemDown fis2 _\! _\mf r2 | % 318
    R1*5 | % 323
    r2 \stemUp eis,4 ( _\mf ^ "I." \stemUp e8. \stemUp eis16 ) | % 324
    \stemUp fis4 ~ \stemUp fis8 r8 r2 | % 325
    R1 \break | % 326
    r4 \stemUp dis4 ^ "I." _\pppp _\< \stemUp cisis2 _\! _\pp _\> | % 327
    \stemUp dis2 ~ _\! _\pppp \stemUp dis8 r8 r4 | % 328
    \stemUp dis8 ~ _\pppp _\< \stemUp dis16 r16 r4 \stemUp cis2 _\! _\pp
    _\> | % 329
    \stemUp dis2 _\! _\pppp _\< \stemUp a'2 _\! _\pp ^ "I." ^ "II." |
    \barNumberCheck #330
    \stemUp gis2 \stemUp g2 | % 331
    \stemUp fis2 _\< \stemUp gis2 ( _\! _\p _\> | % 332
    \stemUp fis8 ) _\! _\pppp r8 r4 \stemUp e2 ( _\pp _\> | % 333
    \stemUp dis2 ) _\! _\pppp _\< \stemUp e4.. -> _\! _\pp _\> \stemUp
    dis16 \pageBreak | % 334
    \stemUp dis2 _\! _\pppp _\< \stemUp e4.. -> _\! _\pp _\> \stemUp dis16
    \bar "||"
    \stemUp dis4 ~ _\! _\pppp \stemUp dis8 r8 r2 | % 336
    R1*4 | \barNumberCheck #340
    \stemDown gis'2 ^ "I." ^\markup{ \italic {cantabile} } _\p \stemDown
    b4. _\< \stemDown cis8 | % 341
    \stemDown e8 ( _\! _\mf _\> \stemDown dis8 ~ \stemDown dis2 ~
    \stemDown dis8 ) r8 _\! | % 342
    \stemDown gis,2 _\p \stemDown b4. _\< \stemDown cis8 \pageBreak | % 343
    dis1 _\! _\mf _\> | % 344
    \stemDown b2. ~ _\! _\p \stemDown b8 \stemDown fis8 | % 345
    dis1 _\> | % 346
    R1*9 \bar "|."
    _\! }

PartPTwoVoiceFive =  \relative b'' {
    \clef "treble" \time 4/4 \key d \major | % 1
    R1*11 \break | % 12
    R1*7 \bar "||"
    R1*5 \pageBreak | % 24
    R1*6 | \barNumberCheck #30
    \time 2/4  R2 \break | % 31
    \time 4/4  R1*6 \break | % 37
    R1*7 \pageBreak | % 44
    R1*6 \break | \barNumberCheck #50
    R1*4 \pageBreak | % 54
    R1*5 \break | % 59
    R1*5 \pageBreak | % 64
    R1*5 \pageBreak | % 69
    R1*5 \pageBreak | % 74
    R1*4 \break | % 78
    R1*5 \pageBreak | % 83
    R1*6 \bar "||"
    R1*5 \break | % 94
    R1*7 \bar "||"
    R1*2 \pageBreak | % 103
    R1*5 \break | % 108
    R1*4 \pageBreak | % 112
    R1*4 \break | % 116
    R1*4 \pageBreak | \barNumberCheck #120
    \stemDown b4 ( ~ -> ^ "II.III." ^\markup{ \bold\small {a. 2} }
    \stemDown b16 \stemDown g16 \stemDown e16 \stemDown b16 \stemUp g8 )
    r8 r4 | % 121
    r4 \stemDown e''2 _\f \stemDown d4 -- | % 122
    \stemDown d4 ~ -> \stemDown d8. \stemDown cis16 \stemDown cis4 ~
    \stemDown cis8 r8 | % 123
    r4 \stemDown cis2 _\ff \stemDown b4 -- | % 124
    \stemDown b4 ~ -> \stemDown b8. \stemDown a16 \stemDown a2 ~ \break
    | % 125
    \stemDown a8 r8 \stemDown b2 \stemDown a4 ~ | % 126
    \stemDown a8 r8 \stemDown b2 ( \stemDown a4 ) | % 127
    r4 \stemDown g4 ( _\ff \stemDown fis4 \stemDown e4 ) | % 128
    \stemDown d4 ( \stemDown cis2 ) \stemDown b4 ( | % 129
    \stemDown bes2 _\sff _\> \stemUp a4 ~ \stemUp a8 ) r8 ^\fermata _\!
    \bar "||"
    r8*2/3 \stemUp <fis a>8 ^\markup{ \italic {pesante, non staccato} }
    _\p \stemUp <fis a>8 \stemUp <fis a>8 \stemUp <fis a>8 \stemUp <fis
        a>8 \stemUp <fis a>4. ~ ~ \stemUp <fis a>8 r8*2/3 r8*2/3 | % 131
    r8*2/3 \stemUp fis8 _\markup{ \italic {sempre} } _ "" \stemUp d'8
    \stemUp fis,8 \stemUp d'8 \stemUp fis,8 \stemUp d'8 \stemUp fis,8
    \stemUp d'8 \stemUp fis,8 \stemUp d'8 r8*2/3 \stemUp gis,8 \stemUp b8
    \stemUp gis8 \stemUp b8 \stemDown gis8 \stemDown b8 \stemDown gis8
    \stemDown b8 \stemDown gis8 \stemDown d'8 \pageBreak | % 132
    r8*2/3 \stemDown d8 \stemDown fis8 \stemDown d8 \stemDown fis8
    \stemDown d8 \stemDown fis8 \stemDown d8 \stemDown fis8 \stemDown d8
    \stemDown fis8 \stemDown d8 \stemDown fis8 r8*2/3 r8*2/3 r4*2/3 r8*2/3
    | % 133
    r8*2/3 \stemDown a,8 \stemDown d8 \stemDown a8 \stemDown d8
    \stemDown a8 \stemDown d8 \stemDown a8 \stemDown d8 \stemDown a8
    \stemDown d8 r8*2/3 \stemDown cis8 \stemDown e8 \stemDown cis8
    \stemDown e8 \stemDown cis8 \stemDown e8 \stemDown cis8 \stemDown e8
    \stemDown cis8 \stemDown e8 | % 134
    r8*2/3 \stemDown d8 _\p _\< \stemDown fis8 \stemDown d8 \stemDown
    fis8 \stemDown d8 \stemDown fis8 \stemDown d8 \stemDown fis8 r8*2/3
    _\! \stemDown a2. _\mf \stemDown c2. | % 135
    \stemDown g8 \stemDown b8 \stemDown g8 \stemDown b8 \stemDown g8
    \stemDown b8 \stemDown g8 \stemDown b8 \stemDown g8 \stemDown b8
    \stemDown g8 \stemDown b8 \stemDown g2. \stemDown bes2. | % 136
    \stemDown fis8 _\< \stemDown a8 \stemDown fis8 \stemDown a8
    \stemDown fis8 \stemDown a8 \stemDown fis8 \stemDown a8 \stemDown
    fis8 \stemDown a8 \stemDown fis8 \stemDown a8 \stemDown b,2. _\!
    _\sf _\> \stemDown d2. | % 137
    \stemDown a8 _\! _\p _\< \stemDown d8 \stemDown a8 \stemDown d8
    \stemDown a8 \stemDown d8 \stemDown a8 \stemDown d8 \stemDown a8
    \stemDown d8 \stemDown a8 \stemDown d8 \stemDown cis2. _\! _\mf _\>
    \stemDown g'2. \pageBreak | % 138
    r8*2/3 _\! \stemDown d8 _\p _\< \stemDown fis8 \stemDown d8
    \stemDown fis8 \stemDown d8 \stemDown fis8 \stemDown d8 \stemDown
    fis8 r8*2/3 _\! \stemDown a2. _\mf \stemDown c2. | % 139
    \stemDown g8 \stemDown b8 \stemDown g8 \stemDown b8 \stemDown g8
    \stemDown b8 \stemDown g8 \stemDown b8 \stemDown g8 \stemDown b8
    \stemDown g8 \stemDown b8 \stemDown g2. \stemDown bes2. |
    \barNumberCheck #140
    \stemDown fis8 _\< \stemDown a8 \stemDown fis8 \stemDown a8
    \stemDown fis8 \stemDown a8 \stemDown fis8 \stemDown a8 \stemDown
    fis8 \stemDown a8 \stemDown fis8 \stemDown a8 \stemDown b,2. _\!
    _\sf _\> \stemDown d2. | % 141
    \stemDown a8 _\! _\p _\< \stemDown d8 \stemDown a8 \stemDown d8
    \stemDown a8 \stemDown d8 \stemDown a8 \stemDown d8 \stemDown a8
    \stemDown d8 \stemDown a8 \stemDown d8 \stemDown cis2. _\! _\mf _\>
    \stemDown g'2. \bar "||"
    r8*2/3 _\! \stemDown d8 _\mf _\> \stemDown fis8 \stemDown d8
    \stemDown fis8 \stemDown d8 \stemDown fis8 \stemDown d8 \stemDown
    fis8 \stemDown d8 \stemDown fis8 r2.*2/3 _\! | % 143
    R1*2 \break | % 145
    R1*11 \pageBreak | % 156
    R1*5 \bar "||"
    \key c \major R1*4 \pageBreak | % 165
    \stemDown e'8 ^ "III." r8 r4 r2 | % 166
    R1*2 | % 168
    r2 r4 \stemDown e,16 ( _\ff \stemDown g16 ) \stemDown g16 (
    \stemDown e'16 ) | % 169
    \stemDown d8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown d16 _\sff \stemDown d16 \stemDown d16 }
    \stemDown d8 ~ \stemDown d4 ~ | \barNumberCheck #170
    \stemDown d8 \stemDown d8 -> \stemDown d8 -> \stemDown d8 ->
    \stemDown d8 -> \stemDown d8 -> r4 | % 171
    R1 \pageBreak | % 172
    r2 r4 r8 \stemDown d8 ~ _\f | % 173
    \stemDown d4. \stemDown d8 ~ \stemDown d4. \stemDown d8 ~ | % 174
    \stemDown d8 r8 r4 r2 | % 175
    R1 | % 176
    r2 r4 r8 \stemDown a8 ~ _\f | % 177
    \stemDown a4. \stemDown a8 ~ \stemDown a4. \stemDown a8 ~ \pageBreak
    | % 178
    \stemDown a8 r8 r4 r2 | % 179
    r4 \stemDown c8 -. _\mf \stemDown a8 ( \stemDown g8 ) \stemDown a8 ~
    \stemDown a8 r8 | \barNumberCheck #180
    r2 r8 \stemDown fis,8 ( _\mf ^ "II.III." ^\markup{ \bold\small {a.
            2} } \stemDown e8 ) \stemDown e''8 ~ _\f | % 181
    \stemDown e4. \stemDown e8 ~ \stemDown e4. \stemDown e8 ~ | % 182
    \stemDown e8 r8 r4 r2 \break | % 183
    R1*5 \pageBreak | % 188
    R1*4 \break | % 192
    R1*4 \pageBreak | % 196
    R1*5 \break | % 201
    R1*6 \pageBreak | % 207
    R1*6 \pageBreak | % 213
    R1*4 \break | % 217
    R1*4 \pageBreak | % 221
    R1*5 \break | % 226
    R1*5 \break | % 231
    R1*6 \pageBreak | % 237
    R1*5 \pageBreak | % 242
    R1*4 \pageBreak | % 246
    R1*6 \break | % 252
    R1*5 \pageBreak | % 257
    R1*6 \pageBreak | % 263
    R1*5 \pageBreak | % 268
    R1*5 \pageBreak | % 273
    R1*12 \pageBreak | % 285
    R1*17 \break | % 302
    R1*3 \bar "||"
    \pageBreak | % 305
    \key b \major r2 r8 \stemDown dis,8 ( _\p ^ "III." ^\markup{ \italic
        {con dolcezza} } \stemDown cis8 \stemDown b8 ) | % 306
    \stemUp gis8 ( _\< \stemUp fis8 \stemUp dis8 \stemUp fis8 )
    \stemDown b4. ( _\! _\> \stemUp gis8 ) | % 307
    \stemUp fis4 ~ _\! \stemUp fis8 r8 r8 \stemDown dis'8 ( \stemDown
    cis8 \stemDown b8 ) | % 308
    \stemUp fis8 ( _\< \stemUp dis8 \stemUp b'8 \stemUp dis,8 ) \stemUp
    gis4. ( _\! _\> \stemUp fis8 ) | % 309
    \stemUp fis2 _\! _\< \stemDown fis'4 -- _\! _\mf \stemDown e8. (
    \stemDown dis16 ) | \barNumberCheck #310
    \stemDown dis4 ( -> _\markup{ \italic {poco cresc.} } \stemDown cis4
    ) \stemDown e4 -- \stemDown dis8. ( \stemDown cis16 ) \pageBreak | % 311
    \stemDown cis4 ( -> \stemDown b4 ) r8 \stemDown dis'8 ( _\mf _\>
    \stemDown cis8 \stemDown b8 ) | % 312
    \stemDown fis8 ( _\! _\p _\< \stemDown dis8 \stemDown b8 \stemDown
    dis8 ) \stemDown gis4.. ( _\! _\> \stemDown fis16 ) | % 313
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis16 -. _\! _\p _\< \stemDown fis16 ( \stemDown g16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown gis16 \stemDown a16 \stemDown ais16 ) }
    \stemDown b32 ( \stemDown bis32 \stemDown cis32 \stemDown d32
    \stemDown dis32 \stemDown e32 \stemDown eis32 \stemDown fis32 )
    \stemDown fis4 -- _\! _\fff \stemDown e8. ( \stemDown dis16 ) | % 314
    \stemDown dis4 ( -> \stemDown cis4 ) \stemDown e4 -- \stemDown dis8.
    ( \stemDown cis16 ) | % 315
    \stemDown cis4 ( -> \stemDown b4 ) r8 \stemDown dis8 ( _\> \stemDown
    cis8 \stemDown b8 ) | % 316
    \stemDown fis8 ( _\! _\mf _\< \stemDown dis8 \stemDown b8 \stemDown
    dis8 ) \stemDown gis4.. ( _\! _\ff _\> \stemDown fis16 ) \pageBreak
    | % 317
    \stemDown fis2 _\! _\mf r2 | % 318
    R1*3 | % 321
    r2 \stemUp fis,2 ^ "II." ^ "III." _\mf | % 322
    \stemUp e2 \stemUp e2 | % 323
    \stemUp dis2 r2 | % 324
    R1*2 \break | % 326
    R1*8 \pageBreak | % 334
    R1 \bar "||"
    R1*5 | \barNumberCheck #340
    \stemDown e'2 ^ "II.III." ^\markup{ \italic {cantabile} } _\p
    \stemDown gis2 \stemDown e4. _\< \stemDown gis4. \stemDown e8
    \stemDown gis8 | % 341
    \stemDown fis2. ~ _\! _\mf _\> \stemDown b2. ~ \stemDown fis8
    \stemDown b8 r8 _\! | % 342
    \stemDown e,2 _\p \stemDown gis2 \stemDown e4. _\< \stemDown gis4.
    \stemDown e8 \stemDown gis8 \pageBreak | % 343
    fis1 _\! _\mf _\> b1 | % 344
    \stemUp dis,2. ~ _\! _\p \stemUp dis8 \stemUp dis8 | % 345
    b1 _\> | % 346
    R1*9 \bar "|."
    _\! }

PartPTwoVoiceTwo =  \relative g' {
    \clef "treble" \time 4/4 \key d \major s1*11 \break s1*7 \bar "||"
    s1*5 \pageBreak s4*7 r8 \stemDown g8 | % 26
    r8 \stemDown fis8 r8 \stemDown e8 r8 \stemDown e8 r8 \stemDown d8 | % 27
    r8 \stemDown d8 r8 \stemDown g8 ~ \stemDown g8 r8 s4*9 |
    \barNumberCheck #30
    \time 2/4  s2 \break | % 31
    \time 4/4  s1*6 \break s1*7 \pageBreak s1*5 | % 49
    r8 s8*7 \break s8*13 \stemDown cis8 ( \stemDown e8 \stemDown gis8 )
    s8*13 \stemDown cis,8 ( \stemDown e8 \stemDown gis8 ) \pageBreak
    s1*5 \break s1*5 \pageBreak s1*5 \pageBreak s16*25 \stemDown a16 -.
    \stemDown a16 -. \stemDown a16 -. \stemDown a16 ( \stemDown c16 )
    \stemDown b16 -. \stemDown a16 -. | % 71
    \stemDown f16 \stemDown e16 \stemDown d'16 \stemDown c16 \stemDown b16
    \stemDown a16 \stemDown f16 \stemDown e16 s16 \stemDown a16 -.
    \stemDown a16 -. \stemDown a16 -. \stemDown a16 ( \stemDown c16 )
    \stemDown b16 -. \stemDown a16 -. | % 72
    \stemDown f16 \stemDown e16 \stemDown d'16 \stemDown c16 \stemDown b16
    \stemDown a16 \stemDown f16 \stemDown e16 s16 \stemDown a16 -.
    \stemDown a16 -. \stemDown a16 -. \stemDown a16 ( \stemDown c16 )
    \stemDown b16 -. \stemDown a16 -. s16 \stemDown a16 -. \stemDown a16
    -. \stemDown a16 -. \stemDown a16 ( \stemDown c16 \stemDown b16
    \stemDown a16 ) s16 \stemDown a16 -. \stemDown a16 -. \stemDown a16
    -. \stemDown a16 ( \stemDown c16 \stemDown b16 \stemDown a16 )
    \pageBreak s1*4 \break s1*5 \pageBreak s1*6 \bar "||"
    s1*5 \break s1*7 \bar "||"
    s1*2 \pageBreak s1*5 \break s1*4 \pageBreak s1*4 \break s1*4
    \pageBreak s1*5 \break s1*5 \bar "||"
    s1*2 \pageBreak s1*6 \pageBreak s2*9 \bar "||"
    s2*5 \break s1*11 \pageBreak s1*5 \bar "||"
    \key c \major s1*4 \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*5
    \break s1*5 \pageBreak s1*4 \break s1*4 \pageBreak s1*5 \break s1*6
    \pageBreak s1*6 \pageBreak s1*4 \break s1*4 \pageBreak s1*5 \break
    s1*5 \break s1*6 \pageBreak s1*5 \pageBreak s1*4 \pageBreak s1*6
    \break s1*5 \pageBreak s1*6 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*12 \pageBreak s1*17 \break s1*3 \bar "||"
    \pageBreak | % 305
    \key b \major s1*6 \pageBreak s1*6 \pageBreak s1*9 \break s1*3 | % 329
    r2 \stemDown fis,2 | \barNumberCheck #330
    \stemDown e2 \stemDown e2 | % 331
    \stemDown dis2 \stemDown dis2 | % 332
    \stemDown dis8 ~ \stemDown dis16 r16 s4 \stemDown cis2 ( | % 333
    \stemDown dis8 ) r8 r4 \stemDown cis4.. -> \stemDown dis16
    \pageBreak | % 334
    \stemDown dis2 \stemDown cis4.. -> \stemDown dis16 \bar "||"
    \stemDown dis4 ~ \stemDown dis8 s8*61 \pageBreak s1*12 \bar "|."
    }

PartPTwoVoiceSix =  \relative dis' {
    \clef "treble" \time 4/4 \key d \major s1*11 \break s1*7 \bar "||"
    s1*5 \pageBreak s1*6 | \barNumberCheck #30
    \time 2/4  s2 \break | % 31
    \time 4/4  s1*6 \break s1*7 \pageBreak s1*6 \break s1*4 \pageBreak
    s1*5 \break s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*4
    \break s1*5 \pageBreak s1*6 \bar "||"
    s1*5 \break s1*7 \bar "||"
    s1*2 \pageBreak s1*5 \break s1*4 \pageBreak s1*4 \break s1*4
    \pageBreak s1*5 \break s1*5 \bar "||"
    s1*2 \pageBreak s1*6 \pageBreak s2*9 \bar "||"
    s2*5 \break s1*11 \pageBreak s1*5 \bar "||"
    \key c \major s1*4 \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*5
    \break s1*5 \pageBreak s1*4 \break s1*4 \pageBreak s1*5 \break s1*6
    \pageBreak s1*6 \pageBreak s1*4 \break s1*4 \pageBreak s1*5 \break
    s1*5 \break s1*6 \pageBreak s1*5 \pageBreak s1*4 \pageBreak s1*6
    \break s1*5 \pageBreak s1*6 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*12 \pageBreak s1*17 \break s1*3 \bar "||"
    \pageBreak | % 305
    \key b \major s1*6 \pageBreak s1*6 \pageBreak s2*9 \stemDown dis2 | % 322
    \stemDown e2 \stemDown cis2 | % 323
    \stemDown dis2 s2*5 \break s1*8 \pageBreak s1 \bar "||"
    s1*8 \pageBreak s1 | % 344
    \stemDown fis'2. ~ \stemDown fis8 \stemDown b,8 | % 345
    fis1 s1*9 \bar "|."
    }

PartPThreeVoiceOne =  \relative d'' {
    \clef "treble" \time 4/4 \key d \major | % 1
    R1*11 \break | % 12
    r2 r4 \stemUp d8 ( _\p _\< \stemUp e8 ) | % 13
    \stemUp fis2. ~ _\! _\mf _\> \stemUp fis8 r8 _\! | % 14
    R1*5 \bar "||"
    R1*5 \pageBreak | % 24
    R1*6 | \barNumberCheck #30
    \time 2/4  R2 \break | % 31
    \time 4/4  R1*6 \break | % 37
    R1*7 \pageBreak | % 44
    r2 r8 \stemDown fis8 ( _\pp ^ "I." \stemDown e8 \stemDown d8 | % 45
    \stemUp cis8 ) \stemUp b8 ( \stemUp a8 \stemUp gis8 \stemUp fis8 )
    \stemUp e8 ( \stemUp d8 \stemUp cis8 ) | % 46
    \stemDown cis'16 ( \stemDown d16 \stemDown cis16 \stemDown d16
    \stemDown cis16 \stemDown d16 \stemDown cis16 \stemDown d16
    \stemDown cis8 ) r8 r4 | % 47
    R1*3 \break | \barNumberCheck #50
    R1*2 | % 52
    r4 \stemUp gis4 ~ _\sf ^ "I." _\> \stemUp gis8 r8 _\! r4 | % 53
    R1 \pageBreak | % 54
    r4 \stemUp gis4 ~ ^ "I." _\sf _\> \stemDown gis16 \stemDown gis'16
    -. _\! _\pp _\< \stemDown gis16 -. \stemDown gis16 -. \stemDown gis16
    -. \stemDown gis16 -. \stemDown e16 -. \stemDown e16 -. | % 55
    \stemDown dis8 -- _\! _\> \stemDown b8 -- \stemDown b8 -- r8 _\! r16
    \stemDown dis16 -. _\pp _\< \stemDown dis16 -. \stemDown dis16 -.
    \stemDown dis16 -. \stemDown dis16 -. \stemDown a16 -. \stemDown a16
    -. | % 56
    \stemUp gis8 -- _\! _\> \stemUp gis8 -- \stemUp gis8 -- r8 _\! r16
    \stemUp <e b'>16 _. _\p _\< \stemUp <e b'>16 _. \stemUp <e b'>16 _.
    \stemDown <e b'>16 ( \stemDown <b' gis'>16 ) \stemDown <gis e'>16 ^.
    \stemDown <gis e'>16 ^. | % 57
    \stemDown <fisis dis'>8 -- _\! _\> \stemDown <a fis'>8 -- \stemDown
    <dis fisis>8 -- r8 _\! r16 \stemDown <b fisis'>16 -. _\p _\<
    \stemDown <b fisis'>16 -. \stemDown <b fisis'>16 -. \stemDown <b
        fisis'>16 ( \stemDown <ais fisis'>16 ) \stemDown <gis cis>16 -.
    \stemDown <fisis cis'>16 -. | % 58
    \stemUp <e b'>8 -- _\! _\> \stemUp <cisis b'>8 -- \stemUp <dis b'>8
    -- r8 _\! r2 \break | % 59
    r2 r8 \stemUp gis8 ( _\mp _\< \stemUp b8 \stemUp dis8 ) |
    \barNumberCheck #60
    \stemDown <fisis, fisis'>8 ( -. \stemDown <ais ais'>8 ) -. \stemDown
    <dis dis'>4 ~ ~ _\! _\> \stemDown <dis dis'>8 r8 _\! r4 | % 61
    r2 r8 \stemUp gis,8 ( ^\mp _\< \stemUp b8 \stemUp dis8 ) | % 62
    \stemUp fisis8 ( -. _ "" \stemUp ais8 ) -. \stemUp dis4 ~ _\! _\>
    \stemUp dis16 \stemUp dis,16 -. _\! ^\p _\< \stemUp dis16 -. \stemUp
    dis16 -. \stemUp dis16 -. \stemUp dis16 -. \stemUp b16 -. \stemUp b16
    -. | % 63
    \stemUp ais8 -- _\! _\> \stemUp fis8 -- \stemUp fis8 -- r8 _\! r16
    \stemUp ais16 -. _\p _\< \stemUp ais16 -. \stemUp ais16 -. \stemUp
    ais16 -. \stemUp ais16 -. \stemUp e16 -. \stemUp e16 -. \pageBreak | % 64
    \stemUp dis8 -- _\! _\> \stemUp cisis8 -- \stemUp dis8 -- r8 _\! r16
    \stemUp fis'16 -. _\mp _\< \stemUp fis16 -. \stemUp fis16 -. \stemUp
    fis16 -. \stemUp fis16 -. \stemUp dis16 -. \stemUp dis16 -. | % 65
    \stemUp cisis8 -- _\! _\> \stemUp ais8 -- \stemUp ais8 -- r8 _\! r16
    \stemUp cisis16 -. _\mp _\< \stemUp cisis16 -. \stemUp cisis16 -.
    \stemUp cisis16 -. \stemUp cisis16 -. r8 | % 66
    r2 _\! _\> r16 \stemUp <dis, dis'>16 -. _\f ^\markup{ \italic {solo}
        } \stemUp <dis dis'>16 -. \stemUp <dis dis'>16 -. \stemUp <dis
        dis'>16 ( \stemUp <fis fis'>16 ) \stemUp <eis eis'>16 -. \stemUp
    <dis dis'>16 -. | % 67
    \stemUp <cisis cisis'>2 ( \stemUp <dis dis'>8 ) r8 r4 | % 68
    r2 r16 \stemDown <fis fis'>16 -. _\ff \stemDown <fis fis'>16 -.
    \stemDown <fis fis'>16 -. \stemDown <fis fis'>16 ( \stemDown <a a'>16
    ) \stemDown <gis gis'>16 -. \stemDown <fis fis'>16 -. \pageBreak | % 69
    \stemUp <eis eis'>2 ( \stemDown <fis fis'>8 ) r8 r4 |
    \barNumberCheck #70
    R1 | % 71
    \stemUp a'4 -> \stemUp c,4 -> r2 | % 72
    \stemUp a'4 -> \stemUp c,4 -> r2 | % 73
    \stemUp <f, f'>8 -> \stemUp <dis dis'>8 -> \stemUp <e e'>8 -> r8 r2
    \pageBreak | % 74
    \stemUp <f f'>8 -> \stemUp <dis dis'>8 -> \stemUp <e e'>8 -> r8
    \stemUp <dis dis'>4 ( -> \stemUp <e e'>8 ) r8 | % 75
    \stemUp <dis dis'>4 ( -> \stemUp <e e'>8 ) r8 \stemUp <bis bis'>4 (
    -> \stemUp <cis cis'>8 ) r8 | % 76
    \stemUp <bis bis'>4 ( -> \stemUp <cis cis'>8 ) r8 r2 _\f | % 77
    R1 \break | % 78
    R1*5 \pageBreak | % 83
    R1*6 \bar "||"
    R1*5 \break | % 94
    R1*7 \bar "||"
    R1*2 \pageBreak | % 103
    R1*2 | % 105
    r4 \stemDown fis'2 _ "" _\markup{ \italic {espress.} } ^ "I."
    \stemDown e4 -- | % 106
    \stemDown e4 ~ -> \stemDown e8. \stemDown d16 \stemDown d2 _\< | % 107
    r4 _\! \stemDown cis2 _\f _\> \stemDown b4 -- \break | % 108
    \stemDown b4 ~ -> _\! _\mf \stemUp b8. _\> \stemUp a16 \stemUp a4 ~
    \stemUp a8 r8 _\! | % 109
    R1*3 \pageBreak | % 112
    R1 | % 113
    r4 \stemDown <cis cis'>2 _ "" _\markup{ \italic {espress.} }
    \stemDown <b b'>4 -- | % 114
    \stemDown <b b'>4 ~ -> ~ \stemDown <b b'>8. \stemDown <a a'>16
    \stemDown <a a'>2 _\< | % 115
    r4 _\! \stemDown <gis gis'>2 _\f _\> \stemDown <fis fis'>4 -- \break
    | % 116
    \stemDown <fis fis'>4 ~ -> ~ _\! _\mf _\> \stemDown <fis fis'>8.
    \stemDown <e e'>16 \stemUp <e e'>4 ~ ~ \stemUp <e e'>8 r8 _\! | % 117
    R1*3 \pageBreak | \barNumberCheck #120
    R1 | % 121
    r4 \stemDown e'2 _\f ^\markup{ \bold\small {a. 2} } \stemDown d4 --
    | % 122
    \stemDown d4 ~ -> \stemDown d8. \stemDown cis16 \stemDown cis4 ~
    \stemDown cis8 r8 | % 123
    r4 \stemDown cis2 _\ff \stemDown b4 -- | % 124
    \stemDown b4 ~ -> \stemUp b8. \stemUp a16 \stemUp a2 ~ \break | % 125
    \stemUp a8 r8 \stemDown b2 \stemUp a4 ~ | % 126
    \stemUp a8 r8 \stemDown b2 ( \stemUp a4 ) | % 127
    r4 \stemDown g'4 ( _\ff ^ "I." \stemDown fis4 \stemDown e4 ) | % 128
    \stemDown d4 ( \stemDown cis2 ) \stemDown b4 ( | % 129
    \stemDown bes2 _\sff _\> \stemUp a4 ~ \stemUp a8 ) r8 ^\fermata _\!
    \bar "||"
    \time 12/8  r1 s2 | % 131
    r2.*2/3 r8*2/3 \stemUp <gis b>8 ^\markup{ \italic {pesante, non
            staccato} } _\p \stemUp <gis b>8 \stemDown <gis b>8
    \stemDown <gis b>8 \stemDown <gis d'>8 s1*7/24 \pageBreak | % 132
    r8*2/3 \stemDown <d' fis>8 _\markup{ \italic {sempre} } _ ""
    \stemDown <d fis>8 \stemDown <d fis>8 \stemDown <d fis>8 \stemDown
    <d fis>8 \stemDown <d fis>8 r8*2/3 r8*2/3 r4*2/3 r8*2/3 s4 | % 133
    r8*2/3 \stemUp <fis, d'>8 \stemUp <fis d'>8 \stemUp <fis d'>8
    \stemUp <fis d'>8 \stemUp <fis d'>8 r8*2/3 \stemDown <g e'>8
    \stemDown <g e'>8 \stemDown <g e'>8 \stemDown <g e'>8 \stemDown <g
        e'>8 s1*1/12 | % 134
    r8*2/3 \stemDown <fis fis'>8 _\p _\< \stemDown <fis fis'>8 \stemDown
    <fis fis'>8 \stemDown <fis fis'>8 r8*2/3 _\! \stemDown <a' c>2. _\mf
    s1*1/12 | % 135
    \stemDown <g b>8 \stemDown <g b>8 \stemDown <g b>8 \stemDown <g b>8
    \stemDown <g b>8 \stemDown <g b>8 \stemDown <g bes>2. | % 136
    \stemDown <fis a>8 _\< \stemDown <fis a>8 \stemDown <fis a>8
    \stemDown <fis a>8 \stemDown <fis a>8 \stemDown <fis a>8 \stemDown
    <b, d>2. _\! _\sf _\> | % 137
    \stemDown <a d>8 _\! _\p _\< \stemDown <a d>8 \stemDown <a d>8
    \stemDown <a d>8 \stemDown <a d>8 \stemDown <a d>8 \stemDown <cis
        g'>2. _\! _\mf _\> \pageBreak | % 138
    r8*2/3 _\! \stemDown <fis, fis'>8 _\p _\< \stemDown <fis fis'>8
    \stemDown <fis fis'>8 \stemDown <fis fis'>8 r8*2/3 _\! \stemDown <a'
        c>2. _\mf s1*1/12 | % 139
    \stemDown <g b>8 \stemDown <g b>8 \stemDown <g b>8 \stemDown <g b>8
    \stemDown <g b>8 \stemDown <g b>8 \stemDown <g bes>2. |
    \barNumberCheck #140
    \stemDown <fis a>8 _\< \stemDown <fis a>8 \stemDown <fis a>8
    \stemDown <fis a>8 \stemDown <fis a>8 \stemDown <fis a>8 \stemDown
    <b, d>2. _\! _\sf _\> | % 141
    \stemDown <a d>8 _\! _\p _\< \stemDown <a d>8 \stemDown <a d>8
    \stemDown <a d>8 \stemDown <a d>8 \stemDown <a d>8 \stemDown <cis
        g'>2. _\! _\mf _\> \bar "||"
    r8*2/3 _\! \stemDown <d fis>8 _\mf _\> \stemDown <d fis>8 \stemDown
    <d fis>8 \stemDown <d fis>8 \stemDown <d fis>8 \stemUp <d, d'>4. (
    _\! _\mp \stemUp <dis dis'>4. ) s1*1/24 | % 143
    \numericTimeSignature\time 4/4  \stemUp <dis dis'>4 ( \stemUp <e e'>4
    ) \stemUp <b b'>4 ( \stemUp <cis cis'>4 ) | % 144
    \stemUp <cis cis'>4 ( _\> \stemUp <d d'>4 ) \stemUp <d d'>4 ( _\!
    _\p \stemUp <dis dis'>4 ) \break | % 145
    \stemUp <e e'>4 ( \stemDown <gis gis'>4 ) \stemUp <b, b'>4 ( \stemUp
    <cis cis'>4 ) | % 146
    \stemUp d'2 r2 | % 147
    R1*9 \pageBreak | % 156
    R1*5 \bar "||"
    \key c \major \stemDown <g a>8 _\ff r8 r4 \stemUp es,16 -> _\sff
    ^\markup{ \bold\small {a. 2} } \stemUp es16 \stemUp es8 ~ \stemUp es4
    ~ | % 162
    \stemUp es8 \stemUp e8 -> \stemUp f8 -> \stemUp e8 -> \stemUp es8 ->
    r8 r4 | % 163
    \stemUp d8 _\sf r8 \stemUp c8 _\sf r8 r4 r8 \stemUp c8 _\sf | % 164
    \stemUp d8 _\sf r8 \stemUp es8 _\sf r8 r4 \stemDown <g es'>8 ( _\ff
    \stemDown <es' g>8 ) \pageBreak | % 165
    \stemDown <e g>8 r8 r4 \stemUp e,16 _\sff ^\markup{ \bold\small {a.
            2} } \stemUp e16 \stemUp e8 ~ \stemUp e4 ~ | % 166
    \stemUp e8 \stemUp fis8 -> \stemUp g8 -> \stemUp fis8 -> \stemUp e8
    -> r8 r4 | % 167
    \stemUp es8 _\sf r8 \stemUp d8 _\sf r8 r4 r8 \stemUp d8 _\sf | % 168
    \stemUp dis8 _\sf r8 \stemUp e8 _\sf r8 r4 \stemDown <g e'>8 ( _\ff
    \stemDown <e' g>8 ) | % 169
    \stemDown <f d'>8 r8 r4 \stemDown <f d'>16 _\sff \stemDown <f d'>16
    \stemDown <f d'>8 ~ ~ \stemDown <f d'>4 ~ ~ | \barNumberCheck #170
    \stemDown <f d'>8 \stemDown <g, g'>8 -> \stemDown <f f'>8 ->
    \stemDown <g g'>8 -> \stemDown <gis gis'>8 -> \stemDown <a a'>8 -> r4
    | % 171
    R1 \pageBreak | % 172
    r2 r4 r8 \stemDown <d d'>8 ~ ~ _\f | % 173
    \stemDown <d d'>4. \stemDown <d d'>8 ~ ~ \stemDown <d d'>4.
    \stemDown <d d'>8 ~ ~ | % 174
    \stemDown <d d'>8 r8 r4 r2 | % 175
    r4 r8 \stemDown <d a'>8 ( _\ff \stemDown <f, d'>8 ) r8 r4 | % 176
    r4 r8 \stemDown <d' a'>8 ( _\ff \stemDown <f, d'>8 ) r8 r4 | % 177
    R1 \pageBreak | % 178
    \stemUp b'8 _\sf r8 r4 r2 | % 179
    r4 \stemUp c8 -. ^\mf \stemUp a8 ( \stemUp g8 ) \stemUp a8 ~ _\mf
    \stemUp a8 r8 | \barNumberCheck #180
    r4 \stemUp e8 -. _\mf \stemUp fis8 ( \stemUp b,8 ) \stemUp e8 -. r8
    \stemUp e'8 ~ _\f | % 181
    \stemUp e4. \stemUp e8 ~ \stemUp e4. \stemUp e8 ~ | % 182
    \stemUp e8 r8 r4 r2 \break | % 183
    r4 r8 \stemDown <e, b'>8 ( _\ff \stemDown <g, e'>8 ) r8 r4 | % 184
    r4 r8 \stemDown <e' b'>8 ( _\ff \stemDown <g, e'>8 ) r8 r4 | % 185
    r2 r4 \stemUp fis8 ( _\ff ^\markup{ \bold\small {a. 2} } \stemUp e16
    \stemUp fis16 ) | % 186
    \stemUp g8 ( \stemUp fis16 \stemUp g16 ) \stemUp a8 ( \stemUp g16
    \stemUp a16 ) \stemUp b8 ( \stemUp a16 \stemUp b16 \stemDown cis8 )
    r8 | % 187
    r2 r4 \stemUp d,8 ( _\fff \stemUp cis16 \stemUp d16 ) \pageBreak | % 188
    \stemUp e8 ( \stemUp d16 \stemUp e16 ) \stemUp fis8 ( \stemUp e16
    \stemUp fis16 ) \stemUp g8 ( \stemUp fis16 \stemUp g16 ) \stemUp g8
    ( \stemUp fis16 \stemUp g16 ) | % 189
    \stemUp g8 ( \stemUp fis16 \stemUp g16 ) \stemUp g8 ( \stemUp fis16
    \stemUp g16 ) \stemUp g8 ( \stemUp fis16 \stemUp g16 ) r4 |
    \barNumberCheck #190
    \stemDown bes'2 -> \stemDown a4 -> \stemDown g4 -> | % 191
    \stemDown f2 -> \stemDown es2 -> \break | % 192
    \stemDown es2 -> \stemDown d4 -> \stemDown c4 -> | % 193
    \stemDown ces2 -> \stemDown bes2 -> | % 194
    \stemDown bes'2 -> \stemDown a4 -> \stemDown g4 -> | % 195
    \stemDown f4 -> \stemDown e4 -> \stemDown d4 -> \stemDown c4 ->
    \pageBreak | % 196
    \stemUp bes4 -> \stemUp a4 -> \stemUp g4 -> \stemUp f4 -> | % 197
    \stemUp e4 -> \stemUp d4 -> r2 | % 198
    R1*3 \break | % 201
    R1*4 | % 205
    r2 \once \omit TupletBracket
    \times 4/7  {
        \stemDown <cis' e>16*161/160 ( _\p _\< \stemDown <d f>16*161/160
        \stemDown <e g>16*161/160 \stemDown <f a>16*161/160 \stemDown <g
            bes>16*161/160 \stemDown <a cis>16*161/160 \stemDown <bes d>16*161/160
        }
    \stemDown <cis e>8 ) _\! r8 | % 206
    R1 \pageBreak | % 207
    R1*2 | % 209
    r2 r4 r8. \stemUp dis,16 _\mf | \barNumberCheck #210
    \stemUp dis8 _\markup{ \italic {poco cresc.} } r8 \stemUp cis8 r8
    \stemUp b8 r8 \stemUp ais8 r16 \stemUp fis'16 | % 211
    \stemUp fis8 r8 \stemUp e8 r8 \stemUp d8 r8 \stemUp cis8 r8 | % 212
    \stemUp e8 r8 \stemUp dis8 r8 \stemUp fis8 _\f _\< r8 \stemUp eis8 r8
    \pageBreak | % 213
    \stemUp fis8 r8 \stemUp eis8 r8 \stemUp fis8 r8 \stemUp eis8 r8 | % 214
    \stemDown eis4 -- _\! _\ff ^\markup{ \bold\small {a. 2} } \stemDown
    fis4 -- \stemDown b,4 -- \stemUp a4 -- | % 215
    \stemDown b4 -- \stemUp fis4 -- \stemUp a4 -- \stemUp gis4 -- | % 216
    \stemDown cis4 -- _\markup{ \italic {dim. un poco} } \stemDown fis4
    -- \stemDown b,4 -- \stemDown e4 -- \break | % 217
    \stemUp gis,4 -- \stemDown cis4 -- \stemUp g4 -- \stemDown cis4 -- | % 218
    \stemDown eis4 _\f ^ "I." \stemDown fis4 r2 | % 219
    R1*2 \pageBreak | % 221
    R1*5 \break | % 226
    R1*5 \break | % 231
    R1*6 \pageBreak | % 237
    R1 | % 238
    r2 \stemUp des,4 ~ -> _\mp ^ "I." \stemUp des8. \stemUp des16 | % 239
    \stemUp ges2. -> _\markup{ \italic {cresc.} } \stemUp es4 |
    \barNumberCheck #240
    \stemDown bes'2 -> \stemUp a2 | % 241
    \stemDown bes2 \stemUp as4.. _ "" _\markup{ \italic {cresc.} }
    \stemUp as16 \pageBreak | % 242
    \stemDown es'8 r8 \stemDown d8 r8 \stemDown es8 r8 r4 | % 243
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis8 _\ff \stemUp fis8 \stemUp fis8 ~ }
    \stemUp fis8 \stemUp fis8 ~ \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis8 \stemUp fis8 \stemUp fis8 ~ }
    \stemUp fis8 \stemUp fis8 | % 244
    \stemUp fis8 r8 \stemUp fis8 r8 \stemUp g16 ( \stemUp fis16 )
    \stemUp fis8 \stemUp b,8 _\fff \stemUp cis8 | % 245
    \stemUp d4 ( -> \stemUp cis8 ) r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp e8 \stemUp b8 }
    \pageBreak | % 246
    \stemUp d4 ( -> \stemUp cis8 ) r8 r4 r8 \stemUp g'8 | % 247
    r8 \stemDown b,8 \stemDown d8 r8 \stemDown cis8 \stemDown e8 r8
    \stemDown d8 \stemDown fis8 r4 | % 248
    R1 | % 249
    r4 \stemDown cis8 _\ff \stemDown fis8 \stemDown d8 \stemDown fis8
    \stemDown e4 -> \stemDown fis4 \stemDown d8 \stemDown fis8 r8 |
    \barNumberCheck #250
    r4 \stemDown cis8 \stemDown fis8 \stemDown d8 \stemDown fis8
    \stemDown e4 -> \stemDown fis4 \stemDown d8 \stemDown fis8 r8 | % 251
    r4 \stemDown e8 \stemDown a8 \stemDown fis8 \stemDown a8 \stemDown g4
    -> \stemDown a4 \stemDown fis8 \stemDown a8 r8 \break | % 252
    r4 \stemDown e8 \stemDown a8 \stemDown fis8 \stemDown a8 \stemDown g4
    -> \stemDown a4 \stemDown fis8 \stemDown a8 r8 | % 253
    r4 \stemDown cis,8 \stemDown fis8 \stemDown d8 \stemDown gis8
    \stemDown dis8 ( -> \stemDown a'8 \stemDown eis8 ) \stemDown gis8 r4
    | % 254
    r4 \stemUp fis16 ( \stemUp gis16 ) \stemUp a16 ( \stemUp fis16 )
    \stemUp a8 ( -> \stemUp gis8 ) r4 | % 255
    r4 r8 \stemDown b,8 _\ff \stemDown eis8 r8 \stemDown cis8 \stemDown
    fis8 r4 | % 256
    r4 r8 \stemDown b,8 \stemDown fis'8 r8 \stemDown b,8 \stemDown e8 r4
    \pageBreak | % 257
    r4 r8 \stemDown a,8 \stemDown d8 r8 \stemDown b8 \stemDown e8 r4 | % 258
    r4 r8 \stemDown a,8 \stemDown e'8 r8 \stemDown a,8 \stemDown d8 r4 | % 259
    r2 r4 \stemUp c,4 ~ _ "" _\markup{ \italic {cresc.} } \stemUp c'4 ~
    | \barNumberCheck #260
    \stemUp c,4 \stemUp c'4 \stemUp c,4 ( \stemUp c'4 \stemUp ces,4 )
    \stemUp ces'4 \stemDown bes4 _\mf \stemDown es4 | % 261
    \stemDown a,4 _\markup{ \italic {cresc.} } \stemDown es'4 \stemDown
    a,4 \stemDown d4 \stemDown a4 \stemDown cis4 \stemUp c,4 ~ \stemUp
    c'4 ~ | % 262
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c,8 \stemUp c'8 \stemUp c,8 \stemUp c'8 \stemUp c,8 }
    \stemUp c'8*2/3 \stemUp c,4 ~ \stemUp c'4 ~ \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp c,8 \stemUp c'8 \stemUp c,8 \stemUp c'8 \stemUp c,8 }
    \stemUp c'8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 _\ff \stemDown c8 \stemDown a8 \stemDown c8
        \stemDown a8 }
    \stemDown c8*2/3 \pageBreak | % 263
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown c8 \stemDown a16 \stemDown c16 \stemDown
        a16 \stemDown c16 \stemDown a8 }
    \stemDown c8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown c8 \stemDown a8 \stemDown c8 \stemDown a8
        }
    \stemDown c8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown c8 \stemDown a8 \stemDown c8 \stemDown a8
        }
    \stemDown c8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown c8 \stemDown a8 \stemDown c8 \stemDown a8
        }
    \stemDown c8*2/3 | % 264
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown c8 \stemDown a16 \stemDown c16 \stemDown
        a16 \stemDown c16 \stemDown a8 }
    \stemDown c8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown c8 \stemDown a8 \stemDown c8 \stemDown a8
        }
    \stemDown c8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown c8 \stemDown a8 \stemDown c8 \stemDown a8
        }
    \stemDown c8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown es8 \stemDown c8 \stemDown es8 \stemDown
        c8 }
    \stemDown es8*2/3 | % 265
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown es8 \stemDown c16 \stemDown es16
        \stemDown c16 \stemDown es16 \stemDown c8 }
    \stemDown es8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown es8 \stemDown c8 \stemDown es8 \stemDown
        c8 }
    \stemDown es8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown es8 \stemDown c8 \stemDown es8 \stemDown
        c8 }
    \stemDown es8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown es8 \stemDown c8 \stemDown es8 \stemDown
        c8 }
    \stemDown es8*2/3 | % 266
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown es8 \stemDown c16 \stemDown es16
        \stemDown c16 \stemDown es16 \stemDown c8 }
    \stemDown es8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown es8 \stemDown c8 \stemDown es8 \stemDown
        c8 }
    \stemDown es8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown es8 \stemDown c8 \stemDown es8 \stemDown
        c8 }
    \stemDown es8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown es8 \stemDown c8 \stemDown es8 \stemDown
        c8 }
    \stemDown es8*2/3 | % 267
    \stemDown c8 \stemDown es8 r8 r4 \stemDown es'4. ^\markup{
        \bold\small {a. 2} } _ "" _\markup{ \italic {pesante} }
    \stemDown d8 \pageBreak | % 268
    \stemDown c4 \stemDown b4 \stemDown a,4. \stemDown a'4. \stemDown
    gis,8 \stemDown gis'8 | % 269
    \stemDown fis,4 \stemDown fis'4 \stemDown f,4 \stemDown f'4 \stemUp
    es,4. \stemUp es'4. \stemUp d,8 \stemUp d'8 | \barNumberCheck #270
    \stemUp c,8 \stemUp c'8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp es,8 \stemUp es'8 \stemUp es,8 \stemUp es'8 \stemUp es,8
        ~ }
    \stemUp es'8*2/3 ~ \stemUp es,8 \stemUp es'8 \stemUp es,8 -> \stemUp
    es'8 r4 | % 271
    r2 \stemUp c,4. _\ff ^\markup{ \bold\small {a. 2} } \stemUp d8 | % 272
    \stemUp es2 r2 \pageBreak | % 273
    R1 | % 274
    \stemUp c8 _\ff ^\markup{ \bold\small {a. 2} } r8 \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 ~ }
    \stemUp c8 \stemUp c8 -> r4 | % 275
    r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 }
    r4 r8 \stemUp c8 -> | % 276
    r4 \stemUp c8 -> r8 r2 | % 277
    R1*4 | % 281
    gis'1 ~ _\ff b1 ~ | % 282
    gis1 b1 | % 283
    fis'1 | % 284
    \stemUp g4. ( -> \stemUp fis8 ) \stemUp fis4 \stemUp cis4 _\fff
    \pageBreak | % 285
    fis1 ~ | % 286
    fis1 | % 287
    d,1 ~ d'1 ~ | % 288
    d,1 d'1 | % 289
    ais1 ~ e'1 ~ | \barNumberCheck #290
    ais,1 e'1 | % 291
    e,1 ~ fis1 ~ | % 292
    e1 fis1 | % 293
    R1*6 | % 299
    b,1 ~ _\ffff ^ "I." _\> | \barNumberCheck #300
    \stemUp b2 ~ \stemUp b8 _\! _\p r8 r4 | % 301
    R1 \break | % 302
    R1*3 \bar "||"
    \pageBreak | % 305
    \key b \major R1 | % 306
    r4 \stemUp dis4 -- ^\markup{ \bold\small {a. 2} } _\pp \stemUp e8 (
    \stemUp fis8 \stemUp gis8 \stemUp ais8 ) | % 307
    \stemDown b4 -- _\< \stemDown cis8. \stemDown d16 \stemDown dis4 --
    _\! _\> \stemDown e8 ( \stemDown dis8 ) | % 308
    \stemUp fis,4 -- _\! \stemUp dis4 -- \stemDown cis'4 -- \stemDown e4
    -- | % 309
    \stemDown dis4 -- _\< \stemDown cis8 ( \stemDown b8 ) \stemUp fis2
    _\! _\mp \stemUp a2 | \barNumberCheck #310
    \stemUp e2 _\markup{ \italic {poco cresc.} } \stemUp e'2 \stemUp e,2
    \stemUp g2 \pageBreak | % 311
    \stemUp dis2 \stemUp dis'2 r8 \stemDown dis8 ( _\mf ^\markup{
        \bold\small {a. 2} } _\> \stemDown cis8 \stemDown b8 ) | % 312
    \stemUp fis8 ( _\! _\p _\< \stemUp dis8 \stemUp b8 \stemUp dis8 )
    \stemUp gis4.. ( _\! _\> \stemUp fis16 ) | % 313
    \stemUp fis2 _\! _\p _\< \stemUp fis2 _\! _\ff \stemUp a2 | % 314
    \stemUp e2 \stemUp e'2 \stemUp e,2 \stemUp g2 | % 315
    \stemUp dis2 \stemUp dis'2 \stemUp b,2 _\sff _\> \stemUp gis'2 | % 316
    \stemUp b,2 _\! _\mf \stemUp fis'2 \stemUp e2 \stemUp ais2
    \pageBreak | % 317
    \stemUp dis,2 _\mf \stemUp b'2 \stemUp dis,2 \stemUp fis2 | % 318
    \stemUp e2 \stemUp cis'2 \stemUp cis,2 \stemUp e2 | % 319
    \stemUp dis2 \stemUp b'2 \stemUp b2 | \barNumberCheck #320
    \stemUp dis,2 \stemUp b'2 r8 \stemUp cis,4. -> \stemUp e4. | % 321
    \stemUp dis2 \stemUp fis2 \stemUp dis2 _\mf \stemUp fis2 | % 322
    \stemUp cis2 \stemUp e2 \stemUp cis2 \stemUp e2 | % 323
    \stemUp dis2 r2 | % 324
    R1*2 \break | % 326
    R1*8 \pageBreak | % 334
    R1 \bar "||"
    R1*5 | \barNumberCheck #340
    \stemUp e2 _\p ^\markup{ \italic {cantabile} } \stemUp gis2 \stemUp
    e4. _\< \stemUp gis4. \stemUp e8 \stemUp gis8 | % 341
    \stemUp fis2. ~ _\! _\mf _\> \stemUp b2. ~ \stemUp fis8 \stemUp b8 r8
    _\! | % 342
    \stemUp e,2 _\p \stemUp gis2 \stemUp e4. _\< \stemUp gis4. \stemUp e8
    \stemUp gis8 \pageBreak | % 343
    fis1 _\! _\mf _\> b1 | % 344
    \stemUp b2. ~ _\! _\p \stemUp b8 r8 | % 345
    R1*10 \bar "|."
    }

PartPThreeVoiceTwo =  \relative b' {
    \clef "treble" \time 4/4 \key d \major s1*11 \break s2. \stemDown b4
    | % 13
    \stemDown e,2. ~ \stemDown e8 s8*41 \bar "||"
    s1*5 \pageBreak s1*6 | \barNumberCheck #30
    \time 2/4  s2 \break | % 31
    \time 4/4  s1*6 \break s1*7 \pageBreak s1*6 \break s1*4 \pageBreak
    s1*2 | % 56
    r2 s2*5 \break | % 59
    R1 s1 | % 61
    R1 | % 62
    \stemDown fisis8 ( -. \stemDown ais8 ) -. \stemDown dis4 ~ \stemDown
    dis8 r8 r4 | % 63
    R1 \pageBreak | % 64
    r2 s16 \stemDown fis,16 -. \stemDown fis16 -. \stemDown fis16 -.
    \stemDown fis16 ( \stemDown ais16 ) \stemDown gis16 -. \stemDown fis16
    -. | % 65
    \stemDown fis8 -- \stemDown cis8 -- \stemDown cisis8 -- s8.
    \stemDown fis16 -. \stemDown fis16 -. \stemDown fis16 -. \stemDown
    fis16 ( \stemDown eis16 ) \stemDown gis16 -. \stemDown gis16 -. | % 66
    \stemDown fis8 -- \stemDown fis8 -- \stemDown fis8 -- r8 _\! s2*5
    \pageBreak s1*2 | % 71
    r8 \stemDown e'8 ~ -> \stemDown e8 \stemDown a,8 -. s2 | % 72
    r8 \stemDown e'8 ~ -> \stemDown e8 \stemDown a,8 -. s1. \pageBreak
    s2*5 \stemDown bis,4 ( -> \stemDown cis8 ) r8 | % 77
    \stemDown bis4 ( -> \stemDown cis8 ) r8 r2 \break s1*5 \pageBreak
    s1*6 \bar "||"
    s1*5 \break s1*7 \bar "||"
    s1*2 \pageBreak s1*5 \break s1*4 \pageBreak s1*4 \break s1*4
    \pageBreak s1*5 \break s1*5 \bar "||"
    \time 12/8  s1*3 \pageBreak s1*9 \pageBreak s1*6 \bar "||"
    s1. | % 143
    \numericTimeSignature\time 4/4  s1*2 \break s1 | % 146
    \stemDown d4 ( \stemDown fis4 ) s2*19 \pageBreak s1*5 \bar "||"
    \key c \major s1*4 \pageBreak s1*7 \pageBreak s1*6 \pageBreak | % 178
    \stemDown b'8 s8*7 | % 179
    r2 r8 \stemDown fis8 ( \stemDown e8 ) s4. \stemDown c8 -. \stemDown
    a8 ( \stemDown g8 ) \stemDown a8 ~ \stemDown a8 \stemDown e'8 ~ | % 181
    \stemDown e4. \stemDown e8 ~ \stemDown e4. \stemDown e8 ~ | % 182
    \stemDown e8 s8*7 \break s1*5 \pageBreak s1*4 \break s1*4 \pageBreak
    | % 196
    \stemDown bes4 -> \stemDown a4 -> \stemDown d,2 | % 197
    \stemDown e4 -> \stemDown d4 -> s2*7 \break s1*6 \pageBreak s16*47
    \stemDown b'16 | \barNumberCheck #210
    \stemDown b8 s8 \stemDown ais8 s8 \stemDown gis8 s8 \stemDown ais8
    s16 \stemDown d16 | % 211
    \stemDown d8 s8 \stemDown cis8 s8 \stemDown b8 s8 \stemDown cis8 s8
    | % 212
    \stemDown cis8 s8 \stemDown dis8 s8 \stemDown dis8 s8 \stemDown eis8
    s8 \pageBreak | % 213
    \stemDown dis8 s8 \stemDown eis8 s8 \stemDown dis8 s8 \stemDown eis8
    s8*25 \break s1*4 \pageBreak s1*5 \break s1*5 \break s1*6 \pageBreak
    s1*5 \pageBreak s1 | % 243
    \stemDown d2 \stemDown e4.. \stemDown e16 | % 244
    \stemDown b8 s8 \stemDown ais8 s8 \stemDown g16 ( \stemDown fis16 )
    \stemDown fis8 \stemDown fis8 \stemDown g8 | % 245
    \stemDown gis4 ( -> \stemDown ais8 ) s4. \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 \stemDown e,8 \stemDown b'8 }
    \pageBreak | % 246
    \stemDown gis4 ( -> \stemDown ais8 ) s2 \stemDown ais8 s1*5 \break
    s4*9 \stemDown cis8 \stemDown d8 \stemDown dis8 ( -> \stemDown eis8
    ) s4*9 \pageBreak s1*6 \pageBreak s1*5 \pageBreak s1*5 \pageBreak
    s1*10 | % 283
    \stemDown d2 \stemDown cis2 ~ | % 284
    \stemDown cis2. \stemDown cis4 \pageBreak | % 285
    fis1 ~ | % 286
    fis1 s1*15 \break s1*3 \bar "||"
    \pageBreak | % 305
    \key b \major s1*6 \pageBreak s1*6 \pageBreak s2*5 \stemDown d,4 (
    \stemDown e8 \stemDown d8 ) s1*3 | % 323
    \stemDown b2 \stemDown b2 | % 324
    \stemDown b2 r2 s1 \break s1*8 \pageBreak s1 \bar "||"
    s1*8 \pageBreak s1 | % 344
    R1 s1*10 \bar "|."
    }

PartPFourVoiceOne =  \relative b {
    \clef "treble" \time 4/4 \key f \major \transposition a | % 1
    R1*11 \break | % 12
    r2 r4 \stemUp b4 _\p ^ "I." _\< | % 13
    \stemUp cis2. ~ _\! _\mf _\> \stemUp cis8 r8 _\! | % 14
    r2 r4 \stemUp f8 ( _\p _\< \stemUp g8 ) | % 15
    \stemUp a2 ~ _\! _\mf _\> \stemUp a8 r8 _\! r4 | % 16
    R1*3 \bar "||"
    R1*4 | % 23
    r2 r4 \stemUp <f, f'>8 ( -. _\p _\< \stemUp <g e'>8 ) -. \pageBreak
    | % 24
    \stemUp <gis d'>4 ( _\! _\> \stemUp <a cis>8 ) r8 _\! r4 \stemUp d4
    ( ~ _\p _\< | % 25
    \stemUp d4 _\! _\> \stemUp cis8 ) r8 _\! r4 r8 \stemUp <e cis'>8 _\p
    | % 26
    r8 \stemUp <f d'>8 r8 \stemUp <bes, d'>8 r8 \stemUp <c c'>8 r8
    \stemUp <a c'>8 | % 27
    r8 \stemUp <bes bes'>8 r8 \stemUp <g d'>8 ~ ~ \stemUp <g d'>8 r8 r4
    | % 28
    r4 \stemUp e''16 ( _\p \stemUp d16 ) \stemUp c16 -. \stemUp bes16 -.
    \stemUp a16 -. \stemUp g16 -. \stemUp f16 -. \stemUp e16 -. r4 | % 29
    R1 | \barNumberCheck #30
    \time 2/4  r4 \stemUp d4 ~ _\pp ^ "I." _\< \break | % 31
    \time 4/4  \stemUp d4 ~ _\! _\> \stemUp d8 r8 _\! r4 \stemUp d4 ~
    _\< | % 32
    \stemUp d4 ~ _\! _\> \stemUp d8 r8 _\! r4 \stemUp f4 ~ _\< | % 33
    \stemUp f4 ~ _\! _\> \stemUp f8 r8 _\! r4 \stemUp f4 ~ _\< | % 34
    \stemUp f4 ~ _\! _\> \stemUp f8 r8 _\! r4 \stemUp as4 ~ _\p _\< | % 35
    \stemUp as8 r8 _\! \stemUp as4 ~ _\p _\< \stemUp as8 r8 _\!
    \stemDown b4 ~ _\p _\< | % 36
    \stemDown b8 r8 _\! \stemDown b4 ~ _\p _\< \stemDown b8 r8 _\!
    \stemDown d4 ~ _\mp _\< \break | % 37
    \stemDown d8 r8 _\! r4 r2 | % 38
    R1*6 \pageBreak | % 44
    r2 r8 \stemUp a8 ( _\pp ^ "I." \stemUp g8 \stemUp f8 | % 45
    \stemUp e8 ) \stemUp d8 ( \stemUp c8 \stemUp b8 \stemUp a8 ) \stemUp
    g8 ( \stemUp f8 \stemUp e8 ) | % 46
    \stemUp e'16 ( \stemUp f16 \stemUp e16 \stemUp f16 \stemUp e16
    \stemUp f16 \stemUp e16 \stemUp f16 \stemUp e8 ) r8 r4 | % 47
    R1 | % 48
    r2 r8 \stemDown e'8 ( _\p \stemDown d8 \stemDown c8 | % 49
    \stemUp b8 ) \stemUp a8 ( \stemUp g8 \stemUp fis8 \stemUp e8 )
    \stemUp d8 ( \stemUp c8 \stemUp b8 ) \break | \barNumberCheck #50
    \stemDown b'16 ( \stemDown c16 \stemDown b16 \stemDown c16 \stemDown
    b16 \stemDown c16 \stemDown b16 \stemDown c16 \stemDown b8 ) r8 r4 | % 51
    R1*3 \pageBreak | % 54
    r2 r16 \stemDown <g' e'>16 -. _\pp _\< \stemDown <g e'>16 -.
    \stemDown <g e'>16 -. \stemDown <g e'>16 ( \stemDown <g d'>16 )
    \stemDown <e c'>16 -. \stemDown <e b'>16 -. | % 55
    \stemDown <d b'>8 -- _\! _\> \stemDown <gis, eis'>8 -- \stemDown
    <fis fis'>8 -- r8 _\! r16 \stemDown <c' b'>16 -. _\pp _\< \stemDown
    <c b'>16 -. \stemDown <c b'>16 -. \stemDown <c b'>16 ( \stemDown <c
        a'>16 ) \stemDown <a g'>16 -. \stemDown <a fis'>16 -. | % 56
    \stemUp <g e'>8 -- _\! _\> \stemUp <e cis'>8 -- \stemUp <d d'>8 -- r8
    _\! r16 \stemDown <d g'>16 -. _\p _\< \stemDown <d g'>16 -.
    \stemDown <d g'>16 -. \stemDown <d g'>16 ( \stemDown <b' fis'>16 )
    \stemDown <g e'>16 -. \stemDown <g d'>16 -. | % 57
    \stemUp d'8 -- _\! _\> \stemUp a8 -- \stemUp ais8 -- r8 _\! r16
    \stemDown <e' d'>16 ^. _\p _\< \stemDown <e d'>16 ^. \stemDown <e
        d'>16 ^. \stemDown <e d'>16 ( \stemDown <e cis'>16 ) \stemDown
    <cis b'>16 ^. \stemDown <cis ais'>16 ^. | % 58
    \stemDown <b g'>8 -- _\! _\> \stemDown <g eis'>8 -- \stemDown <fis
        fis'>8 -- r8 _\! r2 \break | % 59
    R1 | \barNumberCheck #60
    r4 \stemUp fis4 ~ _\sf ^ "I." _\> \stemUp fis8 r8 _\! r4 | % 61
    R1 | % 62
    r4 \stemUp fis4 ~ _\sf _\> \stemUp fis16 \stemUp b'16 -. _\! _\p
    ^\markup{ \italic {solo} } _\< \stemUp b16 -. \stemUp b16 -. \stemUp
    b16 ( \stemUp a16 ) \stemUp g16 -. \stemUp fis16 -. | % 63
    \stemUp fis8 -- _\! _\> \stemUp bis,8 -- \stemUp cis8 -- r8 _\! r16
    \stemUp fis16 -. _\p ^\markup{ \italic {solo} } _\< \stemUp fis16 -.
    \stemUp fis16 -. \stemUp fis16 ( \stemUp e16 ) \stemUp d16 -.
    \stemUp cis16 -. \pageBreak | % 64
    \stemUp b8 -- _\! _\> \stemUp gis8 -- \stemUp a8 -- r8 _\! r16
    \stemUp d'16 -. _\mp ^\markup{ \italic {solo} } _\< \stemUp d16 -.
    \stemUp d16 -. \stemUp d16 ( \stemUp cis16 ) \stemUp b16 -. \stemUp
    a16 -. | % 65
    \stemUp a8 -- _\! _\> \stemUp e8 -- \stemUp eis8 -- r8 _\! r16
    \stemUp a16 -. _\mp ^\markup{ \italic {solo} } _\< \stemUp a16 -.
    \stemUp a16 -. \stemUp a16 ( \stemUp gis16 ) \stemUp fis16 -.
    \stemUp eis16 -. | % 66
    \stemUp d8 -- _\! _\> \stemUp bis8 -- \stemUp cis8 -- r8 _\! r16
    \stemDown <fis, fis'>16 -. _\f ^\markup{ \italic {solo} } \stemDown
    <fis fis'>16 -. \stemDown <fis fis'>16 -. \stemDown <fis fis'>16 (
    \stemDown <a a'>16 ) \stemDown <gis gis'>16 -. \stemDown <fis fis'>16
    -. | % 67
    \stemUp <eis eis'>2 ( \stemDown <fis fis'>8 ) r8 r4 | % 68
    r2 r16 \stemDown <a a'>16 -. _\ff \stemDown <a a'>16 -. \stemDown <a
        a'>16 -. \stemDown <a a'>16 ( \stemDown <c c'>16 ) \stemDown <b
        b'>16 -. \stemDown <a a'>16 -. \pageBreak | % 69
    \stemDown <gis gis'>2 ( \stemDown <a a'>8 ) r8 r4 | \barNumberCheck
    #70
    r2 r16 \stemUp c'16 -. \stemUp c16 -. \stemUp c16 -. \stemUp c8 -. r8
    | % 71
    \stemUp as16 ( \stemUp g16 \stemUp f16 \stemUp es16 ) \stemUp d16 (
    \stemUp c16 \stemUp as16 \stemUp g16 ) r16 \stemUp c'16 -. \stemUp c16
    -. \stemUp c16 -. \stemUp c8 -. r8 | % 72
    \stemUp as16 ( \stemUp g16 \stemUp f16 \stemUp es16 ) \stemUp d16 (
    \stemUp c16 \stemUp as16 \stemUp g16 ) r16 \stemUp c'16 -. \stemUp c16
    -. \stemUp c16 -. \stemUp c8 -. r8 | % 73
    r16 \stemUp c,16 -. \stemUp c16 -. \stemUp c16 -. \stemUp c8 -. r8 r16
    \stemUp c'16 -. \stemUp c16 -. \stemUp c16 -. \stemUp c8 -. r8
    \pageBreak | % 74
    r16 \stemUp c,16 -. \stemUp c16 -. \stemUp c16 -. \stemUp c8 -. r8
    \stemDown <fis, fis'>4 ( -> \stemDown <g g'>8 ) r8 | % 75
    \stemDown <fis fis'>4 ( -> \stemDown <g g'>8 ) r8 \stemUp <dis dis'>4
    ( -> \stemUp <e e'>8 ) r8 | % 76
    \stemUp <dis dis'>4 ( -> \stemUp <e e'>8 ) r8 \stemUp dis4 ( -> ^\f
    \stemUp e8 ) r8 | % 77
    \stemUp dis4 ( -> \stemUp e8 ) r8 \stemUp <e, bes'>4 ~ -> ~ _\mf
    \stemUp <e bes'>8 r8 \break | % 78
    \stemUp <e bes'>4 ~ -> ~ \stemUp <e bes'>8 r8 r4 \stemUp <e bes'>4 ~
    ~ _\mp | % 79
    \stemUp <e bes'>4 ~ ~ _\> \stemUp <e bes'>8 r8 _\! r4 \stemUp <e
        bes'>4 ~ ~ _\p | \barNumberCheck #80
    \stemUp <e bes'>8 r8 r4 r2 | % 81
    R1*2 \pageBreak | % 83
    R1*6 \bar "||"
    R1 | \barNumberCheck #90
    r2 \stemUp b'2 ( ^ "I." _\mp _\> | % 91
    \stemUp c8 ) _\! _\pp r8 r4 r2 | % 92
    r2 \stemUp <g g'>2 ( _\mp _\> | % 93
    \stemUp a'8 ) _\! _\pp r8 r4 r2 _\mf \break | % 94
    R1 | % 95
    r2 _\! _\p _\< \stemUp d2 ( _\! _\mf _\> | % 96
    \stemUp c8 ) _\! _\p r8 r4 r2 | % 97
    R1*2 | % 99
    r2 _\! _\p _\< \stemUp d2 ( _\! _\mf _\> | \barNumberCheck #100
    \stemUp c8 ) _\! _\p r8 r4 r2 \bar "||"
    R1*2 \pageBreak | % 103
    R1*3 | % 106
    \stemUp <a, a'>4 ~ ~ _\mp _\< \once \omit TupletBracket
    \times 2/3  {
        \stemUp <a a'>8 \stemUp <b b'>8 ( \stemUp <cis cis'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d d'>8 ) \stemUp <d d'>8 ( -. \stemUp <e e'>8 ) -. }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <f f'>16 ( \stemDown <g g'>16 \stemDown <a a'>16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <b b'>16 \stemDown <c c'>16 \stemDown <cis cis'>16 }
    | % 107
    \stemDown <d d'>8 ) _\! _\f r8 r4 r2 \break | % 108
    R1 | % 109
    \stemUp g,4 ~ _\p ^ "I." _\< \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 \stemUp a8 ( \stemUp b8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 ) \stemDown c8 ( -- \stemDown d8 -- }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 -- \stemDown f8 -- \stemDown g8 ) -- }
    | \barNumberCheck #110
    \stemDown a4 ( ~ -> _\! _\> \stemDown a16 \stemDown e16 \stemDown c16
    \stemDown b16 \stemUp a8 ) r8 _\! r4 | % 111
    \stemDown d4 ~ _\p _\< \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 ( \stemDown e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f8 ) \stemDown f8 ( -- \stemDown g8 -- }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 -- \stemDown b8 -- \stemDown c8 ) -- }
    \pageBreak | % 112
    \stemDown d4 ( ~ -> _\! _\> \stemDown d16 \stemDown b16 \stemDown g16
    \stemDown d16 \stemDown b8 ) r8 _\! r4 | % 113
    R1 | % 114
    \stemUp <e,, e'>4 ~ ~ _\mp _\< \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <fis fis'>8 ( \stemUp <gis gis'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <a a'>8 ) \stemUp <a a'>8 ( -- \stemUp <b b'>8 ) -- }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <c c'>16 ( \stemUp <d d'>16 \stemUp <e e'>16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <fis fis'>16 \stemUp <g g'>16 \stemUp <gis gis'>16 }
    | % 115
    \stemUp <a a'>8 ) _\! _\f r8 r4 r2 \break | % 116
    R1 | % 117
    \stemUp d,4 ~ ^\markup{ \bold\small {a. 2} } _\p \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp d8 _\< \stemUp e8 ( \stemUp fis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 ) \stemUp g8 ( -- \stemUp a8 -- }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 -- \stemDown c8 -- \stemDown cis8 ) -- }
    | % 118
    \stemDown d4 ( ~ -> _\! _\> \stemUp d16 \stemUp b16 \stemUp g16
    \stemUp d16 \stemUp b8 ) r8 _\! r4 | % 119
    \stemUp d4 ~ _\markup{ \italic {più} } _ "" \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp d8 \stemUp e8 ( \stemUp fis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 ) \stemUp g8 ( -- \stemUp a8 -- }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown bes8 -- \stemDown c8 -- \stemDown cis8 ) -- }
    \pageBreak | \barNumberCheck #120
    \stemDown d4 ( ~ -> \stemUp d16 \stemUp bes16 \stemUp g16 \stemUp d16
    \stemUp bes8 ) r8 r4 | % 121
    R1 | % 122
    \stemDown c'4 ( ~ _\f ^\markup{ \bold\small {a. 2} } \stemUp c16
    \stemUp g16 \stemUp f16 \stemUp c16 ) \stemDown g''4 ( ~ \stemDown g16
    \stemDown c,16 \stemDown g16 \stemDown e16 ) | % 123
    \stemUp d2 \once \omit TupletBracket
    \times 4/6  {
        \stemUp d16 ( \stemUp e16 \stemUp d16 \stemUp e16 \stemUp d16
        \stemUp cis16 }
    \stemUp d8 ) r8 | % 124
    r2 \stemDown f'4 ( ~ _\ff \stemUp f16 \stemUp c16 \stemUp f,16
    \stemUp c16 ) \break | % 125
    r8 \stemDown f'8 ( ~ \stemUp f16 \stemUp c16 \stemUp f,16 \stemUp c16
    ) r8 \stemDown f'8 ( ~ \stemUp f16 \stemUp c16 \stemUp f,16 \stemUp
    c16 ) | % 126
    r8 \stemDown bes''8 ( ~ \stemDown bes16 \stemDown e,16 \stemDown bes16
    \stemDown e,16 ) r8 \stemDown bes''8 ( ~ \stemDown bes16 \stemDown
    e,16 \stemDown bes16 \stemDown e,16 ) | % 127
    r4 \stemDown bes'4 ( _\ff \stemUp a4 \stemUp g4 ) | % 128
    \stemUp f4 ( \stemUp e2 ) \stemUp d4 ( | % 129
    \stemUp des2 _\sff _\> \stemUp c4 ~ \stemUp c8 ) r8 ^\fermata _\!
    \bar "||"
    \time 12/8  r8*2/3 \stemUp <a c>8 ^\markup{ \italic {pesante, non
            staccato} } _\p \stemUp <a c>8 \stemUp <a c>8 \stemUp <a c>8
    \stemUp <a c>8 \stemUp <a c>4. ~ ~ \stemUp <a c>8 r8*2/3 r8*2/3 s8 | % 131
    r8*2/3 \stemDown <f' f'>8 _\markup{ \italic {sempre} } _ ""
    \stemDown <f f'>8 \stemDown <f f'>8 \stemDown <f f'>8 \stemDown <f
        f'>8 r8*2/3 \stemUp <d gis>8 \stemUp <d gis>8 \stemUp <d gis>8
    \stemUp <d gis>8 \stemUp <f gis>8 s1*1/12 \pageBreak | % 132
    r8*2/3 \stemUp <f a>8 \stemUp <f a>8 \stemUp <f a>8 \stemUp <f a>8
    \stemUp <f a>8 \stemUp <f a>8 r8*2/3 r8*2/3 r4*2/3 r8*2/3 s4 | % 133
    r8*2/3 \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c
        c'>8 \stemUp <c c'>8 r8*2/3 \stemDown <g' e'>8 \stemDown <g e'>8
    \stemDown <g e'>8 \stemDown <g e'>8 \stemDown <g e'>8 s1*1/12 | % 134
    r8*2/3 \stemDown <a f'>8 _\p _\< \stemDown <a f'>8 \stemDown <a f'>8
    \stemDown <a f'>8 r8*2/3 _\! \stemDown <c es>2. _\mf s1*1/12 | % 135
    \stemDown <bes d>8 \stemDown <bes d>8 \stemDown <bes d>8 \stemDown
    <bes d>8 \stemDown <bes d>8 \stemDown <bes d>8 \stemDown <bes des>2.
    | % 136
    \stemDown <a c>8 _\< \stemDown <a c>8 \stemDown <a c>8 \stemDown <a
        c>8 \stemDown <a c>8 \stemDown <a c>8 \stemUp <d, a'>2. _\! _\sf
    _\> | % 137
    \stemUp <c a'>8 _\! _\p _\< \stemUp <c a'>8 \stemUp <c a'>8 \stemUp
    <c a'>8 \stemUp <c a'>8 \stemUp <c a'>8 \stemUp <e bes'>2. _\! _\mf
    _\> \pageBreak | % 138
    r8*2/3 _\! \stemDown <a f'>8 _\p _\< \stemDown <a f'>8 \stemDown <a
        f'>8 \stemDown <a f'>8 r8*2/3 _\! \stemDown <c es>2. _\mf
    s1*1/12 | % 139
    \stemDown <bes d>8 \stemDown <bes d>8 \stemDown <bes d>8 \stemDown
    <bes d>8 \stemDown <bes d>8 \stemDown <bes d>8 \stemDown <bes des>2.
    | \barNumberCheck #140
    \stemDown <a c>8 _\< \stemDown <a c>8 \stemDown <a c>8 \stemDown <a
        c>8 \stemDown <a c>8 \stemDown <a c>8 \stemUp <d, a'>2. _\! _\sf
    _\> | % 141
    \stemUp <c a'>8 _\! _\p _\< \stemUp <c a'>8 \stemUp <c a'>8 \stemUp
    <c a'>8 \stemUp <c a'>8 \stemUp <c a'>8 \stemUp <e bes'>2. _\! _\mf
    _\> \bar "||"
    r8*2/3 _\! \stemUp <f a>8 _\mf _\> \stemUp <f a>8 \stemUp <f a>8
    \stemUp <f a>8 \stemUp <f a>8 \stemDown <f f'>4. ( _\! _\mp
    \stemDown <fis fis'>4. ) s1*1/24 | % 143
    \numericTimeSignature\time 4/4  \stemDown <fis fis'>4 ( \stemDown <g
        g'>4 ) \stemUp <d d'>4 ( \stemUp <e e'>4 ) | % 144
    \stemUp <e e'>4 ( _\> \stemDown <f f'>4 ) \stemDown <f f'>4 ( _\!
    _\p \stemDown <fis fis'>4 ) \break | % 145
    \stemDown <a a'>4 ( \stemDown <b b'>4 ) \stemUp <d, d'>4 ( \stemUp
    <e e'>4 ) | % 146
    \stemUp f'2 \stemUp f,4 ( _\p \stemUp fis4 ) | % 147
    \stemUp fis4 ( ^\markup{ \bold\small {a. 2} } \stemUp g4 ) \stemUp d4
    ( \stemUp e4 ) | % 148
    \stemUp e4 ( _\> \stemUp f4 ) \stemUp f4 ( _\! _\pp \stemUp fis4 ) | % 149
    \stemUp g4 ( \stemDown b4 ) \stemUp d,4 ( \stemUp e4 |
    \barNumberCheck #150
    \stemUp f8 ) r8 r4 r2 | % 151
    R1*2 | % 153
    r2 r8 \stemDown a'8 ( ^ "I." ^\markup{ \italic {solo} } _\ppp
    \stemDown g8 \stemDown f8 ) | % 154
    \stemDown d8 ( _\< \stemDown c8 \stemDown a8 \stemDown c8 )
    \stemDown f4. ( _\! _\p _\> \stemDown d8 ) | % 155
    \stemDown c2 ~ _\! _\ppp \stemDown c8 \stemDown a'8 ( \stemDown g8
    \stemDown f8 ) \pageBreak | % 156
    \stemUp c8 ( _\< \stemUp a8 \stemUp f8 \stemUp a8 ) \stemDown d4.. (
    _\! _\p _\> \stemDown c16 ) | % 157
    \stemDown c2 ~ _\! \stemUp c8 _\pppp \stemUp a8 ( \stemUp g8 \stemUp
    f8 ) | % 158
    \stemUp c2 ~ \stemUp c8 \stemUp a'8 ( \stemUp g8 \stemUp f8 ) | % 159
    \stemUp c2 ~ _\> \stemUp c8 \stemUp a'8 ( _\! _\ppppp \stemUp g8
    \stemUp f8 ) | \barNumberCheck #160
    \stemUp d8 ( \stemUp c8 \stemUp a8 \stemUp f8 ) r2 ^\fermata \bar
    "||"
    \key c \major \stemDown <bes'' c>8 _\ff r8 r4 \stemUp <bes,, c>16 ->
    _\sff \stemUp <bes c>16 \stemUp <bes c>8 ~ ~ \stemUp <bes c>4 ~ ~ | % 162
    \stemUp <bes c>8 \stemUp <a des>8 -> \stemUp <gis c>8 -> \stemUp <a
        d>8 -> \stemUp <bes c>8 -> r8 r4 | % 163
    \stemUp <a c>8 _\sf r8 \stemUp <gis b>8 _\sf r8 r4 r8 \stemUp <gis
        b>8 _\sf | % 164
    \stemUp <a c>8 _\sf r8 \stemUp bes8 _\sf r8 r4 \stemDown <bes' ges'>8
    ( _\ff \stemDown <ges' bes>8 ) \pageBreak | % 165
    \stemDown <bes, bes'>8 r8 r4 \stemUp <bes, g'>16 _\sff \stemUp <bes
        g'>16 \stemUp <bes g'>8 ~ ~ \stemUp <bes g'>4 ~ ~ | % 166
    \stemUp <bes g'>8 \stemUp <a fis'>8 -> \stemUp <gis eis'>8 ->
    \stemUp <a fis'>8 -> \stemUp <bes g'>8 -> r8 r4 | % 167
    \stemUp a8 _\sf r8 \stemUp bes8 _\sf r8 r4 r8 \stemUp bes8 _\sf | % 168
    \stemUp <a c>8 _\sf r8 \stemUp <g bes>8 _\sf r8 r4 \stemDown <bes'
        g'>8 ( _\ff \stemDown <g' bes>8 ) | % 169
    \stemDown <f as>8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <f as>16 _\sff \stemDown <f as>16 \stemDown <f as>16 }
    \stemDown <f as>8 ~ ~ \stemDown <f as>4 ~ ~ | \barNumberCheck #170
    \stemUp <f as>8 \stemUp <g,, g'>8 -> \stemUp <f f'>8 -> \stemUp <g
        g'>8 -> \stemUp <as as'>8 -> \stemUp <as as'>8 -> r4 | % 171
    R1 \pageBreak | % 172
    r2 r4 r8 \stemDown f''8 ~ _\f ^\markup{ \bold\small {a. 2} } | % 173
    \stemDown f4. \stemDown f8 ~ \stemDown f4. \stemDown f8 ~ | % 174
    \stemDown f8 r8 r4 r2 | % 175
    r4 r8 \stemUp <f, c'>8 ( _\ff \stemUp <as, f'>8 ) r8 r4 | % 176
    r4 r8 \stemUp <f' c'>8 ( _\ff \stemUp <as, f'>8 ) r8 r8 \stemUp c''8
    ~ ^\f | % 177
    \stemUp c4. \stemUp c8 ~ \stemUp c4. \stemUp c8 ~ \pageBreak | % 178
    \stemUp c8 _ "" r8 r4 r2 | % 179
    r2 r8 \stemDown a8 ( _\mf ^ "I." \stemDown g8 ) r8 | \barNumberCheck
    #180
    r4 \stemUp g8 -. _\mf \stemUp a8 ( \stemUp d,8 ) \stemUp g8 -. r8
    \stemUp g'8 ~ _\f | % 181
    \stemUp g4. \stemUp g8 ~ \stemUp g4. \stemUp g8 ~ | % 182
    \stemUp g8 r8 r4 r2 \break | % 183
    r4 r8 \stemDown <g, d'>8 ( _\ff \stemDown <bes, g'>8 ) r8 r4 | % 184
    r4 r8 \stemDown <g' d'>8 ( _\ff \stemDown <bes, g'>8 ) r8 r4 | % 185
    r2 r4 \stemDown c16 ( _\ff ^\markup{ \bold\small {a. 2} } \stemDown
    f16 \stemDown e16 \stemDown c16 ) | % 186
    \stemDown d16 ( \stemDown g16 \stemDown f16 \stemDown d16 )
    \stemDown e16 ( \stemDown a16 \stemDown g16 \stemDown e16 )
    \stemDown f16 ( \stemDown bes16 \stemDown a16 \stemDown f16
    \stemDown e8 ) r8 | % 187
    r2 r4 \stemDown a,16 ( _\fff \stemDown d16 \stemDown c16 \stemDown a16
    ) \pageBreak | % 188
    \stemDown bes16 ( \stemDown e16 \stemDown d16 \stemDown bes16 )
    \stemDown c16 ( \stemDown f16 \stemDown e16 \stemDown c16 )
    \stemDown d16 ( \stemDown g16 \stemDown f16 \stemDown d16 )
    \stemDown cis16 ( \stemDown gis'16 \stemDown fis16 \stemDown cis16 )
    | % 189
    \stemDown cis16 ( \stemDown gis'16 \stemDown fis16 \stemDown cis16 )
    \stemDown cis16 ( \stemDown gis'16 \stemDown fis16 \stemDown cis16 )
    \stemDown cis16 ( \stemDown gis'16 \stemDown fis16 \stemDown cis16 )
    \stemDown cis16 ( \stemDown gis'16 \stemDown fis16 \stemDown cis16 )
    | \barNumberCheck #190
    \stemDown cis16 ( \stemDown gis'16 \stemDown fis16 \stemDown cis16 )
    \stemDown cis16 ( \stemDown gis'16 \stemDown fis16 \stemDown cis16 )
    \stemDown cis16 ( \stemDown gis'16 \stemDown fis16 \stemDown cis16 )
    \stemDown cis16 ( \stemDown gis'16 \stemDown fis16 \stemDown cis16 )
    | % 191
    \stemDown cis16 ( \stemDown gis'16 \stemDown fis16 \stemDown cis16 )
    \stemDown cis16 ( \stemDown gis'16 \stemDown fis16 \stemDown cis16 )
    \stemDown cis16 ( \stemDown gis'16 \stemDown fis16 \stemDown cis16 )
    \stemDown cis16 ( \stemDown gis'16 \stemDown fis16 \stemDown cis16 )
    \break | % 192
    \stemDown fis16 ( \stemDown b16 \stemDown ais16 \stemDown fis16 )
    \stemDown fis16 ( \stemDown b16 \stemDown ais16 \stemDown fis16 )
    \stemDown fis16 ( \stemDown b16 \stemDown ais16 \stemDown fis16 )
    \stemDown fis16 ( \stemDown b16 \stemDown ais16 \stemDown fis16 ) | % 193
    \stemDown fis16 ( \stemDown b16 \stemDown ais16 \stemDown fis16 )
    \stemDown fis16 ( \stemDown b16 \stemDown ais16 \stemDown fis16 )
    \stemDown fis16 ( \stemDown b16 \stemDown ais16 \stemDown fis16 )
    \stemDown f16 ( \stemDown bes16 \stemDown as16 \stemDown f16 ) | % 194
    \stemDown f16 ( \stemDown bes16 \stemDown as16 \stemDown f16 )
    \stemDown f16 ( \stemDown bes16 \stemDown as16 \stemDown f16 )
    \stemDown f16 ( \stemDown bes16 \stemDown as16 \stemDown f16 )
    \stemDown f16 ( \stemDown bes16 \stemDown as16 \stemDown f16 ) | % 195
    \stemDown as16 ( \stemDown des16 \stemDown c16 \stemDown as16 )
    \stemDown as16 ( \stemDown des16 \stemDown c16 \stemDown as16 )
    \stemDown as16 ( \stemDown des16 \stemDown c16 \stemDown as16 )
    \stemDown as16 ( \stemDown des16 \stemDown c16 \stemDown as16 )
    \pageBreak | % 196
    \stemDown f16 ( \stemDown bes16 \stemDown as16 \stemDown f16 )
    \stemDown f16 ( \stemDown bes16 \stemDown as16 \stemDown f16 )
    \stemDown c16 ( \stemDown g'16 \stemDown f16 \stemDown c16 )
    \stemDown c16 ( \stemDown g'16 \stemDown f16 \stemDown c16 ) | % 197
    \stemDown as16 ( \stemDown des16 \stemDown c16 \stemDown as16 )
    \stemDown as16 ( \stemDown des16 \stemDown c16 \stemDown as16 )
    \stemUp f16 ( \stemUp bes16 \stemUp as16 \stemUp f16 ) \stemUp c16 (
    \stemUp g'16 \stemUp f16 \stemUp c16 ) | % 198
    \stemUp as16 ( \stemUp des16 \stemUp c16 \stemUp as16 ) \stemUp f16
    ( \stemUp bes16 \stemUp as16 \stemUp f16 ) \stemUp c'16 ( \stemUp g'16
    \stemUp f16 \stemUp c16 ) \stemUp as16 ( \stemUp des16 \stemUp c16
    \stemUp as16 | % 199
    \stemUp f8 ) r8 r4 r2 | \barNumberCheck #200
    R1 \break | % 201
    R1*4 | % 205
    r2 \once \omit TupletBracket
    \times 4/7  {
        \stemDown <e'' g>16*161/160 ( _\p _\< \stemDown <f as>16*161/160
        \stemDown <g bes>16*161/160 \stemDown <as c>16*161/160 \stemDown
        <bes des>16*161/160 \stemDown <c e>16*161/160 \stemDown <des f>16*161/160
        }
    \stemDown <e g>8 ) _\! r8 | % 206
    R1 \pageBreak | % 207
    R1*2 | % 209
    r2 r4 r8. \stemUp a,,,16 _\mf \stemUp a'16 | \barNumberCheck #210
    \stemUp a,8 _\markup{ \italic {poco cresc.} } \stemUp a'8 r8 \stemUp
    bes,8 \stemUp bes'8 r8 r4 r8. \stemUp c,16 \stemUp c'16 | % 211
    \stemUp c,8 \stemUp c'8 r8 \stemUp cis,8 \stemUp cis'8 r8 r2 | % 212
    R1 \pageBreak | % 213
    R1 | % 214
    \stemDown gis4 -- _\ff ^\markup{ \bold\small {a. 2} } \stemDown gis'4
    \stemDown a,4 -- \stemDown a'4 \stemUp d,,4 -- \stemUp d'4 \stemUp
    c,4 -- \stemUp c'4 | % 215
    \stemUp d,4 -- \stemUp d'4 \stemUp a,4 -- \stemUp a'4 \stemUp c,4 --
    \stemUp c'4 \stemUp b,4 -- \stemUp b'4 | % 216
    \stemUp e,4 -- _\markup{ \italic {dim. un poco} } \stemUp e'4
    \stemDown a,4 -- \stemDown a'4 \stemUp d,,4 -- \stemUp d'4 \stemDown
    g,4 -- \stemDown g'4 \break | % 217
    \stemUp b,,4 -- \stemUp b'4 \stemUp e,4 -- \stemUp e'4 \stemUp bes,4
    ( \stemUp bes'4 \stemUp e,8 ) \stemUp e'8 r8 | % 218
    \stemUp gis4 -- _\f \stemUp a4 -- \stemUp d,,4 -- _\f \stemUp d'4
    \stemUp c,4 -- \stemUp c'4 | % 219
    \stemUp d,4 -- \stemUp d'4 \stemUp a,4 -- \stemUp a'4 \stemUp c,4 --
    \stemUp c'4 \stemUp b,4 -- \stemUp b'4 | \barNumberCheck #220
    r4 \stemUp a,4 -- _\markup{ \italic {dim.} } \stemUp a'4 r4 \stemUp
    g,4 -- \stemUp g'4 \pageBreak | % 221
    r4 \stemUp e,4 -- \stemUp e'4 r4 \stemUp e,4 -- \stemUp e'4 | % 222
    r4 \stemUp e,4 -- \stemUp e'4 r4 \stemUp e,4 -- \stemUp e'4 | % 223
    r4 \stemUp e,4 ~ _\p \stemUp e'4 ~ \stemUp e,8 \stemUp e'8 r8 r4 | % 224
    R1*2 \break | % 226
    R1*5 \break | % 231
    R1*6 \pageBreak | % 237
    R1 | % 238
    r2 r4 _\mp \stemUp bis8 ( -. ^\mp \stemUp cis8 ) -. | % 239
    \stemUp e8 ( -> _\markup{ \italic {cresc.} } \stemUp dis8 ) \stemUp
    cisis16 ( \stemUp dis16 \stemUp e16 \stemUp cisis16 ) \stemUp e8 (
    -> \stemUp dis8 ) \stemUp cisis8 ( -. \stemUp dis8 ) -. |
    \barNumberCheck #240
    \stemUp fis8 ( -> \stemUp e8 ) \stemUp dis16 ( \stemUp e16 \stemUp
    fis16 \stemUp e16 ) \stemUp gis8 ( -> \stemUp fis8 ) \stemUp eis16 (
    \stemUp fis16 \stemUp gis16 \stemUp fis16 ) | % 241
    \stemUp a8 ( \stemUp gis8 ) \stemUp fisis16 ( \stemUp gis16 \stemUp
    a16 \stemUp fisis16 ) \stemUp a8 ( _ "" _\markup{ \italic {cresc.}
        } \stemUp gis8 ) \stemUp fisis16 ( \stemUp gis16 \stemUp a16
    \stemUp gis16 ) \pageBreak | % 242
    \stemUp b16 ( \stemUp a16 ) \stemUp a8 \stemUp cis16 ( \stemUp b16
    \stemUp b8 ) \stemUp d16 ( \stemUp cis16 ) \stemUp cis8 \stemUp bis16
    ( \stemUp cis16 \stemUp d16 \stemUp cis16 ) | % 243
    \stemUp e,16 ( _\ff \stemUp e'16 \stemUp d,16 ) \stemUp d'16 \stemUp
    d,8 \stemUp d'8 \stemUp cis,16 ( \stemUp cis'16 \stemUp d,16 \stemUp
    d'16 \stemUp e,16 \stemUp e'16 \stemUp d,16 ) \stemUp d'16 \stemDown
    f,16 ( \stemDown f'16 \stemDown e,16 ) \stemDown e'16 \stemDown e,8
    \stemDown e'8 \stemUp dis,16 ( \stemUp dis'16 \stemUp e,16 \stemUp
    e'16 \stemUp f,16 \stemUp f'16 \stemUp e,16 ) \stemUp e'16 | % 244
    \stemDown g,16 ( \stemDown g'16 \stemDown f,16 ) \stemDown f'16
    \stemDown f,8 \stemDown f'8 \stemDown a,16 ( \stemDown a'16
    \stemDown g,16 ) \stemDown g'16 \stemDown g,8 \stemDown g'8
    \stemDown bes,16 ( \stemDown bes'16 \stemDown a,16 ) \stemDown a'16
    \stemDown a,8 \stemDown a'8 r4 | % 245
    r4 r16 \stemDown a,16 ( _\fff \stemDown a'16 \stemDown gis,16
    \stemDown gis'16 \stemDown a,16 ) \stemDown a'16 \stemDown bes,16 (
    \stemDown bes'16 \stemDown a,16 \stemDown a'16 \stemDown a,8 )
    \stemDown a'8 r4 \pageBreak | % 246
    r4 r16 \stemDown a,16 ( \stemDown a'16 \stemDown gis,16 \stemDown
    gis'16 \stemDown a,16 ) \stemDown a'16 \stemDown bes,16 ( \stemDown
    bes'16 \stemDown a,16 ) \stemDown a'16 \stemDown a,8 \stemDown a'8
    \stemDown a,16 ( \stemDown a'16 \stemDown g,16 ) \stemDown g'16
    \stemDown g,8 \stemDown g'8 | % 247
    \stemDown bes,16 ( \stemDown bes'16 \stemDown a,16 ) \stemDown a'16
    \stemDown a,8 \stemDown a'8 \stemUp d,,16 ( \stemUp d'16 \stemUp
    cis,16 ) \stemUp cis'16 \stemUp cis,8 \stemUp cis'8 \stemUp e,16 (
    \stemUp e'16 \stemUp d,16 ) \stemUp d'16 \stemUp d,8 \stemUp d'8
    \stemUp a16 ( \stemUp g16 ) \stemUp g8 | % 248
    \stemUp bes16 ( \stemUp a16 \stemUp g16 \stemUp f16 ) \stemUp e16 (
    \stemUp f16 \stemUp e16 \stemUp d16 ) \stemUp cis16 ( \stemUp bes'16
    \stemUp a16 \stemUp gis16 \stemUp a8 ) r8 | % 249
    r4 \stemDown e'8 _\ff \stemDown a8 \stemDown f8 \stemDown a8
    \stemDown g4 -> \stemDown a4 \stemDown f8 \stemDown a8 r8 |
    \barNumberCheck #250
    r4 \stemDown e8 \stemDown a8 \stemDown f8 \stemDown a8 \stemDown g4
    -> \stemDown a4 \stemDown f8 \stemDown a8 r8 | % 251
    r4 \stemDown g8 \stemDown c8 \stemDown a8 \stemDown c8 \stemDown bes4
    -> \stemDown c4 \stemDown a8 \stemDown c8 r8 \break | % 252
    r4 \stemDown g8 \stemDown c8 \stemDown a8 \stemDown c8 \stemDown bes4
    -> \stemDown c4 \stemDown a8 \stemDown c8 r8 | % 253
    r4 \stemDown e,8 \stemDown a8 \stemDown f8 \stemDown b8 \stemDown
    fis8 ( -> \stemDown c'8 \stemDown gis8 ) \stemDown b8 r4 | % 254
    r4 \stemUp a16 ( \stemUp b16 ) \stemUp c16 ( \stemUp a16 ) \stemUp c8
    ( -> \stemUp b8 ) r4 | % 255
    r4 r8 \stemDown d,8 _\ff \stemDown gis8 r8 \stemDown e8 \stemDown a8
    r4 | % 256
    r4 r8 \stemDown d,8 \stemDown a'8 r8 \stemDown d,8 \stemDown g8 r4
    \pageBreak | % 257
    r4 r8 \stemDown c,8 \stemDown f8 r8 \stemDown d8 \stemDown g8 r4 | % 258
    r4 r8 \stemDown c,8 \stemDown g'8 r8 \stemDown c,8 \stemDown f8 r4 | % 259
    r2 r4 \stemUp es,4 ~ _ "" _\markup{ \italic {cresc.} } \stemUp es'4
    ~ | \barNumberCheck #260
    \stemUp es,4 \stemUp es'4 \stemUp es,4 ( \stemUp es'4 \stemUp d,4 )
    \stemUp d'4 \stemUp fis,,8 ( _\mf \stemUp fis'8 \stemUp gis,8
    \stemUp gis'8 | % 261
    \stemUp a,8 \stemUp a'8 \stemUp fis,8 ) \stemUp fis'8 \stemUp a,8 (
    _\markup{ \italic {cresc.} } \stemUp a'8 \stemUp b,8 \stemUp b'8
    \stemUp c,8 \stemUp c'8 \stemUp a,8 ) \stemUp a'8 \stemUp c,8 (
    \stemUp c'8 \stemUp d,8 \stemUp d'8 | % 262
    \stemUp es,8 \stemUp es'8 \stemUp c,8 ) \stemUp c'8 \stemDown es,8 (
    \stemDown es'8 \stemDown f,8 \stemDown f'8 \stemDown ges,8 \stemDown
    ges'8 \stemDown es,8 ) \stemDown es'8 \stemDown fis,8 _\ff \stemDown
    fis'8 \stemDown gis,8 \stemDown gis'8 \pageBreak | % 263
    \stemDown a,8 \stemDown a'8 r8 \stemDown fis,8 \stemDown fis'8 r8 r4
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis,8 \stemDown fis'8 \stemDown gis,8 \stemDown gis'8
        \stemDown a,8 }
    \stemDown a'8*2/3 | % 264
    \stemDown a,8 \stemDown a'8 r8 \stemDown fis,8 \stemDown fis'8 r8 r4
    \stemDown a,8 \stemDown a'8 \stemDown b,8 \stemDown b'8 | % 265
    \stemDown c,8 \stemDown c'8 r8 \stemDown a,8 \stemDown a'8 r8 r4
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a,8 \stemDown a'8 \stemDown b,8 \stemDown b'8
        \stemDown c,8 }
    \stemDown c'8*2/3 | % 266
    \stemDown c8 ^\markup{ \bold\small {a. 2} } r8 \stemDown a8 r8 r4
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown b8 \stemDown c8 }
    | % 267
    \stemDown c16 ( _\fff \stemDown b16 \stemDown c16 \stemDown b16
    \stemDown c16 \stemDown b16 \stemDown c16 \stemDown b16 ) \stemDown
    c16 ( \stemDown b16 \stemDown c16 \stemDown gis16 ) \stemDown a16 (
    \stemDown gis16 \stemDown a16 \stemDown f16 ) \pageBreak | % 268
    \stemDown ges16 ( \stemDown f16 \stemDown ges16 \stemDown f16
    \stemDown ges16 \stemDown f16 \stemDown ges16 \stemDown f16 )
    \stemDown ges16 ( \stemDown f16 \stemDown ges16 \stemDown d16 )
    \stemDown es16 ( \stemDown d16 \stemDown es16 \stemDown b'16 ) | % 269
    \stemDown c16 ( \stemDown b16 \stemDown c16 \stemDown b16 \stemDown
    c16 \stemDown b16 \stemDown c16 \stemDown gis16 ) \stemDown a16 (
    \stemDown gis16 \stemDown a16 \stemDown gis16 \stemDown a16
    \stemDown gis16 \stemDown a16 \stemDown f16 | \barNumberCheck #270
    \stemDown ges8 ) r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown ges,8 \stemDown ges'8 \stemDown ges,8 \stemDown ges'8
        \stemDown ges,8 ~ }
    \stemDown ges'8*2/3 ~ \stemDown ges,8 \stemDown ges'8 \stemDown ges,8
    -> \stemDown ges'8 r4 | % 271
    R1 | % 272
    r2 \stemUp a,,4. ^\markup{ \bold\small {a. 2} } _\ff \stemUp b8
    \pageBreak | % 273
    \stemUp c2. ( \stemUp b8 ) r8 | % 274
    \stemUp c8 _\ff ^\markup{ \bold\small {a. 2} } r8 \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 ~ }
    \stemUp c8 \stemUp c8 -> r4 | % 275
    r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 }
    r4 r8 \stemUp c8 -> | % 276
    r4 \stemUp c8 -> r8 r2 | % 277
    R1*4 | % 281
    b1 ~ _\ff d1 ~ | % 282
    b1 d1 | % 283
    a'1 | % 284
    \stemUp bes4. ( -> \stemUp a8 ) \stemUp a4 \stemUp e4 _\fff
    \pageBreak | % 285
    a1 ~ d1 ~ | % 286
    a1 d1 | % 287
    a,1 ~ a'1 ~ | % 288
    a,1 a'1 | % 289
    cis,1 ~ g'1 ~ | \barNumberCheck #290
    cis,1 g'1 | % 291
    a,1 ~ ^\markup{ \bold\small {a. 2} } | % 292
    a1 | % 293
    \stemUp d2 \stemUp cis2 ~ | % 294
    cis1 | % 295
    \stemUp bes2 \stemUp a2 ~ | % 296
    a1 | % 297
    R1*2 | % 299
    f1 ~ _\ffff _\> | \barNumberCheck #300
    \stemUp f2 ~ \stemUp f8 _\! _\p r8 r4 | % 301
    e1 ~ _\ff _\> \break | % 302
    e1 ~ | % 303
    e1 ~ | % 304
    \stemUp e8 _\! _\pp r8 r4 r2 ^\fermata \bar "||"
    \pageBreak | % 305
    \key d \major R1 | % 306
    r4 \stemUp fis4 -- _\pp \stemUp fis'4 \stemUp g,8 ( \stemUp g'8
    \stemUp a,8 \stemUp a'8 \stemUp b,8 \stemUp b'8 \stemUp cis,8 )
    \stemUp cis'8 | % 307
    \stemUp d,4 -- _\< \stemUp d'4 \stemDown e,8. \stemDown e'8.
    \stemDown f,16 \stemDown f'16 \stemDown fis,4 -- _\! _\> \stemDown
    fis'4 \stemDown g,8 ( \stemDown g'8 \stemDown fis,8 ) \stemDown fis'8
    | % 308
    \stemUp a,,4 -- _\! \stemUp a'4 \stemUp fis,4 -- \stemUp fis'4
    \stemUp e4 -- \stemUp e'4 \stemDown g,4 -- \stemDown g'4 | % 309
    \stemDown fis,4 -- _\< \stemDown fis'4 \stemUp e,8 ( \stemUp e'8
    \stemUp d,8 ) \stemUp d'8 \stemDown a2 _\! _\mp \stemDown c2 |
    \barNumberCheck #310
    \stemDown g2 _\markup{ \italic {poco cresc.} } \stemDown g'2 \stemUp
    g,2 \stemUp bes2 \pageBreak | % 311
    \stemDown fis2 \stemDown fis'2 \stemUp b,2 ( _\mf _\> | % 312
    \stemUp a8 ) _\! _\< r8 r4 \stemDown b4.. ( _\! _\mf _\> \stemDown
    b'4.. \stemDown a,16 ) \stemDown a'16 | % 313
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a,16 -. _\! _\p _\< \stemUp a'16 \stemUp a,,16 ( \stemUp
        a'16 \stemUp bes,16 }
    \stemUp bes'16*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemUp b,16 \stemUp b'16 \stemUp c,16 \stemUp c'16 \stemUp cis,16
        ) }
    \stemUp cis'16*2/3 \stemDown d,32 ( \stemDown d'32 \stemDown dis,32
    \stemDown dis'32 \stemDown e,32 \stemDown e'32 \stemDown f,32
    \stemDown f'32 \stemDown fis,32 \stemDown fis'32 \stemDown g,32
    \stemDown g'32 \stemDown gis,32 \stemDown gis'32 \stemDown a,32 )
    \stemDown a'32 \stemDown a,4 -- _\! _\fff \stemDown a'4 \stemDown g,8.
    ( \stemDown g'8. \stemDown fis,16 ) \stemDown fis'16 | % 314
    \stemDown fis,4 ( -> \stemDown fis'4 \stemUp e,4 ) \stemUp e'4
    \stemDown g,4 -- \stemDown g'4 \stemDown fis,8. ( \stemDown fis'8.
    \stemDown e,16 ) \stemDown e'16 | % 315
    \stemUp e,4 ( -> \stemUp e'4 \stemUp d,4 ) \stemUp d'4 r8 \stemUp
    fis,8 ( _\> \stemUp fis'8 \stemUp e,8 \stemUp e'8 \stemUp d,8 )
    \stemUp d'8 | % 316
    \stemUp a8 ( _\! _\mf _\< \stemUp fis8 \stemUp d8 \stemUp fis8 )
    \stemUp b4.. ( _\! _\ff _\> \stemUp a16 ) \pageBreak | % 317
    \stemUp a2 _\! _\mf \stemUp a2 | % 318
    \stemUp e'2 \stemUp g,2 | % 319
    \stemUp d'2 \stemUp d2 | \barNumberCheck #320
    \stemUp fis,2 \stemUp d'2 r8 \stemUp e,4. -> \stemUp g4. | % 321
    \stemUp fis2 \stemUp a2 \stemUp a,2 ( _\mf | % 322
    \stemUp g8 ) r8 r4 \stemUp g2 ( | % 323
    \stemUp fis8 ) r8 r4 r2 | % 324
    r2 \stemUp e2 ( _\mf _\> | % 325
    \stemUp a8 ) _\! _\p r8 r4 r8 \stemUp fis''8 ( ^\markup{ \italic
        {solo} } _\ppp \stemUp e8 \stemUp d8 ) \break | % 326
    \stemUp b8 ( ^ "I." _\< \stemUp a8 \stemUp fis8 \stemUp a8 )
    \stemDown d4. ( _\! _\p _\> \stemDown b8 ) | % 327
    \stemUp a2 ~ _\! _\ppp \stemDown a8 \stemDown fis'8 ( \stemDown e8
    \stemDown d8 ) | % 328
    \stemUp a8 ( _\< \stemUp fis8 \stemUp d8 \stemUp fis8 ) \stemDown b4..
    ( _\! _\p _\> \stemUp a16 ) | % 329
    \stemUp a2 _\! _\ppp _\< \stemDown a'4 -> _\! _\pp ^\markup{ \italic
        {dolcissimo, ma espressivo} } \stemDown g8. ( \stemDown fis16 )
    | \barNumberCheck #330
    \stemDown fis4 ( -> \stemDown e4 ) \stemDown g4 -- \stemDown fis8. (
    \stemDown e16 ) | % 331
    \stemUp e4 ( -> \stemUp d4 ) r8 _ "" \stemUp fis8 ( _\pp _\>
    \stemUp e8 \stemUp d8 ) | % 332
    \stemUp a8 ( _\! _\pppp _\< \stemUp fis8 \stemUp d8 \stemUp fis8 )
    \stemUp b4.. ( _\! _\pp _\> \stemUp a16 ) | % 333
    \stemUp fis,2 _\! _\pppp _\< \stemUp a'2 \stemUp cis,4.. -> _\! _\pp
    _\> \stemUp b'4.. \stemUp d,16 \stemUp a'16 \pageBreak | % 334
    \stemUp d,2 _\! _\pppp _\< \stemUp a'2 \stemUp cis,4.. -> _\! _\pp
    _\> \stemUp b'4.. \stemUp d,16 \stemUp a'16 \bar "||"
    \stemUp d,4 ~ _\! _\pppp \stemUp a'4 ~ \stemUp d,8 \stemUp a'8 r8 r2
    | % 336
    R1*4 | \barNumberCheck #340
    \stemUp d,2 ^\markup{ \italic {cantabile} } _\p \stemUp d'2 \stemUp
    d,4. _\< \stemUp d'4. \stemUp e,8 \stemUp e'8 | % 341
    \stemDown g,8 ( _\! _\mf _\> \stemDown g'8 \stemDown fis,8 ~
    \stemDown fis'8 ~ \stemDown fis,2 ~ \stemDown fis'2 ~ \stemDown fis,8
    ) \stemDown fis'8 r8 _\! | % 342
    \stemUp d,2 _\p \stemUp d'2 \stemUp d,4. _\< \stemUp d'4. \stemUp e,8
    \stemUp e'8 \pageBreak | % 343
    fis,1 _\! _\mf _\> fis'1 | % 344
    \stemUp d,2. ~ _\! _\p \stemUp a'2. ~ \stemUp d,8 \stemUp a'8
    \stemUp d,8 \stemUp a'8 | % 345
    R1*10 \bar "|."
    _\> _\! }

PartPFourVoiceTwo =  \relative d' {
    \clef "treble" \time 4/4 \key f \major \transposition a s1*11 \break
    s4*11 \stemDown d4 | % 15
    \stemDown g,2 ~ \stemDown g8 s8*27 \bar "||"
    s1*5 \pageBreak s2. \stemDown f16 ( \stemDown e16 \stemDown f16
    \stemDown g16 ) | % 25
    \stemDown gis4 ( \stemDown a8 ) s8*23 r8 \stemDown g8 ~ \stemDown g8
    \stemDown bes8 ~ \stemDown bes8 r8 s1 | \barNumberCheck #30
    \time 2/4  s2 \break | % 31
    \time 4/4  s1*6 \break s1*7 \pageBreak s1*6 \break s1*4 \pageBreak
    s1*3 | % 57
    \stemDown fis'8 -- \stemDown fis'8 -- \stemDown ais,8 -- s8*13
    \break s1*3 | % 62
    r2 r16 \stemDown d16 -. \stemDown d16 -. \stemDown d16 -. \stemDown
    d16 -. \stemDown d16 -. \stemDown b16 -. \stemDown b16 -. | % 63
    \stemDown a8 -- \stemDown dis,8 -- \stemDown cis8 -- s8. \stemDown
    g'16 -. \stemDown g16 -. \stemDown g16 -. \stemDown g16 -. \stemDown
    g16 -. \stemDown e16 -. \stemDown e16 -. \pageBreak | % 64
    \stemDown d8 -- \stemDown b8 -- \stemDown a8 -- s8. \stemDown d'16
    -. \stemDown d16 -. \stemDown d16 -. \stemDown d16 ( \stemDown fis16
    ) \stemDown d16 -. \stemDown d16 -. | % 65
    \stemDown cis8 -- \stemDown g8 -- \stemDown f8 -- s8. \stemDown b16
    -. \stemDown b16 -. \stemDown b16 -. \stemDown b16 -. \stemDown b16
    -. \stemDown gis16 -. \stemDown gis16 -. | % 66
    \stemDown fis8 -- \stemDown d8 -- \stemDown cis8 -- s8*21 \pageBreak
    s1. r4 r16 \stemDown es''16 ( \stemDown d16 \stemDown c16 ) | % 71
    \stemDown as16 \stemDown g16 \stemDown f16 \stemDown es16 \stemDown
    d16 \stemDown c16 \stemDown as16 \stemDown g16 r4 r16 \stemDown es''16
    ( \stemDown d16 \stemDown c16 ) | % 72
    \stemDown as16 \stemDown g16 \stemDown f16 \stemDown es16 \stemDown
    d16 \stemDown c16 \stemDown as16 \stemDown g16 r4 \stemDown c'16 (
    \stemDown es16 \stemDown d16 \stemDown c16 ) | % 73
    r4 \stemDown c,16 ( \stemDown es16 \stemDown d16 \stemDown c16 ) r4
    \stemDown c'16 ( \stemDown es16 \stemDown d16 \stemDown c16 )
    \pageBreak | % 74
    r4 \stemDown c,16 ( \stemDown es16 \stemDown d16 \stemDown c16 )
    s1*2 r2 | % 77
    r2 s2 \break s1*5 \pageBreak s1*6 \bar "||"
    s1*4 | % 93
    \stemDown f,,8 s4. \stemDown fis2 \break | % 94
    \stemDown g2 \stemDown e2 _\> | % 95
    \stemDown f2 \stemDown a'2 ~ | % 96
    \stemDown a8 s8*7 | % 97
    r2 \stemDown fis,2 _\mf | % 98
    \stemDown g2 \stemDown e2 _\> | % 99
    \stemDown f2 \stemDown a'2 ~ | \barNumberCheck #100
    \stemDown a8 s8*7 \bar "||"
    s1*2 \pageBreak s1*5 \break s1*4 \pageBreak s1*4 \break s1*4
    \pageBreak s1*5 \break s1*5 \bar "||"
    \time 12/8  s1*3 \pageBreak s1*9 \pageBreak s1*6 \bar "||"
    s1. | % 143
    \numericTimeSignature\time 4/4  s1*2 \break s1 | % 146
    \stemDown f4 ( \stemDown a4 ) \stemDown f4 ( \stemDown fis4 ) s1*9
    \pageBreak s1*5 \bar "||"
    \key c \major s4*13 \stemDown bes,8 s8*5 \pageBreak s1*2 | % 167
    \stemDown a8 s8 \stemDown bes8 s2 \stemDown bes8 s1*4 \pageBreak
    s4*19 r4 | % 177
    R1 \pageBreak | % 178
    \stemDown d''8 s8*17 \stemDown es,8 -. \stemDown c8 ( \stemDown bes8
    ) \stemDown c8 ~ \stemDown c8 \stemDown g'8 ~ | % 181
    \stemDown g4. \stemDown g8 ~ \stemDown g4. \stemDown g8 ~ | % 182
    \stemDown g8 s8*7 \break s1*5 \pageBreak s1*4 \break s1*4 \pageBreak
    s1*5 \break s1*6 \pageBreak s1*6 \pageBreak s1*4 \break s1 | % 218
    r2 s2*5 \pageBreak s1*5 \break s1*5 \break s1*6 \pageBreak s1.
    \stemDown e,,4 ~ -> \stemDown e8. \stemDown e16 | % 239
    \stemDown a2. \stemDown fis4 | \barNumberCheck #240
    \stemDown cis'2 \stemDown bis2 | % 241
    \stemDown cis2 \stemDown b4.. \stemDown b16 \pageBreak | % 242
    \stemDown fis'8 r8 \stemDown eis8 r8 \stemDown fis8 r8 r4 s1*3
    \pageBreak s4*7 \stemDown a16 ( \stemDown g16 ) \stemDown g8 | % 248
    \stemDown bes16 ( \stemDown a16 \stemDown g16 \stemDown f16 )
    \stemDown e16 ( \stemDown f16 \stemDown e16 \stemDown d16 )
    \stemDown cis8 r8 r4 s1*3 \break s4*9 \stemDown e'8 \stemDown f8
    \stemDown fis8 ( -> \stemDown gis8 ) s4*9 \pageBreak s1*6 \pageBreak
    s1*5 \pageBreak s1*5 \pageBreak s1*10 | % 283
    \stemDown f,2 \stemDown e2 ~ | % 284
    \stemDown e2. \stemDown e4 \pageBreak s1*17 \break s1*3 \bar "||"
    \pageBreak | % 305
    \key d \major s1*6 \pageBreak s2 \stemDown b2 | % 312
    \stemDown a2 s2*7 | % 316
    \stemDown a8 ( \stemDown fis8 \stemDown d'8 \stemDown fis,8 )
    \stemDown b4.. ( \stemDown a16 ) \pageBreak | % 317
    \stemDown a2 \stemDown fis'2 | % 318
    \stemDown g2 \stemDown e2 | % 319
    \stemDown fis2 \stemDown f4 ( \stemDown g8 \stemDown f8 ) s1.
    \stemDown fis,2 | % 322
    \stemDown g2 \stemDown e2 | % 323
    \stemDown fis2 \stemDown f4 ( \stemDown g8 \stemDown f8 | % 324
    \stemDown fis8 ) \stemDown fis4. \stemDown g2 ( | % 325
    \stemDown fis8 ) s4. r2 \break s1*5 | % 331
    r2 \stemDown fis2 | % 332
    \stemDown fis2 \stemDown g2 s1 \pageBreak s1 \bar "||"
    s1*8 \pageBreak s1*2 | % 345
    d'1 s1*9 \bar "|."
    }

PartPFiveVoiceOne =  \relative e, {
    \clef "bass" \time 4/4 \key d \major | % 1
    r2 r4 \stemUp e8 ( ^ "I." ^\markup{ \italic {solo} } _\pp _\<
    \stemUp fis8 ) | % 2
    \stemUp g4 ( _\! _\> \stemUp fis2 ) _\! _\< \stemUp fis8 ( _\! _\p
    _\< \stemUp g8 ) | % 3
    \stemUp a4 ( _\! _\> \stemUp g2 ) _\! _\< \stemUp g8 ( _\! _\mp _\<
    \stemUp a8 ) | % 4
    \stemUp b4 ( _\! _\> \stemUp ais2. ) _\! _\< | % 5
    b1 ~ _\! _\sf _\> | % 6
    \stemUp b8 _\! _\p r8 r4 r2 | % 7
    r2 r4 \stemUp e,8 ( _\pp _\< \stemUp fis8 ) | % 8
    \stemUp g4 ( _\! _\> \stemUp fis2 ) _\! _\< \stemUp fis8 ( _\! _\p
    _\< \stemUp g8 ) | % 9
    \stemUp a4 ( _\! _\> \stemUp g2 ) _\! _\< \stemUp g8 ( _\! _\mp _\<
    \stemUp a8 ) | \barNumberCheck #10
    \stemUp b4 ( _\! _\> \stemUp a2 ) _\! _\< \stemUp g4 -- | % 11
    e1 ~ _\! _\sf _\> \break | % 12
    \stemUp e8 _\! _\p r8 r4 r2 | % 13
    R1 | % 14
    r2 r4 \stemUp gis4 _\p _\< | % 15
    \stemUp ais2 ~ _\! _\mf _\> \stemUp ais8 r8 _\! r4 | % 16
    R1*3 \bar "||"
    R1*5 \pageBreak | % 24
    R1*4 | % 28
    r4 r8 \stemDown <g b'>8 ~ ~ _\p \stemUp <g b'>8 \stemUp <e b'>8 ~ ~
    \stemUp <e b'>8 r8 | % 29
    R1 | \barNumberCheck #30
    \time 2/4  R2 \break | % 31
    \time 4/4  R1*6 \break | % 37
    R1*6 | % 43
    r8 \stemUp cis'8 ( _\pp ^ "I." \stemUp b8 \stemUp a8 \stemUp g8 )
    \stemUp fis8 ( \stemUp e8 ) r8 \pageBreak | % 44
    R1*3 | % 47
    r8 \stemDown gis'8 ( _\p \stemDown fis8 \stemDown e8 \stemUp d8 )
    \stemUp cis8 \stemUp b8 r8 | % 48
    R1*2 \break | \barNumberCheck #50
    r2 r8 \stemDown cis8 ( ^ "I." _\mp _\< \stemDown e8 \stemDown gis8 )
    | % 51
    \stemDown bis8 ( -. \stemDown dis8 ) -. \stemDown gis4 ~ _\! _\>
    \stemDown gis8 r8 _\! r4 | % 52
    r2 r8 \stemDown cis,,8 ( _\mp _\< \stemDown e8 \stemDown gis8 ) | % 53
    \stemDown bis8 ( -. \stemDown dis8 ) -. \stemDown gis4 ~ _\! _\>
    \stemDown gis8 r8 _\! r4 \pageBreak | % 54
    R1*4 | % 58
    r2 r8 \stemUp gis,,8 ( _\mp ^ "I." _\< \stemUp b8 \stemUp dis8 )
    \break | % 59
    \stemDown fisis8 ( -. \stemDown ais8 ) -. \stemDown dis4 ~ _\! _\>
    \stemDown dis8 r8 _\! r4 | \barNumberCheck #60
    r4 r8 r16 \stemUp dis,,16 -. _\mp \stemUp dis8 -. \stemUp gis8 ( _\<
    \stemUp b8 \stemUp dis8 ) | % 61
    \stemDown fisis8 ( -. \stemDown ais8 ) -. \stemDown dis4 ~ _\! _\>
    \stemDown dis8 r8 _\! r4 | % 62
    r4 r8 r16 \stemUp dis,,16 _\mp \stemUp dis8 r8 r4 | % 63
    R1 \pageBreak | % 64
    r2 r16 \stemDown <fis' b>16 -. _\mp _\< \stemDown <fis b>16 -.
    \stemDown <fis b>16 -. \stemDown <fis b>16 ( \stemDown <dis' fis>16
    ) \stemDown <b dis>16 -. \stemDown <b dis>16 -. | % 65
    \stemDown <ais cisis>8 _\! r8 r4 r2 | % 66
    r2 _\! _\> \stemUp dis,4 ~ _\f \stemUp dis8 r8 | % 67
    \stemUp eis,2 ( -> _\f \stemUp fis8 ) r8 r4 | % 68
    r2 \stemUp b'8 -> \stemUp gis8 -> \stemUp a8 -> r8 \pageBreak | % 69
    \stemUp gis,2 ( -> \stemUp a8 ) r8 r4 | \barNumberCheck #70
    r2 \stemUp d'8 -> \stemUp b8 -> \stemUp c8 -> r8 | % 71
    \stemUp a'4 -> \stemUp c,4 -> \stemUp d8 -> \stemUp b8 -> \stemUp c8
    -> r8 | % 72
    \stemUp a'4 -> \stemUp c,4 -> \stemUp d8 -> \stemUp b8 -> \stemUp c8
    -> r8 | % 73
    \stemUp c4 ~ \stemUp c8 r8 \stemUp d8 -> \stemUp b8 -> \stemUp c8 ->
    r8 \pageBreak | % 74
    \stemDown <a c>4 ~ ~ \stemDown <a c>8 r8 \stemDown <a c>4 ~ -> ~
    \stemDown <a c>8 r8 | % 75
    \stemDown <a c>4 ~ -> ~ \stemDown <a c>8 r8 \stemDown <g a>4 ~ -> ~
    \stemDown <g a>8 r8 | % 76
    \stemDown <g a>4 ~ -> ~ \stemDown <g a>8 r8 \stemDown <g a>4 ~ -> ~
    _\f \stemDown <g a>8 r8 | % 77
    \stemDown <g a>4 ~ -> ~ \stemDown <g a>8 r8 \stemUp <e, a>4 ( -> ~
    _\mf \stemUp <es a>8 ) r8 \break | % 78
    \stemUp <e a>4 ( -> ~ \stemUp <es a>8 ) r8 r4 \stemUp <es a>4 ~ ~
    _\mp | % 79
    \stemUp <es a>4 ~ ~ _\> \stemUp <es a>8 r8 _\! r4 \stemUp <es a>4 ~
    ~ _\p | \barNumberCheck #80
    \stemUp <es a>8 r8 r4 r2 | % 81
    R1*2 \pageBreak | % 83
    R1*6 \bar "||"
    R1 | \barNumberCheck #90
    \stemUp a2 _\pp ^ "I." _\< \stemUp gis2 _\! _\mp _\> | % 91
    a1 _\! _\pp | % 92
    \stemUp a2 _\pp _\< \stemUp a2 _\! _\mp _\> | % 93
    \stemUp a2 _\! _\pp _\< \stemUp a2 _\! _\mf \break | % 94
    \stemUp b2 \stemUp g2 _\> | % 95
    \stemUp a2 _\! _\p _\< \stemUp gis2 _\! _\mf _\> | % 96
    \stemUp a2 _\! _\p _\< \stemUp a2 _\! _\mf _\> | % 97
    \stemUp a2 _\! _\p _\< \stemUp a2 _\! _\mf | % 98
    \stemUp b2 \stemUp g2 _\> | % 99
    \stemUp a2 _\! _\p _\< \stemUp gis2 _\! _\mf _\> | \barNumberCheck
    #100
    \stemUp a2 _\! _\p _\< \stemUp a2 ~ _\! _\mf _\> \bar "||"
    \stemUp a8 _\! _\p r8 r4 r2 | % 102
    \stemUp b4 ~ _\p _\< \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 ( \stemUp cis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 ) \stemDown d8 ( -- \stemDown e8 -- }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 -- \stemDown g8 -- \stemDown a8 ) -- }
    \pageBreak | % 103
    \stemDown b4 ( ~ -> _\! _\> \stemDown b16 \stemDown a16 \stemDown g16
    \stemDown fis16 \stemDown e8 ) r8 _\! r4 | % 104
    \stemDown e4 ~ _\p _\< \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 ( \stemDown fis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 ) \stemDown g8 ( -- \stemDown a8 ) -- }
    \stemDown b16 ( \stemDown cis16 \stemDown d16 \stemDown e16 ) | % 105
    \stemDown fis4 ( ~ -> _\! _\> \stemDown fis16 \stemDown c16
    \stemDown a16 \stemDown g16 \stemDown fis8 ) r8 _\! r4 | % 106
    R1*2 \break | % 108
    R1*2 | \barNumberCheck #110
    \stemUp fis,4 ~ _\p _\< \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis8 \stemUp fis8 ( \stemUp gis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ) \stemUp a8 ( -- \stemUp b8 -- }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis8 -- \stemUp d8 -- \stemUp e8 ) -- }
    | % 111
    \stemDown fis4 ( ~ -> _\! _\> \stemDown fis16 \stemDown e16
    \stemDown d16 \stemDown cis16 \stemUp b8 ) r8 _\! r4 \pageBreak | % 112
    \stemUp b4 ~ _\p _\< \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 ( \stemUp cis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 ) \stemDown d8 ( -- \stemDown e8 ) -- }
    \stemDown fis16 ( \stemDown gis16 \stemDown a16 \stemDown b16 ) | % 113
    \stemDown bis4 ( ~ -> _\! _\> \stemDown bis16 \stemDown g16
    \stemDown e16 \stemDown d16 \stemUp cis8 ) r8 _\! r4 | % 114
    fis,1 ( ^ "II." _\mp _\< | % 115
    \stemUp b8 ) _\! _\mf r8 r4 r2 \break | % 116
    \stemUp e,2. ~ _\> \stemUp e8 r8 _\! | % 117
    R1 | % 118
    \stemUp b'4 ~ ^\markup{ \bold\small {a. 2} } _\p \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp b8 _\< \stemUp cis8 ( \stemUp dis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ) \stemDown e8 ( -- \stemDown fis8 -- }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown gis8 -- \stemDown a8 -- \stemDown ais8 ) -- }
    | % 119
    \stemDown b4 ( ~ -> _\! _\> \stemDown b16 \stemDown g16 \stemDown e16
    \stemDown b16 \stemUp g8 ) r8 _\! r4 \pageBreak | \barNumberCheck
    #120
    \stemUp b4 ~ _\più _\f _\< \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp cis8 ( \stemUp dis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ) \stemDown e8 ( -- \stemDown fis8 -- }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 -- \stemDown a8 -- \stemDown ais8 ) -- }
    | % 121
    \stemDown b4 ( ~ _\! _\f ^\markup{ \bold\small {a. 2} } \stemDown b16
    \stemDown g16 \stemDown e16 \stemDown b16 ) \stemDown e'4 ( ~
    \stemDown e16 \stemDown b16 \stemDown g16 \stemDown e16 ) | % 122
    \stemDown e2 \once \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown fis16 \stemDown e16 \stemDown fis16
        \stemDown e16 \stemDown dis16 }
    \stemDown e8 ) r8 | % 123
    \stemDown g4 ( ~ _\markup{ \italic {cresc.} } \stemUp g16 \stemUp e16
    \stemUp cis16 \stemUp g16 ) \stemDown cis'4 ( ~ \stemDown cis16
    \stemDown g16 \stemDown e16 \stemDown cis16 ) | % 124
    \stemDown d'4 ( ~ \stemDown d16 \stemDown b16 \stemDown fis16
    \stemDown d16 \stemUp a8 ) r8 r4 \break | % 125
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a'8 ( \stemDown d,8 \stemDown a8 }
    \stemUp f8 ) r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown a'8 ( \stemDown d,8 \stemDown a8 }
    \stemUp f8 ) r8 | % 126
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp g'8 ( \stemUp cis,8 \stemUp g8 }
    \stemUp e8 ) r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp g'8 ( \stemUp cis,8 \stemUp g8 }
    \stemUp e8 ) r8 | % 127
    r4 \stemDown g'4 ( _\ff \stemDown fis4 \stemDown e4 ) | % 128
    \stemDown d4 ( \stemUp cis2 ) \stemUp b4 ( | % 129
    \stemUp bes2 _\sff _\> \stemUp a4 ~ \stemUp a8 ) r8 ^\fermata _\!
    \bar "||"
    \time 12/8  r1 s2 | % 131
    r2.*2/3 r8*2/3 \stemDown <eis' gis>8 ^\markup{ \italic {pesante, non
            staccato} } _\p \stemDown <eis gis>8 \stemDown <eis gis>8
    \stemDown <eis gis>8 \stemDown <eis gis>8 s1*7/24 \pageBreak | % 132
    r8*2/3 \stemDown <fis d'>8 _\markup{ \italic {sempre} } _ ""
    \stemDown <fis d'>8 \stemDown <fis d'>8 \stemDown <fis d'>8
    \stemDown <fis d'>8 \stemDown <fis d'>8 r8*2/3 r8*2/3 r4*2/3 r8*2/3
    s4 | % 133
    r8*2/3 \stemDown <fis d'>8 \stemDown <fis d'>8 \stemDown <fis d'>8
    \stemDown <fis d'>8 \stemDown <fis d'>8 r8*2/3 \stemDown <g cis>8
    \stemDown <g cis>8 \stemDown <g cis>8 \stemDown <g cis>8 \stemDown
    <g cis>8 s1*1/12 | % 134
    r8*2/3 \stemDown <fis d'>8 _\p _\< \stemDown <fis d'>8 \stemDown
    <fis d'>8 \stemDown <fis d'>8 r8*2/3 _\! \stemDown <a c>2. _\mf
    s1*1/12 | % 135
    \stemDown <g b>8 \stemDown <g b>8 \stemDown <g b>8 \stemDown <g b>8
    \stemDown <g b>8 \stemDown <g b>8 \stemDown <g bes>2. | % 136
    \stemDown <fis a>8 _\< \stemDown <fis a>8 \stemDown <fis a>8
    \stemDown <fis a>8 \stemDown <fis a>8 \stemDown <fis a>8 \stemDown
    <fis d'>2. _\! _\sf _\> | % 137
    \stemDown <fis d'>8 _\! _\p _\< \stemDown <fis d'>8 \stemDown <fis
        d'>8 \stemDown <fis d'>8 \stemDown <fis d'>8 \stemDown <fis d'>8
    \stemDown <cis g'>2. _\! _\mf _\> \pageBreak | % 138
    r8*2/3 _\! \stemDown <fis d'>8 _\p _\< \stemDown <fis d'>8 \stemDown
    <fis d'>8 \stemDown <fis d'>8 r8*2/3 _\! \stemDown <a c>2. _\mf
    s1*1/12 | % 139
    \stemDown <g b>8 \stemDown <g b>8 \stemDown <g b>8 \stemDown <g b>8
    \stemDown <g b>8 \stemDown <g b>8 \stemDown <g bes>2. |
    \barNumberCheck #140
    \stemDown <fis a>8 _\< \stemDown <fis a>8 \stemDown <fis a>8
    \stemDown <fis a>8 \stemDown <fis a>8 \stemDown <fis a>8 \stemDown
    <fis d'>2. _\! _\sf _\> | % 141
    \stemDown <fis d'>8 _\! _\p _\< \stemDown <fis d'>8 \stemDown <fis
        d'>8 \stemDown <fis d'>8 \stemDown <fis d'>8 \stemDown <fis d'>8
    \stemDown <cis g'>2. _\! _\mf _\> \bar "||"
    r8*2/3 _\! \stemDown <d fis>8 _\mf _\> \stemDown <d fis>8 \stemDown
    <d fis>8 \stemDown <d fis>8 \stemDown <d fis>8 \stemDown d4. ( _\!
    _\mp ^\markup{ \bold\small {a. 2} } \stemDown dis4. ) s1*1/24 | % 143
    \numericTimeSignature\time 4/4  \stemDown dis4 ( \stemDown e4 )
    \stemUp b4 ( \stemUp cis4 ) | % 144
    \stemUp cis4 ( _\> \stemDown d4 ) \stemDown d4 ( _\! _\p \stemDown
    dis4 ) \break | % 145
    \stemDown e4 ( \stemDown gis4 ) \stemUp b,4 ( \stemUp cis4 ) | % 146
    \stemDown d4 ( \stemDown fis4 ) \stemDown d4 ( _\p \stemDown dis4 )
    | % 147
    \stemDown dis4 ( \stemDown e4 ) \stemUp b4 ( \stemUp cis4 ) | % 148
    \stemUp cis4 ( _\> \stemDown d4 ) \stemDown d4 ( _\! _\pp \stemDown
    dis4 ) | % 149
    \stemDown e4 ( \stemDown gis4 ) \stemUp b,4 ( \stemUp cis4 ) |
    \barNumberCheck #150
    \stemDown d4 ( \stemDown fis4 ) \stemDown d4 ( _\markup{ \italic
        {dim.} } \stemDown f4 ) | % 151
    \stemDown d4 ( \stemDown fis4 ) \stemDown d4 ( \stemDown f4 ) | % 152
    \stemDown d4 ( _\ppp \stemDown fis4 ) \stemDown d4 ( \stemDown fis4
    ) | % 153
    \stemDown d4 ( \stemDown fis4 ) r2 | % 154
    R1*2 \pageBreak | % 156
    R1*4 | \barNumberCheck #160
    r2 \stemUp b,8 ^ "I." _\pppppp \stemUp a8 ( \stemUp fis8 \stemUp d8
    ) ^\fermata \bar "||"
    \key c \major <c c'>1 ~ ~ _\ff | % 162
    <c c'>1 ~ ~ | % 163
    <c c'>1 ~ ~ | % 164
    <c c'>1 \pageBreak | % 165
    <b b'>1 ~ ~ _\markup{ \italic {sempre} } _ "" | % 166
    <b b'>1 ~ ~ | % 167
    <b b'>1 ~ ~ | % 168
    <b b'>1 | % 169
    <bes bes'>1 ~ ~ | \barNumberCheck #170
    \stemUp <bes bes'>8 \stemUp <bes bes'>8 -> \stemUp <bes bes'>8 ->
    \stemUp <bes bes'>8 -> \stemUp bes'8 \stemUp a8 r4 | % 171
    R1 \pageBreak | % 172
    R1*4 | % 176
    r2 r4 r8 \clef "tenor" \stemDown <a' a'>8 ~ ~ _\f | % 177
    \stemDown <a a'>4. \stemDown <a a'>8 ~ ~ \stemDown <a a'>4.
    \stemDown <a a'>8 ~ ~ \pageBreak | % 178
    \stemDown <a a'>8 r8 r4 r2 | % 179
    R1 | \barNumberCheck #180
    r2 r8 \stemDown fis'8 ( ^ "I." _\mf \stemDown e8 ) r8 | % 181
    R1 | % 182
    r2 r4 \clef "bass" \stemUp <b,, b'>8 _\ff \stemUp <cis cis'>8 \break
    | % 183
    \stemUp <d d'>8 r8 \stemUp <cis cis'>8 r8 r4 \stemUp <b b'>16 (
    \stemUp <e e'>16 \stemUp <d d'>16 \stemUp <b b'>16 ) | % 184
    \stemUp <d d'>8 r8 \stemUp <cis cis'>8 r8 r2 | % 185
    r2 r4 \stemDown fis'8 ( _\ff ^\markup{ \bold\small {a. 2} }
    \stemDown e16 \stemDown fis16 ) | % 186
    \stemDown g8 ( \stemDown fis16 \stemDown g16 ) \stemDown a8 (
    \stemDown g16 \stemDown a16 ) \stemDown b8 ( \stemDown a16 \stemDown
    b16 \stemDown cis8 ) r8 | % 187
    r2 r4 \stemUp d,8 ( _\fff \stemUp cis16 \stemUp d16 ) \pageBreak | % 188
    \stemDown e8 ( \stemDown d16 \stemDown e16 ) \stemDown fis8 (
    \stemDown e16 \stemDown fis16 ) \stemDown g8 ( \stemDown fis16
    \stemDown g16 ) \stemDown g8 ( \stemDown fis16 \stemDown g16 ) | % 189
    \stemDown g8 ( \stemDown fis16 \stemDown g16 ) \stemDown g8 (
    \stemDown fis16 \stemDown g16 ) \stemDown g8 ( \stemDown fis16
    \stemDown g16 ) r4 | \barNumberCheck #190
    \clef "tenor" \stemDown bes'2 -> \stemDown a4 -> \stemDown g4 -> | % 191
    \stemDown f2 -> \stemDown es2 -> \break | % 192
    \stemDown es2 -> \stemDown d4 -> \stemDown c4 -> | % 193
    \stemDown ces2 -> \stemDown bes2 -> | % 194
    \stemDown bes'2 -> \stemDown a4 -> \stemDown g4 -> | % 195
    \stemDown f4 -> \stemDown e4 -> \stemDown d4 -> \stemDown c4 ->
    \pageBreak | % 196
    \clef "bass" \stemUp bes4 -> \stemUp a4 -> \stemUp a2 | % 197
    \stemUp a2 \stemUp f8 -> \stemUp f8 -> \stemUp a16 ( \stemUp e'16
    \stemUp d16 \stemUp a16 ) | % 198
    \stemDown f16 ( ^\markup{ \bold\small {a. 2} } \stemDown bes16
    \stemDown a16 \stemDown f16 ) \stemDown d16 ( \stemDown g16
    \stemDown f16 \stemDown d16 ) \stemUp a16 ( \stemUp e'16 \stemUp d16
    \stemUp a16 ) \stemUp f16 ( \stemUp bes16 \stemUp a16 \stemUp f16 )
    | % 199
    \stemUp d'16 ( \stemUp g16 \stemUp f16 \stemUp d16 ) \stemUp a16 (
    \stemUp e'16 \stemUp d16 \stemUp a16 ) \stemUp a16 ( \stemUp e'16
    \stemUp d16 \stemUp a16 ) \stemUp a8 r8 | \barNumberCheck #200
    R1 \break | % 201
    R1*4 | % 205
    r2 r4 r8. \stemDown <f' a>16 _\p | % 206
    \stemDown <f a>2 -> _\markup{ \italic {poco a poco cresc.} }
    \stemDown <e g>2 \pageBreak | % 207
    \stemUp f2 ( \stemUp e8 ) r8 r8. \stemDown <as c>16 | % 208
    \stemUp c2 -> \stemUp bes2 | % 209
    \stemUp as2 ( \stemUp g8 ) r8 r8. \stemUp dis'16 _\mf |
    \barNumberCheck #210
    \stemUp dis8 _\markup{ \italic {poco cresc.} } r8 \stemUp cis8 r8
    \stemUp b8 r8 \stemUp ais8 r16 \stemUp fis'16 | % 211
    \stemUp fis8 r8 \stemUp e8 r8 \stemUp d8 r8 \stemUp cis8 r8 | % 212
    \stemUp e8 r8 \stemUp dis8 r8 \stemUp fis8 _\f _\< r8 \stemUp eis8 r8
    \pageBreak | % 213
    \stemUp fis8 r8 \stemUp eis8 r8 \stemUp fis8 r8 \stemUp eis8 r8 | % 214
    \stemUp <d,, d'>4 -- _\! _\ff \stemUp <dis dis'>4 -- \stemUp <eis
        eis'>4 -- \stemUp <fis fis'>4 -- | % 215
    \stemUp <gis gis'>4 -- \stemDown <a a'>4 -- \stemDown <fis' fis'>4
    -- \stemDown <eis eis'>4 -- | % 216
    \stemDown <e e'>4 -- _\markup{ \italic {dim. un poco} } \stemDown
    <dis dis'>4 -- \stemDown <d d'>4 -- \stemDown <cis cis'>4 -- \break
    | % 217
    \stemDown <b b'>4 -- \stemDown <ais ais'>4 -- \stemDown <a a'>4 (
    \stemUp <gis gis'>8 ) r8 | % 218
    R1*2 | \barNumberCheck #220
    \stemDown <cis cis'>4 -- _\markup{ \italic {dim.} } r4 \stemDown <b
        b'>4 -- r4 \pageBreak | % 221
    \stemUp <gis gis'>4 -- r4 \stemUp <g g'>4 -- r4 | % 222
    \stemUp <g g'>4 -- r4 \stemUp <g g'>4 -- r4 | % 223
    \stemUp <g g'>4 -- _\p r4 r2 | % 224
    R1*2 \break | % 226
    R1*5 \break | % 231
    R1*6 \pageBreak | % 237
    R1*3 | \barNumberCheck #240
    \stemUp es'8 ( -> ^\mf \stemUp des8 ) \stemUp c16 ( ^\markup{
        \italic {cresc.} } \stemUp des16 \stemUp es16 \stemUp des16 ) _
    "" _\markup{ \italic {cresc.} } \stemUp f8 ( -> \stemUp es8 )
    \stemUp d16 ( \stemUp es16 \stemUp f16 \stemUp es16 ) | % 241
    \stemUp ges8 ( \stemUp f8 ) \stemUp e16 ( \stemUp f16 \stemUp ges16
    \stemUp e16 ) \stemUp ges8 ( _ "" _\markup{ \italic {cresc.} }
    \stemUp f8 ) \stemUp e16 ( \stemUp f16 \stemUp ges16 \stemUp f16 )
    \pageBreak | % 242
    \stemUp as16 ( \stemUp ges16 ) \stemUp ges8 \stemUp bes16 ( \stemUp
    as16 \stemUp as8 ) \stemUp b16 ( \stemUp ais16 ) \stemUp ais8
    \stemUp a16 ( \stemUp ais16 \stemUp b16 \stemUp ais16 ) | % 243
    \stemUp cis16 ( _\ff \stemUp b16 ) \stemUp b8 \stemUp ais16 (
    \stemUp b16 \stemUp cis16 \stemUp b16 ) \stemUp d16 ( \stemUp cis16
    ) \stemUp cis8 \stemUp bis16 ( \stemUp cis16 \stemUp d16 \stemUp cis16
    ) | % 244
    \stemUp e16 ( \stemUp d16 ) \stemUp d8 \stemUp fis16 ( \stemUp e16 )
    \stemUp e8 \stemUp g16 ( \stemUp fis16 ) \stemUp fis8 \stemUp b,8
    _\fff \stemUp cis8 | % 245
    \stemUp d4 ( -> \stemUp cis8 ) r8 r4 \stemUp b8 \stemUp b8
    \pageBreak | % 246
    \stemUp d4 ( -> \stemUp cis8 ) r8 r4 r8 \stemUp cis,8 | % 247
    r8 \stemUp <d, d'>8 r8 \stemUp <g g'>8 r8 \stemUp <fis fis'>8 r8
    \stemUp <cis cis'>8 | % 248
    r8 \stemUp <d d'>8 r8 \stemUp <g g'>8 \stemUp <fis fis'>8 r8 r4 | % 249
    \clef "tenor" r4 \stemDown <ais' cis>8 _\ff \stemDown <b d>8
    \stemDown <cis e>4 -> \stemDown <b d>8 r8 | \barNumberCheck #250
    r4 \stemDown <ais cis>8 \stemDown <b d>8 \stemDown <cis e>4 ->
    \stemDown <d fis>8 r8 | % 251
    r4 \stemDown <cis e>8 \stemDown <d fis>8 \stemDown <e g>4 ->
    \stemDown <d fis>8 r8 \break | % 252
    r4 \stemDown <cis e>8 \stemDown <d fis>8 \stemDown <e g>4 ->
    \stemDown <fis a>8 r8 | % 253
    r4 \stemDown <a, cis>8 \stemDown <b d>8 \stemDown <bis dis>8 ( ->
    \stemDown <cis eis>8 ) r4 | % 254
    r4 \stemDown <a cis>8 \stemDown <b d>8 \stemDown <bis dis>8 ( ->
    \stemDown <cis eis>8 ) r4 | % 255
    \clef "bass" r4 r8 \stemDown <b eis>8 _\ff r8 \stemDown <cis fis>8 r4
    | % 256
    r4 r8 \stemDown <b fis'>8 r8 \stemDown <b e>8 r4 \pageBreak | % 257
    r4 r8 \stemDown <a d>8 r8 \stemDown <b e>8 r4 | % 258
    r4 r8 \stemDown <a e'>8 r8 \stemDown <a d>8 r4 | % 259
    r2 r4 \stemUp c,4 ~ _ "" _\markup{ \italic {cresc.} } ^\markup{
        \bold\small {a. 2} } | \barNumberCheck #260
    \stemUp c4 \stemUp c4 ( \stemUp ces4 ) \clef "tenor" \stemDown <bes'
        es>4 _\mf | % 261
    \stemDown <a es'>4 _\markup{ \italic {cresc.} } \stemDown <a d>4
    \stemDown <a cis>4 \stemDown <d, a''>4 | % 262
    \stemDown <dis a''>4 \stemDown <e a'>4 \stemDown <f a'>4 \clef
    "bass" \stemUp <ges, ges'>8 _\ff \stemUp <f f'>8 \pageBreak | % 263
    \stemUp <es es'>8 r8 \stemUp <ges ges'>8 r8 r4 \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp <ges ges'>8 \stemUp <f f'>8 \stemUp <es es'>8 }
    | % 264
    \stemUp <es es'>8 r8 \stemUp <ges ges'>8 r8 r4 \stemDown <a a'>8
    \stemDown <gis gis'>8 | % 265
    \stemUp <fis fis'>8 r8 \stemDown <a a'>8 r8 r4 \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp <a a'>8 \stemUp <gis gis'>8 \stemUp <fis fis'>8 }
    | % 266
    \stemUp <fis fis'>8 r8 \stemDown <a a'>8 r8 r4 \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp <a a'>8 \stemUp <gis gis'>8 \stemUp <fis fis'>8 }
    | % 267
    \stemUp <fis fis'>8 r8 \stemUp <fis fis'>2 _\fff \stemUp <gis gis'>4
    \pageBreak | % 268
    \stemDown <a a'>4 \stemDown <b b'>4 \stemDown <c c'>4 \stemDown <d
        d'>4 | % 269
    \stemDown <es es'>4 \stemDown <f f'>4 \stemDown <fis fis'>4
    \stemDown <gis gis'>4 | \barNumberCheck #270
    \stemDown <a a'>8 r8 \stemUp fis,2. ~ _\ff ^\markup{ \bold\small {a.
            2} } _\> | % 271
    \stemUp fis8 _\! _\p r8 r4 \stemUp fis2 ~ _ "" _\markup{ \italic
        {cresc.} } | % 272
    fis1 ~ \pageBreak | % 273
    fis1 ~ | % 274
    fis1 ~ _\ff | % 275
    fis1 ~ | % 276
    fis1 ~ | % 277
    fis1 ~ | % 278
    fis1 ~ | % 279
    fis1 ~ | \barNumberCheck #280
    fis1 ~ | % 281
    fis1 ~ | % 282
    fis1 ~ | % 283
    fis1 ~ | % 284
    fis1 ~ _\< \pageBreak | % 285
    fis1 ~ _\! _\fff | % 286
    fis1 ~ | % 287
    fis1 ~ | % 288
    fis1 ~ | % 289
    fis1 ~ | \barNumberCheck #290
    fis1 ~ | % 291
    fis1 ~ | % 292
    fis1 ~ | % 293
    fis1 ~ | % 294
    fis1 ~ | % 295
    fis1 ~ | % 296
    fis1 ~ | % 297
    fis1 | % 298
    \stemUp g4.. \stemUp fis16 \stemUp fis2 | % 299
    <d g>1 ~ ~ _\ffff _\> | \barNumberCheck #300
    \stemUp <d g>2 ~ ~ \stemUp <d g>8 _\! _\p r8 r4 | % 301
    cis1 ~ _\ff ^\markup{ \bold\small {a. 2} } _\> \break | % 302
    cis1 ~ | % 303
    cis1 ~ | % 304
    \stemUp cis8 _\! _\pp r8 r4 r2 ^\fermata \bar "||"
    \pageBreak | % 305
    \key b \major R1 | % 306
    r4 \stemDown dis'4 -- ^\markup{ \bold\small {a. 2} } _\pp \stemDown
    e8 ( \stemDown fis8 \stemDown gis8 \stemDown ais8 ) | % 307
    \stemDown b4 -- _\< \stemDown cis8. \stemDown d16 \stemDown dis4 --
    _\! _\> \stemDown e8 ( \stemDown dis8 ) | % 308
    \stemDown fis,4 -- _\! \stemDown dis4 -- \stemDown cis'4 --
    \stemDown e4 -- | % 309
    \stemDown dis4 -- _\< \stemDown cis8 ( \stemDown b8 ) \clef "tenor"
    \stemDown <cisis, cisis'>8 ( _\! _\mp \stemDown <dis dis'>8
    \stemDown <e e'>8 \stemDown <fis fis'>8 ) | \barNumberCheck #310
    \stemDown <fisis fisis'>8 ( _\markup{ \italic {poco cresc.} }
    \stemDown <gis gis'>8 \stemDown <ais ais'>8 \stemDown <gis gis'>8 )
    \stemUp <bis, bis'>8 ( \stemUp <cis cis'>8 \stemUp <dis dis'>8
    \stemUp <e e'>8 ) \pageBreak | % 311
    \stemDown <eis eis'>8 ( \stemDown <fis fis'>8 \stemDown <gis gis'>8
    \stemDown <fis fis'>8 ) \stemUp <b, b'>2 _\mf _\> | % 312
    \clef "bass" \stemDown <b b'>2 _\! _\pp _\< \stemDown <bis bis'>8 (
    _\! _\p _\< \stemDown <cis cis'>8 \stemDown <dis dis'>8 _\! _\>
    \stemDown <cis cis'>8 ) | % 313
    \stemDown <b fis'>2 _\! _\p _\< \stemDown <fis' a>2 _\! _\ff | % 314
    \stemUp e2 \stemUp g2 | % 315
    \stemUp dis2 \stemUp gis2 _\sff _\> | % 316
    \stemUp fis2 _\! _\mf \stemUp ais2 \pageBreak | % 317
    \stemUp b2 r2 | % 318
    R1 | % 319
    r2 r8 \stemDown d8 ( _\f ^\markup{ \bold\small {a. 2} } _\>
    \stemDown cis8 \stemDown b8 ) | \barNumberCheck #320
    \stemDown fis8 ( _\! _\mf _\< \stemDown dis8 \stemDown b8 \stemDown
    dis8 ) \stemDown g4.. ( _\! _\> \stemDown fis16 ) | % 321
    \stemUp fis2 _\! \stemUp b,2 ~ _\p | % 322
    \stemUp b2 \stemUp b2 ~ | % 323
    \stemUp b2 \stemUp b2 ~ | % 324
    \stemUp b4 \stemUp b2. ~ | % 325
    \stemUp b2 ~ _\> \stemUp b8 _\! _\pp r8 r4 \break | % 326
    r4 \stemDown <dis b'>4 _\pppp _\< \stemDown <cisis b'>2 _\! _\pp _\>
    | % 327
    \stemDown <dis b'>2 ~ ~ _\! _\pppp \stemDown <dis b'>8 r8 r4 | % 328
    \stemDown <dis b'>2 _\pppp _\< \stemDown <cis e>2 _\! _\pp _\> | % 329
    \stemDown <dis b'>2 _\! _\pppp _\< \stemDown <dis bis'>2 _\! _\pp |
    \barNumberCheck #330
    \stemDown <e cis'>2 \stemDown <cis ais'>2 | % 331
    \stemDown <dis b'>2 _\< \stemUp <eis, b''>2 _\! _\p _\> | % 332
    \stemDown <fis b'>2 _\! _\pppp _\< \stemUp ais'2 _\! _\pp _\> | % 333
    \stemUp b2 _\! _\pppp \stemUp e,4.. -> _\pp _\> \stemUp dis16
    \pageBreak | % 334
    \stemUp dis2 _\! _\pppp _\< \stemUp e4.. -> _\! _\pp _\> \stemUp dis16
    \bar "||"
    \stemUp dis4 ~ _\! _\pppp \stemUp dis8 r8 r2 | % 336
    R1*4 | \barNumberCheck #340
    \stemDown <e gis>2 _\p ^\markup{ \italic {cantabile} } \stemDown <e
        gis>4. _\< \stemDown <e gis>8 | % 341
    \stemDown <fis b>2. ~ ~ _\! _\mf _\> \stemDown <fis b>8 r8 _\! | % 342
    \stemDown <e gis>2 _\p \stemDown <e gis>4. _\< \stemDown <e gis>8
    \pageBreak | % 343
    <fis b>1 _\! _\mf _\> | % 344
    \stemDown <fis dis'>2. ~ ~ _\! _\p \stemDown <fis dis'>8 \stemDown
    <fis dis'>8 | % 345
    <fis dis'>1 _\> | % 346
    \stemDown fis'2. ~ _\! _\pp ^ "I." \stemDown fis8 r8 | % 347
    R1*8 \bar "|."
    }

PartPFiveVoiceTwo =  \relative cisis' {
    \clef "bass" \time 4/4 \key d \major s1*11 \break s1*7 \bar "||"
    s1*5 \pageBreak s1*6 | \barNumberCheck #30
    \time 2/4  s2 \break | % 31
    \time 4/4  s1*6 \break s1*7 \pageBreak s1*6 \break s1*4 \pageBreak
    s1*5 \break s1*5 \pageBreak s1. r16 \stemDown cisis16 -. _\mp _\<
    \stemDown cisis16 -. \stemDown cisis16 -. \stemDown cisis16 -.
    \stemDown cisis16 -. \stemDown dis16 -. \stemDown cisis16 -. | % 66
    \stemDown b8 -- \stemDown gisis8 -- \stemDown ais8 -- r8 _\!
    \stemDown dis,4 ~ \stemDown dis8 s8 | % 67
    \stemDown eis,2 ( -> \stemDown fis8 ) r8 \stemDown fis8 \stemDown
    ais8 | % 68
    \stemDown dis4 \stemDown ais4 \stemDown fis4 ~ \stemDown fis8 s8
    \pageBreak | % 69
    \stemDown gis2 ( -> \stemDown a8 ) s8 \stemDown a8 \stemDown cis8 |
    \barNumberCheck #70
    \stemDown fis4 \stemDown cis4 \stemDown a4 ~ \stemDown a8 s8 | % 71
    r8 \stemDown e''8 ~ -> \stemDown e8 \stemDown a,8 -. \stemDown g,4 ~
    \stemDown g8 s8 | % 72
    r8 \stemDown e''8 ~ -> \stemDown e8 \stemDown a,8 -. \stemDown f,4 ~
    \stemDown f8 s8 | % 73
    \stemDown a'4 ~ \stemDown a8 s8 \stemDown f,4 ~ \stemDown f8 s8
    \pageBreak s1*4 \break s1*5 \pageBreak s1*6 \bar "||"
    s1*5 \break s1*7 \bar "||"
    s1*2 \pageBreak s1*5 \break s1*4 \pageBreak s1*4 \break s1*4
    \pageBreak s1*5 \break s1*5 \bar "||"
    \time 12/8  s1*3 \pageBreak s1*9 \pageBreak s1*6 \bar "||"
    s1. | % 143
    \numericTimeSignature\time 4/4  s1*2 \break s1*11 \pageBreak s1*5
    \bar "||"
    \key c \major s1*4 \pageBreak s2*11 \stemDown bes8 -> \stemDown a8
    -> s4*5 \pageBreak s8*39 \clef "tenor" s8*9 \pageBreak s4*19 \clef
    "bass" s4 \break s1*5 \pageBreak s1*2 | \barNumberCheck #190
    \clef "tenor" s1*2 \break s1*4 \pageBreak | % 196
    \clef "bass" \stemDown bes'4 -> \stemDown a4 -> \stemDown g4 ->
    \stemDown f4 -> | % 197
    \stemDown f2 \stemDown d8 -> \stemDown d8 -> \stemDown a'16 (
    \stemDown e'16 \stemDown d16 \stemDown a16 ) s1 | % 199
    \stemDown d,,16 ( \stemDown g16 \stemDown f16 \stemDown d16 )
    \stemDown a'16 ( \stemDown e'16 \stemDown d16 \stemDown a16 )
    \stemDown a8 r8 r4 s1 \break s1*6 \pageBreak | % 207
    \stemDown d2 ( \stemDown e8 ) s4. | % 208
    \stemDown as2 -> \stemDown g2 | % 209
    \stemDown f2 ( \stemDown g8 ) s16*5 \stemDown b16 | \barNumberCheck
    #210
    \stemDown b8 s8 \stemDown ais8 s8 \stemDown gis8 s8 \stemDown ais8
    s16 \stemDown d16 | % 211
    \stemDown d8 s8 \stemDown cis8 s8 \stemDown b8 s8 \stemDown cis8 s8
    | % 212
    \stemDown cis8 s8 \stemDown dis8 s8 \stemDown dis8 s8 \stemDown eis8
    s8 \pageBreak | % 213
    \stemDown dis8 s8 \stemDown eis8 s8 \stemDown dis8 s8 \stemDown eis8
    s8*25 \break s1*4 \pageBreak s1*5 \break s1*5 \break s1*6 \pageBreak
    s1*3 | \barNumberCheck #240
    r4 r8. \stemDown bes,,16 \stemDown c4.. \stemDown c16 | % 241
    \stemDown des4.. \stemDown des16 \stemDown d4.. \stemDown d16
    \pageBreak | % 242
    \stemDown es8 r8 \stemDown f8 r8 \stemDown ges8 r8 r4 | % 243
    \stemDown fis4.. \stemDown fis16 \stemDown ais4.. \stemDown ais16 | % 244
    \stemDown b8 r8 \stemDown cis8 r8 \stemDown d8 r8 \stemDown fis8
    \stemDown g8 | % 245
    \stemDown gis4 ( -> \stemDown ais8 ) s4. \stemDown fis8 \stemDown g8
    \pageBreak | % 246
    \stemDown gis4 ( -> \stemDown ais8 ) s2 \stemDown cis,,8 s1*2 | % 249
    \clef "tenor" s1*3 \break s1*3 | % 255
    \clef "bass" s1*2 \pageBreak s4*15 \clef "tenor" s1*2 \clef "bass"
    s4 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*12 \pageBreak s1*17
    \break s1*3 \bar "||"
    \pageBreak | % 305
    \key b \major s2*9 \clef "tenor" s1. \pageBreak s1 | % 312
    \clef "bass" s1*2 | % 314
    \stemDown e'2 \stemDown e2 | % 315
    \stemDown dis2 \stemDown b2 | % 316
    \stemDown b2 \stemDown e2 \pageBreak | % 317
    \stemDown dis2 s2*7 | % 321
    r2 \stemDown b,2 ~ | % 322
    \stemDown b2 \stemDown b2 ~ | % 323
    \stemDown b2 \stemDown b2 ~ | % 324
    \stemDown b2 \stemDown b2 ~ | % 325
    \stemDown b2 ~ \stemDown b8 s4. \break s2*13 \stemDown fis'2 ( | % 333
    \stemDown b8 ) r8 r4 \stemDown cis4.. -> \stemDown dis16 \pageBreak
    | % 334
    \stemDown dis2 \stemDown cis4.. -> \stemDown dis16 \bar "||"
    \stemDown dis4 ~ \stemDown dis8 s8*61 \pageBreak s1*12 \bar "|."
    }

PartPSixVoiceOne =  \relative cis'' {
    \clef "treble" \time 4/4 \key c \major \transposition f | % 1
    R1*11 \break | % 12
    cis1 ~ ^ "I." _\pp _\< | % 13
    \stemDown cis2. ~ _\! _\mf _\> \stemDown cis8 r8 _\! | % 14
    cis,1 ~ ^ "II." _\pp _\< | % 15
    \stemUp cis2. ~ _\! _\mf _\> \stemUp cis8 r8 _\! | % 16
    R1*3 \bar "||"
    R1*5 \pageBreak | % 24
    R1*6 | \barNumberCheck #30
    \time 2/4  R2 \break | % 31
    \time 4/4  R1*6 \break | % 37
    R1*2 | % 39
    r2 r8 \stemUp <e e'>16 -. _\f \stemUp <e e'>16 -. \stemUp <e e'>8 -.
    \stemUp <e e'>8 -. | \barNumberCheck #40
    \stemUp <cis cis'>2 r2 | % 41
    R1*3 \pageBreak | % 44
    R1*6 \break | \barNumberCheck #50
    R1 | % 51
    r2 r8 \stemUp <e d'>8 _\mp ^\markup{ \italic {espressivo} } _\<
    \stemUp <dis dis'>8. \stemUp <dis dis'>16 | % 52
    \stemUp <dis dis'>8. _\! _\> \stemUp <cis cis'>16 \stemUp <cis b'>8.
    _\! \stemUp <ais ais'>16 \stemUp <gis gis'>8 r8 r4 | % 53
    r2 r8 \stemUp <e' d'>8 _\mp _\< \stemUp <dis dis'>8. \stemUp <dis
        dis'>16 \pageBreak | % 54
    \stemUp <dis dis'>8. _\! _\> \stemUp <cis cis'>16 \stemUp <cis b'>8.
    _\! \stemUp <ais ais'>16 \stemUp <gis gis'>8 r8 r4 | % 55
    R1*4 \break | % 59
    r2 r8 \stemUp <b a'>8 _\mp ^\markup{ \italic {espr.} } _\< \stemUp
    <bes bes'>8. \stemUp <bes bes'>16 | \barNumberCheck #60
    \stemUp <bes bes'>8. _\! _\> \stemUp <as as'>16 \stemUp <as ges'>8.
    _\! \stemUp <f f'>16 \stemUp <es es'>8 r8 r4 | % 61
    r2 r8 \stemUp <b' a'>8 _\mp _\< \stemUp <bes bes'>8. \stemUp <bes
        bes'>16 | % 62
    \stemUp <bes bes'>8. _\! _\> \stemUp <as as'>16 \stemUp <as ges'>8.
    _\! \stemUp <f f'>16 \stemUp <es es'>8 r8 r4 | % 63
    R1 \pageBreak | % 64
    R1*4 | % 68
    r4 \stemUp f'4 _\f \stemUp fis8 -> \stemUp dis8 -> \stemUp e8 -> r8
    \pageBreak | % 69
    R1 | \barNumberCheck #70
    r4 \stemUp gis4 _\ff \stemUp a8 -> \stemUp fis8 -> \stemUp g8 -> r8
    | % 71
    r2 \stemUp a8 -> \stemUp fis8 -> \stemUp g8 -> r8 | % 72
    r2 \stemUp a8 -> \stemUp fis8 -> \stemUp g8 -> r8 | % 73
    \stemUp g'4 ~ \stemUp g8 r8 \stemUp a,8 -> \stemUp fis8 -> \stemUp g8
    -> r8 \pageBreak | % 74
    \stemDown <e' g>4 ~ ~ \stemDown <e g>8 r8 \stemDown <e g>4 ~ -> ~
    \stemDown <e g>8 r8 | % 75
    \stemDown <e g>4 ~ -> ~ \stemDown <e g>8 r8 \stemDown <d e>4 ~ -> ~
    \stemDown <d e>8 r8 | % 76
    \stemDown <d e>4 ~ -> ~ \stemDown <d e>8 r8 \stemUp g,4 ( -> ^\f
    \stemUp gis8 ) r8 | % 77
    \stemUp g4 ( -> \stemUp gis8 ) r8 r2 \break | % 78
    R1*5 \pageBreak | % 83
    R1*6 \bar "||"
    R1 | \barNumberCheck #90
    \stemUp <cis, cis'>2 _\pp _\< \stemUp <c c'>2 _\! _\mp _\> | % 91
    \stemUp <cis cis'>8 _\! _\pp \stemUp <cis cis'>4 \stemUp <cis cis'>8
    ~ ~ \stemUp <cis cis'>2 | % 92
    \stemUp <cis cis'>2 _\< \stemUp <d d'>2 _\! _\mp _\> | % 93
    \stemUp <cis cis'>8 _\! _\pp _\< \stemUp <cis cis'>4 \stemUp <cis
        cis'>8 \stemDown <g' g'>2 _\! _\mf \break | % 94
    \stemDown <fis fis'>2 \stemDown <f f'>2 _\> | % 95
    \stemUp <e e'>2 _\! _\p _\< \stemUp <cis a'>2 _\! _\mf _\> | % 96
    \stemUp <cis a'>2 _\! _\p _\< \stemUp <d d'>2 _\! _\mf _\> | % 97
    \stemUp <cis cis'>8 _\! _\p _\< \stemUp <cis cis'>4 \stemUp <cis
        cis'>8 \stemDown <g' g'>2 _\! _\mf | % 98
    \stemDown <fis fis'>2 \stemDown <f f'>2 _\> | % 99
    \stemUp <e e'>2 _\! _\p _\< \stemUp <cis a'>2 _\! _\mf _\> |
    \barNumberCheck #100
    \stemUp <cis a'>2 _\! _\p _\< \stemUp <d d'>2 _\! _\mf _\> \bar "||"
    \stemUp <cis cis'>8 _\! _\p r8 r4 r2 | % 102
    R1 \pageBreak | % 103
    R1*5 \break | % 108
    R1*4 \pageBreak | % 112
    R1*4 \break | % 116
    R1*4 \pageBreak | \barNumberCheck #120
    R1 | % 121
    r4 \stemDown b'2 _\mf ^ "I." ^\markup{ \italic {espress.} } \stemUp
    a4 -- | % 122
    \stemUp a4 ~ -> \stemUp a8. \stemUp gis16 \stemUp gis4 ~ \stemUp gis8
    r8 | % 123
    r4 \stemUp gis2 _\f \stemUp fis4 -- | % 124
    \stemUp fis4 ~ -> \stemUp fis8. \stemUp e16 \stemUp e2 ~ \break | % 125
    \stemUp e8 r8 \stemUp fis2 \stemUp e4 ~ | % 126
    \stemUp e8 r8 \stemUp fis2 ( \stemUp e4 ) | % 127
    R1*3 \bar "||"
    \time 12/8  r8*2/3 \stemUp <e e'>8 ^\markup{ \italic {pesante, non
            staccato} } _\p \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e
        e'>8 \stemUp <e e'>8 \stemUp <e e'>4. ~ ~ \stemUp <e e'>8 r8*2/3
    r8*2/3 s8 | % 131
    r8*2/3 \stemUp <cis cis'>8 _\markup{ \italic {sempre} } _ ""
    \stemUp <cis cis'>8 \stemUp <cis cis'>8 \stemUp <cis cis'>8 \stemUp
    <cis cis'>8 r8*2/3 \stemUp <dis c'>8 \stemUp <dis c'>8 \stemUp <dis
        c'>8 \stemUp <dis c'>8 \stemUp <dis c'>8 s1*1/12 \pageBreak | % 132
    r8*2/3 \stemUp <cis cis'>8 \stemUp <cis cis'>8 \stemUp <cis cis'>8
    \stemUp <cis cis'>8 \stemUp <cis cis'>8 \stemUp <cis cis'>8 r8*2/3 r8*2/3
    r4*2/3 r8*2/3 s4 | % 133
    r8*2/3 \stemUp <e cis'>8 \stemUp <e cis'>8 \stemUp <e cis'>8 \stemUp
    <e cis'>8 \stemUp <e cis'>8 r8*2/3 \stemDown <gis d'>8 \stemDown
    <gis d'>8 \stemDown <gis d'>8 \stemDown <gis d'>8 \stemDown <gis d'>8
    s1*1/12 | % 134
    r8*2/3 \stemDown <a cis>8 _\p _\< \stemDown <a cis>8 \stemDown <a
        cis>8 \stemDown <a cis>8 r8*2/3 _\! \stemDown <g g'>2. _\mf
    s1*1/12 | % 135
    \stemDown <fis fis'>8 \stemDown <fis fis'>8 \stemDown <fis fis'>8
    \stemDown <fis fis'>8 \stemDown <fis fis'>8 \stemDown <fis fis'>8
    \stemDown <f f'>2. | % 136
    \stemUp <e e'>8 _\< \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8
    \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <fis cis'>2. _\! _\sf _\> | % 137
    \stemUp <e cis'>8 _\! _\p _\< \stemUp <e cis'>8 \stemUp <e cis'>8
    \stemUp <e cis'>8 \stemUp <e cis'>8 \stemUp <e cis'>8 \stemUp <d d'>2.
    _\! _\mf _\> \pageBreak | % 138
    r8*2/3 _\! \stemDown <a' cis>8 _\p _\< \stemDown <a cis>8 \stemDown
    <a cis>8 \stemDown <a cis>8 r8*2/3 _\! \stemDown <g g'>2. _\mf
    s1*1/12 | % 139
    \stemDown <fis fis'>8 \stemDown <fis fis'>8 \stemDown <fis fis'>8
    \stemDown <fis fis'>8 \stemDown <fis fis'>8 \stemDown <fis fis'>8
    \stemDown <f f'>2. | \barNumberCheck #140
    \stemUp <e e'>8 _\< \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8
    \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <fis cis'>2. _\! _\sf _\> | % 141
    \stemUp <e cis'>8 _\! _\p _\< \stemUp <e cis'>8 \stemUp <e cis'>8
    \stemUp <e cis'>8 \stemUp <e cis'>8 \stemUp <e cis'>8 \stemUp <d d'>2.
    _\! _\mf _\> \bar "||"
    r8*2/3 _\! \stemUp <cis cis'>8 _\mf _\> \stemUp <cis cis'>8 \stemUp
    <cis cis'>8 \stemUp <cis cis'>8 \stemUp <cis cis'>8 \stemUp <e cis'>2.
    _\! _\mp s1*1/24 | % 143
    \numericTimeSignature\time 4/4  \stemUp <d d'>2 \stemUp <d b'>2 | % 144
    \stemUp <cis cis'>2 _\> \stemUp <e cis'>2 _\! _\p \break | % 145
    \stemUp <fis b>2 \stemUp <d b'>2 | % 146
    \stemUp <e a>2 \stemUp <e e'>2 _\p | % 147
    \stemUp <d d'>2 \stemUp <d d'>2 | % 148
    \stemUp <cis cis'>2 _\> \stemUp <e e'>2 _\! _\pp | % 149
    \stemUp <fis b>2 \stemUp <d d'>2 | \barNumberCheck #150
    \stemUp <e a>2 \stemUp <dis a'>2 _\markup{ \italic {dim.} } | % 151
    \stemUp <e a>2 \stemUp <dis a'>2 | % 152
    \stemUp <e a>2 _\ppp \stemUp <e a>2 | % 153
    \stemUp <e a>2 r2 | % 154
    R1*2 \pageBreak | % 156
    R1*5 \bar "||"
    \key c \major \stemDown <d' e>8 _\ff r8 r4 r2 | % 162
    R1*2 | % 164
    r2 r4 \stemUp <d, bes'>8 ( _\ff \stemUp <bes' d>8 ) \pageBreak | % 165
    \stemDown <b d>8 r8 r4 \stemUp <d, b'>16 _\sff \stemUp <d b'>16
    \stemUp <d b'>8 ~ ~ \stemUp <d b'>4 ~ ~ | % 166
    \stemUp <d b'>8 \stemUp <cis bes'>8 -> \stemUp <c a'>8 -> \stemUp
    <cis bes'>8 -> \stemUp <d b'>8 -> r8 r4 | % 167
    \stemUp <cis e>8 _\sf r8 \stemUp <d a'>8 _\sf r8 r4 r8 \stemUp <d
        a'>8 _\sf | % 168
    \stemUp <cis e>8 _\sf r8 \stemUp <b d>8 _\sf r8 r4 \stemUp <d b'>8 (
    _\ff \stemUp <b' d>8 ) | % 169
    \stemDown <a c>8 r8 r4 \stemDown <a c>16 _\sff \stemDown <a c>16
    \stemDown <a c>8 ~ ~ \stemDown <a c>4 ~ ~ | \barNumberCheck #170
    \stemUp <a c>8 \stemUp <d, d'>8 -> \stemUp <c c'>8 -> \stemUp <d d'>8
    -> \stemUp <dis dis'>8 -> \stemUp <e e'>8 -> r4 | % 171
    R1 \pageBreak | % 172
    R1*3 | % 175
    r2 r8 \stemUp <e e'>8 ( _\f \stemUp <e, e'>8 ) r8 | % 176
    r2 r8 \stemUp <e' e'>8 ( _\f \stemUp <e, e'>8 ) r8 | % 177
    R1 \pageBreak | % 178
    R1 | % 179
    \stemDown <fis' fis'>8 _\f r8 r4 r2 | \barNumberCheck #180
    R1*3 \break | % 183
    r2 r8 \stemUp <fis fis'>8 ( _\f \stemUp <fis, fis'>8 ) r8 | % 184
    r2 r8 \stemUp <fis' fis'>8 ( _\f \stemUp <fis, fis'>8 ) r8 | % 185
    R1*3 \pageBreak | % 188
    R1 | % 189
    r2 r4 \stemUp <f' bes>4 ~ ~ _\fff | \barNumberCheck #190
    <f bes>1 ~ ~ | % 191
    \stemUp <f bes>2. \stemDown <bes d>4 ~ ~ \break | % 192
    <bes d>1 ~ ~ | % 193
    \stemDown <bes d>2. \stemDown <a c>4 | % 194
    <a c>1 | % 195
    <c e>1 \pageBreak | % 196
    \stemUp <c, c'>2 \stemUp <e a>2 | % 197
    \stemUp <c e>2 \stemUp <f, f'>8 -> \stemUp <e e'>8 -> r4 | % 198
    R1*3 \break | % 201
    R1*4 | % 205
    r2 r4 r8. \stemDown <g' e'>16 _\p | % 206
    \stemDown <g e'>2 -> _\markup{ \italic {poco a poco cresc.} }
    \stemDown <gis d'>2 \pageBreak | % 207
    \stemDown <a c>4 ~ ~ \stemDown <a c>8 r8 r4 r8. \stemDown <bes g'>16
    | % 208
    \stemDown <bes g'>2 -> \stemDown <b f'>2 | % 209
    \stemDown <c es>4 ~ ~ \stemDown <c es>8 r8 r4 r8. \stemUp <cis,
        cis'>16 _\mf | \barNumberCheck #210
    \stemUp <cis cis'>8 _\markup{ \italic {poco cresc.} } r8 \stemUp <d
        d'>8 r8 r4 r8. \stemUp <e e'>16 | % 211
    \stemUp <e e'>8 r8 \stemDown <f f'>8 r8 r2 | % 212
    R1 \pageBreak | % 213
    R1 | % 214
    \stemDown c'4 -- _\ff ^ "I." \stemDown cis4 -- \stemUp fis,4 --
    \stemUp e4 -- | % 215
    \stemUp fis4 -- ^ "II." _\ff \stemUp cis4 -- \stemUp e4 -- \stemUp
    dis4 -- | % 216
    \stemUp gis4 -- ^ "I." _\markup{ \italic {dim. un poco} } \stemDown
    cis4 -- \stemUp fis,4 -- \stemDown b4 -- \break | % 217
    \stemUp dis,4 -- ^ "II." _\markup{ \italic {dim. un poco} } \stemUp
    gis4 -- \stemUp d4 -- \stemUp gis4 -- | % 218
    \stemUp c4 -- _\f \stemUp cis4 -- \stemDown <fis, fis'>4 -- \stemUp
    <e e'>4 -- | % 219
    \stemDown <fis fis'>4 -- \stemUp <cis cis'>4 -- \stemUp <e e'>4 --
    \stemUp <dis dis'>4 -- | \barNumberCheck #220
    \stemUp <gis, gis'>4 -- _\markup{ \italic {dim.} } \stemUp <cis
        cis'>4 -- \stemUp <fis, fis'>4 -- \stemUp <b b'>4 -- \pageBreak
    | % 221
    \stemUp <dis, dis'>4 -- \stemUp <gis gis'>4 -- \stemUp <d d'>4 --
    \stemUp <gis gis'>4 -- | % 222
    \stemUp <d d'>4 -- \stemUp <gis gis'>4 -- \stemUp <d d'>4 -- \stemUp
    <gis gis'>4 -- | % 223
    \stemUp <d d'>4 -- _\p \stemUp <gis gis'>4 ~ -- ~ \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp <gis gis'>8 \stemUp <gis gis'>8 \stemUp <gis gis'>8 }
    \stemUp <gis gis'>4 -- | % 224
    R1 | % 225
    \stemUp <d d'>4 -- _\p \stemUp <gis gis'>4 ~ -- ~ \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp <gis gis'>8 \stemUp <gis gis'>8 \stemUp <gis gis'>8 }
    \stemUp <gis gis'>4 -- \break | % 226
    R1*3 | % 229
    \times 2/3  {
        r8 \stemUp <as as'>8 _\pp \stemUp <as as'>8 ~ ~ }
    \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ \once \omit TupletBracket
    \times 2/3  {
        \stemUp <as as'>8 \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ }
    \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ | \barNumberCheck #230
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <as as'>8 \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ }
    \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ \once \omit TupletBracket
    \times 2/3  {
        \stemUp <as as'>8 \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ }
    \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ \break | % 231
    \stemUp <as as'>8 r8 r4 r2 | % 232
    R1 | % 233
    \times 2/3  {
        r8 \stemUp <as as'>8 _\pp \stemUp <as as'>8 ~ ~ }
    \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ \once \omit TupletBracket
    \times 2/3  {
        \stemUp <as as'>8 \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ }
    \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ | % 234
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <as as'>8 \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ }
    \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ \once \omit TupletBracket
    \times 2/3  {
        \stemUp <as as'>8 \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ }
    \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ | % 235
    \stemUp <as as'>8 r8 r4 r2 | % 236
    R1 \pageBreak | % 237
    \times 2/3  {
        r8 _ "" _\markup{ \italic {poco cresc.} } \stemUp <bes bes'>8
        \stemUp <bes bes'>8 ~ ~ }
    \stemUp <bes bes'>8 \stemUp <bes bes'>8 ~ ~ \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp <bes bes'>8 \stemUp <bes bes'>8 \stemUp <bes bes'>8 ~ ~
        }
    \stemUp <bes bes'>8 \stemUp <bes bes'>8 ~ ~ | % 238
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <bes bes'>8 \stemUp <bes bes'>8 \stemUp <bes bes'>8 ~ ~
        }
    \stemUp <bes bes'>8 \stemUp <bes bes'>8 ( \once \omit TupletBracket
    \times 2/3  {
        \stemUp <ces ces'>8 ) _\mp \stemUp <ces ces'>8 \stemUp <ces
            ces'>8 ~ ~ }
    \stemUp <ces ces'>8 \stemUp <ces ces'>8 ( | % 239
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <bes bes'>8 ) _\markup{ \italic {cresc.} } \stemUp <bes
            bes'>8 \stemUp <bes bes'>8 ~ ~ }
    \stemUp <bes bes'>8 \stemUp <bes bes'>8 ~ ~ \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp <bes bes'>8 \stemUp <bes bes'>8 \stemUp <bes bes'>8 ( }
    \stemUp <c c'>8 ) \stemUp <c c'>8 ~ ~ | \barNumberCheck #240
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>8 ~ ~ }
    \stemUp <c c'>8 \stemUp <c c'>8 ( \once \omit TupletBracket
    \times 2/3  {
        \stemUp <des des'>8 ) \stemUp <des des'>8 \stemUp <des des'>8 ~
        ~ }
    \stemUp <des des'>8 \stemUp <des des'>8 | % 241
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <f f'>8 \stemDown <f f'>8 \stemDown <f f'>8 ~ ~ }
    \stemDown <f f'>8 \stemDown <f f'>8 ~ ~ \once \omit TupletBracket
    \times 2/3  {
        \stemDown <f f'>8 \stemDown <f f'>8 \stemDown <f f'>8 ~ ~ }
    \stemDown <f f'>8 \stemDown <f f'>8 \pageBreak | % 242
    \stemDown <f f'>8 _\f _\< r8 \stemDown <f f'>8 r8 \stemUp <bes,
        bes'>8 r8 _\! r4 | % 243
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis'8 _\ff \stemUp cis8 \stemUp cis8 ~ }
    \stemUp cis8 \stemUp cis8 ~ \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis8 \stemUp cis8 \stemUp cis8 ~ }
    \stemUp cis8 \stemUp cis8 | % 244
    \stemUp cis8 r8 \stemUp cis8 r8 \stemUp fis8 r8 \stemUp fis8 _\fff
    \stemUp fis8 | % 245
    \stemUp fis4 ( -> \stemUp gis,8 ) r8 r4 \stemUp fis'8 \stemUp fis8
    \pageBreak | % 246
    \stemUp fis4 ( -> \stemUp gis,8 ) r8 r4 r8 \stemUp d'8 | % 247
    r8 \stemUp <fis, a>8 r8 \stemUp <gis b>8 r8 \stemDown <a cis>8 r8
    \stemUp <eis eis'>8 | % 248
    r8 \stemDown <fis fis'>8 r8 \stemUp <gis b>8 \stemUp <gis cis>8 r8 r4
    | % 249
    r4 \stemUp <gis cis>8 _\f \stemUp <a cis>8 \stemDown <b cis>4 ->
    \stemDown <a cis>8 r8 | \barNumberCheck #250
    r4 \stemUp <gis cis>8 \stemUp <a cis>8 \stemDown <b cis>4 ->
    \stemDown <a cis>8 r8 | % 251
    r4 \stemDown <b e>8 \stemDown <cis e>8 \stemDown <d e>4 -> \stemDown
    <cis e>8 r8 \break | % 252
    r4 \stemDown <b e>8 \stemDown <cis e>8 \stemDown <d e>4 -> \stemDown
    <cis e>8 r8 | % 253
    r4 \stemUp cis8 \stemUp cis8 \stemUp cis8 ( -> \stemUp c8 ) r4 | % 254
    r4 \stemUp cis8 \stemUp cis8 \stemUp cis8 ( -> \stemUp c8 ) r4 | % 255
    r4 r8 \stemUp <dis, c'>8 _\f r8 \stemUp <e cis'>8 r4 | % 256
    r4 r8 \stemUp <a, cis'>8 r8 \stemUp <b b'>8 r4 \pageBreak | % 257
    r4 r8 \stemUp <cis a'>8 r8 \stemUp <dis b'>8 r4 | % 258
    r4 r8 \stemUp <gis, b'>8 r8 \stemUp <a a'>8 r4 _\pp | % 259
    r2 r4 \stemUp bes'4 ~ ^\p _\p | \barNumberCheck #260
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp bes8 \stemUp bes8 \stemUp bes8 }
    \stemUp bes4 ~ _\markup{ \italic {cresc.} } \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp bes8 \stemUp bes8 \stemUp bes8 }
    \stemUp cis4 ~ _\mp | % 261
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <cis, cis'>8 _\markup{ \italic {cresc.} } \stemUp <cis
            cis'>8 \stemUp <cis cis'>8 }
    \stemUp <cis cis'>4 ~ ~ \once \omit TupletBracket
    \times 2/3  {
        \stemUp <cis cis'>8 \stemUp <cis cis'>8 \stemUp <cis cis'>8 }
    \stemDown <cis' e>4 | % 262
    \stemDown <c e>4 \stemDown <b e>4 \stemDown <bes e>4 \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp <e, g>8 _\ff \stemUp <e g>8 \stemUp <e g>8 }
    \pageBreak | % 263
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e g>8 \stemUp <e g>16 \stemUp <e g>16 \stemUp <e g>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e g>8 \stemUp <e g>8 \stemUp <e g>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e g>8 \stemUp <e g>8 \stemUp <e g>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e g>8 \stemUp <e g>8 \stemUp <e g>8 }
    | % 264
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e g>8 \stemUp <e g>16 \stemUp <e g>16 \stemUp <e g>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e g>8 \stemUp <e g>8 \stemUp <e g>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e g>8 \stemUp <e g>8 \stemUp <e g>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g bes>8 \stemUp <g bes>8 \stemUp <g bes>8 }
    | % 265
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g bes>8 \stemUp <g bes>16 \stemUp <g bes>16 \stemUp <g
            bes>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g bes>8 \stemUp <g bes>8 \stemUp <g bes>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g bes>8 \stemUp <g bes>8 \stemUp <g bes>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g bes>8 \stemUp <g bes>8 \stemUp <g bes>8 }
    | % 266
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g bes>8 \stemUp <g bes>16 \stemUp <g bes>16 \stemUp <g
            bes>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g bes>8 \stemUp <g bes>8 \stemUp <g bes>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g bes>8 \stemUp <g bes>8 \stemUp <g bes>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g bes>8 \stemUp <g bes>8 \stemUp <g bes>8 }
    | % 267
    \stemUp <g bes>8 r8 r4 r2 \pageBreak | % 268
    R1 | % 269
    <g g'>1 _\fff | \barNumberCheck #270
    \stemUp bes8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp g'8 \stemUp g8 \stemUp g8 ~ }
    \stemUp g8 \stemUp g8 -> r4 | % 271
    r2 \stemUp g,4. ^ "" ^\markup{ \italic {pesante} } \stemUp a8 | % 272
    \stemUp bes2 r2 \pageBreak | % 273
    g1 | % 274
    \stemUp <g bes>8 _\ff r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g bes>8 \stemUp <g bes>8 \stemUp <g bes>8 ~ ~ }
    \stemUp <g bes>8 \stemUp <g bes>8 -> r4 | % 275
    r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g bes>8 \stemUp <g bes>8 \stemUp <g bes>8 }
    r4 r8 \stemUp <g bes>8 -> | % 276
    r4 \stemUp <g bes>8 -> r8 r2 | % 277
    R1*2 | % 279
    <b, b'>1 ~ ~ ^\ff | \barNumberCheck #280
    <b b'>1 | % 281
    <fis' fis'>1 ~ ~ _\markup{ \italic {sempre} } _ "" | % 282
    <fis fis'>1 | % 283
    <cis b'>1 ~ ~ | % 284
    <cis b'>1 \pageBreak | % 285
    fis1 ( | % 286
    \stemUp a8 ) r8 r4 r2 | % 287
    <cis, cis'>1 ~ ~ | % 288
    <cis cis'>1 | % 289
    <eis b'>1 ~ ~ | \barNumberCheck #290
    <eis b'>1 | % 291
    <cis cis'>1 ~ ~ | % 292
    <cis cis'>1 | % 293
    <gis' b>1 ~ ~ | % 294
    <gis b>1 | % 295
    <eis b'>1 ~ ~ | % 296
    <eis b'>1 | % 297
    <d b'>1 | % 298
    <b gis'>1 | % 299
    <fis d'>1 ~ ~ _\ffff _\> | \barNumberCheck #300
    \stemUp <fis d'>2 ~ ~ \stemUp <fis d'>8 _\! _\p r8 r4 | % 301
    <eis cis'>1 ~ ~ _\ff _\> \break | % 302
    <eis cis'>1 ~ ~ | % 303
    <eis cis'>1 ~ ~ | % 304
    \stemUp <eis cis'>8 _\! _\pp r8 r4 r2 ^\fermata \bar "||"
    \pageBreak | % 305
    \key c \major R1 | % 306
    r2 \stemUp <b' b'>2 _\pp | % 307
    \stemDown <fis' fis'>2 \stemUp <cis cis'>2 | % 308
    \stemDown <fis fis'>2 \stemUp <eis eis'>2 | % 309
    \stemDown <fis fis'>2 _\< \stemUp <cis e>2 _\! _\mp |
    \barNumberCheck #310
    \stemUp <b b'>2 _\markup{ \italic {poco cresc.} } \stemUp <b d>2
    \pageBreak | % 311
    \stemUp bes'2 \stemUp bes2 ~ _\mf _\> | % 312
    \stemUp bes8 _\! _\pp _\< r8 r4 \stemUp b2 _\! _\mp _\> | % 313
    \stemUp <bes, bes'>2 _\! _\p _\< \stemUp <a a'>8 _\! _\fff \stemUp
    <bes bes'>8 \stemUp <b b'>8 \stemUp <cis cis'>8 | % 314
    \stemUp <d d'>8 \stemUp <es es'>8 \stemUp <f f'>8 ( \stemUp <es es'>8
    ) \stemUp <g, g'>8 \stemUp <as as'>8 \stemUp <bes bes'>8 \stemUp <b
        b'>8 | % 315
    \stemUp <c c'>8 \stemUp <des des'>8 \stemUp <es es'>8 ( \stemUp <des
        des'>8 ) \stemUp <bes bes'>2 _\sfff _\> | % 316
    \stemUp <bes bes'>2 _\! _\f \stemUp <g g'>8 \stemUp <as as'>8
    \stemUp <bes bes'>8 ( _\> \stemUp <as as'>8 ) \pageBreak | % 317
    \stemUp <des des'>2 _\! _\mf \stemUp <bes des>2 | % 318
    \stemUp <b as'>2 \stemUp <gis b>2 | % 319
    \stemUp <ais fis'>2 \stemUp fis'2 | \barNumberCheck #320
    \stemUp fis2 \stemUp b,2 | % 321
    \stemUp fis'2 r2 _\mf | % 322
    R1*3 | % 325
    R1 \break | % 326
    r2 _\! _\p _\> \stemUp <dis c'>2 ( _\pp _\> | % 327
    \stemUp <cis cis'>8 ) _\! _\pppp r8 r4 r2 | % 328
    r2 \stemUp <eis b'>2 ( _\pp _\> | % 329
    \stemUp <fis bes>8 ) _\! _\pppp r8 r4 r2 | \barNumberCheck #330
    R1*4 \pageBreak | % 334
    R1 \bar "||"
    R1 | % 336
    r2 \stemDown b4. _\p ^ "I." _\< \stemDown b8 | % 337
    \stemDown fis'2. ~ _\! _\mp _\> \stemDown fis8 r8 _\! | % 338
    r2 \stemDown b,4. _\p _\< \stemDown b8 | % 339
    \stemDown fis'2. ~ _\! _\mp _\> \stemDown fis8 r8 _\! |
    \barNumberCheck #340
    R1*3 \pageBreak | % 343
    R1*3 | % 346
    \stemDown <fis, fis'>2. ~ ~ _\pp \stemDown <fis fis'>8 \stemDown
    <fis cis'>8 | % 347
    <fis bes>1 | % 348
    \stemUp <fis bes>2. ~ ~ \stemUp <fis bes>8 \stemUp <fis bes>8 | % 349
    \stemUp <fis bes>2. ~ ~ \stemUp <fis bes>8 r8 | \barNumberCheck #350
    R1*5 \bar "|."
    }

PartPSixVoiceTwo =  \relative a {
    \clef "treble" \time 4/4 \key c \major \transposition f s1*11 \break
    s1*7 \bar "||"
    s1*5 \pageBreak s1*6 | \barNumberCheck #30
    \time 2/4  s2 \break | % 31
    \time 4/4  s1*6 \break s1*7 \pageBreak s1*6 \break s1*4 \pageBreak
    s1*5 \break s1*5 \pageBreak s4*17 \stemDown a4 \stemDown gis4 ~
    \stemDown gis8 s8 \pageBreak s4*5 \stemDown c4 \stemDown b4 ~
    \stemDown b8 s8*5 \stemDown b4 ~ \stemDown b8 s8*5 \stemDown c4 ~
    \stemDown c8 s8 | % 73
    \stemDown e'4 ~ \stemDown e8 s8 \stemDown c,4 ~ \stemDown c8 s8
    \pageBreak s2*5 r2 | % 77
    R1 \break s1*5 \pageBreak s1*6 \bar "||"
    s1*5 \break s1*7 \bar "||"
    s1*2 \pageBreak s1*5 \break s1*4 \pageBreak s1*4 \break s1*4
    \pageBreak s1*5 \break s1*5 \bar "||"
    \time 12/8  s1*3 \pageBreak s1*9 \pageBreak s1*6 \bar "||"
    s1. | % 143
    \numericTimeSignature\time 4/4  s1*2 \break s1*11 \pageBreak s1*5
    \bar "||"
    \key c \major s1*4 \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*5
    \break s1*5 \pageBreak s1*4 \break s1*4 \pageBreak s1*5 \break s1*6
    \pageBreak s1*6 \pageBreak s1*4 \break s1 | % 218
    \stemDown c'4 -- \stemDown cis4 -- s2*5 \pageBreak s1*5 \break s1*5
    \break s1*6 \pageBreak s1*5 \pageBreak s1 | % 243
    \stemDown a2 \stemDown b4.. \stemDown b16 | % 244
    \stemDown fis8 s8 \stemDown eis8 s8 \stemDown fis8 s8 \stemDown fis8
    \stemDown fis8 | % 245
    \stemDown fis4 ( -> \stemDown eis8 ) s4. \stemDown cis'8 \stemDown d8
    \pageBreak | % 246
    \stemDown fis,4 ( -> \stemDown eis8 ) s2 \stemDown eis8 s1*5 \break
    s4*5 \stemDown gis8 \stemDown a8 \stemDown bes8 ( \stemDown c8 ) s2
    \stemDown gis8 \stemDown a8 \stemDown bes8 ( \stemDown c8 ) s4*9
    \pageBreak s4*7 \stemDown e,4 ~ | % 259
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 }
    \stemDown e4 ~ _\markup{ \italic {cresc.} } \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 }
    \stemDown bes4 ~ | \barNumberCheck #260
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown bes8 \stemDown bes8 \stemDown bes8 }
    \stemDown bes4 ~ \once \omit TupletBracket
    \times 2/3  {
        \stemDown bes8 \stemDown bes8 \stemDown bes8 }
    \stemDown cis4 ~ s1*2 \pageBreak s1*5 \pageBreak s1*2 |
    \barNumberCheck #270
    \stemDown bes'8 s8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 \stemDown g8 \stemDown g8 ~ }
    \stemDown g8 \stemDown g8 -> s4 | % 271
    R1 | % 272
    r2 \stemDown cis,4. \stemDown dis8 \pageBreak | % 273
    \stemDown e2. ( \stemDown dis8 ) r8 s1*4 | % 278
    r2 r4 \stemDown cis4 _\ff s1*6 \pageBreak | % 285
    cis1 ~ | % 286
    cis1 s1*15 \break s1*3 \bar "||"
    \pageBreak | % 305
    \key c \major s1*6 \pageBreak | % 311
    \stemDown bes2 \stemDown bes2 | % 312
    \stemDown bes2 \stemDown b2 s1*4 \pageBreak s2*5 \stemDown a4 (
    \stemDown b8 \stemDown a8 ) | \barNumberCheck #320
    \stemDown ais2 \stemDown gis2 | % 321
    \stemDown ais2 \stemDown cis2 | % 322
    \stemDown gis'2 \stemDown b,2 | % 323
    \stemDown fis'2 \stemDown fis2 | % 324
    \stemDown fis2 \stemDown b,2 _\> | % 325
    \stemDown ais2 ~ \stemDown ais8 _\! _\pp r8 r4 \break s1*8
    \pageBreak s1 \bar "||"
    s1*8 \pageBreak s1*12 \bar "|."
    }

PartPSevenVoiceOne =  \relative e {
    \clef "treble" \time 4/4 \key c \major \transposition f | % 1
    R1*11 \break | % 12
    R1*7 \bar "||"
    R1*5 \pageBreak | % 24
    R1*6 | \barNumberCheck #30
    \time 2/4  R2 \break | % 31
    \time 4/4  R1*6 \break | % 37
    R1*3 | \barNumberCheck #40
    r2 r8 \stemUp <e e'>16 -. _\f \stemUp <e e'>16 -. \stemUp <e e'>8 -.
    \stemUp <e e'>8 -. | % 41
    \stemUp <cis cis'>2 r2 | % 42
    R1*2 \pageBreak | % 44
    R1*6 \break | \barNumberCheck #50
    R1 | % 51
    r2 r8 \stemDown b''8 _\mp _\< \stemDown b8. \stemDown b16 | % 52
    \stemUp bes8. _\! _\> \stemUp g16 \stemUp g8. _\! \stemUp es16
    \stemUp es8 r8 r4 | % 53
    r2 r8 \stemDown b'8 _\mp _\< \stemDown b8. \stemDown b16 \pageBreak
    | % 54
    \stemUp bes8. _\! _\> \stemUp g16 \stemUp g8. _\! \stemUp es16
    \stemUp es8 r8 r4 | % 55
    R1*4 \break | % 59
    r2 r8 \stemUp ges8 ^ "IV." ^\markup{ \italic {espr.} } _\mp _\<
    \stemUp ges8. \stemUp ges16 | \barNumberCheck #60
    \stemUp f8. _\! _\> \stemUp d16 \stemUp d8. _\! \stemUp bes16
    \stemUp bes8 r8 r4 | % 61
    r2 r8 \stemUp ges'8 _\mp _\< \stemUp ges8. \stemUp ges16 | % 62
    \stemUp f8. _\! _\> \stemUp d16 \stemUp d8. _\! \stemUp bes16
    \stemUp bes8 r8 r4 | % 63
    R1 \pageBreak | % 64
    R1*4 | % 68
    r4 \stemUp f'4 _\f \stemUp fis8 -> \stemUp dis8 -> \stemUp e8 -> r8
    \pageBreak | % 69
    R1 | \barNumberCheck #70
    r4 \stemUp gis4 _\ff \stemUp a8 -> \stemUp fis8 -> \stemUp g8 -> r8
    | % 71
    r2 \stemUp a8 -> \stemUp fis8 -> \stemUp g8 -> r8 | % 72
    r2 \stemUp a8 -> \stemUp fis8 -> \stemUp g8 -> r8 | % 73
    \stemUp g'4 ~ \stemUp g8 r8 \stemUp a,8 -> \stemUp fis8 -> \stemUp g8
    -> r8 \pageBreak | % 74
    \stemDown <e' g>4 ~ ~ \stemDown <e g>8 r8 \stemDown <e g>4 ~ -> ~
    \stemDown <e g>8 r8 | % 75
    \stemDown <e g>4 ~ -> ~ \stemDown <e g>8 r8 \stemDown <d e>4 ~ -> ~
    \stemDown <d e>8 r8 | % 76
    \stemDown <d e>4 ~ -> ~ \stemDown <d e>8 r8 \stemUp g,4 ( -> ^\f
    \stemUp gis8 ) r8 | % 77
    \stemUp g4 ( -> \stemUp gis8 ) r8 r2 \break | % 78
    R1*5 \pageBreak | % 83
    R1*6 \bar "||"
    R1 | \barNumberCheck #90
    \stemUp <a, a'>2 _\pp _\< \stemUp <a fis'>2 _\! _\mp _\> | % 91
    \stemUp <a a'>8 _\! _\pp \stemUp <a a'>4 \stemUp <a a'>8 ~ ~ \stemUp
    <a a'>2 | % 92
    \stemUp <a a'>2 _\< \stemUp <gis gis'>2 _\! _\mp _\> | % 93
    \stemUp <a a'>8 _\! _\pp _\< \stemUp <a a'>4 \stemUp <a a'>8 \stemUp
    <e' e'>2 _\! _\mf \break | % 94
    \stemUp <d d'>2 \stemUp <d d'>2 _\> | % 95
    \stemUp <cis cis'>2 _\! _\p _\< \stemUp <a fis'>2 _\! _\mf _\> | % 96
    \stemUp <a e'>2 _\! _\p _\< \stemUp <gis gis'>2 _\! _\mf _\> | % 97
    \stemUp <a a'>8 _\! _\p _\< \stemUp <a a'>4 \stemUp <a a'>8 \stemUp
    <e' e'>2 _\! _\mf | % 98
    \stemUp <d d'>2 \stemUp <d d'>2 _\> | % 99
    \stemUp <cis cis'>2 _\! _\p _\< \stemUp <a fis'>2 _\! _\mf _\> |
    \barNumberCheck #100
    \stemUp <a e'>2 _\! _\p _\< \stemUp <gis gis'>2 _\! _\mf _\> \bar
    "||"
    \stemUp <a a'>8 _\! _\p r8 r4 r2 | % 102
    R1 \pageBreak | % 103
    R1*5 \break | % 108
    R1*4 \pageBreak | % 112
    R1*4 \break | % 116
    R1*4 \pageBreak | \barNumberCheck #120
    R1 | % 121
    r4 \stemDown b'2 _\mf ^ "III." ^\markup{ \italic {espress.} }
    \stemUp a4 -- | % 122
    \stemUp a4 ~ -> \stemUp a8. \stemUp gis16 \stemUp gis4 ~ \stemUp gis8
    r8 | % 123
    r4 \stemUp gis2 _\f \stemUp fis4 -- | % 124
    \stemUp fis4 ~ -> \stemUp fis8. \stemUp e16 \stemUp e2 ~ \break | % 125
    \stemUp e8 r8 \stemUp fis2 \stemUp e4 ~ | % 126
    \stemUp e8 r8 \stemUp fis2 ( \stemUp e4 ) | % 127
    R1*3 \bar "||"
    \time 12/8  r8*2/3 \stemUp <cis cis'>8 ^\markup{ \italic {pesante,
            non staccato} } _\p \stemUp <cis cis'>8 \stemUp <cis cis'>8
    \stemUp <cis cis'>8 \stemUp <cis cis'>8 \stemUp <cis cis'>4. ~ ~
    \stemUp <cis cis'>8 r8*2/3 r8*2/3 s8 | % 131
    r8*2/3 \stemUp <cis a'>8 \stemUp <cis a'>8 \stemUp <cis a'>8 \stemUp
    <cis a'>8 \stemUp <cis a'>8 r8*2/3 \stemUp <c fis>8 \stemUp <c fis>8
    \stemUp <c fis>8 \stemUp <c fis>8 \stemUp <c a'>8 s1*1/12 \pageBreak
    | % 132
    r8*2/3 \stemUp <cis a'>8 \stemUp <cis a'>8 \stemUp <cis a'>8 \stemUp
    <cis a'>8 \stemUp <cis a'>8 \stemUp <cis a'>8 r8*2/3 r8*2/3 r4*2/3 r8*2/3
    s4 | % 133
    r8*2/3 \stemUp <cis a'>8 \stemUp <cis a'>8 \stemUp <cis a'>8 \stemUp
    <cis a'>8 \stemUp <cis a'>8 r8*2/3 \stemUp <d b'>8 \stemUp <d b'>8
    \stemUp <d b'>8 \stemUp <d b'>8 \stemUp <d b'>8 s1*1/12 | % 134
    r8*2/3 \stemUp <cis a'>8 _\p _\< \stemUp <cis a'>8 \stemUp <cis a'>8
    \stemUp <cis a'>8 r8*2/3 _\! \stemUp <e e'>2. _\mf s1*1/12 | % 135
    \stemUp <d d'>8 \stemUp <d d'>8 \stemUp <d d'>8 \stemUp <d d'>8
    \stemUp <d d'>8 \stemUp <d d'>8 \stemUp <d d'>2. | % 136
    \stemUp <cis cis'>8 _\< \stemUp <cis cis'>8 \stemUp <cis cis'>8
    \stemUp <cis cis'>8 \stemUp <cis cis'>8 \stemUp <cis cis'>8 \stemUp
    <cis a'>2. _\! _\sf _\> | % 137
    \stemUp <cis a'>8 _\! _\p _\< \stemUp <cis a'>8 \stemUp <cis a'>8
    \stemUp <cis a'>8 \stemUp <cis a'>8 \stemUp <cis a'>8 \stemUp <gis
        gis'>2. _\! _\mf _\> \pageBreak | % 138
    r8*2/3 _\! \stemUp <cis a'>8 _\p _\< \stemUp <cis a'>8 \stemUp <cis
        a'>8 \stemUp <cis a'>8 r8*2/3 _\! \stemUp <e e'>2. _\mf s1*1/12
    | % 139
    \stemUp <d d'>8 \stemUp <d d'>8 \stemUp <d d'>8 \stemUp <d d'>8
    \stemUp <d d'>8 \stemUp <d d'>8 \stemUp <d d'>2. | \barNumberCheck
    #140
    \stemUp <cis cis'>8 _\< \stemUp <cis cis'>8 \stemUp <cis cis'>8
    \stemUp <cis cis'>8 \stemUp <cis cis'>8 \stemUp <cis cis'>8 \stemUp
    <cis a'>2. _\! _\sf _\> | % 141
    \stemUp <cis a'>8 _\! _\p _\< \stemUp <cis a'>8 \stemUp <cis a'>8
    \stemUp <cis a'>8 \stemUp <cis a'>8 \stemUp <cis a'>8 \stemUp <gis
        gis'>2. _\! _\mf _\> \bar "||"
    r8*2/3 _\! \stemUp <a a'>8 _\mf _\> \stemUp <a a'>8 \stemUp <a a'>8
    \stemUp <a a'>8 \stemUp <a a'>8 \stemUp <e' cis'>2. _\! _\mp s1*1/24
    | % 143
    \numericTimeSignature\time 4/4  r2 \stemUp <d b'>2 _\p _\> | % 144
    r2 _\! \stemUp <e cis'>2 \break | % 145
    \stemUp <fis b>2 \stemUp <d b'>2 | % 146
    \stemUp <e a>2 \stemUp <cis cis'>2 _\p | % 147
    \stemUp <d d'>2 \stemUp <b b'>2 | % 148
    \stemUp <cis cis'>2 _\> \stemUp <cis cis'>2 _\! _\pp | % 149
    \stemUp <b fis'>2 \stemUp <b b'>2 | \barNumberCheck #150
    \stemUp e4 ~ \stemUp e8 r8 r2 _\markup{ \italic {dim.} } | % 151
    \stemUp a,2 ^ "IV." \stemUp a2 | % 152
    \stemUp a2 _\ppp \stemUp a2 | % 153
    \stemUp a2 r2 | % 154
    R1*2 \pageBreak | % 156
    R1*5 \bar "||"
    \key c \major \stemDown <d' e>8 _\ff r8 r4 \stemUp <d, e>16 -> _\sff
    \stemUp <d e>16 \stemUp <d e>8 ~ ~ \stemUp <d e>4 ~ ~ | % 162
    \stemUp <d e>8 \stemUp <cis f>8 -> \stemUp <c e>8 -> \stemUp <cis f>8
    -> \stemUp <d e>8 -> r8 r4 | % 163
    \stemUp <cis e>8 _\sf r8 \stemUp <c es>8 _\sf r8 r4 r8 \stemUp <c
        es>8 _\sf | % 164
    \stemUp <cis e>8 _\sf r8 \stemUp <d bes'>8 _\sf r8 r4 \stemUp <d
        bes'>8 ( _\ff \stemUp <bes' d>8 ) \pageBreak | % 165
    \stemUp d,8 r8 r4 r2 | % 166
    R1*2 | % 168
    r2 r4 \stemUp <d b'>8 ( _\ff \stemUp <b' d>8 ) | % 169
    \stemUp <c, a'>8 r8 r4 \stemUp <c a'>16 _\sff \stemUp <c a'>16
    \stemUp <c a'>8 ~ ~ \stemUp <c a'>4 ~ ~ | \barNumberCheck #170
    \stemUp <c a'>8 \stemUp <d d'>8 -> \stemUp <c c'>8 -> \stemUp <d d'>8
    -> \stemUp <dis dis'>8 -> \stemUp <e e'>8 -> r4 | % 171
    R1 \pageBreak | % 172
    R1*3 | % 175
    r2 r8 \stemUp <a, a'>8 ~ ~ _\f \stemUp <a a'>8 r8 | % 176
    r2 r8 \stemUp <a a'>8 ~ ~ _\f \stemUp <a a'>8 \stemUp <e' e'>8 ~ ~
    _\mf | % 177
    \stemUp <e e'>4. \stemUp <e e'>8 ~ ~ \stemUp <e e'>4. \stemUp <e e'>8
    ~ ~ \pageBreak | % 178
    \stemUp <e e'>8 r8 r4 r2 | % 179
    R1*4 \break | % 183
    r2 r8 \stemUp <b b'>8 ~ ~ _\f \stemUp <b b'>8 r8 | % 184
    r2 r8 \stemUp <b b'>8 ~ ~ _\f \stemUp <b b'>8 r8 | % 185
    R1*3 \pageBreak | % 188
    R1 | % 189
    r2 r4 \stemUp <f' bes>4 ~ ~ _\fff | \barNumberCheck #190
    <f bes>1 ~ ~ | % 191
    \stemUp <f bes>2. \stemDown <bes d>4 ~ ~ \break | % 192
    <bes d>1 ~ ~ | % 193
    \stemDown <bes d>2. \stemDown <a c>4 | % 194
    <a c>1 | % 195
    <c e>1 \pageBreak | % 196
    \stemUp <c, c'>2 \stemUp <e a>2 | % 197
    \stemUp <c e>2 \stemUp <a c>8 -> \stemUp <a c>8 -> r4 | % 198
    R1*3 \break | % 201
    R1*4 | % 205
    r2 r4 r8. \stemUp <g' c>16 _\p | % 206
    \stemUp <g c>2 -> _\markup{ \italic {poco a poco cresc.} } \stemUp
    <gis b>2 \pageBreak | % 207
    r2 r4 r8. \stemDown <bes es>16 | % 208
    \stemDown <bes es>2 -> \stemDown <b d>2 | % 209
    r2 r4 r8. \stemUp <cis, cis'>16 _\mf | \barNumberCheck #210
    \stemUp <cis cis'>8 _\markup{ \italic {poco cresc.} } r8 \stemUp <d
        d'>8 r8 r4 r8. \stemUp <e e'>16 | % 211
    \stemUp <e e'>8 r8 \stemDown <f f'>8 r8 r2 | % 212
    R1 \pageBreak | % 213
    R1 | % 214
    \stemDown c'4 -- _\ff ^ "III." \stemDown cis4 -- \stemUp fis,4 --
    \stemUp e4 -- | % 215
    \stemUp fis4 -- ^ "IV." _\ff \stemUp cis4 -- \stemUp e4 -- \stemUp
    dis4 -- | % 216
    \stemUp gis4 -- ^ "III." _\markup{ \italic {dim. un poco} }
    \stemDown cis4 -- \stemUp fis,4 -- \stemDown b4 -- \break | % 217
    \stemUp dis,4 -- ^ "IV." _\markup{ \italic {dim. un poco} } \stemUp
    gis4 -- \stemUp d4 -- \stemUp gis4 -- | % 218
    R1*3 \pageBreak | % 221
    R1*3 | % 224
    \stemUp <d, d'>4 -- _\p \stemUp <gis gis'>4 ~ -- ~ \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp <gis gis'>8 \stemUp <gis gis'>8 \stemUp <gis gis'>8 }
    \stemUp <gis gis'>4 -- | % 225
    R1 \break | % 226
    \stemUp <dis dis'>4 -- _\markup{ \italic {dim.} } \stemUp <gis gis'>4
    ~ -- ~ \once \omit TupletBracket
    \times 2/3  {
        \stemUp <gis gis'>8 \stemUp <gis gis'>8 \stemUp <gis gis'>8 }
    \stemUp <gis gis'>4 ~ -- ~ _\pp | % 227
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <gis gis'>8 \stemUp <gis gis'>8 \stemUp <gis gis'>8 ~ ~
        }
    \stemUp <gis gis'>8 \stemUp <gis gis'>8 ~ ~ \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp <gis gis'>8 \stemUp <gis gis'>8 \stemUp <gis gis'>8 ~ ~
        }
    \stemUp <gis gis'>8 \stemUp <gis gis'>8 ~ ~ | % 228
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <gis gis'>8 \stemUp <gis gis'>8 \stemUp <gis gis'>8 ~ ~
        }
    \stemUp <gis gis'>8 \stemUp <gis gis'>8 ~ ~ \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp <gis gis'>8 \stemUp <gis gis'>8 \stemUp <gis gis'>8 ~ ~
        }
    \stemUp <gis gis'>8 \stemUp <gis gis'>8 ~ ~ | % 229
    \stemUp <gis gis'>8 r8 r4 r2 | \barNumberCheck #230
    R1 \break | % 231
    \times 2/3  {
        r8 \stemUp <as as'>8 _\pp \stemUp <as as'>8 ~ ~ }
    \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ \once \omit TupletBracket
    \times 2/3  {
        \stemUp <as as'>8 \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ }
    \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ | % 232
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <as as'>8 \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ }
    \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ \once \omit TupletBracket
    \times 2/3  {
        \stemUp <as as'>8 \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ }
    \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ | % 233
    \stemUp <as as'>8 r8 r4 r2 | % 234
    R1 | % 235
    \times 2/3  {
        r8 \stemUp <as as'>8 _\pp \stemUp <as as'>8 ~ ~ }
    \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ \once \omit TupletBracket
    \times 2/3  {
        \stemUp <as as'>8 \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ }
    \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ | % 236
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <as as'>8 _\< \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ }
    \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ \once \omit TupletBracket
    \times 2/3  {
        \stemUp <as as'>8 \stemUp <as as'>8 \stemUp <as as'>8 ~ ~ }
    \stemUp <as as'>8 \stemUp <a a'>8 ( \pageBreak | % 237
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <bes bes'>8 ) _\! _ "" _\markup{ \italic {poco cresc.}
            } \stemUp <bes bes'>8 \stemUp <bes bes'>8 ~ ~ }
    \stemUp <bes bes'>8 \stemUp <bes bes'>8 ~ ~ \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp <bes bes'>8 \stemUp <bes bes'>8 \stemUp <bes bes'>8 ~ ~
        }
    \stemUp <bes bes'>8 \stemUp <bes bes'>8 ~ ~ | % 238
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <bes bes'>8 \stemUp <bes bes'>8 \stemUp <bes bes'>8 ~ ~
        }
    \stemUp <bes bes'>8 \stemUp <bes bes'>8 ( \once \omit TupletBracket
    \times 2/3  {
        \stemUp <ces ces'>8 ) _\mp \stemUp <ces ces'>8 \stemUp <ces
            ces'>8 ~ ~ }
    \stemUp <ces ces'>8 \stemUp <ces ces'>8 ( | % 239
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <bes bes'>8 ) _\markup{ \italic {cresc.} } \stemUp <bes
            bes'>8 \stemUp <bes bes'>8 ~ ~ }
    \stemUp <bes bes'>8 \stemUp <bes bes'>8 ~ ~ \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp <bes bes'>8 \stemUp <bes bes'>8 \stemUp <bes bes'>8 ( }
    \stemUp <c c'>8 ) \stemUp <c c'>8 ~ ~ | \barNumberCheck #240
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>8 ~ ~ }
    \stemUp <c c'>8 \stemUp <c c'>8 ( \once \omit TupletBracket
    \times 2/3  {
        \stemUp <des des'>8 ) \stemUp <des des'>8 \stemUp <des des'>8 ~
        ~ }
    \stemUp <des des'>8 \stemUp <des des'>8 | % 241
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <f f'>8 \stemDown <f f'>8 \stemDown <f f'>8 ~ ~ }
    \stemDown <f f'>8 \stemDown <f f'>8 ~ ~ \once \omit TupletBracket
    \times 2/3  {
        \stemDown <f f'>8 \stemDown <f f'>8 \stemDown <f f'>8 ~ ~ }
    \stemDown <f f'>8 \stemDown <f f'>8 \pageBreak | % 242
    \stemDown <f f'>8 _\f _\< r8 \stemDown <f f'>8 r8 \stemUp <bes,
        bes'>8 r8 _\! r4 | % 243
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis'8 _\ff \stemUp cis8 \stemUp cis8 ~ }
    \stemUp cis8 \stemUp cis8 ~ \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis8 \stemUp cis8 \stemUp cis8 ~ }
    \stemUp cis8 \stemUp cis8 | % 244
    \stemUp cis8 r8 \stemUp cis8 r8 \stemUp fis8 r8 \stemUp fis8 _\fff
    \stemUp fis8 | % 245
    \stemUp fis4 ( -> \stemUp gis,8 ) r8 r4 \stemUp fis'8 \stemUp fis8
    \pageBreak | % 246
    \stemUp fis4 ( -> \stemUp gis,8 ) r8 r4 r8 \stemUp d'8 | % 247
    r8 \stemUp <fis, a>8 r8 \stemUp <gis b>8 r8 \stemDown <a cis>8 r8
    \stemUp <d, d'>8 | % 248
    r8 \stemUp <cis cis'>8 r8 \stemUp <gis' b>8 \stemUp <gis cis>8 r8 r4
    | % 249
    r4 \stemUp <eis cis'>8 _\f \stemUp <fis cis'>8 \stemUp <gis cis>4 ->
    \stemUp <fis cis'>8 r8 | \barNumberCheck #250
    r4 \stemUp <eis cis'>8 \stemUp <fis cis'>8 \stemUp <gis cis>4 ->
    \stemDown <a cis>8 r8 | % 251
    r4 \stemDown <gis e'>8 \stemDown <a e'>8 \stemDown <b e>4 ->
    \stemDown <a e'>8 r8 \break | % 252
    r4 \stemDown <gis e'>8 \stemDown <a e'>8 \stemDown <b e>4 ->
    \stemDown <cis e>8 r8 | % 253
    r4 \stemUp <e, cis'>8 \stemUp <fis cis'>8 \stemUp <g cis>8 ( ->
    \stemUp <gis c>8 ) r4 | % 254
    r4 \stemUp <e cis'>8 \stemUp <fis cis'>8 \stemUp <g cis>8 ( ->
    \stemUp <gis c>8 ) r4 | % 255
    r4 r8 \stemUp <dis fis>8 _\f r8 \stemUp <e gis>8 r4 | % 256
    r4 r8 \stemUp <a, fis'>8 r8 \stemUp <b fis'>8 r4 \pageBreak | % 257
    r4 r8 \stemUp <cis e>8 r8 \stemUp <dis fis>8 r4 | % 258
    r4 r8 \stemUp <gis, e'>8 r8 \stemUp <a e'>8 r4 _\pp | % 259
    r2 r4 \stemUp bes'4 ~ ^\p _\p | \barNumberCheck #260
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp bes8 \stemUp bes8 \stemUp bes8 }
    \stemUp bes4 ~ _\markup{ \italic {cresc.} } \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp bes8 \stemUp bes8 \stemUp bes8 }
    \stemUp cis4 ~ _\mp | % 261
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <cis, cis'>8 _\markup{ \italic {cresc.} } \stemUp <cis
            cis'>8 \stemUp <cis cis'>8 }
    \stemUp <cis cis'>4 ~ ~ \once \omit TupletBracket
    \times 2/3  {
        \stemUp <cis cis'>8 \stemUp <cis cis'>8 \stemUp <cis cis'>8 }
    \stemUp <e e'>4 | % 262
    \stemUp <e e'>4 \stemUp <e e'>4 \stemUp <e e'>4 \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp <e g>8 _\ff \stemUp <e g>8 \stemUp <e g>8 }
    \pageBreak | % 263
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e g>8 \stemUp <e g>16 \stemUp <e g>16 \stemUp <e g>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e g>8 \stemUp <e g>8 \stemUp <e g>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e g>8 \stemUp <e g>8 \stemUp <e g>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e g>8 \stemUp <e g>8 \stemUp <e g>8 }
    | % 264
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e g>8 \stemUp <e g>16 \stemUp <e g>16 \stemUp <e g>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e g>8 \stemUp <e g>8 \stemUp <e g>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e g>8 \stemUp <e g>8 \stemUp <e g>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g bes>8 \stemUp <g bes>8 \stemUp <g bes>8 }
    | % 265
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g bes>8 \stemUp <g bes>16 \stemUp <g bes>16 \stemUp <g
            bes>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g bes>8 \stemUp <g bes>8 \stemUp <g bes>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g bes>8 \stemUp <g bes>8 \stemUp <g bes>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g bes>8 \stemUp <g bes>8 \stemUp <g bes>8 }
    | % 266
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g bes>8 \stemUp <g bes>16 \stemUp <g bes>16 \stemUp <g
            bes>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g bes>8 \stemUp <g bes>8 \stemUp <g bes>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g bes>8 \stemUp <g bes>8 \stemUp <g bes>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g bes>8 \stemUp <g bes>8 \stemUp <g bes>8 }
    | % 267
    \stemUp <g bes>8 r8 r4 r2 \pageBreak | % 268
    R1 | % 269
    <g g'>1 _\fff | \barNumberCheck #270
    \stemUp bes8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 \stemUp e8 \stemUp e8 ~ }
    \stemUp e8 \stemUp e8 -> r4 | % 271
    r2 \stemUp g,4. ^ "" ^\markup{ \italic {pesante} } \stemUp a8 | % 272
    \stemUp bes2 r2 \pageBreak | % 273
    g1 | % 274
    \stemUp <e bes'>8 _\ff r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e bes'>8 \stemUp <e bes'>8 \stemUp <e bes'>8 ~ ~ }
    \stemUp <e bes'>8 \stemUp <e bes'>8 -> r4 | % 275
    r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e bes'>8 \stemUp <e bes'>8 \stemUp <e bes'>8 }
    r4 r8 \stemUp <e bes'>8 -> | % 276
    r4 \stemUp <e bes'>8 -> r8 r2 | % 277
    R1*2 | % 279
    <b b'>1 ~ ~ ^\ff | \barNumberCheck #280
    <b b'>1 | % 281
    <dis dis'>1 ~ ~ _\markup{ \italic {sempre} } _ "" | % 282
    <dis dis'>1 | % 283
    <cis b'>1 ~ ~ | % 284
    <cis b'>1 \pageBreak | % 285
    fis1 ( | % 286
    \stemUp a8 ) r8 r4 r2 | % 287
    <cis, cis'>1 ~ ~ | % 288
    <cis cis'>1 | % 289
    <eis b'>1 ~ ~ | \barNumberCheck #290
    <eis b'>1 | % 291
    <cis b'>1 ~ ~ | % 292
    <cis b'>1 | % 293
    <gis' b>1 ~ ~ | % 294
    <gis b>1 | % 295
    <eis b'>1 ~ ~ | % 296
    <eis b'>1 | % 297
    <b gis'>1 | % 298
    <gis eis'>1 | % 299
    <fis d'>1 ~ ~ _\ffff _\> | \barNumberCheck #300
    \stemUp <fis d'>2 ~ ~ \stemUp <fis d'>8 _\! _\p r8 r4 | % 301
    <eis cis'>1 ~ ~ _\ff _\> \break | % 302
    <eis cis'>1 ~ ~ | % 303
    <eis cis'>1 ~ ~ | % 304
    \stemUp <eis cis'>8 _\! _\pp r8 r4 r2 ^\fermata \bar "||"
    \pageBreak | % 305
    \key c \major R1 | % 306
    r2 \stemUp <b' b'>2 _\pp | % 307
    \stemDown <fis' fis'>2 \stemUp <cis cis'>2 | % 308
    \stemDown <fis fis'>2 \stemUp <eis eis'>2 | % 309
    \stemDown <fis fis'>2 _\< \stemUp <cis e>2 _\! _\mp |
    \barNumberCheck #310
    \stemUp <b b'>2 _\markup{ \italic {poco cresc.} } \stemUp <b d>2
    \pageBreak | % 311
    \stemUp bes'2 \stemUp bes2 ~ _\mf _\> | % 312
    \stemUp bes8 _\! _\pp _\< r8 r4 \stemUp f2 _\! _\mp _\> | % 313
    \stemUp <fis, fis'>2 _\! _\p _\< \stemUp <a a'>8 _\! _\fff \stemUp
    <bes bes'>8 \stemUp <b b'>8 \stemUp <cis cis'>8 | % 314
    \stemUp <d d'>8 \stemUp <es es'>8 \stemUp <f f'>8 ( \stemUp <es es'>8
    ) \stemUp <g, g'>8 \stemUp <as as'>8 \stemUp <bes bes'>8 \stemUp <b
        b'>8 | % 315
    \stemUp <c c'>8 \stemUp <des des'>8 \stemUp <es es'>8 ( \stemUp <des
        des'>8 ) \stemUp <bes bes'>2 _\sfff _\> | % 316
    \stemUp <bes bes'>2 _\! _\f \stemUp <g g'>8 \stemUp <as as'>8
    \stemUp <bes bes'>8 ( _\> \stemUp <as as'>8 ) \pageBreak | % 317
    \stemUp <des ges>2 _\! _\mf \stemUp <bes des>2 | % 318
    \stemUp <b as'>2 \stemUp <gis b>2 | % 319
    \stemUp <ais fis'>2 \stemUp fis'2 | \barNumberCheck #320
    \stemUp fis2 \stemUp b,2 | % 321
    \stemUp fis'2 r2 _\mf | % 322
    R1*3 | % 325
    R1 \break | % 326
    r4 _\! _\p _\> \stemUp <fis, cis'>4 _\pppp _\< \stemUp <fis c'>2 _\!
    _\pp _\> | % 327
    \stemUp <fis cis'>2 ~ ~ _\! _\pppp \stemUp <fis cis'>8 r8 r4 | % 328
    \stemUp <fis cis'>2 _\pppp _\< \stemUp <fis cis'>2 _\! _\pp _\> | % 329
    \stemUp <fis cis'>2 _\! _\pppp _\< \stemUp <fis cis'>2 _\! _\pp |
    \barNumberCheck #330
    \stemUp <fis dis'>2 \stemUp <fis b>2 | % 331
    \stemUp <fis cis'>2 _\< \stemUp <fis dis'>2 _\! _\p _\> | % 332
    \stemUp <fis cis'>2 _\! _\pppp _\< \stemUp <gis cis>2 _\! _\pp _\> | % 333
    \stemUp <fis cis'>2 _\! _\pppp _\< \stemUp <fis cis'>4.. -> _\! _\pp
    _\> \stemUp <fis cis'>16 \pageBreak | % 334
    \stemUp <fis cis'>2 _\! _\pppp _\< \stemUp <fis cis'>4.. -> _\! _\pp
    _\> \stemUp <fis cis'>16 \bar "||"
    \stemUp <fis cis'>4 ~ ~ _\! _\pppp \stemUp <fis cis'>8 r8 r2 | % 336
    R1*7 \pageBreak | % 343
    R1*3 | % 346
    \stemUp <cis' bes'>2. ~ ~ _\pp \stemUp <cis bes'>8 \stemUp <cis
        bes'>8 | % 347
    R1*8 \bar "|."
    }

PartPSevenVoiceTwo =  \relative a {
    \clef "treble" \time 4/4 \key c \major \transposition f s1*11 \break
    s1*7 \bar "||"
    s1*5 \pageBreak s1*6 | \barNumberCheck #30
    \time 2/4  s2 \break | % 31
    \time 4/4  s1*6 \break s1*7 \pageBreak s1*6 \break s1*4 \pageBreak
    s1*5 \break s1*5 \pageBreak s4*17 \stemDown a4 \stemDown gis4 ~
    \stemDown gis8 s8 \pageBreak s4*5 \stemDown c4 \stemDown b4 ~
    \stemDown b8 s8*5 \stemDown b4 ~ \stemDown b8 s8*5 \stemDown c4 ~
    \stemDown c8 s8 | % 73
    \stemDown e'4 ~ \stemDown e8 s8 \stemDown c,4 ~ \stemDown c8 s8
    \pageBreak s2*5 r2 | % 77
    R1 \break s1*5 \pageBreak s1*6 \bar "||"
    s1*5 \break s1*7 \bar "||"
    s1*2 \pageBreak s1*5 \break s1*4 \pageBreak s1*4 \break s1*4
    \pageBreak s1*5 \break s1*5 \bar "||"
    \time 12/8  s1*3 \pageBreak s1*9 \pageBreak s1*6 \bar "||"
    s1. | % 143
    \numericTimeSignature\time 4/4  s1*2 \break s1*5 | \barNumberCheck
    #150
    \stemDown a2 \stemDown a2 s1*5 \pageBreak s1*5 \bar "||"
    \key c \major s1*4 \pageBreak | % 165
    \stemDown b'8 s8*55 \pageBreak s1*6 \pageBreak s1*5 \break s1*5
    \pageBreak s1*4 \break s1*4 \pageBreak s1*5 \break s1*6 \pageBreak
    s1*6 \pageBreak s1*4 \break s1*4 \pageBreak s1*5 \break s1*5 \break
    s1*6 \pageBreak s1*5 \pageBreak s1 | % 243
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 \stemDown cis8 \stemDown cis8 ~ }
    \stemDown cis8 \stemDown cis8 ~ \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 \stemDown cis8 \stemDown cis8 ~ }
    \stemDown cis8 \stemDown cis8 | % 244
    \stemDown fis,8 s8 \stemDown eis8 s8 \stemDown fis8 s8 \stemDown fis8
    \stemDown fis8 | % 245
    \stemDown fis4 ( -> \stemDown eis8 ) s4. \stemDown cis'8 \stemDown d8
    \pageBreak | % 246
    \stemDown fis,4 ( -> \stemDown eis8 ) s2 \stemDown eis8 s1*5 \break
    s1*5 \pageBreak s4*7 \stemDown e4 ~ | % 259
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 }
    \stemDown e4 ~ _\markup{ \italic {cresc.} } \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 }
    \stemDown bes4 ~ | \barNumberCheck #260
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown bes8 \stemDown bes8 \stemDown bes8 }
    \stemDown bes4 ~ \once \omit TupletBracket
    \times 2/3  {
        \stemDown bes8 \stemDown bes8 \stemDown bes8 }
    \stemDown cis4 ~ s1*2 \pageBreak s1*5 \pageBreak s1*2 |
    \barNumberCheck #270
    \stemDown bes'8 s8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown e,8 \stemDown e8 \stemDown e8 ~ }
    \stemDown e8 \stemDown e8 -> s4 | % 271
    R1 | % 272
    r2 \stemDown cis4. \stemDown dis8 \pageBreak | % 273
    \stemDown e2. ( \stemDown dis8 ) r8 s1*4 | % 278
    r2 r4 \stemDown cis4 _\ff s1*6 \pageBreak | % 285
    cis1 ~ | % 286
    cis1 s1*15 \break s1*3 \bar "||"
    \pageBreak | % 305
    \key c \major s1*6 \pageBreak | % 311
    \stemDown bes2 \stemDown bes2 | % 312
    \stemDown bes2 \stemDown f2 s1*4 \pageBreak s2*5 \stemDown a4 (
    \stemDown b8 \stemDown a8 ) | \barNumberCheck #320
    \stemDown ais2 \stemDown gis2 | % 321
    \stemDown ais2 \stemDown cis2 | % 322
    \stemDown b2 \stemDown gis2 | % 323
    \stemDown ais2 \stemDown a4 ( \stemDown b8 \stemDown a8 ) | % 324
    \stemDown ais2 \stemDown gis2 _\> | % 325
    \stemDown ais2 ~ \stemDown ais8 _\! _\pp r8 r4 \break s1*8
    \pageBreak s1 \bar "||"
    s1*8 \pageBreak s1*4 | % 347
    cis1 | % 348
    \stemDown cis2. ~ \stemDown cis8 \stemDown cis8 | % 349
    \stemDown cis2. ~ \stemDown cis8 r8 s1*5 \bar "|."
    }

PartPEightVoiceOne =  \relative f'' {
    \clef "treble" \time 4/4 \key c \major \transposition bes | % 1
    R1*11 \break | % 12
    R1*7 \bar "||"
    R1*5 \pageBreak | % 24
    R1*6 | \barNumberCheck #30
    \time 2/4  R2 \break | % 31
    \time 4/4  R1*6 \break | % 37
    R1*7 \pageBreak | % 44
    R1*6 \break | \barNumberCheck #50
    R1*4 \pageBreak | % 54
    R1*5 \break | % 59
    R1*5 \pageBreak | % 64
    R1*3 | % 67
    r2 r4 \stemUp f8 ^\f \stemUp g8 | % 68
    \stemUp as4 \stemUp g4 \stemUp as8 r8 r4 \pageBreak | % 69
    r2 r4 \stemUp as8 ^\ff \stemUp bes8 | \barNumberCheck #70
    \stemUp ces4 \stemUp bes4 \stemUp ces8 r8 r4 | % 71
    \stemUp b4 -> \stemUp d,4 -> r2 | % 72
    \stemUp b'4 -> \stemUp d,4 -> r2 | % 73
    \stemDown <g, g'>8 -> \stemDown <eis eis'>8 -> \stemDown <fis fis'>8
    -> r8 r2 \pageBreak | % 74
    \stemDown <g g'>8 -> \stemDown <eis eis'>8 -> \stemDown <fis fis'>8
    -> r8 \stemUp <eis eis'>4 ( -> \stemDown <fis fis'>8 ) r8 | % 75
    \stemUp <eis eis'>4 ( -> \stemDown <fis fis'>8 ) r8 \stemUp <d d'>4
    ( -> \stemUp <es es'>8 ) r8 | % 76
    \stemUp <d d'>4 ( -> \stemUp <es es'>8 ) r8 r2 | % 77
    R1 \break | % 78
    R1*5 \pageBreak | % 83
    R1*6 \bar "||"
    R1*5 \break | % 94
    R1*7 \bar "||"
    R1*2 \pageBreak | % 103
    R1*4 | % 107
    r2 \stemUp a4 -- ^\mf \stemUp ais4 -- \break | % 108
    \stemUp b4 -- ^\> \stemUp cis4 -- \stemUp d4 -- \stemUp dis4 -- ^\!
    ^\p | % 109
    R1*3 \pageBreak | % 112
    R1*3 | % 115
    r2 \stemUp e,4 -- _\mf ^ "I." \stemUp eis4 -- \break | % 116
    \stemUp fis4 -- _\> \stemUp gis4 -- \stemUp a4 -- \stemUp ais4 --
    _\! _\p | % 117
    R1*3 \pageBreak | \barNumberCheck #120
    R1*5 \break | % 125
    R1*5 \bar "||"
    R1*2 \pageBreak | % 132
    R1*2 | % 134
    r2 \stemUp gis4 ^ "I." ^\markup{ \italic {marcato} } _\mf \stemUp a8
    \stemUp b8 | % 135
    \stemUp cis,8 _\p r8 r4 \stemUp fis4 _\mf ^\markup{ \italic
        {marcato} } \stemUp gis8 \stemUp a8 | % 136
    \stemUp b,8 _\p r8 r4 r2 | % 137
    r2 \stemUp <eis eis'>4 ( _\mf _\> \stemDown <fis fis'>8 ) _\! _\p r8
    \pageBreak | % 138
    r2 \stemUp gis4 ^ "I." ^\markup{ \italic {marcato} } _\mf \stemUp a8
    \stemUp b8 | % 139
    \stemUp cis,8 _\p r8 r4 \stemUp fis4 _\mf ^\markup{ \italic
        {marcato} } \stemUp gis8 \stemUp a8 | \barNumberCheck #140
    \stemUp b,8 _\p r8 r4 r2 | % 141
    r2 \stemUp <eis eis'>4 ( _\mf _\> \stemDown <fis fis'>8 ) _\! _\p r8
    \bar "||"
    r2 \stemDown <b gis'>2 _\mp | % 143
    \stemDown <a a'>2 \stemDown <a fis'>2 | % 144
    \stemDown <gis gis'>2 _\> \stemDown <b gis'>2 _\! _\p \break | % 145
    \stemDown <cis fis>2 \stemDown <a fis'>2 | % 146
    \stemDown <b e>2 r2 | % 147
    R1*9 \pageBreak | % 156
    R1*5 \bar "||"
    \key c \major \stemDown <f f'>8 _\ff r8 r4 r2 | % 162
    R1*3 \pageBreak | % 165
    \stemDown <a fis'>8 _\ff r8 r4 r2 | % 166
    R1*3 | % 169
    \stemDown <g e'>8 _\ff r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g e'>16 _\sff \stemDown <g e'>16 \stemDown <g e'>16 }
    \stemDown <g e'>8 ~ ~ \stemDown <g e'>4 ~ ~ | \barNumberCheck #170
    \stemUp <g e'>8 \stemUp <fis e'>8 -> \stemUp <g e'>8 -> \stemUp <fis
        e'>8 -> \stemDown <g e'>8 -> \stemDown <g e'>8 -> r4 | % 171
    R1 \pageBreak | % 172
    R1*2 | % 174
    \stemUp fis'8 -. ^\mf _\mf r8 r4 r2 | % 175
    R1*3 \pageBreak | % 178
    \stemUp cis8 -. ^\mf \stemUp g'8 -. _\mf \stemUp d8 -. r8 r2 | % 179
    R1*3 | % 182
    \stemUp gis8 -. ^\mf _\mf r8 r4 r2 \break | % 183
    R1*5 \pageBreak | % 188
    R1*2 | \barNumberCheck #190
    \stemDown <c, c'>2 -> _ "" _\markup{ \italic {marcatissimo} }
    \stemDown <b b'>4 -> \stemDown <a a'>4 -> | % 191
    \stemDown <g g'>2 -> \stemDown <f f'>2 -> \break | % 192
    \stemDown <f f'>2 -> \stemUp <e e'>4 -> \stemUp <d d'>4 -> | % 193
    \stemUp <des des'>2 -> \stemUp <c c'>2 -> | % 194
    \stemDown <c' c'>2 -> \stemDown <b b'>4 -> \stemDown <a a'>4 -> | % 195
    \stemDown <g g'>4 -> \stemDown <fis fis'>4 -> \stemUp <e e'>4 ->
    \stemUp <d d'>4 -> \pageBreak | % 196
    \stemUp c'4 -> \stemUp b4 -> \stemUp a4 -> \stemUp g4 -> | % 197
    \stemUp fis4 -> ^\markup{ \bold\small {a. 2} } \stemUp e4 -> \stemUp
    c8 -> \stemUp b8 -> r4 | % 198
    R1*3 \break | % 201
    r2 r4 \stemUp b4 ~ _\p ^\markup{ \italic {cantabile} } | % 202
    \stemUp b2 \stemUp b2 | % 203
    \stemUp b2 \stemUp e2 | % 204
    \stemUp c2 \stemUp c2 | % 205
    r2 r4 r8. \stemUp <g' b>16 _\p | % 206
    \stemUp <g b>2 -> _\markup{ \italic {poco a poco cresc.} } \stemUp
    <fis a>2 \pageBreak | % 207
    \stemUp <e g>2 \stemUp fis4 ~ \stemUp fis8. \stemUp d'16 | % 208
    \stemDown <bes d>2 -> \stemDown <a c>2 | % 209
    \stemUp <g bes>2 \stemUp a4 ~ \stemUp a8. \stemUp f'16 _\mf |
    \barNumberCheck #210
    \stemUp f8 _\markup{ \italic {poco cresc.} } r8 \stemUp es8 r8
    \stemUp des8 r8 \stemUp c8 r16 \stemUp as'16 | % 211
    \stemUp as8 r8 \stemUp ges8 r8 \stemUp fes8 r8 \stemUp es8 r8 | % 212
    \stemUp ges8 r8 \stemUp f8 r8 \stemUp as8 _\f _\< r8 \stemUp g8 r8
    \pageBreak | % 213
    \stemUp as8 r8 \stemUp g8 r8 \stemUp as8 r8 \stemUp g8 r8 | % 214
    R1*3 \break | % 217
    R1*4 \pageBreak | % 221
    R1*5 \break | % 226
    R1*5 \break | % 231
    R1*6 \pageBreak | % 237
    R1 | % 238
    r2 _\! \stemUp es,4 ~ -> _\mp ^ "I." \stemUp es8. \stemUp es16 | % 239
    \stemUp as2. -> _\markup{ \italic {cresc.} } \stemUp f4 |
    \barNumberCheck #240
    \stemDown c'2 -> \stemDown b2 -> | % 241
    \stemDown c2 _\mf _\< \stemDown bes4.. \stemDown bes16 \pageBreak | % 242
    \stemDown f'8 _\! _\f _\< r8 \stemDown e8 r8 \stemDown f8 r8 _\! r4
    | % 243
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp as8 _\ff \stemUp as8 \stemUp as8 ~ }
    \stemUp as8 \stemUp as8 ~ \once \omit TupletBracket
    \times 2/3  {
        \stemUp as8 \stemUp as8 \stemUp as8 ~ }
    \stemUp as8 \stemUp as8 | % 244
    \stemUp as8 r8 \stemUp as8 r8 \stemUp des,8 r8 \stemUp des8 _\fff
    \stemUp es8 | % 245
    \stemUp fes4 ( -> \stemUp es8 ) r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp des8 \stemUp ges8 \stemUp des8 }
    \pageBreak | % 246
    \stemUp fes4 ( -> \stemUp es8 ) r8 r4 r8 \stemUp a8 | % 247
    r8 \stemDown <cis, e>8 r8 \stemDown <dis fis>8 r8 \stemDown <e gis>8
    r8 \stemUp <a, bis>8 | % 248
    r8 \stemUp <gis cis>8 r4 r2 | % 249
    R1*3 \break | % 252
    R1*5 \pageBreak | % 257
    R1*3 | \barNumberCheck #260
    r4 \stemUp gis2 _ "" _\markup{ \italic {cresc.} } \stemUp f'4 _\mp
    | % 261
    \stemDown <b, f'>4 _\markup{ \italic {cresc.} } \stemDown <b e>4
    \stemDown <b dis>4 \stemUp <d, d'>4 ~ ~ | % 262
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d d'>8 \stemUp <d d'>8 \stemUp <d d'>8 }
    \stemUp <d d'>4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d d'>8 \stemUp <d d'>8 \stemUp <d d'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <b' d>8 _\ff \stemDown <b d>8 \stemDown <b d>8 }
    \pageBreak | % 263
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <b d>8 \stemDown <b d>16 \stemDown <b d>16 \stemDown
        <b d>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <b d>8 \stemDown <b d>8 \stemDown <b d>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <b d>8 \stemDown <b d>8 \stemDown <b d>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <b d>8 \stemDown <b d>8 \stemDown <b d>8 }
    | % 264
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <b d>8 \stemDown <b d>16 \stemDown <b d>16 \stemDown
        <b d>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <b d>8 \stemDown <b d>8 \stemDown <b d>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <b d>8 \stemDown <b d>8 \stemDown <b d>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <d f>8 \stemDown <d f>8 \stemDown <d f>8 }
    | % 265
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <d f>8 \stemDown <d f>16 \stemDown <d f>16 \stemDown
        <d f>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <d f>8 \stemDown <d f>8 \stemDown <d f>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <d f>8 \stemDown <d f>8 \stemDown <d f>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <d f>8 \stemDown <d f>8 \stemDown <d f>8 }
    | % 266
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <d f>8 \stemDown <d f>16 \stemDown <d f>16 \stemDown
        <d f>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <d f>8 \stemDown <d f>8 \stemDown <d f>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <d f>8 \stemDown <d f>8 \stemDown <d f>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <d f>8 \stemDown <d f>8 \stemDown <d f>8 }
    | % 267
    \stemDown <d f>8 r8 r4 \stemDown f4. ^\markup{ \bold\small {a. 2} }
    _\fff ^\markup{ \italic {pesante} } \stemDown e8 \pageBreak | % 268
    \stemDown d4 \stemDown cis4 \stemDown <b b'>4. \stemDown <ais ais'>8
    | % 269
    \stemDown <gis gis'>4 \stemDown <g g'>4 \stemDown <f f'>4. \stemUp
    <e e'>8 | \barNumberCheck #270
    \stemUp <d d'>8 r8 r4 r2 | % 271
    r2 \stemDown f'4. ^\markup{ \bold\small {a. 2} } _\ff \stemDown e8 | % 272
    \stemDown d4 \stemDown cis4 \stemDown b4. \stemUp ais8 \pageBreak | % 273
    \stemUp gis4 \stemUp g4 \stemUp f4. \stemUp e8 | % 274
    \stemUp d8 r8 r4 r2 | % 275
    R1*8 | % 283
    fis'1 ~ _\f | % 284
    fis1 \pageBreak | % 285
    cis1 ( _\ff | % 286
    \stemUp gis8 ) r8 r4 r2 | % 287
    <e e'>1 ~ ~ | % 288
    <e e'>1 | % 289
    <bis' fis'>1 ~ ~ | \barNumberCheck #290
    <bis fis'>1 | % 291
    <fis gis>1 ~ ~ | % 292
    <fis gis>1 | % 293
    <dis fis>1 ~ ~ | % 294
    <dis fis>1 | % 295
    <bis fis'>1 ~ ~ | % 296
    <bis fis'>1 | % 297
    R1*5 \break | % 302
    R1*3 \bar "||"
    \pageBreak | % 305
    \key c \major R1*6 \pageBreak | % 311
    r2 \stemUp bes'2 ( ^\mf ^\> | % 312
    \stemUp as8 ) ^\! r8 r4 \stemUp fis2 _\mp _\> | % 313
    \stemUp <cis eis>2 _\! _\p _\< \stemUp <gis' b>2 _\! _\f | % 314
    \stemDown <fis fis'>2 \stemUp <fis a>2 | % 315
    \stemUp <eis eis'>2 \stemUp <cis ais'>2 _\sff _\> | % 316
    \stemUp <cis gis'>2 _\! _\mf \stemUp <fis bis>2 \pageBreak | % 317
    \stemUp <eis cis'>2 r2 | % 318
    R1*8 \break | % 326
    R1*8 \pageBreak | % 334
    R1 \bar "||"
    R1 | % 336
    \stemUp bes'2 ^\markup{ \italic {cantabile} } _\p \stemUp des4. _\<
    \stemUp es8 | % 337
    \stemUp ges8 ( _\! _\mp _\> \stemUp f8 ~ \stemUp f2 ~ \stemUp f8 )
    _\! r8 | % 338
    \stemUp bes,2 _\p \stemUp des4. _\< \stemUp es8 | % 339
    \stemUp e4. ( _\! _\mp _\> \stemUp f8 ~ _\! ^\p \stemUp f4 ~ \stemUp
    f8 ) r8 | \barNumberCheck #340
    R1*3 \pageBreak | % 343
    R1*12 \bar "|."
    }

PartPEightVoiceTwo =  \relative c'' {
    \clef "treble" \time 4/4 \key c \major \transposition bes s1*11
    \break s1*7 \bar "||"
    s1*5 \pageBreak s1*6 | \barNumberCheck #30
    \time 2/4  s2 \break | % 31
    \time 4/4  s1*6 \break s1*7 \pageBreak s1*6 \break s1*4 \pageBreak
    s1*5 \break s1*5 \pageBreak s2*7 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown c16 _\f \stemDown c16 \stemDown c16 }
    \stemDown c8 \stemDown e8 | % 68
    \stemDown c4 \stemDown e4 \stemDown es8 s4. \pageBreak s2 r8 \once
    \omit TupletBracket
    \times 2/3  {
        \stemDown es16 _\ff \stemDown es16 \stemDown es16 }
    \stemDown es8 \stemDown g8 | \barNumberCheck #70
    \stemDown es4 \stemDown g4 \stemDown ges8 s4. | % 71
    r8 \stemDown fis8 ~ -> \stemDown fis8 \stemDown b,8 -. s2 | % 72
    r8 \stemDown fis'8 ~ -> \stemDown fis8 \stemDown b,8 -. s1.
    \pageBreak s1*4 \break s1*5 \pageBreak s1*6 \bar "||"
    s1*5 \break s1*7 \bar "||"
    s1*2 \pageBreak s1*3 | % 106
    r4 \stemDown dis,4 -- _\p _\< \stemDown e4 -- \stemDown fis4 -- | % 107
    \stemDown g4 -- \stemDown gis4 -- _\! _\mf r2 \break | % 108
    R1 s1*3 \pageBreak s1*4 \break s1*4 \pageBreak s1*5 \break s1*5 \bar
    "||"
    s1*2 \pageBreak s1*6 \pageBreak s1*4 \bar "||"
    s1*3 \break s1*11 \pageBreak s1*5 \bar "||"
    \key c \major s1*4 \pageBreak s1*7 \pageBreak s1*2 | % 174
    \stemDown fis8 -. \stemDown c'8 -. \stemDown g8 -. r8 r2 s1*3
    \pageBreak | % 178
    r8 \stemDown g8 -. \stemDown d8 -. \stemDown a'8 -. s2*7 | % 182
    \stemDown gis8 -. \stemDown d'8 -. \stemDown a8 -. r8 s2 \break s1*5
    \pageBreak s1*4 \break s1*4 \pageBreak | % 196
    \stemDown e2 \stemDown a4 -> \stemDown g4 -> s1*4 \break s1*6
    \pageBreak s2 \stemDown fis4 ~ \stemDown fis8. \stemDown bes16 s1.
    \stemDown a4 ~ \stemDown a8. \stemDown des16 | \barNumberCheck #210
    \stemDown des8 s8 \stemDown c8 s8 \stemDown bes8 s8 \stemDown c8 s16
    \stemDown fes16 | % 211
    \stemDown fes8 s8 \stemDown es8 s8 \stemDown des8 s8 \stemDown es8
    s8 | % 212
    \stemDown es8 s8 \stemDown f8 s8 \stemDown f8 s8 \stemDown g8 s8
    \pageBreak | % 213
    \stemDown f8 s8 \stemDown g8 s8 \stemDown f8 s8 \stemDown g8 s8*25
    \break s1*4 \pageBreak s1*5 \break s1*5 \break s1*6 \pageBreak s1*5
    \pageBreak s1 | % 243
    \stemDown fes2 \stemDown ges4.. \stemDown ges16 | % 244
    \stemDown des8 s8 \stemDown c8 s8 \stemDown des8 s8 \stemDown as8
    \stemDown a8 | % 245
    \stemDown bes4 ( -> \stemDown c8 ) s4. \once \omit TupletBracket
    \times 2/3  {
        \stemDown des,8 \stemDown ges8 \stemDown des8 }
    \pageBreak | % 246
    \stemDown bes'4 ( -> \stemDown c8 ) s2 \stemDown c8 s1*5 \break s1*5
    \pageBreak s1*3 | \barNumberCheck #260
    r2 r4 \stemDown c4 s1*2 \pageBreak s1*5 \pageBreak s1*5 \pageBreak
    s1*10 | % 283
    fis1 ~ | % 284
    fis1 \pageBreak | % 285
    gis,1 ~ | % 286
    gis1 s1*15 \break s1*3 \bar "||"
    \pageBreak | % 305
    \key c \major s1*6 \pageBreak | % 311
    R1 | % 312
    r2 \stemDown bis,2 s1*4 \pageBreak s1*9 \break s1*8 \pageBreak s1
    \bar "||"
    s1 | % 336
    \stemDown ges'2 \stemDown bes4. \stemDown bes8 | % 337
    \stemDown as2. ~ \stemDown as8 s8 | % 338
    \stemDown ges2 \stemDown bes4. \stemDown bes8 | % 339
    \stemDown as2. ~ \stemDown as8 s8*25 \pageBreak s1*12 \bar "|."
    }

PartPNineVoiceOne =  \relative dis' {
    \clef "tenor" \time 4/4 \key d \major | % 1
    R1*11 \break | % 12
    R1*7 \bar "||"
    R1*5 \pageBreak | % 24
    R1*6 | \barNumberCheck #30
    \time 2/4  R2 \break | % 31
    \time 4/4  R1*6 \break | % 37
    R1*7 \pageBreak | % 44
    R1*6 \break | \barNumberCheck #50
    R1*4 \pageBreak | % 54
    R1*5 \break | % 59
    R1*5 \pageBreak | % 64
    R1*3 | % 67
    r2 r4 \stemUp dis8 ^\f \stemUp eis8 | % 68
    \stemUp fis4 \stemUp eis4 \stemUp fis8 r8 r4 \pageBreak | % 69
    r2 r4 \stemUp fis8 ^\ff \stemUp gis8 | \barNumberCheck #70
    \stemUp a4 \stemUp gis4 \stemUp a8 r8 r4 | % 71
    \stemUp a4 -> \stemUp c,4 -> r2 | % 72
    \stemUp a'4 -> \stemUp c,4 -> r2 | % 73
    \stemDown <a c>4 ~ ~ \stemDown <a c>8 r8 r2 \pageBreak | % 74
    \stemDown <a c>4 ~ ~ \stemDown <a c>8 r8 \stemDown <a c>4 ~ -> ~
    \stemDown <a c>8 r8 | % 75
    \stemDown <a c>4 ~ -> ~ \stemDown <a c>8 r8 \stemUp <g a>4 ~ -> ~
    \stemUp <g a>8 r8 | % 76
    \stemUp <g a>4 ~ -> ~ \stemUp <g a>8 r8 \stemUp <g a>4 ~ -> ~ _\f
    \stemUp <g a>8 r8 | % 77
    \stemUp <g a>4 ~ -> ~ \stemUp <g a>8 r8 r2 \break | % 78
    R1 | % 79
    r2 r4 \stemUp <cis, g'>4 ~ ~ _\p | \barNumberCheck #80
    \stemUp <cis g'>4 ~ ~ _\> \stemUp <cis g'>8 r8 _\! r2 | % 81
    r2 \stemUp cis2 ~ _\pp | % 82
    \stemUp cis2 \stemUp d2 ~ \pageBreak | % 83
    \stemUp d2 ~ \stemUp d8 r8 r4 | % 84
    R1*5 \bar "||"
    R1*5 \break | % 94
    R1*7 \bar "||"
    R1*2 \pageBreak | % 103
    R1*2 | % 105
    r4 \stemUp fis4 -- ^\p \stemUp gis4 -- \stemUp ais4 -- | % 106
    \stemUp b4 -- r4 _\p _\< r2 | % 107
    r2 \stemUp g4 -- ^\mf \stemUp gis4 -- \break | % 108
    \stemUp a4 -- ^\> \stemUp b4 -- \stemUp c4 -- \stemUp cis4 -- ^\!
    ^\p | % 109
    R1*3 \pageBreak | % 112
    R1*3 | % 115
    r2 \stemUp d,4 -- ^\mf \stemUp dis4 -- \break | % 116
    \stemUp e4 -- ^\> \stemUp fis4 -- \stemUp g4 -- \stemUp gis4 -- ^\!
    ^\p | % 117
    R1*3 \pageBreak | \barNumberCheck #120
    R1*5 \break | % 125
    R1*5 \bar "||"
    R1*2 \pageBreak | % 132
    R1*2 | % 134
    r2 \stemUp fis4 ^ "I." ^\markup{ \italic {marcato} } _\mf \stemUp g8
    \stemUp a8 | % 135
    \stemUp b,8 _\p r8 r4 \stemUp e4 _\mf ^\markup{ \italic {marcato} }
    \stemUp fis8 \stemUp g8 | % 136
    \stemUp fis8 _\p r8 r4 r2 | % 137
    r2 \stemUp dis4 ( _\mf ^ "II." _\> \stemUp e8 ) _\! _\p r8
    \pageBreak | % 138
    r2 \stemUp fis4 ^ "I." ^\markup{ \italic {marcato} } _\mf \stemUp g8
    \stemUp a8 | % 139
    \stemUp b,8 _\p r8 r4 \stemUp e4 _\mf ^\markup{ \italic {marcato} }
    \stemUp fis8 \stemUp g8 | \barNumberCheck #140
    \stemUp fis8 _\p r8 r4 r2 | % 141
    r2 \stemUp dis4 ( _\mf ^ "II." _\> \stemUp e8 ) _\! _\p r8 \bar "||"
    r2 \stemUp fis2 _\mp | % 143
    \stemUp g2 \stemUp e2 | % 144
    \stemUp fis2 _\> \stemUp fis2 ( _\! _\p \break | % 145
    \stemUp e8 ) r8 r4 \stemUp e2 ( _\> | % 146
    \stemUp d8 ) _\! _\pp r8 r4 r2 | % 147
    R1*9 \pageBreak | % 156
    R1*5 \bar "||"
    \key c \major \stemUp <g a>8 _\ff r8 r4 r2 | % 162
    R1*3 \pageBreak | % 165
    \stemDown <g e'>8 _\ff r8 r4 r2 | % 166
    R1*3 | % 169
    \stemDown <f d'>8 _\ff r8 r4 \stemDown <f d'>16 _\sff \stemDown <f
        d'>16 \stemDown <f d'>8 ~ ~ \stemDown <f d'>4 ~ ~ |
    \barNumberCheck #170
    \stemUp <f d'>8 \stemUp <e d'>8 -> \stemUp <f d'>8 -> \stemUp <e d'>8
    -> \stemDown <f d'>8 -> \stemDown <f d'>8 -> r4 | % 171
    R1 \pageBreak | % 172
    R1*2 | % 174
    r8 \stemUp bes8 -. ^\mf \stemUp f8 -. \stemUp c'8 -. _\mf r2 | % 175
    R1*3 \pageBreak | % 178
    r4 r8 \stemUp g8 -. ^\mf \stemUp d'8 -. _\mf r8 r4 | % 179
    R1*3 | % 182
    r8 \stemUp c8 -. ^\mf \stemUp g8 -. \stemUp d'8 -. _\mf r2 \break | % 183
    r4 \stemUp b8 _\f r8 r2 | % 184
    r4 \stemDown <g b>8 _\f r8 r2 | % 185
    R1*3 \pageBreak | % 188
    R1 | % 189
    r2 r4 \stemUp <bes, es>4 ~ ~ _\fff | \barNumberCheck #190
    <bes es>1 ~ ~ | % 191
    \stemUp <bes es>2. \stemUp <es g>4 ~ ~ \break | % 192
    <es g>1 ~ ~ | % 193
    \stemUp <es g>2. \stemUp <d f>4 | % 194
    <d f>1 | % 195
    <f a>1 \pageBreak | % 196
    \stemUp bes4 -> \stemUp a4 -> \stemUp g4 -> \stemUp f4 -> | % 197
    \stemUp e4 -> \stemUp d4 -> \stemUp f8 -> \stemUp f8 -> r4 | % 198
    R1*3 \break | % 201
    r2 r4 \stemDown <f d'>4 ~ ~ _ "" _\markup{ \italic {cantabile} } | % 202
    \stemDown <f d'>2 \stemDown <f c'>2 | % 203
    \stemDown <f d'>2 \stemDown <a f'>2 | % 204
    \stemDown <g e'>2 \stemDown <g d'>2 | % 205
    \stemUp <e a>2. ~ ~ \stemUp <e a>8. \stemUp <f a>16 _\p | % 206
    \stemUp <f a>2 -> _\markup{ \italic {poco a poco cresc.} } \stemUp
    <e g>2 \pageBreak | % 207
    \stemUp f2 \stemUp e4 ~ \stemUp e8. \stemUp c'16 | % 208
    \stemUp c2 -> \stemUp bes2 | % 209
    \stemUp as2 \stemUp g4 ~ \stemUp g8. \stemUp dis'16 _\mf |
    \barNumberCheck #210
    \stemUp dis8 _\markup{ \italic {poco cresc.} } r8 \stemUp cis8 r8
    \stemUp b8 r8 \stemUp ais8 r16 \stemUp fis'16 | % 211
    \stemUp fis8 r8 \stemUp e8 r8 \stemUp d8 r8 \stemUp cis8 r8 | % 212
    \stemUp e8 r8 \stemUp dis8 r8 \stemUp fis8 _\f _\< r8 \stemUp eis8 r8
    \pageBreak | % 213
    \stemUp fis8 r8 \stemUp eis8 r8 \stemUp fis8 r8 \stemUp eis8 r8 | % 214
    R1 | % 215
    \stemUp gis,4 -- _\! _\ff ^ "I." \stemDown a4 -- \stemDown fis'4 --
    \stemDown eis4 -- | % 216
    \stemDown e4 -- _\markup{ \italic {dim. un poco} } \stemDown dis4 --
    \stemDown d4 -- \stemDown cis4 -- \break | % 217
    \stemDown b4 -- \stemDown ais4 -- \stemDown a4 -- \stemUp gis4 -- | % 218
    R1 | % 219
    \stemUp gis4 -- \stemDown a4 -- \stemDown fis'4 -- \stemDown eis4 --
    | \barNumberCheck #220
    \stemDown e4 _\markup{ \italic {dim.} } \stemDown dis4 \stemDown d4
    \stemDown cis4 \pageBreak | % 221
    \stemDown b4 \stemDown ais4 \stemDown a4 \stemUp gis4 | % 222
    \stemDown a4 \stemUp gis4 \stemDown a4 \stemUp gis4 | % 223
    \stemDown a4 _\p \stemUp gis2. | % 224
    \stemDown cis4 \stemUp gis2. | % 225
    \stemDown cis4 _\markup{ \italic {dim.} } \stemUp gis2. \break | % 226
    \stemDown cis4 \stemUp gis2. | % 227
    a1 _\pp | % 228
    bes1 ~ | % 229
    \stemDown bes8 r8 r4 r2 | \barNumberCheck #230
    bes1 ~ ^\pp \break | % 231
    bes1 ~ | % 232
    \stemUp bes8 _\pp r8 r4 r2 | % 233
    R1 | % 234
    bes1 ~ | % 235
    bes1 ~ | % 236
    \stemUp bes8 _\pp _\< r8 r4 r2 \pageBreak | % 237
    R1 _ "" | % 238
    r2 _\! _\markup{ \italic {poco cresc.} } \stemUp des,4 ~ -> ^\mp
    \stemUp des8. \stemUp des16 | % 239
    \stemUp ges2. -> _\markup{ \italic {cresc.} } \stemUp es4 |
    \barNumberCheck #240
    \stemDown bes'2 -> \stemDown a2 -> | % 241
    \stemDown bes2 _\mf _\< \stemDown as4.. \stemDown as16 \pageBreak | % 242
    \stemDown es'8 _\! _\f _\< r8 \stemDown d8 r8 \stemDown es8 r8 _\! r4
    | % 243
    \stemDown d2 _\ff \stemDown e4.. \stemDown e16 | % 244
    \stemUp b8 r8 \stemUp ais8 r8 \stemUp b8 r8 \stemUp b8 _\fff \stemUp
    cis8 | % 245
    \stemUp d4 ( -> \stemUp cis8 ) r8 r4 \stemUp b8 \stemUp b8
    \pageBreak | % 246
    \stemUp d4 ( -> \stemUp cis8 ) r8 r4 r8 \stemUp g'8 | % 247
    r8 \stemDown <b, d>8 r8 \stemDown <cis e>8 r8 \stemDown <d fis>8 r8
    \stemUp <g, ais>8 | % 248
    r8 \stemUp <fis b>8 r8 \stemDown <cis' e>8 \stemDown <cis fis>8 r8 r4
    | % 249
    R1*3 \break | % 252
    R1*5 \pageBreak | % 257
    R1*3 | \barNumberCheck #260
    r4 \stemUp fis,2 _ "" _\markup{ \italic {cresc.} } \stemUp es'4
    _\mp | % 261
    \stemDown <a, es'>4 _\markup{ \italic {cresc.} } \stemDown <a d>4
    \stemDown <a cis>4 \stemDown <a fis'>4 | % 262
    \stemDown <a f'>4 \stemDown <a e'>4 \stemDown <a es'>4 \stemDown es'8
    ^\markup{ \bold\small {a. 2} } _\ff \stemDown f8 \pageBreak | % 263
    \stemDown ges8 r8 \stemDown es8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown es8 \stemDown f8 \stemDown ges8 }
    | % 264
    \stemDown ges8 r8 \stemDown es8 r8 r4 \stemDown fis8 \stemDown gis8
    | % 265
    \stemDown a8 r8 \stemDown fis8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown gis8 \stemDown a8 }
    | % 266
    \stemDown a8 ^\markup{ \bold\small {a. 2} } r8 \stemDown fis8 r8 r4
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown gis8 \stemDown a8 }
    | % 267
    \stemDown a8 r8 r4 _\fff \stemUp c,4. ^ "" ^\markup{ \italic
        {pesante} } \stemUp d8 \pageBreak | % 268
    \stemUp es2 \stemUp fis4. \stemUp gis8 | % 269
    \stemUp a2. \stemUp gis4 | \barNumberCheck #270
    \stemUp a8 r8 r4 r2 | % 271
    R1*2 \pageBreak | % 273
    R1*12 \pageBreak | % 285
    r2 r4 \stemUp fis,4 ^\markup{ \bold\small {a. 2} } ^\markup{ \italic
        {marcato} } _\ff | % 286
    \stemDown cis'4.. \stemDown b16 \stemDown b2 | % 287
    r2 r4 \stemDown d4 | % 288
    \stemDown g4.. \stemDown fis16 \stemDown fis2 | % 289
    r2 r4 \stemDown ais,4 | \barNumberCheck #290
    \stemDown d4.. \stemDown cis16 \stemDown cis2 | % 291
    r2 r4 \stemUp e,4 | % 292
    \stemDown b'4.. \stemDown ais16 \stemDown ais2 | % 293
    r2 r4 \stemUp cis,4 | % 294
    \stemUp g'4.. \stemUp fis16 \stemUp fis2 | % 295
    r2 r4 \stemUp ais,4 | % 296
    \stemUp d4.. \stemUp cis16 \stemUp cis2 | % 297
    \stemUp b4.. \stemUp ais16 \stemUp ais2 | % 298
    R1*4 \break | % 302
    R1*3 \bar "||"
    \pageBreak | % 305
    \key b \major R1*6 \pageBreak | % 311
    r2 \stemUp gis'2 ^\mf ^\> | % 312
    \stemUp fis2 ^\! _\pp _\< \stemUp <ais, e'>2 _\! _\mp _\> | % 313
    \stemUp <b dis>2 _\! _\p _\< \stemUp <fis' a>2 _\! _\f | % 314
    \stemDown <e e'>2 \stemUp <e g>2 | % 315
    \stemUp <dis dis'>2 \stemUp <b gis'>2 _\sff _\> | % 316
    \stemUp <b fis'>2 _\! _\mf \stemUp <e ais>2 \pageBreak | % 317
    \stemUp <dis b'>2 r2 | % 318
    R1*8 \break | % 326
    R1*8 \pageBreak | % 334
    R1 \bar "||"
    R1 | % 336
    \stemUp b'2 ^\markup{ \italic {cantabile} } _\p \stemUp b4. _\<
    \stemUp cis8 | % 337
    \stemUp e8 ( _\! _\mp _\> \stemUp dis8 ~ \stemUp dis2 ~ \stemUp dis8
    ) _\! r8 | % 338
    \stemUp b2 _\p \stemUp b4. _\< \stemUp cis8 | % 339
    \stemUp d4. ( _\! _\mp _\> \stemUp dis8 ~ _\! ^\p \stemUp dis4 ~
    \stemUp dis8 ) r8 | \barNumberCheck #340
    R1*3 \pageBreak | % 343
    R1*7 | \barNumberCheck #350
    \stemDown <b dis>2. ~ ~ _\pp \stemDown <b dis>8 \stemDown <b dis>8 | % 351
    <b dis>1 ~ ~ _\markup{ \italic {morendo} } | % 352
    <b dis>1 ~ ~ | % 353
    <b dis>1 ~ ~ | % 354
    \stemDown <b dis>8 r8 r4 r2 ^\fermata \bar "|."
    }

PartPNineVoiceTwo =  \relative ais {
    \clef "tenor" \time 4/4 \key d \major s1*11 \break s1*7 \bar "||"
    s1*5 \pageBreak s1*6 | \barNumberCheck #30
    \time 2/4  s2 \break | % 31
    \time 4/4  s1*6 \break s1*7 \pageBreak s1*6 \break s1*4 \pageBreak
    s1*5 \break s1*5 \pageBreak s2*7 r8 \stemDown ais16 _\f \stemDown
    ais16 \stemDown ais8 \stemDown cisis8 | % 68
    \stemDown dis4 \stemDown cisis4 \stemDown cis8 s4. \pageBreak s2 r8
    \stemDown cis16 _\ff \stemDown cis16 \stemDown cis8 \stemDown eis8 |
    \barNumberCheck #70
    \stemDown fis4 \stemDown eis4 \stemDown e8 s4. | % 71
    r8 \stemDown e8 ~ -> \stemDown e8 \stemDown a,8 -. s2 | % 72
    r8 \stemDown e'8 ~ -> \stemDown e8 \stemDown a,8 -. s1. \pageBreak
    s1*4 \break s1*5 \pageBreak s1*6 \bar "||"
    s1*5 \break s1*7 \bar "||"
    s1*2 \pageBreak s1*2 | % 105
    R1 | % 106
    r4 \stemDown cis,4 -- \stemDown d4 -- \stemDown e4 -- | % 107
    \stemDown eis4 -- \stemDown fis4 -- _\! _\mf r2 \break | % 108
    R1 s1*3 \pageBreak s1*2 | % 114
    r4 \stemDown gis4 -- _\p _\< \stemDown a4 -- \stemDown b4 -- | % 115
    \stemDown bis4 -- \stemDown cis4 -- _\! _\mf r2 \break | % 116
    R1 s1*3 \pageBreak s1*5 \break s1*5 \bar "||"
    s1*2 \pageBreak s1*6 \pageBreak s1*4 \bar "||"
    s1*3 \break s1*11 \pageBreak s1*5 \bar "||"
    \key c \major s1*4 \pageBreak s1*7 \pageBreak s1*2 | % 174
    r4 r8 \stemDown c,8 -. \stemDown g'8 -. r8 r4 s1*3 \pageBreak | % 178
    r2 \stemDown d8 -. \stemDown a'8 -. s4*13 | % 182
    r4 r8 \stemDown d,8 -. \stemDown a'8 -. r8 r4 \break s4 \stemDown g8
    s8*37 \pageBreak s1*4 \break s1*4 \pageBreak | % 196
    \stemDown d2 \stemDown d2 | % 197
    \stemDown e4 -> \stemDown d4 -> \stemDown d8 -> \stemDown d8 ->
    s4*13 \break s1*6 \pageBreak | % 207
    r2 r4 r8. \stemDown as'16 | % 208
    \stemDown as2 -> \stemDown g2 | % 209
    r2 r4 r8. \stemDown b16 | \barNumberCheck #210
    \stemDown b8 s8 \stemDown ais8 s8 \stemDown gis8 s8 \stemDown ais8
    s16 \stemDown d16 | % 211
    \stemDown d8 s8 \stemDown cis8 s8 \stemDown b8 s8 \stemDown cis8 s8
    | % 212
    \stemDown cis8 s8 \stemDown dis8 s8 \stemDown dis8 s8 \stemDown eis8
    s8 \pageBreak | % 213
    \stemDown dis8 s8 \stemDown eis8 s8 \stemDown dis8 s8 \stemDown eis8
    s8*25 \break s1*4 \pageBreak s1*5 \break s1*5 \break s1 | % 232
    bes1 ~ | % 233
    bes1 ~ | % 234
    \stemDown bes8 r8 r4 r2 s1 | % 236
    \stemDown bes2 \stemDown a4. \stemDown as8 \pageBreak | % 237
    ges1 ~ -> | % 238
    \stemDown ges2 r2 s1*3 \pageBreak s1*2 | % 244
    r4 \stemDown cis8 s8 \stemDown d8 s8 \stemDown fis,8 \stemDown ais8
    | % 245
    \stemDown gis4 ( -> \stemDown ais8 ) s4. \stemDown fis8 \stemDown g8
    \pageBreak | % 246
    \stemDown gis4 ( -> \stemDown ais8 ) s2 \stemDown ais8 s1*5 \break
    s1*5 \pageBreak s1*3 | \barNumberCheck #260
    r2 r4 \stemDown bes4 s1*2 \pageBreak s4*17 \stemDown fis2 \stemDown
    gis4 \pageBreak | % 268
    \stemDown a4 \stemDown b4 \stemDown c4 \stemDown d4 | % 269
    \stemDown es4 \stemDown f4 \stemDown fis4 \stemDown gis4 |
    \barNumberCheck #270
    \stemDown a8 s8*23 \pageBreak s1*12 \pageBreak s1*17 \break s1*3
    \bar "||"
    \pageBreak | % 305
    \key b \major s1*6 \pageBreak | % 311
    R1 | % 312
    r2 s2*9 \pageBreak s1*9 \break s1*8 \pageBreak s1 \bar "||"
    s1 | % 336
    \stemDown gis,2 \stemDown gis4. \stemDown gis8 | % 337
    \stemDown b2. ~ \stemDown b8 s8 | % 338
    \stemDown gis2 \stemDown gis4. \stemDown gis8 | % 339
    \stemDown b2. ~ \stemDown b8 s8*25 \pageBreak s1*12 \bar "|."
    }

PartPOneZeroVoiceOne =  \relative fis {
    \clef "bass" \time 4/4 \key d \major | % 1
    R1*11 \break | % 12
    R1*7 \bar "||"
    R1*5 \pageBreak | % 24
    R1*6 | \barNumberCheck #30
    \time 2/4  R2 \break | % 31
    \time 4/4  R1*6 \break | % 37
    R1*7 \pageBreak | % 44
    R1*6 \break | \barNumberCheck #50
    R1*4 \pageBreak | % 54
    R1*5 \break | % 59
    R1*5 \pageBreak | % 64
    R1*3 | % 67
    r2 r4 \stemDown fis8 _\f \stemDown ais8 | % 68
    \stemDown ais4 \stemDown eis4 \stemDown fis4 ~ \stemDown fis8 r8
    \pageBreak | % 69
    r2 r4 \stemDown a8 _\ff \stemDown cis8 | \barNumberCheck #70
    \stemDown cis4 \stemDown gis4 \stemDown a4 ~ \stemDown a8 r8 | % 71
    r2 \stemDown a4 ~ \stemDown a8 r8 | % 72
    r2 \stemDown a4 ~ \stemDown a8 r8 | % 73
    \stemDown e4 ~ \stemDown e8 r8 \stemDown a4 ~ \stemDown a8 r8
    \pageBreak | % 74
    \stemDown e4 ~ \stemDown e8 r8 \stemDown f4 ( -> \stemDown e8 ) r8 | % 75
    \stemDown f4 ( -> \stemDown e8 ) r8 \stemDown e4 ( -> \stemDown es8
    ) r8 | % 76
    \stemDown e4 ( -> \stemDown es8 ) r8 \stemDown e4 ( -> _\f \stemDown
    es8 ) r8 | % 77
    \stemDown e4 ( -> \stemDown es8 ) r8 r2 \break | % 78
    R1 | % 79
    r2 r4 \stemUp a,4 ~ _\p | \barNumberCheck #80
    \stemUp a4 ~ _\> \stemUp a8 r8 _\! r2 | % 81
    r2 \stemUp g2 ~ _\pp | % 82
    \stemUp g2 \stemUp fis2 ~ \pageBreak | % 83
    \stemUp fis2 ~ \stemUp fis8 r8 r4 | % 84
    R1*5 \bar "||"
    R1*5 \break | % 94
    R1*7 \bar "||"
    R1*2 \pageBreak | % 103
    R1*2 | % 105
    r4 \stemUp fis4 -- _\p \stemUp gis4 -- \stemUp ais4 -- | % 106
    \stemUp b4 -- r4 r2 | % 107
    R1 \break | % 108
    R1*4 \pageBreak | % 112
    R1 | % 113
    r4 \stemUp cis4 -- _\p \stemDown dis4 -- \stemDown eis4 -- | % 114
    \stemDown fis4 -- \stemUp gis,4 -- _\< \stemUp a4 -- \stemUp b4 -- | % 115
    \stemUp bis4 -- \stemUp cis4 -- _\! _\mf r2 \break | % 116
    R1*4 \pageBreak | \barNumberCheck #120
    R1*5 \break | % 125
    R1*5 \bar "||"
    R1*2 \pageBreak | % 132
    R1*2 | % 134
    r2 \stemDown dis2 _\mf ^\markup{ \italic {marcato} } | % 135
    \stemDown e2 \stemUp cis2 | % 136
    \stemDown d2 r2 | % 137
    R1 \pageBreak | % 138
    r2 \stemDown dis2 _\mf ^\markup{ \italic {marcato} } | % 139
    \stemDown e2 \stemUp cis2 | \barNumberCheck #140
    \stemDown d2 r2 | % 141
    R1 \bar "||"
    R1*3 \break | % 145
    R1*11 \pageBreak | % 156
    R1*5 \bar "||"
    \key c \major \stemUp c8 _\ff r8 r4 r2 | % 162
    R1*3 \pageBreak | % 165
    \stemUp b8 _\ff r8 r4 r2 | % 166
    R1*3 | % 169
    bes1 ~ _\ff _\> | \barNumberCheck #170
    \stemUp bes8 _\! \stemUp bes8 -> _\ff \stemUp bes8 -> \stemUp bes8
    -> \stemUp bes8 -> \stemUp a8 -> r4 | % 171
    R1 \pageBreak | % 172
    R1*2 | % 174
    r2 \stemUp g8 -. _\mf \stemUp d'8 -. \stemUp a8 -. r8 | % 175
    R1*3 \pageBreak | % 178
    r2 r8 \stemUp a8 -. _\mf \stemUp e'8 -. \stemUp b8 -. | % 179
    \stemUp e,8 -. r8 r4 r2 | \barNumberCheck #180
    R1*2 | % 182
    r2 \stemUp a8 -. _\mf \stemUp e'8 -. \stemUp b8 -. r8 \break | % 183
    R1*5 \pageBreak | % 188
    R1 | % 189
    r2 r4 \stemUp g4 ~ _\fff | \barNumberCheck #190
    g1 ~ | % 191
    \stemUp g2. \stemUp g4 ~ \break | % 192
    g1 ~ | % 193
    \stemUp g2. \stemUp gis4 | % 194
    a1 ~ | % 195
    a1 \pageBreak | % 196
    a1 ~ | % 197
    \stemUp a2 \stemUp bes8 -> \stemUp a8 -> r4 | % 198
    R1*3 \break | % 201
    r2 r4 \stemDown d4 ~ _ "" _\markup{ \italic {cantabile} } | % 202
    \stemDown d2 \stemDown f2 | % 203
    \stemDown d2 \stemDown d2 | % 204
    \stemDown d2 \stemDown d2 | % 205
    \stemUp cis2. ~ \stemUp cis8. \stemUp c16 _\p | % 206
    \stemUp c2 -> _\markup{ \italic {poco a poco cresc.} } \stemUp cis2
    \pageBreak | % 207
    \stemDown d2 \stemDown e4 ~ \stemDown e8. \stemDown es16 | % 208
    \stemDown es2 -> \stemDown e2 | % 209
    \stemDown f2 \stemDown g4 ~ \stemDown g8. \stemDown dis16 _\mf |
    \barNumberCheck #210
    \stemDown dis8 _\markup{ \italic {poco cresc.} } r8 \stemDown e8 r8
    \stemDown eis8 r8 \stemDown fis8 r16 \stemDown fis16 | % 211
    \stemDown fis8 r8 \stemDown g8 r8 \stemDown gis8 r8 \stemDown a8 r8
    | % 212
    \stemDown ais8 r8 \stemDown b8 r8 \stemDown bis8 _\f _\< r8
    \stemDown cis8 r8 \pageBreak | % 213
    \stemDown bis8 r8 \stemDown cis8 r8 \stemDown bis8 r8 \stemDown cis8
    r8 | % 214
    \stemDown d,4 -- _\! _\ff \stemDown dis4 -- \stemDown eis4 --
    \stemDown fis4 -- | % 215
    \stemUp gis,4 -- _\ff \stemUp a4 -- \stemDown fis'4 -- \stemDown eis4
    -- | % 216
    \stemDown e4 -- _\markup{ \italic {dim. un poco} } \stemDown dis4 --
    \stemDown d4 -- \stemUp cis4 -- \break | % 217
    \stemUp b4 -- \stemUp ais4 -- \stemUp a4 -- \stemUp gis4 -- | % 218
    \stemDown d'4 -- _\f \stemDown dis4 -- \stemDown eis4 -- \stemDown
    fis4 -- | % 219
    \stemUp gis,4 -- \stemUp a4 -- \stemDown fis'4 -- \stemDown eis4 --
    | \barNumberCheck #220
    \stemDown e4 _\markup{ \italic {dim.} } \stemDown dis4 \stemDown d4
    \stemUp cis4 \pageBreak | % 221
    \stemUp b4 \stemUp ais4 \stemUp a4 \stemUp gis4 | % 222
    \stemUp a4 \stemUp gis4 \stemUp a4 \stemUp gis4 | % 223
    \stemUp a4 _\p \stemUp gis2. | % 224
    \stemUp cis4 \stemUp gis2. | % 225
    \stemUp cis4 _\markup{ \italic {dim.} } \stemUp gis2. \break | % 226
    \stemUp cis4 \stemUp gis2. | % 227
    a1 _\pp | % 228
    bes1 ~ | % 229
    \stemUp bes8 r8 r4 r2 | \barNumberCheck #230
    R1 \break | % 231
    R1*6 \pageBreak | % 237
    R1 | % 238
    r2 \stemUp ges4 ( -. _\p \stemUp g4 ) -. | % 239
    \stemUp as4 ~ \stemUp as8 r8 \stemUp as4 ( -. _\markup{ \italic
        {cresc.} } \stemUp a4 ) -. | \barNumberCheck #240
    \stemUp bes4.. \stemUp bes16 \stemUp c4.. \stemUp c16 | % 241
    \stemDown des4.. _\mf _\< \stemDown des16 \stemDown d4.. \stemDown d16
    \pageBreak | % 242
    \stemDown es8 _\! _\f _\< r8 \stemDown f8 r8 \stemDown ges8 r8 _\! r4
    | % 243
    \stemDown fis4.. _\ff \stemDown fis16 \stemDown ais4.. \stemDown ais16
    | % 244
    \stemDown b8 r8 \stemUp cis,8 r8 \stemDown d8 r8 \stemDown d8 _\fff
    \stemDown e8 | % 245
    \stemDown eis4 ( -> \stemDown fis8 ) r8 r4 \stemDown d8 \stemDown e8
    \pageBreak | % 246
    \stemDown eis4 ( -> \stemDown fis8 ) r8 r4 r8 \stemUp cis8 | % 247
    r8 \stemDown d8 r8 \stemDown g8 r8 \stemDown fis8 r8 \stemUp cis8 | % 248
    r8 \stemDown d8 r8 \stemDown g8 \stemDown fis8 r8 r4 | % 249
    R1*3 \break | % 252
    R1*5 \pageBreak | % 257
    R1*3 | \barNumberCheck #260
    r2 r4 \stemUp bes,4 _\mp | % 261
    \stemUp ces4 _\markup{ \italic {cresc.} } \stemUp c4 \stemUp cis4
    \stemDown d4 | % 262
    \stemDown dis4 \stemDown e4 \stemDown f4 \stemDown ges8 _\ff
    \stemDown f8 \pageBreak | % 263
    \stemDown es8 r8 \stemDown ges8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown ges8 \stemDown f8 \stemDown es8 }
    | % 264
    \stemDown es8 r8 \stemDown ges8 r8 r4 \stemDown a8 \stemDown gis8 | % 265
    \stemDown fis8 r8 \stemDown a8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown gis8 \stemDown fis8 }
    | % 266
    \stemDown fis8 r8 \stemDown a8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown gis8 \stemDown fis8 }
    | % 267
    \stemDown fis8 r8 r4 \stemUp c4. _\fff ^\markup{ \italic {pesante} }
    \stemDown d8 \pageBreak | % 268
    \stemDown es2 \stemDown fis4. \stemDown gis8 | % 269
    \stemDown a2. \stemDown gis4 | \barNumberCheck #270
    \stemDown a8 r8 r4 r2 | % 271
    r4 \stemUp fis,2 _\ff \stemUp gis4 | % 272
    \stemUp a4 \stemUp b4 \stemUp c4 \stemDown d4 \pageBreak | % 273
    \stemDown es4 \stemDown f4 \stemDown fis4 \stemDown gis4 | % 274
    R1*6 | \barNumberCheck #280
    r2 r4 \stemDown dis4 _\f | % 281
    cis1 ~ | % 282
    \stemUp cis2. \stemUp b4 | % 283
    ais1 ~ | % 284
    ais1 \pageBreak | % 285
    \stemUp b2 ~ \stemUp b8 r8 \stemUp fis4 _\ff ^\markup{ \italic
        {marcato} } | % 286
    \stemUp cis'4.. \stemUp b16 \stemUp b2 | % 287
    r2 r4 \stemDown d4 | % 288
    \stemDown g4.. \stemDown fis16 \stemDown fis2 | % 289
    r2 r4 \stemUp ais,4 | \barNumberCheck #290
    \stemDown d4.. \stemUp cis16 \stemUp cis2 | % 291
    r2 r4 \stemUp e,4 | % 292
    \stemUp b'4.. \stemUp ais16 \stemUp ais2 | % 293
    r2 r4 \stemUp cis,4 | % 294
    \stemUp g'4.. \stemUp fis16 \stemUp fis2 | % 295
    r2 r4 \stemUp ais4 | % 296
    \stemDown d4.. \stemUp cis16 \stemUp cis2 | % 297
    \stemUp b4.. \stemUp ais16 \stemUp ais2 | % 298
    \stemUp g4.. \stemUp fis16 \stemUp fis2 | % 299
    eis1 ~ _\ffff _\> | \barNumberCheck #300
    \stemUp eis2 ~ \stemUp eis8 _\! _\p r8 r4 | % 301
    R1 \break | % 302
    R1*3 \bar "||"
    \pageBreak | % 305
    \key b \major R1 | % 306
    \stemUp b'2 _\pp \stemUp b2 | % 307
    b1 | % 308
    \stemUp b2 \stemUp b2 | % 309
    b1 _\< | \barNumberCheck #310
    b1 _\! _ "" _\markup{ \italic {poco cresc.} } \pageBreak | % 311
    \stemUp b2 \stemUp eis,2 _\mf _\> | % 312
    \stemUp fis2 _\! _\pp _\< \stemUp fis2 _\! _\mp _\> | % 313
    \stemDown fis'2 _\! _\p _\< \stemUp b,2 _\! _\f | % 314
    \stemUp b2 \stemUp b2 | % 315
    \stemUp b2 \stemUp eis,2 _\sff _\> | % 316
    \stemUp fis2 _\! _\mf \stemUp fis2 \pageBreak | % 317
    \stemUp b2 \stemUp b2 ~ _\p | % 318
    \stemUp b2 \stemUp b2 ~ | % 319
    \stemUp b2 \stemUp b2 ~ | \barNumberCheck #320
    \stemUp b2 \stemUp b2 ~ | % 321
    \stemUp b2 r2 | % 322
    R1*4 \break | % 326
    R1*8 \pageBreak | % 334
    R1 \bar "||"
    R1 | % 336
    \stemDown e2 _\p \stemDown e4. _\< \stemDown e8 | % 337
    \stemDown fis2. ~ _\! _\mp _\> \stemDown fis8 _\! r8 | % 338
    \stemDown e2 _\p \stemDown e4. _\< \stemDown e8 | % 339
    \stemDown fis2. ~ _\! _\mp _\> \stemDown fis8 _\! r8 |
    \barNumberCheck #340
    R1*3 \pageBreak | % 343
    R1*7 | \barNumberCheck #350
    \stemDown fis2. ~ _\pp \stemDown fis8 \stemDown fis8 | % 351
    fis1 ~ _\markup{ \italic {morendo} } | % 352
    fis1 ~ | % 353
    fis1 ~ | % 354
    \stemDown fis8 r8 r4 r2 ^\fermata \bar "|."
    }

PartPOneZeroVoiceTwo =  \relative c' {
    \clef "bass" \time 4/4 \key d \major s1*11 \break s1*7 \bar "||"
    s1*5 \pageBreak s1*6 | \barNumberCheck #30
    \time 2/4  s2 \break | % 31
    \time 4/4  s1*6 \break s1*7 \pageBreak s1*6 \break s1*4 \pageBreak
    s1*5 \break s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*4
    \break s1*5 \pageBreak s1*6 \bar "||"
    s1*5 \break s1*7 \bar "||"
    s1*2 \pageBreak s1*5 \break s1*4 \pageBreak s1*4 \break s1*4
    \pageBreak s1*5 \break s1*5 \bar "||"
    s1*2 \pageBreak s1*6 \pageBreak s1*4 \bar "||"
    s1*3 \break s1*11 \pageBreak s1*5 \bar "||"
    \key c \major s1*4 \pageBreak s2*9 s2*5 _\! _\p _\< \pageBreak s1*6
    \pageBreak s1*5 \break s1*5 \pageBreak s1*4 \break s1*4 \pageBreak
    s1*5 \break s1*6 \pageBreak s1*6 \pageBreak s1*4 \break s1*4
    \pageBreak s1*5 \break s1*5 \break s1*6 \pageBreak s1*5 \pageBreak
    s1*4 \pageBreak s1*6 \break s1*5 \pageBreak s1*6 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*12 \pageBreak s1*17 \break s1*3 \bar
    "||"
    \pageBreak | % 305
    \key b \major s1*6 \pageBreak s1*6 \pageBreak s1*9 \break s1*8
    \pageBreak s1 \bar "||"
    s1*8 \pageBreak s1*12 \bar "|."
    }

PartPOneOneVoiceOne =  \relative fis, {
    \clef "bass" \time 4/4 \key d \major | % 1
    R1*11 \break | % 12
    R1*7 \bar "||"
    R1*5 \pageBreak | % 24
    R1*6 | \barNumberCheck #30
    \time 2/4  R2 \break | % 31
    \time 4/4  R1*6 \break | % 37
    R1*7 \pageBreak | % 44
    R1*6 \break | \barNumberCheck #50
    R1*4 \pageBreak | % 54
    R1*5 \break | % 59
    R1*5 \pageBreak | % 64
    R1*3 | % 67
    r2 r4 \stemUp fis8 _\f \stemUp ais8 | % 68
    \stemDown dis4 \stemUp ais4 \stemUp fis4 ~ \stemUp fis8 r8
    \pageBreak | % 69
    r2 r4 \stemUp a8 _\ff \stemUp cis8 | \barNumberCheck #70
    \stemDown fis4 \stemUp cis4 \stemUp a4 ~ \stemUp a8 r8 | % 71
    r2 \stemUp g4 ~ \stemUp g8 r8 | % 72
    r2 \stemUp f4 ~ \stemUp f8 r8 | % 73
    \stemUp e4 ~ \stemUp e8 r8 \stemUp f4 ~ \stemUp f8 r8 \pageBreak | % 74
    \stemUp e4 ~ \stemUp e8 r8 \stemUp f4 ( -> \stemUp e8 ) r8 | % 75
    \stemUp f4 ( -> \stemUp e8 ) r8 \stemUp e4 ( -> \stemUp es8 ) r8 | % 76
    \stemUp e4 ( -> \stemUp es8 ) r8 \stemUp e4 ( -> _\f \stemUp es8 ) r8
    | % 77
    \stemUp e4 ( -> \stemUp es8 ) r8 r2 \break | % 78
    R1 | % 79
    r2 r4 \stemUp es4 ~ _\p | \barNumberCheck #80
    \stemUp es4 ~ _\> \stemUp es8 r8 _\! r2 | % 81
    r2 \stemUp es2 ~ _\pp | % 82
    \stemUp es2 \stemUp d2 ~ \pageBreak | % 83
    \stemUp d2 ~ \stemUp d8 r8 r4 | % 84
    R1*5 \bar "||"
    R1*5 \break | % 94
    R1*7 \bar "||"
    R1*2 \pageBreak | % 103
    R1*5 \break | % 108
    R1*4 \pageBreak | % 112
    R1 | % 113
    r4 \stemUp cis4 -- _\p \stemUp dis4 -- \stemUp eis4 -- | % 114
    \stemUp fis4 -- r4 r2 | % 115
    R1 \break | % 116
    R1*4 \pageBreak | \barNumberCheck #120
    R1*5 \break | % 125
    R1*5 \bar "||"
    R1*2 \pageBreak | % 132
    R1*2 | % 134
    r2 \stemUp d4 ~ _\mf _\> \stemUp d8 _\! _\p r8 | % 135
    r2 \stemUp d4 ~ _\mf _\> \stemUp d8 _\! _\p r8 | % 136
    r2 \stemUp gis4 ~ _\mf _\> \stemUp gis8 _\! _\p r8 | % 137
    r2 \stemUp a4 ~ _\mf _\> \stemUp a8 _\! _\p r8 \pageBreak | % 138
    r2 \stemUp d,4 ~ _\mf _\> \stemUp d8 _\! _\p r8 | % 139
    R1*3 \bar "||"
    R1*3 \break | % 145
    R1*11 \pageBreak | % 156
    R1*5 \bar "||"
    \key c \major \stemUp c2 ~ _\ff _\> \stemUp c8 _\! _\pp r8 r4 | % 162
    R1*3 \pageBreak | % 165
    \stemUp b2 ~ _\ff _\> \stemUp b8 _\! _\pp r8 r4 | % 166
    R1*3 | % 169
    bes1 ~ _\ff _\> | \barNumberCheck #170
    \stemUp bes8 _\! \stemUp bes8 -> _\ff \stemUp bes8 -> \stemUp bes8
    -> \stemUp bes8 -> \stemUp a8 -> r4 | % 171
    R1 \pageBreak | % 172
    R1*2 | % 174
    r2 r8 \stemUp d8 -. _\mf \stemUp a8 -. r8 | % 175
    R1*3 \pageBreak | % 178
    r2 r4 \stemUp e'8 -. _\mf \stemUp b8 -. | % 179
    \stemUp e8 -. r8 r4 r2 | \barNumberCheck #180
    R1*2 | % 182
    r2 r8 \stemUp e8 -. _\mf \stemUp b8 -. r8 \break | % 183
    R1*5 \pageBreak | % 188
    R1 | % 189
    r2 r4 \stemUp g4 ~ _\fff | \barNumberCheck #190
    g1 ~ | % 191
    \stemUp g2. \stemUp g4 ~ \break | % 192
    g1 ~ | % 193
    \stemUp g2. \stemUp gis4 | % 194
    a1 ~ | % 195
    a1 \pageBreak | % 196
    a1 ~ | % 197
    \stemUp a2 \stemUp a8 -> \stemUp a8 -> r4 | % 198
    R1*3 \break | % 201
    R1*4 | % 205
    r2 r4 r8. \stemUp c'16 _\p | % 206
    \stemUp c2 -> _\markup{ \italic {poco a poco cresc.} } \stemUp cis2
    \pageBreak | % 207
    \stemDown d8 r8 r4 r4 r8. \stemDown es16 | % 208
    \stemDown es2 -> \stemDown e2 | % 209
    \stemDown f8 r8 r4 r4 r8. \stemUp dis,16 _\mf | \barNumberCheck #210
    \stemUp dis8 _\markup{ \italic {poco cresc.} } r8 \stemUp e8 r8
    \stemUp eis8 r8 \stemUp fis8 r16 \stemUp fis16 | % 211
    \stemUp fis8 r8 \stemUp g8 r8 \stemUp gis8 r8 \stemUp a8 r8 | % 212
    \stemUp ais8 r8 \stemUp b8 r8 \stemUp bis8 _\f _\< r8 \stemUp cis8 r8
    \pageBreak | % 213
    \stemUp bis8 r8 \stemUp cis8 r8 \stemUp bis8 r8 \stemUp cis8 r8 | % 214
    \stemUp d,4 -- _\! _\ff \stemUp dis4 -- \stemUp eis4 -- \stemUp fis4
    -- | % 215
    R1*2 \break | % 217
    R1 | % 218
    \stemUp d4 -- _\f \stemUp dis4 -- \stemUp eis4 -- \stemUp fis4 -- | % 219
    R1*2 \pageBreak | % 221
    R1*5 \break | % 226
    R1*5 \break | % 231
    R1*6 \pageBreak | % 237
    R1*5 \pageBreak | % 242
    R1 | % 243
    \stemUp fis4.. _\ff \stemUp fis16 \stemUp ais4.. \stemUp ais16 | % 244
    \stemUp b8 r8 r4 r4 \stemUp d,8 _\fff \stemUp e8 | % 245
    \stemUp eis4 ( -> \stemUp fis8 ) r8 r4 \stemUp d8 \stemUp e8
    \pageBreak | % 246
    \stemUp eis4 ( -> \stemUp fis8 ) r8 r4 r8 \stemUp cis8 | % 247
    r8 \stemUp d8 r8 \stemUp g8 r8 \stemUp fis8 r8 \stemUp cis8 | % 248
    r8 \stemUp d8 r8 \stemUp g8 \stemUp fis8 r8 r4 | % 249
    R1*3 \break | % 252
    R1*5 \pageBreak | % 257
    R1*2 | % 259
    r2 r4 \stemUp fis4 _\pp | \barNumberCheck #260
    \stemUp g4 _\markup{ \italic {poco cresc.} } \stemUp as4 \stemUp a4
    \stemUp des,4 _\mp | % 261
    \stemUp ces4 _\markup{ \italic {cresc.} } \stemUp c4 \stemUp cis4
    \stemUp d4 | % 262
    \stemUp dis4 \stemUp e4 \stemUp f4 \stemUp ges8 _\ff \stemUp f8
    \pageBreak | % 263
    \stemUp es8 r8 \stemUp ges8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp ges8 \stemUp f8 \stemUp es8 }
    | % 264
    \stemUp es8 r8 \stemUp ges8 r8 r4 \stemUp a8 \stemUp gis8 | % 265
    \stemUp fis8 r8 \stemUp a8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp gis8 \stemUp fis8 }
    | % 266
    \stemUp fis8 r8 \stemUp a8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp gis8 \stemUp fis8 }
    | % 267
    \stemUp fis8 r8 \stemUp fis2 _\fff \stemUp gis4 \pageBreak | % 268
    \stemUp a4 \stemUp b4 \stemUp c4 \stemDown d4 | % 269
    \stemDown es4 \stemDown f4 \stemDown fis4 \stemDown gis4 |
    \barNumberCheck #270
    \stemDown a8 r8 r4 r2 | % 271
    r4 \stemUp fis,2 _\ff \stemUp gis4 | % 272
    \stemUp a4 \stemUp b4 \stemUp c4 \stemDown d4 \pageBreak | % 273
    \stemDown es4 \stemDown f4 \stemDown fis4 \stemDown gis4 | % 274
    R1*6 | \barNumberCheck #280
    r2 r4 \stemDown dis4 _\f | % 281
    cis1 ~ | % 282
    \stemUp cis2. \stemUp b4 | % 283
    ais1 ~ | % 284
    ais1 \pageBreak | % 285
    \stemUp b2 ~ \stemUp b8 r8 \stemUp fis4 _\ff ^\markup{ \italic
        {marcato} } | % 286
    \stemUp cis'4.. \stemUp b16 \stemUp b2 | % 287
    r2 r4 \stemDown d4 | % 288
    \stemDown g4.. \stemDown fis16 \stemDown fis2 | % 289
    R1*6 | % 295
    r2 r4 \stemUp ais,4 | % 296
    \stemDown d4.. \stemUp cis16 \stemUp cis2 | % 297
    \stemUp b4.. \stemUp ais16 \stemUp ais2 | % 298
    \stemUp g4.. \stemUp fis16 \stemUp fis2 | % 299
    eis1 ~ _\ffff _\> | \barNumberCheck #300
    \stemUp eis2 ~ \stemUp eis8 _\! _\p r8 r4 | % 301
    R1 \break | % 302
    R1*3 \bar "||"
    \pageBreak | % 305
    \key b \major R1*6 \pageBreak | % 311
    R1*2 | % 313
    \stemUp b2 _\p _\< \stemUp b2 _\! _\f | % 314
    \stemUp b2 \stemUp b2 | % 315
    \stemUp b2 \stemUp eis4 ~ _\sff _\> \stemUp eis8 r8 _\! | % 316
    \stemUp fis4 ~ _\mf \stemUp fis8 r8 \stemUp fis4 ~ \stemUp fis8 r8
    \pageBreak | % 317
    \stemUp b,2 \stemUp b2 ~ _\p | % 318
    \stemUp b2 \stemUp b2 ~ | % 319
    \stemUp b2 \stemUp b2 ~ | \barNumberCheck #320
    \stemUp b2 \stemUp b2 ~ | % 321
    \stemUp b2 r2 | % 322
    R1*4 \break | % 326
    R1*8 \pageBreak | % 334
    R1 \bar "||"
    R1*8 \pageBreak | % 343
    R1*8 | % 351
    b'1 ~ _ "" _\markup{ \italic {morendo} } | % 352
    b1 ~ | % 353
    b1 ~ | % 354
    \stemUp b8 r8 r4 r2 ^\fermata \bar "|."
    }

PartPOneOneVoiceTwo =  \relative c' {
    \clef "bass" \time 4/4 \key d \major s1*11 \break s1*7 \bar "||"
    s1*5 \pageBreak s1*6 | \barNumberCheck #30
    \time 2/4  s2 \break | % 31
    \time 4/4  s1*6 \break s1*7 \pageBreak s1*6 \break s1*4 \pageBreak
    s1*5 \break s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*4
    \break s1*5 \pageBreak s1*6 \bar "||"
    s1*5 \break s1*7 \bar "||"
    s1*2 \pageBreak s1*5 \break s1*4 \pageBreak s1*4 \break s1*4
    \pageBreak s1*5 \break s1*5 \bar "||"
    s1*2 \pageBreak s1*6 \pageBreak s1*4 \bar "||"
    s1*3 \break s1*11 \pageBreak s1*5 \bar "||"
    \key c \major s1*4 \pageBreak s2*9 s2*5 _\! _\p _\< \pageBreak s1*6
    \pageBreak s1*5 \break s1*5 \pageBreak s1*4 \break s1*4 \pageBreak
    s1*5 \break s1*6 \pageBreak s1*6 \pageBreak s1*4 \break s1*4
    \pageBreak s1*5 \break s1*5 \break s1*6 \pageBreak s1*5 \pageBreak
    s1*4 \pageBreak s1*6 \break s1*5 \pageBreak s1*6 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*12 \pageBreak s1*17 \break s1*3 \bar
    "||"
    \pageBreak | % 305
    \key b \major s1*6 \pageBreak s1*6 \pageBreak s1*9 \break s1*8
    \pageBreak s1 \bar "||"
    s1*8 \pageBreak s1*12 \bar "|."
    }

PartPOneTwoVoiceOne =  \relative a, {
    \clef "bass" \time 4/4 \key c \major | % 1
    R1*11 \break | % 12
    R1*7 \bar "||"
    R1*5 \pageBreak | % 24
    R1*6 | \barNumberCheck #30
    \time 2/4  R2 \break | % 31
    \time 4/4  R1*6 \break | % 37
    R1*7 \pageBreak | % 44
    R1*6 \break | \barNumberCheck #50
    R1*4 \pageBreak | % 54
    R1*5 \break | % 59
    R1*5 \pageBreak | % 64
    R1*5 \pageBreak | % 69
    R1 | \barNumberCheck #70
    r2 \stemUp a4 :32 _\ff \stemUp a8 r8 | % 71
    r2 \stemUp a4 :32 \stemUp a8 r8 | % 72
    r2 \stemUp a4 :32 \stemUp a8 r8 | % 73
    \stemDown e'4 :32 \stemDown e8 r8 \stemUp a,4 :32 \stemUp a8 r8
    \pageBreak | % 74
    \stemDown e'4 :32 \stemDown e8 r8 \stemUp a,8 r8 \stemDown e'8 r8 | % 75
    \stemUp a,8 r8 \stemDown e'8 r8 \stemDown e8 r8 \stemDown es8 r8 | % 76
    \stemDown e8 r8 \stemDown es8 r8 r2 ^\markup{ \italic {muta in} } ^
    "C, D, E" | % 77
    R1 \break | % 78
    R1*5 \pageBreak | % 83
    R1*6 \bar "||"
    R1*5 \break | % 94
    R1*7 \bar "||"
    R1*2 \pageBreak | % 103
    R1*5 \break | % 108
    R1*4 \pageBreak | % 112
    R1*4 \break | % 116
    R1*4 \pageBreak | \barNumberCheck #120
    R1*5 \break | % 125
    R1*5 \bar "||"
    R1*2 \pageBreak | % 132
    R1*2 | % 134
    r2 \stemDown d2 :32 _\p _\< | % 135
    \stemDown d8 _\! _\mf r8 r4 \stemDown d2 :32 _\p _\< | % 136
    \stemDown d8 _\! _\mf r8 r4 r2 | % 137
    R1 \pageBreak | % 138
    r2 \stemDown d2 :32 _\p _\< | % 139
    \stemDown d8 _\! _\mf r8 r4 \stemDown d2 :32 _\p _\< |
    \barNumberCheck #140
    \stemDown d8 _\! _\mf r8 r4 r2 | % 141
    R1 \bar "||"
    r2 \stemDown d2 :32 _\mp | % 143
    d1 :32 _\> | % 144
    d1 :32 \break | % 145
    d1 :32 _\! _\p | % 146
    d1 :32 _\markup{ \italic {poco a poco smorz.} } | % 147
    d1 :32 | % 148
    d1 :32 | % 149
    d1 :32 | \barNumberCheck #150
    d1 :32 | % 151
    d1 :32 | % 152
    d1 :32 _\ppp | % 153
    \stemDown d4 :32 \stemDown d8 r8 r2 | % 154
    d1 :32 _\pppp _\< | % 155
    \stemDown d2 :32 _\! _\pppp \stemDown d8 r8 r4 \pageBreak | % 156
    d1 :32 _\pppp _\< | % 157
    \stemDown d2 :32 _\! _\pppp \stemDown d8 r8 r4 | % 158
    \stemDown d2 :32 _\pppp \stemDown d8 r8 r4 | % 159
    \stemDown d2 :32 _\ppppp \stemDown d8 r8 r4 | \barNumberCheck #160
    R1 \bar "||"
    \key c \major \stemUp c2 :32 _\ff _\> \stemUp c8 _\! _\pp r8 r4 | % 162
    R1*3 \pageBreak | % 165
    \stemDown e2 :32 _\ff _\> \stemDown e8 _\! _\pp r8 r4 | % 166
    R1*3 | % 169
    d1 :32 _\ff _\> | \barNumberCheck #170
    \stemDown d8 _\! \stemDown d8 -> _\ff \stemDown d8 -> \stemDown d8
    -> \stemDown d8 -> \stemDown d8 -> r4 | % 171
    R1 \pageBreak ^\markup{ \italic {muta in} } | % 172
    R1*6 \pageBreak ^ "G, D, A" | % 178
    R1*5 \break | % 183
    R1*5 \pageBreak | % 188
    R1 | % 189
    r2 r4 \stemUp g,4 :32 _\fff | \barNumberCheck #190
    g1 :32 | % 191
    g1 :32 \break | % 192
    g1 :32 | % 193
    \stemUp g2. :32 \stemDown d'4 :32 | % 194
    a1 :32 | % 195
    a1 :32 \pageBreak | % 196
    a1 :32 | % 197
    \stemUp a2 :32 \stemUp a8 -> \stemUp a8 -> r4 | % 198
    R1*3 \break ^\markup{ \italic {muta in} } | % 201
    R1*6 \pageBreak ^ "Fis, H, E" | % 207
    R1*6 \pageBreak | % 213
    R1*4 \break | % 217
    R1*4 \pageBreak | % 221
    R1*5 \break | % 226
    R1*5 \break | % 231
    R1*6 \pageBreak | % 237
    R1*5 \pageBreak | % 242
    R1*2 | % 244
    r2 r4 \stemUp b8 _\fff \stemUp e8 | % 245
    \stemUp b8 -> r8 \stemUp fis8 r8 r4 \stemUp b8 \stemUp e8 \pageBreak
    | % 246
    \stemUp b8 -> r8 \stemUp fis8 r8 r4 r8 \stemDown e'8 | % 247
    r8 \stemUp b8 r8 \stemDown e8 r8 \stemUp b8 r8 \stemDown e8 | % 248
    r8 \stemUp b8 r8 \stemUp b8 \stemUp fis8 r8 r4 | % 249
    R1*3 \break | % 252
    R1*5 \pageBreak | % 257
    R1*6 \pageBreak | % 263
    R1*4 | % 267
    r4 \stemUp fis2. :32 _\fff \pageBreak | % 268
    fis1 :32 | % 269
    fis1 :32 | \barNumberCheck #270
    fis1 :32 _\> | % 271
    fis1 :32 _\! _\ff | % 272
    fis1 :32 \pageBreak | % 273
    fis1 :32 | % 274
    fis1 :32 | % 275
    fis1 :32 | % 276
    fis1 :32 _\> | % 277
    fis1 :32 _\! _\f | % 278
    fis1 :32 | % 279
    fis1 :32 | \barNumberCheck #280
    fis1 :32 | % 281
    fis1 :32 | % 282
    fis1 :32 | % 283
    fis1 :32 | % 284
    fis1 :32 _\< \pageBreak | % 285
    fis1 :32 _\! _\ff | % 286
    fis1 :32 | % 287
    fis1 :32 | % 288
    fis1 :32 | % 289
    fis1 :32 | \barNumberCheck #290
    fis1 :32 | % 291
    fis1 :32 | % 292
    fis1 :32 | % 293
    fis1 :32 | % 294
    fis1 :32 | % 295
    fis1 :32 | % 296
    fis1 :32 | % 297
    fis1 :32 | % 298
    fis1 :32 _\< | % 299
    fis1 :32 _\! _\fff _\> | \barNumberCheck #300
    fis1 :32 | % 301
    fis1 :32 _\ff _\> \break | % 302
    \stemUp fis8 _\! _\f r8 r4 \stemUp fis8 _\mf r8 r4 | % 303
    r2 \stemUp fis8 _\p r8 r4 | % 304
    \stemUp fis8 _\pp r8 r4 r2 ^\fermata \bar "||"
    \pageBreak | % 305
    \key c \major R1*4 | % 309
    r2 \stemUp b2 :32 _\pp _\< | \barNumberCheck #310
    b1 :32 \pageBreak | % 311
    \stemUp b2 :32 \stemUp b8 _\! _\mf r8 r4 | % 312
    r2 \stemUp fis2 :32 _\pp _\< | % 313
    b1 :32 | % 314
    b1 :32 | % 315
    \stemUp b2 :32 \stemUp b8 _\! _\sff r8 r4 | % 316
    \stemUp fis2 :32 _\p _\< \stemUp fis2 :32 _\! _\mf _\> \pageBreak | % 317
    b1 :32 _\! _\p | % 318
    b1 :32 | % 319
    b1 :32 | \barNumberCheck #320
    b1 :32 | % 321
    b1 :32 | % 322
    b1 :32 | % 323
    b1 :32 | % 324
    b1 :32 | % 325
    \stemUp b2 :32 _\> \stemUp b8 _\! _\pp r8 r4 \break | % 326
    R1 | % 327
    r8 \stemUp b32 _\pppp _\< \stemUp b32 \stemUp b32 \stemUp b32
    \stemUp b4 :32 _\! _\pp _\> \stemUp b8 _\! _\pppp r8 r4 | % 328
    R1 | % 329
    r8 \stemUp b32 _\pppp _\< \stemUp b32 \stemUp b32 \stemUp b32
    \stemUp b4 :32 _\! _\pp _\> \stemUp b8 _\! _\pppp r8 r4 |
    \barNumberCheck #330
    r8 \stemUp b32 _\pppp _\< \stemUp b32 \stemUp b32 \stemUp b32
    \stemUp b2. :256 | % 331
    \stemUp b2 :32 \stemUp b8 _\! _\p r8 r4 | % 332
    r8 \stemUp fis32 _\pppp _\< \stemUp fis32 \stemUp fis32 \stemUp fis32
    \stemUp fis4 :32 _\! _\> \stemUp fis8 _\! r8 r4 | % 333
    r8 \stemUp b32 _\pppp _\< \stemUp b32 \stemUp b32 \stemUp b32
    \stemUp b4 :32 _\! _\> \stemUp b8 _\! r8 r4 \pageBreak | % 334
    r8 \stemUp b32 _\pppp _\< \stemUp b32 \stemUp b32 \stemUp b32
    \stemUp b4 :32 _\! _\> \stemUp b8 _\! r8 r4 \bar "||"
    R1*8 \pageBreak | % 343
    R1*8 | % 351
    b1 :32 _ "" _\markup{ \italic {morendo} } | % 352
    \stemUp b8 r8 r4 \stemUp b8 r8 r4 | % 353
    \stemUp b8 r8 r4 \stemUp b8 r8 r4 | % 354
    \stemUp b8 r8 r4 r2 ^\fermata \bar "|."
    }

PartPOneTwoVoiceTwo =  \relative d {
    \clef "bass" \time 4/4 \key c \major s1*11 \break s1*7 \bar "||"
    s1*5 \pageBreak s1*6 | \barNumberCheck #30
    \time 2/4  s2 \break | % 31
    \time 4/4  s1*6 \break s1*7 \pageBreak s1*6 \break s1*4 \pageBreak
    s1*5 \break s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*4
    \break s1*5 \pageBreak s1*6 \bar "||"
    s1*5 \break s1*7 \bar "||"
    s1*2 \pageBreak s1*5 \break s1*4 \pageBreak s1*4 \break s1*4
    \pageBreak s1*5 \break s1*5 \bar "||"
    s1*2 \pageBreak s1*6 \pageBreak s1*4 \bar "||"
    s1*3 \break s1*9 | % 154
     \once \override NoteHead.style = ##f \stemNeutral d2 \once
    \override NoteHead.style = ##f \stemNeutral d2 _\! _\pp _\> s1
    \pageBreak | % 156
     \once \override NoteHead.style = ##f \stemNeutral d2 \once
    \override NoteHead.style = ##f \stemNeutral d2 _\! _\pp _\> s1*4
    \bar "||"
    \key c \major s1*4 \pageBreak s1*4 | % 169
     \once \override NoteHead.style = ##f \stemNeutral d2 \once
    \override NoteHead.style = ##f \stemNeutral d2 _\! _\p _\< s1*2
    \pageBreak s1*6 \pageBreak s1*5 \break s1*5 \pageBreak s1*4 \break
    s1*4 \pageBreak s1*5 \break s1*6 \pageBreak s1*6 \pageBreak s1*4
    \break s1*4 \pageBreak s1*5 \break s1*5 \break s1*6 \pageBreak s1*5
    \pageBreak s1*4 \pageBreak s1*6 \break s1*5 \pageBreak s1*6
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*12 \pageBreak s2*31
    s1. _\! _\p \break s1*3 \bar "||"
    \pageBreak | % 305
    \key c \major s1*6 \pageBreak s1*6 \pageBreak s1*9 \break s1*8
    \pageBreak s1 \bar "||"
    s1*8 \pageBreak s1*12 \bar "|."
    }

PartPOneThreeVoiceOne =  \relative b {
    \clef "treble" \time 4/4 \key d \major | % 1
    R1*11 \break | % 12
    R1*7 \bar "||"
    R1*5 \pageBreak | % 24
    R1*6 | \barNumberCheck #30
    \time 2/4  r4 ^ "I. Hälfte" \stemUp b8 ( -. _\pp _\< \stemUp cis8 )
    -. \break | % 31
    \time 4/4  \stemUp d4 ( _\! _\> \stemUp cis8 ) r8 _\! r4 \stemUp b16
    ( _\< \stemUp e16 \stemUp d16 \stemUp b16 ) | % 32
    \stemUp d4 ( _\! _\> \stemUp cis8 ) r8 _\! r4 \stemUp d8 ( -. _\<
    \stemUp e8 ) -. | % 33
    \stemUp f4 ( _\! _\> \stemUp e8 ) r8 _\! r4 \stemUp d16 ( _\<
    \stemUp g16 \stemUp f16 \stemUp d16 ) | % 34
    \stemUp f4 ( _\! _\> \stemUp e8 ) r8 _\! r4 \stemUp <bes f'>8 ( -.
    _\p _\< \stemUp <b g'>8 ) -. | % 35
    \stemUp as'8 ( _\! _\> \stemUp g8 ) \stemUp f16 ( _\! _\p _\<
    \stemUp bes16 \stemUp as16 \stemUp f16 ) \stemUp as8 ( _\! _\>
    \stemUp g8 ) \stemUp <cis, gis'>8 ( _. _\! _\p _\< \stemUp <cisis
        ais'>8 ) _. | % 36
    \stemUp b'8 ( _\! _\> \stemUp ais8 ) \stemUp gis16 ( _\! _\< \stemUp
    cis16 \stemUp b16 \stemUp gis16 ) \stemUp b8 ( _\! _\> \stemUp ais8
    ) \stemUp <e b'>8 ( _. _\! _\mp _\< \stemUp <eis cis'>8 ) _. \break
    | % 37
    \stemUp d'16 -. _\! _\markup{ \italic {cresc.} } \stemUp cis16 -.
    \stemUp d16 -. \stemUp cis16 -. \stemUp e16 -. \stemUp d16 -.
    \stemUp e16 -. \stemUp d16 -. \stemUp fis16 -. \stemUp e16 -.
    \stemUp fis16 -. \stemUp e16 -. \stemUp g16 -. \stemUp fis16 -.
    \stemUp g16 -. \stemUp fis16 -. | % 38
    \stemUp b16 ( \stemUp ais16 ) \stemUp cis16 ( \stemUp b16 ) \stemUp
    d16 ( \stemUp cis16 ) \stemUp e16 ( \stemUp d16 ) \stemDown <d fis>2
    ~ ^> ~ _\ff | % 39
    \stemDown <d fis>16 \stemDown <cis e>16 -. \stemDown <b d>16 -.
    \stemDown <a cis>16 -. \stemDown <g b>16 -. _\> \stemDown <fis a>16
    -. \stemDown <e g>16 -. \stemDown <d fis>16 -. \stemDown <cis e>8 -.
    r8 _\! r4 | \barNumberCheck #40
    R1*2 | % 42
    r2 r8 ^\markup{ \italic {unis.} } \stemUp cis,16 ( -. ^\markup{
        \italic {saltando} } _\pp \stemUp cis16 ) -. \stemUp d8 ( -.
    \stemUp cis8 -. | % 43
    \stemUp fis8 ) -. \stemUp a16 ( -. \stemUp a16 ) -. \stemUp d8 ( -.
    \stemUp fis,8 -. \stemUp b8 ) -. \stemUp d,16 ( -. \stemUp d16 ) -.
    \stemUp g8 ( -. \stemUp a,8 ) -. \pageBreak | % 44
    \stemUp a16 ( \stemUp b16 \stemUp a16 \stemUp b16 \stemUp a16
    \stemUp b16 \stemUp a16 \stemUp b16 \stemUp a8 ) \stemUp gis16 ( -.
    \stemUp gis16 ) -. \stemUp a8 ( -. \stemUp b8 -. | % 45
    \stemUp cis8 ) -. \stemUp d16 ( -. \stemUp d16 ) -. \stemUp fis8 (
    -. \stemUp b,8 -. \stemUp cis8 ) -. \stemUp gis16 ( -. \stemUp gis16
    ) -. \stemUp a8 ( -. \stemUp b8 ) -. | % 46
    \stemUp fis'16 ( \stemUp b,16 \stemUp fis'16 \stemUp b,16 \stemUp
    fis'16 \stemUp b,16 \stemUp fis'16 \stemUp b,16 ) \stemUp fis'8 -.
    \stemUp gis16 ( -. _\p \stemUp gis16 ) -. \stemUp a8 ( -. \stemUp
    gis8 -. | % 47
    \stemDown cis8 ) -. \stemDown e16 ( -. \stemDown e16 ) -. \stemDown
    a8 ( -. \stemDown cis,8 -. \stemDown fis8 ) -. \stemDown a,16 ( -.
    \stemDown a16 ) -. \stemUp d8 ( -. \stemUp e,8 ) -. | % 48
    \stemUp e16 ( \stemUp fis16 \stemUp e16 \stemUp fis16 \stemUp e16
    \stemUp fis16 \stemUp e16 \stemUp fis16 ) \stemUp e8 -. \stemUp dis16
    ( -. \stemUp dis16 ) -. \stemUp e8 ( -. \stemUp fis8 -. | % 49
    \stemUp gis8 ) -. \stemUp a16 ( -. \stemUp a16 ) -. \stemUp cis8 (
    -. \stemUp fis,8 -. \stemUp gis8 ) -. \stemUp dis16 ( -. \stemUp dis16
    ) -. \stemUp e8 ( -. \stemUp fis8 ) -. \break | \barNumberCheck #50
    \stemUp cis'16 ( \stemUp fis,16 \stemUp cis'16 \stemUp fis,16
    \stemUp cis'16 \stemUp fis,16 \stemUp cis'16 \stemUp fis,16
    \stemDown cis'16 ) \stemDown cis'16 -. _\mp \stemDown cis16 -.
    \stemDown cis16 -. \stemDown cis16 ( \stemDown e16 ) \stemDown bis16
    -. \stemDown cis16 -. | % 51
    \stemDown gis16 ( \stemDown a16 ) \stemDown gis16 -. \stemDown fis16
    -. \stemDown e16 -. \stemDown dis16 -. \stemDown cis16 -. \stemDown
    bis16 -. \stemDown cis8 -. r8 r4 | % 52
    r2 r16 \stemDown cis'16 -. _\mp \stemDown cis16 -. \stemDown cis16
    -. \stemDown cis16 ( \stemDown e16 ) \stemDown bis16 -. \stemDown
    cis16 -. | % 53
    \stemDown gis16 ( \stemDown a16 ) \stemDown gis16 -. \stemDown fis16
    -. \stemDown e16 -. \stemDown dis16 -. \stemDown cis16 -. \stemDown
    bis16 -. \stemDown cis8 -. r8 r4 \pageBreak | % 54
    R1 | % 55
    r16 \stemUp gis16 -. _\pp _\< \stemUp gis16 -. \stemUp gis16 -.
    \stemUp gis16 ( \stemUp fis16 ) \stemUp e16 -. \stemUp dis16 -.
    \stemUp cis8 ( -- _\! _\> \stemUp ais8 ) -- \stemUp b8 -- r8 _\! | % 56
    r16 \stemUp e16 -. _\pp _\< \stemUp e16 -. \stemUp e16 -. \stemUp e16
    ( \stemUp dis16 ) \stemUp cis16 -. \stemUp b16 -. \stemUp a8 ( --
    _\! _\> \stemUp fisis8 ) -- \stemUp gis8 -- r8 _\! | % 57
    r16 \stemDown b'16 -. _\p _\< \stemDown b16 -. \stemDown b16 -.
    \stemUp b16 ( \stemUp ais16 ) \stemUp gis16 -. \stemUp fisis16 -.
    \stemUp e8 ( -- _\! _\> \stemUp cisis8 ) -- \stemUp dis8 -- r8 _\! | % 58
    r2 r16 \stemDown gis'16 -. _\mp \stemDown gis16 -. \stemDown gis16
    -. \stemDown gis16 ( \stemDown b16 ) \stemDown fisis16 -. \stemDown
    gis16 -. \break | % 59
    \stemDown dis16 ( \stemDown e16 ) \stemDown dis16 -. \stemDown cis16
    -. \stemUp b16 -. \stemUp ais16 -. \stemUp gis16 -. \stemUp fisis16
    -. \stemUp gis8 -. r8 r4 | \barNumberCheck #60
    r2 r16 \stemDown gis'16 -. _\mp \stemDown gis16 -. \stemDown gis16
    -. \stemDown gis16 ( \stemDown b16 ) \stemDown fisis16 -. \stemDown
    gis16 -. | % 61
    \stemDown dis16 ( \stemDown e16 ) \stemDown dis16 -. \stemDown cis16
    -. \stemUp b16 -. \stemUp ais16 -. \stemUp gis16 -. \stemUp fisis16
    -. \stemUp gis8 -. r8 r4 | % 62
    R1*2 \pageBreak | % 64
    R1*3 | % 67
    r16 \stemUp gis16 -. _\f \stemUp gis16 -. \stemUp gis16 -. \stemUp
    gis16 ( \stemUp b16 ) \stemUp ais16 -. \stemUp gis16 -. \stemUp fis8
    -. r8 r4 | % 68
    R1 \pageBreak | % 69
    r16 \stemDown b16 -. _\ff \stemDown b16 -. \stemDown b16 -.
    \stemDown b16 ( \stemDown d16 ) \stemDown cis16 -. \stemDown b16 -.
    \stemUp a8 -. r8 r4 | \barNumberCheck #70
    r2 r16 \stemDown a''16 _ "" _\markup{ \italic {détaché} }
    \stemDown a16 \stemDown a16 \stemDown a16 \stemDown c16 \stemDown b16
    \stemDown a16 | % 71
    \stemDown f16 \stemDown e16 \stemDown d16 \stemDown c16 \stemDown b16
    \stemDown a16 \stemDown f16 \stemDown e16 r16 \stemDown a'16
    \stemDown a16 \stemDown a16 \stemDown a16 \stemDown c16 \stemDown b16
    \stemDown a16 | % 72
    \stemDown f16 \stemDown e16 \stemDown d16 \stemDown c16 \stemDown b16
    \stemDown a16 \stemDown f16 \stemDown e16 r16 \stemDown a'16
    \stemDown a16 \stemDown a16 \stemDown a16 \stemDown c16 \stemDown b16
    \stemDown a16 | % 73
    r16 \stemDown a,16 \stemDown a16 \stemDown a16 \stemDown a16
    \stemDown c16 \stemDown b16 \stemDown a16 r16 \stemDown a'16
    \stemDown a16 \stemDown a16 \stemDown a16 \stemDown c16 \stemDown b16
    \stemDown a16 \pageBreak | % 74
    r16 \stemDown a,16 \stemDown a16 \stemDown a16 \stemDown a16 (
    \stemDown c16 \stemDown b16 ) \stemDown a16 -. r16 \stemDown a16
    \stemDown a16 \stemDown a16 \stemDown a16 ( \stemDown c16 \stemDown
    b16 ) \stemDown a16 -. | % 75
    r16 \stemDown a16 \stemDown a16 \stemDown a16 \stemDown a16 (
    \stemDown c16 \stemDown b16 ) \stemDown a16 -. r16 \stemDown a16
    \stemDown a16 \stemDown a16 \stemDown a16 ( \stemDown cis16
    \stemDown b16 ) \stemDown a16 -. | % 76
    r16 \stemDown a16 \stemDown a16 \stemDown a16 \stemDown a16 (
    \stemDown cis16 \stemDown b16 ) \stemDown a16 -. r16 \stemUp a,16
    _\f \stemUp a16 \stemUp a16 \stemUp a16 ( \stemUp cis16 \stemUp b16
    ) \stemUp a16 -. | % 77
    r16 \stemUp a16 \stemUp a16 \stemUp a16 \stemUp a16 ( \stemUp cis16
    \stemUp b16 ) \stemUp a16 -. r16 \stemUp a,16 _\mf \stemUp a16
    \stemUp a16 \stemUp a16 ( \stemUp cis16 \stemUp b16 ) \stemUp a16 -.
    \break | % 78
    r16 \stemUp a16 \stemUp a16 \stemUp a16 \stemUp a16 ( \stemUp cis16
    \stemUp b16 ) \stemUp a16 -. r16 \stemUp a16 _\mp \stemUp a16
    \stemUp a16 \stemUp a16 ( \stemUp cis16 \stemUp b16 ) \stemUp a16 -.
    | % 79
    \stemUp a16 -. \stemUp cis16 -. \stemUp b16 -. \stemUp a16 -.
    \stemUp a16 -. \stemUp cis16 -. \stemUp b16 -. \stemUp a16 -. r16
    \stemUp a16 -. _\p \stemUp a16 -. \stemUp a16 -. \stemUp a16 -.
    \stemUp cis16 -. \stemUp b16 -. \stemUp a16 -. | \barNumberCheck #80
    \stemUp a16 -. _\> \stemUp cis16 -. \stemUp b16 -. \stemUp a16 -.
    \stemUp a16 -. \stemUp cis16 -. \stemUp b16 -. \stemUp a16 -. r2 _\!
    | % 81
    R1*2 \pageBreak | % 83
    R1*6 \bar "||"
    r2 r8 \stemDown fis''8 ( _\p ^\markup{ \italic {con
            sordini,teneramente, molto cantabile, con espansione} }
    \stemDown e8 \stemDown d8 ) | \barNumberCheck #90
    \stemUp b8 ( _\< \stemUp a8 \stemUp fis8 \stemUp a8 ) \stemDown d4.
    ( _\! _\> \stemDown b8 ) | % 91
    \stemUp a2 ~ _\! \stemDown a8 \stemDown fis'8 ( \stemDown e8
    \stemDown d8 ) | % 92
    \stemUp a8 ( _\< \stemUp fis8 \stemUp d8 \stemUp fis8 ) \stemDown b4.
    ( _\! _\> \stemUp a8 ) | % 93
    \stemUp a2 _\! _\< \stemDown a'4 -- _\! _\f \stemDown g8 ( \stemDown
    fis8 ) \break | % 94
    \stemDown fis4 ( -> \stemDown e4 ) \stemDown g4 -- _\> \stemDown fis8
    ( \stemDown e8 ) | % 95
    \stemDown e4 ( -> _\! _\mf _\< \stemDown d4 ) r8 _\! \stemDown fis8
    ( _\f _\> \stemDown e8 \stemDown d8 ) | % 96
    \stemUp a8 ( _\! _\< \stemUp fis8 \stemUp d8 \stemUp fis8 )
    \stemDown b4. ( _\! _\> \stemUp a8 ) | % 97
    \stemUp a2 _\! _\< \stemDown a'4 -- _\! _\f \stemDown g8 ( \stemDown
    fis8 ) | % 98
    \stemDown fis4 ( -> \stemDown e4 ) \stemDown g4 -- _\> \stemDown fis8
    ( \stemDown e8 ) | % 99
    \stemDown e4 ( -> _\! _\mf _\< \stemDown d4 ) r8 _\! \stemDown fis8
    ( _\f _\> \stemDown e8 \stemDown d8 ) | \barNumberCheck #100
    \stemUp a8 ( _\! _\< \stemUp fis8 \stemUp d8 \stemUp fis8 )
    \stemDown b4. ( _\! _\> \stemUp a8 ) \bar "||"
    \stemUp a8 _\! _\p \stemUp fis16 ( -. ^\markup{ \italic {saltando} }
    \stemUp fis16 ) -. \stemUp fis8 ( -. \stemUp fis8 -. \stemUp fis8 )
    -. \stemUp fis16 ( -. \stemUp fis16 ) -. \stemUp fis8 ( -. \stemUp
    fis8 -. | % 102
    \stemUp fis8 ) -. \stemUp fis16 ( -. \stemUp fis16 ) -. \stemUp fis8
    ( -. \stemUp fis8 -. \stemUp fis8 ) -. \stemUp fis16 ( -. \stemUp
    fis16 ) -. \stemUp fis8 ( -. \stemUp fis8 -. \pageBreak | % 103
    \stemUp g8 ) -. \stemUp g16 ( -. \stemUp g16 ) -. \stemUp g8 ( -.
    \stemUp g8 -. \stemUp g8 ) -. \stemUp g16 ( -. \stemUp g16 ) -.
    \stemUp g8 ( -. \stemUp g8 -. | % 104
    \stemUp a8 ) -. _\< \stemUp a16 ( -. \stemUp a16 ) -. \stemUp a8 (
    -. \stemUp a8 -. \stemUp a8 ) -. \stemUp a16 ( -. \stemUp a16 ) -.
    \stemUp a8 ( -. \stemUp a8 -. | % 105
    \stemUp ais8 ) -. _\! _\markup{ \italic {poco più} } _ "" \stemUp
    ais16 ( -. \stemUp ais16 ) -. \stemUp ais8 ( -. \stemUp ais8 -.
    \stemUp fis8 ) -. \stemUp fis16 ( -. \stemUp fis16 ) -. \stemUp fis8
    ( -. \stemUp fis8 -. | % 106
    \stemUp fis8 ) -. _\markup{ \italic {poco cresc.} } \stemUp fis16 (
    -. \stemUp fis16 ) -. \stemUp fis8 ( -. \stemUp fis8 -. \stemUp fis8
    ) -. \stemUp fis16 ( -. \stemUp fis16 ) -. \stemUp fis8 ( -. \stemUp
    fis8 -. | % 107
    \stemUp e8 ) -. _\mf \stemUp e16 ( -. \stemUp e16 ) -. \stemUp e8 (
    -. \stemUp e8 -. \stemUp e8 ) -. \stemUp e16 ( -. \stemUp e16 ) -.
    \stemUp e8 ( -. \stemUp e8 -. \break | % 108
    \stemUp e8 ) -. r8 \stemUp e16 ( _\p _\< \stemUp fis16 \stemUp gis16
    \stemUp a16 ) \once \omit TupletBracket
    \times 4/7  {
        \stemDown a16*161/160 ( \stemDown b16*161/160 \stemDown c16*161/160
        \stemDown d16*161/160 \stemDown e16*161/160 \stemDown fis16*161/160
        \stemDown gis16*161/160 ) }
    \once \omit TupletBracket
    \times 4/7  {
        \stemDown a16*161/160 ( \stemDown b16*161/160 \stemDown cis16*161/160
        \stemDown d16*161/160 \stemDown e16*161/160 \stemDown fis16*161/160
        \stemDown gis16*161/160 ) }
    | % 109
    \stemDown a8 _\! _\mf r8 r4 \stemUp a,,,8 -. _\p ^\markup{ \italic
        {saltando} } \stemUp a16 ( -. \stemUp a16 ) -. \stemUp a8 ( -.
    \stemUp a8 -. | \barNumberCheck #110
    \stemUp a8 ) -. \stemUp a16 ( -. \stemUp a16 ) -. \stemUp a8 ( -.
    \stemUp a8 -. \stemUp a8 ) -. \stemUp a16 ( -. \stemUp a16 ) -.
    \stemUp a8 ( -. \stemUp a8 -. | % 111
    \stemUp b8 ) -. \stemUp b16 ( -. \stemUp b16 ) -. \stemUp b8 ( -.
    \stemUp b8 -. \stemUp b8 ) -. \stemUp b16 ( -. \stemUp b16 ) -.
    \stemUp b8 ( -. \stemUp b8 -. \pageBreak | % 112
    \stemUp b8 ) -. _\< \stemUp b16 ( -. \stemUp b16 ) -. \stemUp b8 (
    -. \stemUp b8 -. \stemUp b8 ) -. \stemUp b16 ( -. \stemUp b16 ) -.
    \stemUp b8 ( -. \stemUp b8 -. | % 113
    \stemUp b8 ) -. _\! _\markup{ \italic {poco più} } _ "" \stemUp b16
    ( -. \stemUp b16 ) -. \stemUp b8 ( -. \stemUp b8 -. \stemUp b8 ) -.
    \stemUp b16 ( -. \stemUp b16 ) -. \stemUp cis8 ( -. \stemUp cis8 -.
    | % 114
    \stemUp fis8 ) -. r8 r4 r2 | % 115
    R1 \break | % 116
    r4 \stemUp b,16 ( _\p _\< \stemUp cis16 \stemUp dis16 \stemUp e16 )
    \once \omit TupletBracket
    \times 4/5  {
        \stemUp e16 ( \stemUp fis16 \stemUp g16 \stemUp a16 \stemUp b16
        ) }
    \stemDown cis32 ( \stemDown dis32 \stemDown e32 \stemDown fis32
    \once \omit TupletBracket
    \times 4/5  {
        \stemDown gis32 \stemDown a32 \stemDown b32 \stemDown cis32
        \stemDown dis32 ) }
    | % 117
    \stemDown e8 _\! _\mf r8 r8 \stemUp gis,,,8 ( -. _\p ^\markup{
        \italic {saltando} } \stemUp gis8 ) -. \stemUp gis16 ( -.
    \stemUp gis16 ) -. \stemUp e'8 ( -. \stemUp e8 -. | % 118
    \stemUp e8 ) -. \stemUp e16 ( -. \stemUp e16 ) -. \stemUp e8 ( -.
    \stemUp gis8 -. \stemUp gis8 ) -. \stemUp gis16 ( -. \stemUp gis16 )
    -. \stemUp gis8 ( -. \stemUp gis8 -. | % 119
    \stemUp g8 ) -. _\markup{ \italic {cresc.} } \stemUp g16 ( -.
    \stemUp g16 ) -. \stemUp g8 ( -. \stemUp g8 -. \stemUp g8 ) -.
    \stemUp g16 ( -. \stemUp g16 ) -. \stemUp e8 ( -. \stemUp e8 -.
    \pageBreak | \barNumberCheck #120
    \stemUp e8 ) -. \stemUp e16 ( -. \stemUp e16 ) -. \stemUp e8 ( -.
    \stemUp g8 -. \stemUp g8 ) -. \stemUp g16 ( -. \stemUp g16 ) -.
    \stemUp g8 ( -. \stemUp g8 -. | % 121
    \stemUp g8 ) -. _\mf \stemUp g16 -- \stemUp g16 -- \stemUp g8 --
    \stemUp g8 -- \stemUp g8 -- \stemUp g16 -- \stemUp g16 -- \stemUp g8
    -- \stemUp g8 -- | % 122
    \stemUp g8 ^\markup{ \italic {simile} } _\markup{ \italic {poco
            cresc.} } \stemUp g16 \stemUp g16 \stemUp g8 \stemUp g8
    \stemUp g8 \stemUp g16 \stemUp g16 \stemUp g8 \stemUp g8 | % 123
    \stemUp e8 \stemUp e16 \stemUp e16 \stemUp e8 \stemUp e8 \stemUp e8
    \stemUp e16 \stemUp e16 \stemUp e8 \stemUp e8 | % 124
    \stemUp d8 r8 r4 r2 \break | % 125
    R1 | % 126
    \stemUp g,8 _\ff \stemUp g'8 \stemUp g,16 \stemUp g'16 \stemUp g,16
    \stemUp g'16 \stemUp g,8 \stemUp g'8 \stemUp g,8 \stemUp g'8 \stemUp
    g,8 \stemUp g'8 \stemUp g,16 \stemUp g'16 \stemUp g,16 \stemUp g'16
    \stemUp g,8 \stemUp g'8 \stemUp g,8 \stemUp g'8 | % 127
    R1*3 ^\markup{ \italic {alzate sordini} } \bar "||"
    r2 ^\markup{ \italic {senza sordini} } r8 \stemDown fis''8 ( _\mf
    \stemDown e8 \stemDown d8 ) | % 131
    \stemDown b8 ( _\< \stemDown a8 \stemDown fis8 \stemDown a8 )
    \stemDown d4. ( _\! _\> \stemDown b8 ) \pageBreak | % 132
    \stemDown a2 ~ _\! \stemDown a8 \stemDown fis'8 ( \stemDown e8
    \stemDown d8 ) | % 133
    \stemDown a8 ( _\< \stemDown fis8 \stemDown d8 \stemDown fis8 )
    \stemDown b4. ( _\! _\> \stemDown a8 ) | % 134
    \stemDown a4 ~ _\! _\< \stemDown a32 \stemDown a32 ( \stemDown b32
    \stemDown cis32 \stemDown d32 \stemDown e32 \stemDown fis32
    \stemDown g32 ) \stemDown a4 -- _\! _\ff \stemDown g8 ( \stemDown
    fis8 ) | % 135
    \stemDown fis4 ( \stemDown e4 ) \stemDown g4 -- \stemDown fis8 (
    \stemDown e8 ) | % 136
    \stemDown e4 ( \stemDown d4 ) r8 \stemDown fis8 ( _\> \stemDown e8
    \stemDown d8 ) | % 137
    \stemDown a8 ( _\! _\mf _\< \stemDown fis8 \stemDown d8 \stemDown
    fis8 ) \stemDown b4. ( _\! _\f _\> \stemDown a8 ) \pageBreak | % 138
    \stemDown a4 ~ _\! _\< \stemDown a32 \stemDown a32 ( \stemDown b32
    \stemDown cis32 \stemDown d32 \stemDown e32 \stemDown fis32
    \stemDown g32 ) \stemDown a4 -- _\! _\ff \stemDown g8 ( \stemDown
    fis8 ) | % 139
    \stemDown fis4 ( \stemDown e4 ) \stemDown g4 -- \stemDown fis8 (
    \stemDown e8 ) | \barNumberCheck #140
    \stemDown e4 ( \stemDown d4 ) r8 \stemDown fis8 ( _\> \stemDown e8
    \stemDown d8 ) | % 141
    \stemDown a8 ( _\! _\mf _\< \stemDown fis8 \stemDown d8 \stemDown
    fis8 ) \stemDown b4. ( _\! _\f _\> \stemDown a8 ) \bar "||"
    \stemDown a2 _\! _\mf _\> \stemDown c4. ( _\! _\mp \stemDown fis8 )
    | % 143
    \stemDown b,2 \stemDown b4. ( \stemDown e8 ) | % 144
    \stemDown a,2 _\> \stemDown a4. ( _\! _\p \stemDown c8 ) \break | % 145
    \stemDown gis4. ( \stemDown b8 ) \stemDown g4. ( \stemDown bes8 ) | % 146
    \stemDown fis4. ( \stemDown a8 ) \stemDown c,4. ( \stemDown fis8 ) | % 147
    \stemDown b,2 \stemDown b4. ( \stemDown e8 ) | % 148
    \stemUp a,2 _\> \stemUp a4. ( _\! _\pp \stemDown c8 ) | % 149
    \stemUp gis4. ( \stemDown b8 ) \stemUp g4. ( \stemDown bes8 ) |
    \barNumberCheck #150
    \stemUp fis4. ( \stemUp a8 ) \stemUp f4. ( _\markup{ \italic {dim.}
        } \stemDown bes8 ) | % 151
    \stemUp fis4. ( \stemUp a8 ) \stemUp f4. ( \stemDown bes8 ) | % 152
    \stemUp fis4. ( _\ppp \stemUp a8 ) \stemUp fis4. ( \stemUp a8 ) | % 153
    \stemUp fis4. ( \stemUp a8 ) r2 | % 154
    \stemUp fis2 ^\markup{ \italic {divisi} } _\ppp _\< \stemUp eis2 _\!
    _\p _\> | % 155
    \stemUp fis2 ~ _\! _\ppp \stemUp fis8 r8 r4 \pageBreak | % 156
    \stemUp d2 _\ppp _\< \stemUp g2 _\! _\p _\> | % 157
    \stemUp fis2 ~ _\! \stemUp fis8 r8 r4 | % 158
    R1*3 \bar "||"
    \key c \major \stemDown g,8 _\ff \stemDown g'8 \stemDown es'8
    \stemDown es'8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp es,,16 -> _\sff \stemUp es16 \stemUp es16 }
    \stemUp es8 ~ \stemUp es4 ~ | % 162
    \stemUp es8 \stemUp e8 -> \stemUp f8 -> \stemUp e8 -> \stemUp es8 ->
    r8 r4 | % 163
    \stemUp d8 _\sf r8 \stemUp c8 _\sf r8 r4 r8 \stemUp c8 _\sf | % 164
    \stemUp d8 _\sf r8 \stemUp g,8 _\sf \stemUp es'8 r8 r4 \stemDown es'16
    ( _\ff \stemDown g16 ) \stemDown g16 ( \stemDown es'16 ) \pageBreak
    | % 165
    \stemDown e8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp e,,16 _\sff \stemUp e16 \stemUp e16 }
    \stemUp e8 ~ \stemUp e4 ~ | % 166
    \stemUp e8 \stemUp fis8 -> \stemUp g8 -> \stemUp fis8 -> \stemUp e8
    -> r8 r4 | % 167
    \stemUp es8 _\sf r8 \stemUp d8 _\sf r8 r4 r8 \stemUp d8 _\sf | % 168
    \stemUp dis8 _\sf r8 \stemUp g,8 _\sf \stemUp e'8 r8 r4 \stemDown e'16
    ( _\ff \stemDown g16 ) \stemDown g16 ( \stemDown e'16 ) | % 169
    \stemDown f8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown f16 _\sff \stemDown f16 \stemDown f16 }
    \stemDown f8 ~ \stemDown f4 ~ | \barNumberCheck #170
    \stemDown f8 \stemDown g8 -> \stemDown f8 -> \stemDown g8 ->
    \stemDown gis8 -> \stemDown a8 -> \stemUp d,,,8 ^\markup{ \italic
        {sul} } ^ "G" ^\markup{ \italic {feroce} } ^ "" _\ff \stemUp e8
    | % 171
    \stemUp f8 r8 \stemUp e8 r8 r4 \stemUp d16 \stemUp g16 \stemUp f16
    \stemUp d16 \pageBreak | % 172
    \stemUp f8 r8 \stemUp e8 r8 r4 \stemUp d16 \stemUp g16 \stemUp f16
    \stemUp d16 | % 173
    \stemUp e16 \stemUp a16 \stemUp g16 \stemUp e16 \stemUp f16 \stemUp
    bes16 \stemUp a16 \stemUp f16 \stemUp g16 \stemUp c16 \stemUp bes16
    \stemUp g16 \stemDown a16 \stemDown d16 \stemDown c16 \stemDown a16
    | % 174
    \stemDown bes16 \stemDown e16 \stemDown d16 \stemDown bes16
    \stemDown c16 \stemDown f16 \stemDown e16 \stemDown c16 \stemDown d16
    \stemDown g16 \stemDown f16 \stemDown d16 \stemDown e16 \stemDown
    fis16 \stemDown g16 \stemDown gis16 | % 175
    \stemDown a8 r8 r4 r2 | % 176
    R1*2 \pageBreak | % 178
    r2 r4 \stemUp e,8 ^\markup{ \italic {sul} } ^ "G" _ "" _\markup{
        \italic {come prima} } \stemUp fis8 | % 179
    \stemUp g8 r8 \stemUp fis8 r8 r4 \stemUp e16 \stemUp a16 \stemUp g16
    \stemUp e16 | \barNumberCheck #180
    \stemUp g8 r8 \stemUp fis8 r8 r4 \stemUp e16 \stemUp a16 \stemUp g16
    \stemUp e16 | % 181
    \stemUp fis16 \stemUp b16 \stemUp a16 \stemUp fis16 \stemUp g16
    \stemUp c16 \stemUp b16 \stemUp g16 \stemDown a16 \stemDown d16
    \stemDown c16 \stemDown a16 \stemDown b16 \stemDown e16 \stemDown d16
    \stemDown b16 | % 182
    \stemDown c16 \stemDown fis16 \stemDown e16 \stemDown c16 \stemDown
    d16 \stemDown g16 \stemDown fis16 \stemDown d16 \stemDown e16
    \stemDown a16 \stemDown g16 \stemDown e16 \stemDown fis16 \stemDown
    gis16 \stemDown a16 \stemDown ais16 \break | % 183
    \stemDown b8 r8 r16 \stemUp fis,16 _\markup{ \italic {sempre} } _
    "" \stemUp g16 \stemUp a16 \stemUp b16 \stemUp a16 \stemUp g16
    \stemUp fis16 \stemUp g8 r8 | % 184
    r4 r16 \stemUp fis16 \stemUp g16 \stemUp a16 \stemUp b16 \stemUp a16
    \stemUp g16 \stemUp fis16 \stemUp g8 \stemUp fis16 \stemUp g16 | % 185
    \stemUp a8 \stemUp g16 \stemUp a16 \stemUp b8 \stemUp a16 \stemUp b16
    \stemDown cis8 \stemDown b16 \stemDown cis16 \stemDown d8 r8 | % 186
    r2 r4 \stemUp e,8 _\ff \stemUp d16 \stemUp e16 | % 187
    \stemUp fis8 \stemUp e16 \stemUp fis16 \stemUp g8 \stemUp fis16
    \stemUp g16 \stemUp a8 \stemUp g16 \stemUp a16 \stemDown b8 r8
    \pageBreak | % 188
    r2 r4 \stemDown bes'16 _\fff \stemDown f'16 \stemDown es16 \stemDown
    bes16 | % 189
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16 |
    \barNumberCheck #190
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16 | % 191
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16 \break
    | % 192
    \stemDown es16 \stemDown as16 \stemDown g16 \stemDown es16 \stemDown
    es16 \stemDown as16 \stemDown g16 \stemDown es16 \stemDown es16
    \stemDown as16 \stemDown g16 \stemDown es16 \stemDown es16 \stemDown
    as16 \stemDown g16 \stemDown es16 | % 193
    \stemDown es16 \stemDown as16 \stemDown g16 \stemDown es16 \stemDown
    es16 \stemDown as16 \stemDown g16 \stemDown es16 \stemDown es16
    \stemDown as16 \stemDown g16 \stemDown es16 \stemDown d16 \stemDown
    g16 \stemDown f16 \stemDown d16 | % 194
    \stemDown d16 \stemDown g16 \stemDown f16 \stemDown d16 \stemDown d16
    \stemDown g16 \stemDown f16 \stemDown d16 \stemDown d16 \stemDown g16
    \stemDown f16 \stemDown d16 \stemDown d16 \stemDown g16 \stemDown f16
    \stemDown d16 | % 195
    \stemDown f16 \stemDown bes16 \stemDown a16 \stemDown f16 \stemDown
    f16 \stemDown bes16 \stemDown a16 \stemDown f16 \stemDown f16
    \stemDown bes16 \stemDown a16 \stemDown f16 \stemDown f16 \stemDown
    bes16 \stemDown a16 \stemDown f16 \pageBreak | % 196
    \stemDown d16 \stemDown g16 \stemDown f16 \stemDown d16 \stemDown d16
    \stemDown g16 \stemDown f16 \stemDown d16 \stemDown a16 \stemDown e'16
    \stemDown d16 \stemDown a16 \stemDown a16 \stemDown e'16 \stemDown d16
    \stemDown a16 | % 197
    \stemDown f16 \stemDown bes16 \stemDown a16 \stemDown f16 \stemDown
    f16 \stemDown bes16 \stemDown a16 \stemDown f16 \stemDown d16
    \stemDown g16 \stemDown f16 \stemDown d16 \stemDown a16 \stemDown e'16
    \stemDown d16 \stemDown a16 | % 198
    \stemUp f16 \stemUp bes16 \stemUp a16 \stemUp f16 \stemUp d16
    \stemUp g16 \stemUp f16 \stemUp d16 r2 | % 199
    R1*2 \break | % 201
    R1*4 | % 205
    r4 \once \omit TupletBracket
    \times 4/7  {
        \stemDown a'16*161/160 ( _\p \stemDown bes16*161/160 \stemDown
        cis16*161/160 \stemDown d16*161/160 \stemDown e16*161/160
        \stemDown f16*161/160 \stemDown g16*161/160 }
    \stemDown a8 ) r8 r4 | % 206
    R1 \pageBreak | % 207
    r4 \stemDown as4 ( ~ -> _\p \stemDown as4 \stemDown g8 ) r8 | % 208
    R1 | % 209
    r4 \stemDown ces4 ( ~ -> _\markup{ \italic {più} } _ "" \stemDown
    ces4 \stemDown bes8 ) r8 | \barNumberCheck #210
    r4 r8 \stemDown d8 ( ~ _\mf \stemDown d8 \stemDown cis8 ~ \stemDown
    cis8 ) r8 | % 211
    r4 r8 \stemDown f8 ( ~ _\markup{ \italic {cresc.} } \stemDown f8
    \stemDown e8 ~ \stemDown e8 ) \stemDown g8 ( ~ | % 212
    \stemDown g8 \stemDown fis8 ~ \stemDown fis8 ) \stemDown a8 ( ~ _\f
    _\< \stemDown a8 \stemDown gis8 ~ \stemDown gis8 ) \stemDown a8 ( ~
    \pageBreak | % 213
    \stemDown a8 \stemDown gis8 ~ \stemDown gis8 ) \stemDown a8 ~
    \stemDown a8 \stemDown gis8 ~ \stemDown gis8 \stemDown b8 ~ _\! _\ff
    | % 214
    \stemDown b8 \stemDown a8 ~ \stemDown a8 \stemDown gis8 ~ \stemDown
    gis8 \stemDown fis8 ~ \stemDown fis8 \stemDown e8 ~ | % 215
    \stemDown e8 \stemDown d8 ~ \stemDown d8 \stemDown bis8 ~ \stemDown
    bis8 \stemDown cis8 ~ \stemDown cis8 \stemDown ais8 ( ~ | % 216
    \stemDown ais8 _\markup{ \italic {dim. un poco} } \stemDown b8 ~
    \stemDown b8 ) \stemDown gis8 ( ~ \stemDown gis8 \stemDown a8 ~
    \stemDown a8 ) \stemDown eis8 ( ~ \break | % 217
    \stemDown eis8 \stemDown fis8 ~ \stemDown fis8 ) \stemDown e8 ( ~
    \stemDown e8 \stemDown eis8 ~ \stemDown eis8 ) \stemDown b'8 ( ~ _\f
    | % 218
    \stemDown b8 \stemDown a8 ~ \stemDown a8 ) \stemDown gis8 ( ~
    \stemDown gis8 \stemDown fis8 ~ \stemDown fis8 ) \stemDown e8 ( ~ | % 219
    \stemDown e8 \stemDown d8 ~ \stemDown d8 ) \stemDown bis8 ( ~
    \stemDown bis8 \stemDown cis8 ~ \stemDown cis8 ) \stemDown ais8 ( ~
    | \barNumberCheck #220
    \stemUp ais8 _\markup{ \italic {dim.} } \stemUp b8 ~ \stemUp b8 )
    \stemUp gis8 ( ~ \stemUp gis8 \stemUp a8 ~ \stemUp a8 ) \stemUp eis8
    ( ~ \pageBreak | % 221
    \stemUp eis8 \stemUp fis8 ~ \stemUp fis8 ) \stemUp e8 ( ~ \stemUp e8
    \stemUp eis8 ~ \stemUp eis8 ) \stemUp e8 ( ~ | % 222
    \stemUp e8 \stemUp eis8 ~ \stemUp eis8 ) \stemUp e8 ( ~ \stemUp e8
    \stemUp eis8 ~ \stemUp eis8 ) \stemUp e8 ( ~ _\p | % 223
    \stemUp e8 \stemUp eis8 ~ \stemUp eis2 ~ \stemUp eis8 ) \stemUp e8 (
    ~ | % 224
    \stemUp e8 \stemUp eis8 ~ \stemUp eis2 ~ \stemUp eis8 ) \stemUp e8 (
    ~ | % 225
    \stemUp e8 _\markup{ \italic {dim.} } \stemUp eis8 ~ \stemUp eis2 ~
    \stemUp eis8 ) \stemUp e8 ( ~ \break | % 226
    \stemUp e8 \stemUp eis8 ~ \stemUp eis2 ~ \stemUp eis8 ) \stemUp dis8
    ( ~ _\pp | % 227
    \stemUp dis8 \stemUp e8 ~ \stemUp e8 \stemUp dis8 ~ \stemUp dis8
    \stemUp e8 ~ \stemUp e8 \stemUp dis8 ~ | % 228
    \stemUp dis8 \stemUp e8 ~ \stemUp e8 _\> \stemUp dis8 ~ \stemUp dis8
    \stemUp e8 ~ \stemUp e8 \stemUp f8 ~ | % 229
    \stemUp f8 ) _\! r8 r4 r2 | \barNumberCheck #230
    r2 r4 \stemUp e8 ( -. _\pp _\< \stemUp f8 ) -. \break | % 231
    \stemUp ges4 ( _\! _\> \stemUp f8 ) r8 _\! r2 | % 232
    r2 r4 \stemUp e8 ( -. _\pp _\< \stemUp f8 ) -. | % 233
    \stemUp ges4 ( _\! _\> \stemUp f8 ) r8 _\! r2 | % 234
    r2 r4 \stemUp e8 ( -. _\pp _\< \stemUp f8 ) -. | % 235
    \stemUp ges4 ( _\! _\> \stemUp f8 ) r8 _\! r4 \stemUp e16 ( _\<
    \stemUp f16 \stemUp ges16 \stemUp e16 ) | % 236
    \stemUp ges4 ( _\! _\> \stemUp f8 ) r8 _\! r4 \stemUp a8 ( -. _\<
    \stemUp bes8 ) -. \pageBreak | % 237
    \stemDown ces4 ( _\! _\> \stemDown bes8 ) r8 _\! r4 \stemDown a16 (
    _\< \stemDown bes16 \stemDown ces16 \stemDown a16 ) | % 238
    \stemDown ces4 ( _\! _\> \stemDown bes8 ) r8 _\! r4 \stemUp a8 ( -.
    _\mp \stemUp bes8 ) -. | % 239
    \stemDown des8 ( -> _\markup{ \italic {cresc.} } \stemDown c8 )
    \stemDown b16 ( \stemDown c16 \stemDown des16 \stemDown b16 )
    \stemDown des8 ( -> \stemDown c8 ) \stemDown b8 ( -. \stemDown c8 )
    -. | \barNumberCheck #240
    \stemDown es8 ( -> \stemDown des8 ) \stemDown c16 ( \stemDown des16
    \stemDown es16 \stemDown des16 ) \stemDown f8 ( -> \stemDown es8 )
    \stemDown d16 ( \stemDown es16 \stemDown f16 \stemDown es16 ) | % 241
    \stemDown ges8 ( _\< \stemDown f8 ) \stemDown e16 ( \stemDown f16
    \stemDown ges16 \stemDown e16 ) \stemDown ges8 ( \stemDown f8 )
    \stemDown e16 ( \stemDown f16 \stemDown ges16 \stemDown f16 )
    \pageBreak | % 242
    \stemDown as16 ( _\! _ "" _\markup{ \italic {cresc.} } \stemDown
    ges16 ) \stemDown ges16 -. \stemDown ges16 -. \stemDown bes16 (
    \stemDown as16 ) \stemDown as16 -. \stemDown as16 -. \stemDown ces16
    ( \stemDown bes16 ) \stemDown bes16 -. \stemDown bes16 -. \stemDown
    a16 ( \stemDown ais16 \stemDown b16 \stemDown ais16 ) | % 243
    \stemDown cis16 ( _\ff \stemDown b16 ) \stemDown b16 -. \stemDown b16
    -. \stemDown ais16 ( \stemDown b16 \stemDown cis16 \stemDown b16 )
    \stemDown d16 ( \stemDown cis16 ) \stemDown cis16 -. \stemDown cis16
    -. \stemDown bis16 ( \stemDown cis16 \stemDown d16 \stemDown cis16 )
    | % 244
    \stemDown e16 ( \stemDown d16 ) \stemDown d16 -. \stemDown d16 -.
    \stemDown fis16 ( \stemDown e16 ) \stemDown e16 -. \stemDown e16 -.
    \stemDown g16 ( \stemDown fis16 ) \stemDown fis16 -. \stemDown fis16
    -. r4 | % 245
    r4 r16 \stemDown fis16 ( _\fff \stemDown eis16 \stemDown fis16 )
    \stemDown g16 ( \stemDown fis16 ) \stemDown fis16 -. \stemDown fis16
    -. r4 \pageBreak | % 246
    r4 r16 \stemDown fis16 ( \stemDown eis16 \stemDown fis16 ) \stemDown
    g16 ( \stemDown fis16 ) \stemDown fis16 -. \stemDown fis16 -.
    \stemDown fis16 ( \stemDown e16 ) \stemDown e16 -. \stemDown e16 -.
    | % 247
    \stemDown g16 ( \stemDown fis16 ) \stemDown fis16 -. \stemDown fis16
    -. \stemDown b,16 ( \stemDown ais16 ) \stemDown ais16 -. \stemDown
    ais16 -. \stemDown cis16 ( \stemDown b16 ) \stemDown b16 -.
    \stemDown b16 -. \stemDown fis16 ( \stemDown e16 ) \stemDown e16 -.
    \stemDown e16 -. | % 248
    \stemDown g16 \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown
    cis16 \stemDown d16 \stemDown cis16 \stemDown b16 \stemUp ais8 r8
    \stemDown b8 _\f \stemDown cis8 | % 249
    \stemDown d4 ( _ "" \stemDown cis8 ) r8 r4 \stemDown b16 (
    \stemDown e16 ) \stemDown e16 ( \stemDown b16 ) | \barNumberCheck
    #250
    \stemDown d4 ( _ "" \stemDown cis8 ) r8 r4 \stemDown d8 \stemDown
    e8 | % 251
    \stemDown fis4 ( _ "" \stemDown e8 ) r8 r4 \stemDown d16 (
    \stemDown g16 ) \stemDown g16 ( \stemDown d16 ) \break | % 252
    \stemDown fis4 ( _ "" \stemDown e8 ) r8 r4 \stemDown fis8 _\ff
    \stemDown gis8 | % 253
    \stemDown a8 ( -> \stemDown gis8 ) r4 r4 \stemDown fis16 ( \stemDown
    gis16 ) \stemDown a16 ( \stemDown fis16 ) | % 254
    \stemDown a8 ( -> \stemDown gis8 ) r4 r4 \stemDown cis16 ( _\ff
    \stemDown b16 ) \stemDown b16 -. \stemDown b16 -. | % 255
    \stemDown d16 ( \stemDown cis16 ) \stemDown cis16 -. \stemDown cis16
    -. r4 r4 \stemDown fis16 ( \stemDown a,16 ) \stemDown a16 -.
    \stemDown a16 -. | % 256
    \stemDown a16 ( \stemDown gis16 ) \stemDown gis16 -. \stemDown gis16
    -. r4 r4 \stemDown b16 ( \stemDown a16 ) \stemDown a16 -. \stemDown
    a16 -. \pageBreak | % 257
    \stemDown cis16 ( \stemDown b16 ) \stemDown b16 -. \stemDown b16 -.
    r4 r4 \stemDown e16 ( \stemDown gis,16 ) \stemDown gis16 -.
    \stemDown gis16 -. | % 258
    \stemDown gis16 ( \stemDown fis16 ) \stemDown fis16 -. \stemDown fis16
    -. r4 r4 \stemUp fis,8 ( _\pp \stemUp gis8 | % 259
    \stemUp a8 \stemUp f8 ) \stemDown a8 ( _\markup{ \italic {cresc.
            molto} } \stemDown b8 \stemDown c8 \stemDown a8 ) \stemDown
    c8 ( \stemDown d8 | \barNumberCheck #260
    \stemDown es8 \stemDown c8 ) \stemDown es8 ( \stemDown f8 \stemDown
    ges8 \stemDown es8 ) \stemDown es8 ( \stemDown f8 | % 261
    \stemDown ges8 \stemDown es8 ) \stemDown fis8 ( \stemDown gis8 )
    \stemDown a8 ( \stemDown fis8 ) \stemDown a8 ( \stemDown b8 ) | % 262
    \stemDown c8 ( \stemDown a8 ) \stemDown c8 ( \stemDown d8 )
    \stemDown es8 ( \stemDown c8 ) \stemDown es8 -! _\ff \stemDown f8 -!
    \pageBreak | % 263
    \stemDown ges8 -! r8 \stemDown es8 -! r8 r4 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown es8 -! \stemDown f8 -! \stemDown ges8 -! }
    | % 264
    \stemDown ges8 -! r8 \stemDown es8 -! r8 r4 \stemDown fis8 -!
    \stemDown gis8 -! | % 265
    \stemDown a8 -! r8 \stemDown fis8 -! r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 -! \stemDown gis8 -! \stemDown a8 -! }
    | % 266
    \stemDown a8 -! r8 \stemDown fis8 -! r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 -! \stemDown gis8 -! \stemDown a8 -! }
    | % 267
    \stemDown a16 ( _\fff \stemDown gis16 \stemDown a16 \stemDown gis16
    \stemDown a16 \stemDown gis16 \stemDown a16 \stemDown gis16 )
    \stemDown a16 ( \stemDown gis16 \stemDown a16 \stemDown eis16 )
    \stemDown fis16 ( \stemDown eis16 \stemDown fis16 \stemDown d16 )
    \pageBreak | % 268
    \stemDown es16 ( \stemDown d16 \stemDown es16 \stemDown d16
    \stemDown es16 \stemDown d16 \stemDown es16 \stemDown d16 )
    \stemDown es16 ( \stemDown d16 \stemDown es16 \stemDown b16 )
    \stemDown c16 ( \stemDown b16 \stemDown c16 \stemDown gis16 ) | % 269
    \stemDown a16 ( \stemDown gis16 \stemDown a16 \stemDown gis16
    \stemDown a16 \stemDown gis16 \stemDown a16 \stemDown eis16 )
    \stemDown fis16 ( \stemDown eis16 \stemDown fis16 \stemDown eis16
    \stemDown fis16 \stemDown eis16 \stemDown fis16 \stemDown d16 |
    \barNumberCheck #270
    \stemDown es8 ) r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 _\fff \stemDown es8 \stemDown c8 \stemDown es8
        \stemDown c8 ~ }
    \stemDown es8*2/3 ~ \stemDown c8 \stemDown es8 \stemDown c8 ->
    \stemDown es8 r8 \stemDown es32 ( _\ff \stemDown f32 \stemDown fis32
    \stemDown gis32 ) | % 271
    \stemDown a16 ( \stemDown gis16 \stemDown a16 \stemDown gis16
    \stemDown a16 \stemDown gis16 \stemDown a16 \stemDown gis16 )
    \stemDown a16 ( \stemDown gis16 \stemDown a16 \stemDown eis16 )
    \stemDown fis16 ( \stemDown eis16 \stemDown fis16 \stemDown d16 ) | % 272
    \stemDown es16 ( \stemDown d16 \stemDown es16 \stemDown d16
    \stemDown es16 \stemDown d16 \stemDown es16 \stemDown d16 )
    \stemDown es16 ( \stemDown d16 \stemDown es16 \stemDown b16 )
    \stemUp c16 ( \stemUp b16 \stemUp c16 \stemUp gis16 ) \pageBreak | % 273
    \stemUp a16 ( \stemUp gis16 \stemUp a16 \stemUp gis16 \stemUp a16
    \stemUp gis16 \stemUp a16 \stemUp eis16 ) \stemUp fis16 ( \stemUp
    eis16 \stemUp fis16 \stemUp eis16 \stemUp fis16 \stemUp eis16
    \stemUp fis16 \stemUp d16 | % 274
    \stemUp es8 ) r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 _\ff \stemUp es8 \stemUp c8 \stemUp es8 \stemUp c8 ~
        }
    \stemUp es8*2/3 ~ \stemUp c8 \stemUp es8 \stemUp c8 -> \stemUp es8 r4
    | % 275
    r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp es8 \stemUp c8 \stemUp es8 \stemUp c8 }
    \stemUp es8*2/3 r4 r8 \stemUp c8 -> \stemUp es8 | % 276
    r4 \stemUp c8 -> \stemUp es8 r8 r2 | % 277
    bis1 ~ -> _\markup{ \italic {sempre} } _ "" | % 278
    bis1 | % 279
    gis'1 -> | \barNumberCheck #280
    \stemUp a4. ( -> \stemUp gis8 ) \stemUp gis2 | % 281
    \stemUp fis2 \stemUp eis2 ~ | % 282
    eis1 | % 283
    fis'1 -> | % 284
    \stemDown g4. ( -> \stemDown fis8 ) \stemDown fis4 \stemDown fis'4
    -- _\fff \pageBreak | % 285
    \stemDown e2 _\markup{ \italic {largamente, forte possibile} }
    \stemDown d2 ~ | % 286
    \stemDown d2. \stemDown d4 | % 287
    \stemDown cis2 \stemDown b2 ~ | % 288
    \stemDown b2. \stemDown a4 | % 289
    \stemDown g2 \stemDown fis2 ~ | \barNumberCheck #290
    \stemDown fis2. \stemDown e4 | % 291
    \stemDown d2 \stemDown cis2 ~ | % 292
    \stemDown cis2. \stemDown cis4 | % 293
    \stemDown b2 \stemUp ais2 ~ | % 294
    ais1 | % 295
    \stemUp g2 \stemUp fis2 ~ | % 296
    fis1 | % 297
    g,1 _ "" e'1 | % 298
    cis1 _ "" | % 299
    b1 ~ _\ffff _\> | \barNumberCheck #300
    \stemUp b2 ~ \stemUp b8 _\! _\p r8 r4 | % 301
    R1 \break | % 302
    R1*3 \bar "||"
    \pageBreak | % 305
    \key b \major r2 r8 \stemDown dis''8 ( _\p ^\markup{ \italic {con
            dolcezza} } \stemDown cis8 \stemDown b8 ) | % 306
    \stemDown gis8 ( _\< \stemDown fis8 \stemDown dis8 \stemDown fis8 )
    \stemDown b4. ( _\! _\> \stemDown gis8 ) | % 307
    \stemDown fis4 ~ _\! \stemDown fis8 r8 r8 \stemDown dis'8 (
    \stemDown cis8 \stemDown b8 ) | % 308
    \stemDown fis8 ( _\< \stemDown dis8 \stemDown b8 \stemDown dis8 )
    \stemDown gis4. ( _\! _\> \stemDown fis8 ) | % 309
    \stemDown fis2 _\! _\< \stemDown fis'4 -- _\! _\mf \stemDown e8. (
    \stemDown dis16 ) | \barNumberCheck #310
    \stemDown dis4 ( -> _\markup{ \italic {poco cresc.} } \stemDown cis4
    ) \stemDown e4 -- \stemDown dis8. ( \stemDown cis16 ) \pageBreak | % 311
    \stemDown cis4 ( -> \stemDown b4 ) r8 \stemDown dis8 ( _\mf _\>
    \stemDown cis8 \stemDown b8 ) | % 312
    \stemDown fis8 ( _\! _\p _\< \stemDown dis8 \stemDown b8 \stemDown
    dis8 ) \stemDown gis4.. ( _\! _\> \stemDown fis16 ) | % 313
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis16 -. _\! _\p _\< \stemDown fis16 ( \stemDown g16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown gis16 \stemDown a16 \stemDown ais16 ) }
    \stemDown b32 ( \stemDown bis32 \stemDown cis32 \stemDown d32
    \stemDown dis32 \stemDown e32 \stemDown eis32 \stemDown fis32 )
    \stemDown fis4 -- _\! _\fff \stemDown e8. ( \stemDown dis16 ) | % 314
    \stemDown dis4 ( -> \stemDown cis4 ) \stemDown e4 -- \stemDown dis8.
    ( \stemDown cis16 ) | % 315
    \stemDown cis4 ( -> \stemDown b4 ) r8 \stemDown dis8 ( _\> \stemDown
    cis8 ) \stemDown b8 -. | % 316
    \stemDown fis8 ( _\! _\mf _\< \stemDown dis8 \stemDown b8 \stemDown
    dis8 ) \stemDown gis4.. ( _\! _\ff _\> \stemDown fis16 ) \pageBreak
    | % 317
    \stemDown fis2 _\! _\mf \stemDown b4 ( \stemDown ais8. \stemDown a16
    ) | % 318
    \stemDown a4 ( -> \stemDown gis4 ) \stemDown ais4 ( \stemDown gis8.
    \stemDown g16 ) | % 319
    \stemDown g4 ( -> \stemDown fis4 ) \stemDown eis4 ( \stemDown e8.
    \stemDown eis16 ) | \barNumberCheck #320
    \stemDown fis2 r8 \stemUp b,8 ( \stemUp a8 \stemUp ais8 | % 321
    \stemUp b8 ) _\mf \stemUp b,8 ( \stemUp dis8 \stemUp fis8 )
    \stemDown b4 ( \stemUp ais8. \stemUp a16 ) | % 322
    \stemUp a4 ( -> \stemUp gis4 ) \stemUp ais4 ( \stemUp gis8. \stemUp
    g16 ) | % 323
    \stemUp g4 ( -> \stemUp fis4 ) \stemUp eis4 ( \stemUp e8. \stemUp
    eis16 ) | % 324
    \stemUp fis2 r8 \stemUp b,8 ( _\> \stemUp a8 \stemUp ais8 ) | % 325
    \stemUp b2 ~ _\! _\p _\> \stemUp b8 _\! _\pp r8 r4 \break | % 326
    R1*8 \pageBreak | % 334
    R1 \bar "||"
    r4 \stemDown b'8 _\p ^\markup{ \italic {pizz.} } r8 \stemUp ais8 r8
    \stemUp gis8 r8 | % 336
    \stemUp fis8 r8 \stemUp e8 r8 \stemUp dis8 r8 \stemUp cis8 r8 | % 337
    \stemUp b8 r8 \stemDown b'8 r8 \stemUp ais8 r8 \stemUp gis8 r8 | % 338
    \stemUp fis8 r8 \stemUp e8 r8 \stemUp dis8 r8 \stemUp cis8 r8 | % 339
    \stemUp b8 r8 \stemDown b'8 r8 \stemUp ais8 r8 \stemUp gis8 r8 |
    \barNumberCheck #340
    \stemUp fis8 r8 \stemUp e8 r8 \stemUp dis8 r8 \stemUp cis8 r8 | % 341
    \stemUp b8 r8 \stemDown b'8 r8 \stemUp ais8 r8 \stemUp gis8 r8 | % 342
    \stemUp fis8 r8 \stemUp e8 r8 \stemUp dis8 r8 \stemUp cis8 r8
    \pageBreak | % 343
    \stemUp b8 r8 \stemDown b'8 r8 \stemUp ais8 r8 \stemUp gis8 r8 | % 344
    \stemUp fis8 r8 \stemUp e8 r8 \stemUp dis8 r8 \stemUp cis8 r8 | % 345
    \stemUp b8 r8 \stemDown b'8 _\> r8 \stemUp ais8 r8 \stemUp gis8 r8 | % 346
    \stemUp fis8 _\! _\pp r8 \stemUp e8 r8 \stemUp dis8 r8 \stemUp cis8
    r8 | % 347
    \stemUp b8 r8 r4 r2 | % 348
    R1*7 \bar "|."
    }

PartPOneThreeVoiceTwo =  \relative c' {
    \clef "treble" \time 4/4 \key d \major s1*11 \break s1*7 \bar "||"
    s1*5 \pageBreak s1*6 | \barNumberCheck #30
    \time 2/4  s2 \break | % 31
    \time 4/4  s1*4 | % 35
    \stemDown c8 r8 \stemDown bes16 -. \stemDown bes16 -. \stemDown b16
    -. \stemDown b16 -. \stemDown c8 r8 s4 | % 36
    \stemDown dis8 r8 \stemDown cis16 -. \stemDown cis16 -. \stemDown
    cisis16 -. \stemDown cisis16 -. \stemDown dis8 r8 s4 \break | % 37
    \stemDown fis8 r8 \stemDown fis8 r8 \stemDown d8 r8 \stemDown d'8 r8
    | % 38
    \stemDown d8 -. \stemDown fis8 -. \stemDown b8 -. \stemDown d8 -.
    s2*11 \pageBreak s1*6 \break s1*4 \pageBreak s1*5 \break s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*4 \break s1*5
    \pageBreak s1*6 \bar "||"
    s1*5 \break s1*7 \bar "||"
    s1*2 \pageBreak s1*5 \break s1*4 \pageBreak s1*4 \break s1*4
    \pageBreak s1*5 \break s1*5 \bar "||"
    s1*2 \pageBreak s1*6 \pageBreak s1*4 \bar "||"
    s1*3 \break s1*9 | % 154
    \stemDown <a,, d>2 \stemDown <b d>2 | % 155
    \stemDown <a d>2 ~ ~ \stemDown <a d>8 s4. \pageBreak | % 156
    \stemDown a2 \stemDown cis2 | % 157
    \stemDown d2 ~ \stemDown d8 s8*27 \bar "||"
    \key c \major s1*4 \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*5
    \break s1*5 \pageBreak s1*4 \break s1*4 \pageBreak s1*5 \break s1*6
    \pageBreak s1*6 \pageBreak s1*4 \break s1*4 \pageBreak s1*5 \break
    s1*5 \break s1*6 \pageBreak s1*5 \pageBreak s1*4 \pageBreak s1*6
    \break s1*5 \pageBreak s1*6 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*12 \pageBreak s1*17 \break s1*3 \bar "||"
    \pageBreak | % 305
    \key b \major s1*6 \pageBreak s1*6 \pageBreak s1*9 \break s1*8
    \pageBreak s1 \bar "||"
    s1*8 \pageBreak s1*12 \bar "|."
    }

PartPOneFourVoiceOne =  \relative d''' {
    \clef "treble" \time 4/4 \key d \major | % 1
    R1*11 \break | % 12
    R1*7 \bar "||"
    R1*5 \pageBreak | % 24
    R1*6 | \barNumberCheck #30
    \time 2/4  R2 \break | % 31
    \time 4/4  R1*6 \break | % 37
    R1 | % 38
    r2 \stemDown <d fis>8 _\ff r8 r4 | % 39
    r2 \stemDown <cis, e>2 ~ ~ _\f | \barNumberCheck #40
    \stemDown <cis e>16 \stemDown <cis e>16 -. \stemDown <b d>16 -.
    \stemDown <a cis>16 -. \stemUp <g b>16 -. _\> \stemUp <fis a>16 -.
    \stemUp <e g>16 -. \stemUp <d fis>16 -. \stemUp <cis e>8 -. r8 _\! r4
    | % 41
    R1 | % 42
    r2 r8 ^\markup{ \italic {unis.} } \stemUp ais16 ( -. ^\markup{
        \italic {saltando} } _\pp \stemUp ais16 ) -. \stemUp b8 ( -.
    \stemUp ais8 -. | % 43
    \stemUp b8 ) -. \stemUp e16 ( -. \stemUp e16 ) -. \stemUp fis8 ( -.
    \stemUp cis8 -. \stemUp d8 ) -. \stemUp a16 ( -. \stemUp a16 ) -.
    \stemUp b8 ( -. \stemUp g8 ) -. \pageBreak | % 44
    r16 \stemUp gis16 ( \stemUp a16 \stemUp gis16 \stemUp a16 \stemUp
    gis16 \stemUp a16 \stemUp gis16 \stemUp a8 ) r8 r4 | % 45
    r2 r4 r8 \stemUp gis8 -. | % 46
    \stemUp a16 ( \stemUp gis16 \stemUp a16 \stemUp gis16 \stemUp a16
    \stemUp gis16 \stemUp a16 \stemUp gis16 ) \stemUp a8 -. \stemUp eis'16
    ( -. _\p \stemUp eis16 ) -. \stemUp fis8 ( -. \stemUp eis8 -. | % 47
    \stemUp fis8 ) -. \stemUp b16 ( -. \stemUp b16 ) -. \stemUp cis8 (
    -. \stemUp gis8 -. \stemUp a8 ) -. \stemUp e16 ( -. \stemUp e16 ) -.
    \stemUp fis8 ( -. \stemUp d8 ) -. | % 48
    r16 \stemUp dis16 ( \stemUp cis16 \stemUp dis16 \stemUp cis16
    \stemUp dis16 \stemUp cis16 \stemUp dis16 ) \stemUp cis8 -. \stemUp
    cis16 ( -. \stemUp cis16 ) -. \stemUp cis8 ( -. \stemUp cis8 ) -. | % 49
    \stemUp cis8 -. r8 \stemUp gis'8 -. r8 \stemUp e8 -. r8 \stemUp cis8
    ( -. \stemUp dis8 ) -. \break | \barNumberCheck #50
    \stemUp e16 ( \stemUp dis16 \stemUp e16 \stemUp dis16 \stemUp e16
    \stemUp dis16 \stemUp e16 \stemUp dis16 \stemDown e16 ) \stemDown
    gis'16 -. _\mp \stemDown gis16 -. \stemDown gis16 -. \stemDown gis16
    -. \stemDown gis16 -. \stemDown gis16 -. \stemDown gis16 -. | % 51
    \stemDown fis16 -. \stemDown fis16 -. \stemDown dis16 -. \stemDown
    dis16 -. \stemUp bis16 -. \stemUp bis16 -. \stemUp fis16 -. \stemUp
    fis16 -. \stemUp e8 -. r8 r4 | % 52
    r2 r16 \stemDown gis'16 -. _\mp \stemDown gis16 -. \stemDown gis16
    -. \stemDown gis16 -. \stemDown gis16 -. \stemDown gis16 -.
    \stemDown gis16 -. | % 53
    \stemDown fis16 -. \stemDown fis16 -. \stemDown dis16 -. \stemDown
    dis16 -. \stemUp bis16 -. \stemUp bis16 -. \stemUp fis16 -. \stemUp
    fis16 -. \stemUp e8 -. r8 r4 \pageBreak | % 54
    R1*4 | % 58
    r2 r16 \stemDown <gis dis'>16 -. _\mp \stemDown <gis dis'>16 -.
    \stemDown <gis dis'>16 -. \stemDown <gis dis'>16 -. \stemDown <gis
        dis'>16 -. \stemDown b16 -. \stemDown b16 -. \break | % 59
    \stemUp ais16 -. \stemUp ais16 -. \stemUp ais16 -. \stemUp ais16 -.
    \stemUp cis,16 -. \stemUp cis16 -. \stemUp cis16 -. \stemUp cis16 -.
    \stemUp b8 -. r8 r4 | \barNumberCheck #60
    r2 r16 \stemDown dis'16 -. _\mp \stemDown dis16 -. \stemDown dis16
    -. \stemDown dis16 -. \stemDown dis16 -. \stemDown dis16 -.
    \stemDown dis16 -. | % 61
    \stemUp ais16 -. \stemUp ais16 -. \stemUp ais16 -. \stemUp ais16 -.
    \stemUp cis,16 -. \stemUp cis16 -. \stemUp cis16 -. \stemUp cis16 -.
    \stemUp b8 -. r8 r4 | % 62
    R1*2 \pageBreak | % 64
    R1*3 | % 67
    r16 \stemUp gis16 -. _\f \stemUp gis16 -. \stemUp gis16 -. \stemUp
    gis16 ( \stemUp b16 ) \stemUp ais16 -. \stemUp gis16 -. \stemUp ais8
    -. r8 r4 | % 68
    R1 \pageBreak | % 69
    r16 \stemUp b16 -. _\ff \stemUp b16 -. \stemUp b16 -. \stemUp b16 (
    \stemUp d16 ) \stemUp cis16 -. \stemUp b16 -. \stemUp a8 -. r8 r4 |
    \barNumberCheck #70
    r2 r16 \stemDown a''16 _ "" _\markup{ \italic {détaché} }
    \stemDown a16 \stemDown a16 \stemDown a16 \stemDown c16 \stemDown b16
    \stemDown a16 | % 71
    \stemUp f16 ^\markup{ \italic {div.} } \stemUp e16 \stemUp d'16
    \stemUp c16 \stemUp b16 \stemUp a16 \stemUp f16 \stemUp e16 r16
    \stemUp a16 \stemUp a16 \stemUp a16 \stemUp a16 \stemUp c16 \stemUp
    b16 \stemUp a16 | % 72
    \stemUp f16 \stemUp e16 \stemUp d'16 \stemUp c16 \stemUp b16 \stemUp
    a16 \stemUp f16 \stemUp e16 r16 \stemUp a16 \stemUp a16 \stemUp a16
    \stemUp a16 \stemUp c16 \stemUp b16 \stemUp a16 | % 73
    r16 \stemUp a16 \stemUp a16 \stemUp a16 \stemUp a16 \stemUp c16
    \stemUp b16 \stemUp a16 r16 \stemUp a16 \stemUp a16 \stemUp a16
    \stemUp a16 \stemUp c16 \stemUp b16 \stemUp a16 \pageBreak | % 74
    r16 \stemUp a16 \stemUp a16 \stemUp a16 \stemUp a16 ( \stemUp c16
    \stemUp b16 ) \stemUp a16 -. r16 \stemUp a16 \stemUp a16 \stemUp a16
    \stemUp a16 ( \stemUp c16 \stemUp b16 ) \stemUp a16 -. | % 75
    r16 \stemDown a16 ^\markup{ \italic {unis.} } \stemDown a16
    \stemDown a16 \stemDown a16 ( \stemDown c16 \stemDown b16 )
    \stemDown a16 -. r16 \stemDown a16 \stemDown a16 \stemDown a16
    \stemDown a16 ( \stemDown cis16 \stemDown b16 ) \stemDown a16 -. | % 76
    r16 \stemDown a16 \stemDown a16 \stemDown a16 \stemDown a16 (
    \stemDown cis16 \stemDown b16 ) \stemDown a16 -. r16 \stemUp a,16
    _\f \stemUp a16 \stemUp a16 \stemUp a16 ( \stemUp cis16 \stemUp b16
    ) \stemUp a16 -. | % 77
    r16 \stemUp a16 \stemUp a16 \stemUp a16 \stemUp a16 ( \stemUp cis16
    \stemUp b16 ) \stemUp a16 -. r16 \stemUp a,16 _\mf \stemUp a16
    \stemUp a16 \stemUp a16 ( \stemUp cis16 \stemUp b16 ) \stemUp a16 -.
    \break | % 78
    r16 \stemUp a16 \stemUp a16 \stemUp a16 \stemUp a16 ( \stemUp cis16
    \stemUp b16 ) \stemUp a16 -. r16 \stemUp a16 _\mp \stemUp a16
    \stemUp a16 \stemUp a16 ( \stemUp cis16 \stemUp b16 ) \stemUp a16 -.
    | % 79
    \stemUp a16 -. \stemUp cis16 -. \stemUp b16 -. \stemUp a16 -.
    \stemUp a16 -. \stemUp cis16 -. \stemUp b16 -. \stemUp a16 -. r2 |
    \barNumberCheck #80
    R1*3 \pageBreak | % 83
    R1*6 \bar "||"
    R1*5 \break | % 94
    R1*2 | % 96
    r2 \stemUp dis4 ( -> _\mf ^\markup{ \italic {con sordini} } _\>
    \stemUp e4 | % 97
    \stemUp fis8 ) _\! _\p r8 r4 r2 | % 98
    R1*2 | \barNumberCheck #100
    r2 \stemUp dis4 ( -> _\mf _\> \stemUp e4 \bar "||"
    \stemUp fis8 ) _\! _\p \stemUp d16 ( -. ^\markup{ \italic {saltando}
        } \stemUp d16 ) -. \stemUp d8 ( -. \stemUp d8 -. \stemUp d8 ) -.
    \stemUp d16 ( -. \stemUp d16 ) -. \stemUp d8 ( -. \stemUp d8 -. | % 102
    \stemUp d8 ) -. \stemUp d16 ( -. \stemUp d16 ) -. \stemUp d8 ( -.
    \stemUp d8 -. \stemUp d8 ) -. \stemUp d16 ( -. \stemUp d16 ) -.
    \stemUp d8 ( -. \stemUp d8 -. \pageBreak | % 103
    \stemUp e8 ) -. \stemUp e16 ( -. \stemUp e16 ) -. \stemUp e8 ( -.
    \stemUp e8 -. \stemUp e8 ) -. \stemUp e16 ( -. \stemUp e16 ) -.
    \stemUp e8 ( -. \stemUp e8 -. | % 104
    \stemUp e8 ) -. _\< \stemUp e16 ( -. \stemUp e16 ) -. \stemUp e8 (
    -. \stemUp e8 -. \stemUp e8 ) -. \stemUp e16 ( -. \stemUp e16 ) -.
    \stemUp e8 ( -. \stemUp e8 -. | % 105
    \stemUp e8 ) -. _\! _\markup{ \italic {poco più} } _ "" \stemUp e16
    ( -. \stemUp e16 ) -. \stemUp e8 ( -. \stemUp e8 -. \stemUp e8 ) -.
    \stemUp e16 ( -. \stemUp e16 ) -. \stemUp cis8 ( -. \stemUp cis8 -.
    | % 106
    \stemUp b8 ) -. _\markup{ \italic {poco cresc.} } \stemUp b16 ( -.
    \stemUp b16 ) -. \stemUp b8 ( -. \stemUp b8 -. \stemUp b8 ) -.
    \stemUp b16 ( -. \stemUp b16 ) -. \stemUp b8 ( -. \stemUp b8 -. | % 107
    \stemUp d8 ) -. _\mf \stemUp d16 ( -. \stemUp d16 ) -. \stemUp d8 (
    -. \stemUp d8 -. \stemUp d8 ) -. \stemUp d16 ( -. \stemUp d16 ) -.
    \stemUp d8 ( -. \stemUp d8 -. \break | % 108
    \stemUp cis8 ) -. \stemUp cis16 ( -. _\markup{ \italic {dim.} }
    \stemUp cis16 ) -. \stemUp cis8 ( -. \stemUp cis8 -. \stemUp a8 ) -.
    \stemUp a16 ( -. \stemUp a16 ) -. \stemUp a8 ( -. \stemUp a8 -. | % 109
    \stemUp cis8 ) -. _\p \stemUp cis16 ( -. \stemUp cis16 ) -. \stemUp
    cis8 ( -. \stemUp cis8 -. \stemUp cis8 ) -. \stemUp cis16 ( -.
    \stemUp cis16 ) -. \stemUp cis8 ( -. \stemUp cis8 -. |
    \barNumberCheck #110
    \stemUp cis8 ) -. \stemUp cis16 ( -. \stemUp cis16 ) -. \stemUp cis8
    ( -. \stemUp cis8 -. \stemUp cis8 ) -. \stemUp cis16 ( -. \stemUp
    cis16 ) -. \stemUp cis8 ( -. \stemUp cis8 -. | % 111
    \stemUp d8 ) -. \stemUp d16 ( -. \stemUp d16 ) -. \stemUp d8 ( -.
    \stemUp d8 -. \stemUp d8 ) -. \stemUp d16 ( -. \stemUp d16 ) -.
    \stemUp d8 ( -. \stemUp d8 -. \pageBreak | % 112
    \stemUp e8 ) -. _\< \stemUp e16 ( -. \stemUp e16 ) -. \stemUp e8 (
    -. \stemUp e8 -. \stemUp e8 ) -. \stemUp e16 ( -. \stemUp e16 ) -.
    \stemUp e8 ( -. \stemUp e8 -. | % 113
    \stemUp eis8 ) -. _\! _\markup{ \italic {poco più} } _ "" \stemUp
    eis16 ( -. \stemUp eis16 ) -. \stemUp eis8 ( -. \stemUp eis8 -.
    \stemUp cis8 ) -. \stemUp cis16 ( -. \stemUp cis16 ) -. \stemUp gis8
    ( -. \stemUp gis8 -. | % 114
    \stemUp cis8 ) -. _\markup{ \italic {poco cresc.} } \stemUp cis16 (
    -. \stemUp cis16 ) -. \stemUp cis8 ( -. \stemUp cis8 -. \stemUp cis8
    ) -. \stemUp cis16 ( -. \stemUp cis16 ) -. \stemUp cis8 ( -. \stemUp
    cis8 -. | % 115
    \stemUp b8 ) -. _\mf \stemUp b16 ( -. \stemUp b16 ) -. \stemUp b8 (
    -. \stemUp b8 -. \stemUp b8 ) -. \stemUp b16 ( -. \stemUp b16 ) -.
    \stemUp b8 ( -. \stemUp b8 -. \break | % 116
    \stemUp b8 ) -. _\markup{ \italic {dim.} } \stemUp b16 ( -. \stemUp
    b16 ) -. \stemUp b8 ( -. \stemUp b8 -. \stemUp b8 ) -. \stemUp b16 (
    -. \stemUp b16 ) -. \stemUp b8 ( -. \stemUp b8 -. | % 117
    \stemUp <gis e'>8 ) -. _\p \stemUp <gis e'>16 ( -. \stemUp <gis e'>16
    ) -. \stemUp <gis e'>8 ( -. \stemUp b8 -. \stemUp b8 ) -. \stemUp b16
    ( -. \stemUp b16 ) -. \stemUp b8 ( -. \stemUp b8 -. | % 118
    \stemUp b8 ) -. \stemUp b16 ( -. \stemUp b16 ) -. \stemUp b8 ( -.
    \stemUp b8 -. \stemUp b8 ) -. \stemUp b16 ( -. \stemUp b16 ) -.
    \stemUp e8 ( -. \stemUp e8 -. | % 119
    \stemUp e8 ) -. _\markup{ \italic {cresc.} } \stemUp e16 ( -.
    \stemUp e16 ) -. \stemUp e8 ( -. \stemUp b8 -. \stemUp b8 ) -.
    \stemUp b16 ( -. \stemUp b16 ) -. \stemUp b8 ( -. \stemUp b8 -.
    \pageBreak | \barNumberCheck #120
    \stemUp b8 ) -. \stemUp b16 ( -. \stemUp b16 ) -. \stemUp b8 ( -.
    \stemUp b8 -. \stemUp b8 ) -. \stemUp b16 ( -. \stemUp b16 ) -.
    \stemUp e8 ( -. \stemUp e8 -. | % 121
    \stemUp e8 ) -. _\mf \stemUp e16 -- \stemUp e16 -- \stemUp e8 --
    \stemUp b8 -- \stemUp b8 -- \stemUp b16 -- \stemUp b16 -- \stemUp b8
    -- \stemUp e8 -- | % 122
    \stemUp e8 ^\markup{ \italic {simile} } _\markup{ \italic {poco
            cresc.} } \stemUp e16 \stemUp e16 \stemUp e8 \stemUp e8
    \stemUp e8 \stemUp e16 \stemUp e16 \stemUp e8 \stemUp e8 | % 123
    \stemUp cis8 \stemUp cis16 \stemUp cis16 \stemUp cis8 \stemUp g8
    \stemUp g8 \stemUp g16 \stemUp g16 \stemUp g8 \stemUp cis8 | % 124
    \stemUp d8 _\f \stemUp d16 \stemUp d16 \stemUp d8 \stemUp d8 \stemUp
    d8 \stemUp d16 \stemUp d16 \stemUp d8 \stemUp d8 \break | % 125
    \stemUp d8 _\< \stemUp d16 \stemUp d16 \stemUp d8 \stemUp d8 \stemUp
    d8 \stemUp d16 \stemUp d16 \stemUp d8 \stemUp d8 | % 126
    \stemUp cis8 _\! _\ff \stemUp cis16 \stemUp cis16 \stemUp cis8
    \stemUp cis8 \stemUp cis8 \stemUp cis16 \stemUp cis16 \stemUp cis8
    \stemUp cis8 | % 127
    R1*3 ^\markup{ \italic {alzate sordini} } \bar "||"
    r2 ^\markup{ \italic {senza sordini} } r8 \stemDown fis'8 ( _\mf
    \stemDown e8 \stemDown d8 ) | % 131
    \stemUp b8 ( _\< \stemUp a8 \stemUp fis8 \stemUp a8 ) \stemDown d4.
    ( _\! _\> \stemDown b8 ) \pageBreak | % 132
    \stemUp a2 ~ _\! \stemDown a8 \stemDown fis'8 ( \stemDown e8
    \stemDown d8 ) | % 133
    \stemUp a8 ( _\< \stemUp fis8 \stemUp d8 \stemUp fis8 ) \stemDown b4.
    ( _\! _\> \stemUp a8 ) | % 134
    \stemUp a4 ~ _\! _\< \stemDown a32 \stemDown a32 ( \stemDown b32
    \stemDown cis32 \stemDown d32 \stemDown e32 \stemDown fis32
    \stemDown g32 ) \stemDown a4 -- _\! _\ff \stemDown g8 ( \stemDown
    fis8 ) | % 135
    \stemDown fis4 ( \stemDown e4 ) \stemDown g4 -- \stemDown fis8 (
    \stemDown e8 ) | % 136
    \stemDown e4 ( \stemDown d4 ) r8 \stemDown fis8 ( _\> \stemDown e8
    \stemDown d8 ) | % 137
    \stemUp a8 ( _\! _\mf _\< \stemUp fis8 \stemUp d8 \stemUp fis8 )
    \stemDown b4. ( _\! _\f _\> \stemUp a8 ) \pageBreak | % 138
    \stemUp a4 ~ _\! _\< \stemDown a32 \stemDown a32 ( \stemDown b32
    \stemDown cis32 \stemDown d32 \stemDown e32 \stemDown fis32
    \stemDown g32 ) \stemDown a4 -- _\! _\ff \stemDown g8 ( \stemDown
    fis8 ) | % 139
    \stemDown fis4 ( \stemDown e4 ) \stemDown g4 -- \stemDown fis8 (
    \stemDown e8 ) | \barNumberCheck #140
    \stemDown e4 ( \stemDown d4 ) r8 \stemDown fis8 ( _\> \stemDown e8
    \stemDown d8 ) | % 141
    \stemUp a8 ( _\! _\mf _\< \stemUp fis8 \stemUp d8 \stemUp fis8 )
    \stemDown b4. ( _\! _\f _\> \stemUp a8 ) \bar "||"
    \stemUp a2 _\! _\mf _\> \stemDown c4. ( _\! _\mp \stemDown fis8 ) | % 143
    \stemDown b,2 \stemDown b4. ( \stemDown e8 ) | % 144
    \stemUp a,2 _\> \stemUp a4. ( _\! _\p \stemDown c8 ) \break | % 145
    \stemUp gis4. ( \stemDown b8 ) \stemUp g4. ( \stemDown bes8 ) | % 146
    \stemUp fis4. ( \stemUp a8 ) r2 | % 147
    R1*9 \pageBreak | % 156
    R1*5 \bar "||"
    \key c \major \stemDown <a a'>8 _\ff r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp a,16 -> _\sff \stemUp a16 \stemUp a16 }
    \stemUp a8 ~ \stemUp a4 ~ | % 162
    \stemUp a8 \stemUp bes8 -> \stemUp a8 -> \stemUp bes8 -> \stemUp a8
    -> r8 r4 | % 163
    \stemUp a8 _\sf r8 \stemUp as8 _\sf r8 r4 r8 \stemUp as8 _\sf | % 164
    \stemUp a8 _\sf r8 \stemUp <g es'>8 _\sf r8 r4 \stemDown g'16 ( _\ff
    \stemDown es'16 ) \stemDown es16 ( \stemDown g16 ) \pageBreak | % 165
    \stemDown g8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g,, e'>16 _\sff \stemUp <g e'>16 \stemUp <g e'>16 }
    \stemUp <g e'>8 ~ ~ \stemUp <g e'>4 ~ ~ | % 166
    \stemUp <g e'>8 \stemUp dis'8 -> \stemUp d8 -> \stemUp dis8 ->
    \stemUp <g, e'>8 -> r8 r4 | % 167
    \stemUp a8 _\sf r8 \stemUp <g d'>8 _\sf r8 r4 r8 \stemUp <g d'>8
    _\sf | % 168
    \stemUp a8 _\sf r8 \stemUp <g e'>8 _\sf r8 r4 \stemDown g'16 ( _\ff
    \stemDown e'16 ) \stemDown e16 ( \stemDown g16 ) | % 169
    \stemDown d'8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <d, d'>16 _\sff \stemDown <d d'>16 \stemDown <d d'>16
        }
    \stemDown <d d'>8 ~ ~ \stemDown <d d'>4 ~ ~ | \barNumberCheck #170
    \stemDown <d d'>8 \stemDown <d d'>8 -> \stemDown <d d'>8 ->
    \stemDown <d d'>8 -> \stemDown <d d'>8 -> \stemDown <d d'>8 -> r4 | % 171
    R1 \pageBreak | % 172
    R1*3 | % 175
    r16 \stemUp a,16 _\ff ^\markup{ \italic {feroce} } \stemUp b16
    \stemUp c16 \stemUp d16 \stemUp e16 \stemUp f16 \stemUp g16 \stemUp
    a16 \stemUp g16 \stemUp f16 \stemUp e16 \stemUp f8 r8 | % 176
    r16 \stemUp a,16 \stemUp b16 \stemUp c16 \stemUp d16 \stemUp e16
    \stemUp f16 \stemUp g16 \stemUp a16 \stemUp g16 \stemUp f16 \stemUp
    e16 \stemUp f8 \stemUp e16 \stemUp f16 | % 177
    \stemUp g8 \stemUp f16 \stemUp g16 \stemUp a8 \stemUp g16 \stemUp a16
    \stemUp b8 \stemUp a16 \stemUp b16 \stemDown c8 \stemDown b16
    \stemDown c16 \pageBreak | % 178
    \stemDown d8 \stemDown cis16 \stemDown d16 \stemDown e8 \stemDown
    dis16 \stemDown e16 \stemDown f8 \stemDown e16 \stemDown f16
    \stemDown g8 \stemDown fis8 | % 179
    \stemDown e8 r8 r4 r2 | \barNumberCheck #180
    R1*3 \break | % 183
    r16 \stemUp b,16 _\markup{ \italic {sempre} } _ "" \stemUp cis16
    \stemUp d16 \stemUp e16 \stemUp fis16 \stemUp g16 \stemUp a16
    \stemUp b16 \stemUp a16 \stemUp g16 \stemUp fis16 \stemUp g8 r8 | % 184
    r16 \stemUp b,16 \stemUp cis16 \stemUp d16 \stemUp e16 \stemUp fis16
    \stemUp g16 \stemUp a16 \stemUp b16 \stemUp a16 \stemUp g16 \stemUp
    fis16 \stemUp g8 \stemUp fis16 \stemUp g16 | % 185
    \stemUp a8 \stemUp g16 \stemUp a16 \stemUp b8 \stemUp a16 \stemUp b16
    \stemDown cis8 \stemDown b16 \stemDown cis16 \stemDown d8 r8 | % 186
    r2 r4 \stemUp e,8 _\ff \stemUp d16 \stemUp e16 | % 187
    \stemUp fis8 \stemUp e16 \stemUp fis16 \stemUp g8 \stemUp fis16
    \stemUp g16 \stemUp a8 \stemUp g16 \stemUp a16 \stemDown b8 r8
    \pageBreak | % 188
    r2 r4 \stemDown bes16 _\fff \stemDown f'16 \stemDown es16 \stemDown
    bes16 | % 189
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16 |
    \barNumberCheck #190
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16 | % 191
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16
    \stemDown bes16 \stemDown f'16 \stemDown es16 \stemDown bes16 \break
    | % 192
    \stemDown es16 \stemDown as16 \stemDown g16 \stemDown es16 \stemDown
    es16 \stemDown as16 \stemDown g16 \stemDown es16 \stemDown es16
    \stemDown as16 \stemDown g16 \stemDown es16 \stemDown es16 \stemDown
    as16 \stemDown g16 \stemDown es16 | % 193
    \stemDown es16 \stemDown as16 \stemDown g16 \stemDown es16 \stemDown
    es16 \stemDown as16 \stemDown g16 \stemDown es16 \stemDown es16
    \stemDown as16 \stemDown g16 \stemDown es16 \stemDown d16 \stemDown
    g16 \stemDown f16 \stemDown d16 | % 194
    \stemDown d16 \stemDown g16 \stemDown f16 \stemDown d16 \stemDown d16
    \stemDown g16 \stemDown f16 \stemDown d16 \stemDown d16 \stemDown g16
    \stemDown f16 \stemDown d16 \stemDown d16 \stemDown g16 \stemDown f16
    \stemDown d16 | % 195
    \stemDown f16 \stemDown bes16 \stemDown a16 \stemDown f16 \stemDown
    f16 \stemDown bes16 \stemDown a16 \stemDown f16 \stemDown f16
    \stemDown bes16 \stemDown a16 \stemDown f16 \stemDown f16 \stemDown
    bes16 \stemDown a16 \stemDown f16 \pageBreak | % 196
    \stemDown d16 \stemDown g16 \stemDown f16 \stemDown d16 \stemDown d16
    \stemDown g16 \stemDown f16 \stemDown d16 \stemDown a16 \stemDown e'16
    \stemDown d16 \stemDown a16 \stemDown a16 \stemDown e'16 \stemDown d16
    \stemDown a16 | % 197
    \stemUp f16 \stemUp bes16 \stemUp a16 \stemUp f16 \stemUp f16
    \stemUp bes16 \stemUp a16 \stemUp f16 \stemUp d16 \stemUp g16
    \stemUp f16 \stemUp d16 \stemDown a'16 \stemDown e'16 \stemDown d16
    \stemDown a16 | % 198
    \stemUp f16 \stemUp bes16 \stemUp a16 \stemUp f16 \stemUp d16
    \stemUp g16 \stemUp f16 \stemUp d16 r2 | % 199
    R1*2 \break | % 201
    R1*4 | % 205
    r4 \once \omit TupletBracket
    \times 4/7  {
        \stemUp e16*161/160 ( _\p \stemUp f16*161/160 \stemUp g16*161/160
        \stemUp a16*161/160 \stemUp bes16*161/160 \stemUp cis16*161/160
        \stemUp d16*161/160 }
    \stemDown e8 ) r8 r4 | % 206
    R1 \pageBreak | % 207
    r4 \stemUp as,4 ( ~ -> _\p \stemUp as4 \stemUp g8 ) r8 | % 208
    R1 | % 209
    r4 \stemDown ces4 ( ~ -> _\markup{ \italic {più} } _ "" \stemDown
    ces4 \stemDown bes8 ) r8 | \barNumberCheck #210
    r4 r8 \stemDown d8 ( ~ _\mf \stemDown d8 \stemDown cis8 ~ \stemDown
    cis8 ) r8 | % 211
    r4 r8 \stemDown f8 ( ~ _\markup{ \italic {cresc.} } \stemDown f8
    \stemDown e8 ~ \stemDown e8 ) \stemDown g8 ( ~ | % 212
    \stemDown g8 \stemDown fis8 ~ \stemDown fis8 ) \stemDown a8 ( ~ _\f
    _\< \stemDown a8 \stemDown gis8 ~ \stemDown gis8 ) \stemDown a8 ( ~
    \pageBreak | % 213
    \stemDown a8 \stemDown gis8 ~ \stemDown gis8 ) \stemDown a8 ~
    \stemDown a8 \stemDown gis8 ~ \stemDown gis8 \stemDown b8 ~ _\! _\ff
    | % 214
    \stemDown b8 \stemDown a8 ~ \stemDown a8 \stemDown gis8 ~ \stemDown
    gis8 \stemDown fis8 ~ \stemDown fis8 \stemDown e8 ~ | % 215
    \stemDown e8 \stemDown d8 ~ \stemDown d8 \stemDown bis8 ~ \stemDown
    bis8 \stemDown cis8 ~ \stemDown cis8 \stemDown ais8 ( ~ | % 216
    \stemUp ais8 _\markup{ \italic {dim. un poco} } \stemUp b8 ~ \stemUp
    b8 ) \stemUp gis8 ( ~ \stemUp gis8 \stemUp a8 ~ \stemUp a8 ) \stemUp
    eis8 ( ~ \break | % 217
    \stemUp eis8 \stemUp fis8 ~ \stemUp fis8 ) \stemUp e8 ( ~ \stemUp e8
    \stemUp eis8 ~ \stemUp eis8 ) \stemUp b'8 ( ~ _\f | % 218
    \stemUp b8 \stemUp a8 ~ \stemUp a8 ) \stemUp gis8 ( ~ \stemUp gis8
    \stemUp fis8 ~ \stemUp fis8 ) \stemUp e8 ( ~ | % 219
    \stemUp e8 \stemUp d8 ~ \stemUp d8 ) \stemUp bis8 ( ~ \stemUp bis8
    \stemUp cis8 ~ \stemUp cis8 ) \stemUp ais8 ( ~ | \barNumberCheck
    #220
    \stemUp ais8 _\markup{ \italic {dim.} } \stemUp b8 ~ \stemUp b8 )
    \stemUp gis8 ( ~ \stemUp gis8 \stemUp a8 ~ \stemUp a8 ) r8
    \pageBreak | % 221
    R1*5 \break | % 226
    R1*5 \break | % 231
    R1*5 | % 236
    r2 r4 \stemUp a8 ( -. _\< \stemUp bes8 ) -. \pageBreak | % 237
    \stemUp ces4 ( _\! _\> \stemUp bes8 ) r8 _\! r4 \stemUp a16 ( _\<
    \stemUp bes16 \stemUp ces16 \stemUp a16 ) | % 238
    \stemUp ces4 ( _\! _\> \stemUp bes8 ) r8 _\! r4 \stemUp a8 ( -. _\mp
    \stemUp bes8 ) -. | % 239
    \stemUp des8 ( -> _\markup{ \italic {cresc.} } \stemUp c8 ) \stemUp
    b16 ( \stemUp c16 \stemUp des16 \stemUp b16 ) \stemUp des8 ( ->
    \stemUp c8 ) \stemUp b8 ( -. \stemUp c8 ) -. | \barNumberCheck #240
    \stemUp es8 ( -> \stemUp des8 ) \stemUp c16 ( \stemUp des16 \stemUp
    es16 \stemUp des16 ) \stemUp f8 ( -> \stemUp es8 ) \stemUp d16 (
    \stemUp es16 \stemUp f16 \stemUp es16 ) | % 241
    \stemUp ges8 ( _\< \stemUp f8 ) \stemUp e16 ( \stemUp f16 \stemUp
    ges16 \stemUp e16 ) \stemUp ges8 ( \stemUp f8 ) \stemUp e16 (
    \stemUp f16 \stemUp ges16 \stemUp f16 ) \pageBreak | % 242
    \stemUp as16 ( _\! _ "" _\markup{ \italic {cresc.} } \stemUp ges16
    ) \stemUp ges16 -. \stemUp ges16 -. \stemUp bes16 ( \stemUp as16 )
    \stemUp as16 -. \stemUp as16 -. \stemDown ces16 ( \stemDown bes16 )
    \stemDown bes16 -. \stemDown bes16 -. \stemUp a16 ( \stemUp ais16
    \stemUp b16 \stemUp ais16 ) | % 243
    \stemDown cis16 ( _\ff \stemDown b16 ) \stemDown b16 -. \stemDown b16
    -. \stemDown ais16 ( \stemDown b16 \stemDown cis16 \stemDown b16 )
    \stemDown d16 ( \stemDown cis16 ) \stemDown cis16 -. \stemDown cis16
    -. \stemDown bis16 ( \stemDown cis16 \stemDown d16 \stemDown cis16 )
    | % 244
    \stemDown e16 ( \stemDown d16 ) \stemDown d16 -. \stemDown d16 -.
    \stemDown fis16 ( \stemDown e16 ) \stemDown e16 -. \stemDown e16 -.
    \stemDown g16 ( \stemDown fis16 ) \stemDown fis16 -. \stemDown fis16
    -. r4 | % 245
    r4 r16 \stemDown fis16 ( _\fff \stemDown eis16 \stemDown fis16 )
    \stemDown g16 ( \stemDown fis16 ) \stemDown fis16 -. \stemDown fis16
    -. r4 \pageBreak | % 246
    r4 r16 \stemDown fis16 ( \stemDown eis16 \stemDown fis16 ) \stemDown
    g16 ( \stemDown fis16 ) \stemDown fis16 -. \stemDown fis16 -.
    \stemDown fis16 ( \stemDown e16 ) \stemDown e16 -. \stemDown e16 -.
    | % 247
    \stemDown g16 ( \stemDown fis16 ) \stemDown fis16 -. \stemDown fis16
    -. \stemUp b,16 ( \stemUp ais16 ) \stemUp ais16 -. \stemUp ais16 -.
    \stemDown cis16 ( \stemDown b16 ) \stemDown b16 -. \stemDown b16 -.
    \stemUp fis'16 ( ^\markup{ \italic {div.} } \stemUp e16 ) \stemUp e16
    -. \stemUp e16 -. | % 248
    \stemUp g16 \stemUp fis16 \stemUp e16 \stemUp d16 \stemUp cis16
    \stemUp d16 \stemUp cis16 \stemUp b16 \stemUp ais16 \stemUp g16
    \stemUp fis16 \stemUp eis16 \stemUp fis8 ^\markup{ \italic {unis.} }
    _\f \stemUp g8 | % 249
    \stemUp gis4 ( _ "" \stemUp ais8 ) r8 r4 \stemUp fis8 \stemUp g8 |
    \barNumberCheck #250
    \stemUp gis4 ( _ "" \stemUp ais8 ) r8 r4 \stemUp a8 \stemUp bes8 | % 251
    \stemDown b4 ( _ "" \stemDown cis8 ) r8 r4 \stemUp a8 \stemUp bes8
    \break | % 252
    \stemDown b4 ( _ "" \stemDown cis8 ) r8 r4 \stemDown cis8 _\ff
    \stemDown d8 | % 253
    \stemDown dis8 ( -> \stemDown eis8 ) r4 r4 \stemDown cis8 \stemDown
    d8 | % 254
    \stemDown dis8 ( -> \stemDown eis8 ) r4 r4 \stemDown cis16 ( _\ff
    \stemDown b16 ) \stemDown b16 -. \stemDown b16 -. | % 255
    \stemDown d16 ( \stemDown cis16 ) \stemDown cis16 -. \stemDown cis16
    -. r4 r4 \stemDown fis16 ( \stemDown a,16 ) \stemDown a16 -.
    \stemDown a16 -. | % 256
    \stemUp a16 ( \stemUp gis16 ) \stemUp gis16 -. \stemUp gis16 -. r4 r4
    \stemUp b16 ( \stemUp a16 ) \stemUp a16 -. \stemUp a16 -. \pageBreak
    | % 257
    \stemDown cis16 ( \stemDown b16 ) \stemDown b16 -. \stemDown b16 -.
    r4 r4 \stemDown e16 ( \stemDown gis,16 ) \stemDown gis16 -.
    \stemDown gis16 -. | % 258
    \stemUp gis16 ( \stemUp fis16 ) \stemUp fis16 -. \stemUp fis16 -. r4
    r4 \stemUp fis4 ( _\pp | % 259
    \stemUp f4 ) \stemUp e4 ( _\markup{ \italic {cresc. molto} } \stemUp
    es4 ) \stemUp as4 ( | \barNumberCheck #260
    \stemUp g4 ) \stemDown c4 ( \stemDown ces4 ) \stemUp es,8 ( \stemUp
    f8 | % 261
    \stemUp ges8 \stemUp es8 ) \stemUp fis8 ( \stemUp gis8 ) \stemUp a8
    ( \stemUp fis8 ) \stemDown a8 ( \stemDown b8 ) | % 262
    \stemDown c8 ( \stemDown a8 ) \stemDown c8 ( \stemDown d8 )
    \stemDown es8 ( \stemDown c8 ) \stemDown es8 -! _\ff \stemDown f8 -!
    \pageBreak | % 263
    \stemDown ges8 -! r8 \stemDown es8 -! r8 r4 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown es8 -! \stemDown f8 -! \stemDown ges8 -! }
    | % 264
    \stemDown ges8 -! r8 \stemDown es8 -! r8 r4 \stemDown fis8 -!
    \stemDown gis8 -! | % 265
    \stemDown a8 -! r8 \stemDown fis8 -! r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 -! \stemDown gis8 -! \stemDown a8 -! }
    | % 266
    \stemDown a8 -! r8 \stemDown fis8 -! r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 -! \stemDown gis8 -! \stemDown a8 -! }
    | % 267
    \stemDown a16 ( _\fff \stemDown gis16 \stemDown a16 \stemDown gis16
    \stemDown a16 \stemDown gis16 \stemDown a16 \stemDown gis16 )
    \stemDown a16 ( \stemDown gis16 \stemDown a16 \stemDown eis16 )
    \stemDown fis16 ( \stemDown eis16 \stemDown fis16 \stemDown d16 )
    \pageBreak | % 268
    \stemDown es16 ( \stemDown d16 \stemDown es16 \stemDown d16
    \stemDown es16 \stemDown d16 \stemDown es16 \stemDown d16 )
    \stemDown es16 ( \stemDown d16 \stemDown es16 \stemDown b16 )
    \stemDown c16 ( \stemDown b16 \stemDown c16 \stemDown gis'16 ) | % 269
    \stemDown a16 ( \stemDown gis16 \stemDown a16 \stemDown gis16
    \stemDown a16 \stemDown gis16 \stemDown a16 \stemDown eis16 )
    \stemDown fis16 ( \stemDown eis16 \stemDown fis16 \stemDown eis16
    \stemDown fis16 \stemDown eis16 \stemDown fis16 \stemDown d16 |
    \barNumberCheck #270
    \stemDown es8 ) r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp es,8 _\fff \stemUp a8 \stemUp es8 \stemUp a8 \stemUp es8
        ~ }
    \stemUp a8*2/3 ~ \stemUp es8 \stemUp a8 \stemUp es8 -> \stemUp a8 r8
    \stemDown es'32 ( _\ff \stemDown f32 \stemDown fis32 \stemDown gis32
    ) | % 271
    \stemDown a16 ( \stemDown gis16 \stemDown a16 \stemDown gis16
    \stemDown a16 \stemDown gis16 \stemDown a16 \stemDown gis16 )
    \stemDown a16 ( \stemDown gis16 \stemDown a16 \stemDown eis16 )
    \stemDown fis16 ( \stemDown eis16 \stemDown fis16 \stemDown d16 ) | % 272
    \stemDown es16 ( \stemDown d16 \stemDown es16 \stemDown d16
    \stemDown es16 \stemDown d16 \stemDown es16 \stemDown d16 )
    \stemDown es16 ( \stemDown d16 \stemDown es16 \stemDown b16 )
    \stemUp c16 ( \stemUp b16 \stemUp c16 \stemUp gis16 ) \pageBreak | % 273
    \stemUp a16 ( \stemUp gis16 \stemUp a16 \stemUp gis16 \stemUp a16
    \stemUp gis16 \stemUp a16 \stemUp eis16 ) \stemUp fis16 ( \stemUp
    eis16 \stemUp fis16 \stemUp eis16 \stemUp fis16 \stemUp eis16
    \stemUp fis16 \stemUp d16 | % 274
    \stemUp es8 ) r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp a,8 _\ff \stemUp es'8 \stemUp a,8 \stemUp es'8 \stemUp
        a,8 ~ }
    \stemUp es'8*2/3 ~ \stemUp a,8 \stemUp es'8 \stemUp a,8 -> \stemUp
    es'8 r4 | % 275
    r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp a,8 \stemUp es'8 \stemUp a,8 \stemUp es'8 \stemUp a,8 }
    \stemUp es'8*2/3 r4 r8 \stemUp a,8 -> \stemUp es'8 | % 276
    r4 \stemUp a,8 -> \stemUp es'8 r8 r2 | % 277
    dis1 -> _\markup{ \italic {sempre} } _ "" | % 278
    \stemUp e4. ( -> \stemUp dis8 ) \stemUp dis2 ~ | % 279
    \stemUp dis2 \stemUp cis2 ~ | \barNumberCheck #280
    cis1 | % 281
    cis'1 -> | % 282
    \stemDown d4. ( -> \stemDown cis8 ) \stemDown cis2 | % 283
    \stemDown d2 \stemDown cis2 ~ | % 284
    \stemDown cis2. \stemDown fis4 -- _\fff \pageBreak | % 285
    \stemDown e2 _\markup{ \italic {largamente, forte possibile} }
    \stemDown d2 ~ | % 286
    \stemDown d2. \stemDown d4 | % 287
    \stemDown cis2 \stemDown b2 ~ | % 288
    \stemDown b2. \stemUp a4 | % 289
    \stemUp g2 \stemUp fis2 ~ | \barNumberCheck #290
    \stemUp fis2. \stemDown e'4 | % 291
    \stemDown d2 \stemDown cis2 ~ | % 292
    \stemDown cis2. \stemDown cis4 | % 293
    \stemDown b2 \stemUp ais2 ~ | % 294
    ais1 | % 295
    \stemUp g2 \stemUp fis2 ~ | % 296
    fis1 | % 297
    cis1 _ "" | % 298
    cis1 _ "" | % 299
    b1 ~ _\ffff _\> | \barNumberCheck #300
    \stemUp b2 ~ \stemUp b8 _\! _\p r8 r4 | % 301
    R1 \break | % 302
    R1*3 \bar "||"
    \pageBreak | % 305
    \key b \major r2 r8 \stemDown dis'8 ( _\p ^\markup{ \italic {con
            dolcezza} } \stemDown cis8 \stemDown b8 ) | % 306
    \stemUp gis8 ( _\< \stemUp fis8 \stemUp dis8 \stemUp fis8 )
    \stemDown b4. ( _\! _\> \stemUp gis8 ) | % 307
    \stemUp fis4 ~ _\! \stemUp fis8 r8 r8 \stemDown dis'8 ( \stemDown
    cis8 \stemDown b8 ) | % 308
    \stemUp fis8 ( _\< \stemUp dis8 \stemUp b8 \stemUp dis8 ) \stemUp
    gis4. ( _\! _\> \stemUp fis8 ) | % 309
    \stemUp fis2 _\! _\< \stemDown fis'4 -- _\! _\mf \stemDown e8. (
    \stemDown dis16 ) | \barNumberCheck #310
    \stemDown dis4 ( -> _\markup{ \italic {poco cresc.} } \stemDown cis4
    ) \stemDown e4 -- \stemDown dis8. ( \stemDown cis16 ) \pageBreak | % 311
    \stemDown cis4 ( -> \stemDown b4 ) r8 \stemDown dis8 ( _\mf _\>
    \stemDown cis8 \stemDown b8 ) | % 312
    \stemUp fis8 ( _\! _\p _\< \stemUp dis8 \stemUp b8 \stemUp dis8 )
    \stemUp gis4.. ( _\! _\> \stemUp fis16 ) | % 313
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis16 -. _\! _\p _\< \stemUp fis16 ( \stemUp g16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp gis16 \stemUp a16 \stemUp ais16 ) }
    \stemDown b32 ( \stemDown bis32 \stemDown cis32 \stemDown d32
    \stemDown dis32 \stemDown e32 \stemDown eis32 \stemDown fis32 )
    \stemDown fis4 -- _\! _\fff \stemDown e8. ( \stemDown dis16 ) | % 314
    \stemDown dis4 ( -> \stemDown cis4 ) \stemDown e4 -- \stemDown dis8.
    ( \stemDown cis16 ) | % 315
    \stemDown cis4 ( -> \stemDown b4 ) r8 \stemDown dis8 ( _\> \stemDown
    cis8 ) \stemDown b8 -. | % 316
    \stemUp fis8 ( _\! _\mf _\< \stemUp dis8 \stemUp b8 \stemUp dis8 )
    \stemUp gis4.. ( _\! _\ff _\> \stemUp fis16 ) \pageBreak | % 317
    \stemUp fis2 _\! _\mf \stemDown b4 ( \stemUp ais8. \stemUp a16 ) | % 318
    \stemUp a4 ( -> \stemUp gis4 ) \stemUp ais4 ( \stemUp gis8. \stemUp
    g16 ) | % 319
    \stemUp g4 ( -> \stemUp fis4 ) \stemUp eis4 ( \stemUp e8. \stemUp
    eis16 ) | \barNumberCheck #320
    \stemUp fis2 r8 \stemUp b8 ( ^\markup{ \italic {div.} } \stemUp a8
    \stemUp ais8 | % 321
    \stemUp b8 ) _\mf \stemUp b,8 ( \stemUp dis8 \stemUp fis8 ) \stemUp
    b4 ( \stemUp ais8. \stemUp a16 ) | % 322
    \stemUp a4 ( -> \stemUp gis4 ) \stemUp ais4 ( \stemUp gis8. \stemUp
    g16 ) | % 323
    \stemUp g4 ( -> \stemUp fis4 ) \stemUp g,2 ( | % 324
    \stemUp b8 ) r8 r4 r8 \stemUp b8 ( _\> \stemUp a8 \stemUp ais8 ) | % 325
    \stemUp b2 ~ _\! _\p _\> \stemUp b8 _\! _\pp r8 r4 \break | % 326
    R1*8 \pageBreak | % 334
    R1 \bar "||"
    r4 \stemDown b'8 _\p ^\markup{ \italic {pizz.} } r8 \stemUp ais8 r8
    \stemUp gis8 r8 | % 336
    \stemUp fis8 r8 \stemUp e8 r8 \stemUp dis8 r8 \stemUp cis8 r8 | % 337
    \stemUp b8 r8 \stemDown b'8 r8 \stemUp ais8 r8 \stemUp gis8 r8 | % 338
    \stemUp fis8 r8 \stemUp e8 r8 \stemUp dis8 r8 \stemUp cis8 r8 | % 339
    \stemUp b8 r8 \stemDown b'8 r8 \stemUp ais8 r8 \stemUp gis8 r8 |
    \barNumberCheck #340
    \stemUp fis8 r8 \stemUp e8 r8 \stemUp dis8 r8 \stemUp cis8 r8 | % 341
    \stemUp b8 r8 \stemDown b'8 r8 \stemUp ais8 r8 \stemUp gis8 r8 | % 342
    \stemUp fis8 r8 \stemUp e8 r8 \stemUp dis8 r8 \stemUp cis8 r8
    \pageBreak | % 343
    \stemUp b8 r8 \stemDown b'8 r8 \stemUp ais8 r8 \stemUp gis8 r8 | % 344
    \stemUp fis8 r8 \stemUp e8 r8 \stemUp dis8 r8 \stemUp cis8 r8 | % 345
    \stemUp b8 r8 \stemDown b'8 _\> r8 \stemUp ais8 r8 \stemUp gis8 r8 | % 346
    \stemUp fis8 _\! _\pp r8 \stemUp e8 r8 \stemUp dis8 r8 \stemUp cis8
    r8 | % 347
    \stemUp b8 r8 r4 r2 | % 348
    R1*7 \bar "|."
    }

PartPOneFourVoiceTwo =  \relative f'' {
    \clef "treble" \time 4/4 \key d \major s1*11 \break s1*7 \bar "||"
    s1*5 \pageBreak s1*6 | \barNumberCheck #30
    \time 2/4  s2 \break | % 31
    \time 4/4  s1*6 \break s1*7 \pageBreak s1*6 \break s1*4 \pageBreak
    s1*5 \break s1*5 \pageBreak s1*5 \pageBreak s1*2 | % 71
    \stemDown f16 \stemDown e16 \stemDown d16 \stemDown c16 \stemDown b16
    \stemDown a16 \stemDown f16 \stemDown e16 s16 \stemDown a'16
    \stemDown a16 \stemDown a16 \stemDown a16 \stemDown c16 \stemDown b16
    \stemDown a16 | % 72
    \stemDown f16 \stemDown e16 \stemDown d16 \stemDown c16 \stemDown b16
    \stemDown a16 \stemDown f16 \stemDown e16 s16 \stemDown a'16
    \stemDown a16 \stemDown a16 \stemDown a16 \stemDown c16 \stemDown b16
    \stemDown a16 s16 \stemDown a,16 \stemDown a16 \stemDown a16
    \stemDown a16 \stemDown c16 \stemDown b16 \stemDown a16 s16
    \stemDown a'16 \stemDown a16 \stemDown a16 \stemDown a16 \stemDown c16
    \stemDown b16 \stemDown a16 \pageBreak s16 \stemDown a,16 \stemDown
    a16 \stemDown a16 \stemDown a16 ( \stemDown c16 \stemDown b16 )
    \stemDown a16 -. s16 \stemDown a'16 \stemDown a16 \stemDown a16
    \stemDown a16 ( \stemDown c16 \stemDown b16 ) \stemDown a16 -. s1*3
    \break s1*5 \pageBreak s1*6 \bar "||"
    s1*5 \break s1*7 \bar "||"
    s1*2 \pageBreak s1*5 \break s1*4 \pageBreak s1*4 \break s1*4
    \pageBreak s1*5 \break s1*5 \bar "||"
    s1*2 \pageBreak s1*6 \pageBreak s1*4 \bar "||"
    s1*3 \break s1*11 \pageBreak s1*5 \bar "||"
    \key c \major s1*4 \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*5
    \break s1*5 \pageBreak s1*4 \break s1*4 \pageBreak s1*5 \break s1*6
    \pageBreak s1*6 \pageBreak s1*4 \break s1*4 \pageBreak s1*5 \break
    s1*5 \break s1*6 \pageBreak s1*5 \pageBreak s1*4 \pageBreak s4*7
    \stemDown fis,16 ( \stemDown e16 ) \stemDown e16 -. \stemDown e16 -.
    | % 248
    \stemDown g16 \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown
    cis16 \stemDown d16 \stemDown cis16 \stemDown b16 \stemDown ais16
    \stemDown g'16 \stemDown fis16 \stemDown eis16 s4*13 \break s1*5
    \pageBreak s1*6 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*12
    \pageBreak s1*17 \break s1*3 \bar "||"
    \pageBreak | % 305
    \key b \major s1*6 \pageBreak s1*6 \pageBreak s8*29 \stemDown b8 (
    \stemDown a8 \stemDown ais8 | % 321
    \stemDown b8 ) \stemDown b8 ( \stemDown dis8 \stemDown fis8 )
    \stemDown b,4 \stemDown ais8. ( \stemDown a16 ) | % 322
    \stemDown a4 ( -> \stemDown gis4 ) \stemDown ais4 ( \stemDown gis8.
    \stemDown g16 ) | % 323
    \stemDown g4 ( -> \stemDown fis'4 ) \stemDown g,2 ( | % 324
    \stemDown b8 ) s8*15 \break s1*8 \pageBreak s1 \bar "||"
    s1*8 \pageBreak s1*12 \bar "|."
    }

PartPOneFiveVoiceOne =  \relative e {
    \clef "alto" \time 4/4 \key d \major | % 1
    R1*3 _\markup{ \italic {div.} } | % 4
    r2 r4 _\mf _\< \stemUp e8 ( \stemUp fis8 ) | % 5
    \stemUp g2 ( _\! _\sf _\> \stemUp fis2 ~ | % 6
    \stemUp fis8 ) _\! _\p r8 r4 r2 | % 7
    R1*3 | \barNumberCheck #10
    r2 r4 _\mf _\< \stemUp d8 ( \stemUp e8 ) | % 11
    fis1 ~ _\! _\sf _\> \break | % 12
    \stemUp fis8 _\! _\p r8 r4 r2 | % 13
    \stemDown d''2 ( _\mf _\> \stemDown cis4 ~ \stemDown cis8 ) r8 _\! | % 14
    R1 | % 15
    \stemDown d,2 ( _\mf _\> \stemDown cis4 ) _\! _\p \stemUp b8. ( --
    _\< \stemUp a16 ) -- | % 16
    \stemUp g2 ( _\! _\mf _\> \stemUp fis4 ) \stemUp e8. ( -- _\! _\<
    \stemUp d16 ) -- | % 17
    \stemUp d2 ~ _\! _\mf _\> \stemUp d8 \stemUp cis8 ( \stemUp e8
    \stemUp d8 ) | % 18
    \stemUp cis2 ~ \stemUp cis8 _\! _\pp r8 r4 ^\fermata \bar "||"
    r2 r4 \stemDown b''8 ( -. _\p _\< \stemDown cis8 ) -. |
    \barNumberCheck #20
    \stemDown d4 ( _\! _\> \stemDown cis8 ) r8 _\! r4 \stemDown b16 (
    _\p _\< \stemDown e16 \stemDown d16 \stemDown b16 ) | % 21
    \stemDown d4 ( _\! _\> \stemDown cis8 ) r8 _\! r4 \stemDown fis16 (
    _\p \stemDown e16 ) \stemDown e16 -. \stemDown e16 -. | % 22
    \stemDown g16 ( \stemDown fis16 ) \stemDown fis16 -. \stemDown fis16
    -. \stemDown b,16 ( \stemDown ais16 ) \stemDown ais16 -. \stemDown
    ais16 -. \stemDown cis16 ( \stemDown b16 ) \stemDown b16 -.
    \stemDown b16 -. \stemDown fis16 ( \stemDown e16 ) \stemDown e16 -.
    \stemDown e16 -. | % 23
    \stemDown g16 ( \stemDown fis16 ) \stemDown e16 -. \stemDown d16 -.
    \stemDown cis16 -. \stemDown d16 -. \stemDown cis16 -. \stemDown b16
    -. \stemUp ais8 r8 r4 \pageBreak | % 24
    R1*3 | % 27
    r2 r4 \stemDown e''16 ( _\p \stemDown d16 ) \stemDown cis16 -.
    \stemDown b16 -. | % 28
    \stemDown a16 -. \stemDown g16 -. \stemDown fis16 -. \stemDown e16
    -. r4 r2 | % 29
    R1 | \barNumberCheck #30
    \time 2/4  r4 \stemUp e,4 -- _\pp _\< \break | % 31
    \time 4/4  \stemUp fis4 ( _\! _\> \stemUp g8 ) r8 _\! r4 \stemUp e8
    ( -. _\< \stemUp eis8 ) -. | % 32
    \stemUp fis4 ( _\! _\> \stemUp g8 ) r8 _\! r4 \stemUp d16 _. _\pp
    \stemUp d16 _. \stemUp d16 _. \stemUp d16 _. | % 33
    \stemUp d16 -. \stemUp d16 -. \stemUp d16 -. \stemUp d16 -. \stemUp
    d16 ( _\< \stemUp cis16 ) \stemUp d16 -. \stemUp e16 -. \stemUp g16
    ( _\! _\> \stemUp f16 ) \stemUp e16 -. \stemUp d16 -. \stemUp d16 -.
    _\! \stemUp d16 -. \stemUp d16 -. \stemUp d16 -. | % 34
    \stemUp d16 -. \stemUp d16 -. \stemUp d16 -. \stemUp d16 -. \stemUp
    d16 ( _\< \stemUp cis16 ) \stemUp d16 -. \stemUp e16 -. \stemUp g16
    ( _\! _\> \stemUp f16 ) \stemUp e16 -. \stemUp d16 -. \stemUp d8 (
    -. _\! _\p _\< \stemUp des8 ) -. | % 35
    \stemUp c8 _\! r8 \stemUp d16 -. _\p _\< \stemUp d16 -. \stemUp des16
    -. \stemUp des16 -. \stemUp c8 _\! r8 \stemUp f8 ( -. _\p _\<
    \stemUp e8 ) -. | % 36
    \stemUp dis8 _\! r8 \stemUp eis16 -. _\p _\< \stemUp eis16 -.
    \stemUp e16 -. \stemUp e16 -. \stemUp dis8 _\! r8 \stemUp gis8 ( -.
    _\mp _\< \stemUp g8 ) -. \break | % 37
    \stemUp fis8 _\! _\markup{ \italic {cresc.} } r8 \stemUp b8 r8
    \stemDown b'8 r8 \stemDown b8 r8 | % 38
    \stemDown b8 -. \stemDown d8 -. \stemDown fis8 -. \stemDown b8 -.
    _\f r2 | % 39
    R1 | \barNumberCheck #40
    r2 \stemDown e,,2 ~ -> _\mf | % 41
    \stemDown e16 \stemDown e16 -. \stemDown d16 -. \stemDown cis16 -.
    \stemUp b16 -. _\> \stemUp a16 -. \stemUp g16 -. \stemUp fis16 -.
    \stemUp e2 ~ _\! _\p | % 42
    \stemUp e16 \stemUp d16 ( \stemUp cis16 \stemUp d16 \stemUp cis16
    \stemUp d16 \stemUp cis16 \stemUp d16 \stemUp cis8 ) \stemUp e16 (
    -. ^\markup{ \italic {saltando} } _\pp \stemUp e16 ) -. \stemUp d8 (
    -. \stemUp g8 -. | % 43
    \stemUp fis8 ) -. \stemUp a16 ( -. \stemUp a16 ) -. \stemUp d8 ( -.
    \stemUp fis,8 -. \stemUp b8 ) -. \stemUp d,16 ( -. \stemUp d16 ) -.
    \stemUp g8 ( -. \stemUp cis,8 ) -. \pageBreak | % 44
    \stemUp fis16 ( ^\markup{ \italic {unis.} } \stemUp eis16 \stemUp
    fis16 \stemUp eis16 \stemUp fis16 \stemUp eis16 \stemUp fis16
    \stemUp eis16 ) \stemUp fis8 -. \stemUp fis16 ( -. \stemUp fis16 )
    -. \stemUp fis8 ( -. \stemUp fis8 ) -. | % 45
    \stemUp fis8 r8 \stemDown cis'8 r8 \stemUp a8 r8 \stemUp fis8 ( -.
    \stemUp eis8 ) -. | % 46
    \stemUp fis2 ~ \stemUp fis8 \stemUp b16 ( -. _\p \stemUp b16 ) -.
    \stemUp a8 ( -. \stemUp d8 -. | % 47
    \stemDown cis8 ) -. \stemDown e16 ( -. \stemDown e16 ) -. \stemDown
    a8 ( -. \stemDown cis,8 -. \stemDown fis8 ) -. \stemDown a,16 ( -.
    \stemDown a16 ) -. \stemUp d8 ( -. \stemUp gis,8 ) -. | % 48
    \stemUp cis16 ( \stemUp bis16 \stemUp cis16 \stemUp bis16 \stemUp
    cis16 \stemUp bis16 \stemUp cis16 \stemUp bis16 ) \stemUp cis8 -.
    \stemUp a16 ( -. \stemUp a16 ) -. \stemUp gis8 ( -. \stemUp fis8 -.
    | % 49
    \stemUp e8 ) -. \stemUp cis'16 ( -. \stemUp cis16 ) -. \stemUp gis8
    ( -. \stemUp a8 -. \stemUp e8 ) -. \stemUp fis16 ( -. \stemUp fis16
    ) -. \stemUp cis8 -. r8 \break | \barNumberCheck #50
    r2 r16 \stemDown e''16 -. _\mp \stemDown e16 -. \stemDown e16 -.
    \stemDown e16 ( \stemDown cis16 ) \stemDown e16 -. \stemDown e16 -.
    | % 51
    \stemDown dis16 -. \stemDown dis16 -. \stemDown bis16 -. \stemDown
    bis16 -. \stemDown fis16 -. \stemDown fis16 -. \stemDown dis16 -.
    \stemDown dis16 -. \stemUp cis16 -. \stemUp e,16 -. \stemUp e16 -.
    \stemUp e16 -. \stemUp e16 -. \stemUp e16 -. \stemUp e16 -. \stemUp
    e16 -. | % 52
    \stemUp dis16 -. \stemUp dis16 -. \stemUp dis16 -. \stemUp bis16 -.
    \stemUp bis16 -. \stemUp bis16 -. \stemUp bis16 -. \stemUp fis'16 -.
    \stemDown e16 -. \stemDown e''16 -. _\mp \stemDown e16 -. \stemDown
    e16 -. \stemDown e16 ( \stemDown cis16 ) \stemDown e16 -. \stemDown
    e16 -. | % 53
    \stemDown dis16 -. \stemDown dis16 -. \stemDown bis16 -. \stemDown
    bis16 -. \stemDown fis16 -. \stemDown fis16 -. \stemDown dis16 -.
    \stemDown dis16 -. \stemUp cis16 -. \stemUp e,16 -. \stemUp e16 -.
    \stemUp e16 -. \stemUp e16 -. \stemUp e16 -. \stemUp e16 -. \stemUp
    e16 -. \pageBreak | % 54
    \stemUp dis16 -. \stemUp dis16 -. \stemUp dis16 -. \stemUp bis16 -.
    \stemUp bis16 -. \stemUp bis16 -. \stemUp bis16 -. \stemUp fis'16 -.
    \stemUp e8 -. r8 r4 | % 55
    r16 \stemUp a16 -. _\pp _\< \stemUp a16 -. \stemUp a16 -. \stemUp a16
    -. \stemUp a16 -. \stemUp a16 -. \stemUp a16 -. \stemUp a8 ( -- _\!
    _\> \stemUp a8 ) -- \stemUp a8 -- r8 _\! | % 56
    r16 \stemUp e16 -. _\pp _\< \stemUp e16 -. \stemUp e16 -. \stemUp e16
    -. \stemUp e16 -. \stemUp e16 -. \stemUp e16 -. \stemUp e8 ( -- _\!
    _\> \stemUp e8 ) -- \stemUp e8 -- r8 _\! | % 57
    r16 \stemDown cis'16 -. _\p _\< \stemDown cis16 -. \stemDown cis16
    -. \stemDown cis16 -. \stemDown cis16 -. \stemDown cis16 -.
    \stemDown cis16 -. \stemDown cis8 ( -- _\! _\> \stemDown cis8 ) --
    \stemDown cis8 -- r8 _\! | % 58
    r16 \stemUp <gis b>16 -. _\p _\< \stemUp <gis b>16 -. \stemUp <gis
        b>16 -. \stemUp <gis b>16 -. \stemUp <gis b>16 -. \stemUp <gis
        b>16 -. \stemUp <gis b>16 -. \stemUp <dis gis>8 ( -- _\! _\>
    \stemUp <dis gis>8 ) -- \stemDown <dis gis>8 _\! \stemDown dis''16
    -. _\mp \stemDown dis16 -. \break | % 59
    \stemDown cis16 -. \stemDown cis16 -. \stemDown fisis,16 -.
    \stemDown fisis16 -. \stemDown fisis16 -. \stemDown fisis16 -.
    \stemDown ais,16 -. \stemDown ais16 -. \stemUp gis16 -. \stemUp gis16
    -. \stemUp gis16 -. \stemUp gis16 -. \stemUp gis16 ( \stemUp b16 )
    \stemUp ais16 -. \stemUp gis16 -. | \barNumberCheck #60
    \stemUp fisis16 ( \stemUp gis16 ) \stemUp fisis16 -. \stemUp e16 -.
    \stemUp dis16 -. \stemUp e16 -. \stemUp dis8 -. r16 \stemDown b''16
    -. _\mp \stemDown b16 -. \stemDown b16 -. \stemDown b16 ( \stemDown
    gis16 \stemDown b16 ) \stemDown b16 -. | % 61
    \stemDown cis16 -. \stemDown cis16 -. \stemDown fisis,16 -.
    \stemDown fisis16 -. \stemDown fisis16 -. \stemDown fisis16 -.
    \stemDown ais,16 -. \stemDown ais16 -. \stemUp gis16 -. \stemUp gis16
    -. \stemUp gis16 -. \stemUp gis16 -. \stemUp gis16 ( \stemUp b16 )
    \stemUp ais16 -. \stemUp gis16 -. | % 62
    \stemUp fisis16 ( \stemUp gis16 ) \stemUp fisis16 -. \stemUp e16 -.
    \stemUp dis16 -. \stemUp e16 -. \stemUp dis8 -. r2 | % 63
    r16 \stemDown dis'16 -. _\p _\< \stemDown dis16 -. \stemDown dis16
    -. \stemUp dis16 ( \stemUp cis16 ) \stemUp b16 -. \stemUp ais16 -.
    \stemUp gis8 ( -- _\! _\> \stemUp eis8 ) -- \stemUp fis8 -- r8 _\!
    \pageBreak | % 64
    r16 \stemUp b16 -. _\p _\< \stemUp b16 -. \stemUp b16 -. \stemUp b16
    ( \stemUp ais16 ) \stemUp gis16 -. \stemUp fis16 -. \stemUp e8 ( --
    _\! _\> \stemUp cisis8 ) -- \stemUp dis8 -- r8 _\! | % 65
    r16 \stemDown fis'16 -. _\mp _\< \stemDown fis16 -. \stemDown fis16
    -. \stemDown fis16 ( \stemDown eis16 ) \stemDown dis16 -. \stemDown
    cisis16 -. \stemUp b8 ( -- _\! _\> \stemUp gisis8 ) -- \stemUp ais8
    -- r8 _\! | % 66
    r16 \stemDown dis16 -. _\mp _\< \stemDown dis16 -. \stemDown dis16
    -. \stemUp dis16 ( \stemUp cis16 ) \stemUp b16 -. \stemUp ais16 -.
    \stemUp gis8 ( -- _\! _\> \stemUp eis8 ) -- \stemUp fis8 -- r8 _\! | % 67
    r16 \stemUp b16 -. _\f \stemUp b16 -. \stemUp b16 -. \stemUp b16 (
    \stemUp gis16 ) \stemUp ais16 -. \stemUp b16 -. \stemUp fis8 -. r8 r4
    | % 68
    R1 \pageBreak | % 69
    r16 \stemDown d'16 -. _\ff \stemDown d16 -. \stemDown d16 -.
    \stemDown d16 ( \stemDown b16 ) \stemDown cis16 -. \stemDown d16 -.
    \stemDown cis8 -. r8 r4 | \barNumberCheck #70
    r2 \stemDown d8 -> _\ff \stemDown b8 -> \stemDown c8 -> r8 | % 71
    r8 \stemDown d'16 _\markup{ \italic {détaché} } \stemDown c16
    \stemDown b16 \stemDown a16 \stemDown f16 \stemDown e16 \stemDown d8
    -> \stemDown b8 -> \stemDown c8 -> r8 | % 72
    r8 \stemDown d'16 \stemDown c16 \stemDown b16 \stemDown a16
    \stemDown f16 \stemDown e16 \stemDown d8 -> \stemDown b8 ->
    \stemDown c8 -> r8 | % 73
    r16 \stemDown a'16 \stemDown a16 \stemDown a16 \stemDown a16
    \stemDown c16 \stemDown b16 \stemDown a16 \stemDown d,8 -> \stemDown
    b8 -> \stemDown c8 -> r8 \pageBreak | % 74
    r16 \stemDown a'16 \stemDown a16 \stemDown a16 \stemDown a16 (
    \stemDown c16 \stemDown b16 ) \stemDown a16 -. \stemDown <a c>4 ~ ->
    ~ \stemDown <a c>8 r8 | % 75
    \stemDown <a c>4 ~ -> ~ \stemDown <a c>8 r8 \stemDown <g a>4 ~ -> ~
    \stemDown <g a>8 r8 | % 76
    \stemDown <g a>4 ~ -> ~ \stemDown <g a>8 r8 \stemUp g,4 ~ -> _\f
    \stemUp g8 r8 | % 77
    \stemUp g4 ~ -> \stemUp g8 r8 \stemUp <cis, g'>4 ~ -> ~ _\mf \stemUp
    <cis g'>8 r8 \break | % 78
    \stemUp <cis g'>4 ~ -> ~ \stemUp <cis g'>8 r8 r4 \stemUp <cis g'>4 ~
    -> ~ _\mp | % 79
    \stemUp <cis g'>4 ~ ~ \stemUp <cis g'>8 r8 r2 | \barNumberCheck #80
    R1*3 \pageBreak | % 83
    R1*3 | % 86
    r8 \stemDown a'8 ( ^\markup{ \italic {espress.} } _\pp \stemDown d8
    \stemDown fis8 ) \stemDown a4. ( \stemDown b8 ) | % 87
    \stemDown b2 ( _\< \stemDown d4. \stemDown fis8 ) | % 88
    \stemDown fis2 ~ _\! _\mp _\> \stemDown fis8 r8 _\! _\ppp r4
    ^\fermata \bar "||"
    R1*4 | % 93
    r2 \stemUp fis,,4 ( ^\markup{ \italic {con sordini} } _\mf \stemUp g8
    \stemUp a8 \break | % 94
    \stemUp e8 ) r8 r4 \stemUp e4 ( _\> \stemUp fis8 \stemUp g8 | % 95
    \stemUp d8 ) _\! r8 r4 r2 | % 96
    r2 \stemUp dis4 ( -> _\mf _\> \stemUp e4 | % 97
    \stemUp fis8 ) _\! _\p r8 r4 \stemUp fis4 ( _\mf \stemUp g8 \stemUp
    a8 | % 98
    \stemUp e8 ) r8 r4 \stemUp e4 ( _\> \stemUp fis8 \stemUp g8 | % 99
    \stemUp d8 ) _\! r8 r4 r2 | \barNumberCheck #100
    r2 \stemUp dis4 ( -> _\mf _\> \stemUp e4 \bar "||"
    \stemUp fis8 ) _\! _\p \stemUp a16 ( -. ^\markup{ \italic {saltando}
        } \stemUp a16 ) -. \stemUp a8 ( -. \stemUp a8 -. \stemUp a8 ) -.
    \stemUp a16 ( -. \stemUp a16 ) -. \stemUp a8 ( -. \stemUp a8 -. | % 102
    \stemUp b8 ) -. \stemUp b16 ( -. \stemUp b16 ) -. \stemUp b8 ( -.
    \stemUp b8 -. \stemUp b8 ) -. \stemUp b16 ( -. \stemUp b16 ) -.
    \stemUp b8 ( -. \stemUp b8 -. \pageBreak | % 103
    \stemUp b8 ) -. \stemUp b16 ( -. \stemUp b16 ) -. \stemUp b8 ( -.
    \stemUp b8 -. \stemUp b8 ) -. \stemUp b16 ( -. \stemUp b16 ) -.
    \stemUp b8 ( -. \stemUp b8 -. | % 104
    \stemUp a8 ) -. _\< \stemUp a16 ( -. \stemUp a16 ) -. \stemUp a8 (
    -. \stemUp a8 -. \stemUp a8 ) -. \stemUp a16 ( -. \stemUp a16 ) -.
    \stemUp a8 ( -. \stemUp a8 -. | % 105
    \stemUp ais8 ) -. _\! _\markup{ \italic {poco più} } _ "" \stemUp
    ais16 ( -. \stemUp ais16 ) -. \stemUp ais8 ( -. \stemUp ais8 -.
    \stemUp fis8 ) -. \stemUp fis16 ( -. \stemUp fis16 ) -. \stemUp fis8
    ( -. \stemUp fis8 -. | % 106
    \stemUp fis8 ) -. _\markup{ \italic {poco cresc.} } \stemUp fis16 (
    -. \stemUp fis16 ) -. \stemUp fis8 ( -. \stemUp fis8 -. \stemUp fis8
    ) -. \stemUp fis16 ( -. \stemUp fis16 ) -. \stemUp fis8 ( -. \stemUp
    fis8 -. | % 107
    \stemUp e8 ) -. _\mf \stemUp e16 ( -. \stemUp e16 ) -. \stemUp e8 (
    -. \stemUp e8 -. \stemUp e8 ) -. \stemUp e16 ( -. \stemUp e16 ) -.
    \stemUp e8 ( -. \stemUp e8 -. \break | % 108
    \stemUp e8 ) -. \stemUp <e e'>16 ( -. _\markup{ \italic {dim.} }
    \stemUp <e e'>16 ) -. \stemUp <e e'>8 ( -. \stemUp <e e'>8 -.
    \stemUp <e e'>8 ) -. \stemUp <e e'>16 ( -. \stemUp <e e'>16 ) -.
    \stemUp <e e'>8 ( -. \stemUp <e e'>8 -. | % 109
    \stemUp <e a>8 ) -. _\p \stemUp <e a>16 ( -. \stemUp <e a>16 ) -.
    \stemUp <e a>8 ( -. \stemUp <e a>8 -. \stemUp e8 ) -. \stemUp e16 (
    -. \stemUp e16 ) -. \stemUp e8 ( -. \stemUp e8 -. | \barNumberCheck
    #110
    \stemUp fis8 ) -. \stemUp fis16 ( -. \stemUp fis16 ) -. \stemUp fis8
    ( -. \stemUp fis8 -. \stemUp fis8 ) -. \stemUp fis16 ( -. \stemUp
    fis16 ) -. \stemUp fis8 ( -. \stemUp fis8 -. | % 111
    \stemUp fis8 ) -. \stemUp fis16 ( -. \stemUp fis16 ) -. \stemUp fis8
    ( -. \stemUp fis8 -. \stemUp fis8 ) -. \stemUp fis16 ( -. \stemUp
    fis16 ) -. \stemUp fis8 ( -. \stemUp fis8 -. \pageBreak | % 112
    \stemUp e8 ) -. _\< \stemUp e16 ( -. \stemUp e16 ) -. \stemUp e8 (
    -. \stemUp e8 -. \stemUp e8 ) -. \stemUp e16 ( -. \stemUp e16 ) -.
    \stemUp e8 ( -. \stemUp e8 -. | % 113
    \stemUp eis8 ) -. _\! \stemUp eis16 ( -. \stemUp eis16 ) -. \stemUp
    eis8 ( -. \stemUp eis8 -. \stemUp cis8 ) -. \stemUp cis16 ( -.
    \stemUp cis16 ) -. \stemUp cis8 ( -. \stemUp cis8 -. | % 114
    \stemUp fis8 ) -. _\markup{ \italic {poco cresc.} } \stemUp fis16 (
    -. \stemUp fis16 ) -. \stemUp fis8 ( -. \stemUp fis8 -. \stemUp fis8
    ) -. \stemUp fis16 ( -. \stemUp fis16 ) -. \stemUp fis8 ( -. \stemUp
    fis8 -. | % 115
    \stemUp a8 ) -. _\mf \stemUp a16 ( -. \stemUp a16 ) -. \stemUp a8 (
    -. \stemUp a8 -. \stemUp a8 ) -. \stemUp a16 ( -. \stemUp a16 ) -.
    \stemUp a8 ( -. \stemUp a8 -. \break | % 116
    \stemUp gis8 ) -. _\markup{ \italic {dim.} } \stemUp gis16 ( -.
    \stemUp gis16 ) -. \stemUp gis8 ( -. \stemUp gis8 -. \stemUp e8 ) -.
    \stemUp e16 ( -. \stemUp e16 ) -. \stemUp e8 ( -. \stemUp e8 -. | % 117
    \stemDown gis'8 ) -. _\p \stemDown gis16 ( -. \stemDown gis16 ) -.
    \stemDown gis8 ( -. \stemDown gis8 -. \stemDown gis8 ) -. \stemDown
    gis16 ( -. \stemDown gis16 ) -. \stemUp gis,8 ( -. \stemUp gis8 -. | % 118
    \stemUp gis8 ) -. \stemUp gis16 ( -. \stemUp gis16 ) -. \stemUp gis8
    ( -. \stemUp gis8 -. \stemUp gis8 ) -. \stemUp gis16 ( -. \stemUp
    gis16 ) -. \stemUp b8 ( -. \stemUp gis8 -. | % 119
    \stemUp g8 ) -. _\markup{ \italic {cresc.} } \stemUp g16 ( -.
    \stemUp g16 ) -. \stemUp g8 ( -. \stemUp g8 -. \stemUp g8 ) -.
    \stemUp g16 ( -. \stemUp g16 ) -. \stemUp g8 ( -. \stemUp g8 -.
    \pageBreak | \barNumberCheck #120
    \stemUp g8 ) -. \stemUp g16 ( -. \stemUp g16 ) -. \stemUp g8 ( -.
    \stemUp g8 -. \stemUp g8 ) -. \stemUp g16 ( -. \stemUp g16 ) -.
    \stemUp b8 ( -. \stemUp g8 -. | % 121
    \stemUp g8 ) -. _\mf \stemUp g16 -- \stemUp g16 -- \stemUp g8 --
    \stemUp g8 -- \stemUp g8 -- \stemUp g16 -- \stemUp g16 -- \stemUp g8
    -- \stemUp g8 -- | % 122
    \stemUp g8 ^\markup{ \italic {simile} } _\markup{ \italic {poco
            cresc.} } \stemUp g16 \stemUp g16 \stemUp g8 \stemUp g8
    \stemUp g8 \stemUp g16 \stemUp g16 \stemUp g8 \stemUp g8 | % 123
    \stemUp e8 \stemUp e16 \stemUp e16 \stemUp e8 \stemUp e8 \stemUp e8
    \stemUp e16 \stemUp e16 \stemUp e8 \stemUp e8 | % 124
    \stemUp d8 _\f \stemUp d16 \stemUp d16 \stemUp d8 \stemUp d8 \stemUp
    d8 \stemUp d16 \stemUp d16 \stemUp d8 \stemUp d8 \break | % 125
    \stemUp d8 _\< \stemUp d16 \stemUp d16 \stemUp d8 \stemUp d8 \stemUp
    d8 \stemUp d16 \stemUp d16 \stemUp d8 \stemUp d8 | % 126
    \stemUp cis8 _\! _\ff \stemUp cis16 \stemUp cis16 \stemUp cis8
    \stemUp cis8 \stemUp cis8 \stemUp cis16 \stemUp cis16 \stemUp cis8
    \stemUp cis8 | % 127
    R1*3 ^\markup{ \italic {alzate sordini} } \bar "||"
    r2 ^\markup{ \italic {senza sordini} } r8 \stemDown fis'8 ( _\mf
    \stemDown e8 \stemDown d8 ) | % 131
    \stemUp b8 ( _\< \stemUp a8 \stemUp fis8 \stemUp a8 ) \stemDown d4.
    ( _\! _\> \stemUp b8 ) \pageBreak | % 132
    \stemUp a2 ~ _\! \stemDown a8 \stemDown fis'8 ( \stemDown e8
    \stemDown d8 ) | % 133
    \stemUp a8 ( _\< \stemUp fis8 \stemUp d8 \stemUp fis8 ) \stemUp b4.
    ( _\! _\> \stemUp a8 ) | % 134
    \stemUp a4 ~ _\! _\< \stemDown a32 \stemDown a32 ( \stemDown b32
    \stemDown cis32 \stemDown d32 \stemDown e32 \stemDown fis32
    \stemDown g32 ) \stemDown a4 -- _\! _\ff \stemDown g8 ( \stemDown
    fis8 ) | % 135
    \stemDown fis4 ( \stemDown e4 ) \stemDown g4 -- \stemDown fis8 (
    \stemDown e8 ) | % 136
    \stemDown e4 ( \stemDown d4 ) r8 \stemDown fis8 ( _\> \stemDown e8
    \stemDown d8 ) | % 137
    \stemUp a8 ( _\! _\mf _\< \stemUp fis8 \stemUp d8 \stemUp fis8 )
    \stemUp b4. ( _\! _\f _\> \stemUp a8 ) \pageBreak | % 138
    \stemUp a4 ~ _\! _\< \stemDown a32 \stemDown a32 ( \stemDown b32
    \stemDown cis32 \stemDown d32 \stemDown e32 \stemDown fis32
    \stemDown g32 ) \stemDown a4 -- _\! _\ff \stemDown g8 ( \stemDown
    fis8 ) | % 139
    \stemDown fis4 ( \stemDown e4 ) \stemDown g4 -- \stemDown fis8 (
    \stemDown e8 ) | \barNumberCheck #140
    \stemDown e4 ( \stemDown d4 ) r8 \stemDown fis8 ( _\> \stemDown e8
    \stemDown d8 ) | % 141
    \stemUp a8 ( _\! _\mf _\< \stemUp fis8 \stemUp d8 \stemUp fis8 )
    \stemUp b4. ( _\! _\f _\> \stemUp a8 ) \bar "||"
    \stemUp a2 _\! _\mf _\> \stemDown c4. ( _\! _\mp \stemDown fis8 ) | % 143
    \stemUp b,2 \stemUp b4. ( \stemDown e8 ) | % 144
    \stemUp a,2 _\> \stemUp a4. ( _\! _\p \stemDown c8 ) \break | % 145
    \stemUp gis4. ( \stemUp b8 ) \stemUp g4. ( \stemUp bes8 ) | % 146
    \stemUp fis4. ( \stemUp a8 ) \stemDown c4. ( \stemDown fis8 ) | % 147
    \stemUp b,2 \stemUp b4. ( \stemDown e8 ) | % 148
    \stemUp a,2 _\> \stemUp a4. ( _\! _\pp \stemDown c8 ) | % 149
    \stemUp gis4. ( \stemUp b8 ) \stemUp g4. ( \stemUp bes8 ) |
    \barNumberCheck #150
    \stemUp fis4. ( \stemUp a8 ) \stemUp f4. ( _\markup{ \italic {dim.}
        } \stemUp bes8 ) | % 151
    \stemUp fis4. ( \stemUp a8 ) \stemUp f4. ( \stemUp bes8 ) | % 152
    \stemUp fis4. ( _\ppp \stemUp a8 ) \stemUp fis4. ( \stemUp a8 ) | % 153
    \stemUp fis4. ( \stemUp a8 ) r2 | % 154
    \stemUp a2 _\ppp ^\markup{ \italic {divisi} } _\< \stemUp b2 _\! _\p
    _\> | % 155
    \stemUp a2 ~ _\! _\ppp \stemUp a8 r8 r4 \pageBreak | % 156
    \stemUp fis2 _\ppp _\< \stemUp g2 _\! _\p _\> | % 157
    \stemUp a2 ~ _\! \stemUp a8 r8 r4 | % 158
    \stemUp fis2 ~ _\pppp \stemUp fis8 r8 r4 | % 159
    \stemUp fis2 ~ _\ppppp \stemUp fis8 r8 r4 | \barNumberCheck #160
    R1 \bar "||"
    \key c \major \stemDown <c g' g' g'>8 _\ff ^\markup{ \italic {unis.}
        } ^ "arco" ^ "" r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp g'16 -> _\sff \stemUp g16 \stemUp g16 }
    \stemUp g8 ~ \stemUp g4 ~ | % 162
    \stemUp g8 \stemUp fis8 -> \stemUp f8 -> \stemUp fis8 -> \stemUp g8
    -> r8 r4 | % 163
    \stemUp fis8 _\sf r8 \stemUp f8 _\sf r8 r4 r8 \stemUp f8 _\sf | % 164
    \stemUp fis8 _\sf r8 \stemUp <g es'>8 _\sf r8 r4 \stemDown <g' es'>16
    _\ff \stemDown <g es'>16 \stemDown <g es'>16 \stemDown <g es'>16
    \pageBreak | % 165
    \stemDown <g e'>8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp g,16 _\sff \stemUp g16 \stemUp g16 }
    \stemUp g8 ~ \stemUp g4 ~ | % 166
    \stemUp g8 \stemUp f8 -> \stemUp fis8 -> \stemUp f8 -> \stemUp g8 ->
    r8 r4 | % 167
    \stemUp fis8 _\sf r8 \stemUp g8 _\sf r8 r4 r8 \stemUp g8 _\sf | % 168
    \stemUp fis8 _\sf r8 \stemUp e8 _\sf r8 r4 \stemDown <g' e'>16 _\ff
    \stemDown <g e'>16 \stemDown <g e'>16 \stemDown <g e'>16 | % 169
    \stemDown <f d'>8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <d f'>16 _\sff \stemDown <d f'>16 \stemDown <d f'>16 }
    \stemDown <d f'>8 ~ ~ \stemDown <d f'>4 ~ ~ | \barNumberCheck #170
    \stemDown <d f'>8 \stemDown <d g'>8 -> \stemDown <d f'>8 ->
    \stemDown <d g'>8 -> \stemDown <d gis'>8 -> \stemDown <d a''>8 -> r4
    | % 171
    r16 \stemUp d,16 _\ff ^\markup{ \italic {feroce} } \stemUp e16
    \stemUp f16 \stemUp g16 \stemUp a16 \stemUp bes16 \stemUp c16
    \stemUp d16 \stemUp c16 \stemUp bes16 \stemUp a16 \stemUp bes8 r8
    \pageBreak | % 172
    r16 \stemUp d,16 \stemUp e16 \stemUp f16 \stemUp g16 \stemUp a16
    \stemUp bes16 \stemUp c16 \stemUp d16 \stemUp c16 \stemUp bes16
    \stemUp a16 \stemUp bes8 \stemUp a16 \stemUp bes16 | % 173
    \stemUp c8 \stemUp bes16 \stemUp c16 \stemDown d8 \stemDown c16
    \stemDown d16 \stemDown e8 \stemDown d16 \stemDown e16 \stemDown f8
    \stemDown e16 \stemDown f16 | % 174
    \stemDown g8 \stemDown fis16 \stemDown g16 \stemDown a8 \stemDown
    gis16 \stemDown a16 \stemDown bes8 \stemDown a16 \stemDown bes16
    \stemDown c8 \stemDown d8 | % 175
    \stemDown e8 r8 \stemUp d,,16 _\ff \stemUp e16 \stemUp f16 \stemUp g16
    \stemUp a16 \stemUp g16 \stemUp f16 \stemUp e16 \stemUp f8 r8 | % 176
    r4 \stemUp d16 \stemUp e16 \stemUp f16 \stemUp g16 \stemUp a16
    \stemUp g16 \stemUp f16 \stemUp e16 \stemUp f8 \stemUp e16 \stemUp f16
    | % 177
    \stemUp g8 \stemUp f16 \stemUp g16 \stemUp a8 \stemUp g16 \stemUp a16
    \stemUp b8 \stemUp a16 \stemUp b16 \stemUp c8 \stemUp b16 \stemUp c16
    \pageBreak | % 178
    \stemDown d8 \stemDown cis16 \stemDown d16 \stemDown e8 \stemDown
    dis16 \stemDown e16 \stemDown f8 \stemDown e16 \stemDown f16
    \stemDown g8 \stemDown fis8 | % 179
    \stemUp e16 \stemUp e,16 _\markup{ \italic {come prima} } \stemUp
    fis16 \stemUp g16 \stemUp a16 \stemUp b16 \stemUp c16 \stemUp d16
    \stemDown e16 \stemDown d16 \stemDown c16 \stemDown b16 \stemDown c8
    r8 | \barNumberCheck #180
    r16 \stemUp e,16 \stemUp fis16 \stemUp g16 \stemUp a16 \stemUp b16
    \stemUp c16 \stemUp d16 \stemDown e16 \stemDown d16 \stemDown c16
    \stemDown b16 \stemUp c8 \stemUp b16 \stemUp c16 | % 181
    \stemDown d8 \stemDown c16 \stemDown d16 \stemDown e8 \stemDown d16
    \stemDown e16 \stemDown fis8 \stemDown e16 \stemDown fis16 \stemDown
    g8 \stemDown fis16 \stemDown g16 | % 182
    \stemDown a8 \stemDown g16 \stemDown a16 \stemDown b8 \stemDown a16
    \stemDown b16 \stemDown c8 \stemDown b16 \stemDown c16 \stemDown d8
    \stemDown e8 \break | % 183
    \stemDown fis8 r8 \stemUp e,,16 _\markup{ \italic {sempre} } _ ""
    \stemUp fis16 \stemUp g16 \stemUp a16 \stemUp b16 \stemUp a16
    \stemUp g16 \stemUp fis16 \stemUp g8 r8 | % 184
    r4 \stemUp e16 \stemUp fis16 \stemUp g16 \stemUp a16 \stemUp b16
    \stemUp a16 \stemUp g16 \stemUp fis16 \stemUp g8 \stemUp fis16
    \stemUp g16 | % 185
    \stemUp a8 \stemUp g16 \stemUp a16 \stemUp b8 \stemUp a16 \stemUp b16
    \stemUp cis8 \stemUp b16 \stemUp cis16 \stemDown d8 r8 | % 186
    r2 r4 \stemUp e,8 _\ff \stemUp d16 \stemUp e16 | % 187
    \stemUp fis8 \stemUp e16 \stemUp fis16 \stemUp g8 \stemUp fis16
    \stemUp g16 \stemUp a8 \stemUp g16 \stemUp a16 \stemUp b8 r8
    \pageBreak | % 188
    r2 r4 \stemDown g'8 _\fff \stemDown fis16 \stemDown g16 | % 189
    \stemDown g8 \stemDown fis16 \stemDown g16 \stemDown g8 \stemDown
    fis16 \stemDown g16 \stemDown g8 \stemDown fis16 \stemDown g16
    \stemDown <bes, es>4 :16 | \barNumberCheck #190
    \stemDown <bes es>2 :16 \stemDown <bes es>2 :16 | % 191
    \stemDown <bes es>2. :16 \stemDown <g g'>4 :16 \break | % 192
    \stemDown <g g'>2 :16 \stemDown <g g'>2 :16 | % 193
    \stemDown <g g'>2. :16 \stemUp <f f'>4 :16 | % 194
    \stemUp <f f'>2 :16 \stemUp <f f'>2 :16 | % 195
    \stemDown <f' a>2 :16 \stemDown <f a>2 :16 \pageBreak | % 196
    \stemUp <f, f'>2 :16 \stemUp <a d>2 :16 | % 197
    \stemUp a2 :16 \stemUp f8 -> \stemUp f8 -> \stemDown a16 \stemDown
    e'16 \stemDown d16 \stemDown a16 | % 198
    \stemUp f16 \stemUp bes16 \stemUp a16 \stemUp f16 \stemUp d16
    \stemUp g16 \stemUp f16 \stemUp d16 \stemDown a'16 \stemDown e'16
    \stemDown d16 \stemDown a16 \stemUp f16 \stemUp bes16 \stemUp a16
    \stemUp f16 | % 199
    \stemUp d16 \stemUp g16 \stemUp f16 \stemUp d16 r4 r2 |
    \barNumberCheck #200
    R1 \break | % 201
    R1*4 | % 205
    r4 \once \omit TupletBracket
    \times 4/7  {
        \stemDown cis'16*161/160 ( _\p \stemDown d16*161/160 \stemDown e16*161/160
        \stemDown f16*161/160 \stemDown g16*161/160 \stemDown a16*161/160
        \stemDown bes16*161/160 }
    \stemDown cis8 ) r8 r4 | % 206
    R1 \pageBreak | % 207
    r4 \stemUp as,4 ( ~ -> _\p \stemUp as4 \stemUp g8 ) r8 | % 208
    R1 | % 209
    r4 \stemDown ces4 ( ~ -> _\markup{ \italic {più} } _ "" \stemDown
    ces4 \stemUp bes8 ) r8 | \barNumberCheck #210
    r4 r8 \stemDown d8 ( ~ _\mf \stemDown d8 \stemDown cis8 ~ \stemDown
    cis8 ) r8 | % 211
    r4 r8 \stemDown f8 ( ~ _\markup{ \italic {cresc.} } \stemDown f8
    \stemDown e8 ~ \stemDown e8 ) \stemDown g8 ( ~ | % 212
    \stemDown g8 \stemDown fis8 ~ \stemDown fis8 ) \stemDown a8 ( ~ _\f
    _\< \stemDown a8 \stemDown gis8 ~ \stemDown gis8 ) \stemDown a8 ( ~
    \pageBreak | % 213
    \stemDown a8 \stemDown gis8 ~ \stemDown gis8 ) \stemDown a8 ~
    \stemDown a8 \stemDown gis8 ~ \stemDown gis8 \stemDown b8 ~ _\! _\ff
    | % 214
    \stemDown b8 \stemDown a8 ~ \stemDown a8 \stemDown gis8 ~ \stemDown
    gis8 \stemDown fis8 ~ \stemDown fis8 \stemDown e8 ~ | % 215
    \stemDown e8 \stemDown d8 ~ \stemDown d8 \stemDown bis8 ~ \stemUp
    bis8 \stemUp cis8 ~ \stemUp cis8 \stemUp ais8 ( ~ | % 216
    \stemUp ais8 _\markup{ \italic {dim. un poco} } \stemUp b8 ~ \stemUp
    b8 ) \stemUp gis8 ( ~ \stemUp gis8 \stemUp a8 ~ \stemUp a8 ) \stemUp
    eis8 ( ~ \break | % 217
    \stemUp eis8 \stemUp fis8 ~ \stemUp fis8 ) \stemUp e8 ( ~ \stemUp e8
    \stemUp eis8 ~ \stemUp eis8 ) \stemUp b'8 ( ~ _\f | % 218
    \stemUp b8 \stemUp a8 ~ \stemUp a8 ) \stemUp gis8 ( ~ \stemUp gis8
    \stemUp fis8 ~ \stemUp fis8 ) r8 | % 219
    R1 | \barNumberCheck #220
    r2 r4 r8 \stemUp eis8 ( ~ _\mf \pageBreak | % 221
    \stemUp eis8 _\markup{ \italic {dim.} } \stemUp fis8 ~ \stemUp fis8
    ) \stemUp e8 ( ~ \stemUp e8 \stemUp eis8 ~ \stemUp eis8 ) \stemUp e8
    ( ~ | % 222
    \stemUp e8 \stemUp eis8 ~ \stemUp eis8 ) \stemUp e8 ( ~ \stemUp e8
    \stemUp eis8 ~ \stemUp eis8 ) \stemUp e8 ( ~ _\p | % 223
    \stemUp e8 \stemUp eis8 ~ \stemUp eis2 ~ \stemUp eis8 ) \stemUp e8 (
    ~ | % 224
    \stemUp e8 \stemUp eis8 ~ \stemUp eis2 ~ \stemUp eis8 ) \stemUp e8 (
    ~ | % 225
    \stemUp e8 _\markup{ \italic {dim.} } \stemUp eis8 ~ \stemUp eis2 ~
    \stemUp eis8 ) \stemUp e8 ( ~ \break | % 226
    \stemUp e8 \stemUp eis8 ~ \stemUp eis2 ~ \stemUp eis8 ) \stemUp dis8
    ( ~ _\pp | % 227
    \stemUp dis8 \stemUp e8 ~ \stemUp e8 \stemUp dis8 ~ \stemUp dis8
    \stemUp e8 ~ \stemUp e8 \stemUp dis8 ~ | % 228
    \stemUp dis8 \stemUp e8 ~ \stemUp e8 _\> \stemUp dis8 ~ \stemUp dis8
    \stemUp e8 ~ \stemUp e8 \stemUp f8 ~ | % 229
    \stemUp f8 ) _\! r8 r4 r2 | \barNumberCheck #230
    r2 r4 \stemUp e8 ( -. _\pp _\< \stemUp f8 ) -. \break | % 231
    \stemUp ges4 ( _\! _\> \stemUp f8 ) r8 _\! r2 | % 232
    r2 r4 \stemUp e8 ( -. _\pp _\< \stemUp f8 ) -. | % 233
    \stemUp ges4 ( _\! _\> \stemUp f8 ) r8 _\! r2 | % 234
    r2 r4 \stemUp e8 ( -. _\pp _\< \stemUp f8 ) -. | % 235
    \stemUp ges4 ( _\! _\> \stemUp f8 ) r8 _\! r4 \stemUp e16 ( _\<
    \stemUp f16 \stemUp ges16 \stemUp e16 ) | % 236
    \stemUp ges4 ( _\! _\> \stemUp f8 ) r8 _\! r2 \pageBreak | % 237
    R1*3 | \barNumberCheck #240
    \stemUp es8 ( -> _ "" _\markup{ \italic {cresc.} } \stemUp des8 )
    \stemUp c16 ( \stemUp des16 \stemUp es16 \stemUp des16 ) \stemUp f8
    ( -> \stemUp es8 ) \stemUp d16 ( \stemUp es16 \stemUp f16 \stemUp es16
    ) | % 241
    \stemUp ges8 ( _\< \stemUp f8 ) \stemUp e16 ( \stemUp f16 \stemUp
    ges16 \stemUp e16 ) \stemUp ges8 ( \stemUp f8 ) \stemUp e16 (
    \stemUp f16 \stemUp ges16 \stemUp f16 ) \pageBreak | % 242
    \stemUp as16 ( _\! _ "" _\markup{ \italic {cresc.} } \stemUp ges16
    ) \stemUp ges16 -. \stemUp ges16 -. \stemUp bes16 ( \stemUp as16 )
    \stemUp as16 -. \stemUp as16 -. \stemUp ces16 ( \stemUp bes16 )
    \stemUp bes16 -. \stemUp bes16 -. \stemUp a16 ( \stemUp ais16
    \stemUp b16 \stemUp ais16 ) | % 243
    \stemUp cis16 ( _\ff \stemUp b16 ) \stemUp b16 -. \stemUp b16 -.
    \stemUp ais16 ( \stemUp b16 \stemUp cis16 \stemUp b16 ) \stemDown d16
    ( \stemDown cis16 ) \stemDown cis16 -. \stemDown cis16 -. \stemDown
    bis16 ( \stemDown cis16 \stemDown d16 \stemDown cis16 ) | % 244
    \stemDown e16 ( \stemDown d16 ) \stemDown d16 -. \stemDown d16 -.
    \stemDown fis16 ( \stemDown e16 ) \stemDown e16 -. \stemDown e16 -.
    \stemDown g16 ( \stemDown fis16 ) \stemDown fis16 -. \stemDown fis16
    -. r4 | % 245
    r4 r16 \stemDown fis16 ( _\fff \stemDown eis16 \stemDown fis16 )
    \stemDown g16 ( \stemDown fis16 ) \stemDown fis16 -. \stemDown fis16
    -. r4 \pageBreak | % 246
    r4 r16 \stemDown fis16 ( \stemDown eis16 \stemDown fis16 ) \stemDown
    g16 ( \stemDown fis16 ) \stemDown fis16 -. \stemDown fis16 -.
    \stemDown fis16 ( \stemDown e16 ) \stemDown e16 -. \stemDown e16 -.
    | % 247
    \stemDown g16 ( \stemDown fis16 ) \stemDown fis16 -. \stemDown fis16
    -. \stemUp b,16 ( \stemUp ais16 ) \stemUp ais16 -. \stemUp ais16 -.
    \stemUp cis16 ( \stemUp b16 ) \stemUp b16 -. \stemUp b16 -.
    \stemDown fis'16 ( \stemDown e16 ) \stemDown e16 -. \stemDown e16 -.
    | % 248
    \stemDown g16 \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown
    cis16 \stemDown d16 \stemDown cis16 \stemDown b16 \stemDown ais16
    \stemDown g'16 \stemDown fis16 \stemDown eis16 \stemDown fis8 _\f
    \stemDown b,8 | % 249
    \stemUp b4 ( _ "" \stemUp ais8 ) r8 r4 \stemUp b8 \stemUp b8 |
    \barNumberCheck #250
    \stemUp b4 ( _ "" \stemUp ais8 ) r8 r4 \stemUp a8 \stemUp d8
    \stemUp g,8 \stemUp d'8 | % 251
    \stemDown d4 ( _ "" \stemDown cis8 ) r8 r4 \stemDown d8 \stemDown
    d8 \break | % 252
    \stemDown d4 ( _ "" \stemDown cis8 ) r8 r4 \stemDown fis8 _\ff
    \stemDown fis8 | % 253
    \stemDown fis8 ( -> \stemDown eis8 ) r4 r4 \stemDown fis8 \stemDown
    fis8 | % 254
    \stemDown fis8 ( -> \stemDown eis8 ) r4 r4 r8 \stemDown b8 _\ff
    \stemDown eis8 | % 255
    r8 \stemDown cis8 \stemDown fis8 r4 r4 r8 \stemDown b,8 \stemDown
    fis'8 | % 256
    r8 \stemDown b,8 \stemDown e8 r4 r4 r8 \stemUp a,8 \stemUp d8
    \pageBreak | % 257
    r8 \stemDown b8 \stemDown e8 r4 r4 r8 \stemDown a,8 \stemDown e'8 | % 258
    r8 \stemUp a,8 \stemUp d8 r4 r4 \stemDown d4 ( _\pp | % 259
    \stemDown c4 ) \stemDown c2 _\markup{ \italic {cresc. molto} }
    \stemUp as4 ( | \barNumberCheck #260
    \stemUp g4 ) \stemDown c4 ( \stemDown ces4 ) \stemUp es,8 ( \stemUp
    f8 | % 261
    \stemUp ges8 \stemUp es8 ) \stemUp fis8 ( \stemUp gis8 ) \stemUp a8
    ( \stemUp fis8 ) \stemUp a8 ( \stemUp b8 ) | % 262
    \stemUp c8 ( \stemUp a8 ) \stemDown c8 ( \stemDown d8 ) \stemDown es8
    ( \stemDown c8 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 _\ff \stemUp c8 \stemUp a8 \stemUp c8 \stemUp a8 }
    \stemUp c8*2/3 \pageBreak | % 263
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp c8 \stemUp a16 \stemUp c16 \stemUp a16
        \stemUp c16 \stemUp a8 }
    \stemUp c8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp c8 \stemUp a8 \stemUp c8 \stemUp a8 }
    \stemUp c8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp c8 \stemUp a8 \stemUp c8 \stemUp a8 }
    \stemUp c8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp c8 \stemUp a8 \stemUp c8 \stemUp a8 }
    \stemUp c8*2/3 | % 264
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp c8 \stemUp a16 \stemUp c16 \stemUp a16
        \stemUp c16 \stemUp a8 }
    \stemUp c8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp c8 \stemUp a8 \stemUp c8 \stemUp a8 }
    \stemUp c8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp c8 \stemUp a8 \stemUp c8 \stemUp a8 }
    \stemUp c8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown es8 \stemDown c8 \stemDown es8 \stemDown
        c8 }
    \stemDown es8*2/3 | % 265
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown es8 \stemDown c16 \stemDown es16
        \stemDown c16 \stemDown es16 \stemDown c8 }
    \stemDown es8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown es8 \stemDown c8 \stemDown es8 \stemDown
        c8 }
    \stemDown es8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown es8 \stemDown c8 \stemDown es8 \stemDown
        c8 }
    \stemDown es8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown es8 \stemDown c8 \stemDown es8 \stemDown
        c8 }
    \stemDown es8*2/3 | % 266
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown es8 \stemDown c16 \stemDown es16
        \stemDown c16 \stemDown es16 \stemDown c8 }
    \stemDown es8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown es8 \stemDown c8 \stemDown es8 \stemDown
        c8 }
    \stemDown es8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown es8 \stemDown c8 \stemDown es8 \stemDown
        c8 }
    \stemDown es8*2/3 \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown es8 \stemDown c8 \stemDown es8 \stemDown
        c8 }
    \stemDown es8*2/3 | % 267
    \stemDown c8 \stemDown es8 r8 r4 \stemUp c16 ^\markup{ \italic
        {div.} } _\fff \stemUp c16 \stemUp c16 \stemUp c16 \stemUp c16
    \stemUp c16 \stemUp d16 \stemUp d16 \pageBreak | % 268
    \stemUp es2 :16 \stemUp fis16 \stemUp fis16 \stemUp fis16 \stemUp
    fis16 \stemUp fis16 \stemUp fis16 \stemUp gis16 \stemUp gis16 | % 269
    \stemUp a2 :16 \stemUp a8 r8 r4 | \barNumberCheck #270
    \stemDown c,8 ^\markup{ \italic {unis.} } \stemDown es8 \stemDown a8
    r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp a,8 _\fff \stemUp c8 \stemUp a8 \stemUp c8 \stemUp a8 ~
        }
    \stemUp c8*2/3 ~ \stemUp a8 \stemUp c8 \stemUp a8 -> \stemUp c8 r4 | % 271
    R1*2 \pageBreak | % 273
    R1 | % 274
    \stemUp a8 _\ff \stemUp c8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp c8 \stemUp a8 \stemUp c8 \stemUp a8 ~ }
    \stemUp c8*2/3 ~ \stemUp a8 \stemUp c8 \stemUp a8 -> \stemUp c8 r4 | % 275
    r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp c8 \stemUp a8 \stemUp c8 \stemUp a8 }
    \stemUp c8*2/3 r4 r8 \stemUp a8 -> \stemUp c8 | % 276
    r4 \stemUp a8 -> \stemUp c8 r8 r2 | % 277
    \stemUp a2 ( -> _\markup{ \italic {sempre} } _ "" \stemUp gis2 ~ | % 278
    gis1 ) | % 279
    gis1 -> | \barNumberCheck #280
    \stemUp a4. ( -> \stemUp gis8 ) \stemUp gis2 | % 281
    \stemUp fis2 \stemUp eis2 ~ | % 282
    eis1 | % 283
    fis'1 -> | % 284
    \stemDown g4. ( -> \stemDown fis8 ) \stemDown fis4 \stemUp fis'4 --
    _\fff ^\markup{ \italic {div.} } \pageBreak | % 285
    \stemUp e2 _\markup{ \italic {largamente, forte possibile} } \stemUp
    d2 ~ | % 286
    \stemUp d2. \stemUp d4 | % 287
    \stemUp cis2 \stemUp b2 ~ | % 288
    \stemUp b2. \stemUp a4 | % 289
    \stemUp g2 \stemUp fis2 ~ | \barNumberCheck #290
    \stemUp fis2. \stemDown e4 ^\markup{ \italic {unis.} } | % 291
    \stemDown d2 \stemDown cis2 ~ | % 292
    \stemDown cis2. \stemDown cis4 | % 293
    \stemUp b2 \stemUp ais2 ~ | % 294
    ais1 | % 295
    \stemUp g2 \stemUp fis2 ~ | % 296
    fis1 | % 297
    e1 _ "" g1 | % 298
    e1 _ "" | % 299
    d1 ~ _\ffff _\> g1 ~ | \barNumberCheck #300
    \stemUp d2 ~ \stemUp g2 ~ \stemUp d8 _\! _\p \stemUp g8 r8 r4 | % 301
    R1 \break | % 302
    R1*3 \bar "||"
    \pageBreak | % 305
    \key b \major r2 r4 \stemUp cis,8 :32 _\pp \stemUp d8 :32 | % 306
    \stemUp dis8 :32 \stemUp e8 :32 \stemUp eis8 :32 \stemUp fis8 :32
    \stemUp gis8 :32 \stemUp ais8 :32 \stemUp b8 :32 \stemUp cis8 :32 | % 307
    \stemDown d8 :32 _\< \stemDown dis8 :32 \stemDown e8 :32 \stemDown
    eis8 :32 \stemDown fis8 :32 \stemDown gis8 :32 \stemDown ais8 :32
    \stemDown b8 :32 | % 308
    \stemDown cisis8 :32 _\! _\p _\> \stemDown dis8 :32 \stemDown fisis,8
    :32 \stemDown gis8 :32 \stemDown dis8 :32 _\! \stemDown e8 :32
    \stemDown bis8 :32 \stemDown cis8 :32 | % 309
    \stemUp fis,8 :32 _\< \stemUp b8 :32 \stemUp cis8 :32 \stemUp d8 :32
    \stemDown d8 :32 _\! _\mp \stemDown dis8 :32 \stemDown e8 :32
    \stemDown fis8 :32 | \barNumberCheck #310
    \stemDown fisis8 :32 _\markup{ \italic {poco cresc.} } \stemDown gis8
    :32 \stemDown ais8 :32 \stemDown gis8 :32 \stemDown bis,8 :32
    \stemDown cis8 :32 \stemDown dis8 :32 \stemDown e8 :32 \pageBreak | % 311
    \stemDown eis8 :32 \stemDown fis8 :32 \stemDown gis8 :32 \stemDown
    fis8 :32 \stemUp b,2 :32 _\mf _\> | % 312
    \stemUp b2 :32 _\! _\pp _\< \stemDown bis8 :32 _\! _\p _\< \stemDown
    cis8 :32 \stemDown dis8 :32 _\! _\> \stemDown cis8 :32 | % 313
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b16 -. _\! _\p ^\markup{ \italic {div.} } _\< \stemUp
        fis'16 ( \stemUp g16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp gis16 \stemUp a16 \stemUp ais16 ) }
    \stemUp b32 ( \stemUp bis32 \stemUp cis32 \stemUp d32 \stemUp dis32
    \stemUp e32 \stemUp eis32 \stemUp fis32 ) \stemUp fis4 -- _\! _\fff
    \stemUp e8. ( \stemUp dis16 ) | % 314
    \stemUp dis4 ( -> \stemUp cis4 ) \stemUp e4 -- \stemUp dis8. (
    \stemUp cis16 ) | % 315
    \stemUp cis4 ( -> \stemUp b4 ) r8 \stemUp dis8 ( _\> \stemUp cis8 )
    \stemUp b8 -. | % 316
    \stemUp fis8 ( _\! _\mf _\< \stemUp dis8 \stemUp b8 \stemUp dis8 )
    \stemUp gis4.. ( _\! _\ff _\> \stemUp fis16 ) \pageBreak | % 317
    \stemUp fis2 _\! _\mf \stemUp b,4 ( \stemUp ais8. \stemUp a16 ) | % 318
    \stemUp a4 ( -> ^\markup{ \italic {unis.} } \stemUp gis4 ) \stemUp
    ais4 ( \stemUp gis8. \stemUp g16 ) | % 319
    \stemUp g4 ( -> \stemUp fis4 ) \stemDown g2 \stemDown g'2 |
    \barNumberCheck #320
    \stemUp fis,2 r8 \stemUp b8 ( \stemUp a8 \stemUp ais8 | % 321
    \stemUp b8 ) _\mf r8 r4 \stemUp b4 ( \stemUp ais8. \stemUp a16 ) | % 322
    \stemUp a4 ( -> \stemUp gis4 ) \stemUp ais4 ( \stemUp gis8. \stemUp
    g16 ) | % 323
    \stemUp g4 ( -> \stemUp fis4 ) r8 \stemDown d'8 ( _\f _\> \stemDown
    cis8 ) \stemDown b8 -- | % 324
    \stemUp fis2 _\! _\mf \stemUp g4.. ( _\> \stemUp fis16 ) | % 325
    \stemUp fis2 ~ _\! _\p _\> \stemUp fis8 _\! _\pp r8 r4 \break | % 326
    R1*8 \pageBreak | % 334
    R1 \bar "||"
    r4 \stemUp b8 _\p ^\markup{ \italic {pizz.} } r8 \stemUp ais8 r8
    \stemUp gis8 r8 | % 336
    \stemUp fis8 r8 \stemUp e8 r8 \stemUp dis8 r8 \stemUp cis8 r8 | % 337
    r4 \stemUp b'8 r8 \stemUp ais8 r8 \stemUp gis8 r8 | % 338
    \stemUp fis8 r8 \stemUp e8 r8 \stemUp dis8 r8 \stemUp cis8 r8 | % 339
    r4 \stemUp b'8 r8 \stemUp ais8 r8 \stemUp gis8 r8 | \barNumberCheck
    #340
    \stemUp fis8 r8 \stemUp e8 r8 \stemUp dis8 r8 \stemUp cis8 r8 | % 341
    r4 \stemUp b'8 r8 \stemUp ais8 r8 \stemUp gis8 r8 | % 342
    \stemUp fis8 r8 \stemUp e8 r8 \stemUp dis8 r8 \stemUp cis8 r8
    \pageBreak | % 343
    r4 \stemUp b'8 r8 \stemUp ais8 r8 \stemUp gis8 r8 | % 344
    \stemUp fis8 r8 \stemUp e8 r8 \stemUp dis8 r8 \stemUp cis8 r8 | % 345
    r4 \stemUp b'8 _\> r8 \stemUp ais8 r8 \stemUp gis8 r8 | % 346
    \stemUp fis8 _\! _\pp r8 \stemUp e8 r8 \stemUp dis8 r8 \stemUp cis8
    r8 | % 347
    R1*8 \bar "|."
    }

PartPOneFiveVoiceFive =  \relative e {
    \clef "alto" \time 4/4 \key d \major | % 1
    R1*3 | % 4
    e1 _\mp _\< | % 5
    dis1 ~ _\! _\sf _\> | % 6
    \stemUp dis8 _\! _\p r8 r4 r2 | % 7
    R1*3 | \barNumberCheck #10
    d1 _\mp _\< | % 11
    \stemUp d2 ( _\! _\sf _\> \stemUp cis2 ~ \break | % 12
    \stemUp cis8 ) _\! _\p r8 r4 r2 | % 13
    R1*4 | % 17
    fis1 ~ _\mf _\> | % 18
    \stemUp fis2 ~ \stemUp fis8 _\! _\pp r8 r4 ^\fermata \bar "||"
    r2 r4 \stemDown fis'8 ( -. _\p _\< \stemDown g8 ) -. |
    \barNumberCheck #20
    \stemDown gis4 ( _\! _\> \stemDown ais8 ) r8 _\! r4 \stemDown fis16
    ( _\p _\< \stemDown g16 \stemDown fis16 \stemDown g16 ) | % 21
    \stemDown gis4 ( _\! _\> \stemDown ais8 ) r8 _\! r4 r8 _\p \stemDown
    ais8 | % 22
    r8 \stemDown b8 r8 \stemDown e,8 r8 \stemDown fis8 r8 \stemUp ais,8
    | % 23
    r8 \stemUp b8 r8 \stemUp e,8 ( \stemUp fis8 ) r8 r4 \pageBreak | % 24
    R1*3 | % 27
    r2 r4 r8 \stemDown e'8 ~ _\p | % 28
    \stemDown e8 r8 r4 r2 | % 29
    R1 | \barNumberCheck #30
    \time 2/4  R2 \break | % 31
    \time 4/4  R1 | % 32
    r2 r4 \stemUp g,4 -- _\pp _\< | % 33
    \stemUp a4 ( _\! _\> \stemUp bes8 ) _\! r8 r4 \stemUp g8 ( -. _\<
    \stemUp gis8 ) -. | % 34
    \stemUp a4 ( _\! _\> \stemUp bes8 ) _\! r8 r4 \stemUp f16 -. _\p
    \stemUp f16 -. \stemUp f16 -. \stemUp f16 -. | % 35
    \stemUp f16 -. \stemUp f16 -. \stemUp f16 -. \stemUp f16 -. \stemUp
    f16 -. \stemUp f16 -. \stemUp f16 -. \stemUp f16 -. \stemUp f16 -.
    \stemUp f16 -. \stemUp f16 -. \stemUp f16 -. \stemUp gis16 -. _\<
    \stemUp gis16 -. \stemUp gis16 -. \stemUp gis16 -. | % 36
    \stemUp gis16 -. \stemUp gis16 -. \stemUp gis16 -. \stemUp gis16 -.
    \stemUp gis16 -. \stemUp gis16 -. \stemUp gis16 -. \stemUp gis16 -.
    \stemUp gis16 -. \stemUp gis16 -. \stemUp gis16 -. \stemUp gis16 -.
    \stemUp b16 -. _\! _\mp _\< \stemUp b16 -. \stemUp b16 -. \stemUp b16
    -. \break | % 37
    \stemUp b8 _\! _\markup{ \italic {cresc.} } r8 \stemDown b'8 r8
    \stemDown fis8 r8 \stemDown fis8 r8 | % 38
    \stemDown fis'8 _\mf r8 r4 r2 | % 39
    R1 | \barNumberCheck #40
    r2 \stemDown cis,2 ~ -> _\mf | % 41
    \stemUp cis16 \stemUp cis16 -. \stemUp b16 -. \stemUp a16 -. \stemUp
    g16 -. _\> \stemUp fis16 -. \stemUp e16 -. \stemUp d16 -. \stemUp
    cis2 ~ _\! _\p | % 42
    \stemUp cis16 \stemUp d16 ( \stemUp cis16 \stemUp d16 \stemUp cis16
    \stemUp d16 \stemUp cis16 \stemUp d16 \stemUp cis8 ) \stemUp e16 (
    -. ^\markup{ \italic {saltando} } _\pp \stemUp e16 ) -. \stemUp d8 (
    -. \stemUp g8 -. | % 43
    \stemUp fis8 ) -. \stemUp a16 ( -. \stemUp a16 ) -. \stemUp d8 ( -.
    \stemUp fis,8 -. \stemUp b8 ) -. \stemUp d,16 ( -. \stemUp d16 ) -.
    \stemUp g8 ( -. \stemUp cis,8 ) -. \pageBreak | % 44
    R1*6 \break | \barNumberCheck #50
    R1*4 \pageBreak | % 54
    R1*5 \break | % 59
    R1*5 \pageBreak | % 64
    R1*5 \pageBreak | % 69
    R1*5 \pageBreak | % 74
    R1*4 \break | % 78
    R1*5 \pageBreak | % 83
    R1*6 \bar "||"
    R1*5 \break | % 94
    R1*7 \bar "||"
    R1*2 \pageBreak | % 103
    R1*5 \break | % 108
    R1*4 \pageBreak | % 112
    R1*4 \break | % 116
    R1*4 \pageBreak | \barNumberCheck #120
    R1*5 \break | % 125
    R1*5 \bar "||"
    R1*2 \pageBreak | % 132
    R1*6 \pageBreak | % 138
    R1*4 \bar "||"
    R1*3 \break | % 145
    R1*11 \pageBreak | % 156
    R1*5 \bar "||"
    \key c \major R1*4 \pageBreak | % 165
    R1*7 \pageBreak | % 172
    R1*6 \pageBreak | % 178
    R1*5 \break | % 183
    R1*5 \pageBreak | % 188
    R1*4 \break | % 192
    R1*4 \pageBreak | % 196
    R1*5 \break | % 201
    R1*4 s1*1/640 R1*2 \pageBreak | % 207
    R1*6 \pageBreak | % 213
    R1*4 \break | % 217
    R1*4 \pageBreak | % 221
    R1*5 \break | % 226
    R1*5 \break | % 231
    R1*6 \pageBreak | % 237
    R1*5 \pageBreak | % 242
    R1*4 \pageBreak | % 246
    R1*6 \break | % 252
    R1*5 \pageBreak | % 257
    R1*6 \pageBreak | % 263
    R1*5 \pageBreak | % 268
    R1*5 \pageBreak | % 273
    R1*12 \pageBreak | % 285
    R1*17 \break | % 302
    R1*3 \bar "||"
    \pageBreak | % 305
    \key b \major R1*6 \pageBreak | % 311
    R1*6 \pageBreak | % 317
    R1*9 \break | % 326
    R1*8 \pageBreak | % 334
    R1 \bar "||"
    R1*8 \pageBreak | % 343
    R1*12 \bar "|."
    }

PartPOneFiveVoiceTwo =  \relative fis {
    \clef "alto" \time 4/4 \key d \major s1*11 \break s1*7 \bar "||"
    s1*5 \pageBreak s1*6 | \barNumberCheck #30
    \time 2/4  s2 \break | % 31
    \time 4/4  s1*6 \break s1*7 \pageBreak s1*6 \break s1*4 \pageBreak
    s1*5 \break s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*4
    \break s1*5 \pageBreak s1*6 \bar "||"
    s1*5 \break s1*7 \bar "||"
    s1*2 \pageBreak s1*5 \break s1*4 \pageBreak s1*4 \break s1*4
    \pageBreak s1*5 \break s1*5 \bar "||"
    s1*2 \pageBreak s1*6 \pageBreak s1*4 \bar "||"
    s1*3 \break s1*9 | % 154
    \stemDown fis2 \stemDown eis2 | % 155
    \stemDown fis2 ~ \stemDown fis8 s4. \pageBreak | % 156
    \stemDown d2 \stemDown e2 | % 157
    \stemDown fis2 ~ \stemDown fis8 s4. | % 158
    \stemDown d2 ~ \stemDown d8 s4. | % 159
    \stemDown d2 ~ \stemDown d8 s4. | \barNumberCheck #160
    r4 \stemDown d8 ^\markup{ \italic {pizz.} } r8 r2 _\fermata \bar
    "||"
    \key c \major s1*4 \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*5
    \break s1*5 \pageBreak s1*4 \break s1*4 \pageBreak s1*5 \break s1*6
    \pageBreak s1*6 \pageBreak s1*4 \break s1*4 \pageBreak s1*5 \break
    s1*5 \break s1*6 \pageBreak s1*5 \pageBreak s1*4 \pageBreak s1*6
    \break s1*5 \pageBreak s1*6 \pageBreak s2*9 \stemDown c16 \stemDown
    c16 \stemDown c16 \stemDown c16 \stemDown c16 \stemDown c16
    \stemDown d16 \stemDown d16 \pageBreak | % 268
    \stemDown es2 :16 \stemDown fis16 \stemDown fis16 \stemDown fis16
    \stemDown fis16 \stemDown fis16 \stemDown fis16 \stemDown gis16
    \stemDown gis16 | % 269
    \stemDown a2 :16 \stemDown a8 s8*27 \pageBreak s4*47 \stemDown fis'4
    -- \pageBreak | % 285
    \stemDown e2 \stemDown d2 ~ | % 286
    \stemDown d2. \stemDown d4 | % 287
    \stemDown cis2 \stemDown b2 ~ | % 288
    \stemDown b2. \stemDown a4 | % 289
    \stemDown g2 \stemDown fis2 ~ | \barNumberCheck #290
    \stemDown fis2. s4*45 \break s1*3 \bar "||"
    \pageBreak | % 305
    \key b \major s1*6 \pageBreak s1*2 | % 313
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown b16 -. \stemDown fis16 ( \stemDown g16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown gis16 \stemDown a16 \stemDown ais16 ) }
    \stemDown b32 \stemDown bis32 \stemDown cis32 \stemDown d32
    \stemDown dis32 \stemDown e32 \stemDown eis32 \stemDown fis32
    \stemDown fis4 \stemDown e8. \stemDown dis16 | % 314
    \stemDown dis4 ( -> \stemDown cis4 ) \stemDown e4 -- \stemDown dis8.
    ( \stemDown cis16 ) | % 315
    \stemDown cis4 \stemDown b4 s8 \stemDown dis8 ( \stemDown cis8 )
    \stemDown b8 -. | % 316
    \stemDown fis8 ( \stemDown dis8 \stemDown b'8 \stemDown dis,8 )
    \stemDown gis4.. ( \stemDown fis16 ) \pageBreak | % 317
    \stemDown fis2 \stemDown b4 ( \stemDown ais8. \stemDown a16 ) s1*8
    \break s1*8 \pageBreak s1 \bar "||"
    s1*8 \pageBreak s1*12 \bar "|."
    }

PartPOneSixVoiceOne =  \relative d' {
    \clef "bass" \time 4/4 \key d \major | % 1
    R1*11 \break | % 12
    R1*7 _\markup{ \italic {div.} } \bar "||"
    r2 r4 \stemDown d8 ( -. _\p _\< \stemDown cis8 ) -. |
    \barNumberCheck #20
    \stemDown b4 ( _\! _\> \stemDown ais8 ) r8 _\! r4 \stemDown b4 ( ~
    _\p _\< | % 21
    \stemDown b4 _\! _\> \stemDown ais8 ) r8 _\! r4 r8 \stemDown g'8 _\p
    | % 22
    r8 \stemDown fis8 r8 \stemDown cis8 r8 \stemDown d8 r8 \stemDown g,8
    | % 23
    r8 \stemDown fis8 r8 \stemUp b,8 ( \stemUp cis8 ) r8 r4 \pageBreak | % 24
    R1*3 | % 27
    r2 r4 r8 \stemDown g'8 ~ _\p | % 28
    \stemDown g8 r8 r4 r4 \stemDown e'16 ( \stemDown d16 ) \stemDown cis16
    -. \stemDown b16 -. | % 29
    \stemDown a16 -. \stemDown g16 -. \stemDown fis16 -. \stemDown e16
    -. \stemDown d16 ( _\> \stemDown cis16 ) \stemDown e16 -. \stemDown
    d16 -. \stemUp cis16 ( _\! _\pp \stemUp d16 ) \stemUp cis16 -.
    \stemUp b16 -. \stemUp b16 -. \stemUp b16 -. \stemUp b16 -. \stemUp
    b16 -. | \barNumberCheck #30
    \time 2/4  \stemUp b16 -. \stemUp b16 -. \stemUp b16 -. \stemUp b16
    -. \stemUp b16 -. \stemUp b16 -. \stemUp b16 -. \stemUp b16 -.
    \break | % 31
    \time 4/4  \stemUp b16 -. \stemUp b16 -. \stemUp b16 -. \stemUp b16
    -. \stemUp b16 ( _\< \stemUp ais16 ) \stemUp b16 -. \stemUp cis16 -.
    \stemUp e16 ( _\! _\> \stemUp d16 ) \stemUp cis16 -. \stemUp b16 -.
    \stemUp b16 -. _\! \stemUp b16 -. \stemUp b16 -. \stemUp b16 -. | % 32
    \stemUp b16 -. \stemUp b16 -. \stemUp b16 -. \stemUp b16 -. \stemUp
    b16 ( _\< \stemUp ais16 ) \stemUp b16 -. \stemUp cis16 -. \stemUp e16
    ( _\! _\> \stemUp d16 ) \stemUp cis16 -. \stemUp b16 -. \stemUp bes4
    _- _\! _\< | % 33
    \stemUp a4 ( _\! _\> \stemUp g8 ) r8 _\! r4 \stemUp b8 ( -. _\<
    \stemUp bes8 ) -. | % 34
    \stemUp a4 ( _\! _\> \stemUp g8 ) r8 _\! r2 | % 35
    R1*2 \break | % 37
    R1*3 | \barNumberCheck #40
    r2 \stemUp e2 _\mf | % 41
    \stemUp fis2 _\> \stemUp g2 ( _\! _\p | % 42
    \stemUp a16 ) \stemUp b16 ( \stemUp a16 \stemUp b16 \stemUp a16
    \stemUp b16 \stemUp a16 \stemUp b16 \stemDown a8 ) \stemDown g'8 (
    _\pp \stemDown fis8 \stemDown e8 | % 43
    \stemDown d8 ) \stemDown e16 ( -. _\markup{ \italic {saltando} }
    \stemDown e16 ) -. \stemDown fis8 ( -. \stemDown cis8 -. \stemUp d8
    ) -. \stemUp a16 ( -. \stemUp a16 ) -. \stemUp b8 ( -. \stemUp e8 )
    -. \pageBreak | % 44
    \stemDown d2 ~ \stemDown d8 \stemDown d16 ( -. \stemDown d16 ) -.
    \stemUp cis8 ( -. \stemUp b8 -. | % 45
    \stemUp a8 ) -. \stemUp fis'16 ( -. \stemUp fis16 ) -. \stemUp cis8
    ( -. \stemUp d8 -. \stemUp a8 ) -. \stemUp b16 ( -. \stemUp b16 ) -.
    \stemUp fis8 ( -. \stemUp eis8 ) -. | % 46
    \stemUp fis2 ~ \stemDown fis8 \stemDown d''8 ( _\p \stemDown cis8
    \stemDown b8 | % 47
    \stemDown a8 ) \stemDown b16 ( -. \stemDown b16 ) -. \stemDown cis8
    ( -. \stemDown gis8 -. \stemDown a8 ) -. \stemDown e16 ( -.
    \stemDown e16 ) -. \stemDown fis8 ( -. \stemDown b8 ) -. | % 48
    \stemDown a2 ~ \stemDown a8 r8 r4 | % 49
    r2 r4 r8 \stemDown bis8 _\p \break | \barNumberCheck #50
    \stemDown cis2 ~ ^\markup{ \italic {unis.} } \stemDown cis8
    \stemDown gis,8 _\mp r4 | % 51
    \stemDown gis'2 ~ _\mp \stemDown gis16 \stemDown cis16 -. \stemDown
    cis16 -. \stemDown cis16 -. \stemDown cis16 ( \stemDown e16 )
    \stemDown dis16 -. \stemDown cis16 -. | % 52
    \stemDown bis16 ( \stemDown cis16 ) \stemDown bis16 -. \stemDown a16
    -. \stemDown gis16 ( \stemDown a16 ) \stemDown gis16 -. \stemDown
    gis,16 -. \stemUp gis8 -. \stemUp gis8 -. r4 | % 53
    \stemDown gis'2 ~ _\mp \stemDown gis16 \stemDown cis16 -. \stemDown
    cis16 -. \stemDown cis16 -. \stemDown cis16 ( \stemDown e16 )
    \stemDown dis16 -. \stemDown cis16 -. \pageBreak | % 54
    \stemDown bis16 ( \stemDown cis16 ) \stemDown bis16 -. \stemDown a16
    -. \stemDown gis16 ( \stemDown a16 ) \stemDown gis16 -. \stemDown
    gis,16 -. \stemUp gis8 -. r8 r4 | % 55
    r16 \stemDown b'16 -. _\pp _\< \stemDown b16 -. \stemDown b16 -.
    \stemDown b16 -. \stemDown b16 -. \stemDown b16 -. \stemDown b16 -.
    \stemDown fis8 ( -- _\! _\> \stemDown fis8 ) -- \stemDown fis8 -- r8
    _\! | % 56
    r16 \stemDown gis16 -. _\pp _\< \stemDown gis16 -. \stemDown gis16
    -. \stemDown gis16 -. \stemDown gis16 -. \stemDown gis16 -.
    \stemDown gis16 -. \stemUp b,8 ( -- _\! _\> \stemUp b8 ) -- \stemUp
    b8 -- r8 _\! | % 57
    r16 \stemDown dis'16 -. _\p _\< \stemDown dis16 -. \stemDown dis16
    -. \stemDown dis16 -. \stemDown dis16 -. \stemDown dis16 -.
    \stemDown dis16 -. \stemDown ais8 ( -- _\! _\> \stemDown ais8 ) --
    \stemDown ais8 -- r8 _\! | % 58
    r16 \clef "tenor" \stemDown gis'16 -. _\p _\< \stemDown gis16 -.
    \stemDown gis16 -. \stemDown gis16 ( \stemDown fis16 ) \stemDown e16
    -. \stemDown dis16 -. \stemDown cis8 ( -- _\! _\> \stemDown ais8 )
    -- \stemDown b8 -- r8 _\! \break | % 59
    \clef "bass" \stemDown dis,2 ~ _\mp \stemUp dis16 \stemUp b16 -.
    \stemUp b16 -. \stemUp b16 -. \stemUp b16 -. \stemUp b16 -. \stemUp
    b16 -. \stemUp b16 -. | \barNumberCheck #60
    \stemUp ais16 -. \stemUp ais16 -. \stemUp ais16 -. \stemUp fisis16
    -. \stemUp fisis16 -. \stemUp fisis16 -. \stemUp fisis16 -. \stemUp
    cis'16 -. \stemUp b8 -. \stemUp dis,8 -. r4 | % 61
    \stemDown dis'2 ~ _\mp \stemUp dis16 \stemUp b16 -. \stemUp b16 -.
    \stemUp b16 -. \stemUp b16 -. \stemUp b16 -. \stemUp b16 -. \stemUp
    b16 -. | % 62
    \stemUp ais16 -. \stemUp ais16 -. \stemUp ais16 -. \stemUp fisis16
    -. \stemUp fisis16 -. \stemUp fisis16 -. \stemUp fisis16 -. \stemUp
    cis'16 -. \stemUp b8 -. \stemUp dis,8 -. r4 | % 63
    r16 \stemDown e'16 -. _\p _\< \stemDown e16 -. \stemDown e16 -.
    \stemDown e16 -. \stemDown e16 -. \stemDown e16 -. \stemDown e16 -.
    \stemDown e8 ( -- _\! _\> \stemDown e8 ) -- \stemDown e8 -- r8 _\!
    \pageBreak | % 64
    r16 \stemUp b16 -. _\p _\< \stemUp b16 -. \stemUp b16 -. \stemUp b16
    -. \stemUp b16 -. \stemUp b16 -. \stemUp b16 -. \stemUp b8 ( -- _\!
    _\> \stemUp b8 ) -- \stemUp b8 -- r8 _\! | % 65
    r16 \stemDown ais'16 -. _\mp _\< \stemDown ais16 -. \stemDown ais16
    -. \stemDown ais16 -. \stemDown ais16 -. \stemDown ais16 -.
    \stemDown ais16 -. \stemDown gis8 ( -- _\! _\> \stemDown gis8 ) --
    \stemDown gis8 -- r8 _\! | % 66
    r16 \stemDown fis16 -. _\mp _\< \stemDown fis16 -. \stemDown fis16
    -. \stemDown fis16 -. \stemDown fis16 -. \stemDown fis16 -.
    \stemDown fis16 -. \stemUp ais,4 ~ _\! _\> \stemUp ais8 r8 _\! | % 67
    r16 \stemUp b16 -. _\f \stemUp b16 -. \stemUp b16 -. \stemUp b16 (
    \stemUp gis16 ) \stemUp ais16 -. \stemUp b16 -. \stemUp ais8 -. r8 r4
    | % 68
    R1 \pageBreak | % 69
    r16 \stemDown d16 -. _\ff \stemDown d16 -. \stemDown d16 -. \stemUp
    d16 ( \stemUp b16 ) \stemUp cis16 -. \stemUp d16 -. \stemUp cis8 -.
    r8 r4 | \barNumberCheck #70
    r2 \stemDown <e a>4 ~ ~ _\ff \stemDown <e a>8 r8 | % 71
    r2 \stemDown <e a>4 ~ ~ \stemDown <e a>8 r8 | % 72
    r2 \stemDown <f a>4 ~ ~ \stemDown <f a>8 r8 | % 73
    \stemDown e4 ~ \stemDown e8 r8 \stemDown <f a>4 ~ ~ \stemDown <f a>8
    r8 \pageBreak | % 74
    \stemDown e4 ~ \stemDown e8 r8 \stemDown f4 ( -> \stemDown e8 ) r8 | % 75
    \stemDown f4 ( -> \stemDown e8 ) r8 \stemDown e4 ( -> \stemDown es8
    ) r8 | % 76
    \stemDown e4 ( -> \stemDown es8 ) r8 \stemDown <e a>4 ( -> ~ _\f
    \stemDown <es a>8 ) r8 | % 77
    \stemDown <e a>4 ( -> ~ \stemDown <es a>8 ) r8 \stemUp a,4 ~ -> _\mf
    \stemUp a8 r8 \break | % 78
    \stemUp a4 ~ -> \stemUp a8 r8 r4 \stemUp a4 ~ _\mp | % 79
    \stemUp a4 ~ \stemUp a8 r8 r2 | \barNumberCheck #80
    r2 r16 \stemUp a16 _\pp \stemUp a16 \stemUp a16 \stemUp a16 \stemUp
    cis16 \stemUp b16 \stemUp a16 | % 81
    \stemUp a16 \stemUp cis16 \stemUp b16 \stemUp a16 \stemUp a16
    \stemUp cis16 \stemUp b16 \stemUp a16 \stemUp a16 \stemUp cis16
    \stemUp b16 \stemUp a16 \stemUp a16 \stemUp cis16 \stemUp b16
    \stemUp a16 | % 82
    \stemUp a16 ( \stemUp cis16 ) \stemUp b16 \stemUp a16 \stemUp a16 (
    \stemUp cis16 ) \stemUp b16 \stemUp a16 \stemUp a16 ( \stemUp d16 )
    \stemUp b16 \stemUp a16 \stemUp a16 ( \stemUp d16 ) \stemUp b16
    \stemUp a16 \pageBreak | % 83
    \stemUp a16 ( \stemUp d16 \stemUp b16 \stemUp a16 ) \stemUp a16 (
    \stemUp d16 \stemUp b16 \stemUp a16 ) \stemUp a16 ( \stemUp d16
    \stemUp b16 \stemUp a16 ) \stemUp a16 ( \stemUp d16 \stemUp b16
    \stemUp a16 ) | % 84
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ( \stemUp d8 \stemUp b8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp d8 \stemUp b8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ) \stemUp d8 ( \stemUp b8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp d8 \stemUp b8 }
    | % 85
    \stemUp a8 ) \stemUp d8 ( \stemUp b8 \stemUp a8 \stemUp d8 \stemUp b8
    \stemUp a8 \stemUp d8 | % 86
    \stemDown fis8 ) r8 r4 r2 | % 87
    R1*2 \bar "||"
    r2 r8 \clef "tenor" \stemDown fis'8 ( _\p ^\markup{ \italic {con
            sordini} } ^ "," ^\markup{ \italic {teneramente, molto
            cantabile, con espansione} } \stemDown e8 \stemDown d8 ) |
    \barNumberCheck #90
    \stemUp b8 ( _\< \stemUp a8 \stemUp fis8 \stemUp a8 ) \stemDown d4.
    ( _\! _\> \stemDown b8 ) | % 91
    \stemDown a2 ~ _\! \stemDown a8 \stemDown fis'8 ( \stemDown e8
    \stemDown d8 ) | % 92
    \stemUp a8 ( _\< \stemUp fis8 \stemUp d8 \stemUp fis8 ) \stemDown b4.
    ( _\! _\> \stemDown a8 ) | % 93
    \stemDown a2 _\! _\< \stemDown a'4 -- _\! _\f \stemDown g8 (
    \stemDown fis8 ) \break | % 94
    \stemDown fis4 ( -> \stemDown e4 ) \stemDown g4 -- _\> \stemDown fis8
    ( \stemDown e8 ) | % 95
    \stemDown e4 ( -> _\! _\mf _\< \stemDown d4 ) r8 _\! \stemDown fis8
    ( _\f _\> \stemDown e8 \stemDown d8 ) | % 96
    \stemUp a8 ( _\! _\< \stemUp fis8 \stemUp d8 \stemUp fis8 )
    \stemDown b4. ( _\! _\> \stemDown a8 ) | % 97
    \stemDown a2 _\! _\< \stemDown a'4 -- _\! _\f \stemDown g8 (
    \stemDown fis8 ) | % 98
    \stemDown fis4 ( -> \stemDown e4 ) \stemDown g4 -- _\> \stemDown fis8
    ( \stemDown e8 ) | % 99
    \stemDown e4 ( -> _\! _\mf _\< \stemDown d4 ) r8 _\! \stemDown fis8
    ( _\f _\> \stemDown e8 \stemDown d8 ) | \barNumberCheck #100
    \stemUp a8 ( _\! _\< \stemUp fis8 \stemUp d8 \stemUp fis8 )
    \stemDown b4. ( _\! _\> \stemDown a8 ) \bar "||"
    \stemDown a8 _\! _\p r8 r4 r2 | % 102
    \clef "bass" \stemDown d,8 ^\markup{ \italic {pizz.} } r8 r4 r2
    \pageBreak | % 103
    d1 ( ^\markup{ \italic {arco} } | % 104
    cis1 ) _\< | % 105
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp c16 ( _\! _\mp \stemUp d16 \stemUp c16 \stemUp d16
        \stemUp c16 \stemUp d16 }
    \once \omit TupletBracket
    \times 4/7  {
        \stemUp c16*161/160 \stemUp d16*161/160 \stemUp c16*161/160
        \stemUp d16*161/160 \stemUp c16*161/160 \stemUp b16*161/160
        \stemUp c16*161/160 }
    \stemDown cis8 ) -. \stemDown cis'8 -. r4 | % 106
    \stemUp b,8 _\p ^\markup{ \italic {pizz.} } r8 r4 r2 | % 107
    \stemUp e,8 _\mf r8 r4 r2 \break | % 108
    \stemUp a8 r8 r4 r2 | % 109
    \stemUp a8 _\p r8 r4 \stemDown e'8 r8 r4 | \barNumberCheck #110
    \stemUp a,8 r8 r4 r2 | % 111
    a1 ( ^\markup{ \italic {arco} } \pageBreak | % 112
    gis1 ) _\< | % 113
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp g16 ( _\! _\mp \stemUp a16 \stemUp g16 \stemUp a16
        \stemUp g16 \stemUp a16 }
    \once \omit TupletBracket
    \times 4/7  {
        \stemUp g16*161/160 \stemUp a16*161/160 \stemUp g16*161/160
        \stemUp a16*161/160 \stemUp g16*161/160 \stemUp fis16*161/160
        \stemUp g16*161/160 ) }
    \stemUp gis8 -. \stemUp gis'8 -. r4 | % 114
    \stemUp cis,8 -. _\markup{ \italic {poco cresc.} } \stemUp cis16 (
    -. \stemUp cis16 ) -. \stemUp cis8 ( -. \stemUp cis8 -. \stemUp cis8
    ) -. \stemUp cis16 ( -. \stemUp cis16 ) -. \stemUp cis8 ( -. \stemUp
    cis8 -. | % 115
    \stemUp b8 ) -. _\mf \stemUp b16 ( -. \stemUp b16 ) -. \stemUp b8 (
    -. \stemUp b8 -. \stemUp b8 ) -. \stemUp b16 ( -. \stemUp b16 ) -.
    \stemUp b8 ( -. \stemUp b8 -. \break | % 116
    \stemUp b8 ) -. _\markup{ \italic {dim.} } \stemUp b16 ( -. \stemUp
    b16 ) -. \stemUp b8 ( -. \stemUp b8 -. \stemUp b8 ) -. \stemUp b16 (
    -. \stemUp b16 ) -. \stemUp b8 ( -. \stemUp b8 -. | % 117
    \stemDown e8 ) -. _\p r8 r4 r2 | % 118
    \stemUp e,8 ^\markup{ \italic {pizz.} } r8 r4 \stemDown e'8 r8 r4 | % 119
    d1 ( _\markup{ \italic {cresc.} } ^\markup{ \italic {arco} }
    \pageBreak | \barNumberCheck #120
    cis1 ) | % 121
    \stemUp b2. _\mf \stemUp b4 | % 122
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp a16 ( _\markup{ \italic {poco cresc.} } \stemUp b16
        \stemUp a16 \stemUp b16 \stemUp a16 \stemUp gis16 ) }
    \stemUp a2 \stemUp a4 | % 123
    \stemUp g2. _\< \stemUp g4 | % 124
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp fis16 ( _\! _\f \stemUp g16 \stemUp fis16 \stemUp g16
        \stemUp fis16 \stemUp eis16 ) }
    \stemUp fis2 \stemUp fis4 \break | % 125
    f1 _\< | % 126
    e1 _\! _\ff | % 127
    R1*3 ^\markup{ \italic {alzate sordini} } \bar "||"
    \time 12/8  r8*2/3 ^\markup{ \italic {senza sordini} } \stemUp a8
    _\p \stemUp d8 \stemUp a8 \stemUp d8 \stemUp a8 \stemUp d8 \stemUp a8
    \stemUp d8 \stemUp a8 \stemUp d8 \stemUp a4. ~ \stemUp d4. ~ \stemUp
    a8 \stemUp d8 r8*2/3 r8*2/3 | % 131
    r8*2/3 \stemUp a8 _\markup{ \italic {sempre} } _ "" \stemUp d8
    \stemUp a8 \stemUp d8 \stemUp a8 \stemUp d8 \stemUp a8 \stemUp d8
    \stemUp a8 \stemUp d8 r8*2/3 \stemUp gis,8 \stemUp d'8 \stemUp gis,8
    \stemUp d'8 \stemUp gis,8 \stemUp d'8 \stemUp gis,8 \stemUp d'8
    \stemUp gis,8 \stemUp d'8 \pageBreak | % 132
    r8*2/3 \stemUp a8 \stemUp d8 \stemUp a8 \stemUp d8 \stemUp a8
    \stemUp d8 \stemUp a8 \stemUp d8 \stemUp a8 \stemUp d8 \stemUp a8
    \stemUp d8 r8*2/3 r8*2/3 r4*2/3 r8*2/3 | % 133
    r8*2/3 \stemUp a8 \stemUp d8 \stemUp a8 \stemUp d8 \stemUp a8
    \stemUp d8 \stemUp a8 \stemUp d8 \stemUp a8 \stemUp d8 r8*2/3
    \stemUp a8 \stemUp a8 \stemUp a8 \stemUp a8 \stemUp a8 | % 134
    r8*2/3 \stemUp a8 _\p _\< \stemUp d8 \stemUp a8 \stemUp d8 \stemUp a8
    \stemUp d8 \stemUp a8 \stemUp d8 r8*2/3 _\! \stemUp a2. _\mf | % 135
    \stemUp b8 \stemUp b8 \stemUp b8 \stemUp b8 \stemUp b8 \stemUp b8
    \stemUp g2. | % 136
    \stemUp a8 _\< \stemUp a8 \stemUp a8 \stemUp a8 \stemUp a8 \stemUp a8
    \stemUp gis2. _\! _\sf _\> | % 137
    \stemUp a8 _\! _\p _\< \stemUp d8 \stemUp a8 \stemUp d8 \stemUp a8
    \stemUp d8 \stemUp a8 \stemUp d8 \stemUp a8 \stemUp d8 \stemUp a8
    \stemUp d8 \stemUp a2. _\! _\mf _\> \pageBreak | % 138
    r8*2/3 _\! \stemUp a8 _\p _\< \stemUp d8 \stemUp a8 \stemUp d8
    \stemUp a8 \stemUp d8 \stemUp a8 \stemUp d8 r8*2/3 _\! \stemUp a2.
    _\mf | % 139
    \stemUp b8 \stemUp b8 \stemUp b8 \stemUp b8 \stemUp b8 \stemUp b8
    \stemUp g2. | \barNumberCheck #140
    \stemUp a8 _\< \stemUp a8 \stemUp a8 \stemUp a8 \stemUp a8 \stemUp a8
    \stemUp gis2. _\! _\sf _\> | % 141
    \stemUp a8 _\! _\p _\< \stemUp d8 \stemUp a8 \stemUp d8 \stemUp a8
    \stemUp d8 \stemUp a8 \stemUp d8 \stemUp a8 \stemUp d8 \stemUp a8
    \stemUp d8 \stemUp a2. _\! _\mf _\> \bar "||"
    r8*2/3 _\! \stemDown d8 _\mf _\> \stemDown d8 \stemDown d8 \stemDown
    d8 \stemDown d8 \stemUp a2. ( _\! _\mp | % 143
    \numericTimeSignature\time 4/4  \stemUp b2 ) \stemUp g2 ( | % 144
    \stemUp a2 ) _\> \stemUp a2 ( _\! _\p \break | % 145
    \stemUp b2 ) \stemUp g2 ( | % 146
    \stemUp a2 ) \stemUp a2 ( | % 147
    \stemUp b2 ) \stemUp g2 ( | % 148
    \stemUp a2 ) _\> \stemUp a2 ( _\! _\pp | % 149
    \stemUp b2 ) \stemUp g2 ( | \barNumberCheck #150
    \stemUp a2 ) \stemUp bes2 ( _\markup{ \italic {dim.} } | % 151
    \stemUp a2 ) \stemUp bes2 ( | % 152
    \stemUp a2 ) _\ppp \stemUp a2 ~ | % 153
    \stemUp a2 r2 | % 154
    \stemUp a2 ^\markup{ \italic {divisi} } _\ppp _\< \stemUp d2 \stemUp
    gis,2 _\! _\p _\> \stemUp d'2 | % 155
    \stemUp a2 ~ _\! _\ppp \stemUp d2 ~ \stemUp a8 \stemUp d8 r8 r4
    \pageBreak | % 156
    \stemUp a2 _\ppp _\< \stemUp a2 _\! _\p _\> | % 157
    \stemUp a2 ~ _\! \stemUp d2 ~ \stemUp a8 \stemUp d8 r8 r4 | % 158
    \stemUp a2 ~ _\pppp \stemUp a8 r8 r4 | % 159
    \stemUp a2 ~ _\ppppp \stemUp a8 r8 r4 | \barNumberCheck #160
    r4 \stemUp a8 ^\markup{ \italic {pizz.} } r8 r2 ^\fermata \bar "||"
    \key c \major \once \omit TupletBracket
    \times 4/6  {
        \stemUp c,16 _\ff ^\markup{ \italic {unis.} } ^ "arco" ^ ""
        \stemUp c'16 \stemUp c,16 \stemUp c'16 \stemUp c,16 \stemUp c'16
        \stemUp c,16 \stemUp c'16 \stemUp c,16 \stemUp c'16 \stemUp c,16
        }
    \stemUp c'16*2/3 \once \omit TupletBracket
    \times 4/6  {
        \stemUp c,4. :64 }
    \stemUp c'4.*2/3 \once \omit TupletBracket
    \times 8/12  {
        \stemUp c,2. :64 }
    \stemUp c'2.*2/3 | % 162
    \once \omit TupletBracket
    \times 8/12  {
        \stemUp c,2. :64 }
    \stemUp c'2.*2/3 \once \omit TupletBracket
    \times 8/12  {
        \stemUp c,2. :64 }
    \stemUp c'2.*2/3 | % 163
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 8/12  {
        \stemUp c,2. :64 }
    \stemUp c'2.*2/3 \once \omit TupletBracket
    \once \omit TupletNumber
    \times 8/12  {
        \stemUp c,2. :64 }
    \stemUp c'2.*2/3 | % 164
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 8/12  {
        \stemUp c,2. :64 }
    \stemUp c'2.*2/3 \once \omit TupletBracket
    \once \omit TupletNumber
    \times 8/12  {
        \stemUp c,2. :64 }
    \stemUp c'2.*2/3 \pageBreak | % 165
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 8/12  {
        \stemUp b2. :64 }
    _\markup{ \italic {sempre} } _ "" \once \omit TupletBracket
    \once \omit TupletNumber
    \times 8/12  {
        \stemUp b2. :64 }
    | % 166
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 8/12  {
        \stemUp b2. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 8/12  {
        \stemUp b2. :64 }
    | % 167
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 8/12  {
        \stemUp b2. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 8/12  {
        \stemUp b2. :64 }
    | % 168
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 8/12  {
        \stemUp b2. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 8/12  {
        \stemUp b2. :64 }
    | % 169
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 8/12  {
        \stemUp bes2. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 8/12  {
        \stemUp bes2. :64 _\sff }
    | \barNumberCheck #170
    \stemUp bes8 \stemUp bes8 -> \stemUp bes8 -> \stemUp bes8 -> \stemUp
    bes8 -> \stemUp a8 -> r4 | % 171
    R1 \pageBreak | % 172
    R1*2 | % 174
    r2 r4 \stemUp a8 ^\markup{ \italic {feroce} } _\ff \stemUp b8 | % 175
    \stemUp c16 \stemUp a16 \stemUp b16 \stemUp c16 \stemUp b8 r8 r4
    \stemUp a16 \stemUp d16 \stemUp c16 \stemUp a16 | % 176
    \stemUp c16 \stemUp a16 \stemUp b16 \stemUp c16 \stemUp b8 r8 r4
    \stemUp a16 \stemUp d16 \stemUp c16 \stemUp a16 | % 177
    \stemUp b16 \stemUp e16 \stemUp d16 \stemUp b16 \stemDown c16
    \stemDown f16 \stemDown e16 \stemDown c16 \stemDown d16 \stemDown g16
    \stemDown f16 \stemDown d16 \stemDown e16 \stemDown a16 \stemDown g16
    \stemDown e16 \pageBreak | % 178
    \stemDown f16 \stemDown b16 \stemDown a16 \stemDown f16 \stemDown g16
    \stemDown c16 \stemDown b16 \stemDown g16 \stemDown a16 \stemDown d16
    \stemDown c16 \stemDown a16 \stemDown b16 \stemDown cis16 \stemDown
    d16 \stemDown dis16 | % 179
    \stemDown e8 r8 r4 r2 | \barNumberCheck #180
    R1*2 | % 182
    r2 r4 \stemUp b,8 _\markup{ \italic {sempre} } _ "" \stemUp cis8
    \break | % 183
    \stemUp d16 \stemUp b16 \stemUp cis16 \stemUp d16 \stemUp cis8 r8 r4
    \stemUp b16 \stemUp e16 \stemUp d16 \stemUp b16 | % 184
    \stemUp d16 \stemUp b16 \stemUp cis16 \stemUp d16 \stemUp cis8 r8 r4
    \stemUp b16 \stemUp e16 \stemUp d16 \stemUp b16 | % 185
    \stemDown cis16 \stemDown fis16 \stemDown e16 \stemDown cis16
    \stemDown d16 \stemDown g16 \stemDown fis16 \stemDown d16 \stemDown
    e16 \stemDown a16 \stemDown g16 \stemDown e16 \stemDown d8 r8 | % 186
    r2 r4 \stemUp g,16 _\ff \stemUp cis16 \stemUp b16 \stemUp g16 | % 187
    \stemUp a16 \stemUp d16 \stemUp cis16 \stemUp a16 \stemUp b16
    \stemUp e16 \stemUp d16 \stemUp b16 \stemDown cis16 \stemDown fis16
    \stemDown e16 \stemDown cis16 \stemUp b8 r8 \pageBreak | % 188
    r2 r4 \stemDown g'8 _\fff \stemDown fis16 \stemDown g16 | % 189
    \stemDown g8 \stemDown fis16 \stemDown g16 \stemDown g8 \stemDown
    fis16 \stemDown g16 \stemDown g8 \stemDown fis16 \stemDown g16
    \stemUp bes,4 :16 ^\markup{ \italic {divisi} } | \barNumberCheck
    #190
    \stemUp bes2 :16 \stemUp bes2 :16 | % 191
    \stemUp bes2. :16 \stemUp es'4 :16 \break | % 192
    \stemUp es2 :16 \stemUp es2 :16 | % 193
    \stemUp es2. :16 \stemUp d4 :16 | % 194
    \stemUp d2 :16 \stemUp d2 :16 | % 195
    \stemUp f,2 :16 \stemUp a2 \stemUp f2 :16 \stemUp a2 \pageBreak | % 196
    \stemUp d,2 :16 \stemUp d'2 \stemUp a,2 :16 \stemUp d2 | % 197
    \stemUp a2 :16 \stemUp f'2 \stemUp d8 -> \stemUp bes'8 \stemUp d,8
    -> \stemUp a'8 r4 | % 198
    r2 \stemUp a,16 ^\markup{ \italic {unis.} } _\ff \stemUp e'16
    \stemUp d16 \stemUp a16 \stemUp f16 \stemUp bes16 \stemUp a16
    \stemUp f16 | % 199
    \stemDown d'16 \stemDown g16 \stemDown f16 \stemDown d16 \stemUp a16
    _\markup{ \italic {dim.} } \stemUp e'16 \stemUp d16 \stemUp a16
    \stemUp a16 \stemUp e'16 \stemUp d16 \stemUp a16 \stemUp a16 \stemUp
    d16 \stemUp bes16 \stemUp a16 | \barNumberCheck #200
    \stemUp a16 \stemUp d16 \stemUp bes16 \stemUp a16 \stemUp a16
    \stemUp cis16 \stemUp bes16 \stemUp a16 \stemUp a16 \stemUp c16
    \stemUp bes16 \stemUp a16 \stemUp a16 \stemUp b16 \stemUp bes16
    \stemUp a16 \break | % 201
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ( ^\markup{ \italic {legatissimo} } \stemUp bes8
        \stemUp a8 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ( _\p \stemUp bes8 \stemUp a8 ) }
    | % 202
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    | % 203
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    | % 204
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    | % 205
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    | % 206
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( _\markup{ \italic {poco a poco cresc.} } \stemUp
        bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \pageBreak | % 207
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp bes8 ( \stemUp c8 \stemUp bes8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 ( \stemUp c8 \stemUp b8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp c8 ( \stemUp des8 \stemUp c8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp c8 ( \stemUp des8 \stemUp c8 ) }
    | % 208
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp c8 ( \stemUp des8 \stemUp c8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp c8 ( \stemUp des8 \stemUp c8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp c8 ( \stemUp des8 \stemUp c8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp c8 ( \stemUp des8 \stemUp c8 ) }
    | % 209
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown des8 ( \stemDown es8 \stemDown des8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown d8 ( \stemDown es8 \stemDown d8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown es8 ( \stemDown fes8 \stemDown es8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown es8 ( _\mf \stemDown fes8 \stemDown es8 ) }
    | \barNumberCheck #210
    \stemDown dis8 r8 \stemDown e8 r8 \stemDown eis8 r8 \stemDown fis8 (
    -. r16 \stemDown fis16 ) -. | % 211
    \stemDown fis8 r8 \stemDown g8 r8 \stemDown gis8 _\markup{ \italic
        {cresc.} } r8 \stemDown a8 r8 | % 212
    \stemDown ais8 r8 \stemDown b8 r8 \stemDown bis8 _\f _\< r8
    \stemDown cis8 r8 \pageBreak | % 213
    \stemDown bis8 r8 \stemDown cis8 r8 \stemDown bis8 r8 \stemDown cis8
    r8 | % 214
    \stemUp cis,,16 _\! _\ff \stemUp d16 \stemUp cis16 \stemUp cis16
    \stemUp cis16 \stemUp d16 \stemUp cis16 \stemUp cis16 \stemUp cis16
    \stemUp d16 \stemUp cis16 \stemUp cis16 \stemUp cis16 \stemUp d16
    \stemUp cis16 \stemUp cis16 | % 215
    \stemUp cis16 \stemUp d16 \stemUp cis16 \stemUp cis16 \stemUp cis16
    \stemUp d16 \stemUp cis16 \stemUp cis16 \stemUp cis16 \stemUp d16
    \stemUp cis16 \stemUp cis16 \stemUp cis16 \stemUp d16 \stemUp cis16
    \stemUp cis16 | % 216
    \stemUp cis16 _\markup{ \italic {dim. un poco} } \stemUp d16 \stemUp
    cis16 \stemUp cis16 \stemUp cis16 \stemUp d16 \stemUp cis16 \stemUp
    cis16 \stemUp cis16 \stemUp d16 \stemUp cis16 \stemUp cis16 \stemUp
    cis16 \stemUp d16 \stemUp cis16 \stemUp cis16 \break | % 217
    \stemUp cis16 \stemUp d16 \stemUp cis16 \stemUp cis16 \stemUp cis16
    \stemUp d16 \stemUp cis16 \stemUp cis16 \stemUp cis16 \stemUp d16
    \stemUp cis16 \stemUp cis16 \stemUp cis16 \stemUp d16 \stemUp cis16
    \stemUp cis16 | % 218
    \stemUp cis16 _\f \stemUp d16 \stemUp cis16 \stemUp cis16 \stemUp
    cis16 \stemUp d16 \stemUp cis16 \stemUp cis16 \stemUp cis16 \stemUp
    d16 \stemUp cis16 \stemUp cis16 \stemUp cis16 \stemUp d16 \stemUp
    cis16 \stemUp cis16 | % 219
    \stemUp cis16 \stemUp d16 \stemUp cis16 \stemUp cis16 \stemUp cis16
    \stemUp d16 \stemUp cis16 \stemUp cis16 \stemUp cis16 \stemUp d16
    \stemUp cis16 \stemUp cis16 \stemUp cis16 \stemUp d16 \stemUp cis16
    \stemUp cis16 | \barNumberCheck #220
    \stemUp cis16 _\markup{ \italic {dim.} } \stemUp d16 \stemUp cis16
    \stemUp cis16 \stemUp cis16 \stemUp d16 \stemUp cis16 \stemUp cis16
    \stemUp cis16 \stemUp d16 \stemUp cis16 \stemUp cis16 \stemUp cis16
    \stemUp d16 \stemUp cis16 \stemUp cis16 \pageBreak | % 221
    \stemUp cis16 \stemUp d16 \stemUp cis16 \stemUp cis16 \stemUp cis16
    \stemUp d16 \stemUp cis16 \stemUp cis16 \stemUp cis16 \stemUp d16
    \stemUp cis16 \stemUp cis16 \stemUp cis16 \stemUp d16 \stemUp cis16
    \stemUp cis16 | % 222
    \stemUp cis16 \stemUp d16 \stemUp cis16 \stemUp cis16 \stemUp cis16
    \stemUp d16 \stemUp cis16 \stemUp cis16 \stemUp cis16 \stemUp d16
    \stemUp cis16 \stemUp cis16 \stemUp cis16 \stemUp d16 \stemUp cis16
    \stemUp cis16 | % 223
    \stemUp cis16 _\p \stemUp d16 \stemUp cis16 \stemUp cis16 \stemUp
    cis16 \stemUp d16 \stemUp cis16 \stemUp cis16 \stemUp cis16 \stemUp
    d16 \stemUp cis16 \stemUp cis16 \stemUp cis16 \stemUp d16 \stemUp
    cis16 \stemUp cis16 | % 224
    \stemUp b'16 \stemUp cis16 \stemUp b16 \stemUp b16 \stemUp b16
    \stemUp cis16 \stemUp b16 \stemUp b16 \stemUp b16 \stemUp cis16
    \stemUp b16 \stemUp b16 \stemUp b16 \stemUp cis16 \stemUp b16
    \stemUp b16 | % 225
    \stemUp a16 _\markup{ \italic {dim.} } \stemUp b16 \stemUp a16
    \stemUp a16 \stemUp a16 \stemUp b16 \stemUp a16 \stemUp a16 \stemUp
    a16 \stemUp b16 \stemUp a16 \stemUp a16 \stemUp a16 \stemUp b16
    \stemUp a16 \stemUp a16 \break | % 226
    \stemUp gis16 \stemUp a16 \stemUp gis16 \stemUp gis16 \stemUp gis16
    \stemUp a16 \stemUp gis16 \stemUp gis16 \stemUp gis16 \stemUp a16
    \stemUp gis16 \stemUp gis16 \stemUp gis16 \stemUp a16 \stemUp gis16
    \stemUp gis16 | % 227
    \stemUp g16 _\pp \stemUp a16 \stemUp g16 \stemUp g16 \stemUp g16
    \stemUp a16 \stemUp g16 \stemUp g16 \stemUp g16 \stemUp a16 \stemUp
    g16 \stemUp g16 \stemUp g16 \stemUp a16 \stemUp g16 \stemUp g16 | % 228
    \stemUp ges16 \stemUp bes16 \stemUp ges16 \stemUp ges16 \stemUp ges16
    _\> \stemUp bes16 \stemUp ges16 \stemUp ges16 \stemUp ges16 \stemUp
    bes16 \stemUp ges16 \stemUp ges16 \stemUp ges16 \stemUp bes16
    \stemUp ges16 \stemUp ges16 | % 229
    \stemUp f8 _\! r8 r4 r2 | \barNumberCheck #230
    R1 \break | % 231
    R1 | % 232
    \stemUp f8 _\pp ^\markup{ \italic {pizz.} } r8 r4 r2 | % 233
    R1 | % 234
    \stemUp f8 _\pp r8 r4 r2 | % 235
    r2 \stemUp f8 _\pp r8 r4 | % 236
    r2 \stemUp f2 ( _\pp ^\markup{ \italic {arco} } _\< \pageBreak | % 237
    \stemUp ges8 ) _\! _\p r8 r4 \stemUp ges8 ^\markup{ \italic {pizz.}
        } r8 r4 | % 238
    r2 \stemUp ges4 ( -. _\mp ^\markup{ \italic {arco} } \stemUp g4 ) -.
    | % 239
    \stemUp as2 _\markup{ \italic {cresc.} } \stemUp as4 ( -. \stemUp a4
    ) -. | \barNumberCheck #240
    \stemUp bes4.. \stemUp bes16 \stemUp c4.. \stemUp c16 | % 241
    \stemDown des4.. _\< \stemDown des16 \stemDown d4.. \stemDown d16
    \pageBreak | % 242
    \stemDown es8 _\! _ "" _\markup{ \italic {cresc.} } r8 \stemDown f8
    r8 \stemDown ges8 r8 r4 | % 243
    \stemDown fis4.. _\ff \stemDown fis16 \stemDown ais4.. \stemDown ais16
    | % 244
    \stemDown b8 r8 \stemDown cis8 r8 \stemDown d8 r8 \stemDown d,8
    _\fff \stemDown e8 | % 245
    \stemDown eis4 ( -> \stemDown fis8 ) r8 r4 \stemDown d8 \stemDown e8
    \pageBreak | % 246
    \stemDown eis4 ( -> \stemDown fis8 ) r8 r4 r8 \stemUp cis8 | % 247
    r8 \stemDown d8 r8 \stemDown g8 r8 \stemDown fis8 r8 \stemUp cis8 | % 248
    r8 \stemDown d8 r8 \stemDown g8 \stemDown fis8 r8 \stemDown d8 _\f
    \stemDown b'8 \stemDown e,8 | % 249
    \stemDown eis4 ( _ "" \stemDown fis8 ) r8 r4 \stemDown d8
    \stemDown e8 | \barNumberCheck #250
    \stemDown eis4 ( _ "" \stemDown fis8 ) r8 r4 \stemDown fis8
    \stemDown a8 \stemDown g8 | % 251
    \stemDown gis4 ( _ "" \stemDown a8 ) r8 r4 \stemDown fis8
    \stemDown g8 \break | % 252
    \stemDown gis4 ( _ "" \stemDown a8 ) r8 r4 \stemDown a8 _\ff
    \stemDown b8 | % 253
    \stemDown bis8 ( -> \stemDown cis8 ) r4 r4 \stemDown a8 \stemDown b8
    | % 254
    \stemDown bis8 ( -> \stemDown cis8 ) r4 r4 r8 \stemDown gis8 _\ff | % 255
    r8 \stemDown a8 r4 r4 r8 \stemDown d,8 | % 256
    r8 \stemDown e8 r4 r4 r8 \stemDown fis8 \pageBreak | % 257
    r8 \stemDown gis8 r4 r4 r8 \stemUp cis,8 | % 258
    r8 \stemDown d8 r4 r4 \stemUp d,16 _\pp \stemUp d16 \stemUp d16
    \stemUp d16 | % 259
    \stemUp dis4 :16 \stemUp e4 :16 _\markup{ \italic {cresc. molto} }
    \stemUp f4 :16 \stemUp fis4 :16 | \barNumberCheck #260
    \stemUp g4 :16 \stemUp as4 :16 \stemUp a4 :16 \stemUp bes4 :16 | % 261
    \stemUp ces4 :16 \stemUp c4 :16 \stemUp cis4 :16 \stemDown d4 :16 | % 262
    \stemDown dis4 :16 \stemDown e4 :16 \stemDown f4 :16 \stemDown ges8
    -! _\ff \stemDown f8 -! \pageBreak | % 263
    \stemDown es8 -! r8 \stemDown ges8 -! r8 r4 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown ges8 -! \stemDown f8 -! \stemDown es8 -! }
    | % 264
    \stemDown es8 -! r8 \stemDown ges8 -! r8 r4 \stemDown a8 -!
    \stemDown gis8 -! | % 265
    \stemDown fis8 -! r8 \stemDown a8 -! r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 -! \stemDown gis8 -! \stemDown fis8 -! }
    | % 266
    \stemDown fis8 -! r8 \stemDown a8 -! r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 -! \stemDown gis8 -! \stemDown fis8 -! }
    | % 267
    \stemDown fis8 r8 \stemUp fis,2. :32 _\fff \pageBreak | % 268
    \stemUp fis2 :16 \stemUp fis2 :16 | % 269
    \stemUp fis2 :16 \stemUp fis2 :16 | \barNumberCheck #270
    \stemUp fis2 :16 \stemUp fis2 :16 | % 271
    \stemUp fis2 :16 _\ff \stemUp fis2 :16 | % 272
    \stemUp fis2 :16 \stemUp fis2 :16 \pageBreak | % 273
    \stemUp fis2 :16 \stemUp fis2 :16 | % 274
    \stemUp fis2 :16 \stemUp fis2 :16 | % 275
    \stemUp fis2 :16 \stemUp fis2 :16 | % 276
    \stemUp fis2 :16 \stemUp fis8 r8 r4 | % 277
    \clef "tenor" dis''1 -> _\markup{ \italic {sempre} } _ "" | % 278
    \stemDown e4. ( -> \stemDown dis8 ) \stemDown dis2 ~ | % 279
    \stemDown dis2 \stemDown cis2 ~ | \barNumberCheck #280
    cis1 | % 281
    cis1 -> | % 282
    \stemDown d4. ( -> \stemDown cis8 ) \stemDown cis2 | % 283
    \stemDown d2 \stemDown cis2 ~ | % 284
    \stemDown cis2. \stemDown fis4 -- _\fff \pageBreak | % 285
    \stemDown e2 _\markup{ \italic {largamente, forte possibile} }
    \stemDown d2 ~ | % 286
    \stemDown d2. \stemDown d4 | % 287
    \stemDown cis2 \stemDown b2 ~ | % 288
    \stemDown b2. \stemDown a4 | % 289
    \stemUp g2 \stemUp fis2 ~ | \barNumberCheck #290
    \stemUp fis2. \stemDown e'4 | % 291
    \stemDown d2 \stemDown cis2 ~ | % 292
    \stemDown cis2. \stemDown cis4 | % 293
    \stemDown b2 \stemDown ais2 ~ | % 294
    ais1 | % 295
    \stemUp g2 \stemUp fis2 ~ | % 296
    fis1 | % 297
    \clef "bass" e1 _ "" cis'1 | % 298
    cis,1 _ "" ais'1 | % 299
    d,,1 ~ _\ffff _\> g1 ~ | \barNumberCheck #300
    \stemUp d2 ~ \stemUp g2 ~ \stemUp d8 _\! _\p \stemUp g8 r8 r4 | % 301
    fis1 ~ _\ff _\> \break | % 302
    \stemUp fis8 _\! _\f r8 r4 \stemUp fis8 _\mf ^\markup{ \italic
        {pizz.} } r8 r4 | % 303
    r2 \stemUp fis8 _\p r8 r4 | % 304
    \stemUp fis8 _\pp r8 r4 r2 ^\fermata \bar "||"
    \pageBreak | % 305
    \key b \major r8 \stemUp fis32 _\pp ^\markup{ \italic {arco} }
    \stemUp fis32 \stemUp fis32 \stemUp fis32 \stemUp gis32 \stemUp gis32
    \stemUp gis32 \stemUp gis32 \stemUp a32 \stemUp a32 \stemUp a32
    \stemUp a32 \stemUp ais8 :32 \stemUp b8 :32 \stemUp cis,8 :32
    \stemUp d8 :32 | % 306
    \stemUp dis8 :32 \stemUp e8 :32 \stemUp eis8 :32 \stemUp fis8 :32
    \stemUp gis8 :32 \stemUp ais8 :32 \stemUp b8 :32 \stemUp cis8 :32 | % 307
    \stemDown d8 :32 _\< \stemDown dis8 :32 \stemDown e8 :32 \stemDown
    eis8 :32 \stemDown fis8 :32 \stemDown gis8 :32 \stemDown ais8 :32
    \stemDown b8 :32 | % 308
    \stemDown cisis8 :32 _\! _\p _\> \stemDown dis8 :32 \stemDown fisis,8
    :32 \stemDown gis8 :32 \stemUp dis8 :32 _\! \stemUp e8 :32 \stemUp
    bis8 :32 \stemUp cis8 :32 | % 309
    \stemUp fis,8 :32 _\< \stemUp b8 :32 \stemUp cis8 :32 \stemUp d8 :32
    \stemDown d8 :32 _\! _\mp \stemDown dis8 :32 \stemDown e8 :32
    \stemDown fis8 :32 | \barNumberCheck #310
    \stemDown fisis8 :32 _\markup{ \italic {poco cresc.} } \stemDown gis8
    :32 \stemDown ais8 :32 \stemDown gis8 :32 \stemUp bis,8 :32 \stemUp
    cis8 :32 \stemUp dis8 :32 \stemUp e8 :32 \pageBreak | % 311
    \stemDown eis8 :32 \stemDown fis8 :32 \stemDown gis8 :32 \stemDown
    fis8 :32 \stemUp b,2 :32 _\mf _\> | % 312
    \stemUp b2 :32 _\! _\pp _\< \stemUp bis8 :32 _\! _\p _\< \stemUp cis8
    :32 \stemUp dis8 :32 _\! _\> \stemUp cis8 :32 | % 313
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown b16 -. _\! _\p _\< \stemDown fis'16 ( \stemDown g16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown gis16 \stemDown a16 \stemDown ais16 ) }
    \stemDown b32 ( \stemDown bis32 \stemDown cis32 \stemDown d32
    \stemDown dis32 \stemDown e32 \stemDown eis32 \stemDown fis32 )
    \stemDown fis4 -- _\! _\fff \stemDown e8. ( \stemDown dis16 ) | % 314
    \stemDown dis4 ( -> \stemDown cis4 ) \stemDown e4 -- \stemDown dis8.
    ( \stemDown cis16 ) | % 315
    \stemDown cis4 ( -> \stemDown b4 ) r8 \stemDown dis8 ( _\> \stemDown
    cis8 ) \stemDown b8 -. | % 316
    \stemDown fis8 ( _\! _\mf _\< \stemDown dis8 \stemDown b8 \stemDown
    dis8 ) \stemDown gis4.. ( _\! _\ff _\> \stemDown fis16 ) \pageBreak
    | % 317
    \stemDown fis2 _\! _\mf r2 | % 318
    R1 | % 319
    r2 r8 \clef "tenor" \stemDown d'8 ( _\f _\> \stemDown cis8 )
    \stemDown b8 -- | \barNumberCheck #320
    \stemUp fis8 ( _\! _\mf _\< \stemUp dis8 \stemUp b8 \stemUp dis8 )
    \stemUp g4.. ( _\! _\> \stemUp fis16 ) | % 321
    \stemUp fis2 _\! _\mf r2 | % 322
    R1 | % 323
    r2 r8 \stemDown d'8 ( _\f _\> \stemDown cis8 ) \stemDown b8 -- | % 324
    \stemUp fis8 -- _\! _\mf \stemUp dis8 ( \stemUp b8 \stemUp dis8 )
    \stemUp g4.. ( _\> \stemUp fis16 ) | % 325
    \stemUp fis2 ~ _\! _\p _\> \stemUp fis8 _\! _\pp r8 r4 \break | % 326
    \clef "bass" R1*8 \pageBreak | % 334
    R1 \bar "||"
    r4 \stemDown b8 _\p ^\markup{ \italic {pizz.} } r8 \stemDown ais8 r8
    \stemDown gis8 r8 | % 336
    \stemDown fis8 r8 \stemDown e8 r8 \stemDown dis8 r8 \stemUp cis8 r8
    | % 337
    \stemUp b8 r8 \stemDown b'8 r8 \stemDown ais8 r8 \stemDown gis8 r8 | % 338
    \stemDown fis8 r8 \stemDown e8 r8 \stemDown dis8 r8 \stemUp cis8 r8
    | % 339
    \stemUp b8 r8 \stemDown b'8 r8 \stemDown ais8 r8 \stemDown gis8 r8 |
    \barNumberCheck #340
    \stemDown fis8 r8 \stemDown e8 r8 \stemDown dis8 r8 \stemUp cis8 r8
    | % 341
    \stemUp b8 r8 \stemDown b'8 r8 \stemDown ais8 r8 \stemDown gis8 r8 | % 342
    \stemDown fis8 r8 \stemDown e8 r8 \stemDown dis8 r8 \stemUp cis8 r8
    \pageBreak | % 343
    \stemUp b8 r8 \stemDown b'8 r8 \stemDown ais8 r8 \stemDown gis8 r8 | % 344
    \stemDown fis8 r8 \stemDown e8 r8 \stemDown dis8 r8 \stemUp cis8 r8
    | % 345
    \stemUp b8 r8 \stemDown b'8 _\> r8 \stemDown ais8 r8 \stemDown gis8
    r8 | % 346
    \stemDown fis8 _\! _\pp r8 \stemDown e8 r8 \stemDown dis8 r8 \stemUp
    cis8 r8 | % 347
    \stemUp b8 _\markup{ \italic {sempre} } _ "" r8 \stemDown b'8 r8
    \stemDown ais8 r8 \stemDown gis8 r8 | % 348
    \stemDown fis8 r8 \stemDown e8 r8 \stemDown dis8 r8 \stemUp cis8 r8
    | % 349
    \stemUp b8 r8 \stemDown b'8 r8 \stemDown ais8 r8 \stemDown gis8 r8 |
    \barNumberCheck #350
    \stemDown fis8 r8 \stemDown e8 r8 \stemDown dis8 r8 \stemUp cis8 r8
    | % 351
    \stemUp b8 r8 r4 r2 | % 352
    R1*3 \bar "|."
    }

PartPOneSixVoiceFive =  \relative d {
    \clef "bass" \time 4/4 \key d \major | % 1
    R1*11 \break | % 12
    R1*7 \bar "||"
    r2 r4 \stemDown d8 ( -. _\p _\< \stemDown e8 ) -. | \barNumberCheck
    #20
    \stemDown eis4 ( _\! _\> \stemDown fis8 ) r8 _\! r4 \stemDown d16 (
    _\p _\< \stemDown cis16 \stemDown d16 \stemDown e16 ) | % 21
    \stemDown eis4 ( _\! _\> \stemDown fis8 ) r8 _\! r4 r8 \stemDown
    cis'8 _\p | % 22
    r8 \stemDown d8 r8 \stemDown g,8 r8 \stemDown fis8 r8 \stemUp cis8 | % 23
    r8 \stemDown d8 r8 \stemUp g,8 ( \stemUp fis8 ) r8 r4 \pageBreak | % 24
    R1*3 | % 27
    r2 r4 r8 \stemUp b8 ~ _\p | % 28
    \stemUp b8 r8 r4 r4 r8 \stemDown e8 ~ | % 29
    \stemUp e8 \stemUp b8 ~ \stemUp b4 ~ _\> \stemUp b8 _\! _\pp r8 r4 |
    \barNumberCheck #30
    \time 2/4  r4 \stemUp g4 _\pp _\< \break | % 31
    \time 4/4  \stemUp fis4 _\! _\> \stemUp e8 _\! r8 r4 \stemUp gis8
    _\< \stemUp g8 | % 32
    \stemUp fis4 _\! _\> \stemUp e8 _\! r8 r2 | % 33
    r2 r2 | % 34
    R1*3 \break | % 37
    R1*3 | \barNumberCheck #40
    r2 \stemUp cis2 _\mf | % 41
    \stemUp d2 _\> \stemUp e2 ( _\! _\p | % 42
    \stemUp fis16 ) \stemUp gis16 ( \stemUp a16 \stemUp gis16 \stemUp a16
    \stemUp gis16 \stemUp a16 \stemUp gis16 \stemDown a8 ) \stemDown g'8
    ( _\pp \stemDown fis8 \stemDown e8 | % 43
    \stemDown d8 ) \stemDown e16 ( -. _\markup{ \italic {saltando} }
    \stemDown e16 ) -. \stemDown fis8 ( -. \stemDown cis8 -. \stemUp d8
    ) -. \stemUp a16 ( -. \stemUp a16 ) -. \stemUp b8 ( -. \stemUp e8 )
    -. \pageBreak | % 44
    \stemDown d2 ~ \stemDown d8 \stemDown d16 ( -. \stemDown d16 ) -.
    \stemUp cis8 ( -. \stemUp b8 -. | % 45
    \stemUp a8 ) -. \stemUp fis'16 ( -. \stemUp fis16 ) -. \stemUp cis8
    ( -. \stemUp d8 -. \stemUp a8 ) -. \stemUp b16 ( -. \stemUp b16 ) -.
    \stemUp fis8 ( -. \stemUp eis8 ) -. | % 46
    \stemUp fis2 ~ \stemDown fis8 \stemDown d''8 ( _\p \stemDown cis8
    \stemDown b8 | % 47
    \stemDown a8 ) \stemDown b16 ( -. \stemDown b16 ) -. \stemDown cis8
    ( -. \stemDown gis8 -. \stemDown a8 ) -. \stemDown e16 ( -.
    \stemDown e16 ) -. \stemDown fis8 ( -. \stemDown b8 ) -. | % 48
    \stemDown a2 ~ \stemDown a8 r8 r4 | % 49
    r2 r4 r8 \stemDown bis8 _\p \break | \barNumberCheck #50
    R1*4 \pageBreak | % 54
    R1*5 \break | % 59
    R1*5 \pageBreak | % 64
    R1*5 \pageBreak | % 69
    R1*5 \pageBreak | % 74
    R1*4 \break | % 78
    R1*5 \pageBreak | % 83
    R1*6 \bar "||"
    R1*5 \break | % 94
    R1*7 \bar "||"
    R1*2 \pageBreak | % 103
    R1*2 s1*1/640 R1*3 \break | % 108
    R1*4 \pageBreak | % 112
    R1*4 \break | % 116
    R1*4 \pageBreak | \barNumberCheck #120
    R1*5 \break | % 125
    R1*5 \bar "||"
    \time 12/8  s1*239/640 r1 s1*13/24 r1 s1*1/12 \pageBreak s4 r1
    s1*2/3 r1 s2 r1 s1*7/12 r1 s2 r1 s2 r1 \pageBreak s1*5/12 r1 s1*7/12
    r1 s2 r1 s2 r1 \bar "||"
    s1*11/24 r1 s1*1/24 | % 143
    \numericTimeSignature\time 4/4  R1*2 \break | % 145
    R1*11 \pageBreak | % 156
    R1*5 \bar "||"
    \key c \major R1*4 \pageBreak | % 165
    R1*7 \pageBreak | % 172
    R1*6 \pageBreak | % 178
    R1*5 \break | % 183
    R1*5 \pageBreak | % 188
    R1*4 \break | % 192
    R1*4 \pageBreak | % 196
    R1*5 \break | % 201
    R1*6 \pageBreak | % 207
    R1*6 \pageBreak | % 213
    R1*4 \break | % 217
    R1*4 \pageBreak | % 221
    R1*5 \break | % 226
    R1*5 \break | % 231
    R1*6 \pageBreak | % 237
    R1*5 \pageBreak | % 242
    R1*4 \pageBreak | % 246
    R1*6 \break | % 252
    R1*5 \pageBreak | % 257
    R1*6 \pageBreak | % 263
    R1*5 \pageBreak | % 268
    R1*5 \pageBreak | % 273
    R1*12 \pageBreak | % 285
    R1*17 \break | % 302
    R1*3 \bar "||"
    \pageBreak | % 305
    \key b \major R1*6 \pageBreak | % 311
    R1*6 \pageBreak | % 317
    R1*9 \break | % 326
    R1*8 \pageBreak | % 334
    R1 \bar "||"
    R1*8 \pageBreak | % 343
    R1*12 \bar "|."
    }

PartPOneSixVoiceTwo =  \relative d, {
    \clef "bass" \time 4/4 \key d \major s1*11 \break s1*7 \bar "||"
    s1*5 \pageBreak s1*6 | \barNumberCheck #30
    \time 2/4  s2 \break | % 31
    \time 4/4  s1*6 \break s1*7 \pageBreak s1*6 \break s1*4 \pageBreak
    s16*65 \clef "tenor" s16*15 \break | % 59
    \clef "bass" s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*4
    \break s1*5 \pageBreak s1*6 \bar "||"
    s8*5 \clef "tenor" s8*35 \break s1*7 \bar "||"
    s1 | % 102
    \clef "bass" s1 \pageBreak s1*5 \break s1*4 \pageBreak s1*4 \break
    s1*4 \pageBreak s1*5 \break s1*5 \bar "||"
    \time 12/8  s1*3 \pageBreak s1*9 \pageBreak s1*6 \bar "||"
    s1. | % 143
    \numericTimeSignature\time 4/4  s1*2 \break s1*9 | % 154
    \stemDown d2 \stemDown d2 | % 155
    \stemDown d2 ~ \stemDown d8 s4. \pageBreak | % 156
    \stemDown d2 \stemDown d2 | % 157
    \stemDown d2 ~ \stemDown d8 s4. | % 158
    \stemDown d2 ~ \stemDown d8 s4. | % 159
    \stemDown d2 ~ \stemDown d8 s8*5 \stemDown d8 s8*5 \bar "||"
    \key c \major s1*4 \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*5
    \break s1*5 \pageBreak s4*7 \stemDown <g es'>4 :16 | \barNumberCheck
    #190
    \stemDown <g es'>2 :16 \stemDown <g es'>2 :16 | % 191
    \stemDown <g es'>2 :16 \stemDown <g es'>2 :16 \break | % 192
    \stemDown <g es'>2 :16 \stemDown <g es'>2 :16 | % 193
    \stemDown <g es'>2. :16 \stemDown <gis d'>4 :16 | % 194
    \stemDown <a d>2 :16 \stemDown <a d>2 :16 | % 195
    \stemDown a2 :16 \stemDown a2 :16 \pageBreak | % 196
    \stemDown <a d>2 :16 \stemDown <a d>2 :16 | % 197
    \stemDown <a f'>2 :16 \stemDown <bes d>8 -> \stemDown <a d>8 ->
    s4*13 \break s1*6 \pageBreak s1*6 \pageBreak s1*4 \break s1*4
    \pageBreak s1*5 \break s1*5 \break s1*6 \pageBreak s1*5 \pageBreak
    s1*4 \pageBreak s1*6 \break s1*5 \pageBreak s1*6 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*4 | % 277
    \clef "tenor" s1*8 \pageBreak s1*12 | % 297
    \clef "bass" s1*5 \break s1*3 \bar "||"
    \pageBreak | % 305
    \key b \major s1*6 \pageBreak s1*6 \pageBreak s8*21 \clef "tenor"
    s8*51 \break | % 326
    \clef "bass" s1*8 \pageBreak s1 \bar "||"
    s1*8 \pageBreak s1*12 \bar "|."
    }

PartPOneSevenVoiceOne =  \relative b {
    \clef "bass" \time 4/4 \key d \major \transposition c | % 1
    b1 ~ _\pp _\markup{ \italic {div.} } | % 2
    b1 ~ | % 3
    b1 | % 4
    g1 | % 5
    a1 ~ _\sf _\> | % 6
    \stemDown a8 _\! _\p r8 r4 r2 | % 7
    b1 ~ _\pp | % 8
    b1 ~ | % 9
    b1 | \barNumberCheck #10
    \stemDown fis2. ( \stemDown g4 ) | % 11
    fis1 ~ _\sf _\> \break | % 12
    \stemDown fis8 _\! _\p r8 r4 r2 | % 13
    R1*4 | % 17
    fis1 ~ _\mf _\> | % 18
    \stemDown fis2 ~ \stemDown fis8 _\! _\pp r8 r4 ^\fermata \bar "||"
    R1*5 \pageBreak | % 24
    R1*4 | % 28
    r2 r4 r8 \stemDown g8 ~ _\p | % 29
    \stemDown g8 \stemDown e8 ~ \stemDown e4 ~ _\> \stemDown e8 _\! _\pp
    r8 r4 | \barNumberCheck #30
    \time 2/4  R2 \break | % 31
    \time 4/4  R1*6 \break | % 37
    R1*2 | % 39
    \stemUp b2 _\ff _\> \stemUp cis2 | \barNumberCheck #40
    \stemDown d2 ~ \stemDown d8 _\! _\mf r8 r4 | % 41
    r2 r8 \stemUp a16 -. _\p \stemUp a16 -. \stemUp a8 -. \stemUp a8 -.
    | % 42
    \stemUp fis2 ~ \stemUp fis8 \stemUp g'8 ( _\pp \stemUp fis8 \stemUp
    e8 | % 43
    \stemUp d8 ) \stemUp cis8 ( \stemUp b8 \stemUp a8 \stemUp g8 )
    \stemUp fis8 ( \stemUp e8 \stemUp e'8 ) \pageBreak | % 44
    \stemDown d2 ~ \stemDown d8 r8 r4 | % 45
    R1 | % 46
    r2 r8 \stemDown d'8 ( _\p \stemDown cis8 \stemDown b8 | % 47
    \stemDown a8 ) \stemDown gis8 ( \stemDown fis8 \stemDown e8
    \stemDown d8 ) \stemDown cis8 ( \stemDown b8 \stemDown b'8 ) | % 48
    \stemDown a2 ~ \stemDown a8 r8 r4 | % 49
    r2 r4 r8 \stemDown bis8 _\p \break | \barNumberCheck #50
    \stemDown cis2 ~ ^\markup{ \italic {unis.} } \stemDown cis8
    \stemDown gis,8 _\mp r4 | % 51
    \stemDown cis'2 ~ _\mp \stemDown cis16 \stemDown cis16 -. \stemDown
    cis16 -. \stemDown cis16 -. \stemDown cis16 -. \stemDown cis16 -.
    \stemDown cis16 -. \stemDown cis16 -. | % 52
    \stemDown cis16 -. \stemDown cis16 -. \stemDown cis16 -. \stemDown
    gis16 -. \stemDown gis16 -. \stemDown gis16 -. \stemDown gis16 -.
    \stemDown cis,16 -. \stemUp cis8 -. \stemUp cis8 -. r4 | % 53
    \stemDown cis'2 ~ _\mp \stemDown cis16 \stemDown cis16 -. \stemDown
    cis16 -. \stemDown cis16 -. \stemDown cis16 -. \stemDown cis16 -.
    \stemDown cis16 -. \stemDown cis16 -. \pageBreak | % 54
    \stemDown cis16 -. \stemDown cis16 -. \stemDown cis16 -. \stemDown
    gis16 -. \stemDown gis16 -. \stemDown gis16 -. \stemDown gis16 -.
    \stemDown cis,16 -. \stemUp cis8 -. r8 r4 | % 55
    R1*3 | % 58
    r2 r8 \stemUp gis8 _\mp ^\markup{ \italic {pizz.} } r4 \break | % 59
    \stemDown gis'2 ~ _\mp ^\markup{ \italic {arco} } \stemDown gis16
    \stemDown gis16 -. \stemDown gis16 -. \stemDown gis16 -. \stemDown
    gis16 -. \stemDown gis16 -. \stemDown gis16 -. \stemDown gis16 -. |
    \barNumberCheck #60
    \stemDown gis16 -. \stemDown gis16 -. \stemDown gis16 -. \stemDown
    dis16 -. \stemUp dis16 -. \stemUp dis16 -. \stemUp dis16 -. \stemUp
    gis,16 -. \stemUp gis8 -. \stemUp gis8 -. r4 | % 61
    \stemDown gis'2 ~ _\mp \stemDown gis16 \stemDown gis16 -. \stemDown
    gis16 -. \stemDown gis16 -. \stemDown gis16 -. \stemDown gis16 -.
    \stemDown gis16 -. \stemDown gis16 -. | % 62
    \stemDown gis16 -. \stemDown gis16 -. \stemDown gis16 -. \stemDown
    dis16 -. \stemUp dis16 -. \stemUp dis16 -. \stemUp dis16 -. \stemUp
    gis,16 -. \stemUp gis8 -. \stemUp gis8 -. r4 | % 63
    r16 \stemDown fis''16 -. _\p _\< \stemDown fis16 -. \stemDown fis16
    -. \stemDown fis16 -. \stemDown fis16 -. \stemDown fis16 -.
    \stemDown fis16 -. \stemDown cis8 ( -- _\! _\> \stemDown cis8 ) --
    \stemDown cis8 -- r8 _\! \pageBreak | % 64
    r16 \stemDown dis16 -. _\p _\< \stemDown dis16 -. \stemDown dis16 -.
    \stemDown dis16 -. \stemDown dis16 -. \stemDown dis16 -. \stemDown
    dis16 -. \stemDown fis,8 ( -- _\! _\> \stemDown fis8 ) -- \stemDown
    fis8 -- r8 _\! | % 65
    r16 \stemDown gis'16 -. _\mp _\< \stemDown gis16 -. \stemDown gis16
    -. \stemDown gis16 -. \stemDown gis16 -. \stemDown gis16 -.
    \stemDown gis16 -. \stemDown eis8 ( -- _\! _\> \stemDown eis8 ) --
    \stemDown eis8 -- r8 _\! | % 66
    r16 \stemDown dis16 -. _\mp _\< \stemDown dis16 -. \stemDown dis16
    -. \stemDown dis16 -. \stemDown dis16 -. \stemDown dis16 -.
    \stemDown dis16 -. \stemDown dis,4 ~ _\! _\> \stemDown dis8 r8 _\! | % 67
    \stemUp eis,2 -> _\f \stemUp fis8 r8 r4 | % 68
    R1 \pageBreak | % 69
    \stemUp gis2 -> _\ff \stemUp a8 r8 r4 | \barNumberCheck #70
    r2 \stemDown a'4 ~ _\ff \stemDown a8 r8 | % 71
    r2 \stemDown g4 ~ \stemDown g8 r8 | % 72
    r2 \stemDown f4 ~ \stemDown f8 r8 | % 73
    \stemDown e4 ~ \stemDown e8 r8 \stemDown f4 ~ \stemDown f8 r8
    \pageBreak | % 74
    \stemDown e4 ~ \stemDown e8 r8 \stemDown f4 ( -> \stemDown e8 ) r8 | % 75
    \stemDown f4 ( -> \stemDown e8 ) r8 \stemDown e4 ( -> \stemDown es8
    ) r8 | % 76
    \stemDown e4 ( -> \stemDown es8 ) r8 \stemDown e4 ( -> _\f \stemDown
    es8 ) r8 | % 77
    \stemDown e4 ( -> \stemDown es8 ) r8 \stemDown e4 ( -> _\mf
    \stemDown es8 ) r8 \break | % 78
    \stemDown e4 ( -> \stemDown es8 ) r8 r4 \stemDown es4 ~ _\mp | % 79
    \stemDown es4 ~ \stemDown es8 r8 r2 | \barNumberCheck #80
    R1*3 \pageBreak | % 83
    R1*6 \bar "||"
    R1 | \barNumberCheck #90
    \stemDown d2 _\pp ^\markup{ \italic {con sordini} } _\< \stemDown d2
    _\! _\mp _\> | % 91
    d1 _\! _\pp | % 92
    \stemDown d2 _\pp _\< \stemDown d2 _\! _\mp _\> | % 93
    \stemDown d2 _\! _\pp _\< \stemDown d2 _\! _\mf \break | % 94
    \stemDown d2 \stemDown d2 _\> | % 95
    \stemDown d2 _\! _\p _\< \stemUp gis,2 _\! _\mf _\> | % 96
    \stemUp a2 _\! _\p _\< \stemUp a2 _\! _\mf _\> | % 97
    \stemDown d2 _\! _\p _\< \stemDown d2 _\! _\mf | % 98
    \stemDown d2 \stemDown d2 _\> | % 99
    \stemDown d2 _\! _\p _\< \stemUp gis,2 _\! _\mf _\> |
    \barNumberCheck #100
    \stemUp a2 _\! _\p _\< \stemUp a2 _\! _\mf _\> \bar "||"
    \stemDown d8 _\! _\p r8 r4 r2 | % 102
    \stemDown d8 ^\markup{ \italic {pizz.} } r8 r4 r2 \pageBreak | % 103
    \stemDown d8 r8 r4 r2 | % 104
    \stemUp cis8 r8 r4 r2 | % 105
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp c16 ( _\mp ^\markup{ \italic {arco} } \stemUp d16
        \stemUp c16 \stemUp d16 \stemUp c16 \stemUp d16 }
    \once \omit TupletBracket
    \times 4/7  {
        \stemUp c16*161/160 \stemUp d16*161/160 \stemUp c16*161/160
        \stemUp d16*161/160 \stemUp c16*161/160 \stemUp b16*161/160
        \stemUp c16*161/160 }
    \stemDown cis8 ) -. \stemDown cis'8 -. r4 | % 106
    \stemUp b,8 _\p ^\markup{ \italic {pizz.} } r8 r4 r2 | % 107
    \stemUp e,8 _\mf r8 r4 r2 \break | % 108
    \stemUp a8 r8 r4 r2 | % 109
    \stemUp a8 _\p r8 r4 \stemDown e'8 r8 r4 | \barNumberCheck #110
    \stemUp a,8 r8 r4 r2 | % 111
    \stemUp a8 r8 r4 r2 \pageBreak | % 112
    \stemUp gis8 r8 r4 r2 | % 113
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp g16 ( _\mp ^\markup{ \italic {arco} } \stemUp a16
        \stemUp g16 \stemUp a16 \stemUp g16 \stemUp a16 }
    \once \omit TupletBracket
    \times 4/7  {
        \stemUp g16*161/160 \stemUp a16*161/160 \stemUp g16*161/160
        \stemUp a16*161/160 \stemUp g16*161/160 \stemUp fis16*161/160
        \stemUp g16*161/160 ) }
    \stemUp gis8 -. \stemUp gis'8 -. r4 | % 114
    \stemUp fis,8 _\mp ^\markup{ \italic {pizz.} } r8 r4 r2 | % 115
    \stemUp b8 _\mf r8 r4 r2 \break | % 116
    \stemUp e,8 r8 r4 r2 | % 117
    \stemDown e'8 _\p r8 r4 r2 | % 118
    \stemUp e,8 r8 r4 \stemDown e'8 r8 r4 | % 119
    \stemDown d8 _\markup{ \italic {cresc.} } r8 r4 r2 \pageBreak |
    \barNumberCheck #120
    \stemUp cis8 r8 r4 r2 | % 121
    \stemUp b2. _\mf ^\markup{ \italic {arco} } \stemUp b4 | % 122
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp a16 ( _\markup{ \italic {poco cresc.} } \stemUp b16
        \stemUp a16 \stemUp b16 \stemUp a16 \stemUp gis16 ) }
    \stemUp a2 \stemUp a4 | % 123
    \stemUp g2. _\< \stemUp g4 | % 124
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp fis16 ( _\! _\f \stemUp g16 \stemUp fis16 \stemUp g16
        \stemUp fis16 \stemUp eis16 ) }
    \stemUp fis2 \stemUp fis4 ( \break | % 125
    \stemUp f8 ) r8 r4 r2 | % 126
    \stemUp e8 _\ff r8 r4 r2 | % 127
    R1*3 ^\markup{ \italic {alzate sordini} } \bar "||"
    \time 12/8  r8*2/3 ^\markup{ \italic {senza sordini} } \stemDown d'8
    _\p \stemDown d8 \stemDown d8 \stemDown d8 \stemDown d8 \stemDown d4.
    ~ \stemDown d8 r8*2/3 r8*2/3 s1*39/320 | % 131
    r8*2/3 \stemDown d8 _\markup{ \italic {sempre} } _ "" \stemDown d8
    \stemDown d8 \stemDown d8 \stemDown d8 r8*2/3 \stemDown d8 \stemDown
    d8 \stemDown d8 \stemDown d8 \stemDown d8 s1*1/12 \pageBreak | % 132
    r8*2/3 \stemDown d8 \stemDown d8 \stemDown d8 \stemDown d8 \stemDown
    d8 \stemDown d8 r8*2/3 r8*2/3 r4*2/3 r8*2/3 s4 | % 133
    r8*2/3 \stemDown d8 \stemDown d8 \stemDown d8 \stemDown d8 \stemDown
    d8 r8*2/3 \stemDown d8 \stemDown d8 \stemDown d8 \stemDown d8
    \stemDown d8 s1*1/12 | % 134
    r8*2/3 \stemDown d8 _\p _\< \stemDown d8 \stemDown d8 \stemDown d8 r8*2/3
    _\! \stemDown d2. _\mf s1*1/12 | % 135
    \stemDown d8 \stemDown d8 \stemDown d8 \stemDown d8 \stemDown d8
    \stemDown d8 \stemDown d2. | % 136
    \stemDown d8 _\< \stemDown d8 \stemDown d8 \stemDown d8 \stemDown d8
    \stemDown d8 \stemUp gis,2. _\! _\sf _\> | % 137
    \stemUp a8 _\! _\p _\< \stemUp a8 \stemUp a8 \stemUp a8 \stemUp a8
    \stemUp a8 \stemUp a2. _\! _\mf _\> \pageBreak | % 138
    r8*2/3 _\! \stemDown d8 _\p _\< \stemDown d8 \stemDown d8 \stemDown
    d8 r8*2/3 _\! \stemDown d2. _\mf s1*1/12 | % 139
    \stemDown d8 \stemDown d8 \stemDown d8 \stemDown d8 \stemDown d8
    \stemDown d8 \stemDown d2. | \barNumberCheck #140
    \stemDown d8 _\< \stemDown d8 \stemDown d8 \stemDown d8 \stemDown d8
    \stemDown d8 \stemUp gis,2. _\! _\sf _\> | % 141
    \stemUp a8 _\! _\p _\< \stemUp a8 \stemUp a8 \stemUp a8 \stemUp a8
    \stemUp a8 \stemUp a2. _\! _\mf _\> \bar "||"
    r8*2/3 _\! \stemDown d8 _\mf _\> \stemDown d8 \stemDown d8 \stemDown
    d8 \stemDown d8 \stemDown d2. ~ _\! _\mp s1*1/24 | % 143
    \numericTimeSignature\time 4/4  \stemDown d2 \stemDown d2 ~ | % 144
    \stemDown d2 _\> \stemDown d2 ~ _\! _\p \break | % 145
    \stemDown d2 \stemDown d2 ~ | % 146
    \stemDown d2 \stemDown d2 ~ | % 147
    \stemDown d2 \stemDown d2 ~ | % 148
    \stemDown d2 _\> \stemDown d2 ~ _\! _\pp | % 149
    \stemDown d2 \stemDown d2 ~ | \barNumberCheck #150
    d1 ~ | % 151
    d1 ~ _\markup{ \italic {dim.} } | % 152
    d1 ~ _\ppp | % 153
    \stemDown d2 r2 | % 154
    R1*2 \pageBreak | % 156
    R1*5 \bar "||"
    \key c \major \stemUp c16 _\ff \stemUp c16 \stemUp c16 \stemUp c16
    \stemUp c4 :16 \stemUp c2 :16 | % 162
    \stemUp c2 :16 \stemUp c2 :16 | % 163
    \stemUp c2 :16 \stemUp c2 :16 | % 164
    \stemUp c2 :16 \stemUp c2 :16 \pageBreak | % 165
    \stemUp b2 :16 _\markup{ \italic {sempre} } _ "" \stemUp b2 :16 | % 166
    \stemUp b2 :16 \stemUp b2 :16 | % 167
    \stemUp b2 :16 \stemUp b2 :16 | % 168
    \stemUp b2 :16 \stemUp b2 :16 | % 169
    \stemUp bes2 :16 \stemUp bes2 :16 _\sff | \barNumberCheck #170
    \stemUp bes8 \stemUp bes8 -> \stemUp bes8 -> \stemUp bes8 -> \stemUp
    bes8 -> \stemUp a8 -> r4 | % 171
    R1 \pageBreak | % 172
    R1*2 | % 174
    r2 r4 \stemUp a8 ^\markup{ \italic {feroce} } _\ff \stemUp b8 | % 175
    \stemUp c8 r8 \stemUp b8 r8 r4 \stemUp a16 \stemUp d16 \stemUp c16
    \stemUp a16 | % 176
    \stemUp c8 r8 \stemUp b8 r8 r4 \stemUp a16 \stemUp d16 \stemUp c16
    \stemUp a16 | % 177
    \stemUp b16 \stemUp e16 \stemUp d16 \stemUp b16 \stemDown c16
    \stemDown f16 \stemDown e16 \stemDown c16 \stemDown d16 \stemDown g16
    \stemDown f16 \stemDown d16 \stemDown e16 \stemDown a16 \stemDown g16
    \stemDown e16 \pageBreak | % 178
    \stemDown f16 \stemDown b16 \stemDown a16 \stemDown f16 \stemDown g16
    \stemDown c16 \stemDown b16 \stemDown g16 \stemDown a16 \stemDown d16
    \stemDown c16 \stemDown a16 \stemDown b16 \stemDown cis16 \stemDown
    d16 \stemDown dis16 | % 179
    \stemDown e8 r8 r4 r2 | \barNumberCheck #180
    R1*2 | % 182
    r2 r4 \stemUp b,8 _\markup{ \italic {sempre} } _ "" \stemUp cis8
    \break | % 183
    \stemDown d8 r8 \stemUp cis8 r8 r4 \stemUp b16 \stemUp e16 \stemUp d16
    \stemUp b16 | % 184
    \stemDown d8 r8 \stemUp cis8 r8 r4 \stemUp b16 \stemUp e16 \stemUp d16
    \stemUp b16 | % 185
    \stemDown cis16 \stemDown fis16 \stemDown e16 \stemDown cis16
    \stemDown d16 \stemDown g16 \stemDown fis16 \stemDown d16 \stemDown
    e16 \stemDown a16 \stemDown g16 \stemDown e16 \stemDown d8 r8 | % 186
    r2 r4 \stemUp g,16 _\ff \stemUp cis16 \stemUp b16 \stemUp g16 | % 187
    \stemUp a16 \stemUp d16 \stemUp cis16 \stemUp a16 \stemUp b16
    \stemUp e16 \stemUp d16 \stemUp b16 \stemDown cis16 \stemDown fis16
    \stemDown e16 \stemDown cis16 \stemUp b8 r8 \pageBreak | % 188
    R1 | % 189
    r2 r4 \stemUp g4 :16 _\fff | \barNumberCheck #190
    \stemUp g2 :16 \stemUp g2 :16 | % 191
    \stemUp g2 :16 \stemUp g2 :16 \break | % 192
    \stemUp g2 :16 \stemUp g2 :16 | % 193
    \stemUp g2. :16 \stemUp gis4 :16 | % 194
    \stemUp a2 :16 \stemUp a2 :16 | % 195
    \stemUp a2 :16 \stemUp a2 :16 \pageBreak | % 196
    \stemUp a2 :16 \stemUp a2 :16 | % 197
    \stemUp a2 :16 \stemUp a8 -> \stemUp a8 -> r4 | % 198
    R1 | % 199
    \stemDown d16 \stemDown g16 \stemDown f16 \stemDown d16 \stemUp a16
    _\markup{ \italic {dim.} } \stemUp e'16 \stemUp d16 \stemUp a16
    \stemUp a16 \stemUp e'16 \stemUp d16 \stemUp a16 \stemUp a16 \stemUp
    d16 \stemUp bes16 \stemUp a16 | \barNumberCheck #200
    \stemUp a16 \stemUp d16 \stemUp bes16 \stemUp a16 \stemUp a16
    \stemUp cis16 \stemUp bes16 \stemUp a16 \stemUp a16 \stemUp c16
    \stemUp bes16 \stemUp a16 \stemUp a16 \stemUp b16 \stemUp bes16
    \stemUp a16 \break | % 201
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ( ^\markup{ \italic {legatissimo} } \stemUp bes8
        \stemUp a8 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ( _\p \stemUp bes8 \stemUp a8 ) }
    | % 202
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    | % 203
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    | % 204
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    | % 205
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    | % 206
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( _\markup{ \italic {poco a poco cresc.} } \stemUp
        bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 ( \stemUp bes8 \stemUp a8 ) }
    \pageBreak | % 207
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp bes8 ( \stemUp c8 \stemUp bes8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp b8 ( \stemUp c8 \stemUp b8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp c8 ( \stemUp des8 \stemUp c8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp c8 ( \stemUp des8 \stemUp c8 ) }
    | % 208
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp c8 ( \stemUp des8 \stemUp c8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp c8 ( \stemUp des8 \stemUp c8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp c8 ( \stemUp des8 \stemUp c8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp c8 ( \stemUp des8 \stemUp c8 ) }
    | % 209
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown des8 ( \stemDown es8 \stemDown des8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown d8 ( \stemDown es8 \stemDown d8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown es8 ( \stemDown fes8 \stemDown es8 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown es8 ( _\mf \stemDown fes8 \stemDown es8 ) }
    | \barNumberCheck #210
    \stemDown dis8 r8 \stemDown e8 r8 \stemDown eis8 r8 \stemDown fis8 (
    -. r16 \stemDown fis16 ) -. | % 211
    \stemDown fis8 r8 \stemDown g8 r8 \stemDown gis8 _\markup{ \italic
        {cresc.} } r8 \stemDown a8 r8 | % 212
    \stemDown ais8 r8 \stemDown b8 r8 \stemDown bis8 _\f _\< r8
    \stemDown cis8 r8 \pageBreak | % 213
    \stemDown bis8 r8 \stemDown cis8 r8 \stemDown bis8 r8 \stemDown cis8
    r8 | % 214
    \stemUp cis,16 ( _\! _\ff ^\markup{ \italic {div.} } \stemUp d16
    \stemUp cis8 ) r8 r16 \stemUp cis16 -. \stemUp cis16 ( \stemUp d16
    \stemUp cis8 ) r8 r16 \stemUp cis16 -. | % 215
    \stemUp cis16 ( \stemUp d16 \stemUp cis8 ) r8 r16 \stemUp cis16 -.
    \stemUp cis16 ( \stemUp d16 \stemUp cis8 ) r8 r16 \stemUp cis16 -. | % 216
    \stemUp cis16 ( _\markup{ \italic {dim. un poco} } \stemUp d16
    \stemUp cis8 ) r8 r16 \stemUp cis16 -. \stemUp cis16 ( \stemUp d16
    \stemUp cis8 ) r8 r16 \stemUp cis16 -. \break | % 217
    \stemUp cis16 ( \stemUp d16 \stemUp cis8 ) r8 r16 \stemUp cis16 -.
    \stemUp cis16 ( \stemUp d16 \stemUp cis8 ) r4 | % 218
    R1*3 \pageBreak | % 221
    R1*3 | % 224
    \stemUp b16 _\p \stemUp cis16 \stemUp b16 \stemUp b16 \stemUp b16
    \stemUp cis16 \stemUp b16 \stemUp b16 \stemUp b16 \stemUp cis16
    \stemUp b16 \stemUp b16 \stemUp b16 \stemUp cis16 \stemUp b16
    \stemUp b16 | % 225
    \stemUp a16 _\markup{ \italic {dim.} } \stemUp b16 \stemUp a16
    \stemUp a16 \stemUp a16 \stemUp b16 \stemUp a16 \stemUp a16 \stemUp
    a16 \stemUp b16 \stemUp a16 \stemUp a16 \stemUp a16 \stemUp b16
    \stemUp a16 \stemUp a16 \break | % 226
    \stemUp gis16 \stemUp a16 \stemUp gis16 \stemUp gis16 \stemUp gis16
    \stemUp a16 \stemUp gis16 \stemUp gis16 \stemUp gis16 \stemUp a16
    \stemUp gis16 \stemUp gis16 \stemUp gis16 \stemUp a16 \stemUp gis16
    \stemUp gis16 | % 227
    \stemUp g16 _\pp \stemUp a16 \stemUp g16 \stemUp g16 \stemUp g16
    \stemUp a16 \stemUp g16 \stemUp g16 \stemUp g16 \stemUp a16 \stemUp
    g16 \stemUp g16 \stemUp g16 \stemUp a16 \stemUp g16 \stemUp g16 | % 228
    \stemUp ges16 \stemUp bes16 \stemUp ges16 \stemUp ges16 \stemUp ges16
    _\> \stemUp bes16 \stemUp ges16 \stemUp ges16 \stemUp ges16 \stemUp
    bes16 \stemUp ges16 \stemUp ges16 \stemUp ges16 \stemUp bes16
    \stemUp ges16 \stemUp ges16 | % 229
    \stemUp f8 _\! r8 r4 r2 | \barNumberCheck #230
    R1 \break | % 231
    R1 | % 232
    \stemUp f8 _\pp ^\markup{ \italic {pizz.} } r8 r4 r2 | % 233
    R1 | % 234
    \stemUp f8 _\pp r8 r4 r2 | % 235
    r2 \stemUp f8 _\pp r8 r4 | % 236
    r2 \stemUp f8 _\pp r8 r4 \pageBreak | % 237
    \stemUp ges8 _\p r8 r4 \stemUp ges8 r8 r4 | % 238
    r2 \stemUp ges4 ( -. _\mp ^\markup{ \italic {arco} } \stemUp g4 ) -.
    | % 239
    \stemUp as8 _\markup{ \italic {cresc.} } r8 r4 \stemUp as4 ( -.
    \stemUp a4 ) -. | \barNumberCheck #240
    \stemUp bes4.. \stemUp bes16 \stemUp c4.. \stemUp c16 | % 241
    \stemDown des4.. _\< \stemDown des16 \stemDown d4.. \stemDown d16
    \pageBreak | % 242
    \stemDown es8 _\! _ "" _\markup{ \italic {cresc.} } r8 \stemDown f8
    r8 \stemDown ges8 r8 r4 | % 243
    \stemDown fis4.. _\ff \stemDown fis16 \stemDown ais4.. \stemDown ais16
    | % 244
    \stemDown b8 r8 \stemDown cis8 r8 \stemDown d8 r8 \stemDown d,8
    _\fff \stemDown e8 | % 245
    \stemDown eis4 ( -> \stemDown fis8 ) r8 r4 \stemDown d8 \stemDown e8
    \pageBreak | % 246
    \stemDown eis4 ( -> \stemDown fis8 ) r8 r4 r8 \stemUp cis8 | % 247
    r8 \stemDown d8 r8 \stemDown g8 r8 \stemDown fis8 r8 \stemUp cis8 | % 248
    r8 \stemDown d8 r8 \stemDown g8 \stemDown fis8 r8 \stemDown d8 _\f
    \stemDown e8 | % 249
    \stemDown eis4 ( _ "" \stemDown fis8 ) r8 r4 \stemDown d8
    \stemDown e8 | \barNumberCheck #250
    \stemDown eis4 ( _ "" \stemDown fis8 ) r8 r4 \stemDown fis8
    \stemDown g8 | % 251
    \stemDown gis4 ( _ "" \stemDown a8 ) r8 r4 \stemDown fis8
    \stemDown g8 \break | % 252
    \stemDown gis4 ( _ "" \stemDown a8 ) r8 r4 \stemDown a8 _\ff
    \stemDown b8 | % 253
    \stemDown bis8 ( -> \stemDown cis8 ) r4 r4 \stemDown a8 \stemDown b8
    | % 254
    \stemDown bis8 ( -> \stemDown cis8 ) r4 r4 r8 \stemDown gis8 _\ff | % 255
    r8 \stemDown a8 r4 r4 r8 \stemDown d,8 | % 256
    r8 \stemDown e8 r4 r4 r8 \stemDown fis8 \pageBreak | % 257
    r8 \stemDown gis8 r4 r4 r8 \stemUp cis,8 | % 258
    r8 \stemDown d8 r4 r4 \stemDown d16 _\pp \stemDown d16 \stemDown d16
    \stemDown d16 | % 259
    \stemDown dis4 :16 \stemUp e,4 :16 _\markup{ \italic {cresc. molto}
        } \stemUp f4 :16 \stemUp fis4 :16 | \barNumberCheck #260
    \stemUp g4 :16 \stemUp as4 :16 \stemUp a4 :16 \stemUp bes4 :16 | % 261
    \stemUp ces4 :16 \stemUp c4 :16 \stemUp cis4 :16 \stemDown d4 :16 | % 262
    \stemDown dis4 :16 \stemDown e4 :16 \stemDown f4 :16 \stemDown ges8
    -! _\ff \stemDown f8 -! \pageBreak | % 263
    \stemDown es8 -! r8 \stemDown ges8 -! r8 r4 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown ges8 -! \stemDown f8 -! \stemDown es8 -! }
    | % 264
    \stemDown es8 -! r8 \stemDown ges8 -! r8 r4 \stemDown a8 -!
    \stemDown gis8 -! | % 265
    \stemDown fis8 -! r8 \stemDown a8 -! r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 -! \stemDown gis8 -! \stemDown fis8 -! }
    | % 266
    \stemDown fis8 -! r8 \stemDown a8 -! r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 -! \stemDown gis8 -! \stemDown fis8 -! }
    | % 267
    \stemDown fis8 r8 \stemUp fis,2. :32 _\fff \pageBreak | % 268
    \stemUp fis2 :16 \stemUp fis2 :16 | % 269
    \stemUp fis2 :16 \stemUp fis2 :16 | \barNumberCheck #270
    \stemUp fis2 :16 \stemUp fis2 :16 | % 271
    \stemUp fis2 :16 _\ff \stemUp fis2 :16 | % 272
    \stemUp fis2 :16 \stemUp fis2 :16 \pageBreak | % 273
    \stemUp fis2 :16 \stemUp fis2 :16 | % 274
    \stemUp fis2 :16 \stemUp fis2 :16 | % 275
    \stemUp fis2 :16 \stemUp fis2 :16 | % 276
    \stemUp fis2 :16 \stemUp fis2 :16 | % 277
    \stemUp fis2 :16 _\markup{ \italic {sempre} } _ "" \stemUp fis2
    :16 | % 278
    \stemUp fis2 :16 \stemUp fis2 :16 | % 279
    \stemUp fis2 :16 \stemUp fis2 :16 | \barNumberCheck #280
    \stemUp fis2 :16 \stemUp fis2 :16 | % 281
    \stemUp fis2 :16 \stemUp fis2 :16 | % 282
    \stemUp fis2 :16 \stemUp fis2 :16 | % 283
    \stemUp fis2 :16 \stemUp fis2 :16 | % 284
    \stemUp fis2 :16 \stemUp fis2 :16 \pageBreak | % 285
    \stemUp fis2 :16 _\fff \stemUp fis2 :16 | % 286
    \stemUp fis2 :16 \stemUp fis2 :16 | % 287
    \stemUp fis2 :16 \stemUp fis2 :16 | % 288
    \stemUp fis2 :16 \stemUp fis2 :16 | % 289
    \stemUp fis2 :16 \stemUp fis2 :16 | \barNumberCheck #290
    \stemUp fis2 :16 \stemUp fis2 :16 | % 291
    \stemUp fis2 :16 \stemUp fis2 :16 | % 292
    \stemUp fis2 :16 \stemUp fis2 :16 | % 293
    \stemUp fis2 :16 \stemUp fis2 :16 | % 294
    \stemUp fis2 :16 \stemUp fis2 :16 | % 295
    \stemUp fis2 :16 \stemUp fis2 :16 | % 296
    \stemUp fis2 :16 \stemUp fis2 :16 | % 297
    \stemUp fis2 :16 \stemUp fis2 :16 | % 298
    \stemUp fis2 :16 \stemUp fis2 :16 | % 299
    \stemUp fis2 :16 _\ffff _\> \stemUp fis2 :16 | \barNumberCheck #300
    \stemUp fis2 :16 \stemUp fis2 :16 _\! _\p | % 301
    \stemUp fis2 :16 _\ff _\> \stemUp fis2 :16 \break | % 302
    \stemUp fis8 _\! _\f r8 r4 \stemUp fis8 _\mf ^\markup{ \italic
        {pizz.} } r8 r4 | % 303
    r2 \stemUp fis8 _\p r8 r4 | % 304
    \stemUp fis8 _\pp r8 r4 r2 ^\fermata \bar "||"
    \pageBreak | % 305
    \key b \major r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis16 _\pp ^\markup{ \italic {arco} } \stemUp fis16
        \stemUp fis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp gis16 \stemUp gis16 \stemUp gis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a16 \stemUp a16 \stemUp a16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp ais16 \stemUp ais16 \stemUp ais16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b16 \stemUp b16 \stemUp b16 }
    r4 | % 306
    \stemUp b2 _\pp \stemUp b2 | % 307
    b1 | % 308
    \stemUp b2 \stemUp b2 | % 309
    b1 _\p _\< | \barNumberCheck #310
    b1 _\! _ "" _\markup{ \italic {poco cresc.} } \pageBreak | % 311
    \stemUp b2 \stemUp eis,2 _\mf _\> | % 312
    \stemUp fis2 _\! _\pp _\< \stemUp fis2 | % 313
    \stemUp b2 _\! _\p _\< \stemUp b'2 _\! ^\markup{ \italic {div.} }
    _\ff | % 314
    \stemUp b2 \stemUp b2 | % 315
    \stemUp b2 \stemUp eis,2 _\sff _\> | % 316
    \stemUp fis2 _\! _\mf _\< \stemUp fis2 _\! _\> \pageBreak | % 317
    \stemUp b2 _\! _\mf \stemUp b2 ~ | % 318
    \stemUp b2 \stemUp b2 ~ | % 319
    \stemUp b2 \stemUp b2 ~ | \barNumberCheck #320
    \stemUp b2 \stemUp b2 ~ | % 321
    \stemUp b2 \stemUp b2 ~ | % 322
    \stemUp b2 \stemUp b2 ~ | % 323
    \stemUp b2 \stemUp b2 ~ | % 324
    \stemUp b2 \stemUp b2 ~ _\> | % 325
    \stemUp b2 ~ _\! _\p _\> \stemUp b8 _\! _\pp r8 r4 \break | % 326
    R1*8 \pageBreak | % 334
    R1 \bar "||"
    r4 \stemDown b8 _\p ^\markup{ \italic {pizz.} } r8 \stemDown ais8 r8
    \stemDown gis8 r8 | % 336
    \stemDown fis8 r8 \stemDown e8 r8 \stemDown dis8 r8 \stemUp cis8 r8
    | % 337
    \stemUp b8 r8 \stemDown b'8 r8 \stemDown ais8 r8 \stemDown gis8 r8 | % 338
    \stemDown fis8 r8 \stemDown e8 r8 \stemDown dis8 r8 \stemUp cis8 r8
    | % 339
    \stemUp b8 r8 \stemDown b'8 r8 \stemDown ais8 r8 \stemDown gis8 r8 |
    \barNumberCheck #340
    \stemDown fis8 r8 \stemDown e8 r8 \stemDown dis8 r8 \stemUp cis8 r8
    | % 341
    \stemUp b8 r8 \stemDown b'8 r8 \stemDown ais8 r8 \stemDown gis8 r8 | % 342
    \stemDown fis8 r8 \stemDown e8 r8 \stemDown dis8 r8 \stemUp cis8 r8
    \pageBreak | % 343
    \stemUp b8 r8 \stemDown b'8 r8 \stemDown ais8 r8 \stemDown gis8 r8 | % 344
    \stemDown fis8 r8 \stemDown e8 r8 \stemDown dis8 r8 \stemUp cis8 r8
    | % 345
    \stemUp b8 r8 \stemDown b'8 _\> r8 \stemDown ais8 r8 \stemDown gis8
    r8 | % 346
    \stemDown fis8 _\! _\pp r8 \stemDown e8 r8 \stemDown dis8 r8 \stemUp
    cis8 r8 | % 347
    \stemUp b8 _\markup{ \italic {sempre} } _ "" r8 \stemDown b'8 r8
    \stemDown ais8 r8 \stemDown gis8 r8 | % 348
    \stemDown fis8 r8 \stemDown e8 r8 \stemDown dis8 r8 \stemUp cis8 r8
    | % 349
    \stemUp b8 r8 \stemDown b'8 r8 \stemDown ais8 r8 \stemDown gis8 r8 |
    \barNumberCheck #350
    \stemDown fis8 r8 \stemDown e8 r8 \stemDown dis8 r8 \stemUp cis8 r8
    | % 351
    \stemUp b8 r8 r4 r2 | % 352
    R1*3 \bar "|."
    }

PartPOneSevenVoiceFive =  \relative e {
    \clef "bass" \time 4/4 \key d \major \transposition c | % 1
    e1 ~ _\pp | % 2
    \stemDown e2 \stemDown dis2 ~ _\markup{ \italic {cresc.} } \change
    Staff="1" \change Staff="2" _\markup{ \italic {cresc.} } | % 3
    \stemDown dis2 \stemDown d2 ~ | % 4
    \stemDown d2 \stemUp cis4 \stemUp c4 | % 5
    b1 ~ _\sf _\> | % 6
    \stemUp b8 _\! _\p r8 r4 r2 | % 7
    e1 ~ _\pp | % 8
    \stemDown e2 \stemDown dis2 ~ _\markup{ \italic {cresc.} } \change
    Staff="1" \change Staff="2" _\markup{ \italic {cresc.} } | % 9
    \stemDown dis2 \stemDown d2 ~ | \barNumberCheck #10
    \stemDown d2 ( \stemUp c4 \stemUp b4 ) | % 11
    ais1 ~ _\sf _\> \break | % 12
    \stemUp ais8 _\! _\p r8 r4 r2 | % 13
    R1*4 | % 17
    ais1 ~ _\mf _\> | % 18
    \stemUp ais2 ~ \stemUp ais8 _\! _\pp r8 r4 ^\fermata \bar "||"
    R1*5 \pageBreak | % 24
    R1*4 | % 28
    r2 r4 r8 \stemUp b8 ~ _\p | % 29
    \stemUp b8 \stemUp g8 ~ \stemUp g4 ~ _\> \stemUp g8 _\! _\pp r8 r4 |
    \barNumberCheck #30
    \time 2/4  R2 \break | % 31
    \time 4/4  R1*6 \break | % 37
    R1*2 | % 39
    \stemUp g2 _\ff _\> \stemUp a2 | \barNumberCheck #40
    \stemUp b2 ~ \stemUp b8 _\! _\mf r8 r4 | % 41
    r2 r8 \stemDown a'16 -. _\p \stemDown a16 -. \stemDown a8 -.
    \stemDown a8 -. | % 42
    \stemDown fis2 ~ \stemDown fis8 \stemDown g8 ( _\pp \stemDown fis8
    \stemDown e8 | % 43
    \stemUp d8 ) \stemUp cis8 ( \stemUp b8 \stemUp a8 \stemUp g8 )
    \stemUp fis8 ( \stemUp e8 \stemUp e'8 ) \pageBreak | % 44
    \stemDown d2 ~ \stemDown d8 r8 r4 | % 45
    R1 | % 46
    r2 r8 \stemDown d'8 ( _\p \stemDown cis8 \stemDown b8 | % 47
    \stemDown a8 ) \stemDown gis8 ( \stemDown fis8 \stemDown e8
    \stemDown d8 ) \stemDown cis8 ( \stemDown b8 \stemDown b'8 ) | % 48
    \stemDown a2 ~ \stemDown a8 r8 r4 | % 49
    r2 r4 r8 \stemDown bis8 _\p \break | \barNumberCheck #50
    R1*4 \pageBreak | % 54
    R1*5 \break | % 59
    R1*5 \pageBreak | % 64
    R1*5 \pageBreak | % 69
    R1*5 \pageBreak | % 74
    R1*4 \break | % 78
    R1*5 \pageBreak | % 83
    R1*6 \bar "||"
    R1*5 \break | % 94
    R1*7 \bar "||"
    R1*2 \pageBreak | % 103
    R1*2 s1*1/640 R1*3 \break | % 108
    R1*4 \pageBreak | % 112
    R1*4 \break | % 116
    R1*4 \pageBreak | \barNumberCheck #120
    R1*5 \break | % 125
    R1*5 \bar "||"
    \time 12/8  s1*239/640 r1 s1*13/24 r1 s1*1/12 \pageBreak s4 r1
    s1*2/3 r1 s2 r1 s1*7/12 r1 s2 r1 s2 r1 \pageBreak s1*5/12 r1 s1*7/12
    r1 s2 r1 s2 r1 \bar "||"
    s1*11/24 r1 s1*1/24 | % 143
    \numericTimeSignature\time 4/4  R1*2 \break | % 145
    R1*11 \pageBreak | % 156
    R1*5 \bar "||"
    \key c \major R1*4 \pageBreak | % 165
    R1*7 \pageBreak | % 172
    R1*6 \pageBreak | % 178
    R1*5 \break | % 183
    R1*5 \pageBreak | % 188
    R1*4 \break | % 192
    R1*4 \pageBreak | % 196
    R1*5 \break | % 201
    R1*6 \pageBreak | % 207
    R1*6 \pageBreak | % 213
    R1*4 \break | % 217
    R1*4 \pageBreak | % 221
    R1*5 \break | % 226
    R1*5 \break | % 231
    R1*6 \pageBreak | % 237
    R1*5 \pageBreak | % 242
    R1*4 \pageBreak | % 246
    R1*6 \break | % 252
    R1*5 \pageBreak | % 257
    R1*6 \pageBreak | % 263
    R1*5 \pageBreak | % 268
    R1*5 \pageBreak | % 273
    R1*12 \pageBreak | % 285
    R1*17 \break | % 302
    R1*3 \bar "||"
    \pageBreak | % 305
    \key b \major R1*6 \pageBreak | % 311
    R1*6 \pageBreak | % 317
    R1*9 \break | % 326
    R1*8 \pageBreak | % 334
    R1 \bar "||"
    R1*8 \pageBreak | % 343
    R1*12 \bar "|."
    }

PartPOneSevenVoiceTwo =  \relative cis {
    \clef "bass" \time 4/4 \key d \major \transposition c s1*11 \break
    s1*7 \bar "||"
    s1*5 \pageBreak s1*6 | \barNumberCheck #30
    \time 2/4  s2 \break | % 31
    \time 4/4  s1*6 \break s1*7 \pageBreak s1*6 \break s1*4 \pageBreak
    s1*5 \break s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*4
    \break s1*5 \pageBreak s1*6 \bar "||"
    s1*5 \break s1*7 \bar "||"
    s1*2 \pageBreak s1*5 \break s1*4 \pageBreak s1*4 \break s1*4
    \pageBreak s1*5 \break s1*5 \bar "||"
    \time 12/8  s1*3 \pageBreak s1*9 \pageBreak s1*6 \bar "||"
    s1. | % 143
    \numericTimeSignature\time 4/4  s1*2 \break s1*11 \pageBreak s1*5
    \bar "||"
    \key c \major s1*4 \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*5
    \break s1*5 \pageBreak s1*4 \break s1*4 \pageBreak s1*5 \break s1*6
    \pageBreak s1*6 \pageBreak s1 | % 214
    r8 r16 \stemDown cis16 -. \stemDown cis16 ( \stemDown d16 \stemDown
    cis8 ) r8 r16 \stemDown cis16 -. \stemDown cis16 ( \stemDown d16
    \stemDown cis8 ) | % 215
    r8 r16 \stemDown cis16 -. \stemDown cis16 ( \stemDown d16 \stemDown
    cis8 ) r8 r16 \stemDown cis16 -. \stemDown cis16 ( \stemDown d16
    \stemDown cis8 ) | % 216
    r8 r16 \stemDown cis16 -. \stemDown cis16 ( \stemDown d16 \stemDown
    cis8 ) r8 r16 \stemDown cis16 -. \stemDown cis16 ( \stemDown d16
    \stemDown cis8 ) \break | % 217
    r8 r16 \stemDown cis16 -. \stemDown cis16 ( \stemDown d16 \stemDown
    cis8 ) r8 r16 \stemDown cis16 -. \stemDown cis16 ( \stemDown d16
    \stemDown cis8 ) s1*3 \pageBreak s1*5 \break s1*5 \break s1*6
    \pageBreak s1*5 \pageBreak s1*4 \pageBreak s1*6 \break s1*5
    \pageBreak s1*6 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*12
    \pageBreak s1*17 \break s1*3 \bar "||"
    \pageBreak | % 305
    \key b \major s1*6 \pageBreak s2*5 \stemDown b2 | % 314
    \stemDown b2 \stemDown b2 | % 315
    \stemDown b2 \stemDown eis,2 | % 316
    \stemDown fis2 \stemDown fis2 \pageBreak | % 317
    \stemDown b2 \stemDown b2 ~ | % 318
    \stemDown b2 \stemDown b2 ~ | % 319
    \stemDown b2 \stemDown b2 ~ | \barNumberCheck #320
    \stemDown b2 \stemDown b2 ~ | % 321
    \stemDown b2 \stemDown b2 ~ | % 322
    \stemDown b2 \stemDown b2 ~ | % 323
    \stemDown b2 \stemDown b2 ~ | % 324
    \stemDown b2 \stemDown b2 ~ | % 325
    \stemDown b2 ~ \stemDown b8 s4. \break s1*8 \pageBreak s1 \bar "||"
    s1*8 \pageBreak s1*12 \bar "|."
    }


% The score definition
\score {
    <<
        
        \new StaffGroup
        <<
            \new Staff
            <<
                \set Staff.instrumentName = "Flauto piccolo"
                \set Staff.shortInstrumentName = "Picc."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneVoiceOne" {  \PartPOneVoiceOne }
                    >>
                >>
            \new PianoStaff
            <<
                \set PianoStaff.instrumentName = "Flauti"
                \set PianoStaff.shortInstrumentName = "Fl."
                
                \context Staff = "1" << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPTwoVoiceOne" {  \voiceOne \PartPTwoVoiceOne }
                    \context Voice = "PartPTwoVoiceTwo" {  \voiceTwo \PartPTwoVoiceTwo }
                    >> \context Staff = "2" <<
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPTwoVoiceFive" {  \voiceOne \PartPTwoVoiceFive }
                    \context Voice = "PartPTwoVoiceSix" {  \voiceTwo \PartPTwoVoiceSix }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Oboi"
                \set Staff.shortInstrumentName = "Ob."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPThreeVoiceOne" {  \voiceOne \PartPThreeVoiceOne }
                    \context Voice = "PartPThreeVoiceTwo" {  \voiceTwo \PartPThreeVoiceTwo }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Clarinetti in A"
                \set Staff.shortInstrumentName = "Cl."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPFourVoiceOne" {  \voiceOne \PartPFourVoiceOne }
                    \context Voice = "PartPFourVoiceTwo" {  \voiceTwo \PartPFourVoiceTwo }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Fagotti"
                \set Staff.shortInstrumentName = "Fag."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPFiveVoiceOne" {  \voiceOne \PartPFiveVoiceOne }
                    \context Voice = "PartPFiveVoiceTwo" {  \voiceTwo \PartPFiveVoiceTwo }
                    >>
                >>
            \new StaffGroup \with { systemStartDelimiter =
                #'SystemStartBrace }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = "Corni in F I II"
                    \set Staff.shortInstrumentName = \markup { \center-column { \line {"Cor."} \line {"I II"} } }
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPSixVoiceOne" {  \voiceOne \PartPSixVoiceOne }
                        \context Voice = "PartPSixVoiceTwo" {  \voiceTwo \PartPSixVoiceTwo }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Corni in F III IV"
                    \set Staff.shortInstrumentName = \markup { \center-column { \line {"Cor."} \line {"III IV"} } }
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPSevenVoiceOne" {  \voiceOne \PartPSevenVoiceOne }
                        \context Voice = "PartPSevenVoiceTwo" {  \voiceTwo \PartPSevenVoiceTwo }
                        >>
                    >>
                
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Trombe in B"
                \set Staff.shortInstrumentName = "Tr."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPEightVoiceOne" {  \voiceOne \PartPEightVoiceOne }
                    \context Voice = "PartPEightVoiceTwo" {  \voiceTwo \PartPEightVoiceTwo }
                    >>
                >>
            \new StaffGroup \with { systemStartDelimiter =
                #'SystemStartBrace }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = \markup { \center-column { \line {"Tromboni"} \line {"Alto e Tenore"} } }
                    \set Staff.shortInstrumentName = \markup { \center-column { \line {"Tbni."} \line {"A. T."} } }
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPNineVoiceOne" {  \voiceOne \PartPNineVoiceOne }
                        \context Voice = "PartPNineVoiceTwo" {  \voiceTwo \PartPNineVoiceTwo }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Trombone basso"
                    \set Staff.shortInstrumentName = \markup { \center-column { \line {"Tbn."} \line {"B."} } }
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneZeroVoiceOne" {  \voiceOne \PartPOneZeroVoiceOne }
                        \context Voice = "PartPOneZeroVoiceTwo" {  \voiceTwo \PartPOneZeroVoiceTwo }
                        >>
                    >>
                
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Tuba"
                \set Staff.shortInstrumentName = "Tuba"
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneOneVoiceOne" {  \voiceOne \PartPOneOneVoiceOne }
                    \context Voice = "PartPOneOneVoiceTwo" {  \voiceTwo \PartPOneOneVoiceTwo }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Timpani in A, E, Es"
                \set Staff.shortInstrumentName = "Timp."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneTwoVoiceOne" {  \voiceOne \PartPOneTwoVoiceOne }
                    \context Voice = "PartPOneTwoVoiceTwo" {  \voiceTwo \PartPOneTwoVoiceTwo }
                    >>
                >>
            \new StaffGroup \with { systemStartDelimiter =
                #'SystemStartBrace }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = "Violino I"
                    \set Staff.shortInstrumentName = "Vl. I"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneThreeVoiceOne" {  \voiceOne \PartPOneThreeVoiceOne }
                        \context Voice = "PartPOneThreeVoiceTwo" {  \voiceTwo \PartPOneThreeVoiceTwo }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Violino II"
                    \set Staff.shortInstrumentName = "Vl. II"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneFourVoiceOne" {  \voiceOne \PartPOneFourVoiceOne }
                        \context Voice = "PartPOneFourVoiceTwo" {  \voiceTwo \PartPOneFourVoiceTwo }
                        >>
                    >>
                
                >>
            \new PianoStaff
            <<
                \set PianoStaff.instrumentName = "Viola"
                \set PianoStaff.shortInstrumentName = "Vla."
                
                \context Staff = "1" << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneFiveVoiceOne" {  \voiceOne \PartPOneFiveVoiceOne }
                    \context Voice = "PartPOneFiveVoiceTwo" {  \voiceTwo \PartPOneFiveVoiceTwo }
                    >> \context Staff = "2" <<
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneFiveVoiceFive" {  \PartPOneFiveVoiceFive }
                    >>
                >>
            \new PianoStaff
            <<
                \set PianoStaff.instrumentName = "Violoncello"
                \set PianoStaff.shortInstrumentName = "Vc."
                
                \context Staff = "1" << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneSixVoiceOne" {  \voiceOne \PartPOneSixVoiceOne }
                    \context Voice = "PartPOneSixVoiceTwo" {  \voiceTwo \PartPOneSixVoiceTwo }
                    >> \context Staff = "2" <<
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneSixVoiceFive" {  \PartPOneSixVoiceFive }
                    >>
                >>
            \new PianoStaff
            <<
                \set PianoStaff.instrumentName = "Basso"
                \set PianoStaff.shortInstrumentName = "Cb."
                
                \context Staff = "1" << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneSevenVoiceOne" {  \voiceOne \PartPOneSevenVoiceOne }
                    \context Voice = "PartPOneSevenVoiceTwo" {  \voiceTwo \PartPOneSevenVoiceTwo }
                    >> \context Staff = "2" <<
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneSevenVoiceFive" {  \PartPOneSevenVoiceFive }
                    >>
                >>
            
            >>
        
        >>
    \layout {}
    % To create MIDI output, uncomment the following line:
    %  \midi {\tempo 4 = 54 }
    }

