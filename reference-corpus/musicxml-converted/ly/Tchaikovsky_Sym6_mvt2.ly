\version "2.24.3"
% automatically converted by musicxml2ly from ../xml/Tchaikovsky_Sym6_mvt2.musicxml
\pointAndClickOff

\header {
    title =  "Symphony No. 6, Pathétique"
    composer =  \markup \column {
        \line { "Pyotr Ilyich Tchaikovsky"}
        \line { ""} }
    
    poet =  "Пётр Ильич Чайкoвский"
    encodingsoftware =  "MuseScore 4.1.0"
    encodingdate =  "2023-07-21"
    source =  "http://musescore.com/user/19710/scores/8945924"
    subtitle =  \markup \column {
        \line { "2"}
        \line { ""} }
    
    }

#(set-global-staff-size 18.28571428571429)
\paper {
    
    paper-width = 29.69\cm
    paper-height = 42.01\cm
    top-margin = 1.5\cm
    bottom-margin = 1.5\cm
    left-margin = 1.5\cm
    right-margin = 1.51\cm
    indent = 2.9555656108597286\cm
    short-indent = 1.4777828054298643\cm
    }
\layout {
    \context { \Score
        skipBars = ##t
        }
    }
PartPOneVoiceOne =  \relative fis'' {
    \repeat volta 2 {
        \repeat volta 2 {
            \clef "treble" \time 5/4 \key d \major | % 1
            R4*25 \pageBreak ^\markup{ \bold {Allegretto con grazia} } | % 6
            R4*15 | % 9
            \stemDown fis4 ( _\mf ^\markup{ \bold\small {a. 3} }
            \stemDown g4 ) \once \omit TupletBracket
            \times 2/3  {
                \stemDown a8 ( _\< \stemDown g8 \stemDown a8 }
            \stemDown b4 \stemDown cis4 ) | \barNumberCheck #10
            \stemDown d4 ( _\! \stemDown b4 ) \stemDown cis2. _\> \break
            | % 11
            \stemDown a4 ( _\! _\mf \stemDown b4 ) \once \omit
            TupletBracket
            \times 2/3  {
                \stemDown cis8 ( _\< \stemDown b8 \stemDown cis8 }
            \stemDown d4 \stemDown e4 ) \pageBreak | % 12
            \stemDown fis4 ( _\! \stemDown d4 ) \stemDown e2. _\markup{
                \italic {più} } _ "" | % 13
            \stemDown e4 ( \stemDown fis4 ) \once \omit TupletBracket
            \times 2/3  {
                \stemDown e8 ( \stemDown fis8 \stemDown e8 }
            \stemDown d4 \stemDown cis4 ) | % 14
            \stemDown b8 -. r16 \stemDown cis16 ( \stemDown b8 ) -. r16
            \stemDown ais16 ( \stemDown b2. ) _\> | % 15
            \stemDown d4 ( _\! _\mf \stemDown e4 ) \once \omit
            TupletBracket
            \times 2/3  {
                \stemDown d8 ( \stemDown e8 \stemDown d8 }
            \stemDown cis4 \stemDown b4 ) }
        \alternative { {
                | % 16
                \stemDown a8 -. r16 \stemDown b16 ( \stemDown a8 ) -. r16
                \stemDown gis16 ( \stemDown a8 ) r8 r4 r4 }
            } \pageBreak }
    \alternative { {
            \stemDown a8 -. r16 \stemDown b16 ( \stemDown a8 ) -. r16
            \stemDown gis16 ( \stemDown a2 ~ \stemDown a8 ) r8 }
        } \bar "||"
    R4*20 \break | % 21
    R4*5 \pageBreak | % 22
    R4*10 | % 24
    r2 \stemUp cis,,8 ( ^ "I." ^ "II." _\mf \stemUp d8 \stemUp eis8 )
    \stemUp fis8 -. \stemUp gis8 -. \stemUp a8 -. | % 25
    \stemUp b4 ( \stemUp e,4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 ( \stemUp d8 \stemUp e8 }
    \stemUp fis4 \stemUp g4 ) | % 26
    \stemUp <fis a>8 -. r16 \stemUp <g b>16 ( \stemUp <fis a>8 ) -. r16
    \stemUp <e g>16 ( \stemUp <fis a>2. ) _\< \break | % 27
    \stemUp <fis a>4 ( _\! _\markup{ \italic {più} } _ "" \stemDown <b
        d>4 ) \stemUp <fis a>4 ( \stemUp <e g>4 \stemUp <d fis>4 ) | % 28
    \stemUp <d fis>8 -. r16 \stemUp <fis a>16 ( \stemUp <e g>8 ) -. r16
    \stemUp <d fis>16 ( \stemUp <cis e>2. ) _\> | % 29
    \stemUp <g' b>4 ( _\! _\mf \stemUp <cis, e>4 ) \stemUp <cis e>4 (
    \stemUp <d fis>4 \stemUp <e g>4 ) | \barNumberCheck #30
    \stemUp <fis a>8 -. r16 \stemUp <g b>16 ( \stemUp <fis a>8 ) -. r16
    \stemUp <e g>16 ( \stemUp <fis a>2. ) _\< | % 31
    \stemUp <fis a>4 ( \stemUp <gis b>4 ) \stemDown <a cis>4 ( _\! _\f
    \stemDown <cis e>4 \stemDown <b d>4 ) \pageBreak | % 32
    \stemUp <a cis>8 r16 \stemUp <fis a>16 ( \stemUp <gis b>8 ) -. r16
    \stemUp <e gis>16 ( \stemUp <e a>4 ~ ~ \stemUp <e a>8 ) r8 r4 | % 33
    \stemUp fis4 ( ^\markup{ \bold\small {a. 3} } _\mf \stemUp g4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ( _\< \stemUp gis8 \stemUp a8 }
    \stemDown b4 \stemDown cis4 ) | % 34
    \stemDown d4 ( _\! \stemDown b4 ) \stemDown cis2. _\> | % 35
    \stemUp a4 ( _\! \stemDown b4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( _\< \stemDown b8 \stemDown cis8 }
    \stemDown d4 \stemDown e4 ) | % 36
    \stemDown fis4 ( _\! \stemDown d4 ) \stemDown e2. \pageBreak | % 37
    \stemDown g4 ( _\f ^ "I.II." ^\markup{ \bold\small {a. 2} }
    \stemDown fis4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( \stemDown fis8 \stemDown e8 }
    \stemDown d4 \stemDown cis4 ) | % 38
    \stemDown fis8 -. r16 \stemDown g16 ( \stemDown fis8 ) -. r16
    \stemDown eis16 ( \stemDown fis2. ) | % 39
    \stemDown fis4 ( \stemDown e4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 ( \stemDown e8 \stemDown d8 }
    \stemDown cis4 ) \stemDown b4 ( _\< | \barNumberCheck #40
    \stemDown b'8 ) _\! _\ff _\> \stemDown a8 -. \stemDown g8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown es8 -. \stemDown d8 -.
    \stemDown cis8 -. \stemDown b8 -. \stemDown bes8 -. \pageBreak | % 41
    \stemUp a2 ~ _\! _\mf \stemUp a8 \stemUp a8 ~ \stemUp a8 \stemUp a8
    ~ \stemUp a8 \stemUp a8 ~ \pageBreak | % 42
    \stemUp a2 ~ \stemUp a8 \stemUp a8 ~ \stemUp a8 \stemUp a8 ~ \stemUp
    a8 \stemUp a8 ~ | % 43
    \stemUp a2 ~ \stemUp a8 \stemUp a8 ~ \stemUp a8 \stemUp a8 ~ \stemUp
    a8 \stemUp a8 ~ | % 44
    \stemUp a2 _\< \stemDown cis8 \stemDown cis8 ~ \stemDown cis8
    \stemDown cis8 ~ \stemDown cis8 \stemDown cis8 | % 45
    \stemDown c4 ( _\! _\f \stemUp a4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 ( \stemUp a8 \stemUp b8 }
    \stemDown c4 \stemDown d4 ) | % 46
    \stemDown e4 ( \stemDown c4 ) \stemDown d2. _\> | % 47
    \stemDown c4 ( _\! _\mf _\< \stemDown d4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( \stemDown d8 \stemDown e8 }
    \stemDown f4 \stemDown fis4 ) \pageBreak | % 48
    \stemDown g4 ( _\! _\ff _\> \stemDown e4 ) \stemDown d2. _\! _\f | % 49
    \stemDown d2 \stemDown es2 \stemDown es4 | \barNumberCheck #50
    \stemDown d4 \stemDown d4 \stemDown es2. | % 51
    \stemDown e2 \stemDown d2 \stemDown d4 | % 52
    \stemDown cis4 \stemDown cis4 \stemDown d2. \pageBreak | % 53
    \stemDown cis2 ~ \stemDown cis2. | % 54
    \stemDown d2 \stemDown d8 r8 r4 r4 | % 55
    \stemUp d,4 ( _\mf \stemUp e4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis8 ( _\< \stemUp e8 \stemUp fis8 }
    \stemUp g4 \stemUp a4 ) | % 56
    \stemDown b4 ( _\! _\> \stemUp cis,4 \stemUp d8 ) r8 _\! r4 r4
    \repeat volta 2 {
        | % 57
        \stemDown fis'4. ( _\p ^ "I." ^\markup{ \italic {con dolcezza e
                flebile} } _\< \stemDown fis8 ) -- \stemDown fis2 ( _\!
        _\> \stemDown e4 ) | % 58
        \stemDown d4. ( _\! _\< \stemDown d8 ) -- \stemDown d2 ( _\! _\>
        \stemDown cis4 ) \pageBreak | % 59
        \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemDown d2 ( _\!
        _\> \stemDown cis4 ) | \barNumberCheck #60
        \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemUp g2 ( _\!
        _\> \stemUp fis4 ) | % 61
        \stemDown fis'4. ( -- _\! _\< \stemDown fis8 ) -- \stemDown fis2
        ( _\! _\> \stemDown e4 ) | % 62
        \stemDown d4. ( -- _\! _\< \stemDown d8 ) -- \stemDown d2 ( _\!
        _\> \stemDown cis4 ) | % 63
        \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemDown d2 ( _\!
        _\> \stemDown cis4 ) | % 64
        \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemDown g'2 ( _\!
        _\sf _\> \stemDown fis4 ) }
    \pageBreak \repeat volta 2 {
        | % 65
        R4*25 | \barNumberCheck #70
        \stemDown g4. ( _\! ^\markup{ \bold\small {a. 3} } _\p _\<
        \stemDown a8 ) \stemDown bes2 ( \stemDown g4 ) \pageBreak | % 71
        \stemDown gis2 ~ _\! _\mf \stemDown gis2. _\< | % 72
        \stemDown d'4. ( _\! _\f _\< \stemDown e8 ) \stemDown fis2 ( _\!
        _\> \stemDown d4 ) }
    | % 73
    \stemDown fis,4. ( _\! _\p ^ "I." _\< \stemDown fis8 ) -- \stemDown
    fis2 ( _\! _\> \stemDown e4 ) | % 74
    \stemDown d4. ( _\! _\< \stemDown d8 ) -- \stemDown d2 ( _\! _\>
    \stemDown cis4 ) | % 75
    \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemDown d2 ( _\! _\>
    \stemDown cis4 ) | % 76
    \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemUp g2 ( _\! _\>
    \stemUp fis4 ) \pageBreak | % 77
    \stemDown fis'4. ( -- _\! _\< \stemDown fis8 ) -- \stemDown fis2 (
    _\! _\> \stemDown e4 ) | % 78
    \stemDown d4. ( -- _\! _\< \stemDown d8 ) -- \stemDown d2 ( _\! _\>
    \stemDown cis4 ) | % 79
    \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemDown d2 ( _\! _\>
    \stemDown cis4 ) | \barNumberCheck #80
    \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemDown g'2 ( _\!
    _\sf _\> \stemDown fis4 ) | % 81
    R4*5 | % 82
    \stemUp gis,4 ( _\! ^\markup{ \bold\small {a. 3} } _\p _\< \stemUp
    ais4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp ais8 \stemUp b8 }
    \stemDown cis4 \stemDown d4 \pageBreak | % 83
    \stemDown e8 ) _\! _\mf r8 r4 r2 r4 | % 84
    \stemDown b'4 ( _\p _\< \stemDown cis4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown cis8 \stemDown d8 }
    \stemDown e4 \stemDown fis4 ) | % 85
    R4*5 | % 86
    \stemUp gis,,4 ( _\! _\p _\< \stemUp ais4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp ais8 \stemUp b8 }
    \stemDown cis4 \stemDown d4 | % 87
    \stemDown e8 ) _\! _\mf r8 r4 r2 r4 | % 88
    \stemDown b'4 ( _\p _\< \stemDown cis4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown cis8 \stemDown d8 }
    \stemDown e4 \stemDown fis4 \pageBreak | % 89
    \stemDown g8 ) _\! _\mf r8 r4 r2 r4 | \barNumberCheck #90
    \stemDown b,,4 ( _\p _\< \stemDown cis4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown cis8 \stemDown d8 }
    \stemDown e4 \stemDown eis4 | % 91
    \stemDown fis8 ) _\! _\mf r8 r4 r2 r4 | % 92
    \stemDown b,4 ( _\p _\< \stemDown cis4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown cis8 \stemDown d8 }
    \stemDown e4 \stemDown fis4 | % 93
    \stemDown g8 ) _\! _\mf r8 r4 r2 r4 | % 94
    R4*5 \pageBreak | % 95
    R4*30 \pageBreak | % 101
    R4*15 | % 104
    \stemDown fis4 ( _\mf ^\markup{ \bold\small {a. 3} } \stemDown g4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 ( _\< \stemDown g8 \stemDown a8 }
    \stemDown b4 \stemDown cis4 ) | % 105
    \stemDown d4 ( _\! \stemDown b4 ) \stemDown cis2. _\> \break | % 106
    \stemDown a4 ( _\! \stemDown b4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( _\< \stemDown b8 \stemDown cis8 }
    \stemDown d4 \stemDown e4 ) | % 107
    \stemDown fis4 ( _\! \stemDown d4 ) \stemDown e2. _\markup{ \italic
        {più} } _ "" | % 108
    \stemDown e4 ( \stemDown fis4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( \stemDown fis8 \stemDown e8 }
    \stemDown d4 \stemDown cis4 ) | % 109
    \stemDown b8 -. r16 \stemDown cis16 ( \stemDown b8 ) -. r16
    \stemDown ais16 ( \stemDown b2. ) _\> | \barNumberCheck #110
    \stemDown d4 ( _\! _\mf \stemDown e4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 ( \stemDown e8 \stemDown d8 }
    \stemDown cis4 \stemDown b4 ) \pageBreak | % 111
    \stemDown a8 -. r16 \stemDown b16 ( \stemDown a8 ) -. r16 \stemDown
    gis16 ( \stemDown a2 ~ \stemDown a8 ) r8 | % 112
    R4*20 \break | % 116
    R4*5 \pageBreak | % 117
    R4*10 | % 119
    r2 \stemUp cis,,8 ( ^ "I." ^ "II." _\mf \stemUp d8 \stemUp eis8 )
    \stemUp fis8 -. \stemUp gis8 -. \stemUp a8 -. | \barNumberCheck #120
    \stemUp b4 ( \stemUp e,4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 ( \stemUp d8 \stemUp e8 }
    \stemUp fis4 \stemUp g4 ) | % 121
    \stemUp <fis a>8 -. r16 \stemUp <g b>16 ( \stemUp <fis a>8 ) -. r16
    \stemUp <e g>16 ( \stemUp <fis a>2. ) _\< \break | % 122
    \stemUp <fis a>4 ( _\! _\markup{ \italic {più} } _ "" \stemDown <b
        d>4 ) \stemUp <fis a>4 ( \stemUp <e g>4 \stemUp <d fis>4 )
    \pageBreak | % 123
    \stemUp <d fis>8 -. r16 \stemUp <fis a>16 ( \stemUp <e g>8 ) -. r16
    \stemUp <d fis>16 ( \stemUp <cis e>2. ) _\> | % 124
    \stemUp <g' b>4 ( _\! _\mf \stemUp <cis, e>4 ) \stemUp <cis e>4 (
    \stemUp <d fis>4 \stemUp <e g>4 ) | % 125
    \stemUp <fis a>8 -. r16 \stemUp <g b>16 ( \stemUp <fis a>8 ) -. r16
    \stemUp <e g>16 ( \stemUp <fis a>2. ) _\< | % 126
    \stemUp <fis a>4 ( \stemUp <gis b>4 ) \stemDown <a cis>4 ( _\! _\f
    \stemDown <cis e>4 \stemDown <b d>4 ) | % 127
    \stemUp <a cis>8 r16 \stemUp <fis a>16 ( \stemUp <gis b>8 ) -. r16
    \stemUp <e gis>16 ( \stemUp <e a>4 ~ ~ \stemUp <e a>8 ) r8 r4
    \pageBreak | % 128
    \stemUp fis4 ( _\mf ^ "I.II." ^\markup{ \bold\small {a. 2} } \stemUp
    g4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ( _\< \stemUp gis8 \stemUp a8 }
    \stemDown b4 \stemDown cis4 ) | % 129
    \stemDown d4 ( _\! \stemDown b4 ) \stemDown cis2. _\> |
    \barNumberCheck #130
    \stemUp a4 ( _\! \stemDown b4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( _\< \stemDown b8 \stemDown cis8 }
    \stemDown d4 \stemDown e4 ) | % 131
    \stemDown fis4 ( _\! \stemDown d4 ) \stemDown e2. | % 132
    \stemDown g4 ( _\f \stemDown fis4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( \stemDown fis8 \stemDown e8 }
    \stemDown d4 \stemDown cis4 ) \pageBreak | % 133
    \stemDown fis8 -. r16 \stemDown g16 ( \stemDown fis8 ) -. r16
    \stemDown eis16 ( \stemDown fis2. ) | % 134
    \stemDown fis4 ( \stemDown e4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 ( \stemDown e8 \stemDown d8 }
    \stemDown cis4 ) \stemDown b4 ( _\< | % 135
    \stemDown b'8 ) _\! _\ff _\> \stemDown a8 -. \stemDown g8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown es8 -. \stemDown d8 -.
    \stemDown cis8 -. \stemDown b8 -. \stemDown bes8 -. | % 136
    \stemUp a2 ~ _\! _\mf \stemUp a8 \stemUp a8 ~ \stemUp a8 \stemUp a8
    ~ \stemUp a8 \stemUp a8 ~ | % 137
    \stemUp a2 ~ \stemUp a8 \stemUp a8 ~ \stemUp a8 \stemUp a8 ~ \stemUp
    a8 \stemUp a8 ~ \pageBreak | % 138
    \stemUp a2 ~ \stemUp a8 \stemUp a8 ~ \stemUp a8 \stemUp a8 ~ \stemUp
    a8 \stemUp a8 ~ | % 139
    \stemUp a2 _\< \stemDown cis8 \stemDown cis8 ~ \stemDown cis8
    \stemDown cis8 ~ \stemDown cis8 \stemDown cis8 | \barNumberCheck
    #140
    \stemDown c4 ( _\! _\f \stemUp a4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 ( \stemUp a8 \stemUp b8 }
    \stemDown c4 \stemDown d4 ) | % 141
    \stemDown e4 ( \stemDown c4 ) \stemDown d2. _\> | % 142
    \stemDown c4 ( _\! _\mf _\< \stemDown d4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( \stemDown d8 \stemDown e8 }
    \stemDown f4 \stemDown fis4 ) \pageBreak | % 143
    \stemDown g4 ( _\! _\ff _\> \stemDown e4 ) \stemDown d2. _\! _\f | % 144
    \stemDown d2 \stemDown es2 \stemDown es4 | % 145
    \stemDown d4 \stemDown d4 \stemDown es2. | % 146
    \stemDown e2 \stemDown d2 \stemDown d4 | % 147
    \stemDown cis4 \stemDown cis4 \stemDown d2. \pageBreak | % 148
    \stemDown cis2 ~ \stemDown cis2. | % 149
    \stemDown d2 \stemDown d8 r8 r4 r4 | \barNumberCheck #150
    \stemUp d,4 ( _\mf \stemUp e4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis8 ( _\< \stemUp e8 \stemUp fis8 }
    \stemUp g4 \stemUp a4 ) | % 151
    \stemDown b4 ( _\! _\< \stemUp cis,4 \stemUp d8 ) r8 _\! r4 r4 | % 152
    R4*10 \pageBreak | % 154
    R4*45 \pageBreak | % 163
    R4*5 | % 164
    \stemUp f4. ( ^ "I." ^\markup{ \italic {solo} } _\f \stemUp f8 ) -.
    \stemUp e2 ( _\> \stemUp d4 ) | % 165
    R4*10 | % 167
    \stemDown fis'4. ( _\! _\f \stemDown fis8 ) -. \stemDown e2 ( _\>
    \stemDown d4 ) | % 168
    R4*15 \break | % 171
    R4*35 \pageBreak | % 178
    R4*5 \bar "|."
    _\! }

PartPOneVoiceFive =  \relative g'' {
    \repeat volta 2 {
        \repeat volta 2 {
            \clef "treble" \time 5/4 \key d \major | % 1
            R4*25 \pageBreak | % 6
            R4*25 \break | % 11
            R4*5 \pageBreak | % 12
            R4*20 }
        \alternative { {
                | % 16
                R4*5 }
            } \pageBreak }
    \alternative { {
            R4*5 }
        } \bar "||"
    R4*20 \break | % 21
    R4*5 \pageBreak | % 22
    R4*25 \break | % 27
    R4*25 \pageBreak | % 32
    R4*25 \pageBreak | % 37
    \stemDown g4 ( _\f ^ "III." \stemDown fis4 ) \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown e8 ( \stemDown fis8 \stemDown e8 }
    \stemDown d4 \stemDown cis4 ) | % 38
    \stemDown fis8 -. r16 \stemDown g16 ( \stemDown fis8 ) -. r16
    \stemDown eis16 ( \stemDown fis2. ) | % 39
    \stemDown fis4 ( \stemDown e4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 ( \stemDown e8 \stemDown d8 }
    \stemDown cis4 ) \stemDown b4 ( _\< | \barNumberCheck #40
    \stemDown b'8 ) _\! _\ff _\> \stemDown a8 -. \stemDown g8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown es8 -. \stemDown d8 -.
    \stemDown cis8 -. \stemDown b8 -. \stemDown bes8 -. \pageBreak | % 41
    \stemUp a2 ~ _\! _\mf \stemUp a8 \stemUp a8 ~ \stemUp a8 \stemUp a8
    ~ \stemUp a8 \stemUp a8 ~ \pageBreak | % 42
    \stemUp a2 ~ \stemUp a8 \stemUp a8 ~ \stemUp a8 \stemUp a8 ~ \stemUp
    a8 \stemUp a8 ~ | % 43
    \stemUp a2 ~ \stemUp a8 \stemUp a8 ~ \stemUp a8 \stemUp a8 ~ \stemUp
    a8 \stemUp a8 ~ | % 44
    \stemUp a2 _\< \stemDown cis8 \stemDown cis8 ~ \stemDown cis8
    \stemDown cis8 ~ \stemDown cis8 \stemDown cis8 | % 45
    \stemDown c4 ( _\! _\f \stemUp a4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 ( \stemUp a8 \stemUp b8 }
    \stemDown c4 \stemDown d4 ) | % 46
    \stemDown e4 ( \stemDown c4 ) \stemDown d2. _\> | % 47
    \stemDown c4 ( _\! _\mf _\< \stemDown d4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 ( \stemDown b8 \stemDown c8 }
    \stemDown d4 \stemDown dis4 ) \pageBreak | % 48
    \stemDown e4 ( _\! _\ff _\> \stemDown c4 ) \stemDown b2 ( _\! _\f
    \stemDown c4 ) | % 49
    \stemDown d2 \stemDown c2 \stemUp a4 | \barNumberCheck #50
    \stemDown bes4 \stemUp g4 \stemUp a2. | % 51
    \stemUp a2 \stemDown b2 \stemUp gis4 | % 52
    \stemUp a4 \stemUp fis4 \stemUp gis2. \pageBreak | % 53
    \stemUp a2 ~ \stemUp a2. | % 54
    \stemUp a2 \stemDown b8 r8 r4 r4 | % 55
    \stemUp d,4 ( _\mf \stemUp e4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis8 ( _\< \stemUp e8 \stemUp fis8 }
    \stemUp g4 \stemUp a4 ) | % 56
    \stemDown b4 ( _\! _\> \stemUp cis,4 \stemUp d8 ) r8 _\! r4 r4
    \repeat volta 2 {
        | % 57
        R4*10 \pageBreak | % 59
        R4*30 }
    \pageBreak \repeat volta 2 {
        | % 65
        R4*30 \pageBreak | % 71
        R4*10 }
    | % 73
    R4*20 \pageBreak | % 77
    R4*30 \pageBreak | % 83
    R4*30 \pageBreak | % 89
    R4*30 \pageBreak | % 95
    R4*30 \pageBreak | % 101
    R4*25 \break | % 106
    R4*25 \pageBreak | % 111
    R4*25 \break | % 116
    R4*5 \pageBreak | % 117
    R4*25 \break | % 122
    R4*5 \pageBreak | % 123
    R4*25 \pageBreak | % 128
    \stemUp fis4 ( _\mf ^ "III." \stemUp g4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ( _\< \stemUp gis8 \stemUp a8 }
    \stemDown b4 \stemDown cis4 ) | % 129
    \stemDown d4 ( _\! \stemDown b4 ) \stemDown cis2. _\> |
    \barNumberCheck #130
    \stemUp a4 ( _\! \stemDown b4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( _\< \stemDown b8 \stemDown cis8 }
    \stemDown d4 \stemDown e4 ) | % 131
    \stemDown fis4 ( _\! \stemDown d4 ) \stemDown e2. | % 132
    \stemDown g4 ( _\f \stemDown fis4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( \stemDown fis8 \stemDown e8 }
    \stemDown d4 \stemDown cis4 ) \pageBreak | % 133
    \stemDown fis8 -. r16 \stemDown g16 ( \stemDown fis8 ) -. r16
    \stemDown eis16 ( \stemDown fis2. ) | % 134
    \stemDown fis4 ( \stemDown e4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 ( \stemDown e8 \stemDown d8 }
    \stemDown cis4 ) \stemDown b4 ( _\< | % 135
    \stemDown b'8 ) _\! _\ff _\> \stemDown a8 -. \stemDown g8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown es8 -. \stemDown d8 -.
    \stemDown cis8 -. \stemDown b8 -. \stemDown bes8 -. | % 136
    \stemUp a2 ~ _\! _\mf \stemUp a8 \stemUp a8 ~ \stemUp a8 \stemUp a8
    ~ \stemUp a8 \stemUp a8 ~ | % 137
    \stemUp a2 ~ \stemUp a8 \stemUp a8 ~ \stemUp a8 \stemUp a8 ~ \stemUp
    a8 \stemUp a8 ~ \pageBreak | % 138
    \stemUp a2 ~ \stemUp a8 \stemUp a8 ~ \stemUp a8 \stemUp a8 ~ \stemUp
    a8 \stemUp a8 ~ | % 139
    \stemUp a2 _\< \stemDown cis8 \stemDown cis8 ~ \stemDown cis8
    \stemDown cis8 ~ \stemDown cis8 \stemDown cis8 | \barNumberCheck
    #140
    \stemDown c4 ( _\! _\f \stemUp a4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 ( \stemUp a8 \stemUp b8 }
    \stemDown c4 \stemDown d4 ) | % 141
    \stemDown e4 ( \stemDown c4 ) \stemDown d2. _\> | % 142
    \stemDown c4 ( _\! _\mf _\< \stemDown d4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 ( \stemDown b8 \stemDown c8 }
    \stemDown d4 \stemDown dis4 ) \pageBreak | % 143
    \stemDown e4 ( _\! _\ff _\> \stemDown c4 ) \stemDown b2 ( _\! _\f
    \stemDown c4 ) | % 144
    \stemDown d2 \stemDown c2 \stemUp a4 | % 145
    \stemDown bes4 \stemUp g4 \stemUp a2. | % 146
    \stemUp a2 \stemDown b2 \stemUp gis4 | % 147
    \stemUp a4 \stemUp fis4 \stemUp gis2. \pageBreak | % 148
    \stemUp a2 ~ \stemUp a2. | % 149
    \stemUp a2 \stemDown b8 r8 r4 r4 | \barNumberCheck #150
    \stemUp d,4 ( _\mf \stemUp e4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis8 ( _\< \stemUp e8 \stemUp fis8 }
    \stemUp g4 \stemUp a4 ) | % 151
    \stemDown b4 ( _\! _\< \stemUp cis,4 \stemUp d8 ) r8 _\! r4 r4 | % 152
    R4*10 \pageBreak | % 154
    R4*45 \pageBreak | % 163
    R4*20 | % 167
    \stemDown fis'4. ( ^ "II." _\f \stemDown fis8 ) -. \stemDown e2 (
    _\> \stemDown d4 ) | % 168
    R4*15 \break | % 171
    R4*35 \pageBreak | % 178
    R4*5 \bar "|."
    _\! }

PartPOneVoiceTwo =  \relative cis' {
    \repeat volta 2 {
        \repeat volta 2 {
            \clef "treble" \time 5/4 \key d \major s4*25 \pageBreak
            s4*25 \break s4*5 \pageBreak s1*5 }
        \alternative { {
                s4*5 }
            } \pageBreak }
    \alternative { {
            s4*5 }
        } \bar "||"
    s1*5 \break s4*5 \pageBreak s1*3 \stemDown cis8 ( \stemDown d8
    \stemDown cis8 ) \stemDown d8 -. \stemDown eis8 -. \stemDown fis8 -.
    | % 25
    \stemDown g4 ( \stemDown cis,4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( \stemDown d8 \stemDown cis8 }
    \stemDown d4 \stemDown e4 ) s4*5 \break s4*25 \pageBreak s4*25
    \pageBreak s1*5 \pageBreak s4*5 \pageBreak s2*15 \pageBreak s4*25
    \pageBreak s1*5 \repeat volta 2 {
        s2*5 \pageBreak s2*15 }
    \pageBreak \repeat volta 2 {
        s2*15 \pageBreak s2*5 }
    s1*5 \pageBreak s2*15 \pageBreak s2*15 \pageBreak s2*15 \pageBreak
    s2*15 \pageBreak s4*25 \break s4*25 \pageBreak s4*25 \break s4*5
    \pageBreak s1*3 \stemDown cis8 ( \stemDown d8 \stemDown cis8 )
    \stemDown d8 -. \stemDown eis8 -. \stemDown fis8 -. |
    \barNumberCheck #120
    \stemDown g4 ( \stemDown cis,4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( \stemDown d8 \stemDown cis8 }
    \stemDown d4 \stemDown e4 ) s4*5 \break s4*5 \pageBreak s4*25
    \pageBreak s4*25 \pageBreak s4*25 \pageBreak s4*25 \pageBreak s4*25
    \pageBreak s2*15 \pageBreak s4*45 \pageBreak s1*10 \break s4*35
    \pageBreak s4*5 \bar "|."
    }

