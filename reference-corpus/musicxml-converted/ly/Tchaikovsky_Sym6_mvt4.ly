\version "2.24.3"
% automatically converted by musicxml2ly from ../xml/Tchaikovsky_Sym6_mvt4.musicxml
\pointAndClickOff

%% additional definitions required by the score:
 gestopft = #(make-dynamic-script " gestopft")
 marcato e pesante = #(make-dynamic-script " marcato e pesante")
sempre  = #(make-dynamic-script "sempre ")

\header {
    title =  "Symphony 6"
    composer =  "Peter Tchaikovsky"
    encodingsoftware =  "MuseScore 4.1.0"
    encodingdate =  "2023-07-21"
    source =  "http://musescore.com/user/32958498/scores/7001379"
    }

#(set-global-staff-size 10.285714285714286)
\paper {
    
    paper-width = 21.59\cm
    paper-height = 27.94\cm
    top-margin = 1.0\cm
    bottom-margin = 1.4\cm
    left-margin = 1.0\cm
    right-margin = 1.0\cm
    indent = 1.6607692307692306\cm
    short-indent = 1.245576923076923\cm
    }
\layout {
    \context { \Score
        skipBars = ##t
        }
    }
PartPOneVoiceOne =  \relative fis' {
    \clef "treble" \time 3/4 \key d \major | % 1
    \tempo "Adagio lamentoso" 4=54 R2. _ "Flutes" | % 2
    r4 \stemUp fis2 ~ _\mf _\> | % 3
    \stemUp fis4 ~ \stemUp fis8 _\! _\p r8 r4 | % 4
    r4 \stemUp fis2 ~ _\mf _\> | % 5
    \stemUp fis4 _\! _\p \stemUp e2 ( ~ | % 6
    \stemUp e4 ^\markup{ \bold {affrettando} } \stemUp d4 ) \stemUp a'4
    ~ _\mp | % 7
    \stemUp a4 \stemUp gis2 ( ~ \pageBreak | % 8
    \stemUp gis4 _ "Fl." \stemUp fis4 ) \stemDown cis'4 ~ _\mf | % 9
    \stemDown cis4 \stemDown b4. ( _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemUp a8 ) | \barNumberCheck #10
    \stemDown e'4 -- \stemDown dis4. ( \stemDown cis8 ) | % 11
    \stemDown gis'4 -- \stemDown fis4. ( \stemDown eis8 ) | % 12
    \stemDown cis'4 ( -> \stopTrillSpan _\ff ^\markup{ \bold
        {rallentando} } \stemDown b8. ) _\> \stemDown a16 -- \stemDown
    gis8 -- \stemDown a8 -- | % 13
    \stemDown gis8 ( -> _\! _\f _\markup{ \small\italic {dim. poco a
            poco} } \startTrillSpan \stemDown fis8 ) \stemDown eis8. --
    \stemDown fis16 -- \stemDown e8 -- \stemDown d8 -- | % 14
    \stemDown cis8 ( -> \stemDown d8 ) \stemDown cis8 -- \stemDown b8 --
    \stemDown a8 ( \stemDown b8 ) | % 15
    \stemUp a8 ( \stemUp g8 ) \stemUp fis8 ( \stemUp g8 ) \stemUp fis8 (
    \stopTrillSpan _\mp _\> \stemUp e8 \break | % 16
    \tempo "Andante" 4=69 \stemUp d8 _ "Fl." \stemUp e8 ) \stemUp d8 (
    _\! _\p \stemUp cis8 \grace { \stemUp d16 \stemUp cis16 } \stemUp
    bis8 \stemUp cis8 ) | % 17
    \stemUp d8. ( _\pp _\< \stemUp cis16 ) \stemUp e4.. _\! _\mp _\>
    \stemUp d16 | % 18
    \stemUp cis2 ~ _\! _\pp _\> \stemUp cis8 r8 _\! | % 19
    R2. | \barNumberCheck #20
    \tempo "Adagio poco meno che prima" 4=60 R2.*3 | % 23
    \tempo 4=40 R2. \pageBreak | % 24
    R2.*9 \break | % 33
    R2.*4 | % 37
    \tempo "Andante" 4=76 R2.*4 \pageBreak | % 41
    R2.*2 | % 43
    R2.*3 ^\markup{ \bold {poco animando} } | % 46
    R2. \break ^\markup{ \bold {ritenuto} } | % 47
    R2.*6 \pageBreak ^\markup{ \bold {Tempo I} } | % 53
    R2. _ "Fl." | % 54
    r2 ^\markup{ \bold {ritenuto} } \stemDown a''4 -- _\mf | % 55
    \stemDown g2 ( ^\markup{ \bold {Tempo I} } \stemDown cis,4 ) | % 56
    \stemDown d2 ( \stemDown a'4 ) | % 57
    \stemDown g2 ( \stemDown cis,4 ) | % 58
    \stemDown d2 \stemDown c'4 -- _\markup{ \small\italic {cresc.} }
    \startTrillSpan \pageBreak | % 59
    \stemDown b2 ^\markup{ \bold {poco animando} } _ "Fl." \stemDown e4
    -- | \barNumberCheck #60
    \stemDown e4 ( \stemDown fis4 ) \stemDown b,4 -- | % 61
    \stemDown b2. | % 62
    \stemDown b4 ( ^\markup{ \bold {ritenuto} } \stemDown bes4 ~ \once
    \omit TupletBracket
    \times 2/3  {
        \stemDown bes8 \stemDown a8 ) \stemDown a8 ~ }
    \stopTrillSpan _\f | % 63
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 ^\markup{ \bold {Tempo I} } \stemDown a8 \stemDown
        a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown gis8 \stemDown gis8 }
    | % 64
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \pageBreak | % 65
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 _ "Fl." \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown gis8 \stemDown gis8 }
    | % 66
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 }
    | % 67
    \once \omit TupletBracket
    \times 2/3  {
        r8 ^\markup{ \bold {animando} } \stemDown b8 _\markup{
            \small\italic {cresc.} } \startTrillSpan \stemDown b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 \stemDown b8 \stemDown b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 \stemDown b8 \stemDown b8 }
    | % 68
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown cis8 \stemDown cis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 \stemDown cis8 \stemDown cis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 \stemDown cis8 \stemDown cis8 }
    | % 69
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown d8 \stopTrillSpan _\ff _\< \stemDown d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 }
    | \barNumberCheck #70
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 }
    \pageBreak | % 71
    \tempo "" 1=96 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 _\! _\fff ^\markup{ \bold {Più mosso (} }
        ^\markup{ \bold {)} } _ "Fl." \stemDown fis8 \stemDown fis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown fis8 \stemDown fis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown fis8 \stemDown fis8 ~ }
    | % 72
    \stemDown fis8 r8 r4 r4 | % 73
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 ~ }
    | % 74
    \stemDown e8 r8 r4 r4 | % 75
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    | % 76
    \stemDown c8 r8 r4 r4 \pageBreak | % 77
    \stemDown c16 _\sempre _\fff ^\markup{ \bold {stringendo} } _ "Fl."
    r16 r8 r4 r4 | % 78
    R2. | % 79
    R2.*2 ^\markup{ \bold {Vivace} } | % 81
    r8 \stemDown e,8 _\fff r4 r4 ^\fermata \pageBreak | % 82
    \tempo "Andante" 4=76 R2.*8 \break | \barNumberCheck #90
    \tempo "Andante non tanto" 4=60 R2.*9 \pageBreak | % 99
    R2.*8 \break | % 107
    R2. _ "Fl." | % 108
    \stemDown b2. _\mf | % 109
    \stemDown d2 ( ^\markup{ \bold {stringendo molto} } \stemUp fis,4 )
    | \barNumberCheck #110
    \stemDown e'2 _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown d4 | % 111
    \stemDown g2 \stemDown b,4 | % 112
    \stemDown b'4 \stopTrillSpan _\ff \stemDown ais8 ( \stemDown b8 )
    \stemDown c4 | % 113
    \stemDown b8 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown c8 ) \stemDown d4 \stemDown cis8 ( \stemDown d8 )
    \pageBreak | % 114
    \stemDown cis4 _ "Fl." -\markup{ \italic {pesante} } \stemDown cis4
    \stemDown cis4 | % 115
    \stemDown d4 \stemDown d4 \stopTrillSpan _\fff \stemDown d4 | % 116
    \tempo "Moderato assai" 4=88 \stemDown e2. | % 117
    \stemDown e4 \stemDown d4 \stemDown a4 \pageBreak | % 118
    \stemDown d2. _ "Fl." | % 119
    \stemDown cis2 \stemDown e,4 | \barNumberCheck #120
    \stemDown b'2. \pageBreak | % 121
    \stemDown ais4 _ "Fl." \stemDown ais4 ^\markup{ \bold {incalzando} }
    \stemDown cis,4 | % 122
    \stemDown fis2. | % 123
    \stemDown cis4 \stemDown d4 \stemDown dis4 \pageBreak | % 124
    \stemDown e4 _ "Fl." \stemDown fis4 \stemDown g8 ( \stemDown fis8 )
    | % 125
    \stemDown e8 ( ^\markup{ \bold {ritenuto} } \stemDown d8 \stemDown
    cis8 \stemDown d8 \stemDown cis8 \stemDown b8 ) | % 126
    \tempo "Andante" 4=80 \stemUp fis8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis16 ( _\fff \stemDown gis16 \stemDown ais16 }
    \stemDown b32 \stemDown cis32 \stemDown d32 \stemDown e32 ) | % 127
    \stemDown fis4 -> \stemDown e8 -- \stemDown d8 -- \stemDown cis8 --
    \stemDown b8 -- | % 128
    \stemDown d8 ( -> \stemDown cis8 ) r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis,16 ( \stemDown gis16 \stemDown ais16 }
    \stemDown b32 \stemDown cis32 \stemDown d32 \stemDown e32 )
    \pageBreak | % 129
    \stemDown fis4 -> _ "Fl." \stemDown e8 -- \stemDown d8 -- \stemDown
    cis8 -- \stemDown b8 -- | \barNumberCheck #130
    \stemDown d8 ( -> \stemDown cis8 ) r4 r4 | % 131
    R2.*4 \pageBreak | % 135
    R2.*5 | \barNumberCheck #140
    R2.*5 ^\markup{ \bold {poco rallentando} } | % 145
    R2.*2 \pageBreak ^\markup{ \bold {quasi adagio} } | % 147
    \tempo "Andante giusto" 4=76 r4 _ "Fl." r4 \stemUp d,4 _\f _\< | % 148
    \stemUp e2 _\! _\sf _\> \stemUp e4 _\! _\f | % 149
    \stemUp fis2 \stemUp d4 _\< | \barNumberCheck #150
    \stemUp e2 _\! _\sf _\> \stemUp e4 _\! _\f | % 151
    \stemUp fis4 ~ \stemUp fis8 r8 r4 | % 152
    R2. \pageBreak | % 153
    R2.*6 \break | % 159
    R2.*6 \break | % 165
    R2.*7 \bar "|."
    }

PartPTwoVoiceOne =  \relative fis' {
    \clef "treble" \time 3/4 \key d \major | % 1
    R2. | % 2
    r4 \stemUp fis2 ~ _\mf _\> | % 3
    \stemUp fis4 ~ \stemUp fis8 _\! _\p r8 r4 | % 4
    r4 \stemUp fis2 ~ _\mf _\> | % 5
    \stemUp fis4 _\! _\p \stemUp e2 ( ~ | % 6
    \stemUp e4 \stemUp d4 ) \stemUp a'4 ~ _\mp | % 7
    \stemUp a4 \stemUp gis2 ( ~ \pageBreak | % 8
    \stemUp gis4 \stemUp fis4 ) \stemDown cis'4 ~ _\mf | % 9
    \stemDown cis4 \stemDown b4. ( _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemUp a8 ) | \barNumberCheck #10
    \stemDown e'4 -- \stemDown dis4. ( \stemDown cis8 ) | % 11
    \stemDown gis'4 -- \stemDown fis4. ( \stemDown eis8 ) | % 12
    \stemDown cis'4 ( -> \stopTrillSpan _\ff \stemDown b8. ) _\>
    \stemDown a16 -- \stemDown gis8 -- \stemDown a8 -- | % 13
    \stemDown gis8 ( -> _\! _\f _\markup{ \small\italic {dim. poco a
            poco} } \startTrillSpan \stemDown fis8 ) \stemDown eis8. --
    \stemDown fis16 -- \stemDown e8 -- \stemDown d8 -- | % 14
    \stemDown cis8 ( -> \stemDown d8 ) \stemDown cis8 -- \stemDown b8 --
    \stemDown a8 ( \stemDown b8 ) | % 15
    \stemUp a8 ( \stemUp g8 ) \stemUp fis8 ( \stemUp g8 ) \stemUp fis8 (
    \stopTrillSpan _\mp _\> \stemUp e8 \break | % 16
    \stemUp d8 \stemUp e8 ) \stemUp d8 ( _\! _\p \stemUp cis8 \grace {
        \stemUp d16 \stemUp cis16 } \stemUp bis8 \stemUp cis8 ) | % 17
    \stemUp d8. ( _\pp _\< \stemUp cis16 ) \stemUp e4.. _\! _\mp _\>
    \stemUp d16 | % 18
    \stemUp cis2 ~ _\! _\pp _\> \stemUp cis8 r8 _\! | % 19
    R2.*5 \pageBreak | % 24
    R2.*9 \break | % 33
    R2.*8 \pageBreak | % 41
    R2.*6 \break | % 47
    R2.*6 \pageBreak | % 53
    R2. | % 54
    r2 \stemDown a''4 -- _\mf | % 55
    \stemDown g2 ( \stemDown cis,4 ) | % 56
    \stemDown d2 ( \stemDown a'4 ) | % 57
    \stemDown g2 ( \stemDown cis,4 ) | % 58
    \stemDown d2 \stemDown c'4 -- _\markup{ \small\italic {cresc.} }
    \startTrillSpan \pageBreak | % 59
    \stemDown b2 \stemDown e4 -- | \barNumberCheck #60
    \stemDown e4 ( \stemDown fis4 ) \stemDown b,4 -- | % 61
    \stemDown b2. | % 62
    \stemDown b4 ( \stemDown bes4 ~ \once \omit TupletBracket
    \times 2/3  {
        \stemDown bes8 \stemDown a8 ) \stemDown a8 ~ }
    \stopTrillSpan _\f | % 63
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown gis8 \stemDown gis8 }
    | % 64
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \pageBreak | % 65
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown gis8 \stemDown gis8 }
    | % 66
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 }
    | % 67
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown b8 _\markup{ \small\italic {cresc.} }
        \startTrillSpan \stemDown b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 \stemDown b8 \stemDown b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 \stemDown b8 \stemDown b8 }
    | % 68
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown cis8 \stemDown cis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 \stemDown cis8 \stemDown cis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 \stemDown cis8 \stemDown cis8 }
    | % 69
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown d8 \stopTrillSpan _\ff _\< \stemDown d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 }
    | \barNumberCheck #70
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 }
    \pageBreak | % 71
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 _\! _\fff \stemDown fis8 \stemDown fis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown fis8 \stemDown fis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown fis8 \stemDown fis8 ~ }
    | % 72
    \stemDown fis8 r8 r4 r4 | % 73
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 ~ }
    | % 74
    \stemDown e8 r8 r4 r4 | % 75
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    | % 76
    \stemDown c8 r8 r4 r4 \pageBreak | % 77
    \stemDown c16 _\sempre _\fff r16 r8 r4 r4 | % 78
    R2.*3 | % 81
    r8 \stemDown e,8 _\fff r4 r4 ^\fermata \pageBreak | % 82
    R2.*8 \break | \barNumberCheck #90
    R2.*9 \pageBreak | % 99
    R2.*8 \break | % 107
    R2.*2 | % 109
    \stemUp d,2 ( _\mf \stemUp fis4 ) | \barNumberCheck #110
    \stemDown e'2 _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown d4 | % 111
    \stemDown g2 \stemDown b,4 | % 112
    \stemDown b'4 \stopTrillSpan _\ff \stemDown ais8 ( \stemDown b8 )
    \stemDown c4 | % 113
    \stemDown b8 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown c8 ) \stemDown d4 \stemDown cis8 ( \stemDown d8 )
    \pageBreak | % 114
    \stemDown cis4 -\markup{ \italic {pesante} } \stemDown cis4
    \stemDown cis4 | % 115
    \stemDown d4 \stemDown d4 \stopTrillSpan _\fff \stemDown d4 | % 116
    \stemDown e2. | % 117
    \stemDown e4 \stemDown d4 \stemDown a4 \pageBreak | % 118
    \stemDown d2. | % 119
    \stemDown cis2 \stemDown e,4 | \barNumberCheck #120
    \stemDown b'2. \pageBreak | % 121
    \stemDown ais4 \stemDown ais4 \stemDown cis,4 | % 122
    \stemDown fis2. | % 123
    \stemDown cis4 \stemDown d4 \stemDown dis4 \pageBreak | % 124
    \stemDown e4 \stemDown fis4 \stemDown g8 ( \stemDown fis8 ) | % 125
    \stemDown e8 ( \stemDown d8 \stemDown cis8 \stemDown d8 \stemDown
    cis8 \stemDown b8 ) | % 126
    \stemUp fis8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis16 ( _\fff \stemDown gis16 \stemDown ais16 }
    \stemDown b32 \stemDown cis32 \stemDown d32 \stemDown e32 ) | % 127
    \stemDown fis4 -> \stemDown e8 -- \stemDown d8 -- \stemDown cis8 --
    \stemDown b8 -- | % 128
    \stemDown d8 ( -> \stemDown cis8 ) r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis,16 ( \stemDown gis16 \stemDown ais16 }
    \stemDown b32 \stemDown cis32 \stemDown d32 \stemDown e32 )
    \pageBreak | % 129
    \stemDown fis4 -> \stemDown e8 -- \stemDown d8 -- \stemDown cis8 --
    \stemDown b8 -- | \barNumberCheck #130
    \stemDown d8 ( -> \stemDown cis8 ) r4 r4 | % 131
    R2.*4 \pageBreak | % 135
    R2.*12 \pageBreak | % 147
    r4 r4 \stemUp b,4 _\f _\< | % 148
    \stemUp c2 _\! _\sf _\> \stemUp cis4 _\! _\f | % 149
    \stemUp d2 \stemUp b4 _\< | \barNumberCheck #150
    \stemUp c2 _\! _\sf _\> \stemUp cis4 _\! _\f | % 151
    \stemUp d2. | % 152
    R2. \pageBreak | % 153
    R2.*6 \break | % 159
    R2.*6 \break | % 165
    R2.*7 \bar "|."
    }

PartPThreeVoiceOne =  \relative fis' {
    \clef "treble" \time 3/4 \key d \major | % 1
    R2. | % 2
    r4 \stemUp fis2 ~ _\mf _\> | % 3
    \stemUp fis4 ~ \stemUp fis8 _\! _\p r8 r4 | % 4
    r4 \stemUp fis2 ~ _\mf _\> | % 5
    \stemUp fis4 _\! _\p \stemUp e2 ( ~ | % 6
    \stemUp e4 \stemUp d4 ) \stemUp a'4 ~ _\mp | % 7
    \stemUp a4 \stemUp gis2 ( ~ \pageBreak | % 8
    \stemUp gis4 \stemUp fis4 ) \stemDown cis'4 ~ _\mf | % 9
    \stemDown cis4 \stemDown b4. ( _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemUp a8 ) | \barNumberCheck #10
    \stemDown e'4 -- \stemDown dis4. ( \stemDown cis8 ) | % 11
    \stemDown gis'4 -- \stemDown fis4. ( \stemDown eis8 ) | % 12
    \stemDown cis'4 ( -> \stopTrillSpan _\ff \stemDown b8. ) _\>
    \stemDown a16 -- \stemDown gis8 -- \stemDown a8 -- | % 13
    \stemDown gis8 ( -> _\! _\f _\markup{ \small\italic {dim. poco a
            poco} } \startTrillSpan \stemDown fis8 ) \stemDown eis8. --
    \stemDown fis16 -- \stemDown e8 -- \stemDown d8 -- | % 14
    \stemDown cis8 ( -> \stemDown d8 ) \stemDown cis8 -- \stemDown b8 --
    \stemDown a8 ( \stemDown b8 ) | % 15
    \stemUp a8 ( \stemUp g8 ) \stemUp fis8 ( \stemUp g8 ) \stemUp fis8 (
    \stopTrillSpan _\mp _\> \stemUp e8 \break | % 16
    \stemUp d8 \stemUp e8 ) \stemUp d8 ( _\! _\p \stemUp cis8 \grace {
        \stemUp d16 \stemUp cis16 } \stemUp bis8 \stemUp cis8 ) | % 17
    \stemUp d8. ( _\pp _\< \stemUp cis16 ) \stemUp e4.. _\! _\mp _\>
    \stemUp d16 | % 18
    \stemUp cis2 ~ _\! _\pp _\> \stemUp cis8 r8 _\! | % 19
    R2.*5 \pageBreak | % 24
    R2.*9 \break | % 33
    R2.*8 \pageBreak | % 41
    R2.*6 \break | % 47
    R2.*6 \pageBreak | % 53
    R2. | % 54
    r2 \stemDown a''4 -- _\mf | % 55
    \stemDown g2 ( \stemDown cis,4 ) | % 56
    \stemDown d2 ( \stemDown a'4 ) | % 57
    \stemDown g2 ( \stemDown cis,4 ) | % 58
    \stemDown d2 \stemDown c'4 -- _\markup{ \small\italic {cresc.} }
    \startTrillSpan \pageBreak | % 59
    \stemDown b2 \stemDown e4 -- | \barNumberCheck #60
    \stemDown e4 ( \stemDown fis4 ) \stemDown b,4 -- | % 61
    \stemDown b2. | % 62
    \stemDown b4 ( \stemDown bes4 ~ \once \omit TupletBracket
    \times 2/3  {
        \stemDown bes8 \stemDown a8 ) \stemDown a8 ~ }
    \stopTrillSpan _\f | % 63
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown gis8 \stemDown gis8 }
    | % 64
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \pageBreak | % 65
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown gis8 \stemDown gis8 }
    | % 66
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 }
    | % 67
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown b8 _\markup{ \small\italic {cresc.} }
        \startTrillSpan \stemDown b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 \stemDown b8 \stemDown b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 \stemDown b8 \stemDown b8 }
    | % 68
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown cis8 \stemDown cis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 \stemDown cis8 \stemDown cis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 \stemDown cis8 \stemDown cis8 }
    | % 69
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown d8 \stopTrillSpan _\ff _\< \stemDown d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 }
    | \barNumberCheck #70
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 }
    \pageBreak | % 71
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 _\! _\fff \stemDown fis8 \stemDown fis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown fis8 \stemDown fis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown fis8 \stemDown fis8 ~ }
    | % 72
    \stemDown fis8 r8 r4 r4 | % 73
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 ~ }
    | % 74
    \stemDown e8 r8 r4 r4 | % 75
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g,8 \stemDown g8 \stemDown g8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 \stemDown g8 \stemDown g8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 \stemDown g8 \stemDown g8 ~ }
    | % 76
    \stemDown g8 r8 r4 r4 \pageBreak | % 77
    \stemDown c16 _\sempre _\fff r16 r8 r4 r4 | % 78
    R2.*3 | % 81
    r8 \stemDown c,8 _\fff r4 r4 ^\fermata \pageBreak | % 82
    R2.*8 \break | \barNumberCheck #90
    R2.*9 \pageBreak | % 99
    R2.*8 \break | % 107
    R2.*3 | \barNumberCheck #110
    \stemDown e2 _\mf _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown d4 | % 111
    \stemUp g,2 \stemDown b4 | % 112
    \stemDown b'4 \stopTrillSpan _\ff \stemDown ais8 ( \stemDown b8 )
    \stemDown c4 | % 113
    \stemDown b8 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown c8 ) \stemDown d4 \stemDown cis8 ( \stemDown d8 )
    \pageBreak | % 114
    \stemDown cis4 -\markup{ \italic {pesante} } \stemDown cis4
    \stemDown cis4 | % 115
    \stemDown d4 \stemDown d4 \stopTrillSpan _\fff \stemDown d4 | % 116
    \stemDown e2. | % 117
    \stemDown e4 \stemDown d4 \stemDown g,4 \pageBreak | % 118
    \stemDown d'2. | % 119
    \stemDown cis2 \stemDown e,4 | \barNumberCheck #120
    \stemDown b'2. \pageBreak | % 121
    \stemDown g4 \stemDown fis4 \stemDown e4 | % 122
    \stemDown d2. | % 123
    \stemDown cis4 \stemDown d4 \stemDown dis4 \pageBreak | % 124
    \stemDown e4 \stemDown fis4 \stemDown g8 ( \stemDown fis8 ) | % 125
    \stemDown e8 ( \stemDown d8 \stemDown cis8 \stemDown d8 \stemDown
    cis8 \stemDown b8 ) | % 126
    \stemUp fis8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis16 ( _\fff \stemDown gis16 \stemDown ais16 }
    \stemDown b32 \stemDown cis32 \stemDown d32 \stemDown e32 ) | % 127
    \stemDown fis4 -> \stemDown e8 -- \stemDown d8 -- \stemDown cis8 --
    \stemDown b8 -- | % 128
    \stemDown d8 ( -> \stemDown cis8 ) r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis,16 ( \stemDown gis16 \stemDown ais16 }
    \stemDown b32 \stemDown cis32 \stemDown d32 \stemDown e32 )
    \pageBreak | % 129
    \stemDown fis4 -> \stemDown e8 -- \stemDown d8 -- \stemDown cis8 --
    \stemDown b8 -- | \barNumberCheck #130
    \stemDown d8 ( -> \stemDown cis8 ) r4 r4 | % 131
    R2.*4 \pageBreak | % 135
    R2.*12 \pageBreak | % 147
    r4 r4 r4 | % 148
    R2.*5 \pageBreak | % 153
    R2.*6 \break | % 159
    R2.*6 \break | % 165
    R2.*7 \bar "|."
    }

