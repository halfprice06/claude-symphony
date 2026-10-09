\version "2.24.3"
% automatically converted by musicxml2ly from ../xml/Beethoven_Sym9_mvt3.musicxml
\pointAndClickOff

\header {
    title =  "Symphony No. 9"
    composer =  \markup \column {
        \line { "Ludwig van Beethoven"}
        \line { ""} }
    
    encodingsoftware =  "MuseScore 4.1.0"
    encodingdate =  "2023-07-21"
    source =  "http://musescore.com/user/19710/scores/5641865"
    subtitle =  \markup \column {
        \line { "3"}
        \line { ""} }
    
    }

#(set-global-staff-size 20.16)
\paper {
    
    paper-width = 29.7\cm
    paper-height = 42.0\cm
    top-margin = 1.0\cm
    bottom-margin = 2.0\cm
    left-margin = 1.0\cm
    right-margin = 1.01\cm
    indent = 2.2846153846153845\cm
    short-indent = 1.7769230769230768\cm
    }
\layout {
    \context { \Score
        skipBars = ##t
        }
    }
PartPOneVoiceOne =  \relative e''' {
    \clef "treble" \time 4/4 \key bes \major | % 1
    R1*9 \pageBreak ^\markup{ \bold {Adagio molto e cantabile} } |
    \barNumberCheck #10
    R1*10 \pageBreak | \barNumberCheck #20
    R1*4 \break | % 24
    R1 \bar "||"
    \pageBreak | % 25
    \time 3/4  \key d \major R2.*4 ^\markup{ \bold {Andante moderato} }
    | % 29
    r4 r4 r8 \stemDown e8 ~ ^ "I." _\markup{ \italic {} } _ "cresc." |
    \barNumberCheck #30
    \stemDown e4 ( \stemDown d8 ) r8 r4 | % 31
    R2. \pageBreak | % 32
    R2.*3 | % 35
    r4 \stemDown g,8 ( -. ^ "I." _\markup{ \italic {cresc.} } \stemDown
    a8 -. \stemDown b8 -. \stemDown cis8 ) -. | % 36
    \stemDown e8 ( \stemDown d4 ) \stemDown d16 ( _\> \stemDown cis16
    \stemDown b16 \stemDown a16 \stemDown g16 \stemDown fis16 ) | % 37
    \stemDown fis8 ( _\! _\p \stemDown e8 ) r4 r4 \pageBreak | % 38
    R2. | % 39
    r4 r8 \stemDown b'16 ( _\> \stemDown g'16 \stemDown fis16 \stemDown
    e16 \stemDown d16 \stemDown cis16 ) | \barNumberCheck #40
    \stemDown e4. ( _\! _\markup{ \italic {morendo} } \stemDown g,8 )
    \stemDown fis4 | % 41
    r4 \stemDown e'8 ( _\markup{ \italic {più} } _ "" \stemDown g,8
    \stemDown f4 ) ~ | % 42
    \stemDown f2 ( _\pp \stemDown es4 ) ^\fermata \bar "||"
    \pageBreak | % 43
    \time 4/4  \key bes \major \stemDown d4 ^\markup{ \bold {Tempo I} }
    r4 r2 | % 44
    R1*3 \break | % 47
    R1*4 \pageBreak | % 51
    R1*5 \break | % 56
    R1*5 \pageBreak | % 61
    R1*3 | % 64
    r2 r4 r8 \stemDown b'8 ~ _\pp ^ "I." \bar "||"
    \pageBreak | % 65
    \time 3/4  \key g \major \stemDown b8 ( ^\markup{ \bold {Andante} }
    \stemDown a4 ) _\markup{ \italic {cresc.} } \stemDown a8 ~ \stemDown
    a16 ( \stemDown b16 \stemDown c16 \stemDown a16 ) | % 66
    \stemDown c8 ( \stemDown b4 ) \stemDown b8 ~ \stemDown b16 (
    \stemDown c16 \stemDown d16 \stemDown b16 ) | % 67
    \stemDown d8 ( \stemDown c4 ) \stemDown c8 ( -. \stemDown c8 -.
    \stemDown c8 ) -. | % 68
    \stemDown c8 ( \stemDown b16 \stemDown a16 \stemDown g16 _\>
    \stemDown d'16 \stemDown g16 \stemDown fis16 \stemDown e16 \stemDown
    d16 \stemDown c16 \stemDown b16 ) | % 69
    \stemDown b8 ( _\! \stemDown a4 ) _\markup{ \italic {cresc.} }
    \stemDown a8 ~ \stemDown a16 ( \stemDown b16 \stemDown c16 \stemDown
    a16 ) | \barNumberCheck #70
    \stemDown c8 ( \stemDown b4 ) \stemDown b8 ~ \stemDown b16 (
    \stemDown c16 \stemDown d16 \stemDown b16 ) \pageBreak | % 71
    \stemDown d8 ( \stemDown c4 ) r8 r4 | % 72
    r4 r8 \stemDown <a c>8 ( _\pp \stemDown <g b>8 ) \stemUp b8 ~ | % 73
    \stemUp b8 ( \stemUp a4 ) _\markup{ \italic {cresc.} } \stemUp a8 ~
    \stemUp a16 ( \stemUp b16 \stemUp c16 \stemUp a16 ) | % 74
    \stemUp c8 ( \stemUp b4 ) \stemUp b8 ~ \stemUp b16 ( \stemUp c16
    \stemUp d16 \stemUp b16 ) | % 75
    \stemUp d8 ( \stemUp c4 ) \stemUp c8 ( -. \stemUp c8 -. \stemUp c8 )
    -. | % 76
    \stemDown c8 ( ^ "I." \stemDown b4 ) \stemDown b16 ( _\> \stemDown d16
    \stemDown c16 \stemDown b16 \stemDown a16 \stemDown g16 ) | % 77
    \stemDown b8 ( _\! \stemDown a4 ) _\markup{ \italic {cresc.} }
    \stemDown a8 ~ \stemDown a16 ( \stemDown b16 \stemDown c16 \stemDown
    a16 ) \pageBreak | % 78
    \stemDown c8 ( \stemDown b4 ) \stemDown b8 ~ \stemDown b16 (
    \stemDown c16 \stemDown d16 \stemDown b16 ) | % 79
    \stemDown d8 ( \stemDown c4 ) \stemDown e16 ( _\> \stemDown c16
    \stemDown b16 \stemDown a16 \stemDown g16 \stemDown fis16 ) |
    \barNumberCheck #80
    r4 _\! \stemDown <c a'>8 ( _\pp \stemDown <a' c>8 \stemDown <g b>4 )
    | % 81
    R2.*2 \bar "||"
    \time 4/4  \key es \major R1*2 \break ^\markup{ \bold {Adagio} } | % 85
    R1*5 \pageBreak | \barNumberCheck #90
    R1 | % 91
    \stemDown ces2 ( _\markup{ \italic {dolce} } ^ "I." \stemDown ges4.
    \stemDown fes8 ) | % 92
    \stemDown fes8 ( \stemDown es8 ) \stemDown es4. \stemDown fes8 ( -.
    \stemDown ges8 -. \stemDown as8 ) -. | % 93
    \stemDown as8 ( _\< \stemDown ges8 \stemDown ces8 _\! _\> \stemDown
    es,8 ) \stemDown ges4 ( _\! \stemDown fes4 ) | % 94
    \stemDown fes8 ( _\< \stemDown es8 ) r4 _\! r4 \stemDown bes4 _\pp
    \break | % 95
    bes1 | % 96
    \stemDown ces4 r4 r4 r8 \stemDown ces8 | % 97
    \stemDown des4 _\markup{ \italic {cresc.} } \stemDown fes2 \stemDown
    fes4 ~ | % 98
    \stemUp fes4 \stemDown <fes des'>2 _\markup{ \italic {cresc.} }
    \stemDown <f d'>4 \bar "||"
    \pageBreak | % 99
    \time 12/8  \key bes \major \stemUp d'2. ( ^\markup{ \bold {Lo
            stesso tempo} } _ "" _\markup{ \italic {dolce} } \stemUp a2.
    | \barNumberCheck #100
    \stemUp bes2. \stemUp f'4. ~ \stemUp f4 \stemUp es8 ) \pageBreak | % 101
    \stemUp d4. ( _\< \stemUp f4. \stemUp bes,4. ~ _\! _\> \once
    \override NoteHead.style = ##f \stemUp bes4 \stemUp c8 ) | % 102
    \stemDown <bes d>4. ( _\! _\< \stemDown <d f>4 \stemDown <c es>8 )
    \stemUp c4. _\! _\> r4 _\! r8 | % 103
    r4 ^ "I." r8 \stemDown bes4. ( ~ _\markup{ \italic {cresc.} }
    \stemDown bes4 \stemDown a8 \stemDown g'8 _\> \stemDown f16
    \stemDown es16 \stemDown c8 ) \pageBreak | % 104
    \stemUp c2. ( _\! _\p \stemUp bes4. ~ \stemUp bes4 \stemUp f'8 ) | % 105
    \stemUp f4. ( \stemUp es4. ~ \stemUp es4. \stemUp d4. ) | % 106
    \stemUp c4. ( ~ \stemUp c4 \stemUp d16 \stemUp es16 ) \stemUp d4. (
    \stemUp c4 \stemUp cis8 ) \pageBreak | % 107
    \stemUp cis4. ( ~ _\< \stemUp cis4 \stemUp d8 ) \stemUp d4. _\! _\>
    r4 _\! r8 | % 108
    r8 _\< \stemUp f8 ( \stemUp cis8 ) \stemUp cis4 ( \stemUp d8 )
    \stemUp d4. _\! _\> \stemUp d4. ( \pageBreak | % 109
    \stemUp c2. _\! \stemUp bes4. ~ \once \override NoteHead.style = ##f
    \stemUp bes4 \stemUp f'8 ) | \barNumberCheck #110
    \stemDown <g, f'>4. ( _\< \stemDown <c g'>4. ~ ~ \stemDown <c g'>4.
    _\! _\> \stemDown <bes d>4 ) r8 _\! \pageBreak | % 111
    r2. ^ "I." r4 r8 \stemDown g'4. _\markup{ \italic {cresc.} } | % 112
    \stemUp g2. ~ \stemUp g4. ~ \stemUp g4 ( \stemUp c,8 ) \pageBreak | % 113
    \stemUp d4. ~ _\> \stemUp d4 \stemUp d8 ( \stemUp f4. _\! _\p
    \stemUp es4 \stemUp c8 ) | % 114
    \stemDown c4. ( ~ ^ "I." \stemDown c4 \stemDown d8 ) r8 \stemDown
    bes8 ( \stemDown c16 \stemDown d16 \stemDown es4 \stemDown c8 )
    \pageBreak | % 115
    \stemDown c4. ( ~ \stemDown c4 \stemDown d8 ) \stemDown c4 (
    \stemDown bes8 \stemDown d4 \stemDown es8 ) | % 116
    \stemDown es4. ( ~ \stemDown es4 \stemDown f8 \stemDown es4
    \stemDown d8 ) \stemDown g4. _\markup{ \italic {cresc.} } | % 117
    \stemDown g2. ~ \stemDown g4 \stemDown g,8 \stemDown g8 ( \stemDown
    a8 \stemDown bes8 ) \pageBreak | % 118
    \stemDown bes4. ( ~ _\> \stemDown bes4 \stemDown d8 \stemDown f4.
    _\! _\p \stemDown es4 \stemDown c8 ) \pageBreak | % 119
    \stemDown es2. ~ _\markup{ \italic {più} } _ "" \stemDown es4. (
    \stemDown d4. ) | \barNumberCheck #120
    \stemDown es2. ~ _\pp \stemDown es4. ( _\markup{ \italic {cresc.} }
    \stemDown d4 ) \stemDown bes16 ^\markup{ \bold\small {a. 2} } _\f
    \stemDown bes16 | % 121
    \stemDown es4 -. r8 r8 r8 \stemDown es,16 \stemDown es16 \stemDown
    bes'4 -. r8 r8 r8 \stemDown bes16 \stemDown bes16 | % 122
    \stemDown es8 -. _\sf r8 \stemDown es16 \stemDown es16 \stemDown d8
    -. _\sf r8 \stemDown d16 \stemDown d16 \stemDown c4 r8 r4 r8
    \pageBreak | % 123
    R1. | % 124
    \stemDown es2. ( ^ "I." _\> \stemDown bes2. ) | % 125
    \stemDown d4 _\! r8 r4 r8 \stemDown es4. ~ _\markup{ \italic {dolce}
        } \stemDown es8 ( \stemDown d8 ) \stemDown c8 -. | % 126
    \stemDown c8 ( \stemDown bes8 \stemDown d8 ) \stemDown f,4.
    \stemDown es'4. ~ \stemDown es8 ( \stemDown d8 ) \stemDown c8 -.
    \pageBreak | % 127
    r4 r8 \stemDown d4. ( ^\markup{ \italic {cantabile} } _\markup{
        \italic {cresc. poco a poco} } \stemDown es4. ~ \stemDown es8
    \stemDown c8 \stemDown f8 ) | % 128
    \stemDown f4. ( \stemDown es4. \stemDown d4. \stemDown c4. )
    \pageBreak | % 129
    \stemDown bes4. ( \stemDown d4 \stemDown c8 ) \stemDown a4. ~
    \stemDown a8 ( \stemDown bes8 ) \stemDown c8 -. | \barNumberCheck
    #130
    \stemDown d4. ( \stemDown f4 \stemDown es8 ) \stemDown c4. (
    \stemDown d4 ) \stemDown bes16 _\f ^\markup{ \bold\small {a. 2} }
    \stemDown bes16 | % 131
    \stemDown es4 -. r8 r8 r8 \stemDown es,16 \stemDown es16 \stemDown
    bes'4 -. r8 r8 r8 \stemDown bes16 \stemDown bes16 \pageBreak | % 132
    \stemDown es8 -. _\sf r8 \stemDown es16 \stemDown es16 \stemDown d8
    -. _\sf r8 \stemDown d16 \stemDown d16 \stemDown c4 r8 r4 r8 | % 133
    des1. ^ "I." _\> | % 134
    \stemDown as4 _\! _\p r8 r4 r8 r2. | % 135
    es'1. _\> | % 136
    \stemDown bes2. ~ _\! _\> \stemDown bes4. ~ _\! _\pp \stemDown bes8
    ( _\markup{ \italic {cresc.} } \stemDown c8 \stemDown des8 )
    \pageBreak | % 137
    \stemDown d4. ~ _\p \stemDown d8 ( \stemDown c8 ) \stemDown bes8 -.
    \stemDown bes8 ( \stemDown a8 \stemDown c8 ) \stemDown es8 (
    \stemDown d8 ) \stemDown c8 -. | % 138
    \stemDown c8 ( _\markup{ \italic {cresc.} } \stemDown bes8 \stemDown
    d8 ) \stemDown f,8 ( \stemDown bes8 \stemDown c16 \stemDown d16 )
    \stemDown es4 ( \stemDown d8 ) ~ \stemDown d16 ( _\> \stemDown c16
    \stemDown g'8 \stemDown f16 \stemDown a,16 ) | % 139
    \stemDown bes4 _\! _\p r8 r4 r8 r2. \pageBreak | \barNumberCheck
    #140
    \stemDown bes4. ~ _\markup{ \italic {dolce} } \stemDown bes8 (
    \stemDown c8 \stemDown d8 ) \stemDown d8 ( \stemDown c4 ) ~
    \stemDown c8 ( \stemDown a8 ) \stemDown f8 -. | % 141
    \stemDown f2. ~ \stemDown f2. ~ _\markup{ \italic {cresc.} } | % 142
    \stemDown f2. ~ \stemDown f2. ~ \pageBreak | % 143
    \stemDown f16 \stemDown f16 ( \stemDown g16 \stemDown a16 \stemDown
    bes16 \stemDown c16 ) \stemDown c4 r8 r16 \stemDown bes16 (
    \stemDown c16 \stemDown d16 \stemDown es16 \stemDown f16 ) \stemDown
    f4 r8 | % 144
    r2. \stemDown es4. ( _\markup{ \italic {cresc.} } \stemDown d4 _\>
    \stemDown f8 ) \pageBreak | % 145
    \stemDown f16 ( _\! _\p _\< \stemDown e,16 \stemDown f16 \stemDown g16
    \stemDown a16 \stemDown bes16 ) \stemDown c16 -. \stemDown g16 (
    \stemDown a16 \stemDown bes16 \stemDown c16 \stemDown d16 )
    \stemDown es4 _\! r8 r4 r8 | % 146
    r16 \stemDown e,16 ( _\< \stemDown f16 \stemDown g16 \stemDown a16
    \stemDown bes16 ) \stemDown c16 -. \stemDown g16 ( \stemDown a16
    \stemDown bes16 \stemDown c16 \stemDown d16 ) \stemDown es4 _\! r8 r4
    r8 \pageBreak | % 147
    r16 \stemDown f,16 ( _\markup{ \italic {cresc.} } \stemDown a16
    \stemDown bes16 \stemDown c16 \stemDown d16 ) \stemDown es4 _\ff r8
    \stemDown es4 _\markup{ \italic {dim.} } r8 \stemDown es4 r8 | % 148
    \stemDown es4 r8 \stemDown es4 r8 \stemDown es4 _\p r8 \stemDown es4
    _\pp \stemDown a,8 | % 149
    r8 r8 \stemDown bes8 _\markup{ \italic {cresc.} } r8 r8 \stemDown
    bes8 r8 r8 \stemDown bes8 r8 r8 \stemDown c8 | \barNumberCheck #150
    r8 r8 \stemUp bes8 r8 r8 \stemUp bes8 r8 r8 \stemUp bes8 _\markup{
        \italic {cresc.} } r8 r8 \stemDown <c es>8 _\f \pageBreak | % 151
    r2. \stemDown <bes d>4 _\p r8 r4 r8 | % 152
    R1. \pageBreak | % 153
    r2. r4 r8 r8 r8 \stemDown es8 _\pp ^ "I." \pageBreak | % 154
    \stemDown f,4. ( _\markup{ \italic {cresc.} } \stemDown bes4.
    \stemDown d4. \stemDown f4. ) | % 155
    \stemDown f2. _\f \stemDown f4. ( ~ _\f _\> \stemDown f4 \stemDown
    es8 ) | % 156
    \stemDown es4. ( _\! _\p \stemDown f4. \stemDown d4 ) \stemDown f,8
    ~ \stemDown f16 ( \stemDown g16 \stemDown a16 \stemDown bes16
    \stemDown c16 \stemDown d16 ) | % 157
    \stemDown es4. \stemDown f4 _\f r8 \stemDown d8 ( -. _\pp \stemDown
    d8 -. \stemDown d8 ) -. \stemDown d4 r8 \bar "|."
    }

PartPOneVoiceTwo =  \relative d' {
    \clef "treble" \time 4/4 \key bes \major s1*9 \pageBreak s1*10
    \pageBreak s1*4 \break s1 \bar "||"
    \pageBreak | % 25
    \time 3/4  \key d \major s4*21 \pageBreak s2*9 \pageBreak s4*15 \bar
    "||"
    \pageBreak | % 43
    \time 4/4  \key bes \major s1*4 \break s1*4 \pageBreak s1*5 \break
    s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 65
    \time 3/4  \key g \major s2*9 \pageBreak s8*11 \stemDown d8 | % 73
    \stemDown d'2. ~ | % 74
    \stemDown d2. ~ | % 75
    \stemDown d4. r8 r4 s1. \pageBreak s4*15 \bar "||"
    \time 4/4  \key es \major s1*2 \break s1*5 \pageBreak s1*5 \break
    s1*3 | % 98
    r4 s2. \bar "||"
    \pageBreak | % 99
    \time 12/8  \key bes \major f1. ~ | \barNumberCheck #100
    \stemDown f2. ~ \stemDown f4. ( ~ \stemDown f4 \stemDown c8 )
    \pageBreak | % 101
    \stemDown d4. \stemDown f4. \stemDown bes4. ~ \stemDown bes4. s2.
    \stemDown c4. s8*15 \pageBreak | % 104
    f,1. ~ | % 105
    \stemDown f2. ~ \stemDown f4 ( \stemDown bes8 ) \stemDown bes4. ~ | % 106
    \stemDown bes2. ~ \stemDown bes4 ( \stemDown f8 ) ~ \stemDown f4. ~
    \pageBreak | % 107
    \stemDown f2. ~ \stemDown f4. s4. | % 108
    r2. r4 r8 \stemDown f4. \pageBreak | % 109
    \stemDown g4. ( \stemDown a4. \stemDown f4. \stemDown bes4. ) s1.
    \pageBreak s1. | % 112
    r2. r8 r8 \stemDown g8 _\markup{ \italic {cresc.} } \stemDown g8 (
    \stemDown a8 \stemDown bes8 ) \pageBreak | % 113
    \stemDown bes4. ~ \stemDown bes4 r8 r2. s1. \pageBreak s2*9
    \pageBreak s1. \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*3
    \pageBreak s2*9 \pageBreak s2*15 \pageBreak s2*9 \pageBreak s2*9
    \pageBreak s1*3 \pageBreak s1*3 \pageBreak s2*9 | \barNumberCheck
    #150
    r2. s4 \stemDown bes8 s4. \pageBreak s1*3 \pageBreak s1. \pageBreak
    s1*6 \bar "|."
    }

PartPTwoVoiceOne =  \relative a'' {
    \clef "treble" \time 4/4 \key bes \major | % 1
    R1*9 \pageBreak | \barNumberCheck #10
    R1*10 \pageBreak | \barNumberCheck #20
    R1*4 \break | % 24
    R1 \bar "||"
    \pageBreak | % 25
    \time 3/4  \key d \major R2.*3 | % 28
    r4 r4 r8 \stemDown a8 ~ _\p ^ "I." | % 29
    \stemDown a4 ( \stemDown g8 ) r8 r8 \stemDown g8 ~ | \barNumberCheck
    #30
    \stemDown g8 ( ^\markup{ \italic {cresc.} } \stemDown fis4 )
    \stemDown fis8 ~ \stemDown fis16 ( \stemDown g16 \stemDown a16
    \stemDown fis16 ) | % 31
    \stemDown a8 ( \stemDown g4 ) \stemDown b16 ( _\> \stemDown g16
    \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown cis16 )
    \pageBreak | % 32
    \stemDown e4. ( _\! ^\markup{ \italic {morendo} } \stemUp g,8 )
    \stemDown fis8 ( \stemDown fis'8 ) ~ | % 33
    \stemDown fis8 ( _\p \stemDown e4 ) \stemDown e8 ~ \stemDown e16 (
    _\markup{ \italic {cresc.} } \stemDown fis16 \stemDown g16 \stemDown
    e16 ) | % 34
    \stemDown g8 ( \stemDown fis4 ) \stemDown fis8 ~ \stemDown fis16 (
    \stemDown g16 \stemDown a16 \stemDown fis16 ) | % 35
    \stemDown a8 ( \stemDown g4 ) \stemDown g8 ( -. \stemDown g8 -.
    \stemDown g8 ) -. | % 36
    \stemDown g8 ( \stemDown fis4 ) r8 r4 | % 37
    r8 \stemDown e4 _\markup{ \italic {cresc.} } \stemDown e8 ~
    \stemDown e16 ( \stemDown fis16 \stemDown g16 \stemDown e16 )
    \pageBreak | % 38
    \stemDown g8 ( \stemDown fis4 ) \stemDown fis8 ~ \stemDown fis16 (
    \stemDown g16 \stemDown a16 \stemDown fis16 ) | % 39
    \stemDown a8 ( \stemDown g4 ) \stemDown b16 ( _\> \stemDown g16
    \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown cis16 ) |
    \barNumberCheck #40
    \stemDown e4. ( _\! _\markup{ \italic {morendo} } \stemUp g,8 )
    \stemUp fis4 | % 41
    r4 \stemDown g'8 ( _\markup{ \italic {più} } _ "" \stemDown e8
    \stemDown d4 ) ~ | % 42
    \stemDown d2 ( _\pp \stemDown c4 ) ^\fermata \bar "||"
    \pageBreak | % 43
    \time 4/4  \key bes \major \stemDown bes4 r4 r2 | % 44
    R1*3 \break | % 47
    R1*4 \pageBreak | % 51
    R1*5 \break | % 56
    R1*5 \pageBreak | % 61
    R1*4 \bar "||"
    \pageBreak | % 65
    \time 3/4  \key g \major r8 \stemUp a4 _\markup{ \italic {cresc.} }
    ^ "I." \stemUp a8 ~ \stemUp a16 ( \stemUp b16 \stemUp c16 \stemUp a16
    ) | % 66
    \stemDown c8 ( \stemDown b4 ) \stemDown b8 ~ \stemDown b16 (
    \stemDown c16 \stemDown d16 \stemDown b16 ) | % 67
    \stemDown d8 ( \stemDown c4 ) \stemDown d8 ( -. \stemDown e8 -.
    \stemDown fis8 ) -. | % 68
    \stemDown a8 ( \stemDown g4 ) \stemDown g16 ( _\> \stemDown fis16
    \stemDown e16 \stemDown d16 \stemDown c16 \stemDown b16 ) | % 69
    \stemDown b8 ( _\! \stemUp a4 ) _\markup{ \italic {cresc.} } \stemUp
    a8 ~ \stemUp a16 ( \stemUp b16 \stemUp c16 \stemUp a16 ) |
    \barNumberCheck #70
    \stemDown c8 ( \stemDown b4 ) \stemDown b8 ~ \stemDown b16 (
    \stemDown c16 \stemDown d16 \stemDown b16 ) \pageBreak | % 71
    \stemUp d8 ( \stemUp c4 ) \stemDown <c e>16 ( _\> \stemDown <e c'>16
    \stemDown <d b'>16 \stemDown <c a'>16 \stemDown <b g'>16 \stemDown
    <a fis'>16 ) | % 72
    \stemDown <c a'>4. ( _\! _\markup{ \italic {morendo} } \stemDown <a
        c>8 ) \stemUp b8 ( \stemUp g'8 ) ~ | % 73
    \stemDown g8 ( ^ "I." \stemDown fis4 ) _\markup{ \italic {cresc.} }
    \stemDown fis8 ~ \stemDown fis16 ( \stemDown g16 \stemDown a16
    \stemDown fis16 ) | % 74
    \stemDown a8 ( \stemDown g4 ) \stemDown g8 ~ \stemDown g16 (
    \stemDown a16 \stemDown b16 \stemDown g16 ) | % 75
    \stemDown b8 ( \stemDown a4 ) \stemDown d,8 ( -. \stemDown e8 -.
    \stemDown fis8 ) -. | % 76
    \stemDown a8 ( \stemDown g4 ) \stemDown g16 ( _\> \stemDown fis16
    \stemDown e16 \stemDown d16 \stemDown c16 \stemDown b16 ) | % 77
    \stemDown g'8 ( _\! \stemDown fis4 ) _\markup{ \italic {cresc.} }
    \stemDown fis8 ~ \stemDown fis16 ( \stemDown g16 \stemDown a16
    \stemDown fis16 ) \pageBreak | % 78
    \stemDown a8 ( \stemDown g4 ) \stemDown g8 ~ \stemDown g16 (
    \stemDown a16 \stemDown b16 \stemDown g16 ) | % 79
    \stemDown b8 ( \stemDown a4 ) \stemDown c16 ( _\> \stemDown e,16
    \stemDown d16 \stemDown c16 \stemDown b16 \stemDown a16 ) |
    \barNumberCheck #80
    \stemDown <c a'>4. ( _\! _\markup{ \italic {morendo} } \stemDown <a
        c>8 ) \stemUp <g b>4 | % 81
    r4 \stemDown <c a'>8 ( _\markup{ \italic {più} } _ "" \stemDown <a'
        c>8 \stemDown <g bes>4 ) ~ ~ | % 82
    \stemDown <g bes>2 ( _\pp \stemDown <f as>8 ) r8 \bar "||"
    \time 4/4  \key es \major R1*2 \break | % 85
    R1*5 \pageBreak | \barNumberCheck #90
    R1*5 \break | % 95
    R1*4 \bar "||"
    \pageBreak | % 99
    \time 12/8  \key bes \major \stemUp d2. ( _ "" _\markup{ \italic
        {dolce} } \stemUp a2. | \barNumberCheck #100
    \stemUp bes2. \stemUp f'4. ~ \stemUp f4 \stemUp es8 ) \pageBreak | % 101
    \stemUp d4. ( _\< \stemUp f4. \stemUp bes,4. ~ _\! _\> \stemUp bes4
    \stemUp c8 ) | % 102
    \stemDown d4. ( _\! ^ "I." _\< \stemDown f4 \stemDown es8 \stemDown
    c4. ) _\! _\> r4 _\! r8 | % 103
    r4 r8 \stemDown bes4. ( ~ _\markup{ \italic {cresc.} } \stemDown bes4
    \stemUp a8 \stemDown g'8 _\> \stemDown f16 \stemDown es16 \stemDown
    c8 ) \pageBreak | % 104
    \stemDown c2. ( _\! _\p \stemDown bes4. ~ \stemDown bes4 \stemDown
    f'8 ) | % 105
    \stemDown f4. ( \stemDown es4. ~ \stemDown es4. \stemDown d4. ) | % 106
    \stemDown c4. ( ~ \stemDown c4 \stemDown d16 \stemDown es16 )
    \stemDown d4. ( \stemDown c4 \stemDown cis8 ) \pageBreak | % 107
    \stemDown cis4. ( ~ _\< \stemDown cis4 \stemDown d8 \stemDown d4. )
    _\! _\> r4 _\! r8 | % 108
    r2. r4 r8 \stemDown f4 ( \stemDown d8 ) \pageBreak | % 109
    \stemDown c2. ( \stemDown bes4. ~ \stemDown bes4 \stemDown f'8 ) |
    \barNumberCheck #110
    \stemDown f4. ( _\< \stemDown es4. ~ \stemDown es4. _\! _\>
    \stemDown d4 ) r8 _\! \pageBreak | % 111
    r2. r4 r8 \stemDown g4. _\markup{ \italic {cresc.} } | % 112
    \stemUp g2. ~ \stemUp g4 \stemDown <g, g'>8 _\markup{ \italic
        {cresc.} } \stemDown <g g'>8 ( \stemDown <a a'>8 \stemDown <bes
        bes'>8 ) \pageBreak | % 113
    \stemUp bes'4. ~ _\> \stemUp bes4 \stemUp d,8 ( \stemUp f4. _\! _\p
    \stemUp es4 \stemUp c8 ) | % 114
    \stemDown c4. ( ~ ^ "I." \stemDown c4 \stemDown d8 ) r8 \stemDown
    bes8 ( \stemDown a'16 \stemDown bes16 \stemDown c4 \stemDown es,8 )
    \pageBreak | % 115
    \stemDown es4. ( ~ \stemDown es4 \stemDown f8 ) \stemDown es4 (
    \stemDown d8 \stemDown bes'4 \stemDown c8 ) | % 116
    \stemDown c4. ( ~ \stemDown c4 \stemDown d8 \stemDown c4 \stemDown
    bes8 ) r8 r8 \stemDown bes,8 _\markup{ \italic {cresc.} } | % 117
    \stemDown g'2. ~ \stemDown g4 \stemUp g,8 \stemUp g8 ( \stemUp a8
    \stemUp bes8 ) \pageBreak | % 118
    \stemDown bes4. ( ~ _\> \stemDown bes4 \stemDown d8 \stemDown f4.
    _\! _\p \stemDown es4 \stemDown c8 ) \pageBreak | % 119
    \stemDown es4. ( _\markup{ \italic {più} } _ "" \stemDown c'4.
    \stemDown a4. \stemDown bes4. ) | \barNumberCheck #120
    \stemDown a4. ( _\pp \stemDown c4. \stemDown a4. _\markup{ \italic
        {cresc.} } \stemDown as4 ) \stemDown bes,16 ^\markup{
        \bold\small {a. 2} } _\f \stemDown bes16 | % 121
    \stemDown es4 -. r8 r8 r8 \stemUp <es, es'>16 \stemUp <es es'>16
    \stemDown <bes' bes'>4 -. r8 r8 r8 \stemDown <bes bes'>16 \stemDown
    <bes bes'>16 | % 122
    \stemDown <g' bes>8 -. _\sf r8 \stemDown <g bes>16 \stemDown <g bes>16
    \stemDown <f bes>8 -. _\sf r8 \stemDown <f bes>16 \stemDown <f bes>16
    \stemDown <f a>4 r8 r4 r8 \pageBreak | % 123
    R1.*2 | % 125
    r2. ^ "I." \stemDown es4. ~ _\markup{ \italic {dolce} } \stemDown es8
    ( \stemDown d8 ) \stemDown c8 -. | % 126
    \stemDown c8 ( \stemDown bes8 \stemDown d8 ) \stemUp f,4. \stemDown
    es'4. ~ \stemDown es8 ( \stemDown d8 ) \stemDown c8 -. \pageBreak | % 127
    r4 r8 \stemDown d4. ( ^\markup{ \italic {cantabile} } _\markup{
        \italic {cresc. poco a poco} } \stemDown es4. ~ \stemDown es8
    \stemDown c8 \stemDown f8 ) | % 128
    \stemDown f4. ( \stemDown es4. \stemDown d4. \stemDown c4. )
    \pageBreak | % 129
    \stemDown bes4. ( \stemDown d4 \stemDown c8 ) \stemUp a4. ~
    \stemDown a8 ( \stemDown bes8 ) \stemDown c8 -. | \barNumberCheck
    #130
    \stemDown d4. ( \stemDown f4 \stemDown es8 ) \stemDown c4. (
    \stemDown d4 ) \stemDown bes16 _\f ^\markup{ \bold\small {a. 2} }
    \stemDown bes16 | % 131
    \stemDown es4 -. r8 r8 r8 \stemUp <es, es'>16 \stemUp <es es'>16
    \stemDown <bes' bes'>4 -. r8 r8 r8 \stemDown <bes bes'>16 \stemDown
    <bes bes'>16 \pageBreak | % 132
    \stemDown <g' bes>8 -. _\sf r8 \stemDown <g bes>16 \stemDown <g bes>16
    \stemDown <f bes>8 -. _\sf r8 \stemDown <f bes>16 \stemDown <f bes>16
    \stemDown <f a>4 r8 r4 r8 | % 133
    R1. | % 134
    as1. ^ "I." _\> | % 135
    \stemDown es4 _\! _\p r8 r4 r8 r2. | % 136
    r2. r4 r8 \stemDown bes'4. ~ _\markup{ \italic {cresc.} } \pageBreak
    | % 137
    \stemDown bes4 ( _\p \stemDown f8 ) ~ \stemDown f4. ~ \stemDown f2.
    ~ | % 138
    \stemDown f4. ~ _\markup{ \italic {cresc.} } \stemDown f8 \stemDown
    d8 ( \stemDown es16 \stemDown f16 \stemDown g8 \stemDown a8
    \stemDown bes8 ) ~ \stemDown bes4 ( _\> \stemDown a8 ) | % 139
    \stemDown bes4 _\! _\p r8 r4 r8 r2. \pageBreak | \barNumberCheck
    #140
    r4 r8 \stemDown f4. ~ _\markup{ \italic {dolce} } \stemDown f4 (
    \stemDown c8 ) ~ \stemUp c8 ( \stemUp a8 ) \stemUp f8 -. | % 141
    \stemDown es16 \stemDown g'16 ( \stemDown f8 ) -. r8 r16 \stemDown g16
    ( \stemDown f8 ) -. r8 r16 _\markup{ \italic {cresc.} } \stemDown g16
    ( \stemDown f8 ) -. r8 r16 \stemDown bes16 ( \stemDown f8 ) -. r8 | % 142
    r16 \stemDown c'16 ( \stemDown f,8 ) -. r8 r16 \stemDown c'16 (
    \stemDown f,8 ) -. r8 r16 \stemDown c'16 ( \stemDown f,8 ) -. r8 r16
    \stemDown bes16 ( \stemDown f8 ) -. r8 \pageBreak | % 143
    r16 \stemUp f,16 ( \stemUp g16 \stemUp a16 \stemUp bes16 \stemUp c16
    ) \stemDown c4 r8 r16 \stemDown bes16 ( \stemDown c16 \stemDown d16
    \stemDown es16 \stemDown f16 ) \stemDown f4 r8 | % 144
    R1. \pageBreak | % 145
    r4 r8 r16 \stemDown g,16 ( _\p _\< \stemDown a16 \stemDown bes16
    \stemDown c16 \stemDown d16 ) \stemDown es16 -. _\! _\> \stemDown c'16
    ( \stemDown bes16 \stemDown a16 \stemDown g16 \stemDown f16 )
    \stemDown f4 _\! r8 | % 146
    r4 r8 r16 \stemDown g,16 ( _\< \stemDown a16 \stemDown bes16
    \stemDown c16 \stemDown d16 ) \stemDown es16 -. _\! _\> \stemDown c'16
    ( \stemDown bes16 \stemDown a16 \stemDown g16 \stemDown f16 )
    \stemDown f4 _\! r8 \pageBreak | % 147
    r16 \stemUp f,16 ( _\markup{ \italic {cresc.} } \stemUp a16 \stemUp
    bes16 \stemUp c16 \stemUp d16 ) \stemDown <c es>4 _\ff r8 \stemDown
    <es c'>4 _\markup{ \italic {dim.} } r8 \stemDown <es c'>4 r8 | % 148
    \stemDown <es c'>4 r8 \stemDown <es c'>4 r8 \stemDown <es c'>4 _\p r8
    \stemDown <es c'>4 _\pp r8 | % 149
    \stemDown <d bes'>4 _\markup{ \italic {cresc.} } r8 \stemDown <g
        bes>4 r8 \stemDown <d bes'>4 r8 \stemDown <a' c>4 r8 |
    \barNumberCheck #150
    \stemDown <d, bes'>4 r8 \stemDown <g bes>4 r8 \stemDown <d bes'>4 r8
    \stemDown <a' c>4 \stemDown <a c>8 _\f \pageBreak | % 151
    r2. \stemDown <d, bes'>4 _\p r8 r4 r8 | % 152
    R1. \pageBreak | % 153
    r2. r4 r8 r8 r8 \stemDown c'8 _\pp ^ "I." \pageBreak | % 154
    \stemDown d,4. ( _\markup{ \italic {cresc.} } \stemDown f4.
    \stemDown bes4. \stemDown d4. ) | % 155
    \stemDown d2. _\f \stemDown a4. ( ~ _\f _\> \stemDown a4 \stemDown c8
    ) | % 156
    \stemDown es,4. ( _\! _\p \stemDown f4. \stemDown d4. ) ~ \stemDown
    d16 ( \stemDown es16 \stemDown f16 \stemDown g16 \stemDown a16
    \stemDown bes16 ) | % 157
    \stemDown c4. \stemDown <c, a'>4 _\f r8 \stemDown <d bes'>8 ( -.
    _\pp \stemDown <d bes'>8 -. \stemDown <d bes'>8 ) -. \stemDown <d
        bes'>4 r8 \bar "|."
    }

PartPTwoVoiceTwo =  \relative g' {
    \clef "treble" \time 4/4 \key bes \major s1*9 \pageBreak s1*10
    \pageBreak s1*4 \break s1 \bar "||"
    \pageBreak | % 25
    \time 3/4  \key d \major s4*21 \pageBreak s2*9 \pageBreak s4*15 \bar
    "||"
    \pageBreak | % 43
    \time 4/4  \key bes \major s1*4 \break s1*4 \pageBreak s1*5 \break
    s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 65
    \time 3/4  \key g \major s2*9 \pageBreak | % 71
    r4 r8 s8*7 \stemDown g4 s4*15 \pageBreak s4*15 \bar "||"
    \time 4/4  \key es \major s1*2 \break s1*5 \pageBreak s1*5 \break
    s1*4 \bar "||"
    \pageBreak | % 99
    \time 12/8  \key bes \major R1. | \barNumberCheck #100
    r4 r8 \stemDown f4. ~ _\p \stemDown f4. ( ~ \stemDown f4 \stemDown
    es8 ) \pageBreak | % 101
    \stemDown d4. ( \stemDown f4. \once \override NoteHead.style = ##f
    \stemDown bes4 ) r8 r4 r8 s1*3 \pageBreak s2*9 \pageBreak s1*3
    \pageBreak s1*3 \pageBreak s1. | % 112
    r2. r8 r8 s2 \pageBreak | % 113
    \stemDown bes4. ~ \stemDown bes4 r8 r2. s1. \pageBreak s2*9
    \pageBreak s1. \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*3
    \pageBreak s2*9 \pageBreak s2*15 \pageBreak s2*9 \pageBreak s2*9
    \pageBreak s1*3 \pageBreak s1*3 \pageBreak | % 147
    r4 r8 s8*45 \pageBreak s1*3 \pageBreak s1. \pageBreak s1*6 \bar "|."
    }

PartPThreeVoiceOne =  \relative a'' {
    \clef "treble" \time 4/4 \key c \major \transposition bes | % 1
    r2 r4 r8 _\< \stemUp a8 ( ^\p | % 2
    \stemDown <d, g>4 ) ( \stemDown <b f'>4 ~ ~ \stemDown <b f'>4. _\!
    _\> \stemDown <c e>8 ) | % 3
    \stemDown <c e>4 _\! r4 r2 | % 4
    R1*2 | % 6
    r2 r4 r8 \stemDown <g d'>8 ( _\p | % 7
    \stemUp e'4 \stemUp g8 \stemUp f8 \stemUp d4 ) r4 | % 8
    R1*2 \pageBreak | \barNumberCheck #10
    R1 | % 11
    r2 r4 \stemUp <g, d'>8 ( \stemUp <f dis'>8 ) | % 12
    \stemUp <f dis'>4. ( \stemUp <e e'>8 ) \stemUp <e e'>4 r4 | % 13
    R1 | % 14
    r2 r4 \stemUp e'8 ( \stemUp g8 ) | % 15
    \stemDown <c, g'>4 ( \stemDown <d f>4 ~ ~ \stemDown <d f>8 \stemDown
    <c e>8 ) r4 | % 16
    R1*2 | % 18
    r2 r4 \stemDown <d f>8 ( _\markup{ \italic {dolce} } \stemDown <b d>8
    ) | % 19
    \stemUp <f d'>4. ( \stemDown <g e'>8 \stemUp <e c'>4 ) \stemDown <c'
        e>8 ( \stemDown <d f>8 ) \pageBreak | \barNumberCheck #20
    \stemUp f4. ( \stemUp g8 \stemUp f8 \stemUp e8 \stemUp a4 )
    _\markup{ \italic {cresc.} } | % 21
    \stemUp a2 ~ \stemUp a8 \stemUp a8 ( \stemUp b8 \stemUp c8 ) | % 22
    \stemUp c4. ( _\> \stemUp e,8 ) \stemDown <e g>4 ( _\! _\p \stemDown
    <d f>8 \stemDown <b d>8 ) | % 23
    \stemDown <b f'>2. _\markup{ \italic {più} } _ "" \stemDown <b e>4
    ~ ~ \break | % 24
    \stemUp e2 _\pp \stemUp e4. \stemUp gis,8 ~ \bar "||"
    \pageBreak | % 25
    \time 3/4  \key c \major \stemUp gis8 ( \stemUp fis8 ) r4 r4 | % 26
    R2. | % 27
    r4 r4 r8 \stemUp a8 ~ ^ "I." _\markup{ \italic {cresc.} } | % 28
    \stemUp a4 ( \stemUp gis8 ) r8 r4 | % 29
    R2.*3 \pageBreak | % 32
    \stemUp a4. ( ^\markup{ \italic {morendo} } \stemUp fis8 ) \stemUp e8
    \stemUp b'8 ~ _\p | % 33
    \stemUp b2. ~ | % 34
    \stemUp b2. ~ | % 35
    \stemUp b2. ~ | % 36
    \stemUp b2. ~ | % 37
    \stemUp b2. ~ _\! _ "" _\markup{ \italic {cresc.} } \pageBreak | % 38
    \stemUp b2. ~ | % 39
    \stemUp b2. ~ | \barNumberCheck #40
    \stemUp b2 ~ _\markup{ \italic {morendo} } \stemUp b8 ( \stemUp e8 )
    | % 41
    \stemDown <a, fis'>4. ( _\markup{ \italic {più} } _ "" \stemUp <fis
        a>8 ) \stemUp <e g>4 ~ ~ | % 42
    \stemUp <e g>2 ( _\pp \stemUp <d f>4 ) ^\fermata \bar "||"
    \pageBreak | % 43
    \time 4/4  \key c \major \stemUp e4 ( _\p \stemUp g2 \stemUp b4 | % 44
    \stemUp c4 \stemUp g2 ~ \stemUp g8 \stemUp f8 ) | % 45
    \stemUp <c e>4 ( \stemUp <d g>4 \stemUp <c c'>2 ) ~ ~ | % 46
    \stemUp <c c'>2 ~ ~ _\< \stemUp <c c'>8 ( \stemUp <b b'>8 _\!
    \stemDown <a' a'>8 _\> \stemDown <g g'>16 \stemDown <f f'>16 )
    \break | % 47
    \stemUp e'4 ( _\! _\< \stemUp g8 \stemUp f8 ) \stemUp d4 _\! _\> r4
    _\! | % 48
    r4 \stemUp g,2 ( \stemUp c4 ) | % 49
    \stemUp d2 \stemUp c2 ~ | \barNumberCheck #50
    \stemUp c2. ( \stemUp b4 ) \pageBreak | % 51
    \stemUp b4. ( _\< \stemUp c8 ) \stemUp c4 ( _\! _\> \stemUp d8
    \stemUp dis8 ) | % 52
    \stemUp <f, dis'>4. ( _\! _\< \stemUp <e e'>8 ) \stemUp <e e'>4 _\!
    _\> \stemUp g4 ( | % 53
    \stemUp a4 _\! \stemUp b4 \stemUp c4 \stemUp g4 | % 54
    \stemUp a4 _\< \stemUp b4 ~ \stemUp b4 _\! _\> \stemUp c8 \stemUp g'8
    ) | % 55
    \stemUp g4 ( _\! _\< \stemUp f8 \stemUp a16 \stemUp f16 ) _\! _\>
    \stemUp f8 ( \stemUp e8 ) r4 _\! _\markup{ \italic {cresc.} } \break
    | % 56
    \stemUp c2. ( \stemUp d4 ) ~ | % 57
    \stemUp d8 ( _\> \stemUp e4. ) ~ \stemUp e4 ( _\! ^\p _\p \stemUp d8
    \stemUp f,8 ) | % 58
    \stemUp <d f>4. ( \stemUp <c e>8 ) \stemUp <c e>4 \stemDown <d' f>8
    ( \stemDown <b d>8 ) | % 59
    \stemUp <f d'>4. ( \stemDown <g e'>8 \stemUp <e c'>4 ) \stemDown <c'
        e>8 ( \stemDown <d f>8 ) | \barNumberCheck #60
    \stemUp f4. ( \stemUp g8 \stemUp f8 \stemUp e8 ) \stemUp a4
    _\markup{ \italic {cresc.} } \pageBreak | % 61
    \stemUp a2 ~ \stemUp a8 \stemUp a8 ( \stemUp b8 \stemUp c8 ) | % 62
    \stemUp c4. ( _\> \stemUp e,8 ) \stemDown <e g>4 ( _\! _\p \stemDown
    <d f>8 \stemDown <b d>8 ) | % 63
    \stemDown <b f'>2. _\markup{ \italic {più} } _ "" \stemDown <b e>4
    ~ ~ | % 64
    \stemUp e2 ~ _\pp \stemUp e4. ( \stemUp cis8 ) ~ \bar "||"
    \pageBreak | % 65
    \time 3/4  \key c \major \stemUp <a cis>8 ( \stemUp <gis b>8 ) r2 | % 66
    R2.*5 \pageBreak | % 71
    R2.*7 \pageBreak | % 78
    R2.*3 | % 81
    \stemDown <d' b'>4. ( _\markup{ \italic {più} } _ "" \stemDown <b
        d>8 ) \stemDown <a c>4 ~ ~ | % 82
    \stemDown <a c>2 ( _\pp \stemDown <g bes>8 \stemDown <c bes'>8 )
    \bar "||"
    \time 4/4  \key f \major \stemUp a'2 ( ^\markup{ \italic {dolce} }
    \stemUp e2 | % 84
    \stemUp f2 ) \stemUp c4. ( \stemUp bes16 \stemUp g16 ) \break | % 85
    \stemUp f8 \stemUp f'8 ( \stemUp c'4 ) ~ \stemUp c8 \stemUp c8 (
    \stemUp bes4 ) ~ | % 86
    \stemUp bes8 \stemUp bes8 ( \stemUp a4 ) ~ \stemUp a8 ( \stemUp g8
    \stemUp a8 \stemUp bes8 | % 87
    \stemUp c4. ) \stemUp a8 ~ \stemUp a8 \stemUp a8 ( \stemUp g4 ) ~ | % 88
    \stemUp g8 \stemUp g8 ( \stemUp f4 ) ~ \stemUp f8 ( \stemUp e8
    \stemUp f8 \stemUp g8 ) | % 89
    \stemUp as8 ( \stemUp f8 \stemUp c'4. ) \stemUp c8 ( \stemUp bes4 )
    \pageBreak | \barNumberCheck #90
    \stemUp as2 \stemUp es2 | % 91
    \stemUp des2 ~ \stemUp des8 ( \stemUp c8 \stemUp des8 \stemUp es8 )
    | % 92
    \stemUp es8 ( \stemUp des8 ) \stemUp des4. \stemUp es8 ( -. \stemUp
    f8 -. \stemUp ges8 ) -. | % 93
    \stemUp ges8 ( _\< \stemUp f8 \stemUp as8 _\! _\> \stemUp des,8 )
    \stemDown <des f>4 ( _\! \stemDown <c es>4 ) | % 94
    \stemUp bes'8 ( _\< \stemUp as8 \stemUp des8 _\! _\> \stemUp f,8 )
    \stemDown <f as>4 ( _\! \stemDown <es ges>4 ) \break | % 95
    <es ges>1 | % 96
    \stemDown <as, f'>4 r4 r2 | % 97
    r2 _\markup{ \italic {cresc.} } r4 \stemUp c'4 ~ ^\markup{ \italic
        {cresc.} } | % 98
    \stemDown <es, c'>4 \stemDown <es c'>2 \stemDown <e c'>4 ~ ~ \bar
    "||"
    \pageBreak | % 99
    \time 12/8  \key c \major \stemDown <e c'>4. ~ ~ _ "" _\markup{
        \italic {dolce} } \stemDown <e c'>4 ( \stemDown <g, g'>8 )
    \stemDown <g g'>4. ( \stemDown <f f'>4. ) | \barNumberCheck #100
    \stemUp <e e'>2. ( \stemUp <b b'>4. ) \stemUp <d d'>4. \pageBreak | % 101
    \stemUp <e e'>4. ( _\< \stemUp <d d'>4. \stemUp <c c'>2. ) ~ ~ _\!
    _\> | % 102
    \stemUp <c c'>2. ~ ~ _\! _\< \stemUp <c c'>4 ( _\! _\> \stemUp <b
        b'>8 \stemDown <a' a'>8 \stemDown <g g'>8 \stemDown <b d>8 ) _\!
    _\p | % 103
    \stemDown <c e>4. ( _\< \stemDown <e g>4 \stemDown <d f>8 ) \stemUp
    d4. \stemDown <b d>4 ( _\! _\> \stemUp <g b>8 ) \pageBreak | % 104
    \stemUp <g, g'>4. _\! \stemUp <g g'>2. \stemUp <c c'>4. | % 105
    \stemUp <d d'>4. \stemUp <d d'>4. ~ ~ \stemUp <d d'>4. \stemUp <c
        c'>4. ~ ~ | % 106
    \stemUp <c c'>4. \stemUp <c c'>2. \stemUp <b b'>4. ~ ~ \pageBreak | % 107
    \stemUp <b b'>4. ~ ~ _\< \stemUp <b b'>4 ( \stemUp <c c'>8 )
    \stemDown <c c'>8 ( _\! _\> \stemDown <g' g'>8 ) \stemDown <g e'>8
    \stemDown <g d'>4 ( \stemUp <f dis'>8 ) | % 108
    \stemUp <f dis'>4. ~ ~ _\! _\< \stemUp <f dis'>4 ( \stemUp <e e'>8 )
    \stemUp <e e'>4. _\! _\> \stemUp <c c'>4. ( \pageBreak | % 109
    \stemUp <a a'>4. _\! \stemUp <b b'>4. \stemUp <g g'>4. \stemUp <c
        c'>4. ) | \barNumberCheck #110
    \stemUp <a a'>4. ( _\< \stemUp <b b'>4. ~ ~ \stemUp <b b'>4. _\! _\>
    \stemUp <c c'>4 ) \stemDown <c' g'>8 \pageBreak | % 111
    \stemUp g'4. ~ _\! _\< \stemUp g16 \stemUp f16 \stemUp e16 \stemUp f16
    \stemUp a16 \stemUp f16 \stemUp f4 ( _\! _\> \stemDown <c e>8 ) r4
    _\! r8 | % 112
    r2. \stemUp d2. ^\markup{ \italic {cresc.} } \pageBreak | % 113
    \stemDown <c e>4. ~ ~ _\> \stemDown <c e>4 \stemUp <e, e'>8 (
    \stemDown <g g'>4. _\! _\p \stemDown <f f'>4 \stemUp <d d'>8 ) | % 114
    \stemUp <d d'>4. ( ~ ~ \stemUp <d d'>4 \stemUp <e e'>8 ) r8 \stemUp
    <c c'>8 \stemUp <b' d>16 \stemUp <c e>16 \stemDown <d f>4 \stemUp
    <f, d'>8 \pageBreak | % 115
    \stemUp <f d'>4. ( ~ ~ \stemUp <f d'>4 \stemDown <g e'>8 ) \stemUp
    <f d'>4 ( \stemUp <e c'>8 \stemDown <c' e>4 \stemDown <d f>8 ) | % 116
    \stemDown <d f>4. ( ~ ~ \stemDown <d f>4 \stemDown <e g>8 \stemDown
    <d f>4 \stemDown <c e>8 ) \stemDown <c a'>4. _\markup{ \italic
        {cresc.} } | % 117
    \stemUp a'2. ~ \stemUp a4 \stemDown <a, a'>8 \stemDown <a a'>8 (
    \stemDown <b b'>8 \stemDown <c c'>8 ) \pageBreak | % 118
    \stemDown <c c'>4. ( ~ ~ _\> \stemDown <c c'>4 \stemUp <e, e'>8
    \stemDown <g g'>4. _\! _\p \stemDown <f f'>4 \stemUp <d d'>8 )
    \pageBreak | % 119
    \stemUp f'2. ~ _\markup{ \italic {più} } _ "" \stemUp f4. ( \stemUp
    e4. ) | \barNumberCheck #120
    \stemUp f2. ~ _\pp \stemUp f4. ( _\markup{ \italic {cresc.} }
    \stemUp e4 ) \stemUp <c, c'>16 _\f \stemUp <c c'>16 | % 121
    \stemDown <f f'>4 -. r8 r8 r8 \stemDown <f f'>16 \stemDown <f f'>16
    \stemDown <c' c'>4 -. r8 r8 r8 \stemDown <c c'>16 \stemDown <c c'>16
    | % 122
    \stemDown <f a>8 -. _\sf r8 \stemDown <f a>16 \stemDown <f a>16
    \stemDown <e g>8 -. _\sf r8 \stemDown <e g>16 \stemDown <e g>16
    \stemDown <d g>4 r8 r4 r8 \pageBreak | % 123
    R1. | % 124
    r2. \stemDown as'2. ( ^ "I." _\> | % 125
    \stemDown e4. _\! _\markup{ \italic {dolce} } \stemDown c4. )
    \stemDown b2. | % 126
    \stemDown c2. \stemDown b4. ~ \stemDown b8 ( \stemDown c8 )
    \stemDown d8 -. \pageBreak | % 127
    \stemUp <e, e'>2. _\markup{ \italic {cresc. poco a poco} } \stemUp
    <b b'>2. | % 128
    \stemUp <c c'>4. ( \stemUp <d d'>4. \stemUp <e e'>4. \stemDown <f
        f'>4. ) \pageBreak | % 129
    \stemDown <g g'>2. ~ ~ \stemDown <g g'>4 ( \stemDown <f f'>8 ) ~ ~
    \stemDown <f f'>8 ( \stemDown <e e'>8 ) \stemDown <d d'>8 -. |
    \barNumberCheck #130
    \stemUp <e e'>4. ( \stemDown <g g'>4 \stemDown <f f'>8 ) \stemUp d'4.
    ( \stemUp c4 ) \stemUp <c, c'>16 _\f \stemUp <c c'>16 | % 131
    \stemDown <f f'>4 -. r8 r8 r8 \stemDown <f f'>16 \stemDown <f f'>16
    \stemDown <c' c'>4 -. r8 r8 r8 \stemDown <c c'>16 \stemDown <c c'>16
    \pageBreak | % 132
    \stemDown <f a>8 -. _\sf r8 \stemDown <f a>16 \stemDown <f a>16
    \stemDown <e g>8 -. _\sf r8 \stemDown <e g>16 \stemDown <e g>16
    \stemDown <d g>4 r8 r4 r8 | % 133
    <g bes>1. _\> | % 134
    \stemUp g4. ( _\! _\> \stemUp f4. ) \stemUp g2. | % 135
    c1. _\> | % 136
    \stemUp as4. ( _\! _\> \stemUp g4. ) ~ \stemUp g2. ~ _\! _ ""
    _\markup{ \italic {cresc.} } \pageBreak | % 137
    \stemUp g8 ( _\p \stemUp e,8 ^ "I." \stemUp g8 \stemDown c8
    \stemDown d8 \stemDown e8 ) \stemDown f4. ~ \stemDown f8 ( \stemDown
    e8 ) \stemDown d8 ^. | % 138
    \stemDown d8 ( _\markup{ \italic {cresc.} } \stemDown c8 \stemDown e8
    ) \stemDown g,8 ( \stemDown c8 \stemDown d16 \stemDown e16 )
    \stemDown f4 ( \stemDown e8 ) ~ \stemDown e16 ( _\> \stemDown d16
    \stemDown a'8 \stemDown g16 \stemDown b,16 ) | % 139
    \stemDown c4 _\! _\p r8 r4 r8 r2. \pageBreak | \barNumberCheck #140
    \stemDown c4. ~ _\markup{ \italic {dolce} } \stemDown c8 ( \stemDown
    d8 \stemDown e8 ) \stemDown e8 ( \stemDown d4 ) ~ \stemDown d8 (
    \stemDown b8 ) \stemDown g8 -. | % 141
    \stemUp f16 \stemUp a16 ( \stemUp g8 ) -. r8 r16 \stemUp a16 (
    \stemUp g8 ) -. r8 r16 _\markup{ \italic {cresc.} } \stemUp a16 (
    \stemUp g8 ) -. r8 r16 \stemUp c16 ( \stemUp g8 ) -. r8 | % 142
    r16 \stemDown d'16 ( \stemDown g,8 ) -. r8 r16 \stemDown d'16 (
    \stemDown g,8 ) -. r8 r16 \stemDown d'16 ( \stemDown g,8 ) -. r8 r16
    \stemUp c16 ( \stemUp g8 ) -. r8 \pageBreak | % 143
    <g g'>1. ~ ~ | % 144
    \stemDown <g g'>4. \stemDown <d' d'>4. ~ ~ \stemDown <d d'>4.
    \stemDown <c c'>4 ( ~ _\> \stemDown <c e>8 ) \pageBreak | % 145
    \stemUp g'4. ( _\! _\p _\< \stemUp f4. ~ \stemUp f4. _\! _\> \stemUp
    e4 \stemUp g8 ) | % 146
    \stemUp g4. ( _\! _\< \stemUp f4. ~ \stemUp f4. _\! _\> \stemUp e4
    \stemUp g8 ) \pageBreak | % 147
    \stemDown <b, g'>4 ~ ~ _\! _\markup{ \italic {cresc.} } \stemDown <b
        g'>16 ( \stemDown <d f>16 ) \stemDown <d f>4 _\ff r8 \stemDown
    <d f>4 _\markup{ \italic {dim.} } r8 \stemDown <d f>4 r8 | % 148
    \stemDown <d f>4 r8 \stemDown <d f>4 r8 \stemDown <d f>4 _\p r8
    \stemDown <d f>4 _\pp r8 | % 149
    \stemDown <c e>4 _\markup{ \italic {cresc.} } r8 \stemDown <c a'>4 r8
    \stemDown <e g>4 r8 \stemDown <d f>4 r8 | \barNumberCheck #150
    \stemDown <c e>4 r8 \stemDown <c a'>4 r8 \stemDown <e g>4 r8
    \stemDown <d f>4 \stemDown <d b'>8 _\f \pageBreak | % 151
    r2. \stemDown <e c'>4 _\p r8 r4 \stemDown <b as'>8 ~ ~ | % 152
    \stemDown <b as'>8 ( _\markup{ \italic {dim.} } \stemDown <c g'>8 )
    r8 r8 r8 \stemDown <b f'>8 ~ ~ \stemDown <b f'>8 ( \stemDown <c e>8
    ) r8 r8 r8 \stemDown <b f'>8 ~ ~ \pageBreak | % 153
    \stemDown <b f'>8 ( _\markup{ \italic {sempre} } _ "" \stemDown <c
        e>8 ) r8 r8 r8 \stemDown <b f'>8 ~ ~ \stemDown <b f'>8 (
    \stemDown <c e>8 ) \stemDown <b f'>8 ~ ~ \stemDown <b f'>8 (
    \stemDown <c e>8 ) \stemDown <d f>8 \pageBreak | % 154
    \stemDown <e g>4. ( _\markup{ \italic {cresc.} } \stemUp <e, g>4.
    \stemUp <g c>4. \stemDown <c e>4. ) | % 155
    \stemDown <c e>2. _\f \stemUp <g b>2. ~ ~ _\f _\> | % 156
    \stemUp <g b>2. ( ~ _\! _\p \stemUp <g c>4. ) \stemUp <e g>16 (
    \stemUp <f a>16 \stemUp <g b>16 \stemUp <a c>16 \stemUp <b d>16
    \stemUp <c e>16 ) | % 157
    \stemDown <d f>4. \stemDown <b g'>4 _\f r8 \stemDown <c e>8 ( -.
    _\pp \stemDown <c e>8 -. \stemDown <c e>8 ) -. \stemDown <c e>4 r8
    \bar "|."
    }

PartPThreeVoiceTwo =  \relative e'' {
    \clef "treble" \time 4/4 \key c \major \transposition bes s2 r8
    \stemDown e8 ( _\p \stemDown d4 ) ~ s1*5 | % 7
    \stemDown g,8 \stemDown c8 \stemDown e8 \stemDown d8 \stemDown d8
    \stemDown b,8 ( \stemDown a'8 \stemDown g8 ) | % 8
    \stemDown g4 r4 r2 s1 \pageBreak s4*19 \stemDown c4 s1*5 \pageBreak
    | \barNumberCheck #20
    \stemDown d4. ( \stemDown e8 \stemDown d8 \stemDown c8 \stemDown a8
    \stemDown f'8 ) | % 21
    \stemDown f8 \stemDown c8 \stemDown c8 \stemDown c8 \stemDown c4. (
    \stemDown b16 \stemDown a16 ) | % 22
    \stemDown a8 \stemDown g8 \stemDown c8 \stemDown c8 s1. \break | % 24
    b1 ~ \bar "||"
    \pageBreak | % 25
    \time 3/4  \key c \major \stemDown b4 s1*5 \pageBreak | % 32
    r4 r4 r8 \stemDown gis8 ~ | % 33
    \stemDown gis8 \stemDown fis8 ~ \stemDown fis2 ~ ^\markup{ \italic
        {cresc.} } | % 34
    \stemDown fis8 \stemDown gis8 ~ \stemDown gis2 ~ | % 35
    \stemDown gis8 \stemDown a8 ~ \stemDown a2 ~ | % 36
    \stemDown a8 \stemDown gis8 ~ \stemDown gis2 ~ _\> | % 37
    \stemDown gis8 \stemDown fis8 ~ \stemDown fis2 ~ \pageBreak | % 38
    \stemDown fis8 \stemDown gis8 ~ \stemDown gis2 ~ | % 39
    \stemDown gis8 \stemDown a8 ~ \stemDown a2 ~ | \barNumberCheck #40
    \stemDown a4. \stemDown fis8 ( \stemDown e8 \stemDown gis8 ) s1.
    \bar "||"
    \pageBreak | % 43
    \time 4/4  \key c \major \stemDown c,4 ( \stemDown e4 \stemDown d2 | % 44
    \stemDown c2 \stemDown d2 ) s1*2 \break | % 47
    \stemDown e8 ( \stemDown c'8 \stemDown e8 \stemDown d8 ) \stemDown d4
    \stemDown d,4 ~ | % 48
    \stemDown d2 ( \stemDown c2 ) | % 49
    \stemDown d4 ( \stemDown g2 ) \stemDown a4 ~ | \barNumberCheck #50
    \stemDown a4. ( \stemDown f8 ) \stemDown g2 \pageBreak | % 51
    \stemDown g2 \stemDown g4 ( ~ \stemDown g8 \stemDown f8 ) s2.
    \stemDown g4 ~ | % 53
    g1 ~ | % 54
    \stemDown g2 ~ \stemDown g4. \stemDown c8 | % 55
    \stemDown c4 ( \stemDown d4 ) ~ \stemDown d8 ( \stemDown c8 )
    \stemDown a4 ~ \break | % 56
    \stemDown a2 ( \stemDown c,4 \stemDown d4 ) ~ | % 57
    \stemDown d8 ( \stemDown e4. ) ~ \stemDown e8 ( \stemDown g8
    \stemDown f8 \stemDown d8 ) s1*2 | \barNumberCheck #60
    \stemDown d'4. ( \stemDown e8 \stemDown d8 \stemDown c8 \stemDown a8
    \stemDown f'8 ) \pageBreak | % 61
    \stemDown f8 \stemDown c8 \stemDown c8 \stemDown c8 \stemDown c4. (
    \stemDown b16 \stemDown a16 ) | % 62
    \stemDown a8 ( \stemDown g8 \stemDown c8 ) \stemDown c8 s1. | % 64
    \stemDown b2 ( \stemDown gis4 \stemDown a4 ) ~ \bar "||"
    \pageBreak | % 65
    \time 3/4  \key c \major s2*9 \pageBreak s4*21 \pageBreak s4*15 \bar
    "||"
    \time 4/4  \key f \major \stemDown c4 ( \stemDown a4 \stemDown bes2
    ) | % 84
    \stemDown a4. \stemDown a8 \stemDown a8 ( \stemDown g4 ) \stemDown g8
    \break | % 85
    \stemDown a4 r8 \stemDown c8 \stemDown g'4. \stemDown g8 | % 86
    \stemDown c,4. \stemDown f8 \stemDown f8 ( \stemDown e8 \stemDown f8
    \stemDown g8 ) | % 87
    \stemDown f8 ( \stemDown f,8 \stemDown a8 \stemDown c8 ) ~ \stemDown
    c4. \stemDown bes8 ( | % 88
    \stemDown a4. ) \stemDown a8 ( \stemDown as8 \stemDown g8 \stemDown
    f8 \stemDown e'8 ) | % 89
    \stemDown f4. \stemDown f8 \stemDown f4. \stemDown e8 \pageBreak |
    \barNumberCheck #90
    \stemDown f4. \stemDown c,8 \stemDown c'4. \stemDown es,8 | % 91
    \stemDown as4. \stemDown des,8 \stemDown as'8 \stemDown ges8
    \stemDown as8 \stemDown as8 | % 92
    \stemDown as8 \stemDown as8 \stemDown as4 \stemDown f8 ( -.
    \stemDown des'8 -. \stemDown des8 -. \stemDown des8 ) -. | % 93
    \stemDown des4 ( \stemDown f8 \stemDown as,8 ) s2 | % 94
    \stemDown des4 ( \stemDown f8 \stemDown des8 ) s2 \break s1. r4 r8
    \stemDown des,8 | % 97
    \stemDown es4 \stemDown es'2 \stemDown es4 ~ s1 \bar "||"
    \pageBreak | % 99
    \time 12/8  \key c \major s1*3 \pageBreak s4*15 \stemDown d4. s4.
    \pageBreak s2*9 \pageBreak s1*3 \pageBreak s1*3 \pageBreak | % 111
    \stemDown c4. \stemDown d4. ~ \stemDown d4 ( s2 | % 112
    r4 r8 \stemDown c4. ~ _\markup{ \italic {cresc.} } \stemDown c2.
    \pageBreak s1*3 \pageBreak s1*3 | % 117
    \stemDown c4. \stemDown a4. ~ \stemDown a4 s2 \pageBreak s1.
    \pageBreak | % 119
    \stemDown b4. \stemDown d4. \stemDown b4. \stemDown c4. ) |
    \barNumberCheck #120
    \stemDown b4. \stemDown d4. \stemDown b4. \stemDown bes4 s8*25
    \pageBreak s1*6 \pageBreak s1*3 \pageBreak s4*9 \stemDown d,8 (
    \stemDown b'4 ) ( \stemDown bes4 ) s8*13 \pageBreak s1*3 | % 134
    \stemDown es4. ( \stemDown d4 \stemDown f8 ) ~ \stemDown f4. (
    \stemDown e4. ) _\! | % 135
    \stemDown as2. ~ \stemDown as4. \stemDown f4. ~ | % 136
    \stemDown f2. \stemDown es2. \pageBreak | % 137
    \stemDown e8 s8*35 \pageBreak s2*9 \pageBreak s1*3 \pageBreak | % 145
    \stemDown b4. \stemDown b2. \stemDown c4. | % 146
    \stemDown b4. \stemDown b2. \stemDown c4. \pageBreak s1*6 \pageBreak
    s1*3 \pageBreak s1. \pageBreak s1*6 \bar "|."
    }

PartPFourVoiceOne =  \relative g' {
    \clef "bass" \time 4/4 \key bes \major | % 1
    r4 r8 _\< \stemUp g8 ( ^\p \stemDown <a, f'>2 ) ~ ~ | % 2
    \stemDown <a f'>4 \stemDown <c es>4 ~ ~ \stemDown <c es>4. ( _\! _\>
    \stemDown <bes d>8 ) | % 3
    \stemDown <bes d>4 _\! r4 r2 | % 4
    R1*2 | % 6
    r2 r4 r8 \stemDown <f, a'>8 ( _\p | % 7
    \stemUp bes'4 \stemUp d8 \stemUp c8 \stemUp bes8 ) \stemUp a8 (
    \stemUp g'8 \stemUp f8 ) | % 8
    \stemUp f4 r4 r2 | % 9
    R1 \pageBreak | \barNumberCheck #10
    R1 | % 11
    r2 r4 \stemDown <f, a>4 | % 12
    \stemDown <f a>4. ( \stemDown <f bes>8 ) \stemDown <f bes>4 r4 | % 13
    R1 | % 14
    r2 r4 \stemDown <bes, bes'>4 | % 15
    \stemUp g'4 ( \stemUp a4 ~ \stemUp a8 \stemUp bes8 ) r4 | % 16
    R1*2 | % 18
    r2 r4 \stemDown <c es>8 ( _\markup{ \italic {dolce} } \stemDown <a
        c>8 ) | % 19
    \stemDown <a c>4. ( \stemDown <f d'>8 \stemDown <d bes'>4 )
    \stemDown <bes' d>8 ( \stemDown <c es>8 ) \pageBreak |
    \barNumberCheck #20
    \stemUp es4. ( \stemUp f8 \stemUp es8 ) \stemUp g,8 \stemUp es'8
    _\markup{ \italic {cresc.} } \stemUp g,8 | % 21
    \stemDown <es g>8 \stemDown <es g>8 \stemDown <es g>8 \stemDown <es
        g>8 \stemDown <e g>8 \stemDown <e g>8 \stemDown <e g>8 \stemDown
    <e g>8 | % 22
    \stemUp g8 ( _\> \stemUp f8 ) \stemUp f8 \stemUp f8 \stemUp f,8 _\!
    _\p \stemUp <f f'>4 \stemDown <f' a>8 | % 23
    \stemDown <f a>2. _\markup{ \italic {più} } _ "" \stemDown <fis a>4
    ~ ~ \break | % 24
    <fis a>1 ~ ~ _\pp \bar "||"
    \pageBreak | % 25
    \time 3/4  \key d \major \stemUp a4 r4 _\markup{ \italic {cresc.} }
    r4 | % 26
    r4 r4 r8 \stemUp d8 ~ | % 27
    \stemUp d4 \stemUp cis8 r8 r4 | % 28
    r4 r4 _\> r8 \stemUp fis8 ~ ^\p | % 29
    \stemUp fis8 ( _\! _\p \stemUp e4 ) r8 r8 \stemUp g8 ~ _\p |
    \barNumberCheck #30
    \stemUp g8 ( \stemUp fis4 ) \stemUp fis,8 ~ \stemUp fis16 ( \stemUp
    g16 \stemUp a16 \stemUp fis16 ) | % 31
    \stemUp a8 \stemUp g8 ~ \stemUp g8 \stemUp b16 ( _\> \stemUp g'16
    \stemDown <a, fis'>16 \stemDown <g e'>16 \stemDown <fis d'>16
    \stemDown <e cis'>16 ) \pageBreak | % 32
    \stemDown <g e'>4. ( _\! ^\markup{ \italic {morendo} } \stemDown <e
        g>8 ) \stemUp fis8 ( \stemUp d'8 ) ~ | % 33
    \stemDown <d, d'>4 ( _\p \stemDown <cis cis'>4 \stemDown <a a'>4 ) ~
    ~ _\markup{ \italic {cresc.} } | % 34
    \stemDown <a a'>4 ( \stemDown <d d'>4 \stemDown <a a'>4 ) ~ ~ | % 35
    \stemDown <a a'>4 ( \stemDown <e' e'>4 \stemDown <a, a'>4 ) ~ ~ | % 36
    \stemDown <a a'>4 ( \stemDown <fis' fis'>4 _\> \stemDown <a, a'>4 )
    ~ ~ | % 37
    \stemDown <a a'>4 ( _\! _\markup{ \italic {cresc.} } \stemDown <cis
        cis'>4 \stemDown <a a'>4 ) ~ ~ \pageBreak | % 38
    \stemDown <a a'>4 ( \stemDown <d d'>4 \stemDown <a a'>4 ) ~ ~ | % 39
    \stemDown <a a'>4 ( \stemDown <e' e'>4 _\> \stemDown <a, a'>4 ) ~ ~
    | \barNumberCheck #40
    \stemDown <a a'>4 _\! _\markup{ \italic {morendo} } \stemDown <a a'>4
    ( \stemDown <d d'>4 ) | % 41
    r4 \stemDown <a a'>4 ( _\markup{ \italic {più} } _ "" \stemDown
    <bes bes'>4 ) ~ ~ | % 42
    \stemDown <bes bes'>4 _\pp \stemUp <f f'>2 ^\fermata \bar "||"
    \pageBreak | % 43
    \time 4/4  \key bes \major \stemUp bes4 r4 r2 | % 44
    R1*2 | % 46
    r2 r4 \stemUp es'8 ( \stemUp d16 \stemUp c16 ) \break | % 47
    \stemUp bes2 ~ \stemUp bes8 ( \stemUp a8 \stemUp g'8 \stemUp f8 ) | % 48
    \stemUp f4 r4 r2 | % 49
    R1*2 \pageBreak | % 51
    r2 r4 \stemDown <f, a>8 \stemDown <f a>8 | % 52
    \stemDown <f a>4. ( _\< \stemDown <f bes>8 ) _\! _\> \stemDown <f
        bes>4 r4 _\! | % 53
    R1 | % 54
    r2 r4 r8 \stemDown <d f>8 | % 55
    \stemUp g4 _\< \stemUp a4 ~ \stemUp a8 ( _\! _\> \stemUp bes8 ) r4
    \break | % 56
    R1*2 | % 58
    r2 _\! r4 \stemDown <c es>8 ( \stemDown <a c>8 ) | % 59
    \stemDown <a c>4. ( \stemDown <f d'>8 \stemDown <d bes'>4 )
    \stemDown <bes' d>8 ( \stemDown <c es>8 ) | \barNumberCheck #60
    \stemDown <c es>4. ( \stemDown <d f>8 \stemDown <c es>8 \stemDown
    <bes d>8 ) \stemDown <es, es'>8 _\markup{ \italic {cresc.} }
    \stemDown <es g>8 \pageBreak | % 61
    \stemDown <es g>8 \stemDown <es g>8 \stemDown <es g>8 \stemDown <es
        g>8 \stemDown <e g>8 \stemDown <e g>8 \stemDown <e g>8 \stemDown
    <e g>8 | % 62
    \stemUp g8 ( _\> \stemUp f8 ) \stemUp f8 \stemUp f8 \stemUp f,8 _\!
    _\p \stemUp <f f'>4 \stemDown <f' a>8 | % 63
    \stemDown <f a>2. _\markup{ \italic {più} } _ "" \stemDown <fis a>4
    ~ ~ | % 64
    \stemDown <fis a>2. _\pp \stemDown <g b>4 ~ ~ \bar "||"
    \pageBreak | % 65
    \time 3/4  \key g \major \stemUp b8 ( \stemUp a4 ) _\markup{ \italic
        {cresc.} } \stemUp a8 ~ \stemUp a16 ( \stemUp b16 \stemUp c16
    \stemUp a16 ) | % 66
    \stemDown c8 ( ^ "I." \stemDown b4 ) \stemDown b8 ~ \stemDown b16 (
    \stemDown c16 \stemDown d16 \stemDown b16 ) | % 67
    \stemDown d8 ( \stemDown c4 ) \stemDown d8 ( -. \stemDown e8 -.
    \stemDown fis8 ) -. | % 68
    \stemDown a8 ( \stemDown g4 ) \stemDown g16 ( _\> \stemDown fis16
    \stemDown e16 \stemDown d16 \stemDown c16 \stemDown b16 ) | % 69
    \stemDown b8 ( _\! ^ "I." \stemDown a4 ) _\markup{ \italic {cresc.}
        } \stemDown a8 ~ \stemDown a16 ( \stemDown b16 \stemDown c16
    \stemDown a16 ) | \barNumberCheck #70
    \stemDown c8 ( \stemDown b4 ) \stemDown b8 ~ \stemDown b16 (
    \stemDown c16 \stemDown d16 \stemDown b16 ) \pageBreak | % 71
    \stemDown d8 ( \stemDown c4 ) \stemDown e16 ( _\> \stemDown c16
    \stemDown b16 \stemDown a16 \stemDown g16 \stemDown fis16 ) | % 72
    \stemUp c'4. ( _\! _\markup{ \italic {morendo} } \stemUp a8 )
    \stemUp g8 ( \stemUp b8 ) ~ | % 73
    \stemDown <g b>8 ( \stemDown <fis a>4 ) _\markup{ \italic {cresc.} }
    \stemDown <fis a>8 ~ ~ \stemDown <fis a>16 ( \stemDown <g b>16
    \stemDown <a c>16 \stemDown <fis a>16 ) | % 74
    \stemDown <a c>8 ( \stemDown <g b>4 ) \stemDown <g b>8 ~ ~ \stemDown
    <g b>16 ( \stemDown <a c>16 \stemDown <b d>16 \stemDown <g b>16 ) | % 75
    \stemDown <b d>8 ( \stemDown <a c>4 ) \stemDown <a c>8 ( -.
    \stemDown <a c>8 -. \stemDown <a c>8 ) -. | % 76
    \stemDown <a c>8 ( \stemDown <g b>4 ) \stemDown <b g'>16 ( _\>
    \stemDown <d fis>16 \stemDown <c e>16 \stemDown <b d>16 \stemDown <a
        c>16 \stemDown <g b>16 ) | % 77
    \stemDown <g b>8 ( _\! \stemDown <fis a>4 ) _\markup{ \italic
        {cresc.} } \stemDown <fis a>8 ~ ~ \stemDown <fis a>16 (
    \stemDown <g b>16 \stemDown <a c>16 \stemDown <fis a>16 ) \pageBreak
    | % 78
    \stemDown <a c>8 ( \stemDown <g b>4 ) \stemDown <g b>8 ~ ~ \stemDown
    <g b>16 ( \stemDown <a c>16 \stemDown <b d>16 \stemDown <g b>16 ) | % 79
    \stemDown <b d>8 ( \stemDown <a c>4 ) \stemUp e'16 ( _\> \stemUp c16
    \stemUp b16 \stemUp a16 \stemUp g16 \stemUp fis16 ) |
    \barNumberCheck #80
    \stemUp a4. ~ _\! _\markup{ \italic {morendo} } \stemDown <a c>8
    \stemDown <g b>8 ( \stemDown <b g'>8 ) | % 81
    \stemDown <c a'>4. ( _\markup{ \italic {più} } _ "" \stemDown <a c>8
    ) \stemDown <g bes>4 ~ ~ | % 82
    \stemDown <g bes>2 ( _\pp \stemDown <f as>8 \stemDown <d' f>8 ) \bar
    "||"
    \time 4/4  \key es \major \stemUp g4 ( _\markup{ \italic {dolce} }
    \stemUp es4 \stemUp f2 ) | % 84
    \stemDown es4. ^ "I." \stemDown es8 \stemDown es4 ( \stemDown d4 )
    \break | % 85
    \stemDown es4 r8 \stemDown g8 \stemDown f4. \stemDown f8 ~ | % 86
    \stemDown f8 \stemDown f8 ( \stemDown es4. ) \stemDown as8 (
    \stemDown g8 \stemDown f8 | % 87
    \stemDown es8 \stemDown bes8 ) \stemDown bes4. \stemDown bes8
    \stemDown bes4 ~ | % 88
    \stemDown bes8 \stemDown bes8 \stemDown bes4 ~ \stemDown bes8 (
    \stemDown as'8 \stemDown ges8 \stemDown f8 ) | % 89
    \stemDown es8 ( \stemDown ges8 ) \stemDown ges4 ( \stemDown f4. )
    \stemDown f8 \pageBreak | \barNumberCheck #90
    \stemDown es4 r4 r2 | % 91
    R1 | % 92
    \stemDown ces2 \stemDown as8 ( -. \stemDown as8 -. \stemDown ges8 -.
    \stemDown fes8 ) -. | % 93
    \stemDown fes8 ( _\< \stemDown ges8 ) \stemDown ges8 _\! _\>
    \stemDown ges8 \stemDown ges4 _\! \stemDown ges4 | % 94
    \stemUp ces,2 _\< \stemUp ges4 ( _\! \stemDown ges'4 ) \break | % 95
    ges1 | % 96
    \stemUp ces,4 r4 r4 r8 \stemDown ces'8 | % 97
    \stemDown ges4 _\markup{ \italic {cresc.} } \stemDown ges2 \stemDown
    ges4 ~ | % 98
    \stemUp ges4 \stemUp <ges, ges'>2 _\markup{ \italic {cresc.} }
    \stemUp <f f'>4 ~ ~ \bar "||"
    \pageBreak | % 99
    \time 12/8  \key bes \major \stemUp f'4. _ "" _\markup{ \italic
        {dolce} } \stemUp d'4. ( \stemUp a2. | \barNumberCheck #100
    \stemUp bes2. \stemUp f4. ~ \stemUp f4 \stemUp es8 ) \pageBreak | % 101
    \stemUp d4. ( _\< \stemUp f4. \stemUp bes4. ~ _\! _\> \stemUp bes4
    \stemUp c8 ) | % 102
    \stemUp d4. ( _\! _\< \stemUp f4 \stemUp es8 \stemUp c4. ) _\! _\>
    \stemUp c4. ( | % 103
    \stemDown <bes d>4. ) ( _\! _\< \stemDown <d f>4 \stemDown <c es>8 )
    \stemUp c4. \stemDown <es, c'>4. _\! _\> \pageBreak | % 104
    \stemUp c'2. ( _\! \stemUp bes4. ~ \stemUp bes4 \stemUp f'8 ) | % 105
    \stemUp f4. ( \stemUp es4. ~ \stemUp es4. \stemUp d4. ) | % 106
    \stemUp c4. ( ~ \stemUp c4 \stemUp d16 \stemUp es16 ) \stemUp d4. (
    \stemUp c4 \stemUp cis8 ) \pageBreak | % 107
    \stemUp cis4. ( ~ _\< \stemUp cis4 \stemUp d8 ) \stemDown <bes, d'>8
    _\! _\> \stemDown <bes' d>8 \stemDown <bes d>8 \stemDown <a c>4 (
    \stemDown <f a>8 ) | % 108
    \stemDown <f a>4. ~ ~ _\! _\< \stemDown <f a>4 ( \stemDown <f bes>8
    ) \stemDown <bes, bes'>4. _\! _\> \stemDown <bes d'>4. ( \pageBreak
    | % 109
    \stemUp c'2. _\! \stemUp bes4. ~ \stemUp bes4 \stemUp f'8 ) |
    \barNumberCheck #110
    \stemUp f4. ( _\< \stemUp es4. ~ \stemUp es4. _\! _\> \stemUp d4 )
    \stemUp f,8 \pageBreak | % 111
    \stemUp g4. _\! _\< \stemUp a4. ~ \stemUp a4 _\! _\> \stemUp bes8
    \stemUp g4. _\! _\markup{ \italic {cresc.} } | % 112
    \stemUp g2. ~ \stemUp g4 \stemUp g8 \stemUp g8 ( \stemUp a8 \stemUp
    bes8 ) \pageBreak | % 113
    \stemUp bes4. ~ _\> \stemUp bes4 \stemUp d8 ( \stemUp f4. _\! _\p
    \stemUp es4 \stemUp c8 ) | % 114
    \stemUp c4. ( ~ \stemUp c4 \stemUp d8 ) r8 \stemDown <bes, bes'>8 (
    \stemDown <a' c>16 \stemDown <bes d>16 \stemDown <c es>4 \stemDown
    <es, c'>8 ) \pageBreak | % 115
    \stemDown <es c'>4. ( ~ ~ \stemDown <es c'>4 \stemDown <f d'>8 )
    \stemDown <es c'>4 ( \stemDown <d bes'>8 \stemDown <bes' d>4
    \stemDown <c es>8 ) | % 116
    \stemDown <c es>4. ( ~ ~ \stemDown <c es>4 \stemDown <d f>8
    \stemDown <c es>4 \stemDown <bes d>8 ) \stemDown <es, g>4. _\markup{
        \italic {cresc.} } | % 117
    \stemUp g2. ~ \stemUp g4 \stemUp g8 \stemUp g8 ( \stemUp a8 \stemUp
    bes8 ) \pageBreak | % 118
    \stemUp bes4. ( ~ _\> \stemUp bes4 \stemUp d8 \stemUp f4. _\! _\p
    \stemUp es4 \stemUp c8 ) \pageBreak | % 119
    \stemUp es2. ~ _\markup{ \italic {più} } _ "" \stemUp es4. (
    \stemUp d4. ) | \barNumberCheck #120
    \stemUp es2. ~ _\pp \stemUp es4. ( _\markup{ \italic {cresc.} }
    \stemUp d4 ) \stemUp bes,16 _\f \stemUp bes16 | % 121
    \stemDown es4 -. ^\markup{ \bold\small {a. 2} } r8 r8 r8 \stemDown
    es'16 \stemDown es16 \stemDown bes4 -. r8 r8 r8 \stemDown bes16
    \stemDown bes16 | % 122
    \stemDown es,8 -. _\sf r8 \stemDown es16 \stemDown es16 \stemDown
    bes'8 -. _\sf r8 \stemDown d,16 \stemDown d16 \stemDown f4 r8 r4 r8
    \pageBreak | % 123
    r2. \stemDown f'2. ( ^ "I." _\> | % 124
    \stemDown c2. ) \stemDown es2. ( _\! _\> | % 125
    \stemDown d2. ) _\! _\markup{ \italic {dolce} } \stemDown c2. | % 126
    \stemDown bes2. \stemDown c4. ~ \stemDown c8 ( \stemDown d8 )
    \stemDown es8 -. \pageBreak | % 127
    \stemUp bes,2. _\markup{ \italic {cresc. poco a poco} } ^\markup{
        \bold\small {a. 2} } \stemUp f2. | % 128
    \stemUp d4. ( \stemUp f4. \stemUp bes4. \stemUp c4. ) \pageBreak | % 129
    \stemDown d4. ( \stemDown f4 \stemDown es8 \stemUp c4 ) \stemDown <c
        c'>8 ~ ~ \stemDown <c c'>8 ( \stemDown <bes bes'>8 ) \stemDown
    <a a'>8 -. | \barNumberCheck #130
    \stemDown <bes bes'>4. ( \stemDown <d d'>4 \stemDown <c c'>8 )
    \stemDown <a' c>4. \stemDown <as bes>4 \stemUp bes,16 _\f ^\markup{
        \bold\small {a. 2} } \stemUp bes16 | % 131
    \stemDown es4 -. r8 r8 r8 \stemDown es16 \stemDown es16 \stemDown
    bes'4 -. r8 r8 r8 \stemDown bes16 \stemDown bes16 \pageBreak | % 132
    \stemDown es8 -. _\sf r8 \stemDown es,16 \stemDown es16 \stemDown
    bes'8 -. _\sf r8 \stemDown bes,16 \stemDown bes16 \stemDown f'4 r8 r4
    r8 | % 133
    r2. \stemDown <des' f>2. ~ ~ _\p _\> | % 134
    \stemUp f4. ( _\! _\> \stemUp es4. ~ \stemUp es4. \stemUp d4. ) _\!
    | % 135
    ges1. ~ _\> | % 136
    \stemUp ges4. ( _\! _\> \stemUp f4. ) ~ \stemUp f2. ~ _\! _ ""
    _\markup{ \italic {cresc.} } \pageBreak | % 137
    \stemUp f8 ( _\p \stemUp d,8 ^ "I." \stemUp f8 \stemDown bes8
    \stemDown c8 \stemDown d8 ) \stemDown es4. ~ \stemDown es8 (
    \stemDown d8 ) \stemDown c8 ^. | % 138
    \stemDown c8 ( _\markup{ \italic {cresc.} } \stemDown bes8 \stemDown
    d8 ) \stemDown f,8 ( \stemDown bes8 \stemDown c16 \stemDown d16 )
    \stemDown es4 ( \stemDown d8 ) ~ \stemDown d16 ( _\> \stemDown c16
    \stemDown g'8 \stemDown f16 \stemDown a,16 ) | % 139
    \stemDown bes4 _\! _\p r8 r4 r8 r2. \pageBreak | \barNumberCheck
    #140
    \stemDown bes4. ~ _\markup{ \italic {dolce} } \stemDown bes8 (
    \stemDown c8 \stemDown d8 ) \stemDown d8 ( \stemDown c4 ) ~
    \stemDown c8 ( \stemDown a8 ) \stemDown f8 -. | % 141
    \stemDown c'2. ( \stemDown bes4. ) ~ _\markup{ \italic {cresc.} }
    \stemDown bes4 ( \stemDown f'8 ) | % 142
    \stemDown f4. ( \stemDown es4. ) ~ \stemDown es4. \stemDown d16 (
    \stemDown f,16 \stemDown a16 \stemDown bes16 \stemDown c16 \stemDown
    d16 ) \pageBreak | % 143
    \stemDown d4 ( \stemDown c8 ) \stemDown c16 ( \stemDown f,16
    \stemDown g16 \stemDown a16 \stemDown bes16 \stemDown c16 )
    \stemDown c4 ( \stemDown bes8 ) ~ \stemDown bes16 \stemDown bes16 (
    \stemDown c16 \stemDown d16 \stemDown es16 \stemDown f16 ) | % 144
    \stemDown f4. ( \stemDown es4. ) ~ \stemDown es4. \stemDown d4 ( _\>
    \stemDown f8 ) \pageBreak | % 145
    \stemDown f16 ( _\! _\p _\< \stemDown e,16 \stemDown f16 \stemDown g16
    \stemDown a16 \stemDown bes16 ) \stemDown c16 -. \stemDown g16 (
    \stemDown a16 \stemDown bes16 \stemDown c16 \stemDown d16 )
    \stemDown es4 _\! r8 r4 r8 | % 146
    r16 \stemDown e,16 ( _\< \stemDown f16 \stemDown g16 \stemDown a16
    \stemDown bes16 ) \stemDown c16 -. \stemDown g16 ( \stemDown a16
    \stemDown bes16 \stemDown c16 \stemDown d16 ) \stemDown es4 _\! r8 r4
    r8 \pageBreak | % 147
    r16 \stemUp f,16 ( _\markup{ \italic {cresc.} } \stemUp a16 \stemUp
    bes16 \stemUp c16 \stemUp d16 ) \stemDown <c es>4 _\ff r8 \stemDown
    <c es>4 _\markup{ \italic {dim.} } r8 \stemDown <c es>4 r8 | % 148
    \stemDown <c es>4 r8 \stemUp <f,, f'>4 r8 \stemUp <f f'>4 _\p r8
    \stemUp <f f'>4 _\pp r8 | % 149
    \stemUp <g g'>4 _\markup{ \italic {cresc.} } r8 \stemUp <es es'>4 r8
    \stemUp <f f'>4 r8 \stemUp <f f'>4 r8 | \barNumberCheck #150
    \stemUp <g g'>4 r8 \stemUp <es es'>4 r8 \stemUp <f f'>4 r8 \stemUp
    <f f'>4 \stemDown <c'' es>8 _\f \pageBreak | % 151
    r2. \stemDown <bes d>4 _\p r8 r4 \stemDown es8 ~ ^ "I." | % 152
    \stemDown es8 ( _\markup{ \italic {dim.} } \stemDown d8 ) r8 r8 r8
    \stemDown ges8 ~ \stemDown ges8 ( \stemDown f8 ) r8 r8 r8 \stemDown
    <a, es'>8 ~ ~ \pageBreak | % 153
    \stemDown <a es'>8 ( _\markup{ \italic {sempre} } _ "" \stemDown
    <bes d>8 ) r8 r8 r8 \stemDown <ges a>8 ~ ~ \stemDown <ges a>8 (
    \stemDown <f bes>8 ) \stemDown <ges a>8 ~ ~ \stemDown <ges a>8 (
    \stemDown <f bes>8 ) \stemDown <c es>8 \pageBreak | % 154
    \stemDown <d f>4. ( _\markup{ \italic {cresc.} } \stemDown <f bes>4.
    \stemDown <bes d>4. \stemDown <d f>4. ) | % 155
    \stemDown <bes d>2. _\f \stemDown <f a>2. ~ ~ _\f _\> | % 156
    \stemDown <f a>2. ( ~ _\! _\p \stemDown <f bes>4. ) \stemDown <d f>16
    ( \stemDown <es g>16 \stemDown <f a>16 \stemDown <g bes>16 \stemDown
    <a c>16 \stemDown <bes d>16 ) | % 157
    \stemDown <c es>4. \stemDown <a f'>4 _\f r8 \stemDown <bes d>8 ( -.
    _\pp \stemDown <bes d>8 -. \stemDown <bes d>8 ) -. \stemDown <bes d>4
    r8 \bar "|."
    }

PartPFourVoiceTwo =  \relative bes {
    \clef "bass" \time 4/4 \key bes \major | % 1
    r8 \stemDown bes8 ( _\p \stemDown a4 ) ~ s2*11 | % 7
    \stemDown f,4 \stemDown f'4 \stemDown f4 r4 | % 8
    R1 s1 \pageBreak s1*5 | % 15
    \stemDown c2 \stemDown f8 ( \stemDown g8 ) s4*17 \pageBreak |
    \barNumberCheck #20
    \stemDown c4. ( \stemDown d8 \stemDown c8 ) \stemDown g8 \stemDown
    es8 \stemDown es8 s1 | % 22
    \stemDown e8 ( \stemDown f8 ) \stemDown f8 \stemDown f8 \stemDown f,8
    s8*11 \break s1 \bar "||"
    \pageBreak | % 25
    \time 3/4  \key d \major \stemDown fis'8 ( \stemDown e8 ) \stemDown
    cis4 ( \stemDown a4 ) ~ | % 26
    \stemDown a4 ( \stemDown d4 \stemDown a4 ) ~ | % 27
    \stemDown a4 ( \stemDown e'4 \stemDown a,4 ) ~ | % 28
    \stemDown a4 ( \stemDown fis'4 \stemDown a,4 ) ~ | % 29
    \stemDown a4 ( \stemDown cis4 \stemDown a4 ) ~ | \barNumberCheck #30
    \stemDown a4 ( \stemDown d4 ^\markup{ \italic {cresc.} } \stemDown a4
    ) ~ | % 31
    \stemDown a4 \stemDown e'8 ( \stemDown g16 \stemDown b16 s4
    \pageBreak s2 \stemDown d,4 ~ s4*15 \pageBreak s4*15 \bar "||"
    \pageBreak | % 43
    \time 4/4  \key bes \major \stemDown bes4 s2*7 r8 \stemDown f8
    \break | % 47
    \stemDown f4 r8 \stemDown f'8 \stemDown f4 r4 | % 48
    R1 s1*2 \pageBreak s1*4 | % 55
    \stemDown c2 \stemDown f8 \stemDown g8 ) s4 \break s1*5 \pageBreak
    s1 | % 62
    \stemDown e8 ( \stemDown f8 ) \stemDown f8 \stemDown f8 \stemDown f,8
    s8*19 \bar "||"
    \pageBreak | % 65
    \time 3/4  \key g \major \stemDown g'8 ( \stemDown fis8 ) r4 r4
    s4*15 \pageBreak s2. | % 72
    r4 r4 r8 \stemDown g8 ~ s4*15 \pageBreak s8*9 \stemDown c16 (
    \stemDown e16 \stemDown d16 \stemDown c16 \stemDown b16 \stemDown a16
    ) | \barNumberCheck #80
    \stemDown c4. ~ s8*15 \bar "||"
    \time 4/4  \key es \major \stemDown es4 r4 r2 s1 \break s1*5
    \pageBreak s4*17 s2. _\! _\> \break s1*3 | % 98
    r4 s2. \bar "||"
    \pageBreak | % 99
    \time 12/8  \key bes \major f,,1. ~ | \barNumberCheck #100
    \stemDown f2. ~ \stemDown f4. \stemDown a4. \pageBreak | % 101
    \stemDown bes4. \stemDown a4. \stemDown g2. | % 102
    \stemDown f4. \stemDown f'4. \stemDown f4. \stemDown a4. ( s2.
    \stemDown c4. s4. \pageBreak | % 104
    \stemDown es,2. \stemDown d2. | % 105
    \stemDown a2. \stemDown bes4. ) \stemDown g'4 \stemDown g,8 | % 106
    \stemDown es4. \stemDown g4. \stemDown f4. \stemDown f4. ~
    \pageBreak | % 107
    \stemDown f2. s4*9 \pageBreak | % 109
    \stemDown es'2. \stemDown d2. | \barNumberCheck #110
    \stemDown c2. ~ \stemDown c4. ( \stemDown bes4 ) \stemDown d8
    \pageBreak | % 111
    \stemDown c2. \stemDown f4 \stemDown g8 \stemDown es4 \stemDown es,8
    | % 112
    \stemDown es2. \stemDown e2. \pageBreak | % 113
    \stemDown f2. \stemDown f2. ~ | % 114
    \stemDown f4. \stemDown f'4 ( \stemDown bes,8 ) s2. \pageBreak s1*3
    | % 117
    \stemDown es4. \stemDown es,4. \stemDown e4. \stemDown e'4. ~
    \pageBreak | % 118
    \stemDown e8 \stemDown f4 ~ \stemDown f8 \stemDown f,4 \stemDown f4.
    \stemDown f4. \pageBreak | % 119
    \stemDown a'4. ( \stemDown c4. \stemDown a4. \stemDown bes4. ) |
    \barNumberCheck #120
    \stemDown a4. ( \stemDown c4. \stemDown a4. \stemDown as4 )
    \stemDown bes,16 \stemDown bes16 s1*3 \pageBreak s1*6 \pageBreak
    s1*3 \pageBreak s2*9 \pageBreak s1*3 | % 134
    \stemDown des'4. ( \stemDown c4. \stemDown ces4. \stemDown bes4. ) ~
    | % 135
    \stemDown bes4. \stemDown es2. ~ \stemDown es4. ~ | % 136
    \stemDown es2. \stemDown des2. \pageBreak | % 137
    \stemDown d8 s8*35 \pageBreak s2*9 \pageBreak s1*3 \pageBreak s1*3
    \pageBreak | % 147
    r4 r8 s8*45 \pageBreak s1*3 \pageBreak s1. \pageBreak s1*6 \bar "|."
    }

PartPFiveVoiceOne =  \relative g' {
    \clef "treble" \time 4/4 \key c \major \transposition bes, | % 1
    R1*5 | % 6
    r2 r4 r8 \stemDown <g d'>8 ( _\p | % 7
    \stemUp e'4 \stemUp g8 \stemUp f8 \stemUp d4 ) r4 | % 8
    R1*2 \pageBreak | \barNumberCheck #10
    R1 | % 11
    r2 r4 \stemUp <g,, g'>4 | % 12
    \stemUp <g g'>2 \stemUp <c g'>4 r4 | % 13
    R1 | % 14
    r2 r4 \stemDown <c' e>8 ( \stemDown <e g>8 ) | % 15
    \stemUp g4 \stemDown <d f>4 ~ ~ \stemDown <d f>8 ( \stemDown <c e>8
    ) \stemDown <c f>8 r8 | % 16
    R1*2 | % 18
    r2 r4 \stemUp <g, g'>8 ( _\markup{ \italic {dolce} } \stemUp <g' g'>8
    ) | % 19
    \stemDown <g g'>4. ( \stemUp <c, c'>8 ) \stemUp <c c'>4 \stemUp <g
        g'>8 ( \stemUp <g' g'>8 ) \pageBreak | \barNumberCheck #20
    \stemDown <g g'>4. ( \stemUp <c, c'>8 ) \stemUp <c c'>8 \stemDown
    <c' e>8 \stemDown <c f>8 _\markup{ \italic {cresc.} } \stemDown <c
        f>8 | % 21
    \stemDown <c f>8 \stemDown <c f>8 \stemDown <c f>8 \stemDown <c f>8
    \stemDown <c d>8 \stemDown <c d>8 \stemDown <c d>8 \stemDown <c d>8
    | % 22
    \stemDown <c d>8 ( _\> \stemDown <c e>8 ) \stemDown <c e>8 \stemDown
    <c e>8 \stemDown <c e>8 ( _\! _\p \stemDown <e g>8 \stemDown <d f>8
    \stemDown <g, d'>8 ) | % 23
    \stemUp f'2. _\markup{ \italic {più} } _ "" \stemUp <e, e'>4 ~ ~
    \break | % 24
    \stemUp <e e'>4 _\pp \stemUp <e e'>2. ~ ~ \bar "||"
    \pageBreak | % 25
    \time 3/4  \key c \major \stemUp <e e'>8 r8 r4 r4 | % 26
    R2.*6 \pageBreak | % 32
    R2.*6 \pageBreak | % 38
    R2.*3 | % 41
    r4 r4 \stemDown <c' e>4 ~ ~ _ "" | % 42
    \stemDown <c e>2 ( _\pp \stemDown <g d'>4 ) ^\fermata \bar "||"
    \pageBreak | % 43
    \time 4/4  \key c \major \stemDown <c e>4 -. r8 \stemDown <c e>8 -.
    \stemDown <g d'>4 -. r8 \stemDown <g d'>8 -. | % 44
    \stemUp <g c>4 -. r8 \stemUp <g c>8 -. \stemDown <g d'>4 -. r8
    \stemDown <g d'>8 -. | % 45
    \stemDown <g e'>4 -. _\markup{ \italic {sempre staccato} } r8
    \stemDown <g d'>8 -. \stemUp <c, c'>4 -. r8 \stemUp <c c'>8 -. | % 46
    \stemDown <c' e>4 -. r8 \stemDown <c e>8 -. \stemDown <g d'>8 -. r8
    r8 \stemDown <g d'>8 -. \break | % 47
    \stemUp e'4 ( _\< \stemUp g8 _\! _\> \stemUp f8 ) \stemDown <g, d'>4
    ^. _\! r8 \stemDown <g d'>8 ^. | % 48
    \stemDown <g d'>4 -. r8 \stemDown <g d'>8 -. \stemUp <g c>4 -. r8
    \stemUp <g c>8 -. | % 49
    \stemDown <d' f>4 ^. r8 \stemDown <g, d'>8 ^. \stemUp <c, c'>4 _. r8
    \stemUp c'8 -. | \barNumberCheck #50
    \stemDown <c d>4 -. r8 \stemDown <c d>8 -. \stemDown <c e>4 -. r8
    \stemDown <g g'>8 -. \pageBreak | % 51
    \stemDown <g g'>4 -. r8 \stemDown <c e>8 -. _\< \stemUp <c e>8 -.
    \stemUp <c e>8 -. _\! \stemUp <g d'>8 -. _\> \stemUp <g, g'>8 -. | % 52
    \stemUp <g g'>2 _\! _\< \stemUp <c g'>4 _\! r8 \stemDown <c' e>8 ^.
    | % 53
    \stemDown <g d'>4 -. r8 \stemDown <g d'>8 -. \stemUp <g c>4 -. r8
    \stemDown <g g'>8 -. | % 54
    \stemDown <g f'>4 -. r8 \stemDown <g f'>8 -. \stemDown <g f'>8 -. r8
    \stemDown <g e'>8 -. \stemDown <g g'>8 -. | % 55
    \stemDown <c g'>4 -. _\< \stemDown <d f>4 ~ ~ \stemDown <d f>8 ( _\!
    _\> \stemDown <c e>8 ) \stemDown <c f>8 _\! _\markup{ \italic
        {cresc.} } \stemDown <c f>8 \break | % 56
    \stemDown <c f>4 -. r8 \stemDown <c f>8 -. \stemDown <c d>4 -. r8
    \stemDown <c d>8 -. | % 57
    \stemDown <c d>8 -. _\> \stemDown <c e>8 -. r8 \stemDown <c e>8 -.
    \stemDown <c e>4 -. _\! _\p r8 \stemDown <g d'>8 -. | % 58
    \stemDown <g d'>4 -. r8 \stemUp <e c'>8 -. \stemUp <e c'>8 ( -.
    \stemUp <g, g'>8 ) -. \stemUp <g g'>8 ( \stemUp <g' g'>8 ) | % 59
    \stemDown <g g'>4. ( \stemUp <c, c'>8 ) \stemUp <c c'>4 \stemUp <g
        g'>8 ( \stemUp <g' g'>8 ) | \barNumberCheck #60
    \stemDown <g g'>4. ( \stemUp <c, c'>8 ) \stemUp <c c'>8 \stemUp <c'
        e>8 \stemUp <c f>8 _\markup{ \italic {cresc.} } \stemUp <c f>8
    \pageBreak | % 61
    \stemDown <c f>8 \stemDown <c f>8 \stemDown <c f>8 \stemDown <c f>8
    \stemDown <c d>8 \stemDown <c d>8 \stemDown <c d>8 \stemDown <c d>8
    | % 62
    \stemDown <c d>8 ( _\> \stemDown <c e>8 ) \stemDown <c e>8 \stemDown
    <c e>8 \stemDown <c e>8 ( _\! _\p \stemDown <e g>8 \stemDown <d f>8
    \stemDown <g, d'>8 ) | % 63
    \stemUp f'2. _\markup{ \italic {più} } _ "" \stemUp e4 ~ | % 64
    \stemUp <e, e'>4 _\pp \stemUp <e e'>2. ~ ~ \bar "||"
    \pageBreak | % 65
    \time 3/4  \key c \major \stemUp <e e'>2. ~ ~ _\markup{ \italic
        {cresc.} } | % 66
    \stemUp <e e'>2. ~ ~ | % 67
    \stemUp <e e'>2. ~ ~ | % 68
    \stemUp <e e'>2. ~ ~ _\> | % 69
    \stemUp <e e'>2. ~ ~ _\! _\markup{ \italic {cresc.} } |
    \barNumberCheck #70
    \stemUp <e e'>2. ~ ~ \pageBreak | % 71
    \stemUp <e e'>2. ~ ~ | % 72
    \stemUp <e e'>2 ~ ~ _\markup{ \italic {morendo} } \stemUp <e e'>8
    \stemUp <e e'>8 ~ ~ | % 73
    \stemUp <e e'>8 \stemUp <e e'>8 _\markup{ \italic {cresc.} } \stemUp
    e8 ^\markup{ \bold\small {a. 2} } \stemUp e'8 \stemUp e,8 \stemUp e'8
    | % 74
    \stemUp e,8 \stemUp e'8 \stemUp e,8 \stemUp e'8 \stemUp e,8 \stemUp
    e'8 | % 75
    \stemUp e,8 \stemUp e'8 \stemUp e,8 \stemUp e'8 \stemUp e,8 \stemUp
    e'8 | % 76
    \stemUp e,8 \stemUp e'8 \stemUp e,8 \stemUp e'8 _\> \stemUp e,8
    \stemUp e'8 | % 77
    \stemUp e,8 _\! \stemUp e'8 _\markup{ \italic {cresc.} } \stemUp e,8
    \stemUp e'8 \stemUp e,8 \stemUp e'8 \pageBreak | % 78
    \stemUp e,8 \stemUp e'8 \stemUp e,8 \stemUp e'8 \stemUp e,8 \stemUp
    e'8 | % 79
    \stemUp e,8 \stemUp e'8 \stemUp e,8 _\> \stemUp e'8 \stemUp e,8
    \stemUp e'8 | \barNumberCheck #80
    \stemUp e,8 _\! _\markup{ \italic {morendo} } \stemUp e'8 \stemUp e,8
    \stemUp e'8 \stemUp e,8 \stemUp e'8 | % 81
    \stemUp e,8 _\markup{ \italic {più} } _ "" \stemUp e'8 \stemUp e,8
    \stemUp e'8 \stemUp f4 ~ | % 82
    \stemUp f2 ( _\pp \stemUp g4 ) \bar "||"
    \time 4/4  \key c \major \stemDown <c, f>4 r4 r2 | % 84
    R1 \break | % 85
    R1*5 \pageBreak | \barNumberCheck #90
    R1*5 \break | % 95
    R1*3 | % 98
    r4 \stemUp <c, c'>2 _\markup{ \italic {cresc.} } \stemDown <c' e>4 ~
    ~ \bar "||"
    \pageBreak | % 99
    \time 12/8  \key c \major \stemDown <c e>2. _\p \stemDown <g d'>2. |
    \barNumberCheck #100
    \stemUp <e c'>2. \stemDown <g d'>2. \pageBreak | % 101
    \stemDown <g e'>4. _\< \stemDown <g d'>4. \stemUp <c, c'>4. ~ ~ _\!
    _\> \stemUp <c c'>4 \stemDown <c' d>8 | % 102
    \stemDown <c e>4. ( _\! _\< \stemDown <e g>4 \stemDown <d f>8 )
    \stemDown <g, d'>4. ~ ~ _\! _\> \stemDown <g d'>8 \stemDown <g g'>8
    \stemDown <g g'>8 | % 103
    \stemDown <g g'>2. ~ ~ _\! _\< \stemDown <g g'>4. ~ ~ \stemUp <g g'>8
    _\! _\> \stemUp <g, g'>8 \stemUp <g g'>8 \pageBreak | % 104
    <g g'>1. ~ ~ _\! | % 105
    \stemUp <g g'>2. ~ ~ \stemUp <g g'>4 \stemUp <c c'>8 \stemUp <c c'>4.
    ~ ~ | % 106
    \stemUp <c c'>2. ~ ~ \stemUp <c c'>4. \stemUp <g g'>4. \pageBreak | % 107
    \stemUp g'2. ~ \stemUp g4 r8 \stemUp <g, g'>4 \stemUp <g g'>8 | % 108
    \stemUp <g g'>2. _\< \stemUp <c g'>4. _\! _\> \stemUp <g g'>4. ~ ~
    \pageBreak | % 109
    <g g'>1. ~ ~ _\! | \barNumberCheck #110
    \stemUp <g g'>2. ~ ~ _\< \stemUp <g g'>4. _\! _\> \stemUp <g g'>4. ~
    ~ \pageBreak | % 111
    \stemUp <g g'>2. ~ ~ _\! _\< \stemUp <g g'>4 _\! _\> \stemUp <c c'>8
    \stemUp <c c'>4. ~ ~ _\! _\markup{ \italic {cresc.} } | % 112
    \stemUp <c c'>2. ~ ~ \stemUp c'8 ( \stemUp d4 ) ~ \stemUp d4.
    \pageBreak | % 113
    \stemUp e2. ~ _\> \stemUp e4 ( _\! _\p \stemDown <e g>8 \stemDown <d
        f>4 \stemDown <g, d'>8 ) | % 114
    \stemDown <g d'>4. ~ ~ \stemDown <g d'>4 \stemUp <c, c'>8 \stemDown
    <c c'>8 \stemDown <g' g'>8 \stemDown <g g'>8 \stemUp g'8 \stemUp g8
    \stemUp g,8 \pageBreak | % 115
    \stemUp g'4 r8 r8 \stemUp g8 \stemUp c,8 \stemUp c4 r8 r8 \stemUp g'8
    \stemUp g,8 | % 116
    \stemUp g'4 r8 r8 \stemUp g8 \stemUp c,8 \stemUp <c, c'>8 \stemUp <c
        c'>8 \stemUp <c c'>8 \stemUp <c c'>8 _\markup{ \italic {cresc.}
        } \stemUp <c c'>8 \stemUp <c c'>8 | % 117
    \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>8
    \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>8
    \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>8
    \pageBreak | % 118
    \stemUp <c c'>8 _\> \stemUp <g g'>8 \stemUp <g g'>8 \stemUp <g g'>8
    \stemUp <g g'>8 \stemUp <g g'>8 \stemUp <g g'>8 _\! _\p \stemUp <g
        g'>8 \stemUp <g g'>8 \stemUp <g g'>8 \stemUp <g g'>8 \stemUp <g
        g'>8 \pageBreak | % 119
    \stemUp <g g'>8 _\markup{ \italic {più} } _ "" \stemUp <g g'>8
    \stemUp <g g'>8 \stemUp <g g'>8 \stemUp <g g'>8 \stemUp <g g'>8
    \stemUp <g g'>8 \stemUp <g g'>8 \stemUp <g g'>8 \stemUp <c c'>8
    \stemUp <c c'>8 \stemUp <c c'>8 | \barNumberCheck #120
    \stemUp <g g'>8 _\pp \stemUp <g g'>8 \stemUp <g g'>8 \stemUp <g g'>8
    \stemUp <g g'>8 \stemUp <g g'>8 \stemUp <g g'>8 _\markup{ \italic
        {cresc.} } \stemUp <g g'>8 \stemUp <g g'>8 \stemUp <g g'>8
    \stemUp <g g'>8 \stemUp <c c'>16 _\f \stemUp <c c'>16 | % 121
    \stemUp f'4 -. r8 r8 r8 \stemUp f16 \stemUp f16 \stemUp <c, c'>4 _.
    r8 r8 r8 \stemUp <c c'>16 \stemUp <c c'>16 | % 122
    \stemDown f'8 -. _\sf ^\markup{ \bold\small {a. 2} } r8 \stemDown f16
    \stemDown f16 \stemDown <c e>8 ^. _\sf r8 \stemDown <c e>16
    \stemDown <c e>16 \stemDown <g d'>8 _\ff r8 \stemDown <g g'>16
    \stemDown <g g'>16 \stemDown <g g'>8 r8 \stemDown <g g'>16 \stemDown
    <g g'>16 \pageBreak | % 123
    \stemDown <g g'>4 r8 r4 r8 r2. | % 124
    R1. | % 125
    <g g'>1. ~ ~ _ "" _\markup{ \italic {dolce} } | % 126
    \stemDown <g g'>2. ~ ~ \stemDown <g g'>4. ~ ~ \stemDown <g g'>8
    \stemDown <g g'>8 \stemDown <g g'>8 \pageBreak | % 127
    \stemUp <c, c'>2. _\markup{ \italic {cresc. poco a poco} } \stemUp
    <g g'>2. | % 128
    \stemUp e'4. ( ^\markup{ \bold\small {a. 2} } \stemUp g4. \stemDown
    c4. \stemDown d4. ) \pageBreak | % 129
    \stemDown e4. ( \stemDown g4 \stemDown f8 \stemDown d4 ) \stemUp
    <g,, g'>8 ~ ~ \stemUp <g g'>8 \stemUp <g g'>8 \stemUp <g g'>8 |
    \barNumberCheck #130
    \stemUp <g g'>4. \stemUp <g g'>4 \stemUp <g g'>8 \stemUp <g g'>4. ~
    ~ \stemUp <g g'>4 \stemUp <c c'>16 _\f \stemUp <c c'>16 | % 131
    \stemUp f'4 -. r8 r8 r8 \stemUp f16 \stemUp f16 \stemUp <c, c'>4 _.
    r8 r8 r8 \stemUp <c c'>16 \stemUp <c c'>16 \pageBreak | % 132
    \stemDown f'8 -. _\sf ^\markup{ \bold\small {a. 2} } r8 \stemDown f16
    \stemDown f16 \stemDown <c e>8 ^. _\sf r8 \stemDown <c e>16
    \stemDown <c e>16 \stemDown <g d'>8 _\ff r8 \stemDown <g g'>16
    \stemDown <g g'>16 \stemDown <g g'>8 r8 \stemDown <g g'>16 \stemDown
    <g g'>16 | % 133
    \stemDown <g g'>4 r8 r4 r8 r2. | % 134
    R1. | % 135
    <c, c'>1. _\> | % 136
    \stemUp <c c'>2. ~ ~ _\! _\> \stemUp <c c'>2. _\! _ "" _\markup{
        \italic {cresc.} } \pageBreak | % 137
    <g g'>1. _\p | % 138
    \stemUp <g g'>2. ~ ~ _\markup{ \italic {cresc.} } \stemUp <g g'>4
    \stemUp <c c'>8 ~ ~ \stemUp <c c'>8 _\> \stemUp <c' d>8 \stemUp <g
        d'>8 | % 139
    \stemUp <e c'>4. ~ ~ _\! _\p \stemUp <e c'>8 ( \stemUp <g d'>8
    \stemUp <c e>8 ) \stemUp e8 ( \stemUp d4 ) ~ \stemDown <g, d'>8
    \stemDown <g d'>8 \stemDown <g d'>8 \pageBreak | \barNumberCheck
    #140
    \stemUp <c, c'>8 ( \stemUp <e e'>8 \stemUp <g g'>8 ) ~ ~ \stemDown
    <g g'>8 \stemDown <g g'>4 \stemDown <g g'>4. ~ ~ \stemDown <g g'>8
    \stemDown <g g'>8 \stemDown <g g'>8 | % 141
    \stemDown <g g'>2. ~ ~ \stemDown <g g'>2. ~ ~ _\markup{ \italic
        {cresc.} } | % 142
    \stemDown <g g'>4. \stemDown <g d'>4. ~ ~ \stemDown <g d'>4. \stemUp
    <g c>8 ( \stemUp <g, g'>8 ) \stemUp <g g'>8 \pageBreak | % 143
    <g g'>1. | % 144
    \stemDown <g' d'>2. ~ ~ \stemDown <g d'>4. \stemUp <c, c'>4. _\>
    \pageBreak | % 145
    \stemDown <g' d'>4. _\! _\p _\< \stemDown <g d'>4. ~ ~ \stemDown <g
        d'>4. _\! _\> \stemUp <c, c'>4. | % 146
    \stemDown <g' d'>4. _\! _\< \stemDown <g d'>4. ~ ~ \stemDown <g d'>4.
    _\! _\> \stemUp <c, c'>4 \stemDown <c' e>8 \pageBreak | % 147
    \stemDown <g d'>4. _\! _\markup{ \italic {cresc.} } \stemDown <g d'>4
    _\ff r8 \stemDown <g d'>4 _\markup{ \italic {dim.} } r8 \stemDown <g
        d'>4 r8 | % 148
    \stemDown <g d'>4 r8 \stemDown <d' f>4 r8 \stemDown <d f>4 _\p r8
    \stemDown <d f>4 _\pp r8 | % 149
    \stemDown <c e>4 _\markup{ \italic {cresc.} } r8 \stemUp <c, f'>4 r8
    \stemDown <c' e>4 r8 \stemDown <g d'>4 r8 | \barNumberCheck #150
    \stemUp <c, c'>4 r8 \stemUp <c f'>4 r8 \stemDown <c' e>4 r8
    \stemDown <g d'>4 \stemDown <g d'>8 _\f \pageBreak | % 151
    r2. \stemUp <c, c'>8 _ "" _\markup{ \italic {sempre dim.} } \stemUp
    <c g'>8 ( -. \stemUp <c g'>8 ) -. \stemUp <c g'>8 ( -. \stemUp <c
        g'>8 -. \stemUp <c g'>8 ) -. | % 152
    \stemUp <c g'>8 ( -. \stemUp <c g'>8 -. \stemUp <c g'>8 ) -. \stemUp
    <c g'>8 ( -. \stemUp <c g'>8 -. \stemUp <c g'>8 ) -. \stemUp <c g'>8
    ( -. \stemUp <c g'>8 -. \stemUp <c g'>8 ) -. \stemUp <c g'>8 ( -.
    \stemUp <c g'>8 -. \stemUp <c g'>8 ) -. \pageBreak | % 153
    \stemUp <c g'>8 ( -. _\markup{ \italic {sempre} } _ "" \stemUp <c
        g'>8 -. \stemUp <c g'>8 ) -. \stemUp <c g'>4 r8 r8 \stemUp <c
        g'>8 ( -. \stemUp <c g'>8 ) -. \stemUp <c g'>4 r8 \pageBreak | % 154
    r8 \stemUp <c g'>8 ( -. _\markup{ \italic {cresc.} } \stemUp <c g'>8
    ) -. \stemUp <c g'>4 r8 r8 \stemUp <c g'>8 ( -. \stemUp <c g'>8 ) -.
    \stemUp <c g'>8 ( -. \stemUp <c g'>8 -. \stemUp <c g'>8 ) -. | % 155
    \stemDown <c' e>2. _\f \stemDown <g d'>2. ~ ~ _\f _\> | % 156
    \stemUp d'2. ( _\! _\p \stemUp e4 ) \stemUp <g,, g'>8 \stemUp <g g'>8
    \stemUp <g g'>8 \stemUp <g g'>8 | % 157
    \stemDown <d'' f>4. \stemDown <g, d'>4 _\f r8 \stemUp <e c'>8 ( -.
    _\pp \stemUp <e c'>8 -. \stemUp <e c'>8 ) -. \stemUp <e c'>4 r8 \bar
    "|."
    }

PartPFiveVoiceTwo =  \relative c'' {
    \clef "treble" \time 4/4 \key c \major \transposition bes, s1*6 | % 7
    \stemDown c8 ( \stemDown g8 \stemDown e'8 \stemDown d8 ) \stemDown
    g,4 s4*9 \pageBreak s1*5 | % 15
    \stemDown e'8 ( \stemDown c8 ) s4*19 \pageBreak s1*3 | % 23
    r2 r4 s4 \break s1 \bar "||"
    \pageBreak | % 25
    \time 3/4  \key c \major s4*21 \pageBreak s2*9 \pageBreak s4*15 \bar
    "||"
    \pageBreak | % 43
    \time 4/4  \key c \major s1*4 \break | % 47
    \stemDown c8 ( \stemDown g8 \stemDown e'8 \stemDown d8 ) s8*19
    \stemDown c8 -. s1 \pageBreak s4*5 s4*15 _\! _\> \break s1*5
    \pageBreak s1*2 | % 63
    r2 r4 \stemDown e,4 ~ s1 \bar "||"
    \pageBreak | % 65
    \time 3/4  \key c \major s2*9 \pageBreak s4*21 \pageBreak s4*11
    \stemDown f'4 ~ | % 82
    \stemDown f4 \stemDown c4 ~ \stemDown c4 \bar "||"
    \time 4/4  \key c \major s1*2 \break s1*5 \pageBreak s1*5 \break
    s1*4 \bar "||"
    \pageBreak | % 99
    \time 12/8  \key c \major s1*3 \pageBreak s2*9 \pageBreak s2*9
    \pageBreak | % 107
    \stemDown g,2. \stemDown c4 s1*2 \pageBreak s1*3 \pageBreak s4*9
    \stemDown c2. \pageBreak | % 113
    \stemDown c4. \stemDown c'4. ~ \stemDown c4 s8*13 \stemDown g8 r8 r8
    \pageBreak | % 115
    r8 \stemDown g8 \stemDown g,8 \stemDown g'4 r8 r8 \stemDown c8
    \stemDown c,8 \stemDown c'4 r8 | % 116
    r8 \stemDown g8 \stemDown g,8 \stemDown g'8 \stemDown g8 \stemDown
    c,8 s4*9 \pageBreak s1. \pageBreak s1*3 | % 121
    \stemDown f'4 -. s4. \stemDown f16 \stemDown f16 s4*9 \pageBreak
    s1*6 \pageBreak s1*3 \pageBreak s1*3 | % 131
    \stemDown f4 -. s4. \stemDown f16 \stemDown f16 s2. \pageBreak s2*15
    \pageBreak s4*15 \stemDown g,4. ~ s4. \pageBreak s2*9 \pageBreak
    s1*3 \pageBreak s1*3 \pageBreak s1*6 \pageBreak s1*3 \pageBreak s1.
    \pageBreak s1*3 | % 156
    \stemDown g2. ~ \stemDown g4 s1*2 \bar "|."
    }

PartPSixVoiceOne =  \relative d'' {
    \clef "treble" \time 4/4 \key c \major \transposition es | % 1
    R1*5 | % 6
    r2 r4 r8 \stemDown d8 _\p ^ "IV." | % 7
    \stemDown d4 \stemDown d8 \stemDown d8 \stemDown d4 r4 | % 8
    R1*2 \pageBreak | \barNumberCheck #10
    R1 | % 11
    r2 r4 \stemDown d4 | % 12
    \stemDown d2 \stemDown d4 r4 | % 13
    R1*2 | % 15
    r2 r8 \stemUp g,8 _\markup{ \italic {cresc.} } \stemUp c8 \stemUp g16
    \stemUp e16 | % 16
    \stemUp c8 \stemUp g'8 \stemUp g8 \stemUp g8 \stemUp g8 \stemUp g8
    \stemUp g8 \stemUp g8 | % 17
    \stemUp g8 r8 r4 r2 | % 18
    r2 r4 \stemDown d'4 _\markup{ \italic {dolce} } | % 19
    \stemDown d4. \stemDown d8 \stemDown d4 \stemDown d8 \stemDown d8
    \pageBreak | \barNumberCheck #20
    \stemDown d4. \stemDown d8 \stemUp g,8 \stemUp g8 \stemUp c,8 r8 | % 21
    R1 | % 22
    r8 \stemDown d'8 _\> \stemDown d8 \stemDown d8 \stemDown d8 _\! _\p
    \stemDown d8 \stemDown d8 ( \stemDown c8 ) | % 23
    R1 \break | % 24
    R1 \bar "||"
    \pageBreak | % 25
    \time 3/4  \key c \major R2.*7 \pageBreak | % 32
    R2.*6 \pageBreak | % 38
    R2.*5 \bar "||"
    \pageBreak | % 43
    \time 4/4  \key c \major r4 r8 \stemDown d8 -. ^ "IV." \stemDown d4
    -. r8 \stemDown d8 -. | % 44
    \stemDown d4 -. r8 \stemDown d8 -. \stemDown d4 -. r8 \stemDown d8
    -. | % 45
    \stemDown d4 -. _\markup{ \italic {sempre staccato} } r8 \stemDown d8
    -. \stemDown d4 -. r8 \stemUp g,8 -. | % 46
    \stemDown d'4 -. r8 \stemDown d8 -. \stemDown d8 -. r8 r8 \stemDown
    d8 -. \break | % 47
    \stemDown d4 -. _\< r8 \stemDown d8 -. _\! _\> \stemDown d4 -. _\! r8
    \stemDown d8 -. | % 48
    \stemDown d4 -. r8 \stemDown d8 -. \stemDown d4 -. r8 \stemDown d8
    -. | % 49
    \stemDown d4 -. r8 \stemDown d8 -. \stemDown d4 -. r8 \stemDown e8
    -. | \barNumberCheck #50
    \stemDown e4 -. r8 \stemDown c8 -. \stemDown d4 -. r4 \pageBreak | % 51
    r4 r8 \stemDown d8 -. _\< \stemDown d8 -. \stemDown d8 -. _\!
    \stemDown d8 -. _\> \stemDown d8 -. | % 52
    \stemDown d2 _\! _\< \stemDown d4 _\! r8 \stemDown d8 ^. | % 53
    \stemDown d4 -. r8 \stemDown d8 -. \stemDown d4 -. r8 \stemDown d8
    -. | % 54
    \stemDown d4 -. r8 \stemDown d8 -. \stemDown d8 -. r8 \stemDown d8
    -. \stemDown d8 -. | % 55
    \stemDown d8 -. _\< \stemDown g,8 -. r8 \stemDown c8 _\! _\> r8
    \stemDown b8 \stemUp e16 _\! _\markup{ \italic {cresc.} } \stemUp c16
    \stemUp g16 \stemUp e16 \break | % 56
    \stemUp c8 -. \stemUp e'8 -. r8 \stemDown e8 -. \stemDown e4 -. r8
    \stemDown e8 -. | % 57
    \stemDown e8 -. _\> \stemDown d8 -. r8 \stemUp g,8 -. \stemDown d'4
    -. _\! _\p r8 \stemDown d8 -. | % 58
    \stemDown d4 -. r8 \stemDown d8 -. \stemDown d4 \stemDown d4 | % 59
    \stemDown d4. \stemDown d8 \stemDown d4 \stemDown d8 \stemDown d8 |
    \barNumberCheck #60
    \stemDown d4. \stemDown d8 \stemUp g,8 \stemUp g8 \stemUp c,8 r8
    \pageBreak | % 61
    R1 | % 62
    r8 \stemDown d'8 _\> \stemDown d8 \stemDown d8 \stemDown d8 _\! _\p
    \stemDown d8 \stemDown d8 ( \stemDown c8 ) | % 63
    R1*2 \bar "||"
    \pageBreak | % 65
    \time 3/4  \key c \major R2.*6 \pageBreak | % 71
    R2.*7 \pageBreak | % 78
    R2.*4 | % 82
    r4 r4 \stemUp g,4 ^ "IV." \bar "||"
    \time 4/4  \key c \major \stemUp c4 \stemUp g'2 \stemUp g4 ~ | % 84
    \stemUp g4 \stemUp g,4 ~ \stemUp g8 \stemUp g'8 r8 \stemUp g8 \break
    | % 85
    \stemDown e'2 \stemDown b2 | % 86
    \stemDown c2 \stemUp g2 | % 87
    \stemUp e4 \stemUp c4 \stemUp b2 | % 88
    \stemUp c2 \stemUp g2 | % 89
    \clef "bass" \stemUp c,2 \stemUp g2 \pageBreak | \barNumberCheck #90
    \stemUp g8 \clef "treble" \stemUp g''8 \stemDown es'4. \stemDown es8
    \stemDown des4 ~ | % 91
    \stemDown des8 \stemDown des8 \stemDown c4. \stemDown bes8 (
    \stemDown c8 \stemDown des8 ) | % 92
    \stemDown des8 ( \stemDown c8 ) \stemDown c4. \stemDown des8 ( -.
    \stemDown es8 -. \stemDown f8 ) -. | % 93
    \stemDown f8 ( _\< \stemDown es8 \stemDown as8 _\! _\> \stemDown c,8
    ) \stemDown es4 ( _\! \stemDown des4 ) | % 94
    \stemDown des8 ( _\< \stemDown c8 ) r8 _\! _\> \stemUp as8 r8 _\!
    \stemUp as8 ( \stemUp g4 ) \break | % 95
    g1 | % 96
    \stemDown as8 \stemDown bes16 \stemDown c16 \stemDown des16
    \stemDown es16 \stemDown f16 \stemDown g16 \stemDown as16 \stemDown
    es16 \stemDown as16 \stemDown g16 \stemDown f16 \stemDown es16
    \stemDown des16 \stemDown c16 | % 97
    \stemDown des4 _\markup{ \italic {cresc.} } \stemDown des2 \stemDown
    des4 ~ | % 98
    \stemDown des4 \stemDown des2 \stemDown d4 ~ \bar "||"
    \pageBreak | % 99
    \time 12/8  \key c \major \stemDown d4. ~ _\p \stemDown d8 \stemDown
    d8 \stemDown d8 \stemDown d4 r8 r8 \stemDown d8 \stemDown d8 |
    \barNumberCheck #100
    \stemDown d4 r8 r8 \stemDown d8 \stemDown d8 \stemDown d4 r8 r8
    \stemDown d8 \stemDown d8 \pageBreak | % 101
    \stemDown d4 _\< r8 r8 \stemDown d8 \stemDown d8 \stemUp g,4 _\! _\>
    r8 r8 \stemDown e'8 \stemDown e8 | % 102
    \stemDown d4. _\! _\< r8 \stemDown d8 \stemDown d8 \stemDown d4 _\!
    _\> r8 _\! r4 r8 | % 103
    r4 r8 \stemUp g,4. ( ~ _\markup{ \italic {cresc.} } \stemUp g4
    \stemUp fis8 \stemDown e'8 _\> \stemDown d8 ) \stemDown d8 _\! _\p
    \pageBreak | % 104
    d1. ~ | % 105
    \stemDown d2. ~ \stemDown d4. \stemDown e4. ~ | % 106
    \stemDown e2. ( \stemDown d2. ) \pageBreak | % 107
    \stemDown d2. ~ \stemDown d4 r8 \stemDown d4 \stemDown d8 | % 108
    \stemDown d2. _\< \stemDown d4. _\! _\> \stemDown d4. \pageBreak | % 109
    \stemDown e4. _\! \stemDown fis4. \stemDown d4. \stemDown g4. |
    \barNumberCheck #110
    \stemDown e4. _\< \stemDown fis4. ~ \stemDown fis4. ( _\! _\>
    \stemDown g4 ) \stemDown d8 \pageBreak | % 111
    \stemDown d8 ( _\! _\< \stemDown e8 ) \stemDown e8 \stemDown e8 (
    \stemDown fis8 ) \stemDown fis8 ~ \stemDown fis16 _\! _\> \stemDown
    d16 \stemDown e16 \stemDown fis16 \stemDown g8 ~ \stemUp g16 _\!
    _\markup{ \italic {cresc.} } \stemUp e16 \stemUp c16 \stemUp g16
    \stemUp c,16 \clef "bass" \stemUp g16 | % 112
    \stemUp c,8 \clef "treble" \stemDown e''4 ~ \stemDown e4. ~
    \stemDown e2. \pageBreak | % 113
    \stemUp g,4. ~ _\> \stemUp g4 \stemDown b8 \stemDown d2. ~ _\! _\p | % 114
    \stemDown d2. ~ \stemDown d4 r8 r4 r8 \pageBreak | % 115
    r4 r8 \stemDown d4 \stemUp g,8 \stemUp g4. r4 r8 | % 116
    r4 r8 \stemDown d'4 \stemUp g,8 \stemUp g4. \stemDown e'4. ~
    _\markup{ \italic {cresc.} } | % 117
    \stemUp e16 \stemUp c16 \stemUp g16 \stemUp e16 \once \omit
    TupletBracket
    \times 2/3  {
        \stemUp c'16 ( \stemUp g16 \stemUp e16 ) }
    \stemDown c8 \stemDown e'8 \stemDown e8 \stemDown e4. ~ \stemDown e8
    ( \stemDown fis8 \stemDown g8 ) \pageBreak | % 118
    \stemDown g4. ~ _\> \stemDown g4 \stemDown d8 \stemDown d4. ~ _\!
    _\p \stemDown d8 ( \stemDown e8 \stemDown d8 ) \pageBreak | % 119
    \stemDown d8 ( _\markup{ \italic {più} } _ "" \stemDown e8
    \stemDown d8 ) \stemDown d8 ( \stemDown e8 \stemDown d8 ) \stemDown
    d8 ( \stemDown e8 \stemDown d8 ) \stemDown d8 ( \stemDown e8
    \stemDown d8 ) | \barNumberCheck #120
    \stemDown d8 ( _\pp \stemDown e8 \stemDown d8 ) \stemDown d8 (
    \stemDown e8 \stemDown d8 ) \stemDown d8 ( _\markup{ \italic
        {cresc.} } \stemDown e8 \stemDown d8 ) \stemDown d16 \stemDown e16
    \stemDown f8 \stemUp <g,, g'>16 _\f \stemUp <g g'>16 | % 121
    \stemUp <c c'>4 -. r8 r8 r8 \stemUp <c c'>16 \stemUp <c c'>16
    \stemDown <g' g'>4 -. r8 r8 r8 \stemDown <g g'>16 \stemDown <g g'>16
    | % 122
    \stemDown <c e>8 ^. _\sf r8 \stemDown <c e>16 \stemDown <c e>16
    \stemDown <g d'>8 ^. _\sf r8 \stemDown <g d'>16 \stemDown <g d'>16
    \stemDown d'8 _\ff ^\markup{ \bold\small {a. 2} } r8 \stemDown d16
    \stemDown d16 \stemDown d8 r8 \stemDown d16 \stemDown d16 \pageBreak
    | % 123
    \stemDown d4 r8 r4 r8 \stemDown f2. ( ^ "IV." _\> | % 124
    \stemDown e2. ) \stemDown es2. ( _\! _\> | % 125
    \stemDown g4. _\! _\markup{ \italic {dolce} } \stemDown d4. )
    \stemDown c2. | % 126
    \stemDown b2. \stemDown c4. ~ \stemDown c8 ( \stemDown d8 )
    \stemDown d8 -. \pageBreak | % 127
    \stemUp g,4 r8 r4 r8 r2. | % 128
    R1. \pageBreak | % 129
    R1. | \barNumberCheck #130
    r2. r4 r8 r8 r8 \stemUp <g, g'>16 _\f \stemUp <g g'>16 | % 131
    \stemUp <c c'>4 -. r8 r8 r8 \stemUp <c c'>16 \stemUp <c c'>16
    \stemDown <g' g'>4 -. r8 r8 r8 \stemDown <g g'>16 \stemDown <g g'>16
    \pageBreak | % 132
    \stemDown <c e>8 ^. _\sf r8 \stemDown <c e>16 \stemDown <c e>16
    \stemDown <g d'>8 ^. _\sf r8 \stemDown <g d'>16 \stemDown <g d'>16
    \stemDown d'8 _\ff ^\markup{ \bold\small {a. 2} } r8 \stemDown d16
    \stemDown d16 \stemDown d8 r8 \stemDown d16 \stemDown d16 | % 133
    \stemUp d4 _\> r8 r4 r8 r2. | % 134
    f1. _\! ^ "IV." _\> | % 135
    \stemDown c2. ~ _\! _\> \stemDown c4. ( \stemDown es4. ) | % 136
    \stemDown g2. ~ _\! _\> \stemDown g2. _\! _ "" _\markup{ \italic
        {cresc.} } _\< \pageBreak | % 137
    \stemDown d4. ~ _\! _\p \stemDown d8 ( \stemDown c8 ) \stemDown b8
    -. \stemUp a4. ~ \stemDown a8 ( \stemDown d8 ) \stemDown d8 -. | % 138
    \stemDown d4. ~ _\markup{ \italic {cresc.} } \stemUp d8 \stemUp g,8
    \stemUp g8 \stemUp a4 \stemUp g8 r8 \stemDown e'8 ( _\> \stemDown d8
    ) | % 139
    \stemUp g,8 _\! _\p r8 r8 r8 \stemDown d'8 \stemDown g,8 \stemDown
    d'4 r8 r8 \stemDown d8 \stemDown d8 \pageBreak | \barNumberCheck
    #140
    \stemDown d4 r8 r8 \stemDown d8 \stemDown g,8 \stemDown d'4 r8 r8
    \stemDown d8 \stemDown d8 | % 141
    \stemDown d4 r8 r4 r8 r2. | % 142
    R1. \pageBreak | % 143
    R1.*2 \pageBreak | % 145
    R1.*2 \pageBreak | % 147
    R1.*2 | % 149
    r8 r8 \stemUp <g,, g'>8 _\markup{ \italic {cresc.} } r8 r8 \stemUp
    <g g'>8 r8 r8 \stemUp <g g'>8 r8 r8 \stemUp d''8 | \barNumberCheck
    #150
    r8 r8 \stemUp <g,, g'>8 r8 r8 \stemUp <g g'>8 r8 r8 \stemUp <g g'>8
    r8 r8 \stemUp d''8 _\f \pageBreak | % 151
    r2. \stemUp <g,, g'>4 _\p r8 r4 r8 | % 152
    R1. \pageBreak | % 153
    R1. \pageBreak | % 154
    R1. | % 155
    \stemUp d''4 _\f r8 r4 r8 \stemUp d4 _\fp r8 r4 r8 | % 156
    r2. \stemUp <g,, g'>4 _\p r8 r4 r8 | % 157
    r4 r8 \stemUp d''4 _\f r8 r4 r8 \stemUp <g,, g'>4 _\pp r8 \bar "|."
    }

PartPSixVoiceTwo =  \relative bes' {
    \clef "treble" \time 4/4 \key c \major \transposition es s1*9
    \pageBreak s1*10 \pageBreak s1*4 \break s1 \bar "||"
    \pageBreak | % 25
    \time 3/4  \key c \major s4*21 \pageBreak s2*9 \pageBreak s4*15 \bar
    "||"
    \pageBreak | % 43
    \time 4/4  \key c \major s1*4 \break s1*4 \pageBreak s4*5 s4*15 _\!
    _\> \break s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 65
    \time 3/4  \key c \major s2*9 \pageBreak s4*21 \pageBreak s4*15 \bar
    "||"
    \time 4/4  \key c \major s1*2 \break s1*4 | % 89
    \clef "bass" s1 \pageBreak s8 \clef "treble" s8*39 \break s1*4 \bar
    "||"
    \pageBreak | % 99
    \time 12/8  \key c \major s1*3 \pageBreak s2*9 \pageBreak s2*9
    \pageBreak s1*3 \pageBreak s1*3 \pageBreak s16*23 \clef "bass" s8.
    \clef "treble" s8*11 \pageBreak s1*3 \pageBreak s2*9 \pageBreak s1.
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*3 \pageBreak s2*9
    \pageBreak s1. | % 133
    \stemDown bes2. ~ \stemDown bes4. ( \stemDown d4. ) s2*9 \pageBreak
    s2*9 \pageBreak s2*9 \pageBreak s1*3 \pageBreak s1*3 \pageBreak
    s8*35 \stemDown d8 s8*11 \stemDown d8 \pageBreak s1*3 \pageBreak s1.
    \pageBreak s1. | % 155
    \stemDown d4 s2 \stemDown d4 s8*19 \stemDown d4 s8*7 \bar "|."
    }

PartPSevenVoiceOne =  \relative c'' {
    \clef "treble" \time 4/4 \key c \major \transposition bes | % 1
    R1*9 \pageBreak | \barNumberCheck #10
    R1*10 \pageBreak | \barNumberCheck #20
    R1*4 \break | % 24
    R1 \bar "||"
    \pageBreak | % 25
    \time 3/4  \key c \major R2.*7 \pageBreak | % 32
    R2.*6 \pageBreak | % 38
    R2.*5 \bar "||"
    \pageBreak | % 43
    \time 4/4  \key c \major R1*4 \break | % 47
    R1*4 \pageBreak | % 51
    R1*5 \break | % 56
    R1*5 \pageBreak | % 61
    R1*4 \bar "||"
    \pageBreak | % 65
    \time 3/4  \key c \major R2.*6 \pageBreak | % 71
    R2.*7 \pageBreak | % 78
    R2.*5 \bar "||"
    \time 4/4  \key c \major R1*2 \break | % 85
    R1*5 \pageBreak | \barNumberCheck #90
    R1*5 \break | % 95
    R1*4 \bar "||"
    \pageBreak | % 99
    \time 12/8  \key c \major R1.*2 \pageBreak | % 101
    R1.*3 \pageBreak | % 104
    R1.*3 \pageBreak | % 107
    R1.*2 \pageBreak | % 109
    R1.*2 \pageBreak | % 111
    R1.*2 \pageBreak | % 113
    R1.*2 \pageBreak | % 115
    R1.*3 \pageBreak | % 118
    R1. \pageBreak | % 119
    R1. | \barNumberCheck #120
    r2. r4 r8 r8 r8 \stemDown c16 ^\markup{ \bold\small {a. 2} } _\f
    \stemDown c16 | % 121
    \stemDown f4 -. r8 r8 r8 \stemDown f16 \stemDown f16 \stemDown c4 -.
    r8 r8 r8 \stemDown c16 \stemDown c16 | % 122
    \stemDown f8 -. _\sf r8 \stemDown f16 \stemDown f16 \stemUp <c, c'>8
    -. _\sf r8 \stemUp <c c'>16 \stemUp <c c'>16 \stemDown <g' g'>8 _\ff
    r8 \stemDown <g g'>16 \stemDown <g g'>16 \stemDown <g g'>8 r8
    \stemDown <g g'>16 \stemDown <g g'>16 \pageBreak | % 123
    \stemDown <g g'>4 r8 r4 r8 r2. | % 124
    R1.*3 \pageBreak | % 127
    R1.*2 \pageBreak | % 129
    R1. | \barNumberCheck #130
    r2. r4 r8 r8 r8 \stemDown c16 _\f ^\markup{ \bold\small {a. 2} }
    \stemDown c16 | % 131
    \stemDown f4 -. r8 r8 r8 \stemDown f16 \stemDown f16 \stemDown c4 -.
    r8 r8 r8 \stemDown c16 \stemDown c16 \pageBreak | % 132
    \stemDown f8 -. _\sf r8 \stemDown f16 \stemDown f16 \stemUp <c, c'>8
    -. _\sf r8 \stemUp <c c'>16 \stemUp <c c'>16 \stemDown <g' g'>8 _\ff
    r8 \stemDown <g g'>16 \stemDown <g g'>16 \stemDown <g g'>8 r8
    \stemDown <g g'>16 \stemDown <g g'>16 | % 133
    \stemDown <g g'>4 r8 r4 r8 r2. | % 134
    R1.*3 \pageBreak | % 137
    R1.*3 \pageBreak | \barNumberCheck #140
    R1.*3 \pageBreak | % 143
    R1.*2 \pageBreak | % 145
    R1.*2 \pageBreak | % 147
    r4 r8 \stemDown <g d'>4 _\ff r8 r2. | % 148
    R1. | % 149
    r4 r8 \stemUp <c, c'>4 _\p r8 \stemUp <c c'>4 r8 \stemUp <g g'>4 r8
    | \barNumberCheck #150
    r4 r8 \stemUp <c c'>4 _\markup{ \italic {cresc.} } r8 \stemUp <c c'>4
    r8 \stemUp <g g'>4 \stemDown <g' d'>8 _\f \pageBreak | % 151
    r2. \stemUp <e c'>4 _\p r8 r4 r8 | % 152
    R1. \pageBreak | % 153
    R1. \pageBreak | % 154
    R1. | % 155
    \stemDown <c' e>4 _\f r8 r4 r8 \stemDown <g d'>4 _\fp r8 r4 r8 | % 156
    r4 r8 \stemDown <g d'>4 _\p r8 \stemUp <e c'>4 r8 r4 r8 | % 157
    r4 r8 \stemDown <g d'>4 _\f r8 \stemUp <c, e>8 ( -. _\pp \stemUp <c
        e>8 -. \stemUp <c e>8 ) -. \stemUp <c e>4 r8 \bar "|."
    }

PartPEightVoiceOne =  \relative f {
    \clef "bass" \time 4/4 \key bes \major | % 1
    R1*9 \pageBreak | \barNumberCheck #10
    R1*9 | % 19
    r4 \stemUp f8 _\p \stemUp bes,8 \stemUp bes4 r4 \pageBreak |
    \barNumberCheck #20
    r4 \stemUp f'8 \stemUp bes,8 \stemUp bes4 r4 | % 21
    R1*3 \break | % 24
    R1 \bar "||"
    \pageBreak | % 25
    \time 3/4  \key d \major R2.*7 \pageBreak | % 32
    R2.*6 \pageBreak | % 38
    R2.*5 \bar "||"
    \pageBreak | % 43
    \time 4/4  \key bes \major R1*4 \break | % 47
    R1*4 \pageBreak | % 51
    R1*5 \break | % 56
    R1*3 | % 59
    r4 \stemDown f'8 _\p \stemDown bes,8 \stemUp bes4 r4 |
    \barNumberCheck #60
    r4 \stemDown f'8 \stemDown bes,8 \stemUp bes4 r4 \pageBreak | % 61
    R1*4 \bar "||"
    \pageBreak | % 65
    \time 3/4  \key g \major R2.*6 \pageBreak | % 71
    R2.*7 \pageBreak | % 78
    R2.*5 \bar "||"
    \time 4/4  \key es \major R1*2 \break | % 85
    R1*5 \pageBreak | \barNumberCheck #90
    R1*5 \break | % 95
    R1*4 \bar "||"
    \pageBreak | % 99
    \time 12/8  \key bes \major r4 r8 \stemDown f'4 _\p r8 r4 r8
    \stemDown f4 r8 | \barNumberCheck #100
    r4 r8 \stemDown f4 r8 r4 r8 \stemDown f4 _\markup{ \italic {sempre}
        } _ "" r8 \pageBreak | % 101
    \stemUp bes,4 r8 \stemDown f'4 r8 \stemUp bes,4 r8 \stemUp bes4 r8 | % 102
    r4 r8 \stemDown f'4 r8 r4 r8 \stemDown f4 r8 | % 103
    r4 r8 \stemDown f4 r8 r4 r8 \stemDown f4 r8 \pageBreak | % 104
    r4 r8 \stemDown f4 r8 r4 r8 \stemDown f4 r8 | % 105
    r4 r8 \stemDown f4 r8 \stemUp bes,4 r8 \stemUp bes4 r8 | % 106
    \stemUp bes4 r8 \stemUp bes4 r8 \stemDown f'4 r8 \stemDown f4 r8
    \pageBreak | % 107
    r4 r8 \stemDown f4 r8 \stemUp bes,4 \stemDown f'8 \stemDown f4 r8 | % 108
    r4 r8 \stemDown f4 r8 \stemUp bes,4 \stemUp bes8 \stemUp bes4 r8
    \pageBreak | % 109
    r4 r8 \stemDown f'4 r8 r4 r8 \stemDown f4 r8 | \barNumberCheck #110
    r4 r8 \stemDown f4 r8 r4 r8 \stemUp bes,4 r8 \pageBreak | % 111
    r4 r8 \stemDown f'4 r8 \stemDown f4 \stemUp bes,8 _\markup{ \italic
        {cresc.} } \stemUp bes8 \stemUp bes8 \stemUp bes8 | % 112
    \stemUp bes4 r8 \stemUp bes4 r8 r4 r8 \stemUp bes4 r8 \pageBreak | % 113
    r4 r8 \stemDown f'4 r8 r4 r8 \stemDown f4 _\p r8 | % 114
    r4 r8 \stemDown f8 r8 \stemUp bes,8 \stemUp bes4 r8 r4 r8 \pageBreak
    | % 115
    r4 r8 \stemDown f'4 \stemUp bes,8 \stemUp bes4 r8 r4 r8 | % 116
    r4 r8 \stemDown f'4 \stemUp bes,8 \stemUp bes4 r8 \stemUp bes4
    _\markup{ \italic {cresc.} } \stemUp bes8 | % 117
    \stemUp bes4 r8 \stemUp bes4 \stemUp bes8 \stemUp bes4 r8 \stemUp
    bes4 \stemUp bes8 \pageBreak | % 118
    \stemUp bes4 _\markup{ \italic {dim.} } r8 \stemDown f'4 \stemDown f8
    \stemDown f4 _\p r8 \stemDown f4 \stemDown f8 \pageBreak | % 119
    \stemDown f4 _\markup{ \italic {più} } _ "" r8 \stemDown f4
    \stemDown f8 \stemDown f4 r8 \stemDown f4 \stemUp bes,8 |
    \barNumberCheck #120
    \stemDown f'4 _\pp r8 \stemDown f4 \stemDown f8 \stemDown f4 r8
    \stemDown f8 r8 r8 | % 121
    R1. | % 122
    r4 r8 \stemUp bes,8 _\f r8 \stemUp bes16 \stemUp bes16 \stemUp bes4
    r2 \pageBreak | % 123
    R1.*4 \pageBreak | % 127
    R1.*2 \pageBreak | % 129
    R1.*3 \pageBreak | % 132
    r4 r8 \stemUp bes8 _\sf r8 \stemUp bes16 \stemUp bes16 \stemUp bes4
    r2 | % 133
    R1.*4 \pageBreak | % 137
    R1.*2 | % 139
    r8 \stemUp f'8 _\p \stemUp bes,8 \stemDown f'8 r8 r8 r8 \stemUp f8
    _\p \stemUp bes,8 \stemDown f'4 r8 \pageBreak | \barNumberCheck #140
    r8 \stemDown f8 \stemDown bes,8 \stemDown f'4 r8 r8 \stemDown f8
    \stemDown f8 \stemDown f8 \stemDown f8 \stemDown f8 | % 141
    \stemDown f4 r8 r4 r8 r2. | % 142
    R1. \pageBreak | % 143
    R1.*2 \pageBreak | % 145
    R1.*2 \pageBreak | % 147
    r4 r8 \stemDown f4 _\ff r8 r2. | % 148
    R1. | % 149
    r4 r8 \stemUp bes,4 _\p r8 \stemDown f'4 r8 \stemDown f4 r8 |
    \barNumberCheck #150
    r4 r8 \stemUp bes,4 _\markup{ \italic {cresc.} } r8 \stemUp bes4 r8
    \stemDown f'4 \stemDown f8 _\f \pageBreak | % 151
    r2. r8 \stemDown f8 _\p \stemDown bes,8 \stemDown f'4 r8 | % 152
    r8 \stemDown f8 \stemDown bes,8 \stemDown f'4 r8 r8 \stemDown f8
    \stemDown bes,8 \stemDown f'4 r8 \pageBreak | % 153
    r8 \stemDown f8 _\markup{ \italic {sempre} } _ "" \stemDown bes,8
    \stemDown f'8 \stemDown <bes, f'>8 ( -. \stemDown <bes f'>8 ) -.
    \stemDown <bes f'>4 r8 r8 \stemDown <bes f'>8 ( -. \stemDown <bes
        f'>8 ) -. \pageBreak | % 154
    \stemDown <bes f'>4 _\markup{ \italic {cresc.} } r8 r8 \stemDown
    <bes f'>8 ( -. \stemDown <bes f'>8 ) -. \stemDown <bes f'>4 r8 r8
    \stemDown <bes f'>8 ( -. \stemDown <bes f'>8 ) -. | % 155
    \stemDown f'4 _\f r8 r4 r8 \stemDown f4 _\fp r8 r4 r8 | % 156
    r4 r8 \stemDown f4 _\p r8 \stemUp bes,4 r8 r4 r8 | % 157
    r4 r8 \stemDown f'4 _\f r8 \stemDown <bes, f'>8 ( -. _\pp \stemDown
    <bes f'>8 -. \stemDown <bes f'>8 ) -. \stemDown <bes f'>4 r8 \bar
    "|."
    }

PartPNineVoiceOne =  \relative d'' {
    \clef "treble" \time 4/4 \key bes \major | % 1
    R1*2 | % 3
    \stemDown d2 ( _\markup{ \italic {mezza voce} } \stemUp a2 | % 4
    \stemDown bes2 \stemUp f4. \stemUp es8 ) | % 5
    \stemUp d4 ( \stemUp f4 \stemDown bes4. \stemDown c8 ) | % 6
    \stemDown d4 ( \stemDown f8 \stemDown es8 \stemDown c4 ) r4 | % 7
    r2 r4 \stemDown c4 | % 8
    \stemDown c2 ( \stemDown bes4. \stemDown f'8 ) | % 9
    \stemDown f4 ( \stemDown es4 ~ \stemDown es4 \stemDown d4 )
    \pageBreak | \barNumberCheck #10
    \stemDown c4 ( ~ \stemDown c8 \stemDown d16 \stemDown es16 \stemDown
    d4 \stemDown c8 \stemDown cis8 ) | % 11
    \stemDown cis4. ( \stemDown d8 ) \stemDown d4 r4 | % 12
    r2 r4 \stemDown d4 ( | % 13
    \stemDown c2 \stemDown bes4. \stemDown f'8 ) | % 14
    \stemDown f4 ( \stemDown es4 ~ \stemDown es4 \stemDown d4 ) | % 15
    r2 r8 \stemDown d8 _\markup{ \italic {cresc.} } \stemDown g4 | % 16
    \stemDown g2 ~ \stemDown g8 \stemDown g8 ( \stemDown a8 \stemDown
    bes8 ) | % 17
    \stemDown bes4. _\> \stemDown d,8 \stemDown f4 ( _\! _\p \stemDown
    es8 \stemDown c8 ) | % 18
    \stemDown c4. ( \stemDown d8 \stemDown bes4 ) r4 | % 19
    r2 \stemUp bes,8 r8 r4 \pageBreak | \barNumberCheck #20
    r2 \stemUp bes8 \stemUp <bes d>8 \stemUp <bes g'>8 _\markup{ \italic
        {cresc.} } r8 | % 21
    \acciaccatura { \stemUp bes32 ( \stemUp es32 } \stemUp g8 ) r8
    \acciaccatura { \stemUp bes,32 ( \stemUp es32 } \stemUp g8 ) r8
    \acciaccatura { \stemUp bes,32 ( \stemUp c32 } \stemUp g'8 ) r8
    \acciaccatura { \stemUp bes,32 ( \stemUp c32 } \stemUp g'8 ) r8 | % 22
    \acciaccatura { \stemUp bes,32 ( \stemUp c32 } \stemUp g'8 ) _\>
    \acciaccatura { \stemUp bes,32 ( \stemUp d32 } \stemUp f8 )
    \acciaccatura { \stemUp bes,32 ( \stemUp d32 } \stemUp f8 ) r8
    \acciaccatura { \stemUp bes,32 ( \stemUp d32 } \stemUp f8 ) _\! _\p
    r8 \acciaccatura { \stemUp a,32 ( \stemUp c32 } \stemUp es8 ) r8 | % 23
    \acciaccatura { \stemUp es32 ( } \stemUp a8 ) _\markup{ \italic
        {più} } _ "" r8 \acciaccatura { \stemUp es32 ( } \stemUp a8 ) r8
    \acciaccatura { \stemUp es32 ( } \stemUp a8 ) r8 \acciaccatura {
        \stemUp d,32 ( } \stemUp a'8 ) r8 \break | % 24
    \acciaccatura { \stemUp d,32 ( } \stemUp a'8 ) _\pp r8 \acciaccatura
    { \stemUp d,32 ( } \stemUp a'8 ) r8 \acciaccatura { \stemUp d,32 ( }
    \stemUp a'8 ) r8 r4 \bar "||"
    \pageBreak | % 25
    \time 3/4  \key d \major R2.*7 \pageBreak | % 32
    R2. | % 33
    r4 \stemDown g'4. ( ^ "" ^\markup{ \italic {cresc.} } \stemDown
    cis,8 | % 34
    \stemDown e8 \stemDown d8 ) \stemDown d4 r8 \stemDown a'8 ~ | % 35
    \stemDown a4 ( \stemUp a,8 ) r8 r8 \stemDown a'8 ~ | % 36
    \stemDown a4 ( \stemUp a,8 ) \stemDown d8 ( _\> \stemDown e8
    \stemDown fis8 ) | % 37
    \stemDown fis8 ( _\! _\markup{ \italic {cresc.} } \stemDown g8 )
    \stemDown g4. \stemDown cis,8 ( \pageBreak | % 38
    \stemDown e8 \stemDown d8 ) \stemDown d4 r8 \stemDown a'8 ~ | % 39
    \stemDown a4 ( \stemUp a,8 ) r8 r8 \stemDown a'8 ~ _\> |
    \barNumberCheck #40
    \stemDown a4 ( _\! _\markup{ \italic {morendo} } \stemUp a,8 ) r8 r8
    \stemDown a'8 ~ | % 41
    \stemDown a4 ( _\markup{ \italic {più} } _ "" \stemUp a,8 ) \stemUp
    a,8 r8 \stemUp d8 | % 42
    r4 _\pp r8 \stemUp d8 ( \stemUp es16 \stemUp a16 \stemUp c16 \stemUp
    es16 ) ^\fermata \bar "||"
    \pageBreak | % 43
    \time 4/4  \key bes \major \acciaccatura { \stemUp f,8 ( } \stemDown
    d'4. ) \stemDown c16 \stemDown bes16 \stemUp bes8 ( \stemUp a8 ) ~
    \stemUp a16 ( \stemUp c16 \stemUp bes16 \stemUp a16 ) | % 44
    \stemDown c8 ( \stemDown bes8 ) ~ \stemDown bes16 ( \stemDown d16
    \stemDown bes16 \stemDown g16 ) \stemUp g16 ( \stemUp f16 \stemUp e16
    \stemUp f16 \stemUp e16 \stemUp f16 \stemUp g16 \stemUp es16 ) | % 45
    \stemUp es16 ( \stemUp d16 \stemUp cis16 \stemUp d16 \stemUp g16
    \stemUp f16 \stemUp e16 \stemUp f16 ) \stemDown c'16 ( \stemDown bes16
    \stemDown a16 \stemDown bes16 \stemDown a16 \stemDown bes16 )
    \stemDown bes16 ( \stemDown c16 ) | % 46
    \stemDown cis16 ( \stemDown d16 \stemDown es16 \stemDown d16
    \stemDown f16 \stemDown d16 \stemDown f16 \stemDown es16 ) \stemDown
    c4 r4 \break | % 47
    r2 r8 \stemUp f,16 ( _\markup{ \italic {dolce} } \stemUp c'16
    \stemDown b16 _\< \stemDown c16 \stemDown d16 _\! _\> \stemDown c16
    ) | % 48
    \stemDown c4 ~ _\! \stemUp c16 ( \stemUp f,16 \stemUp d'16 \stemUp c16
    ) \stemDown c8 ( \stemDown bes8 ) ~ \stemDown bes16 ( \stemDown e16
    \stemDown g16 \stemDown f16 ) | % 49
    \stemDown f16 ( \stemDown e16 \stemDown g16 \stemDown f16 )
    \stemDown c'16 ( \stemDown f,16 \stemDown c'16 \stemDown es,16 )
    \stemDown c'16 ( \stemDown es,16 \stemDown f16 \stemDown es16 )
    \stemDown es16 ( \stemDown d16 \stemDown bes'16 \stemDown d,16 ) |
    \barNumberCheck #50
    \stemDown d16 ( \stemDown c16 \stemDown b16 \stemDown c16 \stemDown
    b16 \stemDown c16 \stemDown d16 \stemDown es16 ) \stemDown es16 (
    \stemDown d16 ) \stemDown f16 ( \stemDown d16 ) \stemDown d16 (
    \stemDown c16 ) \stemDown f16 ( \stemDown cis16 ) \pageBreak | % 51
    \stemDown f16 ( _\< \stemDown cis16 ) \stemDown f16 ( \stemDown cis16
    ) \stemDown f16 ( \stemDown cis16 ) \stemDown es16 ( \stemDown d16 )
    \stemDown d16 ( _\! _\> \stemDown bes16 \stemDown f'16 \stemDown d16
    \stemDown c8 ) r8 _\! | % 52
    r2 \stemUp d,16 ( \stemUp f16 \stemUp a16 \stemUp bes16 \stemDown c16
    \stemDown bes16 \stemDown es16 \stemDown d16 ) | % 53
    \stemDown c16 ( \stemDown b16 \stemDown d16 \stemDown c16 ) \stemUp
    b16 ( \stemUp c16 ) \stemUp f,16 ( \stemUp c'16 ) \stemUp c16 (
    \stemUp f,16 ) \stemUp f16 ( \stemUp bes16 ) \stemDown bes16 (
    \stemDown f'16 ) \stemDown g16 ( \stemDown f16 ) | % 54
    \stemDown f16 ( _\< \stemDown es16 \stemDown d16 \stemDown es16 )
    \stemDown d16 ( \stemDown es16 ) \stemDown es16 ( \stemDown f16 )
    \stemDown f16 ( _\! _\> \stemDown es16 ) \stemDown g16 ( \stemDown
    es16 ) \stemDown d8 r8 | % 55
    r2 _\! r16 \stemDown es16 ( \stemDown d16 \stemDown bes16 \stemDown
    g'4 ) ~ _\markup{ \italic {cresc.} } \break | % 56
    \stemUp g8 \stemUp g,,8 ~ \stemUp g16 \stemUp g'16 ( \stemUp g'16 )
    \stemUp g16 \stemDown g16 \stemDown g,16 ( \stemDown g'16 )
    \stemDown g16 \stemDown g16 \stemDown g16 ( \stemDown a16 \stemDown
    bes16 ) | % 57
    \stemDown bes16 _\> \stemDown bes16 ( \stemDown a16 \stemDown bes16
    \stemDown c16 \stemDown bes16 \stemDown d16 ) \stemDown f,16 (
    \stemDown e16 \stemDown f16 \stemDown bes16 ) \stemDown d,16 (
    \stemDown g16 _\! _\p \stemDown f16 \stemDown es16 \stemDown c16 | % 58
    \stemDown b16 \stemDown c16 \stemDown f,16 ) \stemDown g'16 (
    \stemDown f16 \stemDown c16 \stemDown es16 \stemDown d16 ) \stemDown
    c16 ( \stemDown bes8. ) r4 | % 59
    r2 \stemUp bes,8 r8 r4 | \barNumberCheck #60
    r2 \stemUp bes8 \stemUp <bes d>8 \stemUp <bes g'>8 _\markup{ \italic
        {cresc.} } r8 \pageBreak | % 61
    \acciaccatura { \stemUp bes32 ( \stemUp es32 } \stemUp g8 ) r8
    \acciaccatura { \stemUp bes,32 ( \stemUp es32 } \stemUp g8 ) r8
    \acciaccatura { \stemUp bes,32 ( \stemUp c32 } \stemUp g'8 ) r8
    \acciaccatura { \stemUp bes,32 ( \stemUp c32 } \stemUp g'8 ) r8 | % 62
    \acciaccatura { \stemUp bes,32 ( \stemUp c32 } \stemUp g'8 ) _\>
    \acciaccatura { \stemUp bes,32 ( \stemUp d32 } \stemUp f8 )
    \acciaccatura { \stemUp bes,32 ( \stemUp d32 } \stemUp f8 ) r8
    \acciaccatura { \stemUp bes,32 ( \stemUp d32 } \stemUp f8 ) _\! _\p
    r8 \acciaccatura { \stemUp a,32 ( \stemUp c32 } \stemUp es8 ) r8 | % 63
    \acciaccatura { \stemUp es32 ( } \stemUp a8 ) _\markup{ \italic
        {più} } _ "" r8 \acciaccatura { \stemUp es32 ( } \stemUp a8 ) r8
    \acciaccatura { \stemUp es32 ( } \stemUp a8 ) r8 \acciaccatura {
        \stemUp es32 ( } \stemUp a8 ) r8 | % 64
    \acciaccatura { \stemUp es32 ( } \stemUp a8 ) _\pp r8 \acciaccatura
    { \stemUp d,32 ( \stemUp fis32 } \stemUp a8 ) r8 \acciaccatura {
        \stemUp d,32 ( \stemUp fis32 } \stemUp a8 ) r8 \acciaccatura {
        \stemUp d,32 ( \stemUp g32 } \stemDown b8 ) r8 \bar "||"
    \pageBreak | % 65
    \time 3/4  \key g \major R2.*2 | % 67
    r4 r4 r8 \stemDown d8 ~ _\markup{ \italic {cresc.} } | % 68
    \stemDown d4 ( \stemUp d,8 ) r8 r4 | % 69
    R2. | \barNumberCheck #70
    r4 r4 r8 \stemDown b''8 ~ _\markup{ \italic {cresc.} } \pageBreak | % 71
    \stemDown b8 ( \stemDown a8 ) \stemDown a8 r8 r4 | % 72
    r4 r4 \stemDown g8 ( _\markup{ \italic {morendo} } \stemDown b,8 | % 73
    \stemDown d8 ) \stemDown d'4 ( _\markup{ \italic {cresc.} }
    \stemDown c8 ) \stemDown b8 ( -. \stemDown a8 ) -. | % 74
    r8 \stemDown d4 ( \stemDown b8 ) \stemDown a8 ( -. \stemDown g8 ) -.
    | % 75
    r8 \stemDown d4 ( \stemDown c8 ) \stemDown c'8 ( -. \stemDown c8 )
    -. | % 76
    r8 \stemDown d,4 ( \stemDown b8 ) _\> \stemDown g'8 ( -. \stemDown g8
    ) -. | % 77
    r8 _\! \stemDown d'4 ( _\markup{ \italic {cresc.} } \stemDown c8 )
    \stemDown b8 ( -. \stemDown a8 ) -. \pageBreak | % 78
    r8 \stemDown d4 ( \stemDown b8 ) \stemDown a8 ( -. \stemDown g8 ) -.
    | % 79
    r8 \stemDown d4 ( \stemDown c8 ) \stemUp c,8 ( _\> \stemUp c'8 ) |
    \barNumberCheck #80
    r8 _\! \stemDown c4 ( _\markup{ \italic {morendo} } \stemUp fis,8 )
    \stemUp g8 ( -. \stemUp b8 ) -. | % 81
    r8 \stemDown c4 ( _\markup{ \italic {più} } _ "" \stemUp fis,8 )
    \stemUp g8 ( -. \stemUp g,8 ) -. | % 82
    r8 \stemUp bes8 ( _\pp \stemUp g'8 \stemUp es8 \stemUp d8 \stemUp d'8
    ) \bar "||"
    \time 4/4  \key es \major \stemDown es4 r4 r2 | % 84
    R1 \break | % 85
    r4 r8 \stemDown bes'8 ^\markup{ \italic {pizz.} } \stemDown bes8 r8
    r4 | % 86
    R1 | % 87
    r4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown bes8 \stemDown bes8 }
    \stemDown bes4 r4 | % 88
    R1*2 \pageBreak | \barNumberCheck #90
    r2 r4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown ges8 \stemDown ges8 }
    | % 91
    \stemDown ges4 r4 r4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown ges8 \stemDown ges8 }
    | % 92
    \stemDown ges4 r4 r2 | % 93
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown ges8 \stemDown ges8 }
    \stemDown ges4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown ges8 \stemDown ges8 }
    \stemDown ges4 | % 94
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown ges8 \stemDown ges8 }
    \stemDown ges4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown ges8 \stemDown ges8 }
    \stemDown ges4 \break | % 95
    r2 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fes8 \stemDown bes8 \stemDown des8 }
    r4 | % 96
    R1 | % 97
    r2 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fes,8 _\markup{ \italic {cresc.} } \stemDown bes8
        \stemDown des8 }
    r4 | % 98
    r2 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fes,8 _\markup{ \italic {cresc.} } \stemDown bes8
        \stemDown des8 }
    \stemDown d4 \bar "||"
    \pageBreak | % 99
    \time 12/8  \key bes \major \acciaccatura { \stemUp d,,32 ( \stemUp
        d'32 } \stemDown d'4. ) ~ _ "" _\markup{ \italic {dolce} }
    ^\markup{ \italic {arco} } \stemDown d16 ( \stemDown c16 \stemDown
    bes16 \stemDown d16 \stemDown c16 \stemDown bes16 \stemDown a16
    \stemDown c16 \stemDown bes16 \stemDown a16 \stemDown bes16
    \stemDown c16 \stemDown f,16 \stemDown a16 \stemDown g16 \stemDown f16
    \stemDown g16 \stemDown a16 ) | \barNumberCheck #100
    \stemDown bes16 ( \stemDown c16 \stemDown bes16 \stemDown a16
    \stemDown bes16 \stemDown c16 \stemDown cis16 \stemDown d16
    \stemDown c16 \stemDown bes16 \stemDown a16 \stemDown g16 \stemUp f16
    ) \stemUp e,16 ( \stemUp f16 \stemUp g16 \stemUp a16 \stemUp bes16
    \stemDown c16 \stemDown d16 \stemDown f16 \stemDown es16 \stemDown d16
    \stemDown es16 ) \pageBreak | % 101
    \stemUp cis16 ( _\< \stemUp d16 \stemUp d,16 \stemUp d'16 \stemUp es16
    \stemUp d16 ) \stemDown e16 ( \stemDown f16 \stemDown f,16 \stemDown
    f'16 \stemDown g16 \stemDown f16 ) \stemDown a16 ( \stemDown bes16 )
    \stemDown bes,16 ( \stemDown bes'16 ) \stemDown bes,16 ( \stemDown
    bes'16 ) \stemDown bes,16 ( _\! _\> \stemDown bes'16 ) \stemDown
    bes,16 ( \stemDown bes'16 ) \stemDown c,16 ( \stemDown c'16 ) | % 102
    \stemDown d16 -. _\! \stemDown a,16 ( _\< \stemDown bes16 \stemDown
    c16 \stemDown d16 \stemDown es16 \stemDown g16 \stemDown f16
    \stemDown e16 \stemDown f16 \stemDown es16 \stemDown f16 \stemDown c16
    ) _\! _\> \stemDown f16 ( \stemDown es16 \stemDown d16 \stemDown c16
    \stemDown bes16 \stemUp a16 \stemUp g16 \stemUp f16 \stemUp es16
    \stemUp d16 \stemUp c16 ) | % 103
    \stemUp bes4 _\! r8 r4 r8 \stemUp f'16 ( _\markup{ \italic {cresc.}
        } \stemUp g16 \stemUp a16 \stemUp bes16 \stemUp b16 \stemUp c16
    \stemDown b16 _\markup{ \italic {dim.} } \stemDown c16 \stemDown d16
    \stemDown c16 \stemDown b16 \stemDown c16 ) \pageBreak | % 104
    \stemDown c4 ( \stemUp bes16 \stemUp a16 \stemUp c16 \stemUp f,16
    \stemUp g16 \stemUp f16 \stemUp a16 \stemUp c16 ) \stemDown c4 (
    \stemDown bes8 ) ~ \stemDown bes16 \stemDown bes16 ( \stemDown a16
    \stemDown bes16 \stemDown g'16 \stemDown f16 ) ~ | % 105
    \stemDown f16 ( \stemDown c16 \stemDown b16 \stemDown c16 \stemDown
    g'16 _> \stemDown f16 ) \stemDown f16 ( \stemDown es16 \stemDown b16
    \stemDown c16 \stemDown f16 _> \stemDown es16 ) \stemDown f16 (
    \stemDown es16 \stemDown d16 \stemDown es16 \stemDown c'16 _>
    \stemDown es,16 ) \stemDown es16 ( \stemDown d16 \stemDown cis16
    \stemDown d16 \stemDown bes'16 _> \stemDown d,16 ) | % 106
    \stemDown d16 ( \stemDown b16 \stemDown d16 ) \stemDown c16 (
    \stemDown g16 \stemDown c16 ) \stemDown b16 ( \stemDown c16
    \stemDown d16 ) \stemDown c16 ( \stemDown d16 \stemDown es16 )
    \stemDown cis16 ( \stemDown d16 \stemDown f,16 ) \stemDown d'16 (
    \stemDown es16 \stemDown d16 ) \stemDown b16 ( \stemDown c16
    \stemDown f,16 ) \stemDown c'16 ( \stemDown f16 ) \stemDown cis16 (
    \pageBreak | % 107
    \stemDown f16 ) _\< \stemDown cis16 ( \stemDown f16 ) \stemDown cis16
    ( \stemDown f16 ) \stemDown cis16 ( \stemDown f16 ) \stemDown cis16
    ( \stemDown f16 ) \stemDown cis16 ( \stemDown es16 \stemDown d16 )
    \stemDown d16 ( _\! _\> \stemDown c16 \stemDown bes16 \stemDown a16
    \stemDown bes16 \stemDown b16 ) \stemDown c4 _\! r8 | % 108
    r2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp bes,16 ( \stemUp c16 \stemUp d16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp es16 \stemUp f16 \stemUp g16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a16 \stemUp bes16 \stemUp c16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d16 \stemDown es16 \stemDown e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f16 \stemDown g16 \stemDown a16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown bes16 \stemDown f16 \stemDown d16 ) }
    \pageBreak | % 109
    \stemDown d16. ( -> \stemDown b32 ) \stemDown d16. ( -> \stemDown c32
    ) \stemDown g16. ( -> \stemDown c32 ) \stemUp d16. ( -> \stemUp c32
    ) \stemUp f,16. ( -> \stemUp c'32 ) \stemUp d16. ( -> \stemUp c32 )
    \stemDown f16. ( \stemDown bes,32 ) \stemDown b16 ( \stemDown c16
    \stemDown cis16 \stemDown d16 \stemDown es16 \stemDown e16 \stemDown
    f16 \stemDown fis16 \stemDown g16 \stemDown f16 ) | \barNumberCheck
    #110
    \stemDown f16 ( _\markup{ \italic {cresc.} } \stemDown es16
    \stemDown es'16 \stemDown d16 \stemDown c16 \stemDown bes16 )
    \stemDown bes16 ( \stemDown a16 \stemDown g16 \stemDown f16
    \stemDown g16 \stemDown es16 ) ~ \stemDown es16 _\> \stemDown es16 (
    \stemDown d16 \stemDown es16 \stemDown es'16. ) \stemDown es,32 ( ~
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown es16 _\! \stemDown d16 \stemDown cis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d16 \stemDown bes16 \stemDown f16 }
    \stemUp d8 ) \pageBreak | % 111
    r2. \stemUp a8 \stemUp a'8 \trill \stemUp bes8 ~ \stemDown bes8 (
    _\markup{ \italic {cresc.} } \stemDown g'4 ) | % 112
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp g,,16 ( \stemUp as16 \stemUp bes16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c16 \stemUp d16 \stemUp es16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp f16 \stemUp g16 \stemUp as16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown a16 \stemDown bes16 \stemDown b16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown c16 \stemDown cis16 \stemDown d16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown es16 \stemDown f16 \stemDown fis16 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown g16 ( \stemDown fis16 \stemDown g16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown bes,16 \stemDown g'16 \stemDown bes,16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown g'16 \stemDown bes,16 \stemDown g'16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown bes,16 \stemDown g'16 \stemDown bes,16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown a'16 \stemDown bes,16 \stemDown a'16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown bes,16 \stemDown bes'16 \stemDown bes,16 ) }
    \pageBreak | % 113
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown a'16 ( _\> \stemDown bes16 \stemDown d16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown c16 \stemDown a16 \stemDown bes16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown d16 \stemDown c16 \stemDown bes16 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown a16 ( \stemDown g16 \stemDown f16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown bes16 \stemDown a16 \stemDown g16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown f16 \stemDown es16 \stemDown d16 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown f16 ( _\! _\p \stemDown e16 \stemDown g16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown f16 \stemDown g,16 \stemDown f16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown d'16 \stemDown f,16 \stemDown f'16 ) }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown f,16 ( \stemDown f'16 \stemDown es16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown d16 \stemDown f16 \stemDown es16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown d16 \stemDown es16 \stemDown c16 ) }
    | % 114
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown b16 ( \stemDown c16 \stemDown b16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown c16 \stemDown b16 \stemDown c16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown b16 \stemDown c16 \stemDown b16 ) }
    \stemDown c32 ( \stemDown b32 \stemDown c32 \stemDown b32 \stemDown
    c32 \stemDown b32 \stemDown c32 \stemDown b32 \stemDown c32
    \stemDown cis32 \stemDown es32 \stemDown d32 ) \stemDown c8 (
    \stemDown bes4 ) r4 r8 \pageBreak | % 115
    r2. r8 r8 \acciaccatura { \stemUp d,16 ( \stemUp f16 } \stemDown bes8
    ) r4 r8 | % 116
    r2. r8 r8 \acciaccatura { \stemUp bes,16 ( \stemUp d16 } \stemDown
    bes'8 ) r4 r8 | % 117
    \acciaccatura { \stemUp bes,16 ( \stemUp g'16 } \stemDown bes4 )
    _\markup{ \italic {cresc.} } r8 \acciaccatura { \stemUp bes,16 (
        \stemUp g'16 } \stemDown bes4 ) r8 \acciaccatura { \stemUp c,16
        ( \stemUp g'16 } \stemDown bes4 ) r8 \acciaccatura { \stemUp c,16
        ( \stemUp g'16 } \stemDown bes4 ) r8 \pageBreak | % 118
    \acciaccatura { \stemUp d,16 ( \stemUp f16 } \stemDown bes4 ) _\> r8
    \acciaccatura { \stemUp f16 ( \stemUp bes16 } \stemDown d4 ) r8
    \acciaccatura { \stemUp a16 ( \stemUp c16 } \stemDown f4 ) _\! _\p r8
    \acciaccatura { \stemUp a,16 ( \stemUp c16 } \stemDown es4 ) r8
    \pageBreak | % 119
    \acciaccatura { \stemUp a,16 ( \stemUp c16 } \stemDown es4 )
    _\markup{ \italic {più} } _ "" r8 \acciaccatura { \stemUp es,16 (
        \stemUp a16 } \stemDown c4 ) r8 \acciaccatura { \stemUp a16 (
        \stemUp c16 } \stemDown es4 ) r8 \acciaccatura { \stemUp f,16 (
        \stemUp bes16 } \stemDown d4 ) r8 | \barNumberCheck #120
    \acciaccatura { \stemUp a16 ( \stemUp c16 } \stemDown es4 ) _\pp r8
    \acciaccatura { \stemUp es,16 ( \stemUp a16 } \stemDown c4 ) r8
    \acciaccatura { \stemUp a16 ( \stemUp c16 } \stemDown es4 )
    _\markup{ \italic {cresc.} } r8 \acciaccatura { \stemUp f,16 (
        \stemUp as16 } \stemDown d4 ) r8 | % 121
    r4 r8 \stemUp <g,, es' es'>4. r4 r8 \stemDown <bes' bes'>4. | % 122
    R1. \pageBreak | % 123
    \stemDown f'2. ( ^\markup{ \italic {espress.} } _\> \stemDown c2. )
    | % 124
    \stemDown es2. ( _\! _\> \stemDown bes2. ) | % 125
    \acciaccatura { \stemUp d8 ( } \stemDown d'4. ) ~ _\! _\markup{
        \italic {dolce} } \stemDown d8 ( \stemDown c8 ) \stemDown bes8
    -. \stemDown bes8 ( \stemDown a8 \stemDown c8 ) \stemDown f,4. | % 126
    \acciaccatura { \stemUp f8 ( } \stemDown d'4. ) ~ \stemDown d16 (
    \stemDown a16 \stemDown bes16 \stemDown a16 \stemDown c16 \stemDown
    bes16 ) \stemDown bes16 ( \stemDown a16 \stemDown bes16 \stemDown b16
    \stemDown c16 \stemDown a16 \stemDown g16 \stemDown f16 \stemDown e16
    \stemDown f16 \stemDown g16 \stemDown es16 ) \pageBreak | % 127
    \stemDown d16 ( _\markup{ \italic {cresc. poco a poco} } \stemDown f16
    \stemDown g16 \stemDown f16 \stemDown es16 \stemDown d16 \stemDown c16
    \stemDown bes16 \stemDown a16 \stemDown bes16 \stemDown c16
    \stemDown d16 \stemDown es16 \stemDown d16 \stemDown c16 \stemDown d16
    \stemDown es16 \stemDown f16 \stemDown g16 \stemDown f16 \stemDown
    es16 \stemDown f16 \stemDown g16 \stemDown a16 ) | % 128
    \stemDown bes16 ( \stemDown d16 \stemDown c16 \stemDown bes16
    \stemDown a16 \stemDown bes16 ) ~ \stemDown bes16 ( \stemDown a16
    \stemDown es'16 \stemDown c16 \stemDown bes16 \stemDown a16 )
    \stemDown c16 ( \stemDown bes16 \stemDown d16 \stemDown bes16
    \stemDown a16 \stemDown g16 ) ~ \stemDown g16 ( \stemDown f16
    \stemDown g16 \stemDown f16 \stemDown g16 \stemDown f16 ) \pageBreak
    | % 129
    \stemDown g16 ( \stemDown f16 \stemDown g16 \stemDown f16 \stemDown
    g16 \stemDown f16 \stemDown g16 \stemDown f16 \stemDown g16
    \stemDown f16 \stemDown g16 \stemDown f16 \stemDown g16 \stemDown f16
    \stemDown g16 \stemDown f16 \stemDown g16 \stemDown f16 \stemDown g16
    \stemDown f16 \stemDown g16 \stemDown f16 \stemDown g16 \stemDown f16
    ) | \barNumberCheck #130
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g16 ( \stemDown f16 \stemDown g16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f16 \stemDown g16 \stemDown f16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g16 \stemDown f16 \stemDown g16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f16 \stemDown g16 \stemDown f16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g16 \stemDown f16 \stemDown g16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f16 \stemDown g16 \stemDown f16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g16 \stemDown f16 \stemDown g16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f16 \stemDown g16 \stemDown f16 }
    \stemDown g32 \stemDown f32 \stemDown g32 \stemDown f32 )
    \afterGrace { \stemDown bes4. ( \trill } { \stemUp a16 \stemUp bes16
        ) } _\f | % 131
    \stemDown g4 -. r8 \stemUp <g,, es' es'>4. r4 r8 \stemDown <bes'
        bes'>4. \pageBreak | % 132
    R1. | % 133
    f'1. _\> | % 134
    \stemDown des4. ( _\! _\> \stemDown c4. \stemDown ces4. \stemDown
    bes4. ) _\! | % 135
    ges'1. _\> | % 136
    \stemDown es2. _\! _\p _\> \stemDown des4 _\! _\pp \stemDown bes8 ~
    _\markup{ \italic {cresc.} } \stemDown bes8 ( \stemDown c8 \stemDown
    des8 ) \pageBreak | % 137
    \stemDown d4. ~ _ "" _\markup{ \italic {dolce} } \stemDown d8 (
    \stemDown c8 ) \stemDown bes8 -. \stemDown bes8 ( \stemDown a8
    \stemDown c8 ) \stemUp f,4. | % 138
    \acciaccatura { \stemUp d'8 ( } \stemDown d'4. ) ~ _\markup{ \italic
        {cresc.} } \stemDown d16 \stemDown a16 ( \stemDown bes16
    \stemDown a16 \stemDown c16 \stemDown bes16 ) \stemDown bes16 (
    \stemDown a16 \stemDown c16 \stemDown a16 \stemDown bes16 \stemDown
    d,16 ) \stemDown d16 ( _\> \stemDown c16 ) \stemDown c16 ( \stemDown
    g'16 \stemDown f16 \stemDown f,16 ) | % 139
    \stemDown bes4. ~ _\! _\markup{ \italic {dolce} } ^\markup{ \italic
        {cantabile} } \stemDown bes8 ( \stemDown c8 \stemDown d8 )
    \stemDown d8 ( \stemDown c4 ) ~ \stemUp c8 ( \stemUp a8 \stemUp f8 )
    -. \pageBreak | \barNumberCheck #140
    r16 \stemDown f'16 ( \stemDown g16 \stemDown e16 \stemDown f16
    \stemDown d16 ) \stemDown bes4. r16 \stemDown f'16 ( \stemDown g16
    \stemDown e16 \stemDown f16 \stemDown es16 ) \stemUp c16 \stemUp e,16
    ( \stemUp f16 \stemUp g16 \stemUp a16 \stemUp bes16 ) | % 141
    \stemDown c2. ( \stemDown bes4. ~ _\markup{ \italic {cresc.} }
    \stemDown bes4 \stemDown f'8 ) | % 142
    \stemDown f4. ( \stemDown es4. ) ~ \stemDown es4. \stemUp d16 (
    \stemUp f,16 \stemUp a16 \stemUp bes16 \stemUp c16 \stemUp d16 )
    \pageBreak | % 143
    \stemDown d4 ( \stemDown c8 ) \stemUp c16 ( \stemUp f,16 \stemUp g16
    \stemUp a16 \stemUp bes16 \stemUp c16 ) \stemDown c4 ( \stemDown bes8
    ) ~ \stemDown bes16 \stemDown bes16 ( \stemDown c16 \stemDown d16
    \stemDown es16 \stemDown f16 ) | % 144
    \stemDown f16 -. \stemDown c16 ( \stemDown g'16 \stemDown e16
    \stemDown g16 \stemDown f16 ) \stemDown b,16 ( \stemDown c16
    \stemDown f16 \stemDown c16 \stemDown f16 \stemDown es16 ) \once
    \omit TupletBracket
    \times 2/3  {
        \stemDown c'16 ( \stemDown es,16 \stemDown c'16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown es,16 \stemDown c'16 \stemDown es,16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c'16 \stemDown es,16 \stemDown c'16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown d,16 _\> \stemDown bes'16 \stemDown d,16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown bes'16 \stemDown d,16 \stemDown bes'16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown d,16 \stemDown bes'16 \stemDown d,16 ) }
    \pageBreak | % 145
    \stemDown c4 _\! _\p r8 r4 r8 r16 \stemUp f,16 ( _\< \stemUp g16
    \stemUp a16 \stemUp bes16 \stemUp c16 \stemDown d16 _\! _\>
    \stemDown f16 \stemDown bes16 \stemDown f16 ) \stemDown es16 ( -.
    \stemDown d16 ) -. | % 146
    \stemDown c4 _\! r8 r4 r8 r16 \stemUp f,16 ( _\< \stemUp g16 \stemUp
    a16 \stemUp bes16 \stemUp c16 ) \once \omit TupletBracket
    \times 2/3  {
        \stemDown d16 ( \stemDown f16 \stemDown e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f16 _\! _\> \stemDown bes16 \stemDown a16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown bes16 \stemDown d16 \stemDown d,16 ) }
    \pageBreak | % 147
    \stemDown c4 _\! _\markup{ \italic {cresc.} } r8 \acciaccatura {
        \stemUp a16 ( \stemUp c16 } \stemDown es4. ) ~ _\ff \stemDown es8
    ( _\markup{ \italic {dim.} } \stemDown c8 \stemDown a8 ) \stemDown
    a'8 ( \stemDown es8 \stemDown c8 ) | % 148
    \stemDown c'8 ( \stemDown a8 \stemDown es8 \stemDown es'8 \stemDown
    c8 \stemDown a8 \stemDown es8 _\p \stemDown c8 \stemDown a8 \stemUp
    f8 \stemUp g8 \stemUp es8 ) | % 149
    \stemUp d4. _\markup{ \italic {cresc.} } \stemUp g4 ~ \stemUp g16 (
    \stemUp f16 ) \stemUp f4. ~ \stemUp f16 \stemUp es16 ( \stemUp d16
    \stemUp es16 \stemUp f16 \stemUp es16 ) | \barNumberCheck #150
    \stemUp d4. \stemDown g'4 ~ \stemDown g16 ( \stemDown f16 )
    \stemDown f4 ( \stemDown bes8 ) ~ \stemDown bes8 \stemDown a16 ( _\f
    \stemDown bes16 \stemDown c16 \stemDown d16 ) \pageBreak | % 151
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown es16 ( _\> \stemDown a,16 \stemDown bes16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c16 \stemDown es,16 \stemDown f16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g16 \stemDown c,16 \stemDown d16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp es16 \stemUp c16 \stemUp bes16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a16 \stemUp g16 \stemUp f16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp es16 \stemUp d16 \stemUp c16 ) }
    \stemUp bes4 _\! _\p r8 r4 r8 | % 152
    r2. r4 r8 r8 r8 \stemUp es8 ~ \pageBreak | % 153
    \stemUp es8 ( _\markup{ \italic {sempre} } _ "" \stemUp d8 ) r8 r8
    r8 \stemUp es8 ~ \stemUp es8 ( \stemUp d8 ) \stemUp es8 ~ \stemUp es8
    ( \stemUp d8 ) \stemUp es8 \pageBreak | % 154
    \stemUp f4. ( _\markup{ \italic {cresc.} } \stemDown bes4. \stemDown
    d4. \stemDown f4. ) | % 155
    \stemDown <d, bes' bes'>4 _\f r8 r4 r8 \stemDown f'4 _\fp r8 r4 r8 | % 156
    \stemDown es4 _\p r8 \stemDown f4 r8 \stemDown d4 ( \stemDown d'8 )
    ~ \stemDown d16 ( \stemDown c16 \stemDown bes16 \stemDown a16
    \stemDown g16 \stemDown f16 ) | % 157
    \stemDown es4 r8 \stemDown <f, c' f>4 _\f r8 \stemUp <bes, d>4
    ^\markup{ \italic {pizz.} } r8 r4 r8 \bar "|."
    }

PartPNineVoiceTwo =  \relative bes'' {
    \clef "treble" \time 4/4 \key bes \major s1*9 \pageBreak s1*10
    \pageBreak s1*4 \break s1 \bar "||"
    \pageBreak | % 25
    \time 3/4  \key d \major s4*21 \pageBreak s2*9 \pageBreak s4*15 \bar
    "||"
    \pageBreak | % 43
    \time 4/4  \key bes \major s1*4 \break s1*4 \pageBreak s1*5 \break
    s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 65
    \time 3/4  \key g \major s2*9 \pageBreak s4*21 \pageBreak s4*15 \bar
    "||"
    \time 4/4  \key es \major s1*2 \break s1*5 \pageBreak s1*5 \break
    s1*4 \bar "||"
    \pageBreak | % 99
    \time 12/8  \key bes \major s1*3 \pageBreak s2*9 \pageBreak s2*9
    \pageBreak s1*3 \pageBreak s1*3 \pageBreak s1*3 \pageBreak s1*3
    \pageBreak s2*9 \pageBreak s1. \pageBreak s1*6 \pageBreak s1*6
    \pageBreak s1*3 \pageBreak s8*21 \once \override NoteHead.style =
    ##f \stemNeutral bes64 \once \override NoteHead.style = ##f
    \stemNeutral c64 \once \override NoteHead.style = ##f \stemNeutral
    bes64 \once \override NoteHead.style = ##f \stemNeutral c64 \once
    \override NoteHead.style = ##f \stemNeutral bes64 \once \override
    NoteHead.style = ##f \stemNeutral c64 \once \override NoteHead.style
    = ##f \stemNeutral bes64 \once \override NoteHead.style = ##f
    \stemNeutral c64 \once \override NoteHead.style = ##f \stemNeutral
    bes64 \once \override NoteHead.style = ##f \stemNeutral c64 \once
    \override NoteHead.style = ##f \stemNeutral bes64 \once \override
    NoteHead.style = ##f \stemNeutral c64 \once \override NoteHead.style
    = ##f \stemNeutral bes64 \once \override NoteHead.style = ##f
    \stemNeutral c64 \once \override NoteHead.style = ##f \stemNeutral
    bes64 \once \override NoteHead.style = ##f \stemNeutral c64 \once
    \override NoteHead.style = ##f \stemNeutral bes64 \once \override
    NoteHead.style = ##f \stemNeutral c64 \once \override NoteHead.style
    = ##f \stemNeutral bes64 \once \override NoteHead.style = ##f
    \stemNeutral c64 \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
         \once \override NoteHead.style = ##f \stemNeutral bes32 \once
        \override NoteHead.style = ##f \stemNeutral a32 \once \override
        NoteHead.style = ##f \stemNeutral bes32 }
    s1. \pageBreak s2*15 \pageBreak s2*9 \pageBreak s2*9 \pageBreak s1*3
    \pageBreak s1*3 \pageBreak s1*6 \pageBreak s1*3 \pageBreak s1.
    \pageBreak s1*6 \bar "|."
    }

PartPOneZeroVoiceOne =  \relative a {
    \clef "treble" \time 4/4 \key bes \major | % 1
    r2 r4 \stemUp a4 ~ _\p _\< | % 2
    \stemUp a2 ~ \stemUp a4. ( _\! _\> \stemUp bes8 ) | % 3
    \stemUp d2 ( _\! _\p \stemUp c2 | % 4
    \stemUp bes2 \stemUp c2 ) | % 5
    \stemUp d4 ( \stemUp c4 \stemUp bes4 \stemDown bes'4 ) ~ | % 6
    \stemDown bes4 \stemUp <bes, d>8 ( \stemUp c8 \stemUp bes8 \stemUp a8
    \stemUp g'8 \stemUp f8 ) | % 7
    \stemUp f4 r4 r4 \stemUp a,4 ( | % 8
    \stemUp f'4 \stemUp a,4 \stemUp f'4 \stemUp bes,4 | % 9
    \stemUp c4 ) \stemDown c'4 ( ~ \stemDown c4 \stemDown bes4 ) ~
    \pageBreak | \barNumberCheck #10
    \stemDown bes4 ( \stemUp es,4 \stemUp f4 \stemUp a4 ) | % 11
    \stemUp a4. ( \stemDown bes8 ) \stemDown bes4 r4 | % 12
    r2 r4 \stemUp f4 ( | % 13
    \stemUp g4 \stemUp a4 \stemDown bes2 ) ~ | % 14
    \stemDown bes4 ( \stemDown c4 \stemUp a4 \stemDown bes4 ) | % 15
    r2 r8 \stemUp bes8 _\markup{ \italic {cresc.} } \stemUp <g bes>8
    \stemUp <g bes>8 | % 16
    \stemUp <g bes>8 _\> \stemUp <g bes>8 \stemUp <g bes>8 \stemUp <g
        bes>8 \stemUp <g bes>8 _\! _\p \stemUp <c, g'>8 \stemUp <c g'>8
    \stemUp <c g'>8 | % 17
    \stemUp <c g'>8 _\> \stemUp <d f>8 \stemUp <d f>8 \stemUp <d f>8
    \stemUp <d f>8 _\! _\p \stemUp bes'8 ( \stemUp a8 \stemUp c8 ) | % 18
    \stemUp es,4. ( \stemUp f8 \stemUp <d f>4 ) r4 | % 19
    r2 \stemUp bes8 r8 r4 \pageBreak | \barNumberCheck #20
    r2 \stemUp bes8 \stemUp <bes d>8 \stemUp <bes g'>8 _\markup{ \italic
        {cresc.} } r8 | % 21
    \acciaccatura { \stemUp g32 ( \stemUp bes32 } \stemUp es8 ) r8
    \acciaccatura { \stemUp g,32 ( \stemUp bes32 } \stemUp es8 ) r8
    \acciaccatura { \stemUp g,32 ( \stemUp bes32 } \stemUp c8 ) r8
    \acciaccatura { \stemUp g32 ( \stemUp bes32 } \stemUp c8 ) r8 | % 22
    \acciaccatura { \stemUp g32 ( \stemUp bes32 } \stemUp c8 ) _\>
    \acciaccatura { \stemUp bes32 ( \stemUp d32 } \stemUp bes8 )
    \acciaccatura { \stemUp bes32 ( \stemUp d32 } \stemUp bes8 ) r8
    \acciaccatura { \stemUp bes32 ( \stemUp d32 } \stemUp bes8 ) _\! _\p
    r8 \acciaccatura { \stemUp a32 ( \stemUp c32 } \stemUp a8 ) r8 | % 23
    \acciaccatura { \stemUp a32 ( } \stemUp es'8 ) _\markup{ \italic
        {più} } _ "" r8 \acciaccatura { \stemUp a,32 ( } \stemUp es'8 )
    r8 \acciaccatura { \stemUp a,32 ( } \stemUp es'8 ) r8 \acciaccatura
    { \stemUp a,32 ( } \stemUp d8 ) r8 \break | % 24
    \acciaccatura { \stemUp a32 ( } \stemUp d8 ) _\pp r8 \acciaccatura {
        \stemUp a32 ( } \stemUp d8 ) r8 \acciaccatura { \stemUp a32 ( }
    \stemUp d8 ) r8 r8 \stemUp fis8 ~ \bar "||"
    \pageBreak | % 25
    \time 3/4  \key d \major \stemUp fis8 ^\markup{ \italic {espressivo}
        } \stemUp e4 ~ _\markup{ \italic {cresc.} } \stemUp e8 ~ \stemUp
    e16 \stemUp fis16 \stemUp g16 \stemUp e16 | % 26
    \stemUp g8 ( \stemUp fis4 ) ~ \stemUp fis8 ~ \stemUp fis16 \stemUp g16
    \stemUp a16 \stemUp fis16 | % 27
    \stemUp a8 \stemUp g4 \stemDown a8 ( -. \stemDown b8 -. \stemDown
    cis8 ) -. | % 28
    \stemDown e8 ( \stemDown d4 ) \stemDown d16 ( _\> \stemDown cis16
    \stemUp b16 \stemUp a16 \stemUp g16 \stemUp fis16 ) | % 29
    \stemUp fis8 ( _\! ^ "" ^\markup{ \italic {cresc.} } \stemUp e4 )
    \stemUp e8 ~ \stemUp e16 ( \stemUp fis16 \stemUp g16 \stemUp e16 ) |
    \barNumberCheck #30
    \stemUp g8 ( \stemUp fis4 ) \stemUp fis8 ~ \stemUp fis16 ( \stemUp g16
    \stemUp a16 \stemUp fis16 ) | % 31
    \stemUp a8 ( \stemUp g4 ) \stemUp b16 ( _\> \stemUp g16 \stemUp fis16
    \stemUp e16 \stemUp d16 \stemUp cis16 ) \pageBreak | % 32
    \stemUp e4. ( _\! _\markup{ \italic {morendo} } \stemUp g,8 )
    \stemUp fis'4 ~ | % 33
    \stemUp fis8 ( ^ "" ^\markup{ \italic {cresc.} } \stemUp e4 )
    \stemUp e8 ~ \stemUp e16 ( \stemUp fis16 \stemUp g16 \stemUp e16 ) | % 34
    \stemUp g8 ( \stemUp fis4 ) \stemUp fis8 ~ \stemUp fis16 ( \stemUp g16
    \stemUp a16 \stemUp fis16 ) | % 35
    \stemUp a8 ( \stemUp g4 ) \stemDown a8 ( -. \stemDown b8 -.
    \stemDown cis8 ) -. | % 36
    \stemDown e8 ( \stemDown d4 ) \stemDown d16 ( _\> \stemDown cis16
    \stemUp b16 \stemUp a16 \stemUp g16 \stemUp fis16 ) | % 37
    \stemUp fis8 ( _\! _\markup{ \italic {cresc.} } \stemUp e4 ) \stemUp
    e8 ~ \stemUp e16 ( \stemUp fis16 \stemUp g16 \stemUp e16 )
    \pageBreak | % 38
    \stemUp g8 ( \stemUp fis4 ) \stemUp fis8 ~ \stemUp fis16 ( \stemUp g16
    \stemUp a16 \stemUp fis16 ) | % 39
    \stemUp a8 ( \stemUp g4 ) \stemUp b16 ( _\> \stemUp g16 \stemUp fis16
    \stemUp e16 \stemUp d16 \stemUp cis16 ) | \barNumberCheck #40
    \stemUp e4. ( _\! _\markup{ \italic {morendo} } \stemUp g,8 )
    \stemUp fis'4 | % 41
    r4 r8 \stemUp g8 ( _\markup{ \italic {più} } _ "" \stemUp f4 ) | % 42
    r4 _\pp \stemUp <d f>4 ^\markup{ \italic {pizz.} } \stemUp <c a'>8 r8
    ^\fermata \bar "||"
    \pageBreak | % 43
    \time 4/4  \key bes \major r8 \stemUp d8 \stemUp f4 r8 \stemUp c8
    \stemUp f4 | % 44
    r8 \stemUp bes,8 \stemUp f'4 r8 \stemUp c8 \stemDown c'4 | % 45
    r8 \stemUp bes,8 \stemUp d8 \stemUp c8 r8 \stemUp bes8 \stemUp e4 | % 46
    r8 \stemUp bes8 \stemUp <d f>8 \stemUp <d bes'>8 \stemUp <es c'>4 r4
    \break | % 47
    \stemUp bes2 ~ ^\markup{ \italic {arco} } _\< \stemUp bes8 ( \stemUp
    a8 _\! _\> \stemUp g'8 \stemUp <c, f>8 ) | % 48
    r8 _\! \stemUp c8 ^\markup{ \italic {pizz.} } \stemUp f4 r8 \stemUp
    bes,8 \stemDown bes'4 | % 49
    r8 \stemUp c,8 \stemDown c'4 r8 \stemDown c8 \stemDown bes8 r8 |
    \barNumberCheck #50
    r8 \stemUp g,8 \stemUp g'4 r8 \stemUp d8 \stemUp f4 \pageBreak | % 51
    r8 \stemUp a,8 \stemUp f'4 r8 \stemUp f8 \stemUp f8 r8 | % 52
    r2 r8 \stemUp <bes, d>8 \stemUp <d bes'>4 | % 53
    r8 \stemUp g8 \stemUp <f a>4 r8 \stemUp f8 \stemDown bes4 | % 54
    r8 \stemUp es,8 \stemDown es'4 r8 \stemUp f,8 \stemUp <f d'>8 r8 | % 55
    r2 r8 \stemUp bes,8 \stemUp <g' bes>8 _\markup{ \italic {cresc.} }
    \stemUp <g bes>8 \break | % 56
    \stemUp <g bes>8 \stemUp bes,8 \stemUp <g' bes>4 r8 \stemUp bes,8
    \stemUp <e c'>4 | % 57
    r8 _\> \stemUp <d f>8 \stemUp <f d'>4 r8 \stemUp <d f>8 _\! _\p
    \stemUp <es c'>4 | % 58
    r8 \stemUp <c es>8 \stemUp <es c'>8 \stemUp <d d'>8 \stemUp <d bes'>4
    r4 | % 59
    r2 \stemUp bes8 ^\markup{ \italic {arco} } r8 r4 | \barNumberCheck
    #60
    r2 \stemUp bes8 \stemUp <bes d>8 \stemUp <bes g'>8 _\markup{ \italic
        {cresc.} } r8 \pageBreak | % 61
    \acciaccatura { \stemUp g32 ( \stemUp bes32 } \stemUp es8 ) r8
    \acciaccatura { \stemUp g,32 ( \stemUp bes32 } \stemUp es8 ) r8
    \acciaccatura { \stemUp g,32 ( \stemUp bes32 } \stemUp c8 ) r8
    \acciaccatura { \stemUp g32 ( \stemUp bes32 } \stemUp c8 ) r8 | % 62
    \acciaccatura { \stemUp g32 ( \stemUp a32 } \stemUp c8 ) _\>
    \acciaccatura { \stemUp bes32 ( \stemUp d32 } \stemUp bes8 )
    \acciaccatura { \stemUp bes32 ( \stemUp d32 } \stemUp bes8 ) r8
    \acciaccatura { \stemUp bes32 ( \stemUp d32 } \stemUp bes8 ) _\! _\p
    r8 \acciaccatura { \stemUp a32 ( \stemUp c32 } \stemUp a8 ) r8 | % 63
    \acciaccatura { \stemUp a32 ( } \stemUp es'8 ) _\markup{ \italic
        {più} } _ "" r8 \acciaccatura { \stemUp a,32 ( } \stemUp es'8 )
    r8 \acciaccatura { \stemUp a,32 ( } \stemUp es'8 ) r8 \acciaccatura
    { \stemUp a,32 ( } \stemUp d8 ) r8 | % 64
    \acciaccatura { \stemUp a32 ( } \stemUp d8 ) _\pp r8 \acciaccatura {
        \stemUp a32 ( \stemUp d32 } \stemUp fis8 ) r8 \acciaccatura {
        \stemUp a,32 ( \stemUp d32 } \stemUp fis8 ) r8 \acciaccatura {
        \stemUp b,32 ( \stemUp d32 } \stemUp g8 ) r8 \bar "||"
    \pageBreak | % 65
    \time 3/4  \key g \major R2. | % 66
    r4 r4 r8 \stemUp g8 ~ _\markup{ \italic {cresc.} } | % 67
    \stemUp g4 ( \stemUp fis8 ) r8 r4 | % 68
    R2. | % 69
    r4 r4 r8 \stemUp a8 ~ _\markup{ \italic {cresc.} } | \barNumberCheck
    #70
    \stemUp a8 ( \stemUp g8 ) \stemUp g8 r8 r8 \stemDown b8 ~ \pageBreak
    | % 71
    \stemUp b8 ( \stemUp a8 ) \stemUp a8 r8 r4 | % 72
    r4 r4 \stemUp b8 ( _\markup{ \italic {morendo} } \stemUp g8 | % 73
    \stemUp d8 ) \stemUp fis8 _\markup{ \italic {cresc.} } ^\markup{
        \italic {pizz.} } \stemUp c'8 \stemUp a8 \stemUp d8 \stemUp c8 | % 74
    r8 \stemUp d,8 \stemUp b'8 \stemUp g8 \stemUp d'8 \stemUp d,8 | % 75
    r8 \stemUp c8 \stemUp a'8 \stemUp fis8 \stemUp c8 \stemUp a'8 | % 76
    r8 \stemUp b,8 \stemUp b'8 _\> \stemUp g8 \stemUp <b, g'>8 \stemUp
    b'8 | % 77
    r8 _\! \stemUp fis8 _\markup{ \italic {cresc.} } \stemUp c'8 \stemUp
    a8 \stemUp d8 \stemUp c8 \pageBreak | % 78
    r8 \stemUp d,8 \stemUp b'8 \stemUp g8 \stemUp <b, g'>8 \stemUp b'8 | % 79
    r8 \stemUp c,8 \stemUp a'8 \stemUp <fis a>8 _\> \stemUp c8 \stemUp
    <c a'>8 | \barNumberCheck #80
    r8 _\! \stemUp c8 _\markup{ \italic {morendo} } \stemUp a'8 \stemUp
    fis8 \stemUp b8 \stemUp g8 | % 81
    r8 \stemUp c,8 _\markup{ \italic {più} } _ "" \stemUp c'8 \stemUp
    <c, a'>8 \stemUp <bes g'>8 \stemUp bes8 | % 82
    r8 \stemUp bes8 _\pp \stemUp bes8 \stemUp g8 \stemUp as8 \stemUp as'8
    \bar "||"
    \time 4/4  \key es \major \stemUp <bes, g'>4 r4 r2 | % 84
    R1 \break | % 85
    r2 r4 r8 \stemDown bes'8 ^\markup{ \italic {pizz.} } | % 86
    \stemDown bes8 r8 r4 r2 | % 87
    r2 r4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown bes8 \stemDown bes8 }
    | % 88
    \stemDown bes4 r4 r2 | % 89
    R1 \pageBreak | \barNumberCheck #90
    r4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp ges8 \stemUp ges8 }
    \stemUp ges4 r4 | % 91
    r4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp ges8 \stemUp ges8 }
    \stemUp ges4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp ges8 \stemUp ges8 }
    | % 92
    \stemUp ges4 r4 r2 | % 93
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp ges8 \stemUp ges8 }
    \stemUp ges4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp ges8 \stemUp ges8 }
    \stemUp ges4 | % 94
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp ges8 \stemUp ges8 }
    \stemUp ges4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp ges8 \stemUp ges8 }
    \stemUp ges4 \break | % 95
    r2 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown des''8 \stemDown bes8 \stemDown fes8 }
    | % 96
    \stemDown es4 r4 r2 | % 97
    r2 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown des'8 _\markup{ \italic {cresc.} } \stemDown bes8
        \stemDown fes8 }
    | % 98
    r2 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown d'8 _\markup{ \italic {cresc.} } \stemDown bes8
        \stemDown f8 }
    \bar "||"
    \pageBreak | % 99
    \time 12/8  \key bes \major \stemUp <d, d'>4 _\p r8 r8 \stemUp d'8
    \stemUp f,8 \stemUp es4 r8 r8 \stemUp c'8 \stemUp es,8 |
    \barNumberCheck #100
    \stemUp d4 r8 r8 \stemUp f8 \stemUp d8 \stemUp c4 r8 r8 \stemUp c8
    \stemUp a8 \pageBreak | % 101
    \stemUp d4 r8 r8 \stemUp c'8 _\< \stemUp f,8 \stemDown bes4 _\! r8 r8
    \stemUp bes8 _\> \stemUp e,8 | % 102
    \stemUp f4 _\! r8 r8 \stemUp d8 \stemUp es8 \stemUp es4 r8 r8
    \stemUp bes8 \stemUp c8 | % 103
    \stemUp d4 r8 r8 \stemUp d8 \stemUp es8 \stemUp es4 r8 r8 \stemUp c8
    \stemUp a8 \pageBreak | % 104
    \stemUp <a f'>4 r8 r8 \stemUp f'8 \stemUp <c f>8 \stemUp <d f>4 r8 r8
    \stemUp bes'8 \stemUp f8 | % 105
    \stemUp <f c'>4 r8 r8 \stemUp c'8 \stemUp f,8 \stemUp f4 r8 r8
    \stemUp bes8 \stemUp d,8 | % 106
    \stemUp <g, g'>4 r8 r8 \stemUp es'8 \stemUp bes8 \stemUp <bes d>4 r8
    r8 \stemUp f'8 \stemUp f8 \pageBreak | % 107
    \stemUp f4 r8 r8 \stemUp f8 \stemUp f8 \stemUp f4 r8 r8 \stemUp f8
    \stemUp f8 | % 108
    \stemUp f4 r8 r8 \stemUp f8 \stemUp f8 \stemUp f4 r8 r8 \stemUp f8
    \stemUp d8 \pageBreak | % 109
    \stemUp c4 r8 r8 \stemUp c8 \stemUp a8 \stemUp <bes f'>4 r8 r8
    \stemUp f'8 \stemUp bes,8 | \barNumberCheck #110
    \stemUp es4 _\markup{ \italic {cresc.} } r8 r8 \stemDown es'8
    \stemDown a,8 \stemDown es'4 r8 r8 \stemUp d,8 _\> \stemUp bes8
    \pageBreak | % 111
    \stemUp g4 _\! r8 r8 \stemUp es'8 \stemUp a8 \stemUp c8 \stemUp c,8
    \stemUp bes8 \stemUp bes8 _\markup{ \italic {cresc.} } \stemUp bes8
    \stemUp g'8 | % 112
    \stemUp <g bes>4 r8 r8 \stemUp bes,8 \stemUp g'8 \stemUp <c, g'>4 r8
    r8 \stemUp bes'8 \stemUp e,8 \pageBreak | % 113
    \stemDown bes'4 _\> r8 r8 \stemUp bes8 \stemUp d,8 \stemUp d4 _\!
    _\p r8 r8 \stemUp es8 \stemUp c8 | % 114
    \stemUp es4 r8 r8 \stemUp es8 \stemUp d8 \stemUp d4 r8 r4 r8
    \pageBreak | % 115
    r2. r4 r8 r8 \stemDown d'8 \stemDown es8 | % 116
    \stemDown es4 r8 r8 \stemUp f,8 \stemUp f8 \stemUp f8 \stemUp f8
    \stemUp <f bes>8 \stemUp <g bes>8 _\markup{ \italic {cresc.} }
    \stemUp <g bes>8 \stemUp bes,8 | % 117
    \stemUp <g' bes>4 r8 r8 \stemUp bes8 \stemUp bes,8 \stemUp c4 r8 r8
    \stemUp c8 \stemUp c8 \pageBreak | % 118
    \stemUp d4 _\> r8 r8 \stemUp d8 \stemUp bes8 \stemUp c4 _\! _\p r8 r8
    \stemUp c8 \stemUp a8 \pageBreak | % 119
    \stemUp c4 _\markup{ \italic {più} } _ "" r8 r8 \stemUp c8 \stemUp
    a8 \stemUp c4 r8 r8 \stemUp d8 \stemUp bes8 | \barNumberCheck #120
    \stemUp c4 _\pp r8 r8 \stemUp c8 \stemUp a8 \stemUp c4 _\markup{
        \italic {cresc.} } r8 r8 \stemUp as8 \stemDown bes'16 _\f
    ^\markup{ \italic {arco} } \stemDown bes16 | % 121
    \stemDown es4 -. r8 r8 r8 \stemDown es16 \stemDown es16 \stemDown
    bes'4 -. r8 r8 r8 \stemDown bes16 \stemDown bes16 | % 122
    \stemDown <es, es'>8 -. _\sf r8 \stemDown <es es'>16 \stemDown <es
        es'>16 \stemDown <d d'>8 -. _\sf r8 \stemDown <d d'>16 \stemDown
    <d d'>16 \stemDown <c c'>4 r8 r4 r8 \pageBreak | % 123
    R1.*2 | % 125
    r8 \stemUp bes8 _\markup{ \italic {dolce} } ^\markup{ \italic
        {pizz.} } \stemUp f8 \stemUp <d bes'>4 r8 r8 \stemUp es8 \stemUp
    c8 \stemUp es4 r8 | % 126
    r8 \stemUp d'8 \stemUp f,8 \stemUp <f d'>4 r8 r8 \stemUp c'8 \stemUp
    <c, es>8 \stemUp <es c'>8 \stemUp c8 \stemUp <c f>8 \pageBreak | % 127
    r4 r8 r8 r8 \stemUp <d f>8 _\markup{ \italic {cresc. poco a poco} }
    ^\markup{ \italic {arco} } r4 r8 r8 r8 \stemUp <es a>8 | % 128
    r8 r8 \stemUp f8 r8 r8 \stemUp f8 r8 r8 \stemUp f8 r8 r8 \stemUp f8
    \pageBreak | % 129
    r8 r8 \stemDown bes8 r8 \stemDown d8 \stemDown c8 r8 r8 \stemUp a8 r8
    \stemDown bes8 \stemDown c8 | \barNumberCheck #130
    r8 r8 \stemDown d8 r8 \stemDown f8 \stemDown es8 r8 r8 \stemDown c8
    r8 \stemDown d8 \stemDown bes16 _\f \stemDown bes16 | % 131
    \stemDown es4 -. r8 r8 r8 \stemDown es16 \stemDown es16 \stemDown
    bes'4 -. r8 r8 r8 \stemDown bes16 \stemDown bes16 \pageBreak | % 132
    \stemDown <es, es'>8 -. _\sf r8 \stemDown <es es'>16 \stemDown <es
        es'>16 \stemDown <d d'>8 -. _\sf r8 \stemDown <d d'>16 \stemDown
    <d d'>16 \stemDown <c c'>4 r8 r4 r8 | % 133
    r4 r8 r8 r8 \stemUp as16 ( -. _\pp \stemUp as16 ) -. \stemUp as4 r8
    r8 r8 \stemUp as16 ( -. \stemUp as16 ) -. | % 134
    \stemUp as4 r8 r8 r8 \stemUp es16 ( -. \stemUp es16 ) -. \stemUp es4
    r8 r8 r8 \stemUp d16 ( -. \stemUp d16 ) -. | % 135
    \stemUp es4 r8 r8 r8 \stemDown bes'16 ( -. \stemDown bes16 ) -.
    \stemDown bes4 r8 r8 r8 \stemUp es,16 ( -. \stemUp es16 ) -. | % 136
    \stemUp es4 r8 r8 r8 \stemUp f16 ( -. \stemUp f16 ) -. \stemUp f4 (
    \stemUp bes,8 ) ~ _\markup{ \italic {cresc.} } \stemUp bes8 (
    \stemUp c8 \stemUp des8 ) \pageBreak | % 137
    \stemUp <d bes'>8 _\p \stemDown d'8 ^\markup{ \italic {pizz.} }
    \stemDown bes8 \stemUp <f d'>4 r8 r8 \stemUp c'8 \stemUp a8 \stemUp
    <es c'>4 r8 | % 138
    r8 \stemUp d'8 _\markup{ \italic {cresc.} } \stemUp <d, bes'>8
    \stemUp <d d'>4 \stemDown d'8 \stemDown es8 \stemDown es8 \stemDown
    d8 \stemUp <bes, g'>8 _\> \stemUp <bes g'>8 \stemUp <a f'>8 | % 139
    \stemUp <d f>8 _\! _\p r8 r8 \stemUp d4. ^\markup{ \italic {arco} }
    \stemUp c8 ( \stemUp d8 \stemUp es8 ~ \stemUp es8 \stemUp c8 \stemUp
    es8 ) \pageBreak | \barNumberCheck #140
    \stemUp d8 ( \stemUp f8 \stemUp bes8 \stemUp d,8 \stemUp c8 \stemUp
    bes8 \stemUp es8 ) \stemUp c'8 -. \stemUp c8 -. \stemUp c8 ( \stemUp
    a8 ) \stemUp f8 -. | % 141
    \stemUp es8 r8 \stemUp a8 ^\markup{ \italic {pizz.} } \stemDown c4 r8
    r8 \stemUp f,8 _\markup{ \italic {cresc.} } \stemUp bes,8 \stemDown
    bes'4 r8 | % 142
    r8 \stemUp d,8 \stemUp c8 \stemDown c'4 r8 r8 \stemUp c8 \stemUp c,8
    \stemUp bes8 \stemUp d'8 \stemUp d,8 \pageBreak | % 143
    \stemUp c8 \stemUp c8 \stemUp a8 \stemUp f'8 \stemUp c8 \stemUp f8 r8
    \stemUp f8 \stemUp bes,8 \stemUp f'8 \stemUp bes,8 \stemUp f'8 | % 144
    r8 \stemUp f8 \stemUp c8 \stemUp f8 \stemUp c8 \stemUp f8 r8 \stemUp
    f8 \stemUp c8 \stemUp bes8 _\> \stemUp f'8 \stemUp bes8 \pageBreak | % 145
    \stemUp <c, f>4 _\! _\p r8 r4 r8 r8 \stemUp f8 _\< \stemUp c8
    \stemUp bes8 _\! _\> \stemUp bes'8 \stemUp d,8 | % 146
    \stemUp <c es>4 _\! r8 r4 r8 r8 \stemUp c'8 _\< \stemUp es,8 \stemUp
    d8 \stemUp bes'8 _\! _\> \stemUp d8 \pageBreak | % 147
    \stemDown es4 _\! _\markup{ \italic {cresc.} } r8 \stemDown <a, c'>4
    _\ff ^\markup{ \italic {arco} } r8 r8 r8 \stemUp es8 _\markup{
        \italic {dim.} } r8 r8 \stemUp es8 | % 148
    r8 r8 \stemUp es8 r8 r8 \stemUp es8 r8 r8 \stemUp es8 _\p r8 r8
    \stemUp <c es>8 _\pp | % 149
    r8 r8 \stemDown bes'8 _\markup{ \italic {cresc.} } r8 r8 \stemUp
    bes,8 r8 r8 \stemUp <bes d>8 r8 r8 \stemDown <a' c>8 |
    \barNumberCheck #150
    r8 r8 \stemDown bes8 r8 r8 \stemUp <bes, g'>8 r8 r8 \stemUp <bes f'>8
    r8 r8 \stemDown <f' c' a'>8 _\f \pageBreak | % 151
    r2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp d16 ( _ "" _\markup{ \italic {sempre dim.} } \stemUp d16
        \stemUp d16 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp d16 ( \stemUp d16 \stemUp d16 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp d16 ( \stemUp d16 \stemUp d16 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp d16 ( \stemUp d16 \stemUp d16 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp d16 ( \stemUp d16 \stemUp d16 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp es16 ( \stemUp es16 \stemUp es16 ) }
    | % 152
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp es8. :32 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp d8. :32 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp d8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp d8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp d8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp es8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp es8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp d8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp d8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp d8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp <a es'>8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8. :32 }
    \pageBreak | % 153
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8. :32 }
    _\markup{ \italic {sempre} } _ "" \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp <bes d>8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp <bes d>8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp <bes d>8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp <bes d>8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp bes8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp bes8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8. :32 }
    \pageBreak | % 154
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp d8. :32 }
    _\markup{ \italic {cresc.} } \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp d8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp d8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp f8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp f8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp f8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown bes8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown bes8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown bes8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown d8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown d8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown d8. :32 }
    | % 155
    \stemDown <f, d' bes'>4 _\f r8 r4 r8 \stemDown c'4 _\fp r8 r4 r8 | % 156
    \stemDown c4 _\p r8 \stemUp c,4 r8 \stemUp <bes d>4 r8 r4 r8 | % 157
    \stemDown c'4 r8 \stemUp <c, f a>4 _\f r8 \stemUp <d bes'>4
    ^\markup{ \italic {pizz.} } r8 r4 r8 \bar "|."
    }

PartPOneOneVoiceOne =  \relative a {
    \clef "alto" \time 4/4 \key bes \major | % 1
    r2 r4 \stemUp a4 ~ _\p _\< | % 2
    \stemUp a2 ~ \stemUp a4. ( _\! _\> \stemUp bes8 ) | % 3
    \stemUp f4 _\! \stemUp f2 \stemUp f4 ~ | % 4
    \stemUp f4 \stemUp f2 \stemUp f4 ~ | % 5
    \stemUp f4 \stemUp f2 \stemUp e4 | % 6
    \stemUp f4 \stemUp bes4 ~ \stemDown bes8 \stemDown a8 ( \stemDown g'8
    \stemDown f8 ) | % 7
    \stemDown f4 r4 r4 \stemUp f,4 ~ | % 8
    \stemUp f4 \stemUp f2 \stemUp f4 ~ | % 9
    \stemUp f4 \stemUp f2 \stemUp g4 ~ \pageBreak | \barNumberCheck #10
    \stemUp g4 \stemUp bes2 ( \stemDown f'8 \stemDown es8 ) | % 11
    \stemDown es4. ( \stemDown d8 ) \stemDown d4 r4 | % 12
    r2 r4 \stemUp f,4 ( | % 13
    \stemUp g4 \stemUp a4 \stemUp bes4 \stemUp f4 | % 14
    \stemUp g4 \stemUp a4 \stemUp f4 \stemUp bes4 ) | % 15
    r2 r8 \stemUp bes8 _\markup{ \italic {cresc.} } \stemUp <es, g>8
    \stemUp <es g>8 | % 16
    \stemUp <es g>8 _\> \stemUp <es g>8 \stemUp <es g>8 \stemUp <es g>8
    \stemUp <e g>8 _\! _\p \stemUp <g bes>8 \stemUp <g bes>8 \stemUp <g
        bes>8 | % 17
    \stemUp <g bes>8 _\> \stemUp bes8 \stemUp bes8 \stemUp bes8 \stemUp
    bes8 _\! _\p \stemUp d8 ( \stemUp c8 \stemUp a8 ) | % 18
    \stemUp a4. ( \stemUp f8 \stemUp f4 ) r4 | % 19
    r2 \stemUp bes8 r8 r4 \pageBreak | \barNumberCheck #20
    r2 \stemUp bes8 \stemUp <g bes>8 \stemUp <es g>8 _\markup{ \italic
        {cresc.} } r8 | % 21
    \acciaccatura { \stemUp es32 ( \stemUp g32 } \stemUp bes8 ) r8
    \acciaccatura { \stemUp es,32 ( \stemUp g32 } \stemUp bes8 ) r8
    \acciaccatura { \stemUp e,32 ( \stemUp g32 } \stemUp bes8 ) r8
    \acciaccatura { \stemUp e,32 ( \stemUp g32 } \stemUp bes8 ) r8 | % 22
    \acciaccatura { \stemUp e,32 ( \stemUp g32 } \stemUp bes8 ) _\>
    \acciaccatura { \stemUp f32 ( \stemUp bes32 } \stemDown d8 )
    \acciaccatura { \stemUp f,32 ( \stemUp bes32 } \stemDown d8 ) r8
    \acciaccatura { \stemUp f,32 ( \stemUp bes32 } \stemDown d8 ) _\!
    _\p r8 \acciaccatura { \stemUp f,32 ( \stemUp a32 } \stemDown c8 ) r8
    | % 23
    \acciaccatura { \stemUp f,32 ( } \stemUp a8 ) _\markup{ \italic
        {più} } _ "" r8 \acciaccatura { \stemUp f32 ( } \stemUp a8 ) r8
    \acciaccatura { \stemUp f32 ( } \stemUp a8 ) r8 \acciaccatura {
        \stemUp f32 ( } \stemUp a8 ) r8 \break | % 24
    \acciaccatura { \stemUp fis32 ( } \stemUp a8 ) _\pp r8 \acciaccatura
    { \stemUp fis32 ( } \stemUp a8 ) r8 \acciaccatura { \stemUp fis32 (
        } \stemUp a8 ) r8 r8 \stemDown fis'8 ~ \bar "||"
    \pageBreak | % 25
    \time 3/4  \key d \major \stemDown fis8 ^\markup{ \italic
        {espressivo} } \stemDown e4 ~ _\markup{ \italic {cresc.} }
    \stemDown e8 ~ \stemDown e16 \stemDown fis16 \stemDown g16 \stemDown
    e16 | % 26
    \stemDown g8 ( \stemDown fis4 ) ~ \stemDown fis8 ~ \stemDown fis16
    \stemDown g16 \stemDown a16 \stemDown fis16 | % 27
    \stemDown a8 \stemDown g4 \stemDown a8 ( -. \stemDown b8 -.
    \stemDown cis8 ) -. | % 28
    \stemDown e8 ( \stemDown d4 ) \stemDown d16 ( _\> \stemDown cis16
    \stemDown b16 \stemDown a16 \stemDown g16 \stemDown fis16 ) | % 29
    \stemDown fis8 ( _\! ^ "" ^\markup{ \italic {cresc.} } \stemDown e4
    ) \stemDown e8 ~ \stemDown e16 ( \stemDown fis16 \stemDown g16
    \stemDown e16 ) | \barNumberCheck #30
    \stemDown g8 ( \stemDown fis4 ) \stemDown fis8 ~ \stemDown fis16 (
    \stemDown g16 \stemDown a16 \stemDown fis16 ) | % 31
    \stemDown a8 ( \stemDown g4 ) \stemDown b16 ( _\> \stemDown g16
    \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown cis16 )
    \pageBreak | % 32
    \stemUp <g e'>4. ( _\! _\markup{ \italic {morendo} } \stemUp <e g>8
    ) \stemUp <d fis>8 \stemDown fis'8 ~ | % 33
    \stemDown fis8 ( ^ "" ^\markup{ \italic {cresc.} } \stemDown e4 )
    \stemDown e8 ~ \stemDown e16 ( \stemDown fis16 \stemDown g16
    \stemDown e16 ) | % 34
    \stemDown g8 ( \stemDown fis4 ) \stemDown fis8 ~ \stemDown fis16 (
    \stemDown g16 \stemDown a16 \stemDown fis16 ) | % 35
    \stemDown a8 ( \stemDown g4 ) \stemDown a8 ( -. \stemDown b8 -.
    \stemDown cis8 ) -. | % 36
    \stemDown e8 ( \stemDown d4 ) \stemDown d16 ( _\> \stemDown cis16
    \stemDown b16 \stemDown a16 \stemDown g16 \stemDown fis16 ) | % 37
    \stemDown fis8 ( _\! _\markup{ \italic {cresc.} } \stemDown e4 )
    \stemDown e8 ~ \stemDown e16 ( \stemDown fis16 \stemDown g16
    \stemDown e16 ) \pageBreak | % 38
    \stemDown g8 ( \stemDown fis4 ) \stemDown fis8 ~ \stemDown fis16 (
    \stemDown g16 \stemDown a16 \stemDown fis16 ) | % 39
    \stemDown a8 ( \stemDown g4 ) \stemDown b16 ( _\> \stemDown g16
    \stemDown fis16 \stemDown e16 \stemDown d16 \stemDown cis16 ) |
    \barNumberCheck #40
    \stemUp <g e'>4. ( _\! _\markup{ \italic {morendo} } \stemUp <e g>8
    ) \stemUp <d fis>4 | % 41
    r4 r8 \stemUp <e g>8 ( _\markup{ \italic {più} } _ "" \stemUp <d f>4
    ) | % 42
    r4 _\pp \stemUp <d f>4 ^\markup{ \italic {pizz.} } \stemUp <c a'>8 r8
    ^\fermata \bar "||"
    \pageBreak | % 43
    \time 4/4  \key bes \major f1 ~ ^\markup{ \italic {arco} } | % 44
    f1 ~ | % 45
    \stemUp f2. ( \stemUp e4 | % 46
    \stemUp f2. ) r4 \break | % 47
    r2 r4 \stemUp <f a>4 ~ ~ _\! _\< | % 48
    \stemUp a2 _\! \stemUp bes2 | % 49
    \stemUp c2 \stemUp bes2 | \barNumberCheck #50
    \stemUp bes2. \stemUp a4 \pageBreak | % 51
    \stemUp a4. ( \stemUp bes8 ) \stemUp bes4 ( \stemUp a8 ) r8 | % 52
    r2 \stemUp f2 ~ | % 53
    \stemUp g4 ( \stemUp a4 \stemUp bes4 \stemUp f4 ) | % 54
    \stemUp g4 ( _\< \stemUp a4 ~ \stemUp a4 _\! _\> \stemUp bes4 ) | % 55
    r2 _\! r8 \stemUp bes8 \stemUp <es, g>4 ~ ~ _\markup{ \italic
        {cresc.} } \break | % 56
    \stemUp <es g>2 \stemUp <e g>2 ~ ~ | % 57
    \stemUp <e g>8 ( _\> \stemUp bes'4. ) ~ \stemUp bes4 _\! _\p \stemUp
    a4 | % 58
    \stemUp a4. ( \stemUp bes8 ) \stemUp bes4 r4 | % 59
    r2 \stemUp bes8 r8 r4 | \barNumberCheck #60
    r2 \stemUp bes8 \stemUp bes8 \stemUp g8 _\markup{ \italic {cresc.} }
    r8 \pageBreak | % 61
    \acciaccatura { \stemUp es32 ( \stemUp g32 } \stemUp bes8 ) r8
    \acciaccatura { \stemUp es,32 ( \stemUp g32 } \stemUp bes8 ) r8
    \acciaccatura { \stemUp e,32 ( \stemUp g32 } \stemUp bes8 ) r8
    \acciaccatura { \stemUp e,32 ( \stemUp g32 } \stemUp bes8 ) r8 | % 62
    \acciaccatura { \stemUp e,32 ( \stemUp g32 } \stemUp bes8 ) _\>
    \acciaccatura { \stemUp f32 ( \stemUp bes32 } \stemDown d8 )
    \acciaccatura { \stemUp f,32 ( \stemUp bes32 } \stemDown d8 ) r8
    \acciaccatura { \stemUp f,32 ( \stemUp bes32 } \stemDown d8 ) _\!
    _\p r8 \acciaccatura { \stemUp f,32 ( \stemUp a32 } \stemDown c8 ) r8
    | % 63
    \acciaccatura { \stemUp f,32 ( } \stemUp a8 ) _\markup{ \italic
        {più} } _ "" r8 \acciaccatura { \stemUp f32 ( } \stemUp a8 ) r8
    \acciaccatura { \stemUp f32 ( } \stemUp a8 ) r8 \acciaccatura {
        \stemUp fis32 ( } \stemUp a8 ) r8 | % 64
    \acciaccatura { \stemUp fis32 ( } \stemUp a8 ) _\pp r8 \acciaccatura
    { \stemUp fis32 ( \stemUp a32 } \stemDown d8 ) r8 \acciaccatura {
        \stemUp fis,32 ( \stemUp a32 } \stemDown d8 ) r8 \acciaccatura {
        \stemUp g,32 ( \stemUp b32 } \stemDown d8 ) r8 \bar "||"
    \pageBreak | % 65
    \time 3/4  \key g \major r4 r4 r8 \stemUp a8 ~ _\markup{ \italic
        {cresc.} } | % 66
    \stemUp a4 ( \stemUp g8 ) r8 r4 | % 67
    R2. | % 68
    r4 r4 r8 \stemUp d8 ~ _\markup{ \italic {cresc.} } | % 69
    \stemUp d8 ( \stemUp c8 ) \stemUp c8 r8 r8 \stemUp a'8 ~ |
    \barNumberCheck #70
    \stemUp a8 ( \stemUp g8 ) \stemUp g8 r8 r4 \pageBreak | % 71
    r8 \stemUp a16 ( \stemUp gis16 \stemUp a16 _\> \stemUp b16 \stemUp c16
    \stemUp e,16 \stemUp d16 \stemUp c16 \stemUp b'16 \stemUp a16 ) | % 72
    \stemUp a4. ( _\! _\markup{ \italic {morendo} } \stemUp c,8 )
    \stemUp b'8 ( \stemUp g8 | % 73
    \stemUp d8 ) \stemUp fis8 _\markup{ \italic {cresc.} } ^\markup{
        \italic {pizz.} } \stemUp c'8 \stemUp a8 \stemUp d8 \stemUp c8 | % 74
    r8 \stemUp d,8 \stemUp b'8 \stemUp g8 \stemUp d'8 \stemUp d,8 | % 75
    r8 \stemUp c8 \stemUp a'8 \stemUp fis8 \stemUp c8 \stemUp a'8 | % 76
    r8 \stemUp b8 \stemUp b8 _\> \stemUp g8 \stemUp <d g>8 \stemUp b'8 | % 77
    r8 _\! \stemUp fis8 _\markup{ \italic {cresc.} } \stemUp c'8 \stemUp
    a8 \stemUp d8 \stemUp c8 \pageBreak | % 78
    r8 \stemUp d,8 \stemUp b'8 \stemUp g8 \stemUp <d g>8 \stemUp b'8 | % 79
    r8 \stemUp c,8 \stemUp a'8 \stemUp <fis a>8 _\> \stemUp c8 \stemUp
    <c a'>8 | \barNumberCheck #80
    r8 _\! \stemUp c8 _\markup{ \italic {morendo} } \stemUp a'8 \stemUp
    fis8 \stemUp b8 \stemUp g8 | % 81
    r8 \stemUp c,8 _\markup{ \italic {più} } _ "" \stemUp c'8 \stemUp
    <c, a'>8 \stemUp g'8 \stemUp g8 | % 82
    r8 \stemUp g8 _\pp \stemUp es'8 \stemUp bes8 \stemUp f8 \stemUp f'8
    \bar "||"
    \time 4/4  \key es \major \stemDown es4 r4 r2 | % 84
    R1 \break | % 85
    R1 | % 86
    r4 r8 \stemUp bes8 ^\markup{ \italic {pizz.} } \stemUp bes8 r8 r4 | % 87
    R1 | % 88
    r4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp bes8 \stemUp bes8 }
    \stemUp bes4 r4 | % 89
    R1 \pageBreak | \barNumberCheck #90
    R1*3 | % 93
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp ges8 \stemUp ges8 }
    \stemUp ges4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp ges8 \stemUp ges8 }
    \stemUp ges4 | % 94
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp ges8 \stemUp ges8 }
    \stemUp ges4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp ges8 \stemUp ges8 }
    \stemUp ges4 \break | % 95
    r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fes'8 \stemDown bes8 \stemDown des8 }
    r2 | % 96
    \stemDown ces,4 r4 r2 | % 97
    r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fes8 _\markup{ \italic {cresc.} } \stemDown bes8
        \stemDown des8 }
    r2 | % 98
    r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fes,8 _\markup{ \italic {cresc.} } \stemDown bes8
        \stemDown des8 }
    r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown f,8 \stemDown bes8 \stemDown d8 }
    \bar "||"
    \pageBreak | % 99
    \time 12/8  \key bes \major \stemDown <bes, d>4 _\p r8 r8 \stemDown
    f'8 \stemDown d8 \stemDown c4 r8 r8 \stemDown es8 \stemDown c8 |
    \barNumberCheck #100
    \stemUp bes4 r8 r8 \stemUp d8 \stemUp bes8 \stemUp a4 r8 r8 \stemUp
    a8 \stemUp f8 \pageBreak | % 101
    \stemUp f4 r8 r8 \stemDown f'8 _\< \stemDown c8 \stemUp bes4 _\! r8
    r8 \stemUp bes8 _\> \stemUp e,8 | % 102
    \stemUp f4 _\! r8 r8 \stemUp bes8 \stemUp c8 \stemDown c4 r8 r8
    \stemUp g8 \stemUp a8 | % 103
    \stemUp bes4 r8 r8 \stemUp bes8 \stemUp c8 \stemDown c4 r8 r8
    \stemUp a8 \stemUp c8 \pageBreak | % 104
    \stemDown c4 r8 r8 \stemUp c8 \stemUp <f, a>8 \stemUp <f bes>4 r8 r8
    \stemUp bes8 \stemUp f8 | % 105
    \stemUp <f c'>4 r8 r8 \stemUp c'8 \stemUp f,8 \stemUp f4 r8 r8
    \stemUp bes8 \stemUp d,8 | % 106
    \stemUp g4 r8 r8 \stemUp bes8 \stemUp es,8 \stemUp f4 r8 r8 \stemUp
    a8 \stemUp f8 \pageBreak | % 107
    \stemUp f4 r8 r8 \stemUp f8 \stemUp f8 \stemUp f4 r8 r8 \stemUp f8
    \stemUp f8 | % 108
    \stemUp f4 r8 r8 \stemUp f8 \stemUp f8 \stemUp f4 r8 r8 \stemDown d'8
    \stemDown bes8 \pageBreak | % 109
    \stemUp g4 r8 r8 \stemUp a8 \stemUp f8 \stemUp f4 r8 r8 \stemUp bes8
    \stemUp f8 | \barNumberCheck #110
    \stemUp a4 _\markup{ \italic {cresc.} } r8 r8 \stemDown es'8
    \stemDown a,8 \stemDown es'4 r8 r8 \stemUp bes8 _\> \stemUp f8
    \pageBreak | % 111
    \stemUp c4 _\! r8 r8 \stemDown a'8 \stemDown es'8 \stemDown a8
    \stemDown f,8 \stemDown g8 \stemUp g8 _\markup{ \italic {cresc.} }
    \stemUp g8 \stemUp bes8 | % 112
    \stemUp <g bes>4 r8 r8 \stemUp g8 \stemUp bes8 \stemUp <c, bes'>4 r8
    r8 \stemUp bes'8 \stemUp e,8 \pageBreak | % 113
    \stemUp bes'4 _\> r8 r8 \stemUp d8 \stemUp bes8 \stemUp bes4 _\! _\p
    r8 r8 \stemUp c8 \stemUp a8 | % 114
    \stemUp a4 r8 r8 \stemUp a8 \stemUp <f bes>8 \stemUp <f bes>4 r8 r4
    r8 \pageBreak | % 115
    r2. r4 r8 r8 \stemUp <d' bes'>8 \stemUp <es c'>8 | % 116
    \stemUp <es c'>4 r8 r8 \stemUp es8 \stemUp f8 \stemUp es8 \stemUp es8
    \stemUp d8 \stemUp es8 _\markup{ \italic {cresc.} } \stemUp <bes g'>8
    \stemUp g8 | % 117
    \stemDown <bes g'>4 r8 r8 \stemDown g'8 \stemDown g,8 \stemUp <g
        bes>4 r8 r8 \stemUp <g bes>8 \stemUp <g bes>8 \pageBreak | % 118
    \stemUp <f bes>4 _\> r8 r8 \stemUp bes8 \stemUp f8 \stemUp a4 _\!
    _\p r8 r8 \stemUp a8 \stemUp f8 \pageBreak | % 119
    \stemUp a4 _\markup{ \italic {più} } _ "" r8 r8 \stemUp a8 \stemUp
    f8 \stemUp a4 r8 r8 \stemUp bes8 \stemUp f8 | \barNumberCheck #120
    \stemUp a4 _\pp r8 r8 \stemUp a8 \stemUp f8 \stemUp a4 _\markup{
        \italic {cresc.} } r8 r8 \stemUp <f bes>8 \stemUp bes16 _\f
    ^\markup{ \italic {arco} } \stemUp bes16 | % 121
    \stemDown es4 -. r8 r8 r8 \stemDown g16 \stemDown g16 \stemDown <f
        d'>4 -. r8 r8 r8 \stemDown <f d'>16 \stemDown <f d'>16 | % 122
    \stemDown <g es'>8 -. _\sf r8 \stemDown <g bes>16 \stemDown <g bes>16
    \stemDown <f bes>8 -. _\sf r8 \stemDown <f bes>16 \stemDown <f bes>16
    \stemDown <f a>4 r8 r4 r8 \pageBreak | % 123
    R1.*2 | % 125
    r8 \stemDown f8 _\markup{ \italic {dolce} } ^\markup{ \italic
        {pizz.} } \stemDown <bes, d>8 \stemDown <bes d>4 r8 r8 \stemUp c8
    \stemUp a8 \stemDown c4 r8 | % 126
    r8 \stemDown bes'8 \stemDown <bes, d>8 \stemDown <bes d>4 r8 r8
    \stemUp <c es>8 \stemUp f,8 \stemUp <f c'>8 \stemUp f8 \stemUp f8
    \pageBreak | % 127
    r4 r8 r8 r8 \stemUp f8 _\markup{ \italic {cresc. poco a poco} }
    ^\markup{ \italic {arco} } r4 r8 r8 r8 \stemUp <c c'>8 | % 128
    r8 r8 \stemDown <bes' d>8 r8 r8 \stemDown <c a'>8 r8 r8 \stemDown <d
        bes'>8 r8 r8 \stemDown <es a>8 \pageBreak | % 129
    r8 r8 \stemDown f8 r8 \stemDown f8 \stemDown f8 r8 r8 \stemDown f8 r8
    \stemDown f8 \stemDown f8 | \barNumberCheck #130
    r8 r8 \stemUp <f, bes>8 r8 \stemUp <f d'>8 \stemUp <f c'>8 r8 r8
    \stemUp <f a>8 r8 \stemUp <f as>8 \stemUp bes16 _\f \stemUp bes16 | % 131
    \stemDown es4 -. r8 r8 r8 \stemDown es16 \stemDown es16 \stemDown
    bes'4 -. r8 r8 r8 \stemDown bes16 \stemDown bes16 \pageBreak | % 132
    \stemDown <g bes>8 -. _\sf r8 \stemDown <g bes>16 \stemDown <g bes>16
    \stemDown <f bes>8 -. _\sf r8 \stemDown <f bes>16 \stemDown <f bes>16
    \stemDown <f a>4 r8 r4 r8 | % 133
    \stemUp des,2. ~ _\> \stemUp des4. ( \stemUp f4. ) | % 134
    \stemUp as2. ~ _\! _\> \stemUp as4. \stemUp bes4. ~ _\! _\p | % 135
    \stemUp bes4. ( _\> \stemUp es,2. \stemUp ges4. ) | % 136
    \stemUp bes2. ~ _\! _\> \stemUp bes4. _\! _ "" _\markup{ \italic
        {cresc.} } \stemUp <f bes>4. \pageBreak | % 137
    \stemUp <f bes>8 _\p \stemDown f'8 ^\markup{ \italic {pizz.} }
    \stemDown d8 \stemDown <bes d>4 r8 r8 \stemDown es8 \stemDown c8
    \stemUp <a c>4 r8 | % 138
    r8 \stemDown bes'8 _\markup{ \italic {cresc.} } \stemDown <bes, f'>8
    \stemDown <bes f'>4 \stemUp bes8 \stemUp c8 \stemUp c8 \stemUp bes8
    \stemDown c8 _\> \stemDown c8 \stemDown c8 | % 139
    \stemUp bes8 _\! _\p r8 r8 \stemUp bes4. ^\markup{ \italic {arco} }
    \stemUp a8 ( \stemUp bes8 \stemUp c8 \stemUp f,8 \stemUp c'8 \stemUp
    f8 ) ~ \pageBreak | \barNumberCheck #140
    \stemDown f8 \stemDown bes8 ( \stemDown d8 \stemDown f,8 \stemDown
    es8 \stemDown d8 \stemUp c,8 ) \stemUp c'8 -. \stemUp c8 -. \stemUp
    c8 ( \stemUp a8 ) \stemUp f8 -. | % 141
    \stemUp es8 \stemDown a'8 ^\markup{ \italic {pizz.} } \stemDown f8
    \stemDown a4 r8 r8 \stemUp bes,8 _\markup{ \italic {cresc.} }
    \stemUp f8 \stemDown f'4 r8 | % 142
    r8 \stemUp c8 \stemUp f,8 \stemDown f'4 r8 r8 \stemUp f8 \stemUp f,8
    \stemUp f8 \stemUp f'8 \stemUp <f, bes>8 \pageBreak | % 143
    \stemUp a8 \stemUp a8 \stemUp f8 \stemUp c'8 \stemUp f,8 \stemUp c'8
    r8 \stemUp bes8 \stemUp f8 \stemUp bes8 \stemUp f8 \stemUp bes8 | % 144
    r8 \stemUp c8 \stemUp f,8 \stemUp c'8 \stemUp f,8 \stemUp c'8 r8
    \stemUp c8 \stemUp f,8 \stemUp f8 _\> \stemUp d'8 \stemUp f8
    \pageBreak | % 145
    \stemUp <f, c'>4 _\! _\p r8 r4 r8 r8 \stemUp c'8 _\< \stemUp f,8
    \stemUp f8 _\! _\> \stemUp d'8 \stemUp bes8 | % 146
    \stemUp <f c'>4 _\! r8 r4 r8 r8 \stemDown es'8 _\< \stemDown c8
    \stemDown bes8 \stemDown d8 _\! _\> \stemDown bes'8 \pageBreak | % 147
    \stemDown a4 _\! _\markup{ \italic {cresc.} } r8 \stemDown <f a>4
    _\ff ^\markup{ \italic {arco} } r8 r8 r8 \stemDown c8 _\markup{
        \italic {dim.} } r8 r8 \stemDown c8 | % 148
    r8 r8 \stemDown c8 r8 r8 \stemDown c8 r8 r8 \stemDown c8 _\p r8 r8
    \stemUp a8 _\pp | % 149
    r8 r8 \stemUp bes8 _\markup{ \italic {cresc.} } r8 r8 \stemDown es8
    r8 r8 \stemUp f,8 r8 r8 \stemUp a8 | \barNumberCheck #150
    r8 r8 \stemUp bes8 r8 r8 \stemDown es8 r8 r8 \stemDown d8 r8 r8
    \stemDown <f es'>8 _\f \pageBreak | % 151
    r2. \once \omit TupletBracket
    \times 2/3  {
        \stemUp bes,16 ( _ "" _\markup{ \italic {sempre dim.} } \stemUp
        bes16 \stemUp bes16 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp bes16 ( \stemUp bes16 \stemUp bes16 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp bes16 ( \stemUp bes16 \stemUp bes16 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp bes16 ( \stemUp bes16 \stemUp bes16 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp bes16 ( \stemUp bes16 \stemUp bes16 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a16 ( \stemUp a16 \stemUp a16 ) }
    | % 152
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8. :32 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp bes8. :32 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp bes8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp bes8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp bes8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp a8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp bes8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp bes8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp bes8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp ges8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp ges8. :32 }
    \pageBreak | % 153
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp ges8. :32 }
    _\markup{ \italic {sempre} } _ "" \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp f8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp f8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp f8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp f8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp ges8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp ges8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp f8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp ges8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp ges8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp f8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp ges8. :32 }
    \pageBreak | % 154
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp f8. :32 }
    _\markup{ \italic {cresc.} } \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp f8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp f8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown d'8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown d8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown d8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown f8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown f8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown f8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown bes8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown bes8. :32 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown bes8. :32 }
    | % 155
    \stemDown <bes, f' d'>4 _\f r8 r4 r8 \stemDown <f' a>4 _\fp r8 r4 r8
    | % 156
    \stemUp a,4 _\p r8 \stemDown a'4 r8 \stemDown <f bes>4 r8 r4 r8 | % 157
    \stemDown a4 r8 \stemUp <f, c'>4 _\f r8 \stemUp <f d'>4 ^\markup{
        \italic {pizz.} } r8 r4 r8 \bar "|."
    }

PartPOneOneVoiceTwo =  \relative f {
    \clef "alto" \time 4/4 \key bes \major s1*9 \pageBreak s1*10
    \pageBreak s1*4 \break s1 \bar "||"
    \pageBreak | % 25
    \time 3/4  \key d \major s4*21 \pageBreak s2*9 \pageBreak s4*15 \bar
    "||"
    \pageBreak | % 43
    \time 4/4  \key bes \major s1*4 \break s8*7 s8 _\> | % 48
    f1 | % 49
    \stemDown f2. \stemDown g4 | \barNumberCheck #50
    \stemDown g2 \stemDown f2 \pageBreak | % 51
    \stemDown f2 ~ \stemDown f4 ~ \stemDown f8 s8*9 | % 53
    \stemDown f2. \stemDown f4 ~ | % 54
    f1 s8*5 \stemDown bes8 s4 \break s8*9 \stemDown f4. ~ \stemDown f2 | % 58
    \stemDown f2 \stemDown f4 s4*7 \stemDown bes8 \stemDown g8 \stemDown
    es8 s8 \pageBreak s1*4 \bar "||"
    \pageBreak | % 65
    \time 3/4  \key g \major s2*9 \pageBreak s4*21 \pageBreak s4*15 \bar
    "||"
    \time 4/4  \key es \major s1*2 \break s1*5 \pageBreak s1*5 \break
    s1*4 \bar "||"
    \pageBreak | % 99
    \time 12/8  \key bes \major s1*3 \pageBreak s2*9 \pageBreak s2*9
    \pageBreak s1*3 \pageBreak s1*3 \pageBreak s1*3 \pageBreak s1*3
    \pageBreak s4*5 \stemDown bes'8 \stemDown c8 | % 116
    \stemDown c4 s4 \stemDown c8 \stemDown d8 \stemDown c8 \stemDown c8
    \stemDown bes8 \stemDown bes8 s4*7 \pageBreak s1. \pageBreak s1*6
    \pageBreak s1*6 \pageBreak s1*3 \pageBreak s2*9 \pageBreak s2*15
    \pageBreak s2*9 \pageBreak s2*9 \pageBreak s1*3 \pageBreak s1*3
    \pageBreak s1*6 \pageBreak s1*3 \pageBreak s1. \pageBreak s1*6 \bar
    "|."
    }

PartPOneTwoVoiceOne =  \relative f, {
    \clef "bass" \time 4/4 \key bes \major | % 1
    r2 r4 \stemUp f4 ~ _\p _\< | % 2
    \stemUp f2 ( \stemUp ges4 _\! _\> \stemUp f4 ) | % 3
    \stemUp bes2 ( _\! _\p \stemDown es2 | % 4
    \stemDown d2 \stemUp a2 ) | % 5
    \stemUp bes4 ( \stemUp a4 \stemUp g2 ) | % 6
    \stemUp f4 \stemDown f'4 \stemDown f4 r4 | % 7
    r2 r4 \stemDown es4 ~ | % 8
    \stemDown es2 ( \stemDown d2 | % 9
    \stemUp a2 \stemUp bes4 \stemDown g'8 \stemDown f8 ) \pageBreak |
    \barNumberCheck #10
    \stemDown es4 ( \stemDown g4 \stemDown f4 \stemUp f,4 ) ~ | % 11
    \stemUp f2 \stemUp bes4 r4 | % 12
    r2 r4 \stemUp bes4 ( | % 13
    \stemDown es2 \stemDown d2 | % 14
    \stemUp c2. \stemUp bes4 ) | % 15
    r2 r8 \stemDown g'8 _\markup{ \italic {cresc.} } \stemDown es8
    \stemDown es8 | % 16
    \stemDown es8 _\> \stemDown es8 \stemDown es8 \stemDown es8
    \stemDown e8 _\! _\p \stemDown e8 \stemDown e8 \stemDown e8 | % 17
    \stemDown e8 _\> \stemDown f8 \stemDown f8 \stemDown f8 \stemUp f8
    _\! _\p \stemUp f,8 \stemUp f'8 \stemUp f8 | % 18
    \stemDown f4. ( \stemUp bes,8 \stemUp bes4 ) r4 | % 19
    r2 \stemUp bes8 r8 r4 \pageBreak | \barNumberCheck #20
    r2 \stemDown bes8 \stemDown g'8 \stemDown es8 _\markup{ \italic
        {cresc.} } r8 | % 21
    \stemDown es8 r8 \stemDown es8 r8 \stemDown e8 r8 \stemDown e8 r8 | % 22
    \stemDown e8 _\> \stemDown f8 \stemDown f8 r8 \stemDown f8 _\! _\p r8
    \stemDown f8 r8 | % 23
    \stemDown f8 _\markup{ \italic {più} } _ "" r8 \stemDown f8 r8
    \stemDown f8 r8 \stemDown fis8 r8 \break | % 24
    \stemDown fis8 _\pp r8 r4 r4 \stemUp a,4 ~ \bar "||"
    \pageBreak | % 25
    \time 3/4  \key d \major \stemUp a2. ~ _\markup{ \italic {cresc.} }
    | % 26
    \stemUp a2. ~ | % 27
    \stemUp a2. ~ | % 28
    \stemUp a2. ~ _\> | % 29
    \stemDown <a a'>2. ~ ~ _\! ^ "" ^\markup{ \italic {cresc.} } |
    \barNumberCheck #30
    \stemDown <a a'>2. ~ ~ | % 31
    \stemDown <a a'>2. ~ ~ _\> \pageBreak | % 32
    \stemDown <a a'>2 _\! ^\markup{ \italic {morendo} } \stemDown d8
    \stemDown <a a'>8 ~ ~ | % 33
    \stemDown <a a'>8 ^ "" ^\markup{ \italic {cresc.} } \stemDown <a
        a'>4 \stemDown <a a'>4 \stemDown <a a'>8 ~ ~ | % 34
    \stemDown <a a'>8 \stemDown <a a'>4 \stemDown <a a'>4 \stemDown <a
        a'>8 ~ ~ | % 35
    \stemDown <a a'>8 \stemDown <a a'>4 \stemDown <a a'>4 \stemDown <a
        a'>8 ~ ~ | % 36
    \stemDown <a a'>8 \stemDown <a a'>4 \stemDown <a a'>4 _\> \stemDown
    <a a'>8 ~ ~ | % 37
    \stemDown <a a'>8 _\! _\markup{ \italic {cresc.} } \stemDown <a a'>4
    \stemDown <a a'>4 \stemDown <a a'>8 ~ ~ \pageBreak | % 38
    \stemDown <a a'>8 \stemDown <a a'>4 \stemDown <a a'>4 \stemDown <a
        a'>8 ~ ~ | % 39
    \stemDown <a a'>8 \stemDown <a a'>4 \stemDown <a a'>4 _\> \stemDown
    <a a'>8 ~ ~ | \barNumberCheck #40
    \stemDown <a a'>8 _\! _\markup{ \italic {morendo} } \stemDown <a a'>4
    \stemDown <a a'>4 \stemDown <a a'>8 ~ ~ | % 41
    \stemDown <a a'>8 \stemDown <a a'>4 _\markup{ \italic {più} } _ ""
    \stemUp a8 ( \stemUp bes4 ) | % 42
    r4 _\pp \stemUp f4 ^\markup{ \italic {pizz.} } \stemDown f'8 r8
    ^\fermata \bar "||"
    \pageBreak | % 43
    \time 4/4  \key bes \major \stemUp bes,4 r8 \stemUp bes8 \stemDown
    es4 r8 \stemDown es8 | % 44
    \stemDown d4 r8 \stemDown d8 \stemUp a4 r8 \stemUp a8 | % 45
    \stemUp bes4 r8 \stemUp a8 \stemUp g4 r8 \stemUp g8 | % 46
    \stemUp f4 r8 \stemDown f'8 \stemDown f4 r4 \break | % 47
    r2 r4 r8 \stemDown es8 | % 48
    \stemDown es4 r8 \stemDown es8 \stemDown d4 r8 \stemDown d8 | % 49
    \stemUp a4 r8 \stemUp a8 \stemUp bes4 r8 \stemDown g'8 |
    \barNumberCheck #50
    \stemDown es4 r8 \stemDown g8 \stemDown f4 r8 \stemUp f,8 \pageBreak
    | % 51
    \stemUp f4 r8 \stemUp f8 \stemDown bes8 \stemDown d8 \stemDown f8 r8
    | % 52
    r2 r4 r8 \stemUp bes,8 | % 53
    \stemDown es4 r8 \stemDown es8 \stemDown d4 r8 \stemDown d8 | % 54
    \stemUp c4 _\< r8 \stemUp c8 \stemUp c8 _\! _\> r8 \stemUp bes8 r8 | % 55
    r2 _\! r8 \stemDown g'8 \stemDown es8 _\markup{ \italic {cresc.} }
    \stemDown es8 \break | % 56
    \stemDown es4 r8 \stemDown es'8 \stemDown e4 r8 \stemDown e,8 | % 57
    \stemDown e8 _\> \stemDown f8 r8 \stemDown f8 \stemDown f4 _\! _\p r8
    \stemUp f,8 | % 58
    \stemUp f4 \stemDown f'8 \stemDown bes,8 \stemUp c4 r4 | % 59
    r2 \stemUp bes8 ^\markup{ \italic {arco} } r8 r4 | \barNumberCheck
    #60
    r2 \stemDown bes8 \stemDown g'8 \stemDown es8 _\markup{ \italic
        {cresc.} } r8 \pageBreak | % 61
    \stemDown es8 r8 \stemDown es8 r8 \stemDown e8 r8 \stemDown e8 r8 | % 62
    \stemDown e8 \stemDown f8 \stemDown f8 r8 \stemDown f8 _\p r8
    \stemDown f8 r8 | % 63
    \stemDown f8 _\markup{ \italic {più} } _ "" r8 \stemDown f8 r8
    \stemDown f8 r8 \stemDown fis8 r8 | % 64
    \stemDown fis8 _\pp r8 r4 r4 \stemDown g4 ( _\pp \bar "||"
    \pageBreak | % 65
    \time 3/4  \key g \major \stemDown d4 \stemDown fis4 _\markup{
        \italic {cresc.} } \stemDown d4 ) ~ | % 66
    \stemDown d4 ( \stemDown g4 \stemDown d4 ) ~ | % 67
    \stemDown d4 ( \stemDown a'4 \stemDown d,4 ) ~ | % 68
    \stemDown d8 \stemDown d'8 r8 \stemDown b8 _\> \stemDown b8 (
    \stemDown g8 ) ~ | % 69
    \stemDown g4 ( _\! \stemDown fis4 _\markup{ \italic {cresc.} }
    \stemDown d4 ) ~ | \barNumberCheck #70
    \stemDown d4 ( \stemDown g4 \stemDown d4 ) ~ \pageBreak | % 71
    \stemDown d4 ( \stemDown d'4 _\> \stemDown d,4 ) ~ | % 72
    \stemDown d4 _\! _\markup{ \italic {morendo} } \stemDown d4 (
    \stemUp g,4 ) | % 73
    \stemUp d4 ( \stemUp d'4 _\markup{ \italic {cresc.} } \stemUp d,4 )
    ~ | % 74
    \stemUp d4 ( \stemUp g4 \stemUp d4 ) ~ | % 75
    \stemUp d4 ( \stemUp d'4 \stemUp d,4 ) ~ | % 76
    \stemUp d4 ( \stemUp g4 _\> \stemUp d4 ) ~ | % 77
    \stemUp d4 ( _\! \stemUp d'4 _\markup{ \italic {cresc.} } \stemUp d,4
    ) ~ \pageBreak | % 78
    \stemUp d4 ( \stemUp g4 \stemUp d4 ) ~ | % 79
    \stemUp d4 ( \stemUp d'4 _\> \stemUp d,4 ) ~ | \barNumberCheck #80
    \stemUp d4 _\! _\markup{ \italic {morendo} } \stemUp d4 ( \stemUp g8
    \stemUp d8 ) ~ | % 81
    \stemUp d4 _\markup{ \italic {più} } _ "" \stemUp d4 ( \stemUp es4
    ) ~ | % 82
    \stemUp es8 ( _\pp \stemUp es'8 \stemUp bes2 ) \bar "||"
    \time 4/4  \key es \major \stemDown es4 r4 r2 | % 84
    R1 \break | % 85
    R1 | % 86
    r2 r4 r8 \stemUp bes8 ^\markup{ \italic {pizz.} } | % 87
    \stemUp bes8 r8 r4 r2 | % 88
    r2 r4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp bes8 \stemUp bes8 }
    | % 89
    \stemUp es,4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp es8 \stemUp es8 }
    \stemUp bes'4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp bes8 \stemUp bes8 }
    \pageBreak | \barNumberCheck #90
    \stemUp bes4 r4 r2 | % 91
    r2 r4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown ges'8 \stemDown ges8 }
    | % 92
    \stemDown ces4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown ces8 \stemDown ces8 }
    \stemDown as8 \stemDown as8 \stemDown ges8 \stemDown fes8 | % 93
    \stemDown fes8 \stemDown ges8 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown ges8 \stemDown ges8 }
    \stemDown ges4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown ges8 \stemDown ges8 }
    | % 94
    \stemUp ces,4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp ces8 \stemUp ces8 }
    \stemUp ges4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown ges'8 \stemDown ges8 }
    \break | % 95
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown ges8 \stemDown bes8 \stemDown des8 }
    r4 r2 | % 96
    \stemUp ces,4 r4 r2 | % 97
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown ges'8 _\markup{ \italic {cresc.} } \stemDown bes8
        \stemDown des8 }
    r4 r2 | % 98
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown ges,8 _\markup{ \italic {cresc.} } \stemDown bes8
        \stemDown des8 }
    r4 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown f,8 \stemDown bes8 \stemDown d8 }
    \bar "||"
    \pageBreak | % 99
    \time 12/8  \key bes \major \stemUp f,,8 _\p \stemUp f'8 \stemUp f,8
    \stemDown f'4 r8 r8 \stemUp f8 \stemUp f,8 \stemDown f'4 r8 |
    \barNumberCheck #100
    r8 \stemUp f8 \stemUp f,8 \stemDown f'4 r8 r8 \stemUp f8 \stemUp f,8
    \stemDown a'4 r8 \pageBreak | % 101
    r8 \stemDown bes8 _\< \stemDown bes,8 \stemDown a'4 r8 r8 \stemUp g8
    _\! \stemUp g,8 \stemDown g'4 _\> r8 _\! | % 102
    r8 \stemUp f8 \stemUp f,8 \stemDown f'4 r8 r8 \stemUp f8 \stemUp f,8
    \stemDown f'4 r8 | % 103
    r8 \stemUp f8 \stemUp f,8 \stemDown f'4 r8 r8 \stemUp f8 \stemUp f,8
    \stemDown es'4 r8 \pageBreak | % 104
    r8 \stemDown es'8 \stemDown es,8 \stemDown es'4 r8 r8 \stemDown d8
    \stemDown d,8 \stemDown d'4 r8 | % 105
    r8 \stemDown a8 \stemDown a,8 \stemDown a'4 r8 r8 \stemDown bes8
    \stemDown bes,8 \stemDown g'4 r8 | % 106
    r8 \stemDown es'8 \stemDown es,8 \stemDown g4 r8 r8 \stemDown f'8
    \stemDown f,8 \stemDown f'4 r8 \pageBreak | % 107
    r8 \stemUp f,8 _\< \stemUp f,8 \stemDown f'4 r8 r8 _\! _\> \stemDown
    bes8 \stemDown f8 \stemDown f4 r8 _\! | % 108
    r8 \stemUp f8 \stemUp f,8 \stemDown f'4 r8 r8 \stemDown bes8
    \stemDown bes,8 \stemDown bes'4 r8 \pageBreak | % 109
    r8 \stemDown es8 \stemDown es,8 \stemDown es'4 r8 r8 \stemDown d8
    \stemDown d,8 \stemDown d'4 r8 | \barNumberCheck #110
    r8 \stemDown c8 _\markup{ \italic {cresc.} } \stemDown c,8 \stemDown
    c'4 r8 r8 \stemDown c8 _\> \stemDown c,8 \stemUp bes4 r8 _\!
    \pageBreak | % 111
    r8 \stemDown c'8 \stemDown c,8 \stemDown c'4 r8 r8 \stemDown f,8
    \stemDown g8 \stemDown es8 _\markup{ \italic {cresc.} } \stemDown
    es'8 \stemDown es8 | % 112
    r8 \stemDown es8 \stemDown es,8 \stemDown es'4 r8 r8 \stemDown e8
    \stemDown e,8 \stemDown e'4 r8 \pageBreak | % 113
    r8 \stemDown f8 _\> \stemDown f,8 \stemDown f'4 r8 r8 \stemUp f,8
    _\! _\p \stemUp f,8 \stemDown f'4 r8 | % 114
    r8 \stemUp f8 \stemUp f,8 \stemDown f'8 r8 \stemUp bes,8 \stemUp bes4
    r8 r4 r8 \pageBreak | % 115
    r2. r8 \stemDown bes'8 \stemDown bes,8 \stemDown bes'4 r8 | % 116
    r8 \stemUp f8 \stemUp f,8 \stemDown f'4 r8 r8 \stemDown f'8
    \stemDown bes,8 \stemDown es,4 r8 | % 117
    r8 \stemDown es'8 _\markup{ \italic {cresc.} } \stemDown es,8
    \stemDown es'4 r8 r8 \stemDown e8 \stemDown e,8 \stemDown e'4 r8
    \pageBreak | % 118
    r8 \stemDown f8 _\> \stemDown f,8 \stemDown f'4 r8 r8 \stemUp f,8
    _\! _\p \stemUp f,8 \stemDown f'4 r8 \pageBreak | % 119
    r8 \stemUp f8 _\markup{ \italic {più} } _ "" \stemUp f,8 \stemDown
    f'4 r8 r8 \stemUp f8 \stemUp f,8 \stemDown bes'4 r8 |
    \barNumberCheck #120
    r8 \stemUp f8 _\pp \stemUp f,8 \stemDown f'4 r8 r8 \stemUp f8
    _\markup{ \italic {cresc.} } \stemUp f,8 \stemDown f'8 r8 \stemUp
    bes,16 _\f ^\markup{ \italic {arco} } \stemUp bes16 | % 121
    \stemDown es4 -. r8 r8 r8 \stemDown es'16 \stemDown es16 \stemDown
    bes4 -. r8 r8 r8 \stemDown bes16 \stemDown bes16 | % 122
    \stemDown es,8 -. _\sf r8 \stemDown es16 \stemDown es16 \stemDown
    bes'8 -. _\sf r8 \stemDown bes,16 \stemDown bes16 \stemDown f'4 r8 r4
    r8 \pageBreak | % 123
    R1. | % 124
    r2. r4 r8 r8 \stemDown es'8 ^\markup{ \italic {pizz.} } \stemDown
    es,8 | % 125
    \stemDown f4 _\markup{ \italic {dolce} } r8 r8 \stemDown f'8
    \stemDown f,8 \stemDown f'4 r8 r8 \stemDown f8 \stemDown f,8 | % 126
    \stemDown f'4 r8 r8 \stemDown f8 \stemDown f,8 \stemDown f'4 r8 r8
    \stemUp f,8 \stemUp a,8 \pageBreak | % 127
    r4 r8 r8 r8 \stemUp bes8 _\markup{ \italic {cresc. poco a poco} }
    ^\markup{ \italic {arco} } r4 r8 r8 r8 \stemUp f8 | % 128
    r8 r8 \stemUp d8 r8 r8 \stemUp f8 r8 r8 \stemUp bes8 r8 r8 \stemUp c8
    \pageBreak | % 129
    r8 r8 \stemDown d'8 r8 \stemDown f8 \stemDown es8 r8 r8 \stemDown c8
    r8 \stemDown bes8 \stemDown a8 | \barNumberCheck #130
    r8 r8 \stemDown bes8 r8 \stemDown d8 \stemDown c8 r8 r8 \stemDown f,8
    r8 \stemDown f8 \stemUp bes,16 _\f \stemUp bes16 | % 131
    \stemDown es4 -. r8 r8 r8 \stemDown es16 \stemDown es16 \stemDown
    bes'4 -. r8 r8 r8 \stemDown bes16 \stemDown bes16 \pageBreak | % 132
    \stemDown es8 -. _\sf r8 \stemDown es,16 \stemDown es16 \stemDown
    bes'8 -. _\sf r8 \stemDown bes,16 \stemDown bes16 \stemDown f'4 r8 r4
    r8 | % 133
    \stemUp des,2. ~ _\> \stemUp des4. ( \stemUp f4. ) | % 134
    \stemUp as2. ~ _\! _\> \stemUp as4. \stemUp bes4. ~ _\! _\p | % 135
    \stemUp bes4. ( _\> \stemUp es,2. \stemUp ges4. ) | % 136
    \stemUp bes2. ~ _\! _\> \stemUp bes4. _\! _ "" _\markup{ \italic
        {cresc.} } \stemUp f4. ~ \pageBreak | % 137
    \stemUp f8 _\p \stemUp f'8 ^\markup{ \italic {pizz.} } \stemUp f,8
    \stemDown f'4 r8 r8 \stemUp f8 \stemUp f,8 \stemDown f'4 r8 | % 138
    \stemDown f4 _\markup{ \italic {cresc.} } r8 r8 \stemUp f8 \stemUp
    f,8 \stemDown f'8 \stemDown f8 \stemDown g8 \stemDown es8 _\>
    \stemDown es8 \stemDown f8 | % 139
    \stemUp bes,8 _\! _\p r8 r8 r8 \stemUp bes8 ^\markup{ \italic {arco}
        } \stemUp bes8 \stemUp bes4 r8 r8 \stemUp bes8 \stemUp bes8
    \pageBreak | \barNumberCheck #140
    \stemUp bes4 r8 r8 \stemUp bes8 \stemUp bes8 \stemDown a8 \stemDown
    c'8 -. \stemDown c8 -. \stemDown c8 ( \stemDown a8 ) \stemDown f8 -.
    | % 141
    \stemDown es4 r8 r8 \stemDown es'8 ^\markup{ \italic {pizz.} }
    \stemDown es,8 \stemDown d4 r8 r8 \stemDown d'8 _\markup{ \italic
        {cresc.} } \stemDown d,8 | % 142
    \stemUp a4 r8 r8 \stemDown a'8 \stemDown a,8 \stemUp bes4 r8 r8
    \stemDown bes'8 \stemDown bes,8 \pageBreak | % 143
    \stemDown es4 r8 r8 \stemDown es'8 \stemDown es,8 \stemDown d4 r8 r8
    \stemDown d'8 \stemDown d,8 | % 144
    \stemUp a4 r8 r8 \stemDown a'8 \stemDown a,8 \stemUp bes4 r8 r8
    \stemDown bes'8 _\> \stemDown bes,8 \pageBreak | % 145
    \stemDown a'4 _\! _\p r8 r4 r8 \stemDown f4 _\< r8 r8 _\! _\>
    \stemDown bes8 \stemDown bes,8 | % 146
    \stemDown a'4 _\! r8 r4 r8 \stemDown f4 _\< r8 r8 _\! _\> \stemDown
    bes8 \stemDown bes,8 \pageBreak | % 147
    \stemDown f'4 _\! _\markup{ \italic {cresc.} } r8 \stemDown f4 _\ff
    ^\markup{ \italic {arco} } r8 r8 r8 \stemDown f8 _\markup{ \italic
        {dim.} } r8 r8 \stemDown f8 | % 148
    r8 r8 \stemDown f8 r8 r8 \stemDown f8 r8 r8 \stemDown f8 _\p r8 r8
    \stemDown f8 _\pp | % 149
    r8 r8 \stemDown g8 _\markup{ \italic {cresc.} } r8 r8 \stemDown es8
    r8 r8 \stemDown f8 r8 r8 \stemDown f8 | \barNumberCheck #150
    r8 r8 \stemDown g8 r8 r8 \stemDown es8 r8 r8 \stemDown f8 r8 r8
    \stemDown f8 _\f \pageBreak | % 151
    r2. \stemUp bes,4 _\p r8 r8 \stemDown f'8 ^\markup{ \italic {pizz.}
        } \stemDown bes,8 | % 152
    \stemDown f'4 r8 r8 \stemDown f8 \stemDown bes,8 \stemDown f'4 r8 r8
    \stemDown f8 \stemDown bes,8 \pageBreak | % 153
    \stemDown f'4 _\pp r8 r8 \stemDown f8 \stemDown bes,8 \stemDown f'8
    r8 \stemUp bes,8 \stemDown f'8 r8 \stemUp bes,8 \pageBreak | % 154
    r8 r8 \stemDown bes'8 _\markup{ \italic {cresc.} } ^\markup{ \italic
        {arco} } r8 r8 \stemDown f8 r8 r8 \stemDown d8 r8 r8 \stemUp bes8
    | % 155
    \stemUp f4 _\f r8 r4 r8 \stemDown f'4 _\fp r8 r4 r8 | % 156
    \stemDown f4 _\p r8 \stemDown f4 r8 \stemDown bes4 r8 r4 r8 | % 157
    \stemDown f4 r8 \stemDown f4 _\f r8 \stemUp bes,4 ^\markup{ \italic
        {pizz.} } r8 r4 r8 \bar "|."
    }

PartPOneThreeVoiceOne =  \relative bes, {
    \clef "bass" \time 4/4 \key bes \major \transposition c | % 1
    R1*9 \pageBreak | \barNumberCheck #10
    R1*9 | % 19
    r2 \stemUp bes8 _\p r8 r4 \pageBreak | \barNumberCheck #20
    r2 \stemDown bes8 \stemDown g'8 \stemDown es8 _\markup{ \italic
        {cresc.} } r8 | % 21
    \stemDown es8 r8 \stemDown es8 r8 \stemDown e8 r8 \stemDown e8 r8 | % 22
    \stemDown e8 _\> \stemDown f8 \stemDown f8 r8 \stemDown f8 _\! _\p r8
    \stemDown f8 r8 | % 23
    \stemDown f8 _\markup{ \italic {più} } _ "" r8 \stemDown f8 r8
    \stemDown f8 r8 \stemDown fis8 r8 \break | % 24
    \stemDown fis8 _\pp r8 r4 \stemDown d2 ~ \bar "||"
    \pageBreak | % 25
    \time 3/4  \key d \major \stemDown d4 ( \stemUp cis4 _\markup{
        \italic {cresc.} } \stemUp a4 ) ~ | % 26
    \stemUp a4 ( \stemDown d4 \stemUp a4 ) ~ | % 27
    \stemUp a4 ( \stemDown e'4 \stemUp a,4 ) ~ | % 28
    \stemUp a4 ( \stemDown fis'4 _\> \stemUp a,4 ) ~ | % 29
    \stemUp a4 ( _\! ^ "" ^\markup{ \italic {cresc.} } \stemUp cis4
    \stemUp a4 ) ~ | \barNumberCheck #30
    \stemUp a4 ( \stemDown d4 \stemUp a4 ) ~ | % 31
    \stemUp a4 ( \stemDown e'4 _\> \stemUp a,4 ) ~ \pageBreak | % 32
    \stemUp a4 _\! ^\markup{ \italic {morendo} } \stemUp a4 ( \stemDown
    d4 ) | % 33
    r4 \stemUp cis4 ^ "" ^\markup{ \italic {cresc.} } ^\markup{ \italic
        {pizz.} } \stemUp a4 | % 34
    r4 \stemDown d4 \stemUp a4 | % 35
    r4 \stemDown e'4 \stemUp a,4 | % 36
    r4 \stemDown fis'4 _\> \stemUp a,4 | % 37
    r4 _\! \stemUp cis4 _\markup{ \italic {cresc.} } \stemUp a4
    \pageBreak | % 38
    r4 \stemDown d4 \stemUp a4 | % 39
    r4 \stemDown e'4 _\> \stemUp a,4 | \barNumberCheck #40
    r4 _\! _\markup{ \italic {morendo} } \stemUp a4 \stemDown fis'4 | % 41
    r4 \stemUp a,4 _\markup{ \italic {più} } _ "" \stemUp bes4 | % 42
    r4 _\pp \stemUp f4 ^\markup{ \italic {pizz.} } \stemDown f'8 r8
    ^\fermata \bar "||"
    \pageBreak | % 43
    \time 4/4  \key bes \major R1*4 \break | % 47
    R1*4 \pageBreak | % 51
    R1*5 \break | % 56
    R1*3 | % 59
    r2 \stemUp bes,8 _\p ^\markup{ \italic {arco} } r8 r4 |
    \barNumberCheck #60
    r2 \stemDown bes8 \stemDown g'8 \stemDown es8 _\markup{ \italic
        {cresc.} } r8 \pageBreak | % 61
    \stemDown es8 r8 \stemDown es8 r8 \stemDown e8 r8 \stemDown e8 r8 | % 62
    \stemDown e8 \stemDown f8 \stemDown f8 r8 \stemDown f8 _\p r8
    \stemDown f8 r8 | % 63
    \stemDown f8 _\markup{ \italic {più} } _ "" r8 \stemDown f8 r8
    \stemDown f8 r8 \stemDown fis8 r8 | % 64
    \stemDown fis8 _\pp r8 r4 r4 \stemDown g4 ( _\pp \bar "||"
    \pageBreak | % 65
    \time 3/4  \key g \major \stemDown d4 \stemDown fis4 _\markup{
        \italic {cresc.} } \stemDown d4 ) ~ | % 66
    \stemDown d4 ( \stemDown g4 \stemDown d4 ) ~ | % 67
    \stemDown d4 ( \stemDown a'4 \stemDown d,4 ) ~ | % 68
    \stemDown d8 \stemDown d'8 r8 \stemDown b8 _\> \stemDown b8 (
    \stemDown g8 ) ~ | % 69
    \stemDown g4 ( _\! \stemDown fis4 _\markup{ \italic {cresc.} }
    \stemDown d4 ) ~ | \barNumberCheck #70
    \stemDown d4 ( \stemDown g4 \stemDown d4 ) ~ \pageBreak | % 71
    \stemDown d4 ( \stemDown d'4 _\> \stemDown d,4 ) ~ | % 72
    \stemDown d4 _\! _\markup{ \italic {morendo} } \stemDown d4 (
    \stemDown g4 ) | % 73
    r4 \stemDown d4 _\markup{ \italic {cresc.} } ^\markup{ \italic
        {pizz.} } \stemUp d,4 | % 74
    r4 \stemUp g4 \stemUp d4 | % 75
    r4 \stemDown d'4 \stemUp d,4 | % 76
    r4 \stemUp g4 _\> \stemUp d4 | % 77
    r4 _\! \stemDown d'4 _\markup{ \italic {cresc.} } \stemUp d,4
    \pageBreak | % 78
    r4 \stemUp g4 \stemUp d4 | % 79
    r4 \stemDown d'4 _\> \stemUp d,4 | \barNumberCheck #80
    r4 _\! \stemUp d4 _\markup{ \italic {morendo} } \stemUp g4 | % 81
    r4 \stemDown d'4 _\markup{ \italic {più} } _ "" \stemDown es4 | % 82
    \stemDown es4 _\pp \stemUp bes4 r4 \bar "||"
    \time 4/4  \key es \major \stemDown es4 r4 r2 | % 84
    R1 \break | % 85
    R1*5 \pageBreak | \barNumberCheck #90
    R1*5 \break | % 95
    R1*3 | % 98
    r2 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 _\markup{ \italic {cresc.} } \stemDown bes'8
        \stemDown d8 }
    \bar "||"
    \pageBreak | % 99
    \time 12/8  \key bes \major \stemUp f,,8 _\p \stemUp f'8 \stemUp f,8
    \stemDown f'4 r8 r8 \stemUp f8 \stemUp f,8 \stemDown f'4 r8 |
    \barNumberCheck #100
    r8 \stemUp f8 \stemUp f,8 \stemDown f'4 r8 r8 \stemUp f8 \stemUp f,8
    \stemDown a'4 r8 \pageBreak | % 101
    r8 \stemDown bes8 _\< \stemDown bes,8 \stemDown a'4 r8 r8 \stemUp g8
    _\! \stemUp g,8 \stemDown g'4 _\> r8 _\! | % 102
    r8 \stemUp f8 \stemUp f,8 \stemDown f'4 r8 r8 \stemUp f8 \stemUp f,8
    \stemDown f'4 r8 | % 103
    r8 \stemUp f8 \stemUp f,8 \stemDown f'4 r8 r8 \stemUp f8 \stemUp f,8
    \stemDown es'4 r8 \pageBreak | % 104
    r8 \stemDown es'8 \stemDown es,8 \stemDown es'4 r8 r8 \stemDown d8
    \stemDown d,8 \stemDown d'4 r8 | % 105
    r8 \stemDown a8 \stemDown a,8 \stemDown a'4 r8 r8 \stemDown bes8
    \stemDown bes,8 \stemDown g'4 r8 | % 106
    r8 \stemDown es'8 \stemDown es,8 \stemDown g4 r8 r8 \stemDown f'8
    \stemDown f,8 \stemDown f'4 r8 \pageBreak | % 107
    r8 \stemUp f,8 _\< \stemUp f,8 \stemDown f'4 r8 r8 _\! _\> \stemDown
    bes8 \stemDown f8 \stemDown f4 r8 _\! | % 108
    r8 \stemUp f8 \stemUp f,8 \stemDown f'4 r8 r8 \stemDown bes8
    \stemDown bes,8 \stemDown bes'4 r8 \pageBreak | % 109
    r8 \stemDown es8 \stemDown es,8 \stemDown es'4 r8 r8 \stemDown d8
    \stemDown d,8 \stemDown d'4 r8 | \barNumberCheck #110
    r8 \stemDown c8 _\markup{ \italic {cresc.} } \stemDown c,8 \stemDown
    c'4 r8 r8 \stemDown c8 _\> \stemDown c,8 \stemUp bes4 r8 _\!
    \pageBreak | % 111
    r8 \stemDown c'8 \stemDown c,8 \stemDown c'4 r8 r8 \stemDown f,8
    \stemDown g8 \stemDown es8 _\markup{ \italic {cresc.} } \stemDown
    es'8 \stemDown es8 | % 112
    r8 \stemDown es8 \stemDown es,8 \stemDown es'4 r8 r8 \stemDown e8
    \stemDown e,8 \stemDown e'4 r8 \pageBreak | % 113
    r8 \stemDown f8 _\> \stemDown f,8 \stemDown f'4 r8 r8 \stemUp f,8
    _\! _\p \stemUp f,8 \stemDown f'4 r8 | % 114
    r8 \stemUp f8 \stemUp f,8 \stemDown f'8 r8 \stemUp bes,8 \stemUp bes4
    r8 r4 r8 \pageBreak | % 115
    r2. r8 \stemDown bes'8 \stemDown bes,8 \stemDown bes'4 r8 | % 116
    r8 \stemUp f8 \stemUp f,8 \stemDown f'4 r8 r8 \stemDown f'8
    \stemDown bes,8 \stemDown es,4 r8 | % 117
    r8 \stemDown es'8 _\markup{ \italic {cresc.} } \stemDown es,8
    \stemDown es'4 r8 r8 \stemDown e8 \stemDown e,8 \stemDown e'4 r8
    \pageBreak | % 118
    r8 \stemDown f8 _\> \stemDown f,8 \stemDown f'4 r8 r8 \stemUp f,8
    _\! _\p \stemUp f,8 \stemDown f'4 r8 \pageBreak | % 119
    r8 \stemUp f8 _\markup{ \italic {più} } _ "" \stemUp f,8 \stemDown
    f'4 r8 r8 \stemUp f8 \stemUp f,8 \stemDown bes'4 r8 |
    \barNumberCheck #120
    r8 \stemUp f8 _\pp \stemUp f,8 \stemDown f'4 r8 r8 \stemUp f8
    _\markup{ \italic {cresc.} } \stemUp f,8 \stemDown f'8 r8 \stemUp
    bes,16 _\f ^\markup{ \italic {arco} } \stemUp bes16 | % 121
    \stemDown es4 -. r8 r8 r8 \stemDown es'16 \stemDown es16 \stemDown
    bes4 -. r8 r8 r8 \stemDown bes16 \stemDown bes16 | % 122
    \stemDown es,8 -. _\sf r8 \stemDown es16 \stemDown es16 \stemDown
    bes'8 -. _\sf r8 \stemDown bes,16 \stemDown bes16 \stemDown f'4 r8 r4
    r8 \pageBreak | % 123
    R1. | % 124
    r2. r4 r8 r8 \stemDown es'8 ^\markup{ \italic {pizz.} } \stemDown
    es,8 | % 125
    \stemDown f4 _\markup{ \italic {dolce} } r8 r8 \stemDown f'8
    \stemDown f,8 \stemDown f'4 r8 r8 \stemDown f8 \stemDown f,8 | % 126
    \stemDown f'4 r8 r8 \stemDown f8 \stemDown f,8 \stemDown f'4 r8 r8
    \stemUp f,8 \stemUp a,8 \pageBreak | % 127
    r4 r8 r8 r8 \stemDown bes'8 _\markup{ \italic {cresc. poco a poco} }
    ^\markup{ \italic {arco} } r4 r8 r8 r8 \stemDown f8 | % 128
    r8 r8 \stemDown d8 r8 r8 \stemDown f8 r8 r8 \stemDown bes8 r8 r8
    \stemDown c8 \pageBreak | % 129
    r8 r8 \stemDown d8 r8 \stemDown f8 \stemDown es8 r8 r8 \stemDown c8
    r8 \stemDown bes8 \stemDown a8 | \barNumberCheck #130
    r8 r8 \stemDown bes8 r8 \stemDown d8 \stemDown c8 r8 r8 \stemDown f,8
    r8 \stemDown f8 \stemUp bes,16 _\f \stemUp bes16 | % 131
    \stemDown es4 -. r8 r8 r8 \stemDown es16 \stemDown es16 \stemDown
    bes'4 -. r8 r8 r8 \stemDown bes16 \stemDown bes16 \pageBreak | % 132
    \stemDown es8 -. _\sf r8 \stemDown es,16 \stemDown es16 \stemDown
    bes'8 -. _\sf r8 \stemDown bes,16 \stemDown bes16 \stemDown f'4 r8 r4
    r8 | % 133
    \stemUp des,2. ~ _\> \stemUp des4. ( \stemUp f4. ) | % 134
    \stemUp as2. ~ _\! _\> \stemUp as4. \stemUp bes4. ~ _\! _\p | % 135
    \stemUp bes4. ( _\> \stemUp es,2. \stemUp ges4. ) | % 136
    \stemUp bes2. ~ _\! _\> \stemUp bes4. _\! _ "" _\markup{ \italic
        {cresc.} } \stemUp f4. ~ \pageBreak | % 137
    \stemUp f8 _\p \stemUp f'8 ^\markup{ \italic {pizz.} } \stemUp f,8
    \stemDown f'4 r8 r8 \stemUp f8 \stemUp f,8 \stemDown f'4 r8 | % 138
    \stemDown f4 _\markup{ \italic {cresc.} } r8 r8 \stemUp f8 \stemUp
    f,8 \stemDown f'8 \stemDown f8 \stemDown g8 \stemDown es8 _\>
    \stemDown es8 \stemDown f8 | % 139
    \stemUp bes,8 _\! _\p r8 r8 r8 \stemUp bes8 ^\markup{ \italic {arco}
        } \stemUp bes8 \stemUp bes4 r8 r8 \stemUp bes8 \stemUp bes8
    \pageBreak | \barNumberCheck #140
    \stemUp bes4 r8 r8 \stemUp bes8 \stemUp bes8 \stemDown a8 \stemDown
    c'8 -. \stemDown c8 -. \stemDown c8 ( \stemDown a8 ) \stemDown f8 -.
    | % 141
    \stemDown es4 r8 r8 \stemDown es'8 ^\markup{ \italic {pizz.} }
    \stemDown es,8 \stemDown d4 r8 r8 \stemDown d'8 _\markup{ \italic
        {cresc.} } \stemDown d,8 | % 142
    \stemUp a4 r8 r8 \stemDown a'8 \stemDown a,8 \stemUp bes4 r8 r8
    \stemDown bes'8 \stemDown bes,8 \pageBreak | % 143
    \stemDown es4 r8 r8 \stemDown es'8 \stemDown es,8 \stemDown d4 r8 r8
    \stemDown d'8 \stemDown d,8 | % 144
    \stemUp a4 r8 r8 \stemDown a'8 \stemDown a,8 \stemUp bes4 r8 r8
    \stemDown bes'8 _\> \stemDown bes,8 \pageBreak | % 145
    \stemDown a'4 _\! _\p r8 r4 r8 \stemDown f4 _\< r8 r8 _\! _\>
    \stemDown bes8 \stemDown bes,8 | % 146
    \stemDown a'4 _\! r8 r4 r8 \stemDown f4 _\< r8 r8 _\! _\> \stemDown
    bes8 \stemDown bes,8 \pageBreak | % 147
    \stemDown f'4 _\! _\markup{ \italic {cresc.} } r8 \stemDown f4 _\ff
    ^\markup{ \italic {arco} } r8 r8 r8 \stemDown f8 _\markup{ \italic
        {dim.} } r8 r8 \stemDown f8 | % 148
    r8 r8 \stemDown f8 r8 r8 \stemDown f8 r8 r8 \stemDown f8 _\p r8 r8
    \stemDown f8 _\pp | % 149
    r8 r8 \stemDown g8 _\markup{ \italic {cresc.} } r8 r8 \stemDown es8
    r8 r8 \stemDown f8 r8 r8 \stemDown f8 | \barNumberCheck #150
    r8 r8 \stemDown g8 r8 r8 \stemDown es8 r8 r8 \stemDown f8 r8 r8
    \stemDown f8 _\f \pageBreak | % 151
    r2. \stemUp bes,4 _\p r8 r8 \stemDown f'8 ^\markup{ \italic {pizz.}
        } \stemDown bes,8 | % 152
    \stemDown f'4 r8 r8 \stemDown f8 \stemDown bes,8 \stemDown f'4 r8 r8
    \stemDown f8 \stemDown bes,8 \pageBreak | % 153
    \stemDown f'4 _\pp r8 r8 \stemDown f8 \stemDown bes,8 \stemDown f'8
    r8 \stemUp bes,8 \stemDown f'8 r8 \stemUp bes,8 \pageBreak | % 154
    r8 r8 \stemDown bes'8 _\markup{ \italic {cresc.} } ^\markup{ \italic
        {arco} } r8 r8 \stemDown f8 r8 r8 \stemDown d8 r8 r8 \stemUp bes8
    | % 155
    \stemUp f4 _\f r8 r4 r8 \stemDown f'4 _\fp r8 r4 r8 | % 156
    \stemDown f4 _\p r8 \stemDown f4 r8 \stemDown bes4 r8 r4 r8 | % 157
    \stemDown f4 r8 \stemDown f4 _\f r8 \stemUp bes,4 ^\markup{ \italic
        {pizz.} } r8 r4 r8 \bar "|."
    }


% The score definition
\score {
    <<
        
        \new StaffGroup
        <<
            \new Staff
            <<
                \set Staff.instrumentName = "Flauti"
                \set Staff.shortInstrumentName = "Fl."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneVoiceOne" {  \voiceOne \PartPOneVoiceOne }
                    \context Voice = "PartPOneVoiceTwo" {  \voiceTwo \PartPOneVoiceTwo }
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
                \set Staff.instrumentName = "Clarinetti in B"
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
            \new Staff
            <<
                \set Staff.instrumentName = "Corni in B I II"
                \set Staff.shortInstrumentName = \markup { \center-column { \line {"Cor. B"} \line {"I II"} } }
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPFiveVoiceOne" {  \voiceOne \PartPFiveVoiceOne }
                    \context Voice = "PartPFiveVoiceTwo" {  \voiceTwo \PartPFiveVoiceTwo }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Corni in Es III IV"
                \set Staff.shortInstrumentName = \markup { \center-column { \line {"Cor. Es"} \line {"III IV"} } }
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPSixVoiceOne" {  \voiceOne \PartPSixVoiceOne }
                    \context Voice = "PartPSixVoiceTwo" {  \voiceTwo \PartPSixVoiceTwo }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Trombe in B"
                \set Staff.shortInstrumentName = "Tr."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPSevenVoiceOne" {  \PartPSevenVoiceOne }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Timpani in F–B"
                \set Staff.shortInstrumentName = "Timp."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPEightVoiceOne" {  \PartPEightVoiceOne }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Violino I"
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPNineVoiceOne" {  \voiceOne \PartPNineVoiceOne }
                    \context Voice = "PartPNineVoiceTwo" {  \voiceTwo \PartPNineVoiceTwo }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Violino II"
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneZeroVoiceOne" {  \PartPOneZeroVoiceOne }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Viola"
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneOneVoiceOne" {  \voiceOne \PartPOneOneVoiceOne }
                    \context Voice = "PartPOneOneVoiceTwo" {  \voiceTwo \PartPOneOneVoiceTwo }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Violoncello"
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneTwoVoiceOne" {  \PartPOneTwoVoiceOne }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Basso"
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneThreeVoiceOne" {  \PartPOneThreeVoiceOne }
                    >>
                >>
            
            >>
        
        >>
    \layout {}
    % To create MIDI output, uncomment the following line:
    %  \midi {\tempo 4 = 48 }
    }

