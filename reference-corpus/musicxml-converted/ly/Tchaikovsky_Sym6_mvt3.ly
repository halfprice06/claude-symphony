\version "2.24.3"
% automatically converted by musicxml2ly from ../xml/Tchaikovsky_Sym6_mvt3.musicxml
\pointAndClickOff

%% additional definitions required by the score:
 leggieramente = #(make-dynamic-script " leggieramente")
 leggiero = #(make-dynamic-script " leggiero")
 marcato = #(make-dynamic-script " marcato")
leggieramente = #(make-dynamic-script "leggieramente")
sempre  = #(make-dynamic-script "sempre ")

\header {
    title =  III
    encodingsoftware =  "MuseScore 4.1.0"
    encodingdate =  "2023-07-21"
    source =  "http://musescore.com/user/32958498/scores/6997800"
    }

#(set-global-staff-size 10.285714285714286)
\paper {
    
    paper-width = 21.59\cm
    paper-height = 27.94\cm
    top-margin = 1.0\cm
    bottom-margin = 1.4\cm
    left-margin = 1.0\cm
    right-margin = 1.0\cm
    indent = 2.491153846153846\cm
    short-indent = 1.245576923076923\cm
    }
\layout {
    \context { \Score
        skipBars = ##t
        }
    }
PartPOneVoiceOne =  \relative e''' {
    \clef "treble" \time 4/4 \key g \major | % 1
    \tempo "Allegro molto vivace" 4=152 R1*2 _ "Flutes" | % 3
    \time 12/8  \stemDown e8 -. _\p \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. | % 4
    r1 s2 \pageBreak | % 5
    r1 _ "Fl." s2 | % 6
    r1 s2 | % 7
    \stemDown c8 -. _\p \stemDown b8 -. \stemDown c8 -. \stemDown b8 -.
    \stemDown c8 -. \stemDown b8 -. \stemDown c8 -. \stemDown b8 -.
    \stemDown c8 -. \stemDown b8 -. \stemDown c8 -. \stemDown b8 -. \bar
    "||"
    r1 s2 | % 9
    r1 s2 \pageBreak | \barNumberCheck #10
    r1 s2 | % 11
    r1 s2 | % 12
    r1 s2 | % 13
    r1 s2 | % 14
    r1 s2 \break | % 15
    r1 s2 | % 16
    r1 s2 | % 17
    r1 s2 | % 18
    r1 s2 | % 19
    r1 s2 \pageBreak | \barNumberCheck #20
    r1 s2 | % 21
    r1 s2 | % 22
    r1 s2 | % 23
    r1 s2 \break | % 24
    r1 _ "Fl." s2 | % 25
    r1 s2 | % 26
    r1 s2 | % 27
    \numericTimeSignature\time 4/4  d1 ~ _\pp _\< \pageBreak | % 28
    \stemDown d8 _\! _ "Fl." r8 \stemDown d8 -. _\p _\< r16 \stemDown d16
    -. \stemDown dis8 -. r8 \stemDown e8 -. r8 | % 29
    \stemDown a,8 -. _\! _\mp r8 r4 r2 | \barNumberCheck #30
    R1*2 \pageBreak | % 32
    R1*4 \pageBreak | % 36
    R1*3 _ "Fl." | % 39
    \time 12/8  \stemDown e'8 -. _\p \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. | \barNumberCheck #40
    \stemDown e8 ( -> \stemDown d8 \stemDown c8 \stemDown b8 \stemDown a8
    \stemDown g8 ) r2.*2/3 s4 \pageBreak | % 41
    r1 _ "Fl." s2 | % 42
    r1 s2 | % 43
    \stemDown e'8 -. _\mp \stemDown d8 -. \stemDown e8 -. \stemDown d8
    -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -. \stemDown d8 -.
    \stemDown e8 -. \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. | % 44
    \stemDown e8 ( -> \stemDown d8 \stemDown c8 \stemDown b8 \stemDown a8
    \stemDown g8 ) r2.*2/3 s4 | % 45
    \stemDown es'4. _\f -\markup{ \italic {marcato} } \stemDown d4.
    \stemDown c4. \stemDown bes4 ( ~ \stemDown bes16 \stemDown as16
    \pageBreak | % 46
    \stemDown g8 ) _ "Fl." r8*2/3 r8*2/3 r4.*2/3 r4.*2/3 \stemDown d'8
    _\f \stemDown d8 \stemDown d8 s1*1/3 | % 47
    \stemDown bes8 ( \stemDown c8 \stemDown d8 \stemDown es8 \stemDown d8
    \stemDown c8 \stemDown bes8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 | % 48
    r1 s2 | % 49
    \stemDown b4. _\ff -\markup{ \italic {marcato} } \stemDown ais4.
    \stemDown gis4. \stemDown fis4 ( ~ \stemDown fis16 \stemDown e16 |
    \barNumberCheck #50
    \stemDown dis8 ) r8*2/3 r8*2/3 r4.*2/3 r4.*2/3 \stemDown ais'8 _\ff
    \stemDown ais8 \stemDown ais8 s1*1/3 \pageBreak | % 51
    \stemDown fis8 ( _ "Fl." \stemDown gis8 \stemDown ais8 \stemDown b8
    \stemDown ais8 \stemDown gis8 \stemDown fis8 ) r8*2/3 r8*2/3 r4.*2/3
    s1*5/24 | % 52
    r1 s2 | % 53
    r1 s2 | % 54
    r1 s2 | % 55
    \numericTimeSignature\time 4/4  r2 \stemDown fis4 ^> _\mf \stemDown
    fis8 r16 \stemDown fis16 \pageBreak | % 56
    \stemUp fis,8 _ "Fl." r8 r4 \stemDown fis''4 -> _\ff \stemDown fis8
    r16 \stemDown fis16 | % 57
    \stemDown fis,8 _\pp r8 r4 r2 | % 58
    R1 | % 59
    r2 \stemDown fis4 ^> _\mf \stemDown fis8 r16 \stemDown fis16 |
    \barNumberCheck #60
    \stemUp fis,8 r8 r4 \stemDown fis''4 -> _\f \stemDown fis8 r16
    \stemDown fis16 \pageBreak | % 61
    b,1 -> _\p _ "Fl." _\markup{ \small\italic {poco a poco cresc.} }
    \startTrillSpan | % 62
    g1 -> | % 63
    b1 -> | % 64
    g1 -> | % 65
    b1 -> \pageBreak | % 66
    c1 -> _ "Fl." | % 67
    dis1 -> \stopTrillSpan _\f _\markup{ \small\italic {cresc.} }
    \startTrillSpan | % 68
    g1 -> | % 69
    \stemDown b8 -> \stopTrillSpan _\ff r8 r4 r2 | \barNumberCheck #70
    R1 \bar "||"
    \pageBreak | % 71
    \key e \major R1*5 \break | % 76
    R1*3 _ "Fl." | % 79
    r4 r8 r16 \stemUp gis,,16 ( _\mp _\< \stemDown cis8 ) r16 \stemDown
    dis16 ( \stemDown e8 ) r16 \stemDown fis16 -. | \barNumberCheck #80
    \stemDown gis2 ~ _\! _\mf _\< \stemDown gis8 \stemDown fis16 ( _\!
    _\ff _\> \stemDown e16 \once \omit TupletBracket
    \times 4/6  {
        \stemUp dis16 \stemUp cis16 \stemUp b16 \stemUp a16 \stemUp gis16
        \stemUp fis16 }
    \pageBreak | % 81
    \stemUp e8 ) _\! _\p _ "Fl." r8 r4 r2 | % 82
    R1*4 \pageBreak | % 86
    r2 _ "Fl." r4 \stemUp gis8 ( -. _\mf r16 \stemUp b16 ) -. | % 87
    \stemDown c4 ( -> _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp b8 ) r16 \stemUp a16 -. \stemUp g8 -. r8 \stemDown d'8 ( -.
    r16 \stemDown dis16 ) -. | % 88
    \stemDown e4 ( -> \stemDown d8 ) r16 \stemDown c16 -. \stemDown b8
    -. r8 \stopTrillSpan r4 | % 89
    R1 \pageBreak | \barNumberCheck #90
    R1*5 _ "Fl." | % 95
    r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp e,8 _\ff \stemUp e8 \stemUp e8 }
    \stemUp e2 ~ \pageBreak | % 96
    \stemUp e8 _ "Fl." r8 \stemUp fis8 r16 \stemUp dis16 \stemUp e8 r8 r4
    | % 97
    R1*2 | % 99
    r4 \stemDown dis''16 ( _\mf \stemDown e16 \stemDown dis16 \stemDown
    e16 \stemDown cis8 ) r8 \stemDown fisis,16 ( \stemDown gis16
    \stemDown fisis16 \stemDown gis16 ) | \barNumberCheck #100
    \stemDown a16 ( \stemDown b16 \stemDown a16 \stemDown gis16 )
    \stemDown fis16 ( \stemDown gis16 \stemDown fis16 \stemDown e16 )
    \stemDown dis16 ( \stemDown e16 \stemDown cis16 \stemDown dis16
    \stemDown b8 ) r8 | % 101
    R1 \break | % 102
    r2 _ "Fl." r4 \stemDown gis''16 ( _\mf \stemDown a16 \stemDown gis16
    \stemDown a16 | % 103
    \stemDown e8 ) r8 \stemDown bis16 ( \stemDown cis16 \stemDown bis16
    \stemDown cis16 \stemDown a8 ) r8 \stemDown e'16 ( \stemDown eis16
    \stemDown e16 \stemDown eis16 ) | % 104
    \stemDown fis16 ( \stemDown gis16 \stemDown fis16 \stemDown e16 )
    \stemDown dis16 ( \stemDown e16 \stemDown dis16 \stemDown cis16 )
    \stemDown b16 ( \stemDown cis16 \stemDown a16 \stemDown b16
    \stemDown gis8 ) r8 | % 105
    R1*2 \pageBreak | % 107
    r4 \stemDown dis'16 ( _\mf _ "Fl." \stemDown e16 \stemDown dis16
    \stemDown e16 \stemDown cis8 ) r8 \stemDown fisis,16 ( \stemDown gis16
    \stemDown fisis16 \stemDown gis16 ) | % 108
    \stemDown a16 ( \stemDown b16 \stemDown a16 \stemDown gis16 )
    \stemDown fis16 ( \stemDown gis16 \stemDown fis16 \stemDown e16 )
    \stemDown dis16 ( \stemDown e16 \stemDown cis16 \stemDown dis16
    \stemDown b8 ) r8 | % 109
    R1*4 \break | % 113
    R1*5 \pageBreak | % 118
    R1*3 _ "Fl." | % 121
    r4 r8 r16 \stemUp gis16 ( _\mp _\< \stemDown cis8 ) r16 \stemDown
    dis16 ( \stemDown e8 ) r16 \stemDown fis16 -. | % 122
    \stemDown gis2 ~ _\! _\mf _\< \stemDown gis8 \stemDown fis16 ( _\!
    _\ff _\> \stemDown e16 \once \omit TupletBracket
    \times 4/6  {
        \stemUp dis16 \stemUp cis16 \stemUp b16 \stemUp a16 \stemUp gis16
        \stemUp fis16 }
    \break | % 123
    \stemUp e8 ) _\! _\p _ "Fl." r8 r4 r2 | % 124
    R1*4 \pageBreak | % 128
    r2 _ "Fl." r4 \stemUp gis8 ( -. _\f r16 \stemUp b16 ) -. | % 129
    \stemDown c4 ( -> \stemUp b8 ) r16 \stemUp a16 -. \stemUp g8 -. r8
    \stemDown d'8 ( -. r16 \stemDown dis16 ) -. | \barNumberCheck #130
    \stemDown e4 ( -> \stemDown d8 ) r16 \stemDown c16 -. \stemUp b8 -.
    \stemUp g8 ( \stemUp a8 \stemUp b8 ) | % 131
    \stemDown c8 ( \stemDown d8 \stemDown e8 \stemDown fis8 ) \stemDown
    g8 ( \stemDown a8 \stemDown ais8 \stemDown b8 ) \pageBreak | % 132
    \stemDown c8 ( _ "Fl." \stemDown d8 \stemDown e8 \stemDown fis8
    \stemDown g8 ) r8 r4 | % 133
    \stemDown c,,4 ( -> \stemUp b8 ) r16 \stemUp a16 -. \stemUp g8 -. r8
    \stemDown d'8 ( -. r16 \stemDown dis16 ) -. | % 134
    \stemDown e4 ( -> \stemDown d8 ) r16 \stemDown c16 -. \stemUp b8 -.
    \stemUp g8 ( \stemUp a8 \stemUp b8 ) | % 135
    \stemDown c8 ( \stemDown d8 \stemDown e8 \stemDown fis8 ) \stemDown
    g8 ( \stemDown a8 \stemDown ais8 \stemDown b8 ) \pageBreak | % 136
    \stemDown c8 ( _ "Fl." \stemDown d8 \stemDown e8 \stemDown fis8
    \stemDown g8 ) r8 r4 | % 137
    \time 12/8  r4.*2/3 r8*2/3 \stemDown b,8 -. _\f \stemDown d8 -.
    \stemDown e8 ( \stemDown d8 ) \stemDown c8 -. \stemDown b8 -. r8*2/3
    r8*2/3 s4 | % 138
    r4.*2/3 r8*2/3 \stemDown b8 -. _\mf \stemDown d8 -. \stemDown e8 (
    \stemDown d8 ) \stemDown c8 -. \stemDown b8 -. r4*2/3 \bar "||"
    s4 | % 139
    \key g \major r1 s2 \pageBreak | \barNumberCheck #140
    r1 _ "Fl." s2 | % 141
    \stemDown e8 -. _\p \stemDown d8 -. \stemDown e8 -. \stemDown d8 -.
    \stemDown e8 -. \stemDown d8 -. \stemDown e8 -. \stemDown d8 -.
    \stemDown e8 -. \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. | % 142
    r1 s2 | % 143
    r1 s2 | % 144
    r1 s2 \pageBreak | % 145
    \stemDown c8 -. _\p _ "Fl." \stemDown b8 -. \stemDown c8 -.
    \stemDown b8 -. \stemDown c8 -. \stemDown b8 -. \stemDown c8 -.
    \stemDown b8 -. \stemDown c8 -. \stemDown b8 -. \stemDown c8 -.
    \stemDown b8 -. | % 146
    r1 s2 | % 147
    r1 s2 | % 148
    r1 s2 | % 149
    r1 s2 \pageBreak | \barNumberCheck #150
    r1 s2 | % 151
    r1 s2 | % 152
    r1 s2 | % 153
    r1 s2 | % 154
    r1 s2 \pageBreak | % 155
    r1 s2 | % 156
    r1 s2 | % 157
    r1 s2 | % 158
    r1 s2 \break | % 159
    r1 s2 | \barNumberCheck #160
    r1 s2 | % 161
    r1 s2 | % 162
    r1 s2 \pageBreak | % 163
    r1 _ "Fl." s2 | % 164
    r1 s2 | % 165
    \numericTimeSignature\time 4/4  d1 ~ _\pp _\< | % 166
    \stemDown d8 r8 \stemDown d8 -. _\! _\p _\< r16 \stemDown d16 -.
    \stemDown dis8 -. r8 \stemDown e8 -. r8 \pageBreak | % 167
    \stemDown a,8 -. _\! _\mp _ "Fl." r8 r4 r2 | % 168
    R1*3 \pageBreak | % 171
    R1*4 \pageBreak | % 175
    R1*2 _ "Fl." | % 177
    \time 12/8  \stemDown e'8 -. _\p \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. | % 178
    \stemDown e8 ( -> \stemDown d8 \stemDown c8 \stemDown b8 \stemDown a8
    \stemDown g8 ) r2.*2/3 s4 | % 179
    r1 s2 \pageBreak | \barNumberCheck #180
    r1 _ "Fl." s2 | % 181
    \stemDown e'8 -. _\mp \stemDown d8 -. \stemDown e8 -. \stemDown d8
    -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -. \stemDown d8 -.
    \stemDown e8 -. \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. | % 182
    \stemDown e8 ( -> \stemDown d8 \stemDown c8 \stemDown b8 \stemDown a8
    \stemDown g8 ) r2.*2/3 s4 | % 183
    \stemDown es'4. _\f _\ marcato \stemDown d4. \stemDown c4. \stemDown
    bes4 ( ~ \stemDown bes16 \stemDown as16 \pageBreak | % 184
    \stemDown g8 ) _ "Fl." r8*2/3 r8*2/3 r4.*2/3 r4.*2/3 \stemDown d'8
    \stemDown d8 \stemDown d8 s1*1/3 | % 185
    \stemDown bes8 ( \stemDown c8 \stemDown d8 \stemDown es8 \stemDown d8
    \stemDown c8 \stemDown bes8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 | % 186
    r1 s2 | % 187
    \stemDown g'4. _\ff \stemDown f4. \stemDown es4. \stemDown d4 ( ~
    \stemDown d16 \stemDown c16 ) | % 188
    \stemDown bes8 r8*2/3 r8*2/3 r4.*2/3 r4.*2/3 \stemDown f'8 \stemDown
    f8 \stemDown f8 s1*1/3 \pageBreak | % 189
    \stemDown d8 ( _ "Fl." \stemDown es8 \stemDown f8 \stemDown g8
    \stemDown f8 \stemDown es8 \stemDown d8 ) r8*2/3 r8*2/3 r4.*2/3
    s1*5/24 | \barNumberCheck #190
    r1 s2 | % 191
    \numericTimeSignature\time 4/4  \stemDown g8 ( _\ff \stemDown fis8
    \stemDown e8 \stemDown d8 ) r2 | % 192
    \stemDown g8 ( _\ff \stemDown f8 \stemDown e8 \stemDown d8 ) r2 | % 193
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 ( _\ff \stemDown fis8 \stemDown e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown cis8 \stemDown b8 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 ( \stemDown g8 \stemDown fis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown d8 \stemDown cis8 ) }
    \pageBreak | % 194
    \stemUp b16 ( _ "Fl." \stemUp a16 \stemUp g16 \stemUp fis16 \stemUp
    e16 \stemUp d16 ) r8 \stemUp a'8 r8 r4 | % 195
    R1*5 | \barNumberCheck #200
    \stemDown d8 ^\leggieramente _\pp r8 \stemUp a8 r16 \stemUp a16
    \stemDown d8 r8 \stemUp a8 r8 \pageBreak | % 201
    \stemDown e'8 -> _ "Fl." \stemDown a8 -> r4 r2 | % 202
    R1*2 | % 204
    \stemDown d8 _\p _\< r8 \stemDown a8 r16 \stemDown a16 \stemDown d8
    r8 \stemDown a8 r8 | % 205
    \stemDown d8 -> _\! _\mp \stemDown a'8 -> r4 r2 \pageBreak | % 206
    R1*2 _ "Fl." | % 208
    \stemDown g,8 _\mf r8 \stemDown d8 r16 \stemDown d16 \stemDown g8 r8
    \stemDown d8 r8 | % 209
    \stemDown a'8 -> \stemDown d8 -> r4 r2 | \barNumberCheck #210
    \stemDown e,8 _\f r8 \stemDown b8 r16 \stemDown b16 \stemDown e8 r8
    \stemDown b8 r8 \pageBreak | % 211
    \stemDown e8 -> _ "Fl." \stemDown a8 -> r4 r2 | % 212
    \stemDown g'8 _\ff r8 \stemDown d8 r16 \stemDown d16 \stemDown g8 r8
    \stemDown d8 r8 | % 213
    \stemDown a'8 -> \stemDown d,8 -> r4 r2 | % 214
    \stemDown a8 _\fff r8 \stemDown e8 r16 \stemDown e16 \stemDown a8 r8
    \stemDown e8 r8 | % 215
    \stemDown a8 -> \stemDown d8 ~ -> \stemDown d2. \pageBreak | % 216
    \stemDown a8 _\fff _ "Fl." r8 \stemDown e8 r16 \stemDown e16
    \stemDown a8 r8 \stemDown e8 r8 | % 217
    \stemDown a8 -> \stemDown d8 ~ -> \stemDown d8 \stemDown d8
    \stemDown a8 \stemDown e4 \stemDown e8 | % 218
    \stemDown a8 \stemDown d4 \stemDown d8 \stemDown a8 \stemDown e4
    \stemDown e8 | % 219
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 r8 }
    | \barNumberCheck #220
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 r8 }
    \pageBreak | % 221
    \times 2/3  {
        \stemDown a8 -> _ "Fl." \stemDown a8 -> r8 }
    r4 r2 | % 222
    r4 \stemDown d,32 ( _\sempre _\fff \stemDown e32 \stemDown fis32
    \stemDown g32 \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32
    ) \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16 )
    \stemDown a16 ( \stemDown g16 \stemDown fis16 \stemDown e16 ) | % 223
    \stemDown d16 ( \stemDown c16 \stemDown b16 \stemDown a16 ) \stemUp
    g16 ( \stemUp fis16 \stemUp e16 \stemUp d16 ) r2 | % 224
    r4 \stemDown d'32 ( \stemDown e32 \stemDown fis32 \stemDown g32
    \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32 ) \stemDown
    e16 ( \stemDown d16 \stemDown c16 \stemDown b16 ) \stemDown a16 (
    \stemDown g16 \stemDown fis16 \stemDown e16 ) \pageBreak | % 225
    \stemDown d16 ( _ "Fl." \stemDown c16 \stemDown b16 \stemDown a16 )
    \stemUp g16 ( \stemUp fis16 \stemUp e16 \stemUp d16 ) r4 \stemDown
    d'32 ( \stemDown e32 \stemDown fis32 \stemDown g32 \stemDown a32
    \stemDown b32 \stemDown c32 \stemDown d32 ) | % 226
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemDown fis8 ) r8 r4 \stemDown d32 ( \stemDown e32 \stemDown fis32
    \stemDown g32 \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32
    ) | % 227
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemDown fis8 ) r8 r4 \stemDown d32 ( \stemDown e32 \stemDown fis32
    \stemDown g32 \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32
    ) \pageBreak | % 228
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( _ "Fl." \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemDown fis8 ) r8 \once \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemUp fis8 ) r8 | % 229
    \stemDown g'8 _\fff r8 \stemDown d8 r16 \stemDown d16 \stemDown g8 r8
    \stemDown d8 r8 | \barNumberCheck #230
    \stemDown g8 -> \stemDown c8 ~ ^> \stemDown c2 \stemDown b8 r16
    \stemDown a16 | % 231
    \stemDown d8 r8 \acciaccatura { \stemUp a8 ( } \stemDown g8 ) r16
    \stemDown fis16 \stemDown g8 r8 \stemDown d8 r8 | % 232
    \stemDown g2. -> \stemDown b8 r16 \stemDown d16 \pageBreak | % 233
    \stemDown e8 _ "Fl." r8 \acciaccatura { \stemUp a,8 ( } \stemDown g8
    ) r16 \stemDown fis16 \stemDown g8 r8 \stemDown d8 r8 | % 234
    \stemDown g2. -> \stemDown b8 r16 \stemDown d16 | % 235
    \stemDown g4 ( -> \stemDown fis8 ) r16 \stemDown g16 \stemDown e4 (
    -> \stemDown dis8 ) r16 \stemDown e16 | % 236
    \stemDown c4 ( -> \stemDown b8 ) r16 \stemDown c16 \stemDown a4 ( ->
    \stemDown g8 ) r16 \stemDown a16 -. | % 237
    \stemDown e8 -. r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown b16
    ( \stemDown e8 ) r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown
    a16 -. \pageBreak | % 238
    \stemDown b2 ~ -> _ "Fl." \stemDown b8 \stemDown a16 ( \stemDown g16
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown c16
        \stemDown b16 \stemDown a16 }
    | % 239
    \stemDown g8 ) r8 \stemDown d8 r16 \stemDown d16 \stemDown g8 r8
    \stemDown d8 r8 | \barNumberCheck #240
    \stemDown g8 -> \stemDown c8 ~ ^> \stemDown c2 \stemDown b8 r16
    \stemDown a16 | % 241
    \stemDown d8 r8 \acciaccatura { \stemUp a8 ( } \stemDown g8 ) r16
    \stemDown fis16 \stemDown g8 r8 \stemDown d8 r8 | % 242
    \stemDown g2. -> \stemDown b8 r16 \stemDown d16 \pageBreak | % 243
    \stemDown e8 _ "Fl." r8 \acciaccatura { \stemUp a,8 ( } \stemDown g8
    ) r16 \stemDown fis16 \stemDown g8 r8 \stemDown d8 r8 | % 244
    \stemDown g2. -> \stemDown b8 r16 \stemDown d16 | % 245
    \stemDown es4 ( -> \stemDown d8 ) r16 \stemDown c16 \stemDown bes8 r8
    \stemDown f'8 r16 \stemDown fis16 | % 246
    \stemDown g4 ( -> \stemDown f8 ) r16 \stemDown es16 \stemDown d8 r8
    \stemDown g8 r16 \stemDown a16 | % 247
    \stemDown b2. -> \stemDown a8 r16 \stemDown b,16 \pageBreak | % 248
    \stemDown g'2. -> _ "Fl." \stemDown fis8 r16 \stemDown b,16 | % 249
    \stemDown e4 ( -> \stemDown d8 ) r16 \stemDown e,16 \stemDown c'4 (
    -> \stemDown b8 ) r16 \stemDown e,16 | \barNumberCheck #250
    \stemDown a4 ( -> \stemDown g8 ) r16 \stemDown g,16 \stemDown e'4 (
    -> \stemDown d8 ) r16 \stemDown gis,16 | % 251
    \stemDown c8 r8 r4 r2 | % 252
    R1 | % 253
    r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown b'8 _\fff \stemDown b8 \stemDown b8 }
    \stemDown b2 ~ \pageBreak | % 254
    \stemDown b8 _ "Fl." r8 \stemDown c8 r16 \stemDown fis,16 \stemDown
    g8 r8 r4 | % 255
    R1 | % 256
    r2 r4 \stemDown a'4 ( _\ff | % 257
    \stemDown d,8 ) r8 \stemDown fis16 ( \stemDown g16 \stemDown fis16
    \stemDown g16 \stemDown e8 ) r8 \stemDown ais,16 ( \stemDown b16
    \stemDown ais16 \stemDown b16 ) | % 258
    \stemDown c16 ( \stemDown d16 \stemDown c16 \stemDown b16 )
    \stemDown a16 ( \stemDown b16 \stemDown a16 \stemDown g16 )
    \stemDown fis16 ( \stemDown g16 \stemDown e16 \stemDown fis16
    \stemDown d8 ) r8 \pageBreak | % 259
    R1 _ "Fl." | \barNumberCheck #260
    r2 r4 \stemDown fis'4 ( _\ff | % 261
    \stemDown b,8 ) r8 \stemDown dis16 ( \stemDown e16 \stemDown dis16
    \stemDown e16 \stemDown c8 ) r8 \stemDown g16 ( \stemDown gis16
    \stemDown g16 \stemDown gis16 ) | % 262
    \stemDown a16 ( \stemDown b16 \stemDown a16 \stemDown g16 )
    \stemDown fis16 ( \stemDown g16 \stemDown fis16 \stemDown e16 )
    \stemDown d16 ( \stemDown e16 \stemDown c16 \stemDown d16 \stemDown
    b8 ) r8 | % 263
    R1 \pageBreak | % 264
    r2 _ "Fl." r4 \stemDown a''4 ( _\ff | % 265
    \stemDown d,8 ) r8 \stemDown fis16 ( \stemDown g16 \stemDown fis16
    \stemDown g16 \stemDown e8 ) r8 \stemDown ais,16 ( \stemDown b16
    \stemDown ais16 \stemDown b16 ) | % 266
    \stemDown c16 ( \stemDown d16 \stemDown c16 \stemDown b16 )
    \stemDown a16 ( \stemDown b16 \stemDown a16 \stemDown g16 )
    \stemDown fis16 ( \stemDown g16 \stemDown e16 \stemDown fis16
    \stemDown d8 ) r8 | % 267
    R1*2 \pageBreak | % 269
    R1 _ "Fl." | \barNumberCheck #270
    \stemDown b4 ~ _\fff \stemDown b8 r8 \stemDown b4 ~ \stemDown b8 r8
    | % 271
    \stemDown c4 ~ \stemDown c8 r8 \stemDown d4 ~ \stemDown d8 r8 | % 272
    \stemDown g4 ~ \stemDown g8 r8 \stemDown gis4 ~ \stemDown gis8 r8 | % 273
    \stemDown a8 r8 \stemDown bes8 r8 \stemDown b8 r8 \stemDown c8 r8
    \pageBreak | % 274
    \stemDown cis8 _ "Fl." r8 \stemDown d8 r8 \stemDown e8 r8 r4 | % 275
    R1*6 \pageBreak | % 281
    R1 _ "Fl." | % 282
    r2 r4 \stemDown d,16 ( _\fff \stemDown dis16 \stemDown e16 \stemDown
    fis16 | % 283
    \stemDown g8 ) r8 \stemDown d8 r16 \stemDown d16 \stemDown g8 r8
    \stemDown d8 r8 | % 284
    \stemDown g8 -> \stemDown c8 ~ ^> \stemDown c2 \stemDown b8 r16
    \stemDown a16 | % 285
    \stemDown d8 r8 \acciaccatura { \stemUp a8 ( } \stemDown g8 ) r16
    \stemDown fis16 \stemDown g8 r8 \stemDown d8 r8 | % 286
    \stemDown g2. -> \stemDown b8 r16 \stemDown d16 \pageBreak | % 287
    \stemDown e8 _ "Fl." r8 \acciaccatura { \stemUp a,8 ( } \stemDown g8
    ) r16 \stemDown fis16 \stemDown g8 r8 \stemDown d8 r8 | % 288
    \stemDown g2. -> \stemDown b8 r16 \stemDown d16 | % 289
    \stemDown g4 ( -> \stemDown fis8 ) r16 \stemDown g16 \stemDown e4 (
    -> \stemDown dis8 ) r16 \stemDown e16 | \barNumberCheck #290
    \stemDown c4 ( -> \stemDown b8 ) r16 \stemDown c16 \stemDown a4 ( ->
    \stemDown g8 ) r16 \stemDown a16 -. | % 291
    \stemDown e8 -. r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown b16
    ( \stemDown e8 ) r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown
    a16 -. \pageBreak | % 292
    \stemDown b2 ~ -> _ "Fl." \stemDown b8 \stemDown a16 ( \stemDown g16
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown c16
        \stemDown b16 \stemDown a16 }
    | % 293
    \stemDown g8 ) r8 \stemDown d8 r16 \stemDown d16 \stemDown g8 r8
    \stemDown d8 r8 | % 294
    \stemDown g8 -> \stemDown c8 ~ ^> \stemDown c2 \stemDown b8 r16
    \stemDown a16 | % 295
    \stemDown d8 r8 \acciaccatura { \stemUp a8 ( } \stemDown g8 ) r16
    \stemDown fis16 \stemDown g8 r8 \stemDown d8 r8 | % 296
    \stemDown g2. -> \stemDown b8 r16 \stemDown d16 \pageBreak | % 297
    \stemDown e8 _ "Fl." r8 \acciaccatura { \stemUp a,8 ( } \stemDown g8
    ) r16 \stemDown fis16 \stemDown g8 r8 \stemDown d8 r8 | % 298
    \stemDown g2. -> \stemDown b8 r16 \stemDown d16 | % 299
    \stemDown es4 ( -> \stemDown d8 ) r16 \stemDown c16 \stemDown bes8 r8
    \stemDown f'8 r16 \stemDown fis16 | \barNumberCheck #300
    \stemDown g4 ( -> \stemDown f8 ) r16 \stemDown es16 \stemDown d8 r8
    \stemDown g8 r16 \stemDown a16 | % 301
    \stemDown b2. -> \stemDown a8 r16 \stemDown b,16 \pageBreak | % 302
    \stemDown g'2. -> _ "Fl." \stemDown fis8 r16 \stemDown b,16 | % 303
    \stemDown e4 ( -> \stemDown d8 ) r16 \stemDown e,16 \stemDown c'4 (
    -> \stemDown b8 ) r16 \stemDown e,16 | % 304
    \stemDown a4 ( -> _\sempre _\fff \stemDown g8 ) r16 \stemDown e16
    \stemDown a4 ( -> \stemDown g8 ) r16 \stemDown es16 | % 305
    \stemDown a4 ( -> \stemDown g8 ) r16 \stemDown d16 \stemDown a'4 (
    -> \stemDown g8 ) r16 \stemDown cis,16 | % 306
    \stemDown a'4 ( -> \stemDown g8 ) r16 \stemDown c,16 \stemDown a'4 (
    -> \stemDown g8 ) r16 \stemDown cis,16 | % 307
    \stemDown a'4 ( -> \stemDown g8 ) r16 \stemDown d16 \stemDown a'4 (
    -> \stemDown g8 ) r16 \stemDown dis16 \pageBreak | % 308
    \stemDown b'4 ( -> _ "Fl." \stemDown a8 ) r16 \stemDown e16
    \stemDown c'4 ( -> \stemDown b8 ) r16 \stemDown e,16 | % 309
    \stemDown d'4 ( -> \stemDown c8 ) r16 \stemDown a16 \stemDown d4 (
    -> \stemDown cis8 ) r16 \stemDown a16 | \barNumberCheck #310
    \stemDown e'4 ( -> \stemDown d8 ) r16 \stemDown a16 \stemDown e'4 (
    -> \stemDown dis8 ) r16 \stemDown a16 | % 311
    \stemDown f'4 ( -> \stemDown e8 ) r16 \stemDown a,16 \stemDown g'4 (
    -> \stemDown fis8 ) r16 \stemDown c16 | % 312
    \stemDown a'8 ( _\ffff \stemDown g8 \stemDown d8 \stemDown g8 )
    \stemDown a8 ( \stemDown g8 \stemDown es8 \stemDown g8 ) | % 313
    \stemDown a8 ( \stemDown g8 \stemDown e8 \stemDown g8 ) \stemDown a8
    ( \stemDown g8 \stemDown es8 \stemDown g8 ) \pageBreak | % 314
    \stemDown a8 ( _ "Fl." \stemDown g8 \stemDown fis8 \stemDown e8 )
    \stemDown d8 ( \stemDown cis8 \stemDown c8 \stemDown b8 ) | % 315
    \stemDown a8 ( \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown d8
    ) r8 r4 | % 316
    R1*4 \pageBreak | \barNumberCheck #320
    R1*2 _ "Fl." | % 322
    g'1 ~ _\ff _\markup{ \small\italic {cresc.} } \startTrillSpan | % 323
    \stemDown g4 \stemDown fis4 \stemDown g4 \stemDown a4 | % 324
    \stemDown b8 \stopTrillSpan _\fff r8 \once \omit TupletBracket
    \times 4/7  {
        \stemDown g,16*161/160 ( \stemDown a16*161/160 \stemDown b16*161/160
        \stemDown cis16*161/160 \stemDown dis16*161/160 \stemDown e16*161/160
        \stemDown fis16*161/160 }
    \stemDown g8 ) r16 \stemDown fis16 -. \stemDown g8 -. r16 \stemDown
    dis16 -. \pageBreak | % 325
    \stemDown e8 -. _ "Fl." r8 \once \omit TupletBracket
    \times 4/7  {
        \stemDown c,16*161/160 ( \stemDown d16*161/160 \stemDown e16*161/160
        \stemDown fis16*161/160 \stemDown gis16*161/160 \stemDown a16*161/160
        \stemDown b16*161/160 }
    \stemDown c8 ) r16 \stemDown b16 -. \stemDown c8 -. r16 \stemDown
    gis16 -. | % 326
    \stemDown a8 -. r8 r4 r4 \once \omit TupletBracket
    \times 4/7  {
        \stemDown bes,16*161/160 ( \stemDown c16*161/160 \stemDown d16*161/160
        \stemDown es16*161/160 \stemDown f16*161/160 \stemDown g16*161/160
        \stemDown a16*161/160 }
    | % 327
    \stemDown bes8 ) r8 r4 r4 \once \omit TupletBracket
    \times 4/7  {
        \stemDown c,16*161/160 ( \stemDown d16*161/160 \stemDown e16*161/160
        \stemDown f16*161/160 \stemDown g16*161/160 \stemDown a16*161/160
        \stemDown b16*161/160 }
    \pageBreak | % 328
    \stemDown c8 ) _ "Fl." r8 r4 r4 \once \omit TupletBracket
    \times 4/7  {
        \stemDown d,16*161/160 ( \stemDown e16*161/160 \stemDown fis16*161/160
        \stemDown g16*161/160 \stemDown a16*161/160 \stemDown b16*161/160
        \stemDown cis16*161/160 }
    | % 329
    \stemDown d16 ) \stemDown e16 ( \stemDown fis16 \stemDown g16
    \stemDown a16 \stemDown g16 \stemDown fis16 \stemDown e16 )
    \stemDown d16 ( \stemDown c16 \stemDown b16 \stemDown a16 )
    \stemDown g16 ( \stemDown fis16 \stemDown e16 \stemDown d16 ) |
    \barNumberCheck #330
    \stemDown g8 _\sempre _\fff r8 \stemDown d8 r16 \stemDown d16
    \stemDown g8 r8 \stemDown c,8 r8 | % 331
    \stemDown g'8 -> \stemDown d'8 ^> \stemDown g,16 ( \stemDown a16
    \stemDown b16 \stemDown cis16 \stemDown d8 ) r8 \stemDown d16 (
    \stemDown c16 \stemDown b16 \stemDown a16 \pageBreak | % 332
    \stemDown g8 ) _ "Fl." r8 \stemDown d8 r16 \stemDown d16 \stemDown g8
    r8 \stemDown c,8 r8 | % 333
    \stemDown g'8 -> \stemDown d'8 ^> \stemDown g,16 ( \stemDown a16
    \stemDown b16 \stemDown cis16 \stemDown d8 ) r8 \stemDown d16 (
    \stemDown c16 \stemDown b16 \stemDown a16 | % 334
    \stemDown g8 ) r8 \stemDown d'16 ( \stemDown dis16 \stemDown e16
    \stemDown fis16 \stemDown g8 ) r8 \stemDown d16 ( \stemDown dis16
    \stemDown e16 \stemDown fis16 | % 335
    \stemDown g8 ) r8 \stemDown d16 ( \stemDown dis16 \stemDown e16
    \stemDown fis16 \stemDown g8 ) r8 \stemDown d16 ( \stemDown dis16
    \stemDown e16 \stemDown fis16 \pageBreak | % 336
    \stemDown g8 ) _ "Fl." r8 \stemDown d16 ( \stemDown dis16 \stemDown
    e16 \stemDown fis16 \stemDown g8 ) r8 \stemDown d16 ( \stemDown dis16
    \stemDown e16 \stemDown fis16 | % 337
    \stemDown g8 ) r8 \stemDown d16 ( \stemDown dis16 \stemDown e16
    \stemDown fis16 \stemDown g8 ) r8 \stemDown d16 ( \stemDown dis16
    \stemDown e16 \stemDown fis16 | % 338
    \stemDown g8 ) \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown d8
    \stemDown c8 \stemDown b8 \stemDown a8 | % 339
    \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown es8 \stemDown d8
    \stemDown c8 \stemDown b8 \stemDown a8 | \barNumberCheck #340
    \stemUp g8 r8 r4 \stemDown d'8 r8 r4 \pageBreak | % 341
    \stemDown g8 _ "Fl." r8 r4 \stemDown d'8 r8 r4 | % 342
    \stemDown g8 r8 \stemDown g8 r8 r4 \stemDown g8 r8 | % 343
    r4 \stemDown g8 r8 r4 \stemDown d8 r8 | % 344
    \stemDown g,8 r8 \stemDown d8 r8 \stemUp g,8 r8 r4 | % 345
    R1*3 \bar "|."
    }

PartPTwoVoiceOne =  \relative c''' {
    \clef "treble" \time 4/4 \key g \major | % 1
    R1*2 | % 3
    \time 12/8  \stemDown c8 -. _\p \stemDown fis,8 -. \stemDown c'8 -.
    \stemDown fis,8 -. \stemDown c'8 -. \stemDown fis,8 -. \stemDown c'8
    -. \stemDown g8 -. \stemDown c8 -. \stemDown a8 -. \stemDown c8 -.
    \stemDown a8 -. | % 4
    r1 s2 \pageBreak | % 5
    r1 s2 | % 6
    r1 s2 | % 7
    \stemDown a8 -. _\p \stemDown dis,8 -. \stemDown a'8 -. \stemDown
    dis,8 -. \stemDown a'8 -. \stemDown dis,8 -. \stemDown a'8 -.
    \stemDown e8 -. \stemDown a8 -. \stemDown fis8 -. \stemDown a8 -.
    \stemDown fis8 -. \bar "||"
    r1 s2 | % 9
    r1 s2 \pageBreak | \barNumberCheck #10
    r1 s2 | % 11
    r1 s2 | % 12
    r1 s2 | % 13
    r1 s2 | % 14
    r1 s2 \break | % 15
    r1 s2 | % 16
    r1 s2 | % 17
    r1 s2 | % 18
    r1 s2 | % 19
    r1 s2 \pageBreak | \barNumberCheck #20
    r1 s2 | % 21
    r1 s2 | % 22
    r1 s2 | % 23
    r1 s2 \break | % 24
    r1 s2 | % 25
    r1 s2 | % 26
    r1 s2 | % 27
    \numericTimeSignature\time 4/4  d'1 ~ _\pp _\< \pageBreak | % 28
    \stemDown d8 _\! r8 \stemDown d8 -. _\p _\< r16 \stemDown d16 -.
    \stemDown dis8 -. r8 \stemDown e8 -. r8 | % 29
    \stemDown a,8 -. _\! _\mp r8 r4 r2 | \barNumberCheck #30
    R1*2 \pageBreak | % 32
    R1*4 \pageBreak | % 36
    R1*3 | % 39
    \time 12/8  \stemDown c8 -. _\p \stemDown a8 -. \stemDown c8 -.
    \stemDown fis,8 -. \stemDown c'8 -. \stemDown fis,8 -. \stemDown a8
    -. \stemDown fis8 -. \stemDown a8 -. \stemDown fis8 -. \stemDown c'8
    -. \stemDown fis,8 -. | \barNumberCheck #40
    \stemDown b8 ( -> \stemDown g8 \stemDown e8 \stemDown g8 \stemDown d8
    \stemDown b8 ) r2.*2/3 s4 \pageBreak | % 41
    r1 s2 | % 42
    r1 s2 | % 43
    \stemDown c'8 -. _\mp \stemDown a8 -. \stemDown c8 -. \stemDown fis,8
    -. \stemDown c'8 -. \stemDown fis,8 -. \stemDown a8 -. \stemDown fis8
    -. \stemDown a8 -. \stemDown fis8 -. \stemDown c'8 -. \stemDown fis,8
    -. | % 44
    \stemDown b8 ( -> \stemDown g8 \stemDown e8 \stemDown g8 \stemDown d8
    \stemDown b8 ) r2.*2/3 s4 | % 45
    \stemDown es4. _\f -\markup{ \italic {marcato} } \stemDown d4.
    \stemDown c4. \stemDown bes4 ( ~ \stemUp bes16 \stemUp as16
    \pageBreak | % 46
    \stemUp g8 ) r8*2/3 r8*2/3 r4.*2/3 r4.*2/3 \stemDown d''8 _\f
    \stemDown d8 \stemDown d8 s1*1/3 | % 47
    \stemDown bes8 ( \stemDown c8 \stemDown d8 \stemDown es8 \stemDown d8
    \stemDown c8 \stemDown bes8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 | % 48
    r1 s2 | % 49
    \stemDown b4. _\ff -\markup{ \italic {marcato} } \stemDown ais4.
    \stemDown gis4. \stemDown fis4 ( ~ \stemDown fis16 \stemDown e16 |
    \barNumberCheck #50
    \stemDown dis8 ) r8*2/3 r8*2/3 r4.*2/3 r4.*2/3 \stemDown ais'8 _\ff
    \stemDown ais8 \stemDown ais8 s1*1/3 \pageBreak | % 51
    \stemDown fis8 ( \stemDown gis8 \stemDown ais8 \stemDown b8
    \stemDown ais8 \stemDown gis8 \stemDown fis8 ) r8*2/3 r8*2/3 r4.*2/3
    s1*5/24 | % 52
    r1 s2 | % 53
    r1 s2 | % 54
    r1 s2 | % 55
    \numericTimeSignature\time 4/4  r2 \stemDown fis4 ^> _\mf \stemDown
    fis8 r16 \stemDown fis16 \pageBreak | % 56
    \stemUp fis,8 r8 r4 \stemDown fis''4 -> _\ff \stemDown fis8 r16
    \stemDown fis16 | % 57
    \stemDown fis,8 _\pp r8 r4 r2 | % 58
    R1 | % 59
    r2 \stemDown fis4 ^> _\mf \stemDown fis8 r16 \stemDown fis16 |
    \barNumberCheck #60
    \stemUp fis,8 r8 r4 \stemDown fis''4 -> _\f \stemDown fis8 r16
    \stemDown fis16 \pageBreak | % 61
    b,1 -> _\p _\markup{ \small\italic {poco a poco cresc.} }
    \startTrillSpan | % 62
    g1 -> | % 63
    b1 -> | % 64
    g1 -> | % 65
    b1 -> \pageBreak | % 66
    c1 -> | % 67
    dis1 -> \stopTrillSpan _\f _\markup{ \small\italic {cresc.} }
    \startTrillSpan | % 68
    g1 -> | % 69
    \stemDown b8 -> \stopTrillSpan _\ff r8 r4 r2 | \barNumberCheck #70
    R1 \bar "||"
    \pageBreak | % 71
    \key e \major R1*5 \break | % 76
    R1*3 | % 79
    r4 r8 r16 \stemUp gis,,16 ( _\mp _\< \stemDown cis8 ) r16 \stemDown
    dis16 ( \stemDown e8 ) r16 \stemDown fis16 -. | \barNumberCheck #80
    \stemDown gis2 ~ _\! _\mf _\< \stemDown gis8 \stemDown fis16 ( _\!
    _\ff _\> \stemDown e16 \once \omit TupletBracket
    \times 4/6  {
        \stemUp dis16 \stemUp cis16 \stemUp b16 \stemUp a16 \stemUp gis16
        \stemUp fis16 }
    \pageBreak | % 81
    \stemUp e8 ) _\! _\p r8 r4 r2 | % 82
    R1*4 \pageBreak | % 86
    r2 r4 \stemUp gis8 ( -. _\mf r16 \stemUp b16 ) -. | % 87
    \stemDown c4 ( -> _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp b8 ) r16 \stemUp a16 -. \stemUp g8 -. r8 \stemDown d'8 ( -.
    r16 \stemDown dis16 ) -. | % 88
    \stemDown e4 ( -> \stemDown d8 ) r16 \stemDown c16 -. \stemDown b8
    -. r8 \stopTrillSpan r4 | % 89
    R1 \pageBreak | \barNumberCheck #90
    R1*5 | % 95
    r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp d,8 _\ff \stemUp d8 \stemUp d8 }
    \stemUp d2 ~ \pageBreak | % 96
    \stemUp d8 r8 \stemUp dis8 r16 \stemUp dis16 \stemUp e8 r8 r4 | % 97
    R1 | % 98
    r2 r4 \stemDown fis''4 ( _\mf | % 99
    \stemDown b,8 ) r8 \stemDown b4 ( \stemDown e,8 ) r8 \stemDown e4 ~
    | \barNumberCheck #100
    \stemDown e4 \stemDown cis4 ( \stemUp a4 \stemUp fis8 ) r8 | % 101
    R1 \break | % 102
    r2 r4 \stemDown dis''4 ( _\mf | % 103
    \stemDown gis,8 ) r8 \stemDown gis4 ( \stemDown cis,8 ) r8 \stemDown
    cis'4 ~ | % 104
    \stemDown cis4 \stemDown a4 ( \stemDown fis4 \stemDown dis8 ) r8 | % 105
    R1 | % 106
    r2 r4 \stemDown fis'4 ( _\mf \pageBreak | % 107
    \stemDown b,8 ) r8 \stemDown b4 ( \stemDown e,8 ) r8 \stemDown e4 ~
    | % 108
    \stemDown e4 \stemDown cis4 ( \stemUp a4 \stemUp fis8 ) r8 | % 109
    R1*4 \break | % 113
    R1*5 \pageBreak | % 118
    R1*3 | % 121
    r4 r8 r16 \stemUp gis16 ( _\mp _\< \stemDown cis8 ) r16 \stemDown
    dis16 ( \stemDown e8 ) r16 \stemDown fis16 -. | % 122
    \stemDown gis2 ~ _\! _\mf _\< \stemDown gis8 \stemDown fis16 ( _\!
    _\ff _\> \stemDown e16 \once \omit TupletBracket
    \times 4/6  {
        \stemUp dis16 \stemUp cis16 \stemUp b16 \stemUp a16 \stemUp gis16
        \stemUp fis16 }
    \break | % 123
    \stemUp e8 ) _\! _\p r8 r4 r2 | % 124
    R1*4 \pageBreak | % 128
    r2 r4 \stemUp gis8 ( -. _\f r16 \stemUp b16 ) -. | % 129
    \stemDown c4 ( -> \stemUp b8 ) r16 \stemUp a16 -. \stemUp g8 -. r8
    \stemDown d'8 ( -. r16 \stemDown dis16 ) -. | \barNumberCheck #130
    \stemDown e4 ( -> \stemDown d8 ) r16 \stemDown c16 -. \stemUp b8 -.
    \stemUp g8 ( \stemUp a8 \stemUp b8 ) | % 131
    \stemDown c8 ( \stemDown d8 \stemDown e8 \stemDown fis8 ) \stemDown
    g8 ( \stemDown a8 \stemDown ais8 \stemDown b8 ) \pageBreak | % 132
    \stemDown c8 ( \stemDown d8 \stemDown e8 \stemDown fis8 \stemDown g8
    ) r8 r4 | % 133
    \stemDown c,,4 ( -> \stemUp b8 ) r16 \stemUp a16 -. \stemUp g8 -. r8
    \stemDown d'8 ( -. r16 \stemDown dis16 ) -. | % 134
    \stemDown e4 ( -> \stemDown d8 ) r16 \stemDown c16 -. \stemUp b8 -.
    \stemUp g8 ( \stemUp a8 \stemUp b8 ) | % 135
    \stemDown c8 ( \stemDown d8 \stemDown e8 \stemDown fis8 ) \stemDown
    g8 ( \stemDown a8 \stemDown ais8 \stemDown b8 ) \pageBreak | % 136
    \stemDown c8 ( \stemDown d8 \stemDown e8 \stemDown fis8 \stemDown g8
    ) r8 r4 | % 137
    \time 12/8  r4.*2/3 r8*2/3 \stemDown b,8 -. _\f \stemDown d8 -.
    \stemDown e8 ( \stemDown d8 ) \stemDown c8 -. \stemDown b8 -. r8*2/3
    r8*2/3 s4 | % 138
    r4.*2/3 r8*2/3 \stemDown b8 -. _\mf \stemDown d8 -. \stemDown e8 (
    \stemDown d8 ) \stemDown c8 -. \stemDown b8 -. r4*2/3 \bar "||"
    s4 | % 139
    \key g \major r1 s2 \pageBreak | \barNumberCheck #140
    r1 s2 | % 141
    \stemDown c8 -. _\p \stemDown fis,8 -. \stemDown c'8 -. \stemDown
    fis,8 -. \stemDown c'8 -. \stemDown fis,8 -. \stemDown c'8 -.
    \stemDown g8 -. \stemDown c8 -. \stemDown a8 -. \stemDown c8 -.
    \stemDown a8 -. | % 142
    r1 s2 | % 143
    r1 s2 | % 144
    r1 s2 \pageBreak | % 145
    \stemDown a8 -. _\p \stemDown dis,8 -. \stemDown a'8 -. \stemDown
    dis,8 -. \stemDown a'8 -. \stemDown dis,8 -. \stemDown a'8 -.
    \stemDown e8 -. \stemDown a8 -. \stemDown fis8 -. \stemDown a8 -.
    \stemDown fis8 -. | % 146
    r1 s2 | % 147
    r1 s2 | % 148
    r1 s2 | % 149
    r1 s2 \pageBreak | \barNumberCheck #150
    r1 s2 | % 151
    r1 s2 | % 152
    r1 s2 | % 153
    r1 s2 | % 154
    r1 s2 \pageBreak | % 155
    r1 s2 | % 156
    r1 s2 | % 157
    r1 s2 | % 158
    r1 s2 \break | % 159
    r1 s2 | \barNumberCheck #160
    r1 s2 | % 161
    r1 s2 | % 162
    r1 s2 \pageBreak | % 163
    r1 s2 | % 164
    r1 s2 | % 165
    \numericTimeSignature\time 4/4  d'1 ~ _\pp _\< | % 166
    \stemDown d8 r8 \stemDown d8 -. _\! _\p _\< r16 \stemDown d16 -.
    \stemDown dis8 -. r8 \stemDown e8 -. r8 \pageBreak | % 167
    \stemDown a,8 -. _\! _\mp r8 r4 r2 | % 168
    R1*3 \pageBreak | % 171
    R1*4 \pageBreak | % 175
    R1*2 | % 177
    \time 12/8  \stemDown c8 -. _\p \stemDown a8 -. \stemDown c8 -.
    \stemDown fis,8 -. \stemDown c'8 -. \stemDown fis,8 -. \stemDown a8
    -. \stemDown fis8 -. \stemDown a8 -. \stemDown fis8 -. \stemDown c'8
    -. \stemDown fis,8 -. | % 178
    \stemDown b8 ( -> \stemDown g8 \stemDown e8 \stemDown g8 \stemDown d8
    \stemDown b8 ) r2.*2/3 s4 | % 179
    r1 s2 \pageBreak | \barNumberCheck #180
    r1 s2 | % 181
    \stemDown c'8 -. _\mp \stemDown a8 -. \stemDown c8 -. \stemDown fis,8
    -. \stemDown c'8 -. \stemDown fis,8 -. \stemDown a8 -. \stemDown fis8
    -. \stemDown a8 -. \stemDown fis8 -. \stemDown c'8 -. \stemDown fis,8
    -. | % 182
    \stemDown b8 ( -> \stemDown g8 \stemDown e8 \stemDown g8 \stemDown d8
    \stemDown b8 ) r2.*2/3 s4 | % 183
    \stemDown es4. _\f _\ marcato \stemDown d4. \stemDown c4. \stemDown
    bes4 ( ~ \stemUp bes16 \stemUp as16 \pageBreak | % 184
    \stemUp g8 ) r8*2/3 r8*2/3 r4.*2/3 r4.*2/3 \stemDown d''8 \stemDown
    d8 \stemDown d8 s1*1/3 | % 185
    \stemDown bes8 ( \stemDown c8 \stemDown d8 \stemDown es8 \stemDown d8
    \stemDown c8 \stemDown bes8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 | % 186
    r1 s2 | % 187
    \stemDown g4. _\ff \stemDown f4. \stemDown es4. \stemDown d4 ( ~
    \stemDown d16 \stemDown c16 | % 188
    \stemDown bes8 ) r8*2/3 r8*2/3 r4.*2/3 r4.*2/3 \stemDown f''8
    \stemDown f8 \stemDown f8 s1*1/3 \pageBreak | % 189
    \stemDown d8 ( \stemDown es8 \stemDown f8 \stemDown g8 \stemDown f8
    \stemDown es8 \stemDown d8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 |
    \barNumberCheck #190
    r1 s2 | % 191
    \numericTimeSignature\time 4/4  \stemDown g8 ( _\ff \stemDown fis8
    \stemDown e8 \stemDown d8 ) r2 | % 192
    \stemDown g8 ( _\ff \stemDown f8 \stemDown e8 \stemDown d8 ) r2 | % 193
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 ( _\ff \stemDown fis8 \stemDown e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown cis8 \stemDown b8 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 ( \stemDown g8 \stemDown fis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown d8 \stemDown cis8 ) }
    \pageBreak | % 194
    \stemUp b16 ( \stemUp a16 \stemUp g16 \stemUp fis16 \stemUp e16
    \stemUp d16 ) r8 \stemUp a'8 r8 r4 | % 195
    R1*5 | \barNumberCheck #200
    \stemDown d8 ^\leggieramente _\pp r8 \stemUp a8 r16 \stemUp a16
    \stemDown d8 r8 \stemUp a8 r8 \pageBreak | % 201
    \stemDown e'8 -> \stemDown a8 -> r4 r2 | % 202
    R1*2 | % 204
    \stemDown d8 _\p _\< r8 \stemDown a8 r16 \stemDown a16 \stemDown d8
    r8 \stemDown a8 r8 | % 205
    \stemDown d8 -> _\! _\mp \stemDown a'8 -> r4 r2 \pageBreak | % 206
    R1*2 | % 208
    \stemDown g,8 _\mf r8 \stemDown d8 r16 \stemDown d16 \stemDown g8 r8
    \stemDown d8 r8 | % 209
    \stemDown a'8 -> \stemDown d8 -> r4 r2 | \barNumberCheck #210
    \stemDown e,8 _\f r8 \stemDown b8 r16 \stemDown b16 \stemDown e8 r8
    \stemDown b8 r8 \pageBreak | % 211
    \stemDown e8 -> \stemDown a8 -> r4 r2 | % 212
    \stemDown g'8 _\ff r8 \stemDown d8 r16 \stemDown d16 \stemDown g8 r8
    \stemDown d8 r8 | % 213
    \stemDown a'8 -> \stemDown d,8 -> r4 r2 | % 214
    \stemDown a8 _\fff r8 \stemDown e8 r16 \stemDown e16 \stemDown a8 r8
    \stemDown e8 r8 | % 215
    \stemDown a8 -> \stemDown d8 ~ -> \stemDown d2. \pageBreak | % 216
    \stemDown a8 _\fff r8 \stemDown e8 r16 \stemDown e16 \stemDown a8 r8
    \stemDown e8 r8 | % 217
    \stemDown a8 -> \stemDown d8 ~ -> \stemDown d8 \stemDown d8
    \stemDown a8 \stemDown e4 \stemDown e8 | % 218
    \stemDown a8 \stemDown d4 \stemDown d8 \stemDown a8 \stemDown e4
    \stemDown e8 | % 219
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 r8 }
    | \barNumberCheck #220
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 r8 }
    \pageBreak | % 221
    \times 2/3  {
        \stemDown a8 -> \stemDown a8 -> r8 }
    r4 r2 | % 222
    r4 \stemDown d,32 ( _\sempre _\fff \stemDown e32 \stemDown fis32
    \stemDown g32 \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32
    ) \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16 )
    \stemDown a16 ( \stemDown g16 \stemDown fis16 \stemDown e16 ) | % 223
    \stemDown d16 ( \stemDown c16 \stemDown b16 \stemDown a16 ) \stemUp
    g16 ( \stemUp fis16 \stemUp e16 \stemUp d16 ) r2 | % 224
    r4 \stemDown d'32 ( \stemDown e32 \stemDown fis32 \stemDown g32
    \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32 ) \stemDown
    e16 ( \stemDown d16 \stemDown c16 \stemDown b16 ) \stemDown a16 (
    \stemDown g16 \stemDown fis16 \stemDown e16 ) \pageBreak | % 225
    \stemDown d16 ( \stemDown c16 \stemDown b16 \stemDown a16 ) \stemUp
    g16 ( \stemUp fis16 \stemUp e16 \stemUp d16 ) r4 \stemDown d'32 (
    \stemDown e32 \stemDown fis32 \stemDown g32 \stemDown a32 \stemDown
    b32 \stemDown c32 \stemDown d32 ) | % 226
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemDown fis8 ) r8 r4 \stemDown d32 ( \stemDown e32 \stemDown fis32
    \stemDown g32 \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32
    ) | % 227
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemDown fis8 ) r8 r4 \stemDown d32 ( \stemDown e32 \stemDown fis32
    \stemDown g32 \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32
    ) \pageBreak | % 228
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemDown fis8 ) r8 \once \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemUp fis8 ) r8 | % 229
    \stemDown g'8 _\fff r8 \stemDown d8 r16 \stemDown d16 \stemDown g8 r8
    \stemDown d8 r8 | \barNumberCheck #230
    \stemDown g8 -> \stemDown c8 ~ ^> \stemDown c2 \stemDown b8 r16
    \stemDown a16 | % 231
    \stemDown d8 r8 \acciaccatura { \stemUp a8 ( } \stemDown g8 ) r16
    \stemDown fis16 \stemDown g8 r8 \stemDown d8 r8 | % 232
    \stemDown g2. -> \stemDown b8 r16 \stemDown d16 \pageBreak | % 233
    \stemDown e8 r8 \acciaccatura { \stemUp a,8 ( } \stemDown g8 ) r16
    \stemDown fis16 \stemDown g8 r8 \stemDown d8 r8 | % 234
    \stemDown g2. -> \stemDown b8 r16 \stemDown d16 | % 235
    \stemDown g4 ( -> \stemDown fis8 ) r16 \stemDown g16 \stemDown e4 (
    -> \stemDown dis8 ) r16 \stemDown e16 | % 236
    \stemDown c4 ( -> \stemDown b8 ) r16 \stemDown c16 \stemDown a4 ( ->
    \stemDown g8 ) r16 \stemDown a16 -. | % 237
    \stemDown e8 -. r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown b16
    ( \stemDown e8 ) r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown
    a16 -. \pageBreak | % 238
    \stemDown b2 ~ -> \stemDown b8 \stemDown a16 ( \stemDown g16 \once
    \omit TupletBracket
    \times 4/6  {
        \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown c16
        \stemDown b16 \stemDown a16 }
    | % 239
    \stemDown g8 ) r8 \stemDown d8 r16 \stemDown d16 \stemDown g8 r8
    \stemDown d8 r8 | \barNumberCheck #240
    \stemDown g8 -> \stemDown c8 ~ ^> \stemDown c2 \stemDown b8 r16
    \stemDown a16 | % 241
    \stemDown d8 r8 \acciaccatura { \stemUp a8 ( } \stemDown g8 ) r16
    \stemDown fis16 \stemDown g8 r8 \stemDown d8 r8 | % 242
    \stemDown g2. -> \stemDown b8 r16 \stemDown d16 \pageBreak | % 243
    \stemDown e8 r8 \acciaccatura { \stemUp a,8 ( } \stemDown g8 ) r16
    \stemDown fis16 \stemDown g8 r8 \stemDown d8 r8 | % 244
    \stemDown g2. -> \stemDown b8 r16 \stemDown d16 | % 245
    \stemDown es4 ( -> \stemDown d8 ) r16 \stemDown c16 \stemDown bes8 r8
    \stemDown f'8 r16 \stemDown fis16 | % 246
    \stemDown g4 ( -> \stemDown f8 ) r16 \stemDown es16 \stemDown d8 r8
    \stemDown g8 r16 \stemDown a16 | % 247
    \stemDown b2. -> \stemDown a8 r16 \stemDown b,16 \pageBreak | % 248
    \stemDown g'2. -> \stemDown fis8 r16 \stemDown b,16 | % 249
    \stemDown e4 ( -> \stemDown d8 ) r16 \stemDown e,16 \stemDown c'4 (
    -> \stemDown b8 ) r16 \stemDown e,16 | \barNumberCheck #250
    \stemDown a4 ( -> \stemDown g8 ) r16 \stemDown g,16 \stemDown e'4 (
    -> \stemDown d8 ) r16 \stemDown gis,16 | % 251
    \stemDown c8 r8 r4 r2 | % 252
    R1 | % 253
    r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown g'8 _\fff \stemDown g8 \stemDown g8 }
    \stemDown g2 ~ \pageBreak | % 254
    \stemDown g8 r8 \stemDown a8 r16 \stemDown fis16 \stemDown g8 r8 r4
    | % 255
    R1 | % 256
    r2 r4 \stemDown d'16 ( _\ff \stemDown e16 \stemDown d16 \stemDown e16
    | % 257
    \stemDown b8 ) r8 \stemDown d4 ( \stemDown g,8 ) r8 \stemDown ais16
    ( \stemDown b16 \stemDown ais16 \stemDown b16 ) | % 258
    \stemDown c16 ( \stemDown d16 \stemDown c16 \stemDown b16 )
    \stemDown a16 ( \stemDown b16 \stemDown a16 \stemDown g16 )
    \stemDown fis16 ( \stemDown g16 \stemDown e16 \stemDown fis16
    \stemDown d8 ) r8 \pageBreak | % 259
    R1 | \barNumberCheck #260
    r2 r4 \stemDown b'16 ( _\ff \stemDown c16 \stemDown b16 \stemDown c16
    | % 261
    \stemDown g8 ) r8 \stemDown b4 ( \stemDown e,8 ) r8 \stemDown g16 (
    \stemDown gis16 \stemDown g16 \stemDown gis16 ) | % 262
    \stemDown a16 ( \stemDown b16 \stemDown a16 \stemDown g16 )
    \stemDown fis16 ( \stemDown g16 \stemDown fis16 \stemDown e16 )
    \stemDown d16 ( \stemDown e16 \stemDown c16 \stemDown d16 \stemDown
    b8 ) r8 | % 263
    R1 \pageBreak | % 264
    r2 r4 \stemDown d'16 ( _\ff \stemDown e16 \stemDown d16 \stemDown e16
    | % 265
    \stemDown b8 ) r8 \stemDown d4 ( \stemDown g,8 ) r8 \stemDown ais16
    ( \stemDown b16 \stemDown ais16 \stemDown b16 ) | % 266
    \stemDown c16 ( \stemDown d16 \stemDown c16 \stemDown b16 )
    \stemDown a16 ( \stemDown b16 \stemDown a16 \stemDown g16 )
    \stemDown fis16 ( \stemDown g16 \stemDown e16 \stemDown fis16
    \stemDown d8 ) r8 | % 267
    R1*2 \pageBreak | % 269
    R1*3 | % 272
    \stemDown g4 ~ _\fff \stemDown g8 r8 \stemDown gis4 ~ \stemDown gis8
    r8 | % 273
    \stemDown a8 r8 \stemDown bes8 r8 \stemDown b8 r8 \stemDown c8 r8
    \pageBreak | % 274
    \stemDown cis8 r8 \stemDown d8 r8 \stemDown e8 r8 r4 | % 275
    R1*6 \pageBreak | % 281
    R1 | % 282
    r2 r4 \stemDown d,16 ( _\fff \stemDown dis16 \stemDown e16 \stemDown
    fis16 | % 283
    \stemDown g8 ) r8 \stemDown d8 r16 \stemDown d16 \stemDown g8 r8
    \stemDown d8 r8 | % 284
    \stemDown g8 -> \stemDown c8 ~ ^> \stemDown c2 \stemDown b8 r16
    \stemDown a16 | % 285
    \stemDown d8 r8 \acciaccatura { \stemUp a8 ( } \stemDown g8 ) r16
    \stemDown fis16 \stemDown g8 r8 \stemDown d8 r8 | % 286
    \stemDown g2. -> \stemDown b8 r16 \stemDown d16 \pageBreak | % 287
    \stemDown e8 r8 \acciaccatura { \stemUp a,8 ( } \stemDown g8 ) r16
    \stemDown fis16 \stemDown g8 r8 \stemDown d8 r8 | % 288
    \stemDown g2. -> \stemDown b8 r16 \stemDown d16 | % 289
    \stemDown g4 ( -> \stemDown fis8 ) r16 \stemDown g16 \stemDown e4 (
    -> \stemDown dis8 ) r16 \stemDown e16 | \barNumberCheck #290
    \stemDown c4 ( -> \stemDown b8 ) r16 \stemDown c16 \stemDown a4 ( ->
    \stemDown g8 ) r16 \stemDown a16 -. | % 291
    \stemDown e8 -. r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown b16
    ( \stemDown e8 ) r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown
    a16 -. \pageBreak | % 292
    \stemDown b2 ~ -> \stemDown b8 \stemDown a16 ( \stemDown g16 \once
    \omit TupletBracket
    \times 4/6  {
        \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown c16
        \stemDown b16 \stemDown a16 }
    | % 293
    \stemDown g8 ) r8 \stemDown d8 r16 \stemDown d16 \stemDown g8 r8
    \stemDown d8 r8 | % 294
    \stemDown g8 -> \stemDown c8 ~ ^> \stemDown c2 \stemDown b8 r16
    \stemDown a16 | % 295
    \stemDown d8 r8 \acciaccatura { \stemUp a8 ( } \stemDown g8 ) r16
    \stemDown fis16 \stemDown g8 r8 \stemDown d8 r8 | % 296
    \stemDown g2. -> \stemDown b8 r16 \stemDown d16 \pageBreak | % 297
    \stemDown e8 r8 \acciaccatura { \stemUp a,8 ( } \stemDown g8 ) r16
    \stemDown fis16 \stemDown g8 r8 \stemDown d8 r8 | % 298
    \stemDown g2. -> \stemDown b8 r16 \stemDown d16 | % 299
    \stemDown es4 ( -> \stemDown d8 ) r16 \stemDown c16 \stemDown bes8 r8
    \stemDown f'8 r16 \stemDown fis16 | \barNumberCheck #300
    \stemDown g4 ( -> \stemDown f8 ) r16 \stemDown es16 \stemDown d8 r8
    \stemDown g8 r16 \stemDown a16 | % 301
    \stemDown b2. -> \stemDown a8 r16 \stemDown b,16 \pageBreak | % 302
    \stemDown g'2. -> \stemDown fis8 r16 \stemDown b,16 | % 303
    \stemDown e4 ( -> \stemDown d8 ) r16 \stemDown e,16 \stemDown c'4 (
    -> \stemDown b8 ) r16 \stemDown e,16 | % 304
    \stemDown a4 ( -> _\sempre _\fff \stemDown g8 ) r16 \stemDown e16
    \stemDown a4 ( -> \stemDown g8 ) r16 \stemDown es16 | % 305
    \stemDown a4 ( -> \stemDown g8 ) r16 \stemDown d16 \stemDown a'4 (
    -> \stemDown g8 ) r16 \stemDown cis,16 | % 306
    \stemDown a'4 ( -> \stemDown g8 ) r16 \stemDown c,16 \stemDown a'4 (
    -> \stemDown g8 ) r16 \stemDown cis,16 | % 307
    \stemDown a'4 ( -> \stemDown g8 ) r16 \stemDown d16 \stemDown a'4 (
    -> \stemDown g8 ) r16 \stemDown dis16 \pageBreak | % 308
    \stemDown b'4 ( -> \stemDown a8 ) r16 \stemDown e16 \stemDown c'4 (
    -> \stemDown b8 ) r16 \stemDown e,16 | % 309
    \stemDown d'4 ( -> \stemDown c8 ) r16 \stemDown a16 \stemDown d4 (
    -> \stemDown cis8 ) r16 \stemDown a16 | \barNumberCheck #310
    \stemDown e'4 ( -> \stemDown d8 ) r16 \stemDown a16 \stemDown e'4 (
    -> \stemDown dis8 ) r16 \stemDown a16 | % 311
    \stemDown f'4 ( -> \stemDown e8 ) r16 \stemDown a,16 \stemDown g'4 (
    -> \stemDown fis8 ) r16 \stemDown c16 | % 312
    \stemDown a'8 ( _\ffff \stemDown g8 \stemDown d8 \stemDown g8 )
    \stemDown a8 ( \stemDown g8 \stemDown es8 \stemDown g8 ) | % 313
    \stemDown a8 ( \stemDown g8 \stemDown e8 \stemDown g8 ) \stemDown a8
    ( \stemDown g8 \stemDown es8 \stemDown g8 ) \pageBreak | % 314
    \stemDown a8 ( \stemDown g8 \stemDown fis8 \stemDown e8 ) \stemDown
    d8 ( \stemDown cis8 \stemDown c8 \stemDown b8 ) | % 315
    \stemDown a8 ( \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown d8
    ) r8 r4 | % 316
    R1*4 \pageBreak | \barNumberCheck #320
    R1*2 | % 322
    g'1 ~ _\ff _\markup{ \small\italic {cresc.} } \startTrillSpan | % 323
    \stemDown g4 \stemDown fis4 \stemDown g4 \stemDown a4 | % 324
    \stemDown b8 \stopTrillSpan _\fff r8 \once \omit TupletBracket
    \times 4/7  {
        \stemDown g,16*161/160 ( \stemDown a16*161/160 \stemDown b16*161/160
        \stemDown cis16*161/160 \stemDown dis16*161/160 \stemDown e16*161/160
        \stemDown fis16*161/160 }
    \stemDown g8 ) r16 \stemDown fis16 -. \stemDown g8 -. r16 \stemDown
    dis16 -. \pageBreak | % 325
    \stemDown e8 -. r8 \once \omit TupletBracket
    \times 4/7  {
        \stemDown c,16*161/160 ( \stemDown d16*161/160 \stemDown e16*161/160
        \stemDown fis16*161/160 \stemDown gis16*161/160 \stemDown a16*161/160
        \stemDown b16*161/160 }
    \stemDown c8 ) r16 \stemDown b16 -. \stemDown c8 -. r16 \stemDown
    gis16 -. | % 326
    \stemDown a8 -. r8 r4 r4 \once \omit TupletBracket
    \times 4/7  {
        \stemDown bes,16*161/160 ( \stemDown c16*161/160 \stemDown d16*161/160
        \stemDown es16*161/160 \stemDown f16*161/160 \stemDown g16*161/160
        \stemDown a16*161/160 }
    | % 327
    \stemDown bes8 ) r8 r4 r4 \once \omit TupletBracket
    \times 4/7  {
        \stemDown c,16*161/160 ( \stemDown d16*161/160 \stemDown e16*161/160
        \stemDown f16*161/160 \stemDown g16*161/160 \stemDown a16*161/160
        \stemDown b16*161/160 }
    \pageBreak | % 328
    \stemDown c8 ) r8 r4 r4 \once \omit TupletBracket
    \times 4/7  {
        \stemDown d,16*161/160 ( \stemDown e16*161/160 \stemDown fis16*161/160
        \stemDown g16*161/160 \stemDown a16*161/160 \stemDown b16*161/160
        \stemDown cis16*161/160 }
    | % 329
    \stemDown d16 ) \stemDown e16 ( \stemDown fis16 \stemDown g16
    \stemDown a16 \stemDown g16 \stemDown fis16 \stemDown e16 )
    \stemDown d16 ( \stemDown c16 \stemDown b16 \stemDown a16 )
    \stemDown g16 ( \stemDown fis16 \stemDown e16 \stemDown d16 ) |
    \barNumberCheck #330
    \stemDown g8 _\sempre _\fff r8 \stemDown d8 r16 \stemDown d16
    \stemDown g8 r8 \stemDown c,8 r8 | % 331
    \stemDown g'8 -> \stemDown d'8 ^> \stemDown g,16 ( \stemDown a16
    \stemDown b16 \stemDown cis16 \stemDown d8 ) r8 \stemDown d16 (
    \stemDown c16 \stemDown b16 \stemDown a16 \pageBreak | % 332
    \stemDown g8 ) r8 \stemDown d8 r16 \stemDown d16 \stemDown g8 r8
    \stemDown c,8 r8 | % 333
    \stemDown g'8 -> \stemDown d'8 ^> \stemDown g,16 ( \stemDown a16
    \stemDown b16 \stemDown cis16 \stemDown d8 ) r8 \stemDown d16 (
    \stemDown c16 \stemDown b16 \stemDown a16 | % 334
    \stemDown g8 ) r8 \stemDown d'16 ( \stemDown dis16 \stemDown e16
    \stemDown fis16 \stemDown g8 ) r8 \stemDown d16 ( \stemDown dis16
    \stemDown e16 \stemDown fis16 | % 335
    \stemDown g8 ) r8 \stemDown d16 ( \stemDown dis16 \stemDown e16
    \stemDown fis16 \stemDown g8 ) r8 \stemDown d16 ( \stemDown dis16
    \stemDown e16 \stemDown fis16 \pageBreak | % 336
    \stemDown g8 ) r8 \stemDown d16 ( \stemDown dis16 \stemDown e16
    \stemDown fis16 \stemDown g8 ) r8 \stemDown d16 ( \stemDown dis16
    \stemDown e16 \stemDown fis16 | % 337
    \stemDown g8 ) r8 \stemDown d16 ( \stemDown dis16 \stemDown e16
    \stemDown fis16 \stemDown g8 ) r8 \stemDown d16 ( \stemDown dis16
    \stemDown e16 \stemDown fis16 | % 338
    \stemDown g8 ) \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown d8
    \stemDown c8 \stemDown b8 \stemDown a8 | % 339
    \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown es8 \stemDown d8
    \stemDown c8 \stemDown b8 \stemDown a8 | \barNumberCheck #340
    \stemUp g8 r8 r4 \stemDown d'8 r8 r4 \pageBreak | % 341
    \stemDown g8 r8 r4 \stemDown d'8 r8 r4 | % 342
    \stemDown g8 r8 \stemDown g8 r8 r4 \stemDown g8 r8 | % 343
    r4 \stemDown g8 r8 r4 \stemDown d8 r8 | % 344
    \stemDown g,8 r8 \stemDown d8 r8 \stemUp g,8 r8 r4 | % 345
    R1*3 \bar "|."
    }

PartPTwoVoiceTwo =  \relative d'' {
    \clef "treble" \time 4/4 \key g \major s1*2 | % 3
    \time 12/8  s1*3 \pageBreak s2*9 \bar "||"
    s1*3 \pageBreak s2*15 \break s2*15 \pageBreak s1*6 \break s2*9 | % 27
    \numericTimeSignature\time 4/4  s1 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1*3 | % 39
    \time 12/8  s1*3 \pageBreak s2*15 \pageBreak s2*15 \pageBreak s1*6 | % 55
    \numericTimeSignature\time 4/4  s1 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \bar "||"
    \pageBreak | % 71
    \key e \major s1*5 \break s1*5 \pageBreak s1*5 \pageBreak s1*4
    \pageBreak s1*6 \pageBreak s1*6 \break s1*5 \pageBreak s1*6 \break
    s1*5 \pageBreak s1*5 \break s1*5 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1 | % 137
    \time 12/8  s4*11 \bar "||"
    s4 | % 139
    \key g \major s1. \pageBreak s2*15 \pageBreak s2*15 \pageBreak s2*15
    \pageBreak s1*6 \break s1*6 \pageBreak s1*3 | % 165
    \numericTimeSignature\time 4/4  \once \override NoteHead.style = ##f
    d1 s1 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*2 | % 177
    \time 12/8  s2*9 \pageBreak s1*6 \pageBreak s2*15 \pageBreak s1*3 | % 191
    \numericTimeSignature\time 4/4  s1*3 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*4
    \pageBreak s1*3 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*6 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*7 \pageBreak s1*6
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*6
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*5 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*5 \pageBreak s1*7 \bar
    "|."
    }

PartPThreeVoiceOne =  \relative g''' {
    \clef "treble" \time 4/4 \key g \major \transposition c'' | % 1
    R1*4 \pageBreak | % 5
    R1*3 \bar "||"
    R1*2 \pageBreak | \barNumberCheck #10
    R1*5 \break | % 15
    R1*5 \pageBreak | \barNumberCheck #20
    R1*4 \break | % 24
    R1*4 \pageBreak | % 28
    R1*4 \pageBreak | % 32
    R1*4 \pageBreak | % 36
    R1 | % 37
    \numericTimeSignature\time 4/4  \stemDown g8 -. _\p r8 \stemDown d8
    -. r8 \stemDown a8 -. r8 \stemDown e8 -. r8 | % 38
    \stemDown a8 -. r8 \stemDown d8 -. r8 \stemDown b8 -. r8 \stemDown
    d,8 -. _\< \stemDown e8 -. | % 39
    \stemDown fis8 -. \stemDown g8 -. \stemDown a8 -. \stemDown b8 -.
    \stemDown c8 -. _\! _\mf r8 \stemDown b8 -. \stemDown a8 -. |
    \barNumberCheck #40
    \stemDown d8 -. _\> r8 \stemDown g,8 -. r8 \stemDown g8 -. r8 _\! r4
    \pageBreak | % 41
    R1*2 | % 43
    \time 12/8  \stemDown e'8 -. _\mp \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. | % 44
    \stemDown e8 ( -> \stemDown d8 \stemDown c8 \stemDown b8 \stemDown a8
    \stemDown g8 ) r2.*2/3 s4 | % 45
    r1 s2 \pageBreak | % 46
    r2.*2/3 r4.*2/3 \stemDown d8 _\f \stemDown d8 \stemDown d8 s4. | % 47
    \stemDown bes8 ( \stemDown c8 \stemDown d8 \stemDown es8 \stemDown d8
    \stemDown c8 \stemDown bes8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 | % 48
    r1 s2 | % 49
    r1 s2 | \barNumberCheck #50
    r1 s2 \pageBreak | % 51
    r1 s2 | % 52
    r1 s2 | % 53
    r1 s2 | % 54
    r1 s2 | % 55
    r1 s2 \pageBreak | % 56
    \numericTimeSignature\time 4/4  r2 \stemDown fis'4 -> _\ff \stemDown
    fis8 r16 \stemDown fis16 | % 57
    \stemUp fis,8 _\pp r8 r4 r2 | % 58
    R1*2 | \barNumberCheck #60
    r2 \stemDown fis'4 -> _\f \stemDown fis8 r16 \stemDown fis16
    \pageBreak | % 61
    \stemDown b,8 -> _\p r8 r4 r2 | % 62
    R1*4 \pageBreak | % 66
    R1 | % 67
    dis1 -> _\f _\markup{ \small\italic {cresc.} } \startTrillSpan | % 68
    g1 -> | % 69
    \stemDown b8 -> \stopTrillSpan _\ff r8 r4 r2 | \barNumberCheck #70
    R1 \bar "||"
    \pageBreak | % 71
    \key e \major R1*5 \break | % 76
    R1*5 \pageBreak | % 81
    R1*5 \pageBreak | % 86
    R1*4 \pageBreak | \barNumberCheck #90
    R1*6 \pageBreak | % 96
    R1*2 | % 98
    r2 r4 \stemDown b16 ( _\mf \stemDown cis16 \stemDown b16 \stemDown
    cis16 | % 99
    \stemDown gis8 ) r8 r4 r2 | \barNumberCheck #100
    R1*2 \break | % 102
    r2 r4 \stemDown gis'16 ( _\mf \stemDown a16 \stemDown gis16
    \stemDown a16 | % 103
    \stemDown e8 ) r8 \stemDown bis16 ( \stemDown cis16 \stemDown bis16
    \stemDown cis16 \stemDown a8 ) r8 r4 | % 104
    R1*2 | % 106
    r2 r4 \stemDown b16 ( _\mf \stemDown cis16 \stemDown b16 \stemDown
    cis16 \pageBreak | % 107
    \stemDown gis8 ) r8 r4 r2 | % 108
    R1*5 \break | % 113
    R1*5 \pageBreak | % 118
    R1*5 \break | % 123
    R1*5 \pageBreak | % 128
    R1*4 \pageBreak | % 132
    R1*4 \pageBreak | % 136
    R1 | % 137
    \time 12/8  r4.*2/3 r8*2/3 \stemDown b8 -. _\f \stemDown d8 -.
    \stemDown e8 ( \stemDown d8 ) \stemDown c8 -. \stemDown b8 -. r8*2/3
    r8*2/3 s4 | % 138
    r4.*2/3 r8*2/3 \stemDown b8 -. _\mf \stemDown d8 -. \stemDown e8 (
    \stemDown d8 ) \stemDown c8 -. \stemDown b8 -. r4*2/3 \bar "||"
    s4 | % 139
    \key g \major r1 s2 \pageBreak | \barNumberCheck #140
    r1 s2 | % 141
    r1 r2*2/3 s1*1/6 | % 142
    r1 s2 | % 143
    r1 s2 | % 144
    r1 s2 \pageBreak | % 145
    r1 r2*2/3 s1*1/6 | % 146
    r1 s2 | % 147
    r1 s2 | % 148
    r1 s2 | % 149
    r1 s2 \pageBreak | \barNumberCheck #150
    r1 s2 | % 151
    r1 s2 | % 152
    r1 s2 | % 153
    r1 s2 | % 154
    r1 s2 \pageBreak | % 155
    r1 s2 | % 156
    r1 s2 | % 157
    r1 s2 | % 158
    r1 s2 \break | % 159
    r1 s2 | \barNumberCheck #160
    r1 s2 | % 161
    r1 s2 | % 162
    r1 s2 \pageBreak | % 163
    r1 s2 | % 164
    r1 s2 | % 165
    r1 s2 | % 166
    r1 s2 \pageBreak | % 167
    r1 s2 | % 168
    r1 s2 | % 169
    r1 s2 | \barNumberCheck #170
    r1 s2 \pageBreak | % 171
    r1 s2 | % 172
    r1 s2 | % 173
    r1 s2 | % 174
    r1 s2 \pageBreak | % 175
    \numericTimeSignature\time 4/4  \stemDown g'8 -. _\p r8 \stemDown d8
    -. r8 \stemDown a8 -. r8 \stemDown e8 -. r8 | % 176
    \stemDown a8 -. r8 \stemDown d8 -. r8 \stemDown b8 -. r8 \stemDown
    d,8 -. _\< \stemDown e8 -. | % 177
    \stemDown fis8 -. \stemDown g8 -. \stemDown a8 -. \stemDown b8 -.
    \stemDown c8 -. _\! _\mf r8 \stemDown b8 -. \stemDown a8 -. | % 178
    \stemDown d8 -. _\> r8 \stemDown g,8 -. r8 \stemDown g8 -. r8 _\! r4
    | % 179
    R1 \pageBreak | \barNumberCheck #180
    R1 | % 181
    \time 12/8  \stemDown e'8 -. _\mp \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. | % 182
    \stemDown e8 ( -> \stemDown d8 \stemDown c8 \stemDown b8 \stemDown a8
    \stemDown g8 ) r2.*2/3 s4 | % 183
    r1 s2 \pageBreak | % 184
    r2.*2/3 r4.*2/3 \stemDown d8 _\f \stemDown d8 \stemDown d8 s4. | % 185
    \stemDown bes8 ( \stemDown c8 \stemDown d8 \stemDown es8 \stemDown d8
    \stemDown c8 \stemDown bes8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 | % 186
    r1 s2 | % 187
    r1 s2 | % 188
    r1 s2 \pageBreak | % 189
    \stemDown d8 ( \stemDown es8 \stemDown f8 \stemDown g8 \stemDown f8
    \stemDown es8 \stemDown d8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 |
    \barNumberCheck #190
    r1 s2 | % 191
    \numericTimeSignature\time 4/4  \stemDown g8 ( _\ff \stemDown fis8
    \stemDown e8 \stemDown d8 ) r2 | % 192
    \stemDown g8 ( _\ff \stemDown f8 \stemDown e8 \stemDown d8 ) r2 | % 193
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 ( _\ff \stemDown fis8 \stemDown e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown cis8 \stemDown b8 ) }
    \stemUp a8 r8 r4 \pageBreak | % 194
    R1*7 \pageBreak | % 201
    R1*3 | % 204
    \stemDown d8 _\p -\markup{ \italic {leggieramente} } _\< r8 \stemUp
    a8 r16 \stemUp a16 \stemDown d8 r8 \stemUp a8 r8 | % 205
    \stemDown d8 -> _\! _\mp \stemDown a'8 -> r4 r2 \pageBreak | % 206
    R1*5 \pageBreak | % 211
    R1 | % 212
    \stemDown g8 _\ff r8 \stemDown d8 r16 \stemDown d16 \stemDown g8 r8
    \stemDown d8 r8 | % 213
    \stemDown a'8 -> \stemDown d8 -> r4 r2 | % 214
    \stemUp a,8 _\fff r8 \stemUp e8 r16 \stemUp e16 \stemUp a8 r8
    \stemUp e8 r8 | % 215
    \stemDown a8 -> \stemDown d8 ~ -> \stemDown d2. \pageBreak | % 216
    \stemUp a8 _\fff r8 \stemUp e8 r16 \stemUp e16 \stemUp a8 r8 \stemUp
    e8 r8 | % 217
    \stemDown a8 -> \stemDown d8 ~ -> \stemDown d8 \stemDown d8 \stemUp
    a8 \stemUp e4 \stemUp e8 | % 218
    \stemUp a8 \stemDown d4 \stemDown d8 \stemUp a8 \stemUp e4 \stemUp e8
    | % 219
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp a8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp a8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 \stemUp e8 r8 }
    | \barNumberCheck #220
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp a8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp a8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 \stemUp e8 r8 }
    \pageBreak | % 221
    \times 2/3  {
        \stemUp a8 -> \stemUp a8 -> r8 }
    r4 r2 | % 222
    r4 \stemUp d,32 ( _\sempre _\fff \stemUp e32 \stemUp fis32 \stemUp g32
    \stemUp a32 \stemUp b32 \stemUp c32 \stemUp d32 ) \stemDown e16 (
    \stemDown d16 \stemDown c16 \stemDown b16 \stemUp a8 ) r8 | % 223
    R1 | % 224
    r4 \stemUp d,32 ( \stemUp e32 \stemUp fis32 \stemUp g32 \stemUp a32
    \stemUp b32 \stemUp c32 \stemUp d32 ) \stemDown e16 ( \stemDown d16
    \stemDown c16 \stemDown b16 \stemUp a8 ) r8 \pageBreak | % 225
    r2 r4 \stemUp d,32 ( \stemUp e32 \stemUp fis32 \stemUp g32 \stemUp a32
    \stemUp b32 \stemUp c32 \stemUp d32 ) | % 226
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemUp fis8 ) r8 r4 \stemUp d32 ( \stemUp e32 \stemUp fis32 \stemUp
    g32 \stemUp a32 \stemUp b32 \stemUp c32 \stemUp d32 ) | % 227
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemUp fis8 ) r8 r4 \stemUp d32 ( \stemUp e32 \stemUp fis32 \stemUp
    g32 \stemUp a32 \stemUp b32 \stemUp c32 \stemUp d32 ) \pageBreak | % 228
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemUp fis8 ) r8 r2 | % 229
    \stemUp g8 _\fff r8 \stemUp d8 r16 \stemUp d16 \stemUp g8 r8 \stemUp
    d8 r8 | \barNumberCheck #230
    \stemUp g8 -> \stemUp c8 ~ ^> \stemDown c2 \stemUp b8 r16 \stemUp a16
    | % 231
    \stemDown d8 r8 \acciaccatura { \stemUp a8 ( } \stemUp g8 ) r16
    \stemUp fis16 \stemUp g8 r8 \stemUp d8 r8 | % 232
    \stemUp g2. -> \stemDown b8 r16 \stemDown d16 \pageBreak | % 233
    \stemDown e8 r8 \acciaccatura { \stemUp a,8 ( } \stemUp g8 ) r16
    \stemUp fis16 \stemUp g8 r8 \stemUp d8 r8 | % 234
    \stemUp g2. -> \stemDown b8 r16 \stemDown d16 | % 235
    \stemDown g4 ( -> \stemDown fis8 ) r16 \stemDown g16 \stemDown e4 (
    -> \stemDown dis8 ) r16 \stemDown e16 | % 236
    \stemDown c4 ( -> \stemDown b8 ) r16 \stemDown c16 \stemUp a4 ( ->
    \stemUp g8 ) r16 \stemUp a16 -. | % 237
    \stemUp e8 -. r16 \stemUp fis16 ( \stemUp g8 ) r16 \stemUp b16 (
    \stemDown e8 ) r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown a16
    -. \pageBreak | % 238
    \stemDown b2 ~ -> \stemDown b8 \stemDown a16 ( \stemDown g16 \once
    \omit TupletBracket
    \times 4/6  {
        \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown c16
        \stemDown b16 \stemDown a16 }
    | % 239
    \stemUp g8 ) r8 \stemUp d8 r16 \stemUp d16 \stemUp g8 r8 \stemUp d8
    r8 | \barNumberCheck #240
    \stemUp g8 -> \stemUp c8 ~ ^> \stemDown c2 \stemUp b8 r16 \stemUp a16
    | % 241
    \stemDown d8 r8 \acciaccatura { \stemUp a8 ( } \stemUp g8 ) r16
    \stemUp fis16 \stemUp g8 r8 \stemUp d8 r8 | % 242
    \stemUp g2. -> \stemDown b8 r16 \stemDown d16 \pageBreak | % 243
    \stemDown e8 r8 \acciaccatura { \stemUp a,8 ( } \stemUp g8 ) r16
    \stemUp fis16 \stemUp g8 r8 \stemUp d8 r8 | % 244
    \stemUp g2. -> \stemDown b8 r16 \stemDown d16 | % 245
    \stemDown es4 ( -> \stemDown d8 ) r16 \stemDown c16 \stemDown bes8 r8
    \stemDown f'8 r16 \stemDown fis16 | % 246
    \stemDown g4 ( -> \stemDown f8 ) r16 \stemDown es16 \stemDown d8 r8
    \stemDown g8 r16 \stemDown a16 | % 247
    \stemDown b2. -> \stemDown a8 r16 \stemDown b,16 \pageBreak | % 248
    \stemDown g'2. -> \stemDown fis8 r16 \stemDown b,16 | % 249
    \stemDown e4 ( -> \stemUp d8 ) r16 \stemUp e,16 \stemDown c'4 ( ->
    \stemUp b8 ) r16 \stemUp e,16 | \barNumberCheck #250
    \stemUp a8 r8 r4 r2 | % 251
    R1*3 \pageBreak | % 254
    R1*2 | % 256
    r2 r4 \stemDown d'16 ( _\ff \stemDown e16 \stemDown d16 \stemDown e16
    | % 257
    \stemDown b8 ) r8 \stemDown fis16 ( \stemDown g16 \stemDown fis16
    \stemDown g16 \stemDown e8 ) r8 \stemUp ais,16 ( \stemUp b16 \stemUp
    ais16 \stemUp b16 ) | % 258
    \stemDown c16 ( \stemDown d16 \stemDown c16 \stemDown b16 ) \stemUp
    a16 ( \stemUp b16 \stemUp a16 \stemUp g16 ) \stemUp fis16 ( \stemUp
    g16 \stemUp e16 \stemUp fis16 \stemUp d8 ) r8 \pageBreak | % 259
    R1 | \barNumberCheck #260
    r2 r4 \stemDown b''16 ( _\ff \stemDown c16 \stemDown b16 \stemDown c16
    | % 261
    \stemDown g8 ) r8 \stemDown dis'16 ( \stemDown e16 \stemDown dis16
    \stemDown e16 \stemDown c8 ) r8 \stemUp g,16 ( \stemUp gis16 \stemUp
    g16 \stemUp gis16 ) | % 262
    \stemUp a16 ( \stemUp b16 \stemUp a16 \stemUp g16 ) \stemUp fis16 (
    \stemUp g16 \stemUp fis16 \stemUp e16 \stemUp d16 ) r16 r8 r4 | % 263
    R1 \pageBreak | % 264
    r2 r4 \stemDown d''16 ( _\ff \stemDown e16 \stemDown d16 \stemDown e16
    | % 265
    \stemDown b8 ) r8 \stemDown fis16 ( \stemDown g16 \stemDown fis16
    \stemDown g16 \stemDown e8 ) r8 \stemUp ais,16 ( \stemUp b16 \stemUp
    ais16 \stemUp b16 ) | % 266
    \stemDown c16 ( \stemDown d16 \stemDown c16 \stemDown b16 ) \stemUp
    a16 ( \stemUp b16 \stemUp a16 \stemUp g16 ) \stemUp fis16 ( \stemUp
    g16 \stemUp e16 \stemUp fis16 \stemUp d8 ) r8 | % 267
    R1*2 \pageBreak | % 269
    R1*3 | % 272
    \stemUp g4 ~ _\fff \stemUp g8 r8 \stemUp gis4 ~ \stemUp gis8 r8 | % 273
    \stemUp a8 r8 \stemDown bes8 r8 \stemDown b8 r8 \stemDown c8 r8
    \pageBreak | % 274
    \stemDown cis8 r8 \stemDown d8 r8 \stemDown e8 r8 r4 | % 275
    R1*6 \pageBreak | % 281
    R1 | % 282
    r2 r4 \stemUp d,16 ( _\fff \stemUp dis16 \stemUp e16 \stemUp fis16 | % 283
    \stemUp g8 ) r8 \stemUp d8 r16 \stemUp d16 \stemUp g8 r8 \stemUp d8
    r8 | % 284
    \stemUp g8 -> \stemUp c8 ~ ^> \stemDown c2 \stemUp b8 r16 \stemUp a16
    | % 285
    \stemDown d8 r8 \acciaccatura { \stemUp a8 ( } \stemUp g8 ) r16
    \stemUp fis16 \stemUp g8 r8 \stemUp d8 r8 | % 286
    \stemUp g2. -> \stemDown b8 r16 \stemDown d16 \pageBreak | % 287
    \stemDown e8 r8 \acciaccatura { \stemUp a,8 ( } \stemUp g8 ) r16
    \stemUp fis16 \stemUp g8 r8 \stemUp d8 r8 | % 288
    \stemUp g2. -> \stemDown b8 r16 \stemDown d16 | % 289
    \stemDown g4 ( -> \stemDown fis8 ) r16 \stemDown g16 \stemDown e4 (
    -> \stemDown dis8 ) r16 \stemDown e16 | \barNumberCheck #290
    \stemDown c4 ( -> \stemDown b8 ) r16 \stemDown c16 \stemUp a4 ( ->
    \stemUp g8 ) r16 \stemUp a16 -. | % 291
    \stemUp e8 -. r16 \stemUp fis16 ( \stemUp g8 ) r16 \stemUp b16 (
    \stemDown e8 ) r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown a16
    -. \pageBreak | % 292
    \stemDown b2 ~ -> \stemDown b8 \stemDown a16 ( \stemDown g16 \once
    \omit TupletBracket
    \times 4/6  {
        \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown c16
        \stemDown b16 \stemDown a16 }
    | % 293
    \stemUp g8 ) r8 \stemUp d8 r16 \stemUp d16 \stemUp g8 r8 \stemUp d8
    r8 | % 294
    \stemUp g8 -> \stemUp c8 ~ ^> \stemDown c2 \stemUp b8 r16 \stemUp a16
    | % 295
    \stemDown d8 r8 \acciaccatura { \stemUp a8 ( } \stemUp g8 ) r16
    \stemUp fis16 \stemUp g8 r8 \stemUp d8 r8 | % 296
    \stemUp g2. -> \stemDown b8 r16 \stemDown d16 \pageBreak | % 297
    \stemDown e8 r8 \acciaccatura { \stemUp a,8 ( } \stemUp g8 ) r16
    \stemUp fis16 \stemUp g8 r8 \stemUp d8 r8 | % 298
    \stemUp g2. -> \stemDown b8 r16 \stemDown d16 | % 299
    \stemDown es4 ( -> \stemDown d8 ) r16 \stemDown c16 \stemDown bes8 r8
    \stemDown f'8 r16 \stemDown fis16 | \barNumberCheck #300
    \stemDown g4 ( -> \stemDown f8 ) r16 \stemDown es16 \stemDown d8 r8
    \stemDown g8 r16 \stemDown a16 | % 301
    \stemDown b2. -> \stemDown a8 r16 \stemDown b,16 \pageBreak | % 302
    \stemDown g'2. -> \stemDown fis8 r16 \stemDown b,16 | % 303
    \stemDown e4 ( -> \stemUp d8 ) r16 \stemUp e,16 \stemDown c'4 ( ->
    \stemUp b8 ) r16 \stemUp e,16 | % 304
    \stemUp a8 r8 r4 r2 | % 305
    R1*2 | % 307
    \stemUp a4 ( -> _\fff \stemUp g8 ) r16 \stemUp d16 \stemUp a'4 ( ->
    \stemUp g8 ) r16 \stemUp dis16 \pageBreak | % 308
    \stemDown b'4 ( -> \stemUp a8 ) r16 \stemUp e16 \stemDown c'4 ( ->
    \stemUp b8 ) r16 \stemUp e,16 | % 309
    \stemDown d'4 ( -> \stemDown c8 ) r16 \stemDown a16 \stemDown d4 (
    -> \stemDown cis8 ) r16 \stemDown a16 | \barNumberCheck #310
    \stemDown e'4 ( -> \stemDown d8 ) r16 \stemDown a16 \stemDown e'4 (
    -> \stemDown dis8 ) r16 \stemDown a16 | % 311
    \stemDown f'4 ( -> \stemDown e8 ) r16 \stemDown a,16 \stemDown g'4 (
    -> \stemDown fis8 ) r16 \stemDown c16 | % 312
    \stemDown a'8 ( _\ffff \stemDown g8 \stemDown d8 \stemDown g8 )
    \stemDown a8 ( \stemDown g8 \stemDown es8 \stemDown g8 ) | % 313
    \stemDown a8 ( \stemDown g8 \stemDown e8 \stemDown g8 ) \stemDown a8
    ( \stemDown g8 \stemDown es8 \stemDown g8 ) \pageBreak | % 314
    \stemDown a8 ( \stemDown g8 \stemDown fis8 \stemDown e8 ) \stemDown
    d8 ( \stemDown cis8 \stemDown c8 \stemDown b8 ) | % 315
    \stemUp a8 ( \stemUp g8 \stemUp fis8 \stemUp e8 \stemUp d8 ) r8 r4 | % 316
    R1*4 \pageBreak | \barNumberCheck #320
    R1*2 | % 322
    g''1 ~ _\ff _\markup{ \small\italic {cresc.} } \startTrillSpan | % 323
    \stemDown g4 \stemDown fis4 \stemDown e4 \stemDown d4 | % 324
    \stemDown dis8 \stopTrillSpan _\fff r8 \once \omit TupletBracket
    \times 4/7  {
        \stemDown g,,16*161/160 ( \stemDown a16*161/160 \stemDown b16*161/160
        \stemDown cis16*161/160 \stemDown dis16*161/160 \stemDown e16*161/160
        \stemDown fis16*161/160 }
    \stemDown g8 ) r16 \stemDown fis16 -. \stemDown g8 -. r16 \stemDown
    dis16 -. \pageBreak | % 325
    \stemDown e8 -. r8 r4 r2 | % 326
    R1*2 \pageBreak | % 328
    r2 r4 \once \omit TupletBracket
    \times 4/7  {
        \stemDown d16*161/160 ( \stemDown e16*161/160 \stemDown fis16*161/160
        \stemDown g16*161/160 \stemDown a16*161/160 \stemDown b16*161/160
        \stemDown cis16*161/160 }
    | % 329
    \stemDown d16 ) \stemDown e16 ( \stemDown fis16 \stemDown g16
    \stemDown a16 \stemDown g16 \stemDown fis16 \stemDown e16 )
    \stemDown d16 ( \stemDown c16 \stemDown b16 \stemDown a16 )
    \stemDown g16 ( \stemDown fis16 \stemDown e16 \stemDown d16 ) |
    \barNumberCheck #330
    \stemUp g,8 _\sempre _\fff r8 \stemUp d8 r16 \stemUp d16 \stemUp g8
    r8 r4 | % 331
    \stemDown g8 -> \stemDown d'8 ^> \stemDown g16 ( \stemDown a16
    \stemDown b16 \stemDown cis16 \stemDown d8 ) r8 \stemDown d16 (
    \stemDown c16 \stemDown b16 \stemDown a16 \pageBreak | % 332
    \stemDown g8 ) r8 \stemUp d,8 r16 \stemUp d16 \stemUp g8 r8 r4 | % 333
    \stemDown g8 -> \stemDown d'8 ^> \stemDown g16 ( \stemDown a16
    \stemDown b16 \stemDown cis16 \stemDown d8 ) r8 \stemDown d16 (
    \stemDown c16 \stemDown b16 \stemDown a16 | % 334
    \stemDown g8 ) r8 \stemDown d'16 ( \stemDown dis16 \stemDown e16
    \stemDown fis16 \stemDown g8 ) r8 \stemDown d16 ( \stemDown dis16
    \stemDown e16 \stemDown fis16 | % 335
    \stemDown g8 ) r8 \stemDown d16 ( \stemDown dis16 \stemDown e16
    \stemDown fis16 \stemDown g8 ) r8 \stemDown d16 ( \stemDown dis16
    \stemDown e16 \stemDown fis16 \pageBreak | % 336
    \stemDown g8 ) r8 \stemDown d16 ( \stemDown dis16 \stemDown e16
    \stemDown fis16 \stemDown g8 ) r8 \stemDown d16 ( \stemDown dis16
    \stemDown e16 \stemDown fis16 | % 337
    \stemDown g8 ) r8 \stemDown d16 ( \stemDown dis16 \stemDown e16
    \stemDown fis16 \stemDown g8 ) r8 \stemDown d16 ( \stemDown dis16
    \stemDown e16 \stemDown fis16 | % 338
    \stemDown g8 ) \stemDown g,8 \stemDown fis8 \stemDown e8 \stemDown d8
    \stemDown c8 \stemDown b8 \stemDown a8 | % 339
    \stemUp g8 r8 r4 r2 | \barNumberCheck #340
    R1 \pageBreak | % 341
    r2 \stemDown d'8 r8 r4 | % 342
    \stemDown g8 r8 \stemDown g8 r8 r4 \stemDown g8 r8 | % 343
    r4 \stemDown g8 r8 r4 \stemDown d8 r8 | % 344
    \stemUp g,8 r8 r4 r2 | % 345
    R1*3 \bar "|."
    }

PartPThreeVoiceTwo =  \relative e' {
    \clef "treble" \time 4/4 \key g \major \transposition c'' | % 1
     \once \override NoteHead.style = ##f e1 s1*3 \pageBreak s1*3 \bar
    "||"
    s1*2 \pageBreak s1*5 \break s1*5 \pageBreak s1*4 \break s1*4
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1 | % 37
    \numericTimeSignature\time 4/4  s1*4 \pageBreak s1*2 | % 43
    \time 12/8  s2*9 \pageBreak s2*15 \pageBreak s2*15 \pageBreak | % 56
    \numericTimeSignature\time 4/4  s1*5 \pageBreak s1*5 \pageBreak s1*5
    \bar "||"
    \pageBreak | % 71
    \key e \major s1*5 \break s1*5 \pageBreak s1*5 \pageBreak s1*4
    \pageBreak s1*6 \pageBreak s1*6 \break s1*5 \pageBreak s1*6 \break
    s1*5 \pageBreak s1*5 \break s1*5 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1 | % 137
    \time 12/8  s4*11 \bar "||"
    s4 | % 139
    \key g \major s1. \pageBreak s2*15 \pageBreak s2*15 \pageBreak s2*15
    \pageBreak s1*6 \break s1*6 \pageBreak s1*6 \pageBreak s1*6
    \pageBreak s1*6 \pageBreak | % 175
    \numericTimeSignature\time 4/4  s1*5 \pageBreak s1 | % 181
    \time 12/8  s2*9 \pageBreak s2*15 \pageBreak s1*3 | % 191
    \numericTimeSignature\time 4/4  s1*3 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*4
    \pageBreak s1*3 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*6 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*7 \pageBreak s1*6
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*6
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*5 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*5 \pageBreak s1*7 \bar
    "|."
    }

PartPFourVoiceOne =  \relative d' {
    \clef "treble" \time 4/4 \key g \major | % 1
    R1*2 | % 3
    r8 \stemUp <d fis>8 -. _\p \stemUp <a' c>8 -. \stemUp <d, fis>8 -.
    \stemUp <a' c>8 -. \stemUp <e g>8 -. \stemUp <a c>8 -. \stemUp <fis
        a>8 -. | % 4
    R1 \pageBreak | % 5
    R1*2 | % 7
    r8 \stemUp <b, dis>8 -. _\p \stemUp <fis' a>8 -. \stemUp <b, dis>8
    -. \stemUp <fis' a>8 -. \stemUp <c e>8 -. \stemUp <fis a>8 -.
    \stemUp <dis fis>8 -. \bar "||"
    R1 | % 9
    \stemUp e8 -. ^\p r8 \stemUp b8 -. r16 \stemUp b16 -. \stemUp e8 -.
    r8 \stemUp b8 -. r8 \pageBreak | \barNumberCheck #10
    \stemUp e8 -. ^\< \stemUp a8 ~ ^> \stemUp a4 ~ \stemUp a8 r8 ^\! r4
    | % 11
    \stemUp <e e'>8 -. _\mp r8 \stemUp <b b'>8 -. r16 \stemUp <b b'>16
    -. \stemUp <e e'>8 -. r8 \stemUp <b b'>8 -. r8 | % 12
    \stemDown <e e'>8 -. _\< \stemDown <a a'>8 ~ ^> ~ \stemDown <a a'>4
    ~ ~ \stemDown <a a'>8 r8 _\! r4 | % 13
    R1*2 \break | % 15
    R1*4 | % 19
    <b b'>1 ~ ~ _\pp _\< \pageBreak | \barNumberCheck #20
    \stemDown <b b'>8 _\! _\p r8 \stemUp <e, e'>8 -. r16 \stemUp <e e'>16
    -. \stemDown <b' b'>8 -. r8 \stemUp <e, e'>8 -. r8 | % 21
    \stemDown <b' b'>8 -. r8 r4 r2 | % 22
    R1 | % 23
    <b b'>1 ~ ~ _\pp _\< \break | % 24
    \stemDown <b b'>8 _\! _\p r8 \stemUp <e, e'>8 -. r16 \stemUp <e e'>16
    -. \stemDown <b' b'>8 -. r8 \stemUp <e, e'>8 -. r8 | % 25
    \stemDown <b' b'>8 -. r8 r4 r2 | % 26
    R1 | % 27
    <d, d'>1 ~ ~ _\pp _\< \pageBreak | % 28
    \stemUp <d d'>8 _\! r8 \stemUp <d d'>8 -. _\p _\< r16 \stemUp <d d'>16
    -. \stemUp <dis dis'>8 -. r8 \stemUp <e e'>8 -. r8 | % 29
    \stemDown <fis fis'>8 -. _\! _\mp r8 r4 r2 | \barNumberCheck #30
    R1*2 \pageBreak | % 32
    R1*4 \pageBreak | % 36
    R1*5 \pageBreak | % 41
    R1*5 \pageBreak | % 46
    \time 12/8  r2.*2/3 r4.*2/3 \stemDown d'8 _\f ^ "a 2" \stemDown d8
    \stemDown d8 s4. | % 47
    \stemDown bes8 ( \stemDown c8 \stemDown d8 \stemDown es8 \stemDown d8
    \stemDown c8 \stemDown bes8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 | % 48
    r1 s2 | % 49
    \stemDown <b b'>4. _\ff -\markup{ \italic {marcato} } \stemDown <ais
        ais'>4. \stemDown <gis gis'>4. \stemDown <fis fis'>4 ( ~ ~
    \stemDown <fis fis'>16 \stemDown <e e'>16 ) | \barNumberCheck #50
    \stemUp <dis dis'>8 r8*2/3 r8*2/3 r4.*2/3 r4.*2/3 \stemDown <ais'
        ais'>8 _\ff \stemDown <ais ais'>8 \stemDown <ais ais'>8 s1*1/3
    \pageBreak | % 51
    \stemDown <fis fis'>8 ( \stemDown <gis gis'>8 \stemDown <ais ais'>8
    \stemDown <b b'>8 \stemDown <ais ais'>8 \stemDown <gis gis'>8
    \stemDown <fis fis'>8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 | % 52
    r1 s2 | % 53
    r1 s2 | % 54
    r1 s2 | % 55
    \numericTimeSignature\time 4/4  r2 \stemDown fis'4 ^> _\mf ^ "a 2"
    \stemDown fis8 r16 \stemDown fis16 \pageBreak | % 56
    \stemUp fis,8 r8 r4 \stemDown fis'4 -> _\ff \stemDown fis8 r16
    \stemDown fis16 | % 57
    \stemUp fis,8 _\pp r8 r4 r2 | % 58
    R1*2 | \barNumberCheck #60
    r2 \stemDown fis'4 -> _\f \stemDown fis8 r16 \stemDown fis16
    \pageBreak | % 61
    b1 -> _\p _\markup{ \small\italic {poco a poco cresc.} }
    \startTrillSpan | % 62
    g1 -> | % 63
    b1 -> | % 64
    g1 -> | % 65
    b1 -> \pageBreak | % 66
    c1 -> | % 67
    <dis, dis'>1 -> \stopTrillSpan _\f | % 68
    <g g>1 -> | % 69
    \stemUp <fis, dis'>8 -> _\ff r8 r4 r2 | \barNumberCheck #70
    R1 \bar "||"
    \pageBreak | % 71
    \key e \major R1*5 \break | % 76
    R1*3 | % 79
    r2 r4 \stemDown cis'8 _\mf ^ "a 2" r8 | \barNumberCheck #80
    \stemDown cis4 ~ _\< \stemDown cis8 \stemDown cis16 \stemDown cis16
    \stemDown bis8 _\! _\f \stemDown b8 r4 \pageBreak | % 81
    R1*5 \pageBreak | % 86
    R1 | % 87
    \stemUp <c, g'>8 _\mf _\< r8 r4 \stemUp <b d>8 r8 r4 | % 88
    \stemUp <e c'>8 r8 r4 \stemUp <b e>8 r8 \stemUp e'8 ( -. _\! ^\f r16
    \stemUp fis16 ) -. | % 89
    \stemUp gis2. -> _\f \stemUp fis8 ( -. r16 \stemUp gis,16 ) -.
    \pageBreak | \barNumberCheck #90
    \stemUp e'2. -> \stemUp dis8 ( -. r16 \stemUp gis,16 ) -. | % 91
    \stemUp cis8 r8 r4 _\< r2 | % 92
    R1 | % 93
    r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d, a'>8 \stemUp <d a'>8 \stemUp <d a'>8 }
    \stemUp <d a'>2 ~ ~ | % 94
    \stemUp <d a'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <dis dis'>8 \stemUp <dis dis'>8 \stemUp <dis dis'>8 }
    \stemUp <dis dis'>2 ~ ~ | % 95
    \stemUp <dis dis'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <gis gis'>8 \stemDown <gis gis'>8 \stemDown <gis gis'>8
        }
    \stemDown <gis gis'>2 ~ ~ \pageBreak | % 96
    \stemDown <gis gis'>8 r8 \stemUp a'8 r16 \stemUp dis,16 \stemUp e8 r8
    r4 | % 97
    R1*5 \break | % 102
    R1*5 \pageBreak | % 107
    R1*2 | % 109
    \stemUp fis,2 ^\ff \stemUp <cis fisis>2 _\ff | \barNumberCheck #110
    \stemUp <bis gis'>2 \stemUp <cis a'>2 | % 111
    \stemUp <cis ais'>8 r8 \stemUp <e b'>8 r8 \stemUp <fis bis>8 r8
    \stemUp <e cis'>8 r8 | % 112
    \stemUp <fis d'>8 r8 \stemUp <fis dis'>8 r8 r2 \break | % 113
    R1*5 \pageBreak | % 118
    R1*3 | % 121
    r2 r4 \stemDown cis'8 _\mf ^ "a 2" r8 | % 122
    \stemDown cis4 ~ _\< \stemDown cis8 \stemDown cis16 \stemDown cis16
    \stemDown bis8 _\! _\f \stemDown b8 r4 \break | % 123
    R1*5 \pageBreak | % 128
    R1 | % 129
    \stemUp <c, g'>8 _\f r8 r4 \stemUp <b d>8 r8 r4 | \barNumberCheck
    #130
    \stemUp <e c'>8 r8 r4 \stemDown d'16 ( ^ "a 2" \stemDown c16
    \stemDown b16 \stemDown a16 \stemUp g16 \stemUp f16 \stemUp e16
    \stemUp d16 ) | % 131
    \stemUp <c c'>2 \stemUp <d d'>8 r8 r4 \pageBreak | % 132
    r4 \stemDown c''4 -- ^ "a 2" \stemDown d16 ( \stemDown c16 \stemDown
    b16 \stemDown a16 \stemDown g16 \stemDown f16 \stemDown e16
    \stemDown d16 | % 133
    \stemDown c8 ) r8 r4 \stemUp <b, d>8 r8 r4 | % 134
    \stemUp <e c'>8 r8 r4 \stemDown d'16 ( ^ "a 2" \stemDown c16
    \stemDown b16 \stemDown a16 \stemUp g16 \stemUp f16 \stemUp e16
    \stemUp d16 ) | % 135
    \stemUp <c c'>2 \stemUp <d d'>8 r8 r4 \pageBreak | % 136
    r4 \stemDown c''4 -- ^ "a 2" \stemDown d16 ( \stemDown c16 \stemDown
    b16 \stemDown a16 \stemDown g16 \stemDown f16 \stemDown e16
    \stemDown d16 | % 137
    \time 12/8  \stemDown c8 ) r8*2/3 r8*2/3 r4.*2/3 \stemUp <g c>4. ->
    _\f \stemDown <g d'>8 r8*2/3 r8*2/3 s1*7/24 | % 138
    r2.*2/3 \stemUp <g c>4. ^> _\mf \stemDown <g d'>8 r4*2/3 \bar "||"
    s1*1/3 | % 139
    \key g \major r1 s2 \pageBreak | \barNumberCheck #140
    r1 s2 | % 141
    \numericTimeSignature\time 4/4  r8 \stemUp <d fis>8 -. _\p \stemUp
    <a' c>8 -. \stemUp <d, fis>8 -. \stemUp <a' c>8 -. \stemUp <e g>8 -.
    \stemUp <a c>8 -. \stemUp <fis a>8 -. | % 142
    R1*3 \pageBreak | % 145
    r8 \stemUp <b, dis>8 -. _\p \stemUp <fis' a>8 -. \stemUp <b, dis>8
    -. \stemUp <fis' a>8 -. \stemUp <c e>8 -. \stemUp <fis a>8 -.
    \stemUp <dis fis>8 -. | % 146
    R1 | % 147
    \stemUp e8 -. ^\p r8 \stemUp b8 -. r16 \stemUp b16 -. \stemUp e8 -.
    r8 \stemUp b8 -. r8 | % 148
    \stemUp e8 -. ^\< \stemUp a8 ~ ^> \stemUp a4 ~ \stemUp a8 r8 ^\! r4
    | % 149
    \stemUp <e e'>8 -. _\mp r8 \stemUp <b b'>8 -. r16 \stemUp <b b'>16
    -. \stemUp <e e'>8 -. r8 \stemUp <b b'>8 -. r8 \pageBreak |
    \barNumberCheck #150
    \stemDown <e e'>8 -. _\< \stemDown <a a'>8 ~ ^> ~ \stemDown <a a'>4
    ~ ~ \stemDown <a a'>8 r8 _\! r4 | % 151
    R1*4 \pageBreak | % 155
    R1*2 | % 157
    <b b'>1 ~ ~ _\pp _\< | % 158
    \stemDown <b b'>8 _\! _\p r8 \stemUp <e, e'>8 -. r16 \stemUp <e e'>16
    -. \stemDown <b' b'>8 -. r8 \stemUp <e, e'>8 -. r8 \break | % 159
    \stemDown <b' b'>8 -. r8 r4 r2 | \barNumberCheck #160
    R1 | % 161
    <b b'>1 ~ ~ _\pp _\< | % 162
    \stemDown <b b'>8 _\! _\p r8 \stemUp <e, e'>8 -. r16 \stemUp <e e'>16
    -. \stemDown <b' b'>8 -. r8 \stemUp <e, e'>8 -. r8 \pageBreak | % 163
    \stemDown <b' b'>8 -. r8 r4 r2 | % 164
    R1 | % 165
    <d, d'>1 ~ ~ _\pp _\< | % 166
    \stemUp <d d'>8 r8 \stemUp <d d'>8 -. _\! _\p _\< r16 \stemUp <d d'>16
    -. \stemUp <dis dis'>8 -. r8 \stemUp <e e'>8 -. r8 \pageBreak | % 167
    \stemDown <fis fis'>8 -. _\! _\mp r8 r4 r2 | % 168
    R1*3 \pageBreak | % 171
    R1*4 \pageBreak | % 175
    R1*5 \pageBreak | \barNumberCheck #180
    R1*4 \pageBreak | % 184
    \time 12/8  r2.*2/3 r4.*2/3 \stemDown d'8 ^ "a 2" _\f \stemDown d8
    \stemDown d8 s4. | % 185
    \stemDown bes8 ( \stemDown c8 \stemDown d8 \stemDown es8 \stemDown d8
    \stemDown c8 \stemDown bes8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 | % 186
    r1 s2 | % 187
    r1 s2 | % 188
    r1 s2 \pageBreak | % 189
    \stemDown d8 ( \stemDown es8 \stemDown f8 \stemDown g8 \stemDown f8
    \stemDown es8 \stemDown d8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 |
    \barNumberCheck #190
    r1 s2 | % 191
    r1 s2 | % 192
    r1 s2 | % 193
    \numericTimeSignature\time 4/4  \stemDown <a' d>4 _\ff \stemDown
    <fis a>8 \stemDown <d fis>8 \stemDown <a d>4 \stemUp <fis a>4
    \pageBreak | % 194
    \stemUp <d fis>4 \stemUp fis4 \stemUp <e a>8 r8 r4 | % 195
    R1*4 | % 199
    R1*2 \pageBreak | % 201
    \stemUp a8 _\pp _\ leggieramente ^\p -\markup{ \italic
        {leggieramente} } r8 \stemUp e8 r16 \stemUp e16 \stemUp a8 r8
    \stemUp e8 r8 | % 202
    \stemUp a8 -> \stemUp d8 -> r4 r2 | % 203
    \stemDown gis8 _\p ^ "a 2" r8 \stemDown d8 r16 \stemDown d16
    \stemDown gis8 r8 \stemDown d8 r8 | % 204
    \stemDown a'8 -> \stemDown d8 -> r4 r2 | % 205
    R1 \pageBreak | % 206
    \stemUp e,,8 ^\mp r8 \stemUp b8 r16 \stemUp b16 \stemUp e8 r8
    \stemUp b8 r8 | % 207
    \stemUp e8 -> \stemUp a8 -> r4 r2 | % 208
    \stemDown <g g'>8 _\mf r8 \stemUp <d d'>8 r16 \stemUp <d d'>16
    \stemDown <g g'>8 r8 \stemUp <d d'>8 r8 | % 209
    \stemDown <a' a'>8 -> \stemDown <d d'>8 -> r4 r2 | \barNumberCheck
    #210
    \stemUp <e, e'>8 r8 r4 r2 \pageBreak | % 211
    \stemDown cis''8 _\f ^ "a 2" _\< r8 \stemDown g8 r16 \stemDown g16
    \stemDown cis8 r8 \stemDown g8 r8 | % 212
    \stemDown d'8 -> _\! _\ff \stemDown g,8 -> r4 \stemUp e,2 | % 213
    \stemUp eis2 ( \stemUp fis8 ) r8 r4 | % 214
    \stemDown <e' a>8 _\fff r8 \stemDown <c e>8 r16 \stemDown <c e>16
    \stemDown <e a>8 r8 \stemDown <c e>8 r8 | % 215
    \stemDown <fis a>8 -> \stemDown <a d>8 ~ -> ~ \stemDown <a d>2.
    \pageBreak | % 216
    \stemDown <e a>8 _\fff r8 \stemDown <c e>8 r16 \stemDown <c e>16
    \stemDown <e a>8 r8 \stemDown <c e>8 r8 | % 217
    \stemDown <fis a>8 -> \stemDown <a d>8 ~ -> ~ \stemDown <a d>8
    \stemDown <a d>8 \stemDown <e a>8 \stemDown <c e>4 \stemDown <c e>8
    | % 218
    \stemDown <fis a>8 \stemDown <a d>4 \stemDown <a d>8 \stemDown <e a>8
    \stemDown <c e>4 \stemDown <c e>8 | % 219
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <fis a>8 \stemDown <fis a>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a d>8 \stemDown <a d>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <e a>8 \stemDown <e a>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <c e>8 \stemDown <c e>8 r8 }
    | \barNumberCheck #220
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <fis a>8 \stemDown <fis a>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a d>8 \stemDown <a d>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <e a>8 \stemDown <e a>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <c e>8 \stemDown <c e>8 r8 }
    \pageBreak | % 221
    \times 2/3  {
        \stemDown <fis a>8 -> \stemDown <fis a>8 -> r8 }
    r4 r2 | % 222
    r4 \stemUp d,32 ( _\sempre _\fff ^ "a 2" \stemUp e32 \stemUp fis32
    \stemUp g32 \stemUp a32 \stemUp b32 \stemUp c32 \stemUp d32 )
    \stemDown e16 ( \stemDown d16 \stemDown c'16 \stemDown b16 )
    \stemDown a16 ( \stemDown g16 \stemDown fis16 \stemDown e16 ) | % 223
    \stemDown d16 ( \stemDown c16 \stemDown b16 \stemDown a16 ) \stemUp
    g16 ( \stemUp fis16 \stemUp e16 \stemUp d16 ) r2 | % 224
    r4 \stemUp d32 ( \stemUp e32 \stemUp fis32 \stemUp g32 \stemUp a32
    \stemUp b32 \stemUp c32 \stemUp d32 ) \stemDown e16 ( \stemDown d16
    \stemDown c'16 \stemDown b16 ) \stemDown a16 ( \stemDown g16
    \stemDown fis16 \stemDown e16 ) \pageBreak | % 225
    \stemDown d16 ( \stemDown c16 \stemDown b16 \stemDown a16 ) \stemUp
    g16 ( \stemUp fis16 \stemUp e16 \stemUp d16 ) r4 \stemUp d32 (
    \stemUp e32 \stemUp fis32 \stemUp g32 \stemUp a32 \stemUp b32
    \stemUp c32 \stemUp d32 ) | % 226
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemUp fis8 ) r8 r4 \stemUp d32 ( \stemUp e32 \stemUp fis32 \stemUp
    g32 \stemUp a32 \stemUp b32 \stemUp c32 \stemUp d32 ) | % 227
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemUp fis8 ) r8 r4 \stemUp d32 ( \stemUp e32 \stemUp fis32 \stemUp
    g32 \stemUp a32 \stemUp b32 \stemUp c32 \stemUp d32 ) \pageBreak | % 228
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemUp fis8 ) r8 \once \omit TupletBracket
    \times 4/6  {
        \stemDown e'16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemUp fis8 ) r8 | % 229
    \stemUp <d d'>8 _\fff r8 \stemUp <d d'>8 r16 \stemUp <d d'>16
    \stemUp <d d'>8 r8 \stemUp <d d'>8 r8 | \barNumberCheck #230
    \stemUp <g c>8 r8 \stemUp <g c>8 r16 \stemUp <g c>16 \stemUp <fis
        d'>2 | % 231
    \stemDown <g d'>8 r8 \stemDown <c d>8 r8 \stemDown <b d>8 r8
    \stemDown <a d>8 r8 | % 232
    \stemUp <c, c'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>8 }
    \stemUp <d b'>8 r8 r4 \pageBreak | % 233
    \stemDown <g g'>8 r8 \stemDown <c d>8 r8 \stemDown <b d>8 r8
    \stemDown <a d>8 r8 | % 234
    \stemUp <c, c'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>8 }
    \stemUp <d b'>8 r8 r4 | % 235
    \stemUp <d d'>8 r8 r4 \stemUp <b b'>8 r8 r4 | % 236
    \stemDown <e e'>8 -! \stemDown <f f'>8 -! \stemDown <g g'>8 -!
    \stemDown <gis gis'>8 -! \stemDown <e' a>8 r8 r4 | % 237
    \stemDown <b e>8 r8 \stemDown <b e>8 r8 \stemDown <ais g'>8 r8
    \stemDown <b e>8 r8 \pageBreak | % 238
    \stemUp e4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <b e>8 \stemDown <b e>8 \stemDown <b e>8 }
    \stemDown <dis fis>8 \stemDown <d fis>8 r4 | % 239
    \stemUp <d, d'>8 r8 \stemUp <d d'>8 r16 \stemUp <d d'>16 \stemUp <d
        d'>8 r8 \stemUp <d d'>8 r8 | \barNumberCheck #240
    \stemUp <g c>8 r8 \stemUp <g c>8 r16 \stemUp <g c>16 \stemUp <fis
        d'>2 | % 241
    \stemDown <g d'>8 r8 \stemDown <c d>8 r8 \stemDown <b d>8 r8
    \stemDown <a d>8 r8 | % 242
    \stemUp <c, c'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>8 }
    \stemUp <d b'>8 r8 r4 \pageBreak | % 243
    \stemDown <g g'>8 r8 \stemDown <c d>8 r8 \stemDown <b d>8 r8
    \stemDown <a d>8 r8 | % 244
    \stemUp <c, c'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>8 }
    \stemUp <d b'>8 r8 r4 | % 245
    \stemDown <bes' es>8 r8 r4 \stemUp <d, d'>8 r8 r4 | % 246
    \stemUp <es bes'>8 r8 r4 \stemDown <g d'>8 r8 r4 | % 247
    \stemUp <b, b'>2 ~ ~ \stemUp <b b'>8 \stemUp <b b'>16 \stemUp <b b'>16
    \stemUp <b b'>4 ~ ~ \pageBreak | % 248
    \stemUp <b b'>2 ~ ~ \stemUp <b b'>8 \stemUp <b b'>16 \stemUp <b b'>16
    \stemDown <b' dis>8 r8 | % 249
    \stemDown <b e>8 r8 \stemDown <b e>8 r8 \stemDown <c e>8 r8
    \stemDown <b e>8 r8 | \barNumberCheck #250
    \stemDown <a e'>8 r8 \stemDown <bes e>8 r8 \stemUp g8 r8 \stemUp gis8
    r8 | % 251
    \stemUp a8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <c, f>8 \stemUp <c f>8 \stemUp <c f>8 }
    \stemUp <c f>2 ~ ~ | % 252
    \stemUp <c f>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <b b'>8 \stemUp <b b'>8 \stemUp <b b'>8 }
    \stemUp <b b'>2 ~ ~ | % 253
    \stemUp <b b'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g'' b>8 \stemDown <g b>8 \stemDown <g b>8 }
    \stemDown <g b>2 ~ ~ \pageBreak | % 254
    \stemDown <g b>8 r8 \stemUp c8 r16 \stemUp fis,16 \stemUp g8 r8 r4 | % 255
    R1*2 | % 257
    r4 \stemUp d'4 ( ^\ff \stemUp g,8 ) r8 \stemUp g4 ~ | % 258
    \stemUp g4 \stemUp e4 ( \stemUp c4 \stemUp a8 ) r8 \pageBreak | % 259
    R1*2 | % 261
    r4 \stemUp b'4 ( ^\ff \stemUp e,8 ) r8 \stemUp e4 ~ | % 262
    \stemUp e4 \stemUp c4 ( \stemUp a4 \stemUp fis8 ) r8 | % 263
    R1 \pageBreak | % 264
    R1 | % 265
    r4 \stemUp d''4 ( ^\ff \stemUp g,8 ) r8 \stemUp g4 ~ | % 266
    \stemUp g4 \stemUp e4 ( \stemUp c4 \stemUp a8 ) r8 | % 267
    R1*2 \pageBreak | % 269
    \stemUp cis4 ~ ^\fff \stemUp cis8 r8 \stemUp d4 ~ _\fff \stemUp d8 r8
    | \barNumberCheck #270
    \stemDown <a dis>4 ~ ~ \stemDown <a dis>8 r8 \stemDown <gis e'>4 ~ ~
    \stemDown <gis e'>8 r8 | % 271
    \stemDown <a f'>4 ~ ~ \stemDown <a f'>8 r8 \stemDown <a fis'>4 ~ ~
    \stemDown <a fis'>8 r8 | % 272
    \stemDown <es' g>4 ~ ~ \stemDown <es g>8 r8 \stemDown <e gis>4 ~ ~
    \stemDown <e gis>8 r8 | % 273
    \stemDown <e a>8 r8 \stemDown <d f>8 r8 \stemDown <d g>8 r8
    \stemDown <f a>8 r8 \pageBreak | % 274
    \stemDown <g a>8 r8 \stemDown <fis a>8 r8 \stemDown <g a>8 r8 r4 | % 275
    R1 | % 276
    \stemDown <a, d>4 _\fff \stemUp <d, a'>8. \stemUp <d a'>16 \stemDown
    <a' d>4 \stemUp <d, a'>4 | % 277
    \stemDown <a' e'>8 -. \stemDown <e' a>8 -. r4 r2 | % 278
    \stemDown <a, d>4 \stemUp <d, a'>8. \stemUp <d a'>16 \stemDown <a'
        d>4 \stemUp <d, a'>4 | % 279
    \stemDown <a' e'>8 -. \stemDown <e' a>8 -. r4 \stemUp <d, a'>8 -.
    \stemUp <a' d>8 -. r4 | \barNumberCheck #280
    \stemDown <a e'>8 -. \stemDown <e' a>8 -. r4 \stemUp <d, a'>8 -.
    \stemUp <a' d>8 -. r4 \pageBreak | % 281
    \stemDown <e' a>2 \stemDown <a, d>2 | % 282
    \stemUp <e a>2 \stemUp d8 r8 r4 | % 283
    \stemUp <d d'>8 _\fff r8 \stemUp <d d'>8 r16 \stemUp <d d'>16
    \stemUp <d d'>8 r8 \stemUp <d d'>8 r8 | % 284
    \stemUp <g c>8 r8 \stemUp <g c>8 r16 \stemUp <g c>16 \stemUp <fis
        d'>2 | % 285
    \stemDown <g d'>8 r8 \stemDown <c d>8 r8 \stemDown <b d>8 r8
    \stemDown <a d>8 r8 | % 286
    \stemUp <c, c'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>8 }
    \stemUp <d b'>8 r8 r4 \pageBreak | % 287
    \stemDown <g g'>8 r8 \stemDown <c d>8 r8 \stemDown <b d>8 r8
    \stemDown <a d>8 r8 | % 288
    \stemUp <c, c'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>8 }
    \stemUp <d b'>8 r8 r4 | % 289
    \stemUp <d d'>8 r8 r4 \stemUp <b b'>8 r8 r4 | \barNumberCheck #290
    \stemDown <e e'>8 -! \stemDown <f f'>8 -! \stemDown <g g'>8 -!
    \stemDown <gis gis'>8 -! \stemDown <e' a>8 r8 r4 | % 291
    \stemDown <b e>8 r8 \stemDown <b e>8 r8 \stemDown <ais g'>8 r8
    \stemDown <b e>8 r8 \pageBreak | % 292
    \stemUp e4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <b e>8 \stemDown <b e>8 \stemDown <b e>8 }
    \stemDown <dis fis>8 \stemDown <d fis>8 r4 | % 293
    \stemUp <d, d'>8 r8 \stemUp <d d'>8 r16 \stemUp <d d'>16 \stemUp <d
        d'>8 r8 \stemUp <d d'>8 r8 | % 294
    \stemUp <g c>8 r8 \stemUp <g c>8 r16 \stemUp <g c>16 \stemUp <fis
        d'>2 | % 295
    \stemDown <g d'>8 r8 \stemDown <c d>8 r8 \stemDown <b d>8 r8
    \stemDown <a d>8 r8 | % 296
    \stemUp <c, c'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>8 }
    \stemUp <d b'>8 r8 r4 \pageBreak | % 297
    \stemDown <g g'>8 r8 \stemDown <c d>8 r8 \stemDown <b d>8 r8
    \stemDown <a d>8 r8 | % 298
    \stemUp <c, c'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>8 }
    \stemUp <d b'>8 r8 r4 | % 299
    \stemDown <bes' es>8 r8 r4 \stemUp <d, d'>8 r8 r4 | \barNumberCheck
    #300
    \stemUp <es bes'>8 r8 r4 \stemDown <g d'>8 r8 r4 | % 301
    \stemUp <b, b'>2 ~ ~ \stemUp <b b'>8 \stemUp <b b'>16 \stemUp <b b'>16
    \stemUp <b b'>4 ~ ~ \pageBreak | % 302
    \stemUp <b b'>2 ~ ~ \stemUp <b b'>8 \stemUp <b b'>16 \stemUp <b b'>16
    \stemDown <b' dis>8 r8 | % 303
    \stemDown <b e>8 r8 \stemDown <b e>8 r8 \stemDown <c e>8 r8
    \stemDown <b e>8 r8 | % 304
    \stemDown <a e'>4 ~ -> ~ _\sempre _\fff \stemDown <a e'>8 r8
    \stemDown <a es'>4 ~ -> ~ \stemDown <a es'>8 r8 | % 305
    \stemDown <a d>4 ~ -> ~ \stemDown <a d>8 r8 \stemDown <a cis>4 ~ ->
    ~ \stemDown <a cis>8 r8 | % 306
    \stemDown <a c>4 ~ -> ~ \stemDown <a c>8 r8 \stemDown <a cis>4 ~ ->
    ~ \stemDown <a cis>8 r8 | % 307
    \stemDown <a d>4 ~ -> ~ \stemDown <a d>8 r8 \stemDown <a dis>4 ~ ->
    ~ \stemDown <a dis>8 r8 \pageBreak | % 308
    \stemDown <g e'>4 ~ -> ~ \stemDown <g e'>8 r8 \stemDown <gis e'>4 ~
    -> ~ \stemDown <gis e'>8 r8 | % 309
    \stemDown <a e'>4 ~ -> ~ \stemDown <a e'>8 r8 \stemDown <a e'>4 ~ ->
    ~ \stemDown <a e'>8 r8 | \barNumberCheck #310
    \stemUp e'4 ( -> \stemUp d8 ) r16 \stemUp a16 \stemUp e'4 ( ->
    \stemUp dis8 ) r16 \stemUp a16 | % 311
    \stemUp f'4 ( -> \stemUp e8 ) r16 \stemUp a,16 \stemUp g'4 ( ->
    \stemUp fis8 ) r16 \stemUp c16 | % 312
    \stemDown <b d>4 _\ffff \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g g'>8 \stemDown <g g'>8 \stemDown <g g'>8 }
    \stemDown <bes es>4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g g'>8 \stemDown <g g'>8 \stemDown <g g'>8 }
    | % 313
    \stemDown <a e'>4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g g'>8 \stemDown <g g'>8 \stemDown <g g'>8 }
    \stemDown <bes es>4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g g'>8 \stemDown <g g'>8 \stemDown <g g'>8 }
    \pageBreak | % 314
    \stemDown <b d>2 \stemDown <d d'>8 ( \stemDown <cis cis'>8 \stemDown
    <c c'>8 \stemDown <b b'>8 ) | % 315
    \stemDown <a a'>8 ( \stemDown <g g'>8 \stemDown <fis fis'>8
    \stemDown <e e'>8 \stemUp <d d'>8 ) r8 r4 | % 316
    R1*2 | % 318
    r2 \stemUp d4 ( _\mf _\< \stemUp dis4 ) | % 319
    \stemUp e4 ( \stemUp fis4 \stemUp g4 \stemUp a4 ) \pageBreak |
    \barNumberCheck #320
    \stemUp b4 ( _\! _\f _\< \stemUp c4 \stemUp d4 \stemUp dis4 ) | % 321
    \stemUp e4 ( \stemUp fis4 \stemUp g4 \stemUp a4 ) | % 322
    \stemUp b4 ( _\! _\ff _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemUp c4 \stemUp d4 \stemUp dis4 ) | % 323
    \stemUp e4 ( \stemUp d4 \stemUp e4 \stemUp d4 ) | % 324
    \stemUp dis8 \stopTrillSpan _\fff r8 \stemUp <b,, b'>4 ~ ~ \stemUp
    <b b'>8 r16 \stemUp <b b'>16 -. \stemUp <b b'>8 -. r16 \stemUp <b
        b'>16 -. \pageBreak | % 325
    \stemUp <b b'>8 -. r8 \stemUp e4 ( \stemUp <e e'>8 ) r16 \stemUp <e
        e'>16 -. \stemUp <e e'>8 -. r16 \stemUp <e e'>16 -. | % 326
    \stemUp <e e'>8 -. r8 \stemUp <e a>4 ~ ~ \stemUp <e a>8 r8 r4 | % 327
    r2 r4 \stemUp <e c'>4 ~ ~ \pageBreak | % 328
    \stemUp <e c'>8 r8 \stemUp <e cis'>4 ~ ~ \stemUp <e cis'>8 r8
    \stemDown <a d>4 ~ ~ | % 329
    \stemDown <a d>8 r8 \stemUp <d, fis>4 ~ ~ \stemUp <d fis>8 r8
    \stemUp <c d>8 r8 | \barNumberCheck #330
    \stemUp <b d>8 _\sempre _\fff r8 \stemUp a'8 r8 \stemUp <g b>8 r8
    \stemUp <g c>8 r8 | % 331
    \stemUp <g b>2 \stemUp <gis b>8 r8 \stemUp a8 r8 \pageBreak | % 332
    \stemUp <b, d>8 r8 \stemUp a'8 r8 \stemUp <g b>8 r8 \stemUp <g c>8 r8
    | % 333
    \stemUp <g b>2 \stemUp <gis b>8 r8 \stemUp a8 r8 | % 334
    \stemUp <d, b'>8 -. r8 \stemUp <d d'>16 ( \stemUp <dis dis'>16
    \stemUp <e e'>16 \stemUp <fis fis'>16 \stemDown <g g'>8 ) r8 \stemUp
    <d d'>16 ( \stemUp <dis dis'>16 \stemUp <e e'>16 \stemUp <fis fis'>16
    | % 335
    \stemDown <g g'>8 ) r8 \stemUp <d d'>16 ( \stemUp <dis dis'>16
    \stemUp <e e'>16 \stemUp <fis fis'>16 \stemDown <g g'>8 ) r8 \stemUp
    <d d'>16 ( \stemUp <dis dis'>16 \stemUp <e e'>16 \stemUp <fis fis'>16
    \pageBreak | % 336
    \stemDown <g g'>8 ) r8 \stemUp <d d'>16 ( \stemUp <dis dis'>16
    \stemUp <e e'>16 \stemUp <fis fis'>16 \stemDown <g g'>8 ) r8 \stemUp
    <d d'>16 ( \stemUp <dis dis'>16 \stemUp <e e'>16 \stemUp <fis fis'>16
    | % 337
    \stemDown <g g'>8 ) r8 \stemUp <d d'>16 ( \stemUp <dis dis'>16
    \stemUp <e e'>16 \stemUp <fis fis'>16 \stemDown <g g'>8 ) r8 \stemUp
    <d d'>16 ( \stemUp <dis dis'>16 \stemUp <e e'>16 \stemUp <fis fis'>16
    | % 338
    \stemDown <g g'>8 ) r8 r8 \stemDown <b g'>8 \stemDown <b g'>8 r8 r8
    \stemDown <b d>8 | % 339
    \stemDown <b d>8 r8 r8 \stemUp <g b>8 \stemUp <g b>8 r8 r8 \stemUp
    <b, d>8 | \barNumberCheck #340
    \stemUp <b d>8 r8 r4 \stemUp <fis' d'>8 r8 r4 \pageBreak | % 341
    \stemDown <g d'>8 r8 r4 \stemDown <fis' a>8 r8 r4 | % 342
    \stemDown <d b'>8 r8 \stemDown <d b'>8 r8 r4 \stemDown <d b'>8 r8 | % 343
    r4 \stemDown <d b'>8 r8 r4 \stemDown <d b'>8 r8 | % 344
    \stemDown <d g>8 r8 \stemDown <b d>8 r8 \stemUp <d, g>8 r8 \stemUp
    <b d>8 r8 | % 345
    R1*3 \bar "|."
    }

PartPFourVoiceTwo =  \relative gis' {
    \clef "treble" \time 4/4 \key g \major s1*4 \pageBreak s1*3 \bar
    "||"
    s1 | % 9
    R1 \pageBreak | \barNumberCheck #10
    R1 s1*4 \break s1*5 \pageBreak s1*4 \break s1*4 \pageBreak s1*4
    \pageBreak s1*4 \pageBreak s1*5 \pageBreak s1*5 \pageBreak | % 46
    \time 12/8  s2*15 \pageBreak s1*6 | % 55
    \numericTimeSignature\time 4/4  s1 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \bar "||"
    \pageBreak | % 71
    \key e \major s1*5 \break s1*5 \pageBreak s1*5 \pageBreak s4*11 r4 | % 89
    \stemDown gis8 \stemDown gis16 \stemDown gis16 \stemDown gis4 ~
    \stemDown gis8 \stemDown gis16 \stemDown gis16 \stemDown gis4 ~
    \pageBreak | \barNumberCheck #90
    \stemDown gis8 \stemDown gis16 \stemDown gis16 \stemDown gis4 ~
    \stemDown gis8 \stemDown gis16 \stemDown gis16 \stemDown bis4 | % 91
    \stemDown gis8 r8 \stemDown cis,4 \stemDown cis4 ~ \stemDown cis8 r8
    _\! s1*4 \pageBreak s4 \stemDown a'8 s8 \stemDown gis8 s8*43 \break
    s1*5 \pageBreak s1*2 | % 109
    r2 s2*7 \break s1*5 \pageBreak s1*5 \break s1*5 \pageBreak s1*4
    \pageBreak s1*4 \pageBreak s1 | % 137
    \time 12/8  s1*8/3 \bar "||"
    s1*1/3 | % 139
    \key g \major s1. \pageBreak s1. | % 141
    \numericTimeSignature\time 4/4  s1*4 \pageBreak s1*2 | % 147
    R1*2 s1 \pageBreak s1*5 \pageBreak s1*4 \break s1*4 \pageBreak s1*4
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*5 \pageBreak s1*4
    \pageBreak | % 184
    \time 12/8  s2*15 \pageBreak s1*6 | % 193
    \numericTimeSignature\time 4/4  s1 \pageBreak s4 \stemDown fis4 s2*9
    | % 199
    \stemDown gis8 r8 \stemDown d8 r16 \stemDown d16 \stemDown gis8 r8
    \stemDown d8 r8 | \barNumberCheck #200
    \stemDown a'8 -> \stemDown d8 -> s2. \pageBreak | % 201
    R1*2 s1*3 \pageBreak | % 206
    R1*2 s1*3 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*4 \pageBreak
    s1*3 \pageBreak s1*5 \pageBreak s1*5 \pageBreak | % 238
    \stemDown e4 s4*19 \pageBreak s1*5 \pageBreak s2*5 \stemDown b8 s8
    \stemDown b8 s8 | % 251
    \stemDown a8 s8*23 \pageBreak s4 \stemDown a'8 s16 \stemDown fis16
    \stemDown g8 s8*19 | % 257
    R1*2 \pageBreak s1*2 | % 261
    R1*2 s1 \pageBreak s1 | % 265
    R1*2 s1*2 \pageBreak | % 269
    r4 r8 s8 \stemDown b,4 ~ \stemDown b8 s8*33 \pageBreak s1*7
    \pageBreak s1. \stemDown d,8 s8*35 \pageBreak s1*5 \pageBreak | % 292
    \stemDown e'4 s4*19 \pageBreak s1*5 \pageBreak s1*6 \pageBreak s1*2
    | \barNumberCheck #310
    \stemDown e,4 ( -> \stemDown d8 ) s16 \stemDown a'16 \stemDown e4 (
    -> \stemDown dis8 ) s16 \stemDown a'16 | % 311
    \stemDown f4 ( -> \stemDown e8 ) s16 \stemDown a16 \stemDown g4 ( ->
    \stemDown fis8 ) s16 \stemDown c'16 s1*2 \pageBreak s2*9 \stemDown
    b,2 | % 319
    \stemDown c4 ( \stemDown d4 \stemDown e4 \stemDown fis4 ) \pageBreak
    | \barNumberCheck #320
    \stemDown g4 ( \stemDown a4 \stemDown b2 ) | % 321
    \stemDown c4 ( \stemDown d4 \stemDown e4 \stemDown fis4 ) | % 322
    \stemDown g4 ( \stemDown a4 \stemDown b4 \stemDown b4 ) | % 323
    \stemDown c4 \stemDown d4 \stemDown e4 \stemDown d4 | % 324
    \stemDown dis8 s8*7 \pageBreak s4 \stemDown e,,4 ~ s2*5 \pageBreak
    s4*9 \stemDown a8 s8*11 \stemDown a8 s8 \pageBreak s4 \stemDown a8
    s8*11 \stemDown a8 s8*17 \pageBreak s1*5 \pageBreak s1*7 \bar "|."
    }

PartPFiveVoiceOne =  \relative g'' {
    \clef "treble" \time 4/4 \key bes \major \transposition a | % 1
    R1*2 _ "Clarinets" | % 3
    \time 12/8  \stemDown g8 -. _ "in A" _\p \stemDown f8 -. \stemDown g8
    -. \stemDown f8 -. \stemDown g8 -. \stemDown f8 -. \stemDown g8 -.
    \stemDown f8 -. \stemDown g8 -. \stemDown f8 -. \stemDown g8 -.
    \stemDown f8 -. | % 4
    r2.*2/3 \stemDown g8 ( -> _\p \stemDown f8 \stemDown es8 \stemDown d8
    \stemDown c8 \stemDown bes8 ) s4 \pageBreak | % 5
    r1 _ "Cl." s2 | % 6
    r1 s2 | % 7
    \stemDown es8 -. _\p \stemDown d8 -. \stemDown es8 -. \stemDown d8
    -. \stemDown es8 -. \stemDown d8 -. \stemDown es8 -. \stemDown d8 -.
    \stemDown es8 -. \stemDown d8 -. \stemDown es8 -. \stemDown d8 -.
    \bar "||"
    r2.*2/3 \stemDown es8 ( -> _\p \stemDown d8 \stemDown c8 \stemUp bes8
    \stemUp a8 \stemUp g8 ) s4 | % 9
    r1 s2 \pageBreak | \barNumberCheck #10
    r1 s2 | % 11
    r1 s2 | % 12
    r1 s2 | % 13
    r1 s2 | % 14
    r1 s2 \break | % 15
    r1 s2 | % 16
    r1 s2 | % 17
    r1 s2 | % 18
    r1 s2 | % 19
    r1 s2 \pageBreak | \barNumberCheck #20
    r1 s2 | % 21
    r1 s2 | % 22
    r1 s2 | % 23
    r1 s2 \break | % 24
    r1 s2 | % 25
    r1 s2 | % 26
    r1 s2 | % 27
    r1 s2 \pageBreak | % 28
    r1 _ "Cl." s2 | % 29
    f'1. _\mp _\< | \barNumberCheck #30
    \stemDown fis4. ( -> _\! _\mf \stemDown g8 ) r8*2/3 r8*2/3 r2.*2/3
    s1*1/3 | % 31
    r4.*2/3 \stemDown fis8 -. _\f \stemDown gis8 -. \stemDown ais8 -.
    \stemDown b8 -. r8*2/3 r8*2/3 r4.*2/3 s1*1/3 \pageBreak | % 32
    r4.*2/3 _ "Cl." \stemDown fis8 -. _\f \stemDown gis8 -. \stemDown
    ais8 -. \stemDown b8 -. r8*2/3 r8*2/3 r4.*2/3 s1*1/3 | % 33
    r4.*2/3 \stemUp fis,8 -. _\mf \stemUp gis8 -. \stemUp ais8 -.
    \stemDown b8 -. r8*2/3 r8*2/3 r4.*2/3 s1*1/3 | % 34
    r4.*2/3 \stemUp fis8 -. _\mp \stemUp gis8 -. \stemUp ais8 -.
    \stemDown b8 -. r8*2/3 r8*2/3 r4.*2/3 s1*1/3 | % 35
    r4.*2/3 \stemDown a8 -. _\p \stemDown bes8 -. \stemDown c8 -. r4.*2/3
    \stemDown a8 -. \stemDown bes8 -. \stemDown c8 -. s4 \pageBreak | % 36
    r4.*2/3 _ "Cl." \stemDown a8 -. \stemDown bes8 -. \stemDown c8 -. r4.*2/3
    \stemDown a8 -. \stemDown bes8 -. \stemDown c8 -. s4 | % 37
    r1 s2 | % 38
    r1 s2 | % 39
    \stemDown g'8 -. _\p \stemDown f8 -. \stemDown g8 -. \stemDown f8 -.
    \stemDown g8 -. \stemDown f8 -. \stemDown g8 -. \stemDown f8 -.
    \stemDown g8 -. \stemDown f8 -. \stemDown g8 -. \stemDown f8 -. |
    \barNumberCheck #40
    \stemDown g8 ( -> \stemDown f8 \stemDown es8 \stemDown d8 \stemDown
    c8 \stemDown bes8 ) r2.*2/3 s4 \pageBreak | % 41
    r1 _ "Cl." s2 | % 42
    r1 s2 | % 43
    \stemDown g'8 -. _\mp \stemDown f8 -. \stemDown g8 -. \stemDown f8
    -. \stemDown g8 -. \stemDown f8 -. \stemDown g8 -. \stemDown f8 -.
    \stemDown g8 -. \stemDown f8 -. \stemDown g8 -. \stemDown f8 -. | % 44
    \stemDown g8 ( -> \stemDown f8 \stemDown es8 \stemDown d8 \stemDown
    c8 \stemDown bes8 ) r2.*2/3 s4 | % 45
    r1 s2 \pageBreak | % 46
    \stemDown ges'4. _\f _ "Cl." -\markup{ \italic {marcato} } \stemDown
    f4. \stemDown es4. \stemDown des4 ( ~ \stemDown des16 \stemDown ces16
    | % 47
    \stemDown bes8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 48
    \stemUp des,8 ( \stemUp es8 \stemUp f8 \stemUp ges8 \stemUp f8
    \stemUp es8 \stemUp des8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 | % 49
    r1 s2 | \barNumberCheck #50
    r2.*2/3 r4.*2/3 \stemDown cis''8 _\ff \stemDown cis8 \stemDown cis8
    s4. \pageBreak | % 51
    \stemDown a8 ( _ "Cl." \stemDown b8 \stemDown cis8 \stemDown d8
    \stemDown cis8 \stemDown b8 \stemDown a8 ) r8*2/3 r8*2/3 r4.*2/3
    s1*5/24 | % 52
    \stemUp a,,8 ( _\ff \stemUp b8 \stemUp cis8 \stemUp d8 \stemUp cis8
    \stemUp b8 \stemUp a8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 | % 53
    r1 s2 | % 54
    r1 s2 | % 55
    r1 r2*2/3 s1*1/6 \pageBreak | % 56
    \numericTimeSignature\time 4/4  \stemDown fis'''4 -> _\mf _ "Cl."
    \stemDown fis8 r16 \stemDown fis16 \stemDown a,8 r8 r4 | % 57
    R1*3 | \barNumberCheck #60
    \stemDown fis'4 -> _\mf \stemDown fis8 r16 \stemDown fis16 \stemDown
    a,8 r8 r4 \pageBreak | % 61
    d1 -> _\p _ "Cl." _\markup{ \small\italic {poco a poco cresc.} }
    \startTrillSpan | % 62
    bes1 -> | % 63
    d1 -> | % 64
    bes1 -> | % 65
    d1 -> \pageBreak | % 66
    es1 -> _ "Cl." | % 67
    fis,1 -> \stopTrillSpan _\f _\markup{ \small\italic {cresc.} }
    \startTrillSpan | % 68
    bes1 -> | % 69
    \stemDown d8 -> \stopTrillSpan _\ff r8 \stemUp d,,8 -! _\markup{
        \small\italic {dim.} } \startTrillSpan \stemUp e,8 -! \stemUp f8
    -! \stemUp fis8 -! \stemUp g8 -! \stemUp a8 -! | \barNumberCheck #70
    \stemUp bes8 -! \stemUp b8 -! \stemUp c8 -! \stemUp cis8 -! \stemUp
    d8 -! \stemUp e8 -! \stemUp f8 -! \stemUp fis8 -! \bar "||"
    \pageBreak | % 71
    \key g \major \stemUp g8 \stopTrillSpan _\p _ "Cl." -\markup{
        \italic {leggieramente} } r8 \stemUp d8 r16 \stemUp d16 \stemUp
    g8 r8 \stemUp d8 r8 | % 72
    \stemUp g8 -. \stemUp c8 ~ ^> \stemDown c2 \stemUp b8 -. r16 \stemUp
    a16 ( | % 73
    \stemDown d8 ) r8 \acciaccatura { \stemUp a8 ( } \stemUp g8 ) -. r16
    \stemUp fis16 -. \stemUp g8 -. r8 \stemUp d8 r8 | % 74
    \stemUp g2. -> \stemDown b8 -. _\< r16 \stemDown d16 ( | % 75
    \stemDown e8 ) _\! r8 \acciaccatura { \stemUp a,8 ( } \stemUp g8 )
    -. _\p r16 \stemUp fis16 -. \stemUp g8 -. r8 \stemUp d8 r8 \break | % 76
    \stemUp g2 ~ -> _ "Cl." \stemUp g8 r8 \stemDown b8 -. _\< r16
    \stemDown d16 -. | % 77
    \stemDown g4 ( -> _\! _\sempre _\p \stemDown fis8 ) r16 \stemDown g16
    \stemDown e4 ( -> \stemDown dis8 ) r16 \stemDown e16 | % 78
    \stemDown c4 ( -> \stemDown b8 ) r16 \stemDown c16 \stemUp a4 ( ->
    \stemUp g8 ) r16 \stemUp a16 ( | % 79
    \stemUp e8 ) _\< r16 \stemUp fis16 ( \stemUp g8 ) r16 \stemUp b16 (
    \stemDown e8 ) r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown a16
    -. | \barNumberCheck #80
    \stemDown b2 ~ _\! _\mf _\< \stemDown b8 \stemDown a16 ( _\! _\ff
    _\> \stemDown g16 \once \omit TupletBracket
    \times 4/6  {
        \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown c16
        \stemDown b16 \stemDown a16 }
    \pageBreak | % 81
    \stemUp g8 ) _\! _\p _ "Cl." r8 r4 r2 | % 82
    \stemUp g8 _\pp r8 \stemUp g8 r16 \stemUp g16 \stemUp fis8 r8
    \stemUp fis8 r16 \stemUp fis16 | % 83
    \stemUp g8 _\markup{ \small\italic {un poco cresc.} }
    \startTrillSpan r8 \stemUp d8 r16 \stemUp d16 \stemUp d8 r8 \stemUp
    d8 r8 | % 84
    \stemUp c8 r8 \stemUp c8 r16 \stemUp c16 \stemUp b4 ( \stemUp d8 ) r8
    | % 85
    \stemUp g8 r8 \stemUp d8 r16 \stemUp d16 \stemUp d8 r8 \stemUp d8 r8
    \pageBreak | % 86
    \stemUp c8 _ "Cl." r8 \stemUp c8 r16 \stemUp c16 \stemUp c8 r8 \once
    \omit TupletBracket
    \times 2/3  {
        \stemUp d8 ( \stopTrillSpan _\mf \stemUp c8 \stemUp b8 }
    | % 87
    \stemUp bes8 ) _\< r8 r4 \stemUp f'8 r8 r4 | % 88
    \stemDown bes8 r8 r4 \stemDown bes8 ( \stemDown b8 ) \stemUp g8 ( -.
    _\! _\f r16 \stemUp a16 ) -. | % 89
    \stemDown b2. -> \stemUp a8 ( -. r16 \stemUp b,16 ) -. \pageBreak |
    \barNumberCheck #90
    \stemUp g'2. -> _ "Cl." \stemUp fis8 ( -. r16 \stemUp b,16 ) -. | % 91
    \stemUp e4 _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown b'4 \stemUp a4 \stemUp e4 | % 92
    \stemUp e4 \stemUp bes4 \stemUp b4 \stemUp b4 | % 93
    \stemUp a8 \stopTrillSpan _\ff r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp a'8 \stemUp a8 \stemUp a8 }
    \stemUp a2 ~ | % 94
    \stemUp a8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 \stemDown b8 \stemDown b8 }
    \stemDown b2 ~ | % 95
    \stemDown b8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown b'8 \stemDown b8 \stemDown b8 }
    \stemDown b2 ~ \pageBreak | % 96
    \stemDown b8 _ "Cl." r8 \stemDown c8 r8 \stemUp d,,8 r8 r4 | % 97
    R1 | % 98
    r2 r4 \stemDown d''16 ( _\mf \stemDown e16 \stemDown d16 \stemDown e16
    | % 99
    \stemDown b8 ) r8 \stemDown fis16 ( \stemDown g16 \stemDown fis16
    \stemDown g16 \stemDown e8 ) r8 \stemUp ais,16 ( \stemUp b16 \stemUp
    ais16 \stemUp b16 ) | \barNumberCheck #100
    \stemDown c16 ( \stemDown d16 \stemDown c16 \stemDown b16 ) \stemUp
    a16 ( \stemUp b16 \stemUp a16 \stemUp g16 ) \stemUp fis16 ( \stemUp
    g16 \stemUp e16 \stemUp fis16 \stemUp d8 ) r8 | % 101
    R1 \break | % 102
    r2 _ "Cl." r4 \stemDown b''16 ( _\mf \stemDown c16 \stemDown b16
    \stemDown c16 | % 103
    \stemDown g8 ) r8 \stemDown dis16 ( \stemDown e16 \stemDown dis16
    \stemDown e16 \stemDown c8 ) r8 \stemDown g'16 ( \stemDown gis16
    \stemDown g16 \stemDown gis16 ) | % 104
    \stemDown a16 ( \stemDown b16 \stemDown a16 \stemDown g16 )
    \stemDown fis16 ( \stemDown g16 \stemDown fis16 \stemDown e16 )
    \stemDown d16 ( \stemDown e16 \stemDown c16 \stemDown d16 \stemDown
    b8 ) r8 | % 105
    R1 | % 106
    r2 r4 \stemDown d'16 ( _\mf \stemDown e16 \stemDown d16 \stemDown e16
    \pageBreak | % 107
    \stemDown b8 ) _ "Cl." r8 \stemDown fis16 ( \stemDown g16 \stemDown
    fis16 \stemDown g16 \stemDown e8 ) r8 \stemUp ais,16 ( \stemUp b16
    \stemUp ais16 \stemUp b16 ) | % 108
    \stemDown c16 ( \stemDown d16 \stemDown c16 \stemDown b16 ) \stemUp
    a16 ( \stemUp b16 \stemUp a16 \stemUp g16 ) \stemUp fis16 ( \stemUp
    g16 \stemUp e16 \stemUp fis16 \stemUp d8 ) r8 | % 109
    \stemUp fis2 _\ff \stemUp fis2 | \barNumberCheck #110
    \stemUp fis2 \stemUp g2 | % 111
    \stemUp a8 r8 \stemDown b8 r8 \stemDown b8 r8 \stemDown b8 r8 | % 112
    \stemDown c8 r8 \stemDown c8 r8 r2 \break | % 113
    \stemUp g8 _\p _ "Cl." r8 \stemUp d8 r16 \stemUp d16 \stemUp g8 r8
    \stemUp d8 r8 | % 114
    \stemUp g8 -. \stemUp c8 ~ ^> \stemDown c2 \stemUp b8 -. r16 \stemUp
    a16 ( | % 115
    \stemDown d8 ) r8 \acciaccatura { \stemUp a8 ( } \stemUp g8 ) -. r16
    \stemUp fis16 -. \stemUp g8 -. r8 \stemUp d8 r8 | % 116
    \stemUp g2. -> \stemDown b8 -. _\< r16 \stemDown d16 ( | % 117
    \stemDown e8 ) _\! r8 \acciaccatura { \stemUp a,8 ( } \stemUp g8 )
    -. _\p r16 \stemUp fis16 -. \stemUp g8 -. r8 \stemUp d8 r8
    \pageBreak | % 118
    \stemUp g2 ~ -> _ "Cl." \stemUp g8 r8 \stemDown b8 -. _\< r16
    \stemDown d16 -. | % 119
    \stemDown g4 ( -> _\! _\sempre _\p \stemDown fis8 ) r16 \stemDown g16
    \stemDown e4 ( -> \stemDown dis8 ) r16 \stemDown e16 |
    \barNumberCheck #120
    \stemDown c4 ( -> \stemDown b8 ) r16 \stemDown c16 \stemUp a4 ( ->
    \stemUp g8 ) r16 \stemUp a16 ( | % 121
    \stemUp e8 ) _\< r16 \stemUp fis16 ( \stemUp g8 ) r16 \stemUp b16 (
    \stemDown e8 ) r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown a16
    -. | % 122
    \stemDown b2 ~ _\! _\mf _\< \stemDown b8 \stemDown a16 ( _\! _\ff
    _\> \stemDown g16 \once \omit TupletBracket
    \times 4/6  {
        \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown c16
        \stemDown b16 \stemDown a16 }
    \break | % 123
    \stemUp g8 ) _\! _\p _ "Cl." r8 r4 r2 | % 124
    \stemUp g8 _\pp r8 \stemUp g8 r16 \stemUp g16 \stemUp fis8 r8
    \stemUp fis8 r16 \stemUp fis16 | % 125
    \stemUp g8 _\markup{ \small\italic {un poco cresc.} }
    \startTrillSpan r8 \stemUp d8 r16 \stemUp d16 \stemUp d8 r8 \stemUp
    d8 r8 | % 126
    \stemUp c8 r8 \stemUp c8 r16 \stemUp c16 \stemUp b4 ( \stemUp d8 ) r8
    | % 127
    \stemUp g8 r8 \stemUp d8 r16 \stemUp d16 \stemUp d8 r8 \stemUp d8 r8
    \pageBreak | % 128
    \stemUp c8 _ "Cl." r8 \stemUp c8 r16 \stemUp c16 \stemUp c8 r8 \once
    \omit TupletBracket
    \times 2/3  {
        \stemUp d8 ( \stopTrillSpan _\f \stemUp c8 \stemUp b8 }
    | % 129
    \stemUp bes8 ) r8 \stemUp d8 r16 \stemUp c16 -. \stemUp bes8 -. r8
    \stemUp f'8 ( -. r16 \stemUp fis16 ) -. | \barNumberCheck #130
    \stemUp g4 ( -> \stemUp f8 ) -. r16 \stemUp es16 ( \stemUp d16
    \stemUp es16 \stemUp d16 \stemUp c16 ) \stemUp bes16 ( \stemUp as16
    \stemUp g16 \stemUp f16 | % 131
    \stemUp es'8 ) \stemUp f8 ( \stemUp g8 \stemUp a8 ) \stemDown bes8 (
    \stemDown c8 \stemDown cis8 \stemDown d8 ) \pageBreak | % 132
    \stemDown es8 ( _ "Cl." \stemDown f8 \stemDown g8 \stemDown a8
    \stemDown bes16 ) \stemDown es16 ( \stemDown d16 \stemDown c16
    \stemDown bes16 \stemDown as16 \stemDown g16 \stemDown f16 | % 133
    \stemDown es8 ) r8 \stemUp d,8 ( -. r16 \stemUp c16 ) -. \stemUp bes8
    -. r8 \stemUp f'8 ( -. r16 \stemUp fis16 ) -. | % 134
    \stemUp g4 ( -> \stemUp f8 ) -. r16 \stemUp es16 ( \stemUp d16
    \stemUp es16 \stemUp d16 \stemUp c16 ) \stemUp bes16 \stemUp as16
    \stemUp g16 \stemUp f16 | % 135
    \stemUp es'8 \stemUp f8 ( \stemUp g8 \stemUp a8 ) \stemDown bes8 (
    \stemDown c8 \stemDown cis8 \stemDown d8 ) \pageBreak | % 136
    \stemDown es8 ( _ "Cl." \stemDown f8 \stemDown g8 \stemDown a8
    \stemDown bes16 ) \stemDown es16 ( \stemDown d16 \stemDown c16
    \stemDown bes16 \stemDown as16 \stemDown g16 \stemDown f16 | % 137
    \time 12/8  \stemDown es8 ) r8*2/3 r8*2/3 r8*2/3 \stemDown d8 -. _\f
    \stemDown f8 -. \stemDown g8 ( \stemDown f8 ) \stemDown es8 -.
    \stemDown d8 -. r8*2/3 r8*2/3 s1*5/24 | % 138
    r4.*2/3 r8*2/3 \stemDown d8 -. _\mf \stemDown f8 -. \stemDown g8 (
    \stemDown f8 ) \stemDown es8 -. \stemDown d8 -. r4*2/3 \bar "||"
    s4 | % 139
    \key bes \major r1 s2 \pageBreak | \barNumberCheck #140
    r1 _ "Cl." s2 | % 141
    \stemDown g8 -. _\p \stemDown f8 -. \stemDown g8 -. \stemDown f8 -.
    \stemDown g8 -. \stemDown f8 -. \stemDown g8 -. \stemDown f8 -.
    \stemDown g8 -. \stemDown f8 -. \stemDown g8 -. \stemDown f8 -. | % 142
    r2.*2/3 \stemDown g8 ( -> _\p \stemDown f8 \stemDown es8 \stemDown d8
    \stemDown c8 \stemDown bes8 ) s4 | % 143
    r1 s2 | % 144
    r1 s2 \pageBreak | % 145
    \stemDown es8 -. _\p _ "Cl." \stemDown d8 -. \stemDown es8 -.
    \stemDown d8 -. \stemDown es8 -. \stemDown d8 -. \stemDown es8 -.
    \stemDown d8 -. \stemDown es8 -. \stemDown d8 -. \stemDown es8 -.
    \stemDown d8 -. | % 146
    r2.*2/3 \stemDown es8 ( -> _\p \stemDown d8 \stemDown c8 \stemUp bes8
    \stemUp a8 \stemUp g8 ) s4 | % 147
    r1 s2 | % 148
    r1 s2 | % 149
    r1 s2 \pageBreak | \barNumberCheck #150
    r1 s2 | % 151
    r1 s2 | % 152
    r1 s2 | % 153
    r1 s2 | % 154
    r1 s2 \pageBreak | % 155
    r1 s2 | % 156
    r1 s2 | % 157
    r1 s2 | % 158
    r1 s2 \break | % 159
    r1 s2 | \barNumberCheck #160
    r1 s2 | % 161
    r1 s2 | % 162
    r1 s2 \pageBreak | % 163
    r1 s2 | % 164
    r1 s2 | % 165
    r1 s2 | % 166
    r1 s2 \pageBreak | % 167
    f'1. _\mp _ "Cl." _\< | % 168
    \stemDown fis4. ( _\! _\mf \stemDown g8 ) r8*2/3 r8*2/3 r2.*2/3
    s1*1/3 | % 169
    r4.*2/3 \stemDown fis8 -. _\f \stemDown gis8 -. \stemDown ais8 -.
    \stemDown b8 -. r8*2/3 r8*2/3 r4.*2/3 s1*1/3 | \barNumberCheck #170
    r4.*2/3 \stemDown fis8 -. _\f \stemDown gis8 -. \stemDown ais8 -.
    \stemDown b8 -. r8*2/3 r8*2/3 r4.*2/3 s1*1/3 \pageBreak | % 171
    r4.*2/3 _ "Cl." \stemUp fis,8 -. _\mf \stemUp gis8 -. \stemUp ais8
    -. \stemDown b8 -. r8*2/3 r8*2/3 r4.*2/3 s1*1/3 | % 172
    r4.*2/3 \stemUp fis8 -. _\mp \stemUp gis8 -. \stemUp ais8 -.
    \stemDown b8 -. r8*2/3 r8*2/3 r4.*2/3 s1*1/3 | % 173
    r4.*2/3 \stemDown a8 -. _\p \stemDown bes8 -. \stemDown c8 -. r4.*2/3
    \stemDown a8 -. \stemDown bes8 -. \stemDown c8 -. s4 | % 174
    r4.*2/3 \stemDown a8 -. \stemDown bes8 -. \stemDown c8 -. r4.*2/3
    \stemDown a8 -. \stemDown bes8 -. \stemDown c8 -. s4 \pageBreak | % 175
    r1 _ "Cl." s2 | % 176
    r1 s2 | % 177
    \stemDown g'8 -. _\p \stemDown f8 -. \stemDown g8 -. \stemDown f8 -.
    \stemDown g8 -. \stemDown f8 -. \stemDown g8 -. \stemDown f8 -.
    \stemDown g8 -. \stemDown f8 -. \stemDown g8 -. \stemDown f8 -. | % 178
    \stemDown g8 ( -> \stemDown f8 \stemDown es8 \stemDown d8 \stemDown
    c8 \stemDown bes8 ) r2.*2/3 s4 | % 179
    r1 s2 \pageBreak | \barNumberCheck #180
    r1 _ "Cl." s2 | % 181
    \stemDown g'8 -. _\mp \stemDown f8 -. \stemDown g8 -. \stemDown f8
    -. \stemDown g8 -. \stemDown f8 -. \stemDown g8 -. \stemDown f8 -.
    \stemDown g8 -. \stemDown f8 -. \stemDown g8 -. \stemDown f8 -. | % 182
    \stemDown g8 ( -> \stemDown f8 \stemDown es8 \stemDown d8 \stemDown
    c8 \stemDown bes8 ) r2.*2/3 s4 | % 183
    r1 s2 \pageBreak | % 184
    \stemDown ges'4. _\f _\ marcato _ "Cl." \stemDown f4. \stemDown es4.
    \stemDown des4 ( ~ \stemDown des16 \stemDown ces16 | % 185
    \stemDown bes8 ) r8*2/3 r8*2/3 r4.*2/3 \stemDown bes8 ( _\f
    \stemDown ces8 \stemDown des8 \stemDown es8 \stemDown des8 \stemDown
    ces8 s1*5/24 | % 186
    \stemDown bes8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 187
    r1 s2 | % 188
    \stemDown bes'4. \stemDown as4. \stemDown ges4. \stemDown f4 ( ~
    \stemDown f16 \stemDown es16 \pageBreak | % 189
    \stemDown des8 ) _ "Cl." r8*2/3 r8*2/3 r4.*2/3 \stemDown des8 ( _\ff
    \stemDown es8 \stemDown f8 \stemDown ges8 \stemDown f8 \stemDown es8
    s1*5/24 | \barNumberCheck #190
    \stemDown des8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 191
    \numericTimeSignature\time 4/4  r2 \stemUp bes,8 ( _\ff \stemUp a8
    \stemUp g8 \stemUp f8 ) | % 192
    r2 \stemUp bes8 ( _\ff \stemUp as8 \stemUp g8 \stemUp f8 ) | % 193
    \stemDown f'''4 _\ff \stemDown c8 \stemDown a8 \stemDown f4
    \stemDown c4 \pageBreak | % 194
    \stemDown d16 ( _ "Cl." \stemDown c16 \stemDown bes16 \stemDown a16
    ) \stemUp g16 ( \stemUp f16 \stemUp e16 \stemUp d16 \stemUp c8 ) r8
    r4 | % 195
    R1*6 \pageBreak | % 201
    R1 _ "Cl." | % 202
    \stemDown d'8 _\p -\markup{ \italic {leggieramente} } r8 \stemUp a8
    r16 \stemUp a16 \stemDown d8 r8 \stemUp a8 r8 | % 203
    \stemDown d8 -> \stemDown g8 -> r4 r2 | % 204
    \stemDown f'8 _\p _\< r8 \stemDown c8 r16 \stemDown c16 \stemDown f8
    r8 \stemDown c8 r8 | % 205
    \stemDown f8 -> _\! _\mp \stemDown c8 -> r4 r2 \pageBreak | % 206
    R1 _ "Cl." | % 207
    \stemDown e,8 _\mf r8 \stemDown bes8 r16 \stemDown bes16 \stemDown e8
    r8 \stemDown bes8 r8 | % 208
    \stemDown f'8 -> \stemDown bes8 -> r4 r2 | % 209
    \stemDown f8 _\f r8 \stemDown c8 r16 \stemDown c16 \stemDown f8 r8
    \stemDown c8 r8 | \barNumberCheck #210
    \stemDown f8 -> \stemDown bes8 -> r4 r2 \pageBreak | % 211
    \stemDown e8 _\f _ "Cl." _\< r8 \stemDown bes8 r16 \stemDown bes16
    \stemDown e8 r8 \stemDown bes8 r8 | % 212
    \stemDown bes8 -> _\! _\ff r8 \stemDown f8 r16 \stemDown f16
    \stemDown bes8 r8 \stemDown f8 r8 | % 213
    \stemDown c'8 -> \stemDown f8 -> r4 r2 | % 214
    \stemDown g,8 _\fff r8 \stemDown g8 r16 \stemDown g16 \stemDown g8 r8
    \stemDown g8 r8 | % 215
    \stemDown a8 -> \stemDown c8 ~ -> \stemDown c2. \pageBreak | % 216
    \stemDown g8 _\fff _ "Cl." r8 \stemDown g8 r16 \stemDown g16
    \stemDown g8 r8 \stemDown g8 r8 | % 217
    \stemDown a8 -> \stemDown c8 ~ -> \stemDown c8 \stemDown c8
    \stemDown g8 \stemDown g4 \stemDown g8 | % 218
    \stemDown g8 \stemDown c4 \stemDown c8 \stemDown g8 \stemDown g4
    \stemDown g8 | % 219
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown es8 \stemDown es8 r8 }
    | \barNumberCheck #220
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown es8 \stemDown es8 r8 }
    \pageBreak | % 221
    \times 2/3  {
        \stemDown a8 -> _ "Cl." \stemDown a8 -> r8 }
    r4 r2 | % 222
    r4 \stemDown f,32 ( _\sempre _\fff \stemDown g32 \stemDown a32
    \stemDown bes32 \stemDown c32 \stemDown d32 \stemDown es32 \stemDown
    f32 ) \stemDown g16 ( \stemDown f16 \stemDown es16 \stemDown d16 )
    \stemUp c16 ( \stemUp bes16 \stemUp a16 \stemUp g16 ) | % 223
    \stemUp f16 ( \stemUp es16 \stemUp d16 \stemUp c16 ) \stemUp bes16 (
    \stemUp a16 \stemUp g16 \stemUp f16 ) r2 | % 224
    r4 \stemDown f'32 ( \stemDown g32 \stemDown a32 \stemDown bes32
    \stemDown c32 \stemDown d32 \stemDown es32 \stemDown f32 ) \stemDown
    g16 ( \stemDown f16 \stemDown es16 \stemDown d16 ) \stemUp c16 (
    \stemUp bes16 \stemUp a16 \stemUp g16 ) \pageBreak | % 225
    \stemUp f16 ( _ "Cl." \stemUp es16 \stemUp d16 \stemUp c16 ) \stemUp
    bes16 ( \stemUp a16 \stemUp g16 \stemUp f16 ) r4 \stemDown f'32 (
    \stemDown g32 \stemDown a32 \stemDown bes32 \stemDown c32 \stemDown
    d32 \stemDown es32 \stemDown f32 ) | % 226
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown g16 ( \stemDown f16 \stemDown es16 \stemDown d16
        \stemDown c16 \stemDown bes16 }
    \stemUp a8 ) r8 r4 \stemDown f32 ( \stemDown g32 \stemDown a32
    \stemDown bes32 \stemDown c32 \stemDown d32 \stemDown es32 \stemDown
    f32 ) | % 227
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown g16 ( \stemDown f16 \stemDown es16 \stemDown d16
        \stemDown c16 \stemDown bes16 }
    \stemUp a8 ) r8 r4 \stemDown f32 ( \stemDown g32 \stemDown a32
    \stemDown bes32 \stemDown c32 \stemDown d32 \stemDown es32 \stemDown
    f32 ) \pageBreak | % 228
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown g16 ( _ "Cl." \stemDown f16 \stemDown es16 \stemDown d16
        \stemDown c16 \stemDown bes16 }
    \stemUp a8 ) r8 \once \omit TupletBracket
    \times 4/6  {
        \stemUp g16 ( \stemUp f16 \stemUp es16 \stemUp d16 \stemUp c16
        \stemUp bes16 }
    \stemUp a8 ) r8 | % 229
    \stemDown bes'8 _\fff r8 \stemDown c8 r8 \stemDown d8 r8 \stemDown f8
    r8 | \barNumberCheck #230
    \stemDown bes8 -> \stemDown es,8 ~ ^> \stemDown es2 \stemDown d8 r16
    \stemDown c16 | % 231
    \stemDown f8 r8 \acciaccatura { \stemUp c8 ( } \stemUp bes8 ) r16
    \stemUp a16 \stemDown bes8 r8 \stemDown f'8 r8 | % 232
    \stemDown bes2. -> \stemDown d,8 r16 \stemDown f16 \pageBreak | % 233
    \stemDown g8 _ "Cl." r8 \acciaccatura { \stemUp c,8 ( } \stemUp bes8
    ) r16 \stemUp a16 \stemDown bes8 r8 \stemUp f8 r8 | % 234
    \stemDown bes2. -> \stemDown d8 r16 \stemDown f16 | % 235
    \stemDown bes4 ( -> \stemDown a8 ) r16 \stemDown bes16 \stemDown g4
    ( -> \stemDown fis8 ) r16 \stemDown g16 | % 236
    \stemDown es4 ( -> \stemDown d8 ) r16 \stemDown es16 \stemDown c4 (
    -> \stemDown bes8 ) r16 \stemDown c16 -. | % 237
    \stemUp g8 -. r16 \stemUp a16 ( \stemDown bes8 ) r16 \stemDown d16 (
    \stemDown g8 ) r16 \stemDown a16 ( \stemDown bes8 ) r16 \stemDown c16
    -. \pageBreak | % 238
    \stemDown d2 ~ -> _ "Cl." \stemDown d8 \stemDown c16 ( \stemDown bes16
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown a16 \stemDown g16 \stemDown f16 \stemDown es16
        \stemDown d16 \stemDown c16 }
    | % 239
    \stemDown bes8 ) r8 \stemDown c8 r8 \stemDown d8 r8 \stemDown f8 r8
    | \barNumberCheck #240
    \stemDown bes8 -> \stemDown es,8 ~ ^> \stemDown es2 \stemDown d8 r16
    \stemDown c16 | % 241
    \stemDown f8 r8 \acciaccatura { \stemUp c8 ( } \stemUp bes8 ) r16
    \stemUp a16 \stemDown bes8 r8 \stemDown f'8 r8 | % 242
    \stemDown bes2. -> \stemDown d,8 r16 \stemDown f16 \pageBreak | % 243
    \stemDown g8 _ "Cl." r8 \acciaccatura { \stemUp c,8 ( } \stemUp bes8
    ) r16 \stemUp a16 \stemDown bes8 r8 \stemUp f8 r8 | % 244
    \stemDown bes2. -> \stemDown d8 r16 \stemDown f16 | % 245
    \stemDown ges4 ( -> \stemDown f8 ) r16 \stemDown es16 \stemDown des8
    r8 \stemDown as'8 r16 \stemDown a16 | % 246
    \stemDown bes4 ( -> \stemDown as8 ) r16 \stemDown ges16 \stemDown f8
    r8 \stemDown bes8 r16 \stemDown c16 | % 247
    \stemDown d2. -> \stemDown c8 r16 \stemDown d,16 \pageBreak | % 248
    \stemDown bes'2. -> _ "Cl." \stemDown a8 r16 \stemDown d,16 | % 249
    \stemDown g4 ( -> \stemDown f8 ) r16 \stemDown g,16 \stemDown es'4 (
    -> \stemDown d8 ) r16 \stemDown g,16 | \barNumberCheck #250
    \stemDown c4 ( -> \stemDown bes8 ) r16 \stemDown bes16 \stemDown g'4
    ( -> \stemDown f8 ) r16 \stemDown b,16 | % 251
    \stemDown es8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown es8 \stemDown es8 \stemDown es8 }
    \stemDown es2 ~ | % 252
    \stemDown es8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 }
    \stemDown a2 ~ | % 253
    \stemDown a8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown d,8 \stemDown d8 \stemDown d8 }
    \stemDown d2 ~ \pageBreak | % 254
    \stemDown d8 _ "Cl." r8 \stemDown es8 r16 \stemDown a,16 \stemDown
    bes8 r8 r4 | % 255
    R1 | % 256
    r2 r4 \stemDown f''16 ( _\ff \stemDown g16 \stemDown f16 \stemDown g16
    | % 257
    \stemDown d8 ) r8 \stemDown a16 ( \stemDown bes16 \stemDown a16
    \stemDown bes16 \stemDown g8 ) r8 \stemDown cis,16 ( \stemDown d16
    \stemDown cis16 \stemDown d16 ) | % 258
    \stemDown es16 ( \stemDown f16 \stemDown es16 \stemDown d16 )
    \stemDown c16 ( \stemDown d16 \stemDown c16 \stemDown bes16 )
    \stemUp a16 ( \stemUp bes16 \stemUp g16 \stemUp a16 \stemUp f8 ) r8
    \pageBreak | % 259
    R1 _ "Cl." | \barNumberCheck #260
    r2 r4 \stemDown d''16 ( _\ff \stemDown es16 \stemDown d16 \stemDown
    es16 | % 261
    \stemDown bes8 ) r8 \stemDown fis16 ( \stemDown g16 \stemDown fis16
    \stemDown g16 \stemDown es8 ) r8 \stemDown bes16 ( \stemDown b16
    \stemDown bes16 \stemDown b16 ) | % 262
    \stemDown c16 ( \stemDown d16 \stemDown c16 \stemDown bes16 )
    \stemUp a16 ( \stemUp bes16 \stemUp a16 \stemUp g16 ) \stemUp f16 (
    \stemUp g16 \stemUp es16 \stemUp f16 \stemUp d8 ) r8 | % 263
    R1 \pageBreak | % 264
    r2 _ "Cl." r4 \stemDown f''16 ( _\ff \stemDown g16 \stemDown f16
    \stemDown g16 | % 265
    \stemDown d8 ) r8 \stemDown a16 ( \stemDown bes16 \stemDown a16
    \stemDown bes16 \stemDown g8 ) r8 \stemDown cis,16 ( \stemDown d16
    \stemDown cis16 \stemDown d16 ) | % 266
    \stemDown es16 ( \stemDown f16 \stemDown es16 \stemDown d16 )
    \stemDown c16 ( \stemDown d16 \stemDown c16 \stemDown bes16 )
    \stemUp a16 ( \stemUp bes16 \stemUp g16 \stemUp a16 \stemUp f8 ) r8
    | % 267
    R1*2 \pageBreak | % 269
    R1 _ "Cl." | \barNumberCheck #270
    \stemUp d4 ~ _\fff \stemUp d8 r8 \stemUp d4 ~ \stemUp d8 r8 | % 271
    \stemUp es4 ~ \stemUp es8 r8 \stemUp f4 ~ \stemUp f8 r8 | % 272
    \stemDown bes'4 ~ \stemDown bes8 r8 \stemDown b4 ~ \stemDown b8 r8 | % 273
    \stemDown c8 r8 \stemDown as8 r8 \stemDown f8 r8 \stemDown c8 r8
    \pageBreak | % 274
    \stemDown c8 _ "Cl." r8 \stemDown c8 r8 \stemDown c8 r8 r4 | % 275
    R1 | % 276
    \stemDown f4 _\fff \stemDown c8. \stemDown c16 \stemDown f4
    \stemDown c4 | % 277
    \stemDown g'8 -. \stemDown c8 -. r4 r2 | % 278
    \stemDown f,4 \stemDown c8. \stemDown c16 \stemDown f4 \stemDown c4
    | % 279
    \stemDown g'8 -. \stemDown c8 -. r4 \stemDown c,8 -. \stemDown f8 -.
    r4 | \barNumberCheck #280
    \stemDown g8 -. \stemDown c8 -. r4 \stemDown c,8 -. \stemDown f8 -.
    r4 \pageBreak | % 281
    \stemDown c'2 _ "Cl." \stemDown f,2 | % 282
    \stemDown c2 \stemUp c,8 r8 \stemUp f16 ( _\fff \stemUp fis16
    \stemUp g16 \stemUp a16 | % 283
    \stemDown bes8 ) r8 \stemDown c8 r8 \stemDown d8 r8 \stemDown f8 r8
    | % 284
    \stemDown bes8 -> \stemDown es,8 ~ ^> \stemDown es2 \stemDown d8 r16
    \stemDown c16 | % 285
    \stemDown f8 r8 \acciaccatura { \stemUp c8 ( } \stemUp bes8 ) r16
    \stemUp a16 \stemDown bes8 r8 \stemDown f'8 r8 | % 286
    \stemDown bes2. -> \stemDown d,8 r16 \stemDown f16 \pageBreak | % 287
    \stemDown g8 _ "Cl." r8 \acciaccatura { \stemUp c,8 ( } \stemUp bes8
    ) r16 \stemUp a16 \stemDown bes8 r8 \stemUp f8 r8 | % 288
    \stemDown bes2. -> \stemDown d8 r16 \stemDown f16 | % 289
    \stemDown bes4 ( -> \stemDown a8 ) r16 \stemDown bes16 \stemDown g4
    ( -> \stemDown fis8 ) r16 \stemDown g16 | \barNumberCheck #290
    \stemDown es4 ( -> \stemDown d8 ) r16 \stemDown es16 \stemDown c4 (
    -> \stemDown bes8 ) r16 \stemDown c16 -. | % 291
    \stemUp g8 -. r16 \stemUp a16 ( \stemDown bes8 ) r16 \stemDown d16 (
    \stemDown g8 ) r16 \stemDown a16 ( \stemDown bes8 ) r16 \stemDown c16
    -. \pageBreak | % 292
    \stemDown d2 ~ -> _ "Cl." \stemDown d8 \stemDown c16 ( \stemDown bes16
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown a16 \stemDown g16 \stemDown f16 \stemDown es16
        \stemDown d16 \stemDown c16 }
    | % 293
    \stemDown bes8 ) r8 \stemDown c8 r8 \stemDown d8 r8 \stemDown f8 r8
    | % 294
    \stemDown bes8 -> \stemDown es,8 ~ ^> \stemDown es2 \stemDown d8 r16
    \stemDown c16 | % 295
    \stemDown f8 r8 \acciaccatura { \stemUp c8 ( } \stemUp bes8 ) r16
    \stemUp a16 \stemDown bes8 r8 \stemDown f'8 r8 | % 296
    \stemDown bes2. -> \stemDown d,8 r16 \stemDown f16 \pageBreak | % 297
    \stemDown g8 _ "Cl." r8 \acciaccatura { \stemUp c,8 ( } \stemUp bes8
    ) r16 \stemUp a16 \stemDown bes8 r8 \stemUp f8 r8 | % 298
    \stemDown bes2. -> \stemDown d8 r16 \stemDown f16 | % 299
    \stemDown ges4 ( -> \stemDown f8 ) r16 \stemDown es16 \stemDown des8
    r8 \stemDown as'8 r16 \stemDown a16 | \barNumberCheck #300
    \stemDown bes4 ( -> \stemDown as8 ) r16 \stemDown ges16 \stemDown f8
    r8 \stemDown bes8 r16 \stemDown c16 | % 301
    \stemDown d2. -> \stemDown c8 r16 \stemDown d,16 \pageBreak | % 302
    \stemDown bes'2. -> _ "Cl." \stemDown a8 r16 \stemDown d,16 | % 303
    \stemDown g4 ( -> \stemDown f8 ) r16 \stemDown g,16 \stemDown es'4 (
    -> \stemDown d8 ) r16 \stemDown g,16 | % 304
    \stemDown bes4 ~ -> _\sempre _\fff \stemDown bes8 r8 \stemDown bes4
    ~ -> \stemDown bes8 r8 | % 305
    \stemDown bes4 ~ -> \stemDown bes8 r8 \stemDown bes4 ~ -> \stemDown
    bes8 r8 | % 306
    \stemDown bes4 ~ -> \stemDown bes8 r8 \stemDown bes4 ~ -> \stemDown
    bes8 r8 | % 307
    \stemDown bes4 ~ -> \stemDown bes8 r8 \stemDown bes4 ~ -> \stemDown
    bes8 r8 \pageBreak | % 308
    \stemDown d4 ( -> _ "Cl." \stemUp c8 ) r16 \stemUp g16 \stemDown es'4
    ( -> \stemDown d8 ) r16 \stemDown g,16 | % 309
    \stemDown f'4 ( -> \stemDown es8 ) r16 \stemDown c16 \stemDown f4 (
    -> \stemDown e8 ) r16 \stemDown c16 | \barNumberCheck #310
    \stemDown g'4 ( -> \stemDown f8 ) r16 \stemDown c16 \stemDown g'4 (
    -> \stemDown fis8 ) r16 \stemDown c16 | % 311
    \stemDown as'4 ( -> \stemDown g8 ) r16 \stemDown c,16 \stemDown bes'4
    ( -> \stemDown a8 ) r16 \stemDown es16 | % 312
    \stemDown c'8 ( _\ffff \stemDown bes8 \stemDown f8 \stemDown bes8 )
    \stemDown c8 ( \stemDown bes8 \stemDown ges8 \stemDown bes8 ) | % 313
    \stemDown c8 ( \stemDown bes8 \stemDown g8 \stemDown bes8 )
    \stemDown c8 ( \stemDown bes8 \stemDown ges8 \stemDown bes8 )
    \pageBreak | % 314
    \stemDown c8 ( _ "Cl." \stemDown bes8 \stemDown a8 \stemDown g8 )
    \stemDown f8 ( \stemDown e'8 \stemDown es8 \stemDown d8 ) | % 315
    \stemDown c8 ( \stemDown bes8 \stemDown a8 \stemDown g8 \stemDown f8
    ) r8 r4 | % 316
    r2 \stemUp f,,4 ( _\p _\< \stemUp fis4 ) | % 317
    \stemUp g4 ( \stemUp a4 \stemUp bes4 \stemUp c4 ) | % 318
    \stemUp d4 ( _\! _\mf \stemUp es4 ) \stemUp f,4 ( _\< \stemUp fis4 )
    | % 319
    \stemUp g4 ( \stemUp a4 \stemUp bes4 \stemUp c4 ) \pageBreak |
    \barNumberCheck #320
    \stemUp d4 ( _\! _\f _ "Cl." _\< \stemUp es4 \stemUp f4 \stemUp fis4
    ) | % 321
    \stemUp g4 ( \stemUp a4 \stemDown bes4 \stemDown c4 ) | % 322
    \stemDown d4 ( _\! _\ff _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemDown es4 \stemDown f4 \stemDown fis4 ) | % 323
    \stemDown g4 ( \stemDown a4 \stemDown bes4 \stemDown c4 ) | % 324
    \stemDown d8 \stopTrillSpan _\fff r8 \once \omit TupletBracket
    \times 4/7  {
        \stemDown bes,16*161/160 ( \stemDown c16*161/160 \stemDown d16*161/160
        \stemDown e16*161/160 \stemDown fis16*161/160 \stemDown g16*161/160
        \stemDown a16*161/160 }
    \stemDown bes8 ) r16 \stemDown a16 -. \stemDown bes8 -. r16
    \stemDown fis16 -. \pageBreak | % 325
    \stemDown g8 -. _ "Cl." r8 \once \omit TupletBracket
    \times 4/7  {
        \stemUp es,16*161/160 ( \stemUp f16*161/160 \stemUp g16*161/160
        \stemUp a16*161/160 \stemUp b16*161/160 \stemUp c16*161/160
        \stemUp d16*161/160 }
    \stemDown es8 ) r16 \stemDown d16 -. \stemDown es8 -. r16 \stemDown
    b16 -. | % 326
    \stemDown c8 -. r8 r4 r4 \once \omit TupletBracket
    \times 4/7  {
        \stemDown cis16*161/160 ( \stemDown dis16*161/160 \stemDown eis16*161/160
        \stemDown fis16*161/160 \stemDown gis16*161/160 \stemDown ais16*161/160
        \stemDown bis16*161/160 }
    | % 327
    \stemDown cis8 ) r8 r4 r4 \once \omit TupletBracket
    \times 4/7  {
        \stemDown es,16*161/160 ( \stemDown f16*161/160 \stemDown g16*161/160
        \stemDown as16*161/160 \stemDown bes16*161/160 \stemDown c16*161/160
        \stemDown d16*161/160 }
    \pageBreak | % 328
    \stemDown es8 ) _ "Cl." r8 r4 r4 \once \omit TupletBracket
    \times 4/7  {
        \stemDown f,16*161/160 ( \stemDown g16*161/160 \stemDown a16*161/160
        \stemDown bes16*161/160 \stemDown c16*161/160 \stemDown d16*161/160
        \stemDown e16*161/160 }
    | % 329
    \stemDown f16 ) \stemDown g,16 ( \stemDown a16 \stemDown bes16
    \stemDown c16 \stemDown bes16 \stemDown a16 \stemDown g16 )
    \stemDown f16 ( \stemDown es16 \stemDown d16 \stemDown c16 ) \stemUp
    bes16 ( \stemUp a16 \stemUp g16 \stemUp f16 ) | \barNumberCheck #330
    \stemDown bes8 _\sempre _\fff r8 \stemUp f8 r16 \stemUp f16
    \stemDown bes8 r8 \stemUp es,8 r8 | % 331
    \stemDown bes'8 -> \stemDown f'8 ^> \stemDown bes16 ( \stemDown c16
    \stemDown d16 \stemDown e16 \stemDown f8 ) r8 \stemDown f,16 (
    \stemDown es16 \stemDown d16 \stemDown c16 \pageBreak | % 332
    \stemDown bes8 ) _ "Cl." r8 \stemUp f8 r16 \stemUp f16 \stemDown bes8
    r8 \stemUp es,8 r8 | % 333
    \stemDown bes'8 -> \stemDown f'8 ^> \stemDown bes16 ( \stemDown c16
    \stemDown d16 \stemDown e16 \stemDown f8 ) r8 \stemDown f,16 (
    \stemDown es16 \stemDown d16 \stemDown c16 | % 334
    \stemDown bes8 ) r8 \stemDown f'16 ( \stemDown fis16 \stemDown g16
    \stemDown a16 \stemDown bes8 ) r8 \stemDown f16 ( \stemDown fis16
    \stemDown g16 \stemDown a16 | % 335
    \stemDown bes8 ) r8 \stemDown f16 ( \stemDown fis16 \stemDown g16
    \stemDown a16 \stemDown bes8 ) r8 \stemDown f16 ( \stemDown fis16
    \stemDown g16 \stemDown a16 \pageBreak | % 336
    \stemDown bes8 ) _ "Cl." r8 \stemDown f16 ( \stemDown fis16
    \stemDown g16 \stemDown a16 \stemDown bes8 ) r8 \stemDown f16 (
    \stemDown fis16 \stemDown g16 \stemDown a16 | % 337
    \stemDown bes8 ) r8 \stemDown f16 ( \stemDown fis16 \stemDown g16
    \stemDown a16 \stemDown bes8 ) r8 \stemDown f16 ( \stemDown fis16
    \stemDown g16 \stemDown a16 | % 338
    \stemDown bes8 ) \stemDown bes8 \stemDown a8 \stemDown g8 \stemDown
    f8 \stemDown es8 \stemDown d8 \stemDown c8 | % 339
    \stemDown bes8 \stemDown a'8 \stemDown g8 \stemDown ges8 \stemDown f8
    \stemDown es8 \stemDown d8 \stemDown c8 | \barNumberCheck #340
    \stemDown bes8 r8 r4 \stemDown c8 r8 r4 \pageBreak | % 341
    \stemDown d8 _ "Cl." r8 r4 \stemDown c'8 r8 r4 | % 342
    \stemDown bes8 r8 \stemDown bes8 r8 r4 \stemDown bes8 r8 | % 343
    r4 \stemDown bes8 r8 r4 \stemDown bes8 r8 | % 344
    \stemDown f8 r8 \stemDown d8 r8 \stemUp f,8 r8 \stemUp f8 r8 | % 345
    f,1 ~ | % 346
    \stemUp f2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp f8 \stemUp f8 \stemUp f8 }
    | % 347
    \stemUp f8 r8 r4 r2 \bar "|."
    }

PartPSixVoiceOne =  \relative es'' {
    \clef "treble" \time 4/4 \key bes \major \transposition a | % 1
    R1*2 | % 3
    \time 12/8  \stemDown es8 -. _\p \stemDown a,8 -. \stemDown es'8 -.
    \stemDown a,8 -. \stemDown es'8 -. \stemDown a,8 -. \stemDown es'8
    -. \stemDown bes8 -. \stemDown es8 -. \stemDown c8 -. \stemDown es8
    -. \stemDown c8 -. | % 4
    r2.*2/3 \stemDown cis8 ( -> _\p \stemDown d8 \stemDown c8 \stemUp
    bes8 \stemUp ges8 \stemUp f8 ) s4 \pageBreak | % 5
    r1 s2 | % 6
    r1 s2 | % 7
    \stemUp c'8 -. _\p \stemUp fis,8 -. \stemUp c'8 -. \stemUp fis,8 -.
    \stemUp c'8 -. \stemUp fis,8 -. \stemUp c'8 -. \stemUp g8 -. \stemUp
    c8 -. \stemDown a8 -. \stemDown c8 -. \stemDown a8 -. \bar "||"
    r2.*2/3 \stemUp a8 ( ^> _\p \stemUp bes8 \stemUp a8 \stemUp g8
    \stemUp es8 \stemUp d8 ) s4 | % 9
    r1 s2 \pageBreak | \barNumberCheck #10
    r1 s2 | % 11
    r1 s2 | % 12
    r1 s2 | % 13
    r1 s2 | % 14
    r1 s2 \break | % 15
    r1 s2 | % 16
    r1 s2 | % 17
    r1 s2 | % 18
    r1 s2 | % 19
    r1 s2 \pageBreak | \barNumberCheck #20
    r1 s2 | % 21
    r1 s2 | % 22
    r1 s2 | % 23
    r1 s2 \break | % 24
    r1 s2 | % 25
    r1 s2 | % 26
    r1 s2 | % 27
    r1 s2 \pageBreak | % 28
    r1 s2 | % 29
    f1. _\mp _\< | \barNumberCheck #30
    \stemUp fis4. ( ^> _\! _\mf \stemUp g8 ) r8*2/3 r8*2/3 r2.*2/3
    s1*1/3 | % 31
    r4.*2/3 \stemDown ais8 -. _\f \stemDown cis8 -. \stemDown fis8 -.
    \stemDown g8 -. r8*2/3 r8*2/3 r4.*2/3 s1*1/3 \pageBreak | % 32
    r4.*2/3 \stemDown ais,8 -. _\f \stemDown cis8 -. \stemDown fis8 -.
    \stemDown g8 -. r8*2/3 r8*2/3 r4.*2/3 s1*1/3 | % 33
    r4.*2/3 \stemUp ais,,8 -. _\mf \stemUp cis8 -. \stemUp fis8 -.
    \stemUp g8 -. r8*2/3 r8*2/3 r4.*2/3 s1*1/3 | % 34
    r4.*2/3 \stemUp ais,8 -. _\mp \stemUp cis8 -. \stemUp fis8 -.
    \stemUp g8 -. r8*2/3 r8*2/3 r4.*2/3 s1*1/3 | % 35
    r4.*2/3 \stemUp c,8 -. _\p \stemUp f8 -. \stemUp a8 -. r4.*2/3
    \stemUp c,8 -. \stemUp f8 -. \stemUp a8 -. s4 \pageBreak | % 36
    r4.*2/3 \stemUp c,8 -. \stemUp f8 -. \stemUp a8 -. r4.*2/3 \stemUp
    c,8 -. \stemUp f8 -. \stemUp a8 -. s4 | % 37
    r1 s2 | % 38
    r1 s2 | % 39
    \stemDown es'8 -. _\p \stemDown c8 -. \stemDown es8 -. \stemDown a,8
    -. \stemDown es'8 -. \stemDown a,8 -. \stemDown c8 -. \stemDown a8
    -. \stemDown c8 -. \stemDown a8 -. \stemDown es'8 -. \stemDown a,8
    -. | \barNumberCheck #40
    \stemDown d8 ( -> \stemDown bes8 \stemDown g8 \stemUp bes8 \stemUp f8
    \stemUp d8 ) r2.*2/3 s4 \pageBreak | % 41
    r1 s2 | % 42
    r1 s2 | % 43
    \stemDown es'8 -. _\mp \stemDown c8 -. \stemDown es8 -. \stemDown a,8
    -. \stemDown es'8 -. \stemDown a,8 -. \stemDown c8 -. \stemDown a8
    -. \stemDown c8 -. \stemDown a8 -. \stemDown es'8 -. \stemDown a,8
    -. | % 44
    \stemDown d8 ( -> \stemDown bes8 \stemDown g8 \stemUp bes8 \stemUp f8
    \stemUp d8 ) r2.*2/3 s4 | % 45
    r1 s2 \pageBreak | % 46
    \stemUp ges4. _\f -\markup{ \italic {marcato} } \stemUp f4. \stemUp
    es4. \stemUp des4 ( ~ \stemUp des16 \stemUp ces16 | % 47
    \stemUp bes8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 48
    \stemUp des8 ( \stemUp es8 \stemUp f8 \stemUp ges8 \stemUp f8
    \stemUp es8 \stemUp des8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 | % 49
    r1 s2 | \barNumberCheck #50
    r2.*2/3 r4.*2/3 \stemDown cis'8 _\ff \stemDown cis8 \stemDown cis8
    s4. \pageBreak | % 51
    \stemDown a8 ( \stemDown b8 \stemDown cis8 \stemDown d8 \stemDown
    cis8 \stemDown b8 \stemUp a8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 | % 52
    \stemUp a,8 ( _\ff \stemUp b8 \stemUp cis8 \stemUp d8 \stemUp cis8
    \stemUp b8 \stemUp a8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 | % 53
    r1 s2 | % 54
    r1 s2 | % 55
    \numericTimeSignature\time 4/4  \stemDown d'4 -> _\mp \stemDown d8 r16
    \stemDown d16 \stemUp a4 ~ _\< \stemUp a8 r8 \pageBreak | % 56
    \stemDown fis''4 -> _\! _\mf \stemDown fis8 r16 \stemDown fis16
    \stemDown a,8 r8 r4 | % 57
    R1*2 | % 59
    \stemDown d,4 -> _\mp \stemDown d8 r16 \stemDown d16 \stemUp a4 ~
    _\< \stemUp a8 r8 | \barNumberCheck #60
    \stemDown fis''4 -> _\! _\mf \stemDown fis8 r16 \stemDown fis16
    \stemDown a,8 r8 r4 \pageBreak | % 61
    d,1 -> _\p _\markup{ \small\italic {poco a poco cresc.} }
    \startTrillSpan | % 62
    bes1 -> | % 63
    d1 -> | % 64
    bes1 -> | % 65
    d1 -> \pageBreak | % 66
    es1 -> | % 67
    fis1 -> \stopTrillSpan _\f _\markup{ \small\italic {cresc.} }
    \startTrillSpan | % 68
    bes1 -> | % 69
    \stemDown d,8 -> \stopTrillSpan _\ff r8 \stemUp d,8 -! _\markup{
        \small\italic {dim.} } \startTrillSpan \stemUp e,8 -! \stemUp f8
    -! \stemUp fis8 -! \stemUp g8 -! \stemUp a8 -! | \barNumberCheck #70
    \stemUp bes8 -! \stemUp b8 -! \stemUp c8 -! \stemUp cis8 -! \stemUp
    d8 -! \stemUp e8 -! \stemUp f8 -! \stemUp fis8 -! \bar "||"
    \pageBreak | % 71
    \key g \major \stemUp g8 \stopTrillSpan _\p -\markup{ \italic
        {leggieramente} } r8 \stemUp d8 r16 \stemUp d16 \stemUp g8 r8
    \stemUp d8 r8 | % 72
    \stemUp g8 -. \stemUp c8 ~ ^> \stemDown c2 \stemUp b8 -. r16 \stemUp
    a16 ( | % 73
    \stemDown d8 ) r8 \acciaccatura { \stemUp a8 ( } \stemUp g8 ) -. r16
    \stemUp fis16 -. \stemUp g8 -. r8 \stemUp d8 r8 | % 74
    \stemUp g2. -> \stemDown b8 -. _\< r16 \stemDown d16 ( | % 75
    \stemDown e8 ) _\! r8 \acciaccatura { \stemUp a,8 ( } \stemUp g8 )
    -. _\p r16 \stemUp fis16 -. \stemUp g8 -. r8 \stemUp d8 r8 \break | % 76
    \stemUp g2 ~ -> \stemUp g8 r8 \stemDown b8 -. _\< r16 \stemDown d16
    -. | % 77
    \stemDown g4 ( -> _\! _\sempre _\p \stemDown fis8 ) r16 \stemDown g16
    \stemDown e4 ( -> \stemDown dis8 ) r16 \stemDown e16 | % 78
    \stemDown c4 ( -> \stemDown b8 ) r16 \stemDown c16 \stemUp a4 ( ->
    \stemUp g8 ) r16 \stemUp a16 ( | % 79
    \stemUp e8 ) _\< r16 \stemUp fis16 ( \stemUp g8 ) r16 \stemUp b16 (
    \stemDown e8 ) r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown a16
    -. | \barNumberCheck #80
    \stemDown b2 ~ _\! _\mf _\< \stemDown b8 \stemDown a16 ( _\! _\ff
    _\> \stemDown g16 \once \omit TupletBracket
    \times 4/6  {
        \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown c16
        \stemDown b16 \stemDown a16 }
    \pageBreak | % 81
    \stemUp g8 ) _\! _\p r8 r4 r2 | % 82
    \stemUp c,8 _\pp r8 \stemUp c8 r16 \stemUp c16 \stemUp c8 r8 \stemUp
    d8 r16 \stemUp d16 | % 83
    \stemUp d8 _\markup{ \small\italic {un poco cresc.} }
    \startTrillSpan r8 \stemUp c8 r16 \stemUp c16 \stemUp b8 r8 \stemUp
    a8 r8 | % 84
    \stemUp g8 r8 \stemUp g8 r16 \stemUp g16 \stemUp g4 ( \stemUp g'8 )
    r8 | % 85
    \stemUp des8 r8 \stemUp c8 r16 \stemUp c16 \stemUp b8 r8 \stemUp a8
    r8 \pageBreak | % 86
    \stemUp c8 r8 \stemUp c8 r16 \stemUp c16 \stemUp c8 r8 \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp d8 ( \stopTrillSpan _\mf \stemUp c8 \stemUp b8 }
    | % 87
    \stemUp bes8 ) _\< r8 r4 \stemUp d8 r8 r4 | % 88
    \stemUp bes8 r8 r4 \stemUp bes8 ( \stemUp b8 ) r4 _\! | % 89
    \stemUp b8 _\f \stemUp b16 \stemUp b16 \stemUp b4 ~ \stemUp b8
    \stemUp b16 \stemUp b16 \stemUp b4 ~ \pageBreak | \barNumberCheck
    #90
    \stemUp b8 \stemUp b16 \stemUp b16 \stemUp b4 ~ \stemUp b8 \stemUp b16
    \stemUp b16 \stemUp dis4 | % 91
    \stemUp b4 _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp b4 \stemUp c4 \stemUp gis4 | % 92
    \stemUp a4 \stemUp e'4 \stemUp g,4 \stemUp gis4 | % 93
    \stemUp a8 \stopTrillSpan _\ff r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 }
    \stemUp c2 ~ | % 94
    \stemUp c8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 }
    \stemUp b2 ~ | % 95
    \stemUp b8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 }
    \stemUp b2 ~ \pageBreak | % 96
    \stemUp b8 r8 \stemUp c8 r8 \stemUp b8 r8 r4 | % 97
    R1 | % 98
    r2 r4 \stemDown a''4 ( _\mf | % 99
    \stemDown d,8 ) r8 \stemDown d4 ( \stemUp g,8 ) r8 \stemUp g4 ~ |
    \barNumberCheck #100
    \stemUp g4 \stemUp e4 ( \stemUp c4 \stemUp a8 ) r8 | % 101
    R1 \break | % 102
    r2 r4 \stemDown fis''4 ( _\mf | % 103
    \stemDown b,8 ) r8 \stemDown b4 ( \stemUp e,8 ) r8 \stemDown e'4 ~ | % 104
    \stemDown e4 \stemDown c4 ( \stemUp a4 \stemUp fis8 ) r8 | % 105
    R1 | % 106
    r2 r4 \stemDown a'4 ( _\mf \pageBreak | % 107
    \stemDown d,8 ) r8 \stemDown d4 ( \stemUp g,8 ) r8 \stemUp g4 ~ | % 108
    \stemUp g4 \stemUp e4 ( \stemUp c4 \stemUp a8 ) r8 | % 109
    R1*2 | % 111
    r4 \stemUp b8 _\ff r8 \stemUp a8 r8 \stemUp g8 r8 | % 112
    \stemUp a8 r8 \stemUp a8 r8 r2 \break | % 113
    \stemUp g'8 _\p r8 \stemUp d8 r16 \stemUp d16 \stemUp g8 r8 \stemUp
    d8 r8 | % 114
    \stemUp g8 -. \stemUp c8 ~ ^> \stemDown c2 \stemUp b8 -. r16 \stemUp
    a16 ( | % 115
    \stemDown d8 ) r8 \acciaccatura { \stemUp a8 ( } \stemUp g8 ) -. r16
    \stemUp fis16 -. \stemUp g8 -. r8 \stemUp d8 r8 | % 116
    \stemUp g2. -> \stemDown b8 -. _\< r16 \stemDown d16 ( | % 117
    \stemDown e8 ) _\! r8 \acciaccatura { \stemUp a,8 ( } \stemUp g8 )
    -. _\p r16 \stemUp fis16 -. \stemUp g8 -. r8 \stemUp d8 r8
    \pageBreak | % 118
    \stemUp g2 ~ -> \stemUp g8 r8 \stemDown b8 -. _\< r16 \stemDown d16
    -. | % 119
    \stemDown g4 ( -> _\! _\sempre _\p \stemDown fis8 ) r16 \stemDown g16
    \stemDown e4 ( -> \stemDown dis8 ) r16 \stemDown e16 |
    \barNumberCheck #120
    \stemDown c4 ( -> \stemDown b8 ) r16 \stemDown c16 \stemUp a4 ( ->
    \stemUp g8 ) r16 \stemUp a16 ( | % 121
    \stemUp e8 ) _\< r16 \stemUp fis16 ( \stemUp g8 ) r16 \stemUp b16 (
    \stemDown e8 ) r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown a16
    -. | % 122
    \stemDown b2 ~ _\! _\mf _\< \stemDown b8 \stemDown a16 ( _\! _\ff
    _\> \stemDown g16 \once \omit TupletBracket
    \times 4/6  {
        \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown c16
        \stemDown b16 \stemDown a16 }
    \break | % 123
    \stemUp g8 ) _\! _\p r8 r4 r2 | % 124
    \stemUp c,8 _\pp r8 \stemUp c8 r16 \stemUp c16 \stemUp c8 r8 \stemUp
    d8 r16 \stemUp d16 | % 125
    \stemUp d8 _\markup{ \small\italic {un poco cresc.} }
    \startTrillSpan r8 \stemUp c8 r16 \stemUp c16 \stemUp b8 r8 \stemUp
    a8 r8 | % 126
    \stemUp g8 r8 \stemUp g8 r16 \stemUp g16 \stemUp g4 ( \stemUp g'8 )
    r8 | % 127
    \stemUp des8 r8 \stemUp c8 r16 \stemUp c16 \stemUp b8 r8 \stemUp a8
    r8 \pageBreak | % 128
    \stemUp c8 r8 \stemUp c8 r16 \stemUp c16 \stemUp c8 r8 \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp d8 ( \stopTrillSpan _\f \stemUp c8 \stemUp b8 }
    | % 129
    \stemUp bes8 ) \stemUp f8 ( \stemUp g8 \stemUp a8 ) \stemUp bes8 (
    \stemUp c8 \stemUp cis8 \stemUp d8 ) | \barNumberCheck #130
    \stemUp es8 ( \stemUp f8 \stemUp g8 \stemUp a8 \stemDown bes16 )
    \stemDown es16 ( \stemDown d16 \stemDown c16 \stemUp bes16 \stemUp
    as16 \stemUp g16 \stemUp f16 ) | % 131
    \stemUp es4 ( ^> \stemUp d8 ) r16 \stemUp c16 \stemUp bes8 r8
    \stemUp f'8 ( -. r16 \stemUp fis16 ) -. \pageBreak | % 132
    \stemUp g4 ( ^> \stemUp f8 ) r16 \stemUp es16 \stemUp d8 r8 r4 | % 133
    \stemUp bes8 \stemUp f8 ( \stemUp g8 \stemUp a8 ) \stemUp bes8 (
    \stemUp c8 \stemUp cis8 \stemUp d8 ) | % 134
    \stemUp es8 ( \stemUp f8 \stemUp g8 \stemUp a8 \stemDown bes16 )
    \stemDown es16 ( \stemDown d16 \stemDown c16 \stemUp bes16 \stemUp
    as16 \stemUp g16 \stemUp f16 ) | % 135
    \stemUp es4 ( ^> \stemUp d8 ) r16 \stemUp c16 \stemUp bes8 r8
    \stemUp f'8 ( -. r16 \stemUp fis16 ) -. \pageBreak | % 136
    \stemUp g4 ( ^> \stemUp f8 ) r16 \stemUp es16 \stemUp d8 r8 r4 | % 137
    \time 12/8  \stemUp es8 r8*2/3 r8*2/3 r8*2/3 \stemDown d'8 -. _\f
    \stemDown f8 -. \stemDown g8 ( \stemDown f8 ) \stemDown es8 -.
    \stemDown d8 -. r8*2/3 r8*2/3 s1*5/24 | % 138
    r4.*2/3 r8*2/3 \stemDown d8 -. _\mf \stemDown f8 -. \stemDown g8 (
    \stemDown f8 ) \stemDown es8 -. \stemDown d8 -. r4*2/3 \bar "||"
    s4 | % 139
    \key bes \major r1 s2 \pageBreak | \barNumberCheck #140
    r1 s2 | % 141
    \stemDown es8 -. _\p \stemDown a,8 -. \stemDown es'8 -. \stemDown a,8
    -. \stemDown es'8 -. \stemDown a,8 -. \stemDown es'8 -. \stemDown
    bes8 -. \stemDown es8 -. \stemDown c8 -. \stemDown es8 -. \stemDown
    c8 -. | % 142
    r2.*2/3 \stemDown cis8 ( -> _\p \stemDown d8 \stemDown c8 \stemUp
    bes8 \stemUp ges8 \stemUp f8 ) s4 | % 143
    r1 s2 | % 144
    r1 s2 \pageBreak | % 145
    \stemUp c'8 -. _\p \stemUp fis,8 -. \stemUp c'8 -. \stemUp fis,8 -.
    \stemUp c'8 -. \stemUp fis,8 -. \stemUp c'8 -. \stemUp g8 -. \stemUp
    c8 -. \stemDown a8 -. \stemDown c8 -. \stemDown a8 -. | % 146
    r2.*2/3 \stemUp a8 ( _\p \stemUp bes8 \stemUp a8 \stemUp g8 \stemUp
    f8 \stemUp es8 ) s4 | % 147
    r1 s2 | % 148
    r1 s2 | % 149
    r1 s2 \pageBreak | \barNumberCheck #150
    r1 s2 | % 151
    r1 s2 | % 152
    r1 s2 | % 153
    r1 s2 | % 154
    r1 s2 \pageBreak | % 155
    r1 s2 | % 156
    r1 s2 | % 157
    r1 s2 | % 158
    r1 s2 \break | % 159
    r1 s2 | \barNumberCheck #160
    r1 s2 | % 161
    r1 s2 | % 162
    r1 s2 \pageBreak | % 163
    r1 s2 | % 164
    r1 s2 | % 165
    r1 s2 | % 166
    r1 s2 \pageBreak | % 167
    f1. _\mp _\< | % 168
    \stemUp fis4. ( _\! _\mf \stemUp g8 ) r8*2/3 r8*2/3 r2.*2/3 s1*1/3 | % 169
    r4.*2/3 \stemDown ais8 -. _\f \stemDown cis8 -. \stemDown fis8 -.
    \stemDown g8 -. r8*2/3 r8*2/3 r4.*2/3 s1*1/3 | \barNumberCheck #170
    r4.*2/3 \stemDown ais,8 -. _\f \stemDown cis8 -. \stemDown fis8 -.
    \stemDown g8 -. r8*2/3 r8*2/3 r4.*2/3 s1*1/3 \pageBreak | % 171
    r4.*2/3 \stemUp ais,,8 -. _\mf \stemUp cis8 -. \stemUp fis8 -.
    \stemUp g8 -. r8*2/3 r8*2/3 r4.*2/3 s1*1/3 | % 172
    r4.*2/3 \stemUp ais,8 -. _\mp \stemUp cis8 -. \stemUp fis8 -.
    \stemUp g8 -. r8*2/3 r8*2/3 r4.*2/3 s1*1/3 | % 173
    r4.*2/3 \stemUp c,8 -. _\p \stemUp f8 -. \stemUp a8 -. r4.*2/3
    \stemUp c,8 -. \stemUp f8 -. \stemUp a8 -. s4 | % 174
    r4.*2/3 \stemUp c,8 -. \stemUp f8 -. \stemUp a8 -. r4.*2/3 \stemUp
    c,8 -. \stemUp f8 -. \stemUp a8 -. s4 \pageBreak | % 175
    r1 s2 | % 176
    r1 s2 | % 177
    \stemDown es'8 -. _\p \stemDown c8 -. \stemDown es8 -. \stemDown a,8
    -. \stemDown es'8 -. \stemDown a,8 -. \stemDown c8 -. \stemDown a8
    -. \stemDown c8 -. \stemDown a8 -. \stemDown es'8 -. \stemDown a,8
    -. | % 178
    \stemDown d8 ( -> \stemDown bes8 \stemDown g8 \stemUp bes8 \stemUp f8
    \stemUp d8 ) r2.*2/3 s4 | % 179
    r1 s2 \pageBreak | \barNumberCheck #180
    r1 s2 | % 181
    \stemDown es'8 -. _\mp \stemDown c8 -. \stemDown es8 -. \stemDown a,8
    -. \stemDown es'8 -. \stemDown a,8 -. \stemDown c8 -. \stemDown a8
    -. \stemDown c8 -. \stemDown a8 -. \stemDown es'8 -. \stemDown a,8
    -. | % 182
    \stemDown d8 ( -> \stemDown bes8 \stemDown g8 \stemUp bes8 \stemUp f8
    \stemUp d8 ) r2.*2/3 s4 | % 183
    r1 s2 \pageBreak | % 184
    \stemUp ges4. _\f _\ marcato \stemUp f4. \stemUp es4. \stemUp des4 (
    ~ \stemUp des16 \stemUp ces16 | % 185
    \stemUp bes8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 186
    \stemUp des8 ( _\f \stemUp es8 \stemUp f8 \stemUp ges8 \stemUp f8
    \stemUp es8 \stemUp des8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 | % 187
    r1 s2 | % 188
    \stemDown bes'4. \stemUp as4. \stemUp ges4. \stemUp f4 ( ~ \stemUp f16
    \stemUp es16 \pageBreak | % 189
    \stemUp des8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 |
    \barNumberCheck #190
    \stemUp f8 ( _\ff \stemUp ges8 \stemUp as8 \stemUp bes8 \stemUp as8
    \stemUp ges8 \stemUp f8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 | % 191
    \numericTimeSignature\time 4/4  r2 \stemUp bes,8 ( _\ff \stemUp a8
    \stemUp g8 \stemUp f8 ) | % 192
    r2 \stemUp bes8 ( _\ff \stemUp as8 \stemUp g8 \stemUp f8 ) | % 193
    \stemDown c'''4 _\ff \stemDown a8 \stemDown f8 \stemDown c4 \stemUp
    a4 \pageBreak | % 194
    \stemDown d16 ( \stemDown c16 \stemDown bes16 \stemDown a16 )
    \stemUp g16 ( \stemUp f16 \stemUp e16 \stemUp d16 \stemUp c8 ) r8 r4
    | % 195
    R1*3 | % 198
    \stemUp d8 ^\pp ^\ leggieramente r8 \stemUp a8 r16 \stemUp a16
    \stemUp d8 r8 \stemUp a8 r8 | % 199
    \stemUp d8 -> \stemUp g8 -> r4 r2 | \barNumberCheck #200
    R1 \pageBreak | % 201
    \stemUp c,8 _\p r8 \stemUp g8 r16 \stemUp g16 \stemUp c8 r8 \stemUp
    g8 r8 | % 202
    \stemUp c8 -> \stemUp f8 -> r4 r2 | % 203
    \stemDown b8 _\p r8 \stemUp f8 r16 \stemUp f16 \stemDown b8 r8
    \stemUp f8 r8 | % 204
    \stemDown f'8 _\< r8 \stemDown c8 r16 \stemDown c16 \stemDown f8 r8
    \stemDown c8 r8 | % 205
    \stemDown f8 -> _\! _\mp \stemDown c'8 -> r4 r2 \pageBreak | % 206
    R1 | % 207
    \stemUp e,,8 _\mf r8 \stemUp bes8 r16 \stemUp bes16 \stemUp e8 r8
    \stemUp bes8 r8 | % 208
    \stemUp f'8 -> \stemUp bes8 -> r4 r2 | % 209
    \stemUp f8 _\f r8 \stemUp c8 r16 \stemUp c16 \stemUp f8 r8 \stemUp c8
    r8 | \barNumberCheck #210
    \stemUp f8 -> \stemUp bes8 -> r4 r2 \pageBreak | % 211
    \stemDown e8 _\f _\< r8 \stemDown bes8 r16 \stemDown bes16 \stemDown
    e8 r8 \stemDown bes8 r8 | % 212
    \stemDown f'8 -> _\! _\ff \stemDown bes8 -> \stemDown f8 r16
    \stemDown f16 \stemDown bes8 r8 \stemDown f8 r8 | % 213
    \stemDown c'8 -> \stemDown f8 -> r4 r2 | % 214
    \stemDown es,8 _\fff r8 \stemDown es8 r16 \stemDown es16 \stemDown
    es8 r8 \stemDown es8 r8 | % 215
    \stemDown es8 -> \stemDown a8 ~ -> \stemDown a2. \pageBreak | % 216
    \stemDown es8 _\fff r8 \stemDown es8 r16 \stemDown es16 \stemDown es8
    r8 \stemDown es8 r8 | % 217
    \stemDown es8 -> \stemDown a8 ~ -> \stemDown a8 \stemDown a8
    \stemDown es8 \stemDown es4 \stemDown es8 | % 218
    \stemDown es8 \stemDown a4 \stemDown a8 \stemDown es8 \stemDown es4
    \stemDown es8 | % 219
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown es8 \stemDown es8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown es8 \stemDown es8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown bes8 \stemDown bes8 r8 }
    | \barNumberCheck #220
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown es8 \stemDown es8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown es8 \stemDown es8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown bes8 \stemDown bes8 r8 }
    \pageBreak | % 221
    \times 2/3  {
        \stemDown es8 -> \stemDown es8 -> r8 }
    r4 r2 | % 222
    r4 \stemDown f,32 ( _\sempre _\fff \stemDown g32 \stemDown a32
    \stemDown bes32 \stemDown c32 \stemDown d32 \stemDown es32 \stemDown
    f32 ) \stemDown g16 ( \stemDown f16 \stemDown es16 \stemDown d16 )
    \stemUp c16 ( \stemUp bes16 \stemUp a16 \stemUp g16 ) | % 223
    \stemUp f16 ( \stemUp es16 \stemUp d16 \stemUp c16 ) \stemUp bes16 (
    \stemUp a16 \stemUp g16 \stemUp f16 ) r2 | % 224
    r4 \stemDown f'32 ( \stemDown g32 \stemDown a32 \stemDown bes32
    \stemDown c32 \stemDown d32 \stemDown es32 \stemDown f32 ) \stemDown
    g16 ( \stemDown f16 \stemDown es16 \stemDown d16 ) \stemUp c16 (
    \stemUp bes16 \stemUp a16 \stemUp g16 ) \pageBreak | % 225
    \stemUp f16 ( \stemUp es16 \stemUp d16 \stemUp c16 ) \stemUp bes16 (
    \stemUp a16 \stemUp g16 \stemUp f16 ) r4 \stemUp f32 ( \stemUp g32
    \stemUp a32 \stemUp bes32 \stemUp c32 \stemUp d32 \stemUp es32
    \stemUp f32 ) | % 226
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp g16 ( \stemUp f16 \stemUp es16 \stemUp d16 \stemUp c16
        \stemUp bes16 }
    \stemUp a8 ) r8 r4 \stemUp f32 ( \stemUp g32 \stemUp a32 \stemUp bes32
    \stemUp c32 \stemUp d32 \stemUp es32 \stemUp f32 ) | % 227
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp g16 ( \stemUp f16 \stemUp es16 \stemUp d16 \stemUp c16
        \stemUp bes16 }
    \stemUp a8 ) r8 r4 \stemUp f32 ( \stemUp g32 \stemUp a32 \stemUp bes32
    \stemUp c32 \stemUp d32 \stemUp es32 \stemUp f32 ) \pageBreak | % 228
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp g16 ( \stemUp f16 \stemUp es16 \stemUp d16 \stemUp c16
        \stemUp bes16 }
    \stemUp a8 ) r8 \once \omit TupletBracket
    \times 4/6  {
        \stemUp g'16 ( \stemUp f16 \stemUp es16 \stemUp d16 \stemUp c16
        \stemUp bes16 }
    \stemUp a8 ) r8 | % 229
    \stemDown bes'8 _\fff r8 \stemUp a8 r8 \stemDown bes8 r8 \stemUp f8
    r8 | \barNumberCheck #230
    \stemUp bes8 ^> \stemUp es,8 ~ ^> \stemUp es2 \stemUp d8 r16 \stemUp
    c16 | % 231
    \stemUp f8 r8 \acciaccatura { \stemUp c8 ( } \stemUp bes8 ) r16
    \stemUp a16 \stemUp bes8 r8 \stemDown c'8 r8 | % 232
    \stemDown bes2. -> \stemDown d8 r16 \stemDown f16 \pageBreak | % 233
    \stemUp g,8 r8 \acciaccatura { \stemUp c8 ( } \stemUp bes8 ) r16
    \stemUp a16 \stemDown bes8 r8 \stemUp f8 r8 | % 234
    \stemDown bes2. -> \stemUp d,8 r16 \stemUp f16 | % 235
    \stemDown bes4 ( -> \stemUp a8 ) r16 \stemUp bes16 \stemUp g4 ( ->
    \stemUp ges8 ) r16 \stemUp g16 | % 236
    \stemDown es'4 ( -> \stemDown d8 ) r16 \stemDown es16 \stemDown c4 (
    -> \stemDown bes8 ) r16 \stemDown c16 -. | % 237
    \stemUp g8 -. r16 \stemUp a16 ( \stemDown bes8 ) r16 \stemDown d16 (
    \stemUp g,8 ) r16 \stemUp a16 ( \stemDown bes8 ) r16 \stemDown c16
    -. \pageBreak | % 238
    \stemDown d2 ~ -> \stemDown d8 \stemDown c16 ( \stemDown bes16 \once
    \omit TupletBracket
    \times 4/6  {
        \stemUp a16 \stemUp g16 \stemUp f16 \stemUp es16 \stemUp d16
        \stemUp c16 }
    | % 239
    \stemUp bes8 ) r8 \stemUp a'8 r8 \stemDown bes8 r8 \stemUp f8 r8 |
    \barNumberCheck #240
    \stemUp bes8 ^> \stemUp es,8 ~ ^> \stemUp es2 \stemUp d8 r16 \stemUp
    c16 | % 241
    \stemUp f8 r8 \acciaccatura { \stemUp c8 ( } \stemUp bes8 ) r16
    \stemUp a16 \stemUp bes8 r8 \stemDown c'8 r8 | % 242
    \stemDown bes2. -> \stemDown d8 r16 \stemDown f16 \pageBreak | % 243
    \stemUp g,8 r8 \acciaccatura { \stemUp c8 ( } \stemUp bes8 ) r16
    \stemUp a16 \stemDown bes8 r8 \stemUp f8 r8 | % 244
    \stemDown bes2. -> \stemUp d,8 r16 \stemUp f16 | % 245
    \stemUp ges4 ( -> \stemUp f8 ) r16 \stemUp es16 \stemUp des8 r8
    \stemUp as'8 r16 \stemUp a16 | % 246
    \stemDown bes4 ( -> \stemUp as8 ) r16 \stemUp ges16 \stemUp f8 r8
    \stemDown bes8 r16 \stemDown c16 | % 247
    \stemDown d2. -> \stemUp c8 r16 \stemUp d,16 \pageBreak | % 248
    \stemDown bes'2. -> \stemUp a8 r16 \stemUp d,16 | % 249
    \stemUp g4 ( -> \stemUp f8 ) r16 \stemUp g16 \stemUp es4 ( ->
    \stemUp d8 ) r16 \stemUp g16 | \barNumberCheck #250
    \stemUp c,4 ( -> \stemUp bes8 ) r16 \stemUp bes16 \stemUp g'4 ( ->
    \stemUp f8 ) r16 \stemUp b,16 | % 251
    \stemUp es8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown c'8 \stemDown c8 \stemDown c8 }
    \stemDown c2 ~ | % 252
    \stemDown c8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \stemUp a2 ~ | % 253
    \stemUp a8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp as8 \stemUp as8 \stemUp as8 }
    \stemUp as2 ~ \pageBreak | % 254
    \stemUp as8 r8 \stemUp a8 r16 \stemUp a16 \stemDown bes8 r8 r4 | % 255
    R1*2 | % 257
    r4 \stemDown f'4 ( _\ff \stemDown bes,8 ) r8 \stemDown bes'4 ~ | % 258
    \stemDown bes4 \stemDown g4 ( \stemDown es4 \stemDown c8 ) r8
    \pageBreak | % 259
    R1*2 | % 261
    r4 \stemDown d4 ( ^\ff \stemUp g,8 ) r8 \stemDown g'4 ~ | % 262
    \stemDown g4 \stemDown es4 ( \stemDown c4 \stemUp a8 ) r8 | % 263
    R1 \pageBreak | % 264
    R1 | % 265
    r4 \stemDown f'4 ( _\ff \stemDown bes,8 ) r8 \stemDown bes'4 ~ | % 266
    \stemDown bes4 \stemDown g4 ( \stemDown es4 \stemDown c8 ) r8 | % 267
    R1*2 \pageBreak | % 269
    R1 | \barNumberCheck #270
    \stemUp c,4 ~ _\fff \stemUp c8 r8 \stemUp b4 ~ \stemUp b8 r8 | % 271
    \stemUp c4 ~ \stemUp c8 r8 \stemUp es4 ~ \stemUp es8 r8 | % 272
    \stemDown des'4 ~ \stemDown des8 r8 \stemDown d4 ~ \stemDown d8 r8 | % 273
    \stemDown e8 r8 \stemDown f8 r8 \stemDown d8 r8 \stemDown es8 r8
    \pageBreak | % 274
    \stemDown bes8 r8 \stemUp a8 r8 \stemDown bes8 r8 r4 | % 275
    R1 | % 276
    \stemDown c4 _\fff \stemUp f,8. \stemUp f16 \stemDown c'4 \stemUp f,4
    | % 277
    \stemDown c'8 -. \stemDown g'8 -. r4 r2 | % 278
    \stemDown c,4 \stemUp f,8. \stemUp f16 \stemDown c'4 \stemUp f,4 | % 279
    \stemDown c'8 -. \stemDown g'8 -. r4 \stemUp f,8 -. \stemUp c'8 -. r4
    | \barNumberCheck #280
    \stemDown c8 -. \stemDown g'8 -. r4 \stemUp f,8 -. \stemUp c'8 -. r4
    \pageBreak | % 281
    \stemDown g'2 \stemDown c,2 | % 282
    \stemUp g2 \stemUp c,8 r8 \stemUp f16 ( _\fff \stemUp fis16 \stemUp
    g16 \stemUp a16 | % 283
    \stemDown bes8 ) r8 \stemUp a8 r8 \stemDown bes8 r8 \stemUp f8 r8 | % 284
    \stemUp bes8 ^> \stemUp es,8 ~ ^> \stemUp es2 \stemUp d8 r16 \stemUp
    c16 | % 285
    \stemUp f8 r8 \acciaccatura { \stemUp c8 ( } \stemUp bes8 ) r16
    \stemUp a16 \stemUp bes8 r8 \stemDown c'8 r8 | % 286
    \stemDown bes2. -> \stemDown d8 r16 \stemDown f16 \pageBreak | % 287
    \stemUp g,8 r8 \acciaccatura { \stemUp c8 ( } \stemUp bes8 ) r16
    \stemUp a16 \stemDown bes8 r8 \stemUp f8 r8 | % 288
    \stemDown bes2. -> \stemUp d,8 r16 \stemUp f16 | % 289
    \stemDown bes4 ( -> \stemUp a8 ) r16 \stemUp bes16 \stemUp g4 ( ->
    \stemUp ges8 ) r16 \stemUp g16 | \barNumberCheck #290
    \stemDown es'4 ( -> \stemDown d8 ) r16 \stemDown es16 \stemDown c4 (
    -> \stemDown bes8 ) r16 \stemDown c16 -. | % 291
    \stemUp g8 -. r16 \stemUp a16 ( \stemDown bes8 ) r16 \stemDown d16 (
    \stemUp g,8 ) r16 \stemUp a16 ( \stemDown bes8 ) r16 \stemDown c16
    -. \pageBreak | % 292
    \stemDown d2 ~ -> \stemDown d8 \stemDown c16 ( \stemDown bes16 \once
    \omit TupletBracket
    \times 4/6  {
        \stemUp a16 \stemUp g16 \stemUp f16 \stemUp es16 \stemUp d16
        \stemUp c16 }
    | % 293
    \stemUp bes8 ) r8 \stemUp a'8 r8 \stemDown bes8 r8 \stemUp f8 r8 | % 294
    \stemUp bes8 ^> \stemUp es,8 ~ ^> \stemUp es2 \stemUp d8 r16 \stemUp
    c16 | % 295
    \stemUp f8 r8 \acciaccatura { \stemUp c8 ( } \stemUp bes8 ) r16
    \stemUp a16 \stemUp bes8 r8 \stemDown c'8 r8 | % 296
    \stemDown bes2. -> \stemDown d8 r16 \stemDown f16 \pageBreak | % 297
    \stemUp g,8 r8 \acciaccatura { \stemUp c8 ( } \stemUp bes8 ) r16
    \stemUp a16 \stemDown bes8 r8 \stemUp f8 r8 | % 298
    \stemDown bes2. -> \stemUp d,8 r16 \stemUp f16 | % 299
    \stemUp ges4 ( -> \stemUp f8 ) r16 \stemUp es16 \stemUp des8 r8
    \stemUp as'8 r16 \stemUp a16 | \barNumberCheck #300
    \stemDown bes4 ( -> \stemUp as8 ) r16 \stemUp ges16 \stemUp f8 r8
    \stemDown bes8 r16 \stemDown c16 | % 301
    \stemDown d2. -> \stemUp c8 r16 \stemUp d,16 \pageBreak | % 302
    \stemDown bes'2. -> \stemUp a8 r16 \stemUp d,16 | % 303
    \stemUp g4 ( -> \stemUp f8 ) r16 \stemUp g16 \stemUp es4 ( ->
    \stemUp d8 ) r16 \stemUp g16 | % 304
    \stemUp c,4 ~ -> _\sempre _\fff \stemUp c8 r8 \stemUp c4 ~ ->
    \stemUp c8 r8 | % 305
    \stemUp c4 ~ -> \stemUp c8 r8 \stemUp c4 ~ -> \stemUp c8 r8 | % 306
    \stemUp c4 ~ -> \stemUp c8 r8 \stemUp c4 ~ -> \stemUp c8 r8 | % 307
    \stemUp c4 ~ -> \stemUp c8 r8 \stemUp c4 ~ -> \stemUp c8 r8
    \pageBreak | % 308
    \stemUp d4 ( -> \stemUp c8 ) r16 \stemUp g16 \stemUp es'4 ( ->
    \stemUp d8 ) r16 \stemUp g,16 | % 309
    \stemUp f'4 ( -> \stemUp es8 ) r16 \stemUp c16 \stemUp f4 ( ->
    \stemUp e8 ) r16 \stemUp c16 | \barNumberCheck #310
    \stemUp g'4 ( -> \stemUp f8 ) r16 \stemUp c16 \stemUp g'4 ( ->
    \stemUp fis8 ) r16 \stemUp c16 | % 311
    \stemUp as'4 ( -> \stemUp g8 ) r16 \stemUp c,16 \stemDown bes'4 ( ->
    \stemUp a8 ) r16 \stemUp es16 | % 312
    \stemUp c'8 ( _\ffff \stemUp bes8 \stemUp f8 \stemUp bes8 ) \stemUp
    c8 ( \stemUp bes8 \stemUp ges8 \stemUp bes8 ) | % 313
    \stemUp c8 ( \stemUp bes8 \stemUp g8 \stemUp bes8 ) \stemUp c8 (
    \stemUp bes8 \stemUp ges8 \stemUp bes8 ) \pageBreak | % 314
    \stemUp c8 ( \stemUp bes8 \stemUp a8 \stemUp g8 ) \stemDown f8 (
    \stemDown e'8 \stemDown es8 \stemDown d8 ) | % 315
    \stemUp c8 ( \stemUp bes8 \stemUp a8 \stemUp g8 \stemUp f8 ) r8 r4 | % 316
    R1 | % 317
    r4 \stemUp f,4 ( _\mp _\< \stemUp g4 \stemUp a4 ) | % 318
    \stemUp bes4 ( _\! _\mf \stemUp c4 ) \stemUp d8 r8 r4 | % 319
    r4 \stemUp f,4 ( _\mf _\< \stemUp g4 \stemUp a4 ) \pageBreak |
    \barNumberCheck #320
    \stemUp bes4 ( _\! _\f _\< \stemUp c4 \stemUp d2 ) | % 321
    \stemUp es4 ( \stemUp f4 \stemUp g4 \stemUp a4 ) | % 322
    \stemDown bes4 ( _\! _\ff _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemDown c4 \stemDown d2 ) | % 323
    \stemDown es4 ( \stemDown f4 \stemDown g4 \stemDown a4 ) | % 324
    \stemDown a8 \stopTrillSpan _\fff r8 \once \omit TupletBracket
    \times 4/7  {
        \stemUp bes,,16*161/160 ( \stemUp c16*161/160 \stemUp d16*161/160
        \stemUp e16*161/160 \stemUp fis16*161/160 \stemUp g16*161/160
        \stemUp a16*161/160 }
    \stemUp bes8 ) r16 \stemUp a16 -. \stemUp bes8 -. r16 \stemUp fis16
    -. \pageBreak | % 325
    \stemUp g8 -. r8 \once \omit TupletBracket
    \times 4/7  {
        \stemUp es16*161/160 ( \stemUp f16*161/160 \stemUp g16*161/160
        \stemUp a16*161/160 \stemUp b16*161/160 \stemUp c16*161/160
        \stemUp d16*161/160 }
    \stemDown es8 ) r16 \stemDown d16 -. \stemDown es8 -. r16 \stemDown
    b16 -. | % 326
    \stemDown c8 -. r8 r4 r4 \once \omit TupletBracket
    \times 4/7  {
        \stemDown cis16*161/160 ( \stemDown dis16*161/160 \stemDown eis16*161/160
        \stemDown fis16*161/160 \stemDown gis16*161/160 \stemDown ais16*161/160
        \stemDown bis16*161/160 }
    | % 327
    \stemDown cis8 ) r8 r4 r4 \once \omit TupletBracket
    \times 4/7  {
        \stemDown es,16*161/160 ( \stemDown f16*161/160 \stemDown g16*161/160
        \stemDown as16*161/160 \stemDown bes16*161/160 \stemDown c16*161/160
        \stemDown d16*161/160 }
    \pageBreak | % 328
    \stemDown es8 ) r8 r4 r4 \once \omit TupletBracket
    \times 4/7  {
        \stemDown f,16*161/160 ( \stemDown g16*161/160 \stemDown a16*161/160
        \stemDown bes16*161/160 \stemDown c16*161/160 \stemDown d16*161/160
        \stemDown e16*161/160 }
    | % 329
    \stemDown f16 ) \stemDown g,16 ( \stemDown a16 \stemDown bes16
    \stemDown c16 \stemDown bes16 \stemDown a16 \stemDown g16 )
    \stemDown f16 ( \stemDown es16 \stemDown d16 \stemDown c16 ) \stemUp
    bes16 ( \stemUp a16 \stemUp g16 \stemUp f16 ) | \barNumberCheck #330
    \stemDown bes8 _\sempre _\fff r8 \stemUp f8 r16 \stemUp f16
    \stemDown bes8 r8 \stemUp es,8 r8 | % 331
    \stemDown bes'8 -> \stemDown f'8 ^> \stemDown bes16 ( \stemDown c16
    \stemDown d16 \stemDown e16 \stemDown f8 ) r8 \stemUp f,,16 (
    \stemUp es16 \stemUp d16 \stemUp c16 \pageBreak | % 332
    \stemUp bes8 ) r8 \stemUp f'8 r16 \stemUp f16 \stemDown bes8 r8
    \stemUp es,8 r8 | % 333
    \stemDown bes'8 -> \stemDown f'8 ^> \stemDown bes16 ( \stemDown c16
    \stemDown d16 \stemDown e16 \stemDown f8 ) r8 \stemUp f,,16 (
    \stemUp es16 \stemUp d16 \stemUp c16 | % 334
    \stemUp bes8 ) r8 \stemUp f'16 ( \stemUp fis16 \stemUp g16 \stemUp a16
    \stemDown bes8 ) r8 \stemUp f16 ( \stemUp fis16 \stemUp g16 \stemUp
    a16 | % 335
    \stemDown bes8 ) r8 \stemUp f16 ( \stemUp fis16 \stemUp g16 \stemUp
    a16 \stemDown bes8 ) r8 \stemUp f16 ( \stemUp fis16 \stemUp g16
    \stemUp a16 \pageBreak | % 336
    \stemDown bes8 ) r8 \stemUp f16 ( \stemUp fis16 \stemUp g16 \stemUp
    a16 \stemDown bes8 ) r8 \stemUp f16 ( \stemUp fis16 \stemUp g16
    \stemUp a16 | % 337
    \stemDown bes8 ) r8 \stemUp f16 ( \stemUp fis16 \stemUp g16 \stemUp
    a16 \stemDown bes8 ) r8 \stemUp f16 ( \stemUp fis16 \stemUp g16
    \stemUp a16 | % 338
    \stemUp bes8 ) \stemUp bes8 \stemUp a8 \stemUp g8 \stemUp f8 \stemUp
    es8 \stemUp d8 \stemUp c8 | % 339
    \stemUp bes8 \stemUp a'8 \stemUp g8 \stemUp ges8 \stemUp f8 \stemUp
    es8 \stemUp d8 \stemUp c8 | \barNumberCheck #340
    \stemUp bes8 r8 r4 \stemUp f'8 r8 r4 \pageBreak | % 341
    \stemDown f'8 r8 r4 \stemDown a8 r8 r4 | % 342
    \stemDown f8 r8 \stemDown f8 r8 r4 \stemDown f8 r8 | % 343
    r4 \stemDown f8 r8 r4 \stemDown f8 r8 | % 344
    \stemDown d8 r8 \stemDown bes8 r8 \stemUp f8 r8 \stemUp d8 r8 | % 345
    f,1 ~ | % 346
    \stemUp f2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp f8 \stemUp f8 \stemUp f8 }
    | % 347
    \stemUp f8 r8 r4 r2 \bar "|."
    }

PartPSevenVoiceOne =  \relative d {
    \clef "bass" \time 4/4 \key g \major | % 1
    R1*2 | % 3
    r8 \stemDown <d fis>8 -. _\p \stemDown <a' c>8 -. \stemDown <d, fis>8
    -. \stemDown <a' c>8 -. \stemDown <e g>8 -. \stemDown <a c>8 -.
    \stemDown <fis a>8 -. | % 4
    \time 12/8  r2.*2/3 \stemUp cis'8 ( -> ^\p \stemUp d8 \stemUp dis8
    \stemUp e8 \stemUp c8 \stemUp b8 ) s4 \pageBreak | % 5
    r1 s2 | % 6
    r1 s2 | % 7
    \numericTimeSignature\time 4/4  r8 \stemUp <b, dis>8 -. _\p
    \stemDown <fis' a>8 -. \stemDown <b, dis>8 -. \stemDown <fis' a>8 -.
    \stemDown <c e>8 -. \stemDown <fis a>8 -. \stemDown <dis fis>8 -.
    \bar "||"
    \time 12/8  r2.*2/3 \stemUp ais'8 ( -> ^\p \stemUp b8 \stemUp c8
    \stemUp b8 \stemUp a8 \stemUp g8 ) s4 | % 9
    r1 s2 \pageBreak | \barNumberCheck #10
    r1 s2 | % 11
    r1 s2 | % 12
    r1 s2 | % 13
    r1 s2 | % 14
    r1 s2 \break | % 15
    r1 s2 | % 16
    r1 s2 | % 17
    r1 s2 | % 18
    r1 s2 | % 19
    r1 s2 \pageBreak | \barNumberCheck #20
    r1 s2 | % 21
    r1 s2 | % 22
    r1 s2 | % 23
    r1 s2 \break | % 24
    r1 s2 | % 25
    r1 s2 | % 26
    r1 s2 | % 27
    r1 s2 \pageBreak | % 28
    r1 s2 | % 29
    r1 s2 | \barNumberCheck #30
    r1 s2 | % 31
    r4.*2/3 \clef "tenor" \stemDown <g es'>8 -. _\f \stemDown <bes f'>8
    -. \stemDown <es g>8 -. \stemDown <e gis>8 -. r8*2/3 r8*2/3 r4.*2/3
    s1*1/3 \pageBreak | % 32
    r4.*2/3 \stemDown <g, es'>8 -. _\f \stemDown <bes f'>8 -. \stemDown
    <es g>8 -. \stemDown <e gis>8 -. r8*2/3 r8*2/3 r4.*2/3 s1*1/3 | % 33
    r4.*2/3 \clef "bass" \stemUp <g,, es'>8 -. _\mf \stemUp <bes f'>8 -.
    \stemUp <es g>8 -. \stemDown <e gis>8 -. r8*2/3 r8*2/3 r4.*2/3
    s1*1/3 | % 34
    r4.*2/3 \stemUp <g, es'>8 -. _\mp \stemUp <bes f'>8 -. \stemUp <es
        g>8 -. \stemDown <e gis>8 -. r8*2/3 r8*2/3 r4.*2/3 s1*1/3 | % 35
    r4.*2/3 \stemDown <a, fis'>8 -. _\p \stemDown <d g>8 -. \stemDown
    <fis a>8 -. r4.*2/3 \stemDown <a, fis'>8 -. \stemDown <d g>8 -.
    \stemDown <fis a>8 -. s4 \pageBreak | % 36
    r4.*2/3 \stemDown <a, fis'>8 -. \stemDown <d g>8 -. \stemDown <fis
        a>8 -. r4.*2/3 \stemDown <a, fis'>8 -. \stemDown <d g>8 -.
    \stemDown <fis a>8 -. s4 | % 37
    r1 s2 | % 38
    r1 s2 | % 39
    \stemDown <c' e>8 -. _\p \stemDown <a d>8 -. \stemDown <c e>8 -.
    \stemDown <fis, d'>8 -. \stemDown <c' e>8 -. \stemDown <fis, d'>8 -.
    \stemDown <a e'>8 -. \stemDown <fis d'>8 -. \stemDown <a e'>8 -.
    \stemDown <fis d'>8 -. \stemDown <c' e>8 -. \stemDown <fis, d'>8 -.
    | \barNumberCheck #40
    \stemDown <b e>8 ( -> \stemDown <g d'>8 \stemDown <e c'>8 \stemUp <g
        b>8 \stemUp <d a'>8 \stemUp <b g'>8 ) r2.*2/3 s4 \pageBreak | % 41
    r1 s2 | % 42
    r1 s2 | % 43
    \stemDown <c' e>8 -. _\mp \stemDown <a d>8 -. \stemDown <c e>8 -.
    \stemDown <fis, d'>8 -. \stemDown <c' e>8 -. \stemDown <fis, d'>8 -.
    \stemDown <a e'>8 -. \stemDown <fis d'>8 -. \stemDown <a e'>8 -.
    \stemDown <fis d'>8 -. \stemDown <c' e>8 -. \stemDown <fis, d'>8 -.
    | % 44
    \stemDown <b e>8 ( -> \stemDown <g d'>8 \stemDown <e c'>8 \stemUp <g
        b>8 \stemUp <d a'>8 \stemUp <b g'>8 ) r2.*2/3 s4 | % 45
    r1 s2 \pageBreak | % 46
    r2.*2/3 r4.*2/3 \stemDown d'8 _\f ^ "a 2" \stemDown d8 \stemDown d8
    s4. | % 47
    \stemDown bes8 ( \stemDown c8 \stemDown d8 \stemDown es8 \stemDown d8
    \stemDown c8 \stemDown bes8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 | % 48
    \clef "bass" \stemUp bes,8 ( \stemUp c8 \stemUp d8 \stemDown es8
    \stemDown d8 \stemDown c8 \stemUp bes8 ) r8*2/3 r8*2/3 r4.*2/3
    s1*5/24 | % 49
    r4.*2/3 \stemUp <fis cis'>8 -. _\ff \stemUp <b dis>8 -. \stemUp <fis
        cis'>8 -. \stemUp <b dis>8 -. \stemUp <cis fis>8 -. \stemUp <b
        dis>8 -. \stemDown <cis fis>8 -. \stemDown <e gis>8 -. \stemDown
    <cis fis>8 -. s8 | \barNumberCheck #50
    \stemDown <dis b'>8 -. \stemDown <fis cis'>8 -. \stemDown <dis b'>8
    -. r4.*2/3 r4.*2/3 \stemDown ais'8 _\ff ^ "a 2" \stemDown ais8
    \stemDown ais8 s4 \pageBreak | % 51
    \stemDown fis8 ( \stemDown gis8 \stemDown ais8 \stemDown b8
    \stemDown ais8 \stemDown gis8 \stemDown fis8 ) r8*2/3 r8*2/3 r4.*2/3
    s1*5/24 | % 52
    \stemUp fis,8 ( _\ff \stemUp gis8 \stemUp ais8 \stemUp b8 \stemUp
    ais8 \stemUp gis8 \stemUp fis8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 | % 53
    fis1. ~ _\pp _\markup{ \small\italic {cresc.} } \startTrillSpan | % 54
    fis1. ~ | % 55
    fis1. ~ \pageBreak | % 56
    fis1. \stopTrillSpan _\f | % 57
    fis1. ~ _\pp _\markup{ \small\italic {cresc.} } \startTrillSpan | % 58
    fis1. ~ | % 59
    fis1. ~ | \barNumberCheck #60
    \stemUp fis2. ~ \stopTrillSpan _\f \stemUp fis8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/24 \pageBreak | % 61
    \numericTimeSignature\time 4/4  \stemUp b8 -. _\p r8 \stemUp fis8 -.
    r16 \stemUp fis16 -. \stemUp b8 -. r8 \stemUp fis8 -. r8 | % 62
    \stemUp b8 -. \stemUp e8 -. r4 r2 | % 63
    \stemUp b8 -. _\mp r8 \stemUp fis8 -. r16 \stemUp fis16 -. \stemUp b8
    -. r8 \stemUp fis8 -. r8 | % 64
    \stemUp b8 -. \stemUp e8 -. r4 r2 | % 65
    dis'1 -> _\mf \pageBreak | % 66
    e1 -> | % 67
    a1 -> _\f _\markup{ \small\italic {cresc.} } \startTrillSpan | % 68
    g1 -> | % 69
    \stemUp <b,,, b'>8 \stopTrillSpan _\ff r8 \stemUp b'8 -! ^ "a 2"
    _\markup{ \small\italic {dim.} } \startTrillSpan \stemUp cis8 -!
    \stemDown d8 -! \stemDown dis8 -! \stemDown e8 -! \stemDown fis8 -!
    | \barNumberCheck #70
    \stemDown g8 -! \stemDown gis8 -! \stemDown a8 -! \stemDown ais8 -!
    \stemDown b8 -! \stemDown cis8 -! \stemDown d8 -! \stemDown dis8 -!
    \bar "||"
    \pageBreak | % 71
    \key e \major \stemDown e8 \stopTrillSpan _\p r8 r4 r2 | % 72
    R1*4 \break | % 76
    R1*3 | % 79
    r2 r4 \stemUp <gis,, gis'>8 -. _\mf \stemUp <fis fis'>8 -. |
    \barNumberCheck #80
    \stemUp <e e'>4 ~ ~ _\< \stemUp <e e'>8 \stemUp <e e'>16 \stemUp <e
        e'>16 \stemUp <gis gis'>8 _\! _\f \stemUp <b fis'>8 r4
    \pageBreak | % 81
    R1 | % 82
    \time 12/8  r2.*2/3 r4.*2/3 \stemDown <a a'>8 ( _\pp \stemDown <b
        b'>8 \stemDown <a a'>8 ) s4. | % 83
    \stemDown <gis gis'>8 ( _\markup{ \small\italic {un poco cresc.} }
    \startTrillSpan \stemDown <a a'>8 \stemDown <gis gis'>8 ) \stemUp
    <fis fis'>8 ( \stemUp <gis gis'>8 \stemUp <fis fis'>8 ) \stemUp <e
        e'>8 ( \stemUp <fis fis'>8 \stemUp <e e'>8 ) \stemUp <dis dis'>8
    ( \stemUp <e e'>8 \stemUp <dis dis'>8 ) | % 84
    \stemUp <cis cis'>8 ( \stemUp <dis dis'>8 \stemUp <cis cis'>8 )
    \stemUp <c c'>8 ( \stemUp <d d'>8 \stemUp <c c'>8 ) \stemUp <b b'>8
    ( \stemUp <ais ais'>8 \stemUp <b b'>8 ) \stemUp <e e'>8 ( \stemUp
    <fis fis'>8 \stemUp <gis gis'>8 ) | % 85
    \stemDown <g g'>8 ( \stemDown <a a'>8 \stemDown <g g'>8 ) \stemUp
    <fis fis'>8 ( \stemUp <gis gis'>8 \stemUp <fis fis'>8 ) \stemUp <e
        e'>8 ( \stemUp <fis fis'>8 \stemUp <e e'>8 ) \stemUp <dis dis'>8
    ( \stemUp <e e'>8 \stemUp <dis dis'>8 ) \pageBreak | % 86
    \stemUp <cis cis'>8 ( \stemUp <dis dis'>8 \stemUp <cis cis'>8 )
    \stemUp <c c'>8 ( \stemUp <d d'>8 \stemUp <c c'>8 ) \stemUp <b b'>8
    ( \stemUp <ais ais'>8 \stemUp <b b'>8 ) \stemUp b''8 ( \stemUp a8
    \stemUp gis8 | % 87
    \numericTimeSignature\time 4/4  \stemUp g8 ) \stopTrillSpan _\mf _\<
    r8 r4 \stemUp g,8 r8 r4 | % 88
    \stemUp c8 r8 r4 \stemUp e,8 r8 r4 _\! | % 89
    r4 \stemUp gis8 _\f r16 \stemUp a16 \stemUp ais4 \stemUp <bis, bis'>4
    \pageBreak | \barNumberCheck #90
    \stemUp <cis cis'>4 \stemUp <ais ais'>8 r16 \stemUp <bis bis'>16
    \stemUp <cis cis'>4 \stemUp <dis dis'>4 | % 91
    \stemUp <e e'>4 _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp <eis eis'>4 \stemUp <fis fis'>4 \stemUp <gis gis'>4 | % 92
    \stemUp a4 ^ "a 2" \stemUp ais4 \stemUp b4 \stemUp cis4 | % 93
    \stemDown d8 \stopTrillSpan _\ff r8 r4 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <c, c'>8 \stemUp <c c'>8 \stemUp <c c'>8 }
    | % 94
    \stemUp <c c'>2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp <b b'>8 \stemUp <b b'>8 \stemUp <b b'>8 }
    | % 95
    \stemUp <b b'>2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp <bes bes'>8 \stemUp <bes bes'>8 \stemUp <bes bes'>8 }
    \pageBreak | % 96
    \stemUp <bes bes'>8 r8 \stemUp <b b'>8 r8 \stemUp <e e'>8 r8 r4 | % 97
    R1*2 | % 99
    R1 | \barNumberCheck #100
    R1*2 \break | % 102
    r2 _\< _\! _\mf _\> \stemUp <gis gis'>2 ~ ~ _\p | % 103
    <gis gis'>1 ~ ~ _\< | % 104
    \stemUp <gis gis'>2. ~ ~ _\! _\mf _\> \stemUp <gis gis'>8 r8 _\! | % 105
    R1*2 \pageBreak | % 107
    R1 | % 108
    R1 | % 109
    R1 | \barNumberCheck #110
    r2 _\< _\! _\mf _\> _\ff \stemUp a'2 ^\ff | % 111
    \stemDown <fis ais>8 r8 \stemDown <e b'>8 r8 \stemDown <dis bis'>8 r8
    \stemDown <cis cis'>8 r8 | % 112
    \stemDown <c d'>8 r8 \stemDown <b dis'>8 r8 r2 \break | % 113
    R1*5 \pageBreak | % 118
    R1*3 | % 121
    r2 r4 \stemUp <gis gis'>8 -. _\mf \stemUp <fis fis'>8 -. | % 122
    \stemUp <e e'>4 ~ ~ _\< \stemUp <e e'>8 \stemUp <e e'>16 \stemUp <e
        e'>16 \stemUp <gis gis'>8 _\! _\f \stemUp <b fis'>8 r4 \break | % 123
    R1 | % 124
    \time 12/8  r2.*2/3 r4.*2/3 \stemDown <a a'>8 ( _\pp \stemDown <b
        b'>8 \stemDown <a a'>8 ) s4. | % 125
    \stemDown <gis gis'>8 ( _\markup{ \small\italic {un poco cresc.} }
    \startTrillSpan \stemDown <a a'>8 \stemDown <gis gis'>8 ) \stemUp
    <fis fis'>8 ( \stemUp <gis gis'>8 \stemUp <fis fis'>8 ) \stemUp <e
        e'>8 ( \stemUp <fis fis'>8 \stemUp <e e'>8 ) \stemUp <dis dis'>8
    ( \stemUp <e e'>8 \stemUp <dis dis'>8 ) | % 126
    \stemUp <cis cis'>8 ( \stemUp <dis dis'>8 \stemUp <cis cis'>8 )
    \stemUp <c c'>8 ( \stemUp <d d'>8 \stemUp <c c'>8 ) \stemUp <b b'>8
    ( \stemUp <ais ais'>8 \stemUp <b b'>8 ) \stemUp <e e'>8 ( \stemUp
    <fis fis'>8 \stemUp <gis gis'>8 ) | % 127
    \stemDown <g g'>8 ( \stemDown <a a'>8 \stemDown <g g'>8 ) \stemUp
    <fis fis'>8 ( \stemUp <gis gis'>8 \stemUp <fis fis'>8 ) \stemUp <e
        e'>8 ( \stemUp <fis fis'>8 \stemUp <e e'>8 ) \stemUp <dis dis'>8
    ( \stemUp <e e'>8 \stemUp <dis dis'>8 ) \pageBreak | % 128
    \stemUp <cis cis'>8 ( \stemUp <dis dis'>8 \stemUp <cis cis'>8 )
    \stemUp <c c'>8 ( \stemUp <d d'>8 \stemUp <c c'>8 ) \stemUp <b b'>8
    ( \stemUp <ais ais'>8 \stemUp <b b'>8 ) \stemUp b''8 (
    \stopTrillSpan ^\f \stemUp a8 \stemUp gis8 | % 129
    \numericTimeSignature\time 4/4  \stemUp g8 ) _\f r8 r4 \stemDown <d
        b'>8 r8 r4 | \barNumberCheck #130
    \clef "tenor" \stemDown <g g'>8 r8 r4 \clef "bass" \stemDown d'16 (
    ^ "a 2" \stemDown c16 \stemDown b16 \stemDown a16 \stemDown g16
    \stemDown f16 \stemDown e16 \stemDown d16 ) | % 131
    \stemDown <c c'>4 ( ^> \stemDown <b b'>8 ) r16 \stemDown <a a'>16
    \stemUp <g g'>8 r8 \stemDown <d' d'>8 ( -. r16 \stemDown <dis dis'>16
    ) -. \pageBreak | % 132
    \stemDown <e e'>4 ( ^> \stemDown <d d'>8 ) r16 \stemDown <c c'>16
    \stemDown <b b'>8 \stemUp g8 ( ^ "a 2" \stemUp a8 \stemUp b8 | % 133
    \stemUp c8 ) r8 r4 \stemDown <d b'>8 r8 r4 | % 134
    \clef "tenor" \stemDown <g g'>8 r8 r4 \clef "bass" \stemDown d'16 (
    ^ "a 2" \stemDown c16 \stemDown b16 \stemDown a16 \stemDown g16
    \stemDown f16 \stemDown e16 \stemDown d16 ) | % 135
    \stemDown <c c'>4 ( ^> \stemDown <b b'>8 ) r16 \stemDown <a a'>16
    \stemUp <g g'>8 r8 \stemDown <d' d'>8 ( -. r16 \stemDown <dis dis'>16
    ) -. \pageBreak | % 136
    \stemDown <e e'>4 ( ^> \stemDown <d d'>8 ) r16 \stemDown <c c'>16
    \stemDown <b b'>8 \stemUp g8 ( ^ "a 2" \stemUp a8 \stemUp b8 | % 137
    \time 12/8  \stemUp c8 ) r8*2/3 r8*2/3 r4.*2/3 \stemDown <e g>4. ->
    _\f \stemDown <g b>8 r8*2/3 r8*2/3 s1*7/24 | % 138
    r2.*2/3 \stemDown <e g>4. -> _\mf \stemDown <g b>8 r4*2/3 \bar "||"
    s1*1/3 | % 139
    \key g \major r1 s2 \pageBreak | \barNumberCheck #140
    r1 s2 | % 141
    \numericTimeSignature\time 4/4  r8 \stemDown <d fis>8 -. _\p
    \stemDown <a' c>8 -. \stemDown <d, fis>8 -. \stemDown <a' c>8 -.
    \stemDown <e g>8 -. \stemDown <a c>8 -. \stemDown <fis a>8 -. | % 142
    \time 12/8  r2.*2/3 \stemUp cis'8 ( -> ^\p \stemUp d8 \stemUp dis8
    \stemUp e8 \stemUp c8 \stemUp b8 ) s4 | % 143
    r1 s2 | % 144
    r1 s2 \pageBreak | % 145
    \numericTimeSignature\time 4/4  r8 \stemUp <b, dis>8 -. _\p
    \stemDown <fis' a>8 -. \stemDown <b, dis>8 -. \stemDown <fis' a>8 -.
    \stemDown <c e>8 -. \stemDown <fis a>8 -. \stemDown <dis fis>8 -. | % 146
    \time 12/8  r2.*2/3 \stemUp ais'8 ( -> ^\p \stemUp b8 \stemUp c8
    \stemUp b8 \stemUp a8 \stemUp g8 ) s4 | % 147
    r1 s2 | % 148
    r1 s2 | % 149
    r1 s2 \pageBreak | \barNumberCheck #150
    r1 s2 | % 151
    r1 s2 | % 152
    r1 s2 | % 153
    r1 s2 | % 154
    r1 s2 \pageBreak | % 155
    r1 s2 | % 156
    r1 s2 | % 157
    r1 s2 | % 158
    r1 s2 \break | % 159
    r1 s2 | \barNumberCheck #160
    r1 s2 | % 161
    r1 s2 | % 162
    r1 s2 \pageBreak | % 163
    r1 s2 | % 164
    r1 s2 | % 165
    r1 s2 | % 166
    r1 s2 \pageBreak | % 167
    r1 s2 | % 168
    r1 s2 | % 169
    \clef "tenor" r4.*2/3 \stemDown <g es'>8 -. _\f \stemDown <bes f'>8
    -. \stemDown <es g>8 -. \stemDown <e gis>8 -. r8*2/3 r8*2/3 r4.*2/3
    s1*1/3 | \barNumberCheck #170
    r4.*2/3 \stemDown <g, es'>8 -. _\f \stemDown <bes f'>8 -. \stemDown
    <es g>8 -. \stemDown <e gis>8 -. r8*2/3 r8*2/3 r4.*2/3 s1*1/3
    \pageBreak | % 171
    \clef "bass" r4.*2/3 \stemUp <g,, es'>8 -. _\mf \stemUp <bes f'>8 -.
    \stemUp <es g>8 -. \stemDown <e gis>8 -. r8*2/3 r8*2/3 r4.*2/3
    s1*1/3 | % 172
    r4.*2/3 \stemUp <g, es'>8 -. _\mp \stemUp <bes f'>8 -. \stemUp <es
        g>8 -. \stemDown <e gis>8 -. r8*2/3 r8*2/3 r4.*2/3 s1*1/3 | % 173
    r4.*2/3 \stemDown <a, fis'>8 -. _\p \stemDown <d g>8 -. \stemDown
    <fis a>8 -. r4.*2/3 \stemDown <a, fis'>8 -. \stemDown <d g>8 -.
    \stemDown <fis a>8 -. s4 | % 174
    r4.*2/3 \stemDown <a, fis'>8 -. \stemDown <d g>8 -. \stemDown <fis
        a>8 -. r4.*2/3 \stemDown <a, fis'>8 -. \stemDown <d g>8 -.
    \stemDown <fis a>8 -. s4 \pageBreak | % 175
    r1 s2 | % 176
    r1 s2 | % 177
    \clef "tenor" \stemDown <c' e>8 -. _\p \stemDown <a d>8 -. \stemDown
    <c e>8 -. \stemDown <fis, d'>8 -. \stemDown <c' e>8 -. \stemDown
    <fis, d'>8 -. \stemDown <a e'>8 -. \stemDown <fis d'>8 -. \stemDown
    <a e'>8 -. \stemDown <fis d'>8 -. \stemDown <c' e>8 -. \stemDown
    <fis, d'>8 -. | % 178
    \stemDown <b e>8 ( -> \stemDown <g d'>8 \stemDown <e c'>8 \stemUp <g
        b>8 \stemUp <d a'>8 \stemUp <b g'>8 ) r2.*2/3 s4 | % 179
    r1 s2 \pageBreak | \barNumberCheck #180
    r1 s2 | % 181
    \stemDown <c' e>8 -. _\mp \stemDown <a d>8 -. \stemDown <c e>8 -.
    \stemDown <fis, d'>8 -. \stemDown <c' e>8 -. \stemDown <fis, d'>8 -.
    \stemDown <a e'>8 -. \stemDown <fis d'>8 -. \stemDown <a e'>8 -.
    \stemDown <fis d'>8 -. \stemDown <c' e>8 -. \stemDown <fis, d'>8 -.
    | % 182
    \stemDown <b e>8 ( -> \stemDown <g d'>8 \stemDown <e c'>8 \stemUp <g
        b>8 \stemUp <d a'>8 \stemUp <b g'>8 ) r2.*2/3 s4 | % 183
    \clef "bass" g1. ~ ^\f \pageBreak | % 184
    \stemUp g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 185
    r2.*2/3 \stemUp g'8 ( ^\f \stemUp as8 \stemUp bes8 \stemUp c8
    \stemUp bes8 \stemUp as8 s4 | % 186
    \stemUp g8 ) _\f r8*2/3 r8*2/3 r4.*2/3 \stemUp g,8 ( \stemUp as8
    \stemUp a8 \stemUp bes8 \stemUp as8 \stemUp g8 ) s1*5/24 | % 187
    as1. ~ ^\ff | % 188
    as1. ~ \pageBreak | % 189
    \stemUp as8 r8*2/3 r8*2/3 r4.*2/3 \stemUp bes'8 ( \stemUp c8 \stemUp
    d8 \stemUp es8 \stemUp d8 \stemUp c8 s1*5/24 | \barNumberCheck #190
    \stemUp bes8 ) _\ff r8*2/3 r8*2/3 r4.*2/3 \stemUp bes,8 ( \stemUp c8
    \stemUp cis8 \stemUp d8 \stemUp c8 \stemUp bes8 ) s1*5/24 | % 191
    \numericTimeSignature\time 4/4  \stemUp a8 r8 r4 \stemUp g'8 ( ^\ff
    \stemUp fis8 \stemUp e8 \stemUp d8 ) | % 192
    r2 \stemUp g8 ( ^\ff \stemUp f8 \stemUp e8 \stemUp d8 ) | % 193
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp g'8 ( \stemUp fis8 \stemUp e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp d8 \stemUp cis8 \stemUp b8 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ( \stemUp g8 \stemUp fis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 \stemUp d8 \stemUp cis8 ) }
    \pageBreak | % 194
    \stemUp b16 ( \stemUp a16 \stemUp g'16 \stemUp fis16 ) \stemUp e16 (
    \stemUp d16 \stemUp cis16 \stemUp b16 \stemUp a8 ) r8 r4 | % 195
    R1 | % 196
    a1 ~ _\pp | % 197
    a1 ~ | % 198
    a1 ~ | % 199
    a1 ~ | \barNumberCheck #200
    a1 ~ _\< \pageBreak | % 201
    a1 ~ _\! _\p | % 202
    a1 ~ | % 203
    a1 | % 204
    \stemUp d'8 -\markup{ \italic {leggieramente} } _\< r8 \stemUp a8 r16
    \stemUp a16 \stemUp d8 r8 \stemUp a8 r8 | % 205
    \stemUp d8 -> _\! _\mp \stemUp a'8 -> \stemDown <a,, a'>8 r16
    \stemDown <a a'>16 \stemDown <d d'>8 r8 \stemDown <a a'>8 r8
    \pageBreak | % 206
    \stemDown <d d'>8 -> \stemDown <g g'>8 -> \stemDown <b, b'>8 r16
    \stemDown <b b'>16 \stemDown <e e'>8 r8 \stemDown <b b'>8 r8 | % 207
    \stemDown <e e'>8 -> \stemDown <a a'>8 -> r4 r2 | % 208
    \clef "tenor" \stemDown g'8 _\mf ^ "a 2" r8 \stemDown d8 r16
    \stemDown d16 \stemDown g8 r8 \stemDown d8 r8 | % 209
    \stemDown a'8 -> \stemDown d,8 -> r4 r2 | \barNumberCheck #210
    \clef "bass" \stemUp a,8 _\f _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemUp a4 \stemUp a4 \stemUp a4 \stemUp a8 ~
    \pageBreak | % 211
    \stemUp a8 \stemUp a4 \stemUp a4 \stemUp a4 \stemUp a8 ^\ff | % 212
    \stemUp g''8 \stopTrillSpan _\ff r8 \stemUp d8 r16 \stemUp d16
    \stemUp g8 r8 \stemUp d8 r8 | % 213
    \stemDown d,8 ^ "a 2" _\fff r8 \stemUp a8 r16 \stemUp a16 \stemDown
    d8 r8 \stemUp a8 r8 | % 214
    \stemDown d8 -> \stemDown g8 ~ -> \stemDown g2. | % 215
    \stemDown d8 _\fff r8 \stemUp a8 r16 \stemUp a16 \stemDown d8 r8
    \stemUp a8 r8 \pageBreak | % 216
    \stemDown d8 -> \stemDown g8 ~ -> \stemDown g2. | % 217
    \stemDown d8 r8 \stemUp a8 r16 \stemUp a16 \stemDown d8 r8 \stemDown
    g8 r16 \stemDown g16 | % 218
    \stemDown d8 r8 \stemUp a8 r16 \stemUp a16 \stemDown d8 r8 \stemDown
    g8 r16 \stemDown g16 | % 219
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d4 \stemDown d8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a4 \stemUp a8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d4 \stemDown d8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g4 \stemDown g8 }
    | \barNumberCheck #220
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d4 \stemDown d8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a4 \stemUp a8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d4 \stemDown d8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g4 \stemDown g8 }
    \pageBreak | % 221
    \times 2/3  {
        \stemDown d8 -> \stemDown d8 -> r8 }
    r4 r2 | % 222
    r4 \stemDown d32 ( _\sempre _\fff \stemDown e32 \stemDown fis32
    \stemDown g32 \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32
    ) \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16 )
    \stemDown a16 ( \stemDown g16 \stemDown fis16 \stemDown e16 ) | % 223
    \stemUp d16 ( \stemUp c16 \stemUp b16 \stemUp a16 ) \stemUp g16 (
    \stemUp fis16 \stemUp e16 \stemUp d16 ) r2 | % 224
    r4 \stemDown d'32 ( \stemDown e32 \stemDown fis32 \stemDown g32
    \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32 ) \stemDown
    e16 ( \stemDown d16 \stemDown c16 \stemDown b16 ) \stemDown a16 (
    \stemDown g16 \stemDown fis16 \stemDown e16 ) \pageBreak | % 225
    \stemUp d16 ( \stemUp c16 \stemUp b16 \stemUp a16 ) \stemUp g16 (
    \stemUp fis16 \stemUp e16 \stemUp d16 ) r4 \stemDown d'32 (
    \stemDown e32 \stemDown fis32 \stemDown g32 \stemDown a32 \stemDown
    b32 \stemDown c32 \stemDown d32 ) | % 226
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemDown fis8 ) r8 r4 \stemDown d32 ( \stemDown e32 \stemDown fis32
    \stemDown g32 \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32
    ) | % 227
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemDown fis8 ) r8 r4 \stemDown d32 ( \stemDown e32 \stemDown fis32
    \stemDown g32 \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32
    ) \pageBreak | % 228
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemDown fis8 ) r8 \once \omit TupletBracket
    \times 4/6  {
        \stemUp e16 ( \stemUp d16 \stemUp c16 \stemUp b16 \stemUp a16
        \stemUp g16 }
    \stemUp fis8 ) r8 | % 229
    \stemDown <b b'>8 _\fff r8 \stemDown <a a'>8 r8 \stemUp <g g'>8 r8
    \stemUp <fis fis'>8 r8 | \barNumberCheck #230
    \stemUp <e e'>8 r8 \stemUp <es es'>8 r8 \stemUp <d d'>8 r8 \stemUp
    <c c'>8 r8 | % 231
    \stemUp <b b'>8 r8 \stemUp a'8 r8 \stemUp g8 r8 \stemUp d'8 r8 | % 232
    \stemUp g2. -> \stemUp b8 r16 \stemUp d16 \pageBreak | % 233
    \stemDown <b, b'>8 r8 \stemDown <a a'>8 r8 \stemUp <g g'>8 r8
    \stemUp <fis fis'>8 r8 | % 234
    \stemUp <e e'>8 r8 \stemUp <es es'>8 r8 \stemUp <d d'>8 r8 r4 | % 235
    \stemDown <g g'>8 -! \stemDown <a a'>8 -! \stemDown <ais ais'>8 -!
    \stemDown <b b'>8 -! \clef "tenor" \stemDown <g' g'>8 -! \stemDown
    <a a'>8 -! \stemDown <b b'>8 -! \stemDown <c c'>8 -! | % 236
    \stemDown <c e>8 -! r8 r4 \stemDown <c, c'>8 -! \stemDown <d d'>8 -!
    \stemDown <e e'>8 -! \stemDown <fis fis'>8 -! | % 237
    \stemDown <g g'>8 -! \stemDown <fis fis'>8 -! \stemDown <e e'>8 -!
    \stemDown <d d'>8 -! \clef "bass" \stemDown <cis cis'>8 -! \stemDown
    <c c'>8 -! \stemDown <b b'>8 -! \stemDown <a a'>8 -! \pageBreak | % 238
    \stemUp <g g'>4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g e'>8 \stemUp <g e'>8 \stemUp <g e'>8 }
    \stemDown <b fis'>8 \stemDown <d fis>8 r4 | % 239
    \stemDown <b b'>8 r8 \stemDown <a a'>8 r8 \stemUp <g g'>8 r8 \stemUp
    <fis fis'>8 r8 | \barNumberCheck #240
    \stemUp <e e'>8 r8 \stemUp <es es'>8 r8 \stemUp <d d'>8 r8 \stemUp
    <c c'>8 r8 | % 241
    \stemUp <b b'>8 r8 \stemUp a'8 r8 \stemUp g8 r8 \stemUp d'8 r8 | % 242
    \stemUp g2. -> \stemUp b8 r16 \stemUp d16 \pageBreak | % 243
    \stemDown <b, b'>8 r8 \stemDown <a a'>8 r8 \stemUp <g g'>8 r8
    \stemUp <fis fis'>8 r8 | % 244
    \stemUp <e e'>8 r8 \stemUp <es es'>8 r8 \stemUp <d d'>8 r8 r4 | % 245
    \stemUp <g es'>8 -! \stemUp <f f'>8 -! \stemUp <g g'>8 -! \stemUp
    <as as'>8 -! \stemDown <bes bes'>8 -! \stemDown <c c'>8 -! \stemDown
    <cis cis'>8 -! \stemDown <d d'>8 -! | % 246
    \clef "tenor" \stemDown <es es'>8 -! \stemDown <f f'>8 -! \stemDown
    <g g'>8 -! \stemDown <as as'>8 -! \stemDown <bes bes'>8 -! \stemDown
    <b b'>8 -! r4 | % 247
    \clef "bass" r4 \stemUp <b,, b'>8 r16 \stemUp <c c'>16 \stemUp <cis
        cis'>8 r8 \stemUp <dis dis'>8 r8 \pageBreak | % 248
    \stemUp <e e'>8 r8 \stemUp <cis cis'>8 r16 \stemUp <dis dis'>16
    \stemUp <e e'>8 r8 \stemUp <fis fis'>8 r8 | % 249
    \stemUp <g g'>8 r8 \stemUp <gis gis'>8 r8 \stemDown <a a'>8 r8
    \stemUp b'8 r16 \stemUp e16 | \barNumberCheck #250
    \stemUp a,4 ( -> \stemUp g8 ) r16 \stemUp g16 \stemUp e'4 ( ->
    \stemUp d8 ) r16 \stemUp gis,16 | % 251
    \stemDown <f a>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <f a>8 \stemDown <f a>8 \stemDown <f a>8 }
    \stemDown <f a>2 ~ ~ | % 252
    \stemDown <f a>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <fis b>8 \stemDown <fis b>8 \stemDown <fis b>8 }
    \stemDown <fis b>2 ~ ~ | % 253
    \stemDown <fis b>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g b>8 \stemDown <g b>8 \stemDown <g b>8 }
    \stemDown <g b>2 ~ ~ \pageBreak | % 254
    \stemDown <g b>8 r8 \stemUp c8 r16 \stemUp fis16 \stemUp g8 r8 r4 | % 255
    R1 | % 256
    r2 r8 \stemUp <e,, e'>8 -. _\f \stemUp <f f'>8 -. \stemUp <fis fis'>8
    -. | % 257
    \stemDown <g g'>8 -. _\< \stemDown <a a'>8 -. \stemDown <ais ais'>8
    -. \stemDown <b b'>8 -. \stemDown <c c'>8 -. \stemDown <cis cis'>8
    -. \stemDown <d d'>8 -. \stemDown <dis dis'>8 -. | % 258
    \stemDown <e e'>8 -. _\! _\ff _\> \stemDown <d d'>8 -. \stemDown <c
        c'>8 -. \stemDown <b b'>8 -. \stemDown <a a'>8 -. \stemDown <g
        g'>8 -. \stemUp <fis fis'>8 -. r8 _\! \pageBreak | % 259
    R1 | \barNumberCheck #260
    r2 r8 \stemUp <cis cis'>8 -. _\f \stemUp <d d'>8 -. \stemUp <dis
        dis'>8 -. | % 261
    \stemUp <e e'>8 -. _\< \stemUp <fis fis'>8 -. \stemUp <g g'>8 -.
    \stemUp <gis gis'>8 -. \stemDown <a a'>8 -. \stemDown <ais ais'>8 -.
    \stemDown <b b'>8 -. \stemDown <d d'>8 -. | % 262
    \stemDown <c c'>8 -. _\! _\ff _\> \stemDown <b b'>8 -. \stemDown <a
        a'>8 -. \stemDown <g g'>8 -. \stemUp <fis fis'>8 -. \stemUp <e
        e'>8 -. \stemUp <dis dis'>8 -. r8 _\! | % 263
    R1 \pageBreak | % 264
    r2 r8 \stemUp <e e'>8 -. _\f \stemUp <f f'>8 -. \stemUp <fis fis'>8
    -. | % 265
    \stemDown <g g'>8 -. _\< \stemDown <a a'>8 -. \stemDown <ais ais'>8
    -. \stemDown <b b'>8 -. \stemDown <c c'>8 -. \stemDown <cis cis'>8
    -. \stemDown <d d'>8 -. \stemDown <dis dis'>8 -. | % 266
    \stemDown <e e'>8 -. _\! _\ff _\> \stemDown <d d'>8 -. \stemDown <c
        c'>8 -. \stemDown <b b'>8 -. \stemDown <a a'>8 -. \stemDown <g
        g'>8 -. \stemUp <fis fis'>8 -. r8 _\! | % 267
    R1*2 \pageBreak | % 269
    r2 \stemUp d''4 ~ ^\fff \stemUp d8 r8 | \barNumberCheck #270
    \stemDown <fis, dis'>4 ~ ~ \stemDown <fis dis'>8 r8 \stemDown <e e'>4
    ~ ~ \stemDown <e e'>8 r8 | % 271
    \stemDown <es f'>4 ~ ~ \stemDown <es f'>8 r8 \stemDown <d fis'>4 ~ ~
    \stemDown <d fis'>8 r8 | % 272
    \stemDown <cis bes'>4 ~ ~ \stemDown <cis bes'>8 r8 \stemDown <b b'>4
    ~ ~ \stemDown <b b'>8 r8 | % 273
    \stemDown <a cis'>8 r8 \stemDown <as d'>8 r8 \stemDown <g b'>8 r8
    \stemDown <f c''>8 r8 \pageBreak | % 274
    \stemUp cis''8 r8 \stemUp d8 r8 \stemUp e8 _\fff r8 \stemUp c,4 ~
    ^\fff | % 275
    <c, c'>1 ~ ~ | % 276
    <c c'>1 ~ ~ | % 277
    <c c'>1 ~ ~ | % 278
    <c c'>1 ~ ~ | % 279
    <c c'>1 ~ ~ | \barNumberCheck #280
    <c c'>1 ~ ~ \pageBreak | % 281
    <c c'>1 ~ ~ | % 282
    \stemUp <c c'>2 ~ ~ \stemUp <c c'>8 r8 \stemDown <c' c'>8 _\fff r8 | % 283
    \stemDown <b b'>8 r8 \stemDown <a a'>8 r8 \stemUp <g g'>8 r8 \stemUp
    <fis fis'>8 r8 | % 284
    \stemUp <e e'>8 r8 \stemUp <es es'>8 r8 \stemUp <d d'>8 r8 \stemUp
    <c c'>8 r8 | % 285
    \stemUp <b b'>8 r8 \stemUp a'8 r8 \stemUp g8 r8 \stemUp d'8 r8 | % 286
    \stemUp g2. -> \stemUp b8 r16 \stemUp d16 \pageBreak | % 287
    \stemDown <b, b'>8 r8 \stemDown <a a'>8 r8 \stemUp <g g'>8 r8
    \stemUp <fis fis'>8 r8 | % 288
    \stemUp <e e'>8 r8 \stemUp <es es'>8 r8 \stemUp <d d'>8 r8 r4 | % 289
    \stemDown <g g'>8 -! \stemDown <a a'>8 -! \stemDown <ais ais'>8 -!
    \stemDown <b b'>8 -! \clef "tenor" \stemDown <g' g'>8 -! \stemDown
    <a a'>8 -! \stemDown <b b'>8 -! \stemDown <c c'>8 -! |
    \barNumberCheck #290
    \stemDown <c e>8 -! r8 r4 \stemDown <c, c'>8 -! \stemDown <d d'>8 -!
    \stemDown <e e'>8 -! \stemDown <fis fis'>8 -! | % 291
    \stemDown <g g'>8 -! \stemDown <fis fis'>8 -! \stemDown <e e'>8 -!
    \stemDown <d d'>8 -! \clef "bass" \stemDown <cis cis'>8 -! \stemDown
    <c c'>8 -! \stemDown <b b'>8 -! \stemDown <a a'>8 -! \pageBreak | % 292
    \stemUp <g g'>4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g e'>8 \stemUp <g e'>8 \stemUp <g e'>8 }
    \stemDown <b fis'>8 \stemDown <d fis>8 r4 | % 293
    \stemDown <b b'>8 r8 \stemDown <a a'>8 r8 \stemUp <g g'>8 r8 \stemUp
    <fis fis'>8 r8 | % 294
    \stemUp <e e'>8 r8 \stemUp <es es'>8 r8 \stemUp <d d'>8 r8 \stemUp
    <c c'>8 r8 | % 295
    \stemUp <b b'>8 r8 \stemUp a'8 r8 \stemUp g8 r8 \stemUp d'8 r8 | % 296
    \stemUp g2. -> \stemUp b8 r16 \stemUp d16 \pageBreak | % 297
    \stemDown <b, b'>8 r8 \stemDown <a a'>8 r8 \stemUp <g g'>8 r8
    \stemUp <fis fis'>8 r8 | % 298
    \stemUp <e e'>8 r8 \stemUp <es es'>8 r8 \stemUp <d d'>8 r8 r4 | % 299
    \stemUp <g es'>8 -! \stemUp <f f'>8 -! \stemUp <g g'>8 -! \stemUp
    <as as'>8 -! \stemDown <bes bes'>8 -! \stemDown <c c'>8 -! \stemDown
    <cis cis'>8 -! \stemDown <d d'>8 -! | \barNumberCheck #300
    \clef "tenor" \stemDown <es es'>8 -! \stemDown <f f'>8 -! \stemDown
    <g g'>8 -! \stemDown <as as'>8 -! \stemDown <bes bes'>8 -! \stemDown
    <b b'>8 -! r4 | % 301
    \clef "bass" r4 \stemUp <b,, b'>8 r16 \stemUp <c c'>16 \stemUp <cis
        cis'>8 r8 \stemUp <dis dis'>8 r8 \pageBreak | % 302
    \stemUp <e e'>8 r8 \stemUp <cis cis'>8 r16 \stemUp <dis dis'>16
    \stemUp <e e'>8 r8 \stemUp <fis fis'>8 r8 | % 303
    \stemUp <g g'>8 r8 \stemUp <gis gis'>8 r8 \stemDown <a a'>8 r8
    \stemUp b'8 r16 \stemUp e16 | % 304
    \stemDown <g, e'>4 ~ -> ~ _\sempre _\fff \stemDown <g e'>8 r8
    \stemDown <g es'>4 ~ -> ~ \stemDown <g es'>8 r8 | % 305
    \stemDown <g d'>4 ~ -> ~ \stemDown <g d'>8 r8 \stemDown <g cis>4 ~
    -> ~ \stemDown <g cis>8 r8 | % 306
    \stemDown <g c>4 ~ -> ~ \stemDown <g c>8 r8 \stemDown <g cis>4 ~ ->
    ~ \stemDown <g cis>8 r8 | % 307
    \stemDown <g d'>4 ~ -> ~ \stemDown <g d'>8 r8 \stemDown <g dis'>4 ~
    -> ~ \stemDown <g dis'>8 r8 \pageBreak | % 308
    \stemDown <g e'>4 ~ -> ~ \stemDown <g e'>8 r8 \stemDown <gis e'>4 ~
    -> ~ \stemDown <gis e'>8 r8 | % 309
    \stemDown <a e'>4 ~ -> ~ \stemDown <a e'>8 r8 \stemUp <g, g'>4 ~ ->
    ~ \stemUp <g g'>8 r8 | \barNumberCheck #310
    \stemUp <fis fis'>4 ~ -> ~ \stemUp <fis fis'>8 r8 \stemUp <f f'>4 ~
    -> ~ \stemUp <f f'>8 r8 | % 311
    \stemUp <e e'>4 ~ -> ~ \stemUp <e e'>8 r8 \stemUp <es es'>4 ~ -> ~
    \stemUp <es es'>8 r8 | % 312
    \stemUp <d d'>4. _\ffff \stemUp <d d'>8 \stemUp <cis cis'>4. \stemUp
    <cis cis'>8 | % 313
    \stemUp <c c'>4. \stemUp <c c'>8 \stemUp <cis cis'>4. \stemUp <cis
        cis'>8 \pageBreak | % 314
    \stemUp <d d'>4 \stemUp <g g'>4 \stemDown <b b'>4 \stemDown <d d'>4
    | % 315
    \stemUp a''8 ( \stemUp g8 \stemUp fis8 \stemUp e8 \stemUp d8 ) r8
    \stemUp d,16 ( _\fff _\> \stemUp c16 \stemUp b16 \stemUp a16 ) | % 316
    \stemUp b4 ( _\! _\p _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemUp c4 \stemUp b2 ) | % 317
    \stemUp c8 \stemUp c8 ~ \stemUp c4 ~ \stemUp c8 r8 r4 | % 318
    \stemUp b4 ( \stopTrillSpan _\mf _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemUp c4 \stemUp b2 ) | % 319
    \stemUp c8 \stemUp c8 ~ \stemUp c4 ~ \stemUp c8 r8 r4 \pageBreak |
    \barNumberCheck #320
    \stemUp g8 \stopTrillSpan _\f _\< r8 \stemUp d'8 r16 \stemUp d16
    \stemUp g,8 r8 \stemUp d'8 r8 | % 321
    \stemUp g,8 \stemUp c8 ~ \stemUp c4 ~ \stemUp c8 r8 _\! r4 | % 322
    \stemUp b'4 ( _\ff _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemUp c4 \stemUp d4 \stemUp dis4 ) | % 323
    \clef "tenor" \stemDown <c e>4 ( \stemDown <d fis>4 \stemDown <e g>4
    \stemDown <fis a>4 ) | % 324
    \stemDown <fis b>8 \stopTrillSpan _\fff r8 \clef "bass" \stemUp <e,,
        e'>4 ~ ~ \stemUp <e e'>8 r16 \stemUp <dis dis'>16 -. \stemUp <e
        e'>8 -. r16 \stemUp <fis fis'>16 -. \pageBreak | % 325
    \stemUp <g g'>8 -. r8 \stemDown <a a'>4 ~ ~ \stemDown <a a'>8 r16
    \stemDown <gis gis'>16 -. \stemDown <a a'>8 -. r16 \stemDown <b b'>16
    -. | % 326
    \stemDown <c c'>8 -. r8 \stemDown <c c'>4 ~ ~ \stemDown <c c'>8 r8
    \stemUp <g g'>4 ~ ~ | % 327
    \stemUp <g g'>8 r8 \stemUp <es es'>4 ~ ~ \stemUp <es es'>8 r8
    \stemUp <c c'>4 ~ ~ \pageBreak | % 328
    \stemUp <c c'>8 r8 \stemDown <e' cis'>4 ~ ~ \stemDown <e cis'>8 r8
    \stemUp fis,4 ~ | % 329
    \stemUp fis8 r8 \stemUp c''4 ~ \stemUp c8 r8 \stemUp a8 r8 |
    \barNumberCheck #330
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g, g'>8 _\sempre _\fff \stemDown <a a'>8 \stemDown <g
            g'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <fis fis'>8 \stemUp <g g'>8 \stemUp <fis fis'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <fis fis'>8 \stemUp <e e'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <es es'>8 \stemUp <f f'>8 \stemUp <es es'>8 }
    | % 331
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d d'>8 \stemUp <e e'>8 \stemUp <d d'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <f f'>8 \stemUp <e e'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <f f'>8 \stemUp <fis fis'>8 \stemUp <f f'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <fis fis'>8 \stemUp <g g'>8 \stemUp <fis fis'>8 }
    \pageBreak | % 332
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g g'>8 \stemDown <a a'>8 \stemDown <g g'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <fis fis'>8 \stemUp <g g'>8 \stemUp <fis fis'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <fis fis'>8 \stemUp <e e'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <es es'>8 \stemUp <f f'>8 \stemUp <es es'>8 }
    | % 333
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d d'>8 \stemUp <e e'>8 \stemUp <d d'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <f f'>8 \stemUp <e e'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <f f'>8 \stemUp <fis fis'>8 \stemUp <f f'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <fis fis'>8 \stemUp <g g'>8 \stemUp <fis fis'>8 }
    | % 334
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g g'>8 \stemDown <a a'>8 \stemDown <g g'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <fis fis'>8 \stemUp <g g'>8 \stemUp <fis fis'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <fis fis'>8 \stemUp <e e'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d d'>8 \stemUp <e e'>8 \stemUp <d d'>8 }
    | % 335
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g g'>8 \stemDown <a a'>8 \stemDown <g g'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <fis fis'>8 \stemUp <g g'>8 \stemUp <fis fis'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <fis fis'>8 \stemUp <e e'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d d'>8 \stemUp <e e'>8 \stemUp <d d'>8 }
    \pageBreak | % 336
    \stemUp <g g'>8 \stemUp <fis fis'>8 \stemUp <e e'>8 \stemUp <d d'>8
    \stemUp <g g'>8 \stemUp <fis fis'>8 \stemUp <e e'>8 \stemUp <d d'>8
    | % 337
    \stemUp <g g'>8 \stemUp <fis fis'>8 \stemUp <e e'>8 \stemUp <d d'>8
    \stemUp <g g'>8 \stemUp <fis fis'>8 \stemUp <e e'>8 \stemUp <d d'>8
    | % 338
    \stemUp g'8 \stemUp g'8 \stemUp fis8 \stemUp e8 \stemUp d8 \stemUp c8
    \stemUp b8 \stemUp a8 | % 339
    \stemUp g8 \stemUp fis'8 \stemUp e8 \stemUp es8 \stemUp d8 \stemUp c8
    \stemUp b8 \stemUp a8 | \barNumberCheck #340
    \stemUp g8 \stemUp g'8 \stemUp fis8 \stemUp e8 \stemUp d8 \stemUp c8
    \stemUp b8 \stemUp a8 \pageBreak | % 341
    \stemUp g8 \stemUp fis8 \stemUp e8 \stemUp es8 \stemUp d8 \stemUp c8
    \stemUp b8 \stemUp a8 | % 342
    \stemUp g8 ^ "a 2" r8 \stemUp g8 r8 r4 \stemUp g8 r8 | % 343
    r4 \stemUp g8 r8 r4 \stemUp g8 r8 | % 344
    \stemUp g8 r8 \stemUp g8 r8 \stemUp g8 r8 \stemUp g8 r8 | % 345
    b1 ~ | % 346
    \stemUp b2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 }
    | % 347
    \stemUp b8 r8 r4 r2 \bar "|."
    }

PartPSevenVoiceTwo =  \relative b,, {
    \clef "bass" \time 4/4 \key g \major s1*3 | % 4
    \time 12/8  s4 r1 s4 \pageBreak s1*3 | % 7
    \numericTimeSignature\time 4/4  s1 \bar "||"
    \time 12/8  s4 r1 s4*7 \pageBreak s2*15 \break s2*15 \pageBreak s1*6
    \break s1*6 \pageBreak s4*19 \clef "tenor" s4*5 \pageBreak s4*7
    \clef "bass" s4*17 \pageBreak s2*15 \pageBreak s2*15 \pageBreak s1*3
    | % 48
    \clef "bass" s2*9 \pageBreak s2*15 \pageBreak s2*15 \pageBreak | % 61
    \numericTimeSignature\time 4/4  \stemDown b8 -. s8 \stemDown fis'8
    -. s16 \stemDown fis16 -. \stemDown b,8 -. s8 \stemDown fis'8 -. s8
    | % 62
    \stemDown b,8 -. \stemDown e8 -. s2. | % 63
    \stemDown b8 -. s8 \stemDown fis'8 -. s16 \stemDown fis16 -.
    \stemDown b,8 -. s8 \stemDown fis'8 -. s8 | % 64
    \stemDown b,8 -. \stemDown e8 -. s2. | % 65
    \stemDown b'8 -. r8 \stemDown fis8 -. r16 \stemDown fis16 -.
    \stemDown b8 -. r8 \stemDown fis8 -. r8 \pageBreak | % 66
    \stemDown b8 -. \stemDown e8 -. r4 r2 | % 67
    \stemDown b8 -. r8 \stemDown fis8 -. r16 \stemDown fis16 -.
    \stemDown b8 -. r8 \stemDown fis8 -. r8 | % 68
    \stemDown b8 -. \stemDown e8 -. r4 r2 s1*2 \bar "||"
    \pageBreak | % 71
    \key e \major s1*5 \break s1*5 \pageBreak s1 | % 82
    \time 12/8  s1*6 \pageBreak s4*5 r4.*2/3 | % 87
    \numericTimeSignature\time 4/4  \stemDown e,8 s4. \stemDown g8 s4. | % 88
    \stemDown c,8 s4. \stemDown e8 s8*5 \stemDown gis8 s16 \stemDown a16
    \stemDown ais4 s4 \pageBreak s1*6 \pageBreak s1*2 | % 98
    r2 \stemDown b2 ~ _\p | % 99
    b1 ~ | \barNumberCheck #100
    \stemDown b2. ~ \stemDown b8 s8*9 _\! \break s1*4 | % 106
    r2 \stemDown b2 ~ _\p \pageBreak | % 107
    b1 ~ | % 108
    \stemDown b2. ~ \stemDown b8 s8 _\! | % 109
    \stemDown b'2 \stemDown a2 | \barNumberCheck #110
    \stemDown gis2 \stemDown g2 s1*2 \break s1*5 \pageBreak s1*5 \break
    s1 | % 124
    \time 12/8  s1*6 \pageBreak s4*5 r4.*2/3 | % 129
    \numericTimeSignature\time 4/4  \stemDown c,8 s8*7 | \barNumberCheck
    #130
    \clef "tenor" s2 \clef "bass" s1. \pageBreak s1*2 | % 134
    \clef "tenor" s2 \clef "bass" s1. \pageBreak s1 | % 137
    \time 12/8  s1*8/3 \bar "||"
    s1*1/3 | % 139
    \key g \major s1. \pageBreak s1. | % 141
    \numericTimeSignature\time 4/4  s1 | % 142
    \time 12/8  s4 r1 s4*13 \pageBreak | % 145
    \numericTimeSignature\time 4/4  s1 | % 146
    \time 12/8  s4 r1 s4*19 \pageBreak s2*15 \pageBreak s1*6 \break s1*6
    \pageBreak s1*6 \pageBreak s1*3 | % 169
    \clef "tenor" s1*3 \pageBreak | % 171
    \clef "bass" s1*6 \pageBreak s1*3 | % 177
    \clef "tenor" s2*9 \pageBreak s2*9 | % 183
    \clef "bass" s2 r1 \pageBreak s1*1/24 r1 s1*17/24 r1 s1*13/24
    \stemDown bes8 ( \stemDown c8 \stemDown d8 \stemDown es8 \stemDown d8
    \stemDown c8 \stemDown bes8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/12 r1 s2 r1
    \pageBreak s1*7/24 r1 s2 \stemDown d8 ( \stemDown es8 \stemDown f8
    \stemDown g8 \stemDown f8 \stemDown es8 \stemDown d8 ) r8*2/3 r8*2/3
    r4.*2/3 | % 191
    \numericTimeSignature\time 4/4  a1 | % 192
    bes1 | % 193
    a1 ~ \pageBreak | % 194
    \stemDown a2 ~ \stemDown a8 s1*31/24 | % 196
    a1 ~ | % 197
    a1 ~ | % 198
    a1 ~ | % 199
    a1 ~ | \barNumberCheck #200
    a1 ~ \pageBreak | % 201
    a1 ~ | % 202
    a1 ~ | % 203
    a1 ~ | % 204
    \stemDown a8 r8 r4 r2 | % 205
    \stemDown d8 r8 s2. \pageBreak s1*2 | % 208
    \clef "tenor" s1*2 | \barNumberCheck #210
    \clef "bass" s1 \pageBreak s8*7 \stemDown a8 ~ | % 212
    \stemDown a8 \stemDown a4 \stemDown a8 ~ \stemDown a8 r8 r4 s1*3
    \pageBreak s1*5 \pageBreak s1*4 \pageBreak s1*3 \pageBreak s4*13
    \stemDown a8 s8 \stemDown g8 s8 \stemDown fis8 s8 | % 232
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 r4 \pageBreak s2*5
    \clef "tenor" s1*2 \clef "bass" s2 \pageBreak s4*13 \stemDown a'8 s8
    \stemDown g8 s8 \stemDown fis8 s8 | % 242
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 r4 \pageBreak s1*3
    | % 246
    \clef "tenor" s1 | % 247
    \clef "bass" s1 \pageBreak s4*7 \stemDown b'8 r8 | \barNumberCheck
    #250
    \stemDown c8 r8 \stemDown cis8 r8 \stemDown d8 r8 \stemDown e8 r8
    s1*3 \pageBreak s4 \stemDown a8 s16 \stemDown fis'16 \stemDown g8
    s8*35 \pageBreak s1*5 \pageBreak s1*4 | % 268
    r2 \stemDown bes,4 ~ _\fff \stemDown bes8 r8 \pageBreak | % 269
    \stemDown a4 ~ \stemDown a8 s8 \stemDown g4 ~ \stemDown g8 s8*33
    \pageBreak | % 274
    \stemDown e,8 s8 \stemDown d8 s8 \stemDown c2 ~ s1*6 \pageBreak
    s4*17 \stemDown a'8 s8 \stemDown g8 s8 \stemDown fis8 s8 | % 286
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 r4 \pageBreak s2*5
    \clef "tenor" s1*2 \clef "bass" s2 \pageBreak s4*13 \stemDown a'8 s8
    \stemDown g8 s8 \stemDown fis8 s8 | % 296
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 r4 \pageBreak s1*3
    | \barNumberCheck #300
    \clef "tenor" s1 | % 301
    \clef "bass" s1 \pageBreak s4*7 \stemDown b'8 r8 s1*4 \pageBreak
    s1*6 \pageBreak s1 | % 315
    \stemDown fis'4 \stemDown a4 \stemDown d8 s8 \stemDown d,16 (
    \stemDown c16 \stemDown b16 \stemDown a16 ) | % 316
    \stemDown g4 ( \stemDown a4 \stemDown g8 ) r8 \stemDown d8 r8 | % 317
    \stemDown g8 \stemDown c,8 ~ \stemDown c4 ~ \stemDown c8 s4. | % 318
    \stemDown g'4 ( \stemDown a4 \stemDown g8 ) r8 \stemDown d8 r8 | % 319
    \stemDown g8 \stemDown c,8 ~ \stemDown c4 ~ \stemDown c8 s4.
    \pageBreak | \barNumberCheck #320
    \stemDown g'8 s8 \stemDown d8 s16 \stemDown d16 \stemDown g8 s8
    \stemDown d8 s8 | % 321
    \stemDown g8 \stemDown c,8 ~ \stemDown c4 ~ \stemDown c8 s4. | % 322
    \stemDown g''4 ( \stemDown a4 \stemDown b2 ) | % 323
    \clef "tenor" s4*5 \clef "bass" s2. \pageBreak s1*3 \pageBreak s2.
    \stemDown fis,4 ~ | % 329
    \stemDown fis8 s8 \stemDown a8 s8 \stemDown d8 s8 \stemDown fis8
    s8*17 \pageBreak s1*4 \pageBreak s1*2 | % 338
    \stemDown g,8 \stemDown g''8 \stemDown fis8 \stemDown e8 \stemDown d8
    \stemDown c8 \stemDown b8 \stemDown a8 | % 339
    \stemDown g8 \stemDown fis'8 \stemDown e8 \stemDown es8 \stemDown d8
    \stemDown c8 \stemDown b8 \stemDown a8 | \barNumberCheck #340
    \stemDown g8 \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown d8
    \stemDown c8 \stemDown b8 \stemDown a8 \pageBreak | % 341
    \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown es8 \stemDown d8
    \stemDown c8 \stemDown b8 \stemDown a'8 s1*6 \bar "|."
    }

PartPEightVoiceOne =  \relative d' {
    \clef "treble" \time 4/4 \key c \none \transposition f | % 1
    R1*3 _ "Horns" | % 4
    r2 _ "in F" \stemUp <d d'>2 -> _\p \pageBreak | % 5
    R1*3 _ "Hn." \bar "||"
    r2 \stemUp <d d'>2 -> _\p | % 9
    R1 \pageBreak | \barNumberCheck #10
    R1*5 \break | % 15
    \stemUp e8 -. _\p ^ "II" _ "Hn." r8 \stemUp b8 -. r16 \stemUp b16 -.
    \stemUp e8 -. r8 \stemUp b8 -. r8 | % 16
    \stemUp e16 -. _\> r16 \stemUp a8 ~ \stemUp a4 ~ \stemUp a8 _\! _\pp
    r8 r4 | % 17
    R1*3 \pageBreak | \barNumberCheck #20
    R1 _ "Hn." | % 21
    \stemUp <cis, cis'>8 -. _\p ^\markup{ \italic {un poco marcato} } r8
    \stemUp <d d'>8 -. r16 \stemUp <d d'>16 -. \stemUp <cis cis'>8 -. r8
    \stemUp <b b'>8 -. r8 | % 22
    \stemUp <a a'>8 -. r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <gis gis'>8 -. _\< \stemUp <fis fis'>8 -. \stemUp <gis
            gis'>8 -. }
    \stemUp <a a'>8 -. _\! _\> r8 \stemUp <gis gis'>8 -. _\! r8 | % 23
    \stemUp <fis fis'>8 -. r8 r4 r2 \break | % 24
    R1 _ "Hn." | % 25
    \stemUp <cis' cis'>8 -. _\p r8 \stemUp <d d'>8 -. r16 \stemUp <d d'>16
    -. \stemUp <cis cis'>8 -. r8 \stemUp <b b'>8 -. r8 | % 26
    \stemUp <a a'>8 -. r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <gis gis'>8 -. _\< \stemUp <fis fis'>8 -. \stemUp <gis
            gis'>8 -. }
    \stemUp <a a'>8 -. _\! _\> r8 \stemUp <b b'>8 -. _\! r8 | % 27
    \stemUp <cis cis'>8 -. r8 r4 r2 \pageBreak | % 28
    R1*3 _ "Hn." | % 31
    \time 12/8  r2.*2/3 r4.*2/3 \stemUp <c a'>8 _\f \stemUp <dis b'>8 -.
    \stemUp <a' c>8 -. s4. \pageBreak | % 32
    \stemDown <a cis>8 -. _ "Hn." r8*2/3 r8*2/3 r4.*2/3 r4.*2/3 \stemUp
    <c, a'>8 -. _\f \stemUp <dis b'>8 -. \stemUp <a' c>8 -. s1*1/3 | % 33
    \stemDown <a cis>8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 34
    r1 s2 | % 35
    r1 s2 \pageBreak | % 36
    r1 s2 | % 37
    r1 s2 | % 38
    r1 s2 | % 39
    r1 s2 | \barNumberCheck #40
    r1 s2 \pageBreak | % 41
    r1 _ "Hn." s2 | % 42
    r1 s2 | % 43
    r1 s2 | % 44
    r2.*2/3 r4.*2/3 \stemUp <a, a'>8 _\mf \stemUp <a a'>8 \stemUp <a a'>8
    s4. | % 45
    \stemUp <f f'>2. ~ ~ _\> \stemUp <f f'>8 _\! r8*2/3 r8*2/3 r4.*2/3
    s1*5/24 \pageBreak | % 46
    r1 _ "Hn." s2 | % 47
    r1 s2 | % 48
    r1 s2 | % 49
    r1 s2 | \barNumberCheck #50
    \stemDown <fis' fis'>4. _\ff \stemUp <eis eis'>4. \stemUp <dis dis'>4.
    \stemUp <cis cis'>4 ( ~ ~ \stemUp <cis cis'>16 \stemUp <b b'>16
    \pageBreak | % 51
    \stemUp <ais ais'>8 ) _ "Hn." r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24
    | % 52
    r1 s2 | % 53
    \numericTimeSignature\time 4/4  R1 | % 54
    r2 \stemUp cis'4 _> ^\p \stemUp cis8 r16 \stemUp cis16 | % 55
    \stemUp fis,8 r8 r4 r2 \pageBreak | % 56
    r2 _ "Hn." \stemUp cis'4 -> ^\f \stemUp cis8 r16 \stemUp cis16 | % 57
    \stemUp cis,8 ^\pp r8 r4 r2 _\pp | % 58
    r2 \stemUp cis'4 _> ^\p \stemUp cis8 r16 \stemUp cis16 | % 59
    \stemUp fis,8 r8 r4 r2 | \barNumberCheck #60
    r2 \stemUp cis'4 -> ^\f \stemUp cis8 r16 \stemUp cis16 \pageBreak | % 61
    fis1 -> ^\p _ "Hn." ^\markup{ \small\italic {cresc.} }
    \startTrillSpan | % 62
    d1 | % 63
    fis1 | % 64
    d1 | % 65
    <ais fis'>1 \stopTrillSpan _\mf _\markup{ \small\italic {cresc.} }
    \startTrillSpan \pageBreak | % 66
    <b g'>1 -> _ "Hn." | % 67
    <ais e'>1 -> \stopTrillSpan _\f _\< | % 68
    <d fis>1 -> | % 69
    \stemDown <fis, fis'>8 _\! _\ff r8 r4 r2 | \barNumberCheck #70
    R1 \bar "||"
    \pageBreak | % 71
    \key c \none R1 _ "Hn." | % 72
    \stemUp b8 ^\pp -\markup{ \italic {leggieramente} } r8 \stemUp b8 r16
    \stemUp b16 \stemUp ais8 r8 \stemUp <fis ais>8 _\pp r16 \stemUp <fis
        ais>16 | % 73
    \stemUp <fis b>8 r8 \stemUp <e fis>8 r16 \stemUp <e fis>16 \stemUp
    <dis fis>8 r8 \stemUp <cis fis>8 r8 | % 74
    \stemUp <b e>8 r8 r4 r2 | % 75
    \stemUp <eis b'>8 _\pp r8 \stemUp <e fis>8 r16 \stemUp <e fis>16
    \stemUp <dis fis>8 r8 \stemUp <cis fis>8 r8 \break | % 76
    \stemUp <b e>8 _ "Hn." r8 r4 r4 \stemUp b'8 r8 | % 77
    \stemDown <fis fis'>8 _\p r8 r4 \stemUp <dis dis'>8 r8 r4 | % 78
    \stemUp <e b'>8 r8 r4 \stemUp <cis gis'>8 r8 r4 | % 79
    \stemUp <dis gis>8 _\< r8 \stemUp <dis gis>8 r8 \stemUp <d b'>8 r8
    \stemUp <dis b'>8 r8 | \barNumberCheck #80
    \stemUp <dis dis'>4 ~ ~ _\! _\mf _\< \stemUp <dis dis'>8 \stemUp
    <dis dis'>16 \stemUp <dis dis'>16 \stemUp <g dis'>8 _\! _\f \stemUp
    <fis cis'>8 r4 \pageBreak | % 81
    \stemUp fis8 ^\pp _ "Hn." r8 \stemUp <e fis>8 _\pp r16 \stemUp <e
        fis>16 \stemUp <dis fis>8 r8 \stemUp <cis fis>8 r8 | % 82
    \stemUp <b b'>8 r8 \stemUp <b b'>8 r16 \stemUp <b b'>16 \stemUp <ais
        ais'>8 r8 \stemUp <fis' ais>8 r16 \stemUp <fis ais>16 | % 83
    \stemUp <fis b>8 _\markup{ \small\italic {un poco cresc.} }
    \startTrillSpan r8 \stemUp <e fis>8 r16 \stemUp <e fis>16 \stemUp
    <dis fis>8 r8 \stemUp <cis fis>8 r8 | % 84
    \stemUp <b e>8 r8 \stemUp <b e>8 r16 \stemUp <b e>16 \stemUp dis4 (
    \stemUp fis8 ) r8 | % 85
    \stemUp <eis b'>8 r8 \stemUp <e fis>8 r16 \stemUp <e fis>16 \stemUp
    <dis fis>8 r8 \stemUp <cis fis>8 r8 \pageBreak | % 86
    \stemUp <b e>8 _ "Hn." r8 \stemUp <b e>8 r16 \stemUp <b e>16 \stemUp
    <b dis>8 r8 r4 | % 87
    \stemUp <d d'>8 \stopTrillSpan _\mf _\< r8 r4 \stemUp <a a'>8 r8 r4
    | % 88
    \stemDown <b' g'>8 r8 r4 \stemUp <fis b>8 r8 r4 _\! _\f | % 89
    \stemUp <dis dis'>8 _\f \stemUp <dis dis'>16 \stemUp <dis dis'>16
    \stemUp <dis dis'>4 ~ ~ \stemUp <dis dis'>8 \stemUp <dis dis'>16
    \stemUp <dis dis'>16 \stemUp <dis dis'>4 ~ ~ \pageBreak |
    \barNumberCheck #90
    \stemUp <dis dis'>8 _ "Hn." \stemUp <dis dis'>16 \stemUp <dis dis'>16
    \stemUp <dis dis'>4 ~ ~ \stemUp <dis dis'>8 \stemUp <dis dis'>16
    \stemUp <dis dis'>16 \stemUp <dis dis'>4 | % 91
    \stemUp <dis dis'>4 _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemUp <dis dis'>4 \stemUp <e cis'>4 \stemUp <c
        gis'>4 | % 92
    \stemUp gis'4 \stemUp d4 \stemUp dis4 \stemUp dis4 | % 93
    \stemUp cis8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e cis'>8 \stopTrillSpan _\ff \stemUp <e cis'>8 \stemUp
        <e cis'>8 }
    \stemUp <e cis'>2 ~ ~ | % 94
    \stemUp <e cis'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <es bes'>8 \stemUp <es bes'>8 \stemUp <es bes'>8 }
    \stemUp <es bes'>2 ~ ~ | % 95
    \stemUp <es bes'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a es'>8 \stemDown <a es'>8 \stemDown <a es'>8 }
    \stemDown <a es'>2 ~ ~ \pageBreak | % 96
    \stemDown <a es'>8 _ "Hn." r8 \stemUp e'8 r8 \stemUp dis8 r8 r4 | % 97
    R1*5 \break | % 102
    R1*5 \pageBreak | % 107
    R1*6 \break _ "Hn." | % 113
    R1 _ "Hn." | % 114
    \stemUp b8 ^\pp r8 \stemUp b8 r16 \stemUp b16 \stemUp ais8 r8
    \stemUp <fis ais>8 _\pp r16 \stemUp <fis ais>16 | % 115
    \stemUp <fis b>8 r8 \stemUp <e fis>8 r16 \stemUp <e fis>16 \stemUp
    <dis fis>8 r8 \stemUp <cis fis>8 r8 | % 116
    \stemUp <b e>8 r8 r4 r2 | % 117
    \stemUp <eis b'>8 _\pp r8 \stemUp <e fis>8 r16 \stemUp <e fis>16
    \stemUp <dis fis>8 r8 \stemUp <cis fis>8 r8 \pageBreak | % 118
    \stemUp <b e>8 _ "Hn." r8 r4 r4 \stemUp b'8 r8 | % 119
    \stemDown <fis fis'>8 _\p r8 r4 \stemUp <dis dis'>8 r8 r4 |
    \barNumberCheck #120
    \stemUp <e b'>8 r8 r4 \stemUp <cis gis'>8 r8 r4 | % 121
    \stemUp <dis gis>8 _\< r8 \stemUp <dis gis>8 r8 \stemUp <d b'>8 r8
    \stemUp <dis b'>8 r8 | % 122
    \stemUp <dis dis'>4 ~ ~ _\! _\mf _\< \stemUp <dis dis'>8 \stemUp
    <dis dis'>16 \stemUp <dis dis'>16 \stemUp <g dis'>8 _\! _\f \stemUp
    <fis cis'>8 r4 \break | % 123
    \stemUp fis8 ^\pp _ "Hn." r8 \stemUp <e fis>8 _\pp r16 \stemUp <e
        fis>16 \stemUp <dis fis>8 r8 \stemUp <cis fis>8 r8 | % 124
    \stemUp <b b'>8 r8 \stemUp <b b'>8 r16 \stemUp <b b'>16 \stemUp <ais
        ais'>8 r8 \stemUp <fis' ais>8 r16 \stemUp <fis ais>16 | % 125
    \stemUp <fis b>8 _\markup{ \small\italic {un poco cresc.} }
    \startTrillSpan r8 \stemUp <e fis>8 r16 \stemUp <e fis>16 \stemUp
    <dis fis>8 r8 \stemUp <cis fis>8 r8 | % 126
    \stemUp <b e>8 r8 \stemUp <b e>8 r16 \stemUp <b e>16 \stemUp dis4 (
    \stemUp fis8 ) r8 | % 127
    \stemUp <eis b'>8 r8 \stemUp <e fis>8 r16 \stemUp <e fis>16 \stemUp
    <dis fis>8 r8 \stemUp <cis fis>8 r8 \pageBreak | % 128
    \stemUp <b e>8 _ "Hn." r8 \stemUp <b e>8 r16 \stemUp <b e>16 \stemUp
    <b dis>8 r8 r4 | % 129
    \stemUp <d d'>8 \stopTrillSpan _\f r8 r4 \stemUp <a a'>8 r8 r4 |
    \barNumberCheck #130
    \stemDown <b' g'>8 r8 r4 \stemDown <a fis'>8 r8 r4 | % 131
    \stemDown <g g'>2 \stemDown <fis fis'>8 r8 \stemUp <d d'>4 ~ ~
    \pageBreak | % 132
    \stemUp <d d'>4 _ "Hn." \stemDown <g g'>4 \stemUp <d a'>8 r8 r4 | % 133
    \stemUp <d d'>8 r8 r4 \stemUp <a a'>8 r8 r4 | % 134
    \stemDown <b' g'>8 r8 r4 \stemDown <a fis'>8 r8 r4 | % 135
    \stemDown <g g'>2 \stemDown <fis fis'>8 r8 \stemUp <d d'>4 ~ ~
    \pageBreak | % 136
    \stemUp <d d'>4 _ "Hn." \stemDown <g g'>4 \stemUp <d a'>8 r8 r4 | % 137
    \time 12/8  r2.*2/3 \stemUp <d d'>4. _\f \stemUp <fis a>8 r8*2/3 r8*2/3
    s1*1/3 | % 138
    r2.*2/3 \stemUp <d d'>4. -> _\mf \stemUp <fis a>8 r4*2/3 \bar "||"
    s1*1/3 | % 139
    \key c \none r1 s2 \pageBreak | \barNumberCheck #140
    r1 _ "Hn." s2 | % 141
    r1 s2 | % 142
    \numericTimeSignature\time 4/4  r2 \stemUp <d d'>2 ^> _\p | % 143
    R1*2 \pageBreak | % 145
    R1 _ "Hn." | % 146
    r2 \stemUp <b b'>2 ^> _\p | % 147
    R1*3 \pageBreak | \barNumberCheck #150
    R1*3 _ "Hn." | % 153
    R1 | % 154
    R1 \pageBreak | % 155
    R1*4 \break | % 159
    \stemUp <cis cis'>8 -. _\p _\> _\p ^\markup{ \italic {un poco
            marcato} } _ "Hn." r8 \stemUp <d d'>8 -. r16 \stemUp <d d'>16
    -. \stemUp <cis cis'>8 -. r8 \stemUp <b b'>8 -. r8 | \barNumberCheck
    #160
    \stemUp <a a'>8 -. r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <gis gis'>8 -. _\< \stemUp <fis fis'>8 -. \stemUp <gis
            gis'>8 -. }
    \stemUp <a a'>8 -. _\! _\> r8 \stemUp <gis gis'>8 -. _\! r8 | % 161
    \stemUp <fis fis'>8 -. r8 r4 r2 | % 162
    R1 \pageBreak | % 163
    \stemUp <cis' cis'>8 -. _\p _ "Hn." r8 \stemUp <d d'>8 -. r16
    \stemUp <d d'>16 -. \stemUp <cis cis'>8 -. r8 \stemUp <b b'>8 -. r8
    | % 164
    \stemUp <a a'>8 -. r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <gis gis'>8 -. _\< \stemUp <fis fis'>8 -. \stemUp <gis
            gis'>8 -. }
    \stemUp <a a'>8 -. _\! _\> r8 \stemUp <b b'>8 -. _\! r8 | % 165
    \stemUp <cis cis'>8 -. r8 r4 r2 | % 166
    R1 \pageBreak | % 167
    R1*2 _ "Hn." | % 169
    \time 12/8  r2.*2/3 r4.*2/3 \stemUp <c a'>8 -. _\f \stemUp <dis b'>8
    -. \stemUp <a' c>8 -. s4. | \barNumberCheck #170
    \stemDown <a cis>8 -. r8*2/3 r8*2/3 r4.*2/3 r4.*2/3 \stemUp <c, a'>8
    -. _\f \stemUp <dis b'>8 -. \stemUp <a' c>8 -. s1*1/3 \pageBreak | % 171
    \stemDown <a cis>8 -. _ "Hn." r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24
    | % 172
    r1 s2 | % 173
    r1 s2 | % 174
    r1 s2 \pageBreak | % 175
    r1 s2 | % 176
    r1 s2 | % 177
    r1 s2 | % 178
    r1 s2 | % 179
    r1 s2 \pageBreak | \barNumberCheck #180
    r1 _ "Hn." s2 | % 181
    r1 s2 | % 182
    r2.*2/3 r4.*2/3 \stemUp <a, a'>8 _\mf \stemUp <a a'>8 \stemUp <a a'>8
    s4. | % 183
    \stemUp <f f'>2. ~ ~ _\> \stemUp <f f'>8 r8*2/3 _\! r8*2/3 r4.*2/3
    s1*5/24 \pageBreak | % 184
    r1 s2 | % 185
    r1 s2 | % 186
    r1 s2 | % 187
    r1 s2 | % 188
    r1 s2 \pageBreak | % 189
    r1 _ "Hn." s2 | \barNumberCheck #190
    r2.*2/3 r4.*2/3 \stemUp <a a'>8 _\ff \stemUp <a a'>8 \stemUp <a a'>8
    s4. | % 191
    \stemUp <e e'>8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 192
    r1 s2 | % 193
    \numericTimeSignature\time 4/4  \stemUp <e' a>4 _\ff \stemDown <cis'
        e>8 \stemDown <a cis>8 \stemUp <e a>4 \stemDown <cis' e>4
    \pageBreak | % 194
    \stemDown <a cis>4 _ "Hn." \stemUp <cis, e>4 \stemUp <b b'>8 r8 r4 | % 195
    R1*2 | % 197
    R1*3 | \barNumberCheck #200
    \stemUp a'8 _\pp _\ leggieramente ^\leggieramente _\pp r8 \stemUp e8
    r16 \stemUp e16 \stemUp a8 r8 \stemUp e8 r8 \pageBreak | % 201
    \stemUp b'8 -> _ "Hn." _\< \stemUp e8 -> r4 r2 | % 202
    cis1 _\! ^\p _\p | % 203
    fis,1 | % 204
    <e e'>1 _\p _\markup{ \small\italic {poco a poco cresc.} }
    \startTrillSpan | % 205
    <a, a'>1 \pageBreak | % 206
    <fis fis'>1 _ "Hn." | % 207
    <b b'>1 | % 208
    <d d'>1 | % 209
    <e e'>1 | \barNumberCheck #210
    <fis fis'>1 \stopTrillSpan _\f _\markup{ \small\italic {cresc.} }
    \startTrillSpan \pageBreak | % 211
    <b, b'>1 _ "Hn." | % 212
    \stemUp <a a'>2 \stopTrillSpan _\ff \stemUp <b b'>2 | % 213
    \stemUp <c c'>2 \stemUp <cis cis'>8 r8 r4 | % 214
    \stemUp <g' b>8 _\ff r8 \stemUp <e g>8 r16 \stemUp <e g>16 \stemUp
    <g b>8 r8 \stemUp <e g>8 r8 | % 215
    \stemDown <g cis>8 -> \stemDown <cis e>8 ~ -> ~ \stemDown <cis e>2.
    \pageBreak | % 216
    \stemUp <g b>8 _\fff _ "Hn." r8 \stemUp <e g>8 r16 \stemUp <e g>16
    \stemUp <g b>8 r8 \stemUp <e g>8 r8 | % 217
    \stemDown <g cis>8 -> \stemDown <cis e>8 ~ -> ~ \stemDown <cis e>8
    \stemDown <cis e>8 \stemUp <g b>8 \stemUp <e g>4 \stemUp <e g>8 | % 218
    \stemUp <g cis>8 \stemDown <cis e>4 \stemDown <cis e>8 \stemUp <g b>8
    \stemUp <e g>4 \stemUp <e g>8 | % 219
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g cis>8 \stemUp <g cis>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <cis e>8 \stemDown <cis e>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g b>8 \stemUp <g b>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e g>8 \stemUp <e g>8 r8 }
    | \barNumberCheck #220
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g cis>8 \stemUp <g cis>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <cis e>8 \stemDown <cis e>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g b>8 \stemUp <g b>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e g>8 \stemUp <e g>8 r8 }
    \pageBreak | % 221
    \times 2/3  {
        \stemUp <g cis>8 -> _ "Hn." \stemUp <g cis>8 -> r8 }
    r4 r2 | % 222
    R1*3 \pageBreak | % 225
    R1*3 \pageBreak _ "Hn." | % 228
    R1 _ "Hn." | % 229
    \stemUp d'8 _\fff r8 \stemDown <cis e>8 r8 \stemDown <d fis>8 r8
    \stemDown <a e'>8 r8 | \barNumberCheck #230
    \stemDown <g g'>8 r8 \stemDown <g g'>8 r16 \stemDown <g g'>16
    \stemUp <cis, cis'>2 | % 231
    \stemUp <a a'>8 r8 \stemUp <a a'>8 r8 \stemUp <a a'>8 r8 \stemUp <a
        a'>8 r8 | % 232
    \stemUp <g g''>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g g''>8 \stemUp <g g''>8 \stemUp <g g''>8 }
    \stemUp <d' d'>8 r8 r4 \pageBreak | % 233
    r4 _ "Hn." \stemUp <g a>8 r8 \stemUp <fis a>8 r8 \stemUp <e a>8 r8 | % 234
    \stemDown <g g'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g g'>8 \stemDown <g g'>8 \stemDown <g g'>8 }
    \stemDown <a fis'>8 r8 r4 | % 235
    \stemUp <d, d'>8 r8 r4 \stemDown <d d'>8 -! \stemDown <e e'>8 -!
    \stemDown <fis fis'>8 -! \stemDown <g g'>8 -! | % 236
    \stemDown <g g'>8 r8 r4 \stemDown <b e>8 r8 r4 | % 237
    \stemUp <fis b>8 r8 \stemUp <fis b>8 r8 \stemUp <eis d'>8 r8 \stemUp
    <fis b>8 r8 \pageBreak | % 238
    \stemDown <fis fis'>4 _ "Hn." \once \omit TupletBracket
    \times 2/3  {
        \stemUp <b, b'>8 \stemUp <b b'>8 \stemUp <b b'>8 }
    \stemUp <cis cis'>8 \stemUp <cis cis'>8 r4 | % 239
    \stemUp d'8 r8 \stemDown <cis e>8 r8 \stemDown <d fis>8 r8 \stemDown
    <a e'>8 r8 | \barNumberCheck #240
    \stemDown <g g'>8 r8 \stemDown <g g'>8 r16 \stemDown <g g'>16
    \stemUp <cis, cis'>2 | % 241
    \stemUp <a a'>8 r8 \stemUp <a a'>8 r8 \stemUp <a a'>8 r8 \stemUp <a
        a'>8 r8 | % 242
    \stemUp <g g''>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g g''>8 \stemUp <g g''>8 \stemUp <g g''>8 }
    \stemUp <d' d'>8 r8 r4 \pageBreak | % 243
    r4 _ "Hn." \stemUp <g a>8 r8 \stemUp <fis a>8 r8 \stemUp <e a>8 r8 | % 244
    \stemDown <g g'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g g'>8 \stemDown <g g'>8 \stemDown <g g'>8 }
    \stemDown <a fis'>8 r8 r4 | % 245
    \stemDown <f f'>8 r8 r4 \stemDown <a c>8 r8 r4 | % 246
    \stemUp <f d'>8 r8 r4 \stemUp <d a'>8 r8 r4 | % 247
    R1 \pageBreak | % 248
    r2 _ "Hn." r4 \stemDown <b' fis'>8 _\fff r8 | % 249
    \stemDown <b fis'>8 r8 \stemDown <a fis'>8 r8 \stemDown <g e'>8 r8
    \stemUp <fis dis'>8 r8 | \barNumberCheck #250
    \stemUp <e e'>8 r8 \stemUp <f d'>8 r8 \stemDown <fis fis'>8 r8
    \stemDown <fis fis'>8 r8 | % 251
    \stemUp <e e'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e c'>8 \stemUp <e c'>8 \stemUp <e c'>8 }
    \stemUp <e c'>2 ~ ~ | % 252
    \stemUp <e c'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <fis fis'>8 \stemDown <fis fis'>8 \stemDown <fis fis'>8
        }
    \stemDown <fis fis'>2 ~ ~ | % 253
    \stemDown <fis fis'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <fis fis'>8 \stemDown <fis fis'>8 \stemDown <fis fis'>8
        }
    \stemDown <fis fis'>2 ~ ~ \pageBreak | % 254
    \stemDown <fis fis'>8 _ "Hn." r8 r4 r2 | % 255
    \stemDown <cis' e>2 _\fff \stemDown <cis f>2 | % 256
    \stemDown <cis fis>8 r8 \stemDown <d g>8 r8 r2 | % 257
    r2 r4 \stemUp d4 ~ ^\ff | % 258
    \stemUp d4 \stemUp b4 ( \stemUp g4 \stemUp e8 ) r8 \pageBreak | % 259
    \stemDown <cis' e>2 _\fff _ "Hn." \stemDown <cis f>2 |
    \barNumberCheck #260
    \stemDown <cis fis>8 r8 \stemDown <d g>8 r8 r2 | % 261
    R1*2 | % 263
    \stemDown <cis e>2 _\fff \stemDown <cis f>2 \pageBreak | % 264
    \stemDown <cis fis>8 _ "Hn." r8 \stemDown <d g>8 r8 r2 | % 265
    r2 r4 \stemUp d4 ~ ^\ff | % 266
    \stemUp d4 \stemUp b4 ( \stemUp g4 \stemUp e8 ) r8 | % 267
    \stemDown <cis' e>4 ~ ~ _\fff \stemDown <cis e>8 r8 \stemDown <cis
        f>4 ~ ~ \stemDown <cis f>8 r8 | % 268
    \stemDown <cis fis>4 ~ ~ \stemDown <cis fis>8 r8 \stemDown <d g>4 ~
    ~ \stemDown <d g>8 r8 \pageBreak | % 269
    \stemDown <gis, e'>4 ~ ~ _ "Hn." \stemDown <gis e'>8 r8 \stemDown <a
        d>4 ~ ~ \stemDown <a d>8 r8 | \barNumberCheck #270
    \stemDown <fis fis'>4 ~ ~ \stemDown <fis fis'>8 r8 \stemDown <fis
        fis'>4 ~ ~ \stemDown <fis fis'>8 r8 | % 271
    \stemDown <g g'>4 ~ ~ \stemDown <g g'>8 r8 \stemUp <e e'>4 ~ ~
    \stemUp <e e'>8 r8 | % 272
    \stemUp <f d'>4 ~ ~ \stemUp <f d'>8 r8 \stemUp <fis dis'>4 ~ ~
    \stemUp <fis dis'>8 r8 | % 273
    \stemUp <e e'>8 r8 \stemDown <f f'>8 r8 \stemDown <fis fis'>8 r8
    \stemUp <e e'>8 r8 \pageBreak | % 274
    \stemUp <e e'>8 _ "Hn." r8 \stemUp <e e'>8 r8 \stemUp <e e'>8 r8 r4
    | % 275
    d1 -> _\fff ^ "a 2" | % 276
    cis1 -> | % 277
    d1 -> | % 278
    cis1 -> | % 279
    \stemUp d2 ^\markup{ \italic {marcato assai} } \stemUp cis2 |
    \barNumberCheck #280
    \stemUp d2 \stemUp cis2 \pageBreak | % 281
    \stemUp d2 _ "Hn." \stemUp cis2 | % 282
    \stemUp d2 \stemUp <cis e>8 r8 r4 | % 283
    \stemUp d'8 _\fff r8 \stemDown <cis e>8 r8 \stemDown <d fis>8 r8
    \stemDown <a e'>8 r8 | % 284
    \stemDown <g g'>8 r8 \stemDown <g g'>8 r16 \stemDown <g g'>16
    \stemUp <cis, cis'>2 | % 285
    \stemUp <a a'>8 r8 \stemUp <a a'>8 r8 \stemUp <a a'>8 r8 \stemUp <a
        a'>8 r8 | % 286
    \stemUp <g g''>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g g''>8 \stemUp <g g''>8 \stemUp <g g''>8 }
    \stemUp <d' d'>8 r8 r4 \pageBreak | % 287
    r4 _ "Hn." \stemUp <g a>8 r8 \stemUp <fis a>8 r8 \stemUp <e a>8 r8 | % 288
    \stemDown <g g'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g g'>8 \stemDown <g g'>8 \stemDown <g g'>8 }
    \stemDown <a fis'>8 r8 r4 | % 289
    \stemUp <d, d'>8 r8 r4 \stemDown <d d'>8 -! \stemDown <e e'>8 -!
    \stemDown <fis fis'>8 -! \stemDown <g g'>8 -! | \barNumberCheck #290
    \stemDown <g g'>8 r8 r4 \stemDown <b e>8 r8 r4 | % 291
    \stemUp <fis b>8 r8 \stemUp <fis b>8 r8 \stemUp <eis d'>8 r8 \stemUp
    <fis b>8 r8 \pageBreak | % 292
    \stemDown <fis fis'>4 _ "Hn." \once \omit TupletBracket
    \times 2/3  {
        \stemUp <b, b'>8 \stemUp <b b'>8 \stemUp <b b'>8 }
    \stemUp <cis cis'>8 \stemUp <cis cis'>8 r4 | % 293
    \stemUp d'8 r8 \stemDown <cis e>8 r8 \stemDown <d fis>8 r8 \stemDown
    <a e'>8 r8 | % 294
    \stemDown <g g'>8 r8 \stemDown <g g'>8 r16 \stemDown <g g'>16
    \stemUp <cis, cis'>2 | % 295
    \stemUp <a a'>8 r8 \stemUp <a a'>8 r8 \stemUp <a a'>8 r8 \stemUp <a
        a'>8 r8 | % 296
    \stemUp <g g''>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g g''>8 \stemUp <g g''>8 \stemUp <g g''>8 }
    \stemUp <d' d'>8 r8 r4 \pageBreak | % 297
    r4 _ "Hn." \stemUp <g a>8 r8 \stemUp <fis a>8 r8 \stemUp <e a>8 r8 | % 298
    \stemDown <g g'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g g'>8 \stemDown <g g'>8 \stemDown <g g'>8 }
    \stemDown <a fis'>8 r8 r4 | % 299
    \stemDown <f f'>8 r8 r4 \stemDown <a c>8 r8 r4 | \barNumberCheck
    #300
    \stemUp <f d'>8 r8 r4 \stemUp <d a'>8 r8 r4 | % 301
    R1 \pageBreak | % 302
    r2 _ "Hn." r4 \stemDown <b' fis'>8 _\fff r8 | % 303
    \stemDown <b fis'>8 r8 \stemDown <a fis'>8 r8 \stemDown <g e'>8 r8
    \stemUp <fis dis'>8 r8 | % 304
    \stemUp <e d'>4 ~ -> ~ _\sempre _\fff \stemUp <e d'>8 r8 \stemUp <e
        d'>4 ~ -> ~ \stemUp <e d'>8 r8 | % 305
    \stemUp <e d'>4 ~ -> ~ \stemUp <e d'>8 r8 \stemUp <e d'>4 ~ -> ~
    \stemUp <e d'>8 r8 | % 306
    \stemUp <e d'>4 ~ -> ~ \stemUp <e d'>8 r8 \stemUp <e d'>4 ~ -> ~
    \stemUp <e d'>8 r8 | % 307
    \stemUp <e d'>4 ~ -> ~ \stemUp <e d'>8 r8 \stemUp <e d'>4 ~ -> ~
    \stemUp <e d'>8 r8 \pageBreak | % 308
    \stemDown <fis fis'>4 ( -> _ "Hn." \stemUp <e e'>8 ) r8 \stemDown <g
        g'>4 ( -> \stemDown <fis fis'>8 ) r8 | % 309
    \stemDown <a e'>4 ( -> ~ \stemDown <g e'>8 ) r8 \stemDown <a e'>4 (
    -> ~ \stemDown <gis e'>8 ) r8 | \barNumberCheck #310
    \stemDown <g g'>4 ~ -> ~ \stemDown <g g'>8 r8 \stemDown <g g'>4 ~ ->
    ~ \stemDown <g g'>8 r8 | % 311
    \stemDown <g g'>4 ~ -> ~ \stemDown <g g'>8 r8 \stemDown <g g'>4 ~ ->
    ~ \stemDown <g g'>8 r8 | % 312
    \stemUp <d a'>4. _\ffff \stemUp <d a'>8 \stemUp <d bes'>4. \stemUp
    <d bes'>8 | % 313
    \stemUp <d b'>4. \stemUp <d b'>8 \stemUp <d bes'>4. \stemUp <d bes'>8
    \pageBreak | % 314
    \stemUp <d fis>2 _ "Hn." \stemDown <d' fis>4 \stemDown <a d>4 | % 315
    \stemDown <a cis>4 \stemUp e'4 \stemUp a,8 r8 r4 | % 316
    R1*2 _\markup{ \small\italic {cresc.} } | % 318
    <d, d'>1 ~ ~ _\p \startTrillSpan \stopTrillSpan _\mf _\markup{
        \small\italic {cresc.} } \startTrillSpan _\markup{ \small\italic
        {cresc.} } \startTrillSpan | % 319
    \stemUp <d d'>4 \stemUp <cis cis'>4 \stemUp <b b'>4 \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp <a a'>8 \stemUp <a a'>8 \stemUp <a a'>8 }
    \pageBreak | \barNumberCheck #320
    \stemUp fis'4 ( \stopTrillSpan \stopTrillSpan _\f _ "Hn." _\markup{
        \small\italic {cresc.} } \startTrillSpan \stemUp g4 \stemUp a4
    \stemUp ais4 ) | % 321
    \stemUp b4 ( \stemUp cis4 \stemUp d4 \stemUp e4 ) | % 322
    \stemUp d8 \stopTrillSpan _\ff _\markup{ \small\italic {cresc.} }
    \startTrillSpan r8 \stemUp a8 r16 \stemUp a16 \stemUp d8 r8 \stemUp
    a8 r8 | % 323
    \stemUp d8 \stemUp g8 ~ \stemUp g4 ~ \stemUp g8 r8 r4 | % 324
    \stemDown <cis, fis>8 \stopTrillSpan _\fff r8 \stemUp <d, d'>4 (
    \stemDown <fis fis'>8 ) r8 r4 \pageBreak | % 325
    r4 _ "Hn." \stemDown <g g'>4 ( \stemUp b8 ) r8 r4 | % 326
    r4 \stemDown <b e>4 ~ ~ \stemDown <b e>8 r8 \stemDown <bes f'>4 ~ ~
    | % 327
    \stemDown <bes f'>8 r8 \stemDown <fis fis'>4 ~ ~ \stemDown <fis
        fis'>8 r8 \stemUp <d d'>4 ~ ~ \pageBreak | % 328
    \stemUp <d d'>8 _ "Hn." r8 \stemUp <e e'>4 ~ ~ \stemUp <e e'>8 r8
    \stemUp <e e'>4 ~ ~ | % 329
    \stemUp <e e'>8 r8 \stemDown <g g'>4 ~ ~ \stemDown <g g'>8 r8
    \stemDown <g g'>8 r8 | \barNumberCheck #330
    \stemUp fis'8 _\sempre _\fff r8 \stemUp e8 r8 \stemDown <fis, fis'>8
    r8 \stemDown <g d'>8 r8 | % 331
    \stemDown <fis fis'>2 \stemDown <fis fis'>8 r8 \stemDown <a e'>8 r8
    \pageBreak | % 332
    \stemUp fis'8 _ "Hn." r8 \stemUp e8 r8 \stemDown <fis, fis'>8 r8
    \stemDown <g d'>8 r8 | % 333
    \stemDown <fis fis'>2 \stemDown <fis fis'>8 r8 \stemDown <a e'>8 r8
    | % 334
    \stemDown <a fis'>8 r8 \stemDown <a e'>8 r8 \stemDown <fis fis'>8 r8
    \stemDown <g g'>8 r8 | % 335
    \stemDown <a fis'>8 r8 \stemDown <a e'>8 r8 \stemDown <fis fis'>8 r8
    \stemDown <g g'>8 r8 \pageBreak | % 336
    \stemDown <a fis'>8 _ "Hn." r8 \stemDown <g g'>8 r8 \stemDown <a
        fis'>8 r8 \stemDown <g g'>8 r8 | % 337
    \stemDown <a fis'>8 r8 \stemDown <g g'>8 r8 \stemDown <a fis'>8 r8
    \stemDown <g g'>8 r8 | % 338
    \stemDown <a fis'>8 r8 r8 \stemDown <d fis>8 \stemDown <d fis>8 r8 r8
    \stemUp fis8 | % 339
    \stemUp fis8 r8 r8 \stemUp fis,8 \stemUp fis8 r8 r8 \stemUp a8 |
    \barNumberCheck #340
    \stemUp a8 r8 r4 \stemUp e'8 r8 r4 \pageBreak | % 341
    \stemDown <a, fis'>8 _ "Hn." r8 r4 \stemDown <cis e>8 r8 r4 | % 342
    \stemDown <a fis'>8 r8 \stemDown <a fis'>8 r8 r4 \stemDown <a fis'>8
    r8 | % 343
    r4 \stemDown <a fis'>8 r8 r4 \stemDown <a fis'>8 r8 | % 344
    \stemDown <a fis'>8 r8 \stemUp <d, a'>8 r8 \stemUp <d a'>8 r8
    \stemUp <d a'>8 r8 | % 345
    \clef "bass" <d, d'>1 ~ ~ | % 346
    \stemDown <d d'>2. \once \omit TupletBracket
    \times 2/3  {
        \stemDown <d d'>8 \stemDown <d d'>8 \stemDown <d d'>8 }
    | % 347
    \stemDown <d d'>8 r8 r4 r2 \bar "|."
    }

PartPEightVoiceTwo =  \relative a {
    \clef "treble" \time 4/4 \key c \none \transposition f s1*4
    \pageBreak s1*3 \bar "||"
    s1*2 \pageBreak s1*5 \break s1*5 \pageBreak s1*4 \break s1*4
    \pageBreak s1*3 | % 31
    \time 12/8  s1. \pageBreak s1*49/24 r4.*2/3 \stemDown a8 -. _\mf
    \stemDown b8 -. \stemDown c8 -. s1*1/3 | % 34
    \stemDown cis8 -. r8*2/3 r8*2/3 r4.*2/3 r4.*2/3 \stemDown a8 -. _\mp
    \stemDown b8 -. \stemDown c8 -. s1*1/3 | % 35
    \stemDown cis8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 \pageBreak
    s2*15 \pageBreak s2*15 \pageBreak s2*15 \pageBreak s1*3 | % 53
    \numericTimeSignature\time 4/4  r2 \stemDown cis4 _> _\pp \stemDown
    cis8 r16 \stemDown cis16 | % 54
    \stemDown fis,8 r8 r4 r2 | % 55
    R1 \pageBreak | % 56
    R1 | % 57
    r2 \stemDown cis'4 _> \stemDown cis8 r16 \stemDown cis16 | % 58
    \stemDown fis,8 r8 r4 r2 | % 59
    R1*2 \pageBreak | % 61
    R1*4 s1 \pageBreak s1*5 \bar "||"
    \pageBreak | % 71
    \key c \none s1 | % 72
    r2 r4 s4*13 \break s2 r2 s1*4 \pageBreak | % 81
    r4 s4*13 \stemDown b4 ( \stemDown b'8 ) s8*9 \pageBreak s1*4
    \pageBreak s1*2 | % 92
    \stemDown cis,4 \stemDown gis'4 \stemDown b,4 \stemDown c4 | % 93
    \stemDown cis8 s8*23 \pageBreak s4 \stemDown ais'8 r16 \stemDown ais16
    \stemDown b8 s8*43 \break s1*5 \pageBreak s1*4 | % 111
    r2 \stemDown dis,8 _\f r8 \stemDown dis8 r8 | % 112
    \stemDown e8 r8 \stemDown e8 r8 r2 \break s1 | % 114
    r2 r4 s4*13 \pageBreak s2 r2 s1*4 \break | % 123
    r4 s4*13 \stemDown b4 ( \stemDown b'8 ) s8*9 \pageBreak s1*4
    \pageBreak s1*4 \pageBreak s1 | % 137
    \time 12/8  s1*8/3 \bar "||"
    s1*1/3 | % 139
    \key c \none s1. \pageBreak s1*3 | % 142
    \numericTimeSignature\time 4/4  s1*3 \pageBreak s1*5 \pageBreak s1*3
    | % 153
    \stemDown e,8 -. r8 \stemDown b8 -. r16 \stemDown b16 -. \stemDown e8
    -. r8 \stemDown b8 -. r8 | % 154
    \stemDown e16 -. r16 \stemDown a8 ~ \stemDown a4 ~ \stemDown a8 _\!
    _\pp r8 r4 \pageBreak s1*4 \break s1*4 \pageBreak s1*4 \pageBreak
    s1*2 | % 169
    \time 12/8  s1*3 \pageBreak s1*13/24 r4.*2/3 \stemDown a,8 -. _\mf
    \stemDown b8 -. \stemDown c8 -. s1*1/3 | % 172
    \stemDown cis8 -. r8*2/3 r8*2/3 r4.*2/3 r4.*2/3 \stemDown a8 -. _\mp
    \stemDown b8 -. \stemDown c8 -. s1*1/3 | % 173
    \stemDown cis8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*47/24 \pageBreak
    s2*15 \pageBreak s1*6 \pageBreak s2*15 \pageBreak s1*6 | % 193
    \numericTimeSignature\time 4/4  s1 \pageBreak s1*3 | % 197
    \stemDown e8 r8 \stemDown b8 r16 \stemDown b16 \stemDown e8 r8
    \stemDown b8 r8 | % 198
    \stemDown e8 -> \stemDown a8 -> r4 r2 s1 | \barNumberCheck #200
    a1 \pageBreak | % 201
    b1 | % 202
    \stemDown fis8 r8 \stemDown cis8 r16 \stemDown cis16 \stemDown fis8
    r8 \stemDown cis8 r8 | % 203
    \stemDown fis8 -> \stemDown b8 -> r4 r2 s1*2 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*4 \pageBreak | % 225
     \once \override NoteHead.style = ##f a1 s1*2 \pageBreak s1 | % 229
    \stemDown d8 s8*31 \pageBreak s1*5 \pageBreak s1 | % 239
    \stemDown d8 s8*31 \pageBreak s1*5 \pageBreak s1*6 \pageBreak s1*3 | % 257
    R1*2 \pageBreak s1*2 | % 261
    r2 r4 \stemDown b4 ~ _\ff | % 262
    \stemDown b4 \stemDown g4 ( \stemDown e4 \stemDown cis8 ) r8 s1
    \pageBreak s1 | % 265
    R1*2 s1*2 \pageBreak s1*5 \pageBreak s1*7 \pageBreak s1*2 | % 283
    \stemDown d'8 s8*31 \pageBreak s1*5 \pageBreak s1 | % 293
    \stemDown d8 s8*31 \pageBreak s1*5 \pageBreak s1*6 \pageBreak s1*6
    \pageBreak s4*5 \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 }
    \stemDown a8 s4. | % 316
    d,1 ~ | % 317
    \stemDown d4 \stemDown cis4 \stemDown b4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 }
    s1*2 \pageBreak | \barNumberCheck #320
    d1 ~ | % 321
    \stemDown d4 \stemDown cis4 \stemDown b4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 }
    | % 322
    \stemDown d8 s8 \stemDown a'8 s16 \stemDown a16 \stemDown d,8 s8
    \stemDown a'8 s8 | % 323
    \stemDown d8 \stemDown g8 ~ \stemDown g4 ~ \stemDown g8 s8*11
    \pageBreak s2 \stemDown b,8 s8*19 \pageBreak s1*2 | \barNumberCheck
    #330
    \stemDown a8 s8 \stemDown a8 r16 \stemDown a16 s1. \pageBreak | % 332
    \stemDown a8 s8 \stemDown a8 r16 \stemDown a16 s2*7 \pageBreak s8*23
    \stemDown a8 | % 339
    \stemDown a8 \stemDown cis8 \stemDown b8 \stemDown bes8 \stemDown a8
    \stemDown g8 \stemDown fis8 \stemDown e8 | \barNumberCheck #340
    \stemDown d8 s4. \stemDown cis'8 s4. \pageBreak s1*4 | % 345
    \clef "bass" s1*3 \bar "|."
    }

PartPNineVoiceOne =  \relative e' {
    \clef "treble" \time 4/4 \key c \none \transposition f | % 1
    R1*4 \pageBreak | % 5
    R1*3 \bar "||"
    R1*2 \pageBreak | \barNumberCheck #10
    R1*5 \break | % 15
    R1*5 \pageBreak | \barNumberCheck #20
    R1*4 \break | % 24
    R1*4 \pageBreak | % 28
    R1 | % 29
    \stemUp <e e'>8 -. _\mp _\markup{ \small\italic {un poco cresc.} }
    \startTrillSpan r8 \stemDown <fis fis'>8 -. r16 \stemDown <fis fis'>16
    -. \stemUp <e e'>8 -. r8 \stemUp <d d'>8 -. r8 | \barNumberCheck #30
    \stemUp <cis cis'>8 -. r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <b b'>8 -. _\< \stemUp <a a'>8 -. \stemUp <b b'>8 -. }
    \stemUp <cis cis'>8 -. r8 \stemUp <b b'>8 -. r8 | % 31
    \stemUp <a a'>8 -. \stopTrillSpan _\! _\mf r8 r4 r2 \pageBreak | % 32
    R1 | % 33
    \time 12/8  r2.*2/3 r4.*2/3 \clef "bass" r4.*2/3 _\mf s2 | % 34
    r1 s2 | % 35
    r1 s2 \pageBreak | % 36
    \clef "treble" r1 s2 | % 37
    r1 s2 | % 38
    r1 s2 | % 39
    r1 s2 | \barNumberCheck #40
    r1 s2 \pageBreak | % 41
    r1 s2 | % 42
    r1 s2 | % 43
    r1 s2 | % 44
    r1 s2 | % 45
    r1 s2 \pageBreak | % 46
    r1 s2 | % 47
    r1 s2 | % 48
    r1 s2 | % 49
    r1 s2 | \barNumberCheck #50
    \stemDown <fis' fis'>4. _\ff \stemUp <eis eis'>4. \stemUp <dis dis'>4.
    \stemUp <cis cis'>4 ( ~ ~ \stemUp <cis cis'>16 \stemUp <b b'>16
    \pageBreak | % 51
    \stemUp <ais ais'>8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 52
    r1 s2 | % 53
    \numericTimeSignature\time 4/4  R1 | % 54
    r2 \stemUp cis'4 _> ^\p \stemUp cis8 r16 \stemUp cis16 | % 55
    \stemUp fis,8 r8 r4 r2 \pageBreak | % 56
    r2 \stemUp cis'4 -> ^\f \stemUp cis8 r16 \stemUp cis16 | % 57
    \stemUp cis,8 ^\pp r8 r4 r2 _\pp | % 58
    r2 \stemUp cis'4 _> ^\p \stemUp cis8 r16 \stemUp cis16 | % 59
    \stemUp fis,8 r8 r4 r2 | \barNumberCheck #60
    r2 \stemUp cis'4 -> ^\f \stemUp cis8 r16 \stemUp cis16 \pageBreak | % 61
    fis1 -> ^\p ^\markup{ \small\italic {cresc.} } \startTrillSpan | % 62
    d1 | % 63
    fis1 | % 64
    d1 | % 65
    fis1 \stopTrillSpan _\mf _\markup{ \small\italic {cresc.} }
    \startTrillSpan \pageBreak | % 66
    g1 -> | % 67
    <ais, e'>1 -> \stopTrillSpan _\f _\< | % 68
    <d fis>1 -> | % 69
    \stemUp <cis, ais'>8 _\! _\ff r8 r4 r2 | \barNumberCheck #70
    R1 \bar "||"
    \pageBreak | % 71
    \key c \none \stemUp fis8 _\pp -\markup{ \italic {leggieramente} } r8
    \stemUp <e fis>8 r16 \stemUp <e fis>16 \stemUp <dis fis>8 r8 \stemUp
    <cis fis>8 r8 | % 72
    \stemUp <b e>8 r8 \stemUp <b e>8 r16 \stemUp <b e>16 \stemUp <cis e>8
    r8 r4 | % 73
    R1 | % 74
    r4 \stemUp <b e>8 _\pp r16 \stemUp <b e>16 \stemUp dis4 ( \stemUp
    fis8 ) r8 | % 75
    R1 \break | % 76
    r4 \stemUp <b, e>8 _\pp r16 \stemUp <b e>16 \stemUp <b dis>8 r8
    \stemUp <b fis'>8 r8 | % 77
    \stemUp <b b'>8 _\p r8 r4 \stemUp <b gis'>8 r8 r4 | % 78
    R1 | % 79
    r2 \stemDown <gis' d'>8 _\mp _\< r8 \stemDown <gis dis'>8 r8 |
    \barNumberCheck #80
    \stemUp <dis gis>4 ~ ~ _\! _\mf _\< \stemUp <dis gis>8 \stemUp <dis
        gis>16 \stemUp <dis gis>16 \stemUp <dis ais'>8 _\! _\f \stemUp
    <cis ais'>8 r4 \pageBreak | % 81
    \stemUp fis8 ^\pp r8 \stemUp <e fis>8 _\pp r16 \stemUp <e fis>16
    \stemUp <dis fis>8 r8 \stemUp <cis fis>8 r8 | % 82
    \stemUp <b e>8 r8 \stemUp <b e>8 r16 \stemUp <b e>16 \stemUp <cis e>8
    r8 \stemUp <fis ais>8 r16 \stemUp <fis ais>16 | % 83
    \stemUp <fis b>8 _\markup{ \small\italic {un poco cresc.} }
    \startTrillSpan r8 \stemUp <e fis>8 r16 \stemUp <e fis>16 \stemUp
    <dis fis>8 r8 \stemUp <cis fis>8 r8 | % 84
    \stemUp <b e>8 r8 \stemUp <b e>8 r16 \stemUp <b e>16 \stemUp dis4 (
    \stemUp fis8 ) r8 | % 85
    \stemUp <eis b'>8 r8 \stemUp <e fis>8 r16 \stemUp <e fis>16 \stemUp
    <dis fis>8 r8 \stemUp <cis fis>8 r8 \pageBreak | % 86
    \stemUp <b e>8 r8 \stemUp <b e>8 r16 \stemUp <b e>16 \stemUp <b dis>8
    r8 r4 | % 87
    \stemUp <d g>8 \stopTrillSpan _\mf _\< r8 r4 \stemUp <a fis'>8 r8 r4
    | % 88
    \stemUp <d d'>8 r8 r4 \stemUp <fis b>8 r8 r4 _\! _\f | % 89
    \stemUp <dis dis'>8 _\f \stemUp <dis dis'>16 \stemUp <dis dis'>16
    \stemUp <dis dis'>4 ~ ~ \stemUp <dis dis'>8 \stemUp <dis dis'>16
    \stemUp <dis dis'>16 \stemUp <dis dis'>4 ~ ~ \pageBreak |
    \barNumberCheck #90
    \stemUp <dis dis'>8 \stemUp <dis dis'>16 \stemUp <dis dis'>16
    \stemUp <dis dis'>4 ~ ~ \stemUp <dis dis'>8 \stemUp <dis dis'>16
    \stemUp <dis dis'>16 \stemUp <dis dis'>4 | % 91
    \stemUp <dis dis'>4 _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemUp <dis dis'>4 \stemUp <e cis'>4 \stemUp <c
        gis'>4 | % 92
    \stemUp gis'4 \stemUp d4 \stemUp dis4 \stemUp dis4 | % 93
    \stemUp cis8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e cis'>8 \stopTrillSpan _\ff \stemUp <e cis'>8 \stemUp
        <e cis'>8 }
    \stemUp <e cis'>2 ~ ~ | % 94
    \stemUp <e cis'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <es bes'>8 \stemUp <es bes'>8 \stemUp <es bes'>8 }
    \stemUp <es bes'>2 ~ ~ | % 95
    \stemUp <es bes'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <es b'>8 \stemUp <es b'>8 \stemUp <es b'>8 }
    \stemUp <es b'>2 ~ ~ \pageBreak | % 96
    \stemUp <es b'>8 r8 \stemUp <e cis'>8 r8 \stemUp <dis fis>8 r8 r4 | % 97
    R1*5 \break | % 102
    R1*5 \pageBreak | % 107
    R1*6 \break | % 113
    \stemUp fis8 _\pp r8 \stemUp <e fis>8 r16 \stemUp <e fis>16 \stemUp
    <dis fis>8 r8 \stemUp <cis fis>8 r8 | % 114
    \stemUp <b e>8 r8 \stemUp <b e>8 r16 \stemUp <b e>16 \stemUp <cis e>8
    r8 r4 | % 115
    R1 | % 116
    r4 \stemUp <b e>8 _\pp r16 \stemUp <b e>16 \stemUp dis4 ( \stemUp
    fis8 ) r8 | % 117
    R1 \pageBreak | % 118
    r4 \stemUp <b, e>8 _\pp r16 \stemUp <b e>16 \stemUp <b dis>8 r8
    \stemUp <b fis'>8 r8 | % 119
    \stemUp <b b'>8 _\p r8 r4 \stemUp <b gis'>8 r8 r4 | \barNumberCheck
    #120
    R1 | % 121
    r2 \stemDown <gis' d'>8 _\mp _\< r8 \stemDown <gis dis'>8 r8 | % 122
    \stemUp <dis gis>4 ~ ~ _\! _\mf _\< \stemUp <dis gis>8 \stemUp <dis
        gis>16 \stemUp <dis gis>16 \stemUp <dis ais'>8 _\! _\f \stemUp
    <cis ais'>8 r4 \break | % 123
    \stemUp fis8 ^\pp r8 \stemUp <e fis>8 _\pp r16 \stemUp <e fis>16
    \stemUp <dis fis>8 r8 \stemUp <cis fis>8 r8 | % 124
    \stemUp <b e>8 r8 \stemUp <b e>8 r16 \stemUp <b e>16 \stemUp <cis e>8
    r8 \stemUp <fis ais>8 r16 \stemUp <fis ais>16 | % 125
    \stemUp <fis b>8 _\markup{ \small\italic {un poco cresc.} }
    \startTrillSpan r8 \stemUp <e fis>8 r16 \stemUp <e fis>16 \stemUp
    <dis fis>8 r8 \stemUp <cis fis>8 r8 | % 126
    \stemUp <b e>8 r8 \stemUp <b e>8 r16 \stemUp <b e>16 \stemUp dis4 (
    \stemUp fis8 ) r8 | % 127
    \stemUp <eis b'>8 r8 \stemUp <e fis>8 r16 \stemUp <e fis>16 \stemUp
    <dis fis>8 r8 \stemUp <cis fis>8 r8 \pageBreak | % 128
    \stemUp <b e>8 r8 \stemUp <b e>8 r16 \stemUp <b e>16 \stemUp <b dis>8
    r8 r4 | % 129
    \stemUp <g d''>8 \stopTrillSpan _\f r8 r4 \stemUp <a fis'>8 r8 r4 |
    \barNumberCheck #130
    \stemUp <d d'>8 r8 r4 \stemUp <fis d'>8 r8 r4 | % 131
    r2 \stemDown <fis fis'>8 r8 \stemUp <d d'>4 ~ ~ \pageBreak | % 132
    \stemUp <d d'>4 \stemDown <g g'>4 \stemUp <d a'>8 r8 r4 | % 133
    \stemUp <g, d''>8 r8 r4 \stemUp <a fis'>8 r8 r4 | % 134
    \stemUp <d d'>8 r8 r4 \stemUp <fis d'>8 r8 r4 | % 135
    r2 \stemDown <fis fis'>8 r8 \stemUp <d d'>4 ~ ~ \pageBreak | % 136
    \stemUp <d d'>4 \stemDown <g g'>4 \stemUp <d a'>8 r8 r4 | % 137
    \time 12/8  r2.*2/3 \stemUp <b g'>4. _\f \stemUp <d a'>8 r8*2/3 r8*2/3
    s1*1/3 | % 138
    r2.*2/3 \stemUp <b g'>4. -> _\mf \stemUp <d a'>8 r4*2/3 \bar "||"
    s1*1/3 | % 139
    \key c \none r1 s2 \pageBreak | \barNumberCheck #140
    r1 s2 | % 141
    r1 s2 | % 142
    r1 s2 | % 143
    r1 s2 | % 144
    r1 s2 \pageBreak | % 145
    r1 s2 | % 146
    r1 s2 | % 147
    r1 s2 | % 148
    r1 s2 | % 149
    r1 s2 \pageBreak | \barNumberCheck #150
    r1 s2 | % 151
    r1 s2 | % 152
    r1 s2 | % 153
    r1 s2 | % 154
    r1 s2 \pageBreak | % 155
    r1 s2 | % 156
    r1 s2 | % 157
    r1 s2 | % 158
    r1 s2 \break | % 159
    r1 s2 | \barNumberCheck #160
    r1 s2 | % 161
    r1 s2 | % 162
    r1 s2 \pageBreak | % 163
    r1 s2 | % 164
    r1 s2 | % 165
    r1 s2 | % 166
    r1 s2 \pageBreak | % 167
    \numericTimeSignature\time 4/4  \stemUp <e e'>8 -. _\mp _\markup{
        \small\italic {un poco cresc.} } \startTrillSpan r8 \stemDown
    <fis fis'>8 -. r16 \stemDown <fis fis'>16 -. \stemUp <e e'>8 -. r8
    \stemUp <d d'>8 -. r8 | % 168
    \stemUp <cis cis'>8 -. r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <b b'>8 -. _\< \stemUp <a a'>8 -. \stemUp <b b'>8 -. }
    \stemUp <cis cis'>8 -. r8 \stemUp <b b'>8 -. r8 | % 169
    \stemUp <a a'>8 -. \stopTrillSpan _\! _\mf r8 r4 r2 |
    \barNumberCheck #170
    R1 \pageBreak | % 171
    \time 12/8  r2.*2/3 r2.*2/3 \clef "bass" s2 | % 172
    r1 s2 | % 173
    r1 s2 | % 174
    r1 s2 \pageBreak | % 175
    \clef "treble" r1 s2 | % 176
    r1 s2 | % 177
    r1 s2 | % 178
    r1 s2 | % 179
    r1 s2 \pageBreak | \barNumberCheck #180
    r1 s2 | % 181
    r1 s2 | % 182
    r1 s2 | % 183
    r1 s2 \pageBreak | % 184
    r1 _ "Hn." s2 | % 185
    r1 s2 | % 186
    r2.*2/3 r4.*2/3 \stemUp <f f'>8 _\f \stemUp <f f'>8 \stemUp <f f'>8
    s4. | % 187
    \stemUp <f f'>2. ~ ~ _\> \stemUp <f f'>8 r8*2/3 _\! r8*2/3 r4.*2/3
    s1*5/24 | % 188
    r1 s2 \pageBreak | % 189
    r1 s2 | \barNumberCheck #190
    r1 s2 | % 191
    r1 s2 | % 192
    r1 s2 | % 193
    \numericTimeSignature\time 4/4  \stemUp <e' a>4 _\ff \stemDown <cis'
        e>8 \stemDown <a cis>8 \stemUp <e a>4 \stemDown <cis' e>4
    \pageBreak | % 194
    \stemDown <a cis>4 \stemUp <cis, e>4 \stemUp <b b'>8 r8 r4 | % 195
    R1*2 | % 197
    R1*3 | \barNumberCheck #200
    \stemUp a'8 _\pp _\ leggieramente ^\leggieramente _\pp r8 \stemUp e8
    r16 \stemUp e16 \stemUp a8 r8 \stemUp e8 r8 \pageBreak | % 201
    \stemUp b'8 -> _\< \stemUp e8 -> r4 r2 | % 202
    \stemUp fis,8 _\! ^\p _\p r8 \stemUp cis8 r16 \stemUp cis16 \stemUp
    fis8 r8 \stemUp cis8 r8 | % 203
    \stemUp fis8 -> \stemUp b8 -> r4 r2 | % 204
    <e,, e'>1 _\p _\markup{ \small\italic {poco a poco cresc.} }
    \startTrillSpan | % 205
    <a a'>1 \pageBreak | % 206
    <fis fis'>1 | % 207
    <b b'>1 | % 208
    <d d'>1 | % 209
    <e e'>1 | \barNumberCheck #210
    <fis fis'>1 \stopTrillSpan _\f _\markup{ \small\italic {cresc.} }
    \startTrillSpan \pageBreak | % 211
    <b, b'>1 | % 212
    \stemUp <a a'>2 \stopTrillSpan _\ff \stemUp <b b'>2 | % 213
    \stemUp <c c'>2 \stemUp <cis cis'>8 r8 r4 | % 214
    \stemUp <g' b>8 _\ff r8 \stemUp <e g>8 r16 \stemUp <e g>16 \stemUp
    <g b>8 r8 \stemUp <e g>8 r8 | % 215
    \stemDown <g cis>8 -> \stemDown <cis e>8 ~ -> ~ \stemDown <cis e>2.
    \pageBreak | % 216
    \stemUp <g b>8 _\fff r8 \stemUp <e g>8 r16 \stemUp <e g>16 \stemUp
    <g b>8 r8 \stemUp <e g>8 r8 | % 217
    \stemDown <g cis>8 -> \stemDown <cis e>8 ~ -> ~ \stemDown <cis e>8
    \stemDown <cis e>8 \stemUp <g b>8 \stemUp <e g>4 \stemUp <e g>8 | % 218
    \stemUp <g cis>8 \stemDown <cis e>4 \stemDown <cis e>8 \stemUp <g b>8
    \stemUp <e g>4 \stemUp <e g>8 | % 219
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g cis>8 \stemUp <g cis>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <cis e>8 \stemDown <cis e>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g b>8 \stemUp <g b>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e g>8 \stemUp <e g>8 r8 }
    | \barNumberCheck #220
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g cis>8 \stemUp <g cis>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <cis e>8 \stemDown <cis e>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g b>8 \stemUp <g b>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e g>8 \stemUp <e g>8 r8 }
    \pageBreak | % 221
    \times 2/3  {
        \stemUp <g cis>8 -> \stemUp <g cis>8 -> r8 }
    r4 r2 | % 222
    R1*3 \pageBreak | % 225
    R1*3 \pageBreak | % 228
    R1 | % 229
    \stemDown <a d>8 _\fff r8 \stemDown <g e'>8 r8 \stemDown <fis fis'>8
    r8 \stemUp <e e'>8 r8 | \barNumberCheck #230
    \stemUp <d d'>8 r8 \stemUp <d d'>8 r16 \stemUp <d d'>16 \stemUp <a
        a'>2 | % 231
    \stemUp <a d>8 r8 \stemUp <a g'>8 r8 \stemUp <a fis'>8 r8 \stemUp <a
        e'>8 r8 | % 232
    \stemUp <g g'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g g'>8 \stemUp <g g'>8 \stemUp <g g'>8 }
    \stemUp <a fis'>8 r8 r4 \pageBreak | % 233
    r4 \stemUp <g' a>8 r8 \stemUp <fis a>8 r8 \stemUp <e a>8 r8 | % 234
    \stemUp <d d'>2 \stemUp <fis d'>8 r8 r4 | % 235
    \stemUp a8 r8 r4 \stemDown <d, d'>8 -! \stemDown <e e'>8 -!
    \stemDown <fis fis'>8 -! \stemDown <g g'>8 -! | % 236
    \stemDown <g g'>8 r8 r4 \stemDown <b e>8 r8 r4 | % 237
    \stemUp <fis b>8 r8 \stemUp <fis b>8 r8 \stemUp <eis d'>8 r8 \stemUp
    <fis b>8 r8 \pageBreak | % 238
    \stemUp b4 -> \once \omit TupletBracket
    \times 2/3  {
        \stemUp <b, fis'>8 \stemUp <b fis'>8 \stemUp <b fis'>8 }
    \stemUp <cis bes'>8 \stemUp <cis a'>8 r4 | % 239
    \stemDown <a' d>8 r8 \stemDown <g e'>8 r8 \stemDown <fis fis'>8 r8
    \stemUp <e e'>8 r8 | \barNumberCheck #240
    \stemUp <d d'>8 r8 \stemUp <d d'>8 r16 \stemUp <d d'>16 \stemUp <a
        a'>2 | % 241
    \stemUp <a d>8 r8 \stemUp <a g'>8 r8 \stemUp <a fis'>8 r8 \stemUp <a
        e'>8 r8 | % 242
    \stemUp <g g'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g g'>8 \stemUp <g g'>8 \stemUp <g g'>8 }
    \stemUp <a fis'>8 r8 r4 \pageBreak | % 243
    r4 \stemUp <g' a>8 r8 \stemUp <fis a>8 r8 \stemUp <e a>8 r8 | % 244
    \stemUp <d d'>2 \stemUp <fis d'>8 r8 r4 | % 245
    \stemUp <bes, bes'>8 r8 r4 \stemUp <c c'>8 r8 r4 | % 246
    \stemUp <d d'>8 r8 r4 \stemUp <d a'>8 r8 r4 | % 247
    \stemDown <fis fis'>2 ~ ~ \stemDown <fis fis'>8 \stemDown <fis fis'>16
    \stemDown <fis fis'>16 \stemDown <fis fis'>4 ~ ~ \pageBreak | % 248
    \stemDown <fis fis'>2 ~ ~ \stemDown <fis fis'>8 \stemDown <fis fis'>16
    \stemDown <fis fis'>16 \stemUp <fis ais>8 r8 | % 249
    \stemUp <fis b>8 r8 \stemUp <fis b>8 r8 \stemUp <e b'>8 r8 \stemUp
    <dis b'>8 r8 | \barNumberCheck #250
    \stemUp <e b'>8 r8 \stemUp <d b'>8 r8 \stemUp <d d'>8 r8 \stemUp
    <dis dis'>8 r8 | % 251
    \stemUp <e e'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <c g'>8 \stemUp <c g'>8 \stemUp <c g'>8 }
    \stemUp <c g'>2 ~ ~ | % 252
    \stemUp <c g'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <cis cis'>8 \stemUp <cis cis'>8 \stemUp <cis cis'>8 }
    \stemUp <cis cis'>2 ~ ~ | % 253
    \stemUp <cis cis'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d c'>8 \stemUp <d c'>8 \stemUp <d c'>8 }
    \stemUp <d c'>2 ~ ~ \pageBreak | % 254
    \stemUp <d c'>8 r8 \stemUp cis'8 r16 \stemUp cis16 \stemUp d8 r8 r4
    | % 255
    \stemUp a2 _\fff \stemUp <g b>2 | % 256
    \stemUp <fis ais>8 r8 \stemUp <e b'>8 r8 \clef "bass" \stemDown <a,,
        a'>2 ~ ~ _\f | % 257
    <a a'>1 ~ ~ _\< | % 258
    \stemDown <a a'>2. ~ ~ _\! _\ff _\> \stemDown <a a'>8 _\! r8
    \pageBreak | % 259
    \clef "treble" \stemUp a''2 _\fff \stemUp <g b>2 | \barNumberCheck
    #260
    \stemUp <fis ais>8 r8 \stemUp <e b'>8 r8 r2 | % 261
    R1*2 | % 263
    \stemUp a2 _\fff \stemUp <g b>2 \pageBreak | % 264
    \stemUp <fis ais>8 r8 \stemUp <e b'>8 r8 \clef "bass" \stemDown <a,,
        a'>2 ~ ~ _\f | % 265
    <a a'>1 ~ ~ _\< | % 266
    \stemDown <a a'>2. ~ ~ _\! _\ff _\> \stemDown <a a'>8 _\! r8 | % 267
    \clef "treble" \stemUp a''4 ~ _\fff \stemUp a8 r8 \stemUp <g b>4 ~ ~
    \stemUp <g b>8 r8 | % 268
    \stemUp <fis ais>4 ~ ~ \stemUp <fis ais>8 r8 \stemUp <g b>4 ~ ~
    \stemUp <g b>8 r8 \pageBreak | % 269
    \stemUp <e b'>4 ~ ~ \stemUp <e b'>8 r8 \stemUp <fis a>4 ~ ~ \stemUp
    <fis a>8 r8 | \barNumberCheck #270
    \stemDown <fis fis'>4 ~ ~ \stemDown <fis fis'>8 r8 \stemDown <fis
        fis'>4 ~ ~ \stemDown <fis fis'>8 r8 | % 271
    \stemDown <g g'>4 ~ ~ \stemDown <g g'>8 r8 \stemUp <e e'>4 ~ ~
    \stemUp <e e'>8 r8 | % 272
    \stemUp <f d'>4 ~ ~ \stemUp <f d'>8 r8 \stemUp <fis dis'>4 ~ ~
    \stemUp <fis dis'>8 r8 | % 273
    \stemUp <e e'>8 r8 \stemDown <f f'>8 r8 \stemDown <fis fis'>8 r8
    \stemUp <c c'>8 r8 \pageBreak | % 274
    \stemUp <d d'>8 r8 \stemUp <cis cis'>8 r8 \stemUp <d d'>8 r8 r4 | % 275
    d1 -> _\fff ^ "a 2" | % 276
    cis1 -> | % 277
    d1 -> | % 278
    cis1 -> | % 279
    \stemUp d2 ^\markup{ \italic {marcato assai} } \stemUp cis2 |
    \barNumberCheck #280
    \stemUp d2 \stemUp cis2 \pageBreak | % 281
    \stemUp d2 \stemUp cis2 | % 282
    \stemUp d2 \stemUp cis8 r8 r4 | % 283
    \stemDown <a' d>8 _\fff r8 \stemDown <g e'>8 r8 \stemDown <fis fis'>8
    r8 \stemUp <e e'>8 r8 | % 284
    \stemUp <d d'>8 r8 \stemUp <d d'>8 r16 \stemUp <d d'>16 \stemUp <a
        a'>2 | % 285
    \stemUp <a d>8 r8 \stemUp <a g'>8 r8 \stemUp <a fis'>8 r8 \stemUp <a
        e'>8 r8 | % 286
    \stemUp <g g'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g g'>8 \stemUp <g g'>8 \stemUp <g g'>8 }
    \stemUp <a fis'>8 r8 r4 \pageBreak | % 287
    r4 \stemUp <g' a>8 r8 \stemUp <fis a>8 r8 \stemUp <e a>8 r8 | % 288
    \stemUp <d d'>2 \stemUp <fis d'>8 r8 r4 | % 289
    \stemUp a8 r8 r4 \stemDown <d, d'>8 -! \stemDown <e e'>8 -!
    \stemDown <fis fis'>8 -! \stemDown <g g'>8 -! | \barNumberCheck #290
    \stemDown <g g'>8 r8 r4 \stemDown <b e>8 r8 r4 | % 291
    \stemUp <fis b>8 r8 \stemUp <fis b>8 r8 \stemUp <eis d'>8 r8 \stemUp
    <fis b>8 r8 \pageBreak | % 292
    \stemUp b4 -> \once \omit TupletBracket
    \times 2/3  {
        \stemUp <b, fis'>8 \stemUp <b fis'>8 \stemUp <b fis'>8 }
    \stemUp <cis bes'>8 \stemUp <cis a'>8 r4 | % 293
    \stemDown <a' d>8 r8 \stemDown <g e'>8 r8 \stemDown <fis fis'>8 r8
    \stemUp <e e'>8 r8 | % 294
    \stemUp <d d'>8 r8 \stemUp <d d'>8 r16 \stemUp <d d'>16 \stemUp <a
        a'>2 | % 295
    \stemUp <a d>8 r8 \stemUp <a g'>8 r8 \stemUp <a fis'>8 r8 \stemUp <a
        e'>8 r8 | % 296
    \stemUp <g g'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <g g'>8 \stemUp <g g'>8 \stemUp <g g'>8 }
    \stemUp <a fis'>8 r8 r4 \pageBreak | % 297
    r4 \stemUp <g' a>8 r8 \stemUp <fis a>8 r8 \stemUp <e a>8 r8 | % 298
    \stemUp <d d'>2 \stemUp <fis d'>8 r8 r4 | % 299
    \stemUp <bes, bes'>8 r8 r4 \stemUp <c c'>8 r8 r4 | \barNumberCheck
    #300
    \stemUp <d d'>8 r8 r4 \stemUp <d a'>8 r8 r4 | % 301
    \stemDown <fis fis'>2 ~ ~ \stemDown <fis fis'>8 \stemDown <fis fis'>16
    \stemDown <fis fis'>16 \stemDown <fis fis'>4 ~ ~ \pageBreak | % 302
    \stemDown <fis fis'>2 ~ ~ \stemDown <fis fis'>8 \stemDown <fis fis'>16
    \stemDown <fis fis'>16 \stemUp <fis ais>8 r8 | % 303
    \stemUp <fis b>8 r8 \stemUp <fis b>8 r8 \stemUp <e b'>8 r8 \stemUp
    <dis b'>8 r8 | % 304
    \stemUp <e d'>4 ~ -> ~ _\sempre _\fff \stemUp <e d'>8 r8 \stemUp <e
        d'>4 ~ -> ~ \stemUp <e d'>8 r8 | % 305
    \stemUp <e d'>4 ~ -> ~ \stemUp <e d'>8 r8 \stemUp <e d'>4 ~ -> ~
    \stemUp <e d'>8 r8 | % 306
    \stemUp <e d'>4 ~ -> ~ \stemUp <e d'>8 r8 \stemUp <e d'>4 ~ -> ~
    \stemUp <e d'>8 r8 | % 307
    \stemUp <e d'>4 ~ -> ~ \stemUp <e d'>8 r8 \stemUp <e d'>4 ~ -> ~
    \stemUp <e d'>8 r8 \pageBreak | % 308
    \stemUp <d b'>4 ~ -> ~ \stemUp <d b'>8 r8 \stemUp <dis b'>4 ~ -> ~
    \stemUp <dis b'>8 r8 | % 309
    \stemUp <e b'>4 ~ -> ~ \stemUp <e b'>8 r8 \stemUp <e b'>4 ~ -> ~
    \stemUp <e b'>8 r8 | \barNumberCheck #310
    \stemUp <e e'>4 ~ -> ~ \stemUp <e e'>8 r8 \stemUp <e e'>4 ~ -> ~
    \stemUp <e e'>8 r8 | % 311
    \stemUp <e e'>4 ~ -> ~ \stemUp <e e'>8 r8 \stemUp <e e'>4 ~ -> ~
    \stemUp <e e'>8 r8 | % 312
    \stemUp <d fis>4. _\ffff \stemUp <d fis>8 \stemUp <d f>4. \stemUp <d
        f>8 | % 313
    \stemUp <d e>4. \stemUp <d e>8 \stemUp <d f>4. \stemUp <d f>8
    \pageBreak | % 314
    \stemUp <d fis>2 \stemDown <d' fis>4 \stemDown <a d>4 | % 315
    \stemUp <cis, a'>4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp a'8 \stemUp a8 \stemUp a8 }
    \stemUp a8 r8 r4 | % 316
    R1*2 _\markup{ \small\italic {cresc.} } | % 318
    <d, d'>1 ~ ~ _\p \startTrillSpan \stopTrillSpan _\mf _\markup{
        \small\italic {cresc.} } \startTrillSpan | % 319
    \stemUp <d d'>4 \stemUp <cis cis'>4 \stemUp <b b'>4 \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp <a a'>8 \stemUp <a a'>8 \stemUp <a a'>8 }
    \pageBreak | \barNumberCheck #320
    \stemUp fis'4 ( \stopTrillSpan _\f _\markup{ \small\italic {cresc.}
        } \startTrillSpan \stemUp g4 \stemUp a4 \stemUp ais4 ) | % 321
    \stemUp b4 ( \stemUp cis4 \stemUp d4 \stemUp e4 ) | % 322
    d1 ~ \stopTrillSpan _\ff _\markup{ \small\italic {cresc.} }
    \startTrillSpan | % 323
    \stemUp d4 \stemUp cis4 \stemUp b4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    | % 324
    \stemUp ais8 \stopTrillSpan _\fff r8 \stemUp <d, d'>4 ( \stemDown
    <fis fis'>8 ) r8 r4 \pageBreak | % 325
    r4 \stemDown <g g'>4 ( \stemUp b8 ) r8 r4 | % 326
    r4 \stemUp <g, g'>4 ~ ~ \stemUp <g g'>8 r8 \stemUp <f' d'>4 ~ ~ | % 327
    \stemUp <f d'>8 r8 \stemUp <cis cis'>4 ~ ~ \stemUp <cis cis'>8 r8
    \stemUp <b g'>4 ~ ~ \pageBreak | % 328
    \stemUp <b g'>8 r8 \stemUp <e e'>4 ~ ~ \stemUp <e e'>8 r8 \stemUp
    <a, a'>4 ~ ~ | % 329
    \stemUp <a a'>8 r8 \stemDown <g' g'>4 ~ ~ \stemDown <g g'>8 r8
    \stemDown <g g'>8 r8 | \barNumberCheck #330
    \stemUp fis'8 _\sempre _\fff r8 \stemUp e8 r8 \stemUp <c, fis'>8 r8
    \stemUp <d d'>8 r8 | % 331
    \stemUp <d d'>2 \stemUp <dis dis'>8 r8 \stemUp <e e'>8 r8 \pageBreak
    | % 332
    \stemUp fis'8 r8 \stemUp e8 r8 \stemUp <c, fis'>8 r8 \stemUp <d d'>8
    r8 | % 333
    \stemUp <d d'>2 \stemUp <dis dis'>8 r8 \stemUp <e e'>8 r8 | % 334
    \stemUp <fis d'>8 r8 \stemUp <e a>8 r8 \stemDown <fis fis'>8 r8
    \stemDown <g g'>8 r8 | % 335
    \stemDown <a fis'>8 r8 \stemUp <e a>8 r8 \stemDown <fis fis'>8 r8
    \stemDown <g g'>8 r8 \pageBreak | % 336
    \stemDown <a fis'>8 r8 \stemDown <g g'>8 r8 \stemDown <a fis'>8 r8
    \stemDown <g g'>8 r8 | % 337
    \stemDown <a fis'>8 r8 \stemDown <g g'>8 r8 \stemDown <a fis'>8 r8
    \stemDown <g g'>8 r8 | % 338
    \stemDown <a fis'>8 r8 r8 \stemDown <d fis>8 \stemDown <d fis>8 r8 r8
    \stemUp fis8 | % 339
    \stemUp fis8 r8 r8 \stemUp d,8 \stemUp d8 r8 r8 \stemUp fis8 |
    \barNumberCheck #340
    \stemUp fis8 r8 r4 \stemUp e'8 r8 r4 \pageBreak | % 341
    \stemDown <a, fis'>8 r8 r4 \stemUp <e e'>8 r8 r4 | % 342
    \stemDown <a fis'>8 r8 \stemDown <a fis'>8 r8 r4 \stemDown <a fis'>8
    r8 | % 343
    r4 \stemDown <a fis'>8 r8 r4 \stemDown <a fis'>8 r8 | % 344
    \stemDown <a fis'>8 r8 \stemUp <d, a'>8 r8 \stemUp <d a'>8 r8
    \stemUp <a fis'>8 r8 | % 345
    <fis a>1 ~ ~ | % 346
    \stemUp <fis a>2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp <fis a>8 \stemUp <fis a>8 \stemUp <fis a>8 }
    | % 347
    \stemUp <fis a>8 r8 r4 r2 \bar "|."
    }

PartPNineVoiceTwo =  \relative b' {
    \clef "treble" \time 4/4 \key c \none \transposition f | % 1
     \once \override NoteHead.style = ##f b1 s1*3 \pageBreak s1*3 \bar
    "||"
    s1*2 \pageBreak s1*5 \break s1*5 \pageBreak s1*4 \break s1*4
    \pageBreak s1*4 \pageBreak s1 | % 33
    \time 12/8  s2. \clef "bass" \stemDown c,,8 -. \stemDown dis8 -.
    \stemDown a'8 -. s4. | % 34
    \stemDown a8 -. r8*2/3 r8*2/3 r4.*2/3 r4.*2/3 \stemDown c,8 -. _\mp
    \stemDown dis8 -. \stemDown a'8 -. s1*1/3 | % 35
    \stemDown a8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 \pageBreak | % 36
    \clef "treble" s2*15 \pageBreak s2*15 \pageBreak s2*15 \pageBreak
    s1*3 | % 53
    \numericTimeSignature\time 4/4  r2 \stemDown cis4 _> _\pp \stemDown
    cis8 r16 \stemDown cis16 | % 54
    \stemDown fis,8 r8 r4 r2 | % 55
    R1 \pageBreak | % 56
    R1 | % 57
    r2 \stemDown cis'4 _> \stemDown cis8 r16 \stemDown cis16 | % 58
    \stemDown fis,8 r8 r4 r2 | % 59
    R1*2 \pageBreak | % 61
    R1*5 \pageBreak | % 66
    R1 s1*4 \bar "||"
    \pageBreak | % 71
    \key c \none \stemDown fis'8 s8*27 \stemDown b,4 ( \stemDown b'8 )
    s8*9 \break s1*5 \pageBreak | % 81
    r4 s4*13 \stemDown b,4 ( \stemDown b'8 ) s8*9 \pageBreak s1*4
    \pageBreak s1*2 | % 92
    \stemDown cis,4 \stemDown gis'4 \stemDown b,4 \stemDown c4 | % 93
    \stemDown cis8 s8*23 \pageBreak s1*6 \break s1*5 \pageBreak s1*6
    \break | % 113
    \stemDown fis8 s8*27 \stemDown b,4 ( \stemDown b'8 ) s8*9 \pageBreak
    s1*5 \break | % 123
    r4 s4*13 \stemDown b,4 ( \stemDown b'8 ) s8*9 \pageBreak s1*4
    \pageBreak s1*4 \pageBreak s1 | % 137
    \time 12/8  s1*8/3 \bar "||"
    s1*1/3 | % 139
    \key c \none s1. \pageBreak s2*15 \pageBreak s2*15 \pageBreak s2*15
    \pageBreak s1*6 \break s1*6 \pageBreak s1*6 \pageBreak | % 167
    \numericTimeSignature\time 4/4  s1*4 \pageBreak | % 171
    \time 12/8  s2. \clef "bass" r4.*2/3 -. \stemDown <dis,, a'>8 -. -.
    _\mf s4. | % 172
    \stemDown a'8 -. r8*2/3 r8*2/3 r4.*2/3 r4.*2/3 \stemDown c,8 -. _\mp
    \stemDown dis8 -. \stemDown a'8 -. s1*1/3 | % 173
    \stemDown a8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*47/24 \pageBreak | % 175
    \clef "treble" s2*15 \pageBreak s1*6 \pageBreak s2*15 \pageBreak
    s1*6 | % 193
    \numericTimeSignature\time 4/4  s1 \pageBreak s1*3 | % 197
    \stemDown e'8 r8 \stemDown b8 r16 \stemDown b16 \stemDown e8 r8
    \stemDown b8 r8 | % 198
    \stemDown e8 -> \stemDown a8 -> r4 r2 s1 | \barNumberCheck #200
    a,1 \pageBreak | % 201
    b1 | % 202
    cis1 | % 203
    fis,1 s1*2 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*4 \pageBreak | % 225
     \once \override NoteHead.style = ##f a'1 s1*2 \pageBreak s1*5
    \pageBreak s1*2 | % 235
    \stemDown a8 s8*23 \pageBreak | % 238
    \stemDown b4 s4*19 \pageBreak s1*5 \pageBreak s1*6 \pageBreak s4
    \stemDown e,8 r8 \stemDown d8 s4. | % 255
    \stemDown a'2 s1 \clef "bass" s2*5 \pageBreak | % 259
    \clef "treble" \stemDown a2 s2*7 | % 263
    \stemDown a2 s2 \pageBreak s2 \clef "bass" s2*5 | % 267
    \clef "treble" \stemDown a4 ~ \stemDown a8 s8*13 \pageBreak s1*5
    \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*2 | % 289
    \stemDown a8 s8*23 \pageBreak | % 292
    \stemDown b4 s4*19 \pageBreak s1*5 \pageBreak s1*6 \pageBreak s1*6
    \pageBreak s4*5 \stemDown e,4 \stemDown a8 s4. | % 316
    d,1 ~ | % 317
    \stemDown d4 \stemDown cis4 \stemDown b4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 }
    s1*2 \pageBreak | \barNumberCheck #320
    d1 ~ | % 321
    \stemDown d4 \stemDown cis4 \stemDown b4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 }
    | % 322
    d1 ~ | % 323
    \stemDown d4 \stemDown cis'4 \stemDown b4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 }
    | % 324
    \stemDown ais8 s8*7 \pageBreak s2 \stemDown b8 s8*19 \pageBreak s1*2
    | \barNumberCheck #330
    \stemDown fis8 s8 \stemDown a8 r16 \stemDown a16 s1. \pageBreak | % 332
    \stemDown fis8 s8 \stemDown a8 r16 \stemDown a16 s2*7 \pageBreak
    s8*23 \stemDown fis8 | % 339
    \stemDown fis8 \stemDown cis'8 \stemDown b8 \stemDown bes8 \stemDown
    a8 \stemDown g8 \stemDown fis8 \stemDown e8 | \barNumberCheck #340
    \stemDown d8 s4. \stemDown cis'8 s4. \pageBreak s1*7 \bar "|."
    }

PartPOneZeroVoiceOne =  \relative c'' {
    \clef "treble" \time 4/4 \key c \none \transposition a | % 1
    R1*4 \pageBreak | % 5
    R1*3 \bar "||"
    R1*2 \pageBreak | \barNumberCheck #10
    R1*5 \break | % 15
    \stemUp c8 -. ^\p r8 \stemUp g8 -. r16 \stemUp g16 -. \stemUp c8 -.
    r8 \stemUp g8 -. r8 | % 16
    \stemUp c16 -. _\> r16 \stemUp f8 ~ \stemUp f4 ~ \stemUp f8 _\! _\pp
    r8 r4 | % 17
    R1*3 \pageBreak | \barNumberCheck #20
    R1 | % 21
    d1 ~ _\pp _\< | % 22
    \stemUp d8 _\! _\p r8 \stemUp g,8 -. r16 \stemUp g16 -. \stemUp d'8
    -. r8 \stemUp g,8 -. r8 | % 23
    \stemUp d'8 -. r8 r4 r2 \break | % 24
    R1 | % 25
    d1 ~ _\pp _\< | % 26
    \stemUp d8 _\! _\p r8 \stemUp g,8 -. r16 \stemUp g16 -. \stemUp d'8
    -. r8 \stemUp bes8 -. r16 \stemUp bes16 -. | % 27
    \stemUp f'8 -. r8 r4 r2 \pageBreak | % 28
    R1*2 | \barNumberCheck #30
    r2 \stemUp <c, c'>8 _\mp _\< r8 \stemUp <c c'>8 -. r16 \stemUp <c
        c'>16 -. | % 31
    \stemUp <c c'>8 -. _\! _\mf r8 r4 r2 \pageBreak | % 32
    R1*4 \pageBreak | % 36
    R1*5 \pageBreak | % 41
    R1*4 | % 45
    \time 12/8  r2.*2/3 r4.*2/3 \stemDown <f f'>8 _\mf \stemDown <f f'>8
    \stemDown <f f'>8 s4. \pageBreak | % 46
    \stemUp <des des'>2. ~ ~ _\> \stemUp <des des'>8 _\! r8*2/3 r8*2/3 r4.*2/3
    s1*5/24 | % 47
    r1 s2 | % 48
    r1 s2 | % 49
    r2.*2/3 r4.*2/3 \stemUp <cis cis'>8 _\f \stemUp <cis cis'>8 \stemUp
    <cis cis'>8 s4. | \barNumberCheck #50
    \stemUp a'2. ~ ^\> \stemUp a8 ^\! r8*2/3 r8*2/3 r4.*2/3 s1*5/24
    \pageBreak | % 51
    r1 s2 | % 52
    r1 s2 | % 53
    r1 r2*2/3 s1*1/6 | % 54
    r1 r2*2/3 s1*1/6 | % 55
    \numericTimeSignature\time 4/4  R1 \pageBreak | % 56
    \stemUp fis'4 -> _\mp _\! ^\mf _\mf \stemUp fis8 r16 \stemUp fis16
    \stemUp a,8 r8 r4 | % 57
    R1*2 | % 59
    R1 | \barNumberCheck #60
    \stemUp fis'4 -> _\mp _\! ^\mf _\mf \stemUp fis8 r16 \stemUp fis16
    \stemUp a,8 r8 r4 \pageBreak | % 61
    R1 | % 62
    \stemDown bes8 -. _\p ^ "a 2" r8 \stemUp es,8 -. r16 \stemUp es16 -.
    \stemDown bes'8 -. r8 \stemUp es,8 -. r8 | % 63
    \stemUp a8 -. r8 r4 r2 | % 64
    \stemDown d8 -. _\mp r8 \stemUp g,8 -. r16 \stemUp g16 -. \stemDown
    d'8 -. r8 \stemUp g,8 -. r8 | % 65
    \stemDown c8 -. r8 r4 r2 \pageBreak | % 66
    \stemDown g'8 -. _\mf r8 \stemDown c,8 -. r16 \stemDown c16 -.
    \stemDown g'8 -. r8 \stemDown c,8 -. r8 | % 67
    \stemDown a'8 -. r8 r4 r2 | % 68
    \stemDown d,8 -. _\f r8 \stemUp g,8 -. r16 \stemUp g16 -. \stemDown
    d'8 -. r8 \stemUp g,8 -. r8 | % 69
    \stemDown <a fis'>8 _\ff r8 r4 r2 | \barNumberCheck #70
    R1 \bar "||"
    \pageBreak | % 71
    \key c \none R1*5 \break | % 76
    R1*5 \pageBreak | % 81
    R1*5 \pageBreak | % 86
    R1*4 \pageBreak | \barNumberCheck #90
    r2 r4 \stemUp dis4 _\f | % 91
    \stemUp e8 r8 r4 r2 | % 92
    R1 | % 93
    r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <f, c'>8 _\ff \stemUp <f c'>8 \stemUp <f c'>8 }
    \stemUp <f c'>2 ~ ~ | % 94
    \stemUp <f c'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <b fis'>8 \stemDown <b fis'>8 \stemDown <b fis'>8 }
    \stemDown <b fis'>2 ~ ~ | % 95
    \stemDown <b fis'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp f'8 \stemUp f8 \stemUp f8 }
    \stemUp f2 ~ \pageBreak | % 96
    \stemUp f8 r8 \stemUp fis8 r16 \stemUp fis16 \stemUp g8 r8 r4 | % 97
    R1*5 \break | % 102
    R1*5 \pageBreak | % 107
    R1*6 \break | % 113
    R1*5 \pageBreak | % 118
    R1*5 \break | % 123
    R1*5 \pageBreak | % 128
    R1*3 | % 131
    \stemUp <es, es'>2 _\f \stemDown <f f'>8 r8 \stemDown <bes bes'>4 ~
    ~ \pageBreak | % 132
    \stemDown <bes bes'>4 \stemDown <bes bes'>4 \stemDown <bes f'>8 r8 r4
    | % 133
    R1*2 | % 135
    \stemUp <es, es'>2 _\f \stemDown <f f'>8 r8 \stemDown <bes bes'>4 ~
    ~ \pageBreak | % 136
    \stemDown <bes bes'>4 \stemDown <bes bes'>4 \stemDown <bes f'>8 r8 r4
    | % 137
    \time 12/8  r2.*2/3 \stemUp <es, es'>8 _\mf r8*2/3 r8*2/3 \stemDown
    <bes' d>8 r8*2/3 r8*2/3 s1*5/12 | % 138
    r2.*2/3 \stemUp <es, es'>8 _\mp r8*2/3 r8*2/3 \stemDown <bes' d>8 r4*2/3
    \bar "||"
    s1*5/12 | % 139
    \key c \none r1 s2 \pageBreak | \barNumberCheck #140
    r1 s2 | % 141
    r1 s2 | % 142
    r1 s2 | % 143
    r1 s2 | % 144
    r1 s2 \pageBreak | % 145
    r1 s2 | % 146
    r1 s2 | % 147
    r1 s2 | % 148
    r1 s2 | % 149
    r1 s2 \pageBreak | \barNumberCheck #150
    r1 s2 | % 151
    r1 s2 | % 152
    r1 s2 | % 153
    \numericTimeSignature\time 4/4  \stemUp c8 -. ^\p r8 \stemUp g8 -. r16
    \stemUp g16 -. \stemUp c8 -. r8 \stemUp g8 -. r8 | % 154
    \stemUp c16 -. ^\> r16 \stemUp f8 ~ \stemUp f4 ~ \stemUp f8 ^\! ^\pp
    r8 r4 \pageBreak | % 155
    R1*4 \break | % 159
    d1 ~ _\pp _\< | \barNumberCheck #160
    \stemUp d8 _\! _\p r8 \stemUp g,8 -. r16 \stemUp g16 -. \stemUp d'8
    -. r8 \stemUp g,8 -. r8 | % 161
    \stemUp d'8 -. r8 r4 r2 | % 162
    R1 \pageBreak | % 163
    d1 ~ _\pp _\< | % 164
    \stemUp d8 _\! _\p r8 \stemUp g,8 -. r16 \stemUp g16 -. \stemUp d'8
    -. r8 \stemUp bes8 -. r16 \stemUp bes16 -. | % 165
    \stemUp f'8 -. r8 r4 r2 | % 166
    R1 \pageBreak | % 167
    R1 | % 168
    r2 \stemUp <c, c'>8 _\mp _\< r8 \stemUp <c c'>8 -. r16 \stemUp <c
        c'>16 -. | % 169
    \stemUp <c c'>8 -. _\! _\mf r8 r4 r2 | \barNumberCheck #170
    R1 \pageBreak | % 171
    R1*4 \pageBreak | % 175
    R1*5 \pageBreak | \barNumberCheck #180
    R1*3 | % 183
    \time 12/8  r2.*2/3 r4.*2/3 \stemDown <f f'>8 _\mf \stemDown <f f'>8
    \stemDown <f f'>8 s4. \pageBreak | % 184
    \stemUp <des des'>2. ~ ~ _\> \stemUp <des des'>8 r8*2/3 _\! r8*2/3 r4.*2/3
    s1*5/24 | % 185
    r1 s2 | % 186
    r1 s2 | % 187
    r2.*2/3 r4.*2/3 \stemDown <as' as'>8 _\f \stemDown <as as'>8
    \stemDown <as as'>8 s4. | % 188
    \stemUp <des, des'>2. ~ ~ _\> \stemUp <des des'>8 r8*2/3 _\! r8*2/3
    r4.*2/3 s1*5/24 \pageBreak | % 189
    r1 s2 | \barNumberCheck #190
    r1 s2 | % 191
    r1 s2 | % 192
    r1 s2 | % 193
    \numericTimeSignature\time 4/4  \stemDown <c' f>4 _\ff \stemUp <a c>8
    \stemUp <f a>8 \stemUp <c f>4 \stemUp c4 \pageBreak | % 194
    \stemUp f4 ^ "a 2" \stemUp a4 \stemDown c8 r8 r4 | % 195
    R1*4 | % 199
    R1 | \barNumberCheck #200
    \stemUp f8 _\pp _\ leggieramente ^\pp ^\ leggieramente r8 \stemUp c8
    r16 \stemUp c16 \stemUp f8 r8 \stemUp c8 r8 \pageBreak | % 201
    \stemUp g'8 -> _\p \stemUp c8 -> r4 r2 | % 202
    \stemUp d,8 ^\p r8 \stemUp a8 r16 \stemUp a16 \stemUp d8 r8 \stemUp
    a8 r8 | % 203
    \stemUp d8 -> \stemUp g8 -> r4 r2 | % 204
    \stemDown <f, f'>8 _\p _\< r8 \stemUp <c c'>8 r16 \stemUp <c c'>16
    \stemDown <f f'>8 r8 \stemUp <c c'>8 r8 | % 205
    \stemDown <f f'>8 -> _\! _\mp \stemDown <c' c'>8 -> r4 r2 \pageBreak
    | % 206
    R1 | % 207
    \stemUp e8 ^\mf r8 \stemUp bes8 r16 \stemUp bes16 \stemUp e8 r8
    \stemUp bes8 r8 | % 208
    \stemUp f'8 -> _\mf \stemUp bes8 -> r4 r2 | % 209
    \stemUp f8 r8 \stemUp c8 r16 \stemUp c16 \stemUp f8 r8 \stemUp c8 r8
    | \barNumberCheck #210
    \stemUp f8 -> _\f \stemUp bes8 -> r4 r2 \pageBreak | % 211
    \stemUp e,8 ^\f ^\< r8 \stemUp bes8 r16 \stemUp bes16 \stemUp e8 r8
    \stemUp bes8 r8 | % 212
    \stemUp f'8 -> ^\! _\ff ^\ff \stemUp bes8 -> r4 r4 \stemUp f,8 r8 | % 213
    \stemDown c'8 -> ^ "a 2" \stemDown f8 -> r4 r2 | % 214
    \stemDown c8 _\ff r8 \stemUp g8 r16 \stemUp g16 \stemDown c8 r8
    \stemUp g8 r8 | % 215
    \stemDown c8 -> \stemDown f8 ~ -> \stemDown f2. \pageBreak | % 216
    \stemDown c8 _\fff r8 \stemUp g8 r16 \stemUp g16 \stemDown c8 r8
    \stemUp g8 r8 | % 217
    \stemDown c8 -> \stemDown f8 ~ -> \stemDown f8 \stemDown f8
    \stemDown c8 \stemUp g4 \stemUp g8 | % 218
    \stemDown c8 \stemDown f4 \stemDown f8 \stemDown c8 \stemUp g4
    \stemUp g8 | % 219
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f8 \stemDown f8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 \stemUp g8 r8 }
    | \barNumberCheck #220
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f8 \stemDown f8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 \stemUp g8 r8 }
    \pageBreak | % 221
    \times 2/3  {
        \stemDown c8 \stemDown c8 r8 }
    r4 r2 | % 222
    R1*3 \pageBreak | % 225
    R1*3 \pageBreak | % 228
    R1 | % 229
    \stemDown <f, f'>8 _\fff r8 \stemDown <f f'>8 r16 \stemDown <f f'>16
    \stemDown <f f'>8 r8 \stemDown <f f'>8 r8 | \barNumberCheck #230
    \stemDown <bes es>8 r8 \stemDown <bes es>8 r16 \stemDown <bes es>16
    \stemDown <a f'>2 | % 231
    \stemDown <bes f'>8 r8 \stemDown <es f>8 r8 \stemDown <d f>8 r8
    \stemDown <c f>8 r8 | % 232
    \stemUp <es, es'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <es es'>8 \stemUp <es es'>8 \stemUp <es es'>8 }
    \stemUp <f d'>8 r8 r4 \pageBreak | % 233
    \stemDown <bes bes'>8 r8 \stemDown <es f>8 r8 \stemDown <d f>8 r8
    \stemDown <c f>8 r8 | % 234
    \stemUp <es, es'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <es es'>8 \stemUp <es es'>8 \stemUp <es es'>8 }
    \stemUp <f d'>8 r8 r4 | % 235
    \stemDown <f f'>8 r8 r4 \stemDown <bes d>8 r8 r4 | % 236
    \stemDown <g g'>8 -! \stemDown <as as'>8 -! \stemDown <bes bes'>8 -!
    \stemDown <b b'>8 -! \stemDown <g' c>8 r8 r4 | % 237
    \stemDown <d g>8 r8 \stemDown <d g>8 r8 \stemDown <cis bes'>8 r8
    \stemDown <d g>8 r8 \pageBreak | % 238
    \stemDown <g, g'>4 -> \once \omit TupletBracket
    \times 2/3  {
        \stemDown <d' g>8 \stemDown <d g>8 \stemDown <d g>8 }
    \stemDown <fis a>8 \stemDown <f a>8 r4 | % 239
    \stemDown <f, f'>8 r8 \stemDown <f f'>8 r16 \stemDown <f f'>16
    \stemDown <f f'>8 r8 \stemDown <f f'>8 r8 | \barNumberCheck #240
    \stemDown <bes es>8 r8 \stemDown <bes es>8 r16 \stemDown <bes es>16
    \stemDown <a f'>2 | % 241
    \stemDown <bes f'>8 r8 \stemDown <es f>8 r8 \stemDown <d f>8 r8
    \stemDown <c f>8 r8 | % 242
    \stemUp <es, es'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <es es'>8 \stemUp <es es'>8 \stemUp <es es'>8 }
    \stemUp <f d'>8 r8 r4 \pageBreak | % 243
    \stemDown <bes bes'>8 r8 \stemDown <es f>8 r8 \stemDown <d f>8 r8
    \stemDown <c f>8 r8 | % 244
    \stemUp <es, es'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <es es'>8 \stemUp <es es'>8 \stemUp <es es'>8 }
    \stemUp <f d'>8 r8 r4 | % 245
    \stemUp <fis cis'>8 r8 r4 \stemUp <eis eis'>8 r8 r4 | % 246
    \stemUp cis'8 r8 r4 \stemUp eis8 r8 r4 | % 247
    \stemUp <d, d'>2 ~ ~ \stemUp <d d'>8 \stemUp <d d'>16 \stemUp <d d'>16
    \stemUp <d d'>4 ~ ~ \pageBreak | % 248
    \stemUp <d d'>2 ~ ~ \stemUp <d d'>8 \stemUp <d d'>16 \stemUp <d d'>16
    \stemDown <d' fis>8 r8 | % 249
    \stemDown <d g>8 r8 \stemDown <d g>8 r8 \stemDown <es g>8 r8
    \stemDown <d g>8 r8 | \barNumberCheck #250
    \stemDown <c g'>8 r8 \stemDown <des g>8 r8 \stemUp bes8 r8 \stemUp b8
    r8 | % 251
    \stemUp c8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <c es>8 \stemDown <c es>8 \stemDown <c es>8 }
    \stemDown <c es>2 ~ ~ | % 252
    \stemDown <c es>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <d a'>8 \stemDown <d a'>8 \stemDown <d a'>8 }
    \stemDown <d a'>2 ~ ~ | % 253
    \stemDown <d a'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <bes as'>8 \stemDown <bes as'>8 \stemDown <bes as'>8 }
    \stemDown <bes as'>2 ~ ~ \pageBreak | % 254
    \stemDown <bes as'>8 r8 \stemDown <c a'>8 r8 \stemDown <d f>8 r8 r4
    | % 255
    \stemDown <a c>2 _\fff \stemUp <g cis>2 | % 256
    \stemUp <fis d'>8 r8 \stemDown <g es'>8 r8 r2 | % 257
    R1*2 \pageBreak | % 259
    \stemDown <a c>2 _\fff \stemUp <g cis>2 | \barNumberCheck #260
    \stemUp <fis d'>8 r8 \stemDown <g es'>8 r8 r2 | % 261
    R1*2 | % 263
    \stemDown <a c>2 _\fff \stemUp <g cis>2 \pageBreak | % 264
    \stemUp <fis d'>8 r8 \stemDown <g es'>8 r8 r2 | % 265
    R1*2 | % 267
    \stemDown <a c>4 ~ ~ _\fff \stemDown <a c>8 r8 \stemUp <g cis>4 ~ ~
    \stemUp <g cis>8 r8 | % 268
    \stemUp <fis d'>4 ~ ~ \stemUp <fis d'>8 r8 \stemDown <g es'>4 ~ ~
    \stemDown <g es'>8 r8 \pageBreak | % 269
    \stemDown <c e>4 ~ ~ \stemDown <c e>8 r8 \stemDown <d f>4 ~ ~
    \stemDown <d f>8 r8 | \barNumberCheck #270
    \stemDown <c fis>4 ~ ~ \stemDown <c fis>8 r8 \stemDown <b g'>4 ~ ~
    \stemDown <b g'>8 r8 | % 271
    \stemDown <c as'>4 ~ ~ \stemDown <c as'>8 r8 \stemDown <f a>4 ~ ~
    \stemDown <f a>8 r8 | % 272
    \stemDown <cis fis>4 ~ ~ \stemDown <cis fis>8 r8 \stemDown <d g>4 ~
    ~ \stemDown <d g>8 r8 | % 273
    \stemDown <e g>8 r8 \stemDown <f as>8 r8 \stemDown <f bes>8 r8
    \stemDown <as c>8 r8 \pageBreak | % 274
    \stemDown <bes c>8 r8 \stemDown <a c>8 r8 \stemDown <bes c>8 r8 r4 | % 275
    R1 | % 276
    \stemDown <c, f>4 _\fff \stemUp <f, c'>8. \stemUp <f c'>16 \stemDown
    <c' f>4 \stemUp <f, c'>4 | % 277
    \stemDown <c' g'>8 -. \stemDown <g' c>8 -. r4 r2 | % 278
    \stemDown <c, f>4 \stemUp <f, c'>8. \stemUp <f c'>16 \stemDown <c'
        f>4 \stemUp <f, c'>4 | % 279
    \stemDown <c' g'>8 -. \stemDown <g' c>8 -. r4 \stemDown <f, c'>8 -.
    \stemDown <c' f>8 -. r4 | \barNumberCheck #280
    \stemDown <c g'>8 -. \stemDown <g' c>8 -. r4 \stemDown <f, c'>8 -.
    \stemDown <c' f>8 -. r4 \pageBreak | % 281
    \stemDown <g' c>2 \stemDown <c, f>2 | % 282
    \stemUp <g c>2 \stemUp <c, f>8 r8 r4 | % 283
    \stemDown <f f'>8 _\fff r8 \stemDown <f f'>8 r16 \stemDown <f f'>16
    \stemDown <f f'>8 r8 \stemDown <f f'>8 r8 | % 284
    \stemDown <bes es>8 r8 \stemDown <bes es>8 r16 \stemDown <bes es>16
    \stemDown <a f'>2 | % 285
    \stemDown <bes f'>8 r8 \stemDown <es f>8 r8 \stemDown <d f>8 r8
    \stemDown <c f>8 r8 | % 286
    \stemUp <es, es'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <es es'>8 \stemUp <es es'>8 \stemUp <es es'>8 }
    \stemUp <f d'>8 r8 r4 \pageBreak | % 287
    \stemDown <bes bes'>8 r8 \stemDown <es f>8 r8 \stemDown <d f>8 r8
    \stemDown <c f>8 r8 | % 288
    \stemUp <es, es'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <es es'>8 \stemUp <es es'>8 \stemUp <es es'>8 }
    \stemUp <f d'>8 r8 r4 | % 289
    \stemDown <f f'>8 r8 r4 \stemDown <bes d>8 r8 r4 | \barNumberCheck
    #290
    \stemDown <g g'>8 -! \stemDown <as as'>8 -! \stemDown <bes bes'>8 -!
    \stemDown <b b'>8 -! \stemDown <g' c>8 r8 r4 | % 291
    \stemDown <d g>8 r8 \stemDown <d g>8 r8 \stemDown <cis bes'>8 r8
    \stemDown <d g>8 r8 \pageBreak | % 292
    \stemDown <g, g'>4 -> \once \omit TupletBracket
    \times 2/3  {
        \stemDown <d' g>8 \stemDown <d g>8 \stemDown <d g>8 }
    \stemDown <fis a>8 \stemDown <f a>8 r4 | % 293
    \stemDown <f, f'>8 r8 \stemDown <f f'>8 r16 \stemDown <f f'>16
    \stemDown <f f'>8 r8 \stemDown <f f'>8 r8 | % 294
    \stemDown <bes es>8 r8 \stemDown <bes es>8 r16 \stemDown <bes es>16
    \stemDown <a f'>2 | % 295
    \stemDown <bes f'>8 r8 \stemDown <es f>8 r8 \stemDown <d f>8 r8
    \stemDown <c f>8 r8 | % 296
    \stemUp <es, es'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <es es'>8 \stemUp <es es'>8 \stemUp <es es'>8 }
    \stemUp <f d'>8 r8 r4 \pageBreak | % 297
    \stemDown <bes bes'>8 r8 \stemDown <es f>8 r8 \stemDown <d f>8 r8
    \stemDown <c f>8 r8 | % 298
    \stemUp <es, es'>8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <es es'>8 \stemUp <es es'>8 \stemUp <es es'>8 }
    \stemUp <f d'>8 r8 r4 | % 299
    \stemUp <fis cis'>8 r8 r4 \stemUp <eis eis'>8 r8 r4 |
    \barNumberCheck #300
    \stemUp cis'8 r8 r4 \stemUp eis8 r8 r4 | % 301
    \stemUp <d, d'>2 ~ ~ \stemUp <d d'>8 \stemUp <d d'>16 \stemUp <d d'>16
    \stemUp <d d'>4 ~ ~ \pageBreak | % 302
    \stemUp <d d'>2 ~ ~ \stemUp <d d'>8 \stemUp <d d'>16 \stemUp <d d'>16
    \stemDown <d' fis>8 r8 | % 303
    \stemDown <d g>8 r8 \stemDown <d g>8 r8 \stemDown <es g>8 r8
    \stemDown <d g>8 r8 | % 304
    \stemDown <c g'>4 ~ -> ~ _\sempre _\fff \stemDown <c g'>8 r8
    \stemDown <c ges'>4 ~ -> ~ \stemDown <c ges'>8 r8 | % 305
    \stemDown <c f>4 ~ -> ~ \stemDown <c f>8 r8 \stemDown <c e>4 ~ -> ~
    \stemDown <c e>8 r8 | % 306
    \stemDown <c es>4 ~ -> ~ \stemDown <c es>8 r8 \stemDown <c e>4 ~ ->
    ~ \stemDown <c e>8 r8 | % 307
    \stemDown <c f>4 ~ -> ~ \stemDown <c f>8 r8 \stemDown <c fis>4 ~ ->
    ~ \stemDown <c fis>8 r8 \pageBreak | % 308
    \stemDown <bes g'>4 ~ -> ~ \stemDown <bes g'>8 r8 \stemDown <b g'>4
    ~ -> ~ \stemDown <b g'>8 r8 | % 309
    \stemDown <c g'>4 ~ -> ~ \stemDown <c g'>8 r8 \stemDown <c g'>4 ~ ->
    ~ \stemDown <c g'>8 r8 | \barNumberCheck #310
    \stemDown <c es>4 ~ -> ~ \stemDown <c es>8 r8 \stemDown <c es>4 ~ ->
    ~ \stemDown <c es>8 r8 | % 311
    \stemDown <c es>4 ~ -> ~ \stemDown <c es>8 r8 \stemDown <c es>4 ~ ->
    ~ \stemDown <c es>8 r8 | % 312
    \stemDown <d f>4 _\ffff \once \omit TupletBracket
    \times 2/3  {
        \stemDown <bes bes'>8 \stemDown <bes bes'>8 \stemDown <bes bes'>8
        }
    \stemDown <des ges>4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <bes bes'>8 \stemDown <bes bes'>8 \stemDown <bes bes'>8
        }
    | % 313
    \stemDown <c g'>4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <bes bes'>8 \stemDown <bes bes'>8 \stemDown <bes bes'>8
        }
    \stemDown <des ges>4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <bes bes'>8 \stemDown <bes bes'>8 \stemDown <bes bes'>8
        }
    \pageBreak | % 314
    \stemDown <d f>2 \stemDown <bes d>4 \stemUp bes4 | % 315
    \stemUp f4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp f8 \stemUp f8 \stemUp f8 }
    \stemUp f'8 r8 r4 | % 316
    R1*4 \pageBreak | \barNumberCheck #320
    <bes, bes'>1 ~ ~ _\f _\< | % 321
    \stemDown <bes bes'>4 \stemDown <a a'>4 \stemDown <g g'>4 \once
    \omit TupletBracket
    \times 2/3  {
        \stemDown <f f'>8 _\! \stemDown <f f'>8 \stemDown <f f'>8 }
    | % 322
    <bes bes'>1 ~ ~ _\ff _\< | % 323
    \stemDown <bes bes'>4 \stemDown <a a'>4 \stemDown <g g'>4 \once
    \omit TupletBracket
    \times 2/3  {
        \stemDown <f f'>8 _\! \stemDown <f f'>8 \stemDown <f f'>8 }
    | % 324
    \stemDown <fis fis'>8 _\fff r8 \stemUp <d d'>4 ~ ~ \stemUp <d d'>8 r16
    \stemUp <d d'>16 -. \stemUp <d d'>8 -. r16 \stemUp <d d'>16 -.
    \pageBreak | % 325
    \stemUp <d d'>8 -. r8 \stemUp g4 ( \stemDown <g g'>8 ) r16 \stemDown
    <g g'>16 -. \stemDown <g g'>8 -. r16 \stemDown <g g'>16 -. | % 326
    \stemDown <g g'>8 -. r8 \stemUp <g c>4 ~ ~ \stemUp <g c>8 r8 r4 | % 327
    r4 \stemDown <a d>4 ~ ~ \stemDown <a d>8 r8 r4 \pageBreak | % 328
    r4 \stemDown <g e'>4 ~ ~ \stemDown <g e'>8 r8 r4 | % 329
    r4 \stemDown <f' a>4 ~ ~ \stemDown <f a>8 r8 \stemDown <c f>8 r8 |
    \barNumberCheck #330
    \stemDown <bes bes'>8 _\sempre _\fff r8 \stemDown <f f'>8 r16
    \stemDown <f f'>16 \stemDown <bes bes'>8 r8 \stemUp <es, es'>8 r8 | % 331
    \stemUp bes''8 -> \stemUp f8 ^> r4 r2 \pageBreak | % 332
    \stemDown <bes, bes'>8 r8 \stemDown <f f'>8 r16 \stemDown <f f'>16
    \stemDown <bes bes'>8 r8 \stemUp <es, es'>8 r8 | % 333
    \stemUp bes''8 -> \stemUp f8 ^> r4 r2 | % 334
    \stemDown <bes, d>8 r8 \stemDown <c f>8 r8 \stemDown <bes g'>8 r8
    \stemDown <c a'>8 r8 | % 335
    \stemDown <f bes>8 r8 \stemDown <c f>8 r8 \stemDown <bes g'>8 r8
    \stemDown <c a'>8 r8 \pageBreak | % 336
    \stemDown <f bes>8 r8 \stemDown <a c>8 r8 \stemDown <f bes>8 r8
    \stemDown <a c>8 r8 | % 337
    \stemDown <f bes>8 r8 \stemDown <a c>8 r8 \stemDown <f bes>8 r8
    \stemDown <a c>8 r8 | % 338
    \stemUp bes8 r8 r8 \stemUp bes8 \stemUp bes8 r8 r8 \stemUp f8 | % 339
    \stemDown <bes, f'>8 r8 r8 \stemDown <bes d>8 \stemDown <bes d>8 r8
    r8 \stemUp <d, f>8 | \barNumberCheck #340
    \stemUp <d f>8 r8 r4 \stemUp f'8 r8 r4 \pageBreak | % 341
    \stemDown <bes, bes'>8 r8 r4 \stemDown <f f'>8 r8 r4 | % 342
    \stemDown <bes bes'>8 r8 \stemDown <bes bes'>8 r8 r4 \stemDown <bes
        bes'>8 r8 | % 343
    r4 \stemDown <bes bes'>8 r8 r4 \stemDown <bes f'>8 r8 | % 344
    \stemDown <bes f'>8 r8 \stemDown <bes f'>8 r8 \stemUp bes8 r8
    \stemUp <d, f>8 r8 | % 345
    R1*3 \bar "|."
    }

PartPOneZeroVoiceTwo =  \relative g' {
    \clef "treble" \time 4/4 \key c \none \transposition a | % 1
     \once \override NoteHead.style = ##f g1 s1*3 \pageBreak s1*3 \bar
    "||"
    s1*2 \pageBreak s1*5 \break | % 15
    R1*2 s1*3 \pageBreak s1 | % 21
    d1 ~ | % 22
    \stemDown d8 s8 r4 \stemDown d8 -. s8 r4 | % 23
    \stemDown d8 -. s8*7 \break s1 | % 25
    d1 ~ | % 26
    \stemDown d8 s8 r4 \stemDown d8 -. s8 r4 | % 27
    \stemDown f8 -. s8*7 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*5
    \pageBreak s1*4 | % 45
    \time 12/8  s1. \pageBreak s1*151/24 \stemDown a8 -> r8*2/3 r8*2/3 r4.*2/3
    r2.*2/3 s1*1/6 \pageBreak s1*6 | % 55
    \numericTimeSignature\time 4/4  \stemDown d4 \stemDown d8 r16
    \stemDown d16 \stemDown a2 _\< \pageBreak | % 56
    \stemDown fis8 r8 r4 r2 s1*2 | % 59
    \stemDown d'4 \stemDown d8 r16 \stemDown d16 \stemDown a2 _\< |
    \barNumberCheck #60
    \stemDown fis8 r8 r4 r2 \pageBreak s1*5 \pageBreak s1*5 \bar "||"
    \pageBreak | % 71
    \key c \none s1*5 \break s1*5 \pageBreak s1*5 \pageBreak s1*4
    \pageBreak s2. \stemDown dis4 | % 91
    \stemDown e4 \stemDown e4 \stemDown e4 ~ \stemDown e8 r8 s4*13 \once
    \omit TupletBracket
    \times 2/3  {
        \stemDown g'8 \stemDown g8 \stemDown g8 }
    \stemDown g2 ~ \pageBreak | % 96
    \stemDown g8 s8 \stemDown a8 s8 \stemDown b,8 s8*43 \break s1*5
    \pageBreak s1*6 \break s1*5 \pageBreak s1*5 \break s1*5 \pageBreak
    s1*4 \pageBreak s1*4 \pageBreak s1 | % 137
    \time 12/8  s1*31/12 \bar "||"
    s1*5/12 | % 139
    \key c \none s1. \pageBreak s2*15 \pageBreak s2*15 \pageBreak s2*9 | % 153
    \numericTimeSignature\time 4/4  R1*2 \pageBreak s1*4 \break | % 159
    d,1 ~ | \barNumberCheck #160
    \stemDown d8 s8 r4 \stemDown d8 -. s8 r4 | % 161
    \stemDown d8 -. s8*15 \pageBreak | % 163
    d1 ~ | % 164
    \stemDown d8 s8 r4 \stemDown d8 -. s8 r4 | % 165
    \stemDown f8 -. s8*15 \pageBreak s1*4 \pageBreak s1*4 \pageBreak
    s1*5 \pageBreak s1*3 | % 183
    \time 12/8  s1. \pageBreak s2*15 \pageBreak s1*6 | % 193
    \numericTimeSignature\time 4/4  s2. \stemDown c4 \pageBreak s1*5 | % 199
    \stemDown b'8 r8 \stemDown f8 r16 \stemDown f16 \stemDown b8 r8
    \stemDown f8 r8 | \barNumberCheck #200
    \stemDown c'8 -> \stemDown f8 -> r4 r2 \pageBreak | % 201
    \stemDown c8 r8 \stemDown g8 s16 \stemDown g16 \stemDown c8 r8
    \stemDown g8 r8 | % 202
    \stemDown c8 -> \stemDown f8 -> r4 r2 | % 203
    d1 s1*2 \pageBreak s1 | % 207
    R1 | % 208
    \stemDown bes8 r8 \stemDown f8 r16 \stemDown f16 \stemDown bes8 r8
    \stemDown f8 r8 | % 209
    \stemDown c'8 -> \stemDown f8 -> r4 r2 | \barNumberCheck #210
    \stemDown g,8 r8 \stemDown d8 r16 \stemDown d16 \stemDown g8 r8
    \stemDown d8 r8 \pageBreak | % 211
    \stemDown g8 -> \stemDown c8 -> r4 r2 | % 212
    \stemDown bes8 r8 \stemDown f8 r16 \stemDown f16 \stemDown bes8 r8
    \stemDown f8 s8*25 \pageBreak s1*5 \pageBreak s1*4 \pageBreak | % 225
     \once \override NoteHead.style = ##f f1 s1*2 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*3 | % 246
    \stemDown fis8 -! \stemDown gis8 -! \stemDown ais8 -! \stemDown b8
    -! \stemDown cis8 -! \stemDown d8 -! s4*5 \pageBreak s2*5 \stemDown
    d8 s8 \stemDown d8 s8 | % 251
    \stemDown c8 s8*23 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*3 | \barNumberCheck #300
    \stemDown fis,8 -! \stemDown gis8 -! \stemDown ais8 -! \stemDown b8
    -! \stemDown cis8 -! \stemDown d8 -! s4*5 \pageBreak s1*6 \pageBreak
    s1*6 \pageBreak s2. \stemDown bes4 | % 315
    \stemDown f4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown f8 \stemDown f8 \stemDown f8 }
    \stemDown f'8 s8*35 \pageBreak s1*5 \pageBreak s4 \stemDown g,4 ~
    s2*5 \pageBreak s1*3 | % 331
    \stemDown bes8 _> \stemDown f'8 _> s2. \pageBreak s1 | % 333
    \stemDown bes,8 _> \stemDown f'8 _> s4*11 \pageBreak s1*2 | % 338
    \stemDown f8 \stemDown bes8 \stemDown a8 \stemDown g8 \stemDown f8
    \stemDown es8 \stemDown d8 \stemDown c8 s1. \stemDown f8 s4.
    \pageBreak s2*7 \stemDown bes,8 s8*27 \bar "|."
    }

PartPOneOneVoiceOne =  \relative g' {
    \clef "tenor" \time 4/4 \key g \major | % 1
    R1*4 \pageBreak _ "Trombones" | % 5
    R1*3 \bar "||"
    R1*2 \pageBreak | \barNumberCheck #10
    R1*3 _ "Tbn." | % 13
    R1 | % 14
    R1 \break | % 15
    R1*5 \pageBreak | \barNumberCheck #20
    R1*4 \break | % 24
    R1*4 \pageBreak | % 28
    R1*4 \pageBreak | % 32
    R1*4 \pageBreak | % 36
    R1*5 \pageBreak | % 41
    \stemUp g16 -> _\mp _\> ^\p _ "Tbn." r16 r8 \stemUp d16 -> r16 r8 r2
    _\p | % 42
    \stemUp a16 -> r16 r8 \stemUp d16 -> r16 r8 \stemUp b16 -> r16 r8 r4
    _\p | % 43
    r8 \stemUp g16 ^\< r16 \stemUp a16 r16 \stemUp b16 r16 \stemUp c16
    ^\! ^\mp r16 r8 r4 _\mp | % 44
    r2 _\> \stemUp g16 ^\p r16 r8 r4 | % 45
    R1 \pageBreak | % 46
    R1*2 _ "Tbn." | % 48
    \time 12/8  r2.*2/3 r4.*2/3 r4.*2/3 _\f s2 | % 49
    r1 _\> s2 | \barNumberCheck #50
    r1 _\> s2 \pageBreak | % 51
    r1 _ "Tbn." s2 | % 52
    r1 s2 | % 53
    r1 r2*2/3 s1*1/6 | % 54
    \numericTimeSignature\time 4/4  \stemUp dis'4 -> _\p \stemUp dis8 r16
    \stemUp dis16 \stemUp fis,8 r8 r4 | % 55
    R1 \pageBreak | % 56
    R1*2 _ "Tbn." | % 58
    \stemUp dis'4 -> _\p \stemUp dis8 r16 \stemUp dis16 \stemUp fis,8 r8
    r4 | % 59
    R1*2 \pageBreak | % 61
    R1 _ "Tbn." | % 62
    R1*2 | % 64
    \stemDown b8 -. _\p _\mp ^ "a 2" _\mp r8 \stemUp e,8 -. r16 \stemUp
    e16 -. \stemDown b'8 -. r8 \stemUp e,8 -. r8 | % 65
    \stemDown b'8 -. r8 r4 r2 \pageBreak | % 66
    \stemDown e8 -. ^ "a 2" _\mf _ "Tbn." r8 \stemDown a,8 -. r16
    \stemDown a16 -. \stemDown e'8 -. r8 \stemDown a,8 -. r8 | % 67
    \stemDown g'8 -. r8 r4 r2 | % 68
    \stemDown b,8 -. _\f r8 \stemUp e,8 -. r16 \stemUp e16 -. \stemDown
    b'8 -. r8 \stemUp e,8 -. r8 | % 69
    \stemDown <fis dis'>8 _\ff r8 r4 r2 | \barNumberCheck #70
    R1 \bar "||"
    \pageBreak | % 71
    \key e \major R1*5 \break | % 76
    R1*5 \pageBreak | % 81
    R1*5 \pageBreak | % 86
    R1*4 \pageBreak | \barNumberCheck #90
    R1*6 \pageBreak | % 96
    R1*6 \break | % 102
    R1*5 \pageBreak | % 107
    R1*6 \break | % 113
    R1*5 \pageBreak | % 118
    R1*5 \break | % 123
    R1*5 \pageBreak | % 128
    R1*4 \pageBreak | % 132
    R1*4 \pageBreak | % 136
    R1*3 \bar "||"
    \key g \major R1 \pageBreak | \barNumberCheck #140
    R1*5 \pageBreak | % 145
    R1*5 \pageBreak | \barNumberCheck #150
    R1 _ "Tbn." | % 151
    R1 | % 152
    R1*3 \pageBreak | % 155
    R1*4 \break | % 159
    R1*4 \pageBreak | % 163
    R1*4 \pageBreak | % 167
    R1*4 \pageBreak | % 171
    R1*4 \pageBreak | % 175
    R1*4 _ "Tbn." | % 179
    \stemUp g'16 -> _\mp _\> ^\p r16 r8 \stemUp d16 -> r16 r8 r2 _\p
    \pageBreak | \barNumberCheck #180
    \stemUp a16 -> _ "Tbn." r16 r8 \stemUp d16 -> r16 r8 \stemUp b16 ->
    r16 r8 r4 _\p | % 181
    r8 \stemUp g16 ^\p ^\< r16 \stemUp a16 r16 \stemUp b16 r16 \stemUp c16
    ^\! ^\mp r16 r8 r4 _\mp | % 182
    r2 _\> \stemUp g16 ^\p r16 r8 r4 | % 183
    R1 \pageBreak | % 184
    R1*5 \pageBreak | % 189
    R1*4 _ "Tbn." | % 193
    \stemUp a,4 _\ff ^ "a 2" \stemUp d4 \stemUp fis4 \stemDown a4
    \pageBreak | % 194
    \stemDown <fis d'>4 _ "Tbn." \stemDown <a fis'>4 \stemDown <cis e>8
    r8 r4 | % 195
    R1*3 | % 198
    \stemUp b8 ^\pp ^\ leggieramente r8 \stemUp fis8 r16 \stemUp fis16
    \stemUp b8 r8 \stemUp fis8 r8 | % 199
    \stemUp b8 -> \stemUp e8 -> r4 r2 | \barNumberCheck #200
    R1 \pageBreak | % 201
    \stemUp a,8 ^\p _ "Tbn." r8 \stemUp e8 r16 \stemUp e16 \stemUp a8 r8
    \stemUp e8 r8 | % 202
    \stemUp a8 -> \stemUp d8 -> r4 r2 | % 203
    R1*2 | % 205
    \stemUp d8 _\p _\< r8 \stemUp a8 r16 \stemUp a16 \stemUp d8 r8
    \stemUp a8 r8 \pageBreak | % 206
    \stemUp d8 -> _\! _\mp _\ leggieramente _ "Tbn." \stemUp g8 -> r4 r2
    | % 207
    \stemUp cis,8 ^\mf r8 \stemUp g8 r16 \stemUp g16 \stemUp cis8 r8
    \stemUp g8 r8 | % 208
    \stemUp d'8 -> \stemUp g8 -> r4 r2 | % 209
    R1 | \barNumberCheck #210
    \stemUp e8 r8 \stemUp b8 r16 \stemUp b16 \stemUp e8 r8 \stemUp b8 r8
    \pageBreak | % 211
    \stemUp e8 -> _ "Tbn." \stemUp a8 -> r4 r2 | % 212
    d,1 ^\mf ^\< | % 213
    \stemDown d8 ^\! _\ff ^ "a 2" r8 \stemDown a8 r16 \stemDown a16
    \stemDown d8 r8 \stemDown a8 r8 | % 214
    \stemDown d8 -> \stemDown g8 ~ -> \stemDown g2. | % 215
    \stemDown d8 _\fff r8 \stemDown a8 r16 \stemDown a16 \stemDown d8 r8
    \stemDown a8 r8 \pageBreak | % 216
    \stemDown d8 -> _ "Tbn." \stemDown g8 ~ -> \stemDown g2. | % 217
    \stemDown d8 r8 \stemDown a8 r16 \stemDown a16 \stemDown d8 r8
    \stemDown g8 r16 \stemDown g16 | % 218
    \stemDown d8 r8 \stemDown a8 r16 \stemDown a16 \stemDown d8 r8
    \stemDown g8 r16 \stemDown g16 | % 219
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d4 \stemDown d8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a4 \stemDown a8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d4 \stemDown d8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g4 \stemDown g8 }
    | \barNumberCheck #220
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d4 \stemDown d8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a4 \stemDown a8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d4 \stemDown d8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g4 \stemDown g8 }
    \pageBreak | % 221
    \times 2/3  {
        \stemDown d8 -> _ "Tbn." \stemDown d8 -> r8 }
    r4 r2 | % 222
    R1*3 \pageBreak | % 225
    R1*3 \pageBreak _ "Tbn." | % 228
    R1 _ "Tbn." | % 229
    \stemDown <d g>8 _\fff r8 \stemDown <c fis>8 r8 \stemDown <b g'>8 r8
    \stemDown <a a'>8 r8 | \barNumberCheck #230
    \stemDown <g c>8 r8 \stemDown <g c>8 r16 \stemDown <g c>16 \stemDown
    <fis d'>2 | % 231
    \stemDown <g d'>8 r8 \stemDown <c d>8 r8 \stemDown <b d>8 r8
    \stemDown <a d>8 r8 | % 232
    \stemDown <g g'>2 \stemUp <d b'>8 r8 r4 \pageBreak | % 233
    \stemDown <b' g'>8 _ "Tbn." r8 \stemDown <c d>8 r8 \stemDown <b d>8
    r8 \stemDown <a d>8 r8 | % 234
    \stemDown <g g'>2 \stemDown <g b>8 r8 r4 | % 235
    \stemUp <g, g'>8 -! \stemUp <a a'>8 -! \stemUp <ais ais'>8 -!
    \stemUp <b b'>8 -! \stemDown <g' b>8 r8 r4 | % 236
    \stemDown <c e>8 r8 r4 \stemUp c8 -! \stemUp d8 -! \stemUp e8 -!
    \stemUp fis8 -! | % 237
    \stemUp g8 -! \stemUp fis8 -! \stemUp e8 -! \stemUp d8 -! \stemUp
    cis8 -! \stemUp c8 -! \stemUp b8 -! \stemUp a8 -! \pageBreak | % 238
    \stemUp g4 -> _ "Tbn." \once \omit TupletBracket
    \times 2/3  {
        \stemUp e'8 \stemUp e8 \stemUp e8 }
    \stemUp fis8 \stemUp fis8 r4 | % 239
    \stemUp <d g>8 r8 \stemUp <c fis>8 r8 \stemUp <b g'>8 r8 \stemUp <a
        a'>8 r8 | \barNumberCheck #240
    \stemDown <g c>8 r8 \stemDown <g c>8 r16 \stemDown <g c>16 \stemDown
    <fis d'>2 | % 241
    \stemDown <g d'>8 r8 \stemDown <c d>8 r8 \stemDown <b d>8 r8
    \stemDown <a d>8 r8 | % 242
    \stemDown <g g'>2 \stemUp <d b'>8 r8 r4 \pageBreak | % 243
    \stemDown <b' g'>8 _ "Tbn." r8 \stemDown <c d>8 r8 \stemDown <b d>8
    r8 \stemDown <a d>8 r8 | % 244
    \stemDown <g g'>2 \stemDown <g b>8 r8 r4 | % 245
    \stemUp bes8 r8 r4 \stemUp f8 -! \stemUp c'8 -! \stemUp cis8 -!
    \stemUp d8 -! | % 246
    \stemUp bes8 r8 r4 \stemUp d8 r8 r4 | % 247
    R1 \pageBreak | % 248
    r2 _ "Tbn." r4 \stemDown <b dis>8 r8 | % 249
    \stemDown <b e>8 r8 \stemDown <b e>8 r8 \stemDown <c e>8 r8
    \stemDown <gis e'>8 r8 | \barNumberCheck #250
    \stemDown <a e'>8 r8 \stemDown <bes e>8 r8 \stemUp g8 r8 \stemUp gis8
    r8 | % 251
    \stemUp a8 r8 r4 r2 | % 252
    R1*2 \pageBreak | % 254
    R1 _ "Tbn." | % 255
    \stemDown <d fis>2 _\fff \stemDown <c fis>2 | % 256
    \stemDown <b fis'>8 r8 \stemDown <a g'>8 r8 r2 | % 257
    R1*2 \pageBreak | % 259
    \stemDown <d fis>2 _\fff _ "Tbn." \stemDown <c fis>2 |
    \barNumberCheck #260
    \stemDown <b fis'>8 r8 \stemDown <a g'>8 r8 r2 | % 261
    R1*2 | % 263
    \stemDown <d fis>2 _\fff \stemDown <c fis>2 \pageBreak | % 264
    \stemDown <b fis'>8 _ "Tbn." r8 \stemDown <a g'>8 r8 r2 | % 265
    R1*2 | % 267
    \stemDown <d fis>4 ~ ~ _\fff \stemDown <d fis>8 r8 \stemDown <c fis>4
    ~ ~ \stemDown <c fis>8 r8 | % 268
    \stemDown <b fis'>4 ~ ~ \stemDown <b fis'>8 r8 \stemDown <c g'>4 ~ ~
    \stemDown <c g'>8 r8 \pageBreak | % 269
    \stemDown <cis e>4 ~ ~ _ "Tbn." \stemDown <cis e>8 r8 \stemDown <b
        g'>4 ~ ~ \stemDown <b g'>8 r8 | \barNumberCheck #270
    \stemDown <a dis>4 ~ ~ \stemDown <a dis>8 r8 \stemDown <gis e'>4 ~ ~
    \stemDown <gis e'>8 r8 | % 271
    \stemDown <a f'>4 ~ ~ \stemDown <a f'>8 r8 \stemDown <d fis>4 ~ ~
    \stemDown <d fis>8 r8 | % 272
    \stemDown <as es'>4 ~ ~ \stemDown <as es'>8 r8 \stemDown <gis e'>4 ~
    ~ \stemDown <gis e'>8 r8 | % 273
    \stemDown <cis e>8 r8 \stemDown <d f>8 r8 \stemDown <d g>8 r8
    \stemDown <a f'>8 r8 \pageBreak | % 274
    \stemUp <g a>8 _ "Tbn." r8 \stemUp <fis a>8 r8 \stemUp <g a>8 r8 r4
    | % 275
    \stemDown a4 _\fff ^ "a 2" \stemUp e8. \stemUp e16 \stemDown a4
    \stemUp e4 | % 276
    \stemDown a8 -. \stemDown d8 -. r4 r2 | % 277
    \stemDown a4 \stemUp e8. \stemUp e16 \stemDown a4 \stemUp e4 | % 278
    \stemDown a8 -. \stemDown d8 -. r4 r2 | % 279
    r4 \stemDown a8 -. \stemDown e'8 -. r4 \stemUp d,8 -. \stemUp a'8 -.
    | \barNumberCheck #280
    r4 \stemDown a8 -. \stemDown e'8 -. r4 \stemUp d,8 -. \stemUp a'8 -.
    \pageBreak | % 281
    r4 _ "Tbn." \stemUp e4 -- \stemDown a8 r8 \stemDown a4 -- | % 282
    \stemDown e'8 r8 \stemDown e4 -- \stemDown a8 r8 r4 | % 283
    \stemDown <d, g>8 _\fff r8 \stemDown <c fis>8 r8 \stemDown <b g'>8 r8
    \stemDown <a a'>8 r8 | % 284
    \stemDown <g c>8 r8 \stemDown <g c>8 r16 \stemDown <g c>16 \stemDown
    <fis d'>2 | % 285
    \stemDown <g d'>8 r8 \stemDown <c d>8 r8 \stemDown <b d>8 r8
    \stemDown <a d>8 r8 | % 286
    \stemDown <g g'>2 \stemUp <d b'>8 r8 r4 \pageBreak | % 287
    \stemDown <b' g'>8 _ "Tbn." r8 \stemDown <c d>8 r8 \stemDown <b d>8
    r8 \stemDown <a d>8 r8 | % 288
    \stemDown <g g'>2 \stemDown <g b>8 r8 r4 | % 289
    \stemUp <g, g'>8 -! \stemUp <a a'>8 -! \stemUp <ais ais'>8 -!
    \stemUp <b b'>8 -! \stemDown <g' b>8 r8 r4 | \barNumberCheck #290
    \stemDown <c e>8 r8 r4 \stemUp c8 -! \stemUp d8 -! \stemUp e8 -!
    \stemUp fis8 -! | % 291
    \stemUp g8 -! \stemUp fis8 -! \stemUp e8 -! \stemUp d8 -! \stemUp
    cis8 -! \stemUp c8 -! \stemUp b8 -! \stemUp a8 -! \pageBreak | % 292
    \stemUp g4 -> _ "Tbn." \once \omit TupletBracket
    \times 2/3  {
        \stemUp e'8 \stemUp e8 \stemUp e8 }
    \stemUp fis8 \stemUp fis8 r4 | % 293
    \stemUp <d g>8 r8 \stemUp <c fis>8 r8 \stemUp <b g'>8 r8 \stemUp <a
        a'>8 r8 | % 294
    \stemDown <g c>8 r8 \stemDown <g c>8 r16 \stemDown <g c>16 \stemDown
    <fis d'>2 | % 295
    \stemDown <g d'>8 r8 \stemDown <c d>8 r8 \stemDown <b d>8 r8
    \stemDown <a d>8 r8 | % 296
    \stemDown <g g'>2 \stemUp <d b'>8 r8 r4 \pageBreak | % 297
    \stemDown <b' g'>8 _ "Tbn." r8 \stemDown <c d>8 r8 \stemDown <b d>8
    r8 \stemDown <a d>8 r8 | % 298
    \stemDown <g g'>2 \stemDown <g b>8 r8 r4 | % 299
    \stemUp bes8 r8 r4 \stemUp f8 -! \stemUp c'8 -! \stemUp cis8 -!
    \stemUp d8 -! | \barNumberCheck #300
    \stemUp bes8 r8 r4 \stemUp d8 r8 r4 | % 301
    R1 \pageBreak | % 302
    r2 _ "Tbn." r4 \stemDown <b dis>8 r8 | % 303
    \stemDown <b e>8 r8 \stemDown <b e>8 r8 \stemDown <c e>8 r8
    \stemDown <gis e'>8 r8 | % 304
    \stemDown <g e'>4 ~ -> ~ _\sempre _\fff \stemDown <g e'>8 r8
    \stemDown <g es'>4 ~ -> ~ \stemDown <g es'>8 r8 | % 305
    \stemDown <g d'>4 ~ -> ~ \stemDown <g d'>8 r8 \stemDown <g cis>4 ~
    -> ~ \stemDown <g cis>8 r8 | % 306
    \stemDown <g c>4 ~ -> ~ \stemDown <g c>8 r8 \stemDown <g cis>4 ~ ->
    ~ \stemDown <g cis>8 r8 | % 307
    \stemDown <g d'>4 ~ -> ~ \stemDown <g d'>8 r8 \stemDown <g dis'>4 ~
    -> ~ \stemDown <g dis'>8 r8 \pageBreak | % 308
    \stemDown <g e'>4 ~ -> ~ _ "Tbn." \stemDown <g e'>8 r8 \stemDown
    <gis e'>4 ~ -> ~ \stemDown <gis e'>8 r8 | % 309
    \stemDown <a e'>4 ~ -> ~ \stemDown <a e'>8 r8 \stemDown <a e'>4 ~ ->
    ~ \stemDown <a e'>8 r8 | \barNumberCheck #310
    \stemDown <a c>4 ~ -> ~ \stemDown <a c>8 r8 \stemDown <a c>4 ~ -> ~
    \stemDown <a c>8 r8 | % 311
    \stemDown <a c>4 ~ -> ~ \stemDown <a c>8 r8 \stemDown <a c>4 ~ -> ~
    \stemDown <a c>8 r8 | % 312
    \stemDown <b d>4. _\ffff \stemDown <b d>8 \stemDown <b es>4.
    \stemDown <b es>8 | % 313
    \stemDown <b e>4. \stemDown <b e>8 \stemDown <b es>4. \stemDown <b
        es>8 \pageBreak | % 314
    \stemDown <b d>2 _ "Tbn." \stemDown b4 -> ^ "a 2" \stemDown d4 -> | % 315
    \stemDown fis4 -> \stemDown a4 -> \stemDown d,8 -> r8 r4 | % 316
    R1*4 \pageBreak | \barNumberCheck #320
    \stemUp g,8 _\f ^ "a 2" _ "Tbn." _\< r8 \stemUp d8 r16 \stemUp d16
    \stemUp g8 r8 \stemUp d8 r8 | % 321
    \stemDown g8 \stemDown c8 ~ \stemDown c4 ~ \stemDown c8 r8 _\! r4 | % 322
    \stemDown <g g'>8 _\ff _\< r8 \stemUp <d d'>8 r16 \stemUp <d d'>16
    \stemDown <g g'>8 r8 \stemUp <d d'>8 r8 | % 323
    \stemUp g'8 \stemUp c,8 ~ \stemUp c4 ~ \stemUp c8 r8 _\! r4 | % 324
    \stemUp <fis, b>8 _\fff r8 \stemDown <g b>16 r16 r8 r2 \pageBreak | % 325
    R1 _ "Tbn." | % 326
    r4 \stemUp <c, c'>4 ~ ~ \stemUp <c c'>8 r8 r4 | % 327
    r4 \stemUp <fis b>4 ~ ~ \stemUp <fis b>8 r8 r4 \pageBreak | % 328
    r4 \stemUp <e cis'>4 ~ ~ _ "Tbn." \stemUp <e cis'>8 r8 r4 | % 329
    r4 \stemDown <d' fis>4 ~ ~ \stemDown <d fis>8 r8 \stemDown <a d>8 r8
    | \barNumberCheck #330
    \stemDown <b d>8 _\sempre _\fff r8 \stemUp a8 r8 \stemDown <g b>8 r8
    \stemDown <g c>8 r8 | % 331
    \stemDown <g b>2 \stemDown <gis b>8 r8 \stemUp a8 r8 \pageBreak | % 332
    \stemDown <b d>8 _ "Tbn." r8 \stemUp a8 r8 \stemDown <g b>8 r8
    \stemDown <g c>8 r8 | % 333
    \stemDown <g b>2 \stemDown <gis b>8 r8 \stemUp a8 r8 | % 334
    \stemDown <b d>8 r8 \stemDown <a d>8 r8 \stemDown <g e'>8 r8
    \stemDown <a fis'>8 r8 | % 335
    \stemDown <b g'>8 r8 \stemDown <a d>8 r8 \stemDown <g e'>8 r8
    \stemDown <a fis'>8 r8 \pageBreak | % 336
    \stemDown <b g'>8 _ "Tbn." r8 \stemDown <fis' a>8 r8 \stemDown <b,
        g'>8 r8 \stemDown <fis' a>8 r8 | % 337
    \stemDown <b, g'>8 r8 \stemDown <fis' a>8 r8 \stemDown <b, g'>8 r8
    \stemDown <fis' a>8 r8 | % 338
    \stemDown <b, g'>8 r8 r8 \stemDown <g b>8 \stemDown <g b>8 r8 r8
    \stemDown <b d>8 | % 339
    \stemDown <b d>8 r8 r8 \stemDown <g b>8 \stemDown <g b>8 r8 r8
    \stemDown <b d>8 | \barNumberCheck #340
    \stemUp d8 \stemUp g8 \stemUp fis8 \stemUp e8 \stemUp d8 \stemUp c8
    \stemUp b8 \stemUp a8 \pageBreak | % 341
    \stemUp g8 _ "Tbn." r8 r4 \stemDown <a fis'>8 r8 r4 | % 342
    \stemDown <g b>8 r8 \stemDown <g b>8 r8 r4 \stemDown <g b>8 r8 | % 343
    r4 \stemDown <g b>8 r8 r4 \stemDown <g b>8 r8 | % 344
    \stemDown <g b>8 r8 \stemUp <d b'>8 r8 \stemUp <d b'>8 r8 \stemUp <d
        g>8 r8 | % 345
    <b d>1 ~ ~ | % 346
    \stemUp <b d>2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp <b d>8 \stemUp <b d>8 \stemUp <b d>8 }
    | % 347
    \stemUp <b d>8 r8 r4 r2 \bar "|."
    }

PartPOneOneVoiceTwo =  \relative e {
    \clef "tenor" \time 4/4 \key g \major | % 1
     \once \override NoteHead.style = ##f e1 s1*3 \pageBreak s1*3 \bar
    "||"
    s1*2 \pageBreak s1*3 | % 13
    \stemDown a8 -. r8 \stemDown e8 -. r16 \stemDown e16 -. \stemDown a8
    -. r8 \stemDown e8 -. r8 | % 14
    \stemDown a16 -. r16 \stemDown d8 ~ \stemDown d4 ~ \stemDown d8 _\!
    _\p r8 r4 \break s1*5 \pageBreak s1*4 \break s1*4 \pageBreak s1*4
    \pageBreak s1*4 \pageBreak s1*5 \pageBreak | % 41
    r2 \stemDown a16 -> r16 r8 \stemDown e16 -> r16 r8 | % 42
    r2 r4 \stemDown d16 r16 \stemDown e16 r16 | % 43
    \stemDown fis16 r16 r8 r4 r4 \stemDown b16 r16 \stemDown a16 r16 | % 44
    \stemDown d16 r16 r8 \stemDown g,16 r16 _\! r8 r2 s1 \pageBreak s1*2
    | % 48
    \time 12/8  s2. \stemDown ais8 \stemDown ais8 \stemDown ais8 s4. | % 49
    \stemDown fis2. ~ \stemDown fis8 _\! r8*2/3 r8*2/3 r4.*2/3 s1*5/24 |
    \barNumberCheck #50
    \stemDown fis2. ~ \stemDown fis8 _\! r8*2/3 r8*2/3 r4.*2/3 s1*5/24
    \pageBreak s2*9 | % 54
    \numericTimeSignature\time 4/4  R1 s1 \pageBreak s1*2 | % 58
    R1 s1*2 \pageBreak s1 | % 62
    \stemDown g8 -. r8 \stemDown c,8 -. r16 \stemDown c16 -. \stemDown
    g'8 -. r8 \stemDown c,8 -. r8 | % 63
    \stemDown fis8 -. r8 r4 r2 s1*2 \pageBreak s1*5 \bar "||"
    \pageBreak | % 71
    \key e \major s1*5 \break s1*5 \pageBreak s1*5 \pageBreak s1*4
    \pageBreak s1*6 \pageBreak s1*6 \break s1*5 \pageBreak s1*6 \break
    s1*5 \pageBreak s1*5 \break s1*5 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1*3 \bar "||"
    \key g \major s1 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1 | % 151
    \stemDown a8 -. r8 \stemDown e8 -. r16 \stemDown e16 -. \stemDown a8
    -. r8 \stemDown e8 -. r8 | % 152
    \stemDown a16 -. r16 \stemDown d8 ~ \stemDown d4 ~ \stemDown d8 _\!
    _\p r8 r4 s1*2 \pageBreak s1*4 \break s1*4 \pageBreak s1*4
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*4 | % 179
    r2 \stemDown a16 -> r16 r8 \stemDown e16 -> r16 r8 \pageBreak |
    \barNumberCheck #180
    r2 r4 \stemDown d16 r16 \stemDown e16 r16 | % 181
    \stemDown fis16 r16 r8 r4 r4 \stemDown b16 r16 \stemDown a16 r16 | % 182
    \stemDown d16 r16 r8 \stemDown g,16 r16 _\! r8 r2 s1 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*4 | % 198
    R1*2 s1 \pageBreak | % 201
    R1*2 s1*2 | % 205
    a,1 \pageBreak | % 206
    \stemDown e'8 r8 \stemDown b8 r16 \stemDown b16 \stemDown e8 r8
    \stemDown b8 r8 | % 207
    \stemDown e8 -> \stemDown a8 -> r4 r2 | % 208
    R1 | % 209
    \stemDown d8 r8 \stemDown a8 r16 \stemDown a16 \stemDown d8 r8
    \stemDown a8 r8 | \barNumberCheck #210
    \stemDown d8 -> \stemDown g8 -> r4 r2 \pageBreak | % 211
    R1*2 s1*3 \pageBreak s1*5 \pageBreak s1*4 \pageBreak | % 225
     \once \override NoteHead.style = ##f d1 s1*2 \pageBreak s1*5
    \pageBreak s2*7 r2 | % 237
    R1 \pageBreak | % 238
    \stemDown b4 -> \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 \stemDown b8 \stemDown b8 }
    \stemDown dis8 \stemDown d8 s4 | % 239
    R1 s1*3 \pageBreak s1*2 | % 245
    \stemDown es,8 -! \stemDown f8 -! \stemDown g8 -! \stemDown as8 -!
    \stemDown bes8 -! r8 r4 | % 246
    \stemDown g8 -! \stemDown f8 -! \stemDown g8 -! \stemDown a8 -!
    \stemDown bes8 -! \stemDown b8 -! s4*5 \pageBreak s2*5 \stemDown b8
    s8 \stemDown b8 s8 | % 251
    \stemDown a8 s8*23 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*7 \pageBreak s1*6 \pageBreak s2*7 r2 | % 291
    R1 \pageBreak | % 292
    \stemDown b4 -> \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 \stemDown b8 \stemDown b8 }
    \stemDown dis8 \stemDown d8 s4 | % 293
    R1 s1*3 \pageBreak s1*2 | % 299
    \stemDown es,8 -! \stemDown f8 -! \stemDown g8 -! \stemDown as8 -!
    \stemDown bes8 -! r8 r4 | \barNumberCheck #300
    \stemDown g8 -! \stemDown f8 -! \stemDown g8 -! \stemDown a8 -!
    \stemDown bes8 -! \stemDown b8 -! s4*5 \pageBreak s1*6 \pageBreak
    s1*6 \pageBreak s1*6 \pageBreak s1*3 | % 323
    \stemDown g8 \stemDown c8 ~ \stemDown c4 ~ \stemDown c8 s8*11
    \pageBreak s1*3 \pageBreak s4*9 \stemDown a8 s8*11 \stemDown a8 s8
    \pageBreak s4 \stemDown a8 s8*11 \stemDown a8 s8*17 \pageBreak s1*4
    | \barNumberCheck #340
    \stemDown b8 \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown d8
    \stemDown c'8 \stemDown b8 \stemDown a8 \pageBreak | % 341
    \stemDown g8 s8*55 \bar "|."
    }

PartPOneTwoVoiceOne =  \relative a, {
    \clef "bass" \time 4/4 \key g \major | % 1
    R1*4 \pageBreak | % 5
    R1*3 \bar "||"
    R1*2 \pageBreak | \barNumberCheck #10
    R1*3 | % 13
    \stemUp a8 -. _\mp r8 \stemUp e8 -. r16 \stemUp e16 -. \stemUp a8 -.
    r8 \stemUp e8 -. r8 | % 14
    \stemUp a16 -. _\> r16 \stemUp d8 ~ \stemDown d4 ~ \stemDown d8 _\!
    _\p r8 r4 \break | % 15
    R1*5 \pageBreak | \barNumberCheck #20
    R1*4 \break | % 24
    R1*4 \pageBreak | % 28
    R1*4 \pageBreak | % 32
    R1*4 \pageBreak | % 36
    R1*5 \pageBreak | % 41
    R1*5 \pageBreak | % 46
    R1*2 | % 48
    \time 12/8  r2.*2/3 r4.*2/3 \stemUp ais8 _\f \stemUp ais8 \stemUp
    ais8 s4. | % 49
    fis1. ~ | \barNumberCheck #50
    fis1. ~ \pageBreak | % 51
    \stemUp fis8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 52
    r1 s2 | % 53
    \numericTimeSignature\time 4/4  \stemUp b4 -> _\pp \stemUp b8 r16
    \stemUp b16 \stemUp fis8 r8 r4 | % 54
    R1*2 \pageBreak | % 56
    R1 | % 57
    \stemUp b4 -> _\p \stemUp b8 r16 \stemUp b16 \stemUp fis8 r8 r4 | % 58
    R1*3 \pageBreak | % 61
    R1 | % 62
    \stemDown g'8 -. _\p ^ "a 2" r8 \stemUp c,8 -. r16 \stemUp c16 -.
    \stemDown g'8 -. r8 \stemUp c,8 -. r8 | % 63
    \stemDown fis8 -. r8 r4 r2 | % 64
    R1 | % 65
    \stemUp b,8 -. _\mf r8 \stemUp fis8 -. r16 \stemUp fis16 -. \stemUp
    b8 -. r8 \stemUp fis8 -. r8 \pageBreak | % 66
    \stemUp b8 -. \stemUp e8 -. r4 r2 | % 67
    \stemUp b8 -. _\f r8 \stemUp fis8 -. r16 \stemUp fis16 -. \stemUp b8
    -. r8 \stemUp fis8 -. r8 | % 68
    \stemUp b8 -. \stemUp e8 -. r4 r2 | % 69
    \stemUp b8 _\ff r8 r4 r2 | \barNumberCheck #70
    R1 \bar "||"
    \pageBreak | % 71
    \key e \major R1*5 \break | % 76
    R1*5 \pageBreak | % 81
    R1*5 \pageBreak | % 86
    R1*2 _ "Tbn." | % 88
    \stemUp c8 _\mf r8 r4 \stemDown e8 _\f r8 r4 | % 89
    R1 \pageBreak | \barNumberCheck #90
    R1*6 \pageBreak | % 96
    R1*6 \break | % 102
    R1*5 \pageBreak | % 107
    R1*6 \break | % 113
    R1*5 \pageBreak | % 118
    R1*5 \break | % 123
    R1*5 \pageBreak | % 128
    R1 _ "Tbn." | % 129
    \stemUp e,8 _\f r8 r4 \stemUp g8 r8 r4 | \barNumberCheck #130
    \stemUp c8 r8 r4 \stemDown g'8 r8 r4 | % 131
    R1 \pageBreak | % 132
    R1 _ "Tbn." | % 133
    \stemUp e,8 _\f r8 r4 \stemUp g8 r8 r4 | % 134
    \stemUp c8 r8 r4 \stemDown g'8 r8 r4 | % 135
    R1 \pageBreak | % 136
    R1*3 \bar "||"
    \key g \major R1 \pageBreak | \barNumberCheck #140
    R1*5 \pageBreak | % 145
    R1*5 \pageBreak | \barNumberCheck #150
    R1 | % 151
    \stemUp a,8 -. _\mp r8 \stemUp e8 -. r16 \stemUp e16 -. \stemUp a8
    -. r8 \stemUp e8 -. r8 | % 152
    \stemUp a16 -. _\> r16 \stemUp d8 ~ \stemDown d4 ~ \stemDown d8 _\!
    _\p r8 r4 | % 153
    R1*2 \pageBreak | % 155
    R1*4 \break | % 159
    R1*4 \pageBreak | % 163
    R1*4 \pageBreak | % 167
    R1*4 \pageBreak | % 171
    R1*4 \pageBreak | % 175
    R1*5 \pageBreak | \barNumberCheck #180
    R1*4 \pageBreak | % 184
    R1*5 \pageBreak | % 189
    R1*3 | % 192
    r2 r4 \stemUp bes4 _\ff | % 193
    \stemUp a4 \stemDown d4 \stemDown fis2 \pageBreak | % 194
    \stemDown d4 \stemDown fis4 \stemDown a8 r8 r4 | % 195
    R1*6 \pageBreak | % 201
    R1*4 | % 205
    \stemDown d,8 -. _\p -\markup{ \italic {leggieramente} } _\< r8
    \stemUp a8 r16 \stemUp a16 \stemDown d8 r8 \stemUp a8 r8 \pageBreak
    | % 206
    \stemDown d8 -> _\! _\mp \stemDown g8 -> r4 \stemUp a,2 ~ _\markup{
        \small\italic {cresc.} } \startTrillSpan | % 207
    a1 ~ | % 208
    a1 ~ | % 209
    a1 ~ | \barNumberCheck #210
    \stemUp a8 \stopTrillSpan _\f r8 r4 r2 \pageBreak | % 211
    R1 | % 212
    \stemDown d32 _\mf _\< r32 r16 r8 r4 r2 | % 213
    \stemDown d8 _\! _\ff r8 \stemUp a8 r16 \stemUp a16 \stemDown d8 r8
    \stemUp a8 r8 | % 214
    \stemDown d8 -> \stemDown g8 ~ -> \stemDown g2. | % 215
    \stemDown d8 _\fff r8 \stemUp a8 r16 \stemUp a16 \stemDown d8 r8
    \stemUp a8 r8 \pageBreak | % 216
    \stemDown d8 -> \stemDown g8 ~ -> \stemDown g2. | % 217
    \stemDown d8 r8 \stemUp a8 r16 \stemUp a16 \stemDown d8 r8 \stemDown
    g8 r16 \stemDown g16 | % 218
    \stemDown d8 r8 \stemUp a8 r16 \stemUp a16 \stemDown d8 r8 \stemDown
    g8 r16 \stemDown g16 | % 219
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d4 \stemDown d8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a4 \stemUp a8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d4 \stemDown d8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g4 \stemDown g8 }
    | \barNumberCheck #220
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d4 \stemDown d8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a4 \stemUp a8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d4 \stemDown d8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g4 \stemDown g8 }
    \pageBreak | % 221
    \times 2/3  {
        \stemDown d8 -> \stemDown d8 -> r8 }
    r4 r2 | % 222
    R1*3 \pageBreak | % 225
    R1*3 \pageBreak | % 228
    R1 | % 229
    \stemDown b'8 _\fff r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8
    r8 | \barNumberCheck #230
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 \stemUp c8 r8 | % 231
    \stemUp b8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis8 r8 | % 232
    \stemUp e8 r8 \stemUp es8 r8 \stemUp d8 r8 r4 \pageBreak | % 233
    \stemDown b''8 r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8 r8
    | % 234
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 r4 | % 235
    \stemUp b8 r8 r4 \stemDown e8 r8 r4 | % 236
    \stemDown g8 r8 r4 \stemDown c8 -! \stemDown d8 -! \stemDown e8 -!
    \stemDown fis8 -! | % 237
    \stemDown g8 -! \stemDown fis8 -! \stemDown e8 -! \stemDown d8 -!
    \stemDown cis8 -! \stemDown c8 -! \stemDown b8 -! \stemDown a8 -!
    \pageBreak | % 238
    \stemUp g,4 -> \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 \stemUp g8 \stemUp g8 }
    \stemUp b8 \stemUp d8 r4 | % 239
    \stemDown b'8 r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8 r8 |
    \barNumberCheck #240
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 \stemUp c8 r8 | % 241
    \stemUp b8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis8 r8 | % 242
    \stemUp e8 r8 \stemUp es8 r8 \stemUp d8 r8 r4 \pageBreak | % 243
    \stemDown b''8 r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8 r8
    | % 244
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 r4 | % 245
    \stemUp g,8 -! \stemUp f8 -! \stemUp g8 -! \stemUp as8 -! \stemUp
    bes8 -! \stemUp c8 -! \stemUp cis8 -! \stemUp d8 -! | % 246
    \stemDown es8 r8 r4 \stemUp g,8 r8 r4 | % 247
    r4 \stemUp b8 r16 \stemUp c16 \stemUp cis8 r8 \stemDown dis8 r8
    \pageBreak | % 248
    \stemDown e8 r8 \stemUp cis8 r16 \stemUp dis16 \stemDown e8 r8
    \stemDown fis8 r8 | % 249
    \stemDown g8 r8 \stemDown gis8 r8 \stemDown a8 r8 \stemUp b,8 r8 |
    \barNumberCheck #250
    \stemUp c8 r8 \stemUp cis8 r8 \stemDown d8 r8 \stemDown e8 r8 | % 251
    \stemDown f8 r8 r4 r2 | % 252
    R1*2 \pageBreak | % 254
    R1*5 \pageBreak | % 259
    R1 | \barNumberCheck #260
    r2 \stemUp b,2 ~ _\f | % 261
    b1 ~ _\< | % 262
    \stemUp b2. ~ _\! _\ff _\> \stemUp b8 _\! r8 | % 263
    R1 \pageBreak | % 264
    R1*4 | % 268
    r2 \stemDown bes'4 ~ _\fff \stemDown bes8 r8 \pageBreak | % 269
    \stemDown a4 ~ \stemDown a8 r8 \stemDown g4 ~ \stemDown g8 r8 |
    \barNumberCheck #270
    \stemDown fis4 ~ \stemDown fis8 r8 \stemDown e4 ~ \stemDown e8 r8 | % 271
    \stemDown es4 ~ \stemDown es8 r8 \stemDown d4 ~ \stemDown d8 r8 | % 272
    \stemUp cis4 ~ \stemUp cis8 r8 \stemUp b4 ~ \stemUp b8 r8 | % 273
    \stemUp a8 r8 \stemDown as'8 r8 \stemDown g8 r8 \stemDown f8 r8
    \pageBreak | % 274
    \stemDown e8 r8 \stemDown d8 r8 \stemUp c8 r8 r4 | % 275
    \stemDown e4 _\fff \stemUp a,8. \stemUp a16 \stemDown e'4 \stemUp a,4
    | % 276
    \stemDown d8 -. \stemDown a'8 -. r4 r2 | % 277
    \stemDown e4 \stemUp a,8. \stemUp a16 \stemDown e'4 \stemUp a,4 | % 278
    \stemDown d8 -. \stemDown a'8 -. r4 r2 | % 279
    r4 \stemDown e8 -. \stemDown a8 -. r4 \stemUp a,8 -. \stemUp d8 -. |
    \barNumberCheck #280
    r4 \stemDown e8 -. \stemDown a8 -. r4 \stemUp a,8 -. \stemUp d8 -.
    \pageBreak | % 281
    r4 \stemUp a4 -- \stemDown d8 r8 \stemDown d4 -- | % 282
    \stemDown a'8 r8 \stemDown a4 -- \stemDown d8 r8 \stemDown c8 r8 | % 283
    \stemDown b8 _\fff r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8
    r8 | % 284
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 \stemUp c8 r8 | % 285
    \stemUp b8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis8 r8 | % 286
    \stemUp e8 r8 \stemUp es8 r8 \stemUp d8 r8 r4 \pageBreak | % 287
    \stemDown b''8 r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8 r8
    | % 288
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 r4 | % 289
    \stemUp b8 r8 r4 \stemDown e8 r8 r4 | \barNumberCheck #290
    \stemDown g8 r8 r4 \stemDown c8 -! \stemDown d8 -! \stemDown e8 -!
    \stemDown fis8 -! | % 291
    \stemDown g8 -! \stemDown fis8 -! \stemDown e8 -! \stemDown d8 -!
    \stemDown cis8 -! \stemDown c8 -! \stemDown b8 -! \stemDown a8 -!
    \pageBreak | % 292
    \stemUp g,4 -> \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 \stemUp g8 \stemUp g8 }
    \stemUp b8 \stemUp d8 r4 | % 293
    \stemDown b'8 r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8 r8 | % 294
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 \stemUp c8 r8 | % 295
    \stemUp b8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis8 r8 | % 296
    \stemUp e8 r8 \stemUp es8 r8 \stemUp d8 r8 r4 \pageBreak | % 297
    \stemDown b''8 r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8 r8
    | % 298
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 r4 | % 299
    \stemUp g,8 -! \stemUp f8 -! \stemUp g8 -! \stemUp as8 -! \stemUp
    bes8 -! \stemUp c8 -! \stemUp cis8 -! \stemUp d8 -! |
    \barNumberCheck #300
    \stemDown es8 r8 r4 \stemUp g,8 r8 r4 | % 301
    r4 \stemUp b8 r16 \stemUp c16 \stemUp cis8 r8 \stemDown dis8 r8
    \pageBreak | % 302
    \stemDown e8 r8 \stemUp cis8 r16 \stemUp dis16 \stemDown e8 r8
    \stemDown fis8 r8 | % 303
    \stemDown g8 r8 \stemDown gis8 r8 \stemDown a8 r8 \stemUp b,8 r8 | % 304
    \stemUp c4 ~ -> _\sempre _\fff \stemUp c8 r8 \stemUp cis4 ~ ->
    \stemUp cis8 r8 | % 305
    \stemDown d4 ~ -> \stemDown d8 r8 \stemDown es4 ~ -> \stemDown es8 r8
    | % 306
    \stemDown e4 ~ -> \stemDown e8 r8 \stemDown es4 ~ -> \stemDown es8 r8
    | % 307
    \stemDown d4 ~ -> \stemDown d8 r8 \stemUp cis4 ~ -> \stemUp cis8 r8
    \pageBreak | % 308
    \stemUp c4 ~ -> \stemUp c8 r8 \stemUp b4 ~ -> \stemUp b8 r8 | % 309
    \stemUp a4 ~ -> \stemUp a8 r8 \stemDown g'4 ~ -> \stemDown g8 r8 |
    \barNumberCheck #310
    \stemDown fis4 ~ -> \stemDown fis8 r8 \stemDown f4 ~ -> \stemDown f8
    r8 | % 311
    \stemDown e4 ~ -> \stemDown e8 r8 \stemDown es4 ~ -> \stemDown es8 r8
    | % 312
    \stemDown d4. _\ffff \stemDown d8 \stemUp cis4. \stemUp cis8 | % 313
    \stemUp c4. \stemUp c8 \stemUp cis4. \stemUp cis8 \pageBreak | % 314
    \stemDown d4 -> \stemDown g4 -> \stemUp b,4 -> \stemDown d4 -> | % 315
    \stemDown fis4 -> \stemDown a4 -> \stemDown d8 -> r8 r4 | % 316
    R1*2 | % 318
    \stemUp g,,8 _\mf _\< r8 \stemUp d8 r16 \stemUp d16 \stemUp g8 r8
    \stemUp d8 r8 | % 319
    \stemUp g8 \stemUp c8 ~ \stemUp c4 ~ \stemUp c8 r8 _\! r4 \pageBreak
    | \barNumberCheck #320
    \stemUp g8 _\f _\< r8 \stemDown d'8 r16 \stemDown d16 \stemUp g,8 r8
    \stemDown d'8 r8 | % 321
    \stemDown g8 \stemDown c,8 ~ \stemUp c4 ~ \stemUp c8 r8 _\! r4 | % 322
    \stemUp g8 _\ff _\< r8 \stemDown d'8 r16 \stemDown d16 \stemUp g,8 r8
    \stemDown d'8 r8 | % 323
    \stemDown g8 \stemDown c,8 ~ \stemUp c4 ~ \stemUp c8 r8 _\! r4 | % 324
    \stemUp b8 _\fff r8 \stemDown e16 r16 r8 r2 \pageBreak | % 325
    R1*2 | % 327
    r4 \stemDown dis4 ~ \stemDown dis8 r8 r4 \pageBreak | % 328
    r4 \stemUp a4 ~ \stemUp a8 r8 r4 | % 329
    r4 \stemUp a8 r8 \stemDown d8 r8 \stemDown fis8 r8 | \barNumberCheck
    #330
    \stemDown g16 _\sempre _\fff r16 r8 \stemDown fis16 r16 r8 \stemDown
    e16 r16 r8 \stemDown es16 r16 r8 | % 331
    \stemDown d16 r16 r8 \stemDown e16 r16 r8 \stemDown f16 r16 r8
    \stemDown fis16 r16 r8 \pageBreak | % 332
    \stemDown g16 r16 r8 \stemDown fis16 r16 r8 \stemDown e16 r16 r8
    \stemDown es16 r16 r8 | % 333
    \stemDown d16 r16 r8 \stemDown e16 r16 r8 \stemDown f16 r16 r8
    \stemDown fis16 r16 r8 | % 334
    \stemDown g16 r16 r8 \stemDown fis16 r16 r8 \stemDown e16 r16 r8
    \stemDown d16 r16 r8 | % 335
    \stemDown g16 r16 r8 \stemDown fis16 r16 r8 \stemDown e16 r16 r8
    \stemDown d16 r16 r8 \pageBreak | % 336
    \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown g8
    \stemDown fis8 \stemDown e8 \stemDown d8 | % 337
    \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown g8
    \stemDown fis8 \stemDown e8 \stemDown d8 | % 338
    \stemDown g8 r8 r8 \stemUp g,8 \stemUp g8 r8 r8 \stemUp g8 | % 339
    \stemUp g8 r8 r8 \stemUp g8 \stemUp g8 r8 r8 \stemUp g8 |
    \barNumberCheck #340
    \stemUp g8 \stemUp g'8 \stemUp fis8 \stemUp e8 \stemUp d8 \stemUp c8
    \stemUp b8 \stemUp a8 \pageBreak | % 341
    \stemUp g8 \stemUp fis'8 \stemUp e8 \stemUp es8 \stemUp d8 \stemUp c8
    \stemUp b8 \stemUp a8 | % 342
    \stemUp g8 r8 \stemUp g8 r8 r4 \stemUp g8 r8 | % 343
    r4 \stemUp g8 r8 r4 \stemUp g8 r8 | % 344
    \stemUp g8 r8 \stemUp g8 r8 \stemUp g8 r8 \stemUp g8 r8 | % 345
    g1 ~ | % 346
    \stemUp g2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 \stemUp g8 \stemUp g8 }
    | % 347
    \stemUp g8 r8 r4 r2 \bar "|."
    }

PartPOneTwoVoiceTwo =  \relative e {
    \clef "bass" \time 4/4 \key g \major | % 1
     \once \override NoteHead.style = ##f e1 s1*3 \pageBreak s1*3 \bar
    "||"
    s1*2 \pageBreak s1*5 \break s1*5 \pageBreak s1*4 \break s1*4
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*2 | % 48
    \time 12/8  s2*9 \pageBreak s1*3 | % 53
    \numericTimeSignature\time 4/4  s1*3 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \bar "||"
    \pageBreak | % 71
    \key e \major s1*5 \break s1*5 \pageBreak s1*5 \pageBreak s1*4
    \pageBreak s1*6 \pageBreak s1*6 \break s1*5 \pageBreak s1*6 \break
    s1*5 \pageBreak s1*5 \break s1*5 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1*3 \bar "||"
    \key g \major s1 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*4 \break s1*4 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1*4 \pageBreak s1*5 \pageBreak s1*4 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*7 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*4 \pageBreak | % 225
     \once \override NoteHead.style = ##f d1 s1*2 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*6
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*6
    \pageBreak s1*5 \pageBreak s1*3 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1*5 \pageBreak s1*7 \bar "|."
    }

PartPOneThreeVoiceOne =  \relative b, {
    \clef "bass" \time 4/4 \key g \major | % 1
    R1*4 \pageBreak | % 5
    R1*3 \bar "||"
    R1*2 \pageBreak | \barNumberCheck #10
    R1*5 \break | % 15
    R1*5 \pageBreak | \barNumberCheck #20
    R1*4 \break | % 24
    R1*4 \pageBreak | % 28
    R1*4 \pageBreak | % 32
    R1*4 \pageBreak | % 36
    R1*5 \pageBreak | % 41
    R1*5 \pageBreak | % 46
    R1*5 \pageBreak | % 51
    R1*5 \pageBreak | % 56
    R1*5 \pageBreak | % 61
    \stemUp b8 -. _\p r8 \stemUp fis8 -. r16 \stemUp fis16 -. \stemUp b8
    -. r8 \stemUp fis8 -. r8 | % 62
    \stemUp b8 -. \stemUp e8 -. r4 r2 | % 63
    \stemUp b8 -. _\mp r8 \stemUp fis8 -. r16 \stemUp fis16 -. \stemUp b8
    -. r8 \stemUp fis8 -. r8 | % 64
    \stemUp b8 -. \stemUp e8 -. r4 r2 | % 65
    \stemUp b,8 -. _\mf r8 \stemUp fis'8 -. r16 \stemUp fis16 -. \stemUp
    b,8 -. r8 \stemUp fis'8 -. r8 \pageBreak | % 66
    \stemUp b,8 -. \stemUp e8 -. r4 r2 | % 67
    \stemUp b8 -. _\f r8 \stemUp fis'8 -. r16 \stemUp fis16 -. \stemUp
    b,8 -. r8 \stemUp fis'8 -. r8 | % 68
    \stemUp b,8 \stemUp e8 r4 r2 | % 69
    \stemUp b8 _\ff r8 r4 r2 | \barNumberCheck #70
    R1 \bar "||"
    \pageBreak | % 71
    \key e \major R1*5 \break | % 76
    R1*5 \pageBreak | % 81
    R1*5 \pageBreak | % 86
    R1 | % 87
    \stemUp e8 _\mf _\< r8 r4 \stemUp g8 r8 r4 | % 88
    \stemUp c,8 r8 r4 \stemUp e8 _\! _\f r8 r4 | % 89
    R1 \pageBreak | \barNumberCheck #90
    R1*6 \pageBreak | % 96
    R1*6 \break | % 102
    R1*5 \pageBreak | % 107
    R1*6 \break | % 113
    R1*5 \pageBreak | % 118
    R1*5 \break | % 123
    R1*5 \pageBreak | % 128
    R1*4 \pageBreak | % 132
    R1*4 \pageBreak | % 136
    R1*3 \bar "||"
    \key g \major R1 \pageBreak | \barNumberCheck #140
    R1*5 \pageBreak | % 145
    R1*5 \pageBreak | \barNumberCheck #150
    R1*5 \pageBreak | % 155
    R1*4 \break | % 159
    R1*4 \pageBreak | % 163
    R1*4 \pageBreak | % 167
    R1*4 \pageBreak | % 171
    R1*4 \pageBreak | % 175
    R1*5 \pageBreak | \barNumberCheck #180
    R1*4 \pageBreak | % 184
    R1*5 \pageBreak | % 189
    R1*4 | % 193
    a1 ~ \pageBreak | % 194
    \stemUp a2 ~ \stemUp a8 r8 r4 | % 195
    R1*6 \pageBreak | % 201
    R1*2 | % 203
    a,1 ~ _\pp | % 204
    a1 ~ _\< | % 205
    a1 ( _\! _\p _\< \pageBreak | % 206
    \stemUp a'2 ) _\! _\mp \stemUp a,2 ~ _\markup{ \small\italic
        {cresc.} } \startTrillSpan | % 207
    a1 ~ | % 208
    a1 ~ | % 209
    a1 ~ | \barNumberCheck #210
    \stemUp a8 \stopTrillSpan _\f r8 r4 r2 \pageBreak | % 211
    R1 | % 212
    a1 ~ _\f _\< | % 213
    a1 ~ _\! _\ff | % 214
    a1 ~ | % 215
    a1 ~ \pageBreak | % 216
    a1 ~ | % 217
    a1 ~ | % 218
    a1 ~ | % 219
    a1 ~ | \barNumberCheck #220
    a1 \pageBreak | % 221
    \times 2/3  {
        \stemUp a8 -> \stemUp a8 -> r8 }
    r4 r2 | % 222
    R1*3 \pageBreak | % 225
    R1*3 \pageBreak | % 228
    R1 | % 229
    \stemUp b'8 _\fff r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis8 r8 |
    \barNumberCheck #230
    \stemUp e8 r8 \stemUp es8 r8 \stemUp d8 r8 \stemUp c8 r8 | % 231
    \stemUp b8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis'8 r8 | % 232
    \stemUp e8 r8 \stemUp es8 r8 \stemUp d8 r8 r4 \pageBreak | % 233
    \stemUp b'8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis8 r8 | % 234
    \stemUp e8 r8 \stemUp es8 r8 \stemUp d8 r8 r4 | % 235
    \stemUp b8 r8 r4 \stemUp e8 r8 r4 | % 236
    \stemUp g8 r8 r4 r2 | % 237
    R1 \pageBreak | % 238
    \stemUp g4 -> \stemUp g,8 r8 \stemUp b8 \stemUp d8 r4 | % 239
    \stemUp b'8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis8 r8 |
    \barNumberCheck #240
    \stemUp e8 r8 \stemUp es8 r8 \stemUp d8 r8 \stemUp c8 r8 | % 241
    \stemUp b8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis'8 r8 | % 242
    \stemUp e8 r8 \stemUp es8 r8 \stemUp d8 r8 r4 \pageBreak | % 243
    \stemUp b'8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis8 r8 | % 244
    \stemUp e8 r8 \stemUp es8 r8 \stemUp d8 r8 r4 | % 245
    \stemUp g,8 r8 r4 \stemUp bes8 r8 r4 | % 246
    \stemUp es8 r8 r4 \stemUp g8 r8 r4 | % 247
    r4 \stemUp b,8 r16 \stemUp c16 \stemUp cis8 r8 \stemUp dis8 r8
    \pageBreak | % 248
    \stemUp e8 r8 \stemUp cis8 r16 \stemUp dis16 \stemUp e8 r8 \stemUp
    fis8 r8 | % 249
    \stemUp g8 r8 \stemUp gis8 r8 \stemUp a8 r8 \stemUp b8 r8 |
    \barNumberCheck #250
    \stemUp c8 r8 \stemUp cis8 r8 \stemDown d8 r8 \stemDown e8 r8 | % 251
    \stemDown f8 r8 r4 r2 | % 252
    R1*2 \pageBreak | % 254
    R1*5 \pageBreak | % 259
    R1 | \barNumberCheck #260
    r2 \stemUp b,,2 ~ _\f | % 261
    b1 ~ _\< | % 262
    \stemUp b2. ~ _\! _\ff _\> \stemUp b8 _\! r8 | % 263
    R1 \pageBreak | % 264
    R1*5 \pageBreak | % 269
    R1*4 | % 273
    r4 \stemUp as'8 _\fff r8 \stemUp g8 r8 \stemUp f8 r8 \pageBreak | % 274
    \stemUp e8 r8 \stemUp d8 r8 \stemUp c8 r8 r4 | % 275
    \stemDown e'4 _\fff \stemUp a,8. \stemUp a16 \stemDown e'4 \stemUp
    a,4 | % 276
    \stemDown d8 -. \stemDown a'8 -. r4 r2 | % 277
    \stemDown e4 \stemUp a,8. \stemUp a16 \stemDown e'4 \stemUp a,4 | % 278
    \stemDown d8 -. \stemDown a'8 -. r4 r2 | % 279
    r4 \stemDown e8 -. \stemDown a8 -. r4 \stemUp a,8 -. \stemUp d8 -. |
    \barNumberCheck #280
    r4 \stemDown e8 -. \stemDown a8 -. r4 \stemUp a,8 -. \stemUp d8 -.
    \pageBreak | % 281
    r4 \stemUp a4 -- \stemDown d8 r8 \stemDown d4 -- | % 282
    \stemDown a'8 r8 \stemDown a4 -- \stemDown d8 r8 \stemUp c,8 r8 | % 283
    \stemUp b8 _\fff r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis8 r8 | % 284
    \stemUp e8 r8 \stemUp es8 r8 \stemUp d8 r8 \stemUp c8 r8 | % 285
    \stemUp b8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis'8 r8 | % 286
    \stemUp e8 r8 \stemUp es8 r8 \stemUp d8 r8 r4 \pageBreak | % 287
    \stemUp b'8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis8 r8 | % 288
    \stemUp e8 r8 \stemUp es8 r8 \stemUp d8 r8 r4 | % 289
    \stemUp b8 r8 r4 \stemUp e8 r8 r4 | \barNumberCheck #290
    \stemUp g8 r8 r4 r2 | % 291
    R1 \pageBreak | % 292
    \stemUp g4 -> \stemUp g,8 r8 \stemUp b8 \stemUp d8 r4 | % 293
    \stemUp b'8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis8 r8 | % 294
    \stemUp e8 r8 \stemUp es8 r8 \stemUp d8 r8 \stemUp c8 r8 | % 295
    \stemUp b8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis'8 r8 | % 296
    \stemUp e8 r8 \stemUp es8 r8 \stemUp d8 r8 r4 \pageBreak | % 297
    \stemUp b'8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis8 r8 | % 298
    \stemUp e8 r8 \stemUp es8 r8 \stemUp d8 r8 r4 | % 299
    \stemUp g,8 r8 r4 \stemUp bes8 r8 r4 | \barNumberCheck #300
    \stemUp es8 r8 r4 \stemUp g8 r8 r4 | % 301
    r4 \stemUp b,8 r16 \stemUp c16 \stemUp cis8 r8 \stemUp dis8 r8
    \pageBreak | % 302
    \stemUp e8 r8 \stemUp cis8 r16 \stemUp dis16 \stemUp e8 r8 \stemUp
    fis8 r8 | % 303
    \stemUp g8 r8 \stemUp gis8 r8 \stemUp a8 r8 \stemUp b8 r8 | % 304
    \stemUp c4 ~ -> _\sempre _\fff \stemUp c8 r8 \stemUp cis4 ~ ->
    \stemUp cis8 r8 | % 305
    \stemDown d4 ~ -> \stemDown d8 r8 \stemDown es4 ~ -> \stemDown es8 r8
    | % 306
    \stemDown e4 ~ -> \stemDown e8 r8 \stemDown es4 ~ -> \stemDown es8 r8
    | % 307
    \stemDown d4 ~ -> \stemDown d8 r8 \stemUp cis4 ~ -> \stemUp cis8 r8
    \pageBreak | % 308
    \stemUp c4 ~ -> \stemUp c8 r8 \stemUp b4 ~ -> \stemUp b8 r8 | % 309
    \stemUp a4 ~ -> \stemUp a8 r8 \stemUp g4 ~ -> \stemUp g8 r8 |
    \barNumberCheck #310
    \stemUp fis4 ~ -> \stemUp fis8 r8 \stemUp f4 ~ -> \stemUp f8 r8 | % 311
    \stemUp e4 ~ -> \stemUp e8 r8 \stemUp es4 ~ -> \stemUp es8 r8 | % 312
    \stemUp d4. _\ffff \stemUp d8 \stemUp cis4. \stemUp cis8 | % 313
    \stemUp c4. \stemUp c8 \stemUp cis4. \stemUp cis8 \pageBreak | % 314
    \stemUp d4 -> \stemUp g4 -> \stemUp b4 -> \stemDown d4 -> | % 315
    \stemDown fis4 -> \stemDown a4 -> \stemDown d8 -> r8 r4 | % 316
    \stemUp g,,8 _\p _\< r8 \stemUp d8 r16 \stemUp d16 \stemUp g8 r8
    \stemUp d8 r8 | % 317
    \stemUp g8 \stemUp c8 ~ \stemUp c4 ~ \stemUp c8 r8 _\! r4 | % 318
    \stemUp g8 _\mf _\< r8 \stemUp d8 r16 \stemUp d16 \stemUp g8 r8
    \stemUp d8 r8 | % 319
    \stemUp g8 \stemUp c8 ~ \stemUp c4 ~ \stemUp c8 r8 _\! r4 \pageBreak
    | \barNumberCheck #320
    \stemUp g8 _\f _\< r8 \stemUp d8 r16 \stemUp d16 \stemUp g8 r8
    \stemUp d8 r8 | % 321
    \stemUp g8 \stemUp c8 ~ \stemUp c4 ~ \stemUp c8 r8 _\! r4 | % 322
    \stemUp g8 _\ff _\< r8 \stemUp d8 r16 \stemUp d16 \stemUp g8 r8
    \stemUp d8 r8 | % 323
    \stemUp g8 \stemUp c8 ~ \stemUp c4 ~ \stemUp c8 r8 _\! r4 | % 324
    \stemUp b,8 _\fff r8 \stemUp e16 r16 r8 r2 \pageBreak | % 325
    R1*2 | % 327
    r4 \stemUp dis4 ~ \stemUp dis8 r8 r4 \pageBreak | % 328
    r4 \stemUp a4 ~ \stemUp a8 r8 r4 | % 329
    r4 \stemUp a8 r8 \stemUp d8 r8 \stemUp fis8 r8 | \barNumberCheck
    #330
    \stemUp g16 _\sempre _\fff r16 r8 \stemUp fis16 r16 r8 \stemUp e16 r16
    r8 \stemUp es16 r16 r8 | % 331
    \stemUp d16 r16 r8 \stemUp e16 r16 r8 \stemUp f16 r16 r8 \stemUp fis16
    r16 r8 \pageBreak | % 332
    \stemUp g16 r16 r8 \stemUp fis16 r16 r8 \stemUp e16 r16 r8 \stemUp
    es16 r16 r8 | % 333
    \stemUp d16 r16 r8 \stemUp e16 r16 r8 \stemUp f16 r16 r8 \stemUp fis16
    r16 r8 | % 334
    \stemUp g16 r16 r8 \stemUp fis16 r16 r8 \stemUp e16 r16 r8 \stemUp d16
    r16 r8 | % 335
    \stemUp g16 r16 r8 \stemUp fis16 r16 r8 \stemUp e16 r16 r8 \stemUp d16
    r16 r8 \pageBreak | % 336
    \stemUp g8 \stemUp fis8 \stemUp e8 \stemUp d8 \stemUp g8 \stemUp fis8
    \stemUp e8 \stemUp d8 | % 337
    \stemUp g8 \stemUp fis8 \stemUp e8 \stemUp d8 \stemUp g8 \stemUp fis8
    \stemUp e8 \stemUp d8 | % 338
    \stemUp g8 r8 r8 \stemUp g8 \stemUp g8 r8 r8 \stemUp g8 | % 339
    \stemUp g8 r8 r8 \stemUp g8 \stemUp g8 r8 r8 \stemUp g8 |
    \barNumberCheck #340
    \stemUp g8 r8 r4 r8 \stemUp c8 \stemUp b8 \stemUp a8 \pageBreak | % 341
    \stemUp g8 \stemUp fis8 \stemUp e8 \stemUp es8 \stemUp d8 \stemUp c8
    \stemUp b8 \stemUp a8 | % 342
    \stemUp g8 r8 \stemUp g8 r8 r4 \stemUp g8 r8 | % 343
    r4 \stemUp g8 r8 r4 \stemUp g8 r8 | % 344
    \stemUp g8 r8 \stemUp g8 r8 \stemUp g8 r8 \stemUp g8 r8 | % 345
    g'1 ~ | % 346
    \stemUp g2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 \stemUp g8 \stemUp g8 }
    | % 347
    \stemUp g8 r8 r4 r2 \bar "|."
    }

PartPOneThreeVoiceTwo =  \relative e {
    \clef "bass" \time 4/4 \key g \major | % 1
     \once \override NoteHead.style = ##f e1 s1*3 \pageBreak s1*3 \bar
    "||"
    s1*2 \pageBreak s1*5 \break s1*5 \pageBreak s1*4 \break s1*4
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \bar "||"
    \pageBreak | % 71
    \key e \major s1*5 \break s1*5 \pageBreak s1*5 \pageBreak s1*4
    \pageBreak s1*6 \pageBreak s1*6 \break s1*5 \pageBreak s1*6 \break
    s1*5 \pageBreak s1*5 \break s1*5 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1*3 \bar "||"
    \key g \major s1 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*4 \break s1*4 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1*4 \pageBreak s1*5 \pageBreak s1*4 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*7 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*4 \pageBreak | % 225
     \once \override NoteHead.style = ##f c1 s1*2 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*6
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*6
    \pageBreak s1*5 \pageBreak s1*3 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1*5 \pageBreak s1*7 \bar "|."
    }

PartPOneFourVoiceOne =  \relative g, {
    \clef "bass" \time 4/4 \key c \none | % 1
    R1*4 \pageBreak | % 5
    R1*3 \bar "||"
    R1*2 \pageBreak | \barNumberCheck #10
    R1*5 \break | % 15
    R1*5 \pageBreak | \barNumberCheck #20
    R1*4 \break | % 24
    R1*4 \pageBreak | % 28
    R1*4 \pageBreak | % 32
    R1*4 \pageBreak | % 36
    R1*5 \pageBreak | % 41
    \stemUp g8 _\p r8 r4 r2 | % 42
    \stemUp g8 r8 r4 r2 | % 43
    \stemUp g8 r8 r4 r2 | % 44
    \stemUp g8 r8 r4 r2 | % 45
    g1 :32 _\f _\> \pageBreak | % 46
    g1 :32 _\! _\pp _\< | % 47
    \stemUp g8 _\! _\f r8 r4 r2 | % 48
    R1 | % 49
    fis1 :32 _\ff _\> | \barNumberCheck #50
    fis1 :32 _\! _\p _\< \pageBreak | % 51
    \stemUp fis8 _\! _\ff r8 r4 r2 | % 52
    R1 | % 53
    fis1 :32 _\pp _\markup{ \small\italic {cresc.} } \startTrillSpan | % 54
    fis1 :32 | % 55
    fis1 :32 \pageBreak | % 56
    fis1 :32 \stopTrillSpan _\f | % 57
    fis1 :32 _\pp _\markup{ \small\italic {cresc.} } \startTrillSpan | % 58
    fis1 :32 | % 59
    fis1 :32 | \barNumberCheck #60
    \stemUp fis2 :32 \stopTrillSpan _\f \stemUp fis8 r8 r4 \pageBreak | % 61
    \stemUp b8 -. _\p r8 \stemUp fis8 -. r16 \stemUp fis16 -. \stemUp b8
    -. r8 \stemUp fis8 -. r8 | % 62
    \stemUp b8 -. r8 r4 r2 | % 63
    \stemUp b8 -. _\mp r8 \stemUp fis8 -. r16 \stemUp fis16 -. \stemUp b8
    -. r8 \stemUp fis8 -. r8 | % 64
    \stemUp b8 -. r8 r4 r2 | % 65
    \stemUp b8 -. _\mf r8 \stemUp fis8 -. r16 \stemUp fis16 -. \stemUp b8
    -. r8 \stemUp fis8 -. r8 \pageBreak | % 66
    \stemUp b8 -. r8 r4 r2 | % 67
    \stemUp b8 -. _\f r8 \stemUp fis8 -. r16 \stemUp fis16 -. \stemUp b8
    -. r8 \stemUp fis8 -. r8 | % 68
    \stemUp b8 -. r8 r4 r2 | % 69
    \stemUp b8 _\ff r8 r4 r2 | \barNumberCheck #70
    R1 \bar "||"
    \pageBreak | % 71
    \key c \none R1*5 \break | % 76
    R1*5 \pageBreak | % 81
    R1*5 \pageBreak | % 86
    R1*4 \pageBreak | \barNumberCheck #90
    R1*6 \pageBreak | % 96
    R1*6 \break | % 102
    R1*5 \pageBreak | % 107
    R1*6 \break | % 113
    R1*5 \pageBreak | % 118
    R1*5 \break | % 123
    R1*5 \pageBreak | % 128
    R1*4 \pageBreak | % 132
    R1*4 \pageBreak | % 136
    R1*3 \bar "||"
    \key c \none R1 \pageBreak | \barNumberCheck #140
    R1*5 \pageBreak | % 145
    R1*5 \pageBreak | \barNumberCheck #150
    R1*5 \pageBreak | % 155
    R1*4 \break | % 159
    R1*4 \pageBreak | % 163
    R1*4 \pageBreak | % 167
    R1*4 \pageBreak | % 171
    R1*4 \pageBreak | % 175
    R1*4 | % 179
    \stemUp g8 _\p r8 r4 r2 \pageBreak | \barNumberCheck #180
    \stemUp g8 r8 r4 r2 | % 181
    \stemUp g8 r8 r4 r2 | % 182
    \stemUp g8 r8 r4 r2 | % 183
    g1 :32 _\f _\> \pageBreak | % 184
    g1 :32 _\! _\pp _\< | % 185
    \stemUp g8 _\! _\f r8 r4 r2 | % 186
    R1 | % 187
    d'1 :32 _\f _\> | % 188
    d1 :32 _\! _\pp _\< \pageBreak | % 189
    \stemDown d8 _\! _\f r8 r4 r2 | \barNumberCheck #190
    R1 | % 191
    a1 :32 _\p _\< | % 192
    d1 :32 | % 193
    a1 :32 _\! _\mf _\< \pageBreak | % 194
    \stemUp a2 :32 \stemUp a2 :32 _\! _\ff | % 195
    a1 :32 _\> | % 196
    a1 :32 | % 197
    a1 :32 _\! _\pp | % 198
    a1 :32 | % 199
    a1 :32 | \barNumberCheck #200
    a1 :32 _\< \pageBreak | % 201
    a1 :32 _\! _\p | % 202
    a1 :32 | % 203
    a1 :32 | % 204
    a1 :32 _\< | % 205
    a1 :32 _\! _\mp \pageBreak | % 206
    a1 :32 _\markup{ \small\italic {poco a poco cresc.} }
    \startTrillSpan | % 207
    a1 :32 | % 208
    a1 :32 | % 209
    a1 :32 | \barNumberCheck #210
    a1 :32 \pageBreak | % 211
    a1 :32 | % 212
    a1 :32 \stopTrillSpan _\f _\< | % 213
    a1 :32 | % 214
    a1 :32 _\! _\ff _\< | % 215
    a1 :32 \pageBreak | % 216
    a1 :32 _\! _\fff | % 217
    a1 :32 | % 218
    a1 :32 | % 219
    a1 :32 | \barNumberCheck #220
    a1 :32 \pageBreak | % 221
    \times 2/3  {
        \stemUp a8 -> \stemUp a8 -> r8 }
    r4 r2 | % 222
    R1*3 \pageBreak | % 225
    R1*3 \pageBreak | % 228
    R1 | % 229
    \stemUp g8 _\fff r8 \stemDown d'8 r8 \stemUp g,8 r8 \stemDown d'8 r8
    | \barNumberCheck #230
    \stemUp g,8 r8 \stemUp g8 r8 \stemDown d'8 r8 \stemDown d8 r8 | % 231
    \stemUp g,8 r8 \stemDown d'8 r8 \stemUp g,8 r8 \stemDown d'8 r8 | % 232
    \stemUp g,8 r8 \stemUp g8 r8 \stemDown d'8 r8 r4 \pageBreak | % 233
    \stemUp g,8 r8 \stemDown d'8 r8 \stemUp g,8 r8 \stemDown d'8 r8 | % 234
    \stemUp g,8 r8 \stemUp g8 r8 \stemDown d'8 r8 r4 | % 235
    \stemUp g,8 r8 r4 \stemUp g8 r8 r4 | % 236
    \stemUp g8 r8 r4 r2 | % 237
    R1 \pageBreak | % 238
    \stemUp g8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 \stemUp g8 \stemUp g8 }
    r8 \stemDown d'8 r4 | % 239
    \stemUp g,8 r8 \stemDown d'8 r8 \stemUp g,8 r8 \stemDown d'8 r8 |
    \barNumberCheck #240
    \stemUp g,8 r8 \stemUp g8 r8 \stemDown d'8 r8 \stemDown d8 r8 | % 241
    \stemUp g,8 r8 \stemDown d'8 r8 \stemUp g,8 r8 \stemDown d'8 r8 | % 242
    \stemUp g,8 r8 \stemUp g8 r8 \stemDown d'8 r8 r4 \pageBreak | % 243
    \stemUp g,8 r8 \stemDown d'8 r8 \stemUp g,8 r8 \stemDown d'8 r8 | % 244
    \stemUp g,8 r8 \stemUp g8 r8 \stemDown d'8 r8 r4 | % 245
    \stemUp g,8 r8 r4 \stemDown d'8 r8 r4 | % 246
    \stemUp g,8 r8 r4 \stemDown d'8 r8 r4 | % 247
    R1 \pageBreak | % 248
    R1*6 \pageBreak | % 254
    R1*5 \pageBreak | % 259
    R1*5 \pageBreak | % 264
    R1*5 \pageBreak | % 269
    R1*5 \pageBreak | % 274
    r2 \stemUp c2 :32 _\fff | % 275
    c1 :32 | % 276
    c1 :32 | % 277
    c1 :32 | % 278
    c1 :32 | % 279
    c1 :32 | \barNumberCheck #280
    c1 :32 \pageBreak | % 281
    c1 :32 | % 282
    \stemUp c2 :32 \stemUp c8 r8 r4 | % 283
    \stemUp g8 _\fff r8 \stemDown d'8 r8 \stemUp g,8 r8 \stemDown d'8 r8
    | % 284
    \stemUp g,8 r8 \stemUp g8 r8 \stemDown d'8 r8 \stemDown d8 r8 | % 285
    \stemUp g,8 r8 \stemDown d'8 r8 \stemUp g,8 r8 \stemDown d'8 r8 | % 286
    \stemUp g,8 r8 \stemUp g8 r8 \stemDown d'8 r8 r4 \pageBreak | % 287
    \stemUp g,8 r8 \stemDown d'8 r8 \stemUp g,8 r8 \stemDown d'8 r8 | % 288
    \stemUp g,8 r8 \stemUp g8 r8 \stemDown d'8 r8 r4 | % 289
    \stemUp g,8 r8 r4 \stemUp g8 r8 r4 | \barNumberCheck #290
    \stemUp g8 r8 r4 r2 | % 291
    R1 \pageBreak | % 292
    \stemUp g8 r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 \stemUp g8 \stemUp g8 }
    r8 \stemDown d'8 r4 | % 293
    \stemUp g,8 r8 \stemDown d'8 r8 \stemUp g,8 r8 \stemDown d'8 r8 | % 294
    \stemUp g,8 r8 \stemUp g8 r8 \stemDown d'8 r8 \stemDown d8 r8 | % 295
    \stemUp g,8 r8 \stemDown d'8 r8 \stemUp g,8 r8 \stemDown d'8 r8 | % 296
    \stemUp g,8 r8 \stemUp g8 r8 \stemDown d'8 r8 r4 \pageBreak | % 297
    \stemUp g,8 r8 \stemDown d'8 r8 \stemUp g,8 r8 \stemDown d'8 r8 | % 298
    \stemUp g,8 r8 \stemUp g8 r8 \stemDown d'8 r8 r4 | % 299
    \stemUp g,8 r8 r4 \stemDown d'8 r8 r4 | \barNumberCheck #300
    \stemUp g,8 r8 r4 \stemDown d'8 r8 r4 | % 301
    R1 \pageBreak | % 302
    R1*6 \pageBreak | % 308
    R1*4 | % 312
    g,1 :32 _\ffff | % 313
    g1 :32 \pageBreak | % 314
    R1*2 | % 316
    \stemUp g8 _\p _\< r8 \stemDown d'8 r16 \stemDown d16 \stemUp g,8 r8
    \stemDown d'8 r8 | % 317
    \stemUp g,8 \stemUp c8 r4 _\! r2 | % 318
    \stemUp g8 _\mf _\< r8 \stemDown d'8 r16 \stemDown d16 \stemUp g,8 r8
    \stemDown d'8 r8 | % 319
    \stemUp g,8 \stemUp c8 r4 _\! r2 \pageBreak | \barNumberCheck #320
    \stemUp g8 _\f _\< r8 \stemDown d'8 r16 \stemDown d16 \stemUp g,8 r8
    \stemDown d'8 r8 | % 321
    \stemUp g,8 \stemUp c8 r4 _\! r2 | % 322
    \stemUp g8 _\ff _\< r8 \stemDown d'8 r16 \stemDown d16 \stemUp g,8 r8
    \stemDown d'8 r8 | % 323
    \stemUp g,8 \stemUp c8 r4 _\! r2 | % 324
    R1 \pageBreak | % 325
    R1*3 \pageBreak | % 328
    R1 | % 329
    r4 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 | \barNumberCheck
    #330
    \stemUp g,8 _\sempre _\fff r8 \stemDown d'8 r8 \stemUp g,8 r8
    \stemUp g8 r8 | % 331
    \stemDown d'8 r8 r4 r2 \pageBreak | % 332
    \stemUp g,8 r8 \stemDown d'8 r8 \stemUp g,8 r8 \stemUp g8 r8 | % 333
    \stemDown d'8 r8 r4 r2 | % 334
    \stemUp g,8 r8 \stemDown d'8 r8 \stemUp g,8 r8 \stemDown d'8 r8 | % 335
    \stemUp g,8 r8 \stemDown d'8 r8 \stemUp g,8 r8 \stemDown d'8 r8
    \pageBreak | % 336
    \stemUp g,8 \stemUp d'8 \stemUp g,8 \stemUp d'8 \stemUp g,8 \stemUp
    d'8 \stemUp g,8 \stemUp d'8 | % 337
    \stemUp g,8 \stemUp d'8 \stemUp g,8 \stemUp d'8 \stemUp g,8 \stemUp
    d'8 \stemUp g,8 \stemUp d'8 | % 338
    \stemUp g,8 r8 r8 \stemUp g8 \stemUp g8 r8 r8 \stemUp g8 | % 339
    \stemUp g8 r8 r8 \stemUp g8 \stemUp g8 r8 r8 \stemUp g8 |
    \barNumberCheck #340
    \stemUp g8 r8 r4 r2 \pageBreak | % 341
    r2 \stemDown d'8 r8 r4 | % 342
    g,1 :32 | % 343
    g1 :32 | % 344
    g1 :32 | % 345
    g1 :32 | % 346
    \stemUp g2. :32 \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 \stemUp g8 \stemUp g8 }
    | % 347
    \stemUp g8 r8 r4 r2 \bar "|."
    }

PartPOneFourVoiceTwo =  \relative e {
    \clef "bass" \time 4/4 \key c \none | % 1
     \once \override NoteHead.style = ##f e1 s1*3 \pageBreak s1*3 \bar
    "||"
    s1*2 \pageBreak s1*5 \break s1*5 \pageBreak s1*4 \break s1*4
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \bar "||"
    \pageBreak | % 71
    \key c \none s1*5 \break s1*5 \pageBreak s1*5 \pageBreak s1*4
    \pageBreak s1*6 \pageBreak s1*6 \break s1*5 \pageBreak s1*6 \break
    s1*5 \pageBreak s1*5 \break s1*5 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1*3 \bar "||"
    \key c \none s1 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*4 \break s1*4 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1*4 \pageBreak s1*5 \pageBreak s1*4 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*7 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*4 \pageBreak | % 225
     \once \override NoteHead.style = ##f c1 s1*2 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*6
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*6
    \pageBreak s1*5 \pageBreak s1*3 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1*5 \pageBreak s1*7 \bar "|."
    }

PartPOneFiveVoiceOne =  \relative e' {
    \clef "percussion" \time 4/4 \key c \major \stopStaff \override
    Staff.StaffSymbol.line-count = #1 \startStaff | % 1
    R1*4 \pageBreak | % 5
    R1*2 | % 7
    \numericTimeSignature\time 4/4  R1 \bar "||"
    R1*2 \pageBreak | \barNumberCheck #10
    \numericTimeSignature\time 4/4  R1*2 | % 12
    \numericTimeSignature\time 4/4  R1*3 \break | % 15
    R1*5 \pageBreak | \barNumberCheck #20
    R1*4 \break | % 24
    R1*3 | % 27
    \numericTimeSignature\time 4/4  R1 \pageBreak | % 28
    R1*4 \pageBreak | % 32
    R1*4 \pageBreak | % 36
    \numericTimeSignature\time 4/4  R1 | % 37
    \numericTimeSignature\time 4/4  R1*4 \pageBreak | % 41
    R1*5 \pageBreak | % 46
    R1*5 \pageBreak | % 51
    R1*5 \pageBreak | % 56
    R1*5 \pageBreak | % 61
    R1*5 \pageBreak | % 66
    R1*3 | % 69
    \stemDown e8 _\ff r8 r4 r2 | \barNumberCheck #70
    R1 \bar "||"
    \pageBreak | % 71
    R1*5 \break | % 76
    R1*5 \pageBreak | % 81
    R1*5 \pageBreak | % 86
    R1*4 \pageBreak | \barNumberCheck #90
    R1*6 \pageBreak | % 96
    R1*6 \break | % 102
    R1*5 \pageBreak | % 107
    R1*6 \break | % 113
    R1*5 \pageBreak | % 118
    R1*5 \break | % 123
    R1*5 \pageBreak | % 128
    R1*4 \pageBreak | % 132
    R1*4 \pageBreak | % 136
    R1*3 \bar "||"
    R1 \pageBreak | \barNumberCheck #140
    R1*5 \pageBreak | % 145
    R1*5 \pageBreak | \barNumberCheck #150
    R1*5 \pageBreak | % 155
    R1*4 \break | % 159
    R1*4 \pageBreak | % 163
    R1*4 \pageBreak | % 167
    R1*4 \pageBreak | % 171
    R1*4 \pageBreak | % 175
    R1*5 \pageBreak | \barNumberCheck #180
    R1*4 \pageBreak | % 184
    R1*5 \pageBreak | % 189
    R1*5 \pageBreak | % 194
    R1*7 \pageBreak | % 201
    R1*5 \pageBreak | % 206
    R1*5 \pageBreak | % 211
    R1*5 \pageBreak | % 216
    R1*5 \pageBreak | % 221
    \times 2/3  {
        \stemDown e8 -> _\fff \stemDown e8 -> r8 }
    r4 r2 | % 222
    R1*3 \pageBreak | % 225
    R1*3 \pageBreak | % 228
    R1*5 \pageBreak | % 233
    R1*5 \pageBreak | % 238
    r2 \stemDown e8 _\fff \stemDown e8 r4 | % 239
    R1*4 \pageBreak | % 243
    R1*5 \pageBreak | % 248
    R1*6 \pageBreak | % 254
    R1*5 \pageBreak | % 259
    R1*5 \pageBreak | % 264
    R1*5 \pageBreak | % 269
    R1*5 \pageBreak | % 274
    r2 \stemDown e2 :32 _\fff | % 275
    e1 :32 | % 276
    e1 :32 | % 277
    e1 :32 | % 278
    e1 :32 | % 279
    e1 :32 | \barNumberCheck #280
    e1 :32 \pageBreak | % 281
    e1 :32 | % 282
    \stemDown e2 :32 \stemDown e8 r8 r4 | % 283
    R1*4 \pageBreak | % 287
    R1*5 \pageBreak | % 292
    r2 \stemDown e8 _\fff \stemDown e8 r4 | % 293
    R1*4 \pageBreak | % 297
    R1*5 \pageBreak | % 302
    R1*6 \pageBreak | % 308
    R1*5 | % 313
    \stemDown e8 _\fff r8 r4 r2 \pageBreak | % 314
    R1*6 \pageBreak | \barNumberCheck #320
    R1*4 | % 324
    \stemDown e8 _\fff r8 r4 r2 \pageBreak | % 325
    R1*3 \pageBreak | % 328
    R1*4 \pageBreak | % 332
    R1*4 \pageBreak | % 336
    R1*2 | % 338
    \stemDown e8 _\fff r8 r8 \stemDown e8 \stemDown e8 r8 r8 \stemDown e8
    | % 339
    \stemDown e8 r8 r8 \stemDown e8 \stemDown e8 r8 r8 \stemDown e8 |
    \barNumberCheck #340
    \stemDown e8 r8 r4 r2 \pageBreak | % 341
    R1 | % 342
    \stemDown e8 _\fff r8 \stemDown e8 r8 r4 \stemDown e8 r8 | % 343
    r4 \stemDown e8 r8 r4 \stemDown e8 r8 | % 344
    \stemDown e8 r8 \stemDown e8 r8 \stemDown e8 r8 \stemDown e8 r8 | % 345
    \stemDown e8 r8 r4 r2 | % 346
    R1*2 \bar "|."
    }

PartPOneFiveVoiceTwo =  \relative e' {
    \clef "percussion" \time 4/4 \key c \major \stopStaff \override
    Staff.StaffSymbol.line-count = #1 \startStaff | % 1
     \once \override NoteHead.style = ##f e1 s1*3 \pageBreak s1*2 | % 7
    \numericTimeSignature\time 4/4  s1 \bar "||"
    s1*2 \pageBreak | \barNumberCheck #10
    \numericTimeSignature\time 4/4  s1*2 | % 12
    \numericTimeSignature\time 4/4  s1*3 \break s1*5 \pageBreak s1*4
    \break s1*3 | % 27
    \numericTimeSignature\time 4/4  s1 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak | % 36
    \numericTimeSignature\time 4/4  s1 | % 37
    \numericTimeSignature\time 4/4  s1*4 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \bar
    "||"
    \pageBreak s1*5 \break s1*5 \pageBreak s1*5 \pageBreak s1*4
    \pageBreak s1*6 \pageBreak s1*6 \break s1*5 \pageBreak s1*6 \break
    s1*5 \pageBreak s1*5 \break s1*5 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1*3 \bar "||"
    s1 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*4
    \break s1*4 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1*5 \pageBreak s1*4 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*7 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*4 \pageBreak s1*3 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*6
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*6
    \pageBreak s1*5 \pageBreak s1*3 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1*5 \pageBreak s1*7 \bar "|."
    }

PartPOneSixVoiceOne =  \relative e' {
    \clef "percussion" \time 4/4 \key c \major \stopStaff \override
    Staff.StaffSymbol.line-count = #1 \startStaff | % 1
    R1*4 \pageBreak | % 5
    R1*2 | % 7
    \numericTimeSignature\time 4/4  R1 \bar "||"
    R1*2 \pageBreak | \barNumberCheck #10
    \numericTimeSignature\time 4/4  R1*2 | % 12
    \numericTimeSignature\time 4/4  R1*3 \break | % 15
    R1*5 \pageBreak | \barNumberCheck #20
    R1*4 \break | % 24
    R1*3 | % 27
    \numericTimeSignature\time 4/4  R1 \pageBreak | % 28
    R1*4 \pageBreak | % 32
    R1*4 \pageBreak | % 36
    \numericTimeSignature\time 4/4  R1 | % 37
    \numericTimeSignature\time 4/4  R1*4 \pageBreak | % 41
    R1*5 \pageBreak | % 46
    R1*5 \pageBreak | % 51
    R1*5 \pageBreak | % 56
    R1*5 \pageBreak | % 61
    R1*5 \pageBreak | % 66
    R1*5 \bar "||"
    \pageBreak | % 71
    R1*5 \break | % 76
    R1*5 \pageBreak | % 81
    R1*5 \pageBreak | % 86
    R1*4 \pageBreak | \barNumberCheck #90
    R1*6 \pageBreak | % 96
    R1*6 \break | % 102
    R1*5 \pageBreak | % 107
    R1*6 \break | % 113
    R1*5 \pageBreak | % 118
    R1*5 \break | % 123
    R1*5 \pageBreak | % 128
    R1*4 \pageBreak | % 132
    R1*4 \pageBreak | % 136
    R1*3 \bar "||"
    R1 \pageBreak | \barNumberCheck #140
    R1*5 \pageBreak | % 145
    R1*5 \pageBreak | \barNumberCheck #150
    R1*5 \pageBreak | % 155
    R1*4 \break | % 159
    R1*4 \pageBreak | % 163
    R1*4 \pageBreak | % 167
    R1*4 \pageBreak | % 171
    R1*4 \pageBreak | % 175
    R1*5 \pageBreak | \barNumberCheck #180
    R1*4 \pageBreak | % 184
    R1*5 \pageBreak | % 189
    R1*5 \pageBreak | % 194
    R1*7 \pageBreak | % 201
    R1*5 \pageBreak | % 206
    R1*5 \pageBreak | % 211
    R1*5 \pageBreak | % 216
    R1*5 \pageBreak | % 221
    R1*4 \pageBreak | % 225
    R1*3 \pageBreak | % 228
    R1*5 \pageBreak | % 233
    R1*5 \pageBreak | % 238
    r4 \stemDown e2. ~ ^ "(The cymbals must not be tied up)" _\fff | % 239
    \stemDown e8 r8 r4 r2 | \barNumberCheck #240
    R1*3 \pageBreak | % 243
    R1*5 \pageBreak | % 248
    R1*6 \pageBreak | % 254
    R1*5 \pageBreak | % 259
    R1*5 \pageBreak | % 264
    R1*5 \pageBreak | % 269
    R1*5 \pageBreak | % 274
    R1*7 \pageBreak | % 281
    R1 | % 282
    r2 r4 \stemDown e8 _\fff r8 | % 283
    R1*4 \pageBreak | % 287
    R1*5 \pageBreak | % 292
    r4 \stemDown e2. ~ _\fff | % 293
    \stemDown e8 r8 r4 r2 | % 294
    R1*3 \pageBreak | % 297
    R1*5 \pageBreak | % 302
    R1*6 \pageBreak | % 308
    R1*6 \pageBreak | % 314
    R1 | % 315
    r2 r4 \stemDown e4 ~ _\fff | % 316
    e1 ~ | % 317
    \stemDown e8 r8 r4 r4 r4 | % 318
    R1*2 \pageBreak | \barNumberCheck #320
    R1*5 \pageBreak | % 325
    R1*3 \pageBreak | % 328
    R1*4 \pageBreak | % 332
    R1*4 \pageBreak | % 336
    R1*5 \pageBreak | % 341
    R1*7 \bar "|."
    }

PartPOneSixVoiceTwo =  \relative e' {
    \clef "percussion" \time 4/4 \key c \major \stopStaff \override
    Staff.StaffSymbol.line-count = #1 \startStaff | % 1
     \once \override NoteHead.style = ##f e1 s1*3 \pageBreak s1*2 | % 7
    \numericTimeSignature\time 4/4  s1 \bar "||"
    s1*2 \pageBreak | \barNumberCheck #10
    \numericTimeSignature\time 4/4  s1*2 | % 12
    \numericTimeSignature\time 4/4  s1*3 \break s1*5 \pageBreak s1*4
    \break s1*3 | % 27
    \numericTimeSignature\time 4/4  s1 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak | % 36
    \numericTimeSignature\time 4/4  s1 | % 37
    \numericTimeSignature\time 4/4  s1*4 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \bar
    "||"
    \pageBreak s1*5 \break s1*5 \pageBreak s1*5 \pageBreak s1*4
    \pageBreak s1*6 \pageBreak s1*6 \break s1*5 \pageBreak s1*6 \break
    s1*5 \pageBreak s1*5 \break s1*5 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1*3 \bar "||"
    s1 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*4
    \break s1*4 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1*5 \pageBreak s1*4 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*7 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*4 \pageBreak s1*3 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*6
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*6
    \pageBreak s1*5 \pageBreak s1*3 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1*5 \pageBreak s1*7 \bar "|."
    }

PartPOneSevenVoiceOne =  \relative b' {
    \clef "treble" \time 12/8 \key g \major | % 1
    \stemUp b8 -. _\p \stemUp g8 -. \stemUp b8 -. \stemUp a8 -. \stemUp
    gis8 -. \stemUp a8 -. \stemDown c8 -. \stemDown a8 -. \stemDown c8
    -. \stemUp b8 -. \stemUp ais8 -. \stemUp b8 -. | % 2
    \stemDown c8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown e8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown a8 -. | % 3
    r1 s2 | % 4
    \stemDown e'8 ( -> _\p \stemDown d8 \stemDown c8 \stemDown b8
    \stemDown a8 \stemDown g8 ) r2.*2/3 s4 \pageBreak | % 5
    \stemUp b,8 -. _\p _ "Vln. I" _ "(div.)" \stemUp g8 -. \stemUp b8 -.
    \stemUp a8 -. \stemUp gis8 -. \stemUp a8 -. \stemDown c8 -.
    \stemDown a8 -. \stemDown c8 -. \stemUp b8 -. \stemUp ais8 -.
    \stemUp b8 -. | % 6
    \stemDown c8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown e8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown a8 -. | % 7
    r1 \bar "||"
    s2 | % 8
    \stemDown c8 ( -> _\p \stemDown b8 \stemDown a8 \stemDown g8
    \stemDown fis8 \stemDown e8 ) r2.*2/3 s4 | % 9
    \stemUp g,8 -. _\p \stemUp e8 -. \stemUp g8 -. \stemUp fis8 -.
    \stemUp eis8 -. \stemUp fis8 -. \stemUp a8 -. \stemUp g8 -. \stemUp
    a8 -. \stemUp g8 -. \stemUp fis8 -. \stemUp g8 -. \pageBreak |
    \barNumberCheck #10
    \stemDown b8 -. _ "Vln. I" _ "(div.)" _\markup{ \small\italic {poco
            cresc.} } \startTrillSpan \stemDown d8 -. \stemDown c8 -.
    \stemDown c8 -. \stemDown e8 -. \stemDown dis8 -. \stemDown dis8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown e8 -. \stemDown g8 -.
    \stemDown fis8 -. | % 11
    \stemDown g8 -. \stopTrillSpan _\mp \stemDown e8 -. \stemDown g8 -.
    \stemDown fis8 -. \stemDown eis8 -. \stemDown fis8 -. \stemDown a8
    -. \stemDown g8 -. \stemDown a8 -. \stemDown g8 -. \stemDown fis8 -.
    \stemDown g8 -. | % 12
    \stemDown b8 -. _\markup{ \small\italic {poco cresc.} }
    \startTrillSpan \stemDown d8 -. \stemDown c8 -. \stemDown c8 -.
    \stemDown e8 -. \stemDown dis8 -. \stemDown dis8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown e8 -. \stemDown g8 -. \stemDown fis8 -.
    | % 13
    \stemDown fis8 -. \stopTrillSpan _\mf _\markup{ \small\italic {dim.}
        } \startTrillSpan \stemDown g8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown d8 -. \stemDown e8 -. \stemDown c8 -. \stemDown d8 -.
    \stemDown b8 -. \stemDown c8 -. \stemDown a8 -. \stemDown b8 -. | % 14
    \stemDown g8 -. _\> \stemDown a8 -. \stemDown fis8 -. \stemDown g8
    -. \stemDown e8 -. \stemDown fis8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown c8 -. \stemDown d8 -. \stopTrillSpan _\! _\p \stemDown e8
    -. \stemDown d8 -. \break | % 15
    r1 _ "Vln. I" _ "(div.)" s2 | % 16
    r1 s2 | % 17
    r2.*2/3 r4.*2/3 \stemDown c''8 _\mf ^ "pizz." r8*2/3 r8*2/3 s1*11/24
    | % 18
    r1 s2 | % 19
    \stemDown b,8 -. _\p _\ leggiero ^ "arco" r8*2/3 r8*2/3 \stemDown
    cis8 -. r8*2/3 \stemDown cis8 ( \stemDown b8 ) r8*2/3 r8*2/3
    \stemDown g'8 -. r8*2/3 r8*2/3 s1*7/24 \pageBreak | \barNumberCheck
    #20
    \stemDown fis8 -. _ "Vln. I" _ "(div.)" r8*2/3 r8*2/3 \once \omit
    TupletBracket
    \times 6/7  {
        \stemDown e16*721/720 ( \stemDown fis16*721/720 \stemDown e16*721/720
        \stemDown fis16*721/720 \stemDown e16*721/720 \stemDown fis16*721/720
        \stemDown e16*721/720 }
    \stemDown d8 ) r8*2/3 r8*2/3 \stemDown cis8 -. r8*2/3 r8*2/3
    s1*479/1920 | % 21
    \stemDown b8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 22
    r1 s2 | % 23
    \stemDown b8 -. _\p r8*2/3 r8*2/3 \stemDown cis8 -. r8*2/3 \stemDown
    cis8 ( \stemDown b8 ) r8*2/3 r8*2/3 \stemDown g'8 -. r8*2/3 r8*2/3
    s1*7/24 \break | % 24
    \stemDown fis8 -. _ "Vln. I" _ "(div.)" r8*2/3 r8*2/3 \once \omit
    TupletBracket
    \times 6/7  {
        \stemDown e16*721/720 ( \stemDown fis16*721/720 \stemDown e16*721/720
        \stemDown fis16*721/720 \stemDown e16*721/720 \stemDown fis16*721/720
        \stemDown e16*721/720 }
    \stemDown d8 ) r8*2/3 r8*2/3 \stemDown cis8 -. r8*2/3 r8*2/3
    s1*479/1920 | % 25
    \stemDown b8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 26
    r1 s2 | % 27
    \stemDown d8 -. _\p r8*2/3 r8*2/3 \stemDown e8 -. r8*2/3 \stemDown e8
    ( \stemDown d8 ) r8*2/3 r8*2/3 \stemDown b'8 -. r4*2/3 s1*7/24
    \pageBreak | % 28
    \stemDown a8 -. _ "Vln. I" _ "(div.)" r8*2/3 r8*2/3 \once \omit
    TupletBracket
    \times 6/7  {
        \stemDown g16*721/720 ( _\< \stemDown a16*721/720 \stemDown g16*721/720
        \stemDown a16*721/720 \stemDown g16*721/720 \stemDown a16*721/720
        \stemDown g16*721/720 }
    \stemDown fis8 ) r8*2/3 r8*2/3 \stemDown e8 -. r8*2/3 r8*2/3
    s1*479/1920 _\! | % 29
    \stemDown d8 -. _\mp r8*2/3 r8*2/3 r4.*2/3 r4.*2/3 \stemDown g,8 -.
    _\< \stemDown a8 -. \stemDown g8 -. s1*1/3 | \barNumberCheck #30
    \stemDown a8 -. \stemDown b8 -. \stemDown a8 -. \stemDown a8 -.
    \stemDown b8 -. \stemDown a8 -. \stemDown b8 -. \stemDown cis8 -.
    \stemDown b8 -. \stemDown cis8 -. \stemDown d8 -. \stemDown cis8 -.
    | % 31
    \stemDown d8 -. _\! _\f \stemDown e8 -. \stemDown fis8 -. \stemDown
    g8 -. r8*2/3 r8*2/3 r2.*2/3 s1*1/3 \pageBreak | % 32
    \stemDown d8 -. _\f _ "Vln. I" _ "(div.)" \stemDown e8 -. \stemDown
    fis8 -. \stemDown g8 -. r8*2/3 r8*2/3 r2.*2/3 s1*1/3 | % 33
    r1 s2 | % 34
    r1 s2 | % 35
    r1 s2 \pageBreak | % 36
    \numericTimeSignature\time 4/4  \stemUp a,,8 _\p _ "Vln. I" _
    "(div.)" ^ "pizz." r8 \stemDown d8 r8 \stemDown a'8 r8 \stemDown d8
    r8 | % 37
    \stemDown g8 r8 \stemDown d8 r8 \stemDown a8 r8 \stemDown e8 r8 | % 38
    \stemDown a8 r8 \stemDown d8 r8 \stemDown b8 r8 \stemDown d,8 _\<
    \stemDown e8 | % 39
    \stemDown fis8 \stemDown g8 \stemDown a8 \stemDown b8 \stemDown c8
    _\! _\mf r8 \stemDown b8 \stemDown a8 | \barNumberCheck #40
    \stemDown d8 _\> r8 \stemDown g,8 r8 \stemDown g8 r8 _\! r4
    \pageBreak | % 41
    \time 12/8  \stemDown b8 -. _\p _ "Vln. I" _ "(div.)" ^ "arco"
    \stemDown g8 -. \stemDown b8 -. \stemDown a8 -. \stemDown gis8 -.
    \stemDown a8 -. \stemDown c8 -. \stemDown a8 -. \stemDown c8 -.
    \stemDown b8 -. \stemDown ais8 -. \stemDown b8 -. | % 42
    \stemDown c8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown e8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown a8 -. | % 43
    r1 s2 | % 44
    r2.*2/3 \stemDown e8 ( -> _\p \stemDown d8 \stemDown c8 \stemDown b8
    \stemDown a8 \stemDown g8 ) s4 | % 45
    \stemDown es'4. _\f -\markup{ \italic {marcato} } \stemDown d4.
    \stemDown c4. \stemDown bes4 ( ~ \stemDown bes16 \stemDown as16
    \pageBreak | % 46
    \stemDown g8 ) _ "Vln. I" _ "(div.)" r8*2/3 r8*2/3 r4.*2/3 r2.*2/3
    s1*11/24 | % 47
    r2.*2/3 \stemUp g,8 ( \stemUp as8 \stemUp bes8 ) \stemDown c8 (
    \stemDown bes8 \stemDown as8 s4 | % 48
    \stemUp g8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 49
    \stemDown b'4. _\ff -\markup{ \italic {marcato} } \stemDown ais4.
    \stemDown gis4. \stemDown fis4 ( ~ \stemDown fis16 \stemDown e16 ) |
    \barNumberCheck #50
    \stemDown dis8 r8*2/3 r8*2/3 \stemDown cis8 -. \stemDown dis8 -.
    \stemDown cis8 -. \stemDown dis8 -. \stemDown fis8 -. \stemDown dis8
    -. \stemDown fis8 -. \stemDown gis8 -. \stemDown fis8 -. s1*1/12
    \pageBreak | % 51
    r1 s2 | % 52
    r1 s2 | % 53
    r1 s2 | % 54
    r1 s2 | % 55
    r1 s2 \pageBreak | % 56
    r1 s2 | % 57
    r1 s2 | % 58
    r1 s2 | % 59
    r1 s2 | \barNumberCheck #60
    r1 s2 \pageBreak | % 61
    r1 s2 | % 62
    r1 s2 | % 63
    r1 s2 | % 64
    r1 s2 | % 65
    r1 s2 \pageBreak | % 66
    r1 s2 | % 67
    r1 s2 | % 68
    r1 s2 | % 69
    r1 s2 | \barNumberCheck #70
    r1 \bar "||"
    s2 \pageBreak | % 71
    \key e \major r1 s2 | % 72
    r1 s2 | % 73
    r1 s2 | % 74
    r1 s2 | % 75
    r1 s2 \break | % 76
    r1 s2 | % 77
    r1 s2 | % 78
    r1 s2 | % 79
    r1 s2 | \barNumberCheck #80
    r1 s2 \pageBreak | % 81
    r1 s2 | % 82
    r1 s2 | % 83
    r1 s2 | % 84
    r1 s2 | % 85
    r1 s2 \pageBreak | % 86
    r1 s2 | % 87
    r1 s2 | % 88
    r1 s2 | % 89
    r1 s2 \pageBreak | \barNumberCheck #90
    r1 s2 | % 91
    r1 s2 | % 92
    r1 s2 | % 93
    r1 s2 | % 94
    r1 s2 | % 95
    r1 s2 \pageBreak | % 96
    r1 s2 | % 97
    r1 s2 | % 98
    r1 s2 | % 99
    r1 s2 | \barNumberCheck #100
    r1 s2 | % 101
    r1 s2 \break | % 102
    r1 s2 | % 103
    r1 s2 | % 104
    r1 s2 | % 105
    r1 s2 | % 106
    r1 s2 \pageBreak | % 107
    r1 s2 | % 108
    r1 s2 | % 109
    r1 s2 | \barNumberCheck #110
    r1 s2 | % 111
    r1 s2 | % 112
    r1 s2 \break | % 113
    r1 s2 | % 114
    r1 s2 | % 115
    r1 s2 | % 116
    r1 s2 | % 117
    r1 s2 \pageBreak | % 118
    r1 s2 | % 119
    r1 r2*2/3 s1*1/6 | \barNumberCheck #120
    r1 r2*2/3 s1*1/6 | % 121
    r1 r2*2/3 s1*1/6 | % 122
    r1 r2*2/3 s1*1/6 \break | % 123
    r1 r2*2/3 s1*1/6 | % 124
    r1 r2*2/3 s1*1/6 | % 125
    r1 r2*2/3 s1*1/6 | % 126
    r1 r2*2/3 s1*1/6 | % 127
    r1 r2*2/3 s1*1/6 \pageBreak | % 128
    r1 r2*2/3 s1*1/6 | % 129
    r1 r2*2/3 s1*1/6 | \barNumberCheck #130
    r1 r2*2/3 s1*1/6 | % 131
    r1 r2*2/3 s1*1/6 \pageBreak | % 132
    r1 s2 | % 133
    r1 s2 | % 134
    r1 s2 | % 135
    r1 s2 \pageBreak | % 136
    \time 4/4 \omit Staff.TimeSignature \stemDown c'8 :16 _ "Vln. I" _
    "(div.)" \stemDown d8 :16 \stemDown e8 :16 \stemDown fis8 :16
    \stemDown g8 r8 r4 | % 137
    \time 12/8  \stemDown c,,8 ( _\f \stemDown b8 ) \stemDown a8 -.
    \stemUp g8 -. r8*2/3 r8*2/3 r4.*2/3 r8*2/3 \stemUp g8 -. _\mf
    \stemUp b8 -. s4 | % 138
    \stemDown c8 ( \stemDown b8 ) \stemDown a8 -. \stemUp g8 -. r8*2/3 r8*2/3
    r4.*2/3 r8*2/3 \stemUp g8 -. _\p \stemUp a8 -. \bar "||"
    s4 | % 139
    \key g \major \stemUp b8 -. \stemUp g8 -. \stemUp b8 -. \stemUp a8
    -. \stemUp gis8 -. \stemUp a8 -. \stemDown c8 -. \stemDown a8 -.
    \stemDown c8 -. \stemUp b8 -. \stemUp ais8 -. \stemUp b8 -.
    \pageBreak | \barNumberCheck #140
    \stemDown c8 -. _ "Vln. I" _ "(div.)" \stemDown d8 -. \stemDown e8
    -. \stemDown fis8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown fis8 -. \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -.
    \stemDown a8 -. | % 141
    r1 s2 | % 142
    \stemDown e'8 ( -> _\p \stemDown d8 \stemDown c8 \stemDown b8
    \stemDown a8 \stemDown g8 ) r2.*2/3 s4 | % 143
    \stemUp b,8 -. _\p \stemUp g8 -. \stemUp b8 -. \stemUp a8 -. \stemUp
    gis8 -. \stemUp a8 -. \stemDown c8 -. \stemDown a8 -. \stemDown c8
    -. \stemUp b8 -. \stemUp ais8 -. \stemUp b8 -. | % 144
    \stemDown c8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown e8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown a8 -.
    \pageBreak | % 145
    r1 _ "Vln. I" _ "(div.)" s2 | % 146
    \stemDown c8 ( -> _\p \stemDown b8 \stemDown a8 \stemDown g8
    \stemDown fis8 \stemDown e8 ) r2.*2/3 s4 | % 147
    \stemUp g,8 -. _\p \stemUp e8 -. \stemUp g8 -. \stemUp fis8 -.
    \stemUp eis8 -. \stemUp fis8 -. \stemUp a8 -. \stemUp g8 -. \stemUp
    a8 -. \stemUp g8 -. \stemUp fis8 -. \stemUp g8 -. | % 148
    \stemDown b8 -. _\markup{ \small\italic {poco cresc.} }
    \startTrillSpan \stemDown d8 -. \stemDown c8 -. \stemDown c8 -.
    \stemDown e8 -. \stemDown dis8 -. \stemDown dis8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown e8 -. \stemDown g8 -. \stemDown fis8 -.
    | % 149
    \stemDown g8 -. \stopTrillSpan _\mp \stemDown e8 -. \stemDown g8 -.
    \stemDown fis8 -. \stemDown eis8 -. \stemDown fis8 -. \stemDown a8
    -. \stemDown g8 -. \stemDown a8 -. \stemDown g8 -. \stemDown fis8 -.
    \stemDown g8 -. \pageBreak | \barNumberCheck #150
    \stemDown b8 -. _ "Vln. I" _ "(div.)" _\markup{ \small\italic {poco
            cresc.} } \startTrillSpan \stemDown d8 -. \stemDown c8 -.
    \stemDown c8 -. \stemDown e8 -. \stemDown dis8 -. \stemDown dis8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown e8 -. \stemDown g8 -.
    \stemDown fis8 -. | % 151
    \stemDown fis8 -. \stopTrillSpan _\mf _\markup{ \small\italic {dim.}
        } \startTrillSpan \stemDown g8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown d8 -. \stemDown e8 -. \stemDown c8 -. \stemDown d8 -.
    \stemDown b8 -. \stemDown c8 -. \stemDown a8 -. \stemDown b8 -. | % 152
    \stemDown g8 -. _\> \stemDown a8 -. \stemDown fis8 -. \stemDown g8
    -. \stemDown e8 -. \stemDown fis8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown c8 -. \stemDown d8 -. \stopTrillSpan _\! _\p \stemDown e8
    -. \stemDown d8 -. | % 153
    r1 s2 | % 154
    r1 s2 \pageBreak | % 155
    r2.*2/3 _ "Vln. I" _ "(div.)" r4.*2/3 \stemDown c''8 _\mf ^ "pizz."
    r8*2/3 r8*2/3 s1*11/24 | % 156
    r1 s2 | % 157
    \stemDown b,8 -. _\p _\ leggiero ^ "arco" r8*2/3 r8*2/3 \stemDown
    cis8 -. r8*2/3 \stemDown cis8 ( \stemDown b8 ) r8*2/3 r8*2/3
    \stemDown g'8 -. r8*2/3 r8*2/3 s1*7/24 | % 158
    \stemDown fis8 -. r8*2/3 r8*2/3 \once \omit TupletBracket
    \times 6/7  {
        \stemDown e16*721/720 ( \stemDown fis16*721/720 \stemDown e16*721/720
        \stemDown fis16*721/720 \stemDown e16*721/720 \stemDown fis16*721/720
        \stemDown e16*721/720 }
    \stemDown d8 ) r8*2/3 r8*2/3 \stemDown cis8 -. r8*2/3 r8*2/3
    s1*479/1920 \break | % 159
    \stemDown b8 -. _ "Vln. I" _ "(div.)" r8*2/3 r8*2/3 r4.*2/3 r2.*2/3
    s1*11/24 | \barNumberCheck #160
    r1 s2 | % 161
    \stemDown b8 -. _\p r8*2/3 r8*2/3 \stemDown cis8 -. r8*2/3 \stemDown
    cis8 ( \stemDown b8 ) r8*2/3 r8*2/3 \stemDown g'8 -. r8*2/3 r8*2/3
    s1*7/24 | % 162
    \stemDown fis8 -. r8*2/3 r8*2/3 \once \omit TupletBracket
    \times 6/7  {
        \stemDown e16*721/720 ( _\< \stemDown fis16*721/720 \stemDown e16*721/720
        \stemDown fis16*721/720 \stemDown e16*721/720 \stemDown fis16*721/720
        \stemDown e16*721/720 }
    \stemDown d8 ) r8*2/3 r8*2/3 \stemDown cis8 -. r8*2/3 r8*2/3
    s1*479/1920 _\! \pageBreak | % 163
    \stemDown b8 -. _ "Vln. I" _ "(div.)" r8*2/3 r8*2/3 r4.*2/3 r2.*2/3
    s1*11/24 | % 164
    r1 s2 | % 165
    \stemDown d8 -. _\p r8*2/3 r8*2/3 \stemDown e8 -. r8*2/3 \stemDown e8
    ( \stemDown d8 ) r8*2/3 r8*2/3 \stemDown b'8 -. r8*2/3 r8*2/3
    s1*7/24 | % 166
    \stemDown a8 -. r8*2/3 r8*2/3 \once \omit TupletBracket
    \times 6/7  {
        \stemDown g16*721/720 ( _\< \stemDown a16*721/720 \stemDown g16*721/720
        \stemDown a16*721/720 \stemDown g16*721/720 \stemDown a16*721/720
        \stemDown g16*721/720 }
    \stemDown fis8 ) r8*2/3 r8*2/3 \stemDown e8 -. r8*2/3 r8*2/3
    s1*479/1920 _\! \pageBreak | % 167
    \stemDown d8 -. _\mp _ "Vln. I" _ "(div.)" r8*2/3 r8*2/3 r4.*2/3 r4.*2/3
    \stemDown g,8 -. _\< \stemDown a8 -. \stemDown g8 -. s1*1/3 | % 168
    \stemDown a8 -. \stemDown b8 -. \stemDown a8 -. \stemDown a8 -.
    \stemDown b8 -. \stemDown a8 -. \stemDown b8 -. \stemDown cis8 -.
    \stemDown b8 -. \stemDown cis8 -. \stemDown d8 -. \stemDown cis8 -.
    | % 169
    \stemDown d8 -. _\! _\f \stemDown e8 -. \stemDown fis8 -. \stemDown
    g8 -. r8*2/3 r8*2/3 r2.*2/3 s1*1/3 | \barNumberCheck #170
    \stemDown d8 -. _\f \stemDown e8 -. \stemDown fis8 -. \stemDown g8
    -. r8*2/3 r8*2/3 r2.*2/3 s1*1/3 \pageBreak | % 171
    r1 _ "Vln. I" _ "(div.)" s2 | % 172
    r1 s2 | % 173
    r1 s2 | % 174
    \numericTimeSignature\time 4/4  \stemUp a,,8 _\p ^ "pizz." r8
    \stemDown d8 r8 \stemDown a'8 r8 \stemDown d8 r8 \pageBreak | % 175
    \stemDown g8 _ "Vln. I" _ "(div.)" r8 \stemDown d8 r8 \stemDown a8 r8
    \stemDown e8 r8 | % 176
    \stemDown a8 r8 \stemDown d8 r8 \stemDown b8 r8 \stemDown d,8 _\<
    \stemDown e8 | % 177
    \stemDown fis8 \stemDown g8 \stemDown a8 \stemDown b8 \stemDown c8
    _\! _\mf r8 \stemDown b8 \stemDown a8 | % 178
    \stemDown d8 _\> r8 \stemDown g,8 r8 \stemDown g8 r8 _\! r4 | % 179
    \time 12/8  \stemDown b8 -. _\p ^ "arco" \stemDown g8 -. \stemDown b8
    -. \stemDown a8 -. \stemDown gis8 -. \stemDown a8 -. \stemDown c8 -.
    \stemDown a8 -. \stemDown c8 -. \stemDown b8 -. \stemDown ais8 -.
    \stemDown b8 -. \pageBreak | \barNumberCheck #180
    \stemDown c8 -. _ "Vln. I" _ "(div.)" \stemDown d8 -. \stemDown e8
    -. \stemDown fis8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown fis8 -. \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -.
    \stemDown a8 -. | % 181
    r1 s2 | % 182
    r2.*2/3 \stemDown e8 ( -> _\p \stemDown d8 \stemDown c8 \stemDown b8
    \stemDown a8 \stemDown g8 ) s4 | % 183
    \stemDown es'4. _\f _\ marcato \stemDown d4. \stemDown c4. \stemDown
    bes4 ( ~ \stemDown bes16 \stemDown as16 ) \pageBreak | % 184
    \stemDown g8 _ "Vln. I" _ "(div.)" r8*2/3 r8*2/3 r4.*2/3 r2.*2/3
    s1*11/24 | % 185
    r2.*2/3 \stemUp g,8 ( _\f \stemUp as8 \stemUp bes8 ) \stemDown c8 (
    \stemDown bes8 \stemDown as8 s4 | % 186
    \stemUp g8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 187
    \stemDown g''4. _\ff \stemDown f4. \stemDown es4. \stemDown d4 ( ~
    \stemDown d16 \stemDown c16 ) | % 188
    \stemDown bes8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 \pageBreak | % 189
    r2.*2/3 _ "Vln. I" _ "(div.)" \stemDown bes,8 ( _\ff \stemDown c8
    \stemDown d8 ) \stemDown es8 ( \stemDown d8 \stemDown c8 s4 |
    \barNumberCheck #190
    \stemDown bes8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 191
    \numericTimeSignature\time 4/4  \stemDown g'8 ( _\ff \stemDown fis8
    \stemDown e8 \stemDown d8 ) \stemDown g8 ( \stemDown fis8 \stemDown
    e8 \stemDown d8 ) | % 192
    \stemDown g8 ( \stemDown f8 \stemDown e8 \stemDown d8 ) \stemDown g8
    ( \stemDown f8 \stemDown e8 \stemDown d8 ) | % 193
    \time 12/8  \stemDown g'8 _\ff \stemDown fis8 \stemDown e8 \stemDown
    d8 \stemDown cis8 \stemDown b8 \stemDown a8 \stemDown g8 \stemDown
    fis8 \stemDown e8 \stemDown d8 \stemDown cis8 \pageBreak | % 194
    \numericTimeSignature\time 4/4  R1*7 \pageBreak | % 201
    R1*5 \pageBreak | % 206
    R1*5 \pageBreak | % 211
    R1*5 \pageBreak | % 216
    R1*5 \pageBreak | % 221
    R1*4 \pageBreak | % 225
    R1*3 \pageBreak | % 228
    R1*5 \pageBreak | % 233
    R1*5 \pageBreak | % 238
    R1*5 \pageBreak | % 243
    R1*5 \pageBreak | % 248
    R1*6 \pageBreak | % 254
    R1*5 \pageBreak | % 259
    R1*5 \pageBreak | % 264
    R1*5 \pageBreak | % 269
    R1*5 \pageBreak | % 274
    R1*7 \pageBreak | % 281
    R1*6 \pageBreak | % 287
    R1*5 \pageBreak | % 292
    R1*5 \pageBreak | % 297
    R1*5 \pageBreak | % 302
    R1*6 \pageBreak | % 308
    R1*6 \pageBreak | % 314
    R1*6 \pageBreak | \barNumberCheck #320
    R1*5 \pageBreak | % 325
    R1*3 \pageBreak | % 328
    R1*4 \pageBreak | % 332
    R1*4 \pageBreak | % 336
    R1*5 \pageBreak | % 341
    R1*7 \bar "|."
    }

PartPOneEightVoiceOne =  \relative d' {
    \clef "treble" \time 12/8 \key g \major | % 1
    \stemUp d8 -. _\p \stemUp e8 -. \stemUp d8 -. \stemUp fis8 -.
    \stemUp eis8 -. \stemUp fis8 -. \stemUp e8 -. \stemUp fis8 -.
    \stemUp e8 -. \stemUp g8 -. \stemUp fis8 -. \stemUp g8 -. | % 2
    \stemUp e8 -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp g8
    -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp b8 -.
    \stemDown a8 -. \stemDown b8 -. \stemDown c8 -. | % 3
    r1 s2 | % 4
    \stemDown ais'8 ( -> _\p \stemDown b8 \stemDown a8 \stemDown g8
    \stemDown es8 \stemDown d8 ) r2.*2/3 s4 \pageBreak | % 5
    \stemUp d,8 -. _\p \stemUp e8 -. \stemUp d8 -. \stemUp fis8 -.
    \stemUp eis8 -. \stemUp fis8 -. \stemUp e8 -. \stemUp fis8 -.
    \stemUp e8 -. \stemUp g8 -. \stemUp fis8 -. \stemUp g8 -. | % 6
    \stemUp e8 -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp g8
    -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp b8 -.
    \stemDown a8 -. \stemDown b8 -. \stemDown c8 -. | % 7
    r1 \bar "||"
    s2 | % 8
    \stemDown fis8 ( -> _\p \stemDown g8 \stemDown fis8 \stemDown e8
    \stemDown c8 \stemDown b8 ) r2.*2/3 s4 | % 9
    \stemUp b,8 -. _\p \stemUp c8 -. \stemUp b8 -. \stemUp dis8 -.
    \stemUp cisis8 -. \stemUp dis8 -. \stemUp c8 -. \stemUp e8 -.
    \stemUp c8 -. \stemUp e8 -. \stemUp dis8 -. \stemUp e8 -. \pageBreak
    | \barNumberCheck #10
    \stemUp g8 -. _\markup{ \small\italic {poco cresc.} }
    \startTrillSpan \stemUp fis8 -. \stemUp e8 -. \stemUp a8 -. \stemUp
    g8 -. \stemUp fis8 -. \stemUp b8 -. \stemUp a8 -. \stemUp g8 -.
    \stemDown c8 -. \stemDown b8 -. \stemDown a8 -. | % 11
    \stemDown b8 -. \stopTrillSpan _\mp \stemDown c8 -. \stemDown b8 -.
    \stemDown dis8 -. \stemDown cisis8 -. \stemDown dis8 -. \stemDown c8
    -. \stemDown e8 -. \stemDown c8 -. \stemDown e8 -. \stemDown dis8 -.
    \stemDown e8 -. | % 12
    \stemDown g8 -. _\markup{ \small\italic {poco cresc.} }
    \startTrillSpan \stemDown fis8 -. \stemDown e8 -. \stemDown a8 -.
    \stemDown g8 -. \stemDown fis8 -. \stemDown b8 -. \stemDown a8 -.
    \stemDown g8 -. \stemDown c8 -. \stemDown b8 -. \stemDown a8 -. | % 13
    \stemDown d8 -. \stopTrillSpan _\mf _\markup{ \small\italic {dim.} }
    \startTrillSpan \stemDown b8 -. \stemDown c8 -. \stemDown a8 -.
    \stemDown b8 -. \stemDown g8 -. \stemDown a8 -. \stemDown fis8 -.
    \stemDown g8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown d8 -. | % 14
    \stemDown e8 -. _\> \stemDown c8 -. \stemDown d8 -. \stemDown b8 -.
    \stemDown c8 -. \stemDown a8 -. \stemUp b8 -. \stemUp g8 -. \stemUp
    a8 -. \stemUp fis8 -. \stopTrillSpan _\! _\p \stemUp a8 -. \stemUp
    fis8 -. \break | % 15
    r1 s2 | % 16
    r1 s2 | % 17
    r2.*2/3 r4.*2/3 \stemDown c''8 _\mf ^ "pizz." r8*2/3 r8*2/3 s1*11/24
    | % 18
    \stemDown c8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 19
    \stemDown b,8 -. _\p _\ leggiero ^ "arco" r8*2/3 r8*2/3 \stemDown
    cis8 -. r8*2/3 \stemDown cis8 ( \stemDown b8 ) r8*2/3 r8*2/3
    \stemDown g'8 -. r8*2/3 r8*2/3 s1*7/24 \pageBreak | \barNumberCheck
    #20
    \stemDown fis8 -. r8*2/3 r8*2/3 \once \omit TupletBracket
    \times 6/7  {
        \stemDown e16*721/720 ( \stemDown fis16*721/720 \stemDown e16*721/720
        \stemDown fis16*721/720 \stemDown e16*721/720 \stemDown fis16*721/720
        \stemDown e16*721/720 }
    \stemDown d8 ) r8*2/3 r8*2/3 \stemDown cis8 -. r8*2/3 r8*2/3
    s1*479/1920 | % 21
    \stemDown b8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 22
    r1 s2 | % 23
    \stemDown b8 -. _\p r8*2/3 r8*2/3 \stemDown cis8 -. r8*2/3 \stemDown
    cis8 ( \stemDown b8 ) r8*2/3 r8*2/3 \stemDown g'8 -. r4*2/3 s1*7/24
    \break | % 24
    \stemDown fis8 -. r8*2/3 r8*2/3 \once \omit TupletBracket
    \times 6/7  {
        \stemDown e16*721/720 ( \stemDown fis16*721/720 \stemDown e16*721/720
        \stemDown fis16*721/720 \stemDown e16*721/720 \stemDown fis16*721/720
        \stemDown e16*721/720 }
    \stemDown d8 ) r8*2/3 r8*2/3 \stemDown cis8 -. r8*2/3 r8*2/3
    s1*479/1920 | % 25
    \stemDown b8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 26
    r1 s2 | % 27
    \stemDown d8 -. _\p r8*2/3 r8*2/3 \stemDown e8 -. r8*2/3 \stemDown e8
    ( \stemDown d8 ) r8*2/3 r8*2/3 \stemDown b'8 -. r4*2/3 s1*7/24
    \pageBreak | % 28
    \stemDown a8 -. r8*2/3 r8*2/3 \once \omit TupletBracket
    \times 6/7  {
        \stemDown g16*721/720 ( _\< \stemDown a16*721/720 \stemDown g16*721/720
        \stemDown a16*721/720 \stemDown g16*721/720 \stemDown a16*721/720
        \stemDown g16*721/720 }
    \stemDown fis8 ) r8*2/3 r8*2/3 \stemDown e8 -. r8*2/3 r8*2/3
    s1*479/1920 _\! | % 29
    \stemDown d8 -. _\mp r8*2/3 r8*2/3 r4.*2/3 \stemDown fis8 -. _\<
    \stemDown g8 -. \stemDown fis8 -. \stemDown b,8 -. \stemDown d8 -.
    \stemDown b8 -. s1*5/24 | \barNumberCheck #30
    \stemDown c8 -. \stemDown dis8 -. \stemDown c8 -. \stemDown cis8 -.
    \stemDown fis8 -. \stemDown cis8 -. \stemDown dis8 -. \stemDown fis8
    -. \stemDown dis8 -. \stemDown e8 -. \stemDown g8 -. \stemDown e8 -.
    | % 31
    \stemDown fis8 -. _\! _\f \stemDown a8 -. \stemDown d8 -. \stemDown
    es8 -. r8*2/3 r8*2/3 r2.*2/3 s1*1/3 \pageBreak | % 32
    \stemDown fis,8 -. _\f \stemDown a8 -. \stemDown d8 -. \stemDown es8
    -. r8*2/3 r8*2/3 r2.*2/3 s1*1/3 | % 33
    r1 s2 | % 34
    r1 s2 | % 35
    r1 s2 \pageBreak | % 36
    \numericTimeSignature\time 4/4  \stemUp a,,,8 _\p ^ "pizz." r8
    \stemUp d8 r8 \stemUp a'8 r8 \stemDown d8 r8 | % 37
    \stemDown g8 r8 \stemDown d8 r8 \stemUp a8 r8 \stemUp e8 r8 | % 38
    \stemUp a8 r8 \stemDown d8 r8 \stemDown b8 r8 \stemUp d,8 _\<
    \stemUp e8 | % 39
    \stemUp fis8 \stemUp g8 \stemUp a8 \stemUp b8 \stemDown c8 _\! _\mf
    r8 \stemUp b8 \stemUp a8 | \barNumberCheck #40
    \stemDown d8 -. _\> r8 \stemUp <g,, g'>8 r8 \stemUp <g g'>8 r8 _\! r4
    \pageBreak | % 41
    \time 12/8  \stemDown d''8 -. _\p ^ "arco" \stemDown e8 -. \stemDown
    d8 -. \stemDown fis8 -. \stemDown eis8 -. \stemDown fis8 -.
    \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown g8 -.
    \stemDown fis8 -. \stemDown g8 -. | % 42
    \stemDown e8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown a8 -.
    \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown a8 -.
    \stemDown b8 -. \stemDown a8 -. \stemDown b8 -. \stemDown c8 -. | % 43
    r1 s2 | % 44
    r2.*2/3 \stemDown b8 ( -> _\p \stemDown g8 \stemDown e8 \stemDown g8
    \stemDown d8 \stemDown b8 ) s4 | % 45
    \stemDown es4. _\f -\markup{ \italic {marcato} } \stemDown d4.
    \stemDown c4. \stemDown bes4 ( ~ \stemUp bes16 \stemUp as16
    \pageBreak | % 46
    \stemUp g8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 47
    r2.*2/3 \stemUp g8 ( \stemUp as8 \stemUp bes8 ) \stemDown c8 (
    \stemDown bes8 \stemDown as8 s4 | % 48
    \stemUp g8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 49
    \stemDown b4. _\ff -\markup{ \italic {marcato} } \stemUp ais4.
    \stemUp gis4. \stemUp fis4 ( ~ \stemUp fis16 \stemUp e16 ) |
    \barNumberCheck #50
    \stemUp dis8 r8*2/3 r8*2/3 \stemDown cis'8 -. \stemDown dis8 -.
    \stemDown cis8 -. \stemDown dis8 -. \stemDown fis8 -. \stemDown dis8
    -. \stemDown fis8 -. \stemDown gis8 -. \stemDown fis8 -. s1*1/12
    \pageBreak | % 51
    r1 s2 | % 52
    r1 s2 | % 53
    r1 s2 | % 54
    r1 s2 | % 55
    r1 s2 \pageBreak | % 56
    r1 s2 | % 57
    r1 s2 | % 58
    r1 s2 | % 59
    r1 s2 | \barNumberCheck #60
    r1 s2 \pageBreak | % 61
    r1 s2 | % 62
    r1 s2 | % 63
    r1 s2 | % 64
    r1 s2 | % 65
    r1 s2 \pageBreak | % 66
    r1 s2 | % 67
    r1 s2 | % 68
    r1 s2 | % 69
    r1 s2 | \barNumberCheck #70
    r1 \bar "||"
    s2 \pageBreak | % 71
    \key e \major r1 s2 | % 72
    r1 s2 | % 73
    r1 s2 | % 74
    r1 s2 | % 75
    r1 s2 \break | % 76
    r1 s2 | % 77
    r1 s2 | % 78
    r1 s2 | % 79
    r1 s2 | \barNumberCheck #80
    r1 s2 \pageBreak | % 81
    r1 s2 | % 82
    r1 s2 | % 83
    r1 s2 | % 84
    r1 s2 | % 85
    r1 s2 \pageBreak | % 86
    r1 s2 | % 87
    r1 s2 | % 88
    r1 s2 | % 89
    r1 s2 \pageBreak | \barNumberCheck #90
    r1 s2 | % 91
    r1 s2 | % 92
    r1 s2 | % 93
    r1 s2 | % 94
    r1 s2 | % 95
    r1 s2 \pageBreak | % 96
    r1 s2 | % 97
    r1 s2 | % 98
    r1 s2 | % 99
    r1 s2 | \barNumberCheck #100
    r1 s2 | % 101
    r1 s2 \break | % 102
    r1 s2 | % 103
    r1 s2 | % 104
    r1 s2 | % 105
    r1 s2 | % 106
    r1 s2 \pageBreak | % 107
    r1 s2 | % 108
    r1 s2 | % 109
    r1 s2 | \barNumberCheck #110
    r1 s2 | % 111
    r1 s2 | % 112
    r1 s2 \break | % 113
    r1 s2 | % 114
    r1 s2 | % 115
    r1 s2 | % 116
    r1 s2 | % 117
    r1 s2 \pageBreak | % 118
    r1 s2 | % 119
    r1 r2*2/3 s1*1/6 | \barNumberCheck #120
    r1 r2*2/3 s1*1/6 | % 121
    r1 r2*2/3 s1*1/6 | % 122
    r1 r2*2/3 s1*1/6 \break | % 123
    r1 r2*2/3 s1*1/6 | % 124
    r1 r2*2/3 s1*1/6 | % 125
    r1 r2*2/3 s1*1/6 | % 126
    r1 r2*2/3 s1*1/6 | % 127
    r1 r2*2/3 s1*1/6 \pageBreak | % 128
    r1 r2*2/3 s1*1/6 | % 129
    r1 r2*2/3 s1*1/6 | \barNumberCheck #130
    r1 r2*2/3 s1*1/6 | % 131
    r1 r2*2/3 s1*1/6 \pageBreak | % 132
    r1 s2 | % 133
    r1 s2 | % 134
    r1 s2 | % 135
    r1 s2 \pageBreak | % 136
    \time 4/4 \omit Staff.TimeSignature \stemDown c'8 :16 ^ "div."
    \stemDown d8 :16 \stemDown e8 :16 \stemDown fis8 :16 \stemDown g8 r8
    r4 | % 137
    \time 12/8  \stemDown c,,8 ( _\f \stemDown b8 ) \stemDown a8 -.
    \stemUp g8 -. r8*2/3 r8*2/3 r4.*2/3 r8*2/3 \stemUp g8 -. _\mf
    \stemUp b8 -. s4 | % 138
    \stemDown c8 ( \stemDown b8 ) \stemDown a8 -. \stemUp g8 -. r8*2/3 r8*2/3
    r4.*2/3 r8*2/3 \stemUp b,8 -. _\p \stemUp fis'8 -. \bar "||"
    s4 | % 139
    \key g \major \stemUp d8 -. \stemUp e8 -. \stemUp d8 -. \stemUp fis8
    -. \stemUp eis8 -. \stemUp fis8 -. \stemUp e8 -. \stemUp fis8 -.
    \stemUp e8 -. \stemUp g8 -. \stemUp fis8 -. \stemUp g8 -. \pageBreak
    | \barNumberCheck #140
    \stemUp e8 -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp g8
    -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp b8 -.
    \stemDown a8 -. \stemDown b8 -. \stemDown c8 -. | % 141
    r1 s2 | % 142
    \stemDown ais'8 ( -> _\p \stemDown b8 \stemDown a8 \stemDown g8
    \stemDown es8 \stemDown d8 ) r2.*2/3 s4 | % 143
    \stemUp d,8 -. _\p \stemUp e8 -. \stemUp d8 -. \stemUp fis8 -.
    \stemUp eis8 -. \stemUp fis8 -. \stemUp e8 -. \stemUp fis8 -.
    \stemUp e8 -. \stemUp g8 -. \stemUp fis8 -. \stemUp g8 -. | % 144
    \stemUp e8 -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp g8
    -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp b8 -.
    \stemDown a8 -. \stemDown b8 -. \stemDown c8 -. \pageBreak | % 145
    r1 s2 | % 146
    \stemDown fis8 ( -> _\p \stemDown g8 \stemDown fis8 \stemDown e8
    \stemDown d8 \stemDown c8 ) r2.*2/3 s4 | % 147
    \stemUp b,8 -. _\p \stemUp c8 -. \stemUp b8 -. \stemUp dis8 -.
    \stemUp cisis8 -. \stemUp dis8 -. \stemUp c8 -. \stemUp e8 -.
    \stemUp c8 -. \stemUp e8 -. \stemUp dis8 -. \stemUp e8 -. | % 148
    \stemUp g8 -. _\markup{ \small\italic {poco cresc.} }
    \startTrillSpan \stemUp fis8 -. \stemUp e8 -. \stemUp a8 -. \stemUp
    g8 -. \stemUp fis8 -. \stemUp b8 -. \stemUp a8 -. \stemUp g8 -.
    \stemDown c8 -. \stemDown b8 -. \stemDown a8 -. | % 149
    \stemDown b8 -. \stopTrillSpan _\mp \stemDown c8 -. \stemDown b8 -.
    \stemDown dis8 -. \stemDown cisis8 -. \stemDown dis8 -. \stemDown c8
    -. \stemDown e8 -. \stemDown c8 -. \stemDown e8 -. \stemDown dis8 -.
    \stemDown e8 -. \pageBreak | \barNumberCheck #150
    \stemDown g8 -. _\markup{ \small\italic {poco cresc.} }
    \startTrillSpan \stemDown fis8 -. \stemDown e8 -. \stemDown a8 -.
    \stemDown g8 -. \stemDown fis8 -. \stemDown b8 -. \stemDown a8 -.
    \stemDown g8 -. \stemDown c8 -. \stemDown b8 -. \stemDown a8 -. | % 151
    \stemDown d8 -. \stopTrillSpan _\mf _\markup{ \small\italic {dim.} }
    \startTrillSpan \stemDown b8 -. \stemDown c8 -. \stemDown a8 -.
    \stemDown b8 -. \stemDown g8 -. \stemDown a8 -. \stemDown fis8 -.
    \stemDown g8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown d8 -. | % 152
    \stemDown e8 -. _\> \stemDown c8 -. \stemDown d8 -. \stemDown b8 -.
    \stemDown c8 -. \stemDown a8 -. \stemUp b8 -. \stemUp g8 -. \stemUp
    a8 -. \stemUp fis8 -. \stopTrillSpan _\! _\p \stemUp a8 -. \stemUp
    fis8 -. | % 153
    r1 s2 | % 154
    r1 s2 \pageBreak | % 155
    r2.*2/3 r4.*2/3 \stemDown c''8 _\mf ^ "pizz." r8*2/3 r8*2/3 s1*11/24
    | % 156
    \stemDown c8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 157
    \stemDown b,8 -. _\p _\ leggiero ^ "arco" r8*2/3 r8*2/3 \stemDown
    cis8 -. r8*2/3 \stemDown cis8 ( \stemDown b8 ) r8*2/3 r8*2/3
    \stemDown g'8 -. r8*2/3 r8*2/3 s1*7/24 | % 158
    \stemDown fis8 -. r8*2/3 r8*2/3 \once \omit TupletBracket
    \times 6/7  {
        \stemDown e16*721/720 ( \stemDown fis16*721/720 \stemDown e16*721/720
        \stemDown fis16*721/720 \stemDown e16*721/720 \stemDown fis16*721/720
        \stemDown e16*721/720 }
    \stemDown d8 ) r8*2/3 r8*2/3 \stemDown cis8 -. r8*2/3 r8*2/3
    s1*479/1920 \break | % 159
    \stemDown b8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 |
    \barNumberCheck #160
    r1 s2 | % 161
    \stemDown b8 -. _\p r8*2/3 r8*2/3 \stemDown cis8 -. r8*2/3 \stemDown
    cis8 ( \stemDown b8 ) r8*2/3 r8*2/3 \stemDown g'8 -. r8*2/3 r8*2/3
    s1*7/24 | % 162
    \stemDown fis8 -. r8*2/3 r8*2/3 \once \omit TupletBracket
    \times 6/7  {
        \stemDown e16*721/720 ( _\< \stemDown fis16*721/720 \stemDown e16*721/720
        \stemDown fis16*721/720 \stemDown e16*721/720 \stemDown fis16*721/720
        \stemDown e16*721/720 }
    \stemDown d8 ) r8*2/3 r8*2/3 \stemDown cis8 -. r8*2/3 r8*2/3
    s1*479/1920 _\! \pageBreak | % 163
    \stemDown b8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 164
    r1 s2 | % 165
    \stemDown d8 -. _\p r8*2/3 r8*2/3 \stemDown e8 r8*2/3 \stemDown e8 (
    \stemDown d8 ) r8*2/3 r8*2/3 \stemDown b'8 -. r8*2/3 r8*2/3 s1*7/24
    | % 166
    \stemDown a8 -. r8*2/3 r8*2/3 \once \omit TupletBracket
    \times 6/7  {
        \stemDown g16*721/720 ( _\< \stemDown a16*721/720 \stemDown g16*721/720
        \stemDown a16*721/720 \stemDown g16*721/720 \stemDown a16*721/720
        \stemDown g16*721/720 }
    \stemDown fis8 ) r8*2/3 r8*2/3 \stemDown e8 -. r8*2/3 r8*2/3
    s1*479/1920 _\! \pageBreak | % 167
    \stemDown d8 -. _\mp r8*2/3 r8*2/3 r4.*2/3 \stemDown fis8 -. _\<
    \stemDown g8 -. \stemDown fis8 -. \stemDown b,8 -. \stemDown d8 -.
    \stemDown b8 -. s1*5/24 | % 168
    \stemDown c8 -. \stemDown dis8 -. \stemDown c8 -. \stemDown cis8 -.
    \stemDown fis8 -. \stemDown cis8 -. \stemDown dis8 -. \stemDown fis8
    -. \stemDown dis8 -. \stemDown e8 -. \stemDown g8 -. \stemDown e8 -.
    | % 169
    \stemDown fis8 -. _\! _\f \stemDown a8 -. \stemDown d8 -. \stemDown
    es8 -. r8*2/3 r8*2/3 r2.*2/3 s1*1/3 | \barNumberCheck #170
    \stemDown fis,8 -. _\f \stemDown a8 -. \stemDown d8 -. \stemDown es8
    -. r8*2/3 r8*2/3 r2.*2/3 s1*1/3 \pageBreak | % 171
    r1 s2 | % 172
    r1 s2 | % 173
    r1 s2 | % 174
    \numericTimeSignature\time 4/4  \stemUp a,,,8 _\p ^ "pizz." r8
    \stemUp d8 r8 \stemUp a'8 r8 \stemDown d8 r8 \pageBreak | % 175
    \stemDown g8 r8 \stemDown d8 r8 \stemUp a8 r8 \stemUp e8 r8 | % 176
    \stemUp a8 r8 \stemDown d8 r8 \stemDown b8 r8 \stemUp d,8 _\<
    \stemUp e8 | % 177
    \stemUp fis8 \stemUp g8 \stemUp a8 \stemUp b8 \stemDown c8 _\! _\mf
    r8 \stemUp b8 \stemUp a8 | % 178
    \stemDown d8 _\> r8 \stemUp <g,, g'>8 r8 \stemUp <g g'>8 r8 _\! r4 | % 179
    \time 12/8  \stemDown d''8 -. _\p ^ "arco" \stemDown e8 -. \stemDown
    d8 -. \stemDown fis8 -. \stemDown eis8 -. \stemDown fis8 -.
    \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown g8 -.
    \stemDown fis8 -. \stemDown g8 -. \pageBreak | \barNumberCheck #180
    \stemDown e8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown a8 -.
    \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown a8 -.
    \stemDown b8 -. \stemDown a8 -. \stemDown b8 -. \stemDown c8 -. | % 181
    r1 s2 | % 182
    r2.*2/3 \stemDown b8 ( -> _\p \stemDown g8 \stemDown e8 \stemDown g8
    \stemDown d8 \stemDown b8 ) s4 | % 183
    \stemDown es4. _\f _\ marcato \stemDown d4. \stemDown c4. \stemDown
    bes4 ( ~ \stemUp bes16 \stemUp as16 ) \pageBreak | % 184
    \stemUp g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 185
    r2.*2/3 \stemUp g,8 ( _\f \stemUp as8 \stemUp bes8 ) \stemUp c8 (
    \stemUp bes8 \stemUp as8 s4 | % 186
    \stemUp g8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 187
    \stemDown g''4. _\ff \stemDown f4. \stemDown es4. \stemDown d4 ( ~
    \stemDown d16 \stemDown c16 ) | % 188
    \stemDown bes8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 \pageBreak | % 189
    r2.*2/3 \stemUp bes,8 ( _\ff \stemUp c8 \stemUp d8 ) \stemUp es8 (
    \stemUp d8 \stemUp c8 s4 | \barNumberCheck #190
    \stemUp bes8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 191
    \numericTimeSignature\time 4/4  \stemUp g'8 ( _\ff \stemUp fis8
    \stemUp e8 \stemUp d8 ) \stemUp g8 ( \stemUp fis8 \stemUp e8 \stemUp
    d8 ) | % 192
    \stemUp g8 ( \stemUp f8 \stemUp e8 \stemUp d8 ) \stemUp g8 ( \stemUp
    f8 \stemUp e8 \stemUp d8 ) | % 193
    \time 12/8  \stemDown g''8 _\ff \stemDown fis8 \stemDown e8
    \stemDown d8 \stemDown cis8 \stemDown b8 \stemDown a8 \stemDown g8
    \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown cis8 \pageBreak | % 194
    \numericTimeSignature\time 4/4  R1*7 \pageBreak | % 201
    R1*5 \pageBreak | % 206
    R1*5 \pageBreak | % 211
    R1*5 \pageBreak | % 216
    R1*5 \pageBreak | % 221
    R1*4 \pageBreak | % 225
    R1*3 \pageBreak | % 228
    R1*5 \pageBreak | % 233
    R1*5 \pageBreak | % 238
    R1*5 \pageBreak | % 243
    R1*5 \pageBreak | % 248
    R1*6 \pageBreak | % 254
    R1*5 \pageBreak | % 259
    R1*5 \pageBreak | % 264
    R1*5 \pageBreak | % 269
    R1*5 \pageBreak | % 274
    R1*7 \pageBreak | % 281
    R1*6 \pageBreak | % 287
    R1*5 \pageBreak | % 292
    R1*5 \pageBreak | % 297
    R1*5 \pageBreak | % 302
    R1*6 \pageBreak | % 308
    R1*6 \pageBreak | % 314
    R1*6 \pageBreak | \barNumberCheck #320
    R1*5 \pageBreak | % 325
    R1*3 \pageBreak | % 328
    R1*4 \pageBreak | % 332
    R1*4 \pageBreak | % 336
    R1*5 \pageBreak | % 341
    R1*7 \bar "|."
    }

PartPOneNineVoiceOne =  \relative e'' {
    \clef "treble" \time 12/8 \key g \major | % 1
    r1 s2 | % 2
    r1 s2 | % 3
    r1 s2 | % 4
    \stemDown e8 ( -> _\p \stemDown d8 \stemDown c8 \stemUp b8 \stemUp a8
    \stemUp g8 ) r2.*2/3 s4 \pageBreak | % 5
    r1 _ "Vln. II" _ "(div.)" s2 | % 6
    r1 s2 | % 7
    r1 \bar "||"
    s2 | % 8
    \stemDown c8 ( -> _\p \stemDown b8 \stemDown a8 \stemUp g8 \stemUp
    fis8 \stemUp e8 ) r2.*2/3 s4 | % 9
    r1 s2 \pageBreak | \barNumberCheck #10
    \numericTimeSignature\time 4/4  r4 _ "Vln. II" _ "(div.)" \stemDown
    e''8 _\mp ^ "pizz." \stemDown b8 r2 | % 11
    \time 12/8  \stemUp g,8 -. _\mp ^ "arco" \stemUp a8 -. \stemUp g8 -.
    \stemUp fis8 -. \stemUp eis8 -. \stemUp fis8 -. \stemDown a8 -.
    \stemDown c8 -. \stemDown a8 -. \stemUp g8 -. \stemUp fis8 -.
    \stemUp g8 -. | % 12
    \stemDown b8 -. _\markup{ \small\italic {poco cresc.} }
    \startTrillSpan \stemDown d8 -. \stemDown c8 -. \stemDown c8 -.
    \stemDown e8 -. \stemDown dis8 -. \stemDown dis8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown e8 -. \stemDown g8 -. \stemDown fis8 -.
    | % 13
    \stemDown fis8 -. \stopTrillSpan _\mf _\markup{ \small\italic {dim.}
        } \startTrillSpan \stemDown g8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown d8 -. \stemDown e8 -. \stemDown c8 -. \stemDown d8 -.
    \stemDown b8 -. \stemDown c8 -. \stemDown a8 -. \stemDown b8 -. | % 14
    r1 \stopTrillSpan s2 \break | % 15
    \stemDown fis'8 -. _\p _ "Vln. II" _ "(div.)" \stemDown g8 -.
    \stemDown e8 -. \stemDown fis8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown c8 -. _\markup{ \small\italic {dim.} } \startTrillSpan
    \stemDown d8 -. \stemDown b8 -. \stemDown c8 -. \stemDown a8 -.
    \stemDown b8 -. | % 16
    \stemUp g8 -. \stemUp a8 -. \stemUp fis8 -. \stemUp g8 -. \stemUp e8
    -. \stemUp fis8 -. \stemUp d8 -. \stemUp e8 -. \stemUp c8 -. \stemUp
    d8 -. \stopTrillSpan _\pp \stemUp e8 -. \stemUp d8 -. | % 17
    r1 s2 | % 18
    \stemDown c'8 _\mf ^ "pizz." r8*2/3 r8*2/3 \stemDown c8 r8*2/3 r8*2/3
    r2.*2/3 s1*5/12 | % 19
    r1 s2 \pageBreak | \barNumberCheck #20
    r1 _ "Vln. II" _ "(div.)" s2 | % 21
    \stemDown b8 -. _\p ^ "arco" \stemDown cis8 -. \stemDown b8 -.
    \stemDown cis8 -. \stemDown d8 -. \stemDown cis8 -. \stemDown d8 -.
    \stemDown e8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown e8 -. | % 22
    \stemDown f8 -. \stemDown g8 -. \stemDown f8 -. \stemDown g8 -.
    \stemDown a8 -. \stemDown g8 -. \stemDown gis8 -. \stemDown ais8 -.
    \stemDown gis8 -. \stemDown ais8 -. \stemDown b8 -. \stemDown ais8
    -. | % 23
    \stemDown b8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 \break | % 24
    r1 _ "Vln. II" _ "(div.)" s2 | % 25
    \stemDown b,8 -. _\p \stemDown cis8 -. \stemDown b8 -. \stemDown cis8
    -. \stemDown d8 -. \stemDown cis8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -. | % 26
    \stemDown f8 -. \stemDown g8 -. \stemDown f8 -. \stemDown g8 -.
    \stemDown a8 -. \stemDown g8 -. \stemDown gis8 -. \stemDown a8 -.
    \stemDown gis8 -. \stemDown cis8 -. \stemDown d8 -. \stemDown cis8
    -. | % 27
    \stemDown d8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 \pageBreak | % 28
    r1 _ "Vln. II" _ "(div.)" s2 | % 29
    \stemDown d,8 -. _\mp _\< \stemDown e8 -. \stemDown d8 -. \stemDown
    e8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown a,8 -. \stemDown d8
    -. \stemDown a8 -. \stemUp g8 -. \stemUp a8 -. \stemUp g8 -. |
    \barNumberCheck #30
    \stemUp a8 -. \stemUp b8 -. \stemUp a8 -. \stemUp a8 -. \stemUp b8
    -. \stemUp a8 -. \stemDown b8 -. \stemDown cis8 -. \stemDown b8 -.
    \stemDown cis8 -. \stemDown d8 -. \stemDown cis8 -. | % 31
    \stemDown d8 -. _\! _\f \stemDown e8 -. \stemDown fis8 -. \stemDown
    g8 -. r8*2/3 r8*2/3 r2.*2/3 s1*1/3 \pageBreak | % 32
    \stemDown d8 -. _\f _ "Vln. II" _ "(div.)" \stemDown e8 -. \stemDown
    fis8 -. \stemDown g8 -. r8*2/3 r8*2/3 r2.*2/3 s1*1/3 | % 33
    \stemDown d8 -. _\mf \stemDown e8 -. \stemDown fis8 -. \stemDown g8
    -. r8*2/3 r8*2/3 r2.*2/3 s1*1/3 | % 34
    \stemDown d8 -. _\mp \stemDown e8 -. \stemDown fis8 -. \stemDown g8
    -. r8*2/3 r8*2/3 r2.*2/3 s1*1/3 | % 35
    \stemDown d8 _\p \stemDown e8 -. \stemDown fis8 -. r4.*2/3 \stemDown
    d8 -. \stemDown e8 -. \stemDown fis8 -. r4.*2/3 s4 \pageBreak | % 36
    \stemDown d8 -. _ "Vln. II" _ "(div.)" \stemDown e8 -. \stemDown fis8
    -. r4.*2/3 \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -. r4.*2/3
    s4 | % 37
    \stemUp b,8 -. _\p \stemUp g8 -. \stemUp b8 -. \stemUp a8 -. \stemUp
    gis8 -. \stemUp a8 -. \stemDown c8 -. \stemDown a8 -. \stemDown c8
    -. \stemUp b8 -. \stemUp ais8 -. \stemUp b8 -. | % 38
    \stemDown c8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown e8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown a8 -. | % 39
    r1 s2 | \barNumberCheck #40
    r2.*2/3 \stemDown e8 ( -> _\p \stemDown d8 \stemDown c8 \stemUp b8
    \stemUp a8 \stemUp g8 ) s4 \pageBreak | % 41
    \stemUp b8 -. _ "Vln. II" _ "(div.)" \stemUp g8 -. \stemUp b8 -.
    \stemUp a8 -. \stemUp gis8 -. \stemUp a8 -. \stemDown c8 -.
    \stemDown a8 -. \stemDown c8 -. \stemUp b8 -. \stemUp ais8 -.
    \stemUp b8 -. | % 42
    \stemDown c8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown e8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown a8 -. | % 43
    r1 s2 | % 44
    r2.*2/3 \stemDown e8 ( -> _\p \stemDown d8 \stemDown c8 \stemUp b8
    \stemUp a8 \stemUp g8 ) s4 | % 45
    r1 s2 \pageBreak | % 46
    \stemDown es'4. _\f _ "Vln. II" _ "(div.)" -\markup{ \italic
        {marcato} } \stemDown d4. \stemDown c4. \stemDown bes4 ( ~
    \stemUp bes16 \stemUp as16 | % 47
    \stemUp g8 ) r8*2/3 r8*2/3 r4.*2/3 \stemUp g8 ( \stemUp as8 \stemUp
    bes8 ) \stemDown c8 ( \stemDown bes8 \stemDown as8 s1*5/24 | % 48
    \stemUp g8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 49
    \stemUp b,8 -. _\ff \stemUp cis8 -. \stemUp b8 -. \stemUp cis8 -.
    \stemUp dis8 -. \stemUp cis8 -. \stemUp dis8 -. \stemUp fis8 -.
    \stemUp dis8 -. \stemUp fis8 -. \stemUp gis8 -. \stemUp fis8 -. |
    \barNumberCheck #50
    \stemDown b8 -. \stemDown cis8 -. \stemDown b8 -. \stemUp fis8 -.
    \stemUp b8 -. \stemUp fis8 -. \stemDown b8 -. \stemDown cis8 -.
    \stemDown b8 -. \stemDown cis8 -. \stemDown e8 -. \stemDown cis8 -.
    \pageBreak | % 51
    r1 s2 | % 52
    r1 s2 | % 53
    r1 s2 | % 54
    r1 s2 | % 55
    r1 s2 \pageBreak | % 56
    r1 s2 | % 57
    r1 s2 | % 58
    r1 s2 | % 59
    r1 s2 | \barNumberCheck #60
    r1 s2 \pageBreak | % 61
    r1 s2 | % 62
    r1 s2 | % 63
    r1 s2 | % 64
    r1 s2 | % 65
    r1 s2 \pageBreak | % 66
    r1 s2 | % 67
    r1 s2 | % 68
    r1 s2 | % 69
    r1 s2 | \barNumberCheck #70
    r1 \bar "||"
    s2 \pageBreak | % 71
    \key e \major r1 s2 | % 72
    r1 s2 | % 73
    r1 s2 | % 74
    r1 s2 | % 75
    r1 s2 \break | % 76
    r1 s2 | % 77
    r1 s2 | % 78
    r1 s2 | % 79
    r1 s2 | \barNumberCheck #80
    r1 s2 \pageBreak | % 81
    r1 s2 | % 82
    r1 s2 | % 83
    r1 s2 | % 84
    r1 s2 | % 85
    r1 s2 \pageBreak | % 86
    r1 s2 | % 87
    r1 s2 | % 88
    r1 s2 | % 89
    r1 s2 \pageBreak | \barNumberCheck #90
    r1 s2 | % 91
    r1 s2 | % 92
    r1 s2 | % 93
    r1 s2 | % 94
    r1 s2 | % 95
    r1 s2 \pageBreak | % 96
    r1 s2 | % 97
    r1 s2 | % 98
    r1 s2 | % 99
    r1 s2 | \barNumberCheck #100
    r1 s2 | % 101
    r1 s2 \break | % 102
    r1 s2 | % 103
    r1 s2 | % 104
    r1 s2 | % 105
    r1 s2 | % 106
    r1 s2 \pageBreak | % 107
    r1 s2 | % 108
    r1 s2 | % 109
    r1 s2 | \barNumberCheck #110
    r1 s2 | % 111
    r1 s2 | % 112
    r1 s2 \break | % 113
    r1 s2 | % 114
    r1 s2 | % 115
    r1 s2 | % 116
    r1 s2 | % 117
    r1 s2 \pageBreak | % 118
    r1 s2 | % 119
    r1 r2*2/3 s1*1/6 | \barNumberCheck #120
    r1 r2*2/3 s1*1/6 | % 121
    r1 r2*2/3 s1*1/6 | % 122
    r1 r2*2/3 s1*1/6 \break | % 123
    r1 r2*2/3 s1*1/6 | % 124
    r1 r2*2/3 s1*1/6 | % 125
    r1 r2*2/3 s1*1/6 | % 126
    r1 r2*2/3 s1*1/6 | % 127
    r1 r2*2/3 s1*1/6 \pageBreak | % 128
    r1 r2*2/3 s1*1/6 | % 129
    r1 r2*2/3 s1*1/6 | \barNumberCheck #130
    r1 s2 | % 131
    r1 r2*2/3 s1*1/6 \pageBreak | % 132
    r1 s2 | % 133
    r1 s2 | % 134
    r1 s2 | % 135
    r1 s2 \pageBreak | % 136
    \time 4/4 \omit Staff.TimeSignature \stemDown c8 :16 _ "Vln. II" _
    "(div.)" \stemDown d8 :16 \stemDown e8 :16 \stemDown fis8 :16
    \stemDown g8 :16 r8 r4 | % 137
    \time 12/8  \stemUp c,,8 ( \stemUp b8 ) \stemUp a8 -. \stemUp g8 -.
    r8*2/3 r8*2/3 r4.*2/3 r8*2/3 \stemUp g8 -. _\mf \stemUp b8 -. s4 | % 138
    \stemUp c8 ( \stemUp b8 ) \stemUp a8 -. \stemUp g8 -. r8*2/3 r8*2/3
    r2.*2/3 \bar "||"
    s1*1/3 | % 139
    \key g \major r4.*2/3 r8*2/3 \stemDown d'''8 ( _\p \stemDown d,8 ) r4.*2/3
    r8*2/3 \stemDown e'8 ( \stemDown e,8 ) s1*1/3 \pageBreak |
    \barNumberCheck #140
    r4.*2/3 \stemDown d'8 _ "Vln. II" _ "(div.)" ^ "pizz." r8*2/3 r8*2/3
    \stemDown b,4 ( ^ "arco" \stemUp e,8 ) \stemDown c'4 ( \stemUp fis,8
    ) s1*5/24 | % 141
    r1 s2 | % 142
    \stemDown e'8 ( -> _\p \stemDown d8 \stemDown c8 \stemUp b8 \stemUp
    a8 \stemUp g8 ) r2.*2/3 s4 | % 143
    r4.*2/3 r8*2/3 \stemDown d''8 ( _\p \stemDown d,8 ) r4.*2/3 r8*2/3
    \stemDown e'8 ( \stemDown e,8 ) s1*1/3 | % 144
    r4.*2/3 \stemDown d'8 ^ "pizz." r8*2/3 r8*2/3 \stemDown b,4 ( ^
    "arco" \stemUp e,8 ) \stemDown c'4 ( \stemUp fis,8 ) s1*5/24
    \pageBreak | % 145
    r1 _ "Vln. II" _ "(div.)" s2 | % 146
    \stemDown c'8 ( -> _\p \stemDown b8 \stemDown a8 \stemUp g8 \stemUp
    fis8 \stemUp e8 ) r2.*2/3 s4 | % 147
    r1 s2 | % 148
    \numericTimeSignature\time 4/4  r4 \stemDown e''8 _\mp ^ "pizz."
    \stemDown b8 r2 | % 149
    \time 12/8  \stemUp g,8 -. _\mp ^ "arco" \stemUp a8 -. \stemUp g8 -.
    \stemUp fis8 -. \stemUp eis8 -. \stemUp fis8 -. \stemDown a8 -.
    \stemDown c8 -. \stemDown a8 -. \stemUp g8 -. \stemUp fis8 -.
    \stemUp g8 -. \pageBreak | \barNumberCheck #150
    \stemDown b8 -. _ "Vln. II" _ "(div.)" _\markup{ \small\italic {poco
            cresc.} } \startTrillSpan \stemDown d8 -. \stemDown c8 -.
    \stemDown c8 -. \stemDown e8 -. \stemDown dis8 -. \stemDown dis8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown e8 -. \stemDown g8 -.
    \stemDown fis8 -. | % 151
    \stemDown fis8 -. \stopTrillSpan _\mf _\markup{ \small\italic {dim.}
        } \startTrillSpan \stemDown g8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown c8 -. \stemDown d8 -. \stemDown b8 -. \stemDown c8 -. | % 152
    r1 s2 \stopTrillSpan | % 153
    \stemDown fis8 -. _\p \stemDown g8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown d8 -. \stemDown e8 -. \stemDown c8 -. _\markup{
        \small\italic {dim.} } \startTrillSpan \stemDown d8 -. \stemDown
    b8 -. \stemDown c8 -. \stemDown a8 -. \stemDown b8 -. | % 154
    \stemUp g8 -. \stemUp a8 -. \stemUp fis8 -. \stemUp g8 -. \stemUp e8
    -. \stemUp fis8 -. \stemUp d8 -. \stemUp e8 -. \stemUp c8 -. \stemUp
    d8 -. \stopTrillSpan _\pp \stemUp e8 -. \stemUp d8 -. \pageBreak | % 155
    r1 _ "Vln. II" _ "(div.)" s2 | % 156
    \stemDown c'8 _\mf ^ "pizz." r8*2/3 r8*2/3 \stemDown c8 _\mp r8*2/3
    r8*2/3 r2.*2/3 s1*5/12 | % 157
    r1 s2 | % 158
    r1 s2 \break | % 159
    \stemDown b8 -. _\p _ "Vln. II" _ "(div.)" ^ "arco" \stemDown cis8
    -. \stemDown b8 -. \stemDown cis8 -. \stemDown d8 -. \stemDown cis8
    -. \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown fis8 -. \stemDown e8 -. | \barNumberCheck #160
    \stemDown f8 -. \stemDown g8 -. \stemDown f8 -. \stemDown g8 -.
    \stemDown a8 -. \stemDown g8 -. \stemDown gis8 -. \stemDown ais8 -.
    \stemDown gis8 -. \stemDown ais8 -. \stemDown b8 -. \stemDown ais8
    -. | % 161
    \stemDown b8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 162
    r1 s2 \pageBreak | % 163
    \stemDown b,8 -. _\p _ "Vln. II" _ "(div.)" \stemDown cis8 -.
    \stemDown b8 -. \stemDown cis8 -. \stemDown d8 -. \stemDown cis8 -.
    \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown fis8 -. \stemDown e8 -. | % 164
    \stemDown f8 -. \stemDown g8 -. \stemDown f8 -. \stemDown g8 -.
    \stemDown a8 -. \stemDown g8 -. \stemDown gis8 -. \stemDown a8 -.
    \stemDown gis8 -. \stemDown cis8 -. \stemDown d8 -. \stemDown cis8
    -. | % 165
    \stemDown d8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 166
    r1 s2 \pageBreak | % 167
    \stemDown d,8 -. _\mp _ "Vln. II" _ "(div.)" _\< \stemDown e8 -.
    \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -.
    \stemDown a,8 -. \stemDown d8 -. \stemDown a8 -. \stemUp g8 -.
    \stemUp a8 -. \stemUp g8 -. | % 168
    \stemUp a8 -. \stemUp b8 -. \stemUp a8 -. \stemUp a8 -. \stemUp b8
    -. \stemUp a8 -. \stemDown b8 -. \stemDown cis8 -. \stemDown b8 -.
    \stemDown cis8 -. \stemDown d8 -. \stemDown cis8 -. | % 169
    \stemDown d8 -. _\! _\f \stemDown e8 -. \stemDown fis8 -. \stemDown
    g8 -. r8*2/3 r8*2/3 r2.*2/3 s1*1/3 | \barNumberCheck #170
    \stemDown d8 -. _\f \stemDown e8 -. \stemDown fis8 -. \stemDown g8
    -. r8*2/3 r8*2/3 r2.*2/3 s1*1/3 \pageBreak | % 171
    \stemDown d8 -. _\mf _ "Vln. II" _ "(div.)" \stemDown e8 -.
    \stemDown fis8 -. \stemDown g8 -. r8*2/3 r8*2/3 r2.*2/3 s1*1/3 | % 172
    \stemDown d8 -. _\mp \stemDown e8 -. \stemDown fis8 -. \stemDown g8
    -. r8*2/3 r8*2/3 r2.*2/3 s1*1/3 | % 173
    \stemDown d8 -. _\p \stemDown e8 -. \stemDown fis8 -. r4.*2/3
    \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -. r4.*2/3 s4 | % 174
    \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -. r4.*2/3 \stemDown
    d8 -. \stemDown e8 -. \stemDown fis8 -. r4.*2/3 s4 \pageBreak | % 175
    \stemUp b,8 -. _\p _ "Vln. II" _ "(div.)" \stemUp g8 -. \stemUp b8
    -. \stemUp a8 -. \stemUp gis8 -. \stemUp a8 -. \stemDown c8 -.
    \stemDown a8 -. \stemDown c8 -. \stemUp b8 -. \stemUp ais8 -.
    \stemUp b8 -. | % 176
    \stemDown c8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown e8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown a8 -. | % 177
    r1 s2 | % 178
    r2.*2/3 \stemDown e8 ( -> _\p \stemDown d8 \stemDown c8 \stemUp b8
    \stemUp a8 \stemUp g8 ) s4 | % 179
    \stemUp b8 -. _\p \stemUp g8 -. \stemUp b8 -. \stemUp a8 -. \stemUp
    gis8 -. \stemUp a8 -. \stemDown c8 -. \stemDown a8 -. \stemDown c8
    -. \stemUp b8 -. \stemUp ais8 -. \stemUp b8 -. \pageBreak |
    \barNumberCheck #180
    \stemDown c8 -. _ "Vln. II" _ "(div.)" \stemDown d8 -. \stemDown e8
    -. \stemDown fis8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown fis8 -. \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -.
    \stemDown a8 -. | % 181
    r1 s2 | % 182
    r2.*2/3 \stemDown e8 ( -> _\p \stemDown d8 \stemDown c8 \stemUp b8
    \stemUp a8 \stemUp g8 ) s4 | % 183
    r1 s2 \pageBreak | % 184
    \stemDown es'4. _\f _\ marcato _ "Vln. II" _ "(div.)" \stemDown d4.
    \stemDown c4. \stemDown bes4 ( ~ \stemUp bes16 \stemUp as16 ) | % 185
    \stemUp g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 186
    r1 s2 | % 187
    r1 s2 | % 188
    \stemDown g'4. \stemDown f4. \stemDown es4. \stemDown d4 ( ~
    \stemDown d16 \stemDown c16 ) \pageBreak | % 189
    \stemDown bes8 _ "Vln. II" _ "(div.)" r8*2/3 r8*2/3 r4.*2/3 r2.*2/3
    s1*11/24 | \barNumberCheck #190
    r1 s2 | % 191
    r2.*2/3 \stemDown a'8 -. _\ff \stemDown b8 -. \stemDown a8 -.
    \stemDown a8 -. \stemDown d8 -. \stemDown a8 -. s4 | % 192
    r2.*2/3 \stemDown g8 -. _\ff \stemDown a8 -. \stemDown g8 -.
    \stemDown g8 -. \stemDown d'8 -. \stemDown g,8 -. s4 | % 193
    \stemDown g8 _\ff \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown
    cis8 \stemDown b8 \stemUp a8 \stemUp g8 \stemUp fis8 \stemUp e8
    \stemUp d8 \stemUp cis8 \pageBreak | % 194
    \numericTimeSignature\time 4/4  R1*7 \pageBreak | % 201
    R1*5 \pageBreak | % 206
    R1*5 \pageBreak | % 211
    R1*5 \pageBreak | % 216
    R1*5 \pageBreak | % 221
    R1*4 \pageBreak | % 225
    R1*3 \pageBreak | % 228
    R1*5 \pageBreak | % 233
    R1*5 \pageBreak | % 238
    R1*5 \pageBreak | % 243
    R1*5 \pageBreak | % 248
    R1*6 \pageBreak | % 254
    R1*5 \pageBreak | % 259
    R1*5 \pageBreak | % 264
    R1*5 \pageBreak | % 269
    R1*5 \pageBreak | % 274
    R1*7 \pageBreak | % 281
    R1*6 \pageBreak | % 287
    R1*5 \pageBreak | % 292
    R1*5 \pageBreak | % 297
    R1*5 \pageBreak | % 302
    R1*6 \pageBreak | % 308
    R1*6 \pageBreak | % 314
    R1*6 \pageBreak | \barNumberCheck #320
    R1*5 \pageBreak | % 325
    R1*3 \pageBreak | % 328
    R1*4 \pageBreak | % 332
    R1*4 \pageBreak | % 336
    R1*5 \pageBreak | % 341
    R1*7 \bar "|."
    }

PartPTwoZeroVoiceOne =  \relative ais' {
    \clef "treble" \time 12/8 \key g \major | % 1
    r1 s2 | % 2
    r1 s2 | % 3
    r1 s2 | % 4
    \stemUp ais8 ( -> _\p \stemUp b8 \stemUp a8 \stemUp g8 \stemUp es8
    \stemUp d8 ) r2.*2/3 s4 \pageBreak | % 5
    r1 s2 | % 6
    r1 s2 | % 7
    r1 \bar "||"
    s2 | % 8
    \stemUp fis8 ( ^> _\p \stemUp g8 \stemUp fis8 \stemUp e8 \stemUp c8
    \stemUp b8 ) r2.*2/3 s4 | % 9
    r1 s2 \pageBreak | \barNumberCheck #10
    \numericTimeSignature\time 4/4  r2 \stemDown fis''8 _\mp ^ "pizz."
    \stemDown c8 r4 | % 11
    \time 12/8  r4.*2/3 \stemUp dis,8 -. _\mp ^ "arco" \stemUp cisis8 -.
    \stemUp dis8 -. r4.*2/3 \stemUp e8 -. \stemUp dis8 -. \stemUp e8 -.
    s4 | % 12
    \stemUp g8 -. _\markup{ \small\italic {poco cresc.} }
    \startTrillSpan \stemUp fis8 -. \stemUp e8 -. \stemUp a8 -. \stemUp
    g8 -. \stemUp fis8 -. \stemUp b8 -. \stemUp a8 -. \stemUp g8 -.
    \stemDown c8 -. \stemDown b8 -. \stemDown a8 -. | % 13
    \stemDown d8 -. \stopTrillSpan _\mf _\markup{ \small\italic {dim.} }
    \startTrillSpan \stemDown b8 -. \stemDown c8 -. \stemUp a8 -.
    \stemUp b8 -. \stemUp g8 -. \stemUp a8 -. \stemUp fis8 -. \stemUp g8
    -. \stemUp e8 -. \stemUp fis8 -. \stemUp d8 -. | % 14
    r1 \stopTrillSpan s2 \break | % 15
    \stemDown d'8 -. _\p \stemDown b8 -. \stemDown c8 -. \stemUp a8 -.
    \stemUp b8 -. \stemUp g8 -. \stemUp a8 -. _\markup{ \small\italic
        {dim.} } \startTrillSpan \stemUp fis8 -. \stemUp g8 -. \stemUp e8
    -. \stemUp fis8 -. \stemUp d8 -. | % 16
    \stemUp e8 -. \stemUp c8 -. \stemUp d8 -. \stemUp b8 -. \stemUp c8
    -. \stemUp a8 -. \stemUp b8 -. \stopTrillSpan _\pp \stemUp g8 -.
    \stemUp a8 -. r4.*2/3 s8 | % 17
    r1 s2 | % 18
    r4.*2/3 \stemUp c8 _\mp ^ "pizz." r8*2/3 r8*2/3 \stemUp c8 r8*2/3 r8*2/3
    r4.*2/3 s1*5/12 | % 19
    r1 s2 \pageBreak | \barNumberCheck #20
    r1 s2 | % 21
    \stemUp d8 -. _\p ^ "arco" \stemUp fis8 -. \stemUp d8 -. \stemUp e8
    -. \stemUp g8 -. \stemUp e8 -. \stemUp fis8 -. \stemUp b8 -. \stemUp
    fis8 -. \stemUp g8 -. \stemUp b8 -. \stemUp g8 -. | % 22
    \stemUp gis8 -. \stemUp b8 -. \stemUp gis8 -. \stemDown ais8 -.
    \stemDown cis8 -. \stemDown ais8 -. \stemDown b8 -. \stemDown d8 -.
    \stemDown b8 -. \stemDown cis8 -. \stemDown e8 -. \stemDown cis8 -.
    | % 23
    \stemDown d8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 \break | % 24
    r1 s2 | % 25
    \stemUp d,8 -. _\p \stemUp fis8 -. \stemUp d8 -. \stemUp e8 -.
    \stemUp g8 -. \stemUp e8 -. \stemUp fis8 -. \stemUp b8 -. \stemUp
    fis8 -. \stemUp g8 -. \stemUp b8 -. \stemUp g8 -. | % 26
    \stemUp gis8 -. \stemUp b8 -. \stemUp gis8 -. \stemDown ais8 -.
    \stemDown cis8 -. \stemDown ais8 -. \stemDown b8 -. \stemDown d8 -.
    \stemDown b8 -. \stemDown cis8 -. \stemDown g'8 -. \stemDown cis,8
    -. | % 27
    \stemDown fis8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 \pageBreak
    | % 28
    r2.*2/3 r4.*2/3 \stemUp g,4. ( _\mp _\< s4. | % 29
    \stemUp fis8 ) -. \stemUp a8 -. \stemUp fis8 -. \stemUp g8 -.
    \stemUp b8 -. \stemUp g8 -. \stemUp fis8 -. \stemUp a8 -. \stemUp
    fis8 -. \stemUp b,8 -. \stemUp d8 -. \stemUp b8 -. | \barNumberCheck
    #30
    \stemUp c8 -. \stemUp dis8 -. \stemUp c8 -. \stemUp cis8 -. \stemUp
    fis8 -. \stemUp cis8 -. \stemUp dis8 -. \stemUp fis8 -. \stemUp dis8
    -. \stemUp e8 -. \stemUp g8 -. \stemUp e8 -. | % 31
    \stemUp fis8 -. _\! _\f \stemUp a8 -. \stemUp d8 -. \stemDown es8 -.
    r8*2/3 r8*2/3 r2.*2/3 s1*1/3 \pageBreak | % 32
    \stemUp fis,8 -. _\f \stemUp a8 -. \stemUp d8 -. \stemDown es8 -. r8*2/3
    r8*2/3 r2.*2/3 s1*1/3 | % 33
    \stemUp fis,8 -. _\mf \stemUp a8 -. \stemUp d8 -. \stemDown es8 -. r8*2/3
    r8*2/3 r2.*2/3 s1*1/3 | % 34
    \stemUp fis,8 -. _\mp \stemUp a8 -. \stemUp d8 -. \stemDown es8 -. r8*2/3
    r8*2/3 r2.*2/3 s1*1/3 | % 35
    \stemUp fis,8 -. _\p \stemUp a8 -. \stemUp d8 -. r4.*2/3 \stemUp
    fis,8 -. \stemUp a8 -. \stemUp d8 -. r4.*2/3 s4 \pageBreak | % 36
    \stemUp fis,8 -. \stemUp a8 -. \stemUp d8 -. r4.*2/3 \stemUp fis,8
    \stemUp a8 \stemUp d8 r4.*2/3 s4 | % 37
    \stemUp d,8 -. _\p \stemUp fis8 -. \stemUp d8 -. \stemUp fis8 -.
    \stemUp eis8 -. \stemUp fis8 -. \stemUp e8 -. \stemUp fis8 -.
    \stemUp e8 -. \stemUp g8 -. \stemUp fis8 -. \stemUp g8 -. | % 38
    \stemUp e8 -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp g8
    -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp b8 -.
    \stemDown a8 -. \stemDown b8 -. \stemDown c8 -. | % 39
    r1 s2 | \barNumberCheck #40
    r2.*2/3 \stemUp b8 ( ^> _\p \stemUp g8 \stemUp e8 \stemUp g8 \stemUp
    d8 \stemUp b8 ) s4 \pageBreak | % 41
    \stemUp d8 \stemUp e8 -. \stemUp d8 -. \stemUp fis8 -. \stemUp eis8
    -. \stemUp fis8 -. \stemUp e8 -. \stemUp fis8 -. \stemUp e8 -.
    \stemUp g8 -. \stemUp fis8 -. \stemUp g8 -. | % 42
    \stemUp e8 -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp g8
    -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp b8 -.
    \stemDown a8 -. \stemDown b8 -. \stemDown c8 -. | % 43
    r1 s2 | % 44
    r2.*2/3 \stemUp b8 ( -> _\p \stemUp g8 \stemUp e8 \stemUp g8 \stemUp
    d8 \stemUp b8 ) s4 | % 45
    r1 s2 \pageBreak | % 46
    \stemUp es4. _\f -\markup{ \italic {marcato} } \stemUp d4. \stemUp c4.
    \stemUp bes4 ( ~ \stemUp bes16 \stemUp as16 | % 47
    \stemUp g8 ) r8*2/3 r8*2/3 r4.*2/3 \stemUp g'8 ( \stemUp as8 \stemUp
    bes8 ) \stemDown c8 ( \stemDown bes8 \stemDown as8 s1*5/24 | % 48
    \stemUp g8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 49
    \stemUp b,8 -. _\ff \stemUp cis8 -. \stemUp b8 -. \stemUp cis8 -.
    \stemUp dis8 -. \stemUp cis8 -. \stemUp dis8 -. \stemUp fis8 -.
    \stemUp dis8 -. \stemUp fis8 -. \stemUp gis8 -. \stemUp fis8 -. |
    \barNumberCheck #50
    \stemDown b8 -. \stemDown cis8 -. \stemDown b8 -. \stemUp fis8 -.
    \stemUp b8 -. \stemUp fis8 -. \stemDown b8 -. \stemDown cis8 -.
    \stemDown b8 -. \stemDown cis8 -. \stemDown e8 -. \stemDown cis8 -.
    \pageBreak | % 51
    r1 s2 | % 52
    r1 s2 | % 53
    r1 s2 | % 54
    r1 s2 | % 55
    r1 s2 \pageBreak | % 56
    r1 s2 | % 57
    r1 s2 | % 58
    r1 s2 | % 59
    r1 s2 | \barNumberCheck #60
    r1 s2 \pageBreak | % 61
    r1 s2 | % 62
    r1 s2 | % 63
    r1 s2 | % 64
    r1 s2 | % 65
    r1 s2 \pageBreak | % 66
    r1 s2 | % 67
    r1 s2 | % 68
    r1 s2 | % 69
    r1 s2 | \barNumberCheck #70
    r1 \bar "||"
    s2 \pageBreak | % 71
    \key e \major r1 s2 | % 72
    r1 s2 | % 73
    r1 s2 | % 74
    r1 s2 | % 75
    r1 s2 \break | % 76
    r1 s2 | % 77
    r1 s2 | % 78
    r1 s2 | % 79
    r1 s2 | \barNumberCheck #80
    r1 s2 \pageBreak | % 81
    r1 s2 | % 82
    r1 s2 | % 83
    r1 s2 | % 84
    r1 s2 | % 85
    r1 s2 \pageBreak | % 86
    r1 s2 | % 87
    r1 s2 | % 88
    r1 s2 | % 89
    r1 s2 \pageBreak | \barNumberCheck #90
    r1 s2 | % 91
    r1 s2 | % 92
    r1 s2 | % 93
    r1 s2 | % 94
    r1 s2 | % 95
    r1 s2 \pageBreak | % 96
    r1 s2 | % 97
    r1 s2 | % 98
    r1 s2 | % 99
    r1 s2 | \barNumberCheck #100
    r1 s2 | % 101
    r1 s2 \break | % 102
    r1 s2 | % 103
    r1 s2 | % 104
    r1 s2 | % 105
    r1 s2 | % 106
    r1 s2 \pageBreak | % 107
    r1 s2 | % 108
    r1 s2 | % 109
    r1 s2 | \barNumberCheck #110
    r1 s2 | % 111
    r1 s2 | % 112
    r1 s2 \break | % 113
    r1 s2 | % 114
    r1 s2 | % 115
    r1 s2 | % 116
    r1 s2 | % 117
    r1 s2 \pageBreak | % 118
    r1 s2 | % 119
    r1 r2*2/3 s1*1/6 | \barNumberCheck #120
    r1 r2*2/3 s1*1/6 | % 121
    r1 r2*2/3 s1*1/6 | % 122
    r1 r2*2/3 s1*1/6 \break | % 123
    r1 r2*2/3 s1*1/6 | % 124
    r1 r2*2/3 s1*1/6 | % 125
    r1 r2*2/3 s1*1/6 | % 126
    r1 r2*2/3 s1*1/6 | % 127
    r1 r2*2/3 s1*1/6 \pageBreak | % 128
    r1 r2*2/3 s1*1/6 | % 129
    r1 r2*2/3 s1*1/6 | \barNumberCheck #130
    r1 r2*2/3 s1*1/6 | % 131
    r1 r2*2/3 s1*1/6 \pageBreak | % 132
    r1 s2 | % 133
    r1 s2 | % 134
    r1 s2 | % 135
    r1 s2 \pageBreak | % 136
    \time 4/4 \omit Staff.TimeSignature \stemDown c8 :16 ^ "div."
    \stemDown d8 :16 \stemDown e8 :16 \stemDown fis8 :16 \stemDown g8
    :16 r8 r4 | % 137
    \time 12/8  \stemUp c,,8 ( \stemUp b8 ) \stemUp a8 -. \stemUp g8 -.
    r8*2/3 r8*2/3 r4.*2/3 r8*2/3 \stemUp g8 -. _\mf \stemUp b8 -. s4 | % 138
    \stemUp c8 ( \stemUp b8 ) \stemUp a8 -. \stemUp g8 -. r8*2/3 r8*2/3
    r2.*2/3 \bar "||"
    s1*1/3 | % 139
    \key g \major r4.*2/3 r8*2/3 \stemUp d''8 ( _\p \stemUp d,8 ) r4.*2/3
    r8*2/3 \stemUp e'8 ( \stemUp e,8 ) s1*1/3 \pageBreak |
    \barNumberCheck #140
    r4.*2/3 \stemUp <d d'>8 ^ "pizz." r8*2/3 r8*2/3 r4.*2/3 \stemUp a'4
    ( ^ "arco" \stemUp d,8 ) s1*1/3 | % 141
    r1 s2 | % 142
    \stemUp ais'8 ( -> _\p \stemUp b8 \stemUp a8 \stemUp g8 \stemUp es8
    \stemUp d8 ) r2.*2/3 s4 | % 143
    r4.*2/3 r8*2/3 \stemUp d'8 ( _\p \stemUp d,8 ) r4.*2/3 r8*2/3
    \stemUp e'8 ( \stemUp e,8 ) s1*1/3 | % 144
    r4.*2/3 \stemUp <d d'>8 ^ "pizz." r8*2/3 r8*2/3 r4.*2/3 \stemUp a'4
    ( ^ "arco" \stemUp d,8 ) s1*1/3 \pageBreak | % 145
    r1 s2 | % 146
    \stemUp fis8 ( ^> _\p \stemUp g8 \stemUp fis8 \stemUp e8 \stemUp d8
    \stemUp c8 ) r2.*2/3 s4 | % 147
    r1 s2 | % 148
    \numericTimeSignature\time 4/4  r2 \stemDown fis'8 _\mp ^ "pizz."
    \stemDown c8 r4 | % 149
    \time 12/8  r4.*2/3 \stemUp dis,8 -. _\mp ^ "arco" \stemUp cisis8 -.
    \stemUp dis8 -. r4.*2/3 \stemUp e8 -. \stemUp dis8 -. \stemUp e8 -.
    s4 \pageBreak | \barNumberCheck #150
    \stemUp g8 -. _\markup{ \small\italic {poco cresc.} }
    \startTrillSpan \stemUp fis8 -. \stemUp e8 -. \stemUp a8 -. \stemUp
    g8 -. \stemUp fis8 -. \stemUp b8 -. \stemUp a8 -. \stemUp g8 -.
    \stemDown c8 -. \stemDown b8 -. \stemDown a8 -. | % 151
    \stemDown d8 -. \stopTrillSpan _\mf _\markup{ \small\italic {dim.} }
    \startTrillSpan \stemDown b8 -. \stemDown c8 -. \stemUp a8 -.
    \stemUp b8 -. \stemUp g8 -. \stemUp a8 -. \stemUp fis8 -. \stemUp g8
    -. \stemUp e8 -. \stemUp fis8 -. \stemUp d8 -. | % 152
    r1 s2 \stopTrillSpan | % 153
    \stemDown d'8 -. _\p \stemDown b8 -. \stemDown c8 -. \stemUp a8 -.
    \stemUp b8 -. \stemUp g8 -. \stemUp a8 -. _\markup{ \small\italic
        {dim.} } \startTrillSpan \stemUp fis8 -. \stemUp g8 -. \stemUp e8
    -. \stemUp fis8 -. \stemUp d8 -. | % 154
    \stemUp e8 -. \stemUp c8 -. \stemUp d8 -. \stemUp b8 -. \stemUp c8
    -. \stemUp a8 -. \stemUp b8 -. \stopTrillSpan _\pp \stemUp g8 -.
    \stemUp a8 -. r4.*2/3 s8 \pageBreak | % 155
    r1 s2 | % 156
    r4.*2/3 \stemUp c8 _\mp ^ "pizz." r8*2/3 r8*2/3 \stemUp c8 r8*2/3 r8*2/3
    r4.*2/3 s1*5/12 | % 157
    r1 s2 | % 158
    r1 s2 \break | % 159
    \stemUp d8 -. _\p ^ "arco" \stemUp fis8 -. \stemUp d8 -. \stemUp e8
    -. \stemUp g8 -. \stemUp e8 -. \stemUp fis8 -. \stemUp b8 -. \stemUp
    fis8 -. \stemUp g8 -. \stemUp b8 -. \stemUp g8 -. | \barNumberCheck
    #160
    \stemUp gis8 -. \stemUp b8 -. \stemUp gis8 -. \stemDown ais8 -.
    \stemDown cis8 -. \stemDown ais8 -. \stemDown b8 -. \stemDown d8 -.
    \stemDown b8 -. \stemDown cis8 -. \stemDown e8 -. \stemDown cis8 -.
    | % 161
    \stemDown d8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 162
    r1 s2 \pageBreak | % 163
    \stemUp d,8 -. _\p \stemUp fis8 -. \stemUp d8 -. \stemUp e8 -.
    \stemUp g8 -. \stemUp e8 -. \stemUp fis8 -. \stemUp b8 -. \stemUp
    fis8 -. \stemUp g8 -. \stemUp b8 -. \stemUp g8 -. | % 164
    \stemUp gis8 -. \stemUp b8 -. \stemUp gis8 -. \stemDown ais8 -.
    \stemDown cis8 -. \stemDown ais8 -. \stemDown b8 -. \stemDown d8 -.
    \stemDown b8 -. \stemDown cis8 -. \stemDown g'8 -. \stemDown cis,8
    -. | % 165
    \stemDown fis8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 166
    r2.*2/3 r4.*2/3 \stemUp g,4. ( _\mp s4. \pageBreak | % 167
    \stemUp fis8 ) _\< \stemUp a8 -. \stemUp fis8 -. \stemUp g8 -.
    \stemUp b8 -. \stemUp g8 -. \stemUp fis8 -. \stemUp g8 -. \stemUp
    fis8 -. \stemUp b,8 -. \stemUp d8 -. \stemUp b8 -. | % 168
    \stemUp c8 -. \stemUp dis8 -. \stemUp c8 -. \stemUp cis8 -. \stemUp
    fis8 -. \stemUp cis8 -. \stemUp dis8 -. \stemUp fis8 -. \stemUp dis8
    -. \stemUp e8 -. \stemUp g8 -. \stemUp e8 -. | % 169
    \stemUp fis8 -. _\! _\f \stemUp a8 -. \stemUp d8 -. \stemDown es8 -.
    r8*2/3 r8*2/3 r2.*2/3 s1*1/3 | \barNumberCheck #170
    \stemUp fis,8 -. _\f \stemUp a8 -. \stemUp d8 -. \stemDown es8 -. r8*2/3
    r8*2/3 r2.*2/3 s1*1/3 \pageBreak | % 171
    \stemUp fis,8 -. _\mf \stemUp a8 -. \stemUp d8 -. \stemDown es8 -. r8*2/3
    r8*2/3 r2.*2/3 s1*1/3 | % 172
    \stemUp fis,8 -. _\mp \stemUp a8 -. \stemUp d8 -. \stemDown es8 -. r8*2/3
    r8*2/3 r2.*2/3 s1*1/3 | % 173
    \stemUp fis,8 -. _\p \stemUp a8 -. \stemUp d8 -. r4.*2/3 \stemUp
    fis,8 -. \stemUp a8 -. \stemUp d8 -. r4.*2/3 s4 | % 174
    \stemUp fis,8 -. \stemUp a8 -. \stemUp d8 -. r4.*2/3 \stemUp fis,8
    -. \stemUp a8 -. \stemUp d8 -. r4.*2/3 s4 \pageBreak | % 175
    \stemUp d,8 -. _\p \stemUp e8 -. \stemUp d8 -. \stemUp fis8 -.
    \stemUp eis8 -. \stemUp fis8 -. \stemUp e8 -. \stemUp fis8 -.
    \stemUp e8 -. \stemUp g8 -. \stemUp fis8 -. \stemUp g8 -. | % 176
    \stemUp e8 -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp g8
    -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp b8 -.
    \stemDown a8 -. \stemDown b8 -. \stemDown c8 -. | % 177
    r1 s2 | % 178
    r2.*2/3 \stemUp b8 ( ^> _\p \stemUp g8 \stemUp e8 \stemUp g8 \stemUp
    d8 \stemUp b8 ) s4 | % 179
    \stemUp d8 -. _\p \stemUp e8 -. \stemUp d8 -. \stemUp fis8 -.
    \stemUp eis8 -. \stemUp fis8 -. \stemUp e8 -. \stemUp fis8 -.
    \stemUp e8 -. \stemUp g8 -. \stemUp fis8 -. \stemUp g8 -. \pageBreak
    | \barNumberCheck #180
    \stemUp e8 -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp g8
    -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp b8 -.
    \stemDown a8 -. \stemDown b8 -. \stemDown c8 -. | % 181
    r1 s2 | % 182
    r2.*2/3 \stemUp b8 ( -> _\p \stemUp g8 \stemUp e8 \stemUp g8 \stemUp
    d8 \stemUp b8 ) s4 | % 183
    r1 s2 \pageBreak | % 184
    \stemUp es4. _\f _\ marcato \stemUp d4. \stemUp c4. \stemUp bes4 ( ~
    \stemUp bes16 \stemUp as16 ) | % 185
    \stemUp g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 186
    r1 s2 | % 187
    r1 s2 | % 188
    \stemUp g'4. \stemUp f4. \stemUp es4. \stemUp d4 ( ~ \stemUp d16
    \stemUp c16 ) \pageBreak | % 189
    \stemUp bes8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 |
    \barNumberCheck #190
    r1 s2 | % 191
    r2.*2/3 \stemDown d'8 -. _\ff \stemDown g8 -. \stemDown d8 -.
    \stemDown fis8 -. \stemDown g8 -. \stemDown fis8 -. s4 | % 192
    r2.*2/3 \stemDown d8 -. \stemDown g8 -. \stemDown d8 -. \stemDown d8
    -. \stemDown g8 -. \stemDown d8 -. s4 | % 193
    \stemDown g8 _\ff \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown
    cis8 \stemDown b8 \stemUp a8 \stemUp g8 \stemUp fis8 \stemUp e8
    \stemUp d8 \stemUp cis8 \pageBreak | % 194
    \numericTimeSignature\time 4/4  R1*7 \pageBreak | % 201
    R1*5 \pageBreak | % 206
    R1*5 \pageBreak | % 211
    R1*5 \pageBreak | % 216
    R1*5 \pageBreak | % 221
    R1*4 \pageBreak | % 225
    R1*3 \pageBreak | % 228
    R1*5 \pageBreak | % 233
    R1*5 \pageBreak | % 238
    R1*5 \pageBreak | % 243
    R1*5 \pageBreak | % 248
    R1*6 \pageBreak | % 254
    R1*5 \pageBreak | % 259
    R1*5 \pageBreak | % 264
    R1*5 \pageBreak | % 269
    R1*5 \pageBreak | % 274
    R1*7 \pageBreak | % 281
    R1*6 \pageBreak | % 287
    R1*5 \pageBreak | % 292
    R1*5 \pageBreak | % 297
    R1*5 \pageBreak | % 302
    R1*6 \pageBreak | % 308
    R1*6 \pageBreak | % 314
    R1*6 \pageBreak | \barNumberCheck #320
    R1*5 \pageBreak | % 325
    R1*3 \pageBreak | % 328
    R1*4 \pageBreak | % 332
    R1*4 \pageBreak | % 336
    R1*5 \pageBreak | % 341
    R1*7 \bar "|."
    }

PartPTwoOneVoiceOne =  \relative d' {
    \clef "alto" \time 12/8 \key g \major | % 1
    r4.*2/3 \stemDown d8 -. _\p \stemDown d'8 -. \stemDown d,8 -. r4.*2/3
    \stemDown e8 -. \stemDown e'8 -. \stemDown e,8 -. s4 | % 2
    r4.*2/3 \stemDown d'8 -. r8*2/3 r8*2/3 \stemDown b4 ( \stemDown e,8
    ) \stemDown a4 ( \stemDown d,8 ) s1*5/24 | % 3
    r1 s2 | % 4
    \stemDown g2. -> _\p r2.*2/3 s4 \pageBreak | % 5
    r4.*2/3 _ "Vla." _ "(div.)" \stemDown d8 -. _\p \stemDown d'8 -.
    \stemDown d,8 -. r4.*2/3 \stemDown e8 -. \stemDown e'8 -. \stemDown
    e,8 -. s4 | % 6
    r4.*2/3 \stemDown d'8 -. r8*2/3 r8*2/3 \stemDown b4 ( \stemDown e,8
    ) \stemDown a4 ( \stemDown d,8 ) s1*5/24 | % 7
    r1 \bar "||"
    s2 | % 8
    \stemDown e2. -> _\p r2.*2/3 s4 | % 9
    r1 s2 \pageBreak | \barNumberCheck #10
    \numericTimeSignature\time 4/4  r2 _ "Vla." _ "(div.)" r4 \stemDown
    g8 _\mp ^ "pizz." \stemDown dis8 | % 11
    R1 | % 12
    r4 \stemDown e'8 _\mf \stemDown b8 r2 | % 13
    R1 | % 14
    \time 12/8  \stemDown g8 -. _\mp ^ "arco" _\> \stemDown a8 -.
    \stemDown fis8 -. \stemDown g8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown d8 -. \stemDown e8 -. \stemDown c8 -. \stemDown d8 -. _\!
    _\p \stemDown e8 -. \stemDown d8 -. \break | % 15
    \stemDown fis8 -. _ "Vla." _ "(div.)" \stemDown g8 -. \stemDown e8
    -. \stemDown fis8 -. \stemDown d8 -. \stemDown e8 -. \stemDown c8 -.
    _\markup{ \small\italic {dim.} } \startTrillSpan \stemDown d8 -.
    \stemDown b8 -. \stemUp c8 -. \stemUp a8 -. \stemUp b8 -. | % 16
    \stemUp g8 -. \stemUp a8 -. \stemUp fis8 -. \stemUp g8 -. \stemUp e8
    -. \stemUp fis8 -. \stemUp d8 -. \stemUp e8 -. \stemUp c8 -. \stemUp
    d8 -. \stopTrillSpan _\pp r8*2/3 r8*2/3 s1*1/12 | % 17
    \stemDown d'8 -. _\< \stemDown e8 -. \stemDown d8 -. \stemDown d8 -.
    \stemDown e8 -. \stemDown d8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. \stemDown d8 -. _\! _\mf \stemDown e8 -. \stemDown d8
    -. | % 18
    \stemDown d8 -. _\> \stemDown e8 -. \stemDown d8 -. \stemDown d8 -.
    \stemDown e8 -. \stemDown d8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. | % 19
    \stemDown d8 -. _\! _\p \stemDown e8 -. \stemDown d8 -. \stemDown e8
    -. \stemDown fis8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. \stemDown cis8 -. \stemDown d8 -. \stemDown cis8 -.
    \pageBreak | \barNumberCheck #20
    \stemDown d8 -. _ "Vla." _ "(div.)" \stemDown e8 -. \stemDown d8 -.
    \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown f8 -.
    \stemDown g8 -. \stemDown f8 -. \stemDown g8 -. \stemDown a8 -.
    \stemDown g8 -. | % 21
    \stemDown fis8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 22
    r1 s2 | % 23
    \stemDown d8 -. _\p \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. \stemDown cis8 -. \stemDown d8 -. \stemDown cis8 -.
    \break | % 24
    \stemDown d8 -. _ "Vla." _ "(div.)" \stemDown e8 -. \stemDown d8 -.
    \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown f8 -.
    \stemDown g8 -. \stemDown f8 -. \stemDown g8 -. \stemDown a8 -.
    \stemDown g8 -. | % 25
    \stemDown fis8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 26
    r1 s2 | % 27
    \stemDown fis8 _\p \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -.
    _\markup{ \small\italic {poco cresc.} } \startTrillSpan \stemDown a8
    -. \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -. \pageBreak | % 28
    \stemDown fis8 -. _ "Vla." _ "(div.)" \stemDown g8 -. \stemDown fis8
    -. \stemDown g8 -. \stemDown a8 -. \stemDown g8 -. \stemDown a8 -.
    _\< \stemDown b8 -. \stemDown a8 -. \stemDown a8 -. \stemDown b8 -.
    \stemDown a8 -. | % 29
    \stemDown a8 -. \stopTrillSpan _\! _\mp r8*2/3 r4*2/3 r1*2/3
    s1*11/24 | \barNumberCheck #30
    r1 s2 | % 31
    r2.*2/3 \stemDown e8 -. _\f \stemDown fis8 -. \stemDown gis8 -.
    \stemDown bes8 -. r8*2/3 r8*2/3 s1*1/3 \pageBreak | % 32
    r2.*2/3 _ "Vla." _ "(div.)" \stemDown e,8 -. _\f \stemDown fis8 -.
    \stemDown gis8 -. \stemDown bes8 -. r8*2/3 r8*2/3 s1*1/3 | % 33
    \stemDown d,8 -. _\mf \stemDown e8 -. \stemDown fis8 -. \stemDown g8
    -. r8*2/3 r8*2/3 r2.*2/3 s1*1/3 | % 34
    \stemDown d8 -. _\mp \stemDown e8 -. \stemDown fis8 -. \stemDown g8
    -. r8*2/3 r8*2/3 r2.*2/3 s1*1/3 | % 35
    \stemDown d8 -. _\p \stemDown e8 -. \stemDown fis8 -. r4.*2/3
    \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -. r4.*2/3 s4
    \pageBreak | % 36
    \stemDown d8 -. _ "Vla." _ "(div.)" \stemDown e8 -. \stemDown fis8
    -. r4.*2/3 \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -. r4.*2/3
    s4 | % 37
    \stemUp b,8 -. _\p \stemUp g8 -. \stemUp b8 -. \stemUp a8 -. \stemUp
    gis8 -. \stemUp a8 -. \stemUp c8 -. \stemUp a8 -. \stemUp c8 -.
    \stemUp b8 -. \stemUp ais8 -. \stemUp b8 -. | % 38
    \stemDown c8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown e8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown a8 -. | % 39
    r1 s2 | \barNumberCheck #40
    r2.*2/3 r4.*2/3 \stemDown d,8 _\p r8*2/3 r8*2/3 s1*11/24 \pageBreak
    | % 41
    \numericTimeSignature\time 4/4  \stemDown g'8 _\mf _ "Vla." _
    "(div.)" ^ "pizz." r8 \stemDown d8 r8 \stemDown a8 r8 \stemDown e8 r8
    | % 42
    \stemDown a8 r8 \stemDown d8 r8 \stemDown b8 r8 \stemDown d,8 _\<
    \stemDown e8 | % 43
    \stemDown fis8 \stemDown g8 \stemDown a8 \stemDown b8 \stemDown c8
    _\! r8 \stemDown b8 \stemDown a8 | % 44
    \stemDown <d, d'>8 _\> r8 \stemDown g8 r8 \stemDown g8 r8 _\! r4 | % 45
    R1 \pageBreak | % 46
    \time 12/8  \stemDown es8 -. _\f _ "Vla." _ "(div.)" ^ "arco"
    \stemDown f8 -. \stemDown es8 -. \stemDown f8 -. \stemDown g8 -.
    \stemDown f8 -. \stemDown g8 -. \stemDown bes8 -. \stemDown g8 -.
    \stemDown bes8 -. \stemDown c8 -. \stemDown bes8 -. | % 47
    \stemDown es8 -. r8*2/3 r8*2/3 r4.*2/3 \stemUp g,,8 ( \stemUp as8
    \stemUp bes8 ) \stemUp c8 ( \stemUp bes8 \stemUp as8 s1*5/24 | % 48
    \stemUp g8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 49
    \stemUp dis8 -. _\ff \stemUp fis8 -. \stemUp dis8 -. \stemUp fis8 -.
    \stemUp b8 -. \stemUp fis8 -. \stemUp b8 -. \stemUp cis8 -. \stemUp
    b8 -. \stemDown cis8 -. \stemDown e8 -. \stemDown cis8 -. |
    \barNumberCheck #50
    \stemDown dis8 -. \stemDown fis8 -. \stemDown dis8 -. \stemDown cis8
    -. \stemDown dis8 -. \stemDown cis8 -. \stemDown dis8 -. \stemDown
    fis8 -. \stemDown dis8 -. \stemDown fis8 -. \stemDown ais8 -.
    \stemDown fis8 -. \pageBreak | % 51
    r1 s2 | % 52
    r1 s2 | % 53
    r1 s2 | % 54
    r1 s2 | % 55
    r1 s2 \pageBreak | % 56
    r1 s2 | % 57
    r1 s2 | % 58
    r1 s2 | % 59
    r1 s2 | \barNumberCheck #60
    r1 s2 \pageBreak | % 61
    r1 s2 | % 62
    r1 s2 | % 63
    r1 s2 | % 64
    r1 s2 | % 65
    r1 s2 \pageBreak | % 66
    r1 s2 | % 67
    r1 s2 | % 68
    r1 s2 | % 69
    r1 s2 | \barNumberCheck #70
    r1 \bar "||"
    s2 \pageBreak | % 71
    \key e \major r1 s2 | % 72
    r1 s2 | % 73
    r1 s2 | % 74
    r1 s2 | % 75
    r1 s2 \break | % 76
    r1 s2 | % 77
    r1 s2 | % 78
    r1 s2 | % 79
    r1 s2 | \barNumberCheck #80
    r1 s2 \pageBreak | % 81
    r1 s2 | % 82
    r1 s2 | % 83
    r1 s2 | % 84
    r1 s2 | % 85
    r1 s2 \pageBreak | % 86
    r1 s2 | % 87
    r1 s2 | % 88
    r1 s2 | % 89
    r1 s2 \pageBreak | \barNumberCheck #90
    r1 s2 | % 91
    r1 s2 | % 92
    r1 s2 | % 93
    r1 s2 | % 94
    r1 s2 | % 95
    r1 s2 \pageBreak | % 96
    r1 s2 | % 97
    r1 s2 | % 98
    r1 s2 | % 99
    r1 s2 | \barNumberCheck #100
    r1 s2 | % 101
    r1 s2 \break | % 102
    r1 s2 | % 103
    r1 s2 | % 104
    r1 s2 | % 105
    r1 s2 | % 106
    r1 s2 \pageBreak | % 107
    r1 s2 | % 108
    r1 s2 | % 109
    r1 s2 | \barNumberCheck #110
    r1 s2 | % 111
    r1 s2 | % 112
    r1 s2 \break | % 113
    r1 s2 | % 114
    r1 s2 | % 115
    r1 s2 | % 116
    r1 s2 | % 117
    r1 s2 \pageBreak | % 118
    r1 s2 | % 119
    r1 r2*2/3 s1*1/6 | \barNumberCheck #120
    r1 r2*2/3 s1*1/6 | % 121
    r1 r2*2/3 s1*1/6 | % 122
    r1 r2*2/3 s1*1/6 \break | % 123
    r1 r2*2/3 s1*1/6 | % 124
    r1 r2*2/3 s1*1/6 | % 125
    r1 r2*2/3 s1*1/6 | % 126
    r1 r2*2/3 s1*1/6 | % 127
    r1 r2*2/3 s1*1/6 \pageBreak | % 128
    r1 r2*2/3 s1*1/6 | % 129
    r1 r2*2/3 s1*1/6 | \barNumberCheck #130
    r1 r2*2/3 s1*1/6 | % 131
    r1 r2*2/3 s1*1/6 \pageBreak | % 132
    r1 s2 | % 133
    r1 s2 | % 134
    r1 s2 | % 135
    r1 s2 \pageBreak | % 136
    \time 4/4 \omit Staff.TimeSignature \stemDown <g, g'>8 _ "Vla." _
    "(div.)" r8 r4 \stemDown d''16 \stemDown c16 \stemDown b16 \stemDown
    a16 \stemDown g16 \stemDown f16 \stemDown e16 \stemDown d16 | % 137
    \time 12/8  \stemDown <g, g'>8 _\f r8*2/3 r8*2/3 \stemUp <d b' d>8 r8*2/3
    r8*2/3 r2.*2/3 s1*5/12 | % 138
    \stemDown <g g'>8 _\mf r8*2/3 r8*2/3 \stemUp <d b' d>8 r8*2/3 r8*2/3
    r4.*2/3 r8*2/3 \stemUp g8 -. _\p \stemUp a8 -. \bar "||"
    s1*1/3 | % 139
    \key g \major \stemUp b8 -. \stemUp g8 -. \stemUp b8 -. \stemUp a8
    -. \stemUp gis8 -. \stemUp a8 -. \stemUp c8 -. \stemUp a8 -. \stemUp
    c8 -. \stemUp b8 -. \stemUp ais8 -. \stemUp b8 -. \pageBreak |
    \barNumberCheck #140
    \stemDown c8 -. _ "Vla." _ "(div.)" \stemDown d8 -. \stemDown e8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown fis8 -. \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -.
    \stemDown a8 -. | % 141
    r1 s2 | % 142
    \stemDown g2. -> _\p r2.*2/3 s4 | % 143
    \stemUp b,8 -. _\p \stemUp g8 -. \stemUp b8 -. \stemUp a8 -. \stemUp
    gis8 -. \stemUp a8 -. \stemUp c8 -. \stemUp a8 -. \stemUp c8 -.
    \stemUp b8 -. \stemUp ais8 -. \stemUp b8 -. | % 144
    \stemDown c8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown e8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown a8 -.
    \pageBreak | % 145
    r1 _ "Vla." _ "(div.)" s2 | % 146
    \stemDown e2. ^> _\p r2.*2/3 s4 | % 147
    r1 s2 | % 148
    \numericTimeSignature\time 4/4  r2 r4 \stemDown g8 _\mp ^ "pizz."
    \stemDown dis8 | % 149
    R1 \pageBreak | \barNumberCheck #150
    r4 \stemDown e'8 _\mf _ "Vla." _ "(div.)" \stemDown b8 r2 | % 151
    R1 | % 152
    \time 12/8  \stemDown g8 -. _\mp ^ "arco" _\> \stemDown a8 -.
    \stemDown fis8 -. \stemDown g8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown d8 -. \stemDown e8 -. \stemDown c8 -. \stemDown d8 -. _\!
    _\p \stemDown e8 -. \stemDown d8 -. | % 153
    \stemDown fis8 -. \stemDown g8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown d8 -. \stemDown e8 -. \stemDown c8 -. _\markup{
        \small\italic {dim.} } \startTrillSpan \stemDown d8 -. \stemDown
    b8 -. \stemUp c8 -. \stemUp a8 -. \stemUp b8 -. | % 154
    \stemUp g8 -. \stemUp a8 -. \stemUp fis8 -. \stemUp g8 -. \stemUp e8
    -. \stemUp fis8 -. \stemUp d8 -. \stemUp e8 -. \stemUp c8 -. \stemUp
    d8 -. \stopTrillSpan _\pp r4*2/3 s1*1/12 \pageBreak | % 155
    \stemDown d'8 -. _ "Vla." _ "(div.)" _\< \stemDown e8 -. \stemDown d8
    -. \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. \stemDown d8 -.
    \stemDown e8 -. \stemDown d8 -. \stemDown d8 -. _\! _\mf \stemDown e8
    -. \stemDown d8 -. | % 156
    \stemDown d8 -. _\> \stemDown e8 -. \stemDown d8 -. \stemDown d8 -.
    \stemDown e8 -. \stemDown d8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. | % 157
    \stemDown d8 -. _\! _\p \stemDown e8 -. \stemDown d8 -. \stemDown e8
    -. \stemDown fis8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. \stemDown cis8 -. \stemDown d8 -. \stemDown cis8 -.
    | % 158
    \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown f8 -. \stemDown g8 -.
    \stemDown f8 -. \stemDown g8 -. \stemDown a8 -. \stemDown g8 -.
    \break | % 159
    \stemDown fis8 -. _ "Vla." _ "(div.)" r8*2/3 r8*2/3 r4.*2/3 r2.*2/3
    s1*11/24 | \barNumberCheck #160
    r1 s2 | % 161
    \stemDown d8 -. _\p \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown d8 -. \stemDown cis8 -. \stemDown d8 -. \stemDown cis8 -.
    | % 162
    \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown f8 -. \stemDown g8 -.
    \stemDown f8 -. \stemDown g8 -. \stemDown a8 -. \stemDown g8 -.
    \pageBreak | % 163
    \stemDown fis8 -. _ "Vla." _ "(div.)" r8*2/3 r8*2/3 r4.*2/3 r2.*2/3
    s1*11/24 | % 164
    r1 s2 | % 165
    \stemDown fis8 -. _\p _\markup{ \small\italic {poco cresc.} }
    \startTrillSpan \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -.
    \stemDown a8 -. \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -.
    | % 166
    \stemDown fis8 -. \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -.
    \stemDown a8 -. \stemDown g8 -. \stemDown a8 -. _\< \stemDown b8 -.
    \stemDown a8 -. \stemDown b8 -. \stemDown c8 -. \stemDown b8 -.
    \pageBreak | % 167
    \stemDown a8 -. \stopTrillSpan _\! _\mp _ "Vla." _ "(div.)" r8*2/3 r8*2/3
    r4.*2/3 r2.*2/3 s1*11/24 | % 168
    r1 s2 | % 169
    r2.*2/3 \stemDown e8 -. _\f \stemDown fis8 -. \stemDown gis8 -.
    \stemDown bes8 -. r8*2/3 r8*2/3 s1*1/3 | \barNumberCheck #170
    r2.*2/3 \stemDown e,8 -. _\f \stemDown fis8 -. \stemDown gis8 -.
    \stemDown bes8 -. r8*2/3 r8*2/3 s1*1/3 \pageBreak | % 171
    \stemDown d,8 -. _\mf _ "Vla." _ "(div.)" \stemDown e8 -. \stemDown
    fis8 -. \stemDown g8 -. r8*2/3 r8*2/3 r2.*2/3 s1*1/3 | % 172
    \stemDown d8 -. _\mp \stemDown e8 -. \stemDown fis8 -. \stemDown g8
    -. r8*2/3 r8*2/3 r2.*2/3 s1*1/3 | % 173
    \stemDown d8 -. _\p \stemDown e8 -. \stemDown fis8 -. r4.*2/3
    \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -. r4.*2/3 s4 | % 174
    \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -. r4.*2/3 \stemDown
    d8 -. \stemDown e8 -. \stemDown fis8 -. r4.*2/3 s4 \pageBreak | % 175
    \stemUp b,8 -. _\p _ "Vla." _ "(div.)" \stemUp g8 -. \stemUp b8 -.
    \stemUp a8 -. \stemUp gis8 -. \stemUp a8 -. \stemUp c8 -. \stemUp a8
    -. \stemUp c8 -. \stemUp b8 -. \stemUp ais8 -. \stemUp b8 -. | % 176
    \stemDown c8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown e8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown a8 -. | % 177
    r1 s2 | % 178
    r2.*2/3 r4.*2/3 \stemDown d,8 _\p r8*2/3 r8*2/3 s1*11/24 | % 179
    \numericTimeSignature\time 4/4  \stemDown g'8 _\mf ^ "pizz." r8
    \stemDown d8 r8 \stemDown a8 r8 \stemDown e8 r8 \pageBreak |
    \barNumberCheck #180
    \stemDown a8 _ "Vla." _ "(div.)" r8 \stemDown d8 r8 \stemDown b8 r8
    \stemDown d,8 _\< \stemDown e8 | % 181
    \stemDown fis8 \stemDown g8 \stemDown a8 \stemDown b8 \stemDown c8
    _\! r8 \stemDown b8 \stemDown a8 | % 182
    \stemDown <d, d'>8 _\> r8 \stemDown g8 r8 \stemDown g8 r8 _\! r4 | % 183
    R1 \pageBreak | % 184
    \time 12/8  \stemDown es8 -. _\f _ "Vla." _ "(div.)" ^ "arco"
    \stemDown f8 -. \stemDown es8 -. \stemDown f8 -. \stemDown g8 -.
    \stemDown f8 -. \stemDown g8 -. \stemDown bes8 -. \stemDown g8 -.
    \stemDown bes8 -. \stemDown c8 -. \stemDown bes8 -. | % 185
    \stemDown es8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 186
    r1 s2 | % 187
    r1 s2 | % 188
    \stemDown es,8 -. _\ff \stemDown bes'8 -. \stemDown es,8 -.
    \stemDown bes'8 -. \stemDown c8 -. \stemDown bes8 -. \stemDown c8 -.
    \stemDown d8 -. \stemDown c8 -. \stemDown d8 -. \stemDown f8 -.
    \stemDown d8 -. \pageBreak | % 189
    \stemDown f8 -. _ "Vla." _ "(div.)" r8*2/3 r8*2/3 r4.*2/3 r2.*2/3
    s1*11/24 | \barNumberCheck #190
    r1 s2 | % 191
    \stemDown a,8 -. _\ff \stemDown b8 -. \stemDown a8 -. \stemDown a8
    -. \stemDown d8 -. \stemDown a8 -. \stemDown a8 -. \stemDown b8 -.
    \stemDown a8 -. \stemDown a8 -. \stemDown d8 -. \stemDown a8 -. | % 192
    \stemDown g8 -. \stemDown a8 -. \stemDown g8 -. \stemDown g8 -.
    \stemDown d'8 -. \stemDown g,8 -. \stemDown g8 -. \stemDown a8 -.
    \stemDown g8 -. \stemDown g8 -. \stemDown d'8 -. \stemDown g,8 -. | % 193
    \stemDown g8 _\ff \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown
    cis8 \stemDown b8 \stemUp a8 \stemUp g8 \stemUp fis8 \stemUp e8
    \stemUp d8 \stemUp cis8 \pageBreak | % 194
    \numericTimeSignature\time 4/4  R1*7 \pageBreak | % 201
    R1*5 \pageBreak | % 206
    R1*5 \pageBreak | % 211
    R1*5 \pageBreak | % 216
    R1*5 \pageBreak | % 221
    R1*4 \pageBreak | % 225
    R1*3 \pageBreak | % 228
    R1*5 \pageBreak | % 233
    R1*5 \pageBreak | % 238
    R1*5 \pageBreak | % 243
    R1*5 \pageBreak | % 248
    R1*6 \pageBreak | % 254
    R1*5 \pageBreak | % 259
    R1*5 \pageBreak | % 264
    R1*5 \pageBreak | % 269
    R1*5 \pageBreak | % 274
    R1*7 \pageBreak | % 281
    R1*6 \pageBreak | % 287
    R1*5 \pageBreak | % 292
    R1*5 \pageBreak | % 297
    R1*5 \pageBreak | % 302
    R1*6 \pageBreak | % 308
    R1*6 \pageBreak | % 314
    R1*6 \pageBreak | \barNumberCheck #320
    R1*5 \pageBreak | % 325
    R1*3 \pageBreak | % 328
    R1*4 \pageBreak | % 332
    R1*4 \pageBreak | % 336
    R1*5 \pageBreak | % 341
    R1*7 \bar "|."
    }

PartPTwoTwoVoiceOne =  \relative g {
    \clef "alto" \time 12/8 \key g \major | % 1
    \stemUp g8 -. _\p \stemUp b8 -. \stemUp g8 -. r4.*2/3 \stemUp a8 -.
    \stemUp c8 -. \stemUp a8 -. r4.*2/3 s4 | % 2
    \stemDown a8 -. \stemDown d8 -. \stemDown a'8 -. r4.*2/3 r4.*2/3
    \stemDown c4 ( \stemDown fis,8 ) s4 | % 3
    r1 s2 | % 4
    \stemUp g,2. -> _\p r2.*2/3 s4 \pageBreak | % 5
    \stemUp g8 -. _\p \stemUp b8 -. \stemUp g8 -. r4.*2/3 \stemUp a8 -.
    \stemUp c8 -. \stemUp a8 -. r4.*2/3 s4 | % 6
    \stemDown a8 -. \stemDown d8 -. \stemDown a'8 -. r4.*2/3 r4.*2/3
    \stemDown c4 ( \stemDown fis,8 ) s4 | % 7
    r1 \bar "||"
    s2 | % 8
    \stemUp e,2. ^> _\p r2.*2/3 s4 | % 9
    r1 s2 \pageBreak | \barNumberCheck #10
    \numericTimeSignature\time 4/4  r2 r4 r8 \stemUp b'8 _\mp ^ "pizz."
    | % 11
    \stemDown e8 r8 r4 r2 | % 12
    r4 \stemDown e8 _\mf \stemDown b8 \stemDown fis'8 \stemDown c8 r4 | % 13
    R1 | % 14
    \time 12/8  \stemDown e8 -. _\mp ^ "arco" _\> \stemDown c8 -.
    \stemDown d8 -. \stemUp b8 -. \stemUp c8 -. \stemUp a8 -. \stemUp b8
    -. \stemUp g8 -. \stemUp a8 -. \stemUp fis8 -. _\! _\p \stemUp a8 -.
    \stemUp fis8 -. \break | % 15
    \stemDown d'8 -. \stemDown b8 -. \stemDown c8 -. \stemUp a8 -.
    \stemUp b8 -. \stemUp g8 -. \stemUp a8 -. _\markup{ \small\italic
        {dim.} } \startTrillSpan \stemUp fis8 -. \stemUp g8 -. \stemUp e8
    -. \stemUp fis8 -. \stemUp d8 -. | % 16
    \stemUp e8 -. \stemUp c8 -. \stemUp d8 -. r4.*2/3 r4.*2/3 \stemUp
    fis8 -. \stopTrillSpan _\pp \stemUp a8 -. \stemUp fis8 -. s4 | % 17
    \stemUp fis8 -. _\< \stemUp a8 -. \stemUp fis8 -. \stemUp fis8 -.
    \stemUp a8 -. \stemUp fis8 -. \stemUp fis8 -. \stemUp a8 -. \stemUp
    fis8 -. \stemUp fis8 -. _\! _\mf \stemUp a8 -. \stemUp fis8 -. | % 18
    \stemUp fis8 -. _\> \stemUp a8 -. \stemUp fis8 -. \stemUp fis8 -.
    \stemUp a8 -. \stemUp fis8 -. \stemUp fis8 -. \stemUp a8 -. \stemUp
    fis8 -. \stemUp fis8 -. \stemUp a8 -. \stemUp fis8 -. | % 19
    \stemUp fis8 -. _\! _\p \stemUp b8 -. \stemUp fis8 -. \stemUp g8 -.
    \stemUp b8 -. \stemUp g8 -. \stemUp fis8 -. \stemUp b8 -. \stemUp
    fis8 -. \stemUp e8 -. \stemUp g8 -. \stemUp e8 -. \pageBreak |
    \barNumberCheck #20
    \stemUp fis8 -. \stemUp b8 -. \stemUp fis8 -. \stemUp g8 -. \stemUp
    b8 -. \stemUp g8 -. \stemUp gis8 -. \stemUp d'8 -. \stemUp gis,8 -.
    \stemDown ais8 -. \stemDown e'8 -. \stemDown ais,8 -. | % 21
    \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 22
    r1 s2 | % 23
    \stemUp fis8 -. _\p \stemUp b8 -. \stemUp fis8 -. \stemUp g8 -.
    \stemUp b8 -. \stemUp g8 -. \stemUp fis8 -. \stemUp b8 -. \stemUp
    fis8 -. \stemUp e8 -. \stemUp g8 -. \stemUp e8 -. \break | % 24
    \stemUp fis8 -. \stemUp b8 -. \stemUp fis8 -. \stemUp g8 -. \stemUp
    b8 -. \stemUp g8 -. \stemUp gis8 -. \stemUp d'8 -. \stemUp gis,8 -.
    \stemDown ais8 -. \stemDown e'8 -. \stemDown ais,8 -. | % 25
    \stemUp b8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 26
    r1 s2 | % 27
    \stemUp a8 -. _\p \stemUp d8 -. \stemUp a8 -. \stemDown b8 -.
    _\markup{ \small\italic {poco cresc.} } \startTrillSpan \stemDown d8
    -. \stemDown b8 -. \stemUp a8 -. \stemUp d8 -. \stemUp a8 -. \stemUp
    g8 -. \stemUp b8 -. \stemUp g8 -. \pageBreak | % 28
    \stemUp a8 -. \stemUp d8 -. \stemUp a8 -. \stemDown b8 -. \stemDown
    d8 -. \stemDown b8 -. \stemDown c8 -. _\< \stemDown dis8 -.
    \stemDown c8 -. \stemDown cis8 -. \stemDown e8 -. \stemDown cis8 -.
    | % 29
    \stemDown d8 -. \stopTrillSpan _\! _\mp \stemDown e8 -. \stemDown d8
    -. \stemDown e8 -. _\< \stemDown fis8 -. \stemDown e8 -. \stemUp a,8
    -. \stemUp d8 -. \stemUp a8 -. r8*2/3 _\! r4*2/3 s8 |
    \barNumberCheck #30
    r1 s2 | % 31
    r2.*2/3 \stemUp gis8 -. _\f \stemUp b8 -. \stemUp e8 -. \stemDown d8
    -. r8*2/3 r8*2/3 s1*1/3 \pageBreak | % 32
    r2.*2/3 \stemUp gis,8 -. _\f \stemUp b8 -. \stemUp e8 -. \stemDown d8
    -. r8*2/3 r8*2/3 s1*1/3 | % 33
    \stemUp fis,8 -. _\mf \stemUp a8 -. \stemUp d8 -. \stemDown es8 -. r8*2/3
    r8*2/3 r2.*2/3 s1*1/3 | % 34
    \stemUp fis,8 -. _\mp \stemUp a8 -. \stemUp d8 -. \stemDown es8 -. r8*2/3
    r8*2/3 r2.*2/3 s1*1/3 | % 35
    \stemUp fis,8 -. _\p \stemUp a8 -. \stemUp d8 -. r4.*2/3 \stemUp
    fis,8 -. \stemUp a8 -. \stemUp d8 -. r4.*2/3 s4 \pageBreak | % 36
    \stemUp fis,8 -. \stemUp a8 -. \stemUp d8 -. r4.*2/3 \stemUp fis,8
    -. \stemUp a8 -. \stemUp d8 -. r4.*2/3 s4 | % 37
    \stemUp d,8 -. _\p \stemUp e8 -. \stemUp d8 -. \stemUp fis8 -.
    \stemUp eis8 -. \stemUp fis8 -. \stemUp e8 -. \stemUp fis8 -.
    \stemUp e8 -. \stemUp g8 -. \stemUp fis8 -. \stemUp g8 -. | % 38
    \stemUp e8 -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp g8
    -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp b8 -. \stemUp
    a8 -. \stemUp b8 -. \stemUp c8 -. | % 39
    r1 s2 | \barNumberCheck #40
    r2.*2/3 r4.*2/3 \stemUp d,8 -. _\p r8*2/3 r8*2/3 s1*11/24 \pageBreak
    | % 41
    \numericTimeSignature\time 4/4  \stemDown g''8 _\mf ^ "pizz." r8
    \stemDown d8 r8 \stemDown a8 r8 \stemDown e8 r8 | % 42
    \stemDown a8 r8 \stemDown d8 r8 \stemDown b8 r8 \stemDown d,8 _\<
    \stemDown e8 | % 43
    \stemDown fis8 \stemDown g8 \stemDown a8 \stemDown b8 \stemDown c8
    _\! r8 \stemDown b8 \stemDown a8 | % 44
    \stemDown <d, d'>8 _\> r8 \stemDown g8 r8 \stemDown g8 r8 _\! r4 | % 45
    R1 \pageBreak | % 46
    \time 12/8  \stemUp g,8 -. _\f ^ "arco" \stemUp bes8 -. \stemUp g8
    -. \stemDown bes8 -. \stemDown es8 -. \stemDown bes8 -. \stemDown es8
    -. \stemDown f8 -. \stemDown es8 -. \stemDown f8 -. \stemDown as8 -.
    \stemDown f8 -. | % 47
    \stemDown es8 -. r8*2/3 r8*2/3 r4.*2/3 \stemUp g,8 ( \stemUp as8
    \stemUp bes8 ) \stemUp c8 ( \stemUp bes8 \stemUp as8 s1*5/24 | % 48
    \stemUp g8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 49
    \stemUp dis8 -. _\ff \stemUp fis8 -. \stemUp dis8 -. \stemUp fis8 -.
    \stemUp b8 -. \stemUp fis8 -. \stemUp b8 -. \stemUp cis8 -. \stemUp
    b8 -. \stemDown cis8 -. \stemDown e8 -. \stemDown cis8 -. |
    \barNumberCheck #50
    \stemDown dis8 -. \stemDown fis8 -. \stemDown dis8 -. \stemDown cis8
    -. \stemDown dis8 -. \stemDown cis8 -. \stemDown dis8 -. \stemDown
    fis8 -. \stemDown dis8 -. \stemDown fis8 -. \stemDown gis8 -.
    \stemDown fis8 -. \pageBreak | % 51
    r1 s2 | % 52
    r1 s2 | % 53
    r1 s2 | % 54
    r1 s2 | % 55
    r1 s2 \pageBreak | % 56
    r1 s2 | % 57
    r1 s2 | % 58
    r1 s2 | % 59
    r1 s2 | \barNumberCheck #60
    r1 s2 \pageBreak | % 61
    r1 s2 | % 62
    r1 s2 | % 63
    r1 s2 | % 64
    r1 s2 | % 65
    r1 s2 \pageBreak | % 66
    r1 s2 | % 67
    r1 s2 | % 68
    r1 s2 | % 69
    r1 s2 | \barNumberCheck #70
    r1 \bar "||"
    s2 \pageBreak | % 71
    \key e \major r1 s2 | % 72
    r1 s2 | % 73
    r1 s2 | % 74
    r1 s2 | % 75
    r1 s2 \break | % 76
    r1 s2 | % 77
    r1 s2 | % 78
    r1 s2 | % 79
    r1 s2 | \barNumberCheck #80
    r1 s2 \pageBreak | % 81
    r1 s2 | % 82
    r1 s2 | % 83
    r1 s2 | % 84
    r1 s2 | % 85
    r1 s2 \pageBreak | % 86
    r1 s2 | % 87
    r1 s2 | % 88
    r1 s2 | % 89
    r1 s2 \pageBreak | \barNumberCheck #90
    r1 s2 | % 91
    r1 s2 | % 92
    r1 s2 | % 93
    r1 s2 | % 94
    r1 s2 | % 95
    r1 s2 \pageBreak | % 96
    r1 s2 | % 97
    r1 s2 | % 98
    r1 s2 | % 99
    r1 s2 | \barNumberCheck #100
    r1 s2 | % 101
    r1 s2 \break | % 102
    r1 s2 | % 103
    r1 s2 | % 104
    r1 s2 | % 105
    r1 s2 | % 106
    r1 s2 \pageBreak | % 107
    r1 s2 | % 108
    r1 s2 | % 109
    r1 s2 | \barNumberCheck #110
    r1 s2 | % 111
    r1 s2 | % 112
    r1 s2 \break | % 113
    r1 s2 | % 114
    r1 s2 | % 115
    r1 s2 | % 116
    r1 s2 | % 117
    r1 s2 \pageBreak | % 118
    r1 s2 | % 119
    r1 r2*2/3 s1*1/6 | \barNumberCheck #120
    r1 r2*2/3 s1*1/6 | % 121
    r1 r2*2/3 s1*1/6 | % 122
    r1 r2*2/3 s1*1/6 \break | % 123
    r1 r2*2/3 s1*1/6 | % 124
    r1 r2*2/3 s1*1/6 | % 125
    r1 r2*2/3 s1*1/6 | % 126
    r1 r2*2/3 s1*1/6 | % 127
    r1 r2*2/3 s1*1/6 \pageBreak | % 128
    r1 r2*2/3 s1*1/6 | % 129
    r1 r2*2/3 s1*1/6 | \barNumberCheck #130
    r1 r2*2/3 s1*1/6 | % 131
    r1 r2*2/3 s1*1/6 \pageBreak | % 132
    r1 s2 | % 133
    r1 s2 | % 134
    r1 s2 | % 135
    r1 s2 \pageBreak | % 136
    \time 4/4 \omit Staff.TimeSignature \stemDown <g, g'>8 ^ "div." r8 r4
    \stemDown d''16 \stemDown c16 \stemDown b16 \stemDown a16 \stemDown
    g16 \stemDown f16 \stemDown e16 \stemDown d16 | % 137
    \time 12/8  \stemDown <g, g'>8 _\f r8*2/3 r8*2/3 \stemUp <d b' d>8 r8*2/3
    r8*2/3 r2.*2/3 s1*5/12 | % 138
    \stemDown <g g'>8 _\mf r8*2/3 r8*2/3 \stemUp <d b' d>8 r8*2/3 r8*2/3
    r4.*2/3 r8*2/3 \stemUp g8 -. _\p \stemUp fis8 -. \bar "||"
    s1*1/3 | % 139
    \key g \major \stemUp d8 -. \stemUp e8 -. \stemUp d8 -. \stemUp fis8
    -. \stemUp eis8 -. \stemUp fis8 -. \stemUp e8 -. \stemUp fis8 -.
    \stemUp e8 -. \stemUp g8 -. \stemUp fis8 -. \stemUp g8 -. \pageBreak
    | \barNumberCheck #140
    \stemUp e8 -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp g8
    -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp b8 -. \stemUp
    a8 -. \stemUp b8 -. \stemUp c8 -. | % 141
    r1 s2 | % 142
    \stemUp g2. ^> _\p r2.*2/3 s4 | % 143
    \stemUp d8 -. _\p \stemUp e8 -. \stemUp d8 -. \stemUp fis8 -.
    \stemUp eis8 -. \stemUp fis8 -. \stemUp e8 -. \stemUp fis8 -.
    \stemUp e8 -. \stemUp g8 -. \stemUp fis8 -. \stemUp g8 -. | % 144
    \stemUp e8 -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp g8
    -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp b8 -. \stemUp
    a8 -. \stemUp b8 -. \stemUp c8 -. \pageBreak | % 145
    r1 s2 | % 146
    \stemUp e,2. ^> _\p r2.*2/3 s4 | % 147
    r1 s2 | % 148
    \numericTimeSignature\time 4/4  r2 r4 r8 \stemUp b'8 _\mp ^ "pizz."
    | % 149
    \stemDown e8 r8 r4 r2 \pageBreak | \barNumberCheck #150
    r4 \stemDown e8 _\mf \stemDown b8 \stemDown fis'8 \stemDown c8 r4 | % 151
    R1 | % 152
    \time 12/8  \stemDown e8 -. _\mp ^ "arco" _\> \stemDown c8 -.
    \stemDown d8 -. \stemUp b8 -. \stemUp c8 -. \stemUp a8 -. \stemUp b8
    -. \stemUp g8 -. \stemUp a8 -. \stemUp fis8 -. _\! _\p \stemUp a8 -.
    \stemUp fis8 -. | % 153
    \stemDown d'8 -. \stemDown b8 -. \stemDown c8 -. \stemUp a8 -.
    \stemUp b8 -. \stemUp g8 -. \stemUp a8 -. _\markup{ \small\italic
        {dim.} } \startTrillSpan \stemUp fis8 -. \stemUp g8 -. \stemUp e8
    -. \stemUp fis8 -. \stemUp d8 -. | % 154
    \stemUp e8 -. \stemUp c8 -. \stemUp d8 -. r4.*2/3 r4.*2/3 \stemUp
    fis8 -. \stopTrillSpan _\pp \stemUp a8 -. \stemUp fis8 -. s4
    \pageBreak | % 155
    \stemUp fis8 -. _\< \stemUp a8 -. \stemUp fis8 -. \stemUp fis8 -.
    \stemUp a8 -. \stemUp fis8 -. \stemUp fis8 -. \stemUp a8 -. \stemUp
    fis8 -. \stemUp fis8 -. _\! _\mf \stemUp a8 -. \stemUp fis8 -. | % 156
    \stemUp fis8 -. _\> \stemUp a8 -. \stemUp fis8 -. \stemUp fis8 -.
    \stemUp a8 -. \stemUp fis8 -. \stemUp fis8 -. \stemUp a8 -. \stemUp
    fis8 -. \stemUp fis8 -. \stemUp a8 -. \stemUp fis8 -. | % 157
    \stemUp fis8 -. _\! _\p \stemUp b8 -. \stemUp fis8 -. \stemUp g8 -.
    \stemUp b8 -. \stemUp g8 -. \stemUp fis8 -. \stemUp b8 -. \stemUp
    fis8 -. \stemUp e8 -. \stemUp g8 -. \stemUp e8 -. | % 158
    \stemUp fis8 -. \stemUp b8 -. \stemUp fis8 -. \stemUp g8 -. \stemUp
    b8 -. \stemUp g8 -. \stemUp gis8 -. \stemUp d'8 -. \stemUp gis,8 -.
    \stemDown ais8 -. \stemDown e'8 -. \stemDown ais,8 -. \break | % 159
    \stemUp b8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 |
    \barNumberCheck #160
    r1 s2 | % 161
    \stemUp fis8 -. _\p \stemUp b8 -. \stemUp fis8 -. \stemUp g8 -.
    \stemUp b8 -. \stemUp g8 -. \stemUp fis8 -. \stemUp b8 -. \stemUp
    fis8 -. \stemUp e8 -. \stemUp g8 -. \stemUp e8 -. | % 162
    \stemUp fis8 -. \stemUp b8 -. \stemUp fis8 -. \stemUp g8 -. \stemUp
    b8 -. \stemUp g8 -. \stemUp gis8 -. \stemUp d'8 -. \stemUp gis,8 -.
    \stemDown ais8 -. \stemDown e'8 -. \stemDown ais,8 -. \pageBreak | % 163
    \stemUp b8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 164
    r1 s2 | % 165
    \stemUp a8 -. _\p _\markup{ \small\italic {poco cresc.} }
    \startTrillSpan \stemUp d8 -. \stemUp a8 -. \stemDown b8 -.
    \stemDown d8 -. \stemDown b8 -. \stemUp a8 -. \stemUp d8 -. \stemUp
    a8 -. \stemUp g8 -. \stemUp b8 -. \stemUp g8 -. | % 166
    \stemUp a8 -. \stemUp d8 -. \stemUp a8 -. \stemDown b8 -. \stemDown
    d8 -. \stemDown b8 -. \stemDown c8 -. _\< \stemDown dis8 -.
    \stemDown c8 -. \stemDown cis8 -. \stemDown e8 -. \stemDown cis8 -.
    \pageBreak | % 167
    \stemDown d8 -. \stopTrillSpan _\! _\mp _\< \stemDown e8 -.
    \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -.
    \stemUp a,8 -. \stemUp d8 -. \stemUp a8 -. r4.*2/3 _\! s8 | % 168
    r1 s2 | % 169
    r2.*2/3 \stemUp gis8 -. _\f \stemUp b8 -. \stemUp e8 -. \stemDown d8
    -. r8*2/3 r8*2/3 s1*1/3 | \barNumberCheck #170
    r2.*2/3 \stemUp gis,8 -. _\f \stemUp b8 -. \stemUp e8 -. \stemDown d8
    -. r8*2/3 r8*2/3 s1*1/3 \pageBreak | % 171
    \stemUp fis,8 -. _\mf \stemUp a8 -. \stemUp d8 -. \stemDown es8 -. r8*2/3
    r8*2/3 r2.*2/3 s1*1/3 | % 172
    \stemUp fis,8 -. _\mp \stemUp a8 -. \stemUp d8 -. \stemDown es8 -. r8*2/3
    r8*2/3 r2.*2/3 s1*1/3 | % 173
    \stemUp fis,8 -. _\p \stemUp a8 -. \stemUp d8 -. r4.*2/3 \stemUp
    fis,8 -. \stemUp a8 -. \stemUp d8 -. r4.*2/3 s4 | % 174
    \stemUp fis,8 -. \stemUp a8 -. \stemUp d8 -. r4.*2/3 \stemUp fis,8
    -. \stemUp a8 -. \stemUp d8 -. r4.*2/3 s4 \pageBreak | % 175
    \stemUp d,8 -. _\p \stemUp e8 -. \stemUp d8 -. \stemUp fis8 -.
    \stemUp eis8 -. \stemUp fis8 -. \stemUp e8 -. \stemUp fis8 -.
    \stemUp e8 -. \stemUp g8 -. \stemUp fis8 -. \stemUp g8 -. | % 176
    \stemUp e8 -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp g8
    -. \stemUp fis8 -. \stemUp g8 -. \stemUp a8 -. \stemUp b8 -. \stemUp
    a8 -. \stemUp b8 -. \stemUp c8 -. | % 177
    r1 s2 | % 178
    r2.*2/3 r4.*2/3 \stemUp d,8 _\p r8*2/3 r8*2/3 s1*11/24 | % 179
    \numericTimeSignature\time 4/4  \stemDown g''8 _\mf ^ "pizz." r8
    \stemDown d8 r8 \stemDown a8 r8 \stemDown e8 r8 \pageBreak |
    \barNumberCheck #180
    \stemDown a8 r8 \stemDown d8 r8 \stemDown b8 r8 \stemDown d,8 _\<
    \stemDown e8 | % 181
    \stemDown fis8 \stemDown g8 \stemDown a8 \stemDown b8 \stemDown c8
    _\! r8 \stemDown b8 \stemDown a8 | % 182
    \stemDown <d, d'>8 _\> r8 \stemDown g8 r8 \stemDown g8 r8 _\! r4 | % 183
    R1 \pageBreak | % 184
    \time 12/8  \stemUp a,8 -. _\f ^ "arco" \stemUp bes8 -. \stemUp g8
    -. \stemDown bes8 -. \stemDown es8 -. \stemDown bes8 -. \stemDown es8
    -. \stemDown f8 -. \stemDown es8 -. \stemDown f8 -. \stemDown a8 -.
    \stemDown f8 -. | % 185
    \stemDown es8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 186
    r1 s2 | % 187
    r1 s2 | % 188
    \stemDown c8 -. _\ff \stemDown es8 -. \stemDown c8 -. \stemDown d8
    -. \stemDown f8 -. \stemDown d8 -. \stemDown f8 -. \stemDown bes8 -.
    \stemDown f8 -. \stemDown bes8 -. \stemDown c8 -. \stemDown bes8 -.
    \pageBreak | % 189
    \stemDown f'8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 |
    \barNumberCheck #190
    r1 s2 | % 191
    \stemDown d,8 -. _\ff \stemDown g8 -. \stemDown d8 -. \stemDown fis8
    -. \stemDown g8 -. \stemDown fis8 -. \stemDown d8 -. \stemDown g8 -.
    \stemDown d8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown fis8 -.
    | % 192
    \stemDown d8 -. \stemDown g8 -. \stemDown d8 -. \stemDown d8 -.
    \stemDown g8 -. \stemDown d8 -. \stemDown d8 -. \stemDown g8 -.
    \stemDown d8 -. \stemDown d8 -. \stemDown g8 -. \stemDown d8 -. | % 193
    \stemDown g8 _\ff \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown
    cis8 \stemDown b8 \stemUp a8 \stemUp g8 \stemUp fis8 \stemUp e8
    \stemUp d8 \stemUp cis8 \pageBreak | % 194
    \numericTimeSignature\time 4/4  R1*7 \pageBreak | % 201
    R1*5 \pageBreak | % 206
    R1*5 \pageBreak | % 211
    R1*5 \pageBreak | % 216
    R1*5 \pageBreak | % 221
    R1*4 \pageBreak | % 225
    R1*3 \pageBreak | % 228
    R1*5 \pageBreak | % 233
    R1*5 \pageBreak | % 238
    R1*5 \pageBreak | % 243
    R1*5 \pageBreak | % 248
    R1*6 \pageBreak | % 254
    R1*5 \pageBreak | % 259
    R1*5 \pageBreak | % 264
    R1*5 \pageBreak | % 269
    R1*5 \pageBreak | % 274
    R1*7 \pageBreak | % 281
    R1*6 \pageBreak | % 287
    R1*5 \pageBreak | % 292
    R1*5 \pageBreak | % 297
    R1*5 \pageBreak | % 302
    R1*6 \pageBreak | % 308
    R1*6 \pageBreak | % 314
    R1*6 \pageBreak | \barNumberCheck #320
    R1*5 \pageBreak | % 325
    R1*3 \pageBreak | % 328
    R1*4 \pageBreak | % 332
    R1*4 \pageBreak | % 336
    R1*5 \pageBreak | % 341
    R1*7 \bar "|."
    }

PartPTwoThreeVoiceOne =  \relative cis' {
    \clef "bass" \time 12/8 \key g \major | % 1
    r1 s2 | % 2
    r1 s2 | % 3
    r1 s2 | % 4
    \stemDown cis8 ( -> _\p \stemDown d8 \stemDown dis8 \stemDown e8
    \stemDown c8 \stemDown b8 ) r2.*2/3 s4 \pageBreak | % 5
    r1 _ "Vc." _ "(div.)" s2 | % 6
    r1 s2 | % 7
    r1 \bar "||"
    s2 | % 8
    \stemDown ais8 ( -> _\p \stemDown b8 \stemDown c8 \stemDown b8
    \stemDown a8 \stemDown g8 ) r2.*2/3 s4 | % 9
    r1 s2 \pageBreak | \barNumberCheck #10
    r1 _ "Vc." _ "(div.)" s2 | % 11
    r1 s2 | % 12
    \numericTimeSignature\time 4/4  r2 \stemDown fis8 _\mf ^ "pizz."
    \stemDown c8 \stemDown g'8 \stemDown es8 | % 13
    \stemUp c8 r8 r4 r2 | % 14
    R1 \break | % 15
    R1*3 _ "Vc." | % 18
    \time 12/8  r2.*2/3 _ "(div.)" \stemUp c8 _\mp ^ "pizz." r8*2/3 r8*2/3
    \stemUp c8 _\p r8*2/3 r8*2/3 s1*5/12 | % 19
    \stemUp b8 r8*2/3 r8*2/3 \stemDown b'8 r8*2/3 r8*2/3 r4.*2/3
    \stemDown b8 r8*2/3 r8*2/3 s4. \pageBreak | \barNumberCheck #20
    r4.*2/3 _ "Vc." _ "(div.)" \stemDown b8 _\sempre _\p r8*2/3 r8*2/3 r4.*2/3
    \stemDown b8 r8*2/3 r8*2/3 s1*5/12 | % 21
    r4.*2/3 \stemDown b8 r8*2/3 r8*2/3 r4.*2/3 \stemDown b8 r8*2/3 r8*2/3
    s1*5/12 | % 22
    r4.*2/3 \stemDown b8 r8*2/3 r8*2/3 r4.*2/3 \stemDown b8 r8*2/3 r8*2/3
    s1*5/12 | % 23
    r4.*2/3 \stemDown b8 r8*2/3 r8*2/3 r4.*2/3 \stemDown b8 r8*2/3 r8*2/3
    s1*5/12 \break | % 24
    r4.*2/3 _ "Vc." _ "(div.)" \stemDown b8 r8*2/3 r8*2/3 r4.*2/3
    \stemDown b8 r8*2/3 r8*2/3 s1*5/12 | % 25
    r4.*2/3 \stemDown b8 r8*2/3 r8*2/3 r4.*2/3 \stemDown b8 r8*2/3 r8*2/3
    s1*5/12 | % 26
    r4.*2/3 \stemDown b8 r8*2/3 r8*2/3 r2.*2/3 s1*11/24 | % 27
    r4.*2/3 \stemDown a8 _\markup{ \small\italic {poco a poco cresc.} }
    \startTrillSpan r8*2/3 r8*2/3 r4.*2/3 \stemDown a8 r8*2/3 r8*2/3
    s1*5/12 \pageBreak | % 28
    r4.*2/3 _ "Vc." _ "(div.)" \stemDown a8 r8*2/3 r8*2/3 r4.*2/3
    \stemDown a8 r8*2/3 r8*2/3 s1*5/12 | % 29
    r4.*2/3 \stemDown a8 r8*2/3 r8*2/3 r4.*2/3 \stemDown a8 r8*2/3 r8*2/3
    s1*5/12 | \barNumberCheck #30
    r4.*2/3 \stemDown a8 r8*2/3 r8*2/3 r4.*2/3 \stemDown a8
    \stopTrillSpan _\f r8*2/3 r8*2/3 s1*5/12 | % 31
    r1 s2 \pageBreak | % 32
    r1 _ "Vc." _ "(div.)" s2 | % 33
    r2.*2/3 \stemDown e8 _\mf ^ "arco" \stemDown fis8 \stemDown gis8
    \stemDown bes8 r8*2/3 r8*2/3 s1*1/3 | % 34
    r2.*2/3 \stemDown e,8 -. _\mp \stemDown fis8 -. \stemDown gis8 -.
    \stemDown bes8 -. r8*2/3 r8*2/3 s1*1/3 | % 35
    r2.*2/3 \stemDown a8 -. _\p ^ "pizz." r8*2/3 r8*2/3 \stemDown d8 r8*2/3
    r8*2/3 s1*5/12 \pageBreak | % 36
    r1 _ "Vc." _ "(div.)" s2 | % 37
    \clef "tenor" \numericTimeSignature\time 4/4 \stemDown g8 _\p r8
    \stemDown d8 r8 \stemDown a8 r8 \stemUp e8 r8 | % 38
    \stemDown a8 r8 \stemDown d8 r8 \stemDown b8 r8 \stemUp d,8 _\<
    \stemUp e8 | % 39
    \stemUp fis8 \stemUp g8 \stemUp a8 \stemUp b8 \stemDown c8 _\! _\mf
    r8 \stemDown b8 \stemDown a8 | \barNumberCheck #40
    \time 12/8  \stemDown d8 r8*2/3 r8*2/3 r4.*2/3 \stemDown e8 ( -> _\p
    ^ "arco" \stemDown d8 \stemDown c8 \stemDown b8 \stemDown a8
    \stemDown g8 ) s1*5/24 \pageBreak | % 41
    \stemDown b8 -. _ "Vc." _ "(div.)" \stemDown g8 -. \stemDown b8 -.
    \stemUp a8 -. \stemUp gis8 -. \stemUp a8 -. \stemDown c8 -.
    \stemDown a8 -. \stemDown c8 -. \stemDown b8 -. \stemDown ais8 -.
    \stemDown b8 -. | % 42
    \stemDown c8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown e8 -. \stemDown d8 -. \stemDown e8 -. \stemDown fis8 -.
    \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown a8 -. | % 43
    r1 s2 | % 44
    r2.*2/3 \stemDown e8 ( -> _\p \stemDown d8 \stemDown c8 \stemDown b8
    \stemDown a8 \stemDown g8 ) s4 | % 45
    \clef "bass" \stemDown es8 -. _\f \stemDown f8 -. \stemDown es8 -.
    \stemDown f8 -. \stemDown g8 -. \stemDown f8 -. \stemDown g8 -.
    \stemDown bes8 -. \stemDown g8 -. \stemDown bes8 -. \stemDown c8 -.
    \stemDown bes8 -. \pageBreak | % 46
    \stemDown es,8 -. _ "Vc." _ "(div.)" \stemDown f8 -. \stemDown es8
    -. \stemDown f8 -. \stemDown g8 -. \stemDown f8 -. \stemDown g8 -.
    \stemDown bes8 -. \stemDown g8 -. \stemDown bes8 -. \stemDown c8 -.
    \stemDown bes8 -. | % 47
    \stemDown es8 -. r8*2/3 r8*2/3 r4.*2/3 \stemDown g,8 ( \stemDown as8
    \stemDown bes8 ) \stemDown c8 ( \stemDown bes8 \stemDown as8 s1*5/24
    | % 48
    \stemDown g8 ) r8*2/3 r8*2/3 r4.*2/3 \stemUp g,8 ( _\f \stemUp as8
    \stemUp a8 ) \stemUp bes8 ( \stemUp as8 \stemUp g8 s1*5/24 | % 49
    \stemUp fis8 ) r8*2/3 r8*2/3 \stemUp cis'8 -. _\ff \stemUp dis8 -.
    \stemUp cis8 -. \stemDown dis8 -. \stemDown fis8 -. \stemDown dis8
    -. \stemDown fis8 -. \stemDown gis8 -. \stemDown fis8 -. s1*1/12 |
    \barNumberCheck #50
    \stemDown b8 -. \stemDown cis8 -. \stemDown b8 -. \stemDown fis8 -.
    \stemDown b8 -. \stemDown fis8 -. \stemDown b8 -. \stemDown cis8 -.
    \stemDown b8 -. \stemDown cis8 -. \stemDown e8 -. \stemDown cis8 -.
    \pageBreak | % 51
    r1 s2 | % 52
    r1 s2 | % 53
    r1 s2 | % 54
    r1 s2 | % 55
    r1 _\< s2 _\! \pageBreak | % 56
    r1 s2 | % 57
    r1 s2 | % 58
    r1 s2 | % 59
    r1 _\< s2 | \barNumberCheck #60
    r1 s2 _\! \pageBreak | % 61
    r1 s2 | % 62
    r1 s2 | % 63
    r1 s2 | % 64
    r1 s2 | % 65
    r1 s2 \pageBreak | % 66
    r1 s2 | % 67
    r1 s2 | % 68
    r1 s2 | % 69
    r1 s2 | \barNumberCheck #70
    r1 \bar "||"
    s2 \pageBreak | % 71
    \key e \major r1 s2 | % 72
    r1 s2 | % 73
    r1 s2 | % 74
    r1 s2 | % 75
    r1 s2 \break | % 76
    r1 s2 | % 77
    r1 s2 | % 78
    r1 s2 | % 79
    r1 s2 | \barNumberCheck #80
    r1 s2 \pageBreak | % 81
    r1 s2 | % 82
    r1 s2 | % 83
    r1 s2 | % 84
    r1 s2 | % 85
    r1 s2 \pageBreak | % 86
    r1 s2 | % 87
    r1 s2 | % 88
    r1 s2 | % 89
    r1 s2 \pageBreak | \barNumberCheck #90
    r1 s2 | % 91
    r1 s2 | % 92
    r1 s2 | % 93
    r1 s2 | % 94
    r1 s2 | % 95
    r1 s2 \pageBreak | % 96
    r1 s2 | % 97
    r1 s2 | % 98
    r1 s2 | % 99
    r1 s2 | \barNumberCheck #100
    r1 s2 | % 101
    r1 s2 \break | % 102
    r1 s2 | % 103
    r1 s2 | % 104
    r1 s2 | % 105
    r1 s2 | % 106
    r1 s2 \pageBreak | % 107
    r1 s2 | % 108
    r1 s2 | % 109
    r1 s2 | \barNumberCheck #110
    r1 s2 | % 111
    r1 s2 | % 112
    r1 s2 \break | % 113
    r1 s2 | % 114
    r1 s2 | % 115
    r1 s2 | % 116
    r1 s2 | % 117
    r1 s2 \pageBreak | % 118
    r1 s2 | % 119
    r1 r2*2/3 s1*1/6 | \barNumberCheck #120
    r1 r2*2/3 s1*1/6 | % 121
    r1 r2*2/3 s1*1/6 | % 122
    r1 r2*2/3 s1*1/6 \break | % 123
    r1 r2*2/3 s1*1/6 | % 124
    r1 r2*2/3 s1*1/6 | % 125
    r1 r2*2/3 s1*1/6 | % 126
    r1 r2*2/3 s1*1/6 | % 127
    r1 r2*2/3 s1*1/6 \pageBreak | % 128
    r1 r2*2/3 s1*1/6 | % 129
    r1 r2*2/3 s1*1/6 | \barNumberCheck #130
    r1 s2 | % 131
    r1 r2*2/3 s1*1/6 \pageBreak | % 132
    r1 s2 | % 133
    r1 s2 | % 134
    r1 s2 | % 135
    r1 s2 \pageBreak | % 136
    \time 4/4 \omit Staff.TimeSignature \stemDown e4 ( -> _ "Vc." _
    "(div.)" \stemDown d8 r16 \stemDown c16 ) -. \stemDown b8 -.
    \stemDown g,8 :16 \stemDown a8 :16 \stemDown b8 :16 | % 137
    \time 12/8  \stemUp <e, c'>8 _\f r8*2/3 r8*2/3 \stemUp <g d'>8 r8*2/3
    r8*2/3 r2.*2/3 s1*5/12 | % 138
    \stemUp <e c'>8 _\mf r8*2/3 r8*2/3 \stemUp <g d'>8 r8*2/3 r8*2/3 r4.*2/3
    r8*2/3 \stemDown e''8 -. _\p \stemDown d8 -. \bar "||"
    s1*1/3 | % 139
    \key g \major \stemDown g,8 -. \stemDown b8 -. \stemDown g8 -.
    \stemDown d'8 -. r8*2/3 r8*2/3 \stemDown a8 -. \stemDown c8 -.
    \stemDown a8 -. \stemDown e'8 -. r8*2/3 r8*2/3 s1*1/6 \pageBreak |
    \barNumberCheck #140
    \stemDown a,8 -. _ "Vc." _ "(div.)" \stemDown d8 -. \stemDown a'8 -.
    r4.*2/3 \stemDown b,4 ( \stemDown e,8 ) \stemDown c'4 ( \stemDown
    fis,8 ) s8 | % 141
    r1 s2 | % 142
    \stemDown cis'8 ( -> _\p \stemDown d8 \stemDown dis8 \stemDown e8
    \stemDown c8 \stemDown b8 ) r2.*2/3 s4 | % 143
    \stemDown g8 -. _\p \stemDown b8 -. \stemDown g8 -. \stemDown d'8 -.
    r8*2/3 r8*2/3 \stemDown a8 -. \stemDown c8 -. \stemDown a8 -.
    \stemDown e'8 -. r8*2/3 r8*2/3 s1*1/6 | % 144
    \stemDown a,8 -. \stemDown d8 -. \stemDown a'8 -. r4.*2/3 \stemDown
    b,4 ( \stemDown e,8 ) \stemDown c'4 ( \stemDown fis,8 ) s8
    \pageBreak | % 145
    r1 _ "Vc." _ "(div.)" s2 | % 146
    \stemDown ais8 ( -> _\p \stemDown b8 \stemDown c8 \stemDown b8
    \stemDown a8 \stemDown g8 ) r2.*2/3 s4 | % 147
    r1 s2 | % 148
    r1 s2 | % 149
    r1 s2 \pageBreak | \barNumberCheck #150
    \numericTimeSignature\time 4/4  r2 _ "Vc." _ "(div.)" \stemDown fis8
    _\mf ^ "pizz." \stemDown c8 \stemDown g'8 \stemDown es8 | % 151
    \stemUp c8 r8 r4 r2 | % 152
    R1*3 \pageBreak | % 155
    R1 _ "Vc." | % 156
    \time 12/8  r2.*2/3 _ "(div.)" \stemUp c8 _\mp ^ "pizz." r8*2/3 r8*2/3
    \stemUp c8 _\p r8*2/3 r8*2/3 s1*5/12 | % 157
    \stemUp b8 r8*2/3 r8*2/3 \stemDown b'8 r8*2/3 r8*2/3 r4.*2/3
    \stemDown b8 r8*2/3 r8*2/3 s4. | % 158
    r4.*2/3 \stemDown b8 r8*2/3 r8*2/3 r4.*2/3 \stemDown b8 r8*2/3 r8*2/3
    s1*5/12 \break | % 159
    r4.*2/3 _ "Vc." _ "(div.)" \stemDown b8 r8*2/3 r8*2/3 r4.*2/3
    \stemDown b8 r8*2/3 r8*2/3 s1*5/12 | \barNumberCheck #160
    r4.*2/3 \stemDown b8 r8*2/3 r8*2/3 r4.*2/3 \stemDown b8 r8*2/3 r8*2/3
    s1*5/12 | % 161
    r4.*2/3 \stemDown b8 r8*2/3 r8*2/3 r4.*2/3 \stemDown b8 r8*2/3 r8*2/3
    s1*5/12 | % 162
    r4.*2/3 \stemDown b8 r8*2/3 r8*2/3 r4.*2/3 \stemDown b8 r8*2/3 r8*2/3
    s1*5/12 \pageBreak | % 163
    r4.*2/3 _ "Vc." _ "(div.)" \stemDown b8 r8*2/3 r8*2/3 r4.*2/3
    \stemDown b8 r8*2/3 r8*2/3 s1*5/12 | % 164
    r4.*2/3 \stemDown b8 r8*2/3 r8*2/3 r2.*2/3 s1*11/24 | % 165
    r4.*2/3 \stemDown a8 _\markup{ \small\italic {poco a poco cresc.} }
    \startTrillSpan r8*2/3 r8*2/3 r4.*2/3 \stemDown a8 r8*2/3 r8*2/3
    s1*5/12 | % 166
    r4.*2/3 \stemDown a8 r8*2/3 r8*2/3 r4.*2/3 \stemDown a8 r8*2/3 r8*2/3
    s1*5/12 \pageBreak | % 167
    r4.*2/3 _ "Vc." _ "(div.)" \stemUp a,8 r8*2/3 r8*2/3 r4.*2/3 \stemUp
    a8 r8*2/3 r8*2/3 s1*5/12 | % 168
    r4.*2/3 \stemUp a8 r8*2/3 r8*2/3 r4.*2/3 \stemUp a8 \stopTrillSpan
    _\f r8*2/3 r8*2/3 s1*5/12 | % 169
    r1 s2 | \barNumberCheck #170
    r1 s2 \pageBreak | % 171
    r2.*2/3 _ "Vc." _ "(div.)" \stemDown e'8 -. _\mf ^ "arco" \stemDown
    fis8 -. \stemDown gis8 -. \stemDown bes8 -. r8*2/3 r8*2/3 s1*1/3 | % 172
    r2.*2/3 \stemDown e,8 -. _\mp \stemDown fis8 -. \stemDown gis8 -.
    \stemDown bes8 -. r8*2/3 r8*2/3 s1*1/3 | % 173
    r2.*2/3 \stemDown a8 _\p ^ "pizz." r8*2/3 r8*2/3 \stemDown d8 r8*2/3
    r8*2/3 s1*5/12 | % 174
    r1 s2 \pageBreak | % 175
    \clef "tenor" \numericTimeSignature\time 4/4 \stemDown g8 _\p _
    "Vc." _ "(div.)" r8 \stemDown d8 r8 \stemDown a8 r8 \stemUp e8 r8 | % 176
    \stemDown a8 r8 \stemDown d8 r8 \stemDown b8 r8 \stemUp d,8 _\<
    \stemUp e8 | % 177
    \stemUp fis8 \stemUp g8 \stemUp a8 \stemUp b8 \stemDown c8 _\! _\mf
    r8 \stemDown b8 \stemDown a8 | % 178
    \time 12/8  \stemDown d8 r8*2/3 r8*2/3 r4.*2/3 \stemDown e8 ( -> _\p
    ^ "arco" \stemDown d8 \stemDown c8 \stemDown b8 \stemDown a8
    \stemDown g8 ) s1*5/24 | % 179
    \stemDown b8 -. _\p \stemDown g8 -. \stemDown b8 -. \stemUp a8 -.
    \stemUp gis8 -. \stemUp a8 -. \stemDown c8 -. \stemDown a8 -.
    \stemDown c8 -. \stemDown b8 -. \stemDown ais8 -. \stemDown b8 -.
    \pageBreak | \barNumberCheck #180
    \stemDown c8 -. _ "Vc." _ "(div.)" \stemDown d8 -. \stemDown e8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown d8 -. \stemDown e8 -.
    \stemDown fis8 -. \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -.
    \stemDown a8 -. | % 181
    r1 s2 | % 182
    r2.*2/3 \stemDown e8 ( -> _\p \stemDown d8 \stemDown c8 \stemDown b8
    \stemDown a8 \stemDown g8 ) s4 | % 183
    \clef "bass" \stemDown es8 -. _\f \stemDown f8 -. \stemDown es8 -.
    \stemDown f8 -. \stemDown g8 -. \stemDown f8 -. \stemDown g8 -.
    \stemDown bes8 -. \stemDown g8 -. \stemDown bes8 -. \stemDown c8 -.
    \stemDown bes8 -. \pageBreak | % 184
    \stemDown es,8 -. _ "Vc." _ "(div.)" \stemDown f8 -. \stemDown es8
    -. \stemDown f8 -. \stemDown g8 -. \stemDown f8 -. \stemDown g8 -.
    \stemDown bes8 -. \stemDown g8 -. \stemDown bes8 -. \stemDown c8 -.
    \stemDown bes8 -. | % 185
    \stemDown es8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 186
    \stemDown bes8 ( _\f \stemDown c8 \stemDown d8 ) \stemDown es8 (
    \stemDown d8 \stemDown c8 \stemDown bes8 ) r8*2/3 r8*2/3 r4.*2/3
    s1*5/24 | % 187
    \stemDown es,8 -. _\ff \stemDown bes'8 -. \stemDown es,8 -.
    \stemDown bes'8 -. \stemDown c8 -. \stemDown bes8 -. \stemDown c8 -.
    \stemDown d8 -. \stemDown c8 -. \stemDown d8 -. \stemDown f8 -.
    \stemDown d8 -. | % 188
    \stemDown es,8 -. \stemDown bes'8 -. \stemDown es,8 -. \stemDown
    bes'8 -. \stemDown c8 -. \stemDown bes8 -. \stemDown c8 -. \stemDown
    d8 -. \stemDown c8 -. \stemDown d8 -. \stemDown f8 -. \stemDown d8
    -. \pageBreak | % 189
    \stemDown f8 -. _ "Vc." _ "(div.)" r8*2/3 r8*2/3 r4.*2/3 r2.*2/3
    s1*11/24 | \barNumberCheck #190
    \stemDown d8 ( _\ff \stemDown es8 \stemDown f8 ) \stemDown g8 (
    \stemDown f8 \stemDown es8 \stemDown d8 ) r8*2/3 r8*2/3 r4.*2/3
    s1*5/24 | % 191
    \stemDown a8 -. _\ff \stemDown b8 -. \stemDown a8 -. \stemDown a8 -.
    \stemDown d8 -. \stemDown a8 -. \stemDown a8 -. \stemDown b8 -.
    \stemDown a8 -. \stemDown a8 -. \stemDown d8 -. \stemDown a8 -. | % 192
    \stemDown g8 -. \stemDown a8 -. \stemDown g8 -. \stemDown g8 -.
    \stemDown d'8 -. \stemDown g,8 -. \stemDown g8 -. \stemDown a8 -.
    \stemDown g8 -. \stemDown g8 -. \stemDown d'8 -. \stemDown g,8 -. | % 193
    \stemDown g'8 _\ff \stemDown fis8 \stemDown e8 \stemDown d8
    \stemDown cis8 \stemDown b8 \stemDown a8 \stemDown g8 \stemDown fis8
    \stemDown e8 \stemDown d8 \stemDown cis8 \pageBreak | % 194
    \numericTimeSignature\time 4/4  R1*7 \pageBreak | % 201
    R1*5 \pageBreak | % 206
    R1*5 \pageBreak | % 211
    R1*5 \pageBreak | % 216
    R1*5 \pageBreak | % 221
    R1*4 \pageBreak | % 225
    R1*3 \pageBreak | % 228
    R1*5 \pageBreak | % 233
    R1*5 \pageBreak | % 238
    R1*5 \pageBreak | % 243
    R1*5 \pageBreak | % 248
    R1*6 \pageBreak | % 254
    R1*5 \pageBreak | % 259
    R1*5 \pageBreak | % 264
    R1*5 \pageBreak | % 269
    R1*5 \pageBreak | % 274
    R1*7 \pageBreak | % 281
    R1*6 \pageBreak | % 287
    R1*5 \pageBreak | % 292
    R1*5 \pageBreak | % 297
    R1*5 \pageBreak | % 302
    R1*6 \pageBreak | % 308
    R1*6 \pageBreak | % 314
    R1*6 \pageBreak | \barNumberCheck #320
    R1*5 \pageBreak | % 325
    R1*3 \pageBreak | % 328
    R1*4 \pageBreak | % 332
    R1*4 \pageBreak | % 336
    R1*5 \pageBreak | % 341
    R1*7 \bar "|."
    }

PartPTwoFourVoiceOne =  \relative cis {
    \clef "bass" \time 12/8 \key g \major | % 1
    r1 s2 | % 2
    r1 s2 | % 3
    r1 s2 | % 4
    \stemUp cis8 ( -> _\p \stemUp d8 \stemUp dis8 \stemUp e8 \stemUp c8
    \stemUp b8 ) r2.*2/3 s4 \pageBreak | % 5
    r1 s2 | % 6
    r1 s2 | % 7
    r1 \bar "||"
    s2 | % 8
    \stemUp ais8 ( ^> _\p \stemUp b8 \stemUp c8 \stemUp b8 \stemUp a8
    \stemUp g8 ) r2.*2/3 s4 | % 9
    r1 s2 \pageBreak | \barNumberCheck #10
    r1 s2 | % 11
    r1 s2 | % 12
    \numericTimeSignature\time 4/4  r2 r4 \stemUp g8 _\mf ^ "pizz."
    \stemUp es8 | % 13
    \stemUp c8 r8 r4 r2 | % 14
    R1 \break | % 15
    R1*4 | % 19
    \time 12/8  r4.*2/3 \stemUp b'8 _\p ^ "pizz." r8*2/3 r8*2/3 r4.*2/3
    \stemUp b8 r8*2/3 r8*2/3 s1*5/12 \pageBreak | \barNumberCheck #20
    r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3
    s1*5/12 | % 21
    r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3
    s1*5/12 | % 22
    r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3
    s1*5/12 | % 23
    r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3
    s1*5/12 \break | % 24
    r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3
    s1*5/12 | % 25
    r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3
    s1*5/12 | % 26
    r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r2.*2/3 s1*11/24 | % 27
    r4.*2/3 \stemUp a8 _\markup{ \small\italic {poco a poco cresc.} }
    \startTrillSpan r8*2/3 r8*2/3 r4.*2/3 \stemUp a8 r8*2/3 r8*2/3
    s1*5/12 \pageBreak | % 28
    r4.*2/3 \stemUp a8 r8*2/3 r8*2/3 r4.*2/3 \stemUp a8 r8*2/3 r8*2/3
    s1*5/12 | % 29
    r4.*2/3 \stemUp a8 r8*2/3 r8*2/3 r4.*2/3 \stemUp a8 r8*2/3 r8*2/3
    s1*5/12 | \barNumberCheck #30
    r4.*2/3 \stemUp a8 r8*2/3 r8*2/3 r4.*2/3 \stemUp a8 \stopTrillSpan
    _\f r8*2/3 r8*2/3 s1*5/12 | % 31
    r1 s2 \pageBreak | % 32
    r1 s2 | % 33
    r2.*2/3 \stemUp gis8 -. _\mf ^ "arco" \stemUp b8 -. \stemUp e8 -.
    \stemDown d8 -. r8*2/3 r8*2/3 s1*1/3 | % 34
    r2.*2/3 \stemUp gis,8 -. _\mp \stemUp b8 -. \stemUp e8 -. \stemDown
    d8 -. r8*2/3 r8*2/3 s1*1/3 | % 35
    r2.*2/3 \stemUp a8 _\p ^ "pizz." r8*2/3 r8*2/3 \stemDown d8 r8*2/3 r8*2/3
    s1*5/12 \pageBreak | % 36
    r1 s2 | % 37
    r1 s2 | % 38
    r1 s2 | % 39
    r1 s2 | \barNumberCheck #40
    r2.*2/3 \stemDown b'8 ( -> _\p ^ "arco" \stemDown g8 \stemDown e8
    \stemDown g8 \stemDown d8 \stemDown b8 ) s4 \pageBreak | % 41
    \stemDown d8 -. \stemDown e8 -. \stemDown d8 -. \stemDown fis8 -.
    \stemDown eis8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -.
    | % 42
    \stemDown e8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown a8 -.
    \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown a8 -.
    \stemDown b8 -. \stemDown a8 -. \stemDown b8 -. \stemDown c8 -. | % 43
    \stemDown d,8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 44
    r2.*2/3 \stemDown b'8 ( -> _\p \stemDown g8 \stemDown e8 \stemDown g8
    \stemDown d8 \stemDown b8 ) s4 | % 45
    \stemUp g8 -. _\f \stemUp bes8 -. \stemUp g8 -. \stemUp bes8 -.
    \stemUp es8 -. \stemUp bes8 -. \stemDown es8 -. \stemDown f8 -.
    \stemDown es8 -. \stemDown f8 -. \stemDown as8 -. \stemDown f8 -.
    \pageBreak | % 46
    \stemUp g,8 -. \stemUp bes8 -. \stemUp g8 -. \stemUp bes8 -. \stemUp
    es8 -. \stemUp bes8 -. \stemDown es8 -. \stemDown f8 -. \stemDown es8
    -. \stemDown f8 -. \stemDown as8 -. \stemDown f8 -. | % 47
    \stemDown es8 -. r8*2/3 r8*2/3 r4.*2/3 \stemDown g8 ( \stemDown as8
    \stemDown bes8 ) \stemDown c8 ( \stemDown bes8 \stemDown as8 s1*5/24
    | % 48
    \stemDown g8 ) r8*2/3 r8*2/3 r4.*2/3 \stemUp g,8 ( _\f \stemUp as8
    \stemUp a8 ) \stemUp bes8 ( \stemUp as8 \stemUp g8 s1*5/24 | % 49
    \stemUp fis8 ) r8*2/3 r8*2/3 \stemUp fis8 -. _\ff \stemUp b8 -.
    \stemUp fis8 -. \stemUp b8 -. \stemUp cis8 -. \stemUp b8 -.
    \stemDown cis8 -. \stemDown e8 -. \stemDown cis8 -. s1*1/12 |
    \barNumberCheck #50
    \stemDown dis8 -. \stemDown fis8 -. \stemDown dis8 -. \stemDown fis8
    -. \stemDown b8 -. \stemDown fis8 -. \stemDown b8 -. \stemDown cis8
    -. \stemDown b8 -. \stemDown cis8 -. \stemDown e8 -. \stemDown cis8
    -. \pageBreak | % 51
    r1 s2 | % 52
    r1 s2 | % 53
    r1 s2 | % 54
    r1 s2 | % 55
    r1 _\< s2 _\! \pageBreak | % 56
    r1 s2 | % 57
    r1 s2 | % 58
    r1 s2 | % 59
    r1 _\< s2 | \barNumberCheck #60
    r1 s2 _\! \pageBreak | % 61
    r1 s2 | % 62
    r1 s2 | % 63
    r1 s2 | % 64
    r1 s2 | % 65
    r1 s2 \pageBreak | % 66
    r1 s2 | % 67
    r1 s2 | % 68
    r1 s2 | % 69
    r1 s2 | \barNumberCheck #70
    r1 \bar "||"
    s2 \pageBreak | % 71
    \key e \major r1 s2 | % 72
    r1 s2 | % 73
    r1 s2 | % 74
    r1 s2 | % 75
    r1 s2 \break | % 76
    r1 s2 | % 77
    r1 s2 | % 78
    r1 s2 | % 79
    r1 s2 | \barNumberCheck #80
    r1 s2 \pageBreak | % 81
    r1 s2 | % 82
    r1 s2 | % 83
    r1 s2 | % 84
    r1 s2 | % 85
    r1 s2 \pageBreak | % 86
    r1 s2 | % 87
    r1 s2 | % 88
    r1 s2 | % 89
    r1 s2 \pageBreak | \barNumberCheck #90
    r1 s2 | % 91
    r1 s2 | % 92
    r1 s2 | % 93
    r1 s2 | % 94
    r1 s2 | % 95
    r1 s2 \pageBreak | % 96
    r1 s2 | % 97
    r1 s2 | % 98
    r1 s2 | % 99
    r1 s2 | \barNumberCheck #100
    r1 s2 | % 101
    r1 s2 \break | % 102
    r1 s2 | % 103
    r1 s2 | % 104
    r1 s2 | % 105
    r1 s2 | % 106
    r1 s2 \pageBreak | % 107
    r1 s2 | % 108
    r1 s2 | % 109
    r1 s2 | \barNumberCheck #110
    r1 s2 | % 111
    r1 s2 | % 112
    r1 s2 \break | % 113
    r1 s2 | % 114
    r1 s2 | % 115
    r1 s2 | % 116
    r1 s2 | % 117
    r1 s2 \pageBreak | % 118
    r1 s2 | % 119
    r1 r2*2/3 s1*1/6 | \barNumberCheck #120
    r1 r2*2/3 s1*1/6 | % 121
    r1 r2*2/3 s1*1/6 | % 122
    r1 r2*2/3 s1*1/6 \break | % 123
    r1 r2*2/3 s1*1/6 | % 124
    r1 r2*2/3 s1*1/6 | % 125
    r1 r2*2/3 s1*1/6 | % 126
    r1 r2*2/3 s1*1/6 | % 127
    r1 r2*2/3 s1*1/6 \pageBreak | % 128
    r1 r2*2/3 s1*1/6 | % 129
    r1 r2*2/3 s1*1/6 | \barNumberCheck #130
    r1 r2*2/3 s1*1/6 | % 131
    r1 r2*2/3 s1*1/6 \pageBreak | % 132
    r1 s2 | % 133
    r1 s2 | % 134
    r1 s2 | % 135
    r1 s2 \pageBreak | % 136
    \time 4/4 \omit Staff.TimeSignature \stemDown e4 ( -> ^ "div."
    \stemDown d8 r16 \stemDown c16 ) -. \stemDown b8 -. \stemDown g,8
    :16 \stemDown a8 :16 \stemDown b8 :16 | % 137
    \time 12/8  \stemUp <e, c'>8 _\f r8*2/3 r8*2/3 \stemUp <g d'>8 r8*2/3
    r8*2/3 r2.*2/3 s1*5/12 | % 138
    \stemUp <e c'>8 _\mf r8*2/3 r8*2/3 \stemUp <g d'>8 r8*2/3 r8*2/3 r4.*2/3
    r8*2/3 \stemDown e'8 -. _\p \stemDown d8 -. \bar "||"
    s1*1/3 | % 139
    \key g \major \stemUp g,8 -. \stemUp b8 -. \stemUp g8 -. \stemDown
    d'8 -. r8*2/3 r8*2/3 \stemUp a8 -. \stemUp c8 -. \stemUp a8 -.
    \stemDown e'8 -. r8*2/3 r8*2/3 s1*1/6 \pageBreak | \barNumberCheck
    #140
    \stemDown a,8 -. \stemDown d8 -. \stemDown a'8 -. r4.*2/3 r4.*2/3
    \stemDown a4 ( \stemDown d,8 ) s4 | % 141
    r1 s2 | % 142
    \stemUp cis8 ( -> _\p \stemUp d8 \stemUp dis8 \stemUp e8 \stemUp c8
    \stemUp b8 ) r2.*2/3 s4 | % 143
    \stemUp g8 -. _\p \stemUp b8 -. \stemUp g8 -. \stemDown d'8 -. r8*2/3
    r8*2/3 \stemUp a8 -. \stemUp c8 -. \stemUp a8 -. \stemDown e'8 -. r4*2/3
    s1*1/6 | % 144
    \stemDown a,8 -. \stemDown d8 -. \stemDown a'8 -. r4.*2/3 r4.*2/3
    \stemDown a4 ( \stemDown d,8 ) s4 \pageBreak | % 145
    r1 s2 | % 146
    \stemUp ais8 ( ^> _\p \stemUp b8 \stemUp c8 \stemUp b8 \stemUp a8
    \stemUp g8 ) r2.*2/3 s4 | % 147
    r1 s2 | % 148
    r1 s2 | % 149
    r1 s2 \pageBreak | \barNumberCheck #150
    \numericTimeSignature\time 4/4  r2 r4 \stemUp g8 _\mf ^ "pizz."
    \stemUp es8 | % 151
    \stemUp c8 r8 r4 r2 | % 152
    R1*3 \pageBreak | % 155
    R1*2 | % 157
    \time 12/8  r4.*2/3 \stemUp b'8 _\p ^ "pizz." r8*2/3 r8*2/3 r4.*2/3
    \stemUp b8 r8*2/3 r8*2/3 s1*5/12 | % 158
    r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3
    s1*5/12 \break | % 159
    r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3
    s1*5/12 | \barNumberCheck #160
    r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3
    s1*5/12 | % 161
    r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3
    s1*5/12 | % 162
    r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3
    s1*5/12 \pageBreak | % 163
    r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3
    s1*5/12 | % 164
    r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r2.*2/3 s1*11/24 | % 165
    r4.*2/3 \stemUp a8 _\markup{ \small\italic {poco a poco cresc.} }
    \startTrillSpan r8*2/3 r8*2/3 r4.*2/3 \stemUp a8 r8*2/3 r8*2/3
    s1*5/12 | % 166
    r4.*2/3 \stemUp a8 r8*2/3 r8*2/3 r4.*2/3 \stemUp a8 r8*2/3 r8*2/3
    s1*5/12 \pageBreak | % 167
    r4.*2/3 \stemUp a8 r8*2/3 r8*2/3 r4.*2/3 \stemUp a8 r8*2/3 r8*2/3
    s1*5/12 | % 168
    r4.*2/3 \stemUp a8 r8*2/3 r8*2/3 r4.*2/3 \stemUp a8 \stopTrillSpan
    _\f r8*2/3 r8*2/3 s1*5/12 | % 169
    r1 s2 | \barNumberCheck #170
    r1 s2 \pageBreak | % 171
    r2.*2/3 \stemUp gis8 -. _\mf ^ "arco" \stemUp b8 -. \stemUp e8 -.
    \stemDown d8 -. r8*2/3 r8*2/3 s1*1/3 | % 172
    r2.*2/3 \stemUp gis,8 -. _\mp \stemUp b8 -. \stemUp e8 -. \stemDown
    d8 -. r8*2/3 r8*2/3 s1*1/3 | % 173
    r2.*2/3 \stemUp a8 _\p ^ "pizz." r8*2/3 r8*2/3 \stemDown d8 r8*2/3 r8*2/3
    s1*5/12 | % 174
    r1 s2 \pageBreak | % 175
    r1 s2 | % 176
    r1 s2 | % 177
    r1 s2 | % 178
    r2.*2/3 \stemDown b'8 ( -> _\p ^ "arco" \stemDown g8 \stemDown e8
    \stemDown g8 \stemDown d8 \stemDown b8 ) s4 | % 179
    \stemDown d8 -. _\p \stemDown e8 -. \stemDown d8 -. \stemDown fis8
    -. \stemDown eis8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -.
    \pageBreak | \barNumberCheck #180
    \stemDown e8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown a8 -.
    \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown a8 -.
    \stemDown b8 -. \stemDown a8 -. \stemDown b8 -. \stemDown c8 -. | % 181
    \stemDown d,8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 182
    r2.*2/3 \stemDown b'8 ( -> _\p \stemDown g8 \stemDown e8 \stemDown g8
    \stemDown d8 \stemDown b8 ) s4 | % 183
    \stemUp g8 -. _\f \stemUp bes8 -. \stemUp g8 -. \stemUp bes8 -.
    \stemUp es8 -. \stemUp bes8 -. \stemDown es8 -. \stemDown f8 -.
    \stemDown es8 -. \stemDown f8 -. \stemDown as8 -. \stemDown f8 -.
    \pageBreak | % 184
    \stemUp g,8 -. \stemUp bes8 -. \stemUp g8 -. \stemUp bes8 -. \stemUp
    es8 -. \stemUp bes8 -. \stemDown es8 -. \stemDown f8 -. \stemDown es8
    -. \stemDown f8 -. \stemDown g8 -. \stemDown f8 -. | % 185
    \stemDown e8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 186
    \stemUp bes8 ( _\f \stemUp c8 \stemUp d8 ) \stemDown es8 ( \stemDown
    d8 \stemDown c8 \stemUp bes8 ) r8*2/3 r8*2/3 r4.*2/3 s1*5/24 | % 187
    \stemDown c8 -. _\ff \stemDown es8 -. \stemDown c8 -. \stemDown d8
    -. \stemDown f8 -. \stemDown d8 -. \stemDown f8 -. \stemDown bes8 -.
    \stemDown f8 -. \stemDown bes8 -. \stemDown c8 -. \stemDown bes8 -.
    | % 188
    \stemDown c,8 -. \stemDown es8 -. \stemDown c8 -. \stemDown d8 -.
    \stemDown f8 -. \stemDown d8 -. \stemDown f8 -. \stemDown bes8 -.
    \stemDown f8 -. \stemDown bes8 -. \stemDown c8 -. \stemDown bes8 -.
    \pageBreak | % 189
    \stemDown f'8 -. r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 |
    \barNumberCheck #190
    \stemDown d,8 ( _\ff \stemDown es8 \stemDown f8 ) \stemDown g8 (
    \stemDown f8 \stemDown es8 \stemDown d8 ) r8*2/3 r8*2/3 r4.*2/3
    s1*5/24 | % 191
    \stemDown d8 -. _\ff \stemDown g8 -. \stemDown d8 -. \stemDown fis8
    -. \stemDown g8 -. \stemDown fis8 -. \stemDown d8 -. \stemDown g8 -.
    \stemDown d8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown fis8 -.
    | % 192
    \stemDown d8 -. \stemDown g8 -. \stemDown d8 -. \stemDown d8 -.
    \stemDown g8 -. \stemDown d8 -. \stemDown d8 -. \stemDown g8 -.
    \stemDown d8 -. \stemDown d8 -. \stemDown g8 -. \stemDown d8 -. | % 193
    \stemDown g'8 _\ff \stemDown fis8 \stemDown e8 \stemDown d8
    \stemDown cis8 \stemDown b8 \stemDown a8 \stemDown g8 \stemDown fis8
    \stemDown e8 \stemDown d8 \stemDown cis8 \pageBreak | % 194
    \numericTimeSignature\time 4/4  R1*7 \pageBreak | % 201
    R1*5 \pageBreak | % 206
    R1*5 \pageBreak | % 211
    R1*5 \pageBreak | % 216
    R1*5 \pageBreak | % 221
    R1*4 \pageBreak | % 225
    R1*3 \pageBreak | % 228
    R1*5 \pageBreak | % 233
    R1*5 \pageBreak | % 238
    R1*5 \pageBreak | % 243
    R1*5 \pageBreak | % 248
    R1*6 \pageBreak | % 254
    R1*5 \pageBreak | % 259
    R1*5 \pageBreak | % 264
    R1*5 \pageBreak | % 269
    R1*5 \pageBreak | % 274
    R1*7 \pageBreak | % 281
    R1*6 \pageBreak | % 287
    R1*5 \pageBreak | % 292
    R1*5 \pageBreak | % 297
    R1*5 \pageBreak | % 302
    R1*6 \pageBreak | % 308
    R1*6 \pageBreak | % 314
    R1*6 \pageBreak | \barNumberCheck #320
    R1*5 \pageBreak | % 325
    R1*3 \pageBreak | % 328
    R1*4 \pageBreak | % 332
    R1*4 \pageBreak | % 336
    R1*5 \pageBreak | % 341
    R1*7 \bar "|."
    }

PartPTwoFiveVoiceOne =  \relative g {
    \clef "bass" \time 12/8 \key g \major \transposition c | % 1
    r1 s2 | % 2
    r1 s2 | % 3
    r1 s2 | % 4
    \stemDown g2. -> _\p r2.*2/3 s4 \pageBreak | % 5
    r1 _ "Cb." _ "(div.)" s2 | % 6
    r1 s2 | % 7
    r1 \bar "||"
    s2 | % 8
    \stemDown e2. -> _\p r2.*2/3 s4 | % 9
    r1 s2 \pageBreak | \barNumberCheck #10
    r1 _ "Cb." _ "(div.)" s2 | % 11
    r1 s2 | % 12
    r1 s2 | % 13
    c'1. ~ _\mf _\markup{ \small\italic {dim.} } \startTrillSpan | % 14
    \stemDown c2. ~ _\> \stemDown c8 \stopTrillSpan _\! _\p r8*2/3 r8*2/3
    r4.*2/3 s1*5/24 \break | % 15
    c1. ~ _\p _ "Cb." _ "(div.)" | % 16
    \stemDown c2. ~ _\> \stemDown c8 _\! _\pp r8*2/3 r8*2/3 r4.*2/3
    s1*5/24 | % 17
    r1 s2 | % 18
    r1 s2 | % 19
    r2.*2/3 \stemDown b8 _\p ^ "pizz." r8*2/3 r8*2/3 r4.*2/3 s1*11/24
    \pageBreak | \barNumberCheck #20
    \stemDown b8 _\sempre _\p _ "Cb." _ "(div.)" r8*2/3 r8*2/3 r4.*2/3
    \stemDown b8 r8*2/3 r8*2/3 r4.*2/3 s1*5/12 | % 21
    \stemDown b8 r8*2/3 r8*2/3 r4.*2/3 \stemDown b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | % 22
    \stemDown b8 r8*2/3 r8*2/3 r4.*2/3 \stemDown b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | % 23
    \stemDown b8 r8*2/3 r8*2/3 r4.*2/3 \stemDown b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 \break | % 24
    \stemDown b8 _ "Cb." _ "(div.)" r8*2/3 r8*2/3 r4.*2/3 \stemDown b8 r8*2/3
    r8*2/3 r4.*2/3 s1*5/12 | % 25
    \stemDown b8 r8*2/3 r8*2/3 r4.*2/3 \stemDown b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | % 26
    \stemDown b8 r8*2/3 r8*2/3 r4.*2/3 \stemDown b8 r8*2/3 r8*2/3
    \stemDown bes8 r8*2/3 r8*2/3 s4. | % 27
    \stemDown a8 _\markup{ \small\italic {poco a poco cresc.} }
    \startTrillSpan r8*2/3 r8*2/3 r4.*2/3 \stemDown a8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 \pageBreak | % 28
    \stemDown a8 _ "Cb." _ "(div.)" r8*2/3 r8*2/3 r4.*2/3 \stemDown a8 r8*2/3
    r8*2/3 r4.*2/3 s1*5/12 | % 29
    \stemDown a8 r8*2/3 r8*2/3 r4.*2/3 \stemDown a8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | \barNumberCheck #30
    \stemDown a8 r8*2/3 r8*2/3 r4.*2/3 \stemDown a8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 \stopTrillSpan | % 31
    \stemDown a8 _\f r8*2/3 r8*2/3 \stemDown cis8 -. ^ "arco" r8*2/3
    \stemDown cis8 ( \stemDown b8 ) r8*2/3 r8*2/3 \stemDown bes8 -. r4*2/3
    s1*7/24 \pageBreak | % 32
    \stemDown a8 _ "Cb." _ "(div.)" r8*2/3 r8*2/3 \stemDown cis8 -. r8*2/3
    \stemDown cis8 ( \stemDown b8 ) r8*2/3 r8*2/3 \stemDown bes8 -. r8*2/3
    r8*2/3 s1*7/24 | % 33
    \stemDown a8 -. _\markup{ \small\italic {dim.} } \startTrillSpan r8*2/3
    r8*2/3 \stemDown cis8 -. r8*2/3 \stemDown cis8 ( \stemDown b8 ) r8*2/3
    r8*2/3 \stemDown bes8 -. r8*2/3 r8*2/3 s1*7/24 | % 34
    \stemDown a8 -. r8*2/3 r8*2/3 \stemDown cis8 -. r8*2/3 \stemDown cis8
    ( \stemDown b8 ) r8*2/3 r8*2/3 \stemDown bes8 -. r8*2/3 r8*2/3
    s1*7/24 \stopTrillSpan | % 35
    \stemDown a8 -. _\p r8*2/3 r8*2/3 \stemDown d8 ^ "pizz." r8*2/3 r8*2/3
    r2.*2/3 s1*5/12 \pageBreak | % 36
    r1 _ "Cb." _ "(div.)" s2 | % 37
    \stemDown g,8 _\p r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 38
    \stemDown g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 39
    \stemDown g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 |
    \barNumberCheck #40
    \stemDown g8 r8*2/3 r8*2/3 r4.*2/3 \stemDown d'8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 \pageBreak | % 41
    \stemDown g,8 _ "Cb." _ "(div.)" r8*2/3 r8*2/3 r4.*2/3 r2.*2/3
    s1*11/24 | % 42
    \stemDown g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 43
    \stemDown g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 44
    \stemDown g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 45
    g1. ( _\f ^ "arco" \pageBreak | % 46
    r1 ) s2 | % 47
    r1 s2 | % 48
    r1 s2 | % 49
    r1 s2 | \barNumberCheck #50
    r1 s2 \pageBreak | % 51
    r1 s2 | % 52
    r1 s2 | % 53
    r1 s2 | % 54
    r1 s2 | % 55
    r1 s2 \pageBreak | % 56
    r1 s2 | % 57
    r1 s2 | % 58
    r1 s2 | % 59
    r1 s2 | \barNumberCheck #60
    r1 s2 \pageBreak | % 61
    r1 s2 | % 62
    r1 s2 | % 63
    r1 s2 | % 64
    r1 s2 | % 65
    r1 s2 \pageBreak | % 66
    r1 s2 | % 67
    r1 s2 | % 68
    r1 s2 | % 69
    r1 s2 | \barNumberCheck #70
    r1 \bar "||"
    s2 \pageBreak | % 71
    \key e \major r1 s2 | % 72
    r1 s2 | % 73
    r1 s2 | % 74
    r1 s2 | % 75
    r1 s2 \break | % 76
    r1 s2 | % 77
    r1 s2 | % 78
    r1 s2 | % 79
    r1 s2 | \barNumberCheck #80
    r1 s2 \pageBreak | % 81
    r1 s2 | % 82
    r1 s2 | % 83
    r1 s2 | % 84
    r1 s2 | % 85
    r1 s2 \pageBreak | % 86
    r1 s2 | % 87
    r1 s2 | % 88
    r1 s2 | % 89
    r1 s2 \pageBreak | \barNumberCheck #90
    r1 s2 | % 91
    r1 s2 | % 92
    r1 s2 | % 93
    r1 s2 | % 94
    r1 s2 | % 95
    r1 s2 \pageBreak | % 96
    r1 s2 | % 97
    r1 s2 | % 98
    r1 s2 | % 99
    r1 s2 | \barNumberCheck #100
    r1 s2 | % 101
    r1 s2 \break | % 102
    r1 s2 | % 103
    r1 s2 | % 104
    r1 s2 | % 105
    r1 s2 | % 106
    r1 s2 \pageBreak | % 107
    r1 s2 | % 108
    r1 s2 | % 109
    r1 s2 | \barNumberCheck #110
    r1 s2 | % 111
    r1 s2 | % 112
    r1 s2 \break | % 113
    r1 s2 | % 114
    r1 s2 | % 115
    r1 s2 | % 116
    r1 s2 | % 117
    r1 s2 \pageBreak | % 118
    r1 s2 | % 119
    r1 r2*2/3 s1*1/6 | \barNumberCheck #120
    r1 r2*2/3 s1*1/6 | % 121
    r1 r2*2/3 s1*1/6 | % 122
    r1 r2*2/3 s1*1/6 \break | % 123
    r1 r2*2/3 s1*1/6 | % 124
    r1 r2*2/3 s1*1/6 | % 125
    r1 r2*2/3 s1*1/6 | % 126
    r1 r2*2/3 s1*1/6 | % 127
    r1 r2*2/3 s1*1/6 \pageBreak | % 128
    r1 s2 | % 129
    r1 s2 | \barNumberCheck #130
    r1 s2 | % 131
    r1 s2 \pageBreak | % 132
    r1 s2 | % 133
    r1 s2 | % 134
    r1 s2 | % 135
    r1 s2 \pageBreak | % 136
    \time 4/4 \omit Staff.TimeSignature R1*3 \bar "||"
    \key g \major R1 \pageBreak | \barNumberCheck #140
    R1*5 \pageBreak | % 145
    R1*5 \pageBreak | \barNumberCheck #150
    R1 _ "Cb." | % 151
    \time 12/8  c1. ~ _ "(div.)" _\mf _\markup{ \small\italic {dim.} }
    \startTrillSpan | % 152
    \stemDown c2. ~ _\> \stemDown c8 \stopTrillSpan _\! _\p r8*2/3 r8*2/3
    r4.*2/3 s1*5/24 | % 153
    c1. ~ _\p | % 154
    \stemDown c2. ~ _\> \stemDown c8 _\! _\pp r8*2/3 r8*2/3 r4.*2/3
    s1*5/24 \pageBreak | % 155
    r1 _ "Cb." _ "(div.)" s2 | % 156
    r1 s2 | % 157
    r2.*2/3 \stemDown b8 _\p ^ "pizz." r8*2/3 r8*2/3 r4.*2/3 s1*11/24 | % 158
    \stemDown b8 r8*2/3 r8*2/3 r4.*2/3 \stemDown b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 \break | % 159
    \stemDown b8 _ "Cb." _ "(div.)" r8*2/3 r8*2/3 r4.*2/3 \stemDown b8 r8*2/3
    r8*2/3 r4.*2/3 s1*5/12 | \barNumberCheck #160
    \stemDown b8 r8*2/3 r8*2/3 r4.*2/3 \stemDown b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | % 161
    \stemDown b8 r8*2/3 r8*2/3 r4.*2/3 \stemDown b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | % 162
    \stemDown b8 r8*2/3 r8*2/3 r4.*2/3 \stemDown b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 \pageBreak | % 163
    \stemDown b8 _ "Cb." _ "(div.)" r8*2/3 r8*2/3 r4.*2/3 \stemDown b8 r8*2/3
    r8*2/3 r4.*2/3 s1*5/12 | % 164
    \stemDown b8 r8*2/3 r8*2/3 r4.*2/3 \stemDown b8 r8*2/3 r8*2/3
    \stemDown bes8 r8*2/3 r8*2/3 s4. | % 165
    \stemDown a8 _\markup{ \small\italic {poco a poco cresc.} }
    \startTrillSpan r8*2/3 r8*2/3 r4.*2/3 \stemDown a8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | % 166
    \stemDown a8 r8*2/3 r8*2/3 r4.*2/3 \stemDown a8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 \pageBreak | % 167
    \stemDown a8 _ "Cb." _ "(div.)" r8*2/3 r8*2/3 r4.*2/3 \stemDown a8 r8*2/3
    r8*2/3 r4.*2/3 s1*5/12 | % 168
    \stemDown a8 r8*2/3 r8*2/3 r4.*2/3 \stemDown a8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 \stopTrillSpan | % 169
    \stemDown a8 _\f r8*2/3 r8*2/3 \stemDown cis8 -. ^ "arco" r8*2/3
    \stemDown cis8 ( \stemDown b8 ) r8*2/3 r8*2/3 \stemDown bes8 -. r8*2/3
    r8*2/3 s1*7/24 | \barNumberCheck #170
    \stemDown a8 -. r8*2/3 r8*2/3 \stemDown cis8 -. r8*2/3 \stemDown cis8
    ( \stemDown b8 ) r8*2/3 r8*2/3 \stemDown bes8 -. r8*2/3 r8*2/3
    s1*7/24 \pageBreak | % 171
    \stemDown a8 -. _ "Cb." _ "(div.)" _\markup{ \small\italic {dim.} }
    \startTrillSpan r8*2/3 r8*2/3 \stemDown cis8 -. r8*2/3 \stemDown cis8
    ( \stemDown b8 ) r8*2/3 r8*2/3 \stemDown bes8 -. r8*2/3 r8*2/3
    s1*7/24 | % 172
    \stemDown a8 -. r8*2/3 r8*2/3 \stemDown cis8 -. r8*2/3 \stemDown cis8
    ( \stemDown b8 ) r8*2/3 r8*2/3 \stemDown bes8 -. r8*2/3 r8*2/3
    s1*7/24 \stopTrillSpan | % 173
    \stemDown a8 _\p r8*2/3 r8*2/3 \stemDown d8 ^ "pizz." r8*2/3 r8*2/3
    r2.*2/3 s1*5/12 | % 174
    r1 s2 \pageBreak | % 175
    \stemDown g,8 _\p _ "Cb." _ "(div.)" r8*2/3 r8*2/3 r4.*2/3 r2.*2/3
    s1*11/24 | % 176
    \stemDown g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 177
    \stemDown g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 178
    \stemDown g8 r8*2/3 r8*2/3 r4.*2/3 \stemDown d'8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | % 179
    \stemDown g,8 _\p r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 \pageBreak
    | \barNumberCheck #180
    \stemDown g8 _ "Cb." _ "(div.)" r8*2/3 r8*2/3 r4.*2/3 r2.*2/3
    s1*11/24 | % 181
    \stemDown g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 182
    \stemDown g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 183
    g1. ~ _\f ^ "arco" \pageBreak | % 184
    g1. ~ _ "Cb." _ "(div.)" | % 185
    \stemDown g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 186
    r2.*2/3 \stemDown g8 ( _\f \stemDown as8 \stemDown a8 ) \stemDown
    bes8 ( \stemDown as8 \stemDown g8 ) s4 | % 187
    as1. ~ _\ff | % 188
    as1. ~ \pageBreak | % 189
    \stemDown as8 _ "Cb." _ "(div.)" r8*2/3 r8*2/3 r4.*2/3 r2.*2/3
    s1*11/24 | \barNumberCheck #190
    r2.*2/3 \stemDown bes8 ( _\ff \stemDown c8 \stemDown cis8 )
    \stemDown d8 ( \stemDown c8 \stemDown bes8 ) s4 | % 191
    a1. | % 192
    \numericTimeSignature\time 4/4  \stemDown bes2. ( \stemUp bes,4 ) | % 193
    a1 ( _\ff \pageBreak | % 194
    R1*7 \pageBreak | % 201
    R1*5 \pageBreak | % 206
    R1*5 \pageBreak | % 211
    R1*5 \pageBreak | % 216
    R1*5 \pageBreak | % 221
    R1*4 \pageBreak | % 225
    R1*3 \pageBreak | % 228
    R1*5 \pageBreak | % 233
    R1*5 \pageBreak | % 238
    R1*5 \pageBreak | % 243
    R1*5 \pageBreak | % 248
    R1*6 \pageBreak | % 254
    R1*5 \pageBreak | % 259
    R1*5 \pageBreak | % 264
    R1*5 \pageBreak | % 269
    R1*5 \pageBreak | % 274
    R1*7 \pageBreak | % 281
    R1*6 \pageBreak | % 287
    R1*5 \pageBreak | % 292
    R1*5 \pageBreak | % 297
    R1*5 \pageBreak | % 302
    R1*6 \pageBreak | % 308
    R1*6 \pageBreak | % 314
    R1*6 \pageBreak | \barNumberCheck #320
    R1*5 \pageBreak | % 325
    R1*3 \pageBreak | % 328
    R1*4 \pageBreak | % 332
    R1*4 \pageBreak | % 336
    R1*5 \pageBreak | % 341
    R1*7 \bar "|."
    }

PartPTwoSixVoiceOne =  \relative c {
    \clef "bass" \time 12/8 \key g \major \transposition c | % 1
    r1 s2 | % 2
    r1 s2 | % 3
    r1 s2 | % 4
    r1 s2 \pageBreak | % 5
    r1 s2 | % 6
    r1 s2 | % 7
    r1 \bar "||"
    s2 | % 8
    r1 s2 | % 9
    r1 s2 \pageBreak | \barNumberCheck #10
    r1 s2 | % 11
    r1 s2 | % 12
    r1 s2 | % 13
    c1. ~ _\mf _\markup{ \small\italic {dim.} } \startTrillSpan | % 14
    \stemUp c2. ~ _\> \stemUp c8 \stopTrillSpan _\! _\p r8*2/3 r8*2/3 r4.*2/3
    s1*5/24 \break | % 15
    r1 s2 | % 16
    r1 s2 | % 17
    r1 s2 | % 18
    r2.*2/3 r4.*2/3 \stemUp c8 _\p ^ "pizz." r8*2/3 r8*2/3 s1*11/24 | % 19
    \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 \pageBreak | \barNumberCheck #20
    \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | % 21
    \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | % 22
    \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | % 23
    \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 \break | % 24
    \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | % 25
    \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | % 26
    \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 \stemUp
    bes8 r8*2/3 r8*2/3 s4. | % 27
    \stemUp a8 _\markup{ \small\italic {poco a poco cresc.} }
    \startTrillSpan r8*2/3 r8*2/3 r4.*2/3 \stemUp a8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 \pageBreak | % 28
    \stemUp a8 r8*2/3 r8*2/3 r4.*2/3 \stemUp a8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | % 29
    \stemUp a8 r8*2/3 r8*2/3 r4.*2/3 \stemUp a8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | \barNumberCheck #30
    \stemUp a8 r8*2/3 r8*2/3 r4.*2/3 \stemUp a8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 \stopTrillSpan | % 31
    \stemUp a8 _\f r8*2/3 r8*2/3 \stemUp cis8 -. ^ "arco" r8*2/3 \stemUp
    cis8 ( \stemUp b8 ) r8*2/3 r8*2/3 \stemUp bes8 -. r4*2/3 s1*7/24
    \pageBreak | % 32
    \stemUp a8 -. r8*2/3 r8*2/3 \stemUp cis8 -. r8*2/3 \stemUp cis8 (
    \stemUp b8 ) r8*2/3 r8*2/3 \stemUp bes8 -. r8*2/3 r8*2/3 s1*7/24 | % 33
    \stemUp a8 -. _\markup{ \small\italic {dim.} } \startTrillSpan r8*2/3
    r8*2/3 \stemUp cis8 -. r8*2/3 \stemUp cis8 ( \stemUp b8 ) r8*2/3 r8*2/3
    \stemUp bes8 -. r8*2/3 r8*2/3 s1*7/24 | % 34
    \stemUp a8 -. r8*2/3 r8*2/3 \stemUp cis8 -. r8*2/3 \stemUp cis8 (
    \stemUp b8 ) r8*2/3 r8*2/3 \stemUp bes8 -. r8*2/3 r8*2/3 s1*7/24
    \stopTrillSpan | % 35
    \stemUp a8 -. _\p r8*2/3 r8*2/3 \stemDown d8 ^ "pizz." r8*2/3 r8*2/3
    r2.*2/3 s1*5/12 \pageBreak | % 36
    r1 s2 | % 37
    \stemUp g,8 _\p r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 38
    \stemUp g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 39
    \stemUp g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | \barNumberCheck
    #40
    \stemUp g8 r8*2/3 r8*2/3 r4.*2/3 \stemDown g'8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 \pageBreak | % 41
    \stemUp g,8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 42
    \stemUp g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 43
    \stemUp g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 44
    \stemDown g'8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 45
    g1. ( _\f ^ "arco" \pageBreak | % 46
    r1 ) s2 | % 47
    r1 s2 | % 48
    r1 s2 | % 49
    r1 s2 | \barNumberCheck #50
    r1 s2 \pageBreak | % 51
    r1 s2 | % 52
    r1 s2 | % 53
    r1 s2 | % 54
    r1 s2 | % 55
    r1 s2 \pageBreak | % 56
    r1 s2 | % 57
    r1 s2 | % 58
    r1 s2 | % 59
    r1 s2 | \barNumberCheck #60
    r1 s2 \pageBreak | % 61
    r1 s2 | % 62
    r1 s2 | % 63
    r1 s2 | % 64
    r1 s2 | % 65
    r1 s2 \pageBreak | % 66
    r1 s2 | % 67
    r1 s2 | % 68
    r1 s2 | % 69
    r1 s2 | \barNumberCheck #70
    r1 \bar "||"
    s2 \pageBreak | % 71
    \key e \major r1 s2 | % 72
    r1 s2 | % 73
    r1 s2 | % 74
    r1 s2 | % 75
    r1 s2 \break | % 76
    r1 s2 | % 77
    r1 s2 | % 78
    r1 s2 | % 79
    r1 s2 | \barNumberCheck #80
    r1 s2 \pageBreak | % 81
    r1 s2 | % 82
    r1 s2 | % 83
    r1 s2 | % 84
    r1 s2 | % 85
    r1 s2 \pageBreak | % 86
    r1 s2 | % 87
    r1 s2 | % 88
    r1 s2 | % 89
    r1 s2 \pageBreak | \barNumberCheck #90
    r1 s2 | % 91
    r1 s2 | % 92
    r1 s2 | % 93
    r1 s2 | % 94
    r1 s2 | % 95
    r1 s2 \pageBreak | % 96
    r1 s2 | % 97
    r1 s2 | % 98
    r1 s2 | % 99
    r1 s2 | \barNumberCheck #100
    r1 s2 | % 101
    r1 s2 \break | % 102
    r1 s2 | % 103
    r1 s2 | % 104
    r1 s2 | % 105
    r1 s2 | % 106
    r1 s2 \pageBreak | % 107
    r1 s2 | % 108
    r1 s2 | % 109
    r1 s2 | \barNumberCheck #110
    r1 s2 | % 111
    r1 s2 | % 112
    r1 s2 \break | % 113
    r1 s2 | % 114
    r1 s2 | % 115
    r1 s2 | % 116
    r1 s2 | % 117
    r1 s2 \pageBreak | % 118
    r1 s2 | % 119
    r1 r2*2/3 s1*1/6 | \barNumberCheck #120
    r1 r2*2/3 s1*1/6 | % 121
    r1 r2*2/3 s1*1/6 | % 122
    r1 r2*2/3 s1*1/6 \break | % 123
    r1 r2*2/3 s1*1/6 | % 124
    r1 r2*2/3 s1*1/6 | % 125
    r1 r2*2/3 s1*1/6 | % 126
    r1 r2*2/3 s1*1/6 | % 127
    r1 r2*2/3 s1*1/6 \pageBreak | % 128
    r1 r2*2/3 s1*1/6 | % 129
    r1 r2*2/3 s1*1/6 | \barNumberCheck #130
    r1 r2*2/3 s1*1/6 | % 131
    r1 r2*2/3 s1*1/6 \pageBreak | % 132
    r1 s2 | % 133
    r1 s2 | % 134
    r1 s2 | % 135
    r1 s2 \pageBreak | % 136
    \time 4/4 \omit Staff.TimeSignature R1*3 \bar "||"
    \key g \major R1 \pageBreak | \barNumberCheck #140
    R1*5 \pageBreak | % 145
    R1*5 \pageBreak | \barNumberCheck #150
    R1 | % 151
    \time 12/8  c,1. ~ _\mf ^ "div." _\markup{ \small\italic {dim.} }
    \startTrillSpan | % 152
    \stemUp c2. ~ _\> \stemUp c8 \stopTrillSpan _\! _\p r8*2/3 r8*2/3 r4.*2/3
    s1*5/24 | % 153
    r1 s2 | % 154
    r1 s2 \pageBreak | % 155
    r1 s2 | % 156
    r2.*2/3 r4.*2/3 \stemUp c8 _\p ^ "pizz." r8*2/3 r8*2/3 s1*11/24 | % 157
    \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | % 158
    \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 \break | % 159
    \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | \barNumberCheck #160
    \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | % 161
    \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | % 162
    \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 \pageBreak | % 163
    \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | % 164
    \stemUp b8 r8*2/3 r8*2/3 r4.*2/3 \stemUp b8 r8*2/3 r8*2/3 \stemUp
    bes8 r8*2/3 r8*2/3 s4. | % 165
    \stemUp a8 _\markup{ \small\italic {poco a poco cresc.} }
    \startTrillSpan r8*2/3 r8*2/3 r4.*2/3 \stemUp a8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | % 166
    \stemUp a8 r8*2/3 r8*2/3 r4.*2/3 \stemUp a8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 \pageBreak | % 167
    \stemUp a8 r8*2/3 r8*2/3 r4.*2/3 \stemUp a8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | % 168
    \stemUp a8 r8*2/3 r8*2/3 r4.*2/3 \stemUp a8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 \stopTrillSpan | % 169
    \stemUp a8 _\f r8*2/3 r8*2/3 \stemUp cis8 -. ^ "arco" r8*2/3 \stemUp
    cis8 ( \stemUp b8 ) r8*2/3 r8*2/3 \stemUp bes8 -. r8*2/3 r8*2/3
    s1*7/24 | \barNumberCheck #170
    \stemUp a8 -. r8*2/3 r8*2/3 \stemUp cis8 -. r8*2/3 \stemUp cis8 (
    \stemUp b8 ) r8*2/3 r8*2/3 \stemUp bes8 -. r8*2/3 r8*2/3 s1*7/24
    \pageBreak | % 171
    \stemUp a8 -. _\markup{ \small\italic {dim.} } \startTrillSpan r8*2/3
    r8*2/3 \stemUp cis8 -. r8*2/3 \stemUp cis8 ( \stemUp b8 ) r8*2/3 r8*2/3
    \stemUp bes8 -. r8*2/3 r8*2/3 s1*7/24 | % 172
    \stemUp a8 -. r8*2/3 r8*2/3 \stemUp cis8 -. r8*2/3 \stemUp cis8 (
    \stemUp b8 ) r8*2/3 r8*2/3 \stemUp bes8 -. r8*2/3 r8*2/3 s1*7/24
    \stopTrillSpan | % 173
    \stemUp a8 r8*2/3 r8*2/3 \stemDown d8 ^ "pizz." r8*2/3 r8*2/3 r2.*2/3
    s1*5/12 | % 174
    r1 s2 \pageBreak | % 175
    \stemUp g,8 _\p r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 176
    \stemUp g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 177
    \stemUp g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 178
    \stemUp g8 r8*2/3 r8*2/3 r4.*2/3 \stemDown g'8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/12 | % 179
    \stemUp g,8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 \pageBreak |
    \barNumberCheck #180
    \stemUp g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 181
    \stemUp g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 182
    \stemDown g'8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 183
    g,1. ~ _\f ^ "arco" \pageBreak | % 184
    g1. ~ | % 185
    \stemUp g8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 186
    r2.*2/3 \stemUp g8 ( _\f \stemUp as8 \stemUp a8 ) \stemUp bes8 (
    \stemUp as8 \stemUp g8 ) s4 | % 187
    as1. ~ _\ff | % 188
    as1. ~ \pageBreak | % 189
    \stemUp as8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | \barNumberCheck
    #190
    r2.*2/3 \stemUp bes8 ( _\ff \stemUp c8 \stemUp cis8 ) \stemUp d8 (
    \stemUp c8 \stemUp bes8 ) s4 | % 191
    a1. | % 192
    \numericTimeSignature\time 4/4  \stemUp bes2. \stemUp bes4 | % 193
    a1 ( _\ff \pageBreak | % 194
    R1*7 \pageBreak | % 201
    R1*5 \pageBreak | % 206
    R1*5 \pageBreak | % 211
    R1*5 \pageBreak | % 216
    R1*5 \pageBreak | % 221
    R1*4 \pageBreak | % 225
    R1*3 \pageBreak | % 228
    R1*5 \pageBreak | % 233
    R1*5 \pageBreak | % 238
    R1*5 \pageBreak | % 243
    R1*5 \pageBreak | % 248
    R1*6 \pageBreak | % 254
    R1*5 \pageBreak | % 259
    R1*5 \pageBreak | % 264
    R1*5 \pageBreak | % 269
    R1*5 \pageBreak | % 274
    R1*7 \pageBreak | % 281
    R1*6 \pageBreak | % 287
    R1*5 \pageBreak | % 292
    R1*5 \pageBreak | % 297
    R1*5 \pageBreak | % 302
    R1*6 \pageBreak | % 308
    R1*6 \pageBreak | % 314
    R1*6 \pageBreak | \barNumberCheck #320
    R1*5 \pageBreak | % 325
    R1*3 \pageBreak | % 328
    R1*4 \pageBreak | % 332
    R1*4 \pageBreak | % 336
    R1*5 \pageBreak | % 341
    R1*7 \bar "|."
    }

PartPTwoSixVoiceTwo =  \relative c {
    \clef "bass" \time 12/8 \key g \major \transposition c s2*9 | % 4
     \once \override NoteHead.style = ##f c1. \pageBreak s1*4 \bar "||"
    s2 | % 8
     \once \override NoteHead.style = ##f e1. s1. \pageBreak s2*15
    \break s2*15 \pageBreak s1*6 \break s1*6 \pageBreak s1*6 \pageBreak
    s1*6 \pageBreak s2*15 \pageBreak s2*15 \pageBreak s2*15 \pageBreak
    s2*15 \pageBreak s2*15 \pageBreak s2*15 \pageBreak s1*7 \bar "||"
    s2 \pageBreak | % 71
    \key e \major s2*15 \break s2*15 \pageBreak s2*15 \pageBreak s1*6
    \pageBreak s1*9 \pageBreak s1*9 \break s2*15 \pageBreak s1*9 \break
    s2*15 \pageBreak s2*15 \break s2*15 \pageBreak s1*6 \pageBreak s1*6
    \pageBreak | % 136
    \time 4/4 \omit Staff.TimeSignature s1*3 \bar "||"
    \key g \major s1 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1 | % 151
    \time 12/8  s1*6 \pageBreak s1*6 \break s1*6 \pageBreak s1*6
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak s2*15 \pageBreak s1*6
    \pageBreak s2*15 \pageBreak s2*9 | % 192
    \numericTimeSignature\time 4/4  s1*2 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*4
    \pageBreak s1*3 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*6 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*7 \pageBreak s1*6
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*6
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*5 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*5 \pageBreak s1*7 \bar
    "|."
    }

PartPTwoSevenVoiceOne =  \relative b'' {
    \clef "treble" \time 4/4 \key g \major | % 1
    R1*4 \pageBreak | % 5
    R1*2 | % 7
    \numericTimeSignature\time 4/4  R1 \bar "||"
    R1*2 \pageBreak | \barNumberCheck #10
    \numericTimeSignature\time 4/4  R1*2 | % 12
    \numericTimeSignature\time 4/4  R1*3 \break | % 15
    R1*5 \pageBreak | \barNumberCheck #20
    R1*4 \break | % 24
    R1*3 | % 27
    \numericTimeSignature\time 4/4  R1 \pageBreak | % 28
    R1*4 \pageBreak | % 32
    R1*4 \pageBreak | % 36
    \numericTimeSignature\time 4/4  R1 | % 37
    \numericTimeSignature\time 4/4  R1*4 \pageBreak | % 41
    R1*5 \pageBreak | % 46
    R1*5 \pageBreak | % 51
    \time 12/8 \omit Staff.TimeSignature \stemDown b8 -. ^ "unis." r8*2/3
    r8*2/3 r4.*2/3 \stemUp dis,,8 ( ^ "sul G" \stemUp e8 \stemUp fis8 )
    \stemUp gis8 ( \stemUp fis8 \stemUp e8 s1*5/24 | % 52
    \stemUp dis8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 53
    r1 s2 | % 54
    r1 s2 | % 55
    r1 s2 \pageBreak | % 56
    \stemDown cis'8 -. _\mf \stemDown b8 -. \stemDown cis8 -. \stemDown
    b8 -. \stemDown cis8 -. \stemDown b8 -. \stemDown dis8 -. _\f
    \stemDown cis8 -. \stemDown dis8 -. \stemDown cis8 -. \stemDown dis8
    -. \stemDown cis8 -. | % 57
    r1 s2 | % 58
    r1 s2 | % 59
    r1 s2 | \barNumberCheck #60
    \stemDown cis8 -. _\mf _\< \stemDown b8 -. \stemDown cis8 -.
    \stemDown b8 -. \stemDown cis8 -. \stemDown b8 -. \stemDown dis8 -.
    _\! _\f \stemDown cis8 -. \stemDown dis8 -. \stemDown cis8 -.
    \stemDown dis8 -. \stemDown cis8 -. \pageBreak | % 61
    \stemDown e8 -. _\p _\markup{ \small\italic {cresc. poco a poco} }
    \startTrillSpan \stemDown dis8 -. \stemDown e8 -. \stemDown dis8 -.
    \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8 -.
    \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8 -.
    | % 62
    \stemDown d8 -. \stemDown c8 -. \stemDown d8 -. \stemDown c8 -.
    \stemDown d8 -. \stemDown c8 -. \stemDown d8 -. \stemDown c8 -.
    \stemDown d8 -. \stemDown c8 -. \stemDown d8 -. \stemDown c8 -. | % 63
    \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8 -.
    \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8 -.
    \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8 -.
    | % 64
    \stemDown fis8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -.
    | % 65
    \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown fis8 -.
    \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown fis8 -.
    \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown fis8 -.
    \pageBreak | % 66
    \stemDown b8 -. \stemDown a8 -. \stemDown b8 -. \stemDown a8 -.
    \stemDown b8 -. \stemDown a8 -. \stemDown b8 -. \stemDown a8 -.
    \stemDown b8 -. \stemDown a8 -. \stemDown b8 -. \stemDown a8 -. | % 67
    \stemDown c8 -. \stopTrillSpan _\f _\< \stemDown b8 -. \stemDown c8
    -. \stemDown b8 -. \stemDown c8 -. \stemDown b8 -. \stemDown c8 -.
    \stemDown b8 -. \stemDown c8 -. \stemDown b8 -. \stemDown c8 -.
    \stemDown b8 -. | % 68
    \stemDown fis'8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -.
    | % 69
    \stemDown b'8 -> _\! _\ff r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 |
    \barNumberCheck #70
    r1 \bar "||"
    s2 \pageBreak | % 71
    \key e \major r1 s2 | % 72
    r1 s2 | % 73
    r1 s2 | % 74
    r1 s2 | % 75
    r1 s2 \break | % 76
    r1 s2 | % 77
    \numericTimeSignature\time 4/4  r2 \stemUp e,,,8 :16 _\p \stemUp fis8
    :16 \stemUp gis8 :16 \stemUp a8 :16 | % 78
    \stemUp a8 r8 r4 r2 | % 79
    r2 r4 \stemUp gis8 _\mf r8 | \barNumberCheck #80
    \stemDown cis4 ~ _\< \stemDown cis8 \stemDown cis16 \stemDown cis16
    \stemDown dis8 _\! _\f \stemDown dis8 r4 \pageBreak | % 81
    \stemUp e,8 _\pp -\markup{ \italic {leggieramente} } r8 \stemUp b8 (
    -. r16 \stemUp b16 ) -. \stemUp e8 -. r8 \stemUp b8 -. r8 | % 82
    \stemUp e8 -. \stemUp a8 ~ ^> \stemUp a2 \stemUp gis8 ( -. r16
    \stemUp fis16 ) -. | % 83
    \stemDown b8 -. _\markup{ \small\italic {un poco cresc.} }
    \startTrillSpan r8 \acciaccatura { \stemUp fis8 ( } \stemUp e8 r16
    \stemUp dis16 ) -. \stemUp e8 -. r8 \stemUp b8 -. r8 | % 84
    \stemUp e2. -> \stemUp gis8 ( -. r16 \stemUp b16 ) -. | % 85
    \stemDown cis8 -. r8 \acciaccatura { \stemUp fis,8 ( } \stemUp e8 r16
    \stemUp dis16 ) -. \stemUp e8 -. r8 \stemUp b8 -. r8 \pageBreak | % 86
    \stemUp e2 ~ -. -> \stemUp e8 r8 \stemUp gis8 ( -. \stopTrillSpan
    _\mf r16 \stemUp b16 ) -. | % 87
    \stemDown c4 ( -> _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp b8 r16 \stemUp a16 ) -. \stemUp g8 -. r8 \stemDown d'8 ( -.
    r16 \stemDown dis16 ) -. | % 88
    \stemDown e4 ( -> \stemDown d8 r16 \stemDown c16 ) -. \stemDown b8
    -. r8 \stemDown e8 ( -. \stopTrillSpan r16 \stemDown fis16 ) -. | % 89
    \stemDown gis2. -> \stemDown fis8 ( -. r16 \stemDown gis,16 ) -.
    \pageBreak | \barNumberCheck #90
    \stemDown e'2. -> \stemDown dis8 ( -. r16 \stemDown gis,16 ) -. | % 91
    \stemDown cis4 ( -> _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemUp b8 r16 \stemUp cis,16 ) \stemUp a'4 ( ^>
    \stemUp gis8 r16 \stemUp cis,16 ) | % 92
    \stemUp fis4 ( ^> \stemUp e8 r16 \stemUp g,16 ) \stemUp cis4 ( ^>
    \stemUp b8 r16 \stemUp gis16 ) | % 93
    \stemUp a8 \stopTrillSpan _\ff r8 r4 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 }
    | % 94
    \stemUp c2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 }
    | % 95
    \stemUp b2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp bes8 \stemUp bes8 \stemUp bes8 }
    \pageBreak | % 96
    \stemUp bes8 r8 \stemUp b8 r8 \stemUp <e b' e>8 r8 \stemUp b16 (
    _\ff ^ "sul G" \stemUp cis16 \stemUp dis16 \stemUp e16 ) | % 97
    \stemUp fis2 \downbow \stemUp fisis2 \downbow | % 98
    \stemUp gis8 \downbow r8 \stemUp a8 \downbow r8 r2 | % 99
    R1 | \barNumberCheck #100
    r2 r4 \stemUp b,16 ( _\ff ^ "sul G" \stemUp cis16 \stemUp dis16
    \stemUp e16 ) | % 101
    \stemUp fis2 \downbow \stemUp fisis2 \downbow \break | % 102
    \stemUp gis8 \downbow r8 \stemUp a8 \downbow r8 r2 | % 103
    R1 | % 104
    r2 r4 \once \omit TupletBracket
    \times 4/6  {
        \stemUp gis,16 ( _\ff ^ "sul G" \stemUp ais16 \stemUp bis16
        \stemUp cis16 \stemUp dis16 \stemUp e16 ) }
    | % 105
    \stemUp fis2 \downbow \stemUp fisis2 \downbow | % 106
    \stemUp gis8 r8 \stemUp a8 r8 r2 \pageBreak | % 107
    R1 | % 108
    r2 r4 \stemUp b,16 ( _\ff ^ "sul G" \stemUp cis16 \stemUp dis16
    \stemUp e16 ) | % 109
    \stemUp fis2 \downbow \stemUp fisis2 \downbow | \barNumberCheck #110
    \stemUp gis2 \downbow \stemUp <e a>2 \downbow | % 111
    \stemUp <fis ais>8 \downbow r8 \stemUp <e b'>8 \downbow r8 \stemUp
    <fis bis>8 \downbow r8 \stemUp <e cis'>8 \downbow r8 | % 112
    \stemUp <fis d'>8 \downbow r8 \stemUp <fis dis'>8 \downbow r8 r2
    \break | % 113
    R1*5 \pageBreak | % 118
    R1 | % 119
    r2 \stemUp e8 :16 _\p \stemUp fis8 :16 \stemUp gis8 :16 \stemUp a8
    :16 | \barNumberCheck #120
    \stemUp a8 r8 r4 r2 | % 121
    r2 r4 \stemUp gis8 _\mf r8 | % 122
    \stemDown cis4 ~ _\< \stemDown cis8 \stemDown cis16 \stemDown cis16
    \stemDown dis8 _\! _\f \stemDown dis8 r4 \break | % 123
    \stemUp e,8 _\pp r8 \stemUp b8 ( -. r16 \stemUp b16 ) -. \stemUp e8
    -. r8 \stemUp b8 -. r8 | % 124
    \stemUp e8 -. \stemUp a8 ~ ^> \stemUp a2 \stemUp gis8 ( -. r16
    \stemUp fis16 ) -. | % 125
    \stemDown b8 -. _\markup{ \small\italic {un poco cresc.} }
    \startTrillSpan r8 \acciaccatura { \stemUp fis8 ( } \stemUp e8 r16
    \stemUp dis16 ) -. \stemUp e8 -. r8 \stemUp b8 -. r8 | % 126
    \stemUp e2. -> \stemUp gis8 ( -. r16 \stemUp b16 ) -. | % 127
    \stemDown cis8 -. r8 \acciaccatura { \stemUp fis,8 ( } \stemUp e8 r16
    \stemUp dis16 ) -. \stemUp e8 -. r8 \stemUp b8 -. r8 \pageBreak | % 128
    \stemUp e2 ~ -. -> \stemUp e8 r8 \stemUp gis8 ( -. \stopTrillSpan
    _\f r16 \stemUp b16 ) -. | % 129
    \stemDown c4 ( -> \stemUp b8 r16 \stemUp a16 ) -. \stemUp g8 -. r8
    \stemDown d'8 ( -. r16 \stemDown dis16 ) -. | \barNumberCheck #130
    \stemDown e4 ( -> \stemDown d8 r16 \stemDown c16 ) -. \stemUp b8 -.
    \stemUp g16 \stemUp g16 \stemUp a16 \stemUp a16 \stemUp b16 \stemUp
    b16 | % 131
    \stemDown c8 :16 \stemDown d8 :16 \stemDown e8 :16 \stemDown fis8
    :16 \stemDown g8 :16 \stemDown a8 :16 \stemDown ais8 :16 \stemDown b8
    :16 \pageBreak | % 132
    \stemDown c8 :16 \stemDown d8 :16 \stemDown e8 :16 \stemDown fis8
    :16 \stemDown g8 r8 r4 | % 133
    \stemDown c,,4 ( -> \stemUp b8 r16 \stemUp a16 ) -. \stemUp g8 -. r8
    \stemDown d'8 ( -. r16 \stemDown dis16 ) -. | % 134
    \stemDown e4 ( -> \stemDown d8 r16 \stemDown c16 ) -. \stemDown b8
    -. \stemUp g16 \stemUp g16 \stemUp a16 \stemUp a16 \stemUp b16
    \stemUp b16 | % 135
    \stemDown c8 :16 \stemDown d8 :16 \stemDown e8 :16 \stemDown fis8
    :16 \stemDown g8 :16 \stemDown a8 :16 \stemDown ais8 :16 \stemDown b8
    :16 \pageBreak | % 136
    R1*3 \bar "||"
    \key g \major R1 \pageBreak | \barNumberCheck #140
    R1*5 \pageBreak | % 145
    R1*5 \pageBreak | \barNumberCheck #150
    R1*5 \pageBreak | % 155
    R1*4 \break | % 159
    R1*4 \pageBreak | % 163
    R1*4 \pageBreak | % 167
    R1*4 \pageBreak | % 171
    R1*4 \pageBreak | % 175
    R1*5 \pageBreak | \barNumberCheck #180
    R1*4 \pageBreak | % 184
    R1*5 \pageBreak | % 189
    R1*5 \pageBreak | % 194
    \numericTimeSignature\time 4/4  \stemUp b,16 ^ "unis." \stemUp a16
    \stemUp g16 \stemUp fis16 \stemUp e16 \stemUp d16 \stemUp cis16
    \stemUp b16 \stemUp a8 r8 r4 | % 195
    R1*6 \pageBreak | % 201
    R1 | % 202
    \stemUp d2 :16 _\p \stemUp dis2 :16 | % 203
    \stemUp e2 :16 \stemUp eis2 :16 _\< | % 204
    \stemUp fis2 :16 \stemUp g2 :16 | % 205
    \stemUp a8 _\! _\mp r8 r4 r2 \pageBreak | % 206
    \stemUp e8 _\mp r8 \stemUp b8 ( -. r16 \stemUp b16 ) -. \stemUp e8 r8
    \stemUp b8 r8 | % 207
    \stemUp e8 -> \stemUp a8 -> r4 r2 | % 208
    \stemDown g'8 _\mf r8 \stemDown d8 ( -. r16 \stemDown d16 ) -.
    \stemDown g8 r8 \stemDown d8 r8 | % 209
    \stemDown a'8 -> \stemDown c8 -> r4 r2 | \barNumberCheck #210
    \stemDown e,8 _\f r8 \stemDown b8 ( -. r16 \stemDown b16 ) -.
    \stemDown e8 r8 \stemDown b8 r8 \pageBreak | % 211
    \stemDown e8 -> \stemDown a8 -> r4 r2 | % 212
    \stemDown <g g'>8 _\ff r8 \stemUp d'8 ( -. ^ "div." r16 \stemUp d16
    ) -. \stemUp g8 r8 \stemUp d8 r8 | % 213
    \stemUp a'8 -> \stemUp d,8 -> r4 r2 | % 214
    \stemDown <a, a'>8 _\fff ^ "unis." r8 \stemDown <c e>8 ( -. r16
    \stemDown <c e>16 ) -. \stemDown <a a'>8 r8 \stemDown <c e>8 r8 | % 215
    \stemDown <c a'>8 -> \stemDown d'8 ~ -> \stemDown d2. \pageBreak | % 216
    \stemDown <a, a'>8 r8 \stemDown <c e>8 ( -. r16 \stemDown <c e>16 )
    -. \stemDown <a a'>8 r8 \stemDown <c e>8 r8 | % 217
    \stemDown <c a'>8 -> \stemDown d'8 ~ -> \stemDown d8 \stemDown d8 (
    -. \stemDown <a, a'>8 ) -. \stemDown <c e>4 \stemDown <c e>8 ( -. | % 218
    \stemDown <c a'>8 ) -. \stemDown d'4 \stemDown d8 ( -. \stemDown <a,
        a'>8 ) -. \stemDown <c e>4 \stemDown <c e>8 | % 219
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <c a'>8 \stemDown <c a'>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a d'>8 \stemDown <a d'>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <c a'>8 \stemDown <c a'>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <c e>8 \stemDown <c e>8 r8 }
    | \barNumberCheck #220
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <c a'>8 \stemDown <c a'>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a d'>8 \stemDown <a d'>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <c a'>8 \stemDown <c a'>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <c e>8 \stemDown <c e>8 r8 }
    \pageBreak | % 221
    \times 2/3  {
        \stemDown <c a'>8 -> \stemDown <c a'>8 -> r8 }
    \stemDown d32 ( _\sempre _\fff \stemDown e32 \stemDown fis32
    \stemDown g32 \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32
    ) \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16 )
    \stemDown a16 ( \stemDown g16 \stemDown fis16 \stemDown e16 ) | % 222
    \stemDown d16 ( \stemDown c16 \stemDown b16 \stemDown a16 ) \stemUp
    g16 ( \stemUp fis16 \stemUp e16 \stemUp d16 ) r2 | % 223
    r4 \stemDown d'32 ( \stemDown e32 \stemDown fis32 \stemDown g32
    \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32 ) \stemDown
    e16 ( \stemDown d16 \stemDown c16 \stemDown b16 ) \stemDown a16 (
    \stemDown g16 \stemDown fis16 \stemDown e16 ) | % 224
    \stemDown d16 ( \stemDown c16 \stemDown b16 \stemDown a16 ) \stemUp
    g16 ( \stemUp fis16 \stemUp e16 \stemUp d16 ) r2 \pageBreak | % 225
    r4 \stemDown d'32 ( \stemDown e32 \stemDown fis32 \stemDown g32
    \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32 ) \once
    \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemDown fis8 ) r8 | % 226
    r4 \stemDown d32 ( \stemDown e32 \stemDown fis32 \stemDown g32
    \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32 ) \once
    \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemDown fis8 ) r8 | % 227
    r4 \stemDown d32 ( \stemDown e32 \stemDown fis32 \stemDown g32
    \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32 ) \once
    \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemDown fis8 ) r8 \pageBreak | % 228
    r4 \once \omit TupletBracket
    \times 4/5  {
        \stemDown a16 ( \stemDown g16 \stemDown fis16 \stemDown e16
        \stemDown d16 }
    \stemDown c8 ) r8 r4 | % 229
    \stemDown <d, d' g>8 _\fff r8 \stemDown d'8 ( -. r16 \stemDown d16 )
    -. \stemDown g8 r8 \stemDown d8 r8 | \barNumberCheck #230
    \stemDown g8 -> \stemDown c8 ~ ^> \stemDown c2 \stemDown b8 ( -. r16
    \stemDown a16 ) -. | % 231
    \stemDown d8 r8 \acciaccatura { \stemUp a8 ( } \stemDown g8 ) ( -. r16
    \stemDown fis16 ) -. \stemDown g8 -. r8 \stemDown d8 r8 | % 232
    \stemDown g2. -> \stemDown b8 ( -. r16 \stemDown d16 ) -. \pageBreak
    | % 233
    \stemDown e8 r8 \acciaccatura { \stemUp a,8 ( } \stemDown g8 ) -. r16
    \stemDown fis16 -. \stemDown g8 r8 \stemDown d8 r8 | % 234
    \stemDown g2. -> \stemDown b8 ( -. r16 \stemDown d16 ) -. | % 235
    \stemDown g4 ( -> \stemDown fis8 ) r16 \stemDown g16 -. \stemDown e4
    ( -> \stemDown dis8 ) r16 \stemDown e16 -. | % 236
    \stemDown c4 ( -> \stemDown b8 ) r16 \stemDown c16 -. \stemDown a4 (
    -> \stemDown g8 ) r16 \stemDown a16 -. | % 237
    \stemDown e8 -. r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown b16
    ( \stemDown e8 ) r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown
    a16 ( \pageBreak | % 238
    \stemDown b2 ) ~ -> \stemDown b8 \stemDown a16 ( \stemDown g16 \once
    \omit TupletBracket
    \times 4/6  {
        \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown c16
        \stemDown b16 \stemDown a16 }
    | % 239
    \stemDown g8 ) r8 \stemDown d8 ( -. r16 \stemDown d16 ) -. \stemDown
    g8 r8 \stemDown d8 r8 | \barNumberCheck #240
    \stemDown g8 -> \stemDown c8 ~ ^> \stemDown c2 \stemDown b8 ( -. r16
    \stemDown a16 ) -. | % 241
    \stemDown d8 r8 \acciaccatura { \stemUp a8 ( } \stemDown g8 ) ( -. r16
    \stemDown fis16 ) -. \stemDown g8 -. r8 \stemDown d8 r8 | % 242
    \stemDown g2. -> \stemDown b8 ( -. r16 \stemDown d16 ) -. \pageBreak
    | % 243
    \stemDown e8 r8 \acciaccatura { \stemUp a,8 ( } \stemDown g8 ) -. r16
    \stemDown fis16 -. \stemDown g8 r8 \stemDown d8 r8 | % 244
    \stemDown g2. -> \stemDown b8 ( -. r16 \stemDown d16 ) -. | % 245
    \stemDown es4 ( -> \stemDown d8 ) r16 \stemDown c16 -. \stemDown bes8
    -. r8 \stemDown f'8 ( -. r16 \stemDown fis16 ) -. | % 246
    \stemDown g4 ( -> \stemDown f8 ) r16 \stemDown es16 -. \stemDown d8
    -. r8 \stemDown g8 ( -. r16 \stemDown a16 ) -. | % 247
    \stemDown b2. -> \stemDown a8 ( r16 \stemDown b,16 ) -. \pageBreak | % 248
    \stemDown g'2. -> \stemDown fis8 ( r16 \stemDown b,16 ) -. | % 249
    \stemDown e4 ( -> \stemDown d8 ) r16 \stemDown e,16 -. \stemDown c'4
    ( -> \stemDown b8 ) r16 \stemDown e,16 -. | \barNumberCheck #250
    \stemDown a4 ( -> \stemDown g8 ) r16 \stemDown g,16 -. \stemDown e'4
    ( -> \stemDown d8 ) r16 \stemDown gis,16 -. | % 251
    \stemDown c8 r8 r4 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp es,8 \stemUp es8 \stemUp es8 }
    | % 252
    \stemUp es2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp d8 \stemUp d8 \stemUp d8 }
    | % 253
    \stemUp d2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis8 \stemUp cis8 \stemUp cis8 }
    \pageBreak | % 254
    \stemUp cis8 r8 \stemUp d8 r8 \stemUp <g, d' b' g'>8 r8 \stemUp d'16
    ( \downbow _\fff \stemUp e16 \stemUp fis16 \stemUp g16 | % 255
    \stemUp a8 ) r8 r4 \stemUp fis8 \downbow r8 r4 | % 256
    \stemUp fis8 \downbow r8 \stemUp g8 \downbow r8 r4 \stemDown d''16 (
    _\ff \stemDown e16 \stemDown d16 \stemDown e16 | % 257
    \stemDown b8 ) r8 \stemDown fis16 ( \stemDown g16 \stemDown fis16
    \stemDown g16 \stemDown e8 ) r8 \stemUp ais,16 ( \stemUp b16 \stemUp
    ais16 \stemUp b16 ) | % 258
    \stemDown c16 ( \stemDown d16 \stemDown c16 \stemDown b16 ) \stemUp
    a16 ( \stemUp b16 \stemUp a16 \stemUp g16 ) \stemUp fis16 ( \stemUp
    g16 \stemUp e16 \stemUp fis16 ) \stemUp d16 ( \downbow _\fff \stemUp
    e16 \stemUp fis16 \stemUp g16 \pageBreak | % 259
    \stemUp a8 ) r8 r4 \stemUp fis8 \downbow r8 r4 | \barNumberCheck
    #260
    \stemUp fis8 \downbow r8 \stemUp g8 \downbow r8 r4 \stemDown b'16 (
    _\ff \stemDown c16 \stemDown b16 \stemDown c16 | % 261
    \stemDown g8 ) r8 \stemDown dis16 ( \stemDown e16 \stemDown dis16
    \stemDown e16 \stemDown c8 ) r8 \stemUp g16 ( \stemUp gis16 \stemUp
    g16 \stemUp gis16 ) | % 262
    \stemUp a16 ( \stemUp b16 \stemUp a16 \stemUp g16 ) \stemUp fis16 (
    \stemUp g16 \stemUp fis16 \stemUp e16 ) \stemUp d16 ( \stemUp e16
    \stemUp c16 \stemUp d16 \stemUp b8 ) r8 | % 263
    \stemUp <d fis a>8 \downbow _\fff r8 r4 \stemUp <c e ais>8 \downbow
    r8 r4 \pageBreak | % 264
    \stemUp <b dis b'>8 \downbow r8 \stemUp <a e' c'>8 \downbow r8 r4
    \stemDown d''16 ( _\ff \stemDown e16 \stemDown d16 \stemDown e16 | % 265
    \stemDown b8 ) r8 \stemDown fis16 ( \stemDown g16 \stemDown fis16
    \stemDown g16 \stemDown e8 ) r8 \stemUp ais,16 ( \stemUp b16 \stemUp
    ais16 \stemUp b16 ) | % 266
    \stemDown c16 ( \stemDown d16 \stemDown c16 \stemDown b16 ) \stemUp
    a16 ( \stemUp b16 \stemUp a16 \stemUp g16 ) \stemUp fis16 ( \stemUp
    g16 \stemUp e16 \stemUp fis16 ) \stemUp d16 ( \downbow \stemUp e16
    \stemUp fis16 \stemUp g16 | % 267
    \stemUp a8 ) r8 \once \omit TupletBracket
    \times 4/5  {
        \stemUp d,16 ( _\fff \stemUp e16 \stemUp fis16 \stemUp g16
        \stemUp a16 }
    \stemDown bes8 ) r8 \once \omit TupletBracket
    \times 4/5  {
        \stemUp d,16 ( \stemUp e16 \stemUp fis16 \stemUp g16 \stemUp a16
        }
    | % 268
    \stemDown b8 ) r8 \stemUp fis16 ( \stemUp g16 \stemUp a16 \stemUp b16
    \stemDown c8 ) r8 \stemUp g16 ( \stemUp a16 \stemUp bes16 \stemUp c16
    \pageBreak | % 269
    \stemDown cis8 ) r8 \stemDown as16 ( \stemDown bes16 \stemDown b16
    \stemDown cis16 \stemDown d8 ) r8 \stemDown b16 ( \stemDown c16
    \stemDown cis16 \stemDown d16 | \barNumberCheck #270
    \stemDown dis8 ) r8 \stemDown b16 ( \stemDown cis16 \stemDown d16
    \stemDown dis16 \stemDown e8 ) r8 \stemDown b16 ( \stemDown cis16
    \stemDown dis16 \stemDown e16 | % 271
    \stemDown f8 ) r8 \stemDown c16 ( \stemDown d16 \stemDown e16
    \stemDown f16 \stemDown fis8 ) r8 \stemDown d16 ( \stemDown es16
    \stemDown e16 \stemDown fis16 | % 272
    \stemDown g8 ) r8 \stemDown es16 ( \stemDown f16 \stemDown fis16
    \stemDown g16 \stemDown gis8 ) r8 \stemDown e16 ( \stemDown eis16
    \stemDown fis16 \stemDown gis16 ) | % 273
    \stemDown a4 :16 \stemDown bes4 :16 \stemDown b4 :16 \stemDown c4
    :16 \pageBreak | % 274
    \stemDown cis4 :16 \stemDown d4 :16 \stemDown e8 r8 r4 | % 275
    R1*6 \pageBreak | % 281
    R1 | % 282
    r2 r4 \stemDown d,16 ( _\fff \stemDown dis16 \stemDown e16 \stemDown
    fis16 | % 283
    \stemDown g8 ) r8 \stemDown d8 ( -. r16 \stemDown d16 ) -. \stemDown
    g8 r8 \stemDown d8 r8 | % 284
    \stemDown g8 -> \stemDown c8 ~ ^> \stemDown c2 \stemDown b8 ( -. r16
    \stemDown a16 ) -. | % 285
    \stemDown d8 r8 \acciaccatura { \stemUp a8 ( } \stemDown g8 ) ( -. r16
    \stemDown fis16 ) -. \stemDown g8 -. r8 \stemDown d8 r8 | % 286
    \stemDown g2. -> \stemDown b8 ( -. r16 \stemDown d16 ) -. \pageBreak
    | % 287
    \stemDown e8 r8 \acciaccatura { \stemUp a,8 ( } \stemDown g8 ) -. r16
    \stemDown fis16 -. \stemDown g8 r8 \stemDown d8 r8 | % 288
    \stemDown g2. -> \stemDown b8 ( -. r16 \stemDown d16 ) -. | % 289
    \stemDown g4 ( -> \stemDown fis8 ) r16 \stemDown g16 -. \stemDown e4
    ( -> \stemDown dis8 ) r16 \stemDown e16 -. | \barNumberCheck #290
    \stemDown c4 ( -> \stemDown b8 ) r16 \stemDown c16 -. \stemDown a4 (
    -> \stemDown g8 ) r16 \stemDown a16 -. | % 291
    \stemDown e8 -. r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown b16
    ( \stemDown e8 ) r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown
    a16 ( \pageBreak | % 292
    \stemDown b2 ) ~ -> \stemDown b8 \stemDown a16 ( \stemDown g16 \once
    \omit TupletBracket
    \times 4/6  {
        \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown c16
        \stemDown b16 \stemDown a16 }
    | % 293
    \stemDown g8 ) r8 \stemDown d8 ( -. r16 \stemDown d16 ) -. \stemDown
    g8 r8 \stemDown d8 r8 | % 294
    \stemDown g8 -> \stemDown c8 ~ ^> \stemDown c2 \stemDown b8 ( -. r16
    \stemDown a16 ) -. | % 295
    \stemDown d8 r8 \acciaccatura { \stemUp a8 ( } \stemDown g8 ) ( -. r16
    \stemDown fis16 ) -. \stemDown g8 -. r8 \stemDown d8 r8 | % 296
    \stemDown g2. -> \stemDown b8 ( -. r16 \stemDown d16 ) -. \pageBreak
    | % 297
    \stemDown e8 r8 \acciaccatura { \stemUp a,8 ( } \stemDown g8 ) -. r16
    \stemDown fis16 -. \stemDown g8 r8 \stemDown d8 r8 | % 298
    \stemDown g2. -> \stemDown b8 ( -. r16 \stemDown d16 ) -. | % 299
    \stemDown es4 ( -> \stemDown d8 ) r16 \stemDown c16 -. \stemDown bes8
    -. r8 \stemDown f'8 ( -. r16 \stemDown fis16 ) -. | \barNumberCheck
    #300
    \stemDown g4 ( -> \stemDown f8 ) r16 \stemDown es16 -. \stemDown d8
    -. r8 \stemDown g8 ( -. r16 \stemDown a16 ) -. | % 301
    \stemDown b2. -> \stemDown a8 ( r16 \stemDown b,16 ) -. \pageBreak | % 302
    \stemDown g'2. -> \stemDown fis8 ( r16 \stemDown b,16 ) -. | % 303
    \stemDown e4 ( -> \stemDown d8 ) r16 \stemDown e,16 -. \stemDown c'4
    ( -> \stemDown b8 ) r16 \stemDown e,16 -. | % 304
    \stemDown a4 ( -> _\sempre _\fff \stemDown g8 ) r16 \stemDown e16 -.
    \stemDown a4 ( -> \stemDown g8 ) r16 \stemDown es16 -. | % 305
    \stemDown a4 ( -> \stemDown g8 ) r16 \stemDown d16 -. \stemDown a'4
    ( -> \stemDown g8 ) r16 \stemDown cis,16 -. | % 306
    \stemDown a'4 ( -> \stemDown g8 ) r16 \stemDown c,16 -. \stemDown a'4
    ( -> \stemDown g8 ) r16 \stemDown cis,16 -. | % 307
    \stemDown a'4 ( -> \stemDown g8 ) r16 \stemDown d16 -. \stemDown a'4
    ( -> \stemDown g8 ) r16 \stemDown dis16 -. \pageBreak | % 308
    \stemDown b'4 ( -> \stemDown a8 ) r16 \stemDown e16 -. \stemDown c'4
    ( -> \stemDown b8 ) r16 \stemDown e,16 -. | % 309
    \stemDown d'4 ( -> \stemDown c8 ) r16 \stemDown a16 -. \stemDown d4
    ( -> \stemDown cis8 ) r16 \stemDown a16 -. | \barNumberCheck #310
    \stemDown e'4 ( -> \stemDown d8 ) r16 \stemDown a16 -. \stemDown e'4
    ( -> \stemDown dis8 ) r16 \stemDown a16 -. | % 311
    \stemDown f'4 ( -> \stemDown e8 ) r16 \stemDown a,16 -. \stemDown g'4
    ( -> \stemDown fis8 ) r16 \stemDown c16 -. | % 312
    \stemDown a'8 :16 _\ffff \stemDown g8 :16 \stemDown d8 :16 \stemDown
    g8 :16 \stemDown a8 :16 \stemDown g8 :16 \stemDown es8 :16 \stemDown
    g8 :16 | % 313
    \stemDown a8 :16 \stemDown g8 :16 \stemDown e8 :16 \stemDown g8 :16
    \stemDown a8 :16 \stemDown g8 :16 \stemDown es8 :16 \stemDown g8 :16
    \pageBreak | % 314
    \stemDown a8 :16 \stemDown g8 :16 \stemDown fis8 :16 \stemDown e8
    :16 \stemDown d8 :16 \stemDown cis8 :16 \stemDown c8 :16 \stemDown b8
    :16 | % 315
    \stemDown a8 :16 \stemDown g8 :16 \stemDown fis8 :16 \stemDown e8
    :16 \stemDown d8 r8 r4 | % 316
    R1*2 | % 318
    \stemUp b,4 :16 _\mf _\< \stemUp c4 :16 \stemUp d4 :16 \stemUp dis4
    :16 | % 319
    \stemUp e4 :16 \stemUp fis4 :16 \stemUp g4 :16 \stemUp a4 :16
    \pageBreak | \barNumberCheck #320
    \stemDown b4 :16 _\! _\f _\< \stemDown c4 :16 \stemDown d4 :16
    \stemDown dis4 :16 | % 321
    \stemDown e4 :16 \stemDown fis4 :16 \stemDown g4 :16 \stemDown a4
    :16 | % 322
    \stemDown <g b>4 :16 _\! _\ff ^ "div." _\< \stemDown <a c>4 :16
    \stemDown <b d>4 :16 \stemDown <b dis>4 :16 | % 323
    \stemDown <c e>4 :16 \stemDown <d fis>4 :16 \stemDown <e g>4 :16
    \stemDown <fis a>4 :16 | % 324
    \stemDown <dis b'>8 _\! _\fff r8 \once \omit TupletBracket
    \times 4/7  {
        \stemDown g,16*161/160 ( \stemDown a16*161/160 \stemDown b16*161/160
        \stemDown cis16*161/160 \stemDown dis16*161/160 \stemDown e16*161/160
        \stemDown fis16*161/160 }
    \stemDown g8 ) r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown
    dis16 ( \pageBreak | % 325
    \stemDown e8 ) r8 \once \omit TupletBracket
    \times 4/7  {
        \stemDown c,16*161/160 ( \stemDown d16*161/160 \stemDown e16*161/160
        \stemDown fis16*161/160 \stemDown gis16*161/160 \stemDown a16*161/160
        \stemDown b16*161/160 }
    \stemDown c8 ) r16 \stemDown b16 ( \stemDown c8 ) r16 \stemDown gis16
    ( | % 326
    \stemDown a8 ) r8 \once \omit TupletBracket
    \times 4/7  {
        \stemDown a,16*161/160 ( \stemDown b16*161/160 \stemDown c16*161/160
        \stemDown d16*161/160 \stemDown e16*161/160 \stemDown fis16*161/160
        \stemDown g16*161/160 }
    \stemDown a8 ) r8 \stemUp es,4 ~ \stemUp bes'4 ~ | % 327
    \stemUp es,8 \stemUp bes'8 r8 \once \omit TupletBracket
    \times 4/7  {
        \stemDown b16*161/160 ( \stemDown cis16*161/160 \stemDown dis16*161/160
        \stemDown e16*161/160 \stemDown fis16*161/160 \stemDown g16*161/160
        \stemDown a16*161/160 }
    \stemDown b8 ) r8 \stemUp e,,4 ~ \stemUp c'4 ~ \pageBreak | % 328
    \stemUp e,8 \stemUp c'8 r8 \once \omit TupletBracket
    \times 4/7  {
        \stemDown cis16*161/160 ( \stemDown d16*161/160 \stemDown e16*161/160
        \stemDown fis16*161/160 \stemDown g16*161/160 \stemDown a16*161/160
        \stemDown b16*161/160 }
    \stemDown cis16 ) r16 r8 \stemUp d,,4 ~ \stemUp d'4 ~ | % 329
    \stemUp d,8 \stemUp d'8 r8 \stemDown a''16 \stemDown g16 \stemDown
    fis16 \stemDown e16 \stemDown d16 \stemDown c16 \stemDown b16
    \stemDown a16 \stemDown g16 \stemDown fis16 \stemDown e16 \stemDown
    d16 | \barNumberCheck #330
    \stemDown g8 _\sempre _\fff r8 \stemDown d8 ( -. r16 \stemDown d16 )
    -. \stemDown g8 r8 \stemDown c,8 r8 | % 331
    \stemDown g'8 -> \stemDown d'8 ^> r4 r4 \stemDown d16 ( \stemDown c16
    \stemDown b16 \stemDown a16 \pageBreak | % 332
    \stemDown g8 ) r8 \stemDown d8 ( -. r16 \stemDown d16 ) -. \stemDown
    g8 r8 \stemDown c,8 r8 | % 333
    \stemDown g'8 -> \stemDown d'8 ^> r4 r4 \stemDown d16 ( \stemDown c16
    \stemDown b16 \stemDown a16 | % 334
    \stemDown g16 ) \stemDown a16 -. \stemDown b16 -. \stemDown c16 -.
    \stemDown d16 -. \stemDown c16 -. \stemDown b16 -. \stemDown a16 -.
    \stemDown g16 -. \stemDown a16 -. \stemDown b16 -. \stemDown c16 -.
    \stemDown d16 -. \stemDown c16 -. \stemDown b16 -. \stemDown a16 -.
    | % 335
    \stemDown g16 -. \stemDown a16 -. \stemDown b16 -. \stemDown c16 -.
    \stemDown d16 -. \stemDown c16 -. \stemDown b16 -. \stemDown a16 -.
    \stemDown g16 -. \stemDown a16 -. \stemDown b16 -. \stemDown c16 -.
    \stemDown d16 -. \stemDown c16 -. \stemDown b16 -. \stemDown a16 -.
    \pageBreak | % 336
    \stemDown g16 \stemDown a16 \stemDown b16 \stemDown c16 \stemDown d8
    r8 \stemDown g,16 \stemDown a16 \stemDown b16 \stemDown c16
    \stemDown d8 r8 | % 337
    \stemDown g,16 \stemDown a16 \stemDown b16 \stemDown c16 \stemDown d8
    r8 \stemDown g,16 \stemDown a16 \stemDown b16 \stemDown c16
    \stemDown d8 r8 | % 338
    r8 \stemDown g8 :16 \stemDown fis8 :16 \stemDown e8 :16 \stemDown d8
    :16 \stemDown c8 :16 \stemDown b8 :16 \stemDown a8 :16 | % 339
    \stemDown g8 :16 \stemDown fis8 :16 \stemDown e8 :16 \stemDown es8
    :16 \stemDown d8 :16 \stemDown c8 :16 \stemDown b8 :16 \stemDown a8
    :16 | \barNumberCheck #340
    \stemUp g8 r8 r4 \stemUp d8 \stemUp d'8 r8 r4 \pageBreak | % 341
    \stemUp g,,8 \stemUp d'8 \stemUp b'8 \stemUp g'8 r8 r4 \stemDown d,8
    \stemDown a'8 \stemDown fis'8 \stemDown d'8 r8 r4 | % 342
    \stemDown g,,,8 \stemDown d'8 \stemDown g'8 \stemDown g'8 r8
    \stemDown g,,,8 \stemDown d'8 \stemDown g'8 \stemDown g'8 r8 r4
    \stemDown g,,,8 \stemDown d'8 \stemDown g'8 \stemDown g'8 r8 | % 343
    r4 \stemDown g,,,8 \stemDown d'8 \stemDown g'8 \stemDown g'8 r8 r4
    \stemUp g,,,8 \stemUp d'8 \stemUp d'8 \stemUp d'8 r8 | % 344
    \stemUp g,,,8 \stemUp d'8 \stemUp b'8 \stemUp g'8 r8 \stemUp b,,8
    \stemUp g'8 \stemUp d'8 r8 \stemUp b,8 \stemUp g'8 r8 \stemUp g,8
    \stemUp d'8 r8 | % 345
    g,1 ~ | % 346
    \stemUp g2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 \stemUp g8 \stemUp g8 }
    | % 347
    \stemUp g8 r8 r4 r2 \bar "|."
    }

PartPTwoSevenVoiceTwo =  \relative d'' {
    \clef "treble" \time 4/4 \key g \major s1*4 \pageBreak s1*2 | % 7
    \numericTimeSignature\time 4/4  s1 \bar "||"
    s1*2 \pageBreak | \barNumberCheck #10
    \numericTimeSignature\time 4/4  s1*2 | % 12
    \numericTimeSignature\time 4/4  s1*3 \break s1*5 \pageBreak s1*4
    \break s1*3 | % 27
    \numericTimeSignature\time 4/4  s1 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak | % 36
    \numericTimeSignature\time 4/4  s1 | % 37
    \numericTimeSignature\time 4/4  s1*4 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak | % 51
    \time 12/8 \omit Staff.TimeSignature s2*15 \pageBreak s2*15
    \pageBreak s2*15 \pageBreak s1*7 \bar "||"
    s2 \pageBreak | % 71
    \key e \major s2*15 \break s1. | % 77
    \numericTimeSignature\time 4/4  s1*4 \pageBreak s1*5 \pageBreak s1*4
    \pageBreak s1*6 \pageBreak s1*6 \break s1*5 \pageBreak s1*6 \break
    s1*5 \pageBreak s1*5 \break s1*5 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1*3 \bar "||"
    \key g \major s1 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*4 \break s1*4 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1*4 \pageBreak s1*5 \pageBreak s1*4 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak | % 194
    \numericTimeSignature\time 4/4  s1*7 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s4*5 \stemDown d8 ( -. s16 \stemDown d16 ) -. \stemDown g8
    s8 \stemDown d8 s8 | % 213
    \stemDown a'8 -> \stemDown d8 -> s4*11 \pageBreak s1*5 \pageBreak
    s1*4 \pageBreak s1*3 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*6 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*7 \pageBreak s1*6
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*6
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*5 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*5 \pageBreak s1*7 \bar
    "|."
    }

PartPTwoEightVoiceOne =  \relative b' {
    \clef "treble" \time 4/4 \key g \major | % 1
    R1*4 \pageBreak | % 5
    R1*2 | % 7
    \numericTimeSignature\time 4/4  R1 \bar "||"
    R1*2 \pageBreak | \barNumberCheck #10
    \numericTimeSignature\time 4/4  R1*2 | % 12
    \numericTimeSignature\time 4/4  R1*3 \break | % 15
    R1*5 \pageBreak | \barNumberCheck #20
    R1*4 \break | % 24
    R1*3 | % 27
    \numericTimeSignature\time 4/4  R1 \pageBreak | % 28
    R1*4 \pageBreak | % 32
    R1*4 \pageBreak | % 36
    \numericTimeSignature\time 4/4  R1 | % 37
    \numericTimeSignature\time 4/4  R1*4 \pageBreak | % 41
    R1*5 \pageBreak | % 46
    R1*5 \pageBreak | % 51
    \time 12/8 \omit Staff.TimeSignature \stemDown b8 -. ^ "unis." r8*2/3
    r8*2/3 r4.*2/3 \stemUp dis,8 ( ^ "sul G" \stemUp e8 \stemUp fis8 )
    \stemUp gis8 ( \stemUp fis8 \stemUp e8 s1*5/24 | % 52
    \stemUp dis8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 53
    r1 s2 | % 54
    r1 s2 | % 55
    r2.*2/3 \stemUp gis8 -. _\mp _\< \stemUp fis8 -. \stemUp gis8 -.
    \stemUp fis8 -. \stemUp gis8 -. \stemUp fis8 -. s4 \pageBreak | % 56
    \stemUp fis8 -. \stemUp dis8 -. \stemUp fis8 -. \stemUp dis8 -.
    \stemUp fis8 -. \stemUp dis8 -. \stemUp ais'8 -. _\! _\f \stemUp e8
    -. \stemUp ais8 -. \stemUp e8 -. \stemUp ais8 -. \stemUp e8 -. | % 57
    r1 s2 | % 58
    r1 s2 | % 59
    r2.*2/3 \stemUp gis8 -. _\mp _\< \stemUp fis8 -. \stemUp gis8 -.
    \stemUp fis8 -. \stemUp gis8 -. \stemUp fis8 -. s4 | \barNumberCheck
    #60
    \stemUp fis8 -. \stemUp dis8 -. \stemUp fis8 -. \stemUp dis8 -.
    \stemUp fis8 -. \stemUp dis8 -. \stemUp ais'8 -. _\! _\f \stemUp e8
    -. \stemUp ais8 -. \stemUp e8 -. \stemUp ais8 -. \stemUp e8 -.
    \pageBreak | % 61
    \stemUp a8 -. _\p _\markup{ \small\italic {cresc. poco a poco} }
    \startTrillSpan \stemUp fis8 -. \stemUp a8 -. \stemUp fis8 -.
    \stemUp a8 -. \stemUp fis8 -. \stemUp a8 -. \stemUp fis8 -. \stemUp
    a8 -. \stemUp fis8 -. \stemUp a8 -. \stemUp fis8 -. | % 62
    \stemUp g8 -. \stemUp e8 -. \stemUp g8 -. \stemUp e8 -. \stemUp g8
    -. \stemUp e8 -. \stemUp g8 -. \stemUp e8 -. \stemUp g8 -. \stemUp e8
    -. \stemUp g8 -. \stemUp e8 -. | % 63
    \stemUp a8 -. \stemUp fis8 -. \stemUp a8 -. \stemUp fis8 -. \stemUp
    a8 -. \stemUp fis8 -. \stemUp a8 -. \stemUp fis8 -. \stemUp a8 -.
    \stemUp fis8 -. \stemUp a8 -. \stemUp fis8 -. | % 64
    \stemUp b8 -. \stemUp g8 -. \stemUp b8 -. \stemUp g8 -. \stemUp b8
    -. \stemUp g8 -. \stemUp b8 -. \stemUp g8 -. \stemUp b8 -. \stemUp g8
    -. \stemUp b8 -. \stemUp g8 -. | % 65
    \stemDown dis'8 -. \stemDown a8 -. \stemDown dis8 -. \stemDown a8 -.
    \stemDown dis8 -. \stemDown a8 -. \stemDown dis8 -. \stemDown a8 -.
    \stemDown dis8 -. \stemDown a8 -. \stemDown dis8 -. \stemDown a8 -.
    \pageBreak | % 66
    \stemDown e'8 -. \stemDown c8 -. \stemDown e8 -. \stemDown c8 -.
    \stemDown e8 -. \stemDown c8 -. \stemDown e8 -. \stemDown c8 -.
    \stemDown e8 -. \stemDown c8 -. \stemDown e8 -. \stemDown c8 -. | % 67
    \stemDown a'8 -. \stopTrillSpan _\f _\< \stemDown dis,8 -. \stemDown
    a'8 -. \stemDown dis,8 -. \stemDown a'8 -. \stemDown dis,8 -.
    \stemDown a'8 -. \stemDown dis,8 -. \stemDown a'8 -. \stemDown dis,8
    -. \stemDown a'8 -. \stemDown dis,8 -. | % 68
    \stemDown b'8 -. \stemDown g8 -. \stemDown b8 -. \stemDown g8 -.
    \stemDown b8 -. \stemDown g8 -. \stemDown b8 -. \stemDown g8 -.
    \stemDown b8 -. \stemDown g8 -. \stemDown b8 -. \stemDown g8 -. | % 69
    \stemDown b8 -> _\! _\ff \stemDown b8 -. \stemDown a8 -. \stemDown
    gis8 -. \stemDown a8 -. \stemDown gis8 -. \stemDown fis8 -. _\>
    \stemDown gis8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown e8 -. | \barNumberCheck #70
    \stemDown dis8 -. \stemDown e8 -. \stemDown dis8 -. r4.*2/3 _\! r2.*2/3
    \bar "||"
    s4. \pageBreak | % 71
    \key e \major r1 s2 | % 72
    r1 s2 | % 73
    r1 s2 | % 74
    r1 s2 | % 75
    r1 s2 \break | % 76
    r1 s2 | % 77
    r1 s2 | % 78
    \numericTimeSignature\time 4/4  \stemUp cis,8 :16 _\p \stemUp dis8
    :16 \stemUp e8 :16 \stemUp eis8 :16 \stemUp fis8 r8 r4 | % 79
    r2 r4 \stemUp cis8 _\mf r8 | \barNumberCheck #80
    \stemUp gis'4 ~ _\< \stemUp gis8 \stemUp gis16 \stemUp gis16 \stemUp
    gis8 _\! _\f \stemUp fis8 r4 \pageBreak | % 81
    \stemUp e8 _\pp -\markup{ \italic {leggieramente} } r8 \stemUp b8 (
    -. r16 \stemUp b16 ) -. \stemUp e8 -. r8 \stemUp b8 -. r8 | % 82
    \stemUp e8 -. \stemUp a8 ~ ^> \stemUp a2 \stemUp gis8 ( -. r16
    \stemUp fis16 ) -. | % 83
    \stemDown b8 -. _\markup{ \small\italic {un poco cresc.} }
    \startTrillSpan r8 \acciaccatura { \stemUp fis8 ( } \stemUp e8 r16
    \stemUp dis16 ) -. \stemUp e8 -. r8 \stemUp b8 -. r8 | % 84
    \stemUp e2. -> \stemUp gis8 ( -. r16 \stemUp b16 ) -. | % 85
    \stemDown cis8 -. r8 \acciaccatura { \stemUp fis,8 ( } \stemUp e8 r16
    \stemUp dis16 ) -. \stemUp e8 -. r8 \stemUp b8 -. r8 \pageBreak | % 86
    \stemUp e2 ~ -. -> \stemUp e8 r8 \stemUp gis8 ( -. \stopTrillSpan
    _\mf r16 \stemUp b16 ) -. | % 87
    \stemDown c4 ( -> _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp b8 r16 \stemUp a16 ) -. \stemUp g8 -. r8 \stemDown d'8 ( -.
    r16 \stemDown dis16 ) -. | % 88
    \stemDown e4 ( -> \stemDown d8 r16 \stemDown c16 ) -. \stemDown b8
    -. r8 \stemUp e8 ( -. \stopTrillSpan ^ "div." r16 \stemUp fis16 ) -.
    | % 89
    \stemUp gis2. -> \stemUp fis8 ( -. r16 \stemUp gis,16 ) -.
    \pageBreak | \barNumberCheck #90
    \stemUp e'2. -> \stemUp dis8 ( -. r16 \stemUp gis,16 ) -. | % 91
    \stemUp cis4 ( -> _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp b8 r16 \stemUp cis,16 ) \stemUp a'4 ( -> \stemUp gis8 r16
    \stemUp cis,16 ) | % 92
    \stemUp fis4 ( -> ^ "unis." \stemUp e8 r16 \stemUp g,16 ) \stemUp
    cis4 ( -> \stemUp b8 r16 \stemUp gis16 ) | % 93
    \stemUp a8 \stopTrillSpan _\ff r8 r4 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 }
    | % 94
    \stemUp c2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 }
    | % 95
    \stemUp b2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp bes8 \stemUp bes8 \stemUp bes8 }
    \pageBreak | % 96
    \stemUp bes8 r8 \stemUp b8 r8 \stemUp <b gis' b>8 r8 \stemUp b16 ( ^
    "sul G" _\ff \stemUp cis16 \stemUp dis16 \stemUp e16 ) | % 97
    \stemUp dis2 \downbow \stemUp dis2 \downbow | % 98
    \stemUp dis8 \downbow r8 \stemUp e8 \downbow r8 r2 | % 99
    R1 | \barNumberCheck #100
    r2. \stemUp b16 ( _\ff ^ "sul G" \stemUp cis16 \stemUp dis16 \stemUp
    e16 ) | % 101
    \stemUp dis2 \downbow \stemUp dis2 \downbow \break | % 102
    \stemUp dis8 \downbow r8 \stemUp e8 \downbow r8 r2 | % 103
    R1 | % 104
    r2. \once \omit TupletBracket
    \times 4/6  {
        \stemUp gis,16 ( _\ff ^ "sul G" \stemUp ais16 \stemUp bis16
        \stemUp cis16 \stemUp dis16 \stemUp e16 ) }
    | % 105
    \stemUp dis2 \downbow \stemUp dis2 \downbow | % 106
    \stemUp dis8 r8 \stemUp e8 r8 r2 \pageBreak | % 107
    R1 | % 108
    r2. \stemUp b16 ( _\ff ^ "sul G" \stemUp cis16 \stemUp dis16 \stemUp
    e16 ) | % 109
    \stemUp dis2 \downbow \stemUp dis2 \downbow | \barNumberCheck #110
    \stemUp dis2 \downbow \stemUp a2 \downbow | % 111
    \stemUp ais8 \downbow r8 \stemUp <b gis'>8 \downbow r8 \stemUp <bis
        gis'>8 \downbow r8 \stemUp <cis gis'>8 \downbow r8 | % 112
    \stemUp <d a'>8 \downbow r8 \stemUp <dis a'>8 \downbow r8 r2 \break
    | % 113
    R1*5 \pageBreak | % 118
    R1*2 | \barNumberCheck #120
    \stemUp cis8 :16 _\p \stemUp dis8 :16 \stemUp e8 :16 \stemUp eis8
    :16 \stemUp fis8 r8 r4 | % 121
    r2 r4 \stemUp cis8 _\mf r8 | % 122
    \stemUp gis'4 ~ _\< \stemUp gis8 \stemUp gis16 \stemUp gis16 \stemUp
    gis8 _\! _\f \stemUp fis8 r4 \break | % 123
    \stemUp e8 _\pp r8 \stemUp b8 ( -. r16 \stemUp b16 ) -. \stemUp e8
    -. r8 \stemUp b8 -. r8 | % 124
    \stemUp e8 -. \stemUp a8 ~ ^> \stemUp a2 \stemUp gis8 ( -. r16
    \stemUp fis16 ) -. | % 125
    \stemDown b8 -. _\markup{ \small\italic {un poco cresc.} }
    \startTrillSpan r8 \acciaccatura { \stemUp fis8 ( } \stemUp e8 r16
    \stemUp dis16 ) -. \stemUp e8 -. r8 \stemUp b8 -. r8 | % 126
    \stemUp e2. -> \stemUp gis8 ( -. r16 \stemUp b16 ) -. | % 127
    \stemDown cis8 -. r8 \acciaccatura { \stemUp fis,8 ( } \stemUp e8 r16
    \stemUp dis16 ) -. \stemUp e8 -. r8 \stemUp b8 -. r8 \pageBreak | % 128
    \stemUp e2 ~ -. -> \stemUp e8 r8 \stemUp gis,8 ( -. \stopTrillSpan
    _\f r16 \stemUp b16 ) -. | % 129
    \stemUp c4 ( -> \stemUp b8 r16 \stemUp a16 ) -. \stemUp g8 -. r8
    \stemUp d'8 ( -. r16 \stemUp dis16 ) -. | \barNumberCheck #130
    \stemUp e4 ( -> \stemUp d8 r16 \stemUp c16 ) -. \stemUp b8 -.
    \stemUp g16 \stemUp g16 \stemUp a16 \stemUp a16 \stemUp b16 \stemUp
    b16 | % 131
    \stemUp c8 :16 \stemUp d8 :16 \stemUp e8 :16 \stemUp fis8 :16
    \stemUp g8 :16 \stemUp a8 :16 \stemUp ais8 :16 \stemUp b8 :16
    \pageBreak | % 132
    \stemDown c8 :16 \stemDown d8 :16 \stemDown e8 :16 \stemDown fis8
    :16 \stemDown g8 r8 r4 | % 133
    \stemUp c,,4 ( -> \stemUp b8 r16 \stemUp a16 ) -. \stemUp g8 -. r8
    \stemUp d'8 ( -. r16 \stemUp dis16 ) -. | % 134
    \stemUp e4 ( -> \stemUp d8 r16 \stemUp c16 ) -. \stemUp b8 -.
    \stemUp g16 \stemUp g16 \stemUp a16 \stemUp a16 \stemUp b16 \stemUp
    b16 | % 135
    \stemUp c8 :16 \stemUp d8 :16 \stemUp e8 :16 \stemUp fis8 :16
    \stemUp g8 :16 \stemUp a8 :16 \stemUp ais8 :16 \stemUp b8 :16
    \pageBreak | % 136
    R1*3 \bar "||"
    \key g \major R1 \pageBreak | \barNumberCheck #140
    R1*5 \pageBreak | % 145
    R1*5 \pageBreak | \barNumberCheck #150
    R1*5 \pageBreak | % 155
    R1*4 \break | % 159
    R1*4 \pageBreak | % 163
    R1*4 \pageBreak | % 167
    R1*4 \pageBreak | % 171
    R1*4 \pageBreak | % 175
    R1*5 \pageBreak | \barNumberCheck #180
    R1*4 \pageBreak | % 184
    R1*5 \pageBreak | % 189
    R1*5 \pageBreak | % 194
    \numericTimeSignature\time 4/4  \stemUp b,16 ^ "unis." \stemUp a16
    \stemUp g'16 \stemUp fis16 \stemUp e16 \stemUp d16 \stemUp cis16
    \stemUp b16 \stemUp a8 r8 r4 | % 195
    R1*4 | % 199
    b1 :16 _\pp | \barNumberCheck #200
    \stemUp a2 :16 _\< \stemUp b2 :16 \pageBreak | % 201
    \stemUp c2 :16 _\! _\p \stemUp cis2 :16 | % 202
    \stemUp d8 r8 r4 r2 | % 203
    \stemUp gis'8 _\p ^ "div." r8 \stemUp d8 ( -. r16 \stemUp d16 ) -.
    \stemUp gis8 r8 \stemUp d8 r8 | % 204
    \stemUp <a a'>8 -> \stemUp d'8 -> r4 r2 | % 205
    R1 \pageBreak | % 206
    \stemUp e,,8 _\mp ^ "unis" r8 \stemUp b8 ( -. r16 \stemUp b16 ) -.
    \stemUp e8 r8 \stemUp b8 r8 | % 207
    \stemUp e8 -> \stemUp a8 -> r4 r2 | % 208
    \stemUp d,2 :16 _\mf _\markup{ \small\italic {poco a poco cresc.} }
    \startTrillSpan \stemUp e2 :16 | % 209
    \stemUp eis2 :16 \stemUp fis2 :16 | \barNumberCheck #210
    \stemUp g2 :16 \stemUp gis2 :16 \pageBreak | % 211
    \stemUp a2 :16 \stemUp ais2 :16 | % 212
    \stemDown b2 :16 \stopTrillSpan _\ff \stemDown bes2 :16 | % 213
    \stemUp a2 :16 \stemUp a4 :16 r4 | % 214
    \stemUp <e c' e>8 _\fff r8 \stemUp a8 ( -. r16 \stemUp a16 ) -.
    \stemUp <e c' e>8 r8 \stemUp a8 r8 | % 215
    \stemDown <a fis'>8 -> \stemDown <a a'>8 ~ -> ~ \stemDown <a a'>2.
    \pageBreak | % 216
    \stemUp <e c' e>8 r8 \stemUp a8 ( -. r16 \stemUp a16 ) -. \stemUp <e
        c' e>8 r8 \stemUp a8 r8 | % 217
    \stemDown <a fis'>8 -> \stemDown <a a'>8 ~ -> ~ \stemDown <a a'>8
    \stemDown <a a'>8 ( -. \stemDown <c e>8 ) -. \stemUp <e, a>4 \stemUp
    <e a>8 ( -. | % 218
    \stemDown <a fis'>8 ) -. \stemDown <a a'>4 \stemDown <a a'>8 ( -.
    \stemDown <c e>8 ) -. \stemUp <e, a>4 \stemUp <e a>8 -. | % 219
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a fis'>8 \stemDown <a fis'>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a a'>8 \stemDown <a a'>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a e'>8 \stemDown <a e'>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a e'>8 \stemDown <a e'>8 r8 }
    | \barNumberCheck #220
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a fis'>8 \stemDown <a fis'>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a a'>8 \stemDown <a a'>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a e'>8 \stemDown <a e'>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a e'>8 \stemDown <a e'>8 r8 }
    \pageBreak | % 221
    \times 2/3  {
        \stemDown <a fis'>8 -> \stemDown <a fis'>8 -> r8 }
    \stemUp d,32 ( _\sempre _\fff \stemUp e32 \stemUp fis32 \stemUp g32
    \stemUp a32 \stemUp b32 \stemUp c32 \stemUp d32 ) \stemDown e16 (
    \stemDown d16 \stemDown c16 \stemDown b16 ) \stemUp a16 ( \stemUp g16
    \stemUp fis16 \stemUp e16 ) | % 222
    \stemUp d16 ( \stemUp c'16 \stemUp b16 \stemUp a16 ) \stemUp g16 (
    \stemUp fis16 \stemUp e16 \stemUp d16 ) r2 | % 223
    r4 \stemUp d32 ( \stemUp e32 \stemUp fis32 \stemUp g32 \stemUp a32
    \stemUp b32 \stemUp c32 \stemUp d32 ) \stemDown e16 ( \stemDown d16
    \stemDown c16 \stemDown b16 ) \stemUp a16 ( \stemUp g16 \stemUp fis16
    \stemUp e16 ) | % 224
    \stemUp d16 ( \stemUp c'16 \stemUp b16 \stemUp a16 ) \stemUp g16 (
    \stemUp fis16 \stemUp e16 \stemUp d16 ) r2 \pageBreak | % 225
    r4 \stemUp d32 ( \stemUp e32 \stemUp fis32 \stemUp g32 \stemUp a32
    \stemUp b32 \stemUp c32 \stemUp d32 ) \once \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemUp fis8 ) r8 | % 226
    r4 \stemUp d32 ( \stemUp e32 \stemUp fis32 \stemUp g32 \stemUp a32
    \stemUp b32 \stemUp c32 \stemUp d32 ) \once \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemUp fis8 ) r8 | % 227
    r4 \stemUp d32 ( \stemUp e32 \stemUp fis32 \stemUp g32 \stemUp a32
    \stemUp b32 \stemUp c32 \stemUp d32 ) \once \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemUp fis8 ) r8 \pageBreak | % 228
    r4 \once \omit TupletBracket
    \times 4/5  {
        \stemUp a16 ( \stemUp g16 \stemUp fis16 \stemUp e16 \stemUp d16
        }
    \stemUp c8 ) r8 r4 | % 229
    \stemDown <d b' g'>8 _\fff r8 \stemDown d'8 ( -. r16 \stemDown d16 )
    -. \stemDown g8 r8 \stemDown d8 r8 | \barNumberCheck #230
    \stemDown g8 -> \stemDown c8 ~ ^> \stemDown c2 \stemUp b,8 ( -. r16
    \stemUp a16 ) -. | % 231
    \stemUp <d, d'>8 r8 \acciaccatura { \stemUp a'8 ( } \stemUp g8 ) (
    -. r16 \stemUp fis16 ) -. \stemUp g8 -. r8 \stemUp <d a'>8 r8 | % 232
    \stemDown g'2. -> \stemDown b,8 ( -. r16 \stemDown d16 ) -.
    \pageBreak | % 233
    \stemDown e8 r8 \acciaccatura { \stemUp a8 ( } \stemDown g8 ) -. r16
    \stemDown fis16 -. \stemDown g8 r8 \stemUp <d, g>8 r8 | % 234
    \stemDown g'2. -> \stemDown b,8 ( -. r16 \stemDown d16 ) -. | % 235
    \stemDown g4 ( -> \stemDown fis8 ) r16 \stemDown g16 -. \stemDown e4
    ( -> \stemDown dis8 ) r16 \stemDown e16 -. | % 236
    \stemUp c'4 ( -> ^ "div." \stemUp b8 ) r16 \stemUp c16 -. \stemUp a4
    ( -> \stemUp g8 ) r16 \stemUp a16 -. | % 237
    \stemUp e8 -. r16 \stemUp fis16 ( \stemUp g8 ) r16 \stemUp b16 (
    \stemDown e,8 ) ^ "unis." r16 \stemDown fis16 ( \stemDown g8 ) r16
    \stemDown a16 ( \pageBreak | % 238
    \stemDown b2 ) ~ -> \stemDown b8 \stemDown a16 ( \stemDown g16 \once
    \omit TupletBracket
    \times 4/6  {
        \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown c16
        \stemDown b16 \stemDown a16 }
    | % 239
    \stemUp g8 ) r8 \stemDown d'8 ( -. r16 \stemDown d16 ) -. \stemDown
    g8 r8 \stemDown d8 r8 | \barNumberCheck #240
    \stemDown g8 -> \stemDown c8 ~ ^> \stemDown c2 \stemUp b,8 ( -. r16
    \stemUp a16 ) -. | % 241
    \stemUp <d, d'>8 r8 \acciaccatura { \stemUp a'8 ( } \stemUp g8 ) (
    -. r16 \stemUp fis16 ) -. \stemUp g8 -. r8 \stemUp <d a'>8 r8 | % 242
    \stemDown g'2. -> \stemDown b,8 ( -. r16 \stemDown d16 ) -.
    \pageBreak | % 243
    \stemDown e8 r8 \acciaccatura { \stemUp a8 ( } \stemDown g8 ) -. r16
    \stemDown fis16 -. \stemDown g8 r8 \stemUp <d, g>8 r8 | % 244
    \stemDown g'2. -> \stemDown b,8 ( -. r16 \stemDown d16 ) -. | % 245
    \stemDown es4 ( -> \stemDown d8 ) r16 \stemDown c16 -. \stemDown bes8
    -. r8 \stemDown f'8 ( -. r16 \stemDown fis16 ) -. | % 246
    \stemDown g4 ( -> \stemDown f8 ) r16 \stemDown es16 -. \stemDown d8
    -. r8 \stemDown g8 ( -. r16 \stemDown a16 ) -. | % 247
    \stemDown b2. -> \stemDown a8 ( r16 \stemDown b,16 ) -. \pageBreak | % 248
    \stemDown g'2. -> \stemDown fis8 ( r16 \stemDown b,16 ) -. | % 249
    \stemDown e4 ( -> \stemDown d8 ) r16 \stemDown e16 -. \stemDown <c
        e>4 ( -> \stemDown <b e>8 ) r16 \stemDown e16 -. |
    \barNumberCheck #250
    \stemDown <a, e'>4 ( -> \stemDown g'8 ) r16 \stemDown g,16 -.
    \stemDown e'4 ( -> \stemDown d8 ) r16 \stemDown gis,16 -. | % 251
    \stemDown c8 r8 r4 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp es,8 \stemUp es8 \stemUp es8 }
    | % 252
    \stemUp es2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp d8 \stemUp d8 \stemUp d8 }
    | % 253
    \stemUp d2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis8 \stemUp cis8 \stemUp cis8 }
    \pageBreak | % 254
    \stemUp cis8 r8 \stemUp d8 r8 \stemUp <b g' d'>8 r8 r4 | % 255
    \stemUp <d fis a>8 \downbow _\fff r8 r4 \stemUp <c e ais>8 \downbow
    r8 r4 | % 256
    \stemUp <b dis b'>8 \downbow r8 \stemUp <a e' c'>8 \downbow r8 r4
    \stemDown a''4 ( _\ff | % 257
    \stemDown d,8 ) r8 \stemDown d4 ( \stemUp g,8 ) r8 \stemUp g4 ~ | % 258
    \stemUp g4 \stemUp e4 ( \stemUp c4 \stemUp a8 ) r8 \pageBreak | % 259
    \stemUp <d fis a>8 \downbow _\fff r8 r4 \stemUp <c e ais>8 \downbow
    r8 r4 | \barNumberCheck #260
    \stemUp <b dis b'>8 \downbow r8 \stemUp <a e' c'>8 \downbow r8 r4
    \stemDown fis''4 ( _\ff | % 261
    \stemDown b,8 ) r8 \stemDown b4 ( \stemUp e,8 ) r8 \stemUp e4 ~ | % 262
    \stemUp e4 \stemUp c4 ( \stemUp a4 ) \once \omit TupletBracket
    \times 4/6  {
        \stemUp b16 ( _\fff \stemUp cis16 \stemUp dis16 \stemUp e16
        \stemUp fis16 \stemUp g16 }
    | % 263
    \stemUp a8 ) r8 r4 \stemUp fis8 \downbow r8 r4 \pageBreak | % 264
    \stemUp fis8 \downbow r8 \stemUp g8 \downbow r8 r4 \stemDown a'4 (
    _\ff | % 265
    \stemDown d,8 ) r8 \stemDown d4 ( \stemUp g,8 ) r8 \stemUp g4 ~ | % 266
    \stemUp g4 \stemUp e4 ( \stemUp c4 \stemUp a8 ) r8 | % 267
    \stemUp <d fis a>8 _\fff r8 r4 \stemUp <c e ais>8 r8 r4 | % 268
    \stemUp <b dis b'>8 r8 r4 \stemUp <c e c'>8 r8 r4 \pageBreak | % 269
    \stemUp <cis e cis'>8 r8 r4 \stemUp <b g' d'>8 r8 r4 |
    \barNumberCheck #270
    \stemUp <b dis b'>8 r8 r4 \stemUp <b e b'>8 r8 r4 | % 271
    \stemUp <a f' c'>8 r8 r4 \stemUp <fis' a d>8 r8 r4 | % 272
    \stemUp <bes, g' es'>8 r8 r4 \stemUp <b gis' b e>8 r8 r4 | % 273
    \stemUp a'4 :16 \stemDown bes4 :16 \stemDown b4 :16 \stemDown c4 :16
    \pageBreak | % 274
    \stemDown cis4 :16 \stemDown d4 :16 \stemDown <a e'>8 r8 r4 | % 275
    R1*6 \pageBreak | % 281
    R1 | % 282
    r2 r4 \stemDown d16 ( _\fff \stemDown dis16 \stemDown e16 \stemDown
    fis16 | % 283
    \stemDown g8 ) r8 \stemDown d8 ( -. r16 \stemDown d16 ) -. \stemDown
    g8 r8 \stemDown d8 r8 | % 284
    \stemDown g8 -> \stemDown c8 ~ ^> \stemDown c2 \stemUp b,8 ( -. r16
    \stemUp a16 ) -. | % 285
    \stemUp <d, d'>8 r8 \acciaccatura { \stemUp a'8 ( } \stemUp g8 ) (
    -. r16 \stemUp fis16 ) -. \stemUp g8 -. r8 \stemUp <d a'>8 r8 | % 286
    \stemDown g'2. -> \stemDown b,8 ( -. r16 \stemDown d16 ) -.
    \pageBreak | % 287
    \stemDown e8 r8 \acciaccatura { \stemUp a8 ( } \stemDown g8 ) -. r16
    \stemDown fis16 -. \stemDown g8 r8 \stemUp <d, g>8 r8 | % 288
    \stemDown g'2. -> \stemDown b,8 ( -. r16 \stemDown d16 ) -. | % 289
    \stemDown g4 ( -> \stemDown fis8 ) r16 \stemDown g16 -. \stemDown e4
    ( -> \stemDown dis8 ) r16 \stemDown e16 -. | \barNumberCheck #290
    \stemUp c'4 ( -> ^ "div." \stemUp b8 ) r16 \stemUp c16 -. \stemUp a4
    ( -> \stemUp g8 ) r16 \stemUp a16 -. | % 291
    \stemUp e8 -. r16 \stemUp fis16 ( \stemUp g8 ) r16 \stemUp b16 (
    \stemDown e,8 ) ^ "unis." r16 \stemDown fis16 ( \stemDown g8 ) r16
    \stemDown a16 ( \pageBreak | % 292
    \stemDown b2 ) ~ -> \stemDown b8 \stemDown a16 ( \stemDown g16 \once
    \omit TupletBracket
    \times 4/6  {
        \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown c16
        \stemDown b16 \stemDown a16 }
    | % 293
    \stemUp g8 ) r8 \stemDown d'8 ( -. r16 \stemDown d16 ) -. \stemDown
    g8 r8 \stemDown d8 r8 | % 294
    \stemDown g8 -> \stemDown c8 ~ ^> \stemDown c2 \stemUp b,8 ( -. r16
    \stemUp a16 ) -. | % 295
    \stemUp <d, d'>8 r8 \acciaccatura { \stemUp a'8 ( } \stemUp g8 ) (
    -. r16 \stemUp fis16 ) -. \stemUp g8 -. r8 \stemUp <d a'>8 r8 | % 296
    \stemDown g'2. -> \stemDown b,8 ( -. r16 \stemDown d16 ) -.
    \pageBreak | % 297
    \stemDown e8 r8 \acciaccatura { \stemUp a8 ( } \stemDown g8 ) -. r16
    \stemDown fis16 -. \stemDown g8 r8 \stemUp <d, g>8 r8 | % 298
    \stemDown g'2. -> \stemDown b,8 ( -. r16 \stemDown d16 ) -. | % 299
    \stemDown es4 ( -> \stemDown d8 ) r16 \stemDown c16 -. \stemDown bes8
    -. r8 \stemDown f'8 ( -. r16 \stemDown fis16 ) -. | \barNumberCheck
    #300
    \stemDown g4 ( -> \stemDown f8 ) r16 \stemDown es16 -. \stemDown d8
    -. r8 \stemDown g8 ( -. r16 \stemDown a16 ) -. | % 301
    \stemDown b2. -> \stemDown a8 ( r16 \stemDown b,16 ) -. \pageBreak | % 302
    \stemDown g'2. -> \stemDown fis8 ( r16 \stemDown b,16 ) -. | % 303
    \stemDown e4 ( -> \stemDown d8 ) r16 \stemDown e16 -. \stemDown <c
        e>4 ( -> \stemDown <b e>8 ) r16 \stemDown e16 -. | % 304
    \stemDown a4 ( -> _\sempre _\fff \stemDown g8 ) r16 \stemDown e16 -.
    \stemDown a4 ( -> \stemDown g8 ) r16 \stemDown es16 -. | % 305
    \stemDown a4 ( -> \stemDown g8 ) r16 \stemDown d16 -. \stemDown a'4
    ( -> \stemDown g8 ) r16 \stemDown cis,16 -. | % 306
    \stemDown a'4 ( -> \stemDown g8 ) r16 \stemDown c,16 -. \stemDown a'4
    ( -> \stemDown g8 ) r16 \stemDown cis,16 -. | % 307
    \stemDown a'4 ( -> \stemDown g8 ) r16 \stemDown d16 -. \stemDown a'4
    ( -> \stemDown g8 ) r16 \stemDown dis16 -. \pageBreak | % 308
    \stemDown b'4 ( -> \stemDown a8 ) r16 \stemDown e16 -. \stemDown c'4
    ( -> \stemDown b8 ) r16 \stemDown e,16 -. | % 309
    \stemDown d'4 ( -> \stemDown c8 ) r16 \stemDown a16 -. \stemDown d4
    ( -> \stemDown cis8 ) r16 \stemDown a16 -. | \barNumberCheck #310
    \stemDown e'4 ( -> \stemDown d8 ) r16 \stemDown a16 -. \stemDown e'4
    ( -> \stemDown dis8 ) r16 \stemDown a16 -. | % 311
    \stemDown f'4 ( -> \stemDown e8 ) r16 \stemDown a,16 -. \stemDown g'4
    ( -> \stemDown fis8 ) r16 \stemDown c16 -. | % 312
    \stemDown a8 :16 _\ffff \stemDown g8 :16 \stemDown d8 :16 \stemDown
    g8 :16 \stemDown a8 :16 \stemDown g8 :16 \stemDown es8 :16 \stemDown
    g8 :16 | % 313
    \stemDown a8 :16 \stemDown g8 :16 \stemDown e8 :16 \stemDown g8 :16
    \stemDown a8 :16 \stemDown g8 :16 \stemDown es8 :16 \stemDown g8 :16
    \pageBreak | % 314
    \stemDown a8 :16 \stemDown g8 :16 \stemDown fis8 :16 \stemDown e8
    :16 \stemDown d8 :16 \stemDown cis'8 :16 \stemDown c8 :16 \stemDown
    b8 :16 | % 315
    \stemDown a8 :16 \stemDown g8 :16 \stemDown fis8 :16 \stemDown e8
    :16 \stemDown d8 r8 r4 | % 316
    R1*2 | % 318
    \stemUp g,,4 :16 _\mf _\< \stemUp a4 :16 \stemUp b2 :16 | % 319
    \stemUp c4 :16 \stemUp d4 :16 \stemUp e4 :16 \stemUp fis4 :16
    \pageBreak | \barNumberCheck #320
    \stemUp g4 :16 _\! _\f _\< \stemUp a4 :16 \stemDown b2 :16 | % 321
    \stemDown c4 :16 \stemDown d4 :16 \stemDown e4 :16 \stemDown fis4
    :16 | % 322
    \stemUp <g, b>4 :16 _\! _\ff ^ "div." _\< \stemDown <a c>4 :16
    \stemDown <b d>4 :16 \stemDown <b dis>4 :16 | % 323
    \stemDown <c e>4 :16 \stemDown <d fis>4 :16 \stemDown <e g>4 :16
    \stemDown <fis a>4 :16 | % 324
    \stemDown <dis b'>8 _\! _\fff r8 \once \omit TupletBracket
    \times 4/7  {
        \stemDown g,16*161/160 ( \stemDown a16*161/160 \stemDown b16*161/160
        \stemDown cis16*161/160 \stemDown dis16*161/160 \stemDown e16*161/160
        \stemDown fis16*161/160 }
    \stemDown g8 ) r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown
    dis16 ( \pageBreak | % 325
    \stemDown e8 ) r8 \once \omit TupletBracket
    \times 4/7  {
        \stemDown c16*161/160 ( \stemDown d16*161/160 \stemDown e16*161/160
        \stemDown fis16*161/160 \stemDown gis16*161/160 \stemDown a16*161/160
        \stemDown b16*161/160 }
    \stemDown c8 ) r16 \stemDown b16 ( \stemDown c8 ) r16 \stemDown gis16
    ( | % 326
    \stemDown a8 ) r8 \once \omit TupletBracket
    \times 4/7  {
        \stemDown a,16*161/160 ( \stemDown b16*161/160 \stemDown c16*161/160
        \stemDown d16*161/160 \stemDown e16*161/160 \stemDown fis16*161/160
        \stemDown g16*161/160 }
    \stemDown a8 ) r8 \stemUp bes,,4 ~ \stemUp g'4 ~ | % 327
    \stemUp bes,8 \stemUp g'8 r8 \once \omit TupletBracket
    \times 4/7  {
        \stemDown b16*161/160 ( \stemDown cis16*161/160 \stemDown dis16*161/160
        \stemDown e16*161/160 \stemDown fis16*161/160 \stemDown g16*161/160
        \stemDown a16*161/160 }
    \stemDown b8 ) r8 \stemUp g,,4 ~ \stemUp g'4 ~ \pageBreak | % 328
    \stemUp g,8 \stemUp g'8 r8 \once \omit TupletBracket
    \times 4/7  {
        \stemDown cis16*161/160 ( \stemDown d16*161/160 \stemDown e16*161/160
        \stemDown fis16*161/160 \stemDown g16*161/160 \stemDown a16*161/160
        \stemDown b16*161/160 }
    \stemDown cis16 ) r16 r8 \stemUp d,,4 ~ \stemUp a'4 ~ | % 329
    \stemUp d,8 \stemUp a'8 r8 \stemDown a'16 \stemDown g16 \stemDown
    fis16 \stemDown e16 \stemDown d16 \stemDown c16 \stemDown b16
    \stemDown a16 \stemUp g16 \stemUp fis16 \stemUp e16 \stemUp d16 |
    \barNumberCheck #330
    \stemUp d8 _\sempre _\fff \stemUp d'8 r8 \stemDown d8 ( -. r16
    \stemDown d16 ) -. \stemDown g8 r8 \stemDown c,8 r8 | % 331
    \stemDown g'8 -> \stemDown d'8 ^> r4 r4 \stemDown d,16 ( \stemDown c16
    \stemDown b16 \stemDown a16 \pageBreak | % 332
    \stemUp g8 ) r8 \stemDown d'8 ( -. r16 \stemDown d16 ) -. \stemDown
    g8 r8 \stemDown c,8 r8 | % 333
    \stemDown g'8 -> \stemDown d'8 ^> r4 r4 \stemDown d,16 ( \stemDown c16
    \stemDown b16 \stemDown a16 | % 334
    \stemUp g16 ) \stemUp a16 -. \stemUp b16 -. \stemUp c16 -. \stemDown
    d16 -. \stemDown c16 -. \stemDown b16 -. \stemDown a16 -. \stemUp g16
    -. \stemUp a16 -. \stemUp b16 -. \stemUp c16 -. \stemDown d16 -.
    \stemDown c16 -. \stemDown b16 -. \stemDown a16 -. | % 335
    \stemUp g16 -. \stemUp a16 -. \stemUp b16 -. \stemUp c16 -.
    \stemDown d16 -. \stemDown c16 -. \stemDown b16 -. \stemDown a16 -.
    \stemUp g16 -. \stemUp a16 -. \stemUp b16 -. \stemUp c16 -.
    \stemDown d16 -. \stemDown c16 -. \stemDown b16 -. \stemDown a16 -.
    \pageBreak | % 336
    \stemUp g16 \stemUp a16 \stemUp b16 \stemUp c16 \stemDown d8 r8
    \stemUp g,16 \stemUp a16 \stemUp b16 \stemUp c16 \stemDown d8 r8 | % 337
    \stemUp g,16 \stemUp a16 \stemUp b16 \stemUp c16 \stemDown d8 r8
    \stemUp g,16 \stemUp a16 \stemUp b16 \stemUp c16 \stemDown d8 r8 | % 338
    r8 \stemDown g8 :16 \stemDown fis8 :16 \stemDown e8 :16 \stemDown d8
    :16 \stemDown c8 :16 \stemDown b8 :16 \stemDown a8 :16 | % 339
    \stemDown g8 :16 \stemDown fis'8 :16 \stemDown e8 :16 \stemDown es8
    :16 \stemDown d8 :16 \stemDown c8 :16 \stemDown b8 :16 \stemDown a8
    :16 | \barNumberCheck #340
    \stemUp g8 r8 r4 \stemUp d8 \stemUp fis8 \stemUp a8 r8 r4 \pageBreak
    | % 341
    \stemUp g,8 \stemUp d'8 \stemUp b'8 \stemUp g'8 r8 r4 \stemDown fis,8
    \stemDown d'8 \stemDown a'8 r8 r4 | % 342
    \stemUp g,,8 \stemUp g'8 \stemUp d'8 \stemUp b'8 r8 \stemUp g,,8
    \stemUp g'8 \stemUp d'8 \stemUp b'8 r8 r4 \stemUp g,,8 \stemUp g'8
    \stemUp d'8 \stemUp b'8 r8 | % 343
    r4 \stemUp g,,8 \stemUp g'8 \stemUp d'8 \stemUp b'8 r8 r4 \stemUp
    g,,8 \stemUp g'8 \stemUp d'8 \stemUp b'8 r8 | % 344
    \stemUp b,,8 \stemUp g'8 \stemUp d'8 r8 \stemUp g,,8 \stemUp d'8
    \stemUp b'8 r8 \stemUp b,8 \stemUp g'8 r8 \stemUp b,8 \stemUp d8 r8
    | % 345
    g,1 ~ | % 346
    \stemUp g2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 \stemUp g8 \stemUp g8 }
    | % 347
    \stemUp g8 r8 r4 r2 \bar "|."
    }

PartPTwoEightVoiceTwo =  \relative e' {
    \clef "treble" \time 4/4 \key g \major s1*4 \pageBreak s1*2 | % 7
    \numericTimeSignature\time 4/4  s1 \bar "||"
    s1*2 \pageBreak | \barNumberCheck #10
    \numericTimeSignature\time 4/4  s1*2 | % 12
    \numericTimeSignature\time 4/4  s1*3 \break s1*5 \pageBreak s1*4
    \break s1*3 | % 27
    \numericTimeSignature\time 4/4  s1 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak | % 36
    \numericTimeSignature\time 4/4  s1 | % 37
    \numericTimeSignature\time 4/4  s1*4 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak | % 51
    \time 12/8 \omit Staff.TimeSignature s2*15 \pageBreak s2*15
    \pageBreak s2*15 \pageBreak s8*57 \bar "||"
    s4. \pageBreak | % 71
    \key e \major s2*15 \break s1*3 | % 78
    \numericTimeSignature\time 4/4  s1*3 \pageBreak s1*5 \pageBreak
    s4*11 \stemDown e8 ( -. r16 \stemDown fis16 ) -. | % 89
    \stemDown gis2. \stemDown fis8 ( -. s16 \stemDown gis,16 ) -.
    \pageBreak | \barNumberCheck #90
    \stemDown dis'2. \stemDown d8 ( -. r16 \stemDown g,16 ) -. | % 91
    \stemDown cis4 ( -> \stemDown b'8 s16 \stemDown cis,16 ) \stemDown
    a'4 ( -> \stemDown gis8 s16 \stemDown cis,16 ) s1*4 \pageBreak s1*6
    \break s1*5 \pageBreak s1*6 \break s1*5 \pageBreak s1*5 \break s1*5
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*3 \bar "||"
    \key g \major s1 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*4 \break s1*4 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1*4 \pageBreak s1*5 \pageBreak s1*4 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak | % 194
    \numericTimeSignature\time 4/4  s1*7 \pageBreak s1*2 | % 203
    \stemDown gis'8 s8 \stemDown d8 ( -. s16 \stemDown d16 ) -.
    \stemDown gis8 s8 \stemDown d8 s8 | % 204
    \stemDown <a' a'>8 -> \stemDown d8 -> s4*7 \pageBreak s1*5
    \pageBreak s1*2 | % 213
    \stemDown a2 :16 \stemDown a8 s8*19 \pageBreak s1*5 \pageBreak s1*4
    \pageBreak s1*3 \pageBreak s1*5 \pageBreak s1*3 | % 236
    \stemDown c4 ( -> \stemDown b8 ) s16 \stemDown c16 -. \stemDown a4 (
    -> \stemDown g8 ) s16 \stemDown a16 -. | % 237
    \stemDown e8 s16 \stemDown fis16 ( \stemDown g8 ) s16 \stemDown b16
    s2 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*6 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*7
    \pageBreak s1*6 \pageBreak s1*3 | \barNumberCheck #290
    \stemDown c4 ( -> \stemDown b8 ) s16 \stemDown c16 -. \stemDown a4 (
    -> \stemDown g8 ) s16 \stemDown a16 -. | % 291
    \stemDown e8 s16 \stemDown fis16 ( \stemDown g8 ) s16 \stemDown b16
    s2 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*6 \pageBreak s1*6
    \pageBreak s1*6 \pageBreak s1*5 \pageBreak s1*3 \pageBreak s1*4
    \pageBreak s1*4 \pageBreak s1*5 \pageBreak s1*7 \bar "|."
    }

PartPTwoNineVoiceOne =  \relative b' {
    \clef "alto" \time 4/4 \key g \major | % 1
    R1*4 \pageBreak | % 5
    R1*2 | % 7
    \numericTimeSignature\time 4/4  R1 \bar "||"
    R1*2 \pageBreak | \barNumberCheck #10
    \numericTimeSignature\time 4/4  R1*2 | % 12
    \numericTimeSignature\time 4/4  R1*3 \break | % 15
    R1*5 \pageBreak | \barNumberCheck #20
    R1*4 \break | % 24
    R1*3 | % 27
    \numericTimeSignature\time 4/4  R1 \pageBreak | % 28
    R1*4 \pageBreak | % 32
    R1*4 \pageBreak | % 36
    \numericTimeSignature\time 4/4  R1 | % 37
    \numericTimeSignature\time 4/4  R1*4 \pageBreak | % 41
    R1*5 \pageBreak | % 46
    R1*5 \pageBreak | % 51
    \time 12/8 \omit Staff.TimeSignature \stemDown b8 -. ^ "unis." r8*2/3
    r8*2/3 r4.*2/3 \stemUp dis,,8 ( \stemUp e8 \stemUp fis8 ) \stemUp
    gis8 ( \stemUp fis8 \stemUp e8 s1*5/24 | % 52
    \stemUp dis8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 53
    \stemUp gis8 -. _\pp _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemUp fis8 -. \stemUp gis8 -. \stemUp fis8 -.
    \stemUp gis8 -. \stemUp fis8 -. \stemUp b8 -. \stemUp ais8 -.
    \stemUp b8 -. \stemUp ais8 -. \stemUp b8 -. \stemUp ais8 -. | % 54
    \stemUp cis8 -. \stemUp b8 -. \stemUp cis8 -. \stemUp b8 -. \stemUp
    cis8 -. \stemUp b8 -. \stemDown dis8 -. \stemDown cis8 -. \stemDown
    dis8 -. \stemDown cis8 -. \stemDown dis8 -. \stemDown cis8 -. | % 55
    \stemDown e8 -. \stopTrillSpan _\mp _\< \stemDown dis8 -. \stemDown
    e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8 -. \stemUp
    cis8 -. \stemUp ais8 -. \stemUp cis8 -. \stemUp ais8 -. \stemUp cis8
    -. \stemUp ais8 -. \pageBreak | % 56
    \stemUp cis8 -. \stemUp b8 -. \stemUp cis8 -. \stemUp b8 -. \stemUp
    cis8 -. \stemUp b8 -. \stemDown dis8 -. _\! _\f \stemDown cis8 -.
    \stemDown dis8 -. \stemDown cis8 -. \stemDown dis8 -. \stemDown cis8
    -. | % 57
    \stemUp gis8 -. _\pp _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemUp fis8 -. \stemUp gis8 -. \stemUp fis8 -.
    \stemUp gis8 -. \stemUp fis8 -. \stemUp b8 -. \stemUp ais8 -.
    \stemUp b8 -. \stemUp ais8 -. \stemUp b8 -. \stemUp ais8 -. | % 58
    \stemUp cis8 -. \stemUp b8 -. \stemUp cis8 -. \stemUp b8 -. \stemUp
    cis8 -. \stemUp b8 -. \stemDown dis8 -. \stemDown cis8 -. \stemDown
    dis8 -. \stemDown cis8 -. \stemDown dis8 -. \stemDown cis8 -. | % 59
    \stemDown e8 -. \stopTrillSpan _\mp _\< \stemDown dis8 -. \stemDown
    e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8 -. \stemUp
    cis8 -. \stemUp ais8 -. \stemUp cis8 -. \stemUp ais8 -. \stemUp cis8
    -. \stemUp ais8 -. | \barNumberCheck #60
    \stemUp cis8 -. \stemUp b8 -. \stemUp cis8 -. \stemUp b8 -. \stemUp
    cis8 -. \stemUp b8 -. \stemDown dis8 -. _\! _\f \stemDown cis8 -.
    \stemDown dis8 -. \stemDown cis8 -. \stemDown dis8 -. \stemDown cis8
    -. \pageBreak | % 61
    \stemDown e8 -. _\p _\markup{ \small\italic {cresc. poco a poco} }
    \startTrillSpan \stemDown dis8 -. \stemDown e8 -. \stemDown dis8 -.
    \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8 -.
    \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8 -.
    | % 62
    \stemDown d8 -. \stemDown c8 -. \stemDown d8 -. \stemDown c8 -.
    \stemDown d8 -. \stemDown c8 -. \stemDown d8 -. \stemDown c8 -.
    \stemDown d8 -. \stemDown c8 -. \stemDown d8 -. \stemDown c8 -. | % 63
    \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8 -.
    \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8 -.
    \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8 -.
    | % 64
    \stemDown fis8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -.
    | % 65
    \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown fis8 -.
    \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown fis8 -.
    \stemDown g8 -. \stemDown fis8 -. \stemDown g8 -. \stemDown fis8 -.
    \pageBreak | % 66
    \stemDown b8 -. \stemDown a8 -. \stemDown b8 -. \stemDown a8 -.
    \stemDown b8 -. \stemDown a8 -. \stemDown b8 -. \stemDown a8 -.
    \stemDown b8 -. \stemDown a8 -. \stemDown b8 -. \stemDown a8 -. | % 67
    \stemDown c8 -. \stopTrillSpan _\f _\< \stemDown b8 -. \stemDown c8
    -. \stemDown b8 -. \stemDown c8 -. \stemDown b8 -. \stemDown c8 -.
    \stemDown b8 -. \stemDown c8 -. \stemDown b8 -. \stemDown c8 -.
    \stemDown b8 -. | % 68
    \stemDown fis'8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -.
    | % 69
    \stemDown dis8 -> _\! _\ff \stemDown b8 -. \stemDown a8 -. \stemDown
    gis8 -. \stemDown a8 -. \stemDown gis8 -. \stemDown fis8 -.
    _\markup{ \small\italic {dim.} } \startTrillSpan \stemDown gis8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -.
    | \barNumberCheck #70
    \stemDown dis8 -. \stemDown e8 -. \stemDown dis8 -. \stemDown cis'8
    -. \stopTrillSpan _\mf _\> \stemDown dis8 -. \stemDown cis8 -.
    \stemDown b8 -. \stemDown cis8 -. \stemDown b8 -. \stemDown a8 -.
    \stemDown b8 -. \stemDown a8 -. \bar "||"
    \pageBreak | % 71
    \key e \major \stemDown gis8 -. _\! _\pp \stemDown a8 -. \stemDown
    gis8 -. \stemDown fis8 -. \stemDown gis8 -. \stemDown fis8 -.
    \stemDown e8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown dis8 -.
    \stemDown e8 -. \stemDown dis8 -. | % 72
    \stemDown cis8 -. \stemDown dis8 -. \stemDown cis8 -. \stemDown c8
    -. \stemDown d8 -. \stemDown c8 -. \stemUp b8 -. \stemUp cis8 -.
    \stemUp b8 -. r4.*2/3 s8 | % 73
    r1 s2 | % 74
    r1 s2 | % 75
    r1 s2 \break | % 76
    r1 s2 | % 77
    \numericTimeSignature\time 4/4  R1 | % 78
    r2 \stemUp a8 :16 _\p \stemUp b8 :16 \stemUp cis8 :16 \stemUp dis8
    :16 | % 79
    \stemDown e8 :16 _\< \stemDown dis8 :16 \stemDown cis8 :16 \stemDown
    b8 :16 \stemUp ais16 \stemUp ais16 \stemUp a16 \stemUp a16 \stemDown
    e'8 _\! _\mf r8 | \barNumberCheck #80
    \stemDown cis4 ~ _\< \stemDown cis8 \stemDown cis16 \stemDown cis16
    \stemUp bis8 _\! _\f \stemUp b8 r4 \pageBreak | % 81
    \time 12/8  \stemUp gis8 -. _\pp \stemUp a8 -. \stemUp gis8 -.
    \stemUp fis8 -. \stemUp gis8 -. \stemUp fis8 -. \stemUp e8 -.
    \stemUp fis8 -. \stemUp e8 -. \stemUp dis8 -. \stemUp e8 -. \stemUp
    dis8 -. | % 82
    \numericTimeSignature\time 4/4  \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis8 -. \stemUp dis8 -. \stemUp cis8 -. }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 -. \stemUp d8 -. \stemUp c8 -. }
    r4 \stemDown gis''8 ( -. r16 \stemDown fis16 ) -. | % 83
    \stemDown b8 -. _\markup{ \small\italic {un poco cresc.} }
    \startTrillSpan r8 \acciaccatura { \stemUp fis8 ( } \stemDown e8 r16
    \stemDown dis16 ) -. \stemDown e8 -. r8 \stemUp b8 -. r8 | % 84
    \stemDown e2. -> \stemDown gis8 ( -. r16 \stemDown b16 ) -. | % 85
    \stemDown cis8 -. r8 \acciaccatura { \stemUp fis,8 ( } \stemDown e8
    r16 \stemDown dis16 ) -. \stemDown e8 -. r8 \stemUp b8 -. r8
    \pageBreak | % 86
    \stemDown e2 ~ -. -> \stemDown e8 r8 r4 | % 87
    \stemUp c,16 \stopTrillSpan _\mf _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemUp c16 \stemUp d16 \stemUp d16 \stemUp e16
    \stemUp e16 \stemUp f16 \stemUp f16 \stemUp g16 \stemUp g16 \stemUp
    a16 \stemUp a16 \stemUp ais16 \stemUp ais16 \stemUp b16 \stemUp b16
    | % 88
    \stemDown c16 \stemDown c16 \stemDown d16 \stemDown d16 \stemDown e16
    \stemDown e16 \stemDown f16 \stemDown f16 \stemDown g16 \stemDown g16
    \stemDown gis16 \stemDown gis16 \stemDown e8 ( -. \stopTrillSpan r16
    \stemDown fis16 ) -. | % 89
    \stemDown gis2. -> \stemDown fis8 ( -. r16 \stemDown gis,16 ) -.
    \pageBreak | \barNumberCheck #90
    \stemDown e'2. -> \stemUp dis8 ( -. r16 \stemUp gis,16 ) -. | % 91
    \stemDown cis4 ( -> _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemDown b'8 r16 \stemDown cis,16 ) \stemDown a'4 (
    -> \stemDown gis8 r16 \stemDown cis,16 ) | % 92
    \stemDown fis4 ( -> \stemUp e8 r16 \stemUp g,16 ) \stemDown cis4 (
    -> \stemUp b8 r16 \stemUp gis16 ) | % 93
    \stemUp a8 \stopTrillSpan _\ff r8 r4 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp c,8 \stemUp c8 \stemUp c8 }
    | % 94
    \stemUp c2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp b'8 \stemUp b8 \stemUp b8 }
    | % 95
    \stemUp b2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp bes8 \stemUp bes8 \stemUp bes8 }
    \pageBreak | % 96
    \stemUp bes8 r8 \stemUp b8 r8 \stemUp <gis e'>8 r8 r4 | % 97
    r2 \stemDown cis2 \downbow _\ff | % 98
    \stemUp bis8 \downbow r8 \stemDown cis8 \downbow r8 r8 \stemUp cis,8
    _\p ^ "pizz." \stemUp d8 \stemUp dis8 | % 99
    \stemUp e8 _\< \stemUp fis8 \stemUp g8 \stemUp gis8 \stemUp a8
    \stemUp ais8 \stemUp b8 \stemUp bis8 | \barNumberCheck #100
    \stemUp cis8 _\! _\mf _\> \stemUp b8 \stemUp a8 \stemUp gis8 \stemUp
    fis8 \stemUp e8 \stemUp dis8 r8 _\! | % 101
    r2 \stemDown cis'2 \downbow _\ff ^ "arco" \break | % 102
    \stemUp bis8 \downbow r8 \stemDown cis8 \downbow r8 r8 \stemUp ais8
    _\p ^ "pizz." \stemUp b8 \stemUp bis8 | % 103
    \stemDown cis8 _\< \stemDown dis8 \stemDown e8 \stemDown eis8
    \stemDown fis8 \stemDown fisis8 \stemDown gis8 \stemDown b8 | % 104
    \stemDown a8 _\! _\mf _\> \stemDown gis8 \stemDown fis8 \stemDown e8
    \stemDown dis8 \stemDown cis8 \stemUp bis8 r8 _\! | % 105
    r2 \stemDown cis2 \downbow _\ff ^ "arco" | % 106
    \stemUp bis8 r8 \stemDown cis8 r8 r8 \stemUp cis,8 _\p ^ "pizz."
    \stemUp d8 \stemUp dis8 \pageBreak | % 107
    \stemUp e8 _\< \stemUp fis8 \stemUp g8 \stemUp gis8 \stemUp a8
    \stemUp ais8 \stemUp b8 \stemUp bis8 | % 108
    \stemUp cis8 _\! _\mf _\> \stemUp b8 \stemUp a8 \stemUp gis8 \stemUp
    fis8 \stemUp e8 \stemUp dis8 r8 _\! | % 109
    r2 \stemDown cis'2 \downbow _\ff ^ "arco" | \barNumberCheck #110
    \stemUp bis2 \downbow \stemDown cis2 \downbow | % 111
    \stemDown cis8 \downbow r8 \stemUp gis8 \downbow r8 \stemUp gis8
    \downbow r8 \stemUp gis8 \downbow r8 | % 112
    \stemUp fis8 \downbow r8 \stemUp fis8 \downbow r8 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown b'8 -. _\pp \stemDown cis8 -. \stemDown b8 -. }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 -. \stemDown b8 -. \stemDown a8 -. }
    \break | % 113
    \time 12/8  \stemDown gis8 -. \stemDown a8 -. \stemDown gis8 -.
    \stemDown fis8 -. \stemDown gis8 -. \stemDown fis8 -. \stemDown e8
    -. \stemDown fis8 -. \stemDown e8 -. \stemDown dis8 -. \stemDown e8
    -. \stemDown dis8 -. | % 114
    \stemDown cis8 -. \stemDown dis8 -. \stemDown cis8 -. \stemDown c8
    -. \stemDown d8 -. \stemDown c8 -. \stemUp b8 -. \stemUp cis8 -.
    \stemUp b8 -. r4.*2/3 s8 | % 115
    r1 s2 | % 116
    r1 s2 | % 117
    r1 s2 \pageBreak | % 118
    r1 s2 | % 119
    \numericTimeSignature\time 4/4  \stemUp e,8 :16 _\p \stemUp fis8 :16
    \stemUp fisis8 :16 \stemUp gis8 :16 \stemUp gis8 r8 r4 |
    \barNumberCheck #120
    r2 \stemUp a8 :16 _\p \stemUp b8 :16 \stemUp cis8 :16 \stemUp dis8
    :16 | % 121
    \stemDown e8 :16 _\< \stemDown dis8 :16 \stemDown cis8 :16 \stemDown
    b8 :16 \stemUp ais8 :16 \stemUp a8 :16 \stemDown e'8 _\! _\mf r8 | % 122
    \stemDown cis4 ~ _\< \stemDown cis8 \stemDown cis16 \stemDown cis16
    \stemUp bis8 _\! _\f \stemUp b8 r4 \break | % 123
    \time 12/8  \stemUp gis8 -. _\pp \stemUp a8 -. \stemUp gis8 -.
    \stemUp fis8 -. \stemUp gis8 -. \stemUp fis8 -. \stemUp e8 -.
    \stemUp fis8 -. \stemUp e8 -. \stemUp dis8 -. \stemUp e8 -. \stemUp
    dis8 -. | % 124
    \numericTimeSignature\time 4/4  \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis8 -. \stemUp dis8 -. \stemUp cis8 -. }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 -. \stemUp d8 -. \stemUp c8 -. }
    r4 \stemDown gis''8 ( -. r16 \stemDown fis16 ) -. | % 125
    \stemDown b8 -. _\markup{ \small\italic {un poco cresc.} }
    \startTrillSpan r8 \acciaccatura { \stemUp fis8 ( } \stemDown e8 r16
    \stemDown dis16 ) -. \stemDown e8 -. r8 \stemUp b8 -. r8 | % 126
    \stemDown e2. -> \stemDown gis8 ( -. r16 \stemDown b16 ) -. | % 127
    \stemDown cis8 -. r8 \acciaccatura { \stemUp fis,8 ( } \stemDown e8
    r16 \stemDown dis16 ) -. \stemDown e8 -. r8 \stemUp b8 -. r8
    \pageBreak | % 128
    \stemDown e2 ~ -. -> \stemDown e8 r8 r4 | % 129
    \stemUp c,8 :16 \stopTrillSpan _\f \stemUp d8 :16 \stemUp e8 :16
    \stemUp fis8 :16 \stemUp g8 :16 \stemUp a8 :16 \stemUp ais8 :16
    \stemUp b8 :16 | \barNumberCheck #130
    \stemDown c8 :16 \stemDown d8 :16 \stemDown e8 :16 \stemDown fis8
    :16 \stemDown g8 \stemDown g,16 \stemDown g16 \stemUp a16 \stemUp a16
    \stemUp b16 \stemUp b16 | % 131
    \stemDown c8 r8 r4 \stemDown <b d>8 r8 r4 \pageBreak | % 132
    \stemDown <g g'>8 r8 r4 \stemDown d''16 \stemDown c16 \stemDown b16
    \stemDown a16 \stemDown g16 \stemDown f16 \stemDown e16 \stemDown d16
    | % 133
    \stemDown c8 r8 r4 \stemUp g8 :16 \stemUp a8 :16 \stemUp ais8 :16
    \stemUp b8 :16 | % 134
    \stemDown c8 :16 \stemDown d8 :16 \stemDown e8 :16 \stemDown fis8
    :16 \stemDown g8 \stemUp g,16 \stemUp g16 \stemUp a16 \stemUp a16
    \stemUp b16 \stemUp b16 | % 135
    \stemDown c8 r8 r4 \stemDown <b d>8 r8 r4 \pageBreak | % 136
    R1*3 \bar "||"
    \key g \major R1 \pageBreak | \barNumberCheck #140
    R1*5 \pageBreak | % 145
    R1*5 \pageBreak | \barNumberCheck #150
    R1*5 \pageBreak | % 155
    R1*4 \break | % 159
    R1*4 \pageBreak | % 163
    R1*4 \pageBreak | % 167
    R1*4 \pageBreak | % 171
    R1*4 \pageBreak | % 175
    R1*5 \pageBreak | \barNumberCheck #180
    R1*4 \pageBreak | % 184
    R1*5 \pageBreak | % 189
    R1*5 \pageBreak | % 194
    \numericTimeSignature\time 4/4  \stemUp b16 ^ "unis." \stemUp a16
    \stemUp g16 \stemUp fis16 \stemUp e16 \stemUp d16 \stemUp cis'16
    \stemUp b16 \stemUp a8 r8 r4 | % 195
    R1*3 | % 198
    fis1 :16 _\pp | % 199
    \stemUp e2 :16 \stemUp eis2 :16 | \barNumberCheck #200
    \stemUp fis2 :16 _\< \stemUp f2 :16 \pageBreak | % 201
    \stemUp e8 _\! _\p r8 r4 r2 | % 202
    \stemUp d2 :16 \stemUp dis2 :16 | % 203
    \stemUp e2 :16 \stemUp eis2 :16 _\< | % 204
    \stemUp fis2 :16 \stemUp g2 :16 | % 205
    \stemUp a8 _\! _\mp r8 r4 r2 \pageBreak | % 206
    \stemUp e8 _\mp r8 \stemUp b'8 ( -. r16 \stemUp b16 ) -. \stemUp e,8
    r8 \stemUp b'8 r8 | % 207
    \stemUp e,8 -> \stemUp a8 -> r4 r2 | % 208
    \stemUp d,2 :16 _\mf _\markup{ \small\italic {poco a poco cresc.} }
    \startTrillSpan \stemUp e2 :16 | % 209
    \stemUp eis2 :16 \stemUp fis2 :16 | \barNumberCheck #210
    \stemUp g2 :16 \stemUp gis2 :16 \pageBreak | % 211
    \stemUp a2 :16 \stemUp ais2 :16 | % 212
    \stemUp b2 :16 \stopTrillSpan _\ff \stemUp bes2 :16 | % 213
    \stemUp a2 :16 \stemUp a8 r8 r4 | % 214
    \stemDown <c e a>8 _\fff r8 \stemDown <c e>8 ( -. r16 \stemDown <c
        e>16 ) -. \stemDown <c e>8 r8 \stemDown <c e>8 r8 | % 215
    \stemDown <d c'>8 -> \stemDown fis'8 ~ -> \stemDown fis2. \pageBreak
    | % 216
    \stemDown <c, e a>8 r8 \stemDown <c e>8 ( -. r16 \stemDown <c e>16 )
    -. \stemDown <c e>8 r8 \stemDown <c e>8 r8 | % 217
    \stemDown <d c'>8 -> \stemDown fis'8 ~ -> \stemDown fis8 \stemDown
    fis8 ( -. \stemDown <c, e>8 ) -. \stemDown <c e>4 \stemDown <c e>8 (
    -. | % 218
    \stemDown <d c'>8 ) -. \stemDown fis'4 -> \stemDown fis8 ( -.
    \stemDown <c, e>8 ) -. \stemDown <c e>4 \stemDown <c e>8 -. | % 219
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <c fis>8 \stemDown <c fis>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis'8 \stemDown fis8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <e, c'>8 \stemDown <e c'>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <e c'>8 \stemDown <e c'>8 r8 }
    | \barNumberCheck #220
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <c fis>8 \stemDown <c fis>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis'8 \stemDown fis8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <e, c'>8 \stemDown <e c'>8 r8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <e c'>8 \stemDown <e c'>8 r8 }
    \pageBreak | % 221
    \times 2/3  {
        \stemDown <c fis>8 -> \stemDown <c fis>8 -> r8 }
    \stemUp d,32 ( _\sempre _\fff \stemUp e32 \stemUp fis32 \stemUp g32
    \stemUp a32 \stemUp b32 \stemUp c32 \stemUp d32 ) \stemDown e16 (
    \stemDown d16 \stemDown c16 \stemDown b16 ) \stemDown a16 (
    \stemDown g'16 \stemDown fis16 \stemDown e16 ) | % 222
    \stemUp d16 ( \stemUp c16 \stemUp b16 \stemUp a16 ) \stemUp g16 (
    \stemUp fis16 \stemUp e16 \stemUp d16 ) r2 | % 223
    r4 \stemUp d32 ( \stemUp e32 \stemUp fis32 \stemUp g32 \stemUp a32
    \stemUp b32 \stemUp c32 \stemUp d32 ) \stemDown e16 ( \stemDown d16
    \stemDown c16 \stemDown b16 ) \stemDown a16 ( \stemDown g'16
    \stemDown fis16 \stemDown e16 ) | % 224
    \stemUp d16 ( \stemUp c16 \stemUp b16 \stemUp a16 ) \stemUp g16 (
    \stemUp fis16 \stemUp e16 \stemUp d16 ) r2 \pageBreak | % 225
    r4 \stemUp d32 ( \stemUp e32 \stemUp fis32 \stemUp g32 \stemUp a32
    \stemUp b32 \stemUp c32 \stemUp d32 ) \once \omit TupletBracket
    \times 4/6  {
        \stemUp e16 ( \stemUp d16 \stemUp c16 \stemUp b16 \stemUp a16
        \stemUp g16 }
    \stemUp fis8 ) r8 | % 226
    r4 \stemUp d32 ( \stemUp e32 \stemUp fis32 \stemUp g32 \stemUp a32
    \stemUp b32 \stemUp c32 \stemUp d32 ) \once \omit TupletBracket
    \times 4/6  {
        \stemUp e16 ( \stemUp d16 \stemUp c16 \stemUp b16 \stemUp a16
        \stemUp g16 }
    \stemUp fis8 ) r8 | % 227
    r4 \stemUp d32 ( \stemUp e32 \stemUp fis32 \stemUp g32 \stemUp a32
    \stemUp b32 \stemUp c32 \stemUp d32 ) \once \omit TupletBracket
    \times 4/6  {
        \stemUp e16 ( \stemUp d16 \stemUp c16 \stemUp b16 \stemUp a16
        \stemUp g16 }
    \stemUp fis8 ) r8 \pageBreak | % 228
    r4 \once \omit TupletBracket
    \times 4/5  {
        \stemUp a16 ( \stemUp g16 \stemUp fis16 \stemUp e16 \stemUp d16
        }
    \stemUp c8 ) r8 \once \omit TupletBracket
    \times 4/6  {
        \stemDown a''16 ( \stemDown g16 \stemDown fis16 \stemDown e16
        \stemDown d16 \stemDown c16 }
    | % 229
    \stemUp b8 ) r8 \stemDown <d fis a>8 _\fff r8 \stemDown <g, d' b'>8
    r8 \stemDown <a d a'>8 r8 | \barNumberCheck #230
    \stemDown <g g'>8 -> \stemDown c8 ~ ^> \stemDown c2 \stemUp b8 ( -.
    r16 \stemUp a16 ) -. | % 231
    \stemDown <g g'>8 r8 \acciaccatura { \stemUp a8 ( } \stemUp g8 ) (
    -. r16 \stemUp fis16 ) -. \stemUp g8 -. r8 \stemDown <a d a'>8 r8 | % 232
    \stemDown <g g'>2. -> \stemDown b8 ( -. r16 \stemDown d16 ) -.
    \pageBreak | % 233
    \stemDown e8 r8 \acciaccatura { \stemUp a8 ( } \stemDown g8 ) -. r16
    \stemDown fis16 -. \stemDown g8 r8 \stemDown <a, d a'>8 r8 | % 234
    \stemDown <g g'>2. -> \stemDown b8 ( -. r16 \stemDown d16 ) -. | % 235
    \stemDown g4 ( -> \stemDown fis8 ) r16 \stemDown g16 -. \stemDown e4
    ( -> \stemDown dis8 ) r16 \stemDown e16 -. | % 236
    \stemDown c'4 ( -> \stemDown b8 ) r16 \stemDown c16 -. \stemDown a4
    ( -> \stemDown g8 ) r16 \stemDown a16 -. | % 237
    \stemDown e8 -. r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown b16
    ( \stemDown e,8 ) r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown
    a16 ( \pageBreak | % 238
    \stemDown b2 ) ~ -> \stemDown b8 \stemDown a16 ( \stemDown g16 \once
    \omit TupletBracket
    \times 4/6  {
        \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown c16
        \stemDown b16 \stemDown a16 }
    | % 239
    \stemUp g8 ) r8 \stemDown <d' fis a>8 r8 \stemDown <g, d' b'>8 r8
    \stemDown <a d a'>8 r8 | \barNumberCheck #240
    \stemDown <g g'>8 -> \stemDown c8 ~ ^> \stemDown c2 \stemUp b8 ( -.
    r16 \stemUp a16 ) -. | % 241
    \stemDown <g g'>8 r8 \acciaccatura { \stemUp a8 ( } \stemUp g8 ) (
    -. r16 \stemUp fis16 ) -. \stemUp g8 -. r8 \stemDown <a d a'>8 r8 | % 242
    \stemDown <g g'>2. -> \stemDown b8 ( -. r16 \stemDown d16 ) -.
    \pageBreak | % 243
    \stemDown e8 r8 \acciaccatura { \stemUp a8 ( } \stemDown g8 ) -. r16
    \stemDown fis16 -. \stemDown g8 r8 \stemDown <a, d a'>8 r8 | % 244
    \stemDown <g g'>2. -> \stemDown b8 ( -. r16 \stemDown d16 ) -. | % 245
    \stemDown es4 ( -> \stemDown d8 ) r16 \stemDown c16 -. \stemUp bes8
    -. r8 \stemDown f'8 ( -. r16 \stemDown fis16 ) -. | % 246
    \stemDown g4 ( -> \stemDown f8 ) r16 \stemDown es16 -. \stemDown d8
    -. r8 \stemDown g8 ( -. r16 \stemDown a16 ) -. | % 247
    \stemDown b2. -> \stemDown a8 ( r16 \stemDown b,16 ) -. \pageBreak | % 248
    \stemDown g'2. -> \stemDown fis8 ( r16 \stemDown b,16 ) -. | % 249
    \stemDown e4 ( -> \stemDown d8 ) r16 \stemDown e16 -. \stemDown <c
        e>4 ( -> \stemDown <b e>8 ) r16 \stemDown e16 -. |
    \barNumberCheck #250
    \stemDown <a, e'>4 ( -> \stemUp <g e'>8 ) r16 \stemUp g16 -. \stemUp
    <g e'>4 ( -> \stemUp <gis d'>8 ) r16 \stemUp gis16 -. | % 251
    \stemDown c8 r8 r4 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp es,8 \stemUp es8 \stemUp es8 }
    | % 252
    \stemUp es2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp d8 \stemUp d8 \stemUp d8 }
    | % 253
    \stemUp d2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis8 \stemUp cis8 \stemUp cis8 }
    \pageBreak | % 254
    \stemUp cis8 r8 \stemUp d8 r8 \stemUp <d b' g'>8 r8 r4 | % 255
    \stemDown <d' fis a>8 \downbow _\fff r8 r4 \stemDown <c e ais>8
    \downbow r8 r4 | % 256
    \stemDown <b dis b'>8 \downbow r8 \stemDown <a e' c'>8 \downbow r8 r8
    \stemUp e8 _\f ^ "pizz." \stemUp f8 \stemUp fis8 | % 257
    \stemUp g8 _\< \stemUp a8 \stemUp ais8 \stemUp b8 \stemDown c8
    \stemDown cis8 \stemDown d8 \stemDown dis8 | % 258
    \stemDown e8 _\! _\ff _\> \stemDown d8 \stemDown c8 \stemDown b8
    \stemUp a8 \stemUp g8 \stemUp fis8 r8 _\! \pageBreak | % 259
    \stemDown <d' fis a>8 \downbow _\fff ^ "arco" r8 r4 \stemDown <c e
        ais>8 \downbow r8 r4 | \barNumberCheck #260
    \stemDown <b dis b'>8 \downbow r8 \stemDown <a e' c'>8 \downbow r8 r8
    \stemUp cis,8 _\f ^ "pizz." \stemUp d8 \stemUp dis8 | % 261
    \stemUp e8 _\< \stemUp fis8 \stemUp g8 \stemUp gis8 \stemUp a8
    \stemUp ais8 \stemUp b8 \stemUp d8 | % 262
    \stemUp c8 _\! _\ff _\> \stemUp b8 \stemUp a8 \stemUp g8 \stemUp fis8
    \stemUp e8 \stemUp dis8 r8 _\! | % 263
    \stemDown <d' fis a>8 \downbow _\fff r8 r4 \stemDown <c e ais>8
    \downbow r8 r4 \pageBreak | % 264
    \stemDown <b dis b'>8 \downbow r8 \stemDown <a e' c'>8 \downbow r8 r8
    \stemUp e8 _\f ^ "pizz." \stemUp f8 \stemUp fis8 | % 265
    \stemUp g8 _\< \stemUp a8 \stemUp ais8 \stemUp b8 \stemDown c8
    \stemDown cis8 \stemDown d8 \stemDown dis8 | % 266
    \stemDown e8 _\! _\ff _\> \stemDown d8 \stemDown c8 \stemDown b8
    \stemUp a8 \stemUp g8 \stemUp fis8 r8 _\! | % 267
    \stemDown <d' fis a>8 _\fff ^ "arco" r8 r4 \stemDown <c e ais>8 r8 r4
    | % 268
    \stemDown <b dis b'>8 r8 r4 \stemDown <c g'>8 r8 r4 \pageBreak | % 269
    \stemDown <cis e a>8 r8 r4 \stemDown <g d' b'>8 r8 r4 |
    \barNumberCheck #270
    \stemDown <b a'>8 r8 r4 \stemDown <b gis'>8 r8 r4 | % 271
    \stemDown <f c' f a>8 r8 r4 \stemUp <fis a d>8 r8 r4 | % 272
    \stemDown <g es' bes'>8 r8 r4 \stemDown <gis e' b'>8 r8 r4 | % 273
    \stemUp a4 :16 \stemUp bes4 :16 \stemUp b4 :16 \stemDown c4 :16
    \pageBreak | % 274
    \stemDown cis4 :16 \stemDown d4 :16 \stemUp <a e'>8 \stemUp c,16
    _\fff \stemUp c16 \stemUp c4 :16 | % 275
    c1 :16 | % 276
    c1 :16 | % 277
    c1 :16 | % 278
    c1 :16 | % 279
    c1 :16 | \barNumberCheck #280
    c1 :16 \pageBreak | % 281
    c1 :16 | % 282
    \stemUp c2 :16 \stemUp c8 r8 \stemDown d'16 ( _\fff \stemDown dis16
    \stemDown e16 \stemDown fis16 | % 283
    \stemDown g8 ) r8 \stemDown <d fis a>8 r8 \stemDown <g, d' b'>8 r8
    \stemDown <a d a'>8 r8 | % 284
    \stemDown <g g'>8 -> \stemDown c8 ~ ^> \stemDown c2 \stemUp b8 ( -.
    r16 \stemUp a16 ) -. | % 285
    \stemDown <g g'>8 r8 \acciaccatura { \stemUp a8 ( } \stemUp g8 ) (
    -. r16 \stemUp fis16 ) -. \stemUp g8 -. r8 \stemDown <a d a'>8 r8 | % 286
    \stemDown <g g'>2. -> \stemDown b8 ( -. r16 \stemDown d16 ) -.
    \pageBreak | % 287
    \stemDown e8 r8 \acciaccatura { \stemUp a8 ( } \stemDown g8 ) -. r16
    \stemDown fis16 -. \stemDown g8 r8 \stemDown <a, d a'>8 r8 | % 288
    \stemDown <g g'>2. -> \stemDown b8 ( -. r16 \stemDown d16 ) -. | % 289
    \stemDown g4 ( -> \stemDown fis8 ) r16 \stemDown g16 -. \stemDown e4
    ( -> \stemDown dis8 ) r16 \stemDown e16 -. | \barNumberCheck #290
    \stemDown c'4 ( -> \stemDown b8 ) r16 \stemDown c16 -. \stemDown a4
    ( -> \stemDown g8 ) r16 \stemDown a16 -. | % 291
    \stemDown e8 -. r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown b16
    ( \stemDown e,8 ) r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown
    a16 ( \pageBreak | % 292
    \stemDown b2 ) ~ -> \stemDown b8 \stemDown a16 ( \stemDown g16 \once
    \omit TupletBracket
    \times 4/6  {
        \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown c16
        \stemDown b16 \stemDown a16 }
    | % 293
    \stemUp g8 ) r8 \stemDown <d' fis a>8 r8 \stemDown <g, d' b'>8 r8
    \stemDown <a d a'>8 r8 | % 294
    \stemDown <g g'>8 -> \stemDown c8 ~ ^> \stemDown c2 \stemUp b8 ( -.
    r16 \stemUp a16 ) -. | % 295
    \stemDown <g g'>8 r8 \acciaccatura { \stemUp a8 ( } \stemUp g8 ) (
    -. r16 \stemUp fis16 ) -. \stemUp g8 -. r8 \stemDown <a d a'>8 r8 | % 296
    \stemDown <g g'>2. -> \stemDown b8 ( -. r16 \stemDown d16 ) -.
    \pageBreak | % 297
    \stemDown e8 r8 \acciaccatura { \stemUp a8 ( } \stemDown g8 ) -. r16
    \stemDown fis16 -. \stemDown g8 r8 \stemDown <a, d a'>8 r8 | % 298
    \stemDown <g g'>2. -> \stemDown b8 ( -. r16 \stemDown d16 ) -. | % 299
    \stemDown es4 ( -> \stemDown d8 ) r16 \stemDown c16 -. \stemUp bes8
    -. r8 \stemDown f'8 ( -. r16 \stemDown fis16 ) -. | \barNumberCheck
    #300
    \stemDown g4 ( -> \stemDown f8 ) r16 \stemDown es16 -. \stemDown d8
    -. r8 \stemDown g8 ( -. r16 \stemDown a16 ) -. | % 301
    \stemDown b2. -> \stemDown a8 ( r16 \stemDown b,16 ) -. \pageBreak | % 302
    \stemDown g'2. -> \stemDown fis8 ( r16 \stemDown b,16 ) -. | % 303
    \stemDown e4 ( -> \stemDown d8 ) r16 \stemDown e16 -. \stemDown <c
        e>4 ( -> \stemDown <b e>8 ) r16 \stemDown e16 -. | % 304
    \stemDown a4 ( -> _\sempre _\fff \stemDown g8 ) r16 \stemDown e16 -.
    \stemDown a4 ( -> \stemDown g8 ) r16 \stemDown es16 -. | % 305
    \stemDown a4 ( -> \stemDown g8 ) r16 \stemDown d16 -. \stemDown a'4
    ( -> \stemDown g8 ) r16 \stemDown cis,16 -. | % 306
    \stemDown a'4 ( -> \stemDown g8 ) r16 \stemDown c,16 -. \stemDown a'4
    ( -> \stemDown g8 ) r16 \stemDown cis,16 -. | % 307
    \stemDown a'4 ( -> \stemDown g8 ) r16 \stemDown d16 -. \stemDown a'4
    ( -> \stemDown g8 ) r16 \stemDown dis16 -. \pageBreak | % 308
    \stemDown b'4 ( -> \stemDown a8 ) r16 \stemDown e16 -. \stemDown c'4
    ( -> \stemDown b8 ) r16 \stemDown e,16 -. | % 309
    \stemDown d'4 ( -> \stemDown c8 ) r16 \stemDown a16 -. \stemDown d4
    ( -> \stemDown cis8 ) r16 \stemDown a16 -. | \barNumberCheck #310
    \stemDown e'4 ( -> \stemDown d8 ) r16 \stemDown a16 -. \stemDown e'4
    ( -> \stemDown dis8 ) r16 \stemDown a16 -. | % 311
    \stemDown f'4 ( -> \stemDown e8 ) r16 \stemDown a,16 -. \stemDown g'4
    ( -> \stemDown fis8 ) r16 \stemDown c16 -. | % 312
    \stemDown a8 :16 _\ffff \stemDown g8 :16 \stemDown d8 :16 \stemDown
    g8 :16 \stemDown a8 :16 \stemDown g8 :16 \stemDown es8 :16 \stemDown
    g8 :16 | % 313
    \stemDown a8 :16 \stemDown g8 :16 \stemDown e8 :16 \stemDown g8 :16
    \stemDown a8 :16 \stemDown g8 :16 \stemDown es8 :16 \stemDown g8 :16
    \pageBreak | % 314
    \stemDown a8 :16 \stemDown g8 :16 \stemDown fis8 :16 \stemDown e8
    :16 \stemDown d8 :16 \stemDown cis'8 :16 \stemDown c8 :16 \stemDown
    b8 :16 | % 315
    \stemDown a8 :16 \stemDown g8 :16 \stemDown fis8 :16 \stemDown e8
    :16 \stemDown d8 r8 r4 | % 316
    r4 \stemUp c,4 :16 _\p _\< \stemUp d4 :16 \stemUp dis4 :16 | % 317
    \stemUp e4 :16 \stemUp fis4 :16 \stemUp g4 :16 \stemUp a4 :16 | % 318
    \stemUp b4 :16 _\! _\mf _\< \stemUp c,4 :16 \stemUp d4 :16 \stemUp
    dis4 :16 | % 319
    \stemUp e4 :16 \stemUp fis4 :16 \stemUp g4 :16 \stemUp a4 :16
    \pageBreak | \barNumberCheck #320
    \stemUp b4 :16 _\! _\f _\< \stemDown c4 :16 \stemDown d4 :16
    \stemDown dis4 :16 | % 321
    \stemDown e4 :16 \stemDown fis4 :16 \stemDown g4 :16 \stemDown a4
    :16 | % 322
    \stemUp b,4 :16 _\! _\ff _\< \stemDown c4 :16 \stemDown d4 :16
    \stemDown dis4 :16 | % 323
    \stemDown e4 :16 \stemDown fis4 :16 \stemDown g4 :16 \stemDown a4
    :16 | % 324
    \stemDown <dis, b'>8 _\! _\fff r8 \once \omit TupletBracket
    \times 4/7  {
        \stemDown g,16*161/160 ( \stemDown a16*161/160 \stemDown b16*161/160
        \stemDown cis16*161/160 \stemDown dis16*161/160 \stemDown e16*161/160
        \stemDown fis16*161/160 }
    \stemDown g8 ) r16 \stemDown fis16 ( \stemDown g8 ) r16 \stemDown
    dis16 ( \pageBreak | % 325
    \stemDown e8 ) r8 \once \omit TupletBracket
    \times 4/7  {
        \stemDown c16*161/160 ( \stemDown d16*161/160 \stemDown e16*161/160
        \stemDown fis16*161/160 \stemDown gis16*161/160 \stemDown a16*161/160
        \stemDown b16*161/160 }
    \stemDown c8 ) r16 \stemDown b16 ( \stemDown c8 ) r16 \stemDown gis16
    ( | % 326
    \stemDown a8 ) r8 r4 r4 \stemUp g,4 ~ \stemUp es'4 ~ | % 327
    \stemUp g,8 \stemUp es'8 r8 r4 r4 \stemUp e,4 ~ \stemUp c'4 ~
    \pageBreak | % 328
    \stemUp e,8 \stemUp c'8 r8 \stemUp e,4 ~ \stemUp cis'4 ~ \stemUp e,8
    \stemUp cis'8 r8 \stemUp d,4 ~ \stemUp a'4 ~ | % 329
    \stemUp d,8 \stemUp a'8 r8 \stemDown a'16 \stemDown g'16 \stemDown
    fis16 \stemDown e16 \stemDown d16 \stemDown c16 \stemDown b16
    \stemDown a16 \stemDown g16 \stemDown fis16 \stemDown e16 \stemDown
    d16 | \barNumberCheck #330
    \stemDown d8 _\sempre _\fff \stemDown b'8 r8 \stemDown d,8 \stemDown
    a'8 r8 \stemDown b,8 \stemDown g'8 r8 \stemDown c,8 \stemDown g'8 r8
    | % 331
    \stemDown b,8 -> \stemDown g'8 \stemDown d'8 ^> r4 r4 \stemUp d,16 (
    \stemUp c16 \stemUp b16 \stemUp a16 ) \pageBreak | % 332
    \stemDown g8 \stemDown d'8 \stemDown b'8 r8 \stemDown d,8 \stemDown
    a'8 r8 \stemDown b,8 \stemDown g'8 r8 \stemDown c,8 \stemDown g'8 r8
    | % 333
    \stemDown b,8 -> \stemDown g'8 \stemDown d'8 ^> r4 r4 \stemUp d,16 (
    \stemUp c16 \stemUp b16 \stemUp a16 | % 334
    \stemUp g16 ) \stemUp a16 -. \stemUp b16 -. \stemUp c16 -. \stemUp d16
    -. \stemUp c16 -. \stemUp b16 -. \stemUp a16 -. \stemUp g16 -.
    \stemUp a16 -. \stemUp b16 -. \stemUp c16 -. \stemUp d16 -. \stemUp
    c16 -. \stemUp b16 -. \stemUp a16 -. | % 335
    \stemUp g16 -. \stemUp a16 -. \stemUp b16 -. \stemUp c16 -. \stemUp
    d16 -. \stemUp c16 -. \stemUp b16 -. \stemUp a16 -. \stemUp g16 -.
    \stemUp a16 -. \stemUp b16 -. \stemUp c16 -. \stemUp d16 -. \stemUp
    c16 -. \stemUp b16 -. \stemUp a16 -. \pageBreak | % 336
    \stemUp g16 \stemUp a16 \stemUp b16 \stemUp c16 \stemDown d8 r8
    \stemUp g,16 \stemUp a16 \stemUp b16 \stemUp c16 \stemDown d8 r8 | % 337
    \stemUp g,16 \stemUp a16 \stemUp b16 \stemUp c16 \stemDown d8 r8
    \stemUp g,16 \stemUp a16 \stemUp b16 \stemUp c16 \stemDown d8 r8 | % 338
    r8 \stemDown g8 :16 \stemDown fis8 :16 \stemDown e8 :16 \stemUp d8
    :16 \stemUp c8 :16 \stemUp b8 :16 \stemUp a8 :16 | % 339
    \stemDown g8 :16 \stemDown fis'8 :16 \stemDown e8 :16 \stemDown es8
    :16 \stemUp d8 :16 \stemUp c8 :16 \stemUp b8 :16 \stemUp a8 :16 |
    \barNumberCheck #340
    \stemUp g8 r8 r4 \stemDown d'8 \stemDown fis8 \stemDown a8 r8 r4
    \pageBreak | % 341
    \stemDown b,8 \stemDown g'8 \stemDown d'8 r8 r4 \stemDown a,8
    \stemDown fis'8 \stemDown a8 r8 r4 | % 342
    \stemDown g,8 \stemDown d'8 \stemDown b'8 r8 \stemDown g,8 \stemDown
    d'8 \stemDown b'8 r8 r4 \stemDown g,8 \stemDown d'8 \stemDown b'8 r8
    | % 343
    r4 \stemDown g,8 \stemDown d'8 \stemDown b'8 r8 r4 \stemDown g,8
    \stemDown d'8 \stemDown b'8 r8 | % 344
    \stemDown g,8 \stemDown d'8 \stemDown b'8 r8 \stemDown g,8 \stemDown
    d'8 \stemDown b'8 r8 \stemUp g,8 \stemUp d'8 r8 \stemUp g,8 \stemUp
    d'8 r8 | % 345
    d,1 ~ g1 ~ | % 346
    \stemUp d2. \stemUp g2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp d8 \stemUp g8 \stemUp d8 \stemUp g8 \stemUp d8 }
    \stemUp g8*2/3 | % 347
    \stemUp d8 \stemUp g8 r8 r4 r2 \bar "|."
    }

PartPThreeZeroVoiceOne =  \relative b {
    \clef "bass" \time 4/4 \key g \major | % 1
    R1*4 \pageBreak | % 5
    R1*2 | % 7
    \numericTimeSignature\time 4/4  R1 \bar "||"
    R1*2 \pageBreak | \barNumberCheck #10
    \numericTimeSignature\time 4/4  R1*2 | % 12
    \numericTimeSignature\time 4/4  R1*3 \break | % 15
    R1*5 \pageBreak | \barNumberCheck #20
    R1*4 \break | % 24
    R1*3 | % 27
    \numericTimeSignature\time 4/4  R1 \pageBreak | % 28
    R1*4 \pageBreak | % 32
    R1*4 \pageBreak | % 36
    \numericTimeSignature\time 4/4  R1 | % 37
    \numericTimeSignature\time 4/4  R1*4 \pageBreak | % 41
    R1*5 \pageBreak | % 46
    R1*5 \pageBreak | % 51
    \time 12/8 \omit Staff.TimeSignature \stemDown b8 -. ^ "unis." r8*2/3
    r8*2/3 r4.*2/3 \stemDown dis,8 ( \stemDown e8 \stemDown fis8 )
    \stemDown gis8 ( \stemDown fis8 \stemDown e8 s1*5/24 | % 52
    \stemDown dis8 ) r8*2/3 r8*2/3 r4.*2/3 \stemUp ais8 ( _\ff \stemUp b8
    \stemUp cis8 ) \stemUp b8 ( \stemUp ais8 \stemUp gis8 ) s1*5/24 | % 53
    \stemUp dis'8 -. _\pp _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemUp b8 -. \stemUp dis8 -. \stemUp b8 -. \stemUp
    dis8 -. \stemUp b8 -. \stemDown e8 -. \stemDown cis8 -. \stemDown e8
    -. \stemDown cis8 -. \stemDown e8 -. \stemDown cis8 -. | % 54
    \stemDown fis8 -. \stemDown dis8 -. \stemDown fis8 -. \stemDown dis8
    -. \stemDown fis8 -. \stemDown dis8 -. \stemDown ais'8 -. \stemDown
    e8 -. \stemDown ais8 -. \stemDown e8 -. \stemDown ais8 -. \stemDown
    e8 -. | % 55
    \stemDown b'8 -. \stopTrillSpan _\mp _\< \stemDown fis8 -. \stemDown
    b8 -. \stemDown fis8 -. \stemDown b8 -. \stemDown fis8 -. \stemDown
    gis8 -. \stemDown fis8 -. \stemDown gis8 -. \stemDown fis8 -.
    \stemDown gis8 -. \stemDown fis8 -. \pageBreak | % 56
    \stemDown fis8 -. \stemDown dis8 -. \stemDown fis8 -. \stemDown dis8
    -. \stemDown fis8 -. \stemDown dis8 -. \stemDown ais'8 -. _\! _\f
    \stemDown e8 -. \stemDown ais8 -. \stemDown e8 -. \stemDown ais8 -.
    \stemDown e8 -. | % 57
    \stemUp dis8 -. _\pp _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemUp b8 -. \stemUp dis8 -. \stemUp b8 -. \stemUp
    dis8 -. \stemUp b8 -. \stemDown e8 -. \stemDown cis8 -. \stemDown e8
    -. \stemDown cis8 -. \stemDown e8 -. \stemDown cis8 -. | % 58
    \stemDown fis8 -. \stemDown dis8 -. \stemDown fis8 -. \stemDown dis8
    -. \stemDown fis8 -. \stemDown dis8 -. \stemDown ais'8 -. \stemDown
    e8 -. \stemDown ais8 -. \stemDown e8 -. \stemDown ais8 -. \stemDown
    e8 -. | % 59
    \stemDown b'8 -. \stopTrillSpan _\mp _\< \stemDown fis8 -. \stemDown
    b8 -. \stemDown fis8 -. \stemDown b8 -. \stemDown fis8 -. \stemDown
    gis8 -. \stemDown fis8 -. \stemDown gis8 -. \stemDown fis8 -.
    \stemDown gis8 -. \stemDown fis8 -. | \barNumberCheck #60
    \stemDown fis8 -. \stemDown dis8 -. \stemDown fis8 -. \stemDown dis8
    -. \stemDown fis8 -. \stemDown dis8 -. \stemDown ais'8 -. _\! _\f
    \stemDown e8 -. \stemDown ais8 -. \stemDown e8 -. \stemDown ais8 -.
    \stemDown e8 -. \pageBreak | % 61
    \stemDown a8 -. _\p _\markup{ \small\italic {cresc. poco a poco} }
    \startTrillSpan \stemDown fis8 -. \stemDown a8 -. \stemDown fis8 -.
    \stemDown a8 -. \stemDown fis8 -. \stemDown a8 -. \stemDown fis8 -.
    \stemDown a8 -. \stemDown fis8 -. \stemDown a8 -. \stemDown fis8 -.
    | % 62
    \stemDown g8 -. \stemDown e8 -. \stemDown g8 -. \stemDown e8 -.
    \stemDown g8 -. \stemDown e8 -. \stemDown g8 -. \stemDown e8 -.
    \stemDown g8 -. \stemDown e8 -. \stemDown g8 -. \stemDown e8 -. | % 63
    \stemDown a8 -. \stemDown fis8 -. \stemDown a8 -. \stemDown fis8 -.
    \stemDown a8 -. \stemDown fis8 -. \stemDown a8 -. \stemDown fis8 -.
    \stemDown a8 -. \stemDown fis8 -. \stemDown a8 -. \stemDown fis8 -.
    | % 64
    \stemDown b8 -. \stemDown g8 -. \stemDown b8 -. \stemDown g8 -.
    \stemDown b8 -. \stemDown g8 -. \stemDown b8 -. \stemDown g8 -.
    \stemDown b8 -. \stemDown g8 -. \stemDown b8 -. \stemDown g8 -. | % 65
    \stemDown dis'8 -. \stemDown a8 -. \stemDown dis8 -. \stemDown a8 -.
    \stemDown dis8 -. \stemDown a8 -. \stemDown dis8 -. \stemDown a8 -.
    \stemDown dis8 -. \stemDown a8 -. \stemDown dis8 -. \stemDown a8 -.
    \pageBreak | % 66
    \stemDown e'8 -. \stemDown c8 -. \stemDown e8 -. \stemDown c8 -.
    \stemDown e8 -. \stemDown c8 -. \stemDown e8 -. \stemDown c8 -.
    \stemDown e8 -. \stemDown c8 -. \stemDown e8 -. \stemDown c8 -. | % 67
    \clef "tenor" \stemDown a'8 -. \stopTrillSpan _\f _\< \stemDown dis,8
    -. \stemDown a'8 -. \stemDown dis,8 -. \stemDown a'8 -. \stemDown
    dis,8 -. \stemDown a'8 -. \stemDown dis,8 -. \stemDown a'8 -.
    \stemDown dis,8 -. \stemDown a'8 -. \stemDown dis,8 -. | % 68
    \stemDown b'8 -. \stemDown g8 -. \stemDown b8 -. \stemDown g8 -.
    \stemDown b8 -. \stemDown g8 -. \stemDown b8 -. \stemDown g8 -.
    \stemDown b8 -. \stemDown g8 -. \stemDown b8 -. \stemDown g8 -. | % 69
    \stemDown b,8 -> _\! _\ff r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 |
    \barNumberCheck #70
    r4.*2/3 \clef "bass" \stemDown cis8 -. _\mf _\> \stemDown dis8 -.
    \stemDown cis8 -. \stemDown b8 -. \stemDown cis8 -. \stemDown b8 -.
    \stemDown a8 -. \stemDown b8 -. \stemDown a8 -. \bar "||"
    s8 _\! \pageBreak | % 71
    \key e \major \stemDown gis8 -. _\pp \stemDown a8 -. \stemDown gis8
    -. \stemDown fis8 -. \stemDown gis8 -. \stemDown fis8 -. \stemDown e8
    -. \stemDown fis8 -. \stemDown e8 -. \stemDown dis8 -. \stemDown e8
    -. \stemDown dis8 -. | % 72
    \stemUp cis8 -. \stemUp dis8 -. \stemUp cis8 -. \stemUp c8 -.
    \stemUp d8 -. \stemUp c8 -. \stemUp b8 -. \stemUp cis8 -. \stemUp b8
    -. \stemDown a'8 -. \stemDown b8 -. \stemDown a8 -. | % 73
    \stemDown gis8 -. \stemDown a8 -. \stemDown gis8 -. \stemDown fis8
    -. \stemDown gis8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8
    -. | % 74
    \stemUp cis8 -. _\sempre _\pp \stemUp dis8 -. \stemUp cis8 -.
    \stemUp c8 -. \stemUp d8 -. \stemUp c8 -. \stemUp b8 -. \stemUp ais8
    -. \stemUp b8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown gis8 -.
    | % 75
    \stemDown g8 -. \stemDown a8 -. \stemDown g8 -. \stemDown fis8 -.
    \stemDown gis8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8
    -. \break | % 76
    \stemUp cis8 -. \stemUp dis8 -. \stemUp cis8 -. \stemUp c8 -.
    \stemUp d8 -. \stemUp c8 -. \stemUp b8 -. \stemUp c8 -. \stemUp b8
    -. \stemUp b8 -. \stemUp a8 -. \stemUp gis8 -. | % 77
    \numericTimeSignature\time 4/4  \stemUp gis8 _\p r8 r4 \stemUp cis8
    r8 r4 | % 78
    \stemDown e8 r8 r4 \stemUp a,8 :16 _\p \stemUp b8 :16 \stemUp cis8
    :16 \stemUp dis8 :16 | % 79
    \stemUp e8 :16 _\< \stemUp dis8 :16 \stemUp cis8 :16 \stemUp b8 :16
    \stemDown ais8 :16 \stemDown a8 :16 \stemDown gis'8 :16 _\! _\mf
    \stemDown fis8 :16 | \barNumberCheck #80
    \stemDown e4 ~ _\< \stemDown e8 \stemDown e16 \stemDown e16
    \stemDown dis'8 _\! _\f \stemDown dis8 r4 \pageBreak | % 81
    \time 12/8  \stemDown gis,8 -. _\pp \stemDown a8 -. \stemDown gis8
    -. \stemDown fis8 -. \stemDown gis8 -. \stemDown fis8 -. \stemDown e8
    -. \stemDown fis8 -. \stemDown e8 -. \stemDown dis8 -. \stemDown e8
    -. \stemDown dis8 -. | % 82
    \stemUp cis8 -. \stemUp dis8 -. \stemUp cis8 -. \stemUp c8 -.
    \stemUp d8 -. \stemUp c8 -. \stemUp b8 -. \stemUp cis8 -. \stemUp b8
    -. \stemDown a'8 -. \stemDown b8 -. \stemDown a8 -. | % 83
    \stemDown gis8 -. _\markup{ \small\italic {un poco cresc.} }
    \startTrillSpan \stemDown a8 -. \stemDown gis8 -. \stemDown fis8 -.
    \stemDown gis8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8
    -. | % 84
    \stemUp cis8 -. \stemUp dis8 -. \stemUp cis8 -. \stemUp c8 -.
    \stemUp d8 -. \stemUp c8 -. \stemUp b8 -. \stemUp ais8 -. \stemUp b8
    -. \stemDown e8 -. \stemDown fis8 -. \stemDown gis8 -. | % 85
    \stemDown g8 -. \stemDown a8 -. \stemDown g8 -. \stemDown fis8 -.
    \stemDown gis8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8
    -. \pageBreak | % 86
    \stemUp cis8 -. \stemUp dis8 -. \stemUp cis8 -. \stemUp c8 -.
    \stemUp d8 -. \stemUp c8 -. \stemUp b8 -. \stemUp ais8 -. \stemUp b8
    -. r4.*2/3 s8 \stopTrillSpan | % 87
    \numericTimeSignature\time 4/4  \stemUp c16 _\mf _\markup{
        \small\italic {cresc.} } \startTrillSpan \stemUp c16 \stemUp d16
    \stemUp d16 \stemDown e16 \stemDown e16 \stemDown f16 \stemDown f16
    \stemDown g16 \stemDown g16 \stemDown a16 \stemDown a16 \stemDown
    ais16 \stemDown ais16 \stemDown b16 \stemDown b16 | % 88
    \stemDown c16 \stemDown c16 \stemDown d16 \stemDown d16 \stemDown e16
    \stemDown e16 \stemDown f16 \stemDown f16 \stemDown g,16 \stemDown g16
    \stemDown gis16 \stemDown gis16 r4 \stopTrillSpan | % 89
    r4 \stemUp gis,8 _\f r16 \stemUp a16 \stemUp ais4 \stemUp bis4
    \pageBreak | \barNumberCheck #90
    \stemUp cis4 \stemUp ais8 r16 \stemUp bis16 \stemUp cis4 \stemDown
    dis4 | % 91
    \stemDown e4 _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown eis4 \stemDown fis4 \stemDown gis4 | % 92
    \stemUp a,4 \stemUp ais4 \stemUp b4 \stemUp cis4 | % 93
    \stemDown d8 \stopTrillSpan _\ff r8 r4 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <c, c'>8 \stemUp <c c'>8 \stemUp <c c'>8 }
    | % 94
    \stemUp <c c'>2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp b'8 \stemUp b8 \stemUp b8 }
    | % 95
    \stemUp b2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp bes8 \stemUp bes8 \stemUp bes8 }
    \pageBreak | % 96
    \stemUp bes8 r8 \stemUp b8 r8 \stemDown e8 r8 r4 | % 97
    \stemDown b'2 \downbow _\ff \stemDown a2 \downbow | % 98
    \stemDown gis8 \downbow r8 \stemDown fis8 \downbow r8 r8 \stemUp
    cis,8 _\p ^ "pizz." \stemUp d8 \stemUp dis8 | % 99
    \stemUp e8 _\< \stemUp fis8 \stemUp g8 \stemUp gis8 \stemUp a8
    \stemUp ais8 \stemUp b8 \stemUp bis8 | \barNumberCheck #100
    \stemUp cis8 _\! _\mf _\> \stemUp b8 \stemUp a8 \stemUp gis8 \stemUp
    fis8 \stemUp e8 \stemUp dis8 r8 _\! | % 101
    \stemDown b''2 \downbow _\ff ^ "arco" \stemDown a2 \downbow \break | % 102
    \stemDown gis8 \downbow r8 \stemDown fis8 \downbow r8 r8 \stemUp
    ais,8 _\p ^ "pizz." \stemUp b8 \stemUp bis8 | % 103
    \stemDown cis8 _\< \stemDown dis8 \stemDown e8 \stemDown eis8
    \stemDown fis8 \stemDown fisis8 \stemDown gis8 \stemDown b8 | % 104
    \stemDown a8 _\! _\mf _\> \stemDown gis8 \stemDown fis8 \stemDown e8
    \stemUp dis8 \stemUp cis8 \stemUp bis8 r8 _\! | % 105
    \stemDown b'2 \downbow _\ff ^ "arco" \stemDown a2 \downbow | % 106
    \stemDown gis8 r8 \stemDown fis8 r8 r8 \stemUp cis,8 _\p ^ "pizz."
    \stemUp d8 \stemUp dis8 \pageBreak | % 107
    \stemUp e8 _\< \stemUp fis8 \stemUp g8 \stemUp gis8 \stemUp a8
    \stemUp ais8 \stemUp b8 \stemUp bis8 | % 108
    \stemUp cis8 _\! _\mf _\> \stemUp b8 \stemUp a8 \stemUp gis8 \stemUp
    fis8 \stemUp e8 \stemUp dis8 r8 _\! | % 109
    \stemDown b''2 \downbow _\ff ^ "arco" \stemDown a2 \downbow |
    \barNumberCheck #110
    \stemDown gis2 \downbow \stemDown g2 \downbow | % 111
    \stemDown fis8 \downbow r8 \stemDown e8 \downbow r8 \stemDown fis8
    \downbow r8 \stemDown e8 \downbow r8 | % 112
    \stemDown a8 \downbow r8 \stemDown a8 \downbow r8 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown b8 -. _\pp \stemDown cis8 -. \stemDown b8 -. }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 -. \stemDown b8 -. \stemDown a8 -. }
    \break | % 113
    \time 12/8  \stemDown gis8 -. \stemDown a8 -. \stemDown gis8 -.
    \stemDown fis8 -. \stemDown gis8 -. \stemDown fis8 -. \stemDown e8
    -. \stemDown fis8 -. \stemDown e8 -. \stemDown dis8 -. \stemDown e8
    -. \stemDown dis8 -. | % 114
    \stemUp cis8 -. \stemUp dis8 -. \stemUp cis8 -. \stemUp c8 -.
    \stemUp d8 -. \stemUp c8 -. \stemUp b8 -. \stemUp cis8 -. \stemUp b8
    -. \stemDown a'8 -. \stemDown b8 -. \stemDown a8 -. | % 115
    \stemDown gis8 -. \stemDown a8 -. \stemDown gis8 -. \stemDown fis8
    -. \stemDown gis8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8
    -. | % 116
    \stemUp cis8 -. _\sempre _\pp \stemUp dis8 -. \stemUp cis8 -.
    \stemUp c8 -. \stemUp d8 -. \stemUp c8 -. \stemUp b8 -. \stemUp ais8
    -. \stemUp b8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown gis8 -.
    | % 117
    \stemDown g8 -. \stemDown a8 -. \stemDown g8 -. \stemDown fis8 -.
    \stemDown gis8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8
    -. \pageBreak | % 118
    \stemUp cis8 -. \stemUp dis8 -. \stemUp cis8 -. \stemUp c8 -.
    \stemUp d8 -. \stemUp c8 -. \stemUp b8 -. \stemUp c8 -. \stemUp b8
    -. \stemUp b8 -. \stemUp a8 -. \stemUp gis8 -. | % 119
    \numericTimeSignature\time 4/4  \stemUp gis8 r8 r4 \stemUp cis8 r8 r4
    | \barNumberCheck #120
    \stemDown e8 r8 r4 \stemUp a,8 :16 _\p \stemUp b8 :16 \stemUp cis8
    :16 \stemUp dis8 :16 | % 121
    \stemUp e8 :16 _\< \stemUp dis8 :16 \stemUp cis8 :16 \stemUp b8 :16
    \stemDown ais8 :16 \stemDown a8 :16 \stemDown gis'8 :16 _\! _\mf
    \stemDown fis8 :16 | % 122
    \stemDown e4 ~ _\< \stemDown e8 \stemDown e16 \stemDown e16
    \stemDown dis'8 _\! _\f \stemDown dis8 r4 \break | % 123
    \time 12/8  \stemDown gis,8 -. _\pp \stemDown a8 -. \stemDown gis8
    -. \stemDown fis8 -. \stemDown gis8 -. \stemDown fis8 -. \stemDown e8
    -. \stemDown fis8 -. \stemDown e8 -. \stemDown dis8 -. \stemDown e8
    -. \stemDown dis8 -. | % 124
    \stemUp cis8 -. \stemUp dis8 -. \stemUp cis8 -. \stemUp c8 -.
    \stemUp d8 -. \stemUp c8 -. \stemUp b8 -. \stemUp cis8 -. \stemUp b8
    -. \stemDown a'8 -. \stemDown b8 -. \stemDown a8 -. | % 125
    \stemDown gis8 -. _\markup{ \small\italic {un poco cresc.} }
    \startTrillSpan \stemDown a8 -. \stemDown gis8 -. \stemDown fis8 -.
    \stemDown gis8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8
    -. | % 126
    \stemUp cis8 -. \stemUp dis8 -. \stemUp cis8 -. \stemUp c8 -.
    \stemUp d8 -. \stemUp c8 -. \stemUp b8 -. \stemUp ais8 -. \stemUp b8
    -. \stemDown e8 -. \stemDown fis8 -. \stemDown gis8 -. | % 127
    \stemDown g8 -. \stemDown a8 -. \stemDown g8 -. \stemDown fis8 -.
    \stemDown gis8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8
    -. \pageBreak | % 128
    \stemUp cis8 -. \stemUp dis8 -. \stemUp cis8 -. \stemUp c8 -.
    \stemUp d8 -. \stemUp c8 -. \stemUp b8 -. \stemUp ais8 -. \stemUp b8
    -. r4.*2/3 s8 \stopTrillSpan | % 129
    \numericTimeSignature\time 4/4  \stemUp e,8 _\f r8 r4 \stemUp g8 r8
    r4 | \barNumberCheck #130
    \stemUp c8 r8 r4 \stemDown g'8 r8 r4 | % 131
    \stemDown c4 ( ^> \stemDown b8 r16 \stemDown a16 ) -. \stemDown g8
    -. r8 \stemDown d'8 ( -. r16 \stemDown dis16 ) -. \pageBreak | % 132
    \stemDown e4 ( ^> \stemDown d8 r16 \stemDown c16 ) -. \stemDown b8
    -. \stemDown g,8 :16 \stemDown a8 :16 \stemDown b8 :16 | % 133
    \stemDown c8 :16 \stemDown d8 :16 \stemDown e8 :16 \stemDown fis8
    :16 \stemUp <g, g'>8 r8 r4 | % 134
    \stemUp c8 r8 r4 \stemDown g'8 r8 r4 | % 135
    \stemDown c4 ( ^> \stemDown b8 r16 \stemDown a16 ) -. \stemDown g8
    -. r8 \stemDown d'8 ( -. r16 \stemDown dis16 ) -. \pageBreak | % 136
    R1*3 \bar "||"
    \key g \major R1 \pageBreak | \barNumberCheck #140
    R1*5 \pageBreak | % 145
    R1*5 \pageBreak | \barNumberCheck #150
    R1*5 \pageBreak | % 155
    R1*4 \break | % 159
    R1*4 \pageBreak | % 163
    R1*4 \pageBreak | % 167
    R1*4 \pageBreak | % 171
    R1*4 \pageBreak | % 175
    R1*5 \pageBreak | \barNumberCheck #180
    R1*4 \pageBreak | % 184
    R1*5 \pageBreak | % 189
    R1*5 \pageBreak | % 194
    \numericTimeSignature\time 4/4  \stemDown b,16 ^ "unis." \stemDown a16
    \stemDown g'16 \stemDown fis16 \stemUp e16 \stemUp d16 \stemUp cis16
    \stemUp b16 \stemUp a8 r8 r4 | % 195
    R1 | % 196
    \stemUp a2 :16 _\pp \stemUp b2 :16 | % 197
    \stemUp c2 :16 \stemUp cis2 :16 | % 198
    \stemDown d2 :16 \stemDown dis2 :16 | % 199
    \stemDown e8 r8 r4 r2 | \barNumberCheck #200
    \stemUp a,2 :16 _\< \stemUp b2 :16 \pageBreak | % 201
    \stemUp c2 :16 _\! \stemUp cis2 :16 | % 202
    \stemDown d8 r8 r4 r2 | % 203
    R1 | % 204
    \stemDown fis2 :16 _\p _\< \stemDown g2 :16 | % 205
    \stemDown eis2 :16 _\! _\mp \stemDown fis2 :16 \pageBreak | % 206
    \stemDown g2 :16 _\markup{ \small\italic {poco a poco cresc.} }
    \startTrillSpan \stemDown gis2 :16 | % 207
    \stemDown a2 :16 \stemDown ais2 :16 | % 208
    \stemDown b2 :16 \stemDown bes2 :16 | % 209
    \stemDown a8 \stopTrillSpan r8 r4 r2 | \barNumberCheck #210
    R1 \pageBreak | % 211
    \clef "tenor" \stemDown cis'8 _\f _\< r8 \stemDown g8 r16 \stemDown
    g16 \stemDown cis8 r8 \stemDown g8 r8 | % 212
    \stemDown d'8 -> _\! _\ff \stemDown g,8 -> r4 \clef "bass" \stemUp
    <a,, e'>2 :16 _\< | % 213
    \stemUp <a f'>2 :16 \stemUp <a fis'>16 \stemUp <a fis'>16 \stemUp a16
    \stemUp a16 \stemUp a4 :16 | % 214
    a1 :16 _\! _\fff | % 215
    a1 :16 \pageBreak | % 216
    a1 :16 | % 217
    a1 :16 | % 218
    a1 :16 | % 219
    a1 :16 | \barNumberCheck #220
    a1 :16 \pageBreak | % 221
    \times 2/3  {
        \stemUp a8 -> \stemUp a8 -> r8 }
    \stemDown d32 ( _\sempre _\fff \stemDown e32 \stemDown fis32
    \stemDown g32 \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32
    ) \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16 )
    \stemDown a16 ( \stemDown g16 \stemDown fis16 \stemDown e16 ) | % 222
    \stemDown d16 ( \stemDown c'16 \stemDown b16 \stemDown a16 )
    \stemDown g16 ( \stemDown fis16 \stemDown e16 \stemDown d16 ) r2 | % 223
    r4 \stemDown d32 ( \stemDown e32 \stemDown fis32 \stemDown g32
    \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32 ) \stemDown
    e16 ( \stemDown d16 \stemDown c16 \stemDown b16 ) \stemDown a16 (
    \stemDown g16 \stemDown fis16 \stemDown e16 ) | % 224
    \stemDown d16 ( \stemDown c'16 \stemDown b16 \stemDown a16 )
    \stemDown g16 ( \stemDown fis16 \stemDown e16 \stemDown d16 ) r2
    \pageBreak | % 225
    r4 \stemDown d32 ( \stemDown e32 \stemDown fis32 \stemDown g32
    \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32 ) \once
    \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemDown fis8 ) r8 | % 226
    r4 \stemDown d32 ( \stemDown e32 \stemDown fis32 \stemDown g32
    \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32 ) \once
    \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemDown fis8 ) r8 | % 227
    r4 \stemDown d32 ( \stemDown e32 \stemDown fis32 \stemDown g32
    \stemDown a32 \stemDown b32 \stemDown c32 \stemDown d32 ) \once
    \omit TupletBracket
    \times 4/6  {
        \stemDown e16 ( \stemDown d16 \stemDown c16 \stemDown b16
        \stemDown a16 \stemDown g16 }
    \stemDown fis8 ) r8 \pageBreak | % 228
    r4 \once \omit TupletBracket
    \times 4/5  {
        \stemDown a16 ( \stemDown g16 \stemDown fis16 \stemDown e16
        \stemDown d16 }
    \stemUp c8 ) r8 \once \omit TupletBracket
    \times 4/6  {
        \stemDown a'16 ( \stemDown g16 \stemDown fis16 \stemDown e16
        \stemDown d16 \stemDown c16 }
    | % 229
    \stemUp b8 ) r8 \stemDown a'8 _\fff r8 \stemDown g8 r8 \stemDown fis8
    r8 | \barNumberCheck #230
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 \stemUp c8 r8 | % 231
    \stemUp b8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis8 r8 | % 232
    \stemUp e8 r8 \stemUp es8 r8 \stemUp d8 r8 r4 \pageBreak | % 233
    \stemDown b''8 r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8 r8
    | % 234
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 r4 | % 235
    \stemUp b8 r8 r4 \stemDown e8 r8 r4 | % 236
    \stemUp <g, g'>8 r8 r4 \stemDown c'8 \stemDown d8 \stemDown e8
    \stemDown fis8 | % 237
    \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown cis8
    \stemDown c8 \stemDown b8 \stemDown a8 \pageBreak | % 238
    \stemDown g4 -> \once \omit TupletBracket
    \times 2/3  {
        \stemUp g,8 \stemUp g8 \stemUp g8 }
    \stemUp b8 \stemUp d8 r4 | % 239
    \stemDown b'8 r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8 r8 |
    \barNumberCheck #240
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 \stemUp c8 r8 | % 241
    \stemUp b8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis8 r8 | % 242
    \stemUp e8 r8 \stemUp es8 r8 \stemUp d8 r8 r4 \pageBreak | % 243
    \stemDown b''8 r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8 r8
    | % 244
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 r4 | % 245
    \stemDown <g, es' bes'>8 r8 r4 \stemDown <bes f' d'>8 r8 r4 | % 246
    \stemDown <es bes' g'>8 r8 r4 \stemUp <g, g'>8 r8 r4 | % 247
    r4 \stemUp b8 r16 \stemUp c16 \stemUp cis8 r8 \stemDown dis8 r8
    \pageBreak | % 248
    \stemDown e8 r8 \stemUp cis8 r16 \stemUp dis16 \stemDown e8 r8
    \stemDown fis8 r8 | % 249
    \stemDown g8 r8 \stemDown gis8 r8 \stemDown a8 r8 \stemDown <b,
        gis'>8 r8 | \barNumberCheck #250
    \stemDown <c a'>8 r8 \stemDown <cis bes'>8 r8 \stemDown <d b'>8 r8
    \stemDown <e b'>8 r8 | % 251
    \stemDown <f a>8 r8 r4 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown es8 \stemDown es8 \stemDown es8 }
    | % 252
    \stemDown es2. \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 }
    | % 253
    \stemDown d2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis8 \stemUp cis8 \stemUp cis8 }
    \pageBreak | % 254
    \stemUp cis8 r8 \stemDown d8 r8 \stemDown <g, d' b'>8 r8 r4 | % 255
    R1 | % 256
    r2 r8 \stemUp e8 _\f ^ "pizz." \stemUp f8 \stemUp fis8 | % 257
    \stemUp g8 _\< \stemUp a8 \stemUp ais8 \stemUp b8 \stemUp c8 \stemUp
    cis8 \stemUp d8 \stemUp dis8 | % 258
    \stemUp e8 _\! _\ff _\> \stemUp d8 \stemUp c8 \stemUp b8 \stemUp a8
    \stemUp g8 \stemUp fis8 r8 _\! \pageBreak | % 259
    R1 | \barNumberCheck #260
    r2 r8 \stemUp cis8 _\f ^ "pizz." \stemUp d8 \stemUp dis8 | % 261
    \stemUp e8 _\< \stemUp fis8 \stemUp g8 \stemUp gis8 \stemUp a8
    \stemUp ais8 \stemUp b8 \stemUp d8 | % 262
    \stemUp c8 _\! _\ff _\> \stemUp b8 \stemUp a8 \stemUp g8 \stemUp fis8
    \stemUp e8 \stemUp dis8 r8 _\! | % 263
    R1 \pageBreak | % 264
    r2 r8 \stemUp e8 _\f ^ "pizz." \stemUp f8 \stemUp fis8 | % 265
    \stemUp g8 _\< \stemUp a8 \stemUp ais8 \stemUp b8 \stemUp c8 \stemUp
    cis8 \stemUp d8 \stemUp dis8 | % 266
    \stemUp e8 _\! _\ff _\> \stemUp d8 \stemUp c8 \stemUp b8 \stemUp a8
    \stemUp g8 \stemUp fis8 r8 _\! | % 267
    \clef "tenor" \stemDown a''8 _\fff ^ "arco" r8 r4 \stemDown fis8 r8
    r4 | % 268
    \stemDown fis8 r8 r4 \stemDown bes,8 r8 r4 \pageBreak | % 269
    \stemDown a8 r8 r4 \stemUp g8 r8 r4 | \barNumberCheck #270
    \clef "bass" \stemDown <fis a>8 r8 r4 \stemDown <e b'>8 r8 r4 | % 271
    \stemDown <es a>8 r8 r4 \stemDown <d a'>8 r8 r4 | % 272
    \stemDown <cis bes'>8 r8 r4 \stemDown <b gis' e'>8 r8 r4 | % 273
    \stemDown a'8 r8 \stemDown as8 r8 \stemDown g8 r8 \stemDown f8 r8
    \pageBreak | % 274
    \stemDown e8 r8 \stemDown d8 r8 \stemUp <c, c'>2 :16 _\fff | % 275
    <c c'>1 :16 | % 276
    <c c'>1 :16 | % 277
    <c c'>1 :16 | % 278
    <c c'>1 :16 | % 279
    <c c'>1 :16 | \barNumberCheck #280
    <c c'>1 :16 \pageBreak | % 281
    <c c'>1 :16 | % 282
    \stemUp <c c'>2 :16 \stemUp <c c'>8 r8 \stemDown c''8 _\fff r8 | % 283
    \stemDown b8 r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8 r8 | % 284
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 \stemUp c8 r8 | % 285
    \stemUp b8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis8 r8 | % 286
    \stemUp e8 r8 \stemUp es8 r8 \stemUp d8 r8 r4 \pageBreak | % 287
    \stemDown b''8 r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8 r8
    | % 288
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 r4 | % 289
    \stemUp b8 r8 r4 \stemDown e8 r8 r4 | \barNumberCheck #290
    \stemUp <g, g'>8 r8 r4 \stemDown c'8 \stemDown d8 \stemDown e8
    \stemDown fis8 | % 291
    \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown cis8
    \stemDown c8 \stemDown b8 \stemDown a8 \pageBreak | % 292
    \stemDown g4 -> \once \omit TupletBracket
    \times 2/3  {
        \stemUp g,8 \stemUp g8 \stemUp g8 }
    \stemUp b8 \stemUp d8 r4 | % 293
    \stemDown b'8 r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8 r8 | % 294
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 \stemUp c8 r8 | % 295
    \stemUp b8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis8 r8 | % 296
    \stemUp e8 r8 \stemUp es8 r8 \stemUp d8 r8 r4 \pageBreak | % 297
    \stemDown b''8 r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8 r8
    | % 298
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 r4 | % 299
    \stemDown <g, es' bes'>8 r8 r4 \stemDown <bes f' d'>8 r8 r4 |
    \barNumberCheck #300
    \stemDown <es bes' g'>8 r8 r4 \stemUp <g, g'>8 r8 r4 | % 301
    r4 \stemUp b8 r16 \stemUp c16 \stemUp cis8 r8 \stemDown dis8 r8
    \pageBreak | % 302
    \stemDown e8 r8 \stemUp cis8 r16 \stemUp dis16 \stemDown e8 r8
    \stemDown fis8 r8 | % 303
    \stemDown g8 r8 \stemDown gis8 r8 \stemDown a8 r8 \stemDown <b,
        gis'>8 r8 | % 304
    \stemDown <c a'>8 -> _\sempre _\fff r8 \stemDown g''8 ( r16
    \stemDown e16 ) -. \clef "tenor" \stemDown a4 ( -> \stemDown g8 ) r16
    \stemDown es16 -. | % 305
    \stemDown a4 ( -> \stemDown g8 ) r16 \stemDown d16 -. \stemDown a'4
    ( -> \stemDown g8 ) r16 \stemDown cis,16 -. | % 306
    \stemDown a'4 ( -> \stemDown g8 ) r16 \stemDown c,16 -. \stemDown a'4
    ( -> \stemDown g8 ) r16 \stemDown cis,16 -. | % 307
    \stemDown a'4 ( -> \stemDown g8 ) r16 \stemDown d16 -. \stemDown a'4
    ( -> \stemDown g8 ) r16 \stemDown dis16 -. \pageBreak | % 308
    \stemDown b4 ( -> \stemUp a8 ) r16 \stemUp e16 -. \stemDown c'4 ( ->
    \stemUp b8 ) r16 \stemUp e,16 -. | % 309
    \stemDown d'4 ( -> \stemDown c8 ) r16 \stemDown a16 -. \stemDown d4
    ( -> \stemDown cis8 ) r16 \stemDown a16 -. | \barNumberCheck #310
    \stemDown e'4 ( -> \stemDown d8 ) r16 \stemDown a16 -. \stemDown e'4
    ( -> \stemDown dis8 ) r16 \stemDown a16 -. | % 311
    \stemDown f'4 ( -> \stemDown e8 ) r16 \stemDown a,16 -. \stemDown g'4
    ( -> \stemDown fis8 ) r16 \stemDown c16 -. | % 312
    \stemDown a'8 :16 _\ffff \stemDown g8 :16 \stemDown d8 :16 \stemDown
    g8 :16 \stemDown a8 :16 \stemDown g8 :16 \stemDown es8 :16 \stemDown
    g8 :16 | % 313
    \stemDown a8 :16 \stemDown g8 :16 \stemDown e8 :16 \stemDown g8 :16
    \stemDown a8 :16 \stemDown g8 :16 \stemDown es8 :16 \stemDown g8 :16
    \pageBreak | % 314
    \stemDown a8 :16 \stemDown g8 :16 \stemDown fis8 :16 \stemDown e8
    :16 \stemDown d8 :16 \stemDown cis'8 :16 \stemDown c8 :16 \stemDown
    b8 :16 | % 315
    \stemDown a8 :16 \stemDown g8 :16 \stemDown fis8 :16 \stemDown e8
    :16 \stemDown d8 r8 \clef "bass" \stemUp d,16 ( _\fff _\> \stemUp c16
    \stemUp b16 \stemUp a16 ) | % 316
    \stemUp b4 :16 _\! _\p _\< \stemUp a4 :16 \stemUp b2 :16 | % 317
    \stemUp c4 :16 \stemDown d4 :16 \stemDown e4 :16 \stemDown fis4 :16
    | % 318
    \stemUp b,4 :16 _\! _\mf _\< \stemUp a4 :16 \stemUp b2 :16 | % 319
    \stemUp c4 :16 \stemDown d4 :16 \stemDown e4 :16 \stemDown fis4 :16
    \pageBreak | \barNumberCheck #320
    \stemDown g4 :16 _\! _\f _\< \stemDown a4 :16 \stemDown b2 :16 | % 321
    \stemDown c4 :16 \stemDown d4 :16 \stemDown e4 :16 \stemDown fis4
    :16 | % 322
    \stemDown g,4 :16 _\! _\ff _\< \stemDown a4 :16 \stemDown b2 :16 | % 323
    \stemDown c4 :16 \stemDown d4 :16 \stemDown e4 :16 \stemDown fis4
    :16 | % 324
    \stemDown fis,8 _\! _\fff r8 \stemDown e4 ( ~ \stemDown e8 r16
    \stemDown dis16 ) -. \stemDown e8 ( r16 \stemDown fis16 ) -.
    \pageBreak | % 325
    \stemDown g8 -. r8 \stemDown a4 ( ~ \stemDown a8 r16 \stemDown gis16
    ) -. \stemDown a8 ( r16 \stemDown b16 ) -. | % 326
    \stemDown c8 -. r8 r4 r4 \stemUp <g, g'>4 ~ ~ | % 327
    \stemUp <g g'>8 r8 r4 r4 \stemUp <c, c'>4 ~ ~ \pageBreak | % 328
    \stemUp <c c'>8 r8 \stemUp a'4 ~ \stemUp a8 r8 \stemUp fis4 ~ | % 329
    \stemUp fis8 r8 \stemUp a8 r8 \stemDown d8 r8 \stemDown fis8 r8 |
    \barNumberCheck #330
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 _\sempre _\fff \stemDown a8 \stemDown g8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown g8 \stemDown fis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown fis8 \stemDown e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown es8 \stemDown f8 \stemDown es8 }
    | % 331
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown e8 \stemDown d8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown f8 \stemDown e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f8 \stemDown fis8 \stemDown f8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown g8 \stemDown fis8 }
    \pageBreak | % 332
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 \stemDown a8 \stemDown g8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown g8 \stemDown fis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown fis8 \stemDown e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown es8 \stemDown f8 \stemDown es8 }
    | % 333
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown e8 \stemDown d8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown f8 \stemDown e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f8 \stemDown fis8 \stemDown f8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown g8 \stemDown fis8 }
    | % 334
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 \stemDown a8 \stemDown g8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown g8 \stemDown fis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown fis8 \stemDown e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown e8 \stemDown d8 }
    | % 335
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 \stemDown a8 \stemDown g8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown g8 \stemDown fis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown fis8 \stemDown e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown e8 \stemDown d8 }
    \pageBreak | % 336
    \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown g8
    \stemDown fis8 \stemDown e8 \stemDown d8 | % 337
    \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown g8
    \stemDown fis8 \stemDown e8 \stemDown d8 | % 338
    \stemDown g8 :16 \stemDown g'8 :16 \stemDown fis8 :16 \stemDown e8
    :16 \stemDown d8 :16 \stemDown c8 :16 \stemDown b8 :16 \stemDown a8
    :16 | % 339
    \stemDown g8 :16 \stemDown fis'8 :16 \stemDown e8 :16 \stemDown es8
    :16 \stemDown d8 :16 \stemDown c8 :16 \stemDown b8 :16 \stemDown a8
    :16 | \barNumberCheck #340
    \stemDown g8 :16 \stemDown g'8 :16 \stemDown fis8 :16 \stemDown e8
    :16 \stemDown d8 :16 \stemDown c8 :16 \stemDown b8 :16 \stemDown a8
    :16 \pageBreak | % 341
    \stemDown g8 :16 \stemDown fis8 :16 \stemDown e8 :16 \stemDown es8
    :16 \stemUp d8 :16 \stemUp c8 :16 \stemUp b8 :16 \stemUp a8 :16 | % 342
    \stemUp g8 r8 \stemUp g8 r8 r4 \stemUp g8 r8 | % 343
    r4 \stemUp g8 r8 r4 \stemUp g8 r8 | % 344
    \stemUp g8 r8 \stemDown <g d' b'>8 r8 \stemDown <g d' b'>8 r8
    \stemDown <g d' b'>8 r8 | % 345
    <b d>1 ~ ~ | % 346
    \stemUp <b d>2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp <b d>8 \stemUp <b d>8 \stemUp <b d>8 }
    | % 347
    \stemUp <b d>8 r8 r4 r2 \bar "|."
    }

PartPThreeOneVoiceOne =  \relative g {
    \clef "bass" \time 4/4 \key g \major \transposition c | % 1
    R1*4 \pageBreak | % 5
    R1*2 | % 7
    \numericTimeSignature\time 4/4  R1 \bar "||"
    R1*2 \pageBreak | \barNumberCheck #10
    \numericTimeSignature\time 4/4  R1*2 | % 12
    \numericTimeSignature\time 4/4  R1*3 \break | % 15
    R1*5 \pageBreak | \barNumberCheck #20
    R1*4 \break | % 24
    R1*3 | % 27
    \numericTimeSignature\time 4/4  R1 \pageBreak | % 28
    R1*4 \pageBreak | % 32
    R1*4 \pageBreak | % 36
    \numericTimeSignature\time 4/4  R1 | % 37
    \numericTimeSignature\time 4/4  R1*4 \pageBreak | % 41
    R1*5 \pageBreak | % 46
    \time 12/8 \omit Staff.TimeSignature g1. ( ~ ^ "unis." | % 47
    \stemDown g8 ) r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 48
    r2.*2/3 \stemUp g,8 ( _\f \stemUp as8 \stemUp a8 ) \stemUp bes8 (
    \stemUp as8 \stemUp g8 ) s4 | % 49
    fis1. ~ | \barNumberCheck #50
    fis1. ~ \pageBreak | % 51
    \stemUp fis8 r8*2/3 r8*2/3 r4.*2/3 r2.*2/3 s1*11/24 | % 52
    r2.*2/3 \stemUp ais8 ( _\ff \stemUp b8 \stemUp cis8 ) \stemUp b8 (
    \stemUp ais8 \stemUp gis8 ) s4 | % 53
    fis1. ~ _\pp _\markup{ \small\italic {cresc.} } \startTrillSpan | % 54
    fis1. ~ | % 55
    fis1. ~ \pageBreak | % 56
    fis1. \stopTrillSpan _\f | % 57
    fis1. ~ _\pp _\markup{ \small\italic {cresc.} } \startTrillSpan | % 58
    fis1. ~ | % 59
    fis1. ~ | \barNumberCheck #60
    \stemUp fis2. ~ \stopTrillSpan _\f \stemUp fis8 r8*2/3 r8*2/3 r4.*2/3
    s1*5/24 \pageBreak | % 61
    \numericTimeSignature\time 4/4  \stemUp b8 -. _\p r8 \stemUp fis8 -.
    r16 \stemUp fis16 -. \stemUp b8 -. r8 \stemUp fis8 -. r8 | % 62
    \stemUp b8 -. \stemUp e8 -. r4 r2 | % 63
    \stemUp b8 -. _\mp r8 \stemUp fis8 -. r16 \stemUp fis16 -. \stemUp b8
    -. r8 \stemUp fis8 -. r8 | % 64
    \stemUp b8 -. \stemUp e8 -. r4 r2 | % 65
    \stemUp b8 -. _\mf r8 \stemUp fis8 -. r16 \stemUp fis16 -. \stemUp b8
    -. r8 \stemUp fis8 -. r8 \pageBreak | % 66
    \stemUp b8 -. \stemUp e8 -. r4 r2 | % 67
    \stemUp b8 -. _\f r8 \stemUp fis8 -. r16 \stemUp fis16 -. \stemUp b8
    -. r8 \stemUp fis8 -. r8 | % 68
    \stemUp b8 \stemUp e8 r4 r2 | % 69
    \stemUp b8 -> _\ff r8 r4 r2 | \barNumberCheck #70
    R1 \bar "||"
    \pageBreak | % 71
    \key e \major R1 | % 72
    \time 12/8  r2.*2/3 r4.*2/3 \stemDown a'8 -. _\pp \stemDown b8 -.
    \stemDown a8 -. s4. | % 73
    \stemDown gis8 -. \stemDown a8 -. \stemDown gis8 -. \stemDown fis8
    -. \stemDown gis8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8
    -. | % 74
    \stemUp cis8 -. _\sempre _\pp \stemUp dis8 -. \stemUp cis8 -.
    \stemUp c8 -. \stemUp d8 -. \stemUp c8 -. \stemUp b8 -. \stemUp ais8
    -. \stemUp b8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown gis8 -.
    | % 75
    \stemDown g8 -. \stemDown a8 -. \stemDown g8 -. \stemDown fis8 -.
    \stemDown gis8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8
    -. \break | % 76
    \stemUp cis8 -. \stemUp dis8 -. \stemUp cis8 -. \stemUp c8 -.
    \stemUp d8 -. \stemUp c8 -. \stemUp b8 -. \stemUp c8 -. \stemUp b8
    -. \stemUp b8 -. \stemUp a8 -. \stemUp gis8 -. | % 77
    \numericTimeSignature\time 4/4  \stemUp gis8 _\p r8 r4 \stemUp cis8
    r8 r4 | % 78
    \stemDown e8 r8 r4 r2 | % 79
    r2 r4 \stemDown gis16 _\mf \stemDown gis16 \stemDown fis16 \stemDown
    fis16 | \barNumberCheck #80
    \stemDown e4 ~ _\< \stemDown e8 \stemDown e16 \stemDown e16
    \stemDown gis8 _\! _\f \stemDown b8 r4 \pageBreak | % 81
    \time 12/8  r1 s2 | % 82
    r2.*2/3 \stemDown b8 -. _\pp \stemDown cis8 -. \stemDown b8 -.
    \stemDown a8 -. \stemDown b8 -. \stemDown a8 -. s4 | % 83
    \stemDown gis8 -. _\markup{ \small\italic {un poco cresc.} }
    \startTrillSpan \stemDown a8 -. \stemDown gis8 -. \stemDown fis8 -.
    \stemDown gis8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8
    -. | % 84
    \stemUp cis8 \stemUp dis8 \stemUp cis8 \stemUp c8 \stemUp d8 \stemUp
    c8 \stemUp b8 \stemUp ais8 \stemUp b8 \stemDown e8 \stemDown fis8
    \stemDown gis8 | % 85
    \stemDown g8 -. \stemDown a8 -. \stemDown g8 -. \stemDown fis8 -.
    \stemDown gis8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8
    -. \pageBreak | % 86
    \stemUp cis8 -. \stemUp dis8 -. \stemUp cis8 -. \stemUp c8 -.
    \stemUp d8 -. \stemUp c8 -. \stemUp b8 -. \stemUp ais8 -. \stemUp b8
    -. r4.*2/3 s8 \stopTrillSpan | % 87
    \numericTimeSignature\time 4/4  \stemUp e,8 _\mf _\< r8 r4 \stemUp g8
    r8 r4 | % 88
    \stemUp c8 r8 r4 \stemDown e8 r8 r4 _\! | % 89
    r4 \stemUp gis,8 _\f r16 \stemUp a16 \stemUp ais4 \stemUp bis4
    \pageBreak | \barNumberCheck #90
    \stemUp cis4 \stemUp ais8 r16 \stemUp bis16 \stemUp cis4 \stemDown
    dis4 | % 91
    \stemDown e4 _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown eis4 \stemDown fis4 \stemDown gis4 | % 92
    \stemDown a4 \stemDown ais4 \stemDown b4 \stemDown cis4 | % 93
    \stemDown d8 \stopTrillSpan _\ff r8 r4 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp c,8 \stemUp c8 \stemUp c8 }
    | % 94
    \stemUp c2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 }
    | % 95
    \stemUp b2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp bes8 \stemUp bes8 \stemUp bes8 }
    \pageBreak | % 96
    \stemUp bes8 r8 \stemUp b8 r8 \stemDown e8 r8 r4 | % 97
    R1 | % 98
    r2 \stemUp b2 ~ _\p | % 99
    b1 ~ _\< | \barNumberCheck #100
    \stemUp b2. ~ _\! _\mf _\> \stemUp b8 r8 _\! | % 101
    R1 \break | % 102
    r2 \stemUp gis2 ~ _\p | % 103
    gis1 ~ _\< | % 104
    \stemUp gis2. ~ _\! _\mf _\> \stemUp gis8 r8 _\! | % 105
    R1 | % 106
    r2 \stemUp b2 ~ _\p \pageBreak | % 107
    b1 ~ _\< | % 108
    \stemUp b2. ~ _\! _\mf _\> \stemUp b8 r8 _\! | % 109
    R1*2 | % 111
    r2 \stemDown dis'8 \downbow _\ff r8 \stemDown cis8 \downbow r8 | % 112
    \stemDown c8 \downbow r8 \stemDown b8 \downbow r8 r2 \break | % 113
    R1 | % 114
    \time 12/8  r2.*2/3 r4.*2/3 \stemDown a8 -. _\pp \stemDown b8 -.
    \stemDown a8 -. s4. | % 115
    \stemDown gis8 -. \stemDown a8 -. \stemDown gis8 -. \stemDown fis8
    -. \stemDown gis8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8
    -. | % 116
    \stemUp cis8 -. _\sempre _\pp \stemUp dis8 -. \stemUp cis8 -.
    \stemUp c8 -. \stemUp d8 -. \stemUp c8 -. \stemUp b8 -. \stemUp ais8
    -. \stemUp b8 -. \stemDown e8 -. \stemDown fis8 -. \stemDown gis8 -.
    | % 117
    \stemDown g8 -. \stemDown a8 -. \stemDown g8 -. \stemDown fis8 -.
    \stemDown gis8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8
    -. \pageBreak | % 118
    \stemUp cis8 -. \stemUp dis8 -. \stemUp cis8 -. \stemUp c8 -.
    \stemUp d8 -. \stemUp c8 -. \stemUp b8 -. \stemUp c8 -. \stemUp b8
    -. \stemUp b8 -. \stemUp a8 -. \stemUp gis8 -. | % 119
    \numericTimeSignature\time 4/4  \stemUp gis8 r8 r4 \stemUp cis8 r8 r4
    | \barNumberCheck #120
    \stemDown e8 r8 r4 r2 | % 121
    r2 r4 \stemDown gis16 _\mf \stemDown gis16 \stemDown fis16 \stemDown
    fis16 | % 122
    \stemDown e4 ~ _\< \stemDown e8 \stemDown e16 \stemDown e16
    \stemDown gis8 _\! _\f \stemDown b8 r4 \break | % 123
    \time 12/8  r1 s2 | % 124
    r2.*2/3 \stemDown b8 -. _\pp \stemDown cis8 -. \stemDown b8 -.
    \stemDown a8 -. \stemDown b8 -. \stemDown a8 -. s4 | % 125
    \stemDown gis8 -. _\markup{ \small\italic {un poco cresc.} }
    \startTrillSpan \stemDown a8 -. \stemDown gis8 -. \stemDown fis8 -.
    \stemDown gis8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8
    -. | % 126
    \stemUp cis8 -. \stemUp dis8 -. \stemUp cis8 -. \stemUp c8 -.
    \stemUp d8 -. \stemUp c8 -. \stemUp b8 -. \stemUp ais8 -. \stemUp b8
    -. \stemDown e8 -. \stemDown fis8 -. \stemDown gis8 -. | % 127
    \stemDown g8 -. \stemDown a8 -. \stemDown g8 -. \stemDown fis8 -.
    \stemDown gis8 -. \stemDown fis8 -. \stemDown e8 -. \stemDown fis8
    -. \stemDown e8 -. \stemDown dis8 -. \stemDown e8 -. \stemDown dis8
    -. \pageBreak | % 128
    \stemUp cis8 -. \stemUp dis8 -. \stemUp cis8 -. \stemUp c8 -.
    \stemUp d8 -. \stemUp c8 -. \stemUp b8 -. \stemUp ais8 -. \stemUp b8
    -. r4.*2/3 s8 \stopTrillSpan | % 129
    \numericTimeSignature\time 4/4  \stemUp e,8 _\f r8 r4 \stemUp g8 r8
    r4 | \barNumberCheck #130
    \stemUp c8 r8 r4 \stemDown g'8 r8 r4 | % 131
    \stemDown c4 ( ^> \stemDown b8 r16 \stemDown a16 ) -. \stemDown g8
    -. r8 \stemDown d'8 ( -. r16 \stemDown dis16 ) -. \pageBreak | % 132
    \stemDown e4 ( ^> \stemDown d8 r16 \stemDown c16 ) -. \stemDown b8
    -. r8 r4 | % 133
    \stemUp e,,8 r8 r4 \stemUp g8 r8 r4 | % 134
    \stemUp c8 r8 r4 \stemDown g'8 r8 r4 | % 135
    \stemDown c4 ( ^> \stemDown b8 r16 \stemDown a16 ) -. \stemDown g8
    -. r8 \stemDown d'8 ( -. r16 \stemDown dis16 ) -. \pageBreak | % 136
    \stemDown e4 ( ^> \stemDown d8 r16 \stemDown c16 ) -. \stemDown b8
    -. r8 r4 | % 137
    \time 12/8  \stemUp e,,8 _\f r8*2/3 r8*2/3 \stemUp g8 r8*2/3 r8*2/3
    r2.*2/3 s1*5/12 | % 138
    \stemUp e8 _\mf r8*2/3 r8*2/3 \stemUp g8 r8*2/3 r8*2/3 r2.*2/3 \bar
    "||"
    s1*5/12 | % 139
    \key g \major r1 s2 \pageBreak | \barNumberCheck #140
    r1 s2 | % 141
    r1 s2 | % 142
    \stemUp g'2. -> ^\p r2.*2/3 s4 | % 143
    r1 s2 | % 144
    r1 s2 \pageBreak | % 145
    r1 s2 | % 146
    \stemDown e2. -> _\p r2.*2/3 s4 | % 147
    r1 s2 | % 148
    r1 s2 | % 149
    r1 s2 \pageBreak | \barNumberCheck #150
    r1 s2 | % 151
    r1 s2 | % 152
    r1 s2 | % 153
    r1 s2 | % 154
    r1 s2 \pageBreak | % 155
    r1 s2 | % 156
    r1 s2 | % 157
    r1 s2 | % 158
    r1 s2 \break | % 159
    r1 s2 | \barNumberCheck #160
    r1 s2 | % 161
    r1 s2 | % 162
    r1 s2 \pageBreak | % 163
    r1 s2 | % 164
    r1 s2 | % 165
    r1 s2 | % 166
    r1 s2 \pageBreak | % 167
    r1 s2 | % 168
    r1 s2 | % 169
    r1 s2 | \barNumberCheck #170
    r1 s2 \pageBreak | % 171
    r1 s2 | % 172
    r1 s2 | % 173
    r1 s2 | % 174
    r1 s2 \pageBreak | % 175
    r1 s2 | % 176
    r1 s2 | % 177
    r1 s2 | % 178
    r1 s2 | % 179
    r1 s2 \pageBreak | \barNumberCheck #180
    r1 s2 | % 181
    r1 s2 | % 182
    r1 s2 | % 183
    r1 s2 \pageBreak | % 184
    r1 s2 | % 185
    r1 s2 | % 186
    r1 s2 | % 187
    r1 s2 | % 188
    r1 s2 \pageBreak | % 189
    r1 s2 | \barNumberCheck #190
    r1 s2 | % 191
    r1 s2 | % 192
    r1 s2 | % 193
    r1 s2 \pageBreak | % 194
    \time 4/4 \omit Staff.TimeSignature a,1 ( ~ ^ "unis." | % 195
    a1 ) ~ _\> | % 196
    a1 ~ _\! _\pp | % 197
    a1 ~ | % 198
    a1 ~ | % 199
    a1 ~ | \barNumberCheck #200
    a1 ~ _\< \pageBreak | % 201
    a1 ~ _\! _\p | % 202
    a1 ~ | % 203
    \stemUp a8 r8 r4 r2 | % 204
    \stemDown fis'2 :16 _\p _\< \stemDown g2 :16 | % 205
    \stemDown eis2 :16 _\! _\mp \stemDown fis2 :16 \pageBreak | % 206
    \stemDown g2 :16 _\markup{ \small\italic {poco a poco cresc.} }
    \startTrillSpan \stemDown gis2 :16 | % 207
    \stemDown a2 :16 \stemDown ais2 :16 | % 208
    \stemDown b2 :16 \stemDown bes2 :16 | % 209
    \stemDown a8 \stopTrillSpan r8 r4 r2 | \barNumberCheck #210
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a,8 _\f _\markup{ \small\italic {cresc.} }
        \startTrillSpan \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \pageBreak | % 211
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    | % 212
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stopTrillSpan _\ff \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    | % 213
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 _\< \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    | % 214
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 _\! _\fff \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    | % 215
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \pageBreak | % 216
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    | % 217
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    | % 218
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    | % 219
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    | \barNumberCheck #220
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 }
    \pageBreak | % 221
    \times 2/3  {
        \stemUp a8 -> \stemUp a8 -> r8 }
    r4 r2 | % 222
    \stemDown d'16 ( _\fff \stemDown c16 \stemDown b16 \stemDown a16 )
    \stemDown g16 ( \stemDown fis16 \stemDown e16 \stemDown d16 ) r2 | % 223
    r4 r4 r2 | % 224
    \stemDown d'16 ( \stemDown c16 \stemDown b16 \stemDown a16 )
    \stemDown g16 ( \stemDown fis16 \stemDown e16 \stemDown d16 ) r2
    \pageBreak | % 225
    R1*3 \pageBreak | % 228
    R1 | % 229
    \stemDown b'8 _\fff r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8
    r8 | \barNumberCheck #230
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 \stemUp c8 r8 | % 231
    \stemUp b8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis8 r8 | % 232
    \stemUp e8 r8 \stemDown es'8 r8 \stemDown d8 r8 r4 \pageBreak | % 233
    \stemDown b'8 r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8 r8 | % 234
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 r4 | % 235
    \stemUp b8 r8 r4 \stemDown e8 r8 r4 | % 236
    \stemDown g8 r8 r4 \stemDown c8 \stemDown d8 \stemDown e8 \stemDown
    fis8 | % 237
    \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown cis8
    \stemDown c8 \stemDown b8 \stemDown a8 \pageBreak | % 238
    \stemDown g4 -> \once \omit TupletBracket
    \times 2/3  {
        \stemUp g,8 \stemUp g8 \stemUp g8 }
    \stemUp b8 \stemUp d8 r4 | % 239
    \stemDown b'8 r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8 r8 |
    \barNumberCheck #240
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 \stemUp c8 r8 | % 241
    \stemUp b8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis8 r8 | % 242
    \stemUp e8 r8 \stemDown es'8 r8 \stemDown d8 r8 r4 \pageBreak | % 243
    \stemDown b'8 r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8 r8 | % 244
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 r4 | % 245
    \stemUp g,8 r8 r4 \stemUp bes8 r8 r4 | % 246
    \stemDown es8 r8 r4 \stemDown g8 r8 r4 | % 247
    r4 \stemUp b,8 r16 \stemUp c16 \stemUp cis8 r8 \stemDown dis8 r8
    \pageBreak | % 248
    \stemDown e8 r8 \stemUp cis8 r16 \stemUp dis16 \stemDown e8 r8
    \stemDown fis8 r8 | % 249
    \stemDown g8 r8 \stemDown gis8 r8 \stemDown a8 r8 \stemDown b8 r8 |
    \barNumberCheck #250
    \stemDown c8 r8 \stemDown cis8 r8 \stemDown d8 r8 \stemDown e8 r8 | % 251
    \stemDown f8 r8 r4 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown es,8 \stemDown es8 \stemDown es8 }
    | % 252
    \stemDown es2. \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 }
    | % 253
    \stemDown d2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis8 \stemUp cis8 \stemUp cis8 }
    \pageBreak | % 254
    \stemUp cis8 r8 \stemDown d8 r8 \stemDown g8 r8 r4 | % 255
    R1 | % 256
    r2 \stemDown <d d'>2 ~ ~ _\f ^ "div." | % 257
    <d d'>1 ~ ~ _\< | % 258
    \stemDown <d d'>2. ~ ~ _\! _\ff _\> \stemDown <d d'>8 _\! r8
    \pageBreak | % 259
    R1 | \barNumberCheck #260
    r2 \stemDown <b b'>2 ~ ~ _\f ^ "div." | % 261
    <b b'>1 ~ ~ _\< | % 262
    \stemDown <b b'>2. ~ ~ _\! _\ff _\> \stemDown <b b'>8 _\! r8 | % 263
    R1 \pageBreak | % 264
    r2 \stemDown <d d'>2 ~ ~ _\f | % 265
    <d d'>1 ~ ~ _\< | % 266
    \stemDown <d d'>2. ~ ~ _\! _\ff _\> \stemDown <d d'>8 _\! r8 | % 267
    R1*2 \pageBreak | % 269
    R1*4 | % 273
    \stemDown a'8 _\fff r8 \stemDown as8 r8 \stemDown g8 r8 \stemDown f8
    r8 \pageBreak | % 274
    \stemDown e8 r8 \stemDown d8 r8 \stemUp c2 :16 _\fff | % 275
    c1 :16 | % 276
    c1 :16 | % 277
    c1 :16 | % 278
    c1 :16 | % 279
    c1 :16 | \barNumberCheck #280
    c1 :16 \pageBreak | % 281
    c1 :16 | % 282
    \stemUp c2 :16 \stemUp c8 r8 \stemDown c'8 _\fff r8 | % 283
    \stemDown b8 r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8 r8 | % 284
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 \stemUp c8 r8 | % 285
    \stemUp b8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis8 r8 | % 286
    \stemUp e8 r8 \stemDown es'8 r8 \stemDown d8 r8 r4 \pageBreak | % 287
    \stemDown b'8 r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8 r8 | % 288
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 r4 | % 289
    \stemUp b8 r8 r4 \stemDown e8 r8 r4 | \barNumberCheck #290
    \stemDown g8 r8 r4 \stemDown c8 \stemDown d8 \stemDown e8 \stemDown
    fis8 | % 291
    \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown cis8
    \stemDown c8 \stemDown b8 \stemDown a8 \pageBreak | % 292
    \stemDown g4 -> \once \omit TupletBracket
    \times 2/3  {
        \stemUp g,8 \stemUp g8 \stemUp g8 }
    \stemUp b8 \stemUp d8 r4 | % 293
    \stemDown b'8 r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8 r8 | % 294
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 \stemUp c8 r8 | % 295
    \stemUp b8 r8 \stemUp a8 r8 \stemUp g8 r8 \stemUp fis8 r8 | % 296
    \stemUp e8 r8 \stemDown es'8 r8 \stemDown d8 r8 r4 \pageBreak | % 297
    \stemDown b'8 r8 \stemDown a8 r8 \stemDown g8 r8 \stemDown fis8 r8 | % 298
    \stemDown e8 r8 \stemDown es8 r8 \stemDown d8 r8 r4 | % 299
    \stemUp g,8 r8 r4 \stemUp bes8 r8 r4 | \barNumberCheck #300
    \stemDown es8 r8 r4 \stemDown g8 r8 r4 | % 301
    r4 \stemUp b,8 r16 \stemUp c16 \stemUp cis8 r8 \stemDown dis8 r8
    \pageBreak | % 302
    \stemDown e8 r8 \stemUp cis8 r16 \stemUp dis16 \stemDown e8 r8
    \stemDown fis8 r8 | % 303
    \stemDown g8 r8 \stemDown gis8 r8 \stemDown a8 r8 \stemDown b8 r8 | % 304
    \stemDown c4 ~ -> _\sempre _\fff \stemDown c8 r8 \stemDown cis4 ~ ->
    \stemDown cis8 r8 | % 305
    \stemDown d4 ~ -> \stemDown d8 r8 \stemDown es4 ~ -> \stemDown es8 r8
    | % 306
    \stemDown e4 ~ -> \stemDown e8 r8 \stemDown es4 ~ -> \stemDown es8 r8
    | % 307
    \stemDown d4 ~ -> \stemDown d8 r8 \stemDown cis4 ~ -> \stemDown cis8
    r8 \pageBreak | % 308
    \stemDown c4 ~ -> \stemDown c8 r8 \stemDown b4 ~ -> \stemDown b8 r8
    | % 309
    \stemDown a4 ~ -> \stemDown a8 r8 \stemDown g4 ~ -> \stemDown g8 r8
    | \barNumberCheck #310
    \stemDown fis4 ~ -> \stemDown fis8 r8 \stemDown f4 ~ -> \stemDown f8
    r8 | % 311
    \stemDown e4 ~ -> \stemDown e8 r8 \stemDown es4 ~ -> \stemDown es8 r8
    | % 312
    \stemDown d4. _\ffff \stemDown d8 \stemUp cis4. \stemUp cis8 | % 313
    \stemUp c4. \stemUp c8 \stemUp cis4. \stemUp cis8 \pageBreak | % 314
    \stemDown d4 \stemDown g4 \stemDown b4 \stemDown d4 | % 315
    \stemDown fis8 r8 r4 r4 \stemUp d,16 ( _\fff _\> \stemUp c16 \stemUp
    b16 \stemUp a16 ) | % 316
    \stemUp g8 _\! _\p _\< r8 \stemDown d'8 r16 \stemDown d16 \stemUp g,8
    r8 \stemDown d'8 r8 | % 317
    \stemUp g,8 \stemUp c8 ~ \stemUp c4 ~ \stemUp c8 r8 _\! r4 | % 318
    \stemUp g8 _\mf _\< r8 \stemDown d'8 r16 \stemDown d16 \stemUp g,8 r8
    \stemDown d'8 r8 | % 319
    \stemUp g,8 \stemUp c8 ~ \stemUp c4 ~ \stemUp c8 r8 _\! r4
    \pageBreak | \barNumberCheck #320
    \stemUp g8 _\f _\< r8 \stemDown d'8 r16 \stemDown d16 \stemUp g,8 r8
    \stemDown d'8 r8 | % 321
    \stemUp g,8 \stemUp c8 ~ \stemUp c4 ~ \stemUp c8 r8 _\! r4 | % 322
    \stemUp g8 _\ff _\< r8 \stemDown d'8 r16 \stemDown d16 \stemUp g,8 r8
    \stemDown d'8 r8 | % 323
    \stemUp g,8 \stemUp c8 ~ \stemUp c4 ~ \stemUp c8 r8 _\! r4 | % 324
    \stemUp b8 _\fff r8 \stemDown e4 ( ~ \stemDown e8 r16 \stemDown dis16
    ) -. \stemDown e8 ( r16 \stemDown fis16 ) -. \pageBreak | % 325
    \stemDown g8 -. r8 \stemDown a4 ( ~ \stemDown a8 r16 \stemDown gis16
    ) -. \stemDown a8 ( r16 \stemDown b16 ) -. | % 326
    \stemDown c8 -. r8 r4 r4 \stemDown g4 ~ | % 327
    \stemDown g8 r8 r4 r4 \stemUp c,4 ~ \pageBreak | % 328
    \stemUp c8 r8 \stemUp a4 ~ \stemUp a8 r8 \stemUp fis4 ~ | % 329
    \stemUp fis8 r8 \stemUp a8 r8 \stemDown d8 r8 \stemDown fis8 r8 |
    \barNumberCheck #330
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 _\sempre _\fff \stemDown a8 \stemDown g8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown g8 \stemDown fis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown fis8 \stemDown e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown es8 \stemDown f8 \stemDown es8 }
    | % 331
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown e8 \stemDown d8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown f8 \stemDown e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f8 \stemDown fis8 \stemDown f8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown g8 \stemDown fis8 }
    \pageBreak | % 332
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 \stemDown a8 \stemDown g8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown g8 \stemDown fis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown fis8 \stemDown e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown es8 \stemDown f8 \stemDown es8 }
    | % 333
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown e8 \stemDown d8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown f8 \stemDown e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f8 \stemDown fis8 \stemDown f8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown g8 \stemDown fis8 }
    | % 334
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 \stemDown a8 \stemDown g8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown g8 \stemDown fis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown fis8 \stemDown e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown e8 \stemDown d8 }
    | % 335
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 \stemDown a8 \stemDown g8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown g8 \stemDown fis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown fis8 \stemDown e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown e8 \stemDown d8 }
    \pageBreak | % 336
    \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown g8
    \stemDown fis8 \stemDown e8 \stemDown d8 | % 337
    \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown g8
    \stemDown fis8 \stemDown e8 \stemDown d8 | % 338
    \stemDown g8 r8 r8 \stemDown g8 \stemDown g8 r8 r8 \stemDown g8 | % 339
    \stemDown g8 r8 r8 \stemDown g8 \stemDown g8 r8 r8 \stemDown g8 |
    \barNumberCheck #340
    \stemDown g8 :16 \stemDown g'8 :16 \stemDown fis8 :16 \stemDown e8
    :16 \stemDown d8 :16 \stemDown c8 :16 \stemDown b8 :16 \stemDown a8
    :16 \pageBreak | % 341
    \stemDown g8 :16 \stemDown fis8 :16 \stemDown e8 :16 \stemDown es8
    :16 \stemUp d8 :16 \stemUp c8 :16 \stemUp b8 :16 \stemUp a8 :16 | % 342
    \stemUp g8 r8 \stemUp g8 r8 r4 \stemUp g8 r8 | % 343
    r4 \stemUp g8 r8 r4 \stemUp g8 r8 | % 344
    \stemUp g8 r8 \stemUp g8 r8 \stemUp g8 r8 \stemUp g8 r8 | % 345
    g1 ~ | % 346
    \stemUp g2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 \stemUp g8 \stemUp g8 }
    | % 347
    \stemUp g8 r8 r4 r2 \bar "|."
    }

PartPThreeOneVoiceTwo =  \relative c' {
    \clef "bass" \time 4/4 \key g \major \transposition c s1*4
    \pageBreak s1*2 | % 7
    \numericTimeSignature\time 4/4  s1 \bar "||"
    s1*2 \pageBreak | \barNumberCheck #10
    \numericTimeSignature\time 4/4  s1*2 | % 12
    \numericTimeSignature\time 4/4  s1*3 \break s1*5 \pageBreak s1*4
    \break s1*3 | % 27
    \numericTimeSignature\time 4/4  s1 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak | % 36
    \numericTimeSignature\time 4/4  s1 | % 37
    \numericTimeSignature\time 4/4  s1*4 \pageBreak s1*5 \pageBreak | % 46
    \time 12/8 \omit Staff.TimeSignature s2*15 \pageBreak s2*15
    \pageBreak s2*15 \pageBreak | % 61
    \numericTimeSignature\time 4/4  s1*5 \pageBreak s1*5 \bar "||"
    \pageBreak | % 71
    \key e \major s1 | % 72
    \time 12/8  s1*6 \break s1. | % 77
    \numericTimeSignature\time 4/4  s1*4 \pageBreak | % 81
    \time 12/8  s2*15 \pageBreak s1. | % 87
    \numericTimeSignature\time 4/4  s1*3 \pageBreak s1*6 \pageBreak s1*6
    \break s1*5 \pageBreak s1*6 \break s1 | % 114
    \time 12/8  s1*6 \pageBreak s1. | % 119
    \numericTimeSignature\time 4/4  s1*4 \break | % 123
    \time 12/8  s2*15 \pageBreak s1. | % 129
    \numericTimeSignature\time 4/4  s1*3 \pageBreak s1*4 \pageBreak s1 | % 137
    \time 12/8  s1*31/12 \bar "||"
    s1*5/12 | % 139
    \key g \major s1. \pageBreak s4*13 r1 s4*13 \pageBreak s2*15
    \pageBreak s2*15 \pageBreak s1*6 \break s1*6 \pageBreak s1*6
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak s2*15 \pageBreak s1*6
    \pageBreak s2*15 \pageBreak s2*15 \pageBreak | % 194
    \time 4/4 \omit Staff.TimeSignature s1*7 \pageBreak s1*5 \pageBreak
    s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*4 \pageBreak | % 225
     \once \override NoteHead.style = ##f c1 s1*2 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*6
    \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*5 \pageBreak s1*5
    \pageBreak s1*5 \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*6
    \pageBreak s1*5 \pageBreak s1*3 \pageBreak s1*4 \pageBreak s1*4
    \pageBreak s1*5 \pageBreak s1*7 \bar "|."
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
                    \set Staff.instrumentName = "I"
                    \set Staff.shortInstrumentName = "I"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneVoiceOne" {  \PartPOneVoiceOne }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "II"
                    \set Staff.shortInstrumentName = "II"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPTwoVoiceOne" {  \voiceOne \PartPTwoVoiceOne }
                        \context Voice = "PartPTwoVoiceTwo" {  \voiceTwo \PartPTwoVoiceTwo }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Piccolo"
                    \set Staff.shortInstrumentName = "Picc."
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPThreeVoiceOne" {  \voiceOne \PartPThreeVoiceOne }
                        \context Voice = "PartPThreeVoiceTwo" {  \voiceTwo \PartPThreeVoiceTwo }
                        >>
                    >>
                
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "2 Oboes"
                \set Staff.shortInstrumentName = "Ob."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPFourVoiceOne" {  \voiceOne \PartPFourVoiceOne }
                    \context Voice = "PartPFourVoiceTwo" {  \voiceTwo \PartPFourVoiceTwo }
                    >>
                >>
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = "I"
                    \set Staff.shortInstrumentName = "I"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPFiveVoiceOne" {  \PartPFiveVoiceOne }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "II"
                    \set Staff.shortInstrumentName = "II"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPSixVoiceOne" {  \PartPSixVoiceOne }
                        >>
                    >>
                
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "2 Bassoons"
                \set Staff.shortInstrumentName = "Bsn."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPSevenVoiceOne" {  \voiceOne \PartPSevenVoiceOne }
                    \context Voice = "PartPSevenVoiceTwo" {  \voiceTwo \PartPSevenVoiceTwo }
                    >>
                >>
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = "I &amp; II"
                    \set Staff.shortInstrumentName = "I &amp; II"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPEightVoiceOne" {  \voiceOne \PartPEightVoiceOne }
                        \context Voice = "PartPEightVoiceTwo" {  \voiceTwo \PartPEightVoiceTwo }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "III &amp; IV"
                    \set Staff.shortInstrumentName = "III &amp; IV"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPNineVoiceOne" {  \voiceOne \PartPNineVoiceOne }
                        \context Voice = "PartPNineVoiceTwo" {  \voiceTwo \PartPNineVoiceTwo }
                        >>
                    >>
                
                >>
            \new Staff
            <<
                \set Staff.instrumentName = \markup { \center-column { \line {"2 Trumpets "} \line {"in A"} } }
                \set Staff.shortInstrumentName = "Tpt."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneZeroVoiceOne" {  \voiceOne \PartPOneZeroVoiceOne }
                    \context Voice = "PartPOneZeroVoiceTwo" {  \voiceTwo \PartPOneZeroVoiceTwo }
                    >>
                >>
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = "Alto &amp; Tenor"
                    \set Staff.shortInstrumentName = "A. T."
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneOneVoiceOne" {  \voiceOne \PartPOneOneVoiceOne }
                        \context Voice = "PartPOneOneVoiceTwo" {  \voiceTwo \PartPOneOneVoiceTwo }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Bass"
                    \set Staff.shortInstrumentName = "B."
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneTwoVoiceOne" {  \voiceOne \PartPOneTwoVoiceOne }
                        \context Voice = "PartPOneTwoVoiceTwo" {  \voiceTwo \PartPOneTwoVoiceTwo }
                        >>
                    >>
                
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Tuba"
                \set Staff.shortInstrumentName = "Tba."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneThreeVoiceOne" {  \voiceOne \PartPOneThreeVoiceOne }
                    \context Voice = "PartPOneThreeVoiceTwo" {  \voiceTwo \PartPOneThreeVoiceTwo }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Timpani"
                \set Staff.shortInstrumentName = "Timp."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneFourVoiceOne" {  \voiceOne \PartPOneFourVoiceOne }
                    \context Voice = "PartPOneFourVoiceTwo" {  \voiceTwo \PartPOneFourVoiceTwo }
                    >>
                >>
            \new RhythmicStaff
            <<
                \set RhythmicStaff.instrumentName = "Bass Drum"
                \set RhythmicStaff.shortInstrumentName = "B. D."
                
                \context RhythmicStaff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneFiveVoiceOne" {  \voiceOne \PartPOneFiveVoiceOne }
                    \context Voice = "PartPOneFiveVoiceTwo" {  \voiceTwo \PartPOneFiveVoiceTwo }
                    >>
                >>
            \new RhythmicStaff
            <<
                \set RhythmicStaff.instrumentName = "Cymbal"
                \set RhythmicStaff.shortInstrumentName = "Cym."
                
                \context RhythmicStaff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneSixVoiceOne" {  \voiceOne \PartPOneSixVoiceOne }
                    \context Voice = "PartPOneSixVoiceTwo" {  \voiceTwo \PartPOneSixVoiceTwo }
                    >>
                >>
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = \markup { \center-column { \line {""} \line {"Violins I"} \line {"divisi"} } }
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneSevenVoiceOne" {  \PartPOneSevenVoiceOne }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Violins"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneEightVoiceOne" {  \PartPOneEightVoiceOne }
                        >>
                    >>
                
                >>
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = \markup { \center-column { \line {""} \line {"Violins II"} \line {"divisi"} } }
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneNineVoiceOne" {  \PartPOneNineVoiceOne }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Violins"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPTwoZeroVoiceOne" {  \PartPTwoZeroVoiceOne }
                        >>
                    >>
                
                >>
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = \markup { \center-column { \line {""} \line {"Violas"} \line {"divisi"} } }
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPTwoOneVoiceOne" {  \PartPTwoOneVoiceOne }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Violas"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPTwoTwoVoiceOne" {  \PartPTwoTwoVoiceOne }
                        >>
                    >>
                
                >>
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = \markup { \center-column { \line {""} \line {"Violoncellos"} \line {"divisi"} } }
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPTwoThreeVoiceOne" {  \PartPTwoThreeVoiceOne }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Violoncellos"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPTwoFourVoiceOne" {  \PartPTwoFourVoiceOne }
                        >>
                    >>
                
                >>
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = \markup { \center-column { \line {""} \line {"Contrabasses"} \line {"divisi"} } }
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPTwoFiveVoiceOne" {  \PartPTwoFiveVoiceOne }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Contrabasses"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPTwoSixVoiceOne" {  \voiceOne \PartPTwoSixVoiceOne }
                        \context Voice = "PartPTwoSixVoiceTwo" {  \voiceTwo \PartPTwoSixVoiceTwo }
                        >>
                    >>
                
                >>
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = "Violin I"
                    \set Staff.shortInstrumentName = "Vln. I"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPTwoSevenVoiceOne" {  \voiceOne \PartPTwoSevenVoiceOne }
                        \context Voice = "PartPTwoSevenVoiceTwo" {  \voiceTwo \PartPTwoSevenVoiceTwo }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Violin II"
                    \set Staff.shortInstrumentName = "Vln. II"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPTwoEightVoiceOne" {  \voiceOne \PartPTwoEightVoiceOne }
                        \context Voice = "PartPTwoEightVoiceTwo" {  \voiceTwo \PartPTwoEightVoiceTwo }
                        >>
                    >>
                
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Viola"
                \set Staff.shortInstrumentName = "Vla."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPTwoNineVoiceOne" {  \PartPTwoNineVoiceOne }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Violoncello"
                \set Staff.shortInstrumentName = "Vc."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPThreeZeroVoiceOne" {  \PartPThreeZeroVoiceOne }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Contrabass"
                \set Staff.shortInstrumentName = "Cb."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPThreeOneVoiceOne" {  \voiceOne \PartPThreeOneVoiceOne }
                    \context Voice = "PartPThreeOneVoiceTwo" {  \voiceTwo \PartPThreeOneVoiceTwo }
                    >>
                >>
            
            >>
        
        >>
    \layout {}
    % To create MIDI output, uncomment the following line:
    %  \midi {\tempo 4 = 162 }
    }