PartPFourVoiceOne =  \relative gis' {
    \clef "treble" \time 3/4 \key d \major | % 1
    R2.*7 \pageBreak | % 8
    R2.*3 | % 11
    \stemDown <gis gis'>4 -- _\f _\< \stemDown <fis fis'>4. ( \stemUp
    <eis eis'>8 ) | % 12
    \stemDown <cis' cis'>4 ( -> _\! _\ff \stemDown <b b'>8. ) _\>
    \stemDown <a a'>16 -- \stemDown <gis gis'>8 -- \stemDown <a a'>8 --
    | % 13
    \stemDown <gis gis'>8 ( -> _\! _\f _\markup{ \small\italic {dim.} }
    \startTrillSpan \stemDown <fis fis'>8 ) \stemDown <eis eis'>8. --
    \stemDown <fis fis'>16 -- r4 | % 14
    R2.*2 \break | % 16
    R2.*8 \pageBreak | % 24
    R2.*9 \break | % 33
    R2.*8 \pageBreak | % 41
    R2.*6 \break | % 47
    R2.*6 \pageBreak | % 53
    R2. | % 54
    r2 \stopTrillSpan \stemDown <a a'>4 -- _\mf | % 55
    \stemDown <g g'>2 ( \stemUp <cis, cis'>4 ) | % 56
    \stemUp <d d'>2 ( \stemDown <a' a'>4 ) | % 57
    \stemDown <g g'>2 ( \stemUp <cis, cis'>4 ) | % 58
    \stemUp <d d'>2 \stemDown <c' c'>4 -- _\markup{ \small\italic
        {cresc.} } \startTrillSpan \pageBreak | % 59
    \stemDown <b b'>2 \stemUp <e, e'>4 -- | \barNumberCheck #60
    \stemUp <e e'>4 ( \stemDown <fis fis'>4 ) \stemDown <b b'>4 -- | % 61
    \stemDown <b b'>2. | % 62
    \stemDown <b b'>4 ( \stemDown <bes bes'>4 ~ ~ \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown <bes bes'>8 \stemDown <a a'>8 ) \stemDown <a a'>8 ~ ~
        }
    \stopTrillSpan _\f | % 63
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a a'>8 \stemDown <a a'>8 \stemDown <a a'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a a'>8 \stemDown <a a'>8 \stemDown <a a'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a a'>8 \stemDown <gis gis'>8 \stemDown <gis gis'>8 }
    | % 64
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown <a a'>8 \stemDown <a a'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a a'>8 \stemDown <a a'>8 \stemDown <a a'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a a'>8 \stemDown <a a'>8 \stemDown <a a'>8 ~ ~ }
    \pageBreak | % 65
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a a'>8 \stemDown <a a'>8 \stemDown <a a'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a a'>8 \stemDown <a a'>8 \stemDown <a a'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a a'>8 \stemDown <gis gis'>8 \stemDown <gis gis'>8 }
    | % 66
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown <a a'>8 \stemDown <a a'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a a'>8 \stemDown <a a'>8 \stemDown <a a'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <a a'>8 \stemDown <a a'>8 \stemDown <a a'>8 }
    | % 67
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown <b b'>8 _\markup{ \small\italic {cresc.} }
        \startTrillSpan \stemDown <b b'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <b b'>8 \stemDown <b b'>8 \stemDown <b b'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <b b'>8 \stemDown <b b'>8 \stemDown <b b'>8 }
    | % 68
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown <cis cis'>8 \stemDown <cis cis'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <cis cis'>8 \stemDown <cis cis'>8 \stemDown <cis cis'>8
        ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <cis cis'>8 \stemDown <cis cis'>8 \stemDown <cis cis'>8
        }
    | % 69
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown <d d'>8 \stopTrillSpan _\ff _\< \stemDown <d, d'>8
        ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d d'>8 \stemUp <d d'>8 \stemUp <d d'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d d'>8 \stemUp <d d'>8 \stemUp <d d'>8 }
    | \barNumberCheck #70
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 }
    \pageBreak | % 71
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis'8 _\! _\fff \stemUp fis8 \stemUp fis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis8 \stemUp fis8 \stemUp fis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis8 \stemUp fis8 \stemUp fis8 ~ }
    | % 72
    \stemUp fis8 r8 r4 r4 | % 73
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <c e>8 \stemDown <c e>8 \stemDown <c e>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <c e>8 \stemDown <c e>8 \stemDown <c e>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <c e>8 \stemDown <c e>8 \stemDown <c e>8 ~ ~ }
    | % 74
    \stemDown <c e>8 r8 r4 r4 | % 75
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g' c>8 \stemDown <g c>8 \stemDown <g c>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g c>8 \stemDown <g c>8 \stemDown <g c>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g c>8 \stemDown <g c>8 \stemDown <g c>8 ~ ~ }
    | % 76
    \stemDown <g c>8 r8 r4 r4 \pageBreak | % 77
    \stemDown <c, e>16 _\sempre _\fff r16 r8 r4 \stemDown <c e>16 r16 r8
    | % 78
    r4 \stemDown <c e>16 r16 r8 r4 | % 79
    \stemDown <c e>16 r16 r8 r4 r4 | \barNumberCheck #80
    R2. | % 81
    r8 \stemUp <c, g'>8 _\fff r4 r4 ^\fermata \pageBreak | % 82
    R2. | % 83
    \stemUp <cis cis'>2. ( ~ ~ _\ff | % 84
    \stemUp <cis cis'>8 \stemUp <b b'>8 ) r4 ^\fermata r4 | % 85
    \stemUp gis'2. ( ~ _\f ^ "a 2" | % 86
    \stemUp gis8 \stemUp fis8 ) r4 ^\fermata r8 \stemUp fis8 ( ~ _\mf
    _\< | % 87
    \stemUp fis8 _\! _\> \stemUp e8 ) r4 _\! r8 \stemUp e8 ( ~ _\p _\< | % 88
    \stemUp e8 _\! _\> \stemUp d8 ) r4 _\! r4 | % 89
    R2. \break | \barNumberCheck #90
    R2.*9 \pageBreak | % 99
    R2.*8 \break | % 107
    R2. | % 108
    \stemDown b'2. _\mf ^ "a 2" | % 109
    \stemDown d2 ( \stemUp fis,4 ) | \barNumberCheck #110
    \stemUp <e e'>2 _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp <d d'>4 | % 111
    \stemDown <g g'>2 \stemUp <b, b'>4 | % 112
    \stemUp <gis' b>4 \stopTrillSpan _\ff \stemUp <g ais>8 ( \stemUp
    <gis b>8 ) \stemDown <a c>4 | % 113
    \stemUp <gis b>8 ( _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemUp <a c>8 ) \stemDown <b d>4 \stemDown <a cis>8
    ( \stemDown <b d>8 ) \pageBreak | % 114
    \stemDown <cis e>4 -\markup{ \italic {pesante} } \stemDown <cis a'>4
    \stemDown <cis e>4 | % 115
    \stemDown <d a'>4 \stemDown <d gis>4 \stopTrillSpan _\fff \stemDown
    <d b'>4 | % 116
    \stemDown <e c'>2. | % 117
    \stemDown <e cis'>4 \stemDown <d d'>4 \stemDown <g a>4 \pageBreak | % 118
    \stemDown <d a'>2. | % 119
    \stemUp bes'4 \stemUp a4 \stemUp g4 | \barNumberCheck #120
    \stemUp fis2. \pageBreak | % 121
    \stemDown <g ais>4 \stemDown <fis ais>4 \stemDown <cis e>4 | % 122
    \stemDown <d fis>2. | % 123
    r4 \stemDown <b b'>8 ( \stemDown <a a'>8 \stemDown <g g'>8 \stemDown
    <fis fis'>8 ) \pageBreak | % 124
    \stemDown <a a'>2 ( \stemDown <g g'>8 \stemDown <fis fis'>8 ) | % 125
    \stemUp <e e'>8 ( \stemUp <d d'>8 \stemUp <cis cis'>8 \stemUp <d d'>8
    \stemUp <cis cis'>8 \stemUp <b b'>8 ) | % 126
    \stemUp <b d>8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis16 ( _\fff \stemUp d16 \stemUp e16 }
    \stemUp f32 \stemUp g32 \stemUp gis32 \stemUp ais32 ) | % 127
    \stemDown b4 -> \stemUp ais8 -- \stemUp gis8 -- \stemUp fis8 --
    \stemUp eis8 -- | % 128
    \stemUp e4 -> r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis16 ( \stemUp d16 \stemUp e16 }
    \stemUp f32 \stemUp g32 \stemUp gis32 \stemUp ais32 ) \pageBreak | % 129
    \stemDown b4 -> \stemUp ais8 -- \stemUp gis8 -- \stemUp fis8 --
    \stemUp eis8 -- | \barNumberCheck #130
    \stemUp e4 -> r4 r4 | % 131
    R2.*4 \pageBreak | % 135
    R2.*12 \pageBreak | % 147
    r4 r4 \stemUp <b d>4 _\f _\< | % 148
    \stemUp <c e>2 _\! _\sf _\> \stemUp <cis e>4 _\! _\f | % 149
    \stemUp <d fis>2 \stemUp <b d>4 _\< | \barNumberCheck #150
    \stemUp <c e>2 _\! _\sf _\> \stemUp <cis e>4 _\! _\f | % 151
    \stemUp fis4 ~ \stemUp fis8 r8 r4 | % 152
    R2. \pageBreak | % 153
    R2.*6 \break | % 159
    R2.*6 \break | % 165
    R2.*7 \bar "|."
    }

PartPFourVoiceTwo =  \relative d'' {
    \clef "treble" \time 3/4 \key d \major | % 1
     \once \override NoteHead.style = ##f \stemDown d2. s2*9 \pageBreak
    s1*6 \break s1*6 \pageBreak s4*27 \break s1*6 \pageBreak s2*9 \break
    s2*9 \pageBreak s2*9 \pageBreak s2*9 \pageBreak s2*9 \pageBreak | % 71
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis,8 \stemDown fis'8 \stemDown fis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown fis8 \stemDown fis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis8 \stemDown fis8 \stemDown fis8 ~ }
    | % 72
    \stemDown fis8 s8*29 \pageBreak s4*15 \pageBreak s1*6 \break s4*27
    \pageBreak s1*6 \break s4*21 \pageBreak s1*3 \pageBreak s2. | % 119
    \stemDown cis2 \stemDown e4 | \barNumberCheck #120
    \stemDown b'2. \pageBreak s4*9 \pageBreak s4*15 \pageBreak s2*9
    \pageBreak s1*9 \pageBreak s1*3 | % 151
    \stemDown d,,2. s2. \pageBreak s2*9 \break s2*9 \break s4*21 \bar
    "|."
    }

PartPFiveVoiceOne =  \relative e'' {
    \clef "treble" \time 3/4 \key f \major \transposition a | % 1
    R2.*7 \pageBreak _ "Clarinets" | % 8
    r2 _ "Cl." \stemDown e4 ~ _\mf | % 9
    \stemDown e4 \stemDown d4. ( _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemDown c8 ) | \barNumberCheck #10
    \stemDown g'4 -- \stemDown fis4. ( \stemDown e8 ) | % 11
    \stemDown b'4 -- \stemDown a4. ( \stemDown gis8 ) | % 12
    \stemDown e'4 ( -> \stopTrillSpan _\ff \stemDown d8. ) _\> \stemDown
    c16 -- \stemDown b8 -- \stemDown c8 -- | % 13
    \stemDown b8 ( -> _\! _\f _\markup{ \small\italic {dim. poco a poco}
        } \startTrillSpan \stemDown a8 ) \stemDown gis8. -- \stemDown a16
    -- \stemDown g8 -- \stemDown f8 -- | % 14
    \stemDown e8 ( -> \stemDown f8 ) \stemDown e8 -- \stemDown d8 --
    \stemDown c8 ( \stemDown d8 ) | % 15
    \stemDown c8 ( \stemDown bes8 ) r4 \stopTrillSpan r4 \break | % 16
    R2.*8 \pageBreak | % 24
    R2.*9 \break | % 33
    R2.*5 _ "Cl." | % 38
    r2 \stemUp a4 -- _\pp | % 39
    \stemDown bes2 ( -\markup{ \italic {con espressione} } \stemUp e,4 )
    | \barNumberCheck #40
    \stemUp f2 \stemDown c'4 -- \pageBreak | % 41
    \stemDown bes2 ( _ "Cl." \stemUp e,4 ) | % 42
    \stemUp f2 _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown es'4 -- | % 43
    \stemDown d2 \stemDown g4 -- | % 44
    \stemDown g4 ( \stemDown a4 ) \stemDown d,4 -- \stopTrillSpan _\mf | % 45
    \stemDown d2. | % 46
    \stemDown d4 ( _\> \stemDown des4 ~ \once \omit TupletBracket
    \times 2/3  {
        \stemDown des8 _\! _\p \stemDown c8 ) \stemDown c8 ~ }
    \break | % 47
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 _ "Cl." \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown b8 \stemDown b8 }
    | % 48
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    | % 49
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown b8 \stemDown b8 }
    | \barNumberCheck #50
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 }
    | % 51
    \once \omit TupletBracket
    \times 2/3  {
        r8 _\markup{ \small\italic {cresc.} } \startTrillSpan \stemDown
        d8 \stemDown d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 }
    | % 52
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 }
    \pageBreak | % 53
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stopTrillSpan _ "Cl." _\< \stemDown f8 \stemDown f8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f8 \stemDown f8 \stemDown f8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f8 \stemDown f8 \stemDown f8 }
    | % 54
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown g8 \stemDown g8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 \stemDown g8 \stemDown g8 }
    \stemDown c,4 -- _\! _\mf | % 55
    \stemDown bes2 ( \stemUp e,4 ) | % 56
    \stemUp f2 ( \stemDown c'4 ) | % 57
    \stemDown bes2 ( \stemUp e,4 ) | % 58
    \stemUp f2 \stemDown es'4 -- _\markup{ \small\italic {cresc.} }
    \startTrillSpan \pageBreak | % 59
    \stemDown d2 _ "Cl." \stemDown g4 -- | \barNumberCheck #60
    \stemDown g4 ( \stemDown a4 ) \stemDown d,4 -- | % 61
    \stemDown d2. | % 62
    \stemDown d4 ( \stemDown des4 ~ \once \omit TupletBracket
    \times 2/3  {
        \stemDown des8 \stemDown c8 ) \stemDown c8 ~ }
    \stopTrillSpan _\f | % 63
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown b8 \stemDown b8 }
    | % 64
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \pageBreak | % 65
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 _ "Cl." \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown b8 \stemDown b8 }
    | % 66
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 }
    | % 67
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown d8 _\markup{ \small\italic {cresc.} }
        \startTrillSpan \stemDown d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 }
    | % 68
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 }
    | % 69
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown f8 \stopTrillSpan _\ff _\< \stemDown f8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f8 \stemDown f8 \stemDown f8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f8 \stemDown f8 \stemDown f8 }
    | \barNumberCheck #70
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown g8 \stemDown g8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 \stemDown g8 \stemDown g8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 \stemDown g8 \stemDown g8 }
    \pageBreak | % 71
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 _\! _\fff _ "Cl." \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    | % 72
    \stemDown a8 r8 r4 r4 | % 73
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 \stemDown g8 \stemDown g8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 \stemDown g8 \stemDown g8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 \stemDown g8 \stemDown g8 ~ }
    | % 74
    \stemDown g8 r8 r4 r4 | % 75
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown es'8 \stemDown es8 \stemDown es8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown es8 \stemDown es8 \stemDown es8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown es8 \stemDown es8 \stemDown es8 ~ }
    | % 76
    \stemDown es8 r8 r4 r4 \pageBreak | % 77
    \stemDown g,16 _\sempre _\fff _ "Cl." r16 r8 r4 \stemDown g16 r16 r8
    | % 78
    r4 \stemDown g16 r16 r8 r4 | % 79
    \stemDown g16 r16 r8 r4 r4 | \barNumberCheck #80
    R2. | % 81
    r8 \stemUp g,8 _\fff r4 r4 ^\fermata \pageBreak | % 82
    R2. _ "Cl." | % 83
    \stemDown e'2. ( ~ _\ff | % 84
    \stemDown e8 \stemDown d8 ) r4 ^\fermata r4 | % 85
    \stemUp b,2. ( ~ _\f | % 86
    \stemUp b8 \stemUp a8 ) r4 ^\fermata r8 \stemUp a8 ( _\mf _\< | % 87
    \stemUp bes8 ) _\! r8 r4 r8 \stemUp g8 ( _\p _\< | % 88
    \stemUp a8 ) _\! r8 r4 r4 | % 89
    R2. \break | \barNumberCheck #90
    R2.*9 \pageBreak | % 99
    R2.*8 \break | % 107
    R2. _ "Cl." | % 108
    \stemUp d2. _\mf | % 109
    \stemUp f2 ( \stemUp a,4 ) | \barNumberCheck #110
    \stemDown g''2 _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown f4 | % 111
    \stemDown bes,2 \stemDown d4 | % 112
    \stemUp d,4 \stopTrillSpan _\ff \stemUp cis8 ( \stemUp d8 ) \stemUp
    es4 | % 113
    \stemUp d8 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp es8 ) \stemDown f'4 \stemDown e8 ( \stemDown f8 ) \pageBreak
    | % 114
    \stemDown g4 _ "Cl." -\markup{ \italic {pesante} } \stemDown c4
    \stemDown g4 | % 115
    \stemDown c4 \stemDown b4 \stopTrillSpan _\fff \stemDown d4 | % 116
    \stemDown es2. | % 117
    \stemDown e4 \stemDown f4 \stemDown c4 \pageBreak | % 118
    \stemDown c2. _ "Cl." | % 119
    \stemDown des4 \stemDown c4 \stemDown bes4 | \barNumberCheck #120
    \stemDown a2. \pageBreak | % 121
    \stemDown cis4 _ "Cl." \stemDown cis4 \stemDown g8 ( \stemDown g,8 )
    | % 122
    \stemUp a2. | % 123
    \stemUp d,2. \pageBreak | % 124
    \stemUp d2. _ "Cl." | % 125
    \stemUp d2 \stemUp bes4 | % 126
    \stemUp a8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis16 ( _\fff \stemUp d16 \stemUp e16 }
    \stemUp f32 \stemUp g32 \stemUp as32 \stemUp bes32 ) | % 127
    \stemDown b4 -> \stemUp a8 -- \stemUp gis8 -- \stemUp g8 -- \stemUp
    f8 -- | % 128
    \stemUp a,4 -> r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis16 ( \stemUp d16 \stemUp e16 }
    \stemUp f32 \stemUp g32 \stemUp as32 \stemUp bes32 ) \pageBreak | % 129
    \stemDown b4 -> _ "Cl." \stemUp a8 -- \stemUp gis8 -- \stemUp g8 --
    \stemUp f8 -- | \barNumberCheck #130
    \stemUp a,4 -> r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp d16 ( \stemUp e16 \stemUp f16 }
    \stemUp g32 \stemUp a32 \stemUp bes32 \stemUp c32 ) | % 131
    \stemDown d4 -> \stemDown c8 -- \stemDown bes8 -- \stemUp a8 --
    \stemUp g8 -- | % 132
    \stemUp bes8 ( -> \stemUp a8 ) r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp d,16 ( \stemUp e16 \stemUp f16 }
    \stemUp g32 \stemUp a32 \stemUp bes32 \stemUp c32 ) | % 133
    \stemDown d4 -> \stemDown c8 -- \stemDown bes8 -- \stemUp a8 --
    \stemUp g8 -- | % 134
    \stemUp bes8 ( -> \stemUp a8 ) r4 r4 \pageBreak | % 135
    \stemUp a8 ( -> _\f _ "Cl." \stemUp g8 ) r4 r4 | % 136
    \stemUp g8 ( -> _\mf \stemUp f8 ) r4 r4 | % 137
    R2.*10 \pageBreak | % 147
    r4 _ "Cl." r4 \stemUp f4 _\f _\< | % 148
    \stemUp g2 _\! _\sf _\> \stemUp g4 _\! _\f | % 149
    \stemUp a2 \stemUp f4 _\< | \barNumberCheck #150
    \stemUp g2 _\! _\sf _\> \stemUp g4 _\! _\f | % 151
    \stemUp a4 ~ \stemUp a8 r8 r4 | % 152
    \stemUp e,2 _\sf _\> \stemUp f4 \pageBreak | % 153
    \stemUp bes2 ( _\! _\sf _ "Cl." _\> \stemUp a4 ) _\! | % 154
    \stemUp bes2. _\sf _\> | % 155
    \stemUp a4 ~ _\! _\mf \stemUp a8 r8 r4 | % 156
    R2.*3 \break | % 159
    R2.*6 \break | % 165
    R2.*7 \bar "|."
    }

PartPFiveVoiceTwo =  \relative f'' {
    \clef "treble" \time 3/4 \key f \major \transposition a | % 1
     \once \override NoteHead.style = ##f \stemDown f2. s2*9 \pageBreak
    s1*6 \break s1*6 \pageBreak s4*27 \break s1*6 \pageBreak s2*9 \break
    s2*9 \pageBreak s2*9 \pageBreak s2*9 \pageBreak s2*9 \pageBreak s2*9
    \pageBreak s4*15 \pageBreak s1*6 \break s4*27 \pageBreak s1*6 \break
    s4*21 \pageBreak s1*3 \pageBreak s4*9 \pageBreak s4*9 \pageBreak
    s4*15 \pageBreak s2*9 \pageBreak s1*9 \pageBreak s2*9 \pageBreak
    s2*9 \break s2*9 \break s4*21 \bar "|."
    }

PartPSixVoiceOne =  \relative e' {
    \clef "treble" \time 3/4 \key f \major \transposition a | % 1
    R2.*7 \pageBreak | % 8
    r2 \stemUp e4 ~ _\mf | % 9
    \stemUp e4 \stemUp d4. ( _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemUp c8 ) | \barNumberCheck #10
    \stemUp g'4 -- \stemUp fis4. ( \stemUp e8 ) | % 11
    \stemDown b'4 -- \stemUp a4. ( \stemUp gis8 ) | % 12
    \stemDown e'4 ( -> \stopTrillSpan _\ff \stemDown d8. ) _\> \stemDown
    c16 -- \stemDown b8 -- \stemDown c8 -- | % 13
    \stemUp b8 ( -> _\! _\f _\markup{ \small\italic {dim. poco a poco} }
    \startTrillSpan \stemUp a8 ) \stemUp gis8. -- \stemUp a16 -- \stemUp
    g8 -- \stemUp f8 -- | % 14
    \stemUp e8 ( -> \stemUp f8 ) \stemUp e8 -- \stemUp d8 -- \stemUp c8
    ( \stemUp d8 ) | % 15
    \stemUp c8 ( \stemUp bes8 ) r4 \stopTrillSpan r4 \break | % 16
    R2.*8 \pageBreak | % 24
    R2.*9 \break | % 33
    R2.*5 | % 38
    r2 \stemUp a4 -- _\pp | % 39
    \stemUp bes2 ( -\markup{ \italic {con espressione} } \stemUp e,4 ) |
    \barNumberCheck #40
    \stemUp f2 \stemUp c'4 -- \pageBreak | % 41
    \stemUp bes2 ( \stemUp e,4 ) | % 42
    \stemUp f2 _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown es''4 -- | % 43
    \stemDown d2 \stemDown g4 -- | % 44
    \stemDown g4 ( \stemDown a4 ) \stemDown d,4 -- \stopTrillSpan _\mf | % 45
    \stemDown d2. | % 46
    \stemDown d4 ( _\> \stemDown des4 ~ \once \omit TupletBracket
    \times 2/3  {
        \stemDown des8 _\! _\p \stemDown c8 ) \stemDown c8 }
    \break | % 47
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown b8 \stemDown b8 }
    | % 48
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    | % 49
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown b8 \stemDown b8 }
    | \barNumberCheck #50
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 }
    | % 51
    \once \omit TupletBracket
    \times 2/3  {
        r8 _\markup{ \small\italic {cresc.} } \startTrillSpan \stemDown
        d8 \stemDown d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 }
    | % 52
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 }
    \pageBreak | % 53
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stopTrillSpan _\< \stemDown f8 \stemDown f8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f8 \stemDown f8 \stemDown f8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f8 \stemDown f8 \stemDown f8 }
    | % 54
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown g8 \stemDown g8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 \stemDown g8 \stemDown g8 }
    \stemDown c,4 -- _\! _\mf | % 55
    \stemDown bes2 ( \stemUp e,4 ) | % 56
    \stemUp f2 ( \stemDown c'4 ) | % 57
    \stemDown bes2 ( \stemUp e,4 ) | % 58
    \stemUp f2 \stemUp es4 -- _\markup{ \small\italic {cresc.} }
    \startTrillSpan \pageBreak | % 59
    \stemUp d2 \stemUp g4 -- | \barNumberCheck #60
    \stemUp g4 ( \stemUp a4 ) \stemUp d,4 -- | % 61
    \stemUp d2. | % 62
    \stemUp d4 ( \stemUp des4 ~ \once \omit TupletBracket
    \times 2/3  {
        \stemUp des8 \stemUp c8 ) \stemUp c8 ~ }
    \stopTrillSpan _\f | % 63
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp b8 \stemUp b8 }
    | % 64
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp c8 \stemUp c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 ~ }
    \pageBreak | % 65
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp b8 \stemUp b8 }
    | % 66
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp c8 \stemUp c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 }
    | % 67
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp d8 _\markup{ \small\italic {cresc.} } \startTrillSpan
        \stemUp d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp d8 \stemUp d8 \stemUp d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp d8 \stemUp d8 \stemUp d8 }
    | % 68
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp e8 \stemUp e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 \stemUp e8 \stemUp e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 \stemUp e8 \stemUp e8 }
    | % 69
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp f8 \stopTrillSpan _\ff _\< \stemUp f8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp f8 \stemUp f8 \stemUp f8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp f8 \stemUp f8 \stemUp f8 }
    | \barNumberCheck #70
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp g8 \stemUp g8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 \stemUp g8 \stemUp g8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 \stemUp g8 \stemUp g8 }
    \pageBreak | % 71
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a'8 _\! _\fff \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    | % 72
    \stemDown a8 r8 r4 r4 | % 73
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown es8 \stemDown es8 \stemDown es8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown es8 \stemDown es8 \stemDown es8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown es8 \stemDown es8 \stemDown es8 ~ }
    | % 74
    \stemDown es8 r8 r4 r4 | % 75
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown bes'8 \stemDown bes8 \stemDown bes8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown bes8 \stemDown bes8 \stemDown bes8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown bes8 \stemDown bes8 \stemDown bes8 ~ }
    | % 76
    \stemDown bes8 r8 r4 r4 \pageBreak | % 77
    \stemDown es,16 _\sempre _\fff r16 r8 r4 \stemDown es16 r16 r8 | % 78
    r4 \stemDown es16 r16 r8 r4 | % 79
    \stemDown es16 r16 r8 r4 r4 | \barNumberCheck #80
    R2. | % 81
    r8 \stemUp bes,8 _\fff r4 r4 ^\fermata \pageBreak | % 82
    R2. | % 83
    \stemUp e2. ( ~ _\ff | % 84
    \stemUp e8 \stemUp d8 ) r4 ^\fermata r4 | % 85
    \stemUp b2. ( ~ _\f | % 86
    \stemUp b8 \stemUp a8 ) r4 ^\fermata r8 \stemUp a8 ( _\mf _\< | % 87
    \stemUp g8 ) _\! r8 r4 r8 \stemUp g8 ( _\p _\< | % 88
    \stemUp a8 ) _\! r8 r4 r4 | % 89
    R2. \break | \barNumberCheck #90
    R2.*9 \pageBreak | % 99
    R2.*8 \break | % 107
    R2. | % 108
    \stemUp d2. _\mf | % 109
    \stemUp f2 ( \stemUp a,4 ) | \barNumberCheck #110
    \stemUp g'2 _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp f4 | % 111
    \stemDown bes2 \stemUp d,4 | % 112
    \stemUp b4 \stopTrillSpan _\ff \stemUp ais8 ( \stemUp b8 ) \stemUp c4
    | % 113
    \stemUp b8 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp c8 ) \stemDown d'4 \stemDown c8 ( \stemDown d8 ) \pageBreak
    | % 114
    \stemUp g,4 -\markup{ \italic {pesante} } \stemDown c4 \stemUp g4 | % 115
    \stemDown c4 \stemDown b4 \stopTrillSpan _\fff \stemDown d4 | % 116
    \stemDown g2. | % 117
    \stemDown g4 \stemDown f4 \stemDown bes4 \pageBreak | % 118
    \stemDown c,2. | % 119
    \stemDown des4 \stemDown c4 \stemDown bes4 | \barNumberCheck #120
    \stemDown d2. \pageBreak | % 121
    \stemDown bes'4 \stemDown a4 \stemUp e8 ( \stemUp e,8 ) | % 122
    \stemUp f2. | % 123
    \stemUp c2. \pageBreak | % 124
    \stemUp g2. | % 125
    \stemUp bes2 \stemUp f4 | % 126
    \stemUp a8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis16 ( _\fff \stemUp d16 \stemUp e16 }
    \stemUp f32 \stemUp g32 \stemUp as32 \stemUp bes32 ) | % 127
    \stemDown b4 -> \stemUp a8 -- \stemUp gis8 -- \stemUp g8 -- \stemUp
    f8 -- | % 128
    \stemUp a,4 -> r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis16 ( \stemUp d16 \stemUp e16 }
    \stemUp f32 \stemUp g32 \stemUp as32 \stemUp bes32 ) \pageBreak | % 129
    \stemDown b4 -> \stemUp a8 -- \stemUp gis8 -- \stemUp g8 -- \stemUp
    f8 -- | \barNumberCheck #130
    \stemUp a,4 -> r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp a16 ( \stemUp bes16 \stemUp b16 }
    \stemUp cis32 \stemUp d32 \stemUp e32 \stemUp fis32 ) | % 131
    \stemUp g4 -> \stemUp fis8 -- \stemUp e8 -- \stemUp d8 -- \stemUp
    cis8 -- | % 132
    \stemUp e4 -> r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp a,16 ( \stemUp bes16 \stemUp b16 }
    \stemUp cis32 \stemUp d32 \stemUp e32 \stemUp fis32 ) | % 133
    \stemUp g4 -> \stemUp fis8 -- \stemUp e8 -- \stemUp d8 -- \stemUp
    cis8 -- | % 134
    \stemUp e4 -> r4 r4 \pageBreak | % 135
    \stemUp d4 -> _\f r4 r4 | % 136
    \stemUp d4 -> _\mf r4 r4 | % 137
    R2.*10 \pageBreak | % 147
    r4 r4 \stemUp d4 _\f _\< | % 148
    \stemUp es2 _\! _\sf _\> \stemUp e4 _\! _\f | % 149
    \stemUp f2 \stemUp d4 _\< | \barNumberCheck #150
    \stemUp es2 _\! _\sf _\> \stemUp e4 _\! _\f | % 151
    \stemUp f2. | % 152
    \stemUp e,2 _\sf _\> \stemUp f4 \pageBreak | % 153
    \stemUp bes2 ( _\! _\sf _\> \stemUp a4 ) _\! | % 154
    \stemUp g2. _\sf _\> | % 155
    \stemUp a4 ~ _\! _\mf \stemUp a8 r8 r4 | % 156
    R2.*3 \break | % 159
    R2.*6 \break | % 165
    R2.*7 \bar "|."
    }

PartPSixVoiceTwo =  \relative f'' {
    \clef "treble" \time 3/4 \key f \major \transposition a | % 1
     \once \override NoteHead.style = ##f \stemDown f2. s2*9 \pageBreak
    s1*6 \break s1*6 \pageBreak s4*27 \break s1*6 \pageBreak s2*9 \break
    s2*9 \pageBreak s2*9 \pageBreak s2*9 \pageBreak s2*9 \pageBreak s2*9
    \pageBreak s4*15 \pageBreak s1*6 \break s4*27 \pageBreak s1*6 \break
    s4*21 \pageBreak s1*3 \pageBreak s4*9 \pageBreak s4*9 \pageBreak
    s4*15 \pageBreak s2*9 \pageBreak s1*9 \pageBreak s2*9 \pageBreak
    s2*9 \break s2*9 \break s4*21 \bar "|."
    }