PartPTwoVoiceOne =  \relative fis' {
    \repeat volta 2 {
        \clef "treble" \time 5/4 \key d \major | % 1
        R4*25 \pageBreak | % 6
        R4*15 | % 9
        \stemUp fis4 ( _\mf ^\markup{ \bold\small {a. 2} } \stemUp g4 )
        \once \omit TupletBracket
        \times 2/3  {
            \stemUp a8 ( _\< \stemUp g8 \stemUp a8 }
        \stemDown b4 \stemDown cis4 ) | \barNumberCheck #10
        \stemDown d4 ( _\! \stemDown b4 ) \stemDown cis2. _\> \break | % 11
        \stemUp a4 ( _\! _\mf \stemDown b4 ) \once \omit TupletBracket
        \times 2/3  {
            \stemDown cis8 ( _\< \stemDown b8 \stemDown cis8 }
        \stemDown d4 \stemDown e4 ) \pageBreak | % 12
        \stemDown fis4 ( _\! \stemDown d4 ) \stemDown e2. _\markup{
            \italic {più} } _ "" | % 13
        \stemDown e4 ( \stemDown fis4 ) \once \omit TupletBracket
        \times 2/3  {
            \stemDown e8 ( \stemDown fis8 \stemDown e8 }
        \stemDown d4 \stemDown cis4 ) | % 14
        \stemDown b8 -. r16 \stemDown cis16 ( \stemUp b8 ) -. r16
        \stemUp ais16 ( \stemDown b2. ) _\> | % 15
        \stemDown d4 ( _\! _\mf \stemDown e4 ) \once \omit TupletBracket
        \times 2/3  {
            \stemDown d8 ( \stemDown e8 \stemDown d8 }
        \stemDown cis4 \stemDown b4 ) | % 16
        \stemUp a8 -. r16 \stemUp b16 ( \stemUp a8 ) -. r16 \stemUp gis16
        ( \stemUp a8 ) r8 r4 r4 }
    \pageBreak \stemUp a8 -. r16 \stemUp b16 ( \stemUp a8 ) -. r16
    \stemUp gis16 ( \stemUp a2 ~ \stemUp a8 ) r8 \bar "||"
    R4*20 \break | % 21
    R4*5 \pageBreak | % 22
    R4*10 | % 24
    r2 \stemDown <a cis>8 ( _\mf \stemDown <b d>8 \stemDown <cis eis>8 )
    \stemDown <d fis>8 -. \stemDown <eis gis>8 -. \stemDown <fis a>8 -.
    | % 25
    \stemDown <g b>4 ( \stemDown <e g>4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown <cis e>8 ( \stemDown <b d>8 \stemDown <cis e>8 }
    \stemDown <d fis>4 \stemDown <e g>4 ) | % 26
    \stemDown <fis a>8 -. r16 \stemDown <g b>16 ( \stemDown <fis a>8 )
    -. r16 \stemDown <e g>16 ( \stemDown <fis a>2. ) _\< \break | % 27
    \stemDown <fis a>4 ( _\! _\markup{ \italic {più} } _ "" \stemDown
    <b d>4 ) \stemDown <fis a>4 ( \stemDown <e g>4 \stemDown <d fis>4 )
    | % 28
    \stemDown <d fis>8 -. r16 \stemDown <fis a>16 ( \stemDown <e g>8 )
    -. r16 \stemDown <b d>16 ( \stemDown <cis e>2. ) _\> | % 29
    \stemDown <g' b>4 ( _\! _\mf \stemDown <cis, e>4 ) \stemDown <cis e>4
    ( \stemDown <d fis>4 \stemDown <e g>4 ) | \barNumberCheck #30
    \stemDown <fis a>8 -. r16 \stemDown <g b>16 ( \stemDown <fis a>8 )
    -. r16 \stemDown <e g>16 ( \stemDown <fis a>2. ) _\< | % 31
    \stemDown <fis a>4 ( \stemDown <gis b>4 ) \stemDown <a cis>4 ( _\!
    _\f \stemDown <cis e>4 \stemDown <b d>4 ) \pageBreak | % 32
    \stemDown <a cis>8 r16 \stemDown <fis a>16 ( \stemDown <gis b>8 ) -.
    r16 \stemDown <e gis>16 ( \stemDown <e a>4 ~ ~ \stemDown <e a>8 ) r8
    r4 | % 33
    \stemUp fis,4 ( ^\markup{ \bold\small {a. 2} } _\mf \stemUp g4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ( _\< \stemUp gis8 \stemUp a8 }
    \stemDown b4 \stemDown cis4 ) | % 34
    \stemDown d4 ( _\! \stemDown b4 ) \stemDown cis2. _\> | % 35
    \stemUp a4 ( _\! \stemDown b4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( _\< \stemDown b8 \stemDown cis8 }
    \stemDown d4 \stemDown e4 ) | % 36
    \stemDown fis4 ( _\! \stemDown d4 ) \stemDown e2. \pageBreak | % 37
    \stemDown g4 ( _\f \stemDown fis4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( \stemDown fis8 \stemDown e8 }
    \stemDown d4 \stemDown cis4 ) | % 38
    \stemDown fis8 -. r16 \stemDown g16 ( \stemDown fis8 ) -. r16
    \stemDown eis16 ( \stemDown fis2. ) | % 39
    \stemDown fis4 ( \stemDown e4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 ( \stemDown e8 \stemDown d8 }
    \stemDown cis4 ) \stemDown b4 ( _\< | \barNumberCheck #40
    \stemDown b'8 ) _\! _\ff _\> \stemDown a8 -. \stemDown g8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown es8 -. \stemDown d8 -.
    \stemDown cis8 -. \stemDown b8 -. \stemDown bes8 -. \pageBreak | % 41
    \stemUp a2 ~ _\! _\mf \stemUp a8 \stemUp a8 ~ \stemUp a8 \stemUp a8
    ~ \stemUp a8 \stemUp a8 ~ \pageBreak | % 42
    \stemUp a2 ~ \stemUp a8 \stemUp a8 ~ \stemUp a8 \stemUp a8 ~ \stemUp
    a8 \stemUp a8 ~ | % 43
    \stemUp a2 ~ \stemUp a8 \stemUp a8 ~ \stemUp a8 \stemUp a8 ~ \stemUp
    a8 \stemUp a8 ~ | % 44
    \stemUp a2 _\< \stemDown cis8 \stemDown cis8 ~ \stemDown cis8
    \stemDown cis8 ~ \stemDown cis8 \stemDown cis8 | % 45
    \stemDown c4 ( _\! _\f \stemUp a4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 ( \stemUp a8 \stemUp b8 }
    \stemDown c4 \stemDown d4 ) | % 46
    \stemDown e4 ( \stemDown c4 ) \stemDown d2. _\> | % 47
    \stemDown c4 ( _\! _\mf _\< \stemDown d4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown <c e>8 ( \stemDown <b d>8 \stemDown <c e>8 }
    \stemDown <d f>4 \stemDown <dis fis>4 ) \pageBreak | % 48
    \stemDown <e g>4 ( _\! _\ff _\> \stemDown <c e>4 ) \stemUp d2. _\!
    _\f | % 49
    \stemUp d2 \stemUp es2 \stemUp es4 | \barNumberCheck #50
    \stemDown <bes d>4 \stemDown <g d'>4 \stemDown <a es'>2. | % 51
    \stemDown <a e'>2 \stemDown <b d>2 \stemDown <gis d'>4 | % 52
    \stemDown <a cis>4 \stemUp <fis cis'>4 \stemDown <gis d'>2.
    \pageBreak | % 53
    \stemDown <a cis>2 ~ ~ \stemDown <a cis>2. | % 54
    \stemDown <a d>2 \stemDown <b d>8 r8 r4 r4 | % 55
    R4*10 \repeat volta 2 {
        | % 57
        \stemDown b2 ^\markup{ \bold\small {a. 2} } _\p _\< \stemUp ais2.
        _\! _\> | % 58
        \stemDown b2 _\! _\< \stemUp e,2. _\! _\> \pageBreak | % 59
        \stemUp fis2 _\! _\< \stemUp g2. _\! _\> | \barNumberCheck #60
        \stemUp fis2 _\! _\< \stemUp e2 ( _\! _\> \stemUp d4 ) | % 61
        \stemDown b'2 _\! _\< \stemUp ais2. _\! _\> | % 62
        \stemDown b2 _\! _\< \stemUp e,2. _\! _\> | % 63
        \stemUp fis2 _\! _\< \stemUp g2. _\! _\> | % 64
        \stemUp fis2 _\! _\< \stemUp e2 ( _\! _\sf _\> \stemUp d4 ) }
    \pageBreak \repeat volta 2 {
        | % 65
        R4*25 | \barNumberCheck #70
        \stemDown <g g'>4. ( _\! _\p _\< \stemDown <a a'>8 ) \stemDown
        <bes bes'>2 ( \stemDown <g g'>4 ) \pageBreak | % 71
        \stemDown <gis gis'>2 ~ ~ _\! _\mf \stemDown <gis gis'>2. _\< | % 72
        \stemUp <d d'>4. ( _\! _\f _\< \stemUp <e e'>8 ) \stemDown <fis
            fis'>2 ( _\! _\> \stemUp <d d'>4 ) }
    | % 73
    \stemDown b'2 _\! ^\markup{ \bold\small {a. 2} } _\p _\< \stemUp ais2.
    _\! _\> | % 74
    \stemDown b2 _\! _\< \stemUp e,2. _\! _\> | % 75
    \stemUp fis2 _\! _\< \stemUp g2. _\! _\> | % 76
    \stemUp fis2 _\! _\< \stemUp e2 ( _\! _\> \stemUp d4 ) \pageBreak | % 77
    \stemDown b'2 _\! _\< \stemUp ais2. _\! _\> | % 78
    \stemDown b2 _\! _\< \stemUp e,2. _\! _\> | % 79
    \stemUp fis2 _\! _\< \stemUp g2. _\! _\> | \barNumberCheck #80
    \stemUp fis2 _\! _\< \stemUp e2 ( _\! _\sf _\> \stemUp d4 ) | % 81
    R4*5 | % 82
    \stemUp gis4 ( _\! _\p _\< \stemUp ais4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp ais8 \stemUp b8 }
    \stemDown cis4 \stemDown d4 \pageBreak | % 83
    \stemDown e8 ) _\! _\mf r8 r4 r2 r4 | % 84
    \stemDown b4 ( _\p _\< \stemDown cis4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown cis8 \stemDown d8 }
    \stemDown e4 \stemDown fis4 ) | % 85
    R4*5 | % 86
    \stemUp gis,4 ( _\! _\p _\< \stemUp ais4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp ais8 \stemUp b8 }
    \stemDown cis4 \stemDown d4 | % 87
    \stemDown e8 ) _\! _\mf r8 r4 r2 r4 | % 88
    \stemDown b4 ( _\p _\< \stemDown cis4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown cis8 \stemDown d8 }
    \stemDown e4 \stemDown fis4 \pageBreak | % 89
    \stemDown g8 ) _\! _\mf r8 r4 r2 r4 | \barNumberCheck #90
    \stemDown b,4 ( _\p _\< \stemDown cis4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown cis8 \stemDown d8 }
    \stemDown e4 \stemDown eis4 | % 91
    \stemDown fis8 ) _\! _\mf r8 r4 r2 r4 | % 92
    \stemDown b,4 ( _\p _\< \stemDown cis4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown cis8 \stemDown d8 }
    \stemDown e4 \stemDown fis4 | % 93
    \stemDown g8 ) _\! _\mf r8 r4 r2 r4 | % 94
    \stemUp b,,4 ( _\p _\< \stemUp cis4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp d8 \stemUp cis8 \stemUp d8 }
    \stemUp e4 \stemUp eis4 \pageBreak | % 95
    \stemUp fis8 ) _\! _\mf r8 r4 r2 r4 | % 96
    R4*25 \pageBreak | % 101
    R4*15 | % 104
    \stemUp fis4 ( _\mf ^\markup{ \bold\small {a. 2} } \stemUp g4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ( _\< \stemUp g8 \stemUp a8 }
    \stemDown b4 \stemDown cis4 ) | % 105
    \stemDown d4 ( _\! \stemDown b4 ) \stemDown cis2. _\> \break | % 106
    \stemUp a4 ( _\! \stemDown b4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( _\< \stemDown b8 \stemDown cis8 }
    \stemDown d4 \stemDown e4 ) | % 107
    \stemDown fis4 ( _\! \stemDown d4 ) \stemDown e2. _\markup{ \italic
        {più} } _ "" | % 108
    \stemDown e4 ( \stemDown fis4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( \stemDown fis8 \stemDown e8 }
    \stemDown d4 \stemDown cis4 ) | % 109
    \stemDown b8 -. r16 \stemDown cis16 ( \stemUp b8 ) -. r16 \stemUp
    ais16 ( \stemDown b2. ) _\> | \barNumberCheck #110
    \stemDown d4 ( _\! _\mf \stemDown e4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 ( \stemDown e8 \stemDown d8 }
    \stemDown cis4 \stemDown b4 ) \pageBreak | % 111
    \stemUp a8 -. r16 \stemUp b16 ( \stemUp a8 ) -. r16 \stemUp gis16 (
    \stemUp a2 ~ \stemUp a8 ) r8 | % 112
    R4*20 \break | % 116
    R4*5 \pageBreak | % 117
    R4*10 | % 119
    r2 \stemDown <a cis>8 ( _\mf \stemDown <b d>8 \stemDown <cis eis>8 )
    \stemDown <d fis>8 -. \stemDown <eis gis>8 -. \stemDown <fis a>8 -.
    | \barNumberCheck #120
    \stemDown <g b>4 ( \stemDown <e g>4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown <cis e>8 ( \stemDown <b d>8 \stemDown <cis e>8 }
    \stemDown <d fis>4 \stemDown <e g>4 ) | % 121
    \stemDown <fis a>8 -. r16 \stemDown <g b>16 ( \stemDown <fis a>8 )
    -. r16 \stemDown <e g>16 ( \stemDown <fis a>2. ) _\< \break | % 122
    \stemDown <fis a>4 ( _\! _\markup{ \italic {più} } _ "" \stemDown
    <b d>4 ) \stemDown <fis a>4 ( \stemDown <e g>4 \stemDown <d fis>4 )
    \pageBreak | % 123
    \stemDown <d fis>8 -. r16 \stemDown <fis a>16 ( \stemDown <e g>8 )
    -. r16 \stemDown <b d>16 ( \stemDown <cis e>2. ) _\> | % 124
    \stemDown <g' b>4 ( _\! _\mf \stemDown <cis, e>4 ) \stemDown <cis e>4
    ( \stemDown <d fis>4 \stemDown <e g>4 ) | % 125
    \stemDown <fis a>8 -. r16 \stemDown <g b>16 ( \stemDown <fis a>8 )
    -. r16 \stemDown <e g>16 ( \stemDown <fis a>2. ) _\< | % 126
    \stemDown <fis a>4 ( \stemDown <gis b>4 ) \stemDown <a cis>4 ( _\!
    _\f \stemDown <cis e>4 \stemDown <b d>4 ) | % 127
    \stemDown <a cis>8 r16 \stemDown <fis a>16 ( \stemDown <gis b>8 ) -.
    r16 \stemDown <e gis>16 ( \stemDown <e a>4 ~ ~ \stemDown <e a>8 ) r8
    r4 \pageBreak | % 128
    \stemUp fis,4 ( ^\markup{ \bold\small {a. 2} } _\mf \stemUp g4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ( _\< \stemUp gis8 \stemUp a8 }
    \stemDown b4 \stemDown cis4 ) | % 129
    \stemDown d4 ( _\! \stemDown b4 ) \stemDown cis2. _\> |
    \barNumberCheck #130
    \stemUp a4 ( _\! \stemDown b4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( _\< \stemDown b8 \stemDown cis8 }
    \stemDown d4 \stemDown e4 ) | % 131
    \stemDown fis4 ( _\! \stemDown d4 ) \stemDown e2. | % 132
    \stemDown g4 ( _\f \stemDown fis4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( \stemDown fis8 \stemDown e8 }
    \stemDown d4 \stemDown cis4 ) \pageBreak | % 133
    \stemDown fis8 -. r16 \stemDown g16 ( \stemDown fis8 ) -. r16
    \stemDown eis16 ( \stemDown fis2. ) | % 134
    \stemDown fis4 ( \stemDown e4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 ( \stemDown e8 \stemDown d8 }
    \stemDown cis4 ) \stemDown b4 ( _\< | % 135
    \stemDown b'8 ) _\! _\ff _\> \stemDown a8 -. \stemDown g8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown es8 -. \stemDown d8 -.
    \stemDown cis8 -. \stemDown b8 -. \stemDown bes8 -. | % 136
    \stemUp a2 ~ _\! _\mf \stemUp a8 \stemUp a8 ~ \stemUp a8 \stemUp a8
    ~ \stemUp a8 \stemUp a8 ~ | % 137
    \stemUp a2 ~ \stemUp a8 \stemUp a8 ~ \stemUp a8 \stemUp a8 ~ \stemUp
    a8 \stemUp a8 ~ \pageBreak | % 138
    \stemUp a2 ~ \stemUp a8 \stemUp a8 ~ \stemUp a8 \stemUp a8 ~ \stemUp
    a8 \stemUp a8 ~ | % 139
    \stemUp a2 _\< \stemDown cis8 \stemDown cis8 ~ \stemDown cis8
    \stemDown cis8 ~ \stemDown cis8 \stemDown cis8 | \barNumberCheck
    #140
    \stemDown c4 ( _\! _\f \stemUp a4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 ( \stemUp a8 \stemUp b8 }
    \stemDown c4 \stemDown d4 ) | % 141
    \stemDown e4 ( \stemDown c4 ) \stemDown d2. _\> | % 142
    \stemDown c4 ( _\! _\mf _\< \stemDown d4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown <c e>8 ( \stemDown <b d>8 \stemDown <c e>8 }
    \stemDown <d f>4 \stemDown <dis fis>4 ) \pageBreak | % 143
    \stemDown <e g>4 ( _\! _\ff _\> \stemDown <c e>4 ) \stemUp d2. _\!
    _\f | % 144
    \stemUp d2 \stemUp es2 \stemUp es4 | % 145
    \stemDown <bes d>4 \stemDown <g d'>4 \stemDown <a es'>2. | % 146
    \stemDown <a e'>2 \stemDown <b d>2 \stemDown <gis d'>4 | % 147
    \stemDown <a cis>4 \stemUp <fis cis'>4 \stemDown <gis d'>2.
    \pageBreak | % 148
    \stemDown <a cis>2 ~ ~ \stemDown <a cis>2. | % 149
    \stemDown <a d>2 \stemDown <b d>8 r8 r4 r4 | \barNumberCheck #150
    R4*10 | % 152
    \stemDown <fis' d'>2 _\mf \stemDown <e cis'>2. -> | % 153
    \stemDown <d b'>2 \stemDown <cis a'>2. -> \pageBreak | % 154
    \stemDown <b g'>2 \stemDown <a fis'>2. -> | % 155
    \stemDown <a e'>2 \stemUp <fis d'>2. -> | % 156
    R4*25 | % 161
    \stemDown <a a'>2 ~ ~ _\p \stemDown <a a'>2. | % 162
    R4*5 \pageBreak | % 163
    \stemDown <a a'>2 ~ ~ _\p \stemDown <a a'>2. | % 164
    R4*5 | % 165
    \stemDown bes4. ( ^ "I." ^\markup{ \italic {solo} } _\f \stemDown
    bes8 ) -. \stemUp a2 ( _\> \stemUp g4 ) | % 166
    R4*10 | % 168
    \stemDown <a a'>4. ( _\! _\f \stemDown <a a'>8 ) -. \stemDown <g g'>2
    ( _\> \stemDown <fis fis'>4 | % 169
    \stemUp <e e'>8 ) _\! r8 r4 r2 r4 | \barNumberCheck #170
    R4*5 \break | % 171
    R4*35 \pageBreak | % 178
    R4*5 \bar "|."
    }

PartPTwoVoiceTwo =  \relative b' {
    \repeat volta 2 {
        \clef "treble" \time 5/4 \key d \major s4*25 \pageBreak s4*25
        \break s4*5 \pageBreak s4*25 }
    \pageBreak s4*5 \bar "||"
    s1*5 \break s4*5 \pageBreak s4*25 \break s4*25 \pageBreak s4*25
    \pageBreak s1*5 \pageBreak s4*5 \pageBreak s2*15 \pageBreak s2
    \stemDown b2 ( \stemDown c4 ) | % 49
    \stemDown d2 \stemDown c2 \stemDown a4 s4*15 \pageBreak s1*5 \repeat
    volta 2 {
        s2*5 \pageBreak s2*15 }
    \pageBreak \repeat volta 2 {
        s2*15 \pageBreak s2*5 }
    s1*5 \pageBreak s2*15 \pageBreak s2*15 \pageBreak s2*15 \pageBreak
    s2*15 \pageBreak s4*25 \break s4*25 \pageBreak s4*25 \break s4*5
    \pageBreak s4*25 \break s4*5 \pageBreak s4*25 \pageBreak s4*25
    \pageBreak s4*25 \pageBreak s4*25 \pageBreak s2 \stemDown b2 (
    \stemDown c4 ) | % 144
    \stemDown d2 \stemDown c2 \stemDown a4 s4*15 \pageBreak s2*15
    \pageBreak s4*45 \pageBreak s1*10 \break s4*35 \pageBreak s4*5 \bar
    "|."
    }

PartPThreeVoiceOne =  \relative f'' {
    \repeat volta 2 {
        \clef "treble" \time 5/4 \key f \major \transposition a | % 1
        r2 r4 \stemDown <f a>4 ( _\mf \stemDown <a, c>8 ) r8 | % 2
        r2 r4 \stemDown <c g'>4 ( \stemUp <g c>8 ) r8 | % 3
        r2 r4 \stemDown <c f>4 ( \stemUp <e, c'>8 ) r8 | % 4
        r2 r4 \stemDown <c' e>4 ( \stemUp <e, c'>8 ) r8 | % 5
        r2 r4 \stemDown <cis' a'>4 ( \stemDown <a cis>8 ) r8 \pageBreak
        | % 6
        r2 r4 \stemDown <d f>4 ( \stemUp <f, d'>8 ) r8 | % 7
        r2 r4 \stemDown <g' b>4 ( \stemUp <g, b>8 ) r8 | % 8
        \stemDown <g' bes>8 _\f r8 r4 r2 r4 | % 9
        \stemUp a,,4 ( _\mf ^\markup{ \bold\small {a. 2} } \stemUp bes4
        ) \once \omit TupletBracket
        \times 2/3  {
            \stemUp c8 ( _\< \stemUp bes8 \stemUp c8 }
        \stemUp d4 \stemUp e4 ) | \barNumberCheck #10
        \stemUp f4 ( _\! \stemUp d4 ) \stemUp e2. _\> \break | % 11
        \stemUp c4 ( _\! _\mf \stemUp d4 ) \once \omit TupletBracket
        \times 2/3  {
            \stemUp e8 ( _\< \stemUp d8 \stemUp e8 }
        \stemUp f4 \stemUp g4 ) \pageBreak | % 12
        \stemUp a4 ( _\! \stemUp f4 ) \stemUp g2. _\markup{ \italic
            {più} } _ "" | % 13
        \stemUp g4 ( \stemUp a4 ) \once \omit TupletBracket
        \times 2/3  {
            \stemUp g8 ( \stemUp a8 \stemUp g8 }
        \stemUp f4 \stemUp e4 ) | % 14
        \stemUp d8 -. r16 \stemUp e16 ( \stemUp d8 ) -. r16 \stemUp cis16
        ( \stemUp d2. ) _\> | % 15
        \stemUp f4 ( _\! _\mf \stemUp g4 ) \once \omit TupletBracket
        \times 2/3  {
            \stemUp f8 ( \stemUp g8 \stemUp f8 }
        \stemUp e4 \stemUp d4 ) | % 16
        \stemUp c8 -. r16 \stemUp d16 ( \stemUp c8 ) -. r16 \stemUp b16
        ( \stemUp c8 ) r8 r4 r4 }
    \pageBreak \stemUp c8 -. r16 \stemUp d16 ( \stemUp c8 ) -. r16
    \stemUp b16 ( \stemUp c2 ~ \stemUp c8 ) r8 \bar "||"
    r8 \stemUp c8 ( _\mf \stemUp e8 \stemUp g8 \stemDown c8 ) r8 r4 r4 | % 18
    r8 \stemUp c,8 ( \stemUp f8 \stemUp a8 \stemDown c8 ) r8 r4 r4 | % 19
    r8 \stemUp c,8 ( \stemUp f8 \stemUp a8 \stemDown c8 ) r8 r4 r4 |
    \barNumberCheck #20
    r8 \stemUp c,8 ( \stemUp e8 \stemUp g8 \stemDown c8 ) r8 r4 r4
    \break | % 21
    r8 \stemUp c,8 ( \stemUp e8 \stemUp g8 \stemDown c8 ) r8 r4 r4
    \pageBreak | % 22
    r8 \stemUp c,8 ( \stemUp f8 \stemUp a8 \stemDown c8 ) r8 r4 r4 | % 23
    r8 \stemUp e,8 ( _\f \stemUp gis8 \stemUp b8 \stemDown e8 ) r8 r4 r4
    | % 24
    r8 \stemDown a,8 ( \stemDown c8 \stemDown e8 \stemDown a8 ) r8 r4 r4
    | % 25
    \stemUp <e, g>4 ( _\mf \stemDown <bes' d>4 ) \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown <bes d>8 ( \stemDown <a c>8 \stemDown <bes d>8 }
    \stemDown <a c>4 \stemUp <g bes>4 ) | % 26
    \stemUp <f a>8 -. r16 \stemUp <e g>16 ( \stemUp <f a>8 ) -. r16
    \stemUp <g bes>16 ( \stemUp <f a>2. ) _\< \break | % 27
    \stemUp <f a>4 ( _\! _\markup{ \italic {più} } _ "" \stemUp <d f>4
    ) \stemUp <f a>4 ( \stemUp <g bes>4 \stemDown <a c>4 ) | % 28
    \stemUp <a c>8 -. r16 \stemUp <f a>16 ( \stemUp <g bes>8 ) -. r16
    \stemUp <d c'>16 ( \stemUp <g bes>2. ) _\> | % 29
    \stemUp <e g>4 ( _\! _\mf \stemDown <bes' d>4 ) \stemDown <bes d>4 (
    \stemDown <a c>4 \stemUp <g bes>4 ) | \barNumberCheck #30
    \stemUp <f a>8 -. r16 \stemUp <e g>16 ( \stemUp <f a>8 ) -. r16
    \stemUp <g bes>16 ( \stemUp <f a>2. ) _\< | % 31
    \stemDown <c' e>4 ( \stemDown <b d>4 ) \stemDown <a c>2. ~ ~ _\! _\f
    \pageBreak | % 32
    \stemDown <a c>8 r16 \stemDown <a c>16 ( \stemDown <g b>8 ) -. r16
    \stemDown <d' f>16 ( \stemDown <c e>4 ~ ~ \stemDown <c e>8 ) r8 r4 | % 33
    \stemUp a,4 ( ^\markup{ \bold\small {a. 2} } _\mf \stemUp bes4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 ( _\< \stemUp b8 \stemUp c8 }
    \stemUp d4 \stemUp e4 ) | % 34
    \stemUp f4 ( _\! \stemUp d4 ) \stemUp e2. _\> | % 35
    \stemUp c4 ( _\! \stemUp d4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 ( _\< \stemUp d8 \stemUp e8 }
    \stemUp f4 \stemUp g4 ) | % 36
    \stemUp a4 ( _\! \stemUp f4 ) \stemUp g2. \pageBreak | % 37
    \stemDown bes4 ( _\f \stemUp a4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 ( \stemUp a8 \stemUp g8 }
    \stemUp f4 \stemUp e4 ) | % 38
    \stemUp a8 -. r16 \stemUp bes16 ( \stemUp a8 ) -. r16 \stemUp gis16
    ( \stemUp a2. ) | % 39
    \stemUp a4 ( \stemUp g4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp f8 ( \stemUp g8 \stemUp f8 }
    \stemUp e4 ) \stemUp d4 ( _\< | \barNumberCheck #40
    \stemDown d'8 ) _\! _\ff _\> \stemDown c8 -. \stemDown bes8 -.
    \stemDown a8 -. \stemUp g8 -. \stemUp ges8 -. \stemUp f8 -. \stemUp
    e8 -. \stemUp d8 -. \stemUp des8 -. \pageBreak | % 41
    \stemUp c2 ~ _\! _\mf \stemUp c8 \stemUp c8 ~ \stemUp c8 \stemUp c8
    ~ \stemUp c8 \stemUp c8 ~ \pageBreak | % 42
    \stemUp c2 ~ \stemUp c8 \stemUp c8 ~ \stemUp c8 \stemUp c8 ~ \stemUp
    c8 \stemUp c8 ~ | % 43
    \stemUp c2 ~ \stemUp c8 \stemUp c8 ~ \stemUp c8 \stemUp c8 ~ \stemUp
    c8 \stemUp c8 ~ | % 44
    \stemUp c2 _\< \stemUp e8 \stemUp e8 ~ \stemUp e8 \stemUp e8 ~
    \stemUp e8 \stemUp e8 | % 45
    \stemUp es4 ( _\! _\f \stemUp c4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp d8 ( \stemUp c8 \stemUp d8 }
    \stemUp es4 \stemUp f4 ) | % 46
    \stemUp g4 ( \stemUp es4 ) \stemUp f2. _\> | % 47
    \stemUp es4 ( _\! _\mf _\< \stemDown f8 ) \stemDown f'8 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown <es g>8 ( \stemDown <d f>8 \stemDown <es g>8 }
    \stemDown <f as>4 \stemDown <fis a>4 ) \pageBreak | % 48
    \stemDown <g bes>4 ( _\! _\ff _\> \stemDown <es g>4 ) \stemUp f2.
    _\! _\f | % 49
    \stemUp f2 \stemUp ges2 \stemUp ges4 | \barNumberCheck #50
    \stemDown <des f>4 \stemDown <bes f'>4 \stemDown <c ges'>2. | % 51
    \stemDown <c g'>2 \stemDown <d f>2 \stemDown <b f'>4 | % 52
    \stemDown <c e>4 \stemDown <a e'>4 \stemDown <b f'>2. \pageBreak | % 53
    \stemDown <c e>2 ~ ~ \stemDown <c e>2. | % 54
    \stemDown <c f>2 \stemDown <d f>8 r8 r4 r4 | % 55
    R4*10 \repeat volta 2 {
        | % 57
        \stemUp d,2 ^\markup{ \bold\small {a. 2} } _\p _\< \stemUp cis2.
        _\! _\> | % 58
        \stemUp d2 _\! _\< \stemUp g,2. _\! _\> \pageBreak | % 59
        \stemUp a2 _\! _\< \stemUp bes2. _\! _\> | \barNumberCheck #60
        \stemUp a2 _\! _\< \stemUp g2 ( _\! _\> \stemUp f4 ) | % 61
        \stemUp d'2 _\! _\< \stemUp cis2. _\! _\> | % 62
        \stemUp d2 _\! _\< \stemUp g,2. _\! _\> | % 63
        \stemUp a2 _\! _\< \stemUp bes2. _\! _\> | % 64
        \stemUp a2 _\! _\< \stemUp g2 ( _\! _\sf _\> \stemUp f4 ) }
    \pageBreak \repeat volta 2 {
        | % 65
        R4*25 | \barNumberCheck #70
        \stemDown <bes' bes'>4. ( _\! _\p _\< \stemDown <c c'>8 )
        \stemDown <des des'>2 ( \stemDown <bes bes'>4 ) \pageBreak | % 71
        \stemUp <b, b'>2 ~ ~ _\! _\mf \stemUp <b b'>2. _\< | % 72
        \stemDown <f' f'>4. ( _\! _\f _\< \stemDown <g g'>8 ) \stemDown
        <a a'>2 ( _\! _\> \stemDown <f f'>4 ) }
    | % 73
    \stemUp d2 _\! ^\markup{ \bold\small {a. 2} } _\p _\< \stemUp cis2.
    _\! _\> | % 74
    \stemUp d2 _\! _\< \stemUp g,2. _\! _\> | % 75
    \stemUp a2 _\! _\< \stemUp bes2. _\! _\> | % 76
    \stemUp a2 _\! _\< \stemUp g2 ( _\! _\> \stemUp f4 ) \pageBreak | % 77
    \stemUp d'2 _\! _\< \stemUp cis2. _\! _\> | % 78
    \stemUp d2 _\! _\< \stemUp g,2. _\! _\> | % 79
    \stemUp a2 _\! _\< \stemUp bes2. _\! _\> | \barNumberCheck #80
    \stemUp a2 _\! _\< \stemUp g2 ( _\! _\sf _\> \stemUp f4 ) | % 81
    R4*5 | % 82
    \stemUp b4 ( _\! _\p _\< \stemUp cis4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp d8 \stemUp cis8 \stemUp d8 }
    \stemUp e4 \stemUp f4 \pageBreak | % 83
    \stemUp g8 ) _\! _\mf r8 r4 r2 r4 | % 84
    \stemUp <d d'>4 ( _\p _\< \stemUp <e e'>4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <f f'>8 \stemDown <e e'>8 \stemDown <f f'>8 }
    \stemDown <g g'>4 \stemDown <a a'>4 ) | % 85
    R4*5 | % 86
    \stemUp b,4 ( _\! _\p _\< \stemUp cis4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp d8 \stemUp cis8 \stemUp d8 }
    \stemUp e4 \stemUp f4 | % 87
    \stemUp g8 ) _\! _\mf r8 r4 r2 r4 | % 88
    \stemUp <d d'>4 ( _\p _\< \stemUp <e e'>4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown <f f'>8 \stemDown <e e'>8 \stemDown <f f'>8 }
    \stemDown <g g'>4 \stemDown <a a'>4 \pageBreak | % 89
    \stemUp bes'8 ) _\! _\mf _\> r8 r4 r2 r4 | \barNumberCheck #90
    \stemUp d,,4 ( _\p ^\markup{ \bold\small {a. 2} } _\< \stemUp e4
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp f8 \stemUp e8 \stemUp f8 }
    \stemUp g4 \stemUp gis4 | % 91
    \stemUp a8 ) _\! _\mf r8 r4 r2 r4 | % 92
    \stemUp d,4 ( _\p _\< \stemUp e4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp f8 \stemUp e8 \stemUp f8 }
    \stemUp g4 \stemUp a4 ) | % 93
    \stemDown bes2 ~ _\! _\mf _\> \stemDown bes8 _\! r8 r4 r4 | % 94
    \stemUp d,4 ( _\p _\< \stemUp <e, e'>4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <f f'>8 \stemUp <e e'>8 \stemUp <f f'>8 }
    \stemUp <g g'>4 \stemUp <gis gis'>4 \pageBreak | % 95
    \stemUp <a a'>8 ) _\! _\mf r8 r4 r2 r4 | % 96
    r2 r4 \stemDown <f'' a>4 ( _\mf \stemDown <a, c>8 ) r8 | % 97
    r2 r4 \stemDown <c g'>4 ( \stemUp <g c>8 ) r8 | % 98
    r2 r4 \stemDown <c f>4 ( \stemUp <e, c'>8 ) r8 | % 99
    r2 r4 \stemDown <c' e>4 ( \stemUp <e, c'>8 ) r8 | \barNumberCheck
    #100
    r2 r4 \stemDown <cis' a'>4 ( \stemDown <a cis>8 ) r8 \pageBreak | % 101
    r2 r4 \stemDown <d f>4 ( \stemUp <f, d'>8 ) r8 | % 102
    r2 r4 \stemDown <g' b>4 ( \stemUp <g, b>8 ) r8 | % 103
    \stemDown <g' bes>8 _\f r8 r4 r2 r4 | % 104
    \stemUp a,,4 ( _\mf ^\markup{ \bold\small {a. 2} } \stemUp bes4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 ( _\< \stemUp bes8 \stemUp c8 }
    \stemUp d4 \stemUp e4 ) | % 105
    \stemUp f4 ( _\! \stemUp d4 ) \stemUp e2. _\> \break | % 106
    \stemUp c4 ( _\! \stemUp d4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 ( _\< \stemUp d8 \stemUp e8 }
    \stemUp f4 \stemUp g4 ) | % 107
    \stemUp a4 ( _\! \stemUp f4 ) \stemUp g2. _\markup{ \italic {più} }
    _ "" | % 108
    \stemUp g4 ( \stemUp a4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 ( \stemUp a8 \stemUp g8 }
    \stemUp f4 \stemUp e4 ) | % 109
    \stemUp d8 -. r16 \stemUp e16 ( \stemUp d8 ) -. r16 \stemUp cis16 (
    \stemUp d2. ) _\> | \barNumberCheck #110
    \stemUp f4 ( _\! _\mf \stemUp g4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp f8 ( \stemUp g8 \stemUp f8 }
    \stemUp e4 \stemUp d4 ) \pageBreak | % 111
    \stemUp c8 -. r16 \stemUp d16 ( \stemUp c8 ) -. r16 \stemUp b16 (
    \stemUp c2 ~ \stemUp c8 ) r8 | % 112
    r8 \stemUp c8 ( _\mf \stemUp e8 \stemUp g8 \stemDown c8 ) r8 r4 r4 | % 113
    r8 \stemUp c,8 ( \stemUp f8 \stemUp a8 \stemDown c8 ) r8 r4 r4 | % 114
    r8 \stemUp c,8 ( \stemUp f8 \stemUp a8 \stemDown c8 ) r8 r4 r4 | % 115
    r8 \stemUp c,8 ( \stemUp e8 \stemUp g8 \stemDown c8 ) r8 r4 r4
    \break | % 116
    r8 \stemUp c,8 ( \stemUp e8 \stemUp g8 \stemDown c8 ) r8 r4 r4
    \pageBreak | % 117
    r8 \stemUp c,8 ( \stemUp f8 \stemUp a8 \stemDown c8 ) r8 r4 r4 | % 118
    r8 \stemUp e,8 ( _\f \stemUp gis8 \stemUp b8 \stemDown e8 ) r8 r4 r4
    | % 119
    r8 \stemDown a,8 ( \stemDown c8 \stemDown e8 \stemDown a8 ) r8 r4 r4
    | \barNumberCheck #120
    \stemUp <e, g>4 ( _\mf \stemDown <bes' d>4 ) \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown <bes d>8 ( \stemDown <a c>8 \stemDown <bes d>8 }
    \stemDown <a c>4 \stemUp <g bes>4 ) | % 121
    \stemUp <f a>8 -. r16 \stemUp <e g>16 ( \stemUp <f a>8 ) -. r16
    \stemUp <g bes>16 ( \stemUp <f a>2. ) _\< \break | % 122
    \stemUp <f a>4 ( _\! _\markup{ \italic {più} } _ "" \stemUp <d f>4
    ) \stemUp <f a>4 ( \stemUp <g bes>4 \stemDown <a c>4 ) \pageBreak | % 123
    \stemUp <a c>8 -. r16 \stemUp <f a>16 ( \stemUp <g bes>8 ) -. r16
    \stemUp <d c'>16 ( \stemUp <g bes>2. ) _\> | % 124
    \stemUp <e g>4 ( _\! _\mf \stemDown <bes' d>4 ) \stemDown <bes d>4 (
    \stemDown <a c>4 \stemUp <g bes>4 ) | % 125
    \stemUp <f a>8 -. r16 \stemUp <e g>16 ( \stemUp <f a>8 ) -. r16
    \stemUp <g bes>16 ( \stemUp <f a>2. ) _\< | % 126
    \stemDown <c' e>4 ( \stemDown <b d>4 ) \stemDown <a c>2. ~ ~ _\! _\f
    | % 127
    \stemDown <a c>8 r16 \stemDown <a c>16 ( \stemDown <g b>8 ) -. r16
    \stemDown <d' f>16 ( \stemDown <c e>4 ~ ~ \stemDown <c e>8 ) r8 r4
    \pageBreak | % 128
    \stemUp a,4 ( ^\markup{ \bold\small {a. 2} } _\mf \stemUp bes4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 ( _\< \stemUp b8 \stemUp c8 }
    \stemUp d4 \stemUp e4 ) | % 129
    \stemUp f4 ( _\! \stemUp d4 ) \stemUp e2. _\> | \barNumberCheck #130
    \stemUp c4 ( _\! \stemUp d4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 ( _\< \stemUp d8 \stemUp e8 }
    \stemUp f4 \stemUp g4 ) | % 131
    \stemUp a4 ( _\! \stemUp f4 ) \stemUp g2. | % 132
    \stemDown bes4 ( _\f \stemUp a4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 ( \stemUp a8 \stemUp g8 }
    \stemUp f4 \stemUp e4 ) \pageBreak | % 133
    \stemUp a8 -. r16 \stemUp bes16 ( \stemUp a8 ) -. r16 \stemUp gis16
    ( \stemUp a2. ) | % 134
    \stemUp a4 ( \stemUp g4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp f8 ( \stemUp g8 \stemUp f8 }
    \stemUp e4 ) \stemUp d4 ( _\< | % 135
    \stemDown d'8 ) _\! _\ff _\> \stemDown c8 -. \stemDown bes8 -.
    \stemDown a8 -. \stemUp g8 -. \stemUp ges8 -. \stemUp f8 -. \stemUp
    e8 -. \stemUp d8 -. \stemUp des8 -. | % 136
    \stemUp c2 ~ _\! _\mf \stemUp c8 \stemUp c8 ~ \stemUp c8 \stemUp c8
    ~ \stemUp c8 \stemUp c8 ~ | % 137
    \stemUp c2 ~ \stemUp c8 \stemUp c8 ~ \stemUp c8 \stemUp c8 ~ \stemUp
    c8 \stemUp c8 ~ \pageBreak | % 138
    \stemUp c2 ~ \stemUp c8 \stemUp c8 ~ \stemUp c8 \stemUp c8 ~ \stemUp
    c8 \stemUp c8 ~ | % 139
    \stemUp c2 _\< \stemUp e8 \stemUp e8 ~ \stemUp e8 \stemUp e8 ~
    \stemUp e8 \stemUp e8 | \barNumberCheck #140
    \stemUp es4 ( _\! _\f \stemUp c4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp d8 ( \stemUp c8 \stemUp d8 }
    \stemUp es4 \stemUp f4 ) | % 141
    \stemUp g4 ( \stemUp es4 ) \stemUp f2. _\> | % 142
    \stemUp es4 ( _\! _\mf _\< \stemDown f8 ) \stemDown f'8 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown <es g>8 ( \stemDown <d f>8 \stemDown <es g>8 }
    \stemDown <f as>4 \stemDown <fis a>4 ) \pageBreak | % 143
    \stemDown <g bes>4 ( _\! _\ff _\> \stemDown <es g>4 ) \stemUp f2.
    _\! _\f | % 144
    \stemUp f2 \stemUp ges2 \stemUp ges4 | % 145
    \stemDown <des f>4 \stemDown <bes f'>4 \stemDown <c ges'>2. | % 146
    \stemDown <c g'>2 \stemDown <d f>2 \stemDown <b f'>4 | % 147
    \stemDown <c e>4 \stemDown <a e'>4 \stemDown <b f'>2. \pageBreak | % 148
    \stemDown <c e>2 ~ ~ \stemDown <c e>2. | % 149
    \stemDown <c f>2 \stemDown <d f>8 r8 r4 r4 | \barNumberCheck #150
    R4*10 | % 152
    \stemDown <f c'>2 _\mf \stemDown <e bes'>2. -> | % 153
    \stemDown <d a'>2 \stemDown <c a'>2. -> \pageBreak | % 154
    \stemDown <bes f'>2 \stemDown <a f'>2. -> | % 155
    \stemDown <g e'>2 \stemUp <f c'>2. -> | % 156
    R4*25 | % 161
    \stemDown <f f'>2 ~ ~ _\p \stemDown <f f'>2. | % 162
    R4*5 \pageBreak | % 163
    \stemDown <f f'>2 ~ ~ _\p \stemDown <f f'>2. | % 164
    R4*10 | % 166
    \stemDown f'4. ( ^ "I." ^\markup{ \italic {solo} } _\f \stemDown f8
    ) -. \stemDown e2 ( _\> \stemDown d4 ) | % 167
    R4*20 \break | % 171
    \stemUp a,4. ( _\! _\mp ^ "(I.)" \stemUp a8 ) -. \stemUp g2 ( _\>
    \stemUp f4 ) | % 172
    R4*5 | % 173
    \stemUp a4. ( _\! \stemUp a8 ) -. \stemUp g2 ( -> \stemUp f4 ) | % 174
    R4*5 | % 175
    \stemUp a4. ( _\pp \stemUp a8 ) -. \stemUp g2 ( -> \stemUp f4 ) | % 176
    \stemUp a4. ( \stemUp a8 ) -. \stemUp g2 ( -> \stemUp f4 ) | % 177
    R4*5 \pageBreak | % 178
    \stemUp a2 ~ _\pp \stemUp a2 ~ \stemUp a8 r8 ^\fermata \bar "|."
    }

PartPThreeVoiceTwo =  \relative d'' {
    \repeat volta 2 {
        \clef "treble" \time 5/4 \key f \major \transposition a s4*25
        \pageBreak s4*25 \break s4*5 \pageBreak s4*25 }
    \pageBreak s4*5 \bar "||"
    s1*5 \break s4*5 \pageBreak s4*25 \break s4*25 \pageBreak s4*25
    \pageBreak s1*5 \pageBreak s4*5 \pageBreak s2*15 \pageBreak s2
    \stemDown d2 ( \stemDown es4 ) | % 49
    \stemDown f2 \stemDown es2 \stemDown c4 s4*15 \pageBreak s1*5
    \repeat volta 2 {
        s2*5 \pageBreak s2*15 }
    \pageBreak \repeat volta 2 {
        s2*15 \pageBreak s2*5 }
    s1*5 \pageBreak s2*15 \pageBreak s2*15 \pageBreak | % 89
    \stemDown bes2 ~ \stemDown bes8 r8 _\! r4 r4 s1*5 | % 94
    \stemDown d,4 s1 \pageBreak s2*15 \pageBreak s4*25 \break s4*25
    \pageBreak s4*25 \break s4*5 \pageBreak s4*25 \break s4*5 \pageBreak
    s4*25 \pageBreak s4*25 \pageBreak s4*25 \pageBreak s4*25 \pageBreak
    s2 \stemDown d'2 ( \stemDown es4 ) | % 144
    \stemDown f2 \stemDown es2 \stemDown c4 s4*15 \pageBreak s2*15
    \pageBreak s4*45 \pageBreak s1*10 \break s4*35 \pageBreak s4*5 \bar
    "|."
    }