PartPSevenVoiceOne =  \relative fis' {
    \clef "bass" \time 3/4 \key d \major | % 1
    R2. | % 2
    r4 \clef "tenor" \stemDown fis2 ~ ^ "a 2" _\mf _\> | % 3
    \stemDown fis4 ~ \stemDown fis8 _\! _\p r8 r4 | % 4
    r4 \stemDown fis2 ~ _\mf _\> | % 5
    \stemDown fis4 _\! _\p \stemDown e2 ( ~ | % 6
    \stemDown e4 \stemDown d4 ) \stemDown a'4 ~ _\mp | % 7
    \stemDown a4 \stemDown gis2 ( ~ \pageBreak | % 8
    \stemDown gis4 \stemDown fis4 ) \stemDown cis4 ~ _\mf | % 9
    \stemDown cis4 \stemDown b4. ( _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemDown a8 ) | \barNumberCheck #10
    \stemDown e'4 -- \stemDown dis4. ( \stemDown cis8 ) | % 11
    \stemDown gis'4 -- \stemDown fis4. ( \stemDown eis8 ) | % 12
    \stemDown cis'4 ( -> \stopTrillSpan _\ff \stemDown b8. ) _\>
    \stemDown a16 -- \stemDown gis8 -- \stemDown a8 -- | % 13
    \stemDown gis8 ( -> _\! _\f _\markup{ \small\italic {dim. poco a
            poco} } \startTrillSpan \stemDown fis8 ) \stemDown eis8. --
    \stemDown fis16 -- \stemDown e8 -- \stemDown d8 -- | % 14
    \stemDown cis8 ( -> \stemDown d8 ) \stemDown cis8 -- \stemDown b8 --
    \stemDown a8 ( \stemDown b8 ) | % 15
    \stemDown a8 ( \stemDown g8 ) \stemDown fis'8 ( \stemDown g8 )
    \stemDown fis8 ( \stopTrillSpan _\mp _\> \stemDown e8 \break | % 16
    \stemDown d8 \stemDown e8 ) \stemDown d8 ( _\! _\p _\> \stemDown cis8
    \grace { \stemUp d16 \stemUp cis16 } \stemDown bis8 \stemDown cis8 )
    | % 17
    \stemDown d8. ( _\! _\pp _\< \stemDown cis16 ) \stemDown e4.. _\!
    _\mp _\> \stemDown d16 | % 18
    \stemDown cis2 ~ _\! _\pp _\> \stemDown cis8 r8 _\! | % 19
    R2.*2 | % 21
    r4 \stemDown fis2 ~ _\mf _\> | % 22
    \stemDown fis4 ~ \stemDown fis8 _\! _\p r8 r4 | % 23
    r4 \stemDown fis2 ~ _\mf _\> \pageBreak | % 24
    \stemDown fis4 _\! _\p \stemDown e2 ~ | % 25
    \stemDown e4 _\> \stemDown d2 ~ | % 26
    \stemDown d4 _\! _\pp \stemDown cis2 ~ | % 27
    \stemDown cis4 \stemDown b2 ~ _\pp _\markup{ \small\italic {cresc.}
        } \startTrillSpan | % 28
    \stemDown b4 \stemDown ais2 | % 29
    \stemDown a4 \stemUp g4.. \stemUp fis16 | \barNumberCheck #30
    \clef "bass" \stemDown fis4 -- \stopTrillSpan _\f -\markup{ \italic
        {espressivo} } _\< \stemDown e4.. \stemDown d16 | % 31
    \stemDown d4 -- _\! _\ff \stemUp cis4.. \stemUp b16 | % 32
    \stemUp b8. \stemUp a16 \stemUp a8. _\markup{ \small\italic {dim.} }
    \startTrillSpan \stemUp g16 \stemUp g8. \stemUp fis16 \break | % 33
    \stemUp fis8. \stemUp e16 \stemUp e8. \stemUp d16 \stemUp d8.
    \stemUp cis16 | % 34
    \stemUp cis4 -- \stopTrillSpan _\p \stemUp d16 ( _\< \stemUp cis16 )
    \stemUp bis16 -- \stemUp cis16 -- \stemUp e8. _\! _\> \stemUp d16 | % 35
    \stemUp cis2. ~ _\! _\p _\> | % 36
    \stemUp cis2 ~ _\! _\pp \stemUp cis8 r8 | % 37
    R2. | % 38
    r2 \stemDown <fis' fis'>4 -- _\pp | % 39
    \stemDown <g g'>2 ( -\markup{ \italic {con espressione} } \stemDown
    <cis, cis'>4 ) | \barNumberCheck #40
    \stemDown <d d'>2 \stemDown <a' a'>4 -- \pageBreak | % 41
    \stemDown <g g'>2 ( \stemDown <cis, cis'>4 ) | % 42
    \stemDown <d d'>2 _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown c'4 -- ^ "a 2" | % 43
    \stemDown b2 \clef "tenor" \stemDown e4 -- | % 44
    \stemDown e4 ( \stemDown fis4 ) \stemDown b,4 -- \stopTrillSpan _\mf
    | % 45
    \stemDown b2. | % 46
    \stemDown b4 ( _\> \stemDown bes4 ~ \once \omit TupletBracket
    \times 2/3  {
        \stemDown bes8 _\! _\p \stemDown a8 ) \stemDown a8 ~ }
    \break | % 47
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp gis8 \stemUp gis8 }
    | % 48
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    | % 49
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp gis8 \stemUp gis8 }
    | \barNumberCheck #50
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 }
    | % 51
    \once \omit TupletBracket
    \times 2/3  {
        r8 _\markup{ \small\italic {cresc.} } \startTrillSpan \stemDown
        b8 \stemDown b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 \stemDown b8 \stemDown b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 \stemDown b8 \stemDown b8 }
    | % 52
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown cis8 \stemDown cis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 \stemDown cis8 \stemDown cis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 \stemDown cis8 \stemDown cis8 }
    \pageBreak | % 53
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stopTrillSpan _\< \stemDown d8 \stemDown d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 }
    | % 54
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 }
    r4 _\! | % 55
    R2.*3 | % 58
    r2 \stemDown c4 -- _\mf _\markup{ \small\italic {cresc.} }
    \startTrillSpan \pageBreak | % 59
    \stemDown b2 \stemDown e4 -- | \barNumberCheck #60
    \stemDown e4 ( \stemDown fis4 ) \stemDown b,4 -- | % 61
    \stemDown b2. | % 62
    \stemDown b4 ( \stemDown bes4 ~ \once \omit TupletBracket
    \times 2/3  {
        \stemDown bes8 \stemDown a8 ) \stemDown a8 ~ }
    \stopTrillSpan _\f | % 63
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp gis8 \stemUp gis8 }
    | % 64
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \pageBreak | % 65
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp gis8 \stemUp gis8 }
    | % 66
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown a8 \stemDown a8 }
    | % 67
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown b8 _\markup{ \small\italic {cresc.} }
        \startTrillSpan \stemDown b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 \stemDown b8 \stemDown b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown b8 \stemDown b8 \stemDown b8 }
    | % 68
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown cis8 \stemDown cis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 \stemDown cis8 \stemDown cis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 \stemDown cis8 \stemDown cis8 }
    | % 69
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown d8 \stopTrillSpan _\ff _\< \stemDown d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 }
    | \barNumberCheck #70
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 }
    \pageBreak | % 71
    \clef "bass" \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d,, d'>8 _\! _\fff \stemUp <d d'>8 \stemUp <d d'>8 ~ ~
        }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d d'>8 \stemUp <d d'>8 \stemUp <d d'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d d'>8 \stemUp <d d'>8 \stemUp <d d'>8 ~ ~ }
    | % 72
    \stemUp <d d'>8 r8 r4 r4 | % 73
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <c c'>8 \stemUp <c c'>8 \stemUp <c c'>8 ~ ~ }
    | % 74
    \stemUp <c c'>8 r8 r4 r4 | % 75
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    | % 76
    \stemUp <e e'>8 r8 r4 r4 \pageBreak | % 77
    \stemUp <g g'>16 _\sempre _\fff r16 r8 r4 \stemDown <c c'>16 r16 r8
    | % 78
    r4 \stemDown e16 r16 r8 r4 | % 79
    \stemDown g16 r16 r8 r4 r4 | \barNumberCheck #80
    r4 r4 \once \omit TupletBracket
    \times 4/7  {
        \stemUp c16*161/160 ( _\fff \stemUp b16*161/160 \stemUp a16*161/160
        \stemUp g16*161/160 \stemUp f16*161/160 \stemUp e16*161/160
        \stemUp d16*161/160 }
    | % 81
    \stemUp c8 ) \stemUp c8 r4 r4 ^\fermata \pageBreak | % 82
    R2. | % 83
    \stemUp ais2. ( _\ff ^ "a 2" | % 84
    \stemUp b4 ) r4 ^\fermata r4 | % 85
    \stemUp eis,2. ( ^\f | % 86
    \stemUp fis4 ) r4 ^\fermata r4 | % 87
    R2.*3 \break | \barNumberCheck #90
    R2.*9 \pageBreak | % 99
    R2. | \barNumberCheck #100
    \stemUp e2. ~ ^ "a 2" _\ff | % 101
    \stemUp e2. ~ | % 102
    \stemUp e2 ~ _\> \stemUp e8 _\! _\mf r8 | % 103
    R2.*4 \break | % 107
    R2.*4 | % 111
    \stemDown d'2 _\f ^ "a 2" \stemDown e4 | % 112
    \stemDown e2 _\ff \stemDown dis8 ( \stemDown e8 ) | % 113
    \stemDown e4 \stemDown g2 \pageBreak | % 114
    \stemUp bes,4 _\ff -\markup{ \italic {pesante} } _\markup{
        \small\italic {cresc.} } \startTrillSpan \stemUp a4 \stemUp g4 | % 115
    \stemUp f4 \stemUp e2 \stopTrillSpan _\fff | % 116
    \stemUp fis4 -\markup{ \italic {marcato e pesante} } \stemUp gis4
    \stemUp a4 | % 117
    \stemUp ais4 \stemUp b4 \stemUp cis4 \pageBreak | % 118
    \stemUp d4 \stemUp e4 \stemUp f4 | % 119
    \stemUp g4 \stemUp a4 \stemUp ais4 | \barNumberCheck #120
    \stemUp b4 \stemUp cis4 \stemUp d4 \pageBreak | % 121
    \stemUp e4 \stemUp fis4 \stemUp g4 | % 122
    \stemUp gis4 \stemUp ais4 \stemUp b4 | % 123
    \stemUp b,,2. ~ \pageBreak | % 124
    \stemUp e,2. \stemUp b'2. | % 125
    \stemUp eis,2. \stemUp b'2. | % 126
    \stemUp fis8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown e'16 ( _\fff \stemDown eis16 \stemDown fis16 }
    \stemDown gis32 \stemDown ais32 \stemDown b32 \stemDown cis32 ) | % 127
    \stemDown d4 -> \stemDown cis8 -- \stemDown b8 -- \stemDown ais8 --
    \stemDown gis8 -- | % 128
    \stemDown ais4 -> r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown e16 ( \stemDown eis16 \stemDown fis16 }
    \stemDown gis32 \stemDown ais32 \stemDown b32 \stemDown cis32 )
    \pageBreak | % 129
    \stemDown d4 -> \stemDown cis8 -- \stemDown b8 -- \stemDown ais8 --
    \stemDown gis8 -- | \barNumberCheck #130
    \stemDown ais4 -> r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown gis,16 ( \stemDown d'16 \stemDown ais16 \stemDown e'16
        \stemDown b16 }
    \stemDown f'16*2/3 \stemDown cis32 \stemDown g'32 \stemDown d32
    \stemDown as'32 \stemDown e32 \stemDown bes'32 \stemDown fis32 )
    \stemDown c'32 | % 131
    \stemDown g4 -> \stemDown cis4 \stemDown fis,8 -- \stemDown c'8
    \stemDown e,8 -- \stemDown ais8 \stemDown d,8 -- \stemDown gis8
    \stemDown cis,8 -- \stemDown g'8 | % 132
    \stemUp e4 -> r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp d16 ( \stemUp e16 \stemUp f16 }
    \stemUp g32 \stemUp as32 \stemUp bes32 \stemUp c32 ) | % 133
    \stemUp cis4 -> \stemUp c8 -- \stemUp ais8 -- \stemUp gis8 --
    \stemUp g8 -- | % 134
    \stemUp e4 -> r4 r4 \pageBreak | % 135
    \stemUp g4 -> _\f r4 r4 | % 136
    \stemUp cis8 ( -> _\mf \stemUp d8 ) r4 r4 | % 137
    R2.*10 \pageBreak | % 147
    r4 r4 \clef "tenor" \stemDown b4 _\f _\< \stemDown d4 | % 148
    \stemDown c2 _\! _\sf _\> \stemDown e2 \stemDown cis4 _\! _\f
    \stemDown e4 | % 149
    \stemDown d2 \stemDown fis2 \stemDown b,4 _\< \stemDown d4 |
    \barNumberCheck #150
    \stemDown c2 _\! _\sf _\> \stemDown e2 \stemDown cis4 _\! _\f
    \stemDown e4 | % 151
    \stemUp fis4 ~ \stemUp fis8 r8 r4 | % 152
    \clef "bass" \stemUp cis,2 _\sf _\> \stemUp d4 \pageBreak | % 153
    \stemUp g2 ( _\! _\sf _\> \stemUp fis4 ) _\! | % 154
    \stemUp g2. _\sf _\> | % 155
    \stemDown fis4 ~ _\! _\mf ^ "a 2" _\> \stemDown fis8 _\! r8 \stemUp
    b,4 -- _\mp | % 156
    \stemUp e,2 ( -> \stemUp g4 ) | % 157
    \stemUp d2 \stemUp b'4 -- | % 158
    \stemUp e,2 ( -> \stemUp g4 ) \break | % 159
    \stemUp d2. | \barNumberCheck #160
    \stemUp cis2 -> _\markup{ \small\italic {dim.} } \startTrillSpan
    \stemUp d4 -- | % 161
    \stemUp g2 ( -> \stemUp fis4 ) | % 162
    \stemUp g2. -> | % 163
    \stemUp fis4 ~ \stopTrillSpan _\p \stemUp fis8 r8 r4 | % 164
    R2. \break | % 165
    R2.*7 \bar "|."
    }

PartPSevenVoiceTwo =  \relative c {
    \clef "bass" \time 3/4 \key d \major s1 \clef "tenor" s4*17
    \pageBreak s1*6 \break s1*6 \pageBreak s2*9 | \barNumberCheck #30
    \clef "bass" s4*9 \break s1*6 \pageBreak s1*2 \clef "tenor" s2*5
    \break s2*9 \pageBreak s2*9 \pageBreak s2*9 \pageBreak s2*9
    \pageBreak | % 71
    \clef "bass" s2*9 \pageBreak s1*1761/640 \once \omit TupletBracket
    \times 4/7  {
        \stemDown c16*161/160 ( \stemDown b16*161/160 \stemDown a16*161/160
        \stemDown g16*161/160 \stemDown f16*161/160 \stemDown e16*161/160
        \stemDown d16*161/160 }
    | % 81
    \stemDown c8 ) \stemDown c'8 s1*159/320 \pageBreak s4*9 | % 85
    R2.*2 s4*9 \break s4*27 \pageBreak s1*6 \break s4*21 \pageBreak s2.
    | % 115
    \stemDown f,4 \stemDown e2 ~ | % 116
    \stemDown e2. ~ | % 117
    \stemDown e2. ~ \pageBreak | % 118
    \stemDown e2. ~ | % 119
    \stemDown e2. ~ | \barNumberCheck #120
    \stemDown e2. ~ \pageBreak | % 121
    \stemDown e2. ~ | % 122
    \stemDown e2. ~ | % 123
    \stemDown e2. ~ \pageBreak s4*15 \pageBreak s4*9 | % 132
    \stemDown b'8 ( -> \stemDown ais8 ) s4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown gis16 ( \stemDown ais16 \stemDown b16 }
    \stemDown cis32 \stemDown d32 \stemDown e32 \stemDown fis32 ) | % 133
    \stemDown g4 -> \stemDown fis8 -- \stemDown e8 -- \stemDown d8 --
    \stemDown cis8 -- | % 134
    \stemDown b8 ( -> \stemDown ais8 ) s2 \pageBreak | % 135
    \stemDown d8 ( -> \stemDown cis8 ) s2 | % 136
    \stemDown g'8 ( -> \stemDown fis8 ) s1*8 \pageBreak s2 \clef "tenor"
    s2*5 | % 151
    \stemDown d'2. | % 152
    \clef "bass" \stemDown cis,2 \stemDown d4 \pageBreak | % 153
    \stemDown g2 ( \stemDown fis4 ) | % 154
    \stemDown e2. s1*3 \break s2*9 \break s4*21 \bar "|."
    }

PartPEightVoiceOne =  \relative e {
    \clef "treble" \time 3/4 \key c \none \transposition f | % 1
    R2.*7 \pageBreak _ "Horns" | % 8
    R2.*8 \break _ "in F" | % 16
    R2.*8 \pageBreak | % 24
    R2.*4 _ "Hn." | % 28
    R2.*2 _\markup{ \small\italic {cresc.} } | \barNumberCheck #30
    R2. | % 31
    R2.*2 \break | % 33
    R2.*4 _ "Hn." | % 37
    \once \omit TupletBracket
    \times 2/3  {
        r8 _\pp \startTrillSpan \stopTrillSpan _\mf _\< _\! _\f
        _\markup{ \small\italic {dim.} } \startTrillSpan \stemUp <e e'>8
        _\pp \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    | % 38
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    | % 39
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    | \barNumberCheck #40
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \pageBreak | % 41
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 _ "Hn." \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    | % 42
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 }
    | % 43
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <d d'>8 \stemUp <d d'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp <fis fis'>8 \stemUp <fis fis'>8 ~ ~ }
    | % 44
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <fis fis'>8 \stemUp <fis fis'>8 \stemUp <fis fis'>8 ~ ~
        }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <fis fis'>8 \stemUp <fis fis'>8 \stemUp <fis fis'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp <bes bes'>8 _\mf \stemUp <bes bes'>8 ~ ~ }
    | % 45
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <bes bes'>8 \stemUp <bes bes'>8 \stemUp <bes bes'>8 ~ ~
        }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <bes bes'>8 \stemUp <b b'>8 \stemUp <b b'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <b b'>8 \stemUp <bes bes'>8 \stemUp <a a'>8 ~ ~ }
    | % 46
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <a a'>8 _\> \stemUp <a a'>8 \stemUp <a a'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <a a'>8 \stemUp <gis gis'>8 \stemUp <gis gis'>8 }
    \stemUp <a a'>8 _\! _\p r8 \break | % 47
    R2.*6 \pageBreak | % 53
    R2. _ "Hn." | % 54
    r4 r4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp <e' e'>8 _\mf \stemUp <e e'>8 ~ ~ }
    | % 55
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    | % 56
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    | % 57
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    | % 58
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 }
    \pageBreak | % 59
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 _ "Hn." \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <d d'>8 \stemUp <d d'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown <fis fis'>8 \stemDown <fis fis'>8 ~ ~ }
    | \barNumberCheck #60
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <fis fis'>8 \stemDown <fis fis'>8 \stemDown <fis fis'>8
        ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <fis fis'>8 \stemDown <fis fis'>8 \stemDown <fis fis'>8
        }
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp <bes, bes'>8 \stemUp <bes bes'>8 ~ ~ }
    | % 61
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <bes bes'>8 \stemUp <bes bes'>8 \stemUp <bes bes'>8 ~ ~
        }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <bes bes'>8 \stemUp <b b'>8 \stemUp <b b'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <b b'>8 \stemUp <bes bes'>8 \stemUp <a a'>8 ~ ~ }
    | % 62
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <a a'>8 \stemUp <a a'>8 \stemUp <a a'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <a a'>8 \stemUp <gis gis'>8 \stemUp <gis gis'>8 }
    \stemUp <a a'>8 r8 | % 63
    \stemUp <d d'>2 ( _\f \stemUp <a a'>8 ) r8 | % 64
    R2. \pageBreak | % 65
    \stemUp <d d'>2 ( _ "Hn." \stemUp <a a'>8 ) r8 | % 66
    R2. | % 67
    \stemUp <cis cis'>4 -- _\f \stemUp <b b'>4 -- \stemUp <a a'>4 -- | % 68
    \stemUp gis'8 -- r8 r4 r4 | % 69
    \stemUp <e e'>4 -- _\f \stemUp <d d'>4 -- \stemUp <c c'>4 -- |
    \barNumberCheck #70
    \stemUp b'8 -- _\< r8 r4 r4 \pageBreak | % 71
    \stemDown <fis fis'>2. ~ ~ _\! _\fff _ "Hn." | % 72
    \stemDown <fis fis'>8 r8 r4 r4 | % 73
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d b'>8 \stemUp <d b'>8 \stemUp <d b'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d b'>8 \stemUp <d b'>8 \stemUp <d b'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d b'>8 \stemUp <d b'>8 \stemUp <d b'>8 ~ ~ }
    | % 74
    \stemUp <d b'>8 r8 r4 r4 | % 75
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g g'>8 \stemDown <g g'>8 \stemDown <g g'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g g'>8 \stemDown <g g'>8 \stemDown <g g'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g g'>8 \stemDown <g g'>8 \stemDown <g g'>8 ~ ~ }
    | % 76
    \stemDown <g g'>8 r8 r4 r4 \pageBreak | % 77
    \stemUp <g b>16 _\sempre _\fff _ "Hn." r16 r8 r4 \stemUp <g b>16 r16
    r8 | % 78
    r4 \stemUp <g b>16 r16 r8 r4 | % 79
    \stemUp <g b>16 r16 r8 r4 r4 | \barNumberCheck #80
    R2. | % 81
    r8 \stemDown <g d'>8 _\fff r4 r4 ^\fermata \pageBreak | % 82
    R2.*8 \break | \barNumberCheck #90
    R2. _ "Hn." | % 91
    r4 \stemUp cis2 ~ ^\mf ^\> | % 92
    \stemUp cis4 ~ \stemUp cis8 r8 ^\! r4 | % 93
    r4 \stemUp cis2 ~ ^\mf ^\> | % 94
    \stemUp cis4 ^\! ^\p \stemUp b2 ~ | % 95
    \stemUp b4 \stemUp a2 ~ ^\> | % 96
    \stemUp a4 ^\! ^\pp \stemUp gis2 ~ | % 97
    \stemUp gis4 \stemUp fis4.. ^\< \stemUp e16 | % 98
    \stemUp e4 ^\! ^\f \stemUp d8 r8 _\f r4 \pageBreak | % 99
    R2.*3 _ "Hn." | % 102
    R2.*3 _\markup{ \small\italic {cresc.} } | % 105
    r4 \startTrillSpan _\> \stemUp cis'2 ~ ^\mf ^\> | % 106
    \stemUp cis4 ~ \stemUp cis8 r8 ^\! r4 \break | % 107
    r4 _ "Hn." \stemUp cis2 ~ ^\mf | % 108
    \stemUp cis8 _\mf \stemUp b8 \stemUp d2 ~ | % 109
    \stemUp d8 \stemUp cis8 \stemUp e4 \stemDown <fis, fis'>4 ~ ~ |
    \barNumberCheck #110
    \stemDown <fis fis'>8 \stemDown <e e'>8 \stemDown <g g'>2 ~ ~
    _\markup{ \small\italic {cresc.} } \startTrillSpan | % 111
    \stemDown <g g'>8 \stemDown <fis fis'>8 \stemUp a4 \stemUp b4 | % 112
    \stemDown <fis fis'>4 \stemDown <eis eis'>8 ( \stemDown <fis fis'>8
    ) \stemDown <g g'>4 | % 113
    \stemDown <fis fis'>8 ( \stemDown <g g'>8 ) \stemUp <fis a>4 \stemUp
    <e gis>8 ( \stemUp <fis a>8 ) \pageBreak | % 114
    \stemUp <b, gis'>4 \stopTrillSpan _ "Hn." -\markup{ \italic
        {pesante} } _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp <e gis>4 \stemUp <b gis'>4 | % 115
    \stemUp <e a>4 \stemUp <dis a'>4 \stopTrillSpan _\fff \stemUp <fis
        a>4 | % 116
    \stemUp <g b>2. | % 117
    \stemUp <gis b>4 \stemUp a4 \stemUp <d, e>4 \pageBreak | % 118
    \stemUp e2. _ "Hn." | % 119
    \stemUp gis2 \stemUp b,4 | \barNumberCheck #120
    \stemUp <cis fis>2. \pageBreak | % 121
    \stemUp <d f>4 _ "Hn." \stemUp <cis f>4 \stemUp <b gis'>4 | % 122
    \stemUp <a cis>2. | % 123
    \stemDown <e'' fis>2. \pageBreak | % 124
    \stemDown <b fis'>2. _ "Hn." | % 125
    \stemDown <d fis>2 \stemDown <a d>4 | % 126
    \stemUp fis8 r8 r4 _\ff _\ gestopft r4 | % 127
    R2. | % 128
    \stemUp cis'8 ~ -> ^\ff \stemUp cis16 r16 r4 r4 \pageBreak | % 129
    R2. _ "Hn." | \barNumberCheck #130
    \stemUp cis8 ~ -> \stemUp cis16 r16 \clef "bass" r4 r4 | % 131
    R2. | % 132
    \stemUp gis,8 ~ -> \stemUp gis16 r16 r4 r4 | % 133
    R2. | % 134
    \stemUp gis8 ~ -> \stemUp gis16 r16 r4 r4 \pageBreak | % 135
    R2.*2 _ "Hn." | % 137
    R2.*10 \pageBreak | % 147
    \clef "treble" R2. _ "Hn." -\markup{ \italic {nicht gest.} } | % 148
    R2.*4 | % 152
    \stemUp fis'2. _\! _\p _\p _\< _\! _\mf ^\sf _\mf ^\> \pageBreak | % 153
    \stemUp eis2 ( ^\! ^\sf _ "Hn." ^\> \stemUp fis4 ) ^\! | % 154
    R2. | % 155
    R2.*4 \break | % 159
    R2.*6 \break | % 165
    R2.*7 \bar "|."
    _\> }

PartPEightVoiceTwo =  \relative a' {
    \clef "treble" \time 3/4 \key c \none \transposition f | % 1
     \once \override NoteHead.style = ##f \stemUp a2. s2*9 \pageBreak
    s1*6 \break s1*6 \pageBreak s1*3 | % 28
    \stemDown b,2. | % 29
    \stemDown fis2 ~ \stemDown fis8 r8 | \barNumberCheck #30
    \stemDown fis2. ~ | % 31
    \stemDown fis2 ~ \stemDown fis8 r8 | % 32
    r2 \stemDown fis4 ~ _\mf \break | % 33
    \stemDown fis2. ~ | % 34
    \stemDown fis2. ~ | % 35
    \stemDown fis4 \stemDown f4 ( \stopTrillSpan _\p _\> \stemDown e4 ~
    | % 36
    \stemDown e2 ~ \stemDown e8 ) _\! _\pp r8 s1*3 \pageBreak s2*9
    \break s2*9 \pageBreak s2*9 \pageBreak s2*9 \pageBreak s4*9 | % 68
    \stemDown gis2. s2. | \barNumberCheck #70
    \stemDown b2. \pageBreak s2*9 \pageBreak s4*15 \pageBreak s1*6
    \break s2. | % 91
    R2.*7 | % 98
    r4 r8 \stemDown cis8 -- \stemDown b8. -- \stemDown a16 -- \pageBreak
    | % 99
    \stemDown a2 \stemDown gis8. \stemDown g16 | \barNumberCheck #100
    \stemDown g2 \stemDown g8. \stopTrillSpan _\ff \stemDown fis16 | % 101
    \stemDown fis4.. \stemDown eis16 \stemDown eis4 ~ | % 102
    \stemDown eis2 ~ \stemDown eis8 _\! _\mf r8 s1. | % 105
    R2.*2 \break | % 107
    R2. | % 108
    \stemDown d'2. ~ | % 109
    \stemDown d8 \stemDown cis8 \stemDown e4 s4*5 r4 r4 s1. \pageBreak
    s2*5 \stemDown a4 s4 \pageBreak | % 118
    \stemDown a2. | % 119
    \stemDown f4 \stemDown e4 \stemDown d4 s2. \pageBreak s4*9
    \pageBreak s1. | % 126
    \stemDown fis,8 s8 \stemDown cis'2 ~ | % 127
    \stemDown cis2. ~ | % 128
    \stemDown cis4 \stemDown cis2 ~ \pageBreak | % 129
    \stemDown cis2. ~ s4 \clef "bass" | \barNumberCheck #130
    \stemDown <cis cis,>4 ~ s4 | % 131
    \stemDown cis,2. ~ | % 132
    \stemDown cis4 \stemDown cis2 ~ | % 133
    \stemDown cis2. ~ | % 134
    \stemDown cis4 \stemDown cis2 ~ \pageBreak | % 135
    \stemDown cis4 \stemDown cis2 ~ _\f _\markup{ \small\italic {dim.} }
    \startTrillSpan | % 136
    \stemDown cis4 \stemDown cis2 ~ \stopTrillSpan _\mf _\> | % 137
    \stemDown cis8 r8 r4 r4 s4*27 \pageBreak | % 147
    \clef "treble" \stemDown fis2. ~ | % 148
    \stemDown fis2. ~ | % 149
    \stemDown fis2. ~ | \barNumberCheck #150
    \stemDown fis2. ~ | % 151
    \stemDown fis2. | % 152
    \stemDown fis2. ~ \pageBreak | % 153
    \stemDown fis2. ~ | % 154
    \stemDown fis2. ~ | % 155
    \stemDown fis4 ~ \stemDown fis8 _\! r8 r4 s4*9 \break s2*9 \break
    s4*21 \bar "|."
    }

PartPNineVoiceOne =  \relative d' {
    \clef "treble" \time 3/4 \key c \none \transposition f | % 1
    R2.*7 \pageBreak | % 8
    R2.*8 \break | % 16
    R2.*8 \pageBreak | % 24
    R2.*9 \break | % 33
    R2.*8 \pageBreak | % 41
    R2.*6 \break | % 47
    \stemUp <d d'>2 ( _\p _ "Hn." \stemUp <a a'>8 ) r8 | % 48
    R2. | % 49
    \stemUp <d d'>2 ( _\p \stemUp <a a'>8 ) r8 | \barNumberCheck #50
    R2. | % 51
    \stemUp <cis cis'>4 -- _\mp \stemUp <b b'>4 -- \stemUp <a a'>4 -- | % 52
    \stemUp <gis gis'>8 -- r8 r4 r4 \pageBreak | % 53
    \stemUp <e' e'>4 -- _\mf \stemUp <d d'>4 -- \stemUp <c c'>4 -- | % 54
    \stemUp <b b'>8 -- r8 r4 \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp <e e'>8 _\mf \stemUp <e e'>8 ~ ~ }
    | % 55
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    | % 56
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    | % 57
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    | % 58
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 }
    \pageBreak | % 59
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <e e'>8 \stemUp <e e'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <e e'>8 \stemUp <d d'>8 \stemUp <d d'>8 }
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemDown <fis fis'>8 \stemDown <fis fis'>8 ~ ~ }
    | \barNumberCheck #60
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <fis fis'>8 \stemDown <fis fis'>8 \stemDown <fis fis'>8
        ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <fis fis'>8 \stemDown <fis fis'>8 \stemDown <fis fis'>8
        }
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp <bes, bes'>8 \stemUp <bes bes'>8 ~ ~ }
    | % 61
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <bes bes'>8 \stemUp <bes bes'>8 \stemUp <bes bes'>8 ~ ~
        }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <bes bes'>8 \stemUp <b b'>8 \stemUp <b b'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <b b'>8 \stemUp <bes bes'>8 \stemUp <a a'>8 ~ ~ }
    | % 62
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <a a'>8 \stemUp <a a'>8 \stemUp <a a'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <a a'>8 \stemUp <gis gis'>8 \stemUp <gis gis'>8 }
    \stemUp <a a'>8 r8 | % 63
    \stemUp <d d'>2 ( _\f \stemUp <a a'>8 ) -\markup{ \italic {espress.}
        } r8 | % 64
    R2. \pageBreak | % 65
    \stemUp <d d'>2 ( \stemUp <a a'>8 ) r8 | % 66
    R2. | % 67
    \stemUp <cis cis'>4 -- _\f \stemUp <b b'>4 -- \stemUp <a a'>4 -- | % 68
    \stemUp gis'8 -- r8 r4 r4 | % 69
    \stemUp <e e'>4 -- _\f \stemUp <d d'>4 -- \stemUp <c c'>4 -- |
    \barNumberCheck #70
    \stemUp b'8 -- _\< r8 r4 r4 \pageBreak | % 71
    \stemDown <fis fis'>2. ~ ~ _\! _\fff | % 72
    \stemDown <fis fis'>8 r8 r4 r4 | % 73
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d g>8 \stemUp <d g>8 \stemUp <d g>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d g>8 \stemUp <d g>8 \stemUp <d g>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d g>8 \stemUp <d g>8 \stemUp <d g>8 ~ ~ }
    | % 74
    \stemUp <d g>8 r8 r4 r4 | % 75
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d d'>8 \stemUp <d d'>8 \stemUp <d d'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d d'>8 \stemUp <d d'>8 \stemUp <d d'>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp <d d'>8 \stemUp <d d'>8 \stemUp <d d'>8 ~ ~ }
    | % 76
    \stemUp <d d'>8 r8 r4 r4 \pageBreak | % 77
    \stemUp <d, d'>16 _\sempre _\fff r16 r8 r4 \stemUp <g' b>16 r16 r8 | % 78
    r4 \stemUp <g b>16 r16 r8 r4 | % 79
    \stemUp <g b>16 r16 r8 r4 r4 | \barNumberCheck #80
    R2. | % 81
    r8 \stemDown <g d'>8 _\fff r4 r4 ^\fermata \pageBreak | % 82
    R2.*8 \break | \barNumberCheck #90
    R2. | % 91
    r4 \stemUp cis2 ~ ^\mf ^\> | % 92
    \stemUp cis4 ~ \stemUp cis8 r8 ^\! r4 | % 93
    r4 \stemUp cis2 ~ ^\mf ^\> | % 94
    \stemUp cis4 ^\! ^\p \stemUp b2 ~ | % 95
    \stemUp b4 \stemUp a2 ~ ^\> | % 96
    \stemUp a4 ^\! ^\pp \stemUp gis2 ~ | % 97
    \stemUp gis4 \stemUp fis4.. ^\< \stemUp e16 | % 98
    \stemUp e4 ^\! ^\f \stemUp d8 r8 _\f r4 \pageBreak | % 99
    R2.*3 _\markup{ \small\italic {cresc.} } | % 102
    R2.*3 | % 105
    r4 \startTrillSpan _\> \stemUp cis'2 ~ ^\mf ^\> | % 106
    \stemUp cis4 ~ \stemUp cis8 r8 ^\! r4 \break | % 107
    r4 \stemUp cis2 ~ ^\mf | % 108
    \stemUp cis8 _\mf \stemUp b8 \stemUp d2 ~ | % 109
    \stemUp d8 \stemUp cis8 \stemUp e4 \stemDown <fis, fis'>4 ~ ~ |
    \barNumberCheck #110
    \stemDown <fis fis'>8 \stemDown <e e'>8 \stemDown <g g'>2 ~ ~
    _\markup{ \small\italic {cresc.} } \startTrillSpan | % 111
    \stemDown <g g'>8 \stemDown <fis fis'>8 \stemUp a4 \stemUp b4 | % 112
    \stemUp <dis, dis'>4 \stemUp <d d'>8 ( \stemUp <dis dis'>8 ) \stemUp
    <e e'>4 | % 113
    \stemUp <dis dis'>8 ( \stemUp <e e'>8 ) \stemUp <fis a>4 \stemUp <e
        gis>8 ( \stemUp <fis a>8 ) \pageBreak | % 114
    \stemUp <b, gis'>4 \stopTrillSpan -\markup{ \italic {pesante} }
    _\markup{ \small\italic {cresc.} } \startTrillSpan \stemUp <e gis>4
    \stemUp <b gis'>4 | % 115
    \stemUp <e a>4 \stemUp <dis a'>4 \stopTrillSpan _\fff \stemUp <fis
        a>4 | % 116
    \stemUp <g b>2. | % 117
    \stemUp <gis b>4 \stemUp a4 \stemUp <d, e>4 \pageBreak | % 118
    \stemUp e2. | % 119
    \stemUp gis2 \stemUp b,4 | \barNumberCheck #120
    \stemUp <cis fis>2. \pageBreak | % 121
    \stemUp <d f>4 \stemUp <cis f>4 \stemUp <b gis'>4 | % 122
    \stemUp <a cis>2. | % 123
    \stemDown <e'' fis>2. \pageBreak | % 124
    \stemDown <b fis'>2. | % 125
    \stemDown <d fis>2 \stemDown <a d>4 | % 126
    \stemUp fis8 r8 r4 _\ff _\ gestopft r4 | % 127
    R2. | % 128
    \stemUp cis'8 ~ -> ^\ff \stemUp cis16 r16 r4 r4 \pageBreak | % 129
    R2. | \barNumberCheck #130
    \stemUp cis8 ~ -> \stemUp cis16 r16 \clef "bass" r4 r4 | % 131
    R2. | % 132
    \stemUp gis,8 ~ -> \stemUp gis16 r16 r4 r4 | % 133
    R2. | % 134
    \stemUp gis8 ~ -> \stemUp gis16 r16 r4 r4 \pageBreak | % 135
    R2.*2 | % 137
    R2.*10 \pageBreak | % 147
    \clef "treble" R2. -\markup{ \italic {nicht gest.} } | % 148
    R2.*4 | % 152
    \stemUp fis'2. _\! _\p _\p _\< _\! _\mf ^\sf _\mf ^\> \pageBreak | % 153
    \stemUp eis2 ( ^\! ^\sf ^\> \stemUp fis4 ) ^\! | % 154
    R2. | % 155
    R2.*4 \break | % 159
    R2.*6 \break | % 165
    R2.*7 \bar "|."
    _\> }

PartPNineVoiceTwo =  \relative a' {
    \clef "treble" \time 3/4 \key c \none \transposition f | % 1
     \once \override NoteHead.style = ##f \stemUp a2. s2*9 \pageBreak
    s1*6 \break s1*6 \pageBreak s4*27 \break s1*6 \pageBreak s2*9 \break
    s2*9 \pageBreak s2*9 \pageBreak s2*9 \pageBreak s4*9 | % 68
    \stemDown gis,2. s2. | \barNumberCheck #70
    \stemDown b2. \pageBreak s2*9 \pageBreak s4*15 \pageBreak s1*6
    \break s2. | % 91
    R2.*7 | % 98
    r4 r8 \stemDown cis8 -- \stemDown b8. -- \stemDown a16 -- \pageBreak
    | % 99
    \stemDown a2 \stemDown gis8. \stemDown g16 | \barNumberCheck #100
    \stemDown g2 \stemDown g8. \stopTrillSpan _\ff \stemDown fis16 | % 101
    \stemDown fis4.. \stemDown eis16 \stemDown eis4 ~ | % 102
    \stemDown eis2 ~ \stemDown eis8 _\! _\mf r8 s1. | % 105
    R2.*2 \break | % 107
    R2. | % 108
    \stemDown d'2. ~ | % 109
    \stemDown d8 \stemDown cis8 \stemDown e4 s4*5 r4 r4 s1. \pageBreak
    s2*5 \stemDown a4 s4 \pageBreak | % 118
    \stemDown a2. | % 119
    \stemDown f4 \stemDown e4 \stemDown d4 s2. \pageBreak s4*9
    \pageBreak s1. | % 126
    \stemDown fis,8 s8 \stemDown cis'2 ~ | % 127
    \stemDown cis2. ~ | % 128
    \stemDown cis4 \stemDown cis2 ~ \pageBreak | % 129
    \stemDown cis2. ~ s4 \clef "bass" | \barNumberCheck #130
    \stemDown <cis cis,>4 ~ s4 | % 131
    \stemDown cis,2. ~ | % 132
    \stemDown cis4 \stemDown cis2 ~ | % 133
    \stemDown cis2. ~ | % 134
    \stemDown cis4 \stemDown cis2 ~ \pageBreak | % 135
    \stemDown cis4 \stemDown cis2 ~ _\f _\markup{ \small\italic {dim.} }
    \startTrillSpan | % 136
    \stemDown cis4 \stemDown cis2 ~ \stopTrillSpan _\mf _\> | % 137
    \stemDown cis8 r8 r4 r4 s4*27 \pageBreak | % 147
    \clef "treble" \stemDown fis2. ~ | % 148
    \stemDown fis2. ~ | % 149
    \stemDown fis2. ~ | \barNumberCheck #150
    \stemDown fis2. ~ | % 151
    \stemDown fis2. | % 152
    \stemDown fis2. ~ \pageBreak | % 153
    \stemDown fis2. ~ | % 154
    \stemDown fis2. ~ | % 155
    \stemDown fis4 ~ \stemDown fis8 _\! r8 r4 s4*9 \break s2*9 \break
    s4*21 \bar "|."
    }

PartPOneZeroVoiceOne =  \relative b' {
    \clef "treble" \time 3/4 \key c \none \transposition a | % 1
    R2.*7 \pageBreak | % 8
    R2.*8 \break | % 16
    R2.*8 \pageBreak | % 24
    R2.*9 \break | % 33
    R2.*8 \pageBreak | % 41
    R2.*6 \break | % 47
    R2.*5 | % 52
    \stemUp b4 _\mp \stemUp a4 \stemUp g4 \pageBreak | % 53
    \stemUp f8 r8 r4 r4 | % 54
    \stemUp d'4 -- _\mf \stemUp c8 -- \stemUp bes8 -- \stemUp a8 --
    \stemUp as8 -- | % 55
    \stemUp g8 -- r8 r4 r4 | % 56
    R2.*3 \pageBreak | % 59
    R2.*4 | % 63
    r4 r4 \stemUp f4 -- _\mf ^ "a 2" _\< | % 64
    \stemUp f4 -- _\! _\> \stemUp e4 -- _\! \stemUp d4 -- \pageBreak | % 65
    \stemUp c8 -- r8 r4 \stemUp f4 -- _\< | % 66
    \stemUp f4 -- _\! _\> \stemUp e4 -- _\! \stemUp es4 -- | % 67
    \stemUp d4 ~ \stemUp d8 r8 r4 | % 68
    \stemUp b'4 -- _\f \stemUp a4 -- \stemUp g4 -- | % 69
    \stemUp f4 ~ \stemUp f8 r8 r4 | \barNumberCheck #70
    \stemDown d'4 -- _\ff ^ "a 2" \stemDown c4 -- \stemDown bes4 --
    \pageBreak | % 71
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp a8 \stemUp a8 ~ }
    | % 72
    \stemUp a8 r8 r4 r4 | % 73
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <es' g>8 \stemDown <es g>8 \stemDown <es g>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <es g>8 \stemDown <es g>8 \stemDown <es g>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <es g>8 \stemDown <es g>8 \stemDown <es g>8 ~ ~ }
    | % 74
    \stemDown <es g>8 r8 r4 r4 | % 75
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <bes es>8 \stemDown <bes es>8 \stemDown <bes es>8 ~ ~
        }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <bes es>8 \stemDown <bes es>8 \stemDown <bes es>8 ~ ~
        }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <bes es>8 \stemDown <bes es>8 \stemDown <bes es>8 ~ ~
        }
    | % 76
    \stemDown <bes es>8 r8 r4 r4 \pageBreak | % 77
    \stemDown <es g>16 _\sempre _\fff r16 r8 r4 \stemDown <es g>16 r16 r8
    | % 78
    r4 \stemDown <es g>16 r16 r8 r4 | % 79
    \stemDown <es g>16 r16 r8 r4 r4 | \barNumberCheck #80
    R2. | % 81
    r8 \stemDown <es g>8 _\fff r4 r4 ^\fermata \pageBreak | % 82
    R2.*8 \break | \barNumberCheck #90
    R2.*9 \pageBreak | % 99
    R2.*8 \break | % 107
    R2.*4 | % 111
    r4 \stemUp f4 ^\mf \stemUp g4 | % 112
    \stemDown <g, g'>2 _\mf _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemDown <fis fis'>8 ( \stemDown <g g'>8 ) | % 113
    \stemDown <g g'>4 \stemDown <bes bes'>2 \stopTrillSpan _\f
    \pageBreak | % 114
    \stemDown <g e'>4 -\markup{ \italic {pesante} } _\markup{
        \small\italic {cresc.} } \startTrillSpan \stemDown <c e>4
    \stemDown <g e'>4 | % 115
    \stemDown <c f>4 \stemDown <b f'>4 \stopTrillSpan _\fff \stemDown <d
        f>4 | % 116
    \stemDown <es g>2. | % 117
    \stemDown <e g>4 \stemUp f4 \stemDown <bes, c>4 \pageBreak | % 118
    \stemUp c2. | % 119
    \stemUp e2 \stemUp g,4 | \barNumberCheck #120
    \stemDown <a d>2. \pageBreak | % 121
    \stemDown <bes cis>4 \stemDown <a cis>4 \stemDown <g e'>4 | % 122
    \stemDown b4 ^ "a 2" \stemDown cis4 \stemDown d4 | % 123
    \stemDown e4 \stemDown f4 \stemDown fis4 \pageBreak | % 124
    \stemDown g4 \stemDown a4 \stemDown bes4 | % 125
    R2. | % 126
    \stemUp <f, a>8 r8 r4 r4 | % 127
    R2.*2 \pageBreak | % 129
    R2.*6 \pageBreak | % 135
    R2.*12 \pageBreak | % 147
    R2.*6 \pageBreak | % 153
    R2.*6 \break | % 159
    R2.*6 \break | % 165
    R2.*7 \bar "|."
    }

PartPOneZeroVoiceTwo =  \relative f' {
    \clef "treble" \time 3/4 \key c \none \transposition a | % 1
     \once \override NoteHead.style = ##f \stemUp f2. s2*9 \pageBreak
    s1*6 \break s1*6 \pageBreak s4*27 \break s1*6 \pageBreak s2*9 \break
    s4*15 | % 52
    R2. \pageBreak | % 53
    R2.*3 s4*9 \pageBreak s2*9 \pageBreak s1. | % 67
    \stemDown d8 -- r8 r4 r4 | % 68
    \stemDown b'4 -- \stemDown a4 -- \stemDown g4 -- | % 69
    \stemDown f8 -- r8 r4 r4 s2. \pageBreak s2*9 \pageBreak s4*15
    \pageBreak s1*6 \break s4*27 \pageBreak s1*6 \break s1*3 | % 111
    R2. s1. \pageBreak s2*5 \stemDown f'4 s4 \pageBreak | % 118
    \stemDown f2. | % 119
    \stemDown des4 \stemDown c4 \stemDown bes4 s2. \pageBreak s4*9
    \pageBreak s4*15 \pageBreak s2*9 \pageBreak s1*9 \pageBreak s2*9
    \pageBreak s2*9 \break s2*9 \break s4*21 \bar "|."
    }

PartPOneOneVoiceOne =  \relative d {
    \clef "tenor" \time 3/4 \key d \major | % 1
    R2.*7 \pageBreak _ "Trombone" | % 8
    R2.*8 \break | % 16
    R2.*8 \pageBreak | % 24
    R2.*9 \break | % 33
    R2.*8 \pageBreak | % 41
    R2.*6 \break | % 47
    r4 _ "Tbn." r4 \stemUp <d d'>4 -- _\p ^\markup{ \italic {con
            sentimento} } _\< | % 48
    \stemUp <d d'>4 -- _\! _\> \stemUp <cis cis'>4 -- _\! \stemUp <b b'>4
    -- | % 49
    \stemUp <a a'>8 -- r8 r4 \stemUp <d d'>4 -- _\< | \barNumberCheck
    #50
    \stemUp <d d'>4 -- _\! _\> \stemUp <cis cis'>4 -- _\! \stemUp <c c'>4
    -- | % 51
    \stemUp <b b'>8 -- r8 r4 r4 | % 52
    R2. \pageBreak | % 53
    R2. _ "Tbn." | % 54
    \stemUp b'4 -- _\mp _\mf \stemUp a8 -- \stemUp g8 -- \stemUp fis8 --
    \stemUp f8 -- | % 55
    \stemUp e8 -- r8 r4 r4 | % 56
    R2.*3 \pageBreak | % 59
    R2.*4 _ "Tbn." | % 63
    r4 r4 \stemUp d4 -- _\mf ^ "a 2" -\markup{ \italic {espress.} } _\<
    | % 64
    \stemUp d4 -- _\! _\> \stemUp cis4 -- _\! \stemUp b4 -- \pageBreak | % 65
    \stemUp a8 -- _ "Tbn." r8 r4 \stemUp d4 -- _\< | % 66
    \stemUp d4 -- _\! _\> \stemUp cis4 -- _\! \stemUp c4 -- | % 67
    \stemUp b8 -- r8 r4 r4 | % 68
    \stemUp gis'4 -- _\f \stemUp fis4 -- \stemUp e4 -- | % 69
    \stemUp d8 -- r8 r4 r4 | \barNumberCheck #70
    \stemDown b'4 -- _\ff ^ "a 2" \stemDown a4 -- \stemUp g4 --
    \pageBreak | % 71
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis8 _\ff _ "Tbn." \stemUp fis8 \stemUp fis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis8 \stemUp fis8 \stemUp fis8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis8 \stemUp fis8 \stemUp fis8 ~ }
    | % 72
    \stemUp fis8 r8 r4 r4 | % 73
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <c' e>8 \stemDown <c e>8 \stemDown <c e>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <c e>8 \stemDown <c e>8 \stemDown <c e>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <c e>8 \stemDown <c e>8 \stemDown <c e>8 ~ ~ }
    | % 74
    \stemDown <c e>8 r8 r4 r4 | % 75
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g c>8 \stemDown <g c>8 \stemDown <g c>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g c>8 \stemDown <g c>8 \stemDown <g c>8 ~ ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown <g c>8 \stemDown <g c>8 \stemDown <g c>8 ~ ~ }
    | % 76
    \stemDown <g c>8 r8 r4 r4 \pageBreak | % 77
    \stemDown <c e>16 _\sempre _\fff _ "Tbn." r16 r8 r4 \stemDown <c e>16
    r16 r8 | % 78
    r4 \stemDown <c e>16 r16 r8 r4 | % 79
    \stemDown <c e>16 r16 r8 r4 r4 | \barNumberCheck #80
    R2. | % 81
    r8 \stemDown <g e'>8 _\fff r4 r4 ^\fermata \pageBreak | % 82
    R2.*8 \break | \barNumberCheck #90
    R2.*9 \pageBreak | % 99
    R2.*8 \break | % 107
    R2.*7 \pageBreak | % 114
    R2.*4 \pageBreak _ "Tbn." | % 118
    R2.*2 _ "Tbn." | \barNumberCheck #120
    r4 \stemUp cis4 ^\ff ^\ marcato e pesante \stemUp d4 \pageBreak | % 121
    \stemUp e4 _ "Tbn." \stemUp fis4 \stemUp g4 | % 122
    \stemDown <d fis>2. | % 123
    \stemDown <a b>2. \pageBreak | % 124
    \stemUp <e b'>2. _ "Tbn." | % 125
    \stemDown <g b>2 \stemUp <d g>4 | % 126
    \stemUp <d fis>8 r8 r4 r4 | % 127
    R2.*2 \pageBreak | % 129
    R2.*6 \pageBreak | % 135
    R2.*2 _ "Tbn." | % 137
    r4 \stemDown <b' d>2 _\p _\< | % 138
    \stemDown <b d>2. ( _\! _\mp _\> | % 139
    \stemDown <a cis>8 ) _\! _\p r8 \stemDown <a c>2 _\p _\< |
    \barNumberCheck #140
    \stemDown <a c>2. ( _\! _\mp _\> | % 141
    \stemDown <g b>8 ) _\! _\p r8 \stemDown <g b>2 _\pp _\< | % 142
    \stemDown <g b>2. _\! _\p _\> | % 143
    \stemUp <fis ais>2 ~ ~ _\! _\pp \stemUp <fis ais>8 r8 | % 144
    \stemUp <d b'>2 ~ ~ _\ppp \stemUp <d b'>8 r8 | % 145
    \stemUp <cis g'>2 ~ ~ _\pppp \stemUp <cis g'>8 r8 | % 146
    \stemUp <cis fis>2 ~ ~ _\ppppp \stemUp <cis fis>8 r8 \pageBreak | % 147
    R2. _ "Tbn." | % 148
    \stemUp <e g>2. -> _\mf | % 149
    \stemUp <d fis>2. | \barNumberCheck #150
    \stemUp <e g>2. -> | % 151
    \stemUp <d fis>2. | % 152
    R2. \pageBreak | % 153
    R2.*6 \break | % 159
    R2.*6 \break | % 165
    R2.*7 \bar "|."
    }

PartPOneOneVoiceTwo =  \relative d' {
    \clef "tenor" \time 3/4 \key d \major | % 1
     \once \override NoteHead.style = ##f \stemDown d2. s2*9 \pageBreak
    s1*6 \break s1*6 \pageBreak s4*27 \break s1*6 \pageBreak s2*9 \break
    s4*15 | % 52
    \stemDown gis,4 -- \stemDown fis4 -- \stemDown e4 -- \pageBreak | % 53
    \stemDown d8 r8 r4 r4 | % 54
    R2.*2 s4*9 \pageBreak s2*9 \pageBreak s1. | % 67
    \stemDown b2. | % 68
    \stemDown gis'4 -- \stemDown fis4 -- \stemDown e4 -- | % 69
    \stemDown d2. s2. \pageBreak s2*9 \pageBreak s4*15 \pageBreak s1*6
    \break s4*27 \pageBreak s1*6 \break s4*21 \pageBreak s2. | % 115
    r4 r4 \stemDown e,4 _\ff -\markup{ \italic {marcato e pesante} } | % 116
    \stemDown fis4 \stemDown gis4 \stemDown a4 | % 117
    \stemDown ais4 \stemDown b4 \stemDown cis4 \pageBreak | % 118
    \stemDown d4 \stemDown e4 \stemDown f4 | % 119
    \stemDown g4 \stemDown a4 \stemDown ais4 | \barNumberCheck #120
    \stemDown b4 \stemDown cis4 \stemDown d4 \pageBreak | % 121
    \stemDown e4 \stemDown fis4 \stemDown g4 s1. \pageBreak s4*15
    \pageBreak s2*9 \pageBreak s1*9 \pageBreak s2*9 \pageBreak s2*9
    \break s2*9 \break s4*21 \bar "|."
    }

PartPOneTwoVoiceOne =  \relative fis, {
    \clef "bass" \time 3/4 \key d \major | % 1
    R2.*7 \pageBreak | % 8
    R2.*8 \break | % 16
    R2.*8 \pageBreak | % 24
    R2.*9 \break | % 33
    R2.*8 \pageBreak | % 41
    R2.*6 \break | % 47
    R2.*6 \pageBreak | % 53
    R2.*6 \pageBreak | % 59
    R2.*3 | % 62
    r2 \stemUp fis4 -- _\mf | % 63
    \stemUp e2 \stemUp eis4 -- | % 64
    \stemUp fis2. \pageBreak | % 65
    \stemUp e2 \stemUp eis4 | % 66
    \stemUp fis2. | % 67
    \stemUp g2 _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp gis4 -- | % 68
    \stemUp a2 \stemUp ais4 -- | % 69
    \stemUp b2 \stemUp b4 -- | \barNumberCheck #70
    \stemUp cis2. \stopTrillSpan _\f _\< \pageBreak | % 71
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 _\! _\ff \stemDown d8 \stemDown d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 ~ }
    | % 72
    \stemDown d8 r8 r4 r4 | % 73
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 ~ }
    | % 74
    \stemUp c8 r8 r4 r4 | % 75
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 ~ }
    | % 76
    \stemDown e8 r8 r4 r4 \pageBreak | % 77
    \stemDown g16 _\sempre _\fff r16 r8 r4 \stemUp c,16 r16 r8 | % 78
    r4 \stemDown e16 r16 r8 r4 | % 79
    \stemDown g16 r16 r8 r4 r4 | \barNumberCheck #80
    R2. | % 81
    \stemUp c,8 _\fff \stemUp c8 r4 r4 ^\fermata \pageBreak | % 82
    R2.*8 \break | \barNumberCheck #90
    R2.*9 \pageBreak | % 99
    R2.*8 \break | % 107
    R2.*7 \pageBreak | % 114
    R2. | % 115
    r4 r4 \stemUp e,4 _\ff -\markup{ \italic {marcato e pesante} } | % 116
    \stemUp fis4 \stemUp gis4 \stemUp a4 | % 117
    \stemUp ais4 \stemUp b4 \stemUp cis4 \pageBreak | % 118
    \stemDown d4 \stemDown e4 \stemDown f4 | % 119
    \stemDown g4 \stemDown a4 \stemDown ais4 | \barNumberCheck #120
    \stemDown b4 r4 r4 \pageBreak | % 121
    R2.*2 | % 123
    \stemUp b,2. ~ \pageBreak | % 124
    \stemUp b2. | % 125
    \stemUp b2. | % 126
    \stemUp fis2. ~ _\> | % 127
    \stemUp fis2. ~ _\! _\mf | % 128
    \stemUp fis2. ~ \pageBreak | % 129
    \stemUp fis2. ~ _ "Tbn." _\> | \barNumberCheck #130
    \stemUp fis8 _\! _\p r8 r4 r4 | % 131
    R2.*4 \pageBreak | % 135
    R2.*2 | % 137
    r4 \stemDown fis'2 _\p _\< | % 138
    \stemDown f2 _\! _\mp _\> \stemDown e4 ~ | % 139
    \stemDown e8 _\! _\p r8 \stemDown e2 _\p _\< | \barNumberCheck #140
    \stemDown es2 _\! _\mp _\> \stemDown d4 ~ | % 141
    \stemDown d8 _\! _\p r8 \stemDown d2 _\pp _\< | % 142
    \stemUp cis2. _\! _\p _\> | % 143
    \stemUp cis2 ~ _\! _\pp \stemUp cis8 r8 | % 144
    \stemUp b2 ~ _\ppp \stemUp b8 r8 | % 145
    \stemUp b2 ~ _\pppp \stemUp b8 r8 | % 146
    \stemUp ais2 ~ _\ppppp \stemUp ais8 r8 \pageBreak | % 147
    R2.*6 \pageBreak | % 153
    R2.*6 \break | % 159
    R2.*6 \break | % 165
    R2.*7 \bar "|."
    }