PartPFourVoiceOne =  \relative d' {
    \repeat volta 2 {
        \clef "bass" \time 5/4 \key d \major | % 1
        r2 r4 \clef "tenor" \stemDown <d fis>4 ( _\mf \stemUp <fis, a>8
        ) r8 | % 2
        r2 r4 \stemDown <a e'>4 ( \stemUp <e a>8 ) r8 | % 3
        r2 r4 \stemDown <a d>4 ( \stemUp <cis, a'>8 ) r8 | % 4
        r2 r4 \stemDown <a' cis>4 ( \stemUp <cis, a'>8 ) r8 | % 5
        r2 r4 \stemDown <ais' fis'>4 ( \stemUp <fis ais>8 ) r8
        \pageBreak | % 6
        r2 r4 \stemDown <b d>4 ( \stemUp <fis b>8 ) r8 | % 7
        r2 r4 \stemDown <e' gis>4 ~ ~ \stemDown <e gis>8 r8 | % 8
        \stemDown <e g>8 _\f r8 r2 r2 | % 9
        R4*10 \break | % 11
        R4*5 \pageBreak | % 12
        \clef "bass" R4*5 | % 13
        \stemUp g,,2 ( _\mf ^ "I." \stemUp fis8 ) r8 r4 r4 | % 14
        \stemDown d'2 ~ \stemDown d2 ~ \stemDown d8 r8 | % 15
        \stemUp fis,2 ( \stemUp e8 ) r8 r4 r4 | % 16
        \stemUp cis'4 ( \stemUp a4 ~ \stemUp a8 ) r8 r4 r4 }
    \pageBreak \stemUp cis4 ( \stemUp a4 ~ \stemUp a8 ) r8 r4 r4 \bar
    "||"
    r8 \stemUp a8 ( _\mf ^\markup{ \bold\small {a. 2} } \stemUp cis8
    \stemUp e8 \stemDown a8 ) r8 r4 r4 | % 18
    r8 \stemUp a,8 ( \stemUp d8 \stemUp fis8 \stemDown a8 ) r8 r4 r4 | % 19
    r8 \stemUp a,8 ( \stemUp d8 \stemUp fis8 \stemDown a8 ) r8 r4 r4 |
    \barNumberCheck #20
    r8 \stemUp a,8 ( \stemUp cis8 \stemUp e8 \stemDown a8 ) r8 r4 r4
    \break | % 21
    r8 \stemUp a,8 ( \stemUp cis8 \stemUp e8 \stemDown a8 ) r8 r4 r4
    \pageBreak | % 22
    r8 \stemUp a,8 ( \stemUp d8 \stemUp fis8 \stemDown a8 ) r8 r4 r4 | % 23
    r8 \stemDown cis,8 ( _\f \stemDown eis8 \stemDown gis8 \stemDown cis8
    ) r8 r4 r4 | % 24
    r8 \stemDown fis,8 ( \stemDown a8 \stemDown cis8 \stemDown fis8 ) r8
    r4 r4 | % 25
    \stemDown <cis, e>4 ( _\mf \stemDown <g' b>4 ) \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown <g b>8 ( \stemDown <fis a>8 \stemDown <g b>8 }
    \stemDown <fis a>4 \stemDown <e g>4 ) | % 26
    \stemDown <d fis>8 -. r16 \stemDown <cis e>16 ( \stemDown <d fis>8 )
    -. r16 \stemDown <e g>16 ( \stemDown <d fis>2. ) _\< \break | % 27
    \stemDown <d fis>4 ( _\! _\markup{ \italic {più} } _ "" \stemUp <b
        d>4 ) \stemDown <d fis>4 ( \stemDown <e g>4 \stemDown <fis a>4 )
    | % 28
    \stemDown <fis a>8 -. r16 \stemDown <d fis>16 ( \stemDown <e g>8 )
    -. r16 \stemDown <fis a>16 ( \stemDown <e g>2. ) _\> | % 29
    \stemDown <cis e>4 ( _\! _\mf \stemDown <g' b>4 ) \stemDown <g b>4 (
    \stemDown <fis a>4 \stemDown <e g>4 ) | \barNumberCheck #30
    \stemDown <d fis>8 -. r16 \stemDown <cis e>16 ( \stemDown <d fis>8 )
    -. r16 \stemDown <e g>16 ( \stemDown <d fis>2. ) _\< | % 31
    \stemDown <a' cis>4 ( \stemDown <gis b>4 ) \stemDown <fis a>2. ~ ~
    _\! _\f \pageBreak | % 32
    \stemDown <fis a>8 r16 \stemDown <fis a>16 ( \stemDown <e gis>8 ) -.
    r16 \stemDown <b' d>16 ( \stemDown <a cis>4 ~ ~ \stemDown <a cis>8 )
    r8 r4 | % 33
    \stemDown fis4 ( ^\markup{ \bold\small {a. 2} } _\mf \stemDown g4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 ( _\< \stemDown gis8 \stemDown a8 }
    \stemDown b4 \stemDown cis4 ) | % 34
    \stemDown d4 ( _\! \stemDown b4 ) \stemDown cis2. _\> | % 35
    \clef "tenor" \stemDown a4 ( _\! \stemDown b4 ) \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown cis8 ( _\< \stemDown b8 \stemDown cis8 }
    \stemDown d4 \stemDown e4 ) | % 36
    \stemDown fis4 ( _\! \stemDown d4 ) \stemDown e2. \pageBreak | % 37
    \stemDown g4 ( _\f \stemDown fis4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( \stemDown fis8 \stemDown e8 }
    \stemDown d4 \stemDown cis4 ) | % 38
    \stemDown fis8 -. r16 \stemDown g16 ( \stemDown fis8 ) -. r16
    \stemDown eis16 ( \stemDown fis2. ) | % 39
    \stemDown fis4 ( \stemDown e4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 ( \stemDown e8 \stemDown d8 }
    \stemDown cis4 ) \stemDown b4 ( _\< | \barNumberCheck #40
    \stemDown b'8 ) _\! _\ff _\> \stemDown a8 -. \stemDown g8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown es8 -. \stemDown d8 -.
    \stemDown cis8 -. \stemDown b8 -. \stemDown bes8 -. \pageBreak | % 41
    \stemDown a2 ~ _\! _\mf \stemDown a8 \stemDown a8 ~ \stemDown a8
    \stemDown a8 ~ \stemDown a8 \stemDown a8 ~ \pageBreak | % 42
    \stemDown a2 ~ \stemDown a8 \stemDown a8 ~ \stemDown a8 \stemDown a8
    ~ \stemDown a8 \stemDown a8 ~ | % 43
    \stemDown a2 ~ \stemDown a8 \stemDown a8 ~ \stemDown a8 \stemDown a8
    ~ \stemDown a8 \stemDown a8 ~ | % 44
    \stemDown a2 _\< \stemDown cis8 \stemDown cis8 ~ \stemDown cis8
    \stemDown cis8 ~ \stemDown cis8 \stemDown cis8 | % 45
    \stemDown c4 ( _\! _\f \stemDown a4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 ( \stemDown a8 \stemDown b8 }
    \stemDown c4 \stemDown d4 ) | % 46
    \stemDown e4 ( \stemDown c4 ) \stemDown d2. _\> | % 47
    \stemDown c4 ( _\! _\mf _\< \stemDown d4 ) \stemDown <c e>4 (
    \stemDown <d f>4 \stemDown <dis fis>4 ) \pageBreak | % 48
    \stemDown <e g>4 ( _\! _\ff _\> \stemDown <c e>4 ) \stemUp d2. _\!
    _\f | % 49
    \stemUp d8 r8 \clef "bass" \stemUp f,,4 ~ ^\markup{ \bold\small {a.
            2} } \stemUp f2. ~ | \barNumberCheck #50
    \stemUp f4 \stemUp f4 ~ \stemUp f2. | % 51
    \stemUp e4 \stemUp e4 ~ \stemUp e2. ~ | % 52
    \stemUp e4 \stemUp e4 ~ \stemUp e2. \pageBreak | % 53
    \stemUp <es es'>4 ~ ~ \stemUp <es es'>8 r8 r2 r4 | % 54
    \stemUp <d d'>8 r8 \stemUp <fis fis'>8 r8 \stemUp <g g'>8 r8 r4 r4 | % 55
    R4*5 | % 56
    r2 r4 \stemDown d'4 -- _\p ^\markup{ \bold\small {a. 2} } \stemDown
    d4 -- \repeat volta 2 {
        | % 57
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- | % 58
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- \pageBreak | % 59
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- | \barNumberCheck #60
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- | % 61
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- | % 62
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- | % 63
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- | % 64
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- }
    \pageBreak \repeat volta 2 {
        | % 65
        R4*25 | \barNumberCheck #70
        \stemDown g4. ( ^\markup{ \bold\small {a. 2} } _\p _\< \stemDown
        a8 ) \stemDown bes2 ( \stemDown g4 ) \pageBreak | % 71
        \stemDown gis2 ~ _\! _\mf \stemDown gis2. _\< | % 72
        \clef "tenor" \stemDown d'4. ( _\! _\f _\< \stemDown e8 )
        \stemDown fis2 ( _\! _\> \stemDown d4 ) }
    | % 73
    \clef "bass" \stemDown d,4 -- _\! _\p \stemDown d4 -- \stemDown d4
    -- \stemDown d4 -- \stemDown d4 -- | % 74
    \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
    \stemDown d4 -- | % 75
    \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
    \stemDown d4 -- | % 76
    \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
    \stemDown d4 -- \pageBreak | % 77
    \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
    \stemDown d4 -- | % 78
    \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
    \stemDown d4 -- | % 79
    \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
    \stemDown d4 -- | \barNumberCheck #80
    \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
    \stemDown d4 -- | % 81
    R4*5 | % 82
    \stemDown gis4 ( _\p _\< \stemDown ais4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 \stemDown ais8 \stemDown b8 }
    \stemDown cis4 \stemDown d4 \pageBreak | % 83
    \stemDown e8 ) _\! _\mf r8 r4 r2 r4 | % 84
    \stemDown b4 ( _\p _\< \stemDown cis4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown cis8 \stemDown d8 }
    \stemDown e4 \stemDown fis4 ) | % 85
    R4*5 | % 86
    \stemDown gis,4 ( _\! _\p _\< \stemDown ais4 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown b8 \stemDown ais8 \stemDown b8 }
    \stemDown cis4 \stemDown d4 | % 87
    \stemDown e8 ) _\! _\mf r8 r4 r2 r4 | % 88
    \stemDown b4 ( _\p _\< \stemDown cis4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown cis8 \stemDown d8 }
    \stemDown e4 \stemDown fis4 \pageBreak | % 89
    \stemDown g2 ) ~ _\! _\mf _\> \stemDown g8 r8 _\! r4 r4 |
    \barNumberCheck #90
    \stemDown b,4 ( _\p _\< \stemDown cis4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown cis8 \stemDown d8 }
    \stemDown e4 \stemDown eis4 | % 91
    \stemDown fis8 ) _\! _\mf r8 r4 r2 r4 | % 92
    \stemDown b,4 ( _\p _\< \stemDown cis4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown cis8 \stemDown d8 }
    \stemDown e4 \stemDown fis4 ) | % 93
    \stemDown g2 ~ _\! _\mf _\> \stemDown g8 _\! r8 r4 r4 | % 94
    \stemUp b,,4 ( _\p _\< \stemUp cis4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp d8 \stemUp cis8 \stemUp d8 }
    \stemDown e4 \stemDown eis4 \pageBreak | % 95
    \stemDown fis8 ) _\! _\mf r8 r4 r2 r4 | % 96
    r2 r4 \clef "tenor" \stemDown <d' fis>4 ( _\mf \stemUp <fis, a>8 ) r8
    | % 97
    r2 r4 \stemDown <a e'>4 ( \stemUp <e a>8 ) r8 | % 98
    r2 r4 \stemDown <a d>4 ( \stemUp <cis, a'>8 ) r8 | % 99
    r2 r4 \stemDown <a' cis>4 ( \stemUp <cis, a'>8 ) r8 |
    \barNumberCheck #100
    r2 r4 \stemDown <ais' fis'>4 ( \stemUp <fis ais>8 ) r8 \pageBreak | % 101
    r2 r4 \stemDown <b d>4 ( \stemUp <fis b>8 ) r8 | % 102
    r2 r4 \stemDown <e' gis>4 ~ ~ \stemDown <e gis>8 r8 | % 103
    \stemDown <e g>8 _\f r8 r4 r2 r4 | % 104
    R4*10 \break | % 106
    \clef "bass" R4*10 | % 108
    \stemUp g,,2 ( _\mf ^ "I." \stemUp fis8 ) r8 r4 r4 | % 109
    \stemDown d'2 ~ \stemDown d2 ~ \stemDown d8 r8 | \barNumberCheck
    #110
    \stemUp fis,2 ( \stemUp e8 ) r8 r4 r4 \pageBreak | % 111
    \stemUp cis'4 ( \stemUp a4 ~ \stemUp a8 ) r8 r4 r4 | % 112
    r8 \stemUp a8 ( _\mf ^\markup{ \bold\small {a. 2} } \stemUp cis8
    \stemUp e8 \stemDown a8 ) r8 r4 r4 | % 113
    r8 \stemUp a,8 ( \stemUp d8 \stemUp fis8 \stemDown a8 ) r8 r4 r4 | % 114
    r8 \stemUp a,8 ( \stemUp d8 \stemUp fis8 \stemDown a8 ) r8 r4 r4 | % 115
    r8 \stemUp a,8 ( \stemUp cis8 \stemUp e8 \stemDown a8 ) r8 r4 r4
    \break | % 116
    r8 \stemUp a,8 ( \stemUp cis8 \stemUp e8 \stemDown a8 ) r8 r4 r4
    \pageBreak | % 117
    r8 \stemUp a,8 ( \stemUp d8 \stemUp fis8 \stemDown a8 ) r8 r4 r4 | % 118
    r8 \stemDown cis,8 ( _\f \stemDown eis8 \stemDown gis8 \stemDown cis8
    ) r8 r4 r4 | % 119
    r8 \stemDown fis,8 ( \stemDown a8 \stemDown cis8 \stemDown fis8 ) r8
    r4 r4 | \barNumberCheck #120
    \stemDown <cis, e>4 ( _\mf \stemDown <g' b>4 ) \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown <g b>8 ( \stemDown <fis a>8 \stemDown <g b>8 }
    \stemDown <fis a>4 \stemDown <e g>4 ) | % 121
    \stemDown <d fis>8 -. r16 \stemDown <cis e>16 ( \stemDown <d fis>8 )
    -. r16 \stemDown <e g>16 ( \stemDown <d fis>2. ) _\< \break | % 122
    \stemDown <d fis>4 ( _\! _\markup{ \italic {più} } _ "" \stemUp <b
        d>4 ) \stemDown <d fis>4 ( \stemDown <e g>4 \stemDown <fis a>4 )
    \pageBreak | % 123
    \stemDown <fis a>8 -. r16 \stemDown <d fis>16 ( \stemDown <e g>8 )
    -. r16 \stemDown <fis a>16 ( \stemDown <e g>2. ) _\> | % 124
    \stemDown <cis e>4 ( _\! _\mf \stemDown <g' b>4 ) \stemDown <g b>4 (
    \stemDown <fis a>4 \stemDown <e g>4 ) | % 125
    \stemDown <d fis>8 -. r16 \stemDown <cis e>16 ( \stemDown <d fis>8 )
    -. r16 \stemDown <e g>16 ( \stemDown <d fis>2. ) _\< | % 126
    \stemDown <a' cis>4 ( \stemDown <gis b>4 ) \stemDown <fis a>2. ~ ~
    _\! _\f | % 127
    \stemDown <fis a>8 r16 \stemDown <fis a>16 ( \stemDown <e gis>8 ) -.
    r16 \stemDown <b' d>16 ( \stemDown <a cis>4 ~ ~ \stemDown <a cis>8 )
    r8 r4 \pageBreak | % 128
    \stemDown fis4 ( ^\markup{ \bold\small {a. 2} } _\mf \stemDown g4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 ( _\< \stemDown gis8 \stemDown a8 }
    \stemDown b4 \stemDown cis4 ) | % 129
    \stemDown d4 ( _\! \stemDown b4 ) \stemDown cis2. _\> |
    \barNumberCheck #130
    \clef "tenor" \stemDown a4 ( _\! \stemDown b4 ) \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown cis8 ( _\< \stemDown b8 \stemDown cis8 }
    \stemDown d4 \stemDown e4 ) | % 131
    \stemDown fis4 ( _\! \stemDown d4 ) \stemDown e2. | % 132
    \stemDown g4 ( _\f \stemDown fis4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( \stemDown fis8 \stemDown e8 }
    \stemDown d4 \stemDown cis4 ) \pageBreak | % 133
    \stemDown fis8 -. r16 \stemDown g16 ( \stemDown fis8 ) -. r16
    \stemDown eis16 ( \stemDown fis2. ) | % 134
    \stemDown fis4 ( \stemDown e4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 ( \stemDown e8 \stemDown d8 }
    \stemDown cis4 ) \stemDown b4 ( _\< | % 135
    \stemDown b'8 ) _\! _\ff _\> \stemDown a8 -. \stemDown g8 -.
    \stemDown fis8 -. \stemDown e8 -. \stemDown es8 -. \stemDown d8 -.
    \stemDown cis8 -. \stemDown b8 -. \stemDown bes8 -. | % 136
    \stemDown a2 ~ _\! _\mf \stemDown a8 \stemDown a8 ~ \stemDown a8
    \stemDown a8 ~ \stemDown a8 \stemDown a8 ~ | % 137
    \stemDown a2 ~ \stemDown a8 \stemDown a8 ~ \stemDown a8 \stemDown a8
    ~ \stemDown a8 \stemDown a8 ~ \pageBreak | % 138
    \stemDown a2 ~ \stemDown a8 \stemDown a8 ~ \stemDown a8 \stemDown a8
    ~ \stemDown a8 \stemDown a8 ~ | % 139
    \stemDown a2 _\< \stemDown cis8 \stemDown cis8 ~ \stemDown cis8
    \stemDown cis8 ~ \stemDown cis8 \stemDown cis8 | \barNumberCheck
    #140
    \stemDown c4 ( _\! _\f \stemDown a4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 ( \stemDown a8 \stemDown b8 }
    \stemDown c4 \stemDown d4 ) | % 141
    \stemDown e4 ( \stemDown c4 ) \stemDown d2. _\> | % 142
    \stemDown c4 ( _\! _\mf _\< \stemDown d4 ) \stemDown <c e>4 (
    \stemDown <d f>4 \stemDown <dis fis>4 ) \pageBreak | % 143
    \stemDown <e g>4 ( _\! _\ff _\> \stemDown <c e>4 ) \stemUp d2. _\!
    _\f | % 144
    \stemUp d8 r8 \clef "bass" \stemUp f,,4 ~ ^\markup{ \bold\small {a.
            2} } \stemUp f2. ~ | % 145
    \stemUp f4 \stemUp f4 ~ \stemUp f2. | % 146
    \stemUp e4 \stemUp e4 ~ \stemUp e2. ~ | % 147
    \stemUp e4 \stemUp e4 ~ \stemUp e2. \pageBreak | % 148
    \stemUp <es es'>4 ~ ~ \stemUp <es es'>8 r8 r2 r4 | % 149
    \stemUp <d d'>8 r8 \stemUp <fis fis'>8 r8 \stemUp <g g'>8 r8 r4 r4 |
    \barNumberCheck #150
    R4*10 | % 152
    \clef "tenor" \stemDown <fis'' a>2 _\mf \stemDown <e g>2. -> | % 153
    \stemDown <d fis>2 \stemDown <cis fis>2. -> \pageBreak | % 154
    \stemDown <b d>2 \stemDown <a d>2. -> | % 155
    \stemDown <a cis>2 \stemUp <fis a>2. -> | % 156
    R4*35 \pageBreak | % 163
    R4*20 | % 167
    \stemDown fis'4. ( _\f ^\markup{ \bold\small {a. 2} } \stemDown fis8
    ) -. \stemDown e2 ( _\> \stemDown d4 ) | % 168
    R4*5 | % 169
    \stemDown b'4. ( _\! _\f ^ "I." \stemDown b8 ) -. \stemDown a2 ( _\>
    \stemDown g4 | \barNumberCheck #170
    \stemDown f8 ) _\! r8 r4 r2 r4 \break | % 171
    \clef "bass" R4*35 \pageBreak | % 178
    \stemUp <d,, a'>2 ~ ~ _\pp \stemUp <d a'>2 ~ ~ \stemUp <d a'>8 r8
    ^\fermata \bar "|."
    }

PartPFourVoiceTwo =  \relative b {
    \repeat volta 2 {
        \clef "bass" \time 5/4 \key d \major s2. \clef "tenor" s2*11
        \pageBreak s4*25 \break s4*5 \pageBreak | % 12
        \clef "bass" s4*25 }
    \pageBreak s4*5 \bar "||"
    s1*5 \break s4*5 \pageBreak s4*25 \break s4*25 \pageBreak s4*15 | % 35
    \clef "tenor" s2*5 \pageBreak s1*5 \pageBreak s4*5 \pageBreak s2*15
    \pageBreak s2 \stemDown b2 ( \stemDown c4 ) s4 \clef "bass" | % 49
    \stemDown d8 s8*37 \pageBreak s1*5 \repeat volta 2 {
        s2*5 \pageBreak s2*15 }
    \pageBreak \repeat volta 2 {
        s2*15 \pageBreak s4*5 | % 72
        \clef "tenor" s4*5 }
    | % 73
    \clef "bass" s1*5 \pageBreak s2*15 \pageBreak s2*15 \pageBreak s2*15
    \pageBreak s1*2 \clef "tenor" s2*11 \pageBreak s4*25 \break | % 106
    \clef "bass" s4*25 \pageBreak s4*25 \break s4*5 \pageBreak s4*25
    \break s4*5 \pageBreak s4*25 \pageBreak s2*5 | \barNumberCheck #130
    \clef "tenor" s4*15 \pageBreak s4*25 \pageBreak s4*25 \pageBreak s2
    \stemDown b2 ( \stemDown c4 ) s4 \clef "bass" | % 144
    \stemDown d8 s8*37 \pageBreak s1*5 | % 152
    \clef "tenor" s2*5 \pageBreak s4*45 \pageBreak s1*10 \break | % 171
    \clef "bass" s4*35 \pageBreak s4*5 \bar "|."
    }