PartPOneTwoVoiceTwo =  \relative d {
    \clef "bass" \time 3/4 \key d \major | % 1
     \once \override NoteHead.style = ##f \stemDown d2. s2*9 \pageBreak
    s1*6 \break s1*6 \pageBreak s4*27 \break s1*6 \pageBreak s2*9 \break
    s2*9 \pageBreak s2*9 \pageBreak s2*9 \pageBreak s2*9 \pageBreak s2*9
    \pageBreak s4*15 \pageBreak s1*6 \break s4*27 \pageBreak s1*6 \break
    s4*21 \pageBreak s1*3 \pageBreak s4*9 \pageBreak s4*9 \pageBreak
    s4*15 \pageBreak s2*9 \pageBreak s1*9 \pageBreak s2*9 \pageBreak
    s2*9 \break s2*9 \break s4*21 \bar "|."
    }

PartPOneThreeVoiceOne =  \relative gis,, {
    \clef "bass" \time 3/4 \key d \major | % 1
    R2.*7 \pageBreak | % 8
    R2.*8 \break | % 16
    R2.*8 \pageBreak | % 24
    R2.*9 \break | % 33
    R2.*8 \pageBreak | % 41
    R2.*6 \break | % 47
    R2.*6 \pageBreak | % 53
    R2.*6 \pageBreak | % 59
    R2.*6 \pageBreak | % 65
    R2.*2 | % 67
    r2 \stemUp gis4 -- _\f | % 68
    \stemUp a2 _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp ais4 -- | % 69
    \stemUp b2 \stemUp b4 -- | \barNumberCheck #70
    \stemUp cis2. \stopTrillSpan _\f _\< \pageBreak | % 71
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp d8 _\! _\ff \stemUp d8 \stemUp d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp d8 \stemUp d8 \stemUp d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp d8 \stemUp d8 \stemUp d8 ~ }
    | % 72
    \stemUp d8 r8 r4 r4 | % 73
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 ~ }
    | % 74
    \stemUp c8 r8 r4 r4 | % 75
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 \stemUp e8 \stemUp e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 \stemUp e8 \stemUp e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 \stemUp e8 \stemUp e8 ~ }
    | % 76
    \stemUp e8 r8 r4 r4 \pageBreak | % 77
    \stemUp g16 _\sempre _\fff r16 r8 r4 \stemUp c16 r16 r8 | % 78
    r4 \stemDown e16 r16 r8 r4 | % 79
    \stemDown g16 r16 r8 r4 r4 | \barNumberCheck #80
    R2. | % 81
    \stemUp c,,8 _\fff \stemUp c'8 r4 r4 ^\fermata \pageBreak | % 82
    R2.*8 \break | \barNumberCheck #90
    R2.*9 \pageBreak | % 99
    R2.*8 \break | % 107
    R2.*7 \pageBreak | % 114
    \stemUp bes4 _\f _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp a4 \stemUp g4 | % 115
    \stemUp f4 \stemUp e2 ~ \stopTrillSpan _\ff | % 116
    \stemUp e2. ~ | % 117
    \stemUp e2. ~ \pageBreak | % 118
    \stemUp e2. ~ | % 119
    \stemUp e2. ~ | \barNumberCheck #120
    \stemUp e2. ~ \pageBreak | % 121
    \stemUp e2. ~ | % 122
    \stemUp e2. ~ | % 123
    \stemUp e2. ~ \pageBreak | % 124
    \stemUp e2. | % 125
    \stemUp eis2. | % 126
    \stemUp fis2. ~ _\> | % 127
    \stemUp fis2. ~ _\! _\mf | % 128
    \stemUp fis2. ~ \pageBreak | % 129
    \stemUp fis2. ~ _\> | \barNumberCheck #130
    \stemUp fis8 _\! _\p r8 r4 r4 | % 131
    R2.*4 \pageBreak | % 135
    R2.*2 | % 137
    r4 \stemUp fis2 _\p _\< | % 138
    \stemUp g2 _\! _\mp _\> \stemUp gis4 ( | % 139
    \stemUp a8 ) _\! _\p r8 \stemUp e2 _\p _\< | \barNumberCheck #140
    \stemUp f2 _\! _\mp _\> \stemUp fis4 ( | % 141
    \stemUp g8 ) _\! _\p r8 \stemUp d2 _\pp _\< | % 142
    \stemUp e2 ( _\! _\p _\> \stemUp eis4 ) | % 143
    \stemUp fis2 ~ _\! _\pp \stemUp fis8 r8 | % 144
    \stemUp g2 ~ _\ppp \stemUp g8 r8 | % 145
    \stemUp e2 ~ _\pppp \stemUp e8 r8 | % 146
    \stemUp fis2 ~ _\ppppp \stemUp fis8 r8 \pageBreak | % 147
    R2.*6 \pageBreak | % 153
    R2.*6 \break | % 159
    R2.*6 \break | % 165
    R2.*7 \bar "|."
    }

PartPOneThreeVoiceTwo =  \relative d {
    \clef "bass" \time 3/4 \key d \major | % 1
     \once \override NoteHead.style = ##f \stemDown d2. s2*9 \pageBreak
    s1*6 \break s1*6 \pageBreak s4*27 \break s1*6 \pageBreak s2*9 \break
    s2*9 \pageBreak s2*9 \pageBreak s2*9 \pageBreak s2*9 \pageBreak s2*9
    \pageBreak s4*15 \pageBreak s1*6 \break s4*27 \pageBreak s1*6 \break
    s4*21 \pageBreak s1*3 \pageBreak s4*9 \pageBreak s4*9 \pageBreak
    s4*15 \pageBreak s2*9 \pageBreak s1*9 \pageBreak s2*9 \pageBreak
    s2*9 \break s2*9 \break s4*21 \bar "|."
    }

PartPOneFourVoiceOne =  \relative d {
    \clef "bass" \time 3/4 \key c \none | % 1
    R2.*7 \pageBreak | % 8
    R2.*8 \break | % 16
    R2.*8 \pageBreak | % 24
    R2.*9 \break | % 33
    R2.*8 \pageBreak | % 41
    R2.*6 \break | % 47
    R2.*6 \pageBreak | % 53
    R2.*6 \pageBreak | % 59
    R2.*6 \pageBreak | % 65
    R2.*6 \pageBreak | % 71
    \stemDown d2. :64 _\ff | % 72
    \stemDown d8 r8 r4 r4 | % 73
    \stemUp c2. :32 | % 74
    \stemUp c8 r8 r4 r4 | % 75
    \stemUp c2. :32 | % 76
    \stemUp c8 r8 r4 r4 \pageBreak | % 77
    R2.*4 | % 81
    \stemUp c8 _\fff r8 r4 r4 ^\fermata \pageBreak | % 82
    R2.*8 \break | \barNumberCheck #90
    R2.*9 \pageBreak | % 99
    R2.*8 \break | % 107
    R2.*7 \pageBreak | % 114
    R2. | % 115
    r4 \stemDown e2 :32 _\ff | % 116
    \stemDown e2. :32 | % 117
    \stemDown e2. :32 \pageBreak | % 118
    \stemDown e2. :32 | % 119
    \stemDown e2. :32 | \barNumberCheck #120
    \stemDown e2. :32 \pageBreak | % 121
    \stemDown e2. :32 | % 122
    \stemDown e2. :32 | % 123
    \stemDown e2. :32 \pageBreak | % 124
    \stemDown e2. :32 | % 125
    \stemUp b2. :32 | % 126
    \stemUp fis2. :32 _\> | % 127
    \stemUp fis2. :32 _\! _\mf | % 128
    \stemUp fis2. :32 \pageBreak | % 129
    \stemUp fis2. :32 | \barNumberCheck #130
    \stemUp fis2. :32 _\sempre _\mf | % 131
    \stemUp fis2. :32 | % 132
    \stemUp fis2. :32 | % 133
    \stemUp fis2. :32 | % 134
    \stemUp fis2. :32 _\markup{ \small\italic {dim.} } \startTrillSpan
    \pageBreak | % 135
    \stemUp fis2. :32 | % 136
    \stemUp fis2. :32 | % 137
    \stemUp fis8 \stopTrillSpan _\p r8 r4 r4 | % 138
    R2.*9 \pageBreak | % 147
    R2.*6 \pageBreak | % 153
    R2.*6 \break | % 159
    R2.*6 \break | % 165
    R2.*7 \bar "|."
    }

PartPOneFourVoiceTwo =  \relative d {
    \clef "bass" \time 3/4 \key c \none | % 1
     \once \override NoteHead.style = ##f \stemDown d2. s2*9 \pageBreak
    s1*6 \break s1*6 \pageBreak s4*27 \break s1*6 \pageBreak s2*9 \break
    s2*9 \pageBreak s2*9 \pageBreak s2*9 \pageBreak s2*9 \pageBreak s2*9
    \pageBreak s4*15 \pageBreak s1*6 \break s4*27 \pageBreak s1*6 \break
    s4*21 \pageBreak s1*3 \pageBreak s4*9 \pageBreak s4*9 \pageBreak
    s4*15 \pageBreak s2*9 \pageBreak s1*9 \pageBreak s2*9 \pageBreak
    s2*9 \break s2*9 \break s4*21 \bar "|."
    }

PartPOneFiveVoiceOne =  \relative e' {
    \clef "percussion" \time 3/4 \key c \major \stopStaff \override
    Staff.StaffSymbol.line-count = #1 \startStaff | % 1
    R2.*7 \pageBreak | % 8
    R2.*8 \break | % 16
    R2.*8 \pageBreak | % 24
    R2.*9 \break | % 33
    R2.*8 \pageBreak | % 41
    R2.*6 \break | % 47
    R2.*6 \pageBreak | % 53
    R2.*6 \pageBreak | % 59
    R2.*6 \pageBreak | % 65
    R2.*6 \pageBreak | % 71
    R2.*6 \pageBreak | % 77
    R2.*5 \pageBreak | % 82
    R2.*8 \break | \barNumberCheck #90
    R2.*9 \pageBreak | % 99
    R2.*8 \break | % 107
    R2.*7 \pageBreak | % 114
    R2.*4 \pageBreak | % 118
    R2.*3 \pageBreak | % 121
    R2.*3 \pageBreak | % 124
    R2.*5 \pageBreak | % 129
    R2.*6 \pageBreak | % 135
    R2.*2 | % 137
    \stemUp e2. ~ _\p | % 138
    \stemUp e2. ~ | % 139
    \stemUp e2. ~ | \barNumberCheck #140
    \stemUp e2. ~ | % 141
    \stemUp e8 r8 r4 r4 | % 142
    R2.*5 \pageBreak | % 147
    R2.*6 \pageBreak | % 153
    R2.*6 \break | % 159
    R2.*6 \break | % 165
    R2.*7 \bar "|."
    }

PartPOneFiveVoiceTwo =  \relative e' {
    \clef "percussion" \time 3/4 \key c \major \stopStaff \override
    Staff.StaffSymbol.line-count = #1 \startStaff | % 1
     \once \override NoteHead.style = ##f \stemDown e2. s2*9 \pageBreak
    s1*6 \break s1*6 \pageBreak s4*27 \break s1*6 \pageBreak s2*9 \break
    s2*9 \pageBreak s2*9 \pageBreak s2*9 \pageBreak s2*9 \pageBreak s2*9
    \pageBreak s4*15 \pageBreak s1*6 \break s4*27 \pageBreak s1*6 \break
    s4*21 \pageBreak s1*3 \pageBreak s4*9 \pageBreak s4*9 \pageBreak
    s4*15 \pageBreak s2*9 \pageBreak s1*9 \pageBreak s2*9 \pageBreak
    s2*9 \break s2*9 \break s4*21 \bar "|."
    }

PartPOneSixVoiceOne =  \relative b' {
    \clef "treble" \time 3/4 \key d \major | % 1
    \stemDown b4 -- _\f -\markup{ \italic {largamente} } \stemDown e8 (
    \stemDown gis,8 ) \stemUp cis8. ( _\> \stemUp f,16 ) | % 2
    \stemDown cis'2 ~ _\! _\mf _\> \stemDown cis8 _\! _\p r8 | % 3
    \stemDown b4 -- _\f \stemDown e8 ( \stemDown gis,8 ) \stemUp cis8. (
    _\> \stemUp f,16 ) | % 4
    \stemDown d'8 ( -> _\! _\mf _\> \stemDown cis8 ~ \stemDown cis4 ~
    \stemDown cis8 ) r8 _\! | % 5
    \stemUp g4. ( _\p \stemUp g8 ) -- \stemUp g8. ( -- \stemUp a16 ) --
    | % 6
    \stemUp fis2 r4 | % 7
    \stemDown b4. ( _\mp \stemDown b8 ) -- \stemDown b8. ( -- \stemDown
    cis16 ) -- \pageBreak | % 8
    \stemUp a2 r4 | % 9
    \stemDown d4. ( _\mf _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemDown e8 ) -- \stemDown cis4 -- |
    \barNumberCheck #10
    \stemDown fis4. ( \stemDown gis8 ) -- \stemDown e4 -- | % 11
    \stemDown <cis a'>4. ( \stemDown b'8 ) -- \stemDown cis4 -- | % 12
    \stemDown <fis, d'>2. ~ ~ \stopTrillSpan _\ff _\> | % 13
    \stemDown <fis d'>8 _\! _\mf r8 \stemDown d4 ~ _\f _\> \stemDown d8
    r8 _\! | % 14
    \stemDown b4 ~ _\mf _\> \stemDown b8 r8 _\! \stemUp dis,4 ( _\mp | % 15
    \stemUp b8 ) r8 \stemUp b4 ( _\p \stemUp g8 ) r8 \break | % 16
    \stemUp g2. ~ _\p _\> | % 17
    \stemUp g2 _\! _\pp \stemUp e'4 ~ _\pp _\< | % 18
    \stemUp e2 ~ _\! _\> \stemUp e8 _\! _\ppp r8 | % 19
    r4 r16 \stemUp e16 ( _\p _\< \stemUp cis16 \stemUp a'16 ) \stemUp f16
    ( \stemUp cis'16 ) \stemUp gis16 ( \stemUp e'16 ) | \barNumberCheck
    #20
    \stemDown b4 -- _\! _\f \stemDown e8 ( \stemDown gis,8 ) \stemUp cis8.
    ( _\> \stemUp f,16 ) | % 21
    \stemDown cis'2 ~ _\! _\mf _\> \stemDown cis8 _\! _\p r8 | % 22
    \stemDown b4 -- _\f \stemDown e8 ( \stemDown gis,8 ) \stemUp cis8. (
    _\> \stemUp f,16 ) | % 23
    \stemDown d'8 ( -> _\! _\mf _\> \stemDown cis8 ~ \stemDown cis4 ~
    \stemDown cis8 ) r8 _\! \pageBreak | % 24
    \stemUp g4. ( _\p \stemUp g8 ) -- \stemUp g8. ( -- \stemUp a16 ) --
    | % 25
    \stemUp fis2 ~ \stemUp fis8 r8 | % 26
    \stemUp e4. ( _\pp \stemUp e8 ) -- \stemUp e8. ( -- \stemUp fis16 )
    -- | % 27
    \stemUp d2 ~ \stemUp d8 r8 | % 28
    \stemUp cis4. ( _\pp _\< \stemUp cis8 ) -- \stemUp cis8. ( --
    \stemUp d16 ) -- | % 29
    \stemUp b2 ~ \stemUp b8 r8 _\! | \barNumberCheck #30
    \stemUp g2. ~ _\mf _\< | % 31
    \stemUp g2 ~ _\! _\f \stemUp g8 r8 | % 32
    r2 \stemUp g4 ~ _\mf \break | % 33
    \stemUp g2. ~ _\markup{ \small\italic {dim.} } \startTrillSpan | % 34
    \stemUp g2. ~ | % 35
    \stemUp g2. ~ | % 36
    \stemUp g2 ~ \stopTrillSpan _\pp _\> \stemUp g8 r8 _\! | % 37
    R2. | % 38
    r4 r4 \stemDown d''4 -- _\pp _\< | % 39
    \stemDown d4 ( _\! -\markup{ \italic {con lenezza a devozione} } _\>
    \stemDown cis4 _\! \stemDown b4 ) | \barNumberCheck #40
    \stemUp a2 \stemDown d4 -- _\< \pageBreak | % 41
    \stemDown d4 ( _\! _\> \stemDown cis4 _\! \stemDown b4 ) | % 42
    \stemUp a2 _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown fis'4 -- | % 43
    \stemDown fis4 ( \stemDown e4 ) \stemDown g4 -- | % 44
    \stemDown g4 ( \stemDown fis4 ) \stemDown a4 -- \stopTrillSpan _\mf
    | % 45
    \stemDown a4 ( \stemDown g4 \stemDown b,4 ) | % 46
    \stemDown e2 _\> \stemDown d4 -- _\! _\p _\< \break | % 47
    \stemDown d4 ( _\! _\> \stemDown cis4 _\! \stemDown b4 ) | % 48
    \stemUp a2 \stemDown d4 -- _\< | % 49
    \stemDown d4 ( _\! _\> \stemDown cis4 _\! \stemDown b4 ) |
    \barNumberCheck #50
    \stemUp a2 \stemDown d4 -- | % 51
    \stemDown dis4 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown e4 ) \stemDown e4 -- | % 52
    \stemDown f4 ( \stemDown fis4 ) \stemDown fis4 -- \pageBreak | % 53
    \stemDown fis4 ( \stemDown g4 ) \stemDown g4 -- | % 54
    \stemDown gis4 ( \stemDown a4 ) \stemDown d4 -- \stopTrillSpan _\mf
    _\< | % 55
    \stemDown d4 -- _\! _\> \stemDown cis4 ( _\! \stemDown b4 ) | % 56
    \stemDown a2 \stemDown d4 -- _\< | % 57
    \stemDown d4 -- _\! _\> \stemDown cis4 ( _\! \stemDown b4 ) | % 58
    \stemDown a2 \stemDown fis'4 -- \pageBreak | % 59
    \stemDown fis4 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown e4 ) \stemDown g4 -- | \barNumberCheck #60
    \stemDown g4 ( \stemDown fis4 ) \stemDown a4 -- | % 61
    \stemDown a4 -- \stemDown g4 ( \stemDown b,4 ) | % 62
    \stemDown e2 \stemDown d4 -- \stopTrillSpan _\f _\< | % 63
    \stemDown d4 -- _\! _\> \stemDown cis4 ( _\! \stemDown b4 ) | % 64
    \stemDown a2 \stemDown d4 -- _\< \pageBreak | % 65
    \stemDown d4 -- _\! _\> \stemDown cis4 ( _\! \stemDown b4 ) | % 66
    \stemDown a2 \stemDown d4 -- | % 67
    \stemDown dis4 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown e4 ) \stemDown e4 -- | % 68
    \stemDown eis4 ( \stemDown fis4 ) \stemDown fis4 -- | % 69
    \stemDown fis4 ( \stopTrillSpan _\ff _\< \stemDown g4 ) \stemDown g4
    -- | \barNumberCheck #70
    \stemDown gis4 ( \stemDown a4 ) \stemDown ais4 -- \pageBreak | % 71
    \stemDown b2. ~ -> _\! _\fff | % 72
    \stemDown b8 \stemDown a8 -- \stemDown g8 -- \stemDown fis8 --
    \stemDown e8 -- \stemDown d8 -- | % 73
    \stemDown g2. ~ -> | % 74
    \stemDown g8 \stemDown fis8 -- \stemDown e8 -- \stemDown d8 --
    \stemDown c8 -- \stemDown b8 -- | % 75
    \stemDown e2. ~ -> _\sempre _\fff | % 76
    \stemDown e8 \stemDown d8 -- \stemDown c8 -- \stemDown b8 --
    \stemDown a8 -- \stemDown g8 -- \pageBreak | % 77
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown b8 \stemDown a8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 \stemDown f8 \stemDown e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown g8 \stemDown f8 }
    | % 78
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown d8 \stemDown c8 }
    \stemDown g'16 \stemDown f16 \stemDown e16 \stemDown d16 \stemUp c16
    \stemUp b16 \stemUp a16 \stemUp g16 | % 79
    \stemDown e'16 \stemDown d16 \stemDown c16 \stemDown b16 \stemUp a16
    \stemUp g16 \stemUp f16 \stemUp e16 \once \omit TupletBracket
    \times 4/6  {
        \stemUp c'16 ( \stemUp b16 \stemUp a16 \stemUp g16 \stemUp f16
        \stemUp e16 ) }
    | \barNumberCheck #80
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp a16 ( \stemUp g16 \stemUp f16 \stemUp e16 \stemUp d16
        \stemUp c16 ) }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp e16 ( \stemUp d16 \stemUp c16 \stemUp b16 \stemUp a16
        \stemUp g16 ) }
    r4 | % 81
    r8 \stemUp <g e' c' e>8 _\fff r4 r4 ^\fermata \pageBreak | % 82
    r4 r4 \stemDown g''4 -- _\ff | % 83
    \stemDown g4 -- \stemDown fis4 ( \stemDown e4 ) | % 84
    \stemDown d4 -- r4 ^\fermata \stemDown d4 -- _\f | % 85
    \stemDown d4 -- \stemDown cis4 ( \stemDown b4 ) | % 86
    \stemUp a4 -- r4 ^\fermata r8 \stemUp a8 ( _\mf _\< | % 87
    \stemUp g4 ) _\! r4 r8 \stemUp g8 ( _\p _\< | % 88
    \stemUp fis4 ) _\! r4 \stemUp fis4 ~ _\p | % 89
    \stemUp fis4 ~ \stemUp fis16 _\< \stemUp fis16 ( \stemUp g16 \stemUp
    ais16 ) \stemDown b16 ( \stemDown cis16 ) \stemDown d16 \stemDown e16
    \break | \barNumberCheck #90
    \stemDown fis4 -- _\! _\ff \stemDown e8 -- \stemDown d8 -- \stemDown
    cis8. ( -- _\> \stemDown b16 ) -- | % 91
    \stemDown cis2 ~ _\! _\f _\> \stemDown cis8 _\! r8 | % 92
    \stemDown fis4 -- _\ff \stemDown e8 -- \stemDown d8 -- \stemDown cis8.
    ( -- _\> \stemDown b16 ) -- | % 93
    \stemDown d8 ( -> _\! _\f _\> \stemDown cis8 ~ \stemDown cis4 ~
    \stemDown cis8 ) _\! r8 | % 94
    \stemUp g4. ( _\p \stemUp g8 ) -- \stemUp g8. ( -- \stemUp a16 ) --
    | % 95
    \stemUp fis2 ~ \stemUp fis8 r8 | % 96
    \stemUp e4. ( _\pp \stemUp e8 ) -- \stemUp e8. ( -- \stemUp fis16 )
    -- | % 97
    \stemUp d2 ~ _\< \stemUp d8 _\! r8 | % 98
    \stemUp d2 _\mf _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp e4 ( \pageBreak | % 99
    \stemUp fis2. ) | \barNumberCheck #100
    \stemUp fis4 ( \stopTrillSpan _\f _\< \stemUp e2 ) | % 101
    \stemDown cis'2. ~ _\! _\ff | % 102
    \stemDown cis2 ~ _\> \stemDown cis8 _\! _\mf r8 | % 103
    r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis,16 ( _\mf _\< \stemUp d16 \stemUp e16 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis16 ( \stemUp g16 \stemUp gis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a16 \stemUp ais16 \stemUp b16 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c16 ( \stemDown cis16 \stemDown d16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown dis16 \stemDown e16 \stemDown f16 ) }
    | % 104
    \stemDown fis4 -- _\! _\ff \stemDown e8 -- \stemDown d8 -- \stemDown
    cis8. ( -- _\> \stemDown b16 ) -- | % 105
    \stemDown cis2 ~ _\! _\f _\> \stemDown cis8 r8 _\! | % 106
    \stemDown fis4 -- _\ff \stemDown e8 ( -- \stemDown d8 ) -- \stemDown
    cis8. ( -- \stemDown b16 ) -- \break | % 107
    \stemDown d8 ( -> _\> \stemDown cis8 ~ \stemDown cis4 ~ \stemDown
    cis8 ) _\! r8 | % 108
    \stemDown g'4 ( _\mf \stemDown fis8 \stemDown e8 ) \stemDown d8 (
    \stemDown cis8 ) | % 109
    \stemDown a'4 ( \stemDown g8. \stemDown fis16 ) \stemDown e8 (
    \stemDown dis8 ) | \barNumberCheck #110
    \stemDown c'4 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown b8. \stemDown a16 ) \stemDown g8 ( \stemDown fis8 ) | % 111
    \stemDown d'4 ( \stemDown c8. \stemDown b16 ) \stemDown a8 (
    \stemDown gis8 ) | % 112
    \stemDown e'8 ( \stemDown d8 ) \stemDown c8 ( \stemDown b8 )
    \stemDown f'8 ( \stemDown e8 ) | % 113
    \stemDown d8 ( \stemDown c8 ) \stemDown g'16 -. \stemDown g16 (
    \stemDown f16 ) \stemDown f16 ( \stemDown e16 ) \stemDown e16 (
    \stemDown d16 ) \stemDown d16 ( \pageBreak | % 114
    \stemDown a'16 ) \stemDown a16 ( \stemDown g16 ) \stemDown g16 (
    \stemDown f16 ) \stemDown f16 ( \stemDown e16 ) \stemDown e16 (
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown bes'16 ) \stemDown bes16 \stemDown bes16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a16 \stemDown a16 \stemDown a16 }
    | % 115
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g16 \stemDown g16 \stemDown g16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f16 \stemDown f16 \stemDown f16 }
    \stemDown c'8 :32 \stopTrillSpan _\fff \stemDown b8 :32 \stemDown a8
    :32 \stemDown gis8 :32 | % 116
    \stemDown b2 :32 -> \stemDown a4 :32 | % 117
    r4 \stemDown a8 :32 \stemDown g8 :32 \stemDown f8 :32 \stemDown e8
    :32 \pageBreak | % 118
    \stemDown g2 :32 -> \stemDown f4 :32 | % 119
    r4 \stemDown f8 :32 \stemDown e8 :32 \stemDown d8 :32 \stemDown cis8
    :32 | \barNumberCheck #120
    \stemDown e2 :32 -> \stemDown d4 :32 \pageBreak | % 121
    r4 \stemDown d8 :32 \stemDown cis8 :32 \stemDown b8 :32 \stemDown
    ais8 :32 | % 122
    \stemDown cis2 :32 -> \stemDown b4 :32 | % 123
    r4 \stemDown b8 :32 \stemDown a8 :32 \stemDown g8 :32 \stemDown fis8
    :32 \pageBreak | % 124
    \stemDown a2 :32 -> \stemDown g8 :32 \stemDown fis8 :32 | % 125
    \stemDown e8 :32 \stemDown d8 :32 \stemDown cis8 :32 \stemDown d8
    :32 \stemDown cis8 :32 \stemDown b8 :32 | % 126
    \stemUp fis8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis16 ( _\fff \stemDown gis16 \stemDown ais16 }
    \stemDown b32 \stemDown cis32 \stemDown d32 \stemDown e32 ) | % 127
    \stemDown fis4 -> \stemDown e8 -- \stemDown d8 -- \stemDown cis8 --
    \stemDown b8 -- | % 128
    \stemDown d8 ( -> \stemDown cis8 ) r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis,16 ( \stemUp gis16 \stemUp ais16 }
    \stemUp b32 \stemUp cis32 \stemUp d32 \stemUp e32 ) \pageBreak | % 129
    \stemDown fis4 -> \stemDown e8 -- \stemDown d8 -- \stemDown cis8 (
    -- \stemDown b8 ) -- | \barNumberCheck #130
    \stemDown d8 ( -> \stemDown cis8 ) r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp b,16 ( \stemUp cis16 \stemUp d16 }
    \stemUp e32 \stemUp fis32 \stemUp g32 \stemUp a32 ) | % 131
    \stemDown b4 -> \stemUp a8 -- \stemUp g8 -- \stemUp fis8 ( --
    \stemUp e8 ) -- | % 132
    \stemUp g8 ( -> \stemUp fis8 ) r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp b,16 ( \stemUp cis16 \stemUp d16 }
    \stemUp e32 \stemUp fis32 \stemUp g32 \stemUp a32 ) | % 133
    \stemDown b4 -> \stemUp a8 -- \stemUp g8 -- \stemUp fis8 ( --
    \stemUp e8 ) -- | % 134
    \stemUp g8 ( -> \stemUp fis8 ) r4 r4 \pageBreak | % 135
    \stemUp fis8 ( -> _\f \stemUp e8 ) r4 r4 | % 136
    \stemUp e8 ( -> _\mf \stemUp d8 ) r4 r4 | % 137
    R2.*10 \pageBreak | % 147
    r4 ^ "con sordini" r4 \stemDown b'4 -- _\f ^ "sul G" _\< | % 148
    \stemDown b4 -- _\! _\sff _\> \stemUp a4 ( _\! \stemUp g4 ) | % 149
    \stemUp fis2 \stemDown b4 -- _\f _\< | \barNumberCheck #150
    \stemDown b4 -- _\! _\sff _\> \stemUp a4 ( _\! \stemUp g4 ) | % 151
    \stemUp fis2 \stemUp fis4 -- _\f _\< | % 152
    \stemUp fis4 ( _\! _\sf _\> \stemUp e4 ) _\! \stemUp d4 -- _\<
    \pageBreak | % 153
    \stemUp d4 ( _\! _\sf _\> \stemUp cis4 ) \stemUp b4 -- _\! | % 154
    \stemUp b4 ( _\sf _\> \stemUp a4 \stemUp g8 ) _\! r8 | % 155
    R2.*4 \break | % 159
    R2.*6 \break | % 165
    R2.*7 \bar "|."
    }

PartPOneSevenVoiceOne =  \relative fis'' {
    \clef "treble" \time 3/4 \key d \major | % 1
    \stemDown fis4 -- _\f -\markup{ \italic {largamente} } \stemDown
    ais,8 ( \stemDown d8 ) \stemUp f,8. ( _\> \stemUp b16 ) | % 2
    \stemUp e,2 ~ _\! _\mf _\> \stemUp e8 _\! _\p r8 | % 3
    \stemDown fis'4 -- _\f \stemDown ais,8 ( \stemDown d8 ) \stemUp f,8.
    ( _\> \stemUp b16 ) | % 4
    \stemUp e,2 ~ _\! _\mf _\> \stemUp e8 r8 _\! | % 5
    \stemUp b4. ( _\p \stemUp b8 ) -- \stemUp b8. ( -- \stemUp a16 ) --
    | % 6
    \stemUp a2 r4 | % 7
    \stemUp d4. ( _\mp \stemUp d8 ) -- \stemUp d8. ( -- \stemUp cis16 )
    -- \pageBreak | % 8
    \stemUp cis2 r4 | % 9
    \stemUp d4. ( _\mf _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemUp d8 ) -- \stemUp cis4 -- | \barNumberCheck
    #10
    \stemUp fis4. ( \stemUp fis8 ) -- \stemUp e4 -- | % 11
    \stemDown <a a'>4. ( \stemDown <b gis'>8 ) -- \stemDown <cis gis'>4
    -- | % 12
    \stemUp <d, d'>2. ~ ~ \stopTrillSpan _\ff _\> | % 13
    \stemUp <d d'>8 _\! _\mf r8 \stemUp <d b'>4 ~ ~ _\f _\> \stemUp <d
        b'>8 r8 _\! | % 14
    \stemUp eis4 ( _\mf _\> \stemUp e8 ) r8 _\! \stemUp b4 ( _\mp | % 15
    \stemUp e8 ) r8 r4 r4 \break | % 16
    R2.*3 | % 19
    r4 r16 \stemUp b16 ( _\p _\< \stemUp g'16 \stemUp e16 ) \stemUp b'16
    ( \stemUp g16 ) \stemUp d'16 ( \stemUp ais16 ) | \barNumberCheck #20
    \stemDown fis'4 -- _\! _\f \stemDown ais,8 ( \stemDown d8 ) \stemUp
    f,8. ( _\> \stemUp b16 ) | % 21
    \stemUp e,2 ~ _\! _\mf _\> \stemUp e8 _\! _\p r8 | % 22
    \stemDown fis'4 -- _\f \stemDown ais,8 ( \stemDown d8 ) \stemUp f,8.
    ( _\> \stemUp b16 ) | % 23
    \stemUp e,2 ~ _\! _\mf _\> \stemUp e8 r8 _\! \pageBreak | % 24
    \stemUp b4. ( _\p \stemUp b8 ) -- \stemUp b8. ( -- \stemUp a16 ) --
    | % 25
    \stemUp a2 ~ \stemUp a8 r8 | % 26
    R2.*7 \break | % 33
    R2.*8 \pageBreak | % 41
    R2.*5 | % 46
    r4 r4 \stemUp d'4 -- _\p ^ "a 2" _\< \break | % 47
    \stemUp d4 ( _\! _\> \stemUp cis4 _\! \stemUp b4 ) | % 48
    \stemUp a2 \stemUp d4 -- _\< | % 49
    \stemUp d4 ( _\! _\> \stemUp cis4 _\! \stemUp b4 ) | \barNumberCheck
    #50
    \stemUp a2 \stemUp d4 -- | % 51
    \stemUp dis4 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp e4 ) \stemUp e4 -- | % 52
    \stemUp f4 ( \stemUp fis4 ) \stemUp fis4 -- \pageBreak | % 53
    \stemUp fis4 ( \stemUp g4 ) \stemUp g4 -- | % 54
    \stemUp gis4 ( \stemUp a4 ) \stemUp d,4 -- \stopTrillSpan _\mf _\< | % 55
    \stemDown d4 -- _\! _\> \stemDown cis4 ( _\! \stemDown b4 ) | % 56
    \stemUp a2 \stemDown d4 -- _\< | % 57
    \stemDown d4 -- _\! _\> \stemDown cis4 ( _\! \stemDown b4 ) | % 58
    \stemUp a2 \stemDown fis'4 -- \pageBreak | % 59
    \stemDown fis4 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown e4 ) \stemDown g4 -- | \barNumberCheck #60
    \stemDown g4 ( \stemDown fis4 ) \stemDown a4 -- | % 61
    \stemDown a4 -- \stemDown g4 ( \stemDown b,4 ) | % 62
    \stemDown e2 \stemUp d'4 -- \stopTrillSpan _\f ^ "div." _\< | % 63
    \stemUp d4 -- _\! _\> \stemUp cis4 ( _\! \stemUp b4 ) | % 64
    \stemUp a2 \stemUp d4 -- _\< \pageBreak | % 65
    \stemUp d4 -- _\! _\> \stemUp cis4 ( _\! \stemUp b4 ) | % 66
    \stemUp a2 \stemUp d4 -- | % 67
    \stemUp dis4 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp e4 ) \stemUp e4 -- | % 68
    \stemUp eis4 ( \stemUp fis4 ) \stemUp fis4 -- | % 69
    \stemUp fis4 ( \stopTrillSpan _\ff _\< \stemUp g4 ) \stemUp g4 -- |
    \barNumberCheck #70
    \stemUp gis4 ( \stemUp a4 ) \stemUp ais4 -- \pageBreak | % 71
    \stemUp b2. ~ -> _\! _\fff | % 72
    \stemUp b8 \stemUp a8 -- \stemUp g8 -- \stemUp fis8 -- \stemUp e8 --
    \stemUp d8 -- | % 73
    \stemUp g2. ~ -> | % 74
    \stemUp g8 \stemUp fis8 -- \stemUp e8 -- \stemUp d8 -- \stemUp c8 --
    \stemUp b8 -- | % 75
    \stemUp e2. ~ -> _\sempre _\fff | % 76
    \stemUp e8 \stemUp d8 -- \stemUp c8 -- \stemUp b8 -- \stemUp a8 --
    \stemUp g8 -- \pageBreak | % 77
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp b8 \stemUp a8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 \stemUp f8 \stemUp e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp g8 \stemUp f8 }
    | % 78
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 \stemUp d8 \stemUp c8 }
    \stemUp g'16 \stemUp f16 \stemUp e16 \stemUp d16 \stemUp c16 \stemUp
    b16 \stemUp a16 \stemUp g16 | % 79
    \stemDown e'16 ^ "unis." \stemDown d16 \stemDown c16 \stemDown b16
    \stemUp a16 \stemUp g16 \stemUp f16 \stemUp e16 \once \omit
    TupletBracket
    \times 4/6  {
        \stemUp c'16 ( \stemUp b16 \stemUp a16 \stemUp g16 \stemUp f16
        \stemUp e16 ) }
    | \barNumberCheck #80
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp a16 ( \stemUp g16 \stemUp f16 \stemUp e16 \stemUp d16
        \stemUp c16 ) }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp e16 ( \stemUp d16 \stemUp c16 \stemUp b16 \stemUp a16
        \stemUp g16 ) }
    r4 | % 81
    r8 \stemUp <g e' c' e>8 _\fff r4 r4 ^\fermata \pageBreak | % 82
    R2. | % 83
    \stemUp e'4 -- _\ff \stemUp fis4 ( \stemUp g4 ) | % 84
    \stemUp fis4 -- r4 ^\fermata r4 | % 85
    \stemUp b,4 -- _\f \stemUp cis4 ( \stemUp d4 ) | % 86
    \stemUp cis4 -- r4 ^\fermata r8 \stemUp c8 ( _\mf _\< | % 87
    \stemUp b4 ) _\! r4 r8 \stemUp b8 ~ _\p _\< | % 88
    \stemUp b4 _\! r4 \stemUp <b d>4 ~ ~ _\p | % 89
    \stemUp <b d>4 ~ ~ \stemUp <b d>16 _\< \stemUp d16 ( \stemUp cis16
    \stemUp e16 ) \stemUp d16 ( \stemUp g16 ) \stemUp fis16 \stemUp ais16
    \break | \barNumberCheck #90
    \stemDown b4 -- _\! _\ff \stemUp ais8 -- \stemUp gis8 -- \stemUp f8.
    ( -- _\> \stemUp f16 ) -- | % 91
    \stemUp e2 ~ _\! _\f _\> \stemUp e8 _\! r8 | % 92
    \stemDown b'4 -- _\ff \stemUp ais8 -- \stemUp gis8 -- \stemUp f8. (
    -- _\> \stemUp f16 ) -- | % 93
    \stemUp e2 ~ _\! _\f _\> \stemUp e8 _\! r8 | % 94
    \stemUp b4. ( _\p \stemUp b8 ) -- \stemUp b8. ( -- \stemUp a16 ) --
    | % 95
    \stemUp a2 ~ \stemUp a8 r8 | % 96
    R2.*2 | % 98
    \stemUp b2 _\mf _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp b4 ~ \pageBreak | % 99
    \stemUp b4 \stemUp ais2 | \barNumberCheck #100
    \stemUp g'2. ~ \stopTrillSpan _\f _\< | % 101
    \stemUp g4 _\! _\ff \stemUp fis2 ~ | % 102
    \stemUp fis2 ~ _\> \stemUp fis8 _\! _\mf r8 | % 103
    r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp ais,16 ( _\mf _\< \stemUp b16 \stemUp c16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis16 \stemUp d16 \stemUp dis16 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 ( \stemUp eis16 \stemUp fis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp g16 \stemUp gis16 \stemUp a16 ) }
    | % 104
    \stemDown b4 -- _\! _\ff \stemUp ais8 -- \stemUp gis8 -- \stemUp f8.
    ( -- _\> \stemUp f16 ) -- | % 105
    \stemUp e2 ~ _\! _\f _\> \stemUp e8 r8 _\! | % 106
    \stemDown b'4 -- _\ff \stemUp ais8 ( -- \stemUp gis8 ) -- \stemUp f8.
    ( -- \stemUp f16 ) -- \break | % 107
    \stemUp e2 ~ _\> \stemUp e8 _\! r8 | % 108
    \stemUp g4 ( _\mf \stemUp fis8 \stemUp e8 ) \stemUp d8 ( \stemUp cis8
    ) | % 109
    \stemUp a'4 ( \stemUp g8. \stemUp fis16 ) \stemUp e8 ( \stemUp dis8
    ) | \barNumberCheck #110
    \stemDown c'4 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp b8. \stemUp a16 ) \stemUp g8 ( \stemUp fis8 ) | % 111
    \stemDown d'4 ( \stemDown c8. \stemDown b16 ) \stemUp a8 ( \stemUp
    gis8 ) | % 112
    \stemDown e'8 ( \stemDown d8 ) \stemDown c8 ( \stemDown b8 )
    \stemDown f'8 ( \stemDown e8 ) | % 113
    \stemDown d8 ( \stemDown c8 ) \stemDown g'16 -. \stemDown g16 (
    \stemDown f16 ) \stemDown f16 ( \stemDown e16 ) \stemDown e16 (
    \stemDown d16 ) \stemDown d16 ( \pageBreak | % 114
    \stemDown a'16 ) \stemDown a16 ( \stemDown g16 ) \stemDown g16 (
    \stemDown f16 ) \stemDown f16 ( \stemDown e16 ) \stemDown e16 (
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown bes'16 ) \stemDown bes16 \stemDown bes16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a16 \stemDown a16 \stemDown a16 }
    | % 115
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g16 \stemDown g16 \stemDown g16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f16 \stemDown f16 \stemDown f16 }
    \stemDown c'8 :32 \stopTrillSpan _\fff \stemDown b8 :32 \stemDown a8
    :32 \stemDown gis8 :32 | % 116
    \stemDown b2 :32 -> \stemDown a4 :32 | % 117
    r4 \stemDown a8 :32 \stemDown g8 :32 \stemDown f8 :32 \stemDown e8
    :32 \pageBreak | % 118
    \stemDown g2 :32 -> \stemDown f4 :32 | % 119
    r4 \stemUp f'8 :32 ^ "div." \stemUp e8 :32 \stemUp d8 :32 \stemUp
    cis8 :32 | \barNumberCheck #120
    \stemUp e2 :32 -> \stemUp d4 :32 \pageBreak | % 121
    r4 \stemUp d8 :32 \stemUp cis8 :32 \stemUp b8 :32 \stemUp ais8 :32 | % 122
    \stemUp cis2 :32 -> \stemUp b4 :32 | % 123
    r4 \stemUp b8 :32 \stemUp a8 :32 \stemUp g8 :32 \stemUp fis8 :32
    \pageBreak | % 124
    \stemUp a2 :32 -> \stemUp g8 :32 \stemUp fis8 :32 | % 125
    \stemUp e8 :32 \stemUp d8 :32 \stemUp cis8 :32 \stemUp d8 :32
    \stemUp cis8 :32 \stemUp b8 :32 | % 126
    \stemUp <b, d>8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis16 ( _\fff \stemUp d16 \stemUp e16 }
    \stemUp f32 \stemUp g32 \stemUp gis32 \stemUp ais32 ) | % 127
    \stemDown b4 -> \stemUp ais8 -- \stemUp gis8 -- \stemUp fis8 --
    \stemUp f8 -- | % 128
    \stemUp e4 -> r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp cis16 ( \stemUp d16 \stemUp e16 }
    \stemUp f32 \stemUp g32 \stemUp gis32 \stemUp ais32 ) \pageBreak | % 129
    \stemDown b4 -> \stemUp ais8 -- \stemUp gis8 -- \stemUp fis8 ( --
    \stemUp f8 ) -- | \barNumberCheck #130
    \stemUp e4 -> r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp b16 ( \stemUp g16 \stemUp gis16 }
    \stemUp ais32 \stemUp b32 \stemUp cis32 \stemUp dis32 ) | % 131
    \stemUp e4 -> \stemUp dis8 -- \stemUp cis8 -- \stemUp b8 ( --
    \stemUp ais8 ) -- | % 132
    \stemUp cis4 -> r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp b16 ( \stemUp g16 \stemUp gis16 }
    \stemUp ais32 \stemUp b32 \stemUp cis32 \stemUp dis32 ) | % 133
    \stemUp e4 -> \stemUp dis8 -- \stemUp cis8 -- \stemUp b8 ( --
    \stemUp ais8 ) -- | % 134
    \stemUp cis4 -> r4 r4 \pageBreak | % 135
    \stemUp b4 -> _\f r4 r4 | % 136
    \stemUp b4 -> _\mf r4 r4 | % 137
    R2.*10 \pageBreak | % 147
    r4 ^ "con sordini" r4 \stemDown b'4 -- _\f ^ "sul G" _\< | % 148
    \stemDown b4 -- _\! _\sff _\> \stemUp a4 ( _\! \stemUp g4 ) | % 149
    \stemUp fis2 \stemDown b4 -- _\f _\< | \barNumberCheck #150
    \stemDown b4 -- _\! _\sff _\> \stemUp a4 ( _\! \stemUp g4 ) | % 151
    \stemUp fis2 \stemUp fis4 -- _\f _\< | % 152
    \stemUp fis4 ( _\! _\sf _\> \stemUp e4 ) _\! \stemUp d4 -- _\<
    \pageBreak | % 153
    \stemUp d4 ( _\! _\sf _\> \stemUp cis4 ) \stemUp b4 -- _\! | % 154
    \stemUp b4 ( _\sf _\> \stemUp a4 \stemUp g8 ) _\! r8 | % 155
    R2.*4 \break | % 159
    R2.*6 \break | % 165
    R2.*7 \bar "|."
    }

PartPOneSevenVoiceTwo =  \relative d' {
    \clef "treble" \time 3/4 \key d \major s4*21 \pageBreak s1*6 \break
    s1*6 \pageBreak s4*27 \break s1*6 \pageBreak s4*17 \stemDown d4 --
    \break | % 47
    \stemDown d4 ( \stemDown cis4 \stemDown b4 ) | % 48
    \stemDown a2 \stemDown d4 -- | % 49
    \stemDown d4 ( \stemDown cis4 \stemDown b4 ) | \barNumberCheck #50
    \stemDown a2 \stemDown d4 -- | % 51
    \stemDown dis4 ( \stemDown e4 ) \stemDown e4 -- | % 52
    \stemDown f4 ( \stemDown fis4 ) \stemDown fis4 -- \pageBreak | % 53
    \stemDown fis4 ( \stemDown g4 ) \stemDown g4 -- | % 54
    \stemDown gis4 ( \stemDown a4 ) \stemDown d4 -- s1*3 \pageBreak
    s4*11 \stemDown d4 -- | % 63
    \stemDown d4 -- \stemDown cis4 ( \stemDown b4 ) | % 64
    \stemDown a2 \stemDown d4 -- \pageBreak | % 65
    \stemDown d4 -- \stemDown cis4 ( \stemDown b4 ) | % 66
    \stemDown a2 \stemDown d4 -- | % 67
    \stemDown dis4 ( \stemDown e4 ) \stemDown e4 -- | % 68
    \stemDown eis4 ( \stemDown fis4 ) \stemDown fis4 -- | % 69
    \stemDown fis4 ( \stemDown g4 ) \stemDown g4 -- | \barNumberCheck
    #70
    \stemDown gis4 ( \stemDown a4 ) \stemDown ais4 -- \pageBreak | % 71
    \stemDown b2. ~ -> | % 72
    \stemDown b8 \stemDown a8 -- \stemDown g8 -- \stemDown fis8 --
    \stemDown e8 -- \stemDown d8 -- | % 73
    \stemDown g2. ~ -> | % 74
    \stemDown g8 \stemDown fis8 -- \stemDown e8 -- \stemDown d8 --
    \stemDown c8 -- \stemDown b8 -- | % 75
    \stemDown e2. ~ -> | % 76
    \stemDown e8 \stemDown d8 -- \stemDown c8 -- \stemDown b8 --
    \stemDown a8 -- \stemDown g8 -- \pageBreak | % 77
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown b8 \stemDown a8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 \stemDown f8 \stemDown e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown g8 \stemDown f8 }
    | % 78
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown d8 \stemDown c8 }
    \stemDown g'16 \stemDown f16 \stemDown e16 \stemDown d'16 \stemDown
    c16 \stemDown b16 \stemDown a16 \stemDown g16 s4*9 \pageBreak s1*6
    \break s4*27 \pageBreak s1*6 \break s4*21 \pageBreak s1*3 \pageBreak
    s1 \stemDown f'8 :32 \stemDown e8 :32 \stemDown d8 :32 \stemDown cis8
    :32 | \barNumberCheck #120
    \stemDown e2 :32 -> \stemDown d4 :32 \pageBreak s4 \stemDown d8 :32
    \stemDown cis8 :32 \stemDown b8 :32 \stemDown ais8 :32 | % 122
    \stemDown cis2 :32 \stemDown b4 :32 s4 \stemDown b8 :32 \stemDown a8
    :32 \stemDown g8 :32 \stemDown fis8 :32 \pageBreak | % 124
    \stemDown a2 :32 -> \stemDown g8 :32 \stemDown fis8 :32 | % 125
    \stemDown e8 :32 \stemDown d8 :32 \stemDown cis8 :32 \stemDown d8
    :32 \stemDown cis8 :32 \stemDown b8 :32 s4*9 \pageBreak s2*9
    \pageBreak s1*9 \pageBreak s2*9 \pageBreak s2*9 \break s2*9 \break
    s4*21 \bar "|."
    }

PartPOneEightVoiceOne =  \relative d' {
    \clef "alto" \time 3/4 \key d \major | % 1
    \stemDown d4 -- _\f -\markup{ \italic {largamente} } \stemDown fis8
    ( \stemDown b,8 ) \stemUp b8. ( _\> \stemUp g16 ) | % 2
    \stemUp ais2 ~ _\! _\mf _\> \stemUp ais8 _\! _\p r8 | % 3
    \stemDown d4 -- _\f \stemDown fis8 ( \stemDown b,8 ) \stemUp b8. (
    _\> \stemUp g16 ) | % 4
    \stemUp ais2 ~ _\! _\mf _\> \stemUp ais8 r8 _\! | % 5
    \stemUp g4. ( _\p \stemUp g8 ) -- \stemUp g8. ( -- \stemUp g16 ) --
    | % 6
    \stemUp fis2 r4 | % 7
    \stemUp b4. ( _\mp \stemUp b8 ) -- \stemUp b8. ( -- \stemUp b16 ) --
    \pageBreak | % 8
    \stemUp a2 r4 | % 9
    \stemDown fis'4. ( _\mf _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemDown e8 ) -- \stemDown e4 -- | \barNumberCheck
    #10
    \stemDown a4. ( \stemDown gis8 ) -- \stemDown gis4 -- | % 11
    \stemDown <a cis>4. ( \stemDown gis8 ) -- \stemDown gis4 -- | % 12
    \stemDown fis2. ~ \stopTrillSpan _\ff _\> | % 13
    \stemDown fis8 _\! _\mf r8 \stemUp b,4 ~ _\f _\> \stemUp b8 r8 _\! | % 14
    \stemUp b4 ~ _\mf _\> \stemUp b8 r8 _\! r4 | % 15
    r4 \stemUp fis4 ( _\p \stemUp b8 ) r8 \break | % 16
    R2. | % 17
    r4 r4 \stemDown g'4 ~ _\pp _\< | % 18
    \stemDown g2 ~ _\! _\> \stemDown g8 _\! _\ppp r8 | % 19
    r4 r16 \stemUp g,16 ( _\p _\< \stemUp e16 \stemUp cis'16 ) \stemDown
    gis16 ( \stemDown e'16 ) \stemDown b16 ( \stemDown g'16 ) |
    \barNumberCheck #20
    \stemDown d4 -- _\! _\f \stemDown fis8 ( \stemDown b,8 ) \stemUp b8.
    ( _\> \stemUp g16 ) | % 21
    \stemUp ais2 ~ _\! _\mf _\> \stemUp ais8 _\! _\p r8 | % 22
    \stemDown d4 -- _\f \stemDown fis8 ( \stemDown b,8 ) \stemUp b8. (
    _\> \stemUp g16 ) | % 23
    \stemUp ais2 ~ _\! _\mf _\> \stemUp ais8 r8 _\! \pageBreak | % 24
    \stemUp g4. ( _\p \stemUp g8 ) -- \stemUp g8. ( -- \stemUp g16 ) --
    | % 25
    \stemUp fis2 ~ \stemUp fis8 r8 | % 26
    \stemUp e4. ( _\pp \stemUp e8 ) -- \stemUp e8. ( -- \stemUp e16 ) --
    | % 27
    \stemUp fis2 ~ \stemUp fis8 r8 | % 28
    \stemUp cis4. ( _\pp _\< \stemUp cis8 ) -- \stemUp cis8. ( --
    \stemUp d16 ) -- | % 29
    \stemUp d2 ~ \stemUp d8 r8 _\! | \barNumberCheck #30
    R2.*3 \break | % 33
    R2.*5 | % 38
    r4 r4 \stemDown d'4 -- _\pp _\< | % 39
    \stemDown d4 ( _\! _\> \stemDown cis4 _\! \stemUp b4 ) |
    \barNumberCheck #40
    \stemUp a2 \stemDown d4 -- _\< \pageBreak | % 41
    \stemDown d4 ( _\! _\> \stemDown cis4 _\! \stemUp b4 ) | % 42
    \stemUp a2 _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown fis'4 -- | % 43
    \stemDown fis4 ( \stemDown e4 ) \stemDown g4 -- | % 44
    \stemDown g4 ( \stemDown fis4 ) \stemDown a4 -- \stopTrillSpan _\mf
    | % 45
    \stemDown a4 ( \stemDown g4 \stemUp b,4 ) | % 46
    \stemDown e2 _\> \stemDown d4 -- _\! _\p _\< \break | % 47
    \stemDown d4 ( _\! _\> \stemDown cis4 _\! \stemUp b4 ) | % 48
    \stemUp a2 \stemDown d4 -- _\< | % 49
    \stemDown d4 ( _\! _\> \stemDown cis4 _\! \stemUp b4 ) |
    \barNumberCheck #50
    \stemUp a2 \stemDown d4 -- | % 51
    \stemDown dis4 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown e4 ) \stemDown e4 -- | % 52
    \stemDown f4 ( \stemDown fis4 ) \stemDown fis4 -- \pageBreak | % 53
    \stemDown fis4 ( \stemDown g4 ) \stemDown g4 -- | % 54
    \stemDown gis4 ( \stemDown a4 ) \stemDown d,4 -- \stopTrillSpan _\mf
    _\< | % 55
    \stemDown d4 -- _\! _\> \stemDown cis4 ( _\! \stemUp b4 ) | % 56
    \stemUp a2 \stemDown d4 -- _\< | % 57
    \stemDown d4 -- _\! _\> \stemDown cis4 ( _\! \stemUp b4 ) | % 58
    \stemUp a2 \stemDown fis'4 -- \pageBreak | % 59
    \stemDown fis4 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown e4 ) \stemDown g4 -- | \barNumberCheck #60
    \stemDown g4 ( \stemDown fis4 ) \stemDown a4 -- | % 61
    \stemDown a4 -- \stemDown g4 ( \stemUp b,4 ) | % 62
    \stemDown e2 \stemUp d'4 -- \stopTrillSpan _\f ^ "div." _\< | % 63
    \stemUp d4 -- _\! _\> \stemUp cis4 ( _\! \stemUp b4 ) | % 64
    \stemUp a2 \stemUp d4 -- _\< \pageBreak | % 65
    \stemUp d4 -- _\! _\> \stemUp cis4 ( _\! \stemUp b4 ) | % 66
    \stemUp a2 \stemUp d4 -- | % 67
    \stemUp dis4 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp e4 ) \stemUp e4 -- | % 68
    \stemUp eis4 ( \stemUp fis4 ) \stemUp fis4 -- | % 69
    \stemUp fis4 ( \stopTrillSpan _\ff _\< \stemUp g4 ) \stemUp g4 -- |
    \barNumberCheck #70
    \stemUp gis4 ( \stemUp a4 ) \stemUp ais4 -- \pageBreak | % 71
    \stemUp b2. ~ -> _\! _\fff | % 72
    \stemUp b8 \stemUp a8 -- \stemUp g8 -- \stemUp fis8 -- \stemUp e8 --
    \stemUp d8 -- | % 73
    \stemUp g2. ~ -> | % 74
    \stemUp g8 \stemUp fis8 -- \stemUp e8 -- \stemUp d8 -- \stemUp c8 --
    \stemUp b8 -- | % 75
    \stemUp e2. ~ -> _\sempre _\fff | % 76
    \stemUp e8 \stemUp d8 -- \stemUp c8 -- \stemUp b8 -- \stemUp a8 --
    \stemUp g8 -- \pageBreak | % 77
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp b8 \stemUp a8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp g8 \stemUp f8 \stemUp e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a8 \stemUp g8 \stemUp f8 }
    | % 78
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 \stemUp d8 \stemUp c8 }
    \stemUp g'16 \stemUp f16 \stemUp e16 \stemUp d16 \stemUp c16 \stemUp
    b16 \stemUp a16 \stemUp g16 | % 79
    \stemDown e'16 ^ "unis." \stemDown d16 \stemDown c16 \stemDown b16
    \stemUp a16 \stemUp g16 \stemUp f16 \stemUp e16 \once \omit
    TupletBracket
    \times 4/6  {
        \stemUp c'16 ( \stemUp b16 \stemUp a16 \stemUp g16 \stemUp f16
        \stemUp e16 ) }
    | \barNumberCheck #80
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp a16 ( \stemUp g16 \stemUp f16 \stemUp e16 \stemUp d16
        \stemUp c16 ) }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp e'16 ( \stemUp d16 \stemUp c16 \stemUp b16 \stemUp a16
        \stemUp g16 ) }
    \once \omit TupletBracket
    \times 8/7  {
        \stemUp c32*161/160 ( \stemUp b32*161/160 \stemUp a32*161/160
        \stemUp g32*161/160 \stemUp f32*161/160 \stemUp e32*161/160
        \stemUp d32*161/160 ) }
    | % 81
    \stemUp c8 \stemUp c8 \stemUp g'8 \stemUp e'8 r4 r4 ^\fermata
    \pageBreak | % 82
    R2. | % 83
    \stemUp e,4 -- _\ff \stemUp fis4 ( \stemUp g4 ) | % 84
    \stemUp fis4 -- r4 ^\fermata \stemDown d'4 -- _\f | % 85
    \stemDown d4 -- \stemDown cis4 ( \stemUp b4 ) | % 86
    \stemUp a4 -- r4 ^\fermata r8 \stemUp a8 ( _\mf _\< | % 87
    \stemUp g4 ) _\! r4 r8 \stemUp g8 ( _\p _\< | % 88
    \stemUp fis4 ) _\! r4 \stemUp fis4 ~ _\p | % 89
    \stemUp fis4 ~ \stemUp fis16 _\< \stemUp b16 ( \stemUp ais16 \stemUp
    cis16 ) \stemDown b16 ( \stemDown e16 ) \stemDown d16 \stemDown g16
    \break | \barNumberCheck #90
    \stemDown gis4 -- _\! _\ff \stemDown fis8 -- \stemDown f8 -- \stemUp
    b,8. ( -- _\> \stemUp b16 ) -- | % 91
    \stemUp ais2 ~ _\! _\f _\> \stemUp ais8 _\! r8 | % 92
    \stemDown gis'4 -- _\ff \stemDown fis8 -- \stemDown f8 -- \stemUp b,8.
    ( -- _\> \stemUp b16 ) -- | % 93
    \stemUp ais2 ~ _\! _\f _\> \stemUp ais8 _\! r8 | % 94
    \stemUp g4. ( _\p \stemUp g8 ) -- \stemUp g8. ( -- \stemUp g16 ) --
    | % 95
    \stemUp fis2 ~ \stemUp fis8 r8 | % 96
    \stemUp e4. ( _\pp \stemUp e8 ) -- \stemUp e8. ( -- \stemUp e16 ) --
    | % 97
    \stemUp fis2 ~ _\< \stemUp fis8 _\! r8 | % 98
    \stemUp d2 _\mf _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp e4 ~ \pageBreak | % 99
    \stemUp e2. | \barNumberCheck #100
    \stemUp g2. ~ \stopTrillSpan _\f _\< | % 101
    \stemUp g4 _\! _\ff \stemUp fis2 ~ | % 102
    \stemUp fis2 ~ _\> \stemUp fis8 _\! _\mf r8 | % 103
    r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis16 ( _\mf \stemUp e16 _\< \stemUp g16 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis16 ( \stemDown d16 \stemDown dis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e16 \stemDown f16 \stemDown fis16 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g16 ( \stemDown gis16 \stemDown a16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown ais16 \stemDown b16 \stemDown c16 ) }
    | % 104
    \stemDown gis4 -- _\! _\ff \stemDown fis8 -- \stemDown f8 -- \stemUp
    b,8. ( -- _\> \stemUp b16 ) -- | % 105
    \stemUp ais2 ~ _\! _\f _\> \stemUp ais8 r8 _\! | % 106
    \stemDown gis'4 -- _\ff \stemDown fis8 ( -- \stemDown f8 ) --
    \stemUp b,8. ( -- \stemUp b16 ) -- \break | % 107
    \stemUp ais2 ~ _\> \stemUp ais8 _\! r8 | % 108
    \stemUp e4 ( _\mf \stemUp d8 \stemUp cis8 ) \stemUp e4 | % 109
    \stemUp a4 ( \stemUp g8. \stemUp fis16 ) \stemUp e8 ( \stemUp dis8 )
    | \barNumberCheck #110
    \stemDown c'4 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp b8. \stemUp a16 ) \stemUp g8 ( \stemUp fis8 ) | % 111
    \stemDown d'4 ( \stemUp c8. \stemUp b16 ) \stemUp a8 ( \stemUp gis8
    ) | % 112
    \stemDown e'8 ( \stemDown d8 ) \stemDown c8 ( \stemDown b8 )
    \stemDown f'8 ( \stemDown e8 ) | % 113
    \stemDown d8 ( \stemDown c8 ) \stemDown g'16 -. \stemDown g16 (
    \stemDown f16 ) \stemDown f16 ( \stemDown e16 ) \stemDown e16 (
    \stemDown d16 ) \stemDown d16 ( \pageBreak | % 114
    \stemDown a'16 ) \stemDown a16 ( \stemDown g16 ) \stemDown g16 (
    \stemDown f16 ) \stemDown f16 ( \stemDown e16 ) \stemDown e16 (
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown bes'16 ) \stemDown bes16 \stemDown bes16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a16 \stemDown a16 \stemDown a16 }
    | % 115
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g16 \stemDown g16 \stemDown g16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown f16 \stemDown f16 \stemDown f16 }
    \stemDown c'8 :32 \stopTrillSpan _\fff \stemDown b8 :32 \stemDown a8
    :32 \stemDown gis8 :32 | % 116
    \stemDown b2 :32 -> \stemDown a4 :32 | % 117
    r4 \stemDown a8 :32 \stemDown g8 :32 \stemDown f8 :32 \stemDown e8
    :32 \pageBreak | % 118
    \stemDown g2 :32 -> \stemDown f4 :32 | % 119
    r4 \stemUp f'8 :32 ^ "div." \stemUp e8 :32 \stemUp d8 :32 \stemUp
    cis8 :32 | \barNumberCheck #120
    \stemUp e2 :32 -> \stemUp d4 :32 \pageBreak | % 121
    r4 \stemUp d8 :32 \stemUp cis8 :32 \stemUp b8 :32 \stemUp ais8 :32 | % 122
    \stemUp cis2 :32 -> \stemUp b4 :32 | % 123
    r4 \stemUp b8 :32 \stemUp a8 :32 \stemUp g8 :32 \stemUp fis8 :32
    \pageBreak | % 124
    \stemUp a2 :32 \stemDown g,8 :32 \stemDown g'8 \stemDown fis,8 :32
    \stemDown fis'8 | % 125
    \stemUp e,8 :32 \stemUp e'8 \stemUp d,8 :32 \stemUp d'8 \stemUp cis,8
    :32 \stemUp cis'8 \stemUp d,8 :32 \stemUp d'8 \stemUp cis,8 :32
    \stemUp cis'8 \stemUp b8 :32 | % 126
    \stemUp fis8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown ais16 ( _\fff \stemDown b16 \stemDown cis16 }
    \stemDown d32 \stemDown e32 \stemDown f32 \stemDown g32 ) | % 127
    \stemDown gis4 -> \stemDown fis8 -- \stemDown eis8 -- \stemDown e8
    -- \stemDown d8 -- | % 128
    \stemDown ais4 -> \stemDown fis'4 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown ais,16 ( \stemDown b16 \stemDown cis16 }
    \stemDown d32 \stemDown e32 \stemDown f32 \stemDown g32 ) \pageBreak
    | % 129
    \stemDown gis4 -> \stemDown fis8 -- \stemDown f8 -- \stemDown e8 (
    -- \stemDown d8 ) -- | \barNumberCheck #130
    \stemDown ais4 -> \stemDown fis'4 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis,16 ( \stemUp e16 \stemUp f16 }
    \stemUp g32 \stemUp as32 \stemUp bes32 \stemUp c32 ) | % 131
    \stemUp cis4 -> \stemUp c8 -- \stemUp ais8 -- \stemUp gis8 ( --
    \stemUp g8 ) -- | % 132
    \stemUp e4 -> r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis16 ( \stemUp e16 \stemUp f16 }
    \stemUp g32 \stemUp as32 \stemUp bes32 \stemUp c32 ) | % 133
    \stemDown cis4 -> ^ "unis." \stemUp c8 -- \stemUp ais8 -- \stemUp
    gis8 ( -- \stemUp g8 ) -- | % 134
    \stemUp e4 -> r4 r4 \pageBreak | % 135
    \stemUp g4 -> _\f r4 r4 | % 136
    \stemDown cis8 ( -> _\mf \stemDown d8 ) r4 r4 | % 137
    R2.*10 \pageBreak | % 147
    R2. | % 148
    r4 ^ "con sordini" r4 \stemUp b4 -- _\f _\< | % 149
    \stemUp b4 -- _\! _\sff _\> \stemUp ais4 ( _\! \stemUp a4 ) |
    \barNumberCheck #150
    \stemUp g8 r8 r4 \stemUp b4 -- _\f _\< | % 151
    \stemUp b4 -- _\! _\sff _\> \stemUp ais4 ( _\! \stemUp a4 ) | % 152
    \stemUp g2 _\sf _\> \stemUp fis4 -- \pageBreak | % 153
    R2.*6 \break | % 159
    R2.*6 \break | % 165
    R2.*7 \bar "|."
    _\! }