PartPFiveVoiceOne =  \relative a {
    \repeat volta 2 {
        \clef "treble" \time 5/4 \key c \major \transposition f | % 1
        r4 \stemUp <a e'>4 ( _\mf \stemUp <cis a'>8 ) r8 r2 | % 2
        r4 \stemUp <cis a'>8 r8 r4 r2 | % 3
        R4*10 | % 5
        r4 \stemUp fis4 ( \stemUp d'8 ) r8 r4 r4 \pageBreak | % 6
        r4 \stemUp fis,4 ( \stemUp a8 ) r8 r4 r4 | % 7
        r4 \stemDown <fis fis'>8 r8 r4 \stemUp <b, b'>4 ~ ~ \stemUp <b
            b'>8 r8 | % 8
        \stemUp <b gis'>8 _\f r8 r4 r4 \stemUp <d b'>2 ( _\mf | % 9
        \stemUp <cis a'>8 ) r8 r4 r2 r4 | \barNumberCheck #10
        R4*5 \break | % 11
        R4*5 \pageBreak | % 12
        R4*20 | % 16
        r2 \stemUp <gis gis'>8 _\mf r8 r4 r4 }
    \pageBreak r2 \stemUp <gis gis'>8 _\mf r8 r4 r4 \bar "||"
    r2 r4 \stemUp e''8 ( _\mf \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 ) | % 18
    r2 r4 \stemUp e8 ( \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 ) | % 19
    r2 r4 \stemUp e8 ( \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 ) |
    \barNumberCheck #20
    r2 r4 \stemUp e8 ( \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 ) \break | % 21
    r2 r4 \stemUp e8 ( \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 )
    \pageBreak | % 22
    r2 r4 \stemUp e8 ( \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 ) | % 23
    r2 r4 \stemUp cis8 ( _\markup{ \italic {più} } _ "" \stemUp cis,8 )
    \stemUp cis8 ( \stemUp cis'8 ) | % 24
    r2 \stemUp <cis, cis'>8 r8 r4 r4 | % 25
    R4*10 \break | % 27
    R4*25 \pageBreak | % 32
    R4*5 | % 33
    \stemUp <a e'>8 _\mp r8 r4 \stemUp <cis a'>8 r8 r4 r4 | % 34
    r2 \stemUp b'2 _\mp \stemUp e,8 _\p r8 | % 35
    \stemUp a8 _\mp r8 r4 \stemUp cis8 r8 r4 \stemUp e8 r8 | % 36
    \stemUp e8 _\< r8 \stemUp e8 r8 \stemUp gis,4 ~ _\! _\mf _\> \stemUp
    gis8 r8 _\! r4 \pageBreak | % 37
    \stemUp <fis b>8 _\mp r8 r4 \stemDown <fis fis'>8 r8 \stemDown <fis
        fis'>8 r8 \stemUp <d d'>8 r8 | % 38
    \stemUp <cis fis'>8 r8 \stemUp <cis fis'>8 r8 \stemUp <cis fis>4 ~ ~
    _\mf _\> \stemUp <cis fis>8 r8 _\! r4 | % 39
    \stemUp <cis cis'>2 ~ ~ _\p _\< \stemUp <cis cis'>8 r8 _\! \stemUp
    <cis cis'>4 _\mp \stemUp <a a'>4 | \barNumberCheck #40
    \stemUp <gis gis'>2 _\< \stemUp <d' d'>8 _\! _\mf r8 r4 r4
    \pageBreak | % 41
    r2 r4 \stemUp cis'4 -- ^\mf \stemUp b4 -- \pageBreak | % 42
    \stemUp a2 \stemUp b2. | % 43
    \stemUp a2 ( \stemUp cis8 ) r8 \stemUp fis,4 -- \stemUp gis4 -- | % 44
    \stemUp a2 ( \stemUp e8 ) r8 r4 r4 | % 45
    \stemUp <b b'>4 _\f \stemUp <c c'>4 \stemUp <d d'>4 \stemUp <e e'>4
    \stemDown <fis fis'>4 | % 46
    \stemDown <g g'>4 ( \stemUp <e e'>4 ) \stemDown <fis fis'>2. _\> | % 47
    \stemUp <e e'>4 _\! _\mf _\< \stemDown <fis fis'>4 \stemUp <g b>4
    \stemDown <a c>4 \stemDown <bes cis>4 \pageBreak | % 48
    \stemDown <b d>4 ( _\! _\ff _\> \stemUp <g b>4 ) \stemUp a2. _\! _\f
    | % 49
    \stemUp a2 \stemUp bes2 \stemUp bes4 | \barNumberCheck #50
    \stemUp <f a>4 \stemUp <d a'>4 \stemUp <e bes'>2. | % 51
    \stemUp <e b'>2 \stemUp <fis a>2 \stemUp <dis a'>4 | % 52
    \stemUp <e gis>4 \stemUp <cis gis'>4 \stemUp <dis a'>2. \pageBreak | % 53
    \stemUp <e gis>2 ~ ~ \stemUp <e gis>2. | % 54
    \stemUp <e a>2. \stemUp <fis a>8 r8 r4 | % 55
    \stemUp <a, e'>8 _\mf r8 r4 r2 r4 | % 56
    R4*5 \repeat volta 2 {
        | % 57
        R4*5 | % 58
        \stemUp <cis cis'>2 _\p _\< \stemUp <d d'>2. ( _\! _\>
        \pageBreak | % 59
        \stemUp <cis cis'>8 ) r8 _\! r4 \stemUp <b b'>2. ( _\mp _\> |
        \barNumberCheck #60
        \stemUp <cis cis'>8 ) r8 _\! r4 r2 r4 | % 61
        R4*5 | % 62
        \stemUp <cis cis'>2 _\p _\< \stemUp <d d'>2. ( _\! _\> | % 63
        \stemUp <cis cis'>8 ) r8 _\! r4 \stemUp <b b'>2. ( _\mp _\> | % 64
        \stemUp <cis cis'>8 ) r8 _\! r4 \stemUp <eis eis'>2 ( _\sf _\>
        \stemDown <fis fis'>8 ) r8 _\! }
    \pageBreak \repeat volta 2 {
        | % 65
        \stemDown <fis fis'>2 _\p \stemDown <g g'>2 ( -> \stemDown <fis
            fis'>4 ) | % 66
        \stemUp <b, b'>2 \stemUp <cis cis'>2 ( -> \stemUp <d d'>4 ) | % 67
        \stemUp <b b'>2 \stemDown <f' f'>2 ( -> \stemUp <e e'>4 ) | % 68
        \stemUp <a, a'>2 \stemUp <b b'>2 ( -> \stemUp <cis cis'>4 ) | % 69
        \stemUp <c c'>2 ~ ~ _ "" _\markup{ \italic {cresc.} } \stemUp
        <c c'>2. | \barNumberCheck #70
        \stemDown <f f'>2 ~ ~ \stemDown <f f'>2. \pageBreak | % 71
        \stemDown <fis fis'>2 ~ ~ \stemDown <fis fis'>2. | % 72
        \stemDown <a cis>2 ~ ~ _\mf _\> \stemDown <a cis>2. }
    | % 73
    R4*5 | % 74
    \stemUp <cis, cis'>2 _\! _\p _\< \stemUp <d d'>2. ( _\! _\> | % 75
    \stemUp <cis cis'>8 ) r8 _\! r4 \stemUp <b b'>2. ( _\mp _\> | % 76
    \stemUp <cis cis'>8 ) r8 _\! r4 r2 r4 \pageBreak | % 77
    R4*5 | % 78
    \stemUp <cis cis'>2 _\p _\< \stemUp <d d'>2. ( _\! _\> | % 79
    \stemUp <cis cis'>8 ) _\! r8 r4 \stemUp <b b'>2. ( _\mp _\> |
    \barNumberCheck #80
    \stemUp <cis cis'>8 ) _\! r8 r4 \stemUp <eis eis'>2 ( _\sf _\>
    \stemDown <fis fis'>8 ) r8 | % 81
    R4*5 | % 82
    \stemDown <fis fis'>2 ~ ~ _\! _\p _\< _\! _\p \stemDown <fis fis'>8
    r8 r4 r4 \pageBreak | % 83
    R4*5 | % 84
    \stemDown <fis fis'>2 ~ ~ _\p _\< _\! _\p \stemDown <fis fis'>8 r8 r4
    r4 | % 85
    R4*5 | % 86
    \stemDown <fis fis'>2 ~ ~ _\p _\< _\! _\p \stemDown <fis fis'>8 r8 r4
    r4 | % 87
    R4*5 | % 88
    \stemDown <fis fis'>2 ~ ~ _\p _\< _\! _\p \stemDown <fis fis'>8 r8 r4
    r4 \pageBreak | % 89
    \stemUp <d b'>2 ~ ~ _\mp _\> \stemUp <d b'>8 r8 _\! r4 r4 |
    \barNumberCheck #90
    \stemDown <fis fis'>2 ~ ~ _\mp _\> \stemDown <fis fis'>8 r8 _\! r4 r4
    | % 91
    \stemDown <fis fis'>2 ~ ~ _\mp _\> \stemDown <fis fis'>8 r8 _\! r4 r4
    | % 92
    \stemDown <fis fis'>2 ~ ~ _\mp _\> \stemDown <fis fis'>8 r8 _\! r4 r4
    | % 93
    \stemUp <d b'>2 ~ ~ _\mp _\> \stemUp <d b'>8 r8 _\! r4 r4 | % 94
    \stemDown <fis fis'>2 ~ ~ _\mp _\> \stemDown <fis fis'>8 r8 _\! r4 r4
    \pageBreak | % 95
    \stemUp <e e'>2 ~ ~ _\mp _\> \stemUp <e e'>8 _\! r8 r4 r4 | % 96
    r4 \stemUp <a, e'>4 ( _\mf \stemUp <cis a'>8 ) r8 r2 | % 97
    r4 \stemUp <cis a'>8 r8 r4 r2 | % 98
    R4*10 | \barNumberCheck #100
    r4 \stemUp fis4 ( \stemUp d'8 ) r8 r4 r4 \pageBreak | % 101
    r4 \stemUp fis,4 ( \stemUp a8 ) r8 r4 r4 | % 102
    r4 \stemDown <fis fis'>8 r8 r4 \stemUp <b, a'>4 ~ ~ \stemUp <b a'>8
    r8 | % 103
    \stemUp <b gis'>8 _\f r8 r4 r4 \stemUp <d b'>2 ( _\mf | % 104
    \stemUp <cis a'>8 ) r8 r4 r2 r4 | % 105
    R4*5 \break | % 106
    R4*25 \pageBreak | % 111
    r2 \stemUp <gis gis'>8 _\mf r8 r4 r4 | % 112
    r2 r4 \stemUp e''8 ( _\mf \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 ) | % 113
    r2 r4 \stemUp e8 ( \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 ) | % 114
    r2 r4 \stemUp e8 ( \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 ) | % 115
    r2 r4 \stemUp e8 ( \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 ) \break | % 116
    r2 r4 \stemUp e8 ( \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 )
    \pageBreak | % 117
    r2 r4 \stemUp e8 ( \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 ) | % 118
    r2 r4 \stemUp cis8 ( _\markup{ \italic {più} } _ "" \stemUp cis,8 )
    \stemUp cis8 ( \stemUp cis'8 ) | % 119
    r2 \stemUp <cis, cis'>8 r8 r4 r4 | \barNumberCheck #120
    R4*10 \break | % 122
    R4*5 \pageBreak | % 123
    R4*25 \pageBreak | % 128
    \stemUp <a e'>8 _\mp r8 r4 \stemUp <cis a'>8 r8 r4 r4 | % 129
    r2 \stemUp b'2 _\mp \stemUp e,8 _\p r8 | \barNumberCheck #130
    \stemUp a8 _\mp r8 r4 \stemUp cis8 r8 r4 \stemUp e8 r8 | % 131
    \stemUp e8 _\< r8 \stemUp e8 r8 \stemUp gis,4 ~ _\! _\mf _\> \stemUp
    gis8 r8 _\! r4 | % 132
    \stemUp <fis b>8 _\mp r8 r4 \stemDown <fis fis'>8 r8 \stemDown <fis
        fis'>8 r8 \stemUp <d d'>8 r8 \pageBreak | % 133
    \stemUp <cis fis'>8 r8 \stemUp <cis fis'>8 r8 \stemUp <cis fis>4 ~ ~
    _\mf _\> \stemUp <cis fis>8 r8 _\! r4 | % 134
    \stemUp <cis cis'>2 ~ ~ _\p _\< \stemUp <cis cis'>8 r8 _\! \stemUp
    <cis cis'>4 _\mp \stemUp <a a'>4 | % 135
    \stemUp <gis gis'>2 _\< \stemUp <d' d'>8 _\! _\mf r8 r4 r4 | % 136
    r2 r4 \stemUp cis'4 -- ^\mf \stemUp b4 -- | % 137
    \stemUp a2 \stemUp b2. \pageBreak | % 138
    \stemUp a2 ( \stemUp cis8 ) r8 \stemUp fis,4 -- \stemUp gis4 -- | % 139
    \stemUp a2 ( \stemUp e8 ) r8 r4 r4 | \barNumberCheck #140
    \stemUp <b b'>4 _\f \stemUp <c c'>4 \stemUp <d d'>4 \stemUp <e e'>4
    \stemDown <fis fis'>4 | % 141
    \stemDown <g g'>4 ( \stemUp <e e'>4 ) \stemDown <fis fis'>2. _\> | % 142
    \stemUp <e e'>4 _\! _\mf _\< \stemDown <fis fis'>4 \stemUp <g b>4
    \stemDown <a c>4 \stemDown <bes cis>4 \pageBreak | % 143
    \stemDown <b d>4 ( _\! _\ff _\> \stemUp <g b>4 ) \stemUp a2. _\! _\f
    | % 144
    \stemUp a2 \stemUp bes2 \stemUp bes4 | % 145
    \stemUp <f a>4 \stemUp <d a'>4 \stemUp <e bes'>2. | % 146
    \stemUp <e b'>2 \stemUp <fis a>2 \stemUp <dis a'>4 | % 147
    \stemUp <e gis>4 \stemUp <cis gis'>4 \stemUp <dis a'>2. \pageBreak | % 148
    \stemUp <e gis>2 ~ ~ \stemUp <e gis>2. | % 149
    \stemUp <e a>2. \stemUp <fis a>8 r8 r4 | \barNumberCheck #150
    \stemUp <a, e'>8 _\mf r8 r4 r2 r4 | % 151
    R4*15 \pageBreak | % 154
    R4*10 | % 156
    \stemUp <e' e'>2 _\p \stemUp <d d'>2. -> | % 157
    \stemUp cis'2 \stemUp cis2. -> | % 158
    R4*10 | \barNumberCheck #160
    \stemUp <c, c'>2 ~ ~ _\sf _\> \stemUp <c c'>2. _\! _\p | % 161
    \stemUp <cis cis'>2 ~ ~ \stemUp <cis cis'>2. | % 162
    \stemUp <c c'>2 ~ ~ _\sf _\> \stemUp <c c'>2. _\! _\p \pageBreak | % 163
    \stemUp <cis cis'>2 ~ ~ \stemUp <cis cis'>2. | % 164
    R4*30 | \barNumberCheck #170
    \stemUp a'4. ( ^ "I." _\mf \stemUp a8 ) -. \stemUp gis2 ( _\>
    \stemUp fis4 \break | % 171
    \stemUp e8 ) _\! r8 r4 r2 r4 | % 172
    R4*30 \pageBreak | % 178
    \stemUp <a, e'>2 ~ ~ _\pp \stemUp <a e'>2 ~ ~ \stemUp <a e'>8 r8
    ^\fermata \bar "|."
    }

PartPFiveVoiceTwo =  \relative cis' {
    \repeat volta 2 {
        \clef "treble" \time 5/4 \key c \major \transposition f s4*15 | % 4
        r4 \stemDown cis8 r8 r4 r2 s4 \stemDown d4 ( \stemDown fis8 ) s8
        \stemDown cis4 ~ \stemDown cis8 r8 \pageBreak s4 \stemDown a4 (
        \stemDown fis'8 ) s8 \stemDown cis4 ~ \stemDown cis8 r8 s1*5
        \break s4*5 \pageBreak s4*25 }
    \pageBreak s4*5 \bar "||"
    s2. \stemDown e8 ( \stemDown e'8 ) \stemDown e8 ( \stemDown e,8 )
    s2. \stemDown e8 ( \stemDown e'8 ) \stemDown e8 ( \stemDown e,8 )
    s2. \stemDown e8 ( \stemDown e'8 ) \stemDown e8 ( \stemDown e,8 )
    s2. \stemDown e8 ( \stemDown e'8 ) \stemDown e8 ( \stemDown e,8 )
    \break s2. \stemDown e8 ( \stemDown e'8 ) \stemDown e8 ( \stemDown
    e,8 ) \pageBreak s2. \stemDown e8 ( \stemDown e'8 ) \stemDown e8 (
    \stemDown e,8 ) s2. \stemDown cis8 ( \stemDown cis'8 ) \stemDown cis8
    ( \stemDown cis,8 ) s4*15 \break s4*25 \pageBreak s2*5 | % 34
    \stemDown e8 r8 \stemDown a8 r8 \stemDown e2 \stemDown e,8 s8 | % 35
    \stemDown cis'8 s4. \stemDown cis8 s8 \stemDown cis8 r8 \stemDown e8
    s8 | % 36
    \stemDown e8 s8 \stemDown e8 s8 \stemDown e4 ~ \stemDown e8 s4.
    \pageBreak s1*5 \pageBreak | % 41
    R4*5 \pageBreak | % 42
    R4*15 s4*15 \pageBreak s2 \stemDown fis2 ( \stemDown g4 ) | % 49
    \stemDown a2 \stemDown g2 \stemDown e4 s4*15 \pageBreak s1*5 \repeat
    volta 2 {
        s2*5 \pageBreak s2*15 }
    \pageBreak \repeat volta 2 {
        s2*15 \pageBreak s2*5 }
    s1*5 \pageBreak s1*5 | % 81
    \stemDown fis2 \stemDown fis2. _\! _\> s4*5 \pageBreak | % 83
    \stemDown d2 \stemDown d2. _\! _\> s4*5 | % 85
    \stemDown fis2 \stemDown fis2. _\! _\> s4*5 | % 87
    \stemDown d2 \stemDown d2. _\! _\> s4*5 \pageBreak s2*15 \pageBreak
    s1*5 | % 99
    r4 \stemDown cis8 r8 r4 r2 s4 \stemDown d4 ( \stemDown fis8 ) s8
    \stemDown cis4 ~ \stemDown cis8 r8 \pageBreak s4 \stemDown a4 (
    \stemDown fis'8 ) s8 \stemDown cis4 ~ \stemDown cis8 r8 s1*5 \break
    s4*25 \pageBreak s1*2 \stemDown e8 ( \stemDown e'8 ) \stemDown e8 (
    \stemDown e,8 ) s2. \stemDown e8 ( \stemDown e'8 ) \stemDown e8 (
    \stemDown e,8 ) s2. \stemDown e8 ( \stemDown e'8 ) \stemDown e8 (
    \stemDown e,8 ) s2. \stemDown e8 ( \stemDown e'8 ) \stemDown e8 (
    \stemDown e,8 ) \break s2. \stemDown e8 ( \stemDown e'8 ) \stemDown
    e8 ( \stemDown e,8 ) \pageBreak s2. \stemDown e8 ( \stemDown e'8 )
    \stemDown e8 ( \stemDown e,8 ) s2. \stemDown cis8 ( \stemDown cis'8
    ) \stemDown cis8 ( \stemDown cis,8 ) s4*15 \break s4*5 \pageBreak
    s4*25 \pageBreak s4*5 | % 129
    \stemDown e8 r8 \stemDown a8 r8 \stemDown e2 \stemDown e,8 s8 |
    \barNumberCheck #130
    \stemDown cis'8 s4. \stemDown cis8 s8 \stemDown cis8 r8 \stemDown e8
    s8 | % 131
    \stemDown e8 s8 \stemDown e8 s8 \stemDown e4 ~ \stemDown e8 s8*13
    \pageBreak s4*15 | % 136
    R4*10 \pageBreak | % 138
    R4*10 s4*15 \pageBreak s2 \stemDown fis2 ( \stemDown g4 ) | % 144
    \stemDown a2 \stemDown g2 \stemDown e4 s4*15 \pageBreak s2*15
    \pageBreak s4*15 | % 157
    R4*5 s4*25 \pageBreak s1*10 \break s4*35 \pageBreak s4*5 \bar "|."
    }

PartPSixVoiceOne =  \relative e' {
    \repeat volta 2 {
        \clef "treble" \time 5/4 \key c \major \transposition f | % 1
        R4*5 | % 2
        r4 \stemUp e8 ^\mf r8 r4 r2 | % 3
        r4 \stemUp <cis a'>4 ( _\mf \stemUp <e cis'>8 ) r8 r2 | % 4
        r4 \stemUp <a, e'>8 r8 r4 r2 | % 5
        R4*5 \pageBreak | % 6
        R4*5 | % 7
        r4 \stemUp cis'8 r8 r2 r4 | % 8
        R4*15 \break | % 11
        R4*5 \pageBreak | % 12
        R4*25 }
    \pageBreak | % 16
    \stemUp <b, b'>2 ~ ~ _\mf \stemUp <b b'>8 r8 r2 \bar "||"
    r2 r4 \stemUp e'8 ( _\mf \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 ) | % 18
    r2 r4 \stemUp e8 ( \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 ) | % 19
    r2 r4 \stemUp e8 ( \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 ) |
    \barNumberCheck #20
    r2 r4 \stemUp e8 ( \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 ) \break | % 21
    r2 r4 \stemUp e8 ( \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 )
    \pageBreak | % 22
    r2 r4 \stemUp e8 ( \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 ) | % 23
    r2 r4 \stemUp cis8 ( _\markup{ \italic {più} } _ "" \stemUp cis,8 )
    \stemUp cis8 ( \stemUp cis'8 ) | % 24
    r2 \stemUp <cis, e>8 r8 r4 r4 | % 25
    R4*10 \break | % 27
    R4*25 \pageBreak | % 32
    R4*5 | % 33
    \stemUp <a e'>8 _\mp r8 r4 \stemUp <cis a'>8 r8 r4 r4 | % 34
    r2 \stemUp b'2 _\mp \stemUp e,8 _\p r8 | % 35
    \stemUp cis8 _\mp r8 r4 r2 r4 | % 36
    r2 _\< \stemUp gis'4 ~ _\! _\mf _\> \stemUp gis8 r8 _\! r4
    \pageBreak | % 37
    \stemUp b8 _\mp r8 r4 r2 r4 | % 38
    \stemUp fis8 r8 \stemUp fis8 r8 \stemUp fis4 ~ _\mf _\> \stemUp fis8
    r8 _\! r4 | % 39
    R4*5 | \barNumberCheck #40
    R4*5 \pageBreak | % 41
    r2 _\p _\< _\< r4 \stemUp cis'4 -- ^\mf \stemUp b4 -- \pageBreak | % 42
    \stemUp a2 \stemUp b2. | % 43
    \stemUp a2 ( \stemUp cis8 ) r8 \stemUp fis,4 -- \stemUp gis4 -- | % 44
    \stemUp a2 ( \stemUp e8 ) r8 r4 r4 | % 45
    \stemUp <b b'>4 _\f \stemUp <c c'>4 \stemUp <d d'>4 \stemUp <e e'>4
    \stemDown <fis fis'>4 | % 46
    \stemDown <g g'>4 ( \stemUp <e e'>4 ) \stemDown <fis fis'>2. _\> | % 47
    \stemUp <e e'>4 _\! _\mf _\< \stemDown <fis fis'>4 \stemUp <g b>4
    \stemDown <a c>4 \stemDown <bes cis>4 \pageBreak | % 48
    \stemDown <b d>4 ( _\! _\ff _\> \stemUp <g b>4 ) \stemUp a2. _\! _\f
    | % 49
    \stemDown <a c>8 r8 r4 \stemUp <g bes>2 \stemUp <e bes'>4 |
    \barNumberCheck #50
    \stemUp <f a>4 \stemUp <d a'>4 \stemUp <e bes'>2. | % 51
    \stemUp <e b'>2 \stemUp <fis a>2 \stemUp <dis a'>4 | % 52
    \stemUp <e gis>4 \stemUp <cis gis'>4 \stemUp <dis a'>2. \pageBreak | % 53
    \stemUp <e gis>2 ~ ~ \stemUp <e gis>2. | % 54
    \stemUp <e a>2. \stemUp <fis a>8 r8 r4 | % 55
    \stemUp <a, e'>8 _\mf r8 r4 r2 r4 | % 56
    R4*5 \repeat volta 2 {
        | % 57
        R4*5 | % 58
        \stemUp <cis cis'>2 _\p _\< \stemUp <d d'>2. ( _\! _\>
        \pageBreak | % 59
        \stemUp <cis cis'>8 ) r8 _\! r4 \stemUp <b b'>2. ( _\mp _\> |
        \barNumberCheck #60
        \stemUp <cis cis'>8 ) r8 _\! r4 r2 r4 | % 61
        R4*5 | % 62
        \stemUp <cis cis'>2 _\p _\< \stemUp <d d'>2. ( _\! _\> | % 63
        \stemUp <cis cis'>8 ) r8 _\! r4 \stemUp <b b'>2. ( _\mp _\> | % 64
        \stemUp <cis cis'>8 ) r8 _\! r4 \stemUp <eis eis'>2 ( _\sf _\>
        \stemDown <fis fis'>8 ) r8 _\! }
    \pageBreak \repeat volta 2 {
        | % 65
        \stemDown <fis fis'>2 _\p \stemDown <g g'>2 ( -> \stemDown <fis
            fis'>4 ) | % 66
        \stemUp <b, b'>2 \stemUp <cis cis'>2 ( -> \stemUp <d d'>4 ) | % 67
        \stemUp <b b'>2 \stemDown <f' f'>2 ( -> \stemUp <e e'>4 ) | % 68
        \stemUp <a, a'>2 \stemUp <b b'>2 ( -> \stemUp <cis cis'>4 ) | % 69
        \stemUp <c c'>2 ~ ~ _ "" _\markup{ \italic {cresc.} } \stemUp
        <c c'>2. | \barNumberCheck #70
        \stemDown <f f'>2 ~ ~ \stemDown <f f'>2. \pageBreak | % 71
        \stemDown <fis fis'>2 ~ ~ \stemDown <fis fis'>2. | % 72
        \stemUp <cis a'>2 ~ ~ _\mf _\> \stemUp <cis a'>2. }
    | % 73
    R4*5 | % 74
    \stemUp <cis cis'>2 _\! _\p _\< \stemUp <d d'>2. ( _\! _\> | % 75
    \stemUp <cis cis'>8 ) r8 _\! r4 \stemUp <b b'>2. ( _\mp _\> | % 76
    \stemUp <cis cis'>8 ) r8 _\! r4 r2 r4 \pageBreak | % 77
    R4*5 | % 78
    \stemUp <cis cis'>2 _\p _\< \stemUp <d d'>2. ( _\! _\> | % 79
    \stemUp <cis cis'>8 ) _\! r8 r4 \stemUp <b b'>2. ( _\mp _\> |
    \barNumberCheck #80
    \stemUp <cis cis'>8 ) _\! r8 r4 \stemUp <eis eis'>2 ( _\sf _\>
    \stemDown <fis fis'>8 ) r8 | % 81
    \stemUp <d b'>2 _\! _\p _\< \stemUp <d c'>2. _\! _\> | % 82
    \stemUp <cis cis'>2 ~ ~ _\! _\p \stemUp <cis cis'>8 r8 r4 r4
    \pageBreak | % 83
    \stemUp <b fis'>2 _\p _\< \stemUp <b gis'>2. _\! _\> | % 84
    \stemUp <cis cis'>2 ~ ~ _\! _\p \stemUp <cis cis'>8 r8 r4 r4 | % 85
    \stemUp <d b'>2 _\p _\< \stemUp <d c'>2. _\! _\> | % 86
    \stemUp <cis cis'>2 ~ ~ _\! _\p \stemUp <cis cis'>8 r8 r4 r4 | % 87
    \stemUp <b fis'>2 _\p _\< \stemUp <b gis'>2. _\! _\> | % 88
    \stemUp <cis cis'>2 ~ ~ _\! _\p \stemUp <cis cis'>8 r8 r4 r4
    \pageBreak | % 89
    \stemUp <b g'>2 ~ ~ _\mp _\> \stemUp <b g'>8 r8 _\! r4 r4 |
    \barNumberCheck #90
    \stemUp <c c'>2 ~ ~ _\mp _\> \stemUp <c c'>8 r8 _\! r4 r4 | % 91
    \stemUp <cis cis'>2 ~ ~ _\mp _\> \stemUp <cis cis'>8 r8 _\! r4 r4 | % 92
    \stemUp <cis cis'>2 ~ ~ _\mp _\> \stemUp <cis cis'>8 r8 _\! r4 r4 | % 93
    \stemUp <b g'>2 ~ ~ _\mp _\> \stemUp <b g'>8 r8 _\! r4 r4 | % 94
    \stemUp <c c'>2 ~ ~ _\mp _\> \stemUp <c c'>8 r8 _\! r4 r4 \pageBreak
    | % 95
    \stemUp <cis cis'>2 ~ ~ _\mp _\> \stemUp <cis cis'>8 _\! r8 r4 r4 | % 96
    R4*5 | % 97
    r4 \stemUp e8 ^\mf r8 r4 r2 | % 98
    r4 \stemUp <cis a'>4 ( _\mf \stemUp <e cis'>8 ) r8 r2 | % 99
    r4 \stemUp <a, e'>8 r8 r4 r2 | \barNumberCheck #100
    R4*5 \pageBreak | % 101
    R4*5 | % 102
    r4 \stemUp cis'8 r8 r2 r4 | % 103
    R4*15 \break | % 106
    R4*25 \pageBreak | % 111
    \stemUp <b, b'>2 ~ ~ _\f _\mf \stemUp <b b'>8 r8 r2 | % 112
    r2 r4 \stemUp e'8 ( _\mf \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 ) | % 113
    r2 r4 \stemUp e8 ( \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 ) | % 114
    r2 r4 \stemUp e8 ( \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 ) | % 115
    r2 r4 \stemUp e8 ( \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 ) \break | % 116
    r2 r4 \stemUp e8 ( \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 )
    \pageBreak | % 117
    r2 r4 \stemUp e8 ( \stemUp e,8 ) \stemUp e8 ( \stemUp e'8 ) | % 118
    r2 r4 \stemUp cis8 ( _\markup{ \italic {più} } _ "" \stemUp cis,8 )
    \stemUp cis8 ( \stemUp cis'8 ) | % 119
    r2 \stemUp <cis, e>8 r8 r4 r4 | \barNumberCheck #120
    R4*10 \break | % 122
    R4*5 \pageBreak | % 123
    R4*25 \pageBreak | % 128
    \stemUp <a e'>8 _\mp r8 r4 \stemUp <cis a'>8 r8 r4 r4 | % 129
    r2 \stemUp b'2 _\mp \stemUp e,8 _\p r8 | \barNumberCheck #130
    \stemUp cis8 _\mp r8 r4 r2 r4 | % 131
    r2 _\< \stemUp gis'4 ~ _\! _\mf _\> \stemUp gis8 r8 _\! r4 | % 132
    \stemUp b8 _\mp r8 r4 r2 r4 \pageBreak | % 133
    \stemUp fis8 r8 \stemUp fis8 r8 \stemUp fis4 ~ _\mf _\> \stemUp fis8
    r8 _\! r4 | % 134
    R4*5 | % 135
    R4*5 | % 136
    r2 _\p _\< _\< r4 \stemUp cis'4 -- ^\mf \stemUp b4 -- | % 137
    \stemUp a2 \stemUp b2. \pageBreak | % 138
    \stemUp a2 ( \stemUp cis8 ) r8 \stemUp fis,4 -- \stemUp gis4 -- | % 139
    \stemUp a2 ( \stemUp e8 ) r8 r4 r4 | \barNumberCheck #140
    \stemUp <b b'>4 _\f \stemUp <c c'>4 \stemUp <d d'>4 \stemUp <e e'>4
    \stemDown <fis fis'>4 | % 141
    \stemDown <g g'>4 ( \stemUp <e e'>4 ) \stemDown <fis fis'>2. _\> | % 142
    \stemUp <e e'>4 _\! _\mf _\< \stemDown <fis fis'>4 \stemUp <g b>4
    \stemDown <a c>4 \stemDown <bes cis>4 \pageBreak | % 143
    \stemDown <b d>4 ( _\! _\ff _\> \stemUp <g b>4 ) \stemUp a2. _\! _\f
    | % 144
    \stemDown <a c>8 r8 r4 \stemUp <g bes>2 \stemUp <e bes'>4 | % 145
    \stemUp <f a>4 \stemUp <d a'>4 \stemUp <e bes'>2. | % 146
    \stemUp <e b'>2 \stemUp <fis a>2 \stemUp <dis a'>4 | % 147
    \stemUp <e gis>4 \stemUp <cis gis'>4 \stemUp <dis a'>2. \pageBreak | % 148
    \stemUp <e gis>2 ~ ~ \stemUp <e gis>2. | % 149
    \stemUp <e a>2. \stemUp <fis a>8 r8 r4 | \barNumberCheck #150
    \stemUp <a, e'>8 _\mf r8 r4 r2 r4 | % 151
    R4*15 \pageBreak | % 154
    R4*30 | \barNumberCheck #160
    \stemUp f'2 ~ _\sf ^ "III." _\> \stemUp f2. _\! _\p | % 161
    \stemUp e2 ~ \stemUp e2. | % 162
    \stemUp f2 ~ _\sf _\> \stemUp f2. _\! _\p \pageBreak | % 163
    \stemUp e2 ~ \stemUp e2. | % 164
    R4*35 \break | % 171
    R4*35 \pageBreak | % 178
    R4*5 \bar "|."
    }

PartPSixVoiceTwo =  \relative b {
    \repeat volta 2 {
        \clef "treble" \time 5/4 \key c \major \transposition f s4*5 | % 2
        R4*5 s2*5 | % 5
        r2 r4 \stemDown b4 ~ \stemDown b8 r8 \pageBreak | % 6
        r2 r4 \stemDown a4 ~ \stemDown a8 r8 s4 \stemDown cis8 s8 r4
        \stemDown dis4 ~ \stemDown dis8 r8 | % 8
        \stemDown e8 r8 r4 r2 r4 s2*5 \break s4*5 \pageBreak s4*25 }
    \pageBreak s4*5 \bar "||"
    s2. \stemDown e8 ( \stemDown e'8 ) \stemDown e8 ( \stemDown e,8 )
    s2. \stemDown e8 ( \stemDown e'8 ) \stemDown e8 ( \stemDown e,8 )
    s2. \stemDown e8 ( \stemDown e'8 ) \stemDown e8 ( \stemDown e,8 )
    s2. \stemDown e8 ( \stemDown e'8 ) \stemDown e8 ( \stemDown e,8 )
    \break s2. \stemDown e8 ( \stemDown e'8 ) \stemDown e8 ( \stemDown
    e,8 ) \pageBreak s2. \stemDown e8 ( \stemDown e'8 ) \stemDown e8 (
    \stemDown e,8 ) s2. \stemDown cis8 ( \stemDown cis'8 ) \stemDown cis8
    ( \stemDown cis,8 ) s4*15 \break s4*25 \pageBreak s2*5 | % 34
    \stemDown e8 r8 \stemDown a8 r8 \stemDown e2 \stemDown e,8 s8 | % 35
    \stemDown a8 s4. \stemDown cis8 r8 \stemDown cis8 r8 \stemDown e8 r8
    | % 36
    \stemDown e8 r8 \stemDown e8 r8 \stemDown e4 ~ \stemDown e8 s4.
    \pageBreak | % 37
    \stemDown fis8 s4. \stemDown fis8 r8 \stemDown fis8 r8 \stemDown d8
    r8 | % 38
    \stemDown cis8 s8 \stemDown cis8 s8 \stemDown cis4 ~ \stemDown cis8
    s4. | % 39
    \stemDown cis2 ~ \stemDown cis8 r8 _\! \stemDown cis4 _\mp \stemDown
    a4 | \barNumberCheck #40
    \stemDown gis2 \stemDown d'8 _\! _\mf r8 r4 r4 \pageBreak | % 41
    R4*5 \pageBreak | % 42
    R4*15 s4*15 \pageBreak s2 \stemDown fis2 ( \stemDown g4 ) s1*5
    \pageBreak s1*5 \repeat volta 2 {
        s2*5 \pageBreak s2*15 }
    \pageBreak \repeat volta 2 {
        s2*15 \pageBreak s2*5 }
    s1*5 \pageBreak s2*15 \pageBreak s2*15 \pageBreak s2*15 \pageBreak
    s2*5 | % 97
    R4*5 s2*5 | \barNumberCheck #100
    r2 r4 \stemDown b,4 ~ \stemDown b8 r8 \pageBreak | % 101
    r2 r4 \stemDown a4 ~ \stemDown a8 r8 s4 \stemDown cis8 s8 r4
    \stemDown dis4 ~ \stemDown dis8 r8 | % 103
    \stemDown e8 r8 r4 r2 r4 s2*5 \break s4*25 \pageBreak s1*2 \stemDown
    e8 ( \stemDown e'8 ) \stemDown e8 ( \stemDown e,8 ) s2. \stemDown e8
    ( \stemDown e'8 ) \stemDown e8 ( \stemDown e,8 ) s2. \stemDown e8 (
    \stemDown e'8 ) \stemDown e8 ( \stemDown e,8 ) s2. \stemDown e8 (
    \stemDown e'8 ) \stemDown e8 ( \stemDown e,8 ) \break s2. \stemDown
    e8 ( \stemDown e'8 ) \stemDown e8 ( \stemDown e,8 ) \pageBreak s2.
    \stemDown e8 ( \stemDown e'8 ) \stemDown e8 ( \stemDown e,8 ) s2.
    \stemDown cis8 ( \stemDown cis'8 ) \stemDown cis8 ( \stemDown cis,8
    ) s4*15 \break s4*5 \pageBreak s4*25 \pageBreak s4*5 | % 129
    \stemDown e8 r8 \stemDown a8 r8 \stemDown e2 \stemDown e,8 s8 |
    \barNumberCheck #130
    \stemDown a8 s4. \stemDown cis8 r8 \stemDown cis8 r8 \stemDown e8 r8
    | % 131
    \stemDown e8 r8 \stemDown e8 r8 \stemDown e4 ~ \stemDown e8 s4. | % 132
    \stemDown fis8 s4. \stemDown fis8 r8 \stemDown fis8 r8 \stemDown d8
    r8 \pageBreak | % 133
    \stemDown cis8 s8 \stemDown cis8 s8 \stemDown cis4 ~ \stemDown cis8
    s4. | % 134
    \stemDown cis2 ~ \stemDown cis8 r8 _\! \stemDown cis4 _\mp \stemDown
    a4 | % 135
    \stemDown gis2 \stemDown d'8 _\! _\mf r8 r4 r4 | % 136
    R4*10 \pageBreak | % 138
    R4*10 s4*15 \pageBreak s2 \stemDown fis2 ( \stemDown g4 ) s1*5
    \pageBreak s2*15 \pageBreak s4*45 \pageBreak s1*10 \break s4*35
    \pageBreak s4*5 \bar "|."
    }

PartPSevenVoiceOne =  \relative f' {
    \repeat volta 2 {
        \clef "treble" \time 5/4 \key c \major \transposition a | % 1
        R4*25 \pageBreak | % 6
        R4*25 \break | % 11
        R4*5 \pageBreak | % 12
        R4*25 }
    \pageBreak | % 16
    R4*5 \bar "||"
    R4*20 \break | % 21
    R4*5 \pageBreak | % 22
    R4*25 \break | % 27
    R4*25 \pageBreak | % 32
    R4*5 | % 33
    \stemUp <f c'>8 _\mp r8 r4 \stemDown <a f'>8 r8 r4 r4 | % 34
    \stemUp c8 r8 \stemUp f8 r8 \stemUp g2 _\mp \stemUp c,8 _\p r8 | % 35
    \stemUp f8 _\mp r8 r4 \stemUp a,8 r8 r4 \stemUp c8 r8 | % 36
    \stemUp c8 _\< r8 \stemUp c8 r8 \stemUp e4 ~ _\! _\mf _\> \stemUp e8
    r8 _\! r4 \pageBreak | % 37
    \stemUp g8 _\mp r8 r4 \stemUp d8 r8 \stemUp d8 r8 \stemUp bes8 r8 | % 38
    \stemUp d8 r8 \stemUp d8 r8 \stemUp f4 ~ _\mf _\> \stemUp f8 r8 _\!
    r4 | % 39
    \stemUp a,2 ~ _\p _\< \stemUp a8 r8 _\! \stemUp a4 _\mp \stemUp f4 |
    \barNumberCheck #40
    \stemUp e2 _\< \stemUp bes'8 _\! _\mf r8 r4 r4 \pageBreak | % 41
    R4*5 \pageBreak | % 42
    R4*30 \pageBreak | % 48
    R4*5 | % 49
    \stemUp as4 -- _\f ^\markup{ \bold\small {a. 2} } \stemDown bes4 --
    \stemDown c4 -- \stemDown des4 -- \stemDown es4 -- | \barNumberCheck
    #50
    \stemDown f4 -- \stemDown des4 -- \stemDown es2 ~ \stemDown es8
    \stemDown es8 | % 51
    \stemDown e2 _\> r4 _\! _\p r2 | % 52
    R4*5 \pageBreak | % 53
    R4*20 \repeat volta 2 {
        | % 57
        R4*10 \pageBreak | % 59
        R4*30 }
    \pageBreak \repeat volta 2 {
        | % 65
        \stemDown <a, f'>2 _\p \stemDown <a fis'>2. -> | % 66
        \stemDown <d g>2 ~ ~ \stemDown <d g>2. | % 67
        \stemDown <bes d>2 \stemDown <g e'>2. -> | % 68
        \stemDown <c f>2 ~ ~ \stemDown <c f>2. | % 69
        \stemDown <des f>2 ~ ~ _ "" _\markup{ \italic {cresc.} }
        \stemDown <des f>2. | \barNumberCheck #70
        \stemDown <bes ges'>2 ~ ~ \stemDown <bes ges'>2. \pageBreak | % 71
        \stemDown <as as'>2 ~ ~ \stemDown <as as'>2. | % 72
        \stemDown <f' a>2 ~ ~ _\mf _\> \stemDown <f a>2. }
    | % 73
    R4*20 \pageBreak | % 77
    R4*25 | % 82
    \stemDown d2 ~ _\! ^ "I." _\p \stemDown d8 r8 r4 r4 \pageBreak | % 83
    R4*5 | % 84
    \stemDown d2 ~ _\p \stemDown d8 r8 r4 r4 | % 85
    R4*5 | % 86
    \stemDown d2 ~ _\p \stemDown d8 r8 r4 r4 | % 87
    R4*5 | % 88
    \stemDown d2 ~ _\p \stemDown d8 r8 r4 r4 \pageBreak | % 89
    \stemDown <g, es'>2 ~ ~ _\mp _\> \stemDown <g es'>8 r8 _\! r4 r4 |
    \barNumberCheck #90
    \stemDown <as d>2 ~ ~ _\mp _\> \stemDown <as d>8 r8 _\! r4 r4 | % 91
    \stemDown <a d>2 ~ ~ _\mp _\> \stemDown <a d>8 r8 _\! r4 r4 | % 92
    \stemDown <a d>2 ~ ~ _\mp _\> \stemDown <a d>8 r8 _\! r4 r4 | % 93
    \stemDown <g es'>2 ~ ~ _\mp _\> \stemDown <g es'>8 r8 _\! r4 r4 | % 94
    \stemDown <as d>2 ~ ~ _\mp _\> \stemDown <as d>8 r8 _\! r4 r4
    \pageBreak | % 95
    \stemDown <a c>2 ~ ~ _\mp _\> \stemDown <a c>8 r8 _\! r4 r4 | % 96
    R4*25 \pageBreak | % 101
    R4*25 \break | % 106
    R4*25 \pageBreak | % 111
    R4*25 \break | % 116
    R4*5 \pageBreak | % 117
    R4*25 \break | % 122
    R4*5 \pageBreak | % 123
    R4*25 \pageBreak | % 128
    \stemUp <f c'>8 _\mp r8 r4 \stemDown <a f'>8 r8 r4 r4 | % 129
    \stemUp c8 r8 \stemUp f8 r8 \stemUp g2 _\mp \stemUp c,8 _\p r8 |
    \barNumberCheck #130
    \stemUp f8 _\mp r8 r4 \stemUp a,8 r8 r4 \stemUp c8 r8 | % 131
    \stemUp c8 _\< r8 \stemUp c8 r8 \stemUp e4 ~ _\! _\mf _\> \stemUp e8
    r8 _\! r4 | % 132
    \stemUp g8 _\mp r8 r4 \stemUp d8 r8 \stemUp d8 r8 \stemUp bes8 r8
    \pageBreak | % 133
    \stemUp d8 r8 \stemUp d8 r8 \stemUp f4 ~ _\mf _\> \stemUp f8 r8 _\!
    r4 | % 134
    \stemUp a,2 ~ _\p _\< \stemUp a8 r8 _\! \stemUp a4 _\mp \stemUp f4 | % 135
    \stemUp e2 _\< \stemUp bes'8 _\! _\mf r8 r4 r4 | % 136
    R4*10 \pageBreak | % 138
    R4*25 \pageBreak | % 143
    R4*5 | % 144
    \stemUp as4 -- _\f ^\markup{ \bold\small {a. 2} } \stemDown bes4 --
    \stemDown c4 -- \stemDown des4 -- \stemDown es4 -- | % 145
    \stemDown f4 -- \stemDown des4 -- \stemDown es2 ~ \stemDown es8
    \stemDown es8 | % 146
    \stemDown e2 _\> r4 _\! _\p r2 | % 147
    R4*5 \pageBreak | % 148
    R4*30 \pageBreak | % 154
    R4*10 | % 156
    \stemDown <a, f'>2 _\p \stemDown <g e'>2. -> | % 157
    \stemUp <f d'>2 \stemUp <f c'>2. -> | % 158
    \stemUp <d bes'>2 \stemUp <f a>2. -> | % 159
    \stemUp <e g>2 \stemUp <d f>2. -> | \barNumberCheck #160
    R4*15 \pageBreak | % 163
    R4*40 \break | % 171
    R4*35 \pageBreak | % 178
    R4*5 \bar "|."
    }

PartPSevenVoiceTwo =  \relative c'' {
    \repeat volta 2 {
        \clef "treble" \time 5/4 \key c \major \transposition a s4*25
        \pageBreak s4*25 \break s4*5 \pageBreak s4*25 }
    \pageBreak s4*5 \bar "||"
    s1*5 \break s4*5 \pageBreak s4*25 \break s4*25 \pageBreak s2*5 | % 34
    r2 \stemDown c2 \stemDown c,8 s8 | % 35
    \stemDown f8 s4. r2 r4 | % 36
    r2 \stemDown c'4 ~ \stemDown c8 s4. \pageBreak | % 37
    \stemDown d8 s4. r2 r4 | % 38
    \stemDown d,8 s8 \stemDown d8 s8 \stemDown f4 ~ \stemDown f8 s4. | % 39
    R4*10 \pageBreak s4*5 \pageBreak s2*15 \pageBreak s4*25 \pageBreak
    s1*5 \repeat volta 2 {
        s2*5 \pageBreak s2*15 }
    \pageBreak \repeat volta 2 {
        s2*15 \pageBreak s2*5 }
    s1*5 \pageBreak s2*15 \pageBreak s2*15 \pageBreak s2*15 \pageBreak
    s2*15 \pageBreak s4*25 \break s4*25 \pageBreak s4*25 \break s4*5
    \pageBreak s4*25 \break s4*5 \pageBreak s4*25 \pageBreak s4*5 | % 129
    r2 \stemDown c'2 \stemDown c,8 s8 | \barNumberCheck #130
    \stemDown f8 s4. r2 r4 | % 131
    r2 \stemDown c'4 ~ \stemDown c8 s4. | % 132
    \stemDown d8 s4. r2 r4 \pageBreak | % 133
    \stemDown d,8 s8 \stemDown d8 s8 \stemDown f4 ~ \stemDown f8 s4. | % 134
    R4*10 s2*5 \pageBreak s4*25 \pageBreak s4*25 \pageBreak s2*15
    \pageBreak s4*45 \pageBreak s1*10 \break s4*35 \pageBreak s4*5 \bar
    "|."
    }

PartPEightVoiceOne =  \relative f {
    \repeat volta 2 {
        \clef "tenor" \time 5/4 \key d \major | % 1
        R4*25 \pageBreak | % 6
        R4*25 \break | % 11
        R4*5 \pageBreak | % 12
        R4*25 }
    \pageBreak | % 16
    R4*5 \bar "||"
    R4*20 \break | % 21
    R4*5 \pageBreak | % 22
    R4*25 \break | % 27
    R4*25 \pageBreak | % 32
    R4*25 \pageBreak | % 37
    R4*20 \pageBreak | % 41
    R4*5 \pageBreak | % 42
    R4*30 \pageBreak | % 48
    R4*5 | % 49
    \stemUp f4 -- _\f ^\markup{ \bold\small {a. 2} } \stemUp g4 --
    \stemDown a4 -- \stemDown bes4 -- \stemDown c4 -- | \barNumberCheck
    #50
    \stemDown d4 -- \stemDown bes4 -- \stemDown c2 ~ \stemDown c8
    \stemDown c8 | % 51
    \stemDown cis2 _\> r4 _\! _\p r2 | % 52
    R4*5 \pageBreak | % 53
    R4*20 \repeat volta 2 {
        | % 57
        R4*10 \pageBreak | % 59
        R4*30 }
    \pageBreak \repeat volta 2 {
        | % 65
        \stemDown <fis, d'>2 _\p \stemDown <fis dis'>2. -> | % 66
        \stemDown <b e>2 ~ ~ \stemDown <b e>2. | % 67
        \stemDown <g b>2 \stemUp <e cis'>2. -> | % 68
        \stemDown <a d>2 ~ ~ \stemDown <a d>2. | % 69
        \stemDown <bes d>2 ~ ~ _ "" _\markup{ \italic {cresc.} }
        \stemDown <bes d>2. | \barNumberCheck #70
        \stemDown <g es'>2 ~ ~ \stemDown <g es'>2. \pageBreak | % 71
        \stemDown <f f'>2 ~ ~ \stemDown <f f'>2. | % 72
        \stemDown <fis fis'>2 ~ ~ _\mf _\> \stemDown <fis fis'>2. }
    | % 73
    R4*20 \pageBreak | % 77
    R4*20 | % 81
    \stemUp e'2 _\! _\p _\< \stemUp eis2. ( _\! _\> | % 82
    \stemUp fis8 ) _\! r8 r4 r2 r4 \pageBreak | % 83
    \stemDown <g, b>2 _\p _\< \stemDown <g cis>2. _\! _\> | % 84
    \stemDown <b fis'>2 ~ ~ _\! \stemDown <b fis'>8 r8 r4 r4 | % 85
    \stemUp e2 _\p _\< \stemUp eis2. ( _\! _\> | % 86
    \stemUp fis8 ) _\! r8 r4 r2 r4 | % 87
    \stemDown <g, b>2 _\p _\< \stemDown <g cis>2. _\! _\> | % 88
    \stemDown <b fis'>2 ~ ~ _\! \stemDown <b fis'>8 r8 r4 r4 \pageBreak
    | % 89
    \stemDown <g c>2 ~ ~ _\mp _\> \stemDown <g c>8 r8 _\! r4 r4 |
    \barNumberCheck #90
    \stemUp <f b>2 ~ ~ _\mp _\> \stemUp <f b>8 r8 _\! r4 r4 | % 91
    \stemUp <fis b>2 ~ ~ _\mp _\> \stemUp <fis b>8 r8 _\! r4 r4 | % 92
    \stemUp <fis b>2 ~ ~ _\mp _\> \stemUp <fis b>8 r8 _\! r4 r4 | % 93
    \stemDown <g c>2 ~ ~ _\mp _\> \stemDown <g c>8 r8 _\! r4 r4 | % 94
    \stemUp <f b>2 ~ ~ _\mp _\> \stemUp <f b>8 r8 _\! r4 r4 \pageBreak | % 95
    \stemUp <fis a>2 ~ ~ _\mp _\> \stemUp <fis a>8 r8 _\! r4 r4 | % 96
    R4*25 \pageBreak | % 101
    R4*25 \break | % 106
    R4*25 \pageBreak | % 111
    R4*25 \break | % 116
    R4*5 \pageBreak | % 117
    R4*25 \break | % 122
    R4*5 \pageBreak | % 123
    R4*25 \pageBreak | % 128
    R4*25 \pageBreak | % 133
    R4*25 \pageBreak | % 138
    R4*25 \pageBreak | % 143
    R4*5 | % 144
    \stemUp f4 -- _\f ^\markup{ \bold\small {a. 2} } \stemUp g4 --
    \stemDown a4 -- \stemDown bes4 -- \stemDown c4 -- | % 145
    \stemDown d4 -- \stemDown bes4 -- \stemDown c2 ~ \stemDown c8
    \stemDown c8 | % 146
    \stemDown cis2 _\> r4 _\! _\p r2 | % 147
    R4*5 \pageBreak | % 148
    R4*30 \pageBreak | % 154
    R4*10 | % 156
    \stemDown <fis, d'>2 _\p \stemUp <e cis'>2. -> | % 157
    \stemUp <fis b>2 \stemUp <fis a>2. -> | % 158
    \stemUp d'2 r2 r4 | % 159
    R4*20 \pageBreak | % 163
    R4*40 \break | % 171
    R4*35 \pageBreak | % 178
    R4*5 \bar "|."
    }

PartPEightVoiceTwo =  \relative b {
    \repeat volta 2 {
        \clef "tenor" \time 5/4 \key d \major s4*25 \pageBreak s4*25
        \break s4*5 \pageBreak s4*25 }
    \pageBreak s4*5 \bar "||"
    s1*5 \break s4*5 \pageBreak s4*25 \break s4*25 \pageBreak s4*25
    \pageBreak s1*5 \pageBreak s4*5 \pageBreak s2*15 \pageBreak s4*25
    \pageBreak s1*5 \repeat volta 2 {
        s2*5 \pageBreak s2*15 }
    \pageBreak \repeat volta 2 {
        s2*15 \pageBreak s2*5 }
    s1*5 \pageBreak s1*5 | % 81
    \stemDown b2 \stemDown b2. | % 82
    \stemDown b2 ~ \stemDown b8 r8 r4 r4 \pageBreak s2*5 | % 85
    \stemDown b2 \stemDown b2. | % 86
    \stemDown b2 ~ \stemDown b8 r8 r4 r4 s2*5 \pageBreak s2*15
    \pageBreak s2*15 \pageBreak s4*25 \break s4*25 \pageBreak s4*25
    \break s4*5 \pageBreak s4*25 \break s4*5 \pageBreak s4*25 \pageBreak
    s4*25 \pageBreak s4*25 \pageBreak s4*25 \pageBreak s4*25 \pageBreak
    s2*15 \pageBreak s1*5 | % 158
    \stemDown g2 \stemDown a2. -> | % 159
    \stemDown a2 \stemDown fis2. -> s4*15 \pageBreak s1*10 \break s4*35
    \pageBreak s4*5 \bar "|."
    }

PartPNineVoiceOne =  \relative a, {
    \repeat volta 2 {
        \clef "bass" \time 5/4 \key d \major | % 1
        R4*25 \pageBreak | % 6
        R4*25 \break | % 11
        R4*5 \pageBreak | % 12
        R4*25 }
    \pageBreak | % 16
    R4*5 \bar "||"
    \stemUp a2 ~ _\p \stemUp a8 \stemUp a8 \stemUp a4 \stemUp cis4 | % 18
    \stemUp a2 ~ \stemUp a8 \stemUp a8 \stemUp a4 \stemDown d4 | % 19
    \stemUp a2 ~ \stemUp a8 \stemUp a8 \stemUp a4 \stemDown d4 |
    \barNumberCheck #20
    \stemUp a2 ~ \stemUp a8 \stemUp a8 \stemUp a4 \stemUp cis4 \break | % 21
    \stemUp a2 ~ \stemUp a8 \stemUp a8 \stemUp a4 \stemUp cis4
    \pageBreak | % 22
    \stemUp a2 ~ \stemUp a8 \stemUp a8 \stemUp a4 \stemUp b4 | % 23
    \stemUp cis2 ~ _\mp \stemUp cis8 \stemUp cis8 \stemUp cis4 \stemDown
    fis4 | % 24
    \stemUp cis2 ( \stemUp fis,8 ) r8 r2 | % 25
    R4*10 \break | % 27
    R4*25 \pageBreak | % 32
    R4*25 \pageBreak | % 37
    R4*20 \pageBreak | % 41
    R4*5 \pageBreak | % 42
    R4*30 \pageBreak | % 48
    R4*15 | % 51
    \stemDown e'4 -- _\f \stemDown fis4 -- \stemDown gis4 -- \stemDown a4
    -- \stemDown b4 -- | % 52
    \stemDown cis4 -- \stemDown a4 -- \stemDown b2 ~ _\> \stemDown b8
    \stemDown b8 \pageBreak | % 53
    \stemDown cis8 _\! _\mp r8 r4 r2 r4 | % 54
    R4*15 \repeat volta 2 {
        | % 57
        R4*10 \pageBreak | % 59
        R4*30 }
    \pageBreak \repeat volta 2 {
        | % 65
        R4*30 \pageBreak | % 71
        R4*10 }
    | % 73
    R4*20 \pageBreak | % 77
    R4*20 | % 81
    \stemDown g2 _\p _\< \stemDown g2. _\! _\> | % 82
    \stemDown fis2 ~ _\! \stemDown fis8 r8 r4 r4 \pageBreak | % 83
    \stemDown e2 _\p _\< \stemDown e2. _\! _\> | % 84
    \stemDown fis2 ~ _\! \stemDown fis8 r8 r4 r4 | % 85
    \stemDown g2 _\p _\< \stemDown g2. _\! _\> | % 86
    \stemDown fis2 ~ _\! \stemDown fis8 r8 r4 r4 | % 87
    \stemDown e2 _\p _\< \stemDown e2. _\! _\> | % 88
    \stemDown fis2 ~ _\! \stemDown fis8 r8 r4 r4 \pageBreak | % 89
    \stemDown e2 ~ _\mp _\> \stemDown e8 r8 _\! r4 r4 | \barNumberCheck
    #90
    R4*15 | % 93
    \stemDown e2 ~ _\mp _\> \stemDown e8 r8 _\! r4 r4 | % 94
    R4*5 \pageBreak | % 95
    R4*30 \pageBreak | % 101
    R4*25 \break | % 106
    R4*25 \pageBreak | % 111
    R4*5 | % 112
    \stemUp a,2 ~ _\p \stemUp a8 \stemUp a8 \stemUp a4 \stemUp cis4 | % 113
    \stemUp a2 ~ \stemUp a8 \stemUp a8 \stemUp a4 \stemDown d4 | % 114
    \stemUp a2 ~ \stemUp a8 \stemUp a8 \stemUp a4 \stemDown d4 | % 115
    \stemUp a2 ~ \stemUp a8 \stemUp a8 \stemUp a4 \stemUp cis4 \break | % 116
    \stemUp a2 ~ \stemUp a8 \stemUp a8 \stemUp a4 \stemUp cis4
    \pageBreak | % 117
    \stemUp a2 ~ \stemUp a8 \stemUp a8 \stemUp a4 \stemUp b4 | % 118
    \stemUp cis2 ~ _\mp \stemUp cis8 \stemUp cis8 \stemUp cis4 \stemDown
    fis4 | % 119
    \stemUp cis2 ( \stemUp fis,8 ) r8 r2 | \barNumberCheck #120
    R4*10 \break | % 122
    R4*5 \pageBreak | % 123
    R4*25 \pageBreak | % 128
    R4*25 \pageBreak | % 133
    R4*25 \pageBreak | % 138
    R4*25 \pageBreak | % 143
    R4*15 | % 146
    \stemDown e'4 -- _\f \stemDown fis4 -- \stemDown gis4 -- \stemDown a4
    -- \stemDown b4 -- | % 147
    \stemDown cis4 -- \stemDown a4 -- \stemDown b2 ~ _\> \stemDown b8
    \stemDown b8 \pageBreak | % 148
    \stemDown cis8 _\! _\mp r8 r4 r2 r4 | % 149
    R4*25 \pageBreak | % 154
    R4*45 \pageBreak | % 163
    R4*40 \break | % 171
    R4*35 \pageBreak | % 178
    R4*5 \bar "|."
    }

PartPOneZeroVoiceOne =  \relative e, {
    \repeat volta 2 {
        \clef "bass" \time 5/4 \key d \major | % 1
        R4*25 \pageBreak | % 6
        R4*25 \break | % 11
        R4*5 \pageBreak | % 12
        R4*25 }
    \pageBreak | % 16
    R4*5 \bar "||"
    R4*20 \break | % 21
    R4*5 \pageBreak | % 22
    R4*25 \break | % 27
    R4*25 \pageBreak | % 32
    R4*25 \pageBreak | % 37
    R4*20 \pageBreak | % 41
    R4*5 \pageBreak | % 42
    R4*30 \pageBreak | % 48
    R4*15 | % 51
    \stemUp e4 -- _\f \stemUp fis4 -- \stemUp gis4 -- \stemUp a4 --
    \stemUp b4 -- | % 52
    \stemUp cis4 -- \stemUp a4 -- \stemUp b2 ~ _\> \stemUp b8 \stemUp b8
    \pageBreak | % 53
    \stemUp a8 _\! _\mp r8 r4 r2 r4 | % 54
    R4*15 \repeat volta 2 {
        | % 57
        R4*10 \pageBreak | % 59
        R4*30 }
    \pageBreak \repeat volta 2 {
        | % 65
        R4*30 \pageBreak | % 71
        R4*10 }
    | % 73
    R4*20 \pageBreak | % 77
    R4*20 | % 81
    \stemUp d,2 ~ _\p _\> \stemUp d8 r8 _\! r4 r4 | % 82
    R4*5 \pageBreak | % 83
    \stemUp d2 ~ _\p _\> \stemUp d8 r8 _\! r4 r4 | % 84
    R4*5 | % 85
    \stemUp d2 ~ _\p _\> \stemUp d8 r8 _\! r4 r4 | % 86
    R4*5 | % 87
    \stemUp d2 ~ _\p _\> \stemUp d8 r8 _\! r4 r4 | % 88
    R4*5 \pageBreak | % 89
    \stemUp d2 ~ _\mp _\> \stemUp d8 r8 _\! r4 r4 | \barNumberCheck #90
    \stemUp d2 ~ _\mp _\> \stemUp d8 r8 _\! r4 r4 | % 91
    \stemUp d2 ~ _\mp _\> \stemUp d8 r8 _\! r4 r4 | % 92
    \stemUp d2 ~ _\mp _\> \stemUp d8 r8 _\! r4 r4 | % 93
    \stemUp d2 ~ _\mp _\> \stemUp d8 r8 _\! r4 r4 | % 94
    \stemUp d2 ~ _\mp _\> \stemUp d8 r8 _\! r4 r4 \pageBreak | % 95
    \stemUp d2 ~ _\mp _\> \stemUp d8 r8 _\! r4 r4 | % 96
    R4*25 \pageBreak | % 101
    R4*25 \break | % 106
    R4*25 \pageBreak | % 111
    R4*25 \break | % 116
    R4*5 \pageBreak | % 117
    R4*25 \break | % 122
    R4*5 \pageBreak | % 123
    R4*25 \pageBreak | % 128
    R4*25 \pageBreak | % 133
    R4*25 \pageBreak | % 138
    R4*25 \pageBreak | % 143
    R4*15 | % 146
    \stemUp e4 -- _\f \stemUp fis4 -- \stemUp gis4 -- \stemUp a4 --
    \stemUp b4 -- | % 147
    \stemUp cis4 -- \stemUp a4 -- \stemUp b2 ~ _\> \stemUp b8 \stemUp b8
    \pageBreak | % 148
    \stemUp a8 _\! _\mp r8 r4 r2 r4 | % 149
    R4*25 \pageBreak | % 154
    R4*45 \pageBreak | % 163
    R4*40 \break | % 171
    R4*35 \pageBreak | % 178
    R4*5 \bar "|."
    }

PartPOneOneVoiceOne =  \relative e {
    \repeat volta 2 {
        \clef "bass" \time 5/4 \key c \major | % 1
        R4*25 \pageBreak | % 6
        R4*25 \break | % 11
        R4*5 \pageBreak | % 12
        R4*25 }
    \pageBreak | % 16
    R4*5 \bar "||"
    R4*20 \break | % 21
    R4*5 \pageBreak | % 22
    R4*25 \break | % 27
    R4*25 \pageBreak | % 32
    R4*25 \pageBreak | % 37
    R4*20 \pageBreak | % 41
    R4*5 \pageBreak | % 42
    R4*30 \pageBreak | % 48
    R4*15 | % 51
    \stemDown e2 :32 _\f _\> \stemDown e2. :32 | % 52
    \stemDown e2 :32 \stemDown e2 :32 \stemDown e8 _\! _\p r8 \pageBreak
    | % 53
    R4*10 | % 55
    \stemUp a,8 _\mp r8 r4 r2 r4 | % 56
    \stemUp a8 _\mf r8 r4 \stemDown d8 _\p r8 \stemDown d8 r8 \stemDown
    d8 r8 \repeat volta 2 {
        | % 57
        \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8
        \stemDown d8 r8 | % 58
        \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8
        \stemDown d8 r8 \pageBreak | % 59
        \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8
        \stemDown d8 r8 | \barNumberCheck #60
        \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8
        \stemDown d8 r8 | % 61
        \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8
        \stemDown d8 r8 | % 62
        \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8
        \stemDown d8 r8 | % 63
        \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8
        \stemDown d8 r8 | % 64
        \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8
        \stemDown d8 r8 }
    \pageBreak \repeat volta 2 {
        | % 65
        \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8
        \stemDown d8 r8 | % 66
        \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8
        \stemDown d8 r8 | % 67
        \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8
        \stemDown d8 r8 | % 68
        \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8
        \stemDown d8 r8 | % 69
        \stemDown d8 _ "" _\markup{ \italic {cresc.} } r8 \stemDown d8
        r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 |
        \barNumberCheck #70
        \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8
        \stemDown d8 r8 \pageBreak | % 71
        \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8
        \stemDown d8 r8 | % 72
        \stemDown d8 _\mf _\> r8 \stemDown d8 r8 \stemDown d8 r8
        \stemDown d8 r8 \stemDown d8 r8 }
    | % 73
    \stemDown d8 _\! _\p r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8
    r8 \stemDown d8 r8 | % 74
    \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8
    \stemDown d8 r8 | % 75
    \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8
    \stemDown d8 r8 | % 76
    \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8
    \stemDown d8 r8 \pageBreak | % 77
    \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8
    \stemDown d8 r8 | % 78
    \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8
    \stemDown d8 r8 | % 79
    \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8
    \stemDown d8 r8 | \barNumberCheck #80
    \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8 \stemDown d8 r8
    \stemDown d8 r8 | % 81
    \stemDown d8 _\mf r8 \stemDown d8 r8 \stemDown d8 _\> r8 \stemDown d8
    r8 \stemDown d8 r8 | % 82
    \stemDown d2 :32 _\! _\p \stemDown d8 r8 r4 r4 \pageBreak | % 83
    \stemDown d8 _\mf r8 \stemDown d8 r8 \stemDown d8 _\> r8 \stemDown d8
    r8 \stemDown d8 r8 | % 84
    \stemDown d2 :32 _\! _\p \stemDown d8 r8 r4 r4 | % 85
    \stemDown d8 _\mf r8 \stemDown d8 r8 \stemDown d8 _\> r8 \stemDown d8
    r8 \stemDown d8 r8 | % 86
    \stemDown d2 :32 _\! _\p \stemDown d8 r8 r4 r4 | % 87
    \stemDown d8 _\mf r8 \stemDown d8 r8 \stemDown d8 _\> r8 \stemDown d8
    r8 \stemDown d8 r8 | % 88
    \stemDown d2 :32 _\! _\p \stemDown d8 r8 r4 r4 \pageBreak | % 89
    \stemDown d2 :32 _\mp _\> \stemDown d8 r8 _\! r2 | \barNumberCheck
    #90
    \stemDown d2 :32 _\mp _\> \stemDown d8 r8 _\! r2 | % 91
    \stemDown d2 :32 _\mp _\> \stemDown d8 r8 _\! r2 | % 92
    \stemDown d2 :32 _\mp _\> \stemDown d8 r8 _\! r2 | % 93
    \stemDown d2 :32 _\mp _\> \stemDown d8 r8 _\! r2 | % 94
    \stemDown d2 :32 _\mp _\> \stemDown d8 r8 _\! r2 \pageBreak | % 95
    \stemDown d2 :32 _\mp _\> \stemDown d8 r8 _\! r2 | % 96
    R4*25 \pageBreak | % 101
    R4*25 \break | % 106
    R4*25 \pageBreak | % 111
    R4*25 \break | % 116
    R4*5 \pageBreak | % 117
    R4*25 \break | % 122
    R4*5 \pageBreak | % 123
    R4*25 \pageBreak | % 128
    R4*25 \pageBreak | % 133
    R4*25 \pageBreak | % 138
    R4*25 \pageBreak | % 143
    R4*15 | % 146
    \stemDown e2 :32 _\f _\> \stemDown e2. :32 | % 147
    \stemDown e2 :32 \stemDown e2 :32 \stemDown e8 _\! _\p r8 \pageBreak
    | % 148
    R4*10 | \barNumberCheck #150
    \stemUp a,8 _\mp r8 r4 r2 r4 | % 151
    \stemUp a8 _\mf r8 r4 \stemDown d2. :32 _\p | % 152
    \stemDown d2 :32 \stemDown d2. :32 | % 153
    \stemDown d2 :32 \stemDown d2. :32 \pageBreak | % 154
    \stemDown d2 :32 \stemDown d2. :32 | % 155
    \stemDown d2 :32 \stemDown d2. :32 | % 156
    \stemDown d8 -. r8 r4 r2 r4 | % 157
    R4*30 \pageBreak | % 163
    R4*40 \break | % 171
    R4*35 \pageBreak | % 178
    R4*5 \bar "|."
    }

PartPOneTwoVoiceOne =  \relative d' {
    \repeat volta 2 {
        \clef "treble" \time 5/4 \key d \major | % 1
        R4*15 | % 4
        \stemUp d8 _\mf ^\markup{ \italic {pizz.} } r8 r4 \stemUp cis8 r8
        r4 r4 | % 5
        \stemUp <g e'>8 r8 r4 r2 r4 \pageBreak | % 6
        \stemUp b8 r8 r4 r2 r4 | % 7
        \stemUp d8 r8 r4 \stemUp b8 r8 r4 r4 | % 8
        \stemUp cis8 _\f r8 r4 r2 r4 | % 9
        r4 \stemDown d'8 _\mf r8 \stemDown d2 ( ^\markup{ \italic {arco}
            } \stemUp a8 ) r8 | \barNumberCheck #10
        \stemDown d8 ^\markup{ \italic {pizz.} } r8 r4 \stemDown <g, e'>8
        r8 \stemDown e'4 ( ^\markup{ \italic {arco} } \stemUp a,8 ) r8
        \break | % 11
        \stemDown d8 ^\markup{ \italic {pizz.} } r8 \stemUp a8 r8
        \stemUp e'4 ( ^\markup{ \italic {div.} } ^\markup{ \italic
            {arco} } \stemUp fis4 \stemUp g4 \pageBreak | % 12
        \stemUp fis8 ) r8 \stemUp a,8 ^\markup{ \italic {pizz.} } r8
        \stemUp cis4 ~ ^\markup{ \italic {arco} } \stemUp cis8 r8 r4 | % 13
        \stemDown b2 ( ^\markup{ \italic {unis.} } _\markup{ \italic
            {sempre} } _ "" \stemUp ais2. ) | % 14
        \stemUp fis2 ~ \stemUp fis2. | % 15
        \stemUp a2 ( \stemUp gis2. ) | % 16
        \stemUp e2 ~ \stemUp e8 r8 r4 r4 }
    \pageBreak r2 \stemDown cis'8 ( _\mf \stemDown d8 \stemDown e8 )
    \stemDown fis8 ( -. \stemDown g8 -. \stemDown a8 ) -. \bar "||"
    \stemDown b4 ( \stemDown e,4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( \stemDown d8 \stemDown e8 }
    \stemDown fis4 \stemDown g4 ) | % 18
    \stemDown a8 -. r16 \stemDown b16 ( \stemDown a8 ) -. r16 \stemDown
    g16 ( \stemDown a2. ) _\< | % 19
    \stemDown a4 ( _\! _\markup{ \italic {più} } _ "" \stemDown d4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 ( \stemDown b8 \stemDown a8 }
    \stemDown g4 \stemDown fis4 ) | \barNumberCheck #20
    \stemDown fis8 -. r16 \stemDown a16 ( \stemDown g8 ) -. r16
    \stemDown d16 ( \stemDown e2. ) _\> \break | % 21
    \stemDown b'4 ( _\! _\mf \stemDown e,4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( \stemDown d8 \stemDown e8 }
    \stemDown fis4 \stemDown g4 ) \pageBreak | % 22
    \stemDown a8 -. r16 \stemDown b16 ( \stemDown a8 ) -. r16 \stemDown
    g16 ( \stemDown a2. ) _\< | % 23
    \stemDown a4 ( _\! _\f \stemDown b4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 ( \stemDown gis8 \stemDown a8 }
    \stemDown cis4 ) \stemDown b4 -- | % 24
    \stemDown a8 -. r16 \stemDown b16 ( \stemDown a8 ) -. r16 \stemDown
    gis16 ( \stemDown fis8 ) r8 r4 r4 | % 25
    r2 r4 \stemDown a8 ( _\p \stemDown a'8 ) \stemDown a8 ( \stemDown a,8
    ) | % 26
    r2 r4 \stemDown a8 ( \stemDown a'8 ) \stemDown a8 ( \stemDown a,8 )
    \break | % 27
    r2 r4 \stemDown a8 ( \stemDown a'8 ) \stemDown a8 ( \stemDown a,8 )
    | % 28
    r2 r4 \stemDown a8 ( \stemDown a'8 ) \stemDown a8 ( \stemDown a,8 )
    | % 29
    r2 r4 \stemDown a8 ( \stemDown a'8 ) \stemDown a8 ( \stemDown a,8 )
    | \barNumberCheck #30
    r2 r4 \stemDown fis8 ( \stemDown fis'8 ) \stemDown fis8 ( \stemDown
    fis,8 ) | % 31
    r2 r4 \stemDown fis8 ( _\mp \stemDown fis'8 ) \stemDown fis8 (
    \stemDown fis,8 ) \pageBreak | % 32
    r2 r8 \stemDown <a, a'>8 _\mf ^\markup{ \italic {pizz.} } \stemDown
    a''8 \stemDown g8 \stemDown fis8 \stemDown e8 | % 33
    \stemDown d8 \stemDown cis8 \stemDown b8 \stemDown bes8 \stemDown a8
    \stemDown gis8 \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown es8
    | % 34
    \stemDown d8 \stemDown e8 \stemDown fis8 \stemDown g8 \stemDown a8
    \stemDown b8 \stemDown cis8 \stemDown d8 \stemDown e8 \stemDown eis8
    | % 35
    \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown cis8 \stemDown b8
    \stemDown bes8 \stemDown a8 \stemDown gis8 \stemDown g8 \stemDown
    fis8 | % 36
    \stemDown e8 \stemDown d8 \stemDown cis8 \stemDown b8 \stemUp a8
    \stemUp g8 \stemUp fis8 \stemUp e8 \stemUp d8 \stemUp cis8
    \pageBreak | % 37
    \stemUp b8 \stemUp cis8 \stemUp d8 \stemUp dis8 \stemUp e8 \stemUp
    fis8 \stemUp g8 \stemUp gis8 \stemUp a8 \stemUp ais8 | % 38
    \stemDown b8 \stemDown cis8 \stemDown d8 \stemDown cis8 \stemDown d8
    \stemDown cis8 \stemDown b8 \stemDown ais8 \stemDown a8 \stemDown
    gis8 | % 39
    \stemUp fis8 _\< \stemUp gis8 \stemUp a8 \stemUp ais8 \stemDown b8
    \stemDown cis8 \stemDown d8 \stemDown e8 \stemDown eis8 \stemDown
    fis8 | \barNumberCheck #40
    \stemDown g8 _\! _\f _\> \stemDown fis8 \stemDown e8 \stemDown d8
    \stemDown cis8 \stemDown c8 \stemDown b8 \stemDown a8 \stemUp g8 r8
    \pageBreak | % 41
    \stemDown fis'4 ( _\! _\mf ^\markup{ \italic {arco} } \stemDown g4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 ( _\< \stemDown g8 \stemDown a8 }
    \stemDown b4 \stemDown cis4 ) \pageBreak | % 42
    \stemDown d4 ( _\! \stemDown b4 ) \stemDown cis2. _\> | % 43
    \stemDown a4 ( _\! _\mf \stemDown b4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( _\< \stemDown b8 \stemDown cis8 }
    \stemDown d4 \stemDown e4 ) | % 44
    \stemDown fis4 ( _\! \stemDown d4 ) \stemDown e2 ( \stemDown f4 ) | % 45
    \stemDown g2 ~ _\f _\> \stemDown g8 _\! _\mf \stemDown g8 ~
    \stemDown g8 \stemDown g8 ~ \stemDown g8 \stemDown g8 ~ | % 46
    \stemDown g2 ~ \stemDown g8 _\> \stemDown g4 \stemDown g4 \stemDown
    g8 ~ | % 47
    \stemDown g2 ~ _\! _\p _\< \stemDown g8 \stemDown g4 \stemDown g4
    \stemDown g8 ~ \pageBreak | % 48
    \stemDown g2 ~ \stemDown g8 \stemDown g8 ~ \stemDown g8 \stemDown g8
    ( \stemDown a8 ) \stemDown a8 ( | % 49
    \stemDown bes2 ) _\! _\f \stemDown a2 ( \stemDown g4 ) |
    \barNumberCheck #50
    \stemDown f4 -- \stemDown g4 -- \stemDown a2. | % 51
    \stemDown a2 \stemDown gis2 ( \stemDown fis4 ) | % 52
    \stemDown e4 -- \stemDown fis4 -- \stemDown gis2. \pageBreak | % 53
    \stemDown g4 ( \stemDown a4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 ( \stemDown a8 \stemDown g8 }
    \stemDown fis8 ) r8 \stemDown eis4 ( | % 54
    \stemDown fis8 ) r8 \stemDown d4 ( \stemDown e8 -> \stemDown d8 )
    \stemDown cis8 -. _\> \stemDown b8 -. \stemDown a8 -. \stemDown g8
    -. | % 55
    \stemDown fis8 -. _\! _\mf r8 r4 r2 r4 | % 56
    \stemUp <g,, g'>8 _\f ^\markup{ \italic {pizz.} } r8 r4 \stemUp d'8
    _\mf r8 r4 r4 \repeat volta 2 {
        | % 57
        \stemDown fis'4. ( _\p ^\markup{ \italic {con dolcezza e
                flebile} } ^\markup{ \italic {arco} } _\< \stemDown fis8
        ) -- \stemDown fis2 ( _\! _\> \stemDown e4 ) | % 58
        \stemDown d4. ( _\! _\< \stemDown d8 ) -- \stemDown d2 ( _\! _\>
        \stemDown cis4 ) \pageBreak | % 59
        \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemDown d2 ( _\!
        _\> \stemDown cis4 ) | \barNumberCheck #60
        \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemUp g2 ( _\!
        _\> \stemUp fis4 ) | % 61
        \stemDown fis'4. ( -- _\! _\< \stemDown fis8 ) -- \stemDown fis2
        ( _\! _\> \stemDown e4 ) | % 62
        \stemDown d4. ( -- _\! _\< \stemDown d8 ) -- \stemDown d2 ( _\!
        _\> \stemDown cis4 ) | % 63
        \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemDown d2 ( _\!
        _\> \stemDown cis4 ) | % 64
        \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemDown g'2 ( _\!
        _\sf _\> \stemDown fis4 ) }
    \pageBreak \repeat volta 2 {
        | % 65
        \stemDown fis4. ( _\! _\p _\< \stemDown g8 ) -- \stemDown a2 (
        _\! \stemDown b4 ) | % 66
        \stemDown a4. ( _\> \stemDown g8 ) -- \stemDown fis2 ( -> _\!
        \stemDown e4 ) | % 67
        \stemDown e4. ( _\< \stemDown fis8 ) -- \stemDown g2 ( _\!
        \stemDown a4 ) | % 68
        \stemDown g4. ( _\> \stemDown fis8 ) -- \stemDown e2 ( -> _\!
        \stemDown d4 ) | % 69
        \stemDown d4. ( _\pp _\< \stemDown e8 ) -- \stemDown f2 ( ->
        \stemDown d4 | \barNumberCheck #70
        \stemDown es8 ) _\! r8 r4 r2 r4 \pageBreak | % 71
        \stemDown b'4. ( _\mp _\< \stemDown cis8 ) -- \stemDown d2 ( ->
        \stemDown b4 ) | % 72
        \stemDown b2 ~ _\! _\f _\> \stemDown b2. }
    | % 73
    \stemDown fis4. ( _\! _\p _\< \stemDown fis8 ) -- \stemDown fis2 (
    _\! _\> \stemDown e4 ) | % 74
    \stemDown d4. ( _\! _\< \stemDown d8 ) -- \stemDown d2 ( _\! _\>
    \stemDown cis4 ) | % 75
    \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemDown d2 ( _\! _\>
    \stemDown cis4 ) | % 76
    \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemUp g2 ( _\! _\>
    \stemUp fis4 ) \pageBreak | % 77
    \stemDown fis'4. ( -- _\! _\< \stemDown fis8 ) -- \stemDown fis2 (
    _\! _\> \stemDown e4 ) | % 78
    \stemDown d4. ( -- _\! _\< \stemDown d8 ) -- \stemDown d2 ( _\! _\>
    \stemDown cis4 ) | % 79
    \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemDown d2 ( _\! _\>
    \stemDown cis4 ) | \barNumberCheck #80
    \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemDown g'2 ( _\!
    _\sf _\> \stemDown fis4 ) _\! | % 81
    \stemDown b4. ( _\f \stemDown b8 ) -- \stemDown cis,2 ( _\>
    \stemDown b4 ) | % 82
    \stemDown fis'2 ~ _\! _\mf _\> \stemDown fis8 r8 _\! r4 r4
    \pageBreak | % 83
    \stemDown g4. ( _\f \stemDown g8 ) -- \stemDown b,2 ( _\> \stemUp
    ais4 ) | % 84
    \stemDown d2 ~ _\! _\mf _\> \stemDown d8 r8 _\! r4 r4 | % 85
    \stemDown b'4. ( _\f \stemDown b8 ) -- \stemDown cis,2 ( _\>
    \stemDown b4 ) | % 86
    \stemDown fis'2 ~ _\! _\mf _\> \stemDown fis8 r8 _\! r4 r4 | % 87
    \stemDown g4. ( _\f \stemDown g8 ) -- \stemDown b,2 ( _\> \stemUp
    ais4 ) | % 88
    \stemDown d2 ~ _\! _\mf _\> \stemDown d8 r8 _\! r4 r4 \pageBreak | % 89
    \stemDown c4 ( _\p _\< \stemDown d4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown d8 \stemDown e8 }
    \stemDown fis4 \stemDown g4 ) | \barNumberCheck #90
    \stemDown gis2 ~ _\! _\mf _\> \stemDown gis8 r8 _\! r4 r4 | % 91
    \stemUp gis,4 ( _\p _\< \stemUp ais4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp ais8 \stemUp b8 }
    \stemDown cis4 \stemDown d4 ) | % 92
    \stemDown d2 ~ _\! _\mf _\> \stemDown d8 r8 _\! r4 r4 | % 93
    \stemUp c,4 ( _\mp _\< \stemUp d4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 \stemUp d8 \stemUp e8 }
    \stemUp fis4 \stemUp g4 ) | % 94
    \stemUp gis2 ~ _\! _\mf _\> \stemUp gis8 r8 _\! r4 r4 \pageBreak | % 95
    \stemUp a,4 ( _\p _\< \stemUp b4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis8 \stemUp b8 \stemUp cis8 }
    \stemUp d4 \stemUp e4 ) | % 96
    \stemUp fis4 ( _\! _\mf \stemUp g4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ( _\< \stemUp g8 \stemUp a8 }
    \stemDown b4 \stemDown cis4 ) | % 97
    \stemDown d4 ( _\! \stemDown b4 ) \stemDown cis2. _\> | % 98
    \stemUp a4 ( _\! _\mf \stemDown b4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( _\< \stemDown b8 \stemDown cis8 }
    \stemDown d4 \stemDown e4 ) | % 99
    \stemDown fis4 ( _\! \stemDown d4 ) \stemDown e2. | \barNumberCheck
    #100
    \stemDown g4 ( _\f \stemDown fis4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( \stemDown fis8 \stemDown e8 }
    \stemDown d4 \stemDown cis4 ) \pageBreak | % 101
    \stemDown fis8 -. r16 \stemDown g16 ( \stemDown fis8 ) r16 \stemDown
    eis16 ( \stemDown fis2. ) | % 102
    \stemDown fis4 ( \stemDown e4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 ( \stemDown e8 \stemDown d8 }
    \stemDown cis4 ) \stemDown b4 ( \glissando _\< | % 103
    \stemDown b'8 ) _\! _\ff _\> \stemDown a8 ( \stemDown g8 ) \stemDown
    fis8 -. \stemDown e8 -. \stemDown es8 ( -. \stemDown d8 -. \stemDown
    cis8 -. \stemDown b8 -. \stemDown bes8 ) -. | % 104
    \stemUp a8 _\! _\mf r8 r4 \stemDown d2 ( \stemUp a8 ) r8 | % 105
    \stemDown d8 ^\markup{ \italic {pizz.} } r8 r4 \stemDown <a e'>8 r8
    \stemDown e'4 ( ^\markup{ \italic {arco} } \stemUp a,8 ) r8 \break | % 106
    \stemDown d8 ^\markup{ \italic {pizz.} } r8 \stemUp a8 r8 \stemUp e'4
    ( ^\markup{ \italic {div.} } ^\markup{ \italic {arco} } \stemUp fis4
    \stemUp g4 | % 107
    \stemUp fis8 ) r8 \stemUp a,8 ^\markup{ \italic {pizz.} } r8 \stemUp
    cis4 ~ ^\markup{ \italic {arco} } \stemUp cis8 r8 r4 | % 108
    \stemDown b2 ( ^\markup{ \italic {unis.} } _\markup{ \italic
        {sempre} } _ "" \stemUp ais2. ) | % 109
    \stemUp fis2 ~ \stemUp fis2. | \barNumberCheck #110
    \stemUp a2 ( \stemUp gis2. ) \pageBreak | % 111
    r2 \stemDown cis8 ( _\mf \stemDown d8 \stemDown e8 ) \stemDown fis8
    ( -. \stemDown g8 -. \stemDown a8 ) -. | % 112
    \stemDown b4 ( \stemDown e,4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( \stemDown d8 \stemDown e8 }
    \stemDown fis4 \stemDown g4 ) | % 113
    \stemDown a8 -. r16 \stemDown b16 ( \stemDown a8 ) -. r16 \stemDown
    g16 ( \stemDown a2. ) _\< | % 114
    \stemDown a4 ( _\! _\markup{ \italic {più} } _ "" \stemDown d4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 ( \stemDown b8 \stemDown a8 }
    \stemDown g4 \stemDown fis4 ) | % 115
    \stemDown fis8 -. r16 \stemDown a16 ( \stemDown g8 ) -. r16
    \stemDown d16 ( \stemDown e2. ) _\> \break | % 116
    \stemDown b'4 ( _\! _\mf \stemDown e,4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( \stemDown d8 \stemDown e8 }
    \stemDown fis4 \stemDown g4 ) \pageBreak | % 117
    \stemDown a8 -. r16 \stemDown b16 ( \stemDown a8 ) -. r16 \stemDown
    g16 ( \stemDown a2. ) _\< | % 118
    \stemDown a4 ( _\! _\f \stemDown b4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 ( \stemDown gis8 \stemDown a8 }
    \stemDown cis4 ) \stemDown b4 -- | % 119
    \stemDown a8 -. r16 \stemDown b16 ( \stemDown a8 ) -. r16 \stemDown
    gis16 ( \stemDown fis8 ) r8 r4 r4 | \barNumberCheck #120
    r2 r4 \stemDown a8 ( _\p \stemDown a'8 ) \stemDown a8 ( \stemDown a,8
    ) | % 121
    r2 r4 \stemDown a8 ( \stemDown a'8 ) \stemDown a8 ( \stemDown a,8 )
    \break | % 122
    r2 r4 \stemDown a8 ( \stemDown a'8 ) \stemDown a8 ( \stemDown a,8 )
    \pageBreak | % 123
    r2 r4 \stemDown a8 ( \stemDown a'8 ) \stemDown a8 ( \stemDown a,8 )
    | % 124
    r2 r4 \stemDown a8 ( \stemDown a'8 ) \stemDown a8 ( \stemDown a,8 )
    | % 125
    r2 r4 \stemDown fis8 ( \stemDown fis'8 ) \stemDown fis8 ( \stemDown
    fis,8 ) | % 126
    r2 r4 \stemDown fis8 ( _\mp \stemDown fis'8 ) \stemDown fis8 (
    \stemDown fis,8 ) | % 127
    r2 r8 \stemDown <a, a'>8 _\mf ^\markup{ \italic {pizz.} } \stemDown
    a''8 \stemDown g8 \stemDown fis8 \stemDown e8 \pageBreak | % 128
    \stemDown d8 \stemDown cis8 \stemDown b8 \stemDown bes8 \stemDown a8
    \stemDown gis8 \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown es8
    | % 129
    \stemDown d8 \stemDown e8 \stemDown fis8 \stemDown g8 \stemDown a8
    \stemDown b8 \stemDown cis8 \stemDown d8 \stemDown e8 \stemDown eis8
    | \barNumberCheck #130
    \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown cis8 \stemDown b8
    \stemDown bes8 \stemDown a8 \stemDown gis8 \stemDown g8 \stemDown
    fis8 | % 131
    \stemDown e8 \stemDown d8 \stemDown cis8 \stemDown b8 \stemUp a8
    \stemUp g8 \stemUp fis8 \stemUp e8 \stemUp d8 \stemUp cis8 | % 132
    \stemUp b8 \stemUp cis8 \stemUp d8 \stemUp dis8 \stemUp e8 \stemUp
    fis8 \stemUp g8 \stemUp gis8 \stemUp a8 \stemUp ais8 \pageBreak | % 133
    \stemDown b8 \stemDown cis8 \stemDown d8 \stemDown cis8 \stemDown d8
    \stemDown cis8 \stemDown b8 \stemDown ais8 \stemDown a8 \stemDown
    gis8 | % 134
    \stemUp fis8 _\< \stemUp gis8 \stemUp a8 \stemUp ais8 \stemDown b8
    \stemDown cis8 \stemDown d8 \stemDown e8 \stemDown eis8 \stemDown
    fis8 | % 135
    \stemDown g8 _\! _\f _\> \stemDown fis8 \stemDown e8 \stemDown d8
    \stemDown cis8 \stemDown c8 \stemDown b8 \stemDown a8 \stemUp g8 r8
    | % 136
    \stemDown fis'4 ( _\! _\mf ^\markup{ \italic {arco} } \stemDown g4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 ( _\< \stemDown g8 \stemDown a8 }
    \stemDown b4 \stemDown cis4 ) | % 137
    \stemDown d4 ( _\! \stemDown b4 ) \stemDown cis2. _\> \pageBreak | % 138
    \stemDown a4 ( _\! _\mf \stemDown b4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( _\< \stemDown b8 \stemDown cis8 }
    \stemDown d4 \stemDown e4 ) | % 139
    \stemDown fis4 ( _\! \stemDown d4 ) \stemDown e2 ( \stemDown f4 ) |
    \barNumberCheck #140
    \stemDown g2 ~ _\f _\> \stemDown g8 _\! _\mf \stemDown g8 ~
    \stemDown g8 \stemDown g8 ~ \stemDown g8 \stemDown g8 ~ | % 141
    \stemDown g2 ~ \stemDown g8 _\> \stemDown g4 \stemDown g4 \stemDown
    g8 ~ | % 142
    \stemDown g2 ~ _\! _\p _\< \stemDown g8 \stemDown g4 \stemDown g4
    \stemDown g8 ~ \pageBreak | % 143
    \stemDown g2 ~ \stemDown g8 \stemDown g8 ~ \stemDown g8 \stemDown g8
    ( \stemDown a8 ) \stemDown a8 ( | % 144
    \stemDown bes2 ) _\! _\f \stemDown a2 ( \stemDown g4 ) | % 145
    \stemDown f4 -- \stemDown g4 -- \stemDown a2. | % 146
    \stemDown a2 \stemDown gis2 ( \stemDown fis4 ) | % 147
    \stemDown e4 -- \stemDown fis4 -- \stemDown gis2. \pageBreak | % 148
    \stemDown g4 ( \stemDown a4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 ( \stemDown a8 \stemDown g8 }
    \stemDown fis8 ) r8 \stemDown eis4 ( | % 149
    \stemDown fis8 ) r8 \stemDown d4 ( \stemDown e8 -> \stemDown d8 )
    \stemDown cis8 -. _\> \stemDown b8 -. \stemDown a8 -. \stemDown g8
    -. | \barNumberCheck #150
    \stemDown fis8 -. _\! _\mf r8 r4 r2 r4 | % 151
    \stemUp <g,, g'>8 _\f ^\markup{ \italic {pizz.} } r8 r4 \stemUp d'8
    _\mf r8 r4 r4 | % 152
    R4*10 \pageBreak | % 154
    R4*5 | % 155
    \stemUp g4 ( _\mf ^\markup{ \italic {arco} } \stemUp a4 \stemDown b4
    \stemDown cis4 \stemDown d4 ) | % 156
    R4*15 | % 159
    \stemUp g,4 ( _\p \stemUp a4 \stemDown b4 \stemDown cis4 \stemDown d4
    ) | \barNumberCheck #160
    R4*15 \pageBreak | % 163
    R4*5 | % 164
    \stemUp d,2 ~ _\p \stemUp d2. | % 165
    \stemUp es2 ~ _\markup{ \italic {poco cresc.} } \stemUp es2. | % 166
    \stemUp f2 ~ \stemUp f2. | % 167
    \stemUp <fis a>2 ~ ~ _\mf \stemUp <fis a>2. | % 168
    \stemUp <d c'>2 _\markup{ \italic {dim.} } \stemUp <d c'>2. | % 169
    \stemUp g8 _\mp r8 r4 r2 r4 | \barNumberCheck #170
    \stemUp eis2 ( ~ _\p _\> \stemUp eis2. \break | % 171
    \stemUp fis8 ) _\! _\pp r8 r4 r2 r4 | % 172
    \stemUp a,4 ( _\pp \stemUp b4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis8 ( \stemUp b8 \stemUp cis8 }
    \stemUp d4 \stemUp e4 | % 173
    \stemUp fis8 ) r8 r4 r2 r4 | % 174
    \stemUp a,4 ( _\pp \stemUp b4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis8 ( \stemUp b8 \stemUp cis8 }
    \stemUp d4 \stemUp e4 | % 175
    \stemUp fis8 ) r8 r4 r2 r4 | % 176
    R4*5 | % 177
    r2 \stemDown fis'8 _\pp ^\markup{ \italic {pizz.} } r8 r4 r4
    \pageBreak | % 178
    \stemUp a,,8 _\pp r8 r4 r2 r4 ^\fermata \bar "|."
    }

PartPOneTwoVoiceTwo =  \relative e' {
    \repeat volta 2 {
        \clef "treble" \time 5/4 \key d \major s4*25 \pageBreak s4*25
        \break s2 \stemDown e4 ( \stemDown fis4 \stemDown g4 \pageBreak
        | % 12
        \stemDown fis8 ) s8 \stemDown a8 s8 \stemDown a4 ~ \stemDown a8
        s8*43 }
    \pageBreak s4*5 \bar "||"
    s1*5 \break s4*5 \pageBreak s4*25 \break s4*25 \pageBreak s4*25
    \pageBreak s1*5 \pageBreak s4*5 \pageBreak s2*15 \pageBreak s4*25
    \pageBreak s1*5 \repeat volta 2 {
        s2*5 \pageBreak s2*15 }
    \pageBreak \repeat volta 2 {
        s2*15 \pageBreak s2*5 }
    s1*5 \pageBreak s2*15 \pageBreak s2*15 \pageBreak s2*15 \pageBreak
    s2*15 \pageBreak s4*9 \once \override NoteHead.style = ##f
    \stemNeutral b8 \once \override NoteHead.style = ##f \stemNeutral b8
    | % 103
     \once \override NoteHead.style = ##f \stemNeutral b'8 s8*29 \break
    s2 \stemDown e,,4 ( \stemDown fis4 \stemDown g4 | % 107
    \stemDown fis8 ) s8 \stemDown a8 s8 \stemDown a4 ~ \stemDown a8
    s8*33 \pageBreak s4*25 \break s4*5 \pageBreak s4*25 \break s4*5
    \pageBreak s4*25 \pageBreak s4*25 \pageBreak s4*25 \pageBreak s4*25
    \pageBreak s4*25 \pageBreak s2*15 \pageBreak s4*45 \pageBreak s1*10
    \break s4*35 \pageBreak s4*5 \bar "|."
    }

PartPOneThreeVoiceOne =  \relative a {
    \repeat volta 2 {
        \clef "treble" \time 5/4 \key d \major | % 1
        \stemUp a8 _\mf ^\markup{ \italic {pizz.} } r8 r4 r2 r4 | % 2
        \stemUp a8 r8 r4 \stemUp a8 r8 r4 r4 | % 3
        \stemUp a8 r8 r4 r2 r4 | % 4
        \stemUp a8 r8 r4 \stemUp a8 r8 r4 r4 | % 5
        \stemUp b8 r8 r4 r2 r4 \pageBreak | % 6
        \stemUp d8 r8 r4 r2 r4 | % 7
        \stemUp b8 r8 r4 \stemUp gis8 r8 r4 r4 | % 8
        \stemUp a8 _\f r8 r4 r2 r4 | % 9
        r4 \stemUp <d a'>8 _\mf r8 \stemUp d2 ( ^\markup{ \italic {arco}
            } \stemUp a8 ) r8 | \barNumberCheck #10
        \stemUp <d a'>8 ^\markup{ \italic {pizz.} } r8 r4 \stemUp e8 r8
        \stemUp e4 ( ^\markup{ \italic {arco} } \stemUp a,8 ) r8 \break
        | % 11
        \stemUp <d a'>8 ^\markup{ \italic {pizz.} } r8 \stemUp d8 r8
        \stemUp a''2. ~ ^\markup{ \italic {div.} } ^\markup{ \italic
            {arco} } \pageBreak | % 12
        \stemUp a8 r8 r4 \stemUp cis,,4 ~ \stemUp cis8 r8 r4 | % 13
        \stemUp b2 ( ^\markup{ \italic {unis.} } _\markup{ \italic
            {sempre} } _ "" \stemUp ais2. ) | % 14
        R4*5 | % 15
        \stemUp a2 ( \stemUp gis2. ) | % 16
        r2 \stemUp a8 ^\markup{ \italic {pizz.} } r8 r2 }
    \pageBreak r2 \stemDown a'8 ( _\mf ^\markup{ \italic {arco} }
    \stemDown b8 \stemDown cis8 ) \stemDown d8 ( -. \stemDown e8 -.
    \stemDown fis8 ) -. \bar "||"
    \stemDown g4 ( \stemDown cis,4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( \stemDown b8 \stemDown cis8 }
    \stemDown dis4 \stemDown e4 ) | % 18
    \stemDown fis8 -. r16 \stemDown g16 ( \stemDown fis8 ) -. r16
    \stemDown e16 ( \stemDown fis2. ) _\< | % 19
    \stemDown fis4 ( _\! _\markup{ \italic {più} } _ "" \stemDown b4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 ( \stemDown g8 \stemDown fis8 }
    \stemDown e4 \stemDown d4 ) | \barNumberCheck #20
    \stemDown d8 -. r16 \stemDown fis16 ( \stemDown e8 ) -. r16
    \stemDown b16 ( \stemDown cis2. ) _\> \break | % 21
    \stemDown g'4 ( _\! _\mf \stemDown cis,4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( \stemDown b8 \stemDown cis8 }
    \stemDown d4 \stemDown e4 ) \pageBreak | % 22
    \stemDown fis8 -. r16 \stemDown g16 ( \stemDown fis8 ) -. r16
    \stemDown e16 ( \stemDown fis2. ) _\< | % 23
    \stemDown fis4 ( _\! _\f \stemDown gis4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 ( \stemDown eis8 \stemDown fis8 }
    \stemDown a4 ) \stemDown gis4 -- | % 24
    \stemDown fis8 -. r16 \stemDown gis16 ( \stemDown fis8 ) -. r16
    \stemDown b,16 ( \stemUp a8 ) r8 r4 r4 | % 25
    r2 \stemDown a8 ( _\p \stemDown a'8 ) \stemDown a,8 ( \stemDown a'8
    ) \stemDown a8 ( \stemDown a,8 ) | % 26
    r2 \stemDown a8 ( \stemDown a'8 ) \stemDown a,8 ( \stemDown a'8 )
    \stemDown a8 ( \stemDown a,8 ) \break | % 27
    r2 \stemDown a8 ( \stemDown a'8 ) \stemDown a,8 ( \stemDown a'8 )
    \stemDown a8 ( \stemDown a,8 ) | % 28
    r2 \stemDown a8 ( \stemDown a'8 ) \stemDown a,8 ( \stemDown a'8 )
    \stemDown a8 ( \stemDown a,8 ) | % 29
    r2 \stemDown a8 ( \stemDown a'8 ) \stemDown a,8 ( \stemDown a'8 )
    \stemDown a8 ( \stemDown a,8 ) | \barNumberCheck #30
    r2 \stemDown a8 ( \stemDown fis'8 ) \stemDown fis,8 ( \stemDown fis'8
    ) \stemDown fis8 ( \stemDown fis,8 ) | % 31
    r2 \stemDown fis8 ( _\mp \stemDown fis'8 ) \stemDown fis,8 (
    \stemDown fis'8 ) \stemDown fis8 ( \stemDown fis,8 ) \pageBreak | % 32
    r8 \stemUp a8 ( _\mp _\< \stemDown e'8 ) -. \stemDown e8 -. \stemUp
    e,8 _\! _\mf r8 \stemDown a'8 ^\markup{ \italic {pizz.} } \stemDown
    g8 \stemDown fis8 \stemDown e8 | % 33
    \stemDown d8 \stemDown cis8 \stemDown b8 \stemDown bes8 \stemUp a8
    \stemUp gis8 \stemUp g8 \stemUp fis8 \stemUp e8 \stemUp es8 | % 34
    \stemUp d8 \stemUp e8 \stemUp fis8 \stemUp g8 \stemDown a8 \stemDown
    b8 \stemDown cis8 \stemDown d8 \stemDown e8 \stemDown eis8 | % 35
    \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown cis8 \stemUp b8
    \stemUp bes8 \stemUp a8 \stemUp gis8 \stemUp g8 \stemUp fis8 | % 36
    \stemUp e8 \stemUp d8 \stemUp cis8 \stemUp b8 \stemUp a8 \stemUp g'8
    \stemUp fis8 \stemUp e8 \stemUp d8 \stemUp cis8 \pageBreak | % 37
    \stemUp b8 \stemUp cis8 \stemUp d8 \stemUp dis8 \stemUp e8 ^\markup{
        \italic {div.} } \stemUp fis8 \stemUp g8 \stemUp gis8 \stemUp a8
    \stemUp ais8 | % 38
    \stemUp b8 \stemUp cis8 \stemUp d8 \stemUp cis8 \stemUp d8 \stemUp
    cis8 \stemUp b8 \stemUp ais8 \stemUp a8 \stemUp gis8 | % 39
    \stemUp fis8 _\< \stemUp gis8 \stemUp a8 \stemUp ais8 \stemUp b8
    \stemUp cis8 \stemUp d8 \stemUp e8 \stemUp eis8 \stemUp fis8 |
    \barNumberCheck #40
    \stemUp g8 _\! _\f _\> \stemUp fis8 \stemUp e8 \stemUp d8 \stemUp
    cis8 \stemUp c8 \stemUp b8 \stemUp a8 \stemUp g8 r8 \pageBreak | % 41
    \stemUp fis4 ( _\! _\mf ^\markup{ \italic {unis.} } ^ "arco" ^ ""
    \stemUp g4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ( _\< \stemUp g8 \stemUp a8 }
    \stemDown b4 \stemDown cis4 ) \pageBreak | % 42
    \stemDown d4 ( _\! \stemDown b4 ) \stemDown cis2. _\> | % 43
    \stemUp a4 ( _\! _\mf \stemDown b4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( _\< \stemDown b8 \stemDown cis8 }
    \stemDown d4 \stemDown e4 ) | % 44
    \stemDown fis4 ( _\! \stemDown d4 ) \stemDown e2 ( \stemDown f4 ) | % 45
    \stemDown g2 ~ _\f _\> \stemDown g8 _\! _\mf \stemDown g8 ~
    \stemDown g8 \stemDown g8 ~ \stemDown g8 \stemDown g8 ~ | % 46
    \stemDown g2 ~ \stemDown g8 _\> \stemDown g4 \stemDown g4 \stemDown
    g8 ~ | % 47
    \stemDown g2 ~ _\! _\p _\< \stemDown g8 \stemDown g4 \stemDown g4
    \stemDown g8 ~ \pageBreak | % 48
    \stemDown g2 ~ \stemDown g8 \stemDown g8 ~ \stemDown g8 \stemDown g8
    ( \stemDown a8 ) \stemDown a8 ( | % 49
    \stemDown bes2 ) _\! _\f \stemDown a2 ( \stemDown g4 ) |
    \barNumberCheck #50
    \stemDown f4 -- \stemDown g4 -- \stemDown a2. | % 51
    \stemDown a2 \stemDown gis2 ( \stemDown fis4 ) | % 52
    \stemDown e4 -- \stemDown fis4 -- \stemDown gis2. \pageBreak | % 53
    \stemDown g4 ( \stemDown a4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 ( \stemDown a8 \stemDown g8 }
    \stemDown fis8 ) r8 \stemDown eis4 ( | % 54
    \stemDown fis8 ) r8 \stemDown d4 ( \stemDown e8 -> \stemDown d8 )
    \stemDown cis8 -. _\> \stemDown b8 -. \stemDown a8 -. \stemDown g8
    -. | % 55
    \stemUp fis8 -. _\! _\mf r8 r4 r2 r4 | % 56
    \stemUp cis8 _\f ^\markup{ \italic {pizz.} } r8 r4 \stemUp a8 _\mf r8
    r4 r4 \repeat volta 2 {
        | % 57
        r4 \stemUp fis'4 ( _\p ^\markup{ \italic {arco} } _\< \stemUp g2.
        ) _\! _\> | % 58
        r4 _\! \stemUp gis4 ( _\< \stemUp ais2. _\! _\> \pageBreak | % 59
        \stemDown b8 ) _\! r8 \stemDown b4 ( _\< \stemUp ais2. _\! _\> |
        \barNumberCheck #60
        \stemDown b8 ) _\! r8 \stemUp d,4 ( _\< \stemUp cis2 _\! _\>
        \stemUp d4 ) | % 61
        r4 _\! \stemUp fis4 ( _\< \stemUp g2. ) _\! _\> | % 62
        r4 _\! \stemUp gis4 ( _\< \stemUp ais2. _\! _\> | % 63
        \stemDown b8 ) _\! r8 \stemDown b4 ( _\< \stemUp ais2. _\! _\> | % 64
        \stemDown b8 ) _\! r8 \stemUp d,4 ( _\< \stemUp cis2 _\! _\>
        \stemUp d4 ) }
    \pageBreak \repeat volta 2 {
        | % 65
        \stemDown <fis fis'>4. ( _\! _\p ^\markup{ \italic {div.} } _\<
        \stemDown <g g'>8 ) -- \stemDown <a a'>2 ( _\! \stemDown <b b'>4
        ) | % 66
        \stemDown <a a'>4. ( _\> \stemDown <g g'>8 ) -- \stemDown <fis
            fis'>2 ( -> _\! \stemUp <e e'>4 ) | % 67
        \stemUp <e e'>4. ( _\< \stemDown <fis fis'>8 ) -- \stemDown <g
            g'>2 ( _\! \stemDown <a a'>4 ) | % 68
        \stemDown <g g'>4. ( _\> \stemDown <fis fis'>8 ) -- \stemUp <e
            e'>2 ( -> _\! \stemUp <d d'>4 ) | % 69
        \stemUp <d d'>4. ( _\pp _\< \stemUp <e e'>8 ) -- \stemDown <f
            f'>2 ( -> \stemUp <d d'>4 | \barNumberCheck #70
        \stemUp <es es'>8 ) _\! r8 r4 r2 r4 \pageBreak | % 71
        \stemDown b'4. ( _\mp ^\markup{ \italic {unis.} } _\< \stemDown
        cis8 ) -- \stemDown d2 ( -> \stemDown b4 ) | % 72
        \stemDown b2 ~ _\! _\f _\> \stemDown b2. }
    | % 73
    r4 _\! \stemUp fis4 ( _\p _\< \stemUp g2. ) _\! _\> | % 74
    r4 _\! \stemUp gis4 ( _\< \stemUp ais2. _\! _\> | % 75
    \stemDown b8 ) _\! r8 \stemDown b4 ( _\< \stemUp ais2. _\! _\> | % 76
    \stemDown b8 ) _\! r8 \stemUp d,4 ( _\< \stemUp cis2 _\! _\> \stemUp
    d4 ) \pageBreak | % 77
    r4 _\! \stemUp fis4 ( _\p _\< \stemUp g2. ) _\! _\> | % 78
    r4 _\! \stemUp gis4 ( _\< \stemUp ais2. _\! _\> | % 79
    \stemDown b8 ) _\! r8 \stemDown b4 ( _\< \stemUp ais2. _\! _\> |
    \barNumberCheck #80
    \stemDown b8 ) _\! r8 \stemUp d,4 ( _\< \stemUp cis2 _\! _\sf _\>
    \stemUp d4 ) _\! | % 81
    \stemDown <b' b'>4. ( _\f ^\markup{ \italic {div.} } \stemDown <b
        b'>8 ) -- \stemUp <cis, cis'>2 ( _\> \stemUp <b b'>4 ) | % 82
    \stemDown <fis' fis'>2 ~ ~ _\! _\mf _\> \stemDown <fis fis'>8 r8 _\!
    r4 r4 \pageBreak | % 83
    \stemDown <g g'>4. ( _\f \stemDown <g g'>8 ) -- \stemUp <b, b'>2 (
    _\> \stemUp <ais ais'>4 ) | % 84
    \stemUp <d d'>2 ~ ~ _\! _\mf _\> \stemUp <d d'>8 r8 _\! r4 r4 | % 85
    \stemDown <b' b'>4. ( _\f \stemDown <b b'>8 ) -- \stemUp <cis, cis'>2
    ( _\> \stemUp <b b'>4 ) | % 86
    \stemDown <fis' fis'>2 ~ ~ _\! _\mf _\> \stemDown <fis fis'>8 r8 _\!
    r4 r4 | % 87
    \stemDown <g g'>4. ( _\f \stemDown <g g'>8 ) -- \stemUp <b, b'>2 (
    _\> \stemUp <ais ais'>4 ) | % 88
    \stemUp <d d'>2 ~ ~ _\! _\mf _\> \stemUp <d d'>8 r8 _\! r4 r4
    \pageBreak | % 89
    \stemUp <c c'>4 ( _\p _\< \stemUp <d d'>4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <d d'>8 \stemUp <e e'>8 }
    \stemDown <fis fis'>4 \stemDown <g g'>4 ) | \barNumberCheck #90
    \stemDown <gis gis'>2 ~ ~ _\! _\mf _\> \stemDown <gis gis'>8 r8 _\!
    r4 r4 | % 91
    \stemUp <gis, gis'>4 ( _\p _\< \stemUp <ais ais'>4 \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp <b b'>8 \stemUp <ais ais'>8 \stemUp <b b'>8 }
    \stemUp <cis cis'>4 \stemUp <d d'>4 ) | % 92
    \stemUp <d d'>2 ~ ~ _\! _\mf _\> \stemUp <d d'>8 r8 _\! r4 r4 | % 93
    R4*10 \pageBreak | % 95
    R4*5 | % 96
    \stemUp a8 _\mf ^\markup{ \italic {unis.} } ^\markup{ \italic
        {pizz.} } r8 r4 r2 r4 | % 97
    \stemUp <d a'>8 r8 r4 \stemUp <e a>8 r8 r4 r4 | % 98
    \stemUp <d a'>8 r8 r4 r2 r4 | % 99
    \stemUp <d a'>8 r8 r4 \stemUp <cis a'>8 r8 r4 r4 | \barNumberCheck
    #100
    \stemUp <g e'>8 r8 r4 r2 r4 \pageBreak | % 101
    \stemUp <b d b'>8 r8 r4 r2 r4 | % 102
    \stemUp <b fis' d'>8 r8 r4 \stemUp <gis e' b'>8 r8 r4 r4 | % 103
    \stemUp cis8 _\f r8 r4 r2 r4 | % 104
    r4 \stemUp <d d'>8 _\mf r8 \stemUp d2 ( ^\markup{ \italic {arco} }
    \stemUp a8 ) r8 | % 105
    \stemUp <d a'>8 ^\markup{ \italic {pizz.} } r8 r4 \stemUp e8 r8
    \stemUp e4 ( ^\markup{ \italic {arco} } \stemUp a,8 ) r8 \break | % 106
    \stemUp <d a'>8 ^\markup{ \italic {pizz.} } r8 \stemUp d8 r8
    \stemDown <a' a'>2. ~ ~ ^\markup{ \italic {div.} } ^\markup{ \italic
        {arco} } | % 107
    \stemDown <a a'>8 r8 r4 \stemUp <a, cis>4 ~ ~ \stemUp <a cis>8 r8 r4
    | % 108
    \stemUp b2 ( ^\markup{ \italic {unis.} } _\markup{ \italic {sempre}
        } _ "" \stemUp ais2. ) | % 109
    R4*5 | \barNumberCheck #110
    \stemUp a2 ( \stemUp gis2. ) \pageBreak | % 111
    r2 \stemDown a'8 ( _\mf \stemDown b8 \stemDown cis8 ) \stemDown d8 (
    -. \stemDown e8 -. \stemDown fis8 ) -. | % 112
    \stemDown g4 ( \stemDown cis,4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( \stemDown b8 \stemDown cis8 }
    \stemDown dis4 \stemDown e4 ) | % 113
    \stemDown fis8 -. r16 \stemDown g16 ( \stemDown fis8 ) -. r16
    \stemDown e16 ( \stemDown fis2. ) _\< | % 114
    \stemDown fis4 ( _\! _\markup{ \italic {più} } _ "" \stemDown b4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 ( \stemDown g8 \stemDown fis8 }
    \stemDown e4 \stemDown d4 ) | % 115
    \stemDown d8 -. r16 \stemDown fis16 ( \stemDown e8 ) -. r16
    \stemDown b16 ( \stemDown cis2. ) _\> \break | % 116
    \stemDown g'4 ( _\! _\mf \stemDown cis,4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( \stemDown b8 \stemDown cis8 }
    \stemDown d4 \stemDown e4 ) \pageBreak | % 117
    \stemDown fis8 -. r16 \stemDown g16 ( \stemDown fis8 ) -. r16
    \stemDown e16 ( \stemDown fis2. ) _\< | % 118
    \stemDown fis4 ( _\! _\f \stemDown gis4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 ( \stemDown eis8 \stemDown fis8 }
    \stemDown a4 ) \stemDown gis4 -- | % 119
    \stemDown fis8 -. r16 \stemDown gis16 ( \stemDown fis8 ) -. r16
    \stemDown b,16 ( \stemUp a8 ) r8 r4 r4 | \barNumberCheck #120
    r2 \stemDown a8 ( _\p \stemDown a'8 ) \stemDown a,8 ( \stemDown a'8
    ) \stemDown a8 ( \stemDown a,8 ) | % 121
    r2 \stemDown a8 ( \stemDown a'8 ) \stemDown a,8 ( \stemDown a'8 )
    \stemDown a8 ( \stemDown a,8 ) \break | % 122
    r2 \stemDown a8 ( \stemDown a'8 ) \stemDown a,8 ( \stemDown a'8 )
    \stemDown a8 ( \stemDown a,8 ) \pageBreak | % 123
    r2 \stemDown a8 ( \stemDown a'8 ) \stemDown a,8 ( \stemDown a'8 )
    \stemDown a8 ( \stemDown a,8 ) | % 124
    r2 \stemDown a8 ( \stemDown a'8 ) \stemDown a,8 ( \stemDown a'8 )
    \stemDown a8 ( \stemDown a,8 ) | % 125
    r2 \stemDown a8 ( \stemDown fis'8 ) \stemDown fis,8 ( \stemDown fis'8
    ) \stemDown fis8 ( \stemDown fis,8 ) | % 126
    r2 \stemDown fis8 ( _\mp \stemDown fis'8 ) \stemDown fis,8 (
    \stemDown fis'8 ) \stemDown fis8 ( \stemDown fis,8 ) | % 127
    r8 \stemUp a8 ( _\mp _\< \stemDown e'8 ) -. \stemDown e8 -. \stemUp
    e,8 _\! _\mf r8 \stemDown a'8 _\mf ^\markup{ \italic {pizz.} }
    \stemDown g8 \stemDown fis8 \stemDown e8 \pageBreak | % 128
    \stemDown d8 \stemDown cis8 \stemDown b8 \stemDown bes8 \stemUp a8
    \stemUp gis8 \stemUp g8 \stemUp fis8 \stemUp e8 \stemUp es8 | % 129
    \stemUp d8 \stemUp e8 \stemUp fis8 \stemUp g8 \stemDown a8 \stemDown
    b8 \stemDown cis8 \stemDown d8 \stemDown e8 \stemDown eis8 |
    \barNumberCheck #130
    \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown cis8 \stemUp b8
    \stemUp bes8 \stemUp a8 \stemUp gis8 \stemUp g8 \stemUp fis8 | % 131
    \stemUp e8 \stemUp d8 \stemUp cis8 \stemUp b8 \stemUp a8 \stemUp g'8
    \stemUp fis8 \stemUp e8 \stemUp d8 \stemUp cis8 | % 132
    \stemUp b8 \stemUp cis8 \stemUp d8 \stemUp dis8 \stemUp e8 ^\markup{
        \italic {div.} } \stemUp fis8 \stemUp g8 \stemUp gis8 \stemUp a8
    \stemUp ais8 \pageBreak | % 133
    \stemUp b8 \stemUp cis8 \stemUp d8 \stemUp cis8 \stemUp d8 \stemUp
    cis8 \stemUp b8 \stemUp ais8 \stemUp a8 \stemUp gis8 | % 134
    \stemUp fis8 _\< \stemUp gis8 \stemUp a8 \stemUp ais8 \stemUp b8
    \stemUp cis8 \stemUp d8 \stemUp e8 \stemUp eis8 \stemUp fis8 | % 135
    \stemUp g8 _\! _\f _\> \stemUp fis8 \stemUp e8 \stemUp d8 \stemUp
    cis8 \stemUp c8 \stemUp b8 \stemUp a8 \stemUp g8 r8 | % 136
    \stemUp fis4 ( _\! _\mf ^\markup{ \italic {unis.} } ^ "arco" ^ ""
    \stemUp g4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ( _\< \stemUp g8 \stemUp a8 }
    \stemDown b4 \stemDown cis4 ) | % 137
    \stemDown d4 ( _\! \stemDown b4 ) \stemDown cis2. _\> \pageBreak | % 138
    \stemUp a4 ( _\! _\mf \stemDown b4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( _\< \stemDown b8 \stemDown cis8 }
    \stemDown d4 \stemDown e4 ) | % 139
    \stemDown fis4 ( _\! \stemDown d4 ) \stemDown e2 ( \stemDown f4 ) |
    \barNumberCheck #140
    \stemDown g2 ~ _\f _\> \stemDown g8 _\! _\mf \stemDown g8 ~
    \stemDown g8 \stemDown g8 ~ \stemDown g8 \stemDown g8 ~ | % 141
    \stemDown g2 ~ \stemDown g8 _\> \stemDown g4 \stemDown g4 \stemDown
    g8 ~ | % 142
    \stemDown g2 ~ _\! _\p _\< \stemDown g8 \stemDown g4 \stemDown g4
    \stemDown g8 ~ \pageBreak | % 143
    \stemDown g2 ~ \stemDown g8 \stemDown g8 ~ \stemDown g8 \stemDown g8
    ( \stemDown a8 ) \stemDown a8 ( | % 144
    \stemDown bes2 ) _\! _\f \stemDown a2 ( \stemDown g4 ) | % 145
    \stemDown f4 -- \stemDown g4 -- \stemDown a2. | % 146
    \stemDown a2 \stemDown gis2 ( \stemDown fis4 ) | % 147
    \stemDown e4 -- \stemDown fis4 -- \stemDown gis2. \pageBreak | % 148
    \stemDown g4 ( \stemDown a4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 ( \stemDown a8 \stemDown g8 }
    \stemDown fis8 ) r8 \stemDown eis4 ( | % 149
    \stemDown fis8 ) r8 \stemDown d4 ( \stemDown e8 -> \stemDown d8 )
    \stemDown cis8 -. _\> \stemDown b8 -. \stemDown a8 -. \stemDown g8
    -. | \barNumberCheck #150
    \stemUp fis8 -. _\! _\mf r8 r4 r2 r4 | % 151
    \stemUp cis8 _\f ^\markup{ \italic {pizz.} } r8 r4 \stemUp a8 _\mf r8
    r4 r4 | % 152
    R4*10 \pageBreak | % 154
    \stemUp b4 ( _\mf ^\markup{ \italic {arco} } \stemUp cis4 \stemUp d4
    \stemUp e4 \stemUp fis4 ) | % 155
    R4*15 | % 158
    \stemUp b,4 ( _\p \stemUp cis4 \stemUp d4 \stemUp e4 \stemUp fis4 )
    | % 159
    R4*20 \pageBreak | % 163
    R4*5 | % 164
    \stemUp bes,2 ~ _\p \stemUp bes2. | % 165
    \stemUp bes2 ~ _\markup{ \italic {poco cresc.} } \stemUp bes2. | % 166
    \stemUp b2 ~ \stemUp b2. | % 167
    \stemUp a2 ~ _\mf \stemUp a2. | % 168
    \stemUp <c a'>2 ~ ~ _\markup{ \italic {dim.} } \stemUp <c a'>2. | % 169
    \stemUp b2 ~ _\mp _\> \stemUp b2. | \barNumberCheck #170
    \stemUp b2 ~ _\! _\p _\> \stemUp b2. \break | % 171
    \stemUp a2 ~ _\! _\pp \stemUp a2. | % 172
    R4*5 | % 173
    \stemUp a2 ~ _\pp \stemUp a2. | % 174
    R4*5 | % 175
    \stemUp a2 ~ _\pp \stemUp a2. | % 176
    \stemUp a2 ~ \stemUp a2. | % 177
    r2 \stemUp <fis' a>8 _\pp ^\markup{ \italic {pizz.} } r8 r4 r4
    \pageBreak | % 178
    R4*5 \bar "|."
    }

PartPOneThreeVoiceTwo =  \relative a' {
    \repeat volta 2 {
        \clef "treble" \time 5/4 \key d \major s4*25 \pageBreak s4*25
        \break s2 \stemDown a2. ~ \pageBreak | % 12
        \stemDown a8 s4. \stemDown a,4 ~ \stemDown a8 s8*43 }
    \pageBreak s4*5 \bar "||"
    s1*5 \break s4*5 \pageBreak s4*25 \break s4*25 \pageBreak s4*25
    \pageBreak s2 \stemDown e'8 \stemDown fis8 \stemDown g,8 \stemDown
    gis8 \stemDown a8 \stemDown ais8 | % 38
    \stemDown b8 \stemDown cis8 \stemDown d8 \stemDown cis8 \stemDown d8
    \stemDown cis8 \stemDown b8 \stemDown ais8 \stemDown a8 \stemDown
    gis8 | % 39
    \stemDown fis'8 \stemDown gis,8 \stemDown a8 \stemDown ais8
    \stemDown b8 \stemDown cis8 \stemDown d8 \stemDown e8 \stemDown eis8
    \stemDown fis8 | \barNumberCheck #40
    \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown cis8
    \stemDown c8 \stemDown b8 \stemDown a8 \stemDown g8 s8 \pageBreak
    s4*5 \pageBreak s2*15 \pageBreak s4*25 \pageBreak s1*5 \repeat volta
    2 {
        s2*5 \pageBreak s2*15 }
    \pageBreak \repeat volta 2 {
        s2*15 \pageBreak s2*5 }
    s1*5 \pageBreak s2*15 \pageBreak s2*15 \pageBreak s2*15 \pageBreak
    s2*15 \pageBreak s4*25 \break s4*25 \pageBreak s4*25 \break s4*5
    \pageBreak s4*25 \break s4*5 \pageBreak s4*25 \pageBreak s2*11
    \stemDown e'8 \stemDown fis8 \stemDown g,8 \stemDown gis8 \stemDown
    a8 \stemDown ais8 \pageBreak | % 133
    \stemDown b8 \stemDown cis8 \stemDown d8 \stemDown cis8 \stemDown d8
    \stemDown cis8 \stemDown b8 \stemDown ais8 \stemDown a8 \stemDown
    gis8 | % 134
    \stemDown fis'8 \stemDown gis,8 \stemDown a8 \stemDown ais8
    \stemDown b8 \stemDown cis8 \stemDown d8 \stemDown e8 \stemDown eis8
    \stemDown fis8 | % 135
    \stemDown g8 \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown cis8
    \stemDown c8 \stemDown b8 \stemDown a8 \stemDown g8 s8*21 \pageBreak
    s4*25 \pageBreak s4*25 \pageBreak s2*15 \pageBreak s4*45 \pageBreak
    s1*10 \break s4*35 \pageBreak s4*5 \bar "|."
    }

PartPOneFourVoiceOne =  \relative d {
    \repeat volta 2 {
        \clef "alto" \time 5/4 \key d \major | % 1
        \stemUp d8 _\mf ^\markup{ \italic {pizz.} } r8 r4 r2 r4 | % 2
        \stemUp d8 r8 r4 \stemUp e8 r8 r4 r4 | % 3
        \stemUp d8 r8 r4 r2 r4 | % 4
        \stemUp d8 r8 r4 \stemUp e8 r8 r4 r4 | % 5
        \stemUp e8 r8 r4 r2 r4 \pageBreak | % 6
        \stemUp fis8 ^\markup{ \italic {div.} } r8 r4 r2 r4 | % 7
        \stemUp fis8 ^\markup{ \italic {unis.} } r8 r4 \stemUp e8 r8 r4
        r4 | % 8
        \stemUp e8 _\f r8 r4 r2 \stemUp cis8 _\mf r8 | % 9
        \stemUp d8 r8 \stemUp a'8 r8 r2 r4 | \barNumberCheck #10
        \stemUp <d, a'>8 r8 r4 \stemUp <e a>8 r8 r4 r4 \break | % 11
        \stemUp <d a'>8 r8 \stemUp a'8 r8 r2 r4 \pageBreak | % 12
        \stemUp <d, a'>8 r8 \stemUp a'8 r8 r4 \stemUp a8 r8 r4 | % 13
        r4 \stemUp g8 r8 r4 \stemUp fis2 ^\markup{ \italic {arco} } | % 14
        \stemUp fis2 ~ \stemUp fis2. | % 15
        r4 \stemUp fis8 ^\markup{ \italic {pizz.} } r8 r4 \stemUp e2
        ^\markup{ \italic {arco} } | % 16
        \stemUp e2 ~ \stemUp e8 r8 r2 }
    \pageBreak \stemUp e'2 ~ ^\markup{ \italic {div.} } \stemUp e8 r8 r4
    r4 \bar "||"
    \stemDown e4 ( _\mf ^\markup{ \italic {unis.} } \stemDown b'4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 ( \stemDown a8 \stemDown b8 }
    \stemDown a4 \stemDown g4 ) | % 18
    \stemDown fis8 -. r16 \stemDown e16 ( \stemDown fis8 ) -. r16
    \stemDown g16 ( \stemDown fis2. ) _\< | % 19
    \stemDown fis4 ( _\! _\markup{ \italic {più} } _ "" \stemDown d4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 ( \stemDown e8 \stemDown fis8 }
    \stemDown g4 \stemDown a4 ) | \barNumberCheck #20
    \stemDown a8 -. r16 \stemDown fis16 ( \stemDown g8 ) -. r16
    \stemDown a16 ( \stemDown g2. ) _\> \break | % 21
    \stemDown e4 ( _\! _\mf \stemDown b'4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 ( \stemDown a8 \stemDown b8 }
    \stemDown a4 \stemDown g4 ) \pageBreak | % 22
    \stemDown fis8 -. r16 \stemDown e16 ( \stemDown fis8 ) -. r16
    \stemDown g16 ( \stemDown fis2. ) _\< | % 23
    \stemDown fis4 ( _\! _\f \stemDown eis4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 ( \stemDown gis8 \stemDown fis8 }
    \stemDown cis4 ) \stemDown d4 -- | % 24
    \stemDown dis8 -. r16 \stemDown cisis16 ( \stemDown dis8 ) -. r16
    \stemDown eis16 ( \stemDown fis8 ) r8 r4 r4 | % 25
    r8 \stemUp a,8 -. _\p \stemDown a8 ( \stemDown a'8 ) \stemDown a,8 (
    \stemDown a'8 ) r4 r4 | % 26
    r8 \stemUp a,8 -. \stemDown a8 ( \stemDown a'8 ) \stemDown a,8 (
    \stemDown a'8 ) r4 r4 \break | % 27
    r8 \stemUp a,8 -. \stemDown a8 ( \stemDown a'8 ) \stemDown a,8 (
    \stemDown a'8 ) r4 r4 | % 28
    r8 \stemUp a,8 -. \stemDown a8 ( \stemDown a'8 ) \stemDown a,8 (
    \stemDown a'8 ) r4 r4 | % 29
    r8 \stemUp a,8 -. \stemDown a8 ( \stemDown a'8 ) \stemDown a,8 (
    \stemDown a'8 ) r4 r4 | \barNumberCheck #30
    r8 \stemUp a,8 -. \stemDown a8 ( \stemDown a'8 ) \stemDown a,8 (
    \stemDown fis'8 ) r4 r4 | % 31
    r8 \stemUp fis,8 -. _\< \stemUp fis8 ( \stemUp fis'8 ) \stemUp fis,8
    ( \stemUp fis'8 ) r4 _\! r4 \pageBreak | % 32
    r8 \stemUp a,8 ( _\mp _\< \stemDown e'8 ) -. \stemDown e8 -. \stemUp
    e,8 _\! _\mf r8 \stemDown a'8 ^\markup{ \italic {pizz.} } \stemDown
    g8 \stemDown fis8 \stemDown e8 | % 33
    \stemDown d8 \stemDown cis8 \stemDown b8 \stemDown bes8 \stemUp a8
    \stemUp gis8 \stemUp g8 \stemUp fis8 \stemUp e8 \stemUp es8 | % 34
    \stemUp d8 \stemUp e8 \stemUp fis8 \stemUp g8 \stemDown a8 \stemDown
    b8 \stemDown cis8 \stemDown d8 \stemDown e8 \stemDown eis8 | % 35
    \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown cis8 \stemUp b8
    \stemUp bes8 \stemUp a8 \stemUp gis8 \stemUp a8 r8 | % 36
    r2 r8 \stemUp g8 \stemUp fis8 \stemUp e8 \stemUp d8 \stemUp cis8
    \pageBreak | % 37
    r8 \stemUp cis8 \stemUp d8 \stemUp dis8 \stemUp e8 \stemUp fis8
    \stemUp g8 \stemUp gis8 \stemUp a8 \stemUp ais8 | % 38
    \stemDown b8 \stemDown cis8 \stemDown d8 \stemDown cis8 \stemUp d8
    \stemUp cis8 \stemUp b8 \stemUp ais8 \stemUp a8 \stemUp gis8 | % 39
    \stemUp fis8 _\< \stemUp gis8 \stemUp a8 \stemUp ais8 \stemDown b8
    \stemDown cis8 \stemDown d8 \stemDown e8 \stemDown eis8 \stemDown
    fis8 | \barNumberCheck #40
    \stemDown g8 _\! _\f _\> \stemDown fis8 \stemDown e8 \stemDown d8
    \stemUp cis8 \stemUp c8 \stemUp b8 \stemUp a8 \stemUp g8 r8
    \pageBreak | % 41
    \stemUp fis4 ( _\! _\mf ^\markup{ \italic {arco} } \stemUp g4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ( _\< \stemUp g8 \stemUp a8 }
    \stemUp b4 \stemDown cis4 ) \pageBreak | % 42
    \stemDown d4 ( _\! \stemUp b4 ) \stemDown cis2. _\> | % 43
    \stemUp a4 ( _\! _\mf \stemUp b4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis8 ( _\< \stemUp b8 \stemUp cis8 }
    \stemDown d4 \stemDown e4 ) | % 44
    \stemDown fis4 ( _\! \stemDown d4 ) \stemDown e2 ( \stemDown f4 ) | % 45
    \stemDown g2 ~ _\f _\> \stemDown g8 _\! _\mf \stemDown g8 ~
    \stemDown g8 \stemDown g8 ~ \stemDown g8 \stemDown g8 ~ | % 46
    \stemDown g2 ~ \stemDown g8 _\> \stemDown g4 \stemDown g4 \stemDown
    g8 ~ | % 47
    \stemDown g2 ~ _\! _\p _\< \stemDown g8 \stemDown g4 \stemDown g4
    \stemDown g8 ~ \pageBreak | % 48
    \stemDown g2 ~ \stemDown g8 \stemDown g8 ~ \stemDown g8 \stemDown g8
    ( \stemDown a8 ) \stemDown a8 ( | % 49
    \stemDown bes2 ) _\! _\f \stemDown a2 ( \stemDown g4 ) |
    \barNumberCheck #50
    \stemDown f4 -- \stemDown g4 -- \stemDown a2. | % 51
    \stemDown a2 \stemDown gis2 ( \stemDown fis4 ) | % 52
    \stemDown e4 -- \stemDown fis4 -- \stemDown gis2. \pageBreak | % 53
    \stemDown g4 ( \stemDown a4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 ( \stemDown a8 \stemDown g8 }
    \stemDown fis8 ) r8 \stemDown eis4 ( | % 54
    \stemDown fis8 ) r8 \stemDown d4 ( \stemUp e8 -> \stemUp d8 )
    \stemUp cis8 -. _\> \stemUp b8 -. \stemUp a8 -. \stemUp g8 -. | % 55
    \stemUp fis8 -. _\! _\mf r8 r4 r2 r4 | % 56
    \stemUp e8 _\f ^\markup{ \italic {pizz.} } r8 r4 \stemUp fis8 _\mf r8
    r4 r4 \repeat volta 2 {
        | % 57
        r4 \stemUp fis4 ( _\p ^\markup{ \italic {arco} } _\< \stemUp g2.
        ) _\! _\> | % 58
        r4 _\! \stemUp gis4 ( _\< \stemUp ais2. _\! _\> \pageBreak | % 59
        \stemUp b8 ) _\! r8 \stemUp b4 ( _\< \stemUp ais2. _\! _\> |
        \barNumberCheck #60
        \stemUp b8 ) _\! r8 \stemUp d,4 ( _\< \stemUp ais'2 _\! _\>
        \stemUp b4 ) | % 61
        r4 _\! \stemUp fis4 ( _\< \stemUp g2. ) _\! _\> | % 62
        r4 _\! \stemUp gis4 ( _\< \stemUp ais2. _\! _\> | % 63
        \stemUp b8 ) _\! r8 \stemUp b4 ( _\< \stemUp ais2. _\! _\> | % 64
        \stemUp b8 ) _\! r8 \stemUp d,4 ( _\< \stemUp g2 _\! _\> \stemUp
        fis4 ) }
    \pageBreak \repeat volta 2 {
        | % 65
        \stemDown fis'4. ( _\! _\p _\< \stemDown g8 ) -- \stemDown a2 (
        _\! \stemDown b4 ) | % 66
        \stemDown a4. ( _\> \stemDown g8 ) -- \stemDown fis2 ( -> _\!
        \stemDown e4 ) | % 67
        \stemDown e4. ( _\< \stemDown fis8 ) -- \stemDown g2 ( _\!
        \stemDown a4 ) | % 68
        \stemDown g4. ( _\> \stemDown fis8 ) -- \stemDown e2 ( -> _\!
        \stemDown d4 ) | % 69
        \stemDown d4. ( _\pp _\< \stemDown e8 ) -- \stemDown f2 ( ->
        \stemDown d4 | \barNumberCheck #70
        \stemDown es8 ) _\! r8 r4 r2 r4 \pageBreak | % 71
        \stemUp b4. ( _\mp _\< \stemDown cis8 ) -- \stemDown d2 ( ->
        \stemUp b4 ) | % 72
        \stemUp b2 ~ _\! _\f _\> \stemUp b2. }
    | % 73
    r4 _\! \stemUp fis4 ( _\p _\< \stemUp g2. ) _\! _\> | % 74
    r4 _\! \stemUp gis4 ( _\< \stemUp ais2. _\! _\> | % 75
    \stemUp b8 ) _\! r8 \stemUp b4 ( _\< \stemUp ais2. _\! _\> | % 76
    \stemUp b8 ) _\! r8 \stemUp d,4 ( _\< \stemUp ais'2 _\! _\> \stemUp
    b4 ) \pageBreak | % 77
    r4 _\! \stemUp fis4 ( _\p _\< \stemUp g2. ) _\! _\> | % 78
    r4 _\! \stemUp gis4 ( _\< \stemUp ais2. _\! _\> | % 79
    \stemUp b8 ) _\! r8 \stemUp b4 ( _\< \stemUp ais2. _\! _\> |
    \barNumberCheck #80
    \stemUp b8 ) _\! r8 \stemUp d,4 ( _\< \stemUp g2 _\! _\sf _\>
    \stemUp fis4 ) _\! | % 81
    \stemDown b'4. ( _\f \stemDown b8 ) -- \stemDown cis,2 ( _\> \stemUp
    b4 ) | % 82
    \stemDown fis'2 ~ _\! _\mf _\> \stemDown fis8 r8 _\! r4 r4
    \pageBreak | % 83
    \stemDown g4. ( _\f \stemDown g8 ) -- \stemUp b,2 ( _\> \stemUp ais4
    ) | % 84
    \stemDown d2 ~ _\! _\mf _\> \stemDown d8 r8 _\! r4 r4 | % 85
    \stemDown b'4. ( _\f \stemDown b8 ) -- \stemDown cis,2 ( _\> \stemUp
    b4 ) | % 86
    \stemDown fis'2 ~ _\! _\mf _\> \stemDown fis8 r8 _\! r4 r4 | % 87
    \stemDown g4. ( _\f \stemDown g8 ) -- \stemUp b,2 ( _\> \stemUp ais4
    ) | % 88
    \stemDown d2 ~ _\! _\mf _\> \stemDown d8 r8 _\! r4 r4 \pageBreak | % 89
    \stemDown c4 ( _\p _\< \stemDown d4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown d8 \stemDown e8 }
    \stemDown fis4 \stemDown g4 ) | \barNumberCheck #90
    \stemDown gis2 ~ _\! _\mf _\> \stemDown gis8 r8 _\! r4 r4 | % 91
    \stemUp gis,4 ( _\p _\< \stemUp ais4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp ais8 \stemUp b8 }
    \stemDown cis4 \stemDown d4 ) | % 92
    \stemDown d2 ~ _\! _\mf _\> \stemDown d8 r8 _\! r4 r4 | % 93
    \stemUp <c, c'>4 ( _\p ^\markup{ \italic {div.} } _\< \stemUp <d d'>4
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <d d'>8 \stemUp <e e'>8 }
    \stemUp <fis fis'>4 \stemDown <g g'>4 ) | % 94
    \stemDown <gis gis'>2 ~ ~ _\! _\mf _\> \stemDown <gis gis'>8 r8 _\!
    r4 r4 \pageBreak | % 95
    R4*5 | % 96
    \stemUp d8 _\mf ^\markup{ \italic {unis.} } ^\markup{ \italic
        {pizz.} } r8 r4 r2 r4 | % 97
    \stemUp <d a'>8 r8 r4 \stemUp <e a>8 r8 r4 r4 | % 98
    \stemUp <d a'>8 r8 r4 r2 r4 | % 99
    \stemUp <d a'>8 r8 r4 \stemUp <e a>8 r8 r4 r4 | \barNumberCheck #100
    \stemUp <e b'>8 r8 r4 r2 r4 \pageBreak | % 101
    \stemUp <d fis>8 ^\markup{ \italic {div.} } r8 r4 r2 r4 | % 102
    \stemDown <fis d' b'>8 r8 r4 \stemUp <e b' gis'>8 r8 r4 r4 | % 103
    \stemUp <e a>8 _\f r8 r4 r2 \stemUp cis8 _\sf r8 | % 104
    \stemUp d8 r8 \stemDown <a' d a'>8 r8 r2 r4 | % 105
    \stemUp <d, a'>8 r8 r4 \stemUp <e a>8 r8 r4 r4 \break | % 106
    \stemUp <d a'>8 r8 \stemUp a'8 r8 r2 r4 | % 107
    \stemUp <d, a'>8 r8 \stemUp a'8 r8 r4 \stemUp a8 r8 r4 | % 108
    r4 \stemUp g8 _\markup{ \italic {sempre} } _ "" r8 r4 \stemUp fis2
    ^\markup{ \italic {arco} } | % 109
    \stemUp fis2 ~ \stemUp fis2. | \barNumberCheck #110
    r4 \stemUp fis8 ^\markup{ \italic {pizz.} } r8 r4 \stemUp e2
    ^\markup{ \italic {arco} } \pageBreak | % 111
    \stemUp e'2 ~ ^\markup{ \italic {div.} } \stemUp e8 r8 r4 r4 | % 112
    \stemDown e4 ( _\mf ^\markup{ \italic {unis.} } \stemDown b'4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 ( \stemDown a8 \stemDown b8 }
    \stemDown a4 \stemDown g4 ) | % 113
    \stemDown fis8 -. r16 \stemDown e16 ( \stemDown fis8 ) -. r16
    \stemDown g16 ( \stemDown fis2. ) _\< | % 114
    \stemDown fis4 ( _\! _\markup{ \italic {più} } _ "" \stemDown d4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 ( \stemDown e8 \stemDown fis8 }
    \stemDown g4 \stemDown a4 ) | % 115
    \stemDown a8 -. r16 \stemDown fis16 ( \stemDown g8 ) -. r16
    \stemDown a16 ( \stemDown g2. ) _\> \break | % 116
    \stemDown e4 ( _\! _\mf \stemDown b'4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 ( \stemDown a8 \stemDown b8 }
    \stemDown a4 \stemDown g4 ) \pageBreak | % 117
    \stemDown fis8 -. r16 \stemDown e16 ( \stemDown fis8 ) -. r16
    \stemDown g16 ( \stemDown fis2. ) _\< | % 118
    \stemDown fis4 ( _\! _\f \stemDown eis4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 ( \stemDown gis8 \stemDown fis8 }
    \stemDown cis4 ) \stemDown d4 -- | % 119
    \stemDown dis8 -. r16 \stemDown cisis16 ( \stemDown dis8 ) -. r16
    \stemDown eis16 ( \stemDown fis8 ) r8 r4 r4 | \barNumberCheck #120
    r8 \stemUp a,8 -. _\p \stemDown a8 ( \stemDown a'8 ) \stemDown a,8 (
    \stemDown a'8 ) r4 r4 | % 121
    r8 \stemUp a,8 -. \stemDown a8 ( \stemDown a'8 ) \stemDown a,8 (
    \stemDown a'8 ) r4 r4 \break | % 122
    r8 \stemUp a,8 -. \stemDown a8 ( \stemDown a'8 ) \stemDown a,8 (
    \stemDown a'8 ) r4 r4 \pageBreak | % 123
    r8 \stemUp a,8 -. \stemDown a8 ( \stemDown a'8 ) \stemDown a,8 (
    \stemDown a'8 ) r4 r4 | % 124
    r8 \stemUp a,8 -. \stemDown a8 ( \stemDown a'8 ) \stemDown a,8 (
    \stemDown a'8 ) r4 r4 | % 125
    r8 \stemUp a,8 -. \stemDown a8 ( \stemDown a'8 ) \stemDown a,8 (
    \stemDown fis'8 ) r4 r4 | % 126
    r8 \stemUp fis,8 -. _\< \stemUp fis8 ( \stemUp fis'8 ) \stemUp fis,8
    ( \stemUp fis'8 ) r4 _\! r4 | % 127
    r8 \stemUp a,8 ( _\mp _\< \stemDown e'8 ) -. \stemDown e8 -. \stemUp
    e,8 _\! _\mf r8 \stemDown a'8 _\mf ^\markup{ \italic {pizz.} }
    \stemDown g8 \stemDown fis8 \stemDown e8 \pageBreak | % 128
    \stemDown d8 \stemDown cis8 \stemDown b8 \stemDown bes8 \stemUp a8
    \stemUp gis8 \stemUp g8 \stemUp fis8 \stemUp e8 \stemUp es8 | % 129
    \stemUp d8 \stemUp e8 \stemUp fis8 \stemUp g8 \stemDown a8 \stemDown
    b8 \stemDown cis8 \stemDown d8 \stemDown e8 \stemDown eis8 |
    \barNumberCheck #130
    \stemDown fis8 \stemDown e8 \stemDown d8 \stemDown cis8 \stemUp b8
    \stemUp bes8 \stemUp a8 \stemUp gis8 \stemUp a8 r8 | % 131
    r2 r8 \stemUp g8 \stemUp fis8 \stemUp e8 \stemUp d8 \stemUp cis8 | % 132
    r8 \stemUp cis8 \stemUp d8 \stemUp dis8 \stemUp e8 \stemUp fis8
    \stemUp g8 \stemUp gis8 \stemUp a8 \stemUp ais8 \pageBreak | % 133
    \stemDown b8 \stemDown cis8 \stemDown d8 \stemDown cis8 \stemUp d8
    \stemUp cis8 \stemUp b8 \stemUp ais8 \stemUp a8 \stemUp gis8 | % 134
    \stemUp fis8 _\< \stemUp gis8 \stemUp a8 \stemUp ais8 \stemDown b8
    \stemDown cis8 \stemDown d8 \stemDown e8 \stemDown eis8 \stemDown
    fis8 | % 135
    \stemDown g8 _\! _\f _\> \stemDown fis8 \stemDown e8 \stemDown d8
    \stemUp cis8 \stemUp c8 \stemUp b8 \stemUp a8 \stemUp g8 r8 | % 136
    \stemUp fis4 ( _\! _\mf ^\markup{ \italic {arco} } \stemUp g4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 ( _\< \stemUp g8 \stemUp a8 }
    \stemUp b4 \stemDown cis4 ) | % 137
    \stemDown d4 ( _\! \stemUp b4 ) \stemDown cis2. _\> \pageBreak | % 138
    \stemUp a4 ( _\! _\mf \stemUp b4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis8 ( _\< \stemUp b8 \stemUp cis8 }
    \stemDown d4 \stemDown e4 ) | % 139
    \stemDown fis4 ( _\! \stemDown d4 ) \stemDown e2 ( \stemDown f4 ) |
    \barNumberCheck #140
    \stemDown g2 ~ _\f _\> \stemDown g8 _\! _\mf \stemDown g8 ~
    \stemDown g8 \stemDown g8 ~ \stemDown g8 \stemDown g8 ~ | % 141
    \stemDown g2 ~ \stemDown g8 _\> \stemDown g4 \stemDown g4 \stemDown
    g8 ~ | % 142
    \stemDown g2 ~ _\! _\p _\< \stemDown g8 \stemDown g4 \stemDown g4
    \stemDown g8 ~ \pageBreak | % 143
    \stemDown g2 ~ \stemDown g8 \stemDown g8 ~ \stemDown g8 \stemDown g8
    ( \stemDown a8 ) \stemDown a8 ( | % 144
    \stemDown bes2 ) _\! _\f \stemDown a2 ( \stemDown g4 ) | % 145
    \stemDown f4 -- \stemDown g4 -- \stemDown a2. | % 146
    \stemDown a2 \stemDown gis2 ( \stemDown fis4 ) | % 147
    \stemDown e4 -- \stemDown fis4 -- \stemDown gis2. \pageBreak | % 148
    \stemDown g4 ( \stemDown a4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 ( \stemDown a8 \stemDown g8 }
    \stemDown fis8 ) r8 \stemDown eis4 ( | % 149
    \stemDown fis8 ) r8 \stemDown d4 ( \stemUp e8 -> \stemUp d8 )
    \stemUp cis8 -. _\> \stemUp b8 -. \stemUp a8 -. \stemUp g8 -. |
    \barNumberCheck #150
    \stemUp fis8 -. _\! _\mf r8 r4 r2 r4 | % 151
    \stemUp e8 _\f ^\markup{ \italic {pizz.} } r8 r4 \stemUp fis8 _\mf r8
    r4 r4 | % 152
    R4*5 | % 153
    \stemUp d4 ( _\mf ^\markup{ \italic {arco} } \stemUp e4 \stemUp fis4
    \stemUp g4 \stemUp a4 ) \pageBreak | % 154
    R4*5 | % 155
    \stemUp g4 ( _\mf \stemUp a4 \stemUp b4 \stemDown cis4 \stemDown d4
    ) | % 156
    R4*5 | % 157
    \stemUp d,4 ( _\p \stemUp e4 \stemUp fis4 \stemUp g4 \stemUp a4 ) | % 158
    R4*5 | % 159
    \stemUp g4 ( _\p \stemUp a4 \stemUp b4 \stemDown cis4 \stemDown d4 )
    | \barNumberCheck #160
    \stemUp d,4 -- _\mf _\> \stemUp d4 -- \stemUp d4 -- \stemUp d4 --
    \stemUp d4 -- | % 161
    \stemUp d4 -- _\! _\p \stemUp d4 -- \stemUp d4 -- \stemUp d4 --
    \stemUp d4 -- | % 162
    \stemUp d4 -- _\mf _\> \stemUp d4 -- \stemUp d4 -- \stemUp d4 --
    \stemUp d4 -- \pageBreak | % 163
    \stemUp d4 -- _\! _\p \stemUp d4 -- \stemUp d4 -- \stemUp d4 --
    \stemUp d4 -- | % 164
    \stemUp f2 ~ _\p \stemUp f2. | % 165
    \stemUp g2 ~ _\markup{ \italic {poco cresc.} } \stemUp g2. | % 166
    \stemUp gis2 ~ \stemUp gis2. | % 167
    \stemUp fis2 ~ _\mf \stemUp fis2. | % 168
    \stemUp a2 ~ _\markup{ \italic {dim.} } \stemUp a2. | % 169
    \stemUp <g e'>2 ~ ~ _\mp _\> \stemUp <g e'>2. | \barNumberCheck #170
    \stemUp gis2 ~ _\! _\p _\> \stemUp gis2. \break | % 171
    \stemUp fis2 ~ _\! _\pp \stemUp fis2. | % 172
    R4*5 | % 173
    \stemUp fis2 ~ _\pp \stemUp fis2. | % 174
    R4*5 | % 175
    \stemUp fis2 ~ _\pp \stemUp fis2. | % 176
    \stemUp fis2 ~ \stemUp fis2. | % 177
    r2 \stemDown d'8 _\pp ^\markup{ \italic {pizz.} } r8 r2 \pageBreak | % 178
    \stemUp fis,8 _\pp r8 r4 r2 r4 ^\fermata \bar "|."
    }

PartPOneFourVoiceTwo =  \relative d {
    \repeat volta 2 {
        \clef "alto" \time 5/4 \key d \major s4*25 \pageBreak | % 6
        \stemDown d8 s8*49 \break s4*5 \pageBreak s4*25 }
    \pageBreak | % 16
    \stemDown e2 ~ \stemDown e8 s8*5 \bar "||"
    s1*5 \break s4*5 \pageBreak s4*25 \break s4*25 \pageBreak s4*25
    \pageBreak s1*5 \pageBreak s4*5 \pageBreak s2*15 \pageBreak s4*25
    \pageBreak s1*5 \repeat volta 2 {
        s2*5 \pageBreak s2*15 }
    \pageBreak \repeat volta 2 {
        s2*15 \pageBreak s2*5 }
    s1*5 \pageBreak s2*15 \pageBreak s2*15 \pageBreak s2*15 \pageBreak
    s2*15 \pageBreak s4*25 \break s4*25 \pageBreak | % 111
    \stemDown e2 ~ \stemDown e8 s8*45 \break s4*5 \pageBreak s4*25
    \break s4*5 \pageBreak s4*25 \pageBreak s4*25 \pageBreak s4*25
    \pageBreak s4*25 \pageBreak s4*25 \pageBreak s2*15 \pageBreak s4*45
    \pageBreak s1*10 \break s4*35 \pageBreak s4*5 \bar "|."
    }

PartPOneFiveVoiceOne =  \relative fis {
    \repeat volta 2 {
        \clef "bass" \time 5/4 \key d \major | % 1
        \stemDown fis4 ( _\mf \stemDown g4 ) \once \omit TupletBracket
        \times 2/3  {
            \stemDown a8 ( _\< \stemDown g8 \stemDown a8 }
        \stemDown b4 \stemDown cis4 ) | % 2
        \stemDown d4 ( _\! \stemDown b4 ) \stemDown cis2. _\> | % 3
        \stemDown a4 ( _\! _\mf \stemDown b4 ) \once \omit TupletBracket
        \times 2/3  {
            \stemDown cis8 ( _\< \stemDown b8 \stemDown cis8 }
        \stemDown d4 \stemDown e4 ) | % 4
        \clef "tenor" \stemDown fis4 ( _\! _\f \stemDown d4 ) \stemDown
        e2. | % 5
        \stemDown g4 ( \stemDown fis4 ) \once \omit TupletBracket
        \times 2/3  {
            \stemDown e8 ( \stemDown fis8 \stemDown e8 }
        \stemDown d4 \stemDown cis4 ) \pageBreak | % 6
        \stemDown fis8 -. r16 \stemDown g16 ( \stemDown fis8 ) r16
        \stemDown eis16 ( \stemDown fis2. ) | % 7
        \stemDown fis4 ( \stemDown e4 ) \once \omit TupletBracket
        \times 2/3  {
            \stemDown d8 ( \stemDown e8 \stemDown d8 }
        \stemDown cis4 ) \stemDown b4 ( \glissando _\< | % 8
        \stemDown b'8 ) _\! _\ff _\> \stemDown a8 ( \stemDown g8 )
        \stemDown fis8 -. \stemDown e8 -. \stemDown es8 ( -. \stemDown d8
        -. \stemDown cis8 -. \stemDown b8 -. \stemDown bes8 ) -. | % 9
        \stemDown a4 ( _\! _\mf \stemUp g4 ) \stemUp fis4 ( \stemUp f4
        \stemUp e4 ) | \barNumberCheck #10
        \stemUp fis4 ( \stemUp g4 \stemDown a8 ) r8 \stemDown b8 ( -.
        _\< \stemDown cis8 -. \stemDown d8 -. \stemDown e8 ) -. \break | % 11
        \stemDown fis4 ( _\! \stemDown f4 ) \stemDown e4 ( _\> \stemDown
        d4 \stemDown cis4 ) \pageBreak | % 12
        \stemDown d4 ( _\! _\< \stemDown fis4 \stemDown a8 ) r8 _\!
        \stemDown g8 ( -. _\> \stemDown fis8 -. \stemDown e8 -.
        \stemDown d8 ) -. | % 13
        \stemDown cis2 ~ _\! _\markup{ \italic {sempre} } _ ""
        \stemDown cis8 r8 \stemDown d4 ( _\< \stemDown e4 ) | % 14
        \stemDown fis4 ( _\! _\> \stemDown d4 \stemDown b8 ) r8 _\!
        \stemUp fis8 ( -. \stemUp gis8 -. \stemUp a8 -. \stemUp ais8 )
        -. | % 15
        \stemDown b2 ~ \stemDown b8 r8 \stemDown cis4 ( _\< \stemDown d4
        ) | % 16
        \stemDown e4 ( _\! _\> \stemDown cis4 \stemUp a8 ) \stemUp a8 (
        _\! \stemUp b8 \stemUp a8 \stemUp gis8 \stemUp g8 ) }
    \pageBreak \stemDown e'4 ( _\> \stemDown cis4 \stemDown a8 ) r8 _\!
    r2 \bar "||"
    \stemDown cis4 ( _\mf ^\markup{ \italic {unis.} } \stemDown g'4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 ( \stemDown fis8 \stemDown g8 }
    \stemDown fis4 \stemDown e4 ) | % 18
    \stemDown d8 -. r16 \stemDown cis16 ( \stemDown d8 ) -. r16
    \stemDown e16 ( \stemDown d2. ) _\< | % 19
    \stemDown d4 ( _\! _\markup{ \italic {più} } _ "" \stemDown b4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 ( \stemDown cis8 \stemDown d8 }
    \stemDown e4 \stemDown fis4 ) | \barNumberCheck #20
    \stemDown fis8 -. r16 \stemDown d16 ( \stemDown e8 ) -. r16
    \stemDown fis16 ( \stemDown e2. ) _\> \break | % 21
    \stemDown cis4 ( _\! _\mf \stemDown g'4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 ( \stemDown fis8 \stemDown g8 }
    \stemDown fis4 \stemDown e4 ) \pageBreak | % 22
    \stemDown d8 -. r16 \stemDown cis16 ( \stemDown d8 ) -. r16
    \stemDown e16 ( \stemDown d2. ) _\< | % 23
    \stemDown dis4 ( _\! _\f \stemDown cis4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown dis8 ( \stemDown eis8 \stemDown dis8 }
    \stemDown a4 ) \stemDown b4 -- | % 24
    \stemDown cis8 -. r16 \stemDown b16 ( \stemDown cis8 ) -. r16
    \stemDown b16 ( \stemDown a8 ) r8 r4 r4 | % 25
    \clef "bass" \stemUp a,8 -. _\p \stemUp a8 -. \stemDown a8 (
    \stemDown a'8 ) r4 \stemUp a,4 ( \stemUp cis4 | % 26
    \stemUp a8 ) -. \stemUp a8 -. \stemDown a8 ( \stemDown a'8 ) r4
    \stemUp a,4 ( \stemDown d4 \break | % 27
    \stemUp a8 ) -. \stemUp a8 -. \stemDown a8 ( \stemDown a'8 ) r4
    \stemUp a,4 ( \stemDown d4 | % 28
    \stemUp a8 ) -. \stemUp a8 -. \stemDown a8 ( \stemDown a'8 ) r4
    \stemUp a,4 ( \stemUp cis4 | % 29
    \stemUp a8 ) -. \stemUp a8 -. \stemDown a8 ( \stemDown a'8 ) r4
    \stemUp a,4 ( \stemUp cis4 | \barNumberCheck #30
    \stemUp a8 ) -. \stemUp a8 -. \stemDown a8 ( \stemDown a'8 ) r4
    \stemUp a,4 ( _\< \stemUp b4 | % 31
    \stemUp cis8 ) -. \stemUp fis,8 -. \stemUp fis8 ( \stemUp fis'8 ) r4
    _\! \stemUp cis4 ( _\< \stemDown d4 ) \pageBreak | % 32
    \stemDown dis4 ( \stemDown e4 \stemUp a,8 ) _\! _\mf r8 r4 r4 | % 33
    \stemUp d,8 _\mf ^\markup{ \italic {pizz.} } r8 r4 \stemDown d'8 r8
    r4 r4 | % 34
    \stemDown fis8 r8 \stemDown d8 r8 \stemUp a8 r8 r4 r4 | % 35
    \stemDown d8 r8 r4 \stemUp fis,8 r8 \stemUp fis8 r8 \stemUp cis'8 r8
    | % 36
    \stemDown d8 r8 \stemDown fis8 r8 \stemDown e4 ~ ^\markup{ \italic
        {arco} } \stemDown e8 r8 r4 \pageBreak | % 37
    \stemUp <b e>8 _\p ^\markup{ \italic {pizz.} } r8 r4 \stemUp <g g'>8
    r8 \stemDown e'8 r8 \stemDown e8 r8 | % 38
    \stemDown d8 r8 \stemUp b8 r8 \stemDown fis'4 ~ ^\markup{ \italic
        {arco} } \stemDown fis8 r8 r4 | % 39
    \stemDown d4 ^\markup{ \italic {pizz.} } _\< \stemUp cis4 \stemUp b4
    r4 _\! r4 | \barNumberCheck #40
    \stemUp a2 ~ _\f ^\markup{ \italic {arco} } _\> \stemUp a8 r8 _\! r4
    r4 \pageBreak | % 41
    \stemDown d8 -. _\mf \stemDown d8 -. \stemDown d'8 -. \stemDown d8
    -. r4 \stemDown d,4 \stemDown e4 \pageBreak | % 42
    \stemDown fis8 -. \stemDown fis8 -. \stemDown d8 -. \stemDown d8 -.
    \stemDown a'8 -. r8 r4 r4 | % 43
    \stemDown fis8 -. \stemDown fis8 -. \stemDown fis'8 -. \stemDown fis8
    -. r4 \stemDown fis,4 \stemDown e4 | % 44
    \stemDown d8 -. _\< \stemDown d8 -. \stemDown fis8 -. \stemDown fis8
    -. \stemDown a2 \stemDown as4 | % 45
    \stemUp g8 -. _\! _\f _\> \stemUp g8 -. \stemUp g,8 -. \stemUp g8 -.
    \stemDown g'2. ~ _\! _\mf | % 46
    \stemUp g8 \stemUp g8 -. \stemUp g,8 -. \stemUp g8 -. \stemDown g'2.
    ~ _\> | % 47
    \stemUp g8 _\! _\p _\< \stemUp g8 -. \stemUp g,8 -. \stemUp g8 -.
    \stemDown g'2. ~ \pageBreak | % 48
    \stemUp g8 \stemUp g8 -. \stemUp g,8 -. \stemUp g8 -. \stemDown g'2
    \stemDown fis4 | % 49
    \stemUp f8 -. _\! _\f \stemUp f8 -. \stemUp f,8 -. \stemUp f8 -.
    \stemUp f'8 -. \stemUp f8 -. \stemUp f,8 -. \stemUp f8 -. \stemUp f'8
    -. \stemUp f8 -. | \barNumberCheck #50
    \stemUp f,8 -. \stemUp f8 -. \stemUp f'8 -. \stemUp f8 -. \stemUp f,8
    -. \stemUp f8 -. \stemUp f'8 -. \stemUp f8 -. \stemUp f,8 -. \stemUp
    f8 -. | % 51
    \stemUp e'8 -. \stemUp e8 -. \stemUp e,8 -. \stemUp e8 -. \stemUp e'8
    -. \stemUp e8 -. \stemUp e,8 -. \stemUp e8 -. \stemUp e'8 -. \stemUp
    e8 -. | % 52
    \stemUp e,8 -. \stemUp e8 -. \stemUp e'8 -. \stemUp e8 -. \stemUp e,8
    -. \stemUp e8 -. \stemUp e'8 -. \stemUp e8 -. \stemUp e,8 -. \stemUp
    e8 -. \pageBreak | % 53
    \stemDown es'2 ~ \stemDown es2. | % 54
    \stemDown d4 \stemDown fis4 ( \stemDown g8 ) r8 r4 r4 | % 55
    \stemUp a,8 -. _\mf r8 r4 r2 r4 | % 56
    \stemUp a8 _\f ^\markup{ \italic {pizz.} } r8 r4 \stemUp <a d>8 _\mf
    r8 r4 r4 \repeat volta 2 {
        | % 57
        \clef "tenor" \stemDown fis''4. ( _\p ^\markup{ \italic {arco} }
        _\< \stemDown fis8 ) -- \stemDown fis2 ( _\! _\> \stemDown e4 )
        | % 58
        \stemDown d4. ( _\! _\< \stemDown d8 ) -- \stemDown d2 ( _\! _\>
        \stemDown cis4 ) \pageBreak | % 59
        \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemDown d2 ( _\!
        _\> \stemDown cis4 ) | \barNumberCheck #60
        \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemUp g2 ( _\!
        _\> \stemUp fis4 ) | % 61
        \stemDown fis'4. ( -- _\! _\< \stemDown fis8 ) -- \stemDown fis2
        ( _\! _\> \stemDown e4 ) | % 62
        \stemDown d4. ( -- _\! _\< \stemDown d8 ) -- \stemDown d2 ( _\!
        _\> \stemDown cis4 ) | % 63
        \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemDown d2 ( _\!
        _\> \stemDown cis4 ) | % 64
        \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemDown g'2 ( _\!
        _\sf _\> \stemDown fis4 ) }
    \pageBreak \repeat volta 2 {
        | % 65
        \clef "bass" \stemDown d,4 -- _\! _\p \stemDown d4 -- \stemDown
        d4 -- \stemDown d4 -- \stemDown d4 -- | % 66
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- | % 67
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- | % 68
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- | % 69
        \stemDown d4 -- _ "" _\markup{ \italic {cresc.} } \stemDown d4
        -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- |
        \barNumberCheck #70
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- \pageBreak | % 71
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- | % 72
        \stemDown d4 -- _\f _\> \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- \stemDown d4 -- }
    | % 73
    \clef "tenor" \stemDown fis'4. ( _\! _\p ^\markup{ \italic {arco} }
    _\< \stemDown fis8 ) -- \stemDown fis2 ( _\! _\> \stemDown e4 ) | % 74
    \stemDown d4. ( _\! _\< \stemDown d8 ) -- \stemDown d2 ( _\! _\>
    \stemDown cis4 ) | % 75
    \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemDown d2 ( _\! _\>
    \stemDown cis4 ) | % 76
    \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemUp g2 ( _\! _\>
    \stemUp fis4 ) \pageBreak | % 77
    \stemDown fis'4. ( -- _\! _\< \stemDown fis8 ) -- \stemDown fis2 (
    _\! _\> \stemDown e4 ) | % 78
    \stemDown d4. ( -- _\! _\< \stemDown d8 ) -- \stemDown d2 ( _\! _\>
    \stemDown cis4 ) | % 79
    \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemDown d2 ( _\! _\>
    \stemDown cis4 ) | \barNumberCheck #80
    \stemDown b4. ( -- _\! _\< \stemDown b8 ) -- \stemDown g'2 ( _\!
    _\sf _\> \stemDown fis4 ) _\! | % 81
    \clef "bass" \stemDown d,4 -- _\f \stemDown d4 -- \stemDown d4 --
    _\> \stemDown d4 -- \stemDown d4 -- | % 82
    \stemDown d2 ~ _\! _\mf _\> \stemDown d8 r8 _\! r4 r4 \pageBreak | % 83
    \stemDown d4 -- _\f \stemDown d4 -- \stemDown d4 -- _\> \stemDown d4
    -- \stemDown d4 -- | % 84
    \stemDown d2 ~ _\! _\mf _\> \stemDown d8 r8 _\! r4 r4 | % 85
    \stemDown d4 -- _\f \stemDown d4 -- \stemDown d4 -- _\> \stemDown d4
    -- \stemDown d4 -- | % 86
    \stemDown d2 ~ _\! _\mf _\> \stemDown d8 r8 _\! r4 r4 | % 87
    \stemDown d4 -- _\f \stemDown d4 -- \stemDown d4 -- _\> \stemDown d4
    -- \stemDown d4 -- | % 88
    \stemDown d2 ~ _\! _\mf _\> \stemDown d8 r8 _\! r4 r4 \pageBreak | % 89
    \stemDown d2 ~ _\mf _\> \stemDown d8 r8 _\! r4 r4 | \barNumberCheck
    #90
    \stemDown d2 ~ _\mf _\> \stemDown d8 r8 _\! r4 r4 | % 91
    \stemDown d2 ~ _\mf _\> \stemDown d8 r8 _\! r4 r4 | % 92
    \stemDown d2 ~ _\mf _\> \stemDown d8 r8 _\! r4 r4 | % 93
    \stemUp c4 ( _\p _\< \stemDown d4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown d8 \stemDown e8 }
    \stemDown fis4 \stemDown g4 ) | % 94
    \stemDown gis2 ~ _\! _\mf _\> \stemDown gis8 r8 _\! r4 r4 \pageBreak
    | % 95
    \stemUp a,4 ( _\p _\< \stemUp b4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis8 \stemUp b8 \stemUp cis8 }
    \stemDown d4 \stemDown e4 ) | % 96
    \stemDown fis4 ( _\! _\mf \stemDown g4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 ( _\< \stemDown g8 \stemDown a8 }
    \stemDown b4 \stemDown cis4 ) | % 97
    \clef "tenor" \stemDown d4 ( _\! \stemDown b4 ) \stemDown cis2. _\>
    | % 98
    \stemDown a4 ( _\! _\mf \stemDown b4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( _\< \stemDown b8 \stemDown cis8 }
    \stemDown d4 \stemDown e4 ) | % 99
    \stemDown fis4 ( _\! \stemDown d4 ) \stemDown e2. | \barNumberCheck
    #100
    \stemDown g4 ( _\f \stemDown fis4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( \stemDown fis8 \stemDown e8 }
    \stemDown d4 \stemDown cis4 ) \pageBreak | % 101
    \stemDown fis8 -. r16 \stemDown g16 ( \stemDown fis8 ) r16 \stemDown
    eis16 ( \stemDown fis2. ) | % 102
    \stemDown fis4 ( \stemDown e4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 ( \stemDown e8 \stemDown d8 }
    \stemDown cis4 ) \stemDown b4 ( \glissando _\< | % 103
    \stemDown b'8 ) _\! _\ff _\> \stemDown a8 ( \stemDown g8 ) \stemDown
    fis8 -. \stemDown e8 -. \stemDown es8 ( -. \stemDown d8 -. \stemDown
    cis8 -. \stemDown b8 -. \stemDown bes8 ) -. | % 104
    \stemDown a4 ( _\! _\mf \stemUp g4 ) \stemUp fis4 ( \stemUp f4
    \stemUp e4 ) | % 105
    \stemUp fis4 ( \stemUp g4 \stemDown a8 ) r8 \stemDown b8 ( -. _\<
    \stemDown cis8 -. \stemDown d8 -. \stemDown e8 ) -. \break | % 106
    \stemDown fis4 ( _\! \stemDown f4 ) \stemDown e4 ( _\> \stemDown d4
    \stemDown cis4 ) | % 107
    \stemDown d4 ( _\! _\< \stemDown fis4 \stemDown a8 ) r8 _\!
    \stemDown g8 ( -. _\> \stemDown fis8 -. \stemDown e8 -. \stemDown d8
    ) -. | % 108
    \stemDown cis2 ~ _\! _\markup{ \italic {sempre} } _ "" \stemDown
    cis8 r8 \stemDown d4 ( _\< \stemDown e4 ) | % 109
    \stemDown fis4 ( _\! _\> \stemDown d4 \stemDown b8 ) r8 _\! \stemUp
    fis8 ( -. \stemUp gis8 -. \stemUp a8 -. \stemUp ais8 ) -. |
    \barNumberCheck #110
    \stemDown b2 ~ \stemDown b8 r8 \stemDown cis4 ( _\< \stemDown d4 )
    \pageBreak | % 111
    \stemDown e4 ( _\! _\> \stemDown cis4 \stemDown a8 ) r8 _\! r2 | % 112
    \stemDown cis4 ( _\mf ^\markup{ \italic {unis.} } \stemDown g'4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 ( \stemDown fis8 \stemDown g8 }
    \stemDown fis4 \stemDown e4 ) | % 113
    \stemDown d8 -. r16 \stemDown cis16 ( \stemDown d8 ) -. r16
    \stemDown e16 ( \stemDown d2. ) _\< | % 114
    \stemDown d4 ( _\! _\markup{ \italic {più} } _ "" \stemDown b4 )
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 ( \stemDown cis8 \stemDown d8 }
    \stemDown e4 \stemDown fis4 ) | % 115
    \stemDown fis8 -. r16 \stemDown d16 ( \stemDown e8 ) -. r16
    \stemDown fis16 ( \stemDown e2. ) _\> \break | % 116
    \stemDown cis4 ( _\! _\mf \stemDown g'4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 ( \stemDown fis8 \stemDown g8 }
    \stemDown fis4 \stemDown e4 ) \pageBreak | % 117
    \stemDown d8 -. r16 \stemDown cis16 ( \stemDown d8 ) -. r16
    \stemDown e16 ( \stemDown d2. ) _\< | % 118
    \stemDown dis4 ( _\! _\f \stemDown cis4 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown dis8 ( \stemDown eis8 \stemDown dis8 }
    \stemDown a4 ) \stemDown b4 -- | % 119
    \stemDown cis8 -. r16 \stemDown b16 ( \stemDown cis8 ) -. r16
    \stemDown b16 ( \stemDown a8 ) r8 r4 r4 | \barNumberCheck #120
    \clef "bass" \stemUp a,8 -. _\p \stemUp a8 -. \stemDown a8 (
    \stemDown a'8 ) r4 \stemUp a,4 ( \stemUp cis4 | % 121
    \stemUp a8 ) -. \stemUp a8 -. \stemDown a8 ( \stemDown a'8 ) r4
    \stemUp a,4 ( \stemDown d4 \break | % 122
    \stemUp a8 ) -. \stemUp a8 -. \stemDown a8 ( \stemDown a'8 ) r4
    \stemUp a,4 ( \stemDown d4 \pageBreak | % 123
    \stemUp a8 ) -. \stemUp a8 -. \stemDown a8 ( \stemDown a'8 ) r4
    \stemUp a,4 ( \stemUp cis4 | % 124
    \stemUp a8 ) -. \stemUp a8 -. \stemDown a8 ( \stemDown a'8 ) r4
    \stemUp a,4 ( \stemUp cis4 | % 125
    \stemUp a8 ) -. \stemUp a8 -. \stemDown a8 ( \stemDown a'8 ) r4
    \stemUp a,4 ( _\< \stemUp b4 | % 126
    \stemUp cis8 ) -. \stemUp fis,8 -. \stemUp fis8 ( \stemUp fis'8 ) r4
    _\! \stemUp cis4 ( _\< \stemDown d4 ) | % 127
    \stemDown dis4 ( \stemDown e4 \stemUp a,8 ) _\! _\mf r8 r4 r4
    \pageBreak | % 128
    \stemUp d,8 _\mf ^\markup{ \italic {pizz.} } r8 r4 \stemDown d'8 r8
    r4 r4 | % 129
    \stemDown fis8 r8 \stemDown d8 r8 \stemUp a8 r8 r4 r4 |
    \barNumberCheck #130
    \stemDown d8 r8 r4 \stemUp fis,8 r8 \stemUp fis8 r8 \stemUp cis'8 r8
    | % 131
    \stemDown d8 r8 \stemDown fis8 r8 \stemDown e4 ~ ^\markup{ \italic
        {arco} } \stemDown e8 r8 r4 | % 132
    \stemUp <b e>8 _\p ^\markup{ \italic {pizz.} } r8 r4 \stemUp <g g'>8
    r8 \stemDown e'8 r8 \stemDown e8 r8 \pageBreak | % 133
    \stemDown d8 r8 \stemUp b8 r8 \stemDown fis'4 ~ ^\markup{ \italic
        {arco} } \stemDown fis8 r8 r4 | % 134
    \stemDown d4 ^\markup{ \italic {pizz.} } _\< \stemUp cis4 \stemUp b4
    r4 _\! r4 | % 135
    \stemUp a2 ~ _\f ^\markup{ \italic {arco} } _\> \stemUp a8 r8 _\! r4
    r4 | % 136
    \stemDown d8 -. _\mf \stemDown d8 -. \stemDown d'8 -. \stemDown d8
    -. r4 \stemDown d,4 \stemDown e4 | % 137
    \stemDown fis8 -. \stemDown fis8 -. \stemDown d8 -. \stemDown d8 -.
    \stemDown a'8 -. r8 r4 r4 \pageBreak | % 138
    \stemDown fis8 -. \stemDown fis8 -. \stemDown fis'8 -. \stemDown fis8
    -. r4 \stemDown fis,4 \stemDown e4 | % 139
    \stemDown d8 -. _\< \stemDown d8 -. \stemDown fis8 -. \stemDown fis8
    -. \stemDown a2 \stemDown as4 | \barNumberCheck #140
    \stemUp g8 -. _\! _\f _\> \stemUp g8 -. \stemUp g,8 -. \stemUp g8 -.
    \stemDown g'2. ~ _\! _\mf | % 141
    \stemUp g8 \stemUp g8 -. \stemUp g,8 -. \stemUp g8 -. \stemDown g'2.
    ~ _\> | % 142
    \stemUp g8 _\! _\p _\< \stemUp g8 -. \stemUp g,8 -. \stemUp g8 -.
    \stemDown g'2. ~ \pageBreak | % 143
    \stemUp g8 \stemUp g8 -. \stemUp g,8 -. \stemUp g8 -. \stemDown g'2
    \stemDown fis4 | % 144
    \stemUp f8 -. _\! _\f \stemUp f8 -. \stemUp f,8 -. \stemUp f8 -.
    \stemUp f'8 -. \stemUp f8 -. \stemUp f,8 -. \stemUp f8 -. \stemUp f'8
    -. \stemUp f8 -. | % 145
    \stemUp f,8 -. \stemUp f8 -. \stemUp f'8 -. \stemUp f8 -. \stemUp f,8
    -. \stemUp f8 -. \stemUp f'8 -. \stemUp f8 -. \stemUp f,8 -. \stemUp
    f8 -. | % 146
    \stemUp e'8 -. \stemUp e8 -. \stemUp e,8 -. \stemUp e8 -. \stemUp e'8
    -. \stemUp e8 -. \stemUp e,8 -. \stemUp e8 -. \stemUp e'8 -. \stemUp
    e8 -. | % 147
    \stemUp e,8 -. \stemUp e8 -. \stemUp e'8 -. \stemUp e8 -. \stemUp e,8
    -. \stemUp e8 -. \stemUp e'8 -. \stemUp e8 -. \stemUp e,8 -. \stemUp
    e8 -. \pageBreak | % 148
    \stemDown es'2 ~ \stemDown es2. | % 149
    \stemDown d4 \stemDown fis4 ( \stemDown g8 ) r8 r4 r4 |
    \barNumberCheck #150
    \stemUp a,8 -. _\mf r8 r4 r2 r4 | % 151
    \stemUp a8 _\f ^\markup{ \italic {pizz.} } r8 r4 \stemUp d,8 _\mf
    ^\markup{ \italic {arco} } r8 \stemUp d4 ( \stemUp e4 ) | % 152
    \stemUp fis4 ( \stemUp g4 \stemUp a4 \stemUp b4 \stemUp cis4 ) | % 153
    \stemDown d2 ~ \stemDown d2. ~ \pageBreak | % 154
    \stemDown d2 ~ \stemDown d2. ~ | % 155
    \stemDown d2 ~ \stemDown d2. | % 156
    \stemUp fis,4 ( _\p \stemUp g4 \stemUp a4 \stemUp b4 \stemUp cis4 )
    | % 157
    R4*15 | \barNumberCheck #160
    \clef "tenor" \stemDown f'4. ( _\f _\> \stemDown f8 ) -. \stemDown e2
    ( \stemDown d4 ) | % 161
    R4*5 | % 162
    \stemDown f4. ( _\! _\f _\> \stemDown f8 ) -. \stemDown e2 (
    \stemDown d4 ) \pageBreak | % 163
    \clef "bass" R4*5 | % 164
    \stemDown d,4 ( -. _\! _\p \stemDown d4 ) -. \stemDown d4 ( -.
    \stemDown d4 -. \stemDown d4 ) -. | % 165
    \stemDown d4 ( -. _\markup{ \italic {poco cresc.} } \stemDown d4 )
    -. \stemDown d4 ( -. \stemDown d4 -. \stemDown d4 ) -. | % 166
    \stemDown d4 ( -. \stemDown d4 ) -. \stemDown d4 ( -. \stemDown d4
    -. \stemDown d4 ) -. | % 167
    \stemDown d4 ( -. _\mf \stemDown d4 ) -. \stemDown d4 ( -. \stemDown
    d4 -. \stemDown d4 ) -. | % 168
    \stemDown d4 ( -. _\markup{ \italic {dim.} } \stemDown d4 ) -.
    \stemDown d4 ( -. \stemDown d4 -. \stemDown d4 ) -. | % 169
    \stemDown d4 ( -. _\mp _\> \stemDown d4 ) -. \stemDown d4 ( -.
    \stemDown d4 -. \stemDown d4 ) -. | \barNumberCheck #170
    \stemDown d4 ( -. _\! _\p _\> \stemDown d4 ) -. \stemDown d4 ( -.
    \stemDown d4 -. \stemDown d4 ) -. \break | % 171
    \stemUp a4 ( -. _\! _\pp \stemUp a4 ) -. \stemUp a4 ( -. \stemUp a4
    -. \stemUp a4 ) -. | % 172
    R4*5 | % 173
    \stemUp a4 ( -. \stemUp a4 ) -. \stemUp a4 ( -. \stemUp a4 -.
    \stemUp a4 ) -. | % 174
    R4*5 | % 175
    \stemUp a4 ( -. \stemUp a4 ) -. \stemUp a4 ( -. \stemUp a4 -.
    \stemUp a4 ) -. | % 176
    \stemUp a4 ( -. \stemUp a4 ) -. \stemUp a4 ( -. \stemUp a4 -.
    \stemUp a4 ) -. | % 177
    r2 \stemDown a'8 _\pp ^\markup{ \italic {pizz.} } r8 r4 r4
    \pageBreak | % 178
    \stemUp <a, d>8 _\pp r8 r4 r2 r4 ^\fermata \bar "|."
    }

PartPOneFiveVoiceTwo =  \relative b {
    \repeat volta 2 {
        \clef "bass" \time 5/4 \key d \major s4*15 | % 4
        \clef "tenor" s2*5 \pageBreak s4*9 \once \override
        NoteHead.style = ##f \stemNeutral b8 \once \override
        NoteHead.style = ##f \stemNeutral b8 | % 8
         \once \override NoteHead.style = ##f \stemNeutral b'8 s8*29
        \break s4*5 \pageBreak s4*25 }
    \pageBreak s4*5 \bar "||"
    s1*5 \break s4*5 \pageBreak s4*15 | % 25
    \clef "bass" s2*5 \break s4*25 \pageBreak s4*25 \pageBreak s1*5
    \pageBreak s4*5 \pageBreak s2*15 \pageBreak s4*25 \pageBreak s1*5
    \repeat volta 2 {
        | % 57
        \clef "tenor" s2*5 \pageBreak s2*15 }
    \pageBreak \repeat volta 2 {
        | % 65
        \clef "bass" s2*15 \pageBreak s2*5 }
    | % 73
    \clef "tenor" s1*5 \pageBreak s1*5 | % 81
    \clef "bass" s2*5 \pageBreak s2*15 \pageBreak s2*15 \pageBreak s2*5
    | % 97
    \clef "tenor" s1*5 \pageBreak s4*9 \once \override NoteHead.style =
    ##f \stemNeutral b,8 \once \override NoteHead.style = ##f
    \stemNeutral b8 | % 103
     \once \override NoteHead.style = ##f \stemNeutral b'8 s8*29 \break
    s4*25 \pageBreak s4*25 \break s4*5 \pageBreak s4*15 |
    \barNumberCheck #120
    \clef "bass" s2*5 \break s4*5 \pageBreak s4*25 \pageBreak s4*25
    \pageBreak s4*25 \pageBreak s4*25 \pageBreak s4*25 \pageBreak s2*15
    \pageBreak s2*15 | \barNumberCheck #160
    \clef "tenor" s4*15 \pageBreak | % 163
    \clef "bass" s1*10 \break s4*35 \pageBreak s4*5 \bar "|."
    }

PartPOneSixVoiceOne =  \relative d {
    \repeat volta 2 {
        \clef "bass" \time 5/4 \key d \major \transposition c | % 1
        \stemDown d8 _\mf ^\markup{ \italic {pizz.} } r8 r4 r2 r4 | % 2
        \stemDown fis8 r8 r4 \stemDown a8 r8 r4 r4 | % 3
        \stemDown fis8 r8 r4 r2 r4 | % 4
        \stemDown d8 r8 r4 \stemDown a'8 r8 r4 r4 | % 5
        \stemDown e8 r8 r4 r2 r4 \pageBreak | % 6
        R4*5 | % 7
        \stemUp b'8 ^\markup{ \italic {div.} } r8 r4 \stemUp e,8 r8 r4 r4
        | % 8
        \stemDown a8 _\f ^\markup{ \italic {unis.} } r8 r4 r2 \stemUp
        cis,8 _\mf r8 | % 9
        \stemDown d8 r8 \stemDown d'8 r8 r2 r4 | \barNumberCheck #10
        \stemDown d,8 r8 r4 \stemDown a'8 r8 r4 r4 \break | % 11
        \stemDown d,8 r8 \stemDown d'8 r8 r2 r4 \pageBreak | % 12
        \stemUp d,8 ^\markup{ \italic {div.} } r8 r4 \stemUp a'8 r8
        \stemUp a8 r8 r4 | % 13
        \stemUp g8 _\markup{ \italic {sempre} } _ "" r8 \stemUp g8 r8
        \stemUp fis8 r8 \stemUp fis2 ^\markup{ \italic {arco} } | % 14
        \stemUp d'8 ^\markup{ \italic {pizz.} } r8 \stemUp d8 r8 \stemUp
        d2. ^\markup{ \italic {arco} } | % 15
        \stemUp fis,8 ^\markup{ \italic {pizz.} } r8 \stemUp fis8 r8
        \stemUp e8 r8 \stemUp e2 ^\markup{ \italic {arco} } | % 16
        \stemUp cis'8 ^\markup{ \italic {pizz.} } r8 \stemUp a8 r8
        \stemUp a8 r8 r4 r4 }
    \pageBreak \stemUp cis8 ^\markup{ \italic {pizz.} } r8 \stemUp a8 r8
    \stemUp a8 r8 r2 \bar "||"
    \stemUp a,2 ~ ^\markup{ \italic {unis.} } _\mf ^\markup{ \italic
        {arco} } \stemUp a8 \stemUp a8 \stemUp a4 \stemUp cis4 | % 18
    \stemUp a2 ~ \stemUp a8 \stemUp a8 \stemUp a4 \stemDown d4 | % 19
    \stemUp a2 ~ \stemUp a8 \stemUp a8 \stemUp a4 \stemDown d4 |
    \barNumberCheck #20
    \stemUp a2 ~ \stemUp a8 \stemUp a8 \stemUp a4 \stemUp cis4 \break | % 21
    \stemUp a2 ~ \stemUp a8 \stemUp a8 \stemUp a4 \stemUp cis4
    \pageBreak | % 22
    \stemUp a2 ~ \stemUp a8 _\< \stemUp a8 \stemUp a4 \stemUp b4 | % 23
    \stemUp cis2 ~ _\! _\markup{ \italic {più} } _ "" \stemUp cis8
    \stemUp cis8 \stemUp cis4 \stemDown fis4 | % 24
    \stemUp cis2 ( \stemUp fis,8 ) r8 r4 r4 | % 25
    \stemUp a4 _\p ^\markup{ \italic {pizz.} } r4 r4 \stemUp a4 \stemUp
    cis4 | % 26
    \stemUp a4 r4 r4 \stemUp a4 \stemDown d4 \break | % 27
    \stemUp a4 r4 r4 \stemUp a4 \stemDown d4 | % 28
    \stemUp a4 r4 r4 \stemUp a4 \stemUp cis4 | % 29
    \stemUp a4 r4 r4 \stemUp a4 \stemUp cis4 | \barNumberCheck #30
    \stemUp a4 r4 r4 \stemUp a4 _\< \stemUp b4 | % 31
    \stemUp cis4 r4 _\! r4 \stemUp cis4 _\mp _\< \stemDown d4 \pageBreak
    | % 32
    \stemDown dis4 \stemDown e4 \stemUp a,8 _\! _\mf r8 r4 r4 | % 33
    \stemDown d8 _\mf ^\markup{ \italic {pizz.} } r8 r4 \stemDown d8 r8
    r4 r4 | % 34
    \stemDown fis8 r8 \stemDown d8 r8 \stemUp a8 r8 r4 r4 | % 35
    \stemDown d8 r8 r4 \stemUp fis,8 r8 \stemUp fis8 r8 \stemUp cis'8 r8
    | % 36
    \stemDown d8 r8 \stemDown fis8 r8 \stemDown a4 ~ ^\markup{ \italic
        {arco} } \stemDown a8 r8 r4 \pageBreak | % 37
    \stemDown e8 _\p ^\markup{ \italic {pizz.} } r8 r4 \stemDown g8 r8
    \stemDown e8 r8 \stemDown e8 r8 | % 38
    \stemDown d8 r8 \stemUp b8 r8 \stemDown fis'4 ~ ^\markup{ \italic
        {arco} } \stemDown fis8 r8 r4 | % 39
    \stemDown d4 ^\markup{ \italic {pizz.} } _\< \stemUp cis4 \stemUp b4
    r4 _\! r4 | \barNumberCheck #40
    \stemUp a2 ~ _\f ^\markup{ \italic {arco} } _\> \stemUp a8 r8 _\! r4
    r4 \pageBreak | % 41
    \stemDown d8 -. _\mf \stemDown d8 -. \stemDown d'8 -. \stemDown d8
    -. r4 \stemDown d,4 \stemDown e4 \pageBreak | % 42
    \stemDown fis8 -. \stemDown fis8 -. \stemDown d8 -. \stemDown d8 -.
    \stemDown a'8 -. r8 r4 r4 | % 43
    \stemDown fis8 -. \stemDown fis8 -. \stemDown fis'8 -. \stemDown fis8
    -. r4 \stemDown fis,4 \stemDown e4 | % 44
    \stemDown d8 -. _\< \stemDown d8 -. \stemDown fis8 -. \stemDown fis8
    -. \stemDown a2 \stemDown as4 | % 45
    \stemUp g8 -. _\! _\f _\> \stemUp g8 -. \stemUp g,8 -. \stemUp g8 -.
    \stemDown g'2. ~ _\! _\mf | % 46
    \stemUp g8 \stemUp g8 -. \stemUp g,8 -. \stemUp g8 -. \stemDown g'2.
    ~ _\> | % 47
    \stemUp g8 _\! _\p _\< \stemUp g8 -. \stemUp g,8 -. \stemUp g8 -.
    \stemDown g'2. ~ \pageBreak | % 48
    \stemUp g8 \stemUp g8 -. \stemUp g,8 -. \stemUp g8 -. \stemDown g'2
    \stemDown fis4 | % 49
    \stemUp f8 -. _\! _\f \stemUp f8 -. \stemUp f,8 -. \stemUp f8 -.
    \stemUp f'8 -. \stemUp f8 -. \stemUp f,8 -. \stemUp f8 -. \stemUp f'8
    -. \stemUp f8 -. | \barNumberCheck #50
    \stemUp f,8 -. \stemUp f8 -. \stemUp f'8 -. \stemUp f8 -. \stemUp f,8
    -. \stemUp f8 -. \stemUp f'8 -. \stemUp f8 -. \stemUp f,8 -. \stemUp
    f8 -. | % 51
    \stemUp e'8 -. \stemUp e8 -. \stemUp e,8 -. \stemUp e8 -. \stemUp e'8
    -. \stemUp e8 -. \stemUp e,8 -. \stemUp e8 -. \stemUp e'8 -. \stemUp
    e8 -. | % 52
    \stemUp e,8 -. \stemUp e8 -. \stemUp e'8 -. \stemUp e8 -. \stemUp e,8
    -. \stemUp e8 -. \stemUp e'8 -. \stemUp e8 -. \stemUp e,8 -. \stemUp
    e8 -. \pageBreak | % 53
    \stemDown es'2 ~ \stemDown es2. | % 54
    \stemDown d4 \stemDown fis4 ( \stemDown g8 ) r8 r4 r4 | % 55
    \stemUp a,8 -. _\mf r8 r4 r2 r4 | % 56
    \stemUp a8 _\f ^\markup{ \italic {pizz.} } r8 r4 \stemDown d4 -- _\p
    ^\markup{ \italic {arco} } \stemDown d4 -- \stemDown d4 -- \repeat
    volta 2 {
        | % 57
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- | % 58
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- \pageBreak | % 59
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- | \barNumberCheck #60
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- | % 61
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- | % 62
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- | % 63
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- | % 64
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- }
    \pageBreak \repeat volta 2 {
        | % 65
        \stemDown d4 -- _\p \stemDown d4 -- \stemDown d4 -- \stemDown d4
        -- \stemDown d4 -- | % 66
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- | % 67
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- | % 68
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- | % 69
        \stemDown d4 -- _ "" _\markup{ \italic {cresc.} } \stemDown d4
        -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- |
        \barNumberCheck #70
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- \pageBreak | % 71
        \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- | % 72
        \stemDown d4 -- _\f _\> \stemDown d4 -- \stemDown d4 --
        \stemDown d4 -- \stemDown d4 -- }
    | % 73
    \stemDown d4 -- _\! _\p \stemDown d4 -- \stemDown d4 -- \stemDown d4
    -- \stemDown d4 -- | % 74
    \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
    \stemDown d4 -- | % 75
    \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
    \stemDown d4 -- | % 76
    \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
    \stemDown d4 -- \pageBreak | % 77
    \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
    \stemDown d4 -- | % 78
    \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
    \stemDown d4 -- | % 79
    \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
    \stemDown d4 -- | \barNumberCheck #80
    \stemDown d4 -- \stemDown d4 -- \stemDown d4 -- \stemDown d4 --
    \stemDown d4 -- | % 81
    \stemDown d4 -- _\f \stemDown d4 -- \stemDown d4 -- _\> \stemDown d4
    -- \stemDown d4 -- | % 82
    \stemDown d2 ~ _\! _\mf _\> \stemDown d8 r8 _\! r4 r4 \pageBreak | % 83
    \stemDown d4 -- _\f \stemDown d4 -- \stemDown d4 -- _\> \stemDown d4
    -- \stemDown d4 -- | % 84
    \stemDown d2 ~ _\! _\mf _\> \stemDown d8 r8 _\! r4 r4 | % 85
    \stemDown d4 -- _\f \stemDown d4 -- \stemDown d4 -- _\> \stemDown d4
    -- \stemDown d4 -- | % 86
    \stemDown d2 ~ _\! _\mf _\> \stemDown d8 r8 _\! r4 r4 | % 87
    \stemDown d4 -- _\f \stemDown d4 -- \stemDown d4 -- _\> \stemDown d4
    -- \stemDown d4 -- | % 88
    \stemDown d2 ~ _\! _\mf _\> \stemDown d8 r8 _\! r4 r4 \pageBreak | % 89
    \stemDown d2 ~ _\mf _\> \stemDown d8 r8 _\! r4 r4 | \barNumberCheck
    #90
    \stemDown d2 ~ _\mf _\> \stemDown d8 r8 _\! r4 r4 | % 91
    \stemDown d2 ~ _\mf _\> \stemDown d8 r8 _\! r4 r4 | % 92
    \stemDown d2 ~ _\mf _\> \stemDown d8 r8 _\! r4 r4 | % 93
    \stemDown d2 ~ _\mf _\> \stemDown d8 r8 _\! r4 r4 | % 94
    \stemDown d2 ~ _\mf _\> \stemDown d8 r8 _\! r4 r4 \pageBreak | % 95
    \stemDown d2 ~ _\mf _\> \stemDown d8 r8 _\! r4 r4 | % 96
    \stemDown d8 _\mf ^\markup{ \italic {pizz.} } r8 r4 r2 r4 | % 97
    \stemDown fis8 r8 r4 \stemDown a8 r8 r4 r4 | % 98
    \stemDown fis8 r8 r4 r2 r4 | % 99
    \stemDown d8 r8 r4 \stemDown a'8 r8 r4 r4 | \barNumberCheck #100
    \stemDown e8 r8 r4 r2 r4 \pageBreak | % 101
    \stemDown d8 r8 r4 r2 r4 | % 102
    \stemUp b'8 ^\markup{ \italic {div.} } r8 r4 \stemUp e,8 r8 r2 | % 103
    \stemDown a8 _\f ^\markup{ \italic {unis.} } r8 r4 r2 \stemUp cis,8
    _\mf r8 | % 104
    \stemDown d8 r8 \stemDown d'8 r8 r2 r4 | % 105
    \stemDown d,8 r8 r4 \stemDown a'8 r8 r4 r4 \break | % 106
    \stemDown d,8 r8 \stemDown d'8 r8 r2 r4 | % 107
    \stemUp d,8 ^\markup{ \italic {div.} } r8 r4 \stemUp a'8 r8 \stemUp
    a8 r8 r4 | % 108
    \stemUp g8 _\markup{ \italic {sempre} } _ "" r8 \stemUp g8 r8
    \stemUp fis8 r8 \stemUp fis2 ^\markup{ \italic {arco} } | % 109
    \stemUp d'8 ^\markup{ \italic {pizz.} } r8 \stemUp d8 r8 \stemUp d2.
    ^\markup{ \italic {arco} } | \barNumberCheck #110
    \stemUp fis,8 ^\markup{ \italic {pizz.} } r8 \stemUp fis8 r8 \stemUp
    e8 r8 \stemUp e2 ^\markup{ \italic {arco} } \pageBreak | % 111
    \stemUp cis'8 ^\markup{ \italic {pizz.} } r8 \stemUp a8 r8 \stemUp a8
    r8 r2 | % 112
    \stemUp a,2 ~ ^\markup{ \italic {unis.} } _\mf ^\markup{ \italic
        {arco} } \stemUp a8 \stemUp a8 \stemUp a4 \stemUp cis4 | % 113
    \stemUp a2 ~ \stemUp a8 \stemUp a8 \stemUp a4 \stemDown d4 | % 114
    \stemUp a2 ~ \stemUp a8 \stemUp a8 \stemUp a4 \stemDown d4 | % 115
    \stemUp a2 ~ \stemUp a8 \stemUp a8 \stemUp a4 \stemUp cis4 \break | % 116
    \stemUp a2 ~ \stemUp a8 \stemUp a8 \stemUp a4 \stemUp cis4
    \pageBreak | % 117
    \stemUp a2 ~ \stemUp a8 _\< \stemUp a8 \stemUp a4 \stemUp b4 | % 118
    \stemUp cis2 ~ _\! _\markup{ \italic {più} } _ "" \stemUp cis8
    \stemUp cis8 \stemUp cis4 \stemDown fis4 | % 119
    \stemUp cis2 ( \stemUp fis,8 ) r8 r4 r4 | \barNumberCheck #120
    \stemUp a4 _\p ^\markup{ \italic {pizz.} } r4 r4 \stemUp a4 \stemUp
    cis4 | % 121
    \stemUp a4 r4 r4 \stemUp a4 \stemDown d4 \break | % 122
    \stemUp a4 r4 r4 \stemUp a4 \stemDown d4 \pageBreak | % 123
    \stemUp a4 r4 r4 \stemUp a4 \stemUp cis4 | % 124
    \stemUp a4 r4 r4 \stemUp a4 \stemUp cis4 | % 125
    \stemUp a4 r4 r4 \stemUp a4 _\< \stemUp b4 | % 126
    \stemUp cis4 r4 _\! r4 \stemUp cis4 _\mp _\< \stemDown d4 | % 127
    \stemDown dis4 \stemDown e4 \stemUp a,8 _\! _\mf r8 r4 r4 \pageBreak
    | % 128
    \stemDown d8 _\mf ^\markup{ \italic {pizz.} } r8 r4 \stemDown d8 r8
    r4 r4 | % 129
    \stemDown fis8 r8 \stemDown d8 r8 \stemUp a8 r8 r4 r4 |
    \barNumberCheck #130
    \stemDown d8 r8 r4 \stemUp fis,8 r8 \stemUp fis8 r8 \stemUp cis'8 r8
    | % 131
    \stemDown d8 r8 \stemDown fis8 r8 \stemDown a4 ~ ^\markup{ \italic
        {arco} } \stemDown a8 r8 r4 | % 132
    \stemDown e8 _\p ^\markup{ \italic {pizz.} } r8 r4 \stemDown g8 r8
    \stemDown e8 r8 \stemDown e8 r8 \pageBreak | % 133
    \stemDown d8 r8 \stemUp b8 r8 \stemDown fis'4 ~ ^\markup{ \italic
        {arco} } \stemDown fis8 r8 r4 | % 134
    \stemDown d4 ^\markup{ \italic {pizz.} } _\< \stemUp cis4 \stemUp b4
    r4 _\! r4 | % 135
    \stemUp a2 ~ _\f ^\markup{ \italic {arco} } _\> \stemUp a8 r8 _\! r4
    r4 | % 136
    \stemDown d8 -. _\mf \stemDown d8 -. \stemDown d'8 -. \stemDown d8
    -. r4 \stemDown d,4 \stemDown e4 | % 137
    \stemDown fis8 -. \stemDown fis8 -. \stemDown d8 -. \stemDown d8 -.
    \stemDown a'8 -. r8 r4 r4 \pageBreak | % 138
    \stemDown fis8 -. \stemDown fis8 -. \stemDown fis'8 -. \stemDown fis8
    -. r4 \stemDown fis,4 \stemDown e4 | % 139
    \stemDown d8 -. _\< \stemDown d8 -. \stemDown fis8 -. \stemDown fis8
    -. \stemDown a2 \stemDown as4 | \barNumberCheck #140
    \stemUp g8 -. _\! _\f _\> \stemUp g8 -. \stemUp g,8 -. \stemUp g8 -.
    \stemDown g'2. ~ _\! _\mf | % 141
    \stemUp g8 \stemUp g8 -. \stemUp g,8 -. \stemUp g8 -. \stemDown g'2.
    ~ _\> | % 142
    \stemUp g8 _\! _\p _\< \stemUp g8 -. \stemUp g,8 -. \stemUp g8 -.
    \stemDown g'2. ~ \pageBreak | % 143
    \stemUp g8 \stemUp g8 -. \stemUp g,8 -. \stemUp g8 -. \stemDown g'2
    \stemDown fis4 | % 144
    \stemUp f8 -. _\! _\f \stemUp f8 -. \stemUp f,8 -. \stemUp f8 -.
    \stemUp f'8 -. \stemUp f8 -. \stemUp f,8 -. \stemUp f8 -. \stemUp f'8
    -. \stemUp f8 -. | % 145
    \stemUp f,8 -. \stemUp f8 -. \stemUp f'8 -. \stemUp f8 -. \stemUp f,8
    -. \stemUp f8 -. \stemUp f'8 -. \stemUp f8 -. \stemUp f,8 -. \stemUp
    f8 -. | % 146
    \stemUp e'8 -. \stemUp e8 -. \stemUp e,8 -. \stemUp e8 -. \stemUp e'8
    -. \stemUp e8 -. \stemUp e,8 -. \stemUp e8 -. \stemUp e'8 -. \stemUp
    e8 -. | % 147
    \stemUp e,8 -. \stemUp e8 -. \stemUp e'8 -. \stemUp e8 -. \stemUp e,8
    -. \stemUp e8 -. \stemUp e'8 -. \stemUp e8 -. \stemUp e,8 -. \stemUp
    e8 -. \pageBreak | % 148
    \stemDown es'2 ~ \stemDown es2. | % 149
    \stemDown d4 \stemDown fis4 ( \stemDown g8 ) r8 r4 r4 |
    \barNumberCheck #150
    \stemUp a,8 -. _\mf r8 r4 r2 r4 | % 151
    \stemUp a8 _\f ^\markup{ \italic {pizz.} } r8 r4 \stemDown d2. ~
    _\mf ^\markup{ \italic {arco} } | % 152
    \stemDown d2 ~ \stemDown d2. ~ | % 153
    \stemDown d2 ~ \stemDown d2. ~ \pageBreak | % 154
    \stemDown d2 ~ \stemDown d2. ~ | % 155
    \stemDown d2 ~ \stemDown d2. | % 156
    \stemDown d2 ~ _\p \stemDown d2. | % 157
    \stemDown d'2 ~ \stemDown d2. ~ | % 158
    \stemDown d2 ~ \stemDown d2. ~ | % 159
    \stemDown d2 ~ \stemDown d2. | \barNumberCheck #160
    \stemDown d,4 -- _\mf _\> \stemDown d4 -- \stemDown d4 -- \stemDown
    d4 -- \stemDown d4 -- | % 161
    \stemDown d4 -- _\! _\p \stemDown d4 -- \stemDown d4 -- \stemDown d4
    -- \stemDown d4 -- | % 162
    \stemDown d4 -- _\mf _\> \stemDown d4 -- \stemDown d4 -- \stemDown d4
    -- \stemDown d4 -- \pageBreak | % 163
    \stemDown d4 -- _\! _\p \stemDown d4 -- \stemDown d4 -- \stemDown d4
    -- \stemDown d4 -- | % 164
    \stemDown d4 ( -. _\p \stemDown d4 ) -. \stemDown d4 ( -. \stemDown
    d4 -. \stemDown d4 ) -. | % 165
    \stemDown d4 ( -. _\markup{ \italic {poco cresc.} } \stemDown d4 )
    -. \stemDown d4 ( -. \stemDown d4 -. \stemDown d4 ) -. | % 166
    \stemDown d4 ( -. \stemDown d4 ) -. \stemDown d4 ( -. \stemDown d4
    -. \stemDown d4 ) -. | % 167
    \stemDown d4 ( -. _\mf \stemDown d4 ) -. \stemDown d4 ( -. \stemDown
    d4 -. \stemDown d4 ) -. | % 168
    \stemDown d4 ( -. _\markup{ \italic {dim.} } \stemDown d4 ) -.
    \stemDown d4 ( -. \stemDown d4 -. \stemDown d4 ) -. | % 169
    \stemDown d4 ( -. _\mp _\> \stemDown d4 ) -. \stemDown d4 ( -.
    \stemDown d4 -. \stemDown d4 ) -. | \barNumberCheck #170
    \stemDown d4 ( -. _\! _\p _\> \stemDown d4 ) -. \stemDown d4 ( -.
    \stemDown d4 -. \stemDown d4 ) -. \break | % 171
    \stemDown d4 ( -. _\! _\pp \stemDown d4 ) -. \stemDown d4 ( -.
    \stemDown d4 -. \stemDown d4 ) -. | % 172
    R4*5 | % 173
    \stemDown d4 ( -. \stemDown d4 ) -. \stemDown d4 ( -. \stemDown d4
    -. \stemDown d4 ) -. | % 174
    R4*5 | % 175
    \stemDown d4 ( -. \stemDown d4 ) -. \stemDown d4 ( -. \stemDown d4
    -. \stemDown d4 ) -. | % 176
    \stemDown d4 ( -. \stemDown d4 ) -. \stemDown d4 ( -. \stemDown d4
    -. \stemDown d4 ) -. | % 177
    r2 \stemDown d'8 _\pp ^\markup{ \italic {pizz.} } r8 r4 r4
    \pageBreak | % 178
    \stemDown d,8 _\pp r8 r4 r2 r4 ^\fermata \bar "|."
    }

PartPOneSixVoiceTwo =  \relative b, {
    \repeat volta 2 {
        \clef "bass" \time 5/4 \key d \major \transposition c s4*25
        \pageBreak s4*5 | % 7
        \stemDown b8 s4. \stemDown e8 s8*35 \break s4*5 \pageBreak | % 12
        \stemDown d8 s4. \stemDown a8 s8 \stemDown a'8 s4. | % 13
        \stemDown g,8 s8 \stemDown g'8 s8 \stemDown fis,8 s8 \stemDown
        fis'2 | % 14
        \stemDown d8 s8 \stemDown d'8 s8 \stemDown d,2. | % 15
        \stemDown fis,8 s8 \stemDown fis'8 s8 \stemDown e,8 s8 \stemDown
        e'2 | % 16
        \stemDown cis8 s8 \stemDown a8 s8 \stemDown a'8 s8*5 }
    \pageBreak \stemDown cis,8 s8 \stemDown a8 s8 \stemDown a'8 s8*5
    \bar "||"
    s1*5 \break s4*5 \pageBreak s4*25 \break s4*25 \pageBreak s4*25
    \pageBreak s1*5 \pageBreak s4*5 \pageBreak s2*15 \pageBreak s4*25
    \pageBreak s1*5 \repeat volta 2 {
        s2*5 \pageBreak s2*15 }
    \pageBreak \repeat volta 2 {
        s2*15 \pageBreak s2*5 }
    s1*5 \pageBreak s2*15 \pageBreak s2*15 \pageBreak s2*15 \pageBreak
    s2*15 \pageBreak s4*5 | % 102
    \stemDown b,8 s4. \stemDown e8 s8*35 \break s4*5 | % 107
    \stemDown d8 s4. \stemDown a8 s8 \stemDown a'8 s4. | % 108
    \stemDown g,8 s8 \stemDown g'8 s8 \stemDown fis,8 s8 \stemDown fis'2
    | % 109
    \stemDown d8 s8 \stemDown d'8 s8 \stemDown d,2. | \barNumberCheck
    #110
    \stemDown fis,8 s8 \stemDown fis'8 s8 \stemDown e,8 s8 \stemDown e'2
    \pageBreak | % 111
    \stemDown cis8 s8 \stemDown a8 s8 \stemDown a'8 s8*45 \break s4*5
    \pageBreak s4*25 \break s4*5 \pageBreak s4*25 \pageBreak s4*25
    \pageBreak s4*25 \pageBreak s4*25 \pageBreak s4*25 \pageBreak s2*15
    \pageBreak s4*45 \pageBreak s1*10 \break s4*35 \pageBreak s4*5 \bar
    "|."
    }


% The score definition
\score {
    <<
        
        \new StaffGroup
        <<
            \new PianoStaff
            <<
                \set PianoStaff.instrumentName = "Flauti"
                \set PianoStaff.shortInstrumentName = "Fl."
                
                \context Staff = "1" << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneVoiceOne" {  \voiceOne \PartPOneVoiceOne }
                    \context Voice = "PartPOneVoiceTwo" {  \voiceTwo \PartPOneVoiceTwo }
                    >> \context Staff = "2" <<
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneVoiceFive" {  \PartPOneVoiceFive }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Oboi"
                \set Staff.shortInstrumentName = "Ob."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPTwoVoiceOne" {  \voiceOne \PartPTwoVoiceOne }
                    \context Voice = "PartPTwoVoiceTwo" {  \voiceTwo \PartPTwoVoiceTwo }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Clarinetti in A"
                \set Staff.shortInstrumentName = "Cl."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPThreeVoiceOne" {  \voiceOne \PartPThreeVoiceOne }
                    \context Voice = "PartPThreeVoiceTwo" {  \voiceTwo \PartPThreeVoiceTwo }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Fagotti"
                \set Staff.shortInstrumentName = "Fag."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPFourVoiceOne" {  \voiceOne \PartPFourVoiceOne }
                    \context Voice = "PartPFourVoiceTwo" {  \voiceTwo \PartPFourVoiceTwo }
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
                        \context Voice = "PartPFiveVoiceOne" {  \voiceOne \PartPFiveVoiceOne }
                        \context Voice = "PartPFiveVoiceTwo" {  \voiceTwo \PartPFiveVoiceTwo }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Corni in F III IV"
                    \set Staff.shortInstrumentName = \markup { \center-column { \line {"Cor."} \line {"III IV"} } }
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPSixVoiceOne" {  \voiceOne \PartPSixVoiceOne }
                        \context Voice = "PartPSixVoiceTwo" {  \voiceTwo \PartPSixVoiceTwo }
                        >>
                    >>
                
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Trombe in A"
                \set Staff.shortInstrumentName = "Tr."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPSevenVoiceOne" {  \voiceOne \PartPSevenVoiceOne }
                    \context Voice = "PartPSevenVoiceTwo" {  \voiceTwo \PartPSevenVoiceTwo }
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
                        \context Voice = "PartPEightVoiceOne" {  \voiceOne \PartPEightVoiceOne }
                        \context Voice = "PartPEightVoiceTwo" {  \voiceTwo \PartPEightVoiceTwo }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Trombone Basso"
                    \set Staff.shortInstrumentName = "Tbn. B."
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPNineVoiceOne" {  \PartPNineVoiceOne }
                        >>
                    >>
                
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Tuba"
                \set Staff.shortInstrumentName = "Tuba"
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneZeroVoiceOne" {  \PartPOneZeroVoiceOne }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Timpani in A.D.E."
                \set Staff.shortInstrumentName = "Timp."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneOneVoiceOne" {  \PartPOneOneVoiceOne }
                    >>
                >>
            \new StaffGroup \with { systemStartDelimiter =
                #'SystemStartBrace }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = "Violino I"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneTwoVoiceOne" {  \voiceOne \PartPOneTwoVoiceOne }
                        \context Voice = "PartPOneTwoVoiceTwo" {  \voiceTwo \PartPOneTwoVoiceTwo }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Violino II"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneThreeVoiceOne" {  \voiceOne \PartPOneThreeVoiceOne }
                        \context Voice = "PartPOneThreeVoiceTwo" {  \voiceTwo \PartPOneThreeVoiceTwo }
                        >>
                    >>
                
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Viola"
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneFourVoiceOne" {  \voiceOne \PartPOneFourVoiceOne }
                    \context Voice = "PartPOneFourVoiceTwo" {  \voiceTwo \PartPOneFourVoiceTwo }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Violoncello"
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneFiveVoiceOne" {  \voiceOne \PartPOneFiveVoiceOne }
                    \context Voice = "PartPOneFiveVoiceTwo" {  \voiceTwo \PartPOneFiveVoiceTwo }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Basso"
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneSixVoiceOne" {  \voiceOne \PartPOneSixVoiceOne }
                    \context Voice = "PartPOneSixVoiceTwo" {  \voiceTwo \PartPOneSixVoiceTwo }
                    >>
                >>
            
            >>
        
        >>
    \layout {}
    % To create MIDI output, uncomment the following line:
    %  \midi {\tempo 4 = 144 }
    }