PartPOneEightVoiceTwo =  \relative d' {
    \clef "alto" \time 3/4 \key d \major s4*21 \pageBreak s1*6 \break
    s1*6 \pageBreak s4*27 \break s1*6 \pageBreak s2*9 \break s2*9
    \pageBreak s2*9 \pageBreak s4*11 \stemDown d4 -- | % 63
    \stemDown d4 -- \stemDown cis4 ( \stemDown b4 ) | % 64
    \stemDown a2 \stemDown d4 -- \pageBreak | % 65
    \stemDown d4 -- \stemDown cis4 ( \stemDown b4 ) | % 66
    \stemDown a2 \stemDown d4 -- | % 67
    \stemDown dis4 ( \stemDown e4 ) \stemDown e4 -- | % 68
    \stemDown eis4 ( \stemDown fis4 ) \stemDown fis4 -- | % 69
    \stemDown fis4 ( \stemDown g4 ) \stemDown g4 -- | \barNumberCheck
    #70
    \stemDown gis4 ( \stemDown a4 ) \stemDown ais4 -- \pageBreak | % 71
    \stemDown b2. ~ -> | % 72
    \stemDown b8 \stemDown a8 -- \stemDown g8 -- \stemDown fis8 --
    \stemDown e8 -- \stemDown d8 -- | % 73
    \stemDown g2. ~ -> | % 74
    \stemDown g8 \stemDown fis8 -- \stemDown e8 -- \stemDown d8 --
    \stemDown c8 -- \stemDown b8 -- | % 75
    \stemDown e2. ~ -> | % 76
    \stemDown e8 \stemDown d8 -- \stemDown c8 -- \stemDown b8 --
    \stemDown a8 -- \stemDown g8 -- \pageBreak | % 77
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown b8 \stemDown a8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 \stemDown f8 \stemDown e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown g8 \stemDown f8 }
    | % 78
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown d8 \stemDown c8 }
    \stemDown g'16 \stemDown f16 \stemDown e16 \stemDown d'16 \stemDown
    c16 \stemDown b16 \stemDown a16 \stemDown g16 s4*9 \pageBreak s1*6
    \break s4*27 \pageBreak s1*6 \break s4*21 \pageBreak s1*3 \pageBreak
    s1 \stemDown f'8 :32 \stemDown e8 :32 \stemDown d8 :32 \stemDown cis8
    :32 | \barNumberCheck #120
    \stemDown e2 :32 -> \stemDown d4 :32 \pageBreak s4 \stemDown d8 :32
    \stemDown cis8 :32 \stemDown b8 :32 \stemDown ais8 :32 | % 122
    \stemDown cis2 :32 \stemDown b4 :32 s4 \stemDown b8 :32 \stemDown a8
    :32 \stemDown g8 :32 \stemDown fis8 :32 \pageBreak | % 124
    \stemDown a2 :32 -> s4*13 \pageBreak s4*5 \once \omit TupletBracket
    \times 2/3  {
        \stemDown d,16 ( \stemDown e16 \stemDown f16 }
    \stemDown g32 \stemDown as32 \stemDown bes32 \stemDown c32 ) | % 131
    \stemDown cis4 -> \stemDown c8 -- \stemDown ais8 -- \stemDown gis8 (
    -- \stemDown g8 ) -- | % 132
    \stemDown e4 -> s4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown d16 ( \stemDown e16 \stemDown f16 }
    \stemDown g32 \stemDown as32 \stemDown bes32 \stemDown c32 ) s1.
    \pageBreak s1*9 \pageBreak s2*9 \pageBreak s2*9 \break s2*9 \break
    s4*21 \bar "|."
    }

PartPOneNineVoiceOne =  \relative e {
    \clef "alto" \time 3/4 \key d \major | % 1
    R2.*7 \pageBreak | % 8
    R2.*8 \break | % 16
    R2.*8 \pageBreak | % 24
    R2.*9 \break | % 33
    R2.*8 \pageBreak | % 41
    R2.*6 \break | % 47
    R2.*6 \pageBreak | % 53
    R2.*6 \pageBreak | % 59
    R2.*6 \pageBreak | % 65
    R2.*6 \pageBreak | % 71
    R2.*6 \pageBreak | % 77
    R2.*5 \pageBreak | % 82
    R2.*8 \break | \barNumberCheck #90
    R2.*9 \pageBreak | % 99
    R2.*8 \break | % 107
    R2.*7 \pageBreak | % 114
    R2.*4 \pageBreak | % 118
    R2.*3 \pageBreak | % 121
    R2.*3 \pageBreak | % 124
    R2.*5 \pageBreak | % 129
    R2.*6 \pageBreak | % 135
    R2.*12 \pageBreak | % 147
    R2.*6 \pageBreak | % 153
    \stemUp e2 _\sf _ "Vla." _ "(div.)" _\> \stemUp d4 -- _\! | % 154
    \stemUp cis2. _\sf _\> | % 155
    \stemUp d4 ~ _\! _\mf \stemUp d8 r8 \stemUp d4 -- _\< | % 156
    \stemUp e2 _\! _\sf _\> \stemUp e4 -- _\! | % 157
    \stemUp d2 \stemUp d4 -- _\< | % 158
    \stemUp e2 _\! _\sf _\> \stemUp e4 -- _\! \break | % 159
    \stemUp d4 ~ _ "Vla." _ "(div.)" \stemUp d8 r8 r4 | \barNumberCheck
    #160
    R2.*5 \break | % 165
    R2.*7 \bar "|."
    }

PartPTwoZeroVoiceOne =  \relative e {
    \clef "alto" \time 3/4 \key d \major | % 1
    R2.*7 \pageBreak | % 8
    R2.*8 \break | % 16
    R2.*8 \pageBreak | % 24
    R2.*9 \break | % 33
    R2.*8 \pageBreak | % 41
    R2.*6 \break | % 47
    R2.*6 \pageBreak | % 53
    R2.*6 \pageBreak | % 59
    R2.*6 \pageBreak | % 65
    R2.*6 \pageBreak | % 71
    R2.*6 \pageBreak | % 77
    R2.*5 \pageBreak | % 82
    R2.*8 \break | \barNumberCheck #90
    R2.*9 \pageBreak | % 99
    R2.*8 \break | % 107
    R2.*7 \pageBreak | % 114
    R2.*4 \pageBreak | % 118
    R2.*3 \pageBreak | % 121
    R2.*3 \pageBreak | % 124
    R2.*5 \pageBreak | % 129
    R2.*6 \pageBreak | % 135
    R2.*12 \pageBreak | % 147
    R2.*6 \pageBreak | % 153
    \stemUp e2 _\sf ^ "div." _\> \stemUp d4 -- _\! | % 154
    \stemUp cis2. _\sf _\> | % 155
    \stemUp d4 ~ _\! _\mf \stemUp d8 r8 \stemUp d4 -- _\< | % 156
    \stemUp c2 _\! _\sf _\> \stemUp cis4 -- _\! | % 157
    \stemUp d2 \stemUp d4 -- _\< | % 158
    \stemUp c2 _\! _\sf _\> \stemUp cis4 -- _\! \break | % 159
    \stemUp d2. | \barNumberCheck #160
    R2.*5 \break | % 165
    R2.*7 \bar "|."
    }

PartPTwoOneVoiceOne =  \relative gis' {
    \clef "tenor" \time 3/4 \key d \major | % 1
    \stemDown gis4 -- _\f -\markup{ \italic {largamente} } \stemDown
    cis,8 ( \stemDown eis8 ) \stemDown gis,8. ( _\> \stemDown b16 ) | % 2
    \stemUp fis2 ~ _\! _\mf _\> \stemUp fis8 _\! _\p r8 | % 3
    \stemDown gis'4 -- _\f \stemDown cis,8 ( \stemDown eis8 ) \stemDown
    gis,8. ( _\> \stemDown b16 ) | % 4
    \stemUp fis2 ~ _\! _\mf _\> \stemUp fis8 r8 _\! | % 5
    \clef "bass" \stemDown d4. ( _\p \stemUp d8 ) -- \stemUp d8. ( --
    \stemUp cis16 ) -- | % 6
    \stemDown d2 r4 | % 7
    \stemDown fis4. ( _\mp \stemDown fis8 ) -- \stemDown fis8. ( --
    \stemDown f16 ) -- \pageBreak | % 8
    \stemDown fis2 r4 | % 9
    \stemDown a4. ( _\mf _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemDown gis8 ) -- \stemDown a4 -- |
    \barNumberCheck #10
    \stemDown cis4. ( \stemDown c8 ) -- \stemDown cis4 -- | % 11
    \stemDown e4. ( \stemDown d8 ) -- \stemDown cis4 -- | % 12
    \stemDown b2. ~ \stopTrillSpan _\ff _\> | % 13
    \stemDown b8 _\! _\mf r8 \stemDown a4 ~ _\f _\> \stemDown a8 r8 _\!
    | % 14
    \stemDown gis4 ( _\mf _\> \stemDown g8 ) r8 _\! \stemDown fis8 (
    _\mp \stemDown f8 | % 15
    \stemDown e8 ) r8 \stemDown d4 ( _\p \stemUp cis8 ) r8 \break | % 16
    \stemDown b'2. ~ _\p _\> | % 17
    \stemDown b2 _\! _\pp \clef "tenor" \stemDown b'4 ~ _\pp _\< | % 18
    \stemDown b2 ~ _\! _\> \stemDown b8 _\! _\ppp r8 | % 19
    r4 r16 \clef "bass" \stemDown cis,,16 ( _\p _\< \stemDown b'16
    \stemDown g16 ) \clef "tenor" \stemDown d'16 ( \stemDown ais16 )
    \stemDown eis'16 ( \stemDown cis16 ) | \barNumberCheck #20
    \stemDown gis'4 -- _\! _\f \stemDown cis,8 ( \stemDown eis8 )
    \stemDown gis,8. ( _\> \stemDown b16 ) | % 21
    \stemUp fis2 ~ _\! _\mf _\> \stemUp fis8 _\! _\p r8 | % 22
    \stemDown gis'4 -- _\f \stemDown cis,8 ( \stemDown eis8 ) \stemDown
    gis,8. ( _\> \stemDown b16 ) | % 23
    \stemUp fis2 ~ _\! _\mf _\> \stemUp fis8 r8 _\! \pageBreak | % 24
    \clef "bass" \stemDown d4. ( _\p \stemUp d8 ) -- \stemUp d8. ( --
    \stemUp cis16 ) -- | % 25
    \stemDown d2 ~ \stemDown d8 r8 | % 26
    \stemDown <b g'>4. ( _\pp \stemDown <b g'>8 ) -- \stemDown <b g'>8.
    ( -- \stemDown <ais fis'>16 ) -- | % 27
    \stemUp <b d>2 ~ ~ \stemUp <b d>8 r8 | % 28
    \stemUp g4. ( _\pp _\< \stemUp g8 ) -- \stemUp g8. ( -- \stemUp fis16
    ) -- | % 29
    \stemUp g2 ~ \stemUp g8 r8 _\! | \barNumberCheck #30
    \stemUp <e g>2. ~ ~ _\mf _\< | % 31
    \stemUp <e g>2 ~ ~ _\! _\f \stemUp <e g>8 r8 | % 32
    r2 \stemUp <e g>4 ~ ~ _\mf \break | % 33
    \stemUp <e g>2. ~ ~ _\markup{ \small\italic {dim.} } \startTrillSpan
    | % 34
    \stemUp <e g>2. ~ ~ | % 35
    \stemUp <e g>2. ~ ~ | % 36
    \stemUp <e g>2 ~ ~ \stopTrillSpan _\pp _\> \stemUp <e g>8 r8 _\! | % 37
    R2. | % 38
    r4 r4 \stemDown d'4 -- _\pp | % 39
    \stemDown e2 \stemDown g4 -- _\< | \barNumberCheck #40
    \stemDown g4 ( _\! _\> \stemDown fis4 _\! \stemDown f4 ) \pageBreak
    | % 41
    \stemDown e2 \stemDown g4 -- _\< | % 42
    \stemDown g4 _\! _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown fis4 \stemDown e4 | % 43
    \stemDown dis4 ( \stemDown e4 ) \stemUp cis4 -- | % 44
    \stemUp cis4 ( \stemDown dis4 ) \stemUp fis,4 -- \stopTrillSpan _\mf
    | % 45
    \stemUp g2 \stemDown g'4 -- | % 46
    \stemDown g2 _\> \stemDown fis4 -- _\! _\p \break | % 47
    \stemDown e2 \stemDown f4 | % 48
    \stemDown fis2. | % 49
    \stemDown e2 \stemDown f4 | \barNumberCheck #50
    \stemDown fis2 \stemUp fis,4 -- | % 51
    \stemUp g2 _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp gis4 | % 52
    \stemUp a2 \stemUp ais4 \pageBreak | % 53
    \stemUp b2 \stemUp b4 -- | % 54
    \stemUp c4 ( \stemUp cis4 ) \stemDown d4 -- \stopTrillSpan _\mf | % 55
    \stemDown e2 \stemDown g4 -- _\< | % 56
    \stemDown g4 -- _\! _\> \stemDown fis4 ( _\! \stemDown f4 ) | % 57
    \stemDown e2 \stemDown g4 -- _\< | % 58
    \stemDown g4 -- _\! _\> \stemDown fis4 ( _\! \stemDown e4 )
    \pageBreak | % 59
    \stemDown dis4 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown e4 ) \stemUp cis4 -- | \barNumberCheck #60
    \stemUp cis4 ( \stemDown dis4 ) \stemUp fis,4 -- | % 61
    \stemUp g2. ~ | % 62
    \stemUp g2 \clef "tenor" \stemDown d''4 -- \stopTrillSpan _\f _\< | % 63
    \stemDown d4 -- _\! _\> \stemDown cis4 ( _\! \stemDown b4 ) | % 64
    \stemDown a2 \stemDown d4 -- _\< \pageBreak | % 65
    \stemDown d4 -- _\! _\> \stemDown cis4 ( _\! \stemDown b4 ) | % 66
    \stemDown a2 \stemDown d4 -- | % 67
    \stemDown dis4 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown e4 ) \stemDown e4 -- | % 68
    \stemDown eis4 ( \stemDown fis4 ) \stemDown fis4 -- | % 69
    \stemDown fis4 ( \stopTrillSpan _\ff _\< \stemDown g4 ) \stemDown g4
    -- | \barNumberCheck #70
    \stemDown gis4 ( \stemDown a4 ) \stemDown ais4 -- \pageBreak | % 71
    \stemDown b2. ~ -> _\! _\fff | % 72
    \stemDown b8 \stemDown a8 -- \stemDown g8 -- \stemDown fis8 --
    \stemDown e8 -- \stemDown d8 -- | % 73
    \stemDown g2. ~ -> | % 74
    \stemDown g8 \stemDown fis8 -- \stemDown e8 -- \stemDown d8 --
    \stemDown c8 -- \stemDown b8 -- | % 75
    \stemDown e2. ~ _\sempre _\fff | % 76
    \stemDown e8 \stemDown d8 -- \stemDown c8 -- \stemDown b8 -- \stemUp
    a8 -- \stemUp g8 -- \pageBreak | % 77
    \clef "bass" \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown b8 \stemDown a8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g8 \stemDown f8 \stemDown e8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown a8 \stemDown g8 \stemDown f8 }
    | % 78
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown d8 \stemDown c8 }
    \stemDown g'16 \stemDown f'16 \stemDown e16 \stemDown d16 \stemDown
    c16 \stemDown b16 \stemDown a16 \stemDown g16 | % 79
    \stemDown e'16 \stemDown d16 \stemDown c16 \stemDown b16 \stemDown a16
    \stemDown g16 \stemDown f16 \stemDown e16 \once \omit TupletBracket
    \times 4/6  {
        \stemDown c'16 ( \stemDown b16 \stemDown a16 \stemDown g16
        \stemDown f16 \stemDown e16 ) }
    | \barNumberCheck #80
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown a16 ( \stemDown g16 \stemDown f16 \stemDown e16
        \stemDown d16 \stemDown c16 ) }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp e16 ( \stemUp d16 \stemUp c16 \stemUp b16 \stemUp a16
        \stemUp g16 ) }
    \once \omit TupletBracket
    \times 8/7  {
        \stemUp c32*161/160 ( \stemUp b32*161/160 \stemUp a32*161/160
        \stemUp g32*161/160 \stemUp f32*161/160 \stemUp e32*161/160
        \stemUp d32*161/160 ) }
    | % 81
    \stemUp c8 \stemUp c'8 r4 r4 ^\fermata \pageBreak | % 82
    r4 r4 \clef "tenor" \stemDown g''4 -- _\ff | % 83
    \stemDown g4 -- \stemDown fis4 ( \stemDown e4 ) | % 84
    \stemDown d4 -- r4 ^\fermata r4 | % 85
    \clef "bass" \stemUp b,4 -- _\f \stemUp cis4 ( \stemDown d4 ) | % 86
    \stemUp cis4 -- r4 ^\fermata r8 \stemDown dis8 ( _\mf _\< | % 87
    \stemDown e4 ) _\f r4 _\! r8 \stemUp cis8 ( _\p _\< | % 88
    \stemDown d4 ) _\! r4 \stemDown d4 ~ _\p | % 89
    \stemDown d4 ~ \stemDown d16 _\< \stemDown d16 ( \stemDown e16
    \stemDown fis16 ) \stemDown g16 ( \stemDown ais16 ) \stemDown b16
    \stemDown cis16 \break | \barNumberCheck #90
    \stemDown d4 -- _\! _\ff \stemDown cis8 -- \stemDown b8 -- \stemDown
    gis8. ( -- _\> \stemDown g16 ) -- | % 91
    \stemDown fis2 ~ _\! _\f _\> \stemDown fis8 _\! r8 | % 92
    \stemDown d'4 -- _\ff \stemDown cis8 -- \stemDown b8 -- \stemDown
    gis8. ( -- _\> \stemDown g16 ) -- | % 93
    \stemDown fis2 ~ _\! _\f _\> \stemDown fis8 _\! r8 | % 94
    \stemDown d4. ( _\p \stemUp d8 ) -- \stemUp d8. ( -- \stemUp cis16 )
    -- | % 95
    \stemDown d2 ~ \stemDown d8 r8 | % 96
    \stemDown b4. ( _\pp \stemDown g'4. \stemDown b,8 ) -- \stemDown g'8
    \stemDown b,8. ( -- \stemDown g'8. \stemDown ais,16 ) -- \stemDown
    fis'16 | % 97
    \stemUp b,2 ~ _\< \stemUp d2 ~ \stemUp b8 _\! \stemUp d8 r8 | % 98
    \stemUp g,2. _\mf _\markup{ \small\italic {cresc.} } \startTrillSpan
    \pageBreak | % 99
    \stemUp fis2. | \barNumberCheck #100
    \stemDown fis'4 ( \stopTrillSpan _\f _\< \stemDown e2 ) | % 101
    \stemDown cis'2. ~ _\! _\ff | % 102
    \stemDown cis2 ~ _\> \stemDown cis8 _\! _\mf r8 | % 103
    r8 \once \omit TupletBracket
    \times 2/3  {
        \stemUp ais,16 ( _\mf _\< \stemUp g'16 \stemUp g,16 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e'16 ( \stemDown eis16 \stemDown fis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown g16 \stemDown gis16 \stemDown a16 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown ais16 ( \stemDown b16 \stemDown c16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis16 \stemDown d16 \stemDown es16 ) }
    | % 104
    \stemDown d4 -- _\! _\ff \stemDown cis8 -- \stemDown b8 -- \stemDown
    gis8. ( -- _\> \stemDown g16 ) -- | % 105
    \stemDown fis2 ~ _\! _\f _\> \stemDown fis8 r8 _\! | % 106
    \stemDown d'4 -- _\ff \stemDown cis8 ( -- \stemDown b8 ) --
    \stemDown gis8. ( -- \stemDown g16 ) -- \break | % 107
    \stemDown fis2 ~ _\> \stemDown fis8 _\! r8 | % 108
    \stemDown e4 ( _\mf \stemUp d8 \stemUp cis8 ) \stemDown e4 | % 109
    \stemDown d4. ( \stemDown c'8 ) \stemDown b4 -- | \barNumberCheck
    #110
    \stemDown a4 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown g8 \stemDown fis8 ) \stemDown a4 -- | % 111
    \stemDown g4. ( \stemDown f8 ) \stemDown e4 -- | % 112
    \stemDown d2 \stemUp c4 ~ | % 113
    \stemUp c4 \stemUp b2 \pageBreak | % 114
    \stemDown a'16 r16 \stemDown g16 r16 \stemDown f16 r16 \stemDown e16
    r16 \times 2/3 {
        \stemDown bes'16 r8 }
    \times 2/3  {
        \stemDown a16 r8 }
    | % 115
    \times 2/3  {
        \stemDown g16 r8 }
    \times 2/3  {
        \stemDown f16 r8 }
    \stemDown c'8 :32 \stopTrillSpan _\fff \stemDown b8 :32 \stemDown a8
    :32 \stemDown gis8 :32 | % 116
    \stemDown b2 :32 -> \stemDown a4 :32 | % 117
    r4 \stemDown a8 :32 \stemDown g8 :32 \stemDown f8 :32 \stemDown e8
    :32 \pageBreak | % 118
    \stemDown g2 :32 -> \stemDown f4 :32 | % 119
    r4 \clef "tenor" \stemDown f'8 :32 \stemDown e8 :32 \stemDown d8 :32
    \stemDown cis8 :32 | \barNumberCheck #120
    \stemDown e2 :32 -> \stemDown d4 :32 \pageBreak | % 121
    r4 \stemDown d8 :32 \stemDown cis8 :32 \stemDown b8 :32 \stemDown
    ais8 :32 | % 122
    \stemDown cis2 :32 -> \stemDown b4 :32 | % 123
    r4 \clef "bass" \stemDown b8 :32 \stemDown a8 :32 \stemDown g8 :32
    \stemDown fis8 :32 \pageBreak | % 124
    \stemDown a2 :32 -> \stemDown g8 :32 \stemDown fis8 :32 | % 125
    \stemUp e8 :32 \stemUp d8 :32 \stemUp cis8 :32 \stemUp d8 :32
    \stemUp cis8 :32 \stemUp b8 :32 | % 126
    \stemUp b8 \stemUp d8 r8 r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown e16 ( _\fff \stemDown eis16 \stemDown fis16 }
    \stemDown gis32 \stemDown ais32 \stemDown b32 \stemDown cis32 ) | % 127
    \stemDown d4 -> \stemDown cis8 -- \stemDown b8 -- \stemDown ais8 --
    \stemDown gis8 -- | % 128
    \stemDown fis4 -> r4 \once \omit TupletBracket
    \times 2/3  {
        \stemDown e16 ( \stemDown eis16 \stemDown fis16 }
    \stemDown gis32 \stemDown ais32 \stemDown b32 \stemDown cis32 )
    \pageBreak | % 129
    \stemDown d4 -> \stemDown cis8 -- \stemDown b8 -- \stemDown ais8 (
    -- \stemDown gis8 ) -- | \barNumberCheck #130
    \stemDown fis4 -> r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp gis,16 ( \stemUp ais16 \stemUp b16 }
    \stemUp cis32 \stemUp d32 \stemUp e32 \stemUp fis32 ) | % 131
    \stemDown g4 -> \stemDown fis8 -- \stemDown e8 -- \stemUp d8 ( --
    \stemUp cis8 ) -- | % 132
    \stemUp b8 ( -> \stemUp ais8 ) r4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp gis16 ( \stemUp ais16 \stemUp b16 }
    \stemUp cis32 \stemUp d32 \stemUp e32 \stemUp fis32 ) | % 133
    \stemDown g4 -> \stemDown fis8 -- \stemDown e8 -- \stemUp d8 ( --
    \stemUp cis8 ) -- | % 134
    \stemUp b8 ( -> \stemUp ais8 ) r4 r4 \pageBreak | % 135
    \stemUp d8 ( -> _\f \stemUp cis8 ) r4 r4 | % 136
    \stemDown g'8 ( -> _\mf \stemDown fis8 ) r4 r4 | % 137
    R2.*10 \pageBreak | % 147
    R2. | % 148
    r4 ^ "con sordini" r4 \stemDown b4 -- _\f _\< | % 149
    \stemDown b4 -- _\! _\sff _\> \stemDown ais4 ( _\! \stemDown a4 ) |
    \barNumberCheck #150
    \stemDown g8 r8 r4 \stemDown b4 -- _\< | % 151
    \stemDown b4 -- _\! _\ff _\> \stemDown ais4 ( _\! _\f \stemDown a4 )
    | % 152
    \stemDown g2 _\sf _\> \stemDown fis4 -- \pageBreak | % 153
    R2.*2 | % 155
    r4 _\! r4 r4 | % 156
    R2.*3 \break | % 159
    R2.*6 \break | % 165
    R2.*7 \bar "|."
    }

PartPTwoTwoVoiceOne =  \relative e {
    \clef "bass" \time 3/4 \key d \major | % 1
    R2.*7 \pageBreak | % 8
    R2.*8 \break | % 16
    R2.*8 \pageBreak | % 24
    R2.*9 \break | % 33
    R2.*8 \pageBreak | % 41
    R2.*6 \break | % 47
    R2.*6 \pageBreak | % 53
    R2.*6 \pageBreak | % 59
    R2.*6 \pageBreak | % 65
    R2.*6 \pageBreak | % 71
    R2.*6 \pageBreak | % 77
    R2.*5 \pageBreak | % 82
    R2.*8 \break | \barNumberCheck #90
    R2.*9 \pageBreak | % 99
    R2.*8 \break | % 107
    R2.*7 \pageBreak | % 114
    R2.*4 \pageBreak | % 118
    R2.*3 \pageBreak | % 121
    R2.*3 \pageBreak | % 124
    R2.*5 \pageBreak | % 129
    R2.*6 \pageBreak | % 135
    R2.*12 \pageBreak | % 147
    R2.*6 \pageBreak | % 153
    \stemDown e2 _\sf _ "Vc." _ "(div.)" _\> \stemDown d4 -- _\! | % 154
    \stemUp cis2. _\sf _\> | % 155
    \stemDown d4 ~ _\! \stemDown d8 r8 \stemDown b'4 -- _\mf _\< | % 156
    \stemDown b4 ( _\! _\sf _\> \stemDown a4 \stemDown g4 ) _\! | % 157
    \stemDown fis2 \stemDown b4 -- _\< | % 158
    \stemDown b4 ( _\! _\sf _\> \stemDown a4 \stemDown g4 ) _\! \break | % 159
    \stemDown fis2 _ "Vc." _ "(div.)" \stemDown fis4 -- |
    \barNumberCheck #160
    \stemDown fis4 ( -> _\markup{ \small\italic {dim.} } \startTrillSpan
    \stemDown e4 ) \stemDown d4 -- | % 161
    \stemDown d4 ( -> \stemUp cis4 ) \stemUp b4 | % 162
    \stemUp b4 ( -> \stemUp a4 \stemUp g4 ) | % 163
    \stemUp fis2. \stopTrillSpan _\p _\< | % 164
    \stemUp <cis b'>2. _\! _\sf _\> \break | % 165
    \stemUp fis2. _\! _\p _ "Vc." _ "(div.)" _\< | % 166
    \stemUp <cis b'>2. _\! _\sf _\> | % 167
    \stemUp fis2. ~ _\! _\p _\markup{ \small\italic {dim.} }
    \startTrillSpan | % 168
    \stemUp fis2. ~ | % 169
    \stemUp fis2. ~ | \barNumberCheck #170
    \stemUp fis2. ~ \stopTrillSpan _\pppp | % 171
    \stemUp fis2 ~ _\> \stemUp fis8 _\! r8 ^\fermata \bar "|."
    }

PartPTwoThreeVoiceOne =  \relative e {
    \clef "bass" \time 3/4 \key d \major | % 1
    R2.*7 \pageBreak | % 8
    R2.*8 \break | % 16
    R2.*8 \pageBreak | % 24
    R2.*9 \break | % 33
    R2.*8 \pageBreak | % 41
    R2.*6 \break | % 47
    R2.*6 \pageBreak | % 53
    R2.*6 \pageBreak | % 59
    R2.*6 \pageBreak | % 65
    R2.*6 \pageBreak | % 71
    R2.*6 \pageBreak | % 77
    R2.*5 \pageBreak | % 82
    R2.*8 \break | \barNumberCheck #90
    R2.*9 \pageBreak | % 99
    R2.*8 \break | % 107
    R2.*7 \pageBreak | % 114
    R2.*4 \pageBreak | % 118
    R2.*3 \pageBreak | % 121
    R2.*3 \pageBreak | % 124
    R2.*5 \pageBreak | % 129
    R2.*6 \pageBreak | % 135
    R2.*12 \pageBreak | % 147
    R2.*6 \pageBreak | % 153
    \stemDown e2 _\sf ^ "div." _\> \stemDown d4 -- _\! | % 154
    \stemUp cis2. _\sf _\> | % 155
    \stemDown d4 ~ _\! \stemDown d8 r8 r4 | % 156
    r4 r4 \stemUp b4 -- _\mf _\< | % 157
    \stemUp b4 ( _\! _\sf _\> \stemUp ais4 _\! \stemUp a4 | % 158
    \stemUp g8 ) r8 r4 \stemUp b4 -- _\< \break | % 159
    \stemUp b4 ( _\! _\sf _\> \stemUp ais4 _\! \stemUp a4 ) |
    \barNumberCheck #160
    \stemUp g2 ( -> _\markup{ \small\italic {dim.} } \startTrillSpan
    \stemUp fis4 ) | % 161
    \stemUp e2 ( -> \stemUp d4 ) | % 162
    \stemUp cis2. -> | % 163
    \stemUp d2. \stopTrillSpan _\p _\< | % 164
    \stemUp <e g>2. _\! _\sf _\> \break | % 165
    \stemUp d2. _\! _\p _\< | % 166
    \stemUp <e g>2. _\! _\sf _\> | % 167
    \stemUp d2. ~ _\! _\p _\markup{ \small\italic {dim.} }
    \startTrillSpan | % 168
    \stemUp d2. ~ | % 169
    \stemUp d2. ~ | \barNumberCheck #170
    \stemUp d2. ~ \stopTrillSpan _\pppp | % 171
    \stemUp d2 ~ _\> \stemUp d8 _\! r8 ^\fermata \bar "|."
    }

PartPTwoFourVoiceOne =  \relative d {
    \clef "bass" \time 3/4 \key d \major \transposition c | % 1
    R2.*4 | % 5
    \stemDown d4. ( _\p \stemUp d8 ) -- \stemUp d8. ( -- \stemUp cis16 )
    -- | % 6
    \stemDown d2 r4 | % 7
    \stemDown fis4. ( _\mp \stemDown fis8 ) -- \stemDown fis8. ( --
    \stemDown eis16 ) -- \pageBreak | % 8
    \stemDown fis2 r4 | % 9
    \stemDown a4. ( _\mf _\markup{ \small\italic {cresc.} }
    \startTrillSpan \stemDown gis8 ) -- \stemDown a4 -- |
    \barNumberCheck #10
    \stemDown cis4. ( \stemDown bis8 ) -- \stemDown cis4 -- | % 11
    \stemDown e4. ( \stemDown d8 ) -- \stemDown cis4 -- | % 12
    \stemDown b2. ~ \stopTrillSpan _\ff _\> | % 13
    \stemDown b8 _\! _\mf r8 \stemDown a4 ~ _\f _\> \stemDown a8 r8 _\!
    | % 14
    \stemDown gis4 ( _\mf _\> \stemDown g8 ) r8 _\! \stemDown fis8 (
    _\mp \stemDown f8 | % 15
    \stemDown e8 ) r8 \stemDown d4 ( _\p \stemUp cis8 ) r8 \break | % 16
    \stemDown e'2. ~ _\p _\> | % 17
    \stemDown e2 _\! _\pp r4 | % 18
    R2.*6 \pageBreak | % 24
    \stemDown d,4. ( _\p \stemUp d8 ) -- \stemUp d8. ( -- \stemUp cis16
    ) -- | % 25
    \stemDown d2 ~ \stemDown d8 r8 | % 26
    \stemUp b4. ( _\pp \stemUp b8 ) -- \stemUp b8. ( -- \stemUp ais16 )
    -- | % 27
    \stemUp b2 ~ \stemUp b8 r8 | % 28
    \stemUp g4. ( _\pp _\< \stemUp g8 ) -- \stemUp g8. ( -- \stemUp fis16
    ) -- | % 29
    \stemUp g2 ~ \stemUp g8 r8 _\! | \barNumberCheck #30
    \stemUp e2. ~ _\mf _\< | % 31
    \stemUp e2 ~ _\! _\f \stemUp e8 r8 | % 32
    r2 \stemUp e4 ~ _\mf \break | % 33
    \stemUp e2. ~ _\markup{ \small\italic {dim.} } \startTrillSpan | % 34
    \stemUp e2. ~ | % 35
    \stemUp e2. ~ | % 36
    \stemUp e2 ~ \stopTrillSpan _\pp _\> \stemUp e8 r8 _\! | % 37
    R2. | % 38
    r2 \stemDown d'4 -- _\pp | % 39
    \stemDown e2 \stemDown g4 -- _\< | \barNumberCheck #40
    \stemDown g4 ( _\! _\> \stemDown fis4 _\! \stemDown f4 ) \pageBreak
    | % 41
    \stemDown e2 \stemDown g4 -- _\< | % 42
    \stemDown g4 _\! _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown fis4 \stemDown e4 | % 43
    \stemDown dis4 ( \stemDown e4 ) \stemUp cis4 -- | % 44
    \stemUp cis4 ( \stemDown dis4 ) \stemUp fis,4 -- \stopTrillSpan _\mf
    | % 45
    \stemUp g2 \stemDown g'4 -- | % 46
    \stemDown g2 _\> \stemDown fis4 -- _\! _\p \break | % 47
    \stemDown e2 \stemDown eis4 | % 48
    \stemDown fis2. | % 49
    \stemDown e2 \stemDown eis4 | \barNumberCheck #50
    \stemDown fis2 \stemUp fis,4 -- | % 51
    \stemUp g2 _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp gis4 | % 52
    \stemUp a2 \stemUp ais4 \pageBreak | % 53
    \stemUp b2 \stemUp b4 -- | % 54
    \stemUp c4 ( \stemUp cis4 ) \stemDown d4 -- \stopTrillSpan _\mf | % 55
    \stemDown e2 \stemDown g4 -- _\< | % 56
    \stemDown g4 -- _\! _\> \stemDown fis4 ( _\! \stemDown f4 ) | % 57
    \stemDown e2 \stemDown g4 -- _\< | % 58
    \stemDown g4 -- _\! _\> \stemDown fis4 ( _\! \stemDown e4 )
    \pageBreak | % 59
    \stemDown dis4 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown e4 ) \stemUp cis4 -- | \barNumberCheck #60
    \stemUp cis4 ( \stemDown dis4 ) \stemUp fis,4 -- | % 61
    \stemUp g2. ~ | % 62
    \stemUp g2 \stemUp fis4 -- \stopTrillSpan _\f | % 63
    \stemUp e2 \stemUp eis4 | % 64
    \stemUp fis2. \pageBreak | % 65
    \stemUp e2 \stemUp eis4 | % 66
    \stemUp fis2. | % 67
    \stemUp g2 _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemUp gis'4 -- ^ "div." | % 68
    \stemUp a2 \stemUp ais4 -- | % 69
    \stemUp b2 \stopTrillSpan _\ff _\< \stemUp b4 -- | \barNumberCheck
    #70
    \stemUp cis2. \pageBreak | % 71
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp d8 _\! _\fff \stemUp d8 \stemUp d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp d8 \stemUp d8 \stemUp d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp d8 \stemUp d8 \stemUp d8 ~ }
    | % 72
    \stemUp d8 r8 r4 r4 | % 73
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 _\fff \stemUp c8 \stemUp c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp c8 \stemUp c8 \stemUp c8 ~ }
    | % 74
    \stemUp c8 r8 r4 r4 | % 75
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e,8 _\sempre _\fff ^ "unis." \stemDown e8 \stemDown e8
        ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown e8 \stemDown e8 ~ }
    | % 76
    \stemDown e8 r8 r4 r4 \pageBreak | % 77
    \stemDown g16 r16 r8 r4 \stemDown c16 r16 r8 | % 78
    r4 \stemDown e16 r16 r8 r4 | % 79
    \stemDown g16 r16 r8 r4 r4 | \barNumberCheck #80
    R2. | % 81
    \stemDown c,,8 _\fff \stemDown c'8 r4 r4 ^\fermata \pageBreak | % 82
    R2. | % 83
    \stemUp ais,2. _\ff | % 84
    \stemUp b4 r4 ^\fermata r4 | % 85
    \stemDown eis2. _\f | % 86
    \stemDown fis4 -- r4 ^\fermata r8 \stemDown dis8 ( _\mf _\< | % 87
    \stemDown e4 ) _\! _\f r4 r8 \stemUp cis8 ( _\p _\< | % 88
    \stemDown d4 ) _\! r4 \stemDown d4 ~ _\p | % 89
    \stemDown d4 ~ \stemDown d8 r8 r4 \break | \barNumberCheck #90
    R2.*4 | % 94
    \stemDown d4. ( _\p \stemUp d8 ) -- \stemUp d8. ( -- \stemUp cis16 )
    -- | % 95
    \stemDown d2 ~ \stemDown d8 r8 | % 96
    \stemUp b4. ( _\pp \stemUp b8 ) -- \stemUp b8. ( -- \stemUp ais16 )
    -- | % 97
    \stemUp b2 ~ _\< \stemUp b8 _\! r8 | % 98
    \stemUp g2. _\mf _\markup{ \small\italic {cresc.} } \startTrillSpan
    \pageBreak | % 99
    \stemUp fis2. | \barNumberCheck #100
    \stemUp e2. \stopTrillSpan _\f _\< | % 101
    \stemDown e''2. ~ _\! _\ff | % 102
    \stemDown e2 ~ _\> \stemDown e8 _\! _\mf r8 | % 103
    r8 \once \omit TupletBracket
    \times 1/1  {
        \stemDown e,16 ( _\mf _\< \stemDown b'16 \stemDown cis16 }
    \stemDown e16 ) r8 _\! r4 | % 104
    R2.*3 \break | % 107
    R2.*2 | % 109
    \stemDown d4. ( \stemDown c8 ) \stemDown b4 -- | \barNumberCheck
    #110
    \stemDown a4 ( _\markup{ \small\italic {cresc.} } \startTrillSpan
    \stemDown g8 \stemDown fis8 ) \stemDown a4 -- | % 111
    \stemDown g4. ( \stemDown f8 ) \stemDown e4 -- | % 112
    \stemDown d2 \stemUp c4 ~ | % 113
    \stemUp c4 \stemUp b2 \pageBreak | % 114
    \stemUp bes4 \stemUp a4 \stemUp g4 | % 115
    \stemUp f4 \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stopTrillSpan _\fff \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    | % 116
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    | % 117
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \pageBreak | % 118
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    | % 119
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    | \barNumberCheck #120
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \pageBreak | % 121
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    | % 122
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    | % 123
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \pageBreak | % 124
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    | % 125
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e16 \stemUp e16 \stemUp e16 }
    | % 126
    \stemUp fis2. ~ _\fff | % 127
    \stemUp fis2. ~ | % 128
    \stemUp fis2. ~ \pageBreak | % 129
    \stemUp fis2. ~ | \barNumberCheck #130
    \stemUp fis2. ~ | % 131
    \stemUp fis2. ~ | % 132
    \stemUp fis2. ~ | % 133
    \stemUp fis2. ~ | % 134
    \stemUp fis2. ~ _\markup{ \small\italic {dim.} } \startTrillSpan
    \pageBreak | % 135
    \stemUp fis2. ~ | % 136
    \stemUp fis2. ~ | % 137
    \stemUp fis8 \stopTrillSpan _\p r8 r4 r4 | % 138
    R2.*9 \pageBreak | % 147
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 _\p _\< \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    | % 148
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 _\! _\mf \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    | % 149
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    | \barNumberCheck #150
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    | % 151
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    | % 152
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 }
    \pageBreak | % 153
    R2.*6 \break | % 159
    R2.*6 \break | % 165
    R2.*7 \bar "|."
    }

PartPTwoFourVoiceTwo =  \relative gis, {
    \clef "bass" \time 3/4 \key d \major \transposition c s4*21
    \pageBreak s1*6 \break s1*6 \pageBreak s4*27 \break s1*6 \pageBreak
    s2*9 \break s2*9 \pageBreak s2*9 \pageBreak s2*9 \pageBreak s1*2
    \stemDown gis4 -- | % 68
    \stemDown a2 \stemDown ais4 -- | % 69
    \stemDown b2 \stemDown b4 -- | \barNumberCheck #70
    \stemDown cis2. \pageBreak | % 71
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown d8 \stemDown d8 \stemDown d8 ~ }
    | % 72
    \stemDown d8 s8*5 | % 73
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown c8 \stemDown c8 \stemDown c8 ~ }
    | % 74
    \stemDown c8 s8*17 \pageBreak s4*15 \pageBreak s1*6 \break s4*27
    \pageBreak s1*6 \break s4*21 \pageBreak s1*3 \pageBreak s4*9
    \pageBreak s4*9 \pageBreak s4*15 \pageBreak s2*9 \pageBreak s1*9
    \pageBreak s16*71 \once \override NoteHead.style = ##f \stemDown b32
    ~ \once \override NoteHead.style = ##f \stemDown b32 \pageBreak s2*9
    \break s2*9 \break s4*21 \bar "|."
    }

PartPTwoFiveVoiceOne =  \relative b, {
    \clef "bass" \time 3/4 \key d \major \transposition c | % 1
    R2.*7 \pageBreak | % 8
    R2.*8 \break | % 16
    R2.*8 \pageBreak | % 24
    R2.*9 \break | % 33
    R2.*8 \pageBreak | % 41
    R2.*6 \break | % 47
    R2.*6 \pageBreak | % 53
    R2.*6 \pageBreak | % 59
    R2.*6 \pageBreak | % 65
    R2.*6 \pageBreak | % 71
    R2.*6 \pageBreak | % 77
    R2.*5 \pageBreak | % 82
    R2.*8 \break | \barNumberCheck #90
    R2.*9 \pageBreak | % 99
    R2.*8 \break | % 107
    R2.*7 \pageBreak | % 114
    R2.*4 \pageBreak | % 118
    R2.*3 \pageBreak | % 121
    R2.*3 \pageBreak | % 124
    R2.*5 \pageBreak | % 129
    R2.*6 \pageBreak | % 135
    R2.*12 \pageBreak | % 147
    R2.*6 \pageBreak | % 153
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 _ "Cb." _ "(div.)" \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    | % 154
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    | % 155
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \stemUp b8 r8 \stemDown fis'4 -- _\mf _\< | % 156
    \stemDown g2 _\! _\sf _\> \stemDown fis4 -- _\! | % 157
    \stemDown fis2 \stemDown fis4 -- _\< | % 158
    \stemDown g2 _\! _\> \stemDown fis4 -- _\! \break | % 159
    \stemDown fis2 _ "Cb." _ "(div.)" \stemDown fis4 -- |
    \barNumberCheck #160
    \stemDown b2. -> _\markup{ \small\italic {dim.} } \startTrillSpan | % 161
    \stemDown ais2 ( -> \stemDown b4 ) | % 162
    \stemDown e,2. -> | % 163
    \stemDown d4 ~ \stopTrillSpan _\p _\> \stemDown d8 _\! r8 r4 | % 164
    \once \omit TupletBracket
    \times 2/3  {
        r8 \stemUp b8 _\p \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \break | % 165
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 _ "Cb." _ "(div.)" \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    | % 166
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    | % 167
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 _\markup{ \small\italic {dim.} } \startTrillSpan
        \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    | % 168
    \stemUp b8 \stemUp b8 ~ \stemUp b8 \stemUp b8 ~ \stemUp b8 \stemUp b8
    ~ | % 169
    \stemUp b4 \stemUp b2 | \barNumberCheck #170
    \stemUp b2 \stopTrillSpan _\pppp \stemUp b4 ~ | % 171
    \stemUp b2 ~ _\> \stemUp b8 _\! r8 ^\fermata \bar "|."
    }

PartPTwoFiveVoiceTwo =  \relative b, {
    \clef "bass" \time 3/4 \key d \major \transposition c s4*21
    \pageBreak s1*6 \break s1*6 \pageBreak s4*27 \break s1*6 \pageBreak
    s2*9 \break s2*9 \pageBreak s2*9 \pageBreak s2*9 \pageBreak s2*9
    \pageBreak s2*9 \pageBreak s4*15 \pageBreak s1*6 \break s4*27
    \pageBreak s1*6 \break s4*21 \pageBreak s1*3 \pageBreak s4*9
    \pageBreak s4*9 \pageBreak s4*15 \pageBreak s2*9 \pageBreak s1*9
    \pageBreak s2*9 \pageBreak | % 153
     \once \override NoteHead.style = ##f \stemDown b32 ~ \once
    \override NoteHead.style = ##f \stemDown b32 s16*71 \break s2*9
    \break s4*21 \bar "|."
    }

PartPTwoSixVoiceOne =  \relative b, {
    \clef "bass" \time 3/4 \key d \major \transposition c | % 1
    R2.*7 \pageBreak | % 8
    R2.*8 \break | % 16
    R2.*8 \pageBreak | % 24
    R2.*9 \break | % 33
    R2.*8 \pageBreak | % 41
    R2.*6 \break | % 47
    R2.*6 \pageBreak | % 53
    R2.*6 \pageBreak | % 59
    R2.*6 \pageBreak | % 65
    R2.*6 \pageBreak | % 71
    R2.*6 \pageBreak | % 77
    R2.*5 \pageBreak | % 82
    R2.*8 \break | \barNumberCheck #90
    R2.*9 \pageBreak | % 99
    R2.*8 \break | % 107
    R2.*7 \pageBreak | % 114
    R2.*4 \pageBreak | % 118
    R2.*3 \pageBreak | % 121
    R2.*3 \pageBreak | % 124
    R2.*5 \pageBreak | % 129
    R2.*6 \pageBreak | % 135
    R2.*12 \pageBreak | % 147
    R2.*6 \pageBreak | % 153
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 ^ "div." \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    | % 154
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    | % 155
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 _\sempre _\mf \stemUp b8 \stemUp b8 ~ }
    | % 156
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    | % 157
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    | % 158
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \break | % 159
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    | \barNumberCheck #160
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 _\markup{ \small\italic {dim.} } \startTrillSpan
        \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    | % 161
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    | % 162
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    | % 163
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stopTrillSpan _\p \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp b8 \stemUp b8 ~ }
    | % 164
    \stemUp b8 r8 r4 r4 \break | % 165
    r4 \stemUp b8 _\p ^ "pizz." r8 r4 | % 166
    R2. | % 167
    r4 \stemUp b8 _\p _\> r8 r4 | % 168
    r4 \stemUp b8 r8 r4 | % 169
    r4 \stemUp b8 r8 r4 | \barNumberCheck #170
    \stemUp b8 r8 r4 \stemUp b8 _\! _\pppp r8 | % 171
    R2. \bar "|."
    }

PartPTwoSixVoiceTwo =  \relative b, {
    \clef "bass" \time 3/4 \key d \major \transposition c s4*21
    \pageBreak s1*6 \break s1*6 \pageBreak s4*27 \break s1*6 \pageBreak
    s2*9 \break s2*9 \pageBreak s2*9 \pageBreak s2*9 \pageBreak s2*9
    \pageBreak s2*9 \pageBreak s4*15 \pageBreak s1*6 \break s4*27
    \pageBreak s1*6 \break s4*21 \pageBreak s1*3 \pageBreak s4*9
    \pageBreak s4*9 \pageBreak s4*15 \pageBreak s2*9 \pageBreak s1*9
    \pageBreak s2*9 \pageBreak | % 153
     \once \override NoteHead.style = ##f \stemDown b32 ~ \once
    \override NoteHead.style = ##f \stemDown b32 s16*71 \break s2*9
    \break s4*21 \bar "|."
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
                        \context Voice = "PartPTwoVoiceOne" {  \PartPTwoVoiceOne }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "III"
                    \set Staff.shortInstrumentName = "III"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPThreeVoiceOne" {  \PartPThreeVoiceOne }
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
                        \context Voice = "PartPFiveVoiceOne" {  \voiceOne \PartPFiveVoiceOne }
                        \context Voice = "PartPFiveVoiceTwo" {  \voiceTwo \PartPFiveVoiceTwo }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "II"
                    \set Staff.shortInstrumentName = "II"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPSixVoiceOne" {  \voiceOne \PartPSixVoiceOne }
                        \context Voice = "PartPSixVoiceTwo" {  \voiceTwo \PartPSixVoiceTwo }
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
                \set RhythmicStaff.instrumentName = \markup { \center-column { \line {"Tamtam"} \line {"(ad lib.)"} } }
                \set RhythmicStaff.shortInstrumentName = "Tam"
                
                \context RhythmicStaff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneFiveVoiceOne" {  \voiceOne \PartPOneFiveVoiceOne }
                    \context Voice = "PartPOneFiveVoiceTwo" {  \voiceTwo \PartPOneFiveVoiceTwo }
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
                        \context Voice = "PartPOneSixVoiceOne" {  \PartPOneSixVoiceOne }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Violin II"
                    \set Staff.shortInstrumentName = "Vln. II"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneSevenVoiceOne" {  \voiceOne \PartPOneSevenVoiceOne }
                        \context Voice = "PartPOneSevenVoiceTwo" {  \voiceTwo \PartPOneSevenVoiceTwo }
                        >>
                    >>
                
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Viola"
                \set Staff.shortInstrumentName = "Vla."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneEightVoiceOne" {  \voiceOne \PartPOneEightVoiceOne }
                    \context Voice = "PartPOneEightVoiceTwo" {  \voiceTwo \PartPOneEightVoiceTwo }
                    >>
                >>
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = "Violas"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneNineVoiceOne" {  \PartPOneNineVoiceOne }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Violas"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPTwoZeroVoiceOne" {  \PartPTwoZeroVoiceOne }
                        >>
                    >>
                
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Violoncello"
                \set Staff.shortInstrumentName = "Vc."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPTwoOneVoiceOne" {  \PartPTwoOneVoiceOne }
                    >>
                >>
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = "Violoncellos"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPTwoTwoVoiceOne" {  \PartPTwoTwoVoiceOne }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Violoncellos"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPTwoThreeVoiceOne" {  \PartPTwoThreeVoiceOne }
                        >>
                    >>
                
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Contrabass"
                \set Staff.shortInstrumentName = "Cb."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPTwoFourVoiceOne" {  \voiceOne \PartPTwoFourVoiceOne }
                    \context Voice = "PartPTwoFourVoiceTwo" {  \voiceTwo \PartPTwoFourVoiceTwo }
                    >>
                >>
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = "Contrabasses"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPTwoFiveVoiceOne" {  \voiceOne \PartPTwoFiveVoiceOne }
                        \context Voice = "PartPTwoFiveVoiceTwo" {  \voiceTwo \PartPTwoFiveVoiceTwo }
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
            
            >>
        
        >>
    \layout {}
    % To create MIDI output, uncomment the following line:
    %  \midi {\tempo 4 = 50 }
    }

