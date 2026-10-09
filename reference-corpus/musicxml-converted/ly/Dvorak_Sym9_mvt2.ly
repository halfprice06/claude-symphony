\version "2.24.3"
% automatically converted by musicxml2ly from ../xml/Dvorak_Sym9_mvt2.musicxml
\pointAndClickOff

%% additional definitions required by the score:
ffz = #(make-dynamic-script "ffz")
fz = #(make-dynamic-script "fz")

\header {
    title =  "Symphony No. 9"
    composer =  "Antonin Dvořák"
    encodingsoftware =  "MuseScore 4.2.1"
    encodingdate =  "2024-06-30"
    source =  "https://musescore.com/score/4602736"
    subtitle =  "II - Largo"
    }

#(set-global-staff-size 13.714285714285715)
\paper {
    
    paper-width = 21.01\cm
    paper-height = 39.85\cm
    top-margin = 1.0\cm
    bottom-margin = 2.0\cm
    left-margin = 0.5\cm
    right-margin = 0.5\cm
    indent = 2.1933516483516486\cm
    short-indent = 1.500714285714286\cm
    }
\layout {
    \context { \Score
        skipBars = ##t
        }
    }
PartPOneVoiceOne =  \relative f' {
    \clef "treble" \time 4/4 \key des \major | % 1
    \tempo "Largo" 4=52 R1*7 \pageBreak | % 8
    R1*6 \pageBreak | % 14
    R1*6 \pageBreak | \barNumberCheck #20
    R1 | % 21
    \mark \markup { 1 } r2 \once \omit TupletBracket
    \times 2/3  {
        r8 _\pp \stemUp f8 ( \stemUp as8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown des8 \stemDown f8 \stemDown as8 ) }
    | % 22
    \stemDown des2 ( \stemDown d2 ) | % 23
    \stemDown des2 ( \stemDown d2 ) _\markup{ \italic {cresc.} } | % 24
    \stemDown des2 _\fz \stemDown es2 _\! _\< | % 25
    f1 ~ -> _\ff | % 26
    \stemDown f4 r4 r2 \pageBreak | % 27
    R1*5 \pageBreak | % 32
    R1*2 | % 34
    \time 2/4  R2 | % 35
    \time 4/4  R1*2 \pageBreak | % 37
    R1*5 \pageBreak | % 42
    R1*4 \bar "||"
    \pageBreak | % 46
    \key b \major \once \omit TupletBracket
    \times 2/3  {
        \stemDown e,8 ( _\pp \stemDown dis8 \stemDown cis8 }
    \stemDown cis4 ~ \stemDown cis8 \stemDown e8 \stemDown dis8
    \stemDown cis8 ) | % 47
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( _\< \stemDown dis8 \stemDown cis8 }
    \stemDown cis4 ~ \stemDown cis8 \stemDown e8 \stemDown dis8
    \stemDown cis8 ) | % 48
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 ( _\! \stemUp gis8 \stemUp b8 }
    \stemDown cis4 _\f \stemDown a16 \stemDown cis16 \stemDown b16
    \stemDown a16 \stemDown b4 ) | % 49
    \stemUp gis4 ( _\> \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp gis8 \stemUp b8 }
    \stemDown cis2 ) _\! _\p | \barNumberCheck #50
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( _\p \stemDown dis8 \stemDown cis8 }
    \stemDown cis4 ~ \stemDown cis8 _\< \stemDown e8 \stemDown dis8
    \stemDown cis8 ) | % 51
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( _\! \stemDown dis8 \stemDown cis8 }
    \stemDown cis4 ~ _\markup{ \italic {cresc.} } \stemDown cis8
    \stemDown e8 \stemDown dis8 \stemDown cis8 ) | % 52
    \stemDown cis16 ( _\< \stemDown e16 ) \stemDown gis16 -. \stemDown
    gis16 -. \stemDown gis4. \stemDown fis8 \once \omit TupletBracket
    \times 4/5  {
        \stemDown e16 ( \stemDown fis16 \stemDown a16 \stemDown gis16
        \stemDown fis16 }
    \pageBreak | % 53
    cis'1 ) ^^ _\! _\f _\> | % 54
    R1*3 \pageBreak | % 57
    R1*2 | % 59
    \stemDown e,2 ( _\! _\p _\< \stemDown fis4 \stemDown gis4 |
    \barNumberCheck #60
    \stemDown b4. \stemDown cis16 \stemDown b16 \stemDown b16 _\!
    \stemDown gis8. ~ \stemDown gis4 ) \pageBreak | % 61
    \stemDown fis4. ( _\p _\> \stemDown gis8 \stemDown a4 _\markup{
        \italic {dim.} } \stemDown e4 ) _\! | % 62
    \stemDown e2 ( _\pp \stemDown fis4 \stemDown e8. \prall \stemDown
    cis16 | % 63
    cis1 ~ _\> \pageBreak | % 64
    \stemDown cis8 ) _\! r8 ^\pp \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( \stemDown dis8 \stemDown e8 }
    \stemDown fis2 | % 65
    \stemDown gis8 ) r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis,8 ( ^\< \stemDown dis8 \stemDown e8 }
    \stemDown fis2 ) | % 66
    \stemDown gis2 ( \stemDown a4 ) ^\! ^\f \stemDown gis4 ~ | % 67
    \stemDown gis8 ( ^\markup{ \italic {dim.} } \stemDown fis8 ^\>
    \stemDown dis8 \stemDown e8 ~ \stemDown e8 \stemDown fis8 \stemDown
    e8 \stemDown dis8 \pageBreak | % 68
    \stemDown cis8 ) ^\! r8 \times 2/3 {
        \stemUp e8 ( ^\p ^\< \stemUp fis8 \stemUp gis8 }
    \stemDown a2 | % 69
    \stemDown gis8 ) ^\! r8 \times 2/3 {
        \stemUp e8 ( ^\< \stemUp fis8 \stemUp gis8 }
    \acciaccatura { \stemUp b8 } \stemDown a2 ) ^\! ^\f |
    \barNumberCheck #70
    \acciaccatura { \stemUp b8 ( } \stemDown a2 ) ^\< \acciaccatura {
        \stemUp e'8 ( } \stemDown d2 ) | % 71
    \acciaccatura { \stemUp a'8 ( } \stemDown gis2. ) ( ^\! ^\fz ^\>
    \stemDown e8 \stemDown cis8 ) \pageBreak | % 72
    \stemDown bis8 ^\! r8 r4 r2 | % 73
    R1*6 \pageBreak | % 79
    R1*5 \pageBreak | % 84
    R1*6 \pageBreak | \barNumberCheck #90
    R1 | % 91
    \stemDown gis8 ( \trill ^ "#" ^\p \stemDown cis16 ) r16 \stemDown
    bis8 ( \trill \stemDown cis16 ) r16 \stemDown fis16 ( \prall
    \stemDown dis16 \stemDown cis16 ) r16 \stemDown bis8 ( \trill
    \stemDown cis16 ) r16 \pageBreak | % 92
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown eis16 -. \stemDown fis16 -. \stemDown gis16 -.
        \stemDown eis16 -. \stemDown dis16 -. \stemDown cis16 -. }
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown dis16 -. \stemDown eis16 -. \stemDown fis16 -.
        \stemDown eis16 -. \stemDown dis16 -. \stemDown cis16 -. }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown dis16 -. -> \stemDown eis16 -. \stemDown fis16 -. }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown eis16 -. -> \stemDown gis16 -. r16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis16 -. \stemDown eis16 -. \stemDown dis16 -. }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown eis16 -. \stemDown cis16 -. r16 }
    | % 93
    gis'1 \startTrillSpan \stopTrillSpan ^ "#" ^\markup{ \italic
        {cresc.} } ^\< \pageBreak | % 94
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown gis16 ^\! ^ "a 2" _\mf \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 _\markup{ \italic {cresc.} } \stemDown gis16
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 _\< \stemDown gis16 \stemDown gis16 \stemDown
        gis16 \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 ~ }
    | % 95
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown gis16 _\! ^ "a 2" _\f \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 \stemDown gis16 ~ }
    _\< \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 }
    \pageBreak | % 96
    \stemDown e2 ~ _\! _\ff \stemDown e8 r8 r4 | % 97
    r4 \stemDown a,16. ^ "a 2" _\ff \stemDown cis32 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown e16 -. \stemDown e16 -. \stemDown e16 -. }
    \stemDown e2 | % 98
    r4 \stemDown a,16. _\markup{ \italic {dim.} } \stemDown cis32 \once
    \omit TupletBracket
    \times 2/3  {
        \stemDown e16 -. \stemDown e16 -. \stemDown e16 -. }
    \stemDown e4 \stemDown a,16. \stemDown cis32 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown e16 -. \stemDown e16 -. \stemDown e16 -. }
    | % 99
    e1 ~ _\> \pageBreak | \barNumberCheck #100
    \stemDown e8 _\! r8 r4 r2 | % 101
    R1*6 \pageBreak | % 107
    R1*6 \pageBreak | % 113
    R1*6 \pageBreak | % 119
    R1*6 | % 125
    f1 ~ _\pp | % 126
    \stemDown f4 r4 r2 | % 127
    R1 \bar "|."
    }

PartPTwoVoiceOne =  \relative f' {
    \clef "treble" \time 4/4 \key des \major | % 1
    R1*7 \pageBreak | % 8
    R1*6 \pageBreak | % 14
    R1*6 \pageBreak | \barNumberCheck #20
    R1 s1*7/12 \stemUp f8*2/3 ( \stemUp as8*2/3 \once \omit
    TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown des8 \stemDown f8 \stemDown as8 ) }
    | % 22
    \stemDown as2 ( \stemDown g2 ) | % 23
    \stemDown as2 ( \stemDown bes2 ) _\markup{ \italic {cresc.} } | % 24
    \stemDown bes2 _\fz \stemDown es2 _\! _\< | % 25
    des1 ~ -> _\ff | % 26
    \stemDown des4 r4 r2 \pageBreak | % 27
    R1*5 \pageBreak | % 32
    R1*2 | % 34
    \time 2/4  R2 | % 35
    \time 4/4  R1*2 \pageBreak | % 37
    R1*5 \pageBreak | % 42
    R1*4 \bar "||"
    \pageBreak | % 46
    \key b \major \once \omit TupletBracket
    \times 2/3  {
        \stemDown e,8 ( _\pp \stemDown dis8 \stemDown cis8 }
    \stemDown cis4 ~ \stemDown cis8 \stemDown e8 \stemDown dis8
    \stemDown cis8 ) | % 47
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( _\< \stemDown dis8 \stemDown cis8 }
    \stemDown cis4 ~ \stemDown cis8 \stemDown e8 \stemDown dis8
    \stemDown cis8 ) | % 48
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 ( _\! \stemUp gis8 \stemUp b8 }
    \stemDown cis4 _\f \stemDown a16 \stemDown cis16 \stemDown b16
    \stemDown a16 \stemDown b4 ) | % 49
    \stemUp gis4 ( _\> \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp gis8 \stemUp b8 }
    \stemDown cis2 ) _\! _\p | \barNumberCheck #50
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( _\p \stemDown dis8 \stemDown cis8 }
    \stemDown cis4 ~ \stemDown cis8 _\< \stemDown e8 \stemDown dis8
    \stemDown cis8 ) | % 51
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( _\! \stemDown dis8 \stemDown cis8 }
    \stemDown cis4 ~ _\markup{ \italic {cresc.} } \stemDown cis8
    \stemDown e8 \stemDown dis8 \stemDown cis8 ) | % 52
    \stemDown cis16 ( _\< \stemDown e16 ) \stemDown gis16 -. \stemDown
    gis16 -. \stemDown gis4. \stemDown fis8 \once \omit TupletBracket
    \times 4/5  {
        \stemDown e16 ( \stemDown fis16 \stemDown a16 \stemDown gis16
        \stemDown fis16 }
    \pageBreak | % 53
    cis'1 ) ^^ _\! _\f _\> | % 54
    R1*3 \pageBreak | % 57
    R1*2 | % 59
    \stemDown cis,2 _\! _\p \stemDown dis4 \stemDown e4 |
    \barNumberCheck #60
    \stemDown dis2 \stemDown e2 \pageBreak | % 61
    \stemUp a,4. ( \stemDown d8 \stemDown cis2 ) | % 62
    \stemDown cis2. ( \stemUp bis8 \stemUp gis8 | % 63
    cis1 ~ \pageBreak | % 64
    \stemDown cis8 ) s8 r4 r2 | % 65
    R1*3 \pageBreak | % 68
    R1*4 \pageBreak | % 72
    R1*7 \pageBreak | % 79
    R1*5 \pageBreak | % 84
    R1*6 \pageBreak | \barNumberCheck #90
    R1*2 \pageBreak | % 92
    R1*2 \pageBreak | % 94
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown gis''16 ^ "a 2" _\mf \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 _\markup{ \italic {cresc.} } \stemDown gis16
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 _\< \stemDown gis16 \stemDown gis16 \stemDown
        gis16 \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 ~ }
    | % 95
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown gis16 _\! ^ "a 2" _\f \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 \stemDown gis16 ~ }
    _\< \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 }
    \pageBreak | % 96
    \stemDown e2 ~ _\! _\ff \stemDown e8 r8 r4 | % 97
    r4 \stemDown a,16. ^ "a 2" _\ff \stemDown cis32 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown e16 -. \stemDown e16 -. \stemDown e16 -. }
    \stemDown e2 | % 98
    r4 \stemDown a,16. _\markup{ \italic {dim.} } \stemDown cis32 \once
    \omit TupletBracket
    \times 2/3  {
        \stemDown e16 -. \stemDown e16 -. \stemDown e16 -. }
    \stemDown e4 \stemDown a,16. \stemDown cis32 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown cis16 -. \stemDown cis16 -. \stemDown cis16 -. }
    | % 99
    cis1 ~ _\> \pageBreak | \barNumberCheck #100
    \stemDown cis8 _\! r8 r4 r2 | % 101
    R1*4 | % 105
     \once \override NoteHead.style = ##f \stemNeutral es,,2 s2 | % 106
    R1 \pageBreak | % 107
    R1*4 | % 111
     \once \override NoteHead.style = ##f \stemNeutral e2 s2 | % 112
    R1 \pageBreak | % 113
    R1*3 | % 116
     \once \override NoteHead.style = ##f \stemNeutral es2 s2 | % 117
    R1*2 \pageBreak | % 119
    R1*6 | % 125
    des''1 ~ _\pp | % 126
    \stemDown des4 r4 r2 | % 127
    R1 \bar "|."
    }

PartPThreeVoiceOne =  \relative as' {
    \clef "treble" \time 4/4 \key des \major | % 1
    R1*7 \pageBreak | % 8
    R1*6 \pageBreak | % 14
    R1*6 \pageBreak | \barNumberCheck #20
    R1*2 | % 22
    \stemDown as2 ( _\pp \stemDown g2 ) | % 23
    \stemDown as2 ( \stemDown bes2 ) _\markup{ \italic {cresc.} } | % 24
    \stemDown bes2 ^\f _\fz \stemDown bes4 -> _\< \stemDown c4
    -> _\! | % 25
    des1 ~ -> _\ff | % 26
    \stemDown des4 r4 r2 \pageBreak | % 27
    R1*5 \pageBreak | % 32
    R1*2 | % 34
    \time 2/4  R2 | % 35
    \time 4/4  R1*2 \pageBreak | % 37
    R1*5 \pageBreak | % 42
    R1*4 \bar "||"
    \pageBreak | % 46
    \key b \major \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 ( _\pp \stemUp dis8 \stemUp cis8 }
    \stemUp cis4 ~ \stemUp cis8 \stemUp e8 \stemUp dis8 \stemUp cis8 ) | % 47
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 ( _\< \stemUp dis8 \stemUp cis8 }
    \stemUp cis4 ~ \stemUp cis8 \stemUp e8 \stemUp dis8 \stemUp cis8 ) | % 48
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 ( _\! \stemUp gis8 \stemUp b8 }
    \stemUp cis4 _\f \stemUp a16 \stemUp cis16 \stemUp b16 \stemUp a16
    \stemUp b4 ) | % 49
    \stemUp gis4 ( _\> \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp gis8 \stemUp b8 }
    \stemUp cis2 ) _\! _\p | \barNumberCheck #50
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 ( _\p \stemUp dis8 \stemUp cis8 }
    \stemUp cis4 ~ \stemUp cis8 _\< \stemUp e8 \stemUp dis8 \stemUp cis8
    ) | % 51
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( _\! \stemDown dis8 \stemDown cis8 }
    \stemDown cis4 ~ _\markup{ \italic {cresc.} } \stemDown cis8
    \stemDown e8 \stemDown dis8 \stemDown cis8 ) | % 52
    \stemDown cis16 ( _\< \stemDown e16 ) \stemDown gis16 -. \stemDown
    gis16 -. \stemDown gis4. \stemDown fis8 \once \omit TupletBracket
    \times 4/5  {
        \stemDown e16 ( \stemDown fis16 \stemDown a16 \stemDown gis16
        \stemDown fis16 }
    \pageBreak | % 53
    cis'1 ) ^^ _\! _\f _\> | % 54
    \stemUp gis,2 ( _\! _\pp \stemUp a4 \stemUp gis4 ) | % 55
    a1 ~ ^ "a 2" _\< | % 56
    \stemUp a4 _\! \stemUp gis2 ( ~ \stemUp gis8 _\markup{ \italic
        {dim.} } \stemUp a8 ) \pageBreak | % 57
    \stemUp a4 ( ^ "a 2" \stemUp fis4 \stemUp a4 ^\pp \stemUp gis4 ) | % 58
    gis1 _\> | % 59
    \stemDown e'2 ( _\! _\p _\< \stemDown fis4 \stemDown gis4 |
    \barNumberCheck #60
    \stemDown b4. _\! \stemDown cis16 \stemDown b16 \stemDown b16
    \stemDown gis8. ~ \stemDown gis4 ) \pageBreak | % 61
    \stemDown fis4. ( _\p _\> \stemDown gis8 \stemDown a4 _\markup{
        \italic {dim.} } \stemDown e4 ) _\! | % 62
    \stemDown e2 ( _\pp \stemDown fis4 \stemDown e8. \prall \stemDown
    cis16 | % 63
    cis1 ~ _\> \pageBreak | % 64
    \stemDown cis8 ) _\! r8 ^\pp \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( \stemDown dis8 \stemDown e8 }
    \stemDown fis2 | % 65
    \stemDown gis8 ) r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis,8 ( ^\< \stemDown dis8 \stemDown e8 }
    \stemDown fis2 ) | % 66
    \stemDown gis2 ( \stemDown a4 ) ^\! ^\f \stemDown gis4 ~ | % 67
    \stemDown gis8 ( ^\markup{ \italic {dim.} } \stemDown fis8 ^\>
    \stemDown dis8 \stemDown e8 ~ \stemDown e8 \stemDown fis8 \stemDown
    e8 \stemDown dis8 \pageBreak | % 68
    \stemDown cis8 ) ^\! r8 \times 2/3 {
        \stemUp e8 ( ^\p ^\< \stemUp fis8 \stemUp gis8 }
    \stemDown a2 | % 69
    \stemDown gis8 ) ^\! r8 \times 2/3 {
        \stemUp e8 ( ^\< \stemUp fis8 \stemUp gis8 }
    \acciaccatura { \stemUp b8 } \stemDown a2 ) ^\! ^\f |
    \barNumberCheck #70
    \acciaccatura { \stemUp b8 ( } \stemDown a2 ) ^\< \acciaccatura {
        \stemUp e8 ( } \stemDown d2 ) | % 71
    \acciaccatura { \stemUp a'8 ( } \stemDown gis2. ) ( ^\! ^\fz ^\>
    \stemDown e8 \stemDown cis8 ) \pageBreak | % 72
    \stemDown bis8 ^\! r8 r4 r2 | % 73
    R1*6 \pageBreak | % 79
    R1*5 \pageBreak | % 84
    R1*6 \pageBreak | \barNumberCheck #90
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown eis16 -. ^\p ^ "Solo" \stemDown fis16 -.
        \stemDown gis16 -. \stemDown eis16 -. \stemDown dis16 -.
        \stemDown cis16 -. }
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown dis16 -. \stemDown eis16 -. \stemDown fis16 -.
        \stemDown eis16 -. \stemDown dis16 -. \stemDown cis16 -. }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown dis16 -. \stemDown eis16 -. \stemDown fis16 -. }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown eis16 -. \stemDown gis16 -. r16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis16 -. \stemDown eis16 -. \stemDown dis16 -. }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown eis16 -. \stemDown cis16 -. r16 }
    | % 91
    gis1 _\p ^ "a 2" \pageBreak | % 92
    \stemUp gis8 ( \trill ^ "#" \stemUp cis16 ) r16 \stemDown bis8 (
    \trill \stemDown cis16 ) r16 \stemDown fis16 ( \prall \stemDown dis16
    \stemDown cis16 ) r16 \stemDown bis8 ( \trill \stemDown cis16 ) r16
    | % 93
    gis'1 \startTrillSpan \stopTrillSpan ^ "a 2" ^ "#" _\< _\markup{
        \italic {cresc.} } \pageBreak | % 94
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown gis16 _\! _\mf \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 _\markup{ \italic {cresc.} } \stemDown gis16
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 _\< \stemDown gis16 \stemDown gis16 \stemDown
        gis16 \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 ~ }
    | % 95
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown gis16 _\! ^ "a 2" _\f \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 \stemDown gis16 ~ }
    _\< \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 }
    \pageBreak | % 96
    \stemDown a2 ~ _\! _\ff \stemDown a8 r8 r4 | % 97
    r4 \stemDown a,16. ^ "a 2" _\ff \stemDown cis32 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown e16 -. \stemDown e16 -. \stemDown e16 -. }
    \stemDown e2 | % 98
    r4 \stemDown a,16. _\markup{ \italic {dim.} } \stemDown cis32 \once
    \omit TupletBracket
    \times 2/3  {
        \stemDown e16 ^. \stemDown e16 ^. \stemDown e16 ^. }
    \stemDown e4 \stemDown a,16. \stemDown cis32 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown e16 ^. \stemDown e16 ^. \stemDown e16 ^. }
    | % 99
    e1 ~ _\> \pageBreak | \barNumberCheck #100
    \stemDown e8 _\! r8 r4 r2 | % 101
    R1*6 \pageBreak | % 107
    R1*6 \pageBreak | % 113
    r2 \stemDown as,8 ( ^\p \stemDown des8 \stemDown f8 \stemDown as8 | % 114
    \stemDown bes2 \stemDown as4. ) r8 | % 115
    R1*4 \pageBreak | % 119
    R1*5 | % 124
    f1 ( _\p | % 125
    as1 ) ~ _\pp | % 126
    \stemDown as4 r4 r2 | % 127
    R1 \bar "|."
    }

PartPThreeVoiceTwo =  \relative c' {
    \clef "treble" \time 4/4 \key des \major s1*7 \pageBreak s1*6
    \pageBreak s1*6 \pageBreak s1*7 \pageBreak s1*5 \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key b \major R1*5 s1*2 \pageBreak s1*4 \pageBreak s1*4 \pageBreak
    s1*3 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak s1*2 \pageBreak s1*2
    \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*6
    \pageBreak s1*9 \bar "|."
    }

PartPFourVoiceOne =  \relative as' {
    \clef "treble" \time 4/4 \key des \major | % 1
    R1*7 \pageBreak | % 8
    R1*6 \pageBreak | % 14
    R1*6 \pageBreak | \barNumberCheck #20
    R1*2 | % 22
    \stemDown as2 ( _\pp \stemDown g2 ) | % 23
    \stemDown as2 ( \stemDown bes2 ) _\markup{ \italic {cresc.} } | % 24
    \stemDown bes2 ^\f _\fz \stemDown bes4 -> _\< \stemDown c4
    -> _\! | % 25
    as1 -> _\ff | % 26
    \stemUp as4 s2. \pageBreak | % 27
    R1*5 \pageBreak | % 32
    R1*2 | % 34
    \time 2/4  R2 | % 35
    \time 4/4  R1*2 \pageBreak | % 37
    R1*5 \pageBreak | % 42
    R1*4 \bar "||"
    \pageBreak | % 46
    \key b \major \once \omit TupletBracket
    \times 2/3  {
        \stemUp e'8 ( _\pp \stemUp dis8 \stemUp cis8 }
    \stemUp cis4 ~ \stemUp cis8 \stemUp e8 \stemUp dis8 \stemUp cis8 ) | % 47
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 ( _\< \stemUp dis8 \stemUp cis8 }
    \stemUp cis4 ~ \stemUp cis8 \stemUp e8 \stemUp dis8 \stemUp cis8 ) | % 48
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 ( _\! \stemUp gis8 \stemUp b8 }
    \stemUp cis4 _\f \stemUp a16 \stemUp cis16 \stemUp b16 \stemUp a16
    \stemUp b4 ) | % 49
    \stemUp gis4 ( _\> \once \omit TupletBracket
    \times 2/3  {
        \stemUp b8 \stemUp gis8 \stemUp b8 }
    \stemUp cis2 ) _\! _\p | \barNumberCheck #50
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 ( _\p \stemUp dis8 \stemUp cis8 }
    \stemUp cis4 ~ \stemUp cis8 _\< \stemUp e8 \stemUp dis8 \stemUp cis8
    ) | % 51
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( _\! \stemDown dis8 \stemDown cis8 }
    \stemDown cis4 ~ \stemDown cis8 \stemDown e8 \stemDown dis8
    \stemDown cis8 ) | % 52
    \stemDown cis16 ( _\< \stemDown e16 ) \stemDown gis16 -. \stemDown
    gis16 -. \stemDown gis4. \stemDown fis8 \once \omit TupletBracket
    \times 4/5  {
        \stemDown e16 \stemDown fis16 \stemDown a16 \stemDown gis16
        \stemDown fis16 }
    \pageBreak | % 53
    cis'1 ^^ _\! _\f _\> | % 54
    \stemUp e,,2 ( _\! _\pp \stemUp a4 \stemUp gis4 ) | % 55
    a1 ~ ^ "a 2" _\< | % 56
    \stemUp a4 _\! \stemUp gis2 ( ~ \stemUp gis8 \stemUp a8 ) \pageBreak
    | % 57
    \stemUp a4 ( ^ "a 2" \stemUp fis4 \stemUp a4 ^\pp \stemUp gis4 ) | % 58
    gis1 _\> | % 59
    \stemDown cis2 _\! _\p _\< \stemDown dis4 \stemDown e4 |
    \barNumberCheck #60
    \stemDown dis2 _\! \stemDown e2 \pageBreak | % 61
    \stemUp a,4. ( \stemDown d8 \stemDown cis2 ) | % 62
    \stemDown cis2. \stemUp bis8 \stemUp gis8 | % 63
    cis1 \pageBreak | % 64
    \stemDown cis8 r8 ^\pp \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 ( \stemDown dis8 \stemDown e8 }
    \stemDown fis2 | % 65
    \stemDown gis8 ) r8 \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis,8 ( ^\< \stemDown dis8 \stemDown e8 }
    \stemDown fis2 ) | % 66
    \stemDown gis2 ( \stemDown a4 ) ^\! ^\f \stemDown gis4 ~ | % 67
    \stemDown gis8 ( \stemDown fis8 ^\> \stemDown dis8 \stemDown e8 ~
    \stemDown e8 \stemDown fis8 \stemDown e8 \stemDown dis8 \pageBreak | % 68
    \stemDown cis8 ) ^\! r8 \times 2/3 {
        \stemUp e8 ( ^\p ^\< \stemUp fis8 \stemUp gis8 }
    \stemDown a2 | % 69
    \stemDown gis8 ) ^\! r8 \times 2/3 {
        \stemUp e8 ( ^\< \stemUp fis8 \stemUp gis8 }
    \acciaccatura { \stemUp b8 } \stemDown a2 ) ^\! ^\f |
    \barNumberCheck #70
    \acciaccatura { \stemUp b8 ( } \stemDown a2 ) ^\< \acciaccatura {
        \stemUp e8 ( } \stemDown d2 ) | % 71
    \acciaccatura { \stemUp a'8 ( } \stemDown gis2. ) ( ^\! ^\fz ^\>
    \stemDown e8 \stemDown cis8 ) \pageBreak | % 72
    \stemDown bis8 ^\! r8 r4 r2 | % 73
    R1*6 \pageBreak | % 79
    R1*5 \pageBreak | % 84
    R1*6 \pageBreak | \barNumberCheck #90
    R1 | % 91
    gis1 _\p ^ "a 2" \pageBreak | % 92
    \stemUp gis8 ( \trill ^ "#" \stemUp cis16 ) r16 \stemDown bis8 (
    \trill \stemDown cis16 ) r16 \stemDown fis16 ( \prall \stemDown dis16
    \stemDown cis16 ) r16 \stemDown bis8 ( \trill \stemDown cis16 ) r16
    | % 93
    gis'1 \startTrillSpan \stopTrillSpan ^ "a 2" ^ "#" _\< \pageBreak | % 94
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown gis16 _\! _\mf \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 _\< \stemDown gis16 \stemDown gis16 \stemDown
        gis16 \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 ~ }
    | % 95
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown gis16 _\! ^ "a 2" _\f \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 \stemDown gis16 ~ }
    _\< \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 }
    \pageBreak | % 96
    \stemDown e2 ~ _\! _\ff \stemDown e8 r8 r4 | % 97
    r4 \stemDown a,16. ^ "a 2" _\ff \stemDown cis32 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown e16 -. \stemDown e16 -. \stemDown e16 -. }
    \stemDown e2 | % 98
    r4 \stemDown a,16. \stemDown cis32 \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis16 ^. \stemDown cis16 ^. \stemDown cis16 ^. }
    \stemDown cis4 \stemDown a16. \stemDown cis32 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown cis16 ^. \stemDown cis16 ^. \stemDown cis16 ^. }
    | % 99
    cis1 ~ _\> \pageBreak | \barNumberCheck #100
    \stemDown cis8 _\! r8 r4 r2 | % 101
    R1*6 \pageBreak | % 107
    R1*6 \pageBreak | % 113
    r2 \stemDown as8 ( ^\p \stemDown des8 \stemDown f8 \stemDown as8 | % 114
    \stemDown bes2 \stemDown as4. ) r8 | % 115
    R1*4 \pageBreak | % 119
    R1*5 | % 124
    des,1 ( ~ _\p | % 125
    des1 ) ~ _\pp | % 126
    \stemDown des4 r4 r2 | % 127
    R1 \bar "|."
    }

PartPFourVoiceTwo =  \relative c' {
    \clef "treble" \time 4/4 \key des \major s1*7 \pageBreak s1*6
    \pageBreak s1*6 \pageBreak s1*7 \pageBreak s1*5 \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key b \major R1*5 s1*2 \pageBreak s1*4 \pageBreak s1*4 \pageBreak
    s1*3 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak s1*2 \pageBreak s1*2
    \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*6
    \pageBreak s1*9 \bar "|."
    }

PartPFiveVoiceOne =  \relative c'' {
    \clef "treble" \time 4/4 \key as \major \transposition f | % 1
    R1*6 | % 7
    \stemDown c8. ( _\p ^ "Solo" \stemDown es16 \stemDown es4 \stemDown
    c8. \stemDown bes16 \stemUp as4 ) \pageBreak | % 8
    \stemDown bes8. ( \stemDown c16 \stemDown es8. \stemDown c16
    \stemDown bes2 ) | % 9
    \stemDown c8. ( \stemDown es16 \stemDown es4 \stemDown c8. \stemDown
    bes16 \stemUp as4 ) | \barNumberCheck #10
    \stemDown bes8 ( \stemDown c8 \stemDown bes8. \stemDown as16 \stemUp
    as2 ) | % 11
    \stemDown f'8. ( _\p _ "a 2" _\< \stemDown as16 \stemDown as4
    \stemDown g8 \stemDown es8 \stemDown f4 ) | % 12
    \stemDown f8 ( _\! _\> \stemDown as8 \stemDown g8 \stemDown es8
    \stemDown f2 ) | % 13
    \stemDown f8. ( _\! _\< \stemDown as16 \stemDown as4 \stemDown g8
    \stemDown es8 \stemDown f4 ) \pageBreak | % 14
    \stemDown f8 ( _\! _\> \stemDown as8 \stemDown g8 \stemDown es8
    \stemDown f2 ) | % 15
    \stemDown c8. ( _\! _\pp \stemDown es16 \stemDown es4 \stemDown c8
    \stemDown bes8 \stemUp as4 ) | % 16
    \stemDown bes8. ( \stemDown c16 \stemDown es8. \stemDown c16
    \stemDown bes2 ) | % 17
    \stemDown c8. ( _\< \stemDown es16 \stemDown es4 \stemDown as8.
    \stemDown bes16 \stemDown c4 ) | % 18
    \stemDown bes8. ( _\! _\f _\> \stemDown as16 \stemDown bes8
    \stemDown f8 \stemDown as2 ) | % 19
    R1 \pageBreak | \barNumberCheck #20
    R1*7 \pageBreak | % 27
    R1*5 \pageBreak | % 32
    R1*2 | % 34
    \time 2/4  R2 | % 35
    \time 4/4  R1 | % 36
    \stemDown c,8. ( _\! ^ "Solo" _\p \stemDown es16 \stemDown es4
    \stemDown c8. \stemDown bes16 \stemUp as4 ) \pageBreak | % 37
    \stemDown bes8. ( \stemDown c16 \stemDown es8. \stemDown c16
    \stemDown bes8 \stemDown es4. ) | % 38
    \stemDown c8. ( _\< \stemDown es16 \stemDown es4 ) \stemDown as8. (
    \stemDown bes16 \stemDown c4 ) _\! _\f | % 39
    \stemDown bes8. ( \stemDown as16 _\> \stemDown bes8 \stemDown f8
    \stemDown as2 ) | \barNumberCheck #40
    R1*2 \pageBreak | % 42
    R1*4 \bar "||"
    \pageBreak | % 46
    \key fis \major R1*7 \pageBreak | % 53
    R1*4 \pageBreak | % 57
    R1*4 \pageBreak | % 61
    R1*3 \pageBreak | % 64
    R1*4 \pageBreak | % 68
    R1*4 \pageBreak | % 72
    R1*7 \pageBreak | % 79
    R1*5 \pageBreak | % 84
    R1*6 \pageBreak | \barNumberCheck #90
    R1*2 \pageBreak | % 92
    R1*2 \pageBreak | % 94
    R1*2 \pageBreak | % 96
    R1*4 \pageBreak | \barNumberCheck #100
    R1 | % 101
    \stemDown c,8. ( _\! _\p ^ "Solo" \stemDown es16 \stemDown es4
    \stemDown c8. \stemDown bes16 \stemUp as4 ) | % 102
    \stemDown bes8. ( \stemDown c16 \stemDown es8. \stemDown c16
    \stemDown bes2 ) | % 103
    \stemDown c8. ( \stemDown es16 \stemDown es4 \stemDown c8. \stemDown
    bes16 \stemUp as4 ) | % 104
    \stemDown bes8 ( \stemDown c8 \stemDown bes8. \stemDown as16 \stemUp
    as2 ) ~ _\pp | % 105
    \stemUp as2 ~ \stemUp as8 r8 r4 | % 106
    R1 \pageBreak | % 107
    R1*6 \pageBreak | % 113
    R1*6 \pageBreak | % 119
    R1*9 \bar "|."
    }

PartPFiveVoiceTwo =  \relative bes' {
    \clef "treble" \time 4/4 \key as \major \transposition f s1*7
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak | \barNumberCheck #20
     \once \override NoteHead.style = ##f \stemNeutral bes2 s2*13
    \pageBreak | % 27
     \once \override NoteHead.style = ##f \stemNeutral bes2 s2*9
    \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key fis \major s1*7 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak s1 | % 93
     \once \override NoteHead.style = ##f \stemNeutral gis2 s2
    \pageBreak s1 | % 95
     \once \override NoteHead.style = ##f \stemNeutral gis2 s2
    \pageBreak s1 | % 97
     \once \override NoteHead.style = ##f \stemNeutral gis2 s2*5
    \pageBreak s1*7 \pageBreak s1*4 | % 111
     \once \override NoteHead.style = ##f \stemNeutral bes2 s1.
    \pageBreak s1*3 | % 116
     \once \override NoteHead.style = ##f \stemNeutral bes2 s2*5
    \pageBreak s1*3 | % 122
     \once \override NoteHead.style = ##f \stemNeutral a2 s2*11 \bar
    "|."
    }

PartPFiveVoiceThree =  \relative dis'' {
    \clef "treble" \time 4/4 \key as \major \transposition f s1*7
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key fis \major s1*7 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak | % 92
     \once \override NoteHead.style = ##f \stemNeutral dis32 \once
    \override NoteHead.style = ##f \stemNeutral eis32 \once \override
    NoteHead.style = ##f \stemNeutral dis32 \once \override
    NoteHead.style = ##f \stemNeutral eis32 s8*7 | % 93
     \once \override NoteHead.style = ##f dis'1*1/2 \once \override
    NoteHead.style = ##f eis1*1/2 \pageBreak s1*2 \pageBreak s1*4
    \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*9 \bar
    "|."
    }

PartPSixVoiceOne =  \relative g {
    \clef "treble" \time 4/4 \key es \major \transposition a | % 1
    \stemUp g2 _\pp ^ "a 2" \stemUp f2 | % 2
    \stemUp g2 \stemUp e2 | % 3
    \stemUp e2 _\< \stemUp e4 ( \stemUp fis4 ) | % 4
    gis1 ~ -> _\! _\f | % 5
    \stemUp gis8 _\> \transposition bes r8 _\! ^ "Muta in B" r4 r2 | % 6
    R1*2 \pageBreak | % 8
    R1*3 | % 11
    \stemUp as8 ( _\p _\< \stemUp c8 \stemUp c4 \stemUp bes8 \stemUp g8
    \stemUp as4 ) | % 12
    \stemUp as8 ( _\! _\> \stemUp c8 \stemUp bes8 \stemUp g8 \stemUp as2
    ) | % 13
    \stemUp as8 ( _\! _\< \stemUp c8 \stemUp c4 \stemUp bes8 \stemUp g8
    \stemUp as4 ) \pageBreak | % 14
    \stemUp as8 ( _\! _\> \stemUp c8 \stemUp bes8 \stemUp g8 \stemUp as2
    ) ( _\! | % 15
    \stemUp bes8 ) _\pp r8 r4 r2 | % 16
    R1*3 | % 19
    \stemUp f''8. ( _\pp \stemUp es16 \stemUp f8 \stemUp c8 \stemDown es2
    ) \pageBreak | \barNumberCheck #20
    \stemDown f4. ( \stemDown es8 \stemDown f4 \stemDown c4 ) | % 21
    es1 | % 22
    \stemDown g2 ( _\pp \stemDown a2 ) | % 23
    \stemDown g2 ( ~ \stemDown g2 ) _\markup{ \italic {cresc.} } | % 24
    \stemDown as2 _\fz \stemDown as2 _\< | % 25
    bes1 ~ -> _\! _\ff | % 26
    \stemDown bes4 r4 r2 \pageBreak | % 27
    R1*5 \pageBreak | % 32
    R1*2 | % 34
    \time 2/4  R2 | % 35
    \time 4/4  R1*2 \pageBreak | % 37
    R1*3 | \barNumberCheck #40
    \stemDown f8. ( _\p _\> \stemDown es16 \stemDown f8 \stemDown c8
    \stemDown es2 ) | % 41
    \transposition a R1 \pageBreak ^ "muta in A" | % 42
    R1*4 \bar "||"
    \pageBreak | % 46
    \key d \major R1*6 | % 52
    g,1 _\! _\p _\< \pageBreak | % 53
    g1 _\! _\f _\> | % 54
    \stemDown e'2 ( _\! _\pp \stemDown fis4 \stemDown g4 ) | % 55
    \stemDown <g b>4 ( _\< \stemDown <f a>2 \stemDown <a c>4 ~ ~ | % 56
    \stemDown <a c>4 ) _\! \stemDown <g b>4 ~ ~ \stemDown <g b>8
    \stemDown <fis a>4 ( \stemDown <e g>8 ) \pageBreak | % 57
    \stemDown g4 _\> \stemDown fis4 \stemDown a4 _\! _\pp \stemDown g8
    \prall \stemDown fis8 | % 58
    \stemDown g16 \stemDown e8. ~ \stemDown e2. ~ | % 59
    e1 ^\< | \barNumberCheck #60
    \stemDown <d a'>2 ( ^\! _\fz \stemDown <g, d'>2 ) \pageBreak | % 61
    \stemDown f'4. ( _\p _\> \stemDown d8 \stemDown g4 \stemDown b,4 )
    _\! | % 62
    \stemDown c2. ( \stemDown b4 ) | % 63
    b1 _\> \pageBreak | % 64
    \stemUp e,16 ( _\! _\pp ^ "a 2" \stemUp g16 \stemUp b16 \stemUp g16
    \stemUp e16 \stemUp g16 \stemUp b16 \stemUp g16 \stemUp c,16 \stemUp
    e16 \stemUp a16 \stemUp e16 \stemUp c16 \stemUp e16 \stemUp a16
    \stemUp e16 ) | % 65
    \stemUp e16 ( \stemUp g16 \stemUp b16 \stemUp g16 \stemUp e16
    \stemUp g16 \stemUp b16 \stemUp g16 \stemUp c,16 \stemUp e16 \stemUp
    a16 \stemUp e16 \stemUp c16 _\< \stemUp e16 \stemUp a16 \stemUp e16
    ) | % 66
    \stemUp b16 ( \stemUp d16 \stemUp fis16 \stemUp d16 \stemUp b16
    \stemUp e16 _\! \stemUp g16 \stemUp e16 \stemUp a,16 _\f \stemUp g'16
    \stemUp fis16 \stemUp e16 \stemUp d16 \stemUp fis16 \stemUp b16
    \stemUp fis16 ) | % 67
    \stemDown g16 ( \stemDown b16 \stemDown d16 \stemDown b16 _\>
    \stemDown g16 \stemDown b16 \stemDown d16 \stemDown b16 \stemUp e,16
    \stemUp g16 \stemUp b16 \stemUp g16 \stemUp e16 \stemUp g16 \stemUp
    b16 \stemUp g16 ) \pageBreak | % 68
    \stemUp e16 ( _\! _\p \stemUp g16 \stemUp b16 \stemUp g16 \stemUp e16
    \stemUp g16 \stemUp b16 \stemUp e16 \stemUp g,16 \stemUp bes16
    \stemUp c16 \stemUp bes16 \stemDown g16 \stemDown bes16 \stemDown c16
    \stemDown e16 ) | % 69
    \stemUp e,16 ( \stemUp g16 \stemUp b16 \stemUp g16 \stemUp e16
    \stemUp g16 \stemUp b16 \stemUp e16 \stemDown g,16 \stemDown bes16
    \stemDown c16 \stemDown bes16 \stemDown g16 \stemDown bes16
    \stemDown c16 \stemDown e16 ) | \barNumberCheck #70
    \stemUp f,16 ( ^ "a 2" _\< \stemUp a16 \stemUp c16 \stemUp a16
    \stemDown f16 \stemDown a16 \stemDown c16 \stemDown f16 ) \stemDown
    a,16 ( \stemDown c16 \stemDown f16 \stemDown c16 \stemDown a16
    \stemDown c16 \stemDown f16 \stemDown a16 ) | % 71
    \stemDown b,16 ( _\! _\fz \stemDown g'16 ) \stemDown g16 ( \stemDown
    b,16 ) \stemDown b16 ( _\> \stemDown g'16 ) \stemDown g16 (
    \stemDown b,16 ) \stemDown b16 ( \stemDown g'16 ) \stemDown g16 (
    \stemDown b,16 ) \stemDown b16 ( \stemDown g'16 ) \stemDown g16 (
    \stemDown b,16 ) \pageBreak | % 72
    \stemUp <b, b'>8 _\! r8 r4 r2 | % 73
    R1*5 | % 78
    \stemUp <g b>2 ( _\pp \stemUp e'2 ) \pageBreak | % 79
    \stemUp g4 ( \stemUp f2 \stemUp a4 ~ | \barNumberCheck #80
    \stemUp a4 ) \stemUp g4 ( ~ \stemUp g8 \stemUp fis4 \stemUp e8 ) | % 81
    \stemUp e2. \stemUp dis8 ( \stemUp b'8 ) | % 82
    \stemDown b2 ~ \stemDown b8 r8 \stemUp b,8 ( \stemUp dis8 ) | % 83
    \stemUp e2 ( _\< \stemUp fis4 \stemUp g4 ) \pageBreak | % 84
    \stemUp a2 ( _\! _\mf \stemUp g2 ) | % 85
    \stemUp f2 ( \stemUp g4 \stemUp e4 ) | % 86
    \stemUp e2. ( _\p _\> \stemUp dis4 | % 87
    \stemUp e8 ) r8 _\! r4 r2 | % 88
    R1*2 \pageBreak | \barNumberCheck #90
    R1 | % 91
    \times 4/6  {
        \stemUp gis16 ( _\p _\markup{ \italic {leggiero} } ^ "a 2"
        \stemUp a16 \stemUp b16 \stemUp gis16 \stemUp fis16 \stemUp e16
        }
    \times 4/6  {
        \stemUp fis16 \stemUp gis16 \stemUp a16 \stemUp gis16 \stemUp
        fis16 \stemUp e16 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis16 ( -> \stemUp gis16 \stemUp a16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp gis16 -> \stemUp b16 ) r16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp a16 ( \stemUp gis16 \stemUp fis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp gis16 \stemUp e16 ) r16 }
    \pageBreak | % 92
    \stemDown b'16 -. _\< \stemDown b16 -. \stemDown b16 -. \stemDown b16
    -. \stemDown b16 -. \stemDown b16 -. \stemDown b16 -. \stemDown b16
    -. \stemDown b16 -. _\! \stemDown b16 -. \stemDown b16 -. \stemDown
    b16 -. \stemDown b16 -. \stemDown b16 -. \stemDown b16 -. \stemDown
    b16 -. | % 93
    \stemDown b8 ( \trill _\f ^ "#" _ "#" \stemDown e16 ) r16 \stemDown
    dis8 ( \trill \stemDown e16 ) r16 \stemDown a16 ( \prall _\<
    \stemDown fis16 \stemDown e16 ) r16 \stemDown dis8 ( \trill
    \stemDown e16 ) r16 \pageBreak | % 94
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown b16 _\! ^ "a 2" _\mf \stemDown b16 \stemDown b16
        \stemDown b16 \stemDown b16 \stemDown b16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown b16 \stemDown b16 \stemDown b16 \stemDown b16
        \stemDown b16 \stemDown b16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown b16 _\< \stemDown b16 \stemDown b16 \stemDown b16
        \stemDown b16 \stemDown b16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown b16 \stemDown b16 \stemDown b16 \stemDown b16
        \stemDown b16 \stemDown b16 ~ }
    | % 95
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown b16 _\! ^ "a 2" _\f \stemDown b16 \stemDown b16
        \stemDown b16 \stemDown b16 \stemDown b16 ~ }
    _\< \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown b16 \stemDown b16 \stemDown b16 \stemDown b16
        \stemDown b16 \stemDown b16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown b16 \stemDown b16 \stemDown b16 \stemDown b16
        \stemDown b16 \stemDown b16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown b16 \stemDown b16 \stemDown b16 \stemDown b16
        \stemDown b16 \stemDown b16 }
    \pageBreak | % 96
    \stemDown g'2 ~ _\! _\ff \stemDown g8 r8 r4 | % 97
    r4 \stemDown c,16. ^ "a 2" _\ff \stemDown e32 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown g16 -. \stemDown g16 -. \stemDown g16 -. }
    \stemDown g2 | % 98
    r4 \stemDown c,16. \stemDown e32 \once \omit TupletBracket
    \times 2/3  {
        \stemDown g16 ^. \stemDown g16 ^. \stemDown g16 ^. }
    \stemDown g4 \stemDown c,16. \stemDown e32 \once \omit TupletBracket
    \times 2/3  {
        \stemDown g16 ^. \stemDown g16 ^. \stemDown g16 ^. }
    | % 99
    g1 ~ _\> \pageBreak | \barNumberCheck #100
    \stemDown g8 _\! r8 r4 r2 | % 101
    R1*6 \pageBreak | % 107
    R1*6 \pageBreak | % 113
    R1 | % 114
    \stemDown ges8. ( _\p \stemDown fes16 \stemDown ges8 \stemDown des8
    \stemDown fes2 ) | % 115
    \stemDown ges8. ( _\> \stemDown fes16 \stemDown ges8 \stemDown des8
    \stemDown fes2 ) ~ _\! _\pp _\> | % 116
    fes1 ~ | % 117
    \stemDown fes8 _\! r8 r4 r2 | % 118
    R1 \pageBreak | % 119
    R1*5 | % 124
    ces1 ~ _\p | % 125
    \stemDown ces4 r4 r2 | % 126
    R1*2 \bar "|."
    }

PartPSixVoiceTwo =  \relative b {
    \clef "treble" \time 4/4 \key es \major \transposition a s8*33
    \transposition bes s8*23 \pageBreak s1*6 \pageBreak s1*6 \pageBreak
    s1*7 \pageBreak s1*5 \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1*4 | % 41
    \transposition a s1 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key d \major s1*7 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak s1 | % 93
    \stemNeutral <\tweak style ##f b \tweak style ##f b'>32 \stemNeutral
    <\tweak style ##f cis \tweak style ##f cis'>32 \stemNeutral <\tweak
        style ##f b \tweak style ##f b'>32 \stemNeutral <\tweak style
        ##f cis \tweak style ##f cis'>32 s8*7 \pageBreak s1*2 \pageBreak
    s1*4 \pageBreak s1*5 | % 105
     \once \override NoteHead.style = ##f \stemNeutral ges'2 s1.
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*9 \bar "|."
    }

PartPSixVoiceThree =  \relative g {
    \clef "treble" \time 4/4 \key es \major \transposition a s8*33
    \transposition bes s8*23 \pageBreak s1*6 \pageBreak s1*6 \pageBreak
    s1*7 \pageBreak s1*5 \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1*4 | % 41
    \transposition a s1 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key d \major s1*7 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak s1 | % 93
     \once \override NoteHead.style = ##f \stemDown g8 \trill s8 \once
    \override NoteHead.style = ##f \stemDown g8 \trill s8 \once
    \override NoteHead.style = ##f \stemDown g16 \prall s8. \once
    \override NoteHead.style = ##f \stemDown g8 \trill s8 \pageBreak
    s1*2 \pageBreak s1*4 \pageBreak s1*5 | % 105
     \once \override NoteHead.style = ##f \stemNeutral ges'2 s1.
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*9 \bar "|."
    }

PartPSevenVoiceOne =  \relative fis {
    \clef "treble" \time 4/4 \key es \major \transposition bes | % 1
    \stemUp fis2 _\pp ^ "a 2" \stemUp e2 | % 2
    \stemUp fis2 \stemUp dis2 | % 3
    \stemUp dis2 _\< \stemUp dis4 ( \stemUp eis4 ) | % 4
    fisis1 ~ -> _\! _\f | % 5
    \stemUp fisis8 _\> r8 _\! r4 r2 | % 6
    R1*2 \pageBreak | % 8
    R1*3 | % 11
    \stemUp as8 ( _\p _\< \stemUp c8 \stemUp c4 \stemUp bes8 \stemUp g8
    \stemUp as4 ) | % 12
    \stemUp as8 ( _\! _\> \stemUp c8 \stemUp bes8 \stemUp g8 \stemUp as2
    ) | % 13
    \stemUp as8 ( _\! _\< \stemUp c8 \stemUp c4 \stemUp bes8 \stemUp g8
    \stemUp as4 ) \pageBreak | % 14
    \stemUp as8 ( _\! _\> \stemUp c8 \stemUp bes8 \stemUp g8 \stemUp as2
    ) ( _\! | % 15
    \stemUp bes8 ) _\pp r8 r4 r2 | % 16
    R1*3 | % 19
    \stemDown c'4. ( \stemUp f,8 \stemUp g2 ) \pageBreak |
    \barNumberCheck #20
    \stemDown c2. \stemUp f,4 | % 21
    g1 | % 22
    \stemDown es'2 ( _\pp \stemDown e2 ) | % 23
    \stemDown es2 ( \stemDown e2 ) _\markup{ \italic {cresc.} } | % 24
    \stemDown es2 _\fz \stemDown f2 _\< | % 25
    g1 ~ -> _\! _\ff | % 26
    \stemDown g4 r4 r2 \pageBreak | % 27
    R1*5 \pageBreak | % 32
    R1*2 | % 34
    \time 2/4  R2 | % 35
    \time 4/4  R1*2 \pageBreak | % 37
    R1*3 | \barNumberCheck #40
    \stemDown c,4. ( \stemUp f,8 \stemUp g2 ) | % 41
    R1 \pageBreak | % 42
    R1*4 \bar "||"
    \pageBreak | % 46
    \key des \major R1*6 | % 52
    es1 _\p _\< \pageBreak | % 53
    bes1 _\! _\f _\> | % 54
    es'1 _\! | % 55
    R1*2 \pageBreak | % 57
    \stemDown es2. ( \stemDown d4 | % 58
    \stemDown es16 \stemDown ges,8. ~ \stemUp ges2. ~ | % 59
    \stemUp ges4 ) r4 r2 | \barNumberCheck #60
    R1 \pageBreak | % 61
    \stemDown fes'4. ( \stemDown des8 \stemDown ges4 \stemDown bes,4 ) | % 62
    \stemDown ces2. ( \stemUp bes8 ) ( \stemUp as8 ) | % 63
    ges1 \pageBreak | % 64
    \stemUp es16 ( _\pp ^ "a 2" \stemUp ges16 \stemUp bes16 \stemUp ges16
    \stemUp es16 \stemUp ges16 \stemUp bes16 \stemUp ges16 \stemUp ces,16
    \stemUp es16 \stemUp as16 \stemUp es16 \stemUp ces16 \stemUp es16
    \stemUp as16 \stemUp es16 ) | % 65
    \stemUp es16 ( \stemUp ges16 \stemUp bes16 \stemUp ges16 \stemUp es16
    \stemUp ges16 \stemUp bes16 \stemUp ges16 \stemUp ces,16 \stemUp es16
    \stemUp as16 \stemUp es16 \stemUp ces16 _\< \stemUp es16 \stemUp as16
    \stemUp es16 ) | % 66
    \stemUp bes16 ( \stemUp des16 \stemUp f16 \stemUp des16 \stemUp bes16
    \stemUp es16 _\! \stemUp ges16 \stemUp es16 \stemUp as,16 _\f
    \stemUp ges'16 \stemUp f16 \stemUp es16 \stemUp des16 \stemUp f16
    \stemUp bes16 \stemUp f16 ) | % 67
    \stemDown ges16 ( \stemDown bes16 \stemDown des16 \stemDown bes16
    _\> \stemDown ges16 \stemDown bes16 \stemDown des16 \stemDown bes16
    \stemUp es,16 \stemUp ges16 \stemUp bes16 \stemUp ges16 \stemUp es16
    \stemUp ges16 \stemUp bes16 \stemUp ges16 ) \pageBreak | % 68
    \stemUp es16 ( _\! _\p \stemUp ges16 \stemUp bes16 \stemUp ges16
    \stemUp es16 \stemUp ges16 \stemUp bes16 \stemUp es16 \stemUp ges,16
    \stemUp beses16 \stemUp ces16 \stemUp beses16 \stemDown ges16
    \stemDown beses16 \stemDown ces16 \stemDown es16 ) | % 69
    \stemUp es,16 ( \stemUp ges16 \stemUp bes16 \stemUp ges16 \stemUp es16
    \stemUp ges16 \stemUp bes16 \stemUp es16 \stemDown ges,16 \stemDown
    beses16 \stemDown ces16 \stemDown beses16 \stemDown ges16 \stemDown
    beses16 \stemDown ces16 \stemDown es16 ) | \barNumberCheck #70
    \stemUp fes,16 ( ^ "a 2" _\< \stemUp as16 \stemUp ces16 \stemUp as16
    \stemDown fes16 \stemDown as16 \stemDown ces16 \stemDown fes16 )
    \stemDown as,16 ( \stemDown ces16 \stemDown fes16 \stemDown ces16
    \stemDown as16 \stemDown ces16 \stemDown fes16 \stemDown as16 ) | % 71
    \stemDown bes,16 ( _\! _\fz \stemDown ges'16 ) \stemDown ges16 (
    \stemDown bes,16 ) \stemDown bes16 ( _\> \stemDown ges'16 )
    \stemDown ges16 ( \stemDown bes,16 ) \stemDown bes16 ( \stemDown
    ges'16 ) \stemDown ges16 ( \stemDown bes,16 ) \stemDown bes16 (
    \stemDown ges'16 ) \stemDown ges16 ( \stemDown bes,16 ) \pageBreak | % 72
    \stemUp <bes, bes'>8 _\! r8 r4 r2 | % 73
    R1*5 s2 \stemUp ces4 \stemUp bes4 \pageBreak | % 79
    ces1 | \barNumberCheck #80
    \stemUp ces4 ( \stemUp bes2 ) \stemUp bes8 ( \stemUp ces8 ) | % 81
    \stemUp ces4 ( \stemUp as4 \stemUp ces4 \stemUp bes4 ) | % 82
    \stemUp bes2 ~ \stemUp bes8 s8 r4 | % 83
    \stemUp bes2 ( \stemUp es2 ) \pageBreak | % 84
    \stemUp f2 ( \stemUp des2 ) | % 85
    \stemUp ces4. ( \stemUp des8 \stemUp es4 \stemUp bes4 ) | % 86
    \stemUp ces2. \stemUp bes4 ~ | % 87
    \stemUp bes8 s8*7 | % 88
    R1*2 \pageBreak | \barNumberCheck #90
    R1 | % 91
    \times 4/6  {
        \stemUp g'16 ( _\p _\markup{ \italic {leggiero} } ^ "a 2"
        \stemUp as16 \stemUp bes16 \stemUp g16 \stemUp f16 \stemUp es16
        }
    \times 4/6  {
        \stemUp f16 \stemUp g16 \stemUp as16 \stemUp g16 \stemUp f16
        \stemUp es16 ) }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp f16 ( -> \stemUp g16 \stemUp as16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp g16 -> \stemUp bes16 ) r16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp as16 ( \stemUp g16 \stemUp f16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp g16 \stemUp es16 ) r16 }
    \pageBreak | % 92
    \stemUp es16 -. _\< \stemUp es16 -. \stemUp es16 -. \stemUp es16 -.
    \stemUp es16 -. \stemUp es16 -. \stemUp es16 -. \stemUp es16 -.
    \stemUp es16 -. _\! \stemUp es16 -. \stemUp es16 -. \stemUp es16 -.
    \stemUp es16 -. \stemUp es16 -. \stemUp es16 -. \stemUp es16 -. | % 93
    \stemUp bes8 ( \trill _\f ^ "#" _ "#" \stemUp es16 ) r16 \stemUp d8
    ( \trill \stemUp es16 ) r16 \stemUp as16 ( \prall _\< \stemUp f16
    \stemUp es16 ) r16 \stemUp d8 ( \trill \stemUp es16 ) r16 \pageBreak
    | % 94
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown bes'16 _\! ^ "a 2" _\mf \stemDown bes16 \stemDown bes16
        \stemDown bes16 \stemDown bes16 \stemDown bes16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown bes16 \stemDown bes16 \stemDown bes16 \stemDown bes16
        \stemDown bes16 \stemDown bes16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown bes16 _\< \stemDown bes16 \stemDown bes16 \stemDown
        bes16 \stemDown bes16 \stemDown bes16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown bes16 \stemDown bes16 \stemDown bes16 \stemDown bes16
        \stemDown bes16 \stemDown bes16 ~ }
    | % 95
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown bes16 _\! ^ "a 2" _\f \stemDown bes16 \stemDown bes16
        \stemDown bes16 \stemDown bes16 \stemDown bes16 ~ }
    _\< \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown bes16 \stemDown bes16 \stemDown bes16 \stemDown bes16
        \stemDown bes16 \stemDown bes16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown bes16 \stemDown bes16 \stemDown bes16 \stemDown bes16
        \stemDown bes16 \stemDown bes16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown bes16 \stemDown bes16 \stemDown bes16 \stemDown bes16
        \stemDown bes16 \stemDown bes16 }
    \pageBreak | % 96
    \stemDown ces2 ~ _\! _\ff \stemDown ces8 r8 r4 | % 97
    r4 \stemDown ces16. ^ "a 2" _\ff \stemDown es32 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown ges16 -. \stemDown ges16 -. \stemDown ges16 -. }
    \stemDown ges2 | % 98
    r4 \stemDown ces,16. \stemDown es32 \once \omit TupletBracket
    \times 2/3  {
        \stemDown es16 ^. \stemDown es16 ^. \stemDown es16 ^. }
    \stemDown es4 \stemDown ces16. \stemDown es32 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown es16 ^. \stemDown es16 ^. \stemDown es16 ^. }
    | % 99
    es1 ~ _\> \pageBreak | \barNumberCheck #100
    \stemDown es8 _\! r8 r4 r2 | % 101
    R1*6 \pageBreak | % 107
    R1*6 \pageBreak | % 113
    R1 | % 114
    \stemDown deses4. ( \stemUp geses,8 \stemUp ases2 ) | % 115
    \stemDown deses4. ( \stemUp geses,8 \stemUp ases2 ) ~ | % 116
    ases1 ~ | % 117
    \stemUp ases8 s8*7 | % 118
    R1 \pageBreak | % 119
    R1*5 | % 124
    ases1 ~ _\p | % 125
    \stemUp ases4 r4 r2 | % 126
    R1*2 \bar "|."
    }

PartPSevenVoiceTwo =  \relative bes {
    \clef "treble" \time 4/4 \key es \major \transposition bes s1*7
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key des \major s1*7 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak s1 | % 93
    \stemNeutral <\tweak style ##f bes \tweak style ##f bes'>32
    \stemNeutral <\tweak style ##f c \tweak style ##f c'>32 \stemNeutral
    <\tweak style ##f bes \tweak style ##f bes'>32 \stemNeutral <\tweak
        style ##f c \tweak style ##f c'>32 s8*7 \pageBreak s1*2
    \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*6
    \pageBreak s1*9 \bar "|."
    }

PartPSevenVoiceThree =  \relative ges {
    \clef "treble" \time 4/4 \key es \major \transposition bes s1*7
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key des \major s1*7 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak s1 | % 93
     \once \override NoteHead.style = ##f \stemDown ges8 \trill s8 \once
    \override NoteHead.style = ##f \stemDown ges8 \trill s8 \once
    \override NoteHead.style = ##f \stemDown ges16 \prall s8. \once
    \override NoteHead.style = ##f \stemDown ges8 \trill s8 \pageBreak
    s1*2 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*6
    \pageBreak s1*9 \bar "|."
    }

PartPEightVoiceOne =  \relative b, {
    \clef "bass" \time 4/4 \key des \major | % 1
    \stemUp b2 _\ppp \stemUp bes2 | % 2
    \stemUp b2 \stemUp as2 | % 3
    \stemDown des2 _\< \stemDown ges2 | % 4
    des1 ~ -> _\! _\f | % 5
    \stemDown des8 _\> r8 _\! r4 r2 | % 6
    R1*2 \pageBreak | % 8
    R1*6 \pageBreak | % 14
    R1*3 | % 17
    \stemUp f8. ( ^\p ^\< \stemUp as16 \stemUp as4 \stemUp des8. \stemUp
    es16 \stemUp f4 ) ^\! | % 18
    \stemUp es8. ( ^\f ^\> \stemUp des16 \stemUp es8 \stemUp bes8
    \stemUp des2 ) ^\! | % 19
    \stemDown des2 ( _\pp \stemDown as2 ) \pageBreak | \barNumberCheck
    #20
    des1 | % 21
    as1 | % 22
    \stemDown des2 ^\pp \stemDown b2 | % 23
    \stemDown des2 \stemDown bes2 _\markup{ \italic {cresc.} } | % 24
    \stemDown ges'2 _\fz \stemDown es2 _\< | % 25
    des1 ~ -> _\! _\ff | % 26
    \stemDown des4 r4 r2 \pageBreak | % 27
    R1*5 \pageBreak | % 32
    R1*2 | % 34
    \time 2/4  R2 | % 35
    \time 4/4  R1*2 \pageBreak | % 37
    R1 | % 38
    \stemUp f,8. ( ^\p ^\< \stemUp as16 \stemUp as4 ) \stemUp des8. (
    \stemUp es16 \stemUp f4 ) ^\! ^\f | % 39
    \stemUp es8. ( \stemUp des16 ^\> \stemUp es8 \stemUp bes8 \stemUp
    des2 ) | \barNumberCheck #40
    \stemDown des2 ( ^\! _\p \stemDown as2 ) | % 41
    R1 \pageBreak | % 42
    R1*4 \bar "||"
    \pageBreak | % 46
    \key b \major R1*6 | % 52
    \stemDown cis4 ( _\p ^ "a 2" _\< \stemDown b4 \stemDown a2 )
    \pageBreak | % 53
    cis,1 _\! _\f _\> | % 54
    R1*3 \pageBreak | % 57
    R1*4 \pageBreak | % 61
    R1*3 \pageBreak | % 64
    R1*4 \pageBreak | % 68
    R1*4 \pageBreak | % 72
    R1*7 \pageBreak | % 79
    R1*5 \pageBreak | % 84
    R1*6 \pageBreak | \barNumberCheck #90
    R1*2 \pageBreak | % 92
    R1*2 \pageBreak | % 94
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown gis'16 _\! _\mf \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 _\< \stemDown gis16 \stemDown gis16 \stemDown
        gis16 \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 ~ }
    | % 95
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown gis16 _\! _\f \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 \stemDown gis16 ~ }
    _\< \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 \stemDown gis16 }
    \pageBreak | % 96
    e1 _\! _\ff | % 97
    r4 \stemDown a16. ^ "a 2" _\ff \stemDown cis32 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown e16 -. \stemDown e16 -. \stemDown e16 -. }
    \stemDown e2 | % 98
    r4 \stemDown a,16. \stemDown cis32 \once \omit TupletBracket
    \times 2/3  {
        \stemDown e16 ^. \stemDown e16 ^. \stemDown e16 ^. }
    \stemDown e4 \stemDown a,16. \stemDown cis32 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown e16 ^. \stemDown e16 ^. \stemDown e16 ^. }
    | % 99
    e1 ~ _\> \pageBreak | \barNumberCheck #100
    \stemDown e8 _\! r8 r4 r2 | % 101
    R1*6 \pageBreak | % 107
    R1*6 \pageBreak | % 113
    R1 | % 114
    \stemDown des2 ( _\p \stemDown as2 ) | % 115
    \stemDown des2 ( _\> \stemDown as2 ) _\! _\pp _\> | % 116
    as1 ~ | % 117
    \stemDown as8 _\! r8 r4 r2 | % 118
    R1 \pageBreak | % 119
    R1 | \barNumberCheck #120
    \stemDown des2 _\pp \stemDown b2 | % 121
    \stemDown des2 \stemDown bes2 _\< | % 122
    \stemDown ges2 \stemDown es2 | % 123
    des1 ^> _\! _\f _\> | % 124
    des'1 ~ _\! _\p | % 125
    \stemDown des4 r4 r2 | % 126
    R1*2 \bar "|."
    }

PartPEightVoiceTwo =  \relative es {
    \clef "bass" \time 4/4 \key des \major s1*7 \pageBreak s1*6
    \pageBreak s1*3 | % 17
    R1*2 s1 \pageBreak s1*7 \pageBreak s1*5 \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1 | % 38
    R1*2 s1*2 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key b \major s1*7 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak s1*2 \pageBreak s1*2
    \pageBreak s1*4 \pageBreak s1*5 | % 105
     \once \override NoteHead.style = ##f \stemNeutral es2 s1.
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*9 \bar "|."
    }

PartPNineVoiceOne =  \relative e, {
    \clef "bass" \time 4/4 \key des \major | % 1
    \stemUp e2 _\ppp \stemUp d2 | % 2
    \stemUp e2 \stemUp des2 | % 3
    \stemUp beses'2 _\< \stemUp ges2 | % 4
    des1 ~ -> _\! _\f | % 5
    \stemUp des8 _\> r8 _\! r4 r2 | % 6
    R1*2 \pageBreak | % 8
    R1*6 \pageBreak | % 14
    R1*5 | % 19
    \stemDown ges'2 ( _\pp \stemDown des2 ) \pageBreak | \barNumberCheck
    #20
    ges1 | % 21
    des1 | % 22
    \stemDown des'2 ^\pp \stemDown b2 | % 23
    \stemDown des2 \stemDown bes2 _\markup{ \italic {cresc.} } | % 24
    \stemDown ges'2 _\fz \stemDown es2 _\< | % 25
    des1 ~ -> _\! _\ff | % 26
    \stemDown des4 r4 r2 \pageBreak | % 27
    R1*5 \pageBreak | % 32
    R1*2 | % 34
    \time 2/4  R2 | % 35
    \time 4/4  R1*2 \pageBreak | % 37
    R1*3 | \barNumberCheck #40
    \stemDown ges,2 ( _\p \stemDown des2 ) | % 41
    R1 \pageBreak | % 42
    R1*4 \bar "||"
    \pageBreak | % 46
    \key b \major R1*6 | % 52
    \stemDown cis'4 ( _\p ^ "a 2" _\< \stemDown b4 \stemDown a2 )
    \pageBreak | % 53
    cis,1 _\! _\f _\> | % 54
    R1*3 \pageBreak | % 57
    R1*4 \pageBreak | % 61
    R1*3 \pageBreak | % 64
    R1*4 \pageBreak | % 68
    R1*4 \pageBreak | % 72
    R1*7 \pageBreak | % 79
    R1*5 \pageBreak | % 84
    R1*6 \pageBreak | \barNumberCheck #90
    R1*2 \pageBreak | % 92
    R1*2 \pageBreak | % 94
    \times 4/6  {
        \stemUp gis16 _\! _\mf \stemUp gis16 \stemUp gis16 \stemUp gis16
        \stemUp gis16 \stemUp gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp gis16 \stemUp gis16 \stemUp gis16 \stemUp gis16 \stemUp
        gis16 \stemUp gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp gis16 _\< \stemUp gis16 \stemUp gis16 \stemUp gis16
        \stemUp gis16 \stemUp gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp gis16 \stemUp gis16 \stemUp gis16 \stemUp gis16 \stemUp
        gis16 \stemUp gis16 ~ }
    | % 95
    \times 4/6  {
        \stemUp gis16 _\! _\f \stemUp gis16 \stemUp gis16 \stemUp gis16
        \stemUp gis16 \stemUp gis16 ~ }
    _\< \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp gis16 \stemUp gis16 \stemUp gis16 \stemUp gis16 \stemUp
        gis16 \stemUp gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp gis16 \stemUp gis16 \stemUp gis16 \stemUp gis16 \stemUp
        gis16 \stemUp gis16 ~ }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp gis16 \stemUp gis16 \stemUp gis16 \stemUp gis16 \stemUp
        gis16 \stemUp gis16 }
    \pageBreak | % 96
    cis1 _\! _\ff | % 97
    r4 \stemDown a'16. ^ "a 2" _\ff \stemDown cis32 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown e16 -. \stemDown e16 -. \stemDown e16 -. }
    \stemDown e2 | % 98
    r4 \stemDown a,16. \stemDown a32 \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis16 ^. \stemDown cis16 ^. \stemDown cis16 ^. }
    \stemDown cis4 \stemDown a16. \stemDown cis32 \once \omit
    TupletBracket
    \times 2/3  {
        \stemDown cis16 ^. \stemDown cis16 ^. \stemDown cis16 ^. }
    | % 99
    cis1 ~ _\> \pageBreak | \barNumberCheck #100
    \stemDown cis8 _\! r8 r4 r2 | % 101
    R1*6 \pageBreak | % 107
    R1*6 \pageBreak | % 113
    R1 | % 114
    \stemDown ges2 ( _\p \stemDown des2 ) | % 115
    \stemDown ges2 ( _\> \stemDown des2 ) _\! _\pp _\> | % 116
    as'1 ~ | % 117
    \stemDown as8 _\! r8 r4 r2 | % 118
    R1 \pageBreak | % 119
    R1 | \barNumberCheck #120
    \stemDown des,2 _\pp \stemUp b2 | % 121
    \stemDown des2 \stemUp bes2 _\< | % 122
    \stemUp ges2 \stemUp es2 | % 123
    des1 ^> _\! _\f _\> | % 124
    des'1 ~ _\! _\p | % 125
    \stemDown des4 r4 r2 | % 126
    R1*2 \bar "|."
    }

PartPOneZeroVoiceOne =  \relative g' {
    \clef "treble" \time 4/4 \key c \none \transposition e | % 1
    \stemUp g2 _\ppp \stemUp fis2 | % 2
    \stemUp g2 \stemUp a2 | % 3
    \stemUp a2 ^\< \stemUp a2 | % 4
    a1 ~ ^> ^\! _\f | % 5
    \stemUp a8 _\> r8 _\! r4 r2 | % 6
    R1*2 \pageBreak | % 8
    R1*6 \pageBreak | % 14
    R1*6 \pageBreak | \barNumberCheck #20
    R1*3 | % 23
    r2 \stemUp cis2 _\p _\< | % 24
    \stemDown d2 _\! _\fz _\< \stemDown b2 | % 25
    \stemDown e2 -> _\! _\ff ^\ff \stemDown e2 ~ _\ff | % 26
    \stemDown e2 ~ _\> \stemDown e8 _\! _\pp r8 r4 \pageBreak | % 27
    R1*5 \pageBreak | % 32
    R1*2 | % 34
    \time 2/4  R2 | % 35
    \time 4/4  R1*2 \pageBreak | % 37
    R1*5 \pageBreak | % 42
    \stemDown cis8. ( _\p ^ "con sordini" _\< \stemDown e16 \stemDown e4
    ) \stemDown cis8 ( \stemDown b8 \stemUp a4 ) _\! | % 43
    \stemDown cis8. ( \stemDown e16 \stemDown e4 ) \stemDown cis8 (
    \stemDown b8 \stemUp a4 ) | % 44
    \stemDown cis8. ( \stemDown e16 \stemDown e4 ) \stemDown cis8. (
    \stemDown e16 \stemDown e4 ) | % 45
    \stemDown cis8. ( \stemDown e16 ) \stemDown e2. ^\pp \bar "||"
    \pageBreak | % 46
    \key g \major \stemDown e8 r8 r4 r2 | % 47
    R1*6 \pageBreak | % 53
    R1*4 \pageBreak | % 57
    R1*4 \pageBreak | % 61
    R1*3 \pageBreak | % 64
    R1*4 \pageBreak | % 68
    R1*4 \pageBreak | % 72
    R1*7 \pageBreak | % 79
    R1*5 \pageBreak | % 84
    R1*6 \pageBreak | \barNumberCheck #90
    R1*2 \pageBreak | % 92
    R1*2 \pageBreak | % 94
    R1*2 \pageBreak | % 96
    \stemDown f2. ^ "a 2" ^ "[senza sord.]" _\ff \stemDown f8. \stemDown
    f16 -. | % 97
    \stemDown d16 ^ "a 2" \stemDown c8. \stemDown f2. _\ffz s4 \stemDown
    f16. \stemDown f32 s4. \stemDown f16. \stemDown f32 s8 | % 99
    R1 \pageBreak | \barNumberCheck #100
    R1*7 \pageBreak | % 107
    R1*6 \pageBreak | % 113
    R1 | % 114
    r2 \stemUp a,2 ^\p | % 115
    r2 \stemUp a2 ~ ^\pp ^\> | % 116
    a1 ~ | % 117
    \stemUp a8 ^\! r8 r4 r2 | % 118
    R1 \pageBreak | % 119
    R1*9 \bar "|."
    }

PartPOneZeroVoiceTwo =  \relative a' {
    \clef "treble" \time 4/4 \key c \none \transposition e s1*7
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*3 | % 23
    R1 s1*3 \pageBreak s1*5 \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key g \major s1*7 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak s1 | % 93
     \once \override NoteHead.style = ##f \stemNeutral a2 s2 \pageBreak
    s1*2 \pageBreak s1*4 \pageBreak | \barNumberCheck #100
     \once \override NoteHead.style = ##f \stemNeutral a2 s2*9 | % 105
     \once \override NoteHead.style = ##f \stemNeutral a2 s1. \pageBreak
    s1*6 \pageBreak s1 | % 114
    R1*4 s1 \pageBreak s1*3 | % 122
     \once \override NoteHead.style = ##f \stemNeutral a2 s2*11 \bar
    "|."
    }

PartPOneZeroVoiceThree =  \relative ces'' {
    \clef "treble" \time 4/4 \key c \none \transposition e s1*7
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key g \major s1*7 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak s1*2 \pageBreak s1*2
    \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*3 | % 116
     \once \override NoteHead.style = ##f \stemNeutral ces2 s2*5
    \pageBreak s1*9 \bar "|."
    }

PartPOneOneVoiceOne =  \relative disis' {
    \clef "treble" \time 4/4 \key a \major \transposition e | % 1
    \stemUp disis2 _\ppp \stemUp eisis2 | % 2
    \stemUp fisis2 \stemUp gisis2 | % 3
    \stemUp gisis2 ^\< \stemUp gisis2 | % 4
    gisis,1 ~ ^> ^\! _\f | % 5
    \stemUp gisis8 _\> r8 _\! r4 r2 | % 6
    R1*2 \pageBreak | % 8
    R1*6 \pageBreak | % 14
    R1*6 \pageBreak | \barNumberCheck #20
    R1*5 | % 25
    \stemDown disis''2 -> _\ff ^\ff \stemDown disis2 _\ff | % 26
    \stemDown bisis2 ~ _\> \stemDown bisis8 _\! _\pp r8 r4 \pageBreak | % 27
    R1*5 \pageBreak | % 32
    R1*2 | % 34
    \time 2/4  R2 | % 35
    \time 4/4  R1*2 \pageBreak | % 37
    R1*5 \pageBreak | % 42
    \stemUp gisis8. ( _\p ^ "con sordini" _\< \stemUp bisis16 \stemDown
    bisis4 ) \stemUp gisis8 ( \stemUp disis8 \stemUp bisis4 ) _\! | % 43
    \stemUp gisis'8. ( \stemUp bisis16 \stemDown bisis4 ) \stemUp gisis8
    ( \stemUp disis8 \stemUp bisis4 ) | % 44
    \stemUp gisis'8. ( \stemUp bisis16 \stemDown bisis4 ) \stemUp gisis8.
    ( \stemUp bisis16 \stemDown bisis4 ) | % 45
    \stemDown bisis8. ( \stemDown disis16 ) \stemDown disis2. ^\pp \bar
    "||"
    \pageBreak | % 46
    \key g \major \stemDown e8 r8 r4 r2 | % 47
    R1*6 \pageBreak | % 53
    R1*4 \pageBreak | % 57
    R1*4 \pageBreak | % 61
    R1*3 \pageBreak | % 64
    R1*4 \pageBreak | % 68
    R1*4 \pageBreak | % 72
    R1*7 \pageBreak | % 79
    R1*5 \pageBreak | % 84
    R1*6 \pageBreak | \barNumberCheck #90
    R1*2 \pageBreak | % 92
    R1*2 \pageBreak | % 94
    R1*2 \pageBreak | % 96
    \stemDown f2. ^ "a 2" ^ "[senza sord.]" _\ff \stemDown f8. \stemDown
    f16 -. | % 97
    \stemDown d16 ^ "a 2" \stemDown c8. \stemDown f2. _\ffz s4 \stemDown
    f16. \stemDown f32 s4. \stemDown f16. \stemDown f32 s8 | % 99
    R1 \pageBreak | \barNumberCheck #100
    R1*7 \pageBreak | % 107
    R1*6 \pageBreak | % 113
    R1*6 \pageBreak | % 119
    R1*9 \bar "|."
    }

PartPOneTwoVoiceOne =  \relative gis {
    \clef "treble" \time 4/4 \key c \none | % 1
    \stemUp gis2 _\ppp \stemUp ais2 | % 2
    \stemUp b2 \stemUp cis2 | % 3
    \stemUp cis2 ^\< \stemUp cis2 | % 4
    cis,1 ~ ^> ^\! _\f | % 5
    \stemUp cis8 _\> r8 _\! r4 r2 | % 6
    \transposition e R1*2 \pageBreak _ "IV. muta in E" | % 8
    R1*6 \pageBreak | % 14
    R1*6 \pageBreak | \barNumberCheck #20
    R1 | % 21
    a''1 ~ ^\pp | % 22
    \stemUp a8 r8 r4 r2 | % 23
    R1*2 | % 25
    \stemUp a2 \stemDown cis2 ~ _\ff | % 26
    \stemDown cis2 ~ _\> \stemDown cis8 _\! _\pp r8 r4 \pageBreak | % 27
    R1*5 \pageBreak | % 32
    R1*2 | % 34
    \time 2/4  R2 | % 35
    \time 4/4  R1*2 \pageBreak | % 37
    R1*5 \pageBreak | % 42
    R1*4 \bar "||"
    \pageBreak | % 46
    \key g \major R1*7 \pageBreak | % 53
    R1*4 \pageBreak | % 57
    R1*4 \pageBreak | % 61
    R1*3 \pageBreak | % 64
    R1*4 \pageBreak | % 68
    R1*4 \pageBreak | % 72
    R1*7 \pageBreak | % 79
    R1*5 \pageBreak | % 84
    R1*6 \pageBreak | \barNumberCheck #90
    R1*2 \pageBreak | % 92
    R1*2 \pageBreak | % 94
    R1*2 \pageBreak | % 96
    c'1 -> _\ff | % 97
    c1 -> | % 98
    R1*2 \pageBreak | \barNumberCheck #100
    R1*7 \pageBreak | % 107
    R1*6 \pageBreak | % 113
    R1*6 \pageBreak | % 119
    R1 | \barNumberCheck #120
    \stemUp e,,2 ^ "a 2" _\pp \stemUp bes2 | % 121
    \stemUp e2 \stemUp fis2 _\< | % 122
    \stemUp d2. ^ "a 2" \stemUp d4 | % 123
    e1 _> _\! _\f _\> | % 124
    R1*4 \bar "|."
    _\! }

PartPOneTwoVoiceTwo =  \relative c'' {
    \clef "treble" \time 4/4 \key c \none | % 1
    R1*5 | % 6
    \transposition e s1*2 \pageBreak s1*6 \pageBreak s1*6 \pageBreak
    s1*2 | % 22
    R1 s1*4 \pageBreak s1*5 \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key g \major s1*7 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak s1 | % 93
     \once \override NoteHead.style = ##f \stemNeutral c2 s2 \pageBreak
    s1*2 \pageBreak s1*4 \pageBreak | \barNumberCheck #100
     \once \override NoteHead.style = ##f \stemNeutral a2 s2*9 | % 105
     \once \override NoteHead.style = ##f \stemNeutral a2 s1. \pageBreak
    s1*4 | % 111
     \once \override NoteHead.style = ##f \stemNeutral a2 s1. \pageBreak
    s1*6 \pageBreak s4*19 s4*17 _\p \bar "|."
    }

PartPOneThreeVoiceOne =  \relative gis' {
    \clef "treble" \time 4/4 \key des \major \transposition c | % 1
    \stemUp gis2 _\ppp \stemUp ais2 | % 2
    \stemUp b2 \stemUp cis2 | % 3
    \stemUp cis2 ^\< \stemUp cis2 | % 4
    cis,1 ~ ^> ^\! _\f | % 5
    \stemUp cis8 _\> r8 _\! r4 r2 | % 6
    R1*2 \pageBreak | % 8
    R1*6 \pageBreak | % 14
    R1*6 \pageBreak | \barNumberCheck #20
    R1*5 | % 25
    r2 \stemDown cis'2 | % 26
    \stemDown cis2 ~ _\> \stemDown cis8 _\! _\pp r8 r4 \pageBreak | % 27
    R1*5 \pageBreak | % 32
    R1*2 | % 34
    \time 2/4  R2 | % 35
    \time 4/4  R1*2 \pageBreak | % 37
    R1*5 \pageBreak | % 42
    R1*4 \bar "||"
    \pageBreak | % 46
    \key b \major R1*7 \pageBreak | % 53
    R1*4 \pageBreak | % 57
    R1*4 \pageBreak | % 61
    R1*3 \pageBreak | % 64
    R1*4 \pageBreak | % 68
    R1*4 \pageBreak | % 72
    R1*7 \pageBreak | % 79
    R1*5 \pageBreak | % 84
    R1*6 \pageBreak | \barNumberCheck #90
    R1*2 \pageBreak | % 92
    R1*2 \pageBreak | % 94
    R1*2 \pageBreak | % 96
    e1 -> _\ff | % 97
    e1 -> | % 98
    R1*2 \pageBreak | \barNumberCheck #100
    R1*7 \pageBreak | % 107
    R1*6 \pageBreak | % 113
    R1*6 \pageBreak | % 119
    R1 | \barNumberCheck #120
    \stemUp gis,2 ^ "a 2" _\pp \stemUp d2 | % 121
    \stemUp gis2 \stemUp ais2 _\< | % 122
    \stemUp fis2. ^ "a 2" \stemUp fis4 | % 123
    gis1 _> _\! _\f _\> | % 124
    R1*4 \bar "|."
    _\! }

PartPOneThreeVoiceTwo =  \relative c' {
    \clef "treble" \time 4/4 \key des \major \transposition c | % 1
    R1*5 s1*2 \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*7 \pageBreak
    s1*5 \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key b \major s1*7 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak s1*2 \pageBreak s1*2
    \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*6
    \pageBreak s4*19 s4*17 _\p \bar "|."
    }

PartPOneFourVoiceOne =  \relative c' {
    \clef "treble" \time 4/4 \key c \none \transposition fes' | % 1
    \stemUp c2 _\ppp ^ "a 2" \stemUp des2 | % 2
    \stemUp c2 \stemUp des2 | % 3
    \stemUp c2 _\< \stemUp d2 | % 4
    e1 ~ -> _\! _\f | % 5
    \stemUp e8 _\> r8 _\! r4 r2 | % 6
    R1*2 \pageBreak | % 8
    R1*6 \pageBreak | % 14
    R1*6 \pageBreak | \barNumberCheck #20
    R1*5 | % 25
    r2 \stemDown cis'2 ~ _\ff | % 26
    \stemDown cis2 ~ _\> \stemDown cis8 _\! _\pp r8 r4 \pageBreak | % 27
    R1*5 \pageBreak | % 32
    R1*2 | % 34
    \time 2/4  R2 | % 35
    \time 4/4  R1*2 \pageBreak | % 37
    R1*5 \pageBreak | % 42
    R1*4 \bar "||"
    \pageBreak | % 46
    \key g \major R1*7 \pageBreak | % 53
    R1*4 \pageBreak | % 57
    R1*4 \pageBreak | % 61
    R1*3 \pageBreak | % 64
    R1*4 \pageBreak | % 68
    R1*4 \pageBreak | % 72
    R1*7 \pageBreak | % 79
    R1*5 \pageBreak | % 84
    R1*6 \pageBreak | \barNumberCheck #90
    R1*2 \pageBreak | % 92
    R1*2 \pageBreak | % 94
    R1 | % 95
    \stemUp ges16. _\f \stemUp as32 \stemUp fes8 \stemUp ges16. \stemUp
    as32 \stemUp fes8 \stemUp ges16. \stemUp as32 \stemUp ges16. \stemUp
    as32 \stemUp ges16. \stemUp as32 \stemUp ges16. \stemUp as32
    \pageBreak | % 96
    \stemUp a2 \stemDown a8. -> _\ff \stemDown c16 \stemDown c4 | % 97
    \stemUp a8. \stemUp g16 \stemUp f4 r2 | % 98
    \stemDown a8. \stemDown c16 \stemDown c4 \stemUp a8. \stemUp g16
    \stemUp f4 | % 99
    \stemUp a8. _\mf _\> \stemUp g16 \stemUp f4 \stemUp a8. \stemUp g16
    \stemUp f4 \pageBreak | \barNumberCheck #100
    \stemUp a4 ( _\! _\pp \stemUp g4 \stemUp f4 \stemUp g4 ) | % 101
    \stemUp a2 ~ _\pp \stemUp a8 r8 r4 | % 102
    R1*5 \pageBreak | % 107
    R1*6 \pageBreak | % 113
    R1*6 \pageBreak | % 119
    R1*9 \bar "|."
    }

PartPOneFourVoiceTwo =  \relative c' {
    \clef "treble" \time 4/4 \key c \none \transposition fes' s1*7
    \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key g \major s1*7 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak s1 | % 93
     \once \override NoteHead.style = ##f \stemNeutral c2 s2 \pageBreak
    s1*2 \pageBreak s1*4 \pageBreak s1*5 | % 105
     \once \override NoteHead.style = ##f \stemNeutral c2 s1. \pageBreak
    s1*4 | % 111
     \once \override NoteHead.style = ##f \stemNeutral des2 s1.
    \pageBreak s1*3 | % 116
     \once \override NoteHead.style = ##f \stemNeutral des2 s2*5
    \pageBreak s1*3 | % 122
     \once \override NoteHead.style = ##f \stemNeutral bes2 s2*11 \bar
    "|."
    }

PartPOneFiveVoiceOne =  \relative c' {
    \clef "treble" \time 4/4 \key a \major \transposition e' | % 1
    \stemUp c2 _\ppp ^ "a 2" \stemUp des2 | % 2
    \stemUp c2 \stemUp des2 | % 3
    \stemUp c2 _\< \stemUp d2 | % 4
    e1 ~ -> _\! _\f | % 5
    \stemUp e8 _\> r8 _\! r4 r2 | % 6
    R1*2 \pageBreak | % 8
    R1*6 \pageBreak | % 14
    R1*6 \pageBreak | \barNumberCheck #20
    R1*5 | % 25
    r2 \stemUp a2 ~ _\ff | % 26
    \stemUp a2 ~ _\> \stemUp a8 _\! _\pp r8 r4 \pageBreak | % 27
    R1*5 \pageBreak | % 32
    R1*2 | % 34
    \time 2/4  R2 | % 35
    \time 4/4  R1*2 \pageBreak | % 37
    R1*5 \pageBreak | % 42
    R1*4 \bar "||"
    \pageBreak | % 46
    \key g \major R1*7 \pageBreak | % 53
    R1*4 \pageBreak | % 57
    R1*4 \pageBreak | % 61
    R1*3 \pageBreak | % 64
    R1*4 \pageBreak | % 68
    R1*4 \pageBreak | % 72
    R1*7 \pageBreak | % 79
    R1*5 \pageBreak | % 84
    R1*6 \pageBreak | \barNumberCheck #90
    R1*2 \pageBreak | % 92
    R1*2 \pageBreak | % 94
    R1 | % 95
    \stemUp eses8 \stemUp des8 \stemUp eses8 \stemUp des8 \stemUp eses8
    \stemUp eses8 \stemUp eses8 \stemUp eses8 \pageBreak | % 96
    \stemUp f2 \stemUp f8. -> _\ff \stemUp a16 \stemUp a4 | % 97
    \stemUp f8. \stemUp c16 \stemUp a4 r2 | % 98
    \stemUp f'8. \stemUp a16 \stemUp a4 \stemUp f8. \stemUp c16 \stemUp
    a4 | % 99
    \stemUp f'8. _\mf _\> \stemUp c16 \stemUp a4 \stemUp f'8. \stemUp c16
    \stemUp a4 \pageBreak | \barNumberCheck #100
    \stemUp f'4 ( _\! _\pp \stemUp c4 \stemUp a4 \stemUp c4 ) | % 101
    \stemUp cis2 ~ _\pp \stemUp des8 r8 r4 | % 102
    R1*5 \pageBreak | % 107
    R1*6 \pageBreak | % 113
    R1*6 \pageBreak | % 119
    R1*9 \bar "|."
    }

PartPOneSixVoiceOne =  \relative gis {
    \clef "alto" \time 4/4 \key des \major | % 1
    \stemUp gis2 _\ppp \stemUp f2 | % 2
    \stemUp gis2 \stemUp f2 | % 3
    \stemUp fes2 _\< \stemUp beses2 | % 4
    as1 ~ -> _\! _\f | % 5
    \stemUp as8 _\> r8 _\! r4 r2 | % 6
    R1*2 \pageBreak | % 8
    R1*6 \pageBreak | % 14
    R1*6 \pageBreak | \barNumberCheck #20
    R1*5 | % 25
    r2 \stemDown des2 ~ _\ff | % 26
    \stemDown des2 ~ _\> \stemDown des8 _\! _\pp r8 r4 \pageBreak | % 27
    R1*5 \pageBreak | % 32
    R1*2 | % 34
    \time 2/4  R2 | % 35
    \time 4/4  R1*2 \pageBreak | % 37
    R1*5 \pageBreak | % 42
    R1*4 \bar "||"
    \pageBreak | % 46
    \key b \major R1*7 \pageBreak | % 53
    R1*4 \pageBreak | % 57
    R1*4 \pageBreak | % 61
    R1*3 \pageBreak | % 64
    R1*4 \pageBreak | % 68
    R1*4 \pageBreak | % 72
    R1*7 \pageBreak | % 79
    R1*5 \pageBreak | % 84
    R1*6 \pageBreak | \barNumberCheck #90
    R1*2 \pageBreak | % 92
    R1*2 \pageBreak | % 94
    R1*2 \pageBreak | % 96
    \stemUp cis,8. ^> _\ff ^ "a 2" \stemUp e16 -. \stemUp a16 -. \stemUp
    cis8. -> \stemDown e4. -> r8 | % 97
    r2 \stemUp cis,8. ^> _\f ^ "a 2" \stemUp e16 ^. \stemUp a16 ^.
    \stemUp cis8. ^> | % 98
    \stemDown e4. -> r8 r2 | % 99
    R1 \pageBreak | \barNumberCheck #100
    R1*7 \pageBreak | % 107
    R1*6 \pageBreak | % 113
    R1*6 \pageBreak | % 119
    R1 | \barNumberCheck #120
    \stemDown des2 _\pp \stemDown d2 | % 121
    \stemDown des2 \stemDown d2 _\< | % 122
    \stemDown des2 \stemDown es2 _\! | % 123
    <des f>1 -> _\f _\> | % 124
    R1*4 \bar "|."
    _\! _\p }

PartPOneSixVoiceTwo =  \relative cis' {
    \clef "alto" \time 4/4 \key des \major s1*7 \pageBreak s1*6
    \pageBreak s1*6 \pageBreak s1*7 \pageBreak s1*5 \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key b \major s1*7 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak s1 | % 93
     \once \override NoteHead.style = ##f \stemNeutral cis2 s2
    \pageBreak s1*2 \pageBreak s1*4 \pageBreak | \barNumberCheck #100
     \once \override NoteHead.style = ##f \stemNeutral cis2 s2*9 | % 105
     \once \override NoteHead.style = ##f \stemNeutral es2 s1.
    \pageBreak s1*4 | % 111
     \once \override NoteHead.style = ##f \stemNeutral es2 s1.
    \pageBreak s1*6 \pageBreak s1*9 \bar "|."
    }

PartPOneSevenVoiceOne =  \relative b, {
    \clef "bass" \time 4/4 \key des \major | % 1
    \stemUp b2 _\ppp \stemUp bes2 | % 2
    \stemUp b2 \stemDown des2 | % 3
    \stemDown des2 _\< \stemDown beses'2 | % 4
    f1 ~ -> _\! _\f | % 5
    \stemDown f8 _\> r8 _\! r4 r2 | % 6
    R1*2 \pageBreak | % 8
    R1*6 \pageBreak | % 14
    R1*6 \pageBreak | \barNumberCheck #20
    R1*5 | % 25
    r2 \stemDown as2 ~ _\ff | % 26
    \stemDown as2 ~ _\> \stemDown as8 _\! _\pp r8 r4 \pageBreak | % 27
    R1*5 \pageBreak | % 32
    R1*2 | % 34
    \time 2/4  R2 | % 35
    \time 4/4  R1*2 \pageBreak | % 37
    R1*5 \pageBreak | % 42
    R1*4 \bar "||"
    \pageBreak | % 46
    \key b \major R1*7 \pageBreak | % 53
    R1*4 \pageBreak | % 57
    R1*4 \pageBreak | % 61
    R1*3 \pageBreak | % 64
    R1*4 \pageBreak | % 68
    R1*4 \pageBreak | % 72
    R1*7 \pageBreak | % 79
    R1*5 \pageBreak | % 84
    R1*6 \pageBreak | \barNumberCheck #90
    R1*2 \pageBreak | % 92
    R1*2 \pageBreak | % 94
    R1*2 \pageBreak | % 96
    \stemDown cis,8. ^> _\ff ^ "a 2" \stemDown e16 -. \stemDown a16 -.
    \stemDown cis8. -> \stemDown e4. -> r8 | % 97
    r2 \stemUp cis,8. ^> _\f ^ "a 2" \stemUp e16 ^. \stemDown a16 ^.
    \stemDown cis8. ^> | % 98
    \stemDown e4. -> r8 r2 | % 99
    R1 \pageBreak | \barNumberCheck #100
    R1*7 \pageBreak | % 107
    R1*6 \pageBreak | % 113
    R1*6 \pageBreak | % 119
    R1 | \barNumberCheck #120
    \stemDown f,2 _\pp \stemDown g2 | % 121
    \stemDown f2 \stemDown f2 | % 122
    \stemDown bes2. \stemDown c4 s1 | % 124
    R1*4 \bar "|."
    }

PartPOneEightVoiceOne =  \relative e, {
    \clef "bass" \time 4/4 \key des \major | % 1
    \stemUp e2 _\ppp \stemUp d2 | % 2
    \stemUp e2 \stemUp des2 | % 3
    \stemUp a'2 _\< \stemUp ges2 | % 4
    des1 ~ -> _\! _\f | % 5
    \stemUp des8 _\> r8 _\! r4 r2 | % 6
    R1*2 \pageBreak | % 8
    R1*6 \pageBreak | % 14
    R1*6 \pageBreak | \barNumberCheck #20
    R1*5 | % 25
    r2 \stemUp des'2 ~ _\ff | % 26
    \stemUp des2 ~ _\> \stemUp des8 _\! _\pp r8 r4 \pageBreak | % 27
    R1*5 \pageBreak | % 32
    R1*2 | % 34
    \time 2/4  R2 | % 35
    \time 4/4  R1*2 \pageBreak | % 37
    R1*5 \pageBreak | % 42
    R1*4 \bar "||"
    \pageBreak | % 46
    \key b \major R1*7 \pageBreak | % 53
    R1*4 \pageBreak | % 57
    R1*4 \pageBreak | % 61
    R1*3 \pageBreak | % 64
    R1*4 \pageBreak | % 68
    R1*4 \pageBreak | % 72
    R1*7 \pageBreak | % 79
    R1*5 \pageBreak | % 84
    R1*6 \pageBreak | \barNumberCheck #90
    R1*2 \pageBreak | % 92
    R1*2 \pageBreak | % 94
    R1*2 \pageBreak | % 96
    \stemUp cis8. ^> ^\ff \stemUp e16 _. \stemUp a16 ^. \stemUp cis8. ^>
    r2 | % 97
    r2 \stemUp cis,8. ^> ^\f \stemUp e16 ^. \stemUp a16 ^. \stemUp cis8.
    ^> | % 98
    R1*2 \pageBreak | \barNumberCheck #100
    R1*7 \pageBreak | % 107
    R1*6 \pageBreak | % 113
    R1*6 \pageBreak | % 119
    R1 | \barNumberCheck #120
    \stemDown des,2 _\pp \stemUp b2 | % 121
    \stemDown des2 \stemUp bes2 _\< | % 122
    \stemUp ges2 \stemUp es2 | % 123
    des1 ^> _\! _\f _\> | % 124
    R1*4 \bar "|."
    _\! }

PartPOneEightVoiceTwo =  \relative cis {
    \clef "bass" \time 4/4 \key des \major s1*7 \pageBreak s1*6
    \pageBreak s1*6 \pageBreak s1*7 \pageBreak s1*5 \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key b \major s1*7 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak s1 | % 93
     \once \override NoteHead.style = ##f \stemNeutral cis2 s2
    \pageBreak s1*2 \pageBreak s1*4 \pageBreak | \barNumberCheck #100
     \once \override NoteHead.style = ##f \stemNeutral cis2 s2*9 | % 105
     \once \override NoteHead.style = ##f \stemNeutral es2 s1.
    \pageBreak s1*4 | % 111
     \once \override NoteHead.style = ##f \stemNeutral es2 s1.
    \pageBreak s1*6 \pageBreak s4*19 s4*17 _\p \bar "|."
    }

PartPOneNineVoiceOne =  \relative e, {
    \clef "bass" \time 4/4 \key des \major | % 1
    \stemUp e2 _\ppp \stemUp d2 | % 2
    \stemUp e2 \stemUp des2 | % 3
    \stemUp a'2 _\< \stemUp ges2 | % 4
    des1 ~ -> _\! _\f | % 5
    \stemUp des8 _\> r8 _\! r4 r2 | % 6
    R1*2 \pageBreak | % 8
    R1*6 \pageBreak | % 14
    R1*6 \pageBreak | \barNumberCheck #20
    R1*7 \pageBreak | % 27
    R1*5 \pageBreak | % 32
    R1*2 | % 34
    \time 2/4  R2 | % 35
    \time 4/4  R1*2 \pageBreak | % 37
    R1*5 \pageBreak | % 42
    R1*4 \bar "||"
    \pageBreak | % 46
    \key b \major R1*7 \pageBreak | % 53
    R1*4 \pageBreak | % 57
    R1*4 \pageBreak | % 61
    R1*3 \pageBreak | % 64
    R1*4 \pageBreak | % 68
    R1*4 \pageBreak | % 72
    R1*7 \pageBreak | % 79
    R1*5 \pageBreak | % 84
    R1*6 \pageBreak | \barNumberCheck #90
    R1*2 \pageBreak | % 92
    R1*2 \pageBreak | % 94
    R1*2 \pageBreak | % 96
    \stemUp cis'8. ^> ^\ff \stemUp e16 _. \stemUp a16 ^. \stemUp cis8.
    ^> r2 | % 97
    r2 \stemUp cis,8. ^> ^\f \stemUp e16 ^. \stemUp a16 ^. \stemUp cis8.
    ^> | % 98
    R1*2 \pageBreak | \barNumberCheck #100
    R1*7 \pageBreak | % 107
    R1*6 \pageBreak | % 113
    R1*6 \pageBreak | % 119
    R1 | \barNumberCheck #120
    \stemDown des,2 _\pp \stemUp b2 | % 121
    \stemDown des2 \stemUp bes2 _\< | % 122
    \stemUp ges2 \stemUp es2 | % 123
    des1 ^> _\! _\f _\> | % 124
    R1*4 \bar "|."
    _\! }

PartPOneNineVoiceTwo =  \relative cis {
    \clef "bass" \time 4/4 \key des \major s1*7 \pageBreak s1*6
    \pageBreak s1*6 \pageBreak s1*7 \pageBreak s1*5 \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key b \major s1*7 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak s1 | % 93
     \once \override NoteHead.style = ##f \stemNeutral cis2 s2
    \pageBreak s1*2 \pageBreak s1*4 \pageBreak | \barNumberCheck #100
     \once \override NoteHead.style = ##f \stemNeutral cis2 s2*9 | % 105
     \once \override NoteHead.style = ##f \stemNeutral es2 s1.
    \pageBreak s1*4 | % 111
     \once \override NoteHead.style = ##f \stemNeutral es2 s1.
    \pageBreak s1*6 \pageBreak s4*19 s4*17 _\p \bar "|."
    }

PartPTwoZeroVoiceOne =  \relative des {
    \clef "bass" \time 4/4 \key c \none | % 1
    R1*3 | % 4
    r4 _\ff \stemDown des2. :32 | % 5
    \stemDown des8 _\> r8 _\! r4 r2 | % 6
    R1*2 \pageBreak | % 8
    R1*6 \pageBreak | % 14
    R1*6 \pageBreak | \barNumberCheck #20
    R1*5 | % 25
    r2 \stemDown des2 \trill _\f | % 26
    \stemDown des2 \startTrillSpan \stopTrillSpan _\> \stemDown des8 _\!
    _\pp r8 r4 \pageBreak | % 27
    R1*5 \pageBreak | % 32
    R1*2 | % 34
    \time 2/4  R2 | % 35
    \time 4/4  R1*2 \pageBreak | % 37
    R1*5 \pageBreak | % 42
    R1*4 \bar "||"
    \pageBreak | % 46
    \key b \major R1*7 \pageBreak | % 53
    R1*4 \pageBreak | % 57
    R1*4 \pageBreak | % 61
    R1*3 \pageBreak | % 64
    R1*4 \pageBreak | % 68
    R1*4 \pageBreak | % 72
    R1*7 \pageBreak | % 79
    R1*5 \pageBreak | % 84
    R1*6 \pageBreak | \barNumberCheck #90
    R1*2 \pageBreak | % 92
    R1*2 \pageBreak | % 94
    R1*2 \pageBreak | % 96
    cis1 :32 ^\ff | % 97
    cis1 :32 | % 98
    cis1 :32 _\markup{ \italic {dim.} } _\> | % 99
    cis1 :32 _\! _\> \pageBreak | \barNumberCheck #100
    cis1 :32 _\! _\ppp | % 101
    \stemUp cis4 r4 r2 | % 102
    R1*5 \pageBreak | % 107
    R1*6 \pageBreak | % 113
    R1*6 \pageBreak | % 119
    R1*4 | % 123
    des1 \startTrillSpan \stopTrillSpan _\fz _\> | % 124
    \stemDown des4 _\! _\p r4 r2 | % 125
    R1*3 \bar "|."
    }

PartPTwoZeroVoiceTwo =  \relative d {
    \clef "bass" \time 4/4 \key c \none s1*7 \pageBreak s1*6 \pageBreak
    s1*6 \pageBreak s1*7 \pageBreak s1*5 \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key b \major s1*7 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak s1 | % 93
     \once \override NoteHead.style = ##f \stemNeutral d2 s2 \pageBreak
    s1*2 \pageBreak s1*3 | % 99
     \once \override NoteHead.style = ##f \stemNeutral cis2 \once
    \override NoteHead.style = ##f \stemNeutral cis2 _\! _\p _\>
    \pageBreak s1*5 | % 105
     \once \override NoteHead.style = ##f \stemNeutral d2 s1. \pageBreak
    s1*4 | % 111
     \once \override NoteHead.style = ##f \stemNeutral d2 s1. \pageBreak
    s1*3 | % 116
     \once \override NoteHead.style = ##f \stemNeutral d2 s2*5
    \pageBreak s1*9 \bar "|."
    }

PartPTwoOneVoiceOne =  \relative f' {
    \clef "treble" \time 4/4 \key des \major | % 1
    R1*3 | % 4
    R1 ^ "con sord." | % 5
    \stemUp f4. ( ~ _\ppp \stemUp f8 -- \stemUp f2 ~ | % 6
    \stemUp f8 ) ( -- \stemUp es8 ) -- \stemUp f2. | % 7
    \stemUp f2 ( \stemUp des2 ) \pageBreak | % 8
    c1 | % 9
    des1 | \barNumberCheck #10
    \stemUp des4 ( \stemUp as4 ~ \stemUp as2 ) | % 11
    des1 ~ _\pp | % 12
    des1 | % 13
    des1 ~ \pageBreak | % 14
    des1 _\> | % 15
    \stemUp des2 ( ~ _\! _\ppp \stemUp des8 \stemUp as8 \stemUp f'8
    \stemUp des8 ) | % 16
    c1 | % 17
    \stemUp f4 ( ^\markup{ \italic {molto cresc.} } _\< \stemUp es4 )
    \stemUp des4 ( \stemUp as'4 ) | % 18
    \stemUp <ges bes>4. ( _\! _\f _\markup{ \italic {dim.} } _\> \stemUp
    ges8 \stemUp f2 ) _\! _\p | % 19
    R1 \pageBreak | \barNumberCheck #20
    R1*6 | % 26
    r2 \stemDown f'2 ( ~ _\ppp \pageBreak | % 27
    \stemDown f8. \stemDown as16 \stemDown as4 ) \stemDown ges8 (
    \stemDown es8 \stemDown f4 ) | % 28
    \stemDown des8 ( \stemDown f8 \stemDown es8 \stemDown c8 \stemDown
    des2 ) | % 29
    \stemDown f8. ( \stemDown as16 ) \stemDown as4 \stemDown ges8 (
    \stemDown es8 \stemDown f4 ) | \barNumberCheck #30
    \stemDown des8 ( \stemDown f8 \stemDown es8 \stemDown c8 \stemDown
    des2 ) | % 31
    \stemDown des8 ( \stemDown f8 \stemDown es8 \stemDown c8 \stemDown
    des2 ) \pageBreak | % 32
    \stemDown des8 ( \stemDown f8 \stemDown es8 \stemDown c8 \stemDown
    des8 \stemDown bes8 \stemDown c8 \stemDown as8 ) | % 33
    \stemDown des8 ( _\< \stemDown f8 \stemDown es8 \stemDown c8
    \stemDown des8 \stemDown bes8 \stemDown c8 \stemDown as8 ) | % 34
    \time 2/4  \stemDown des8 ( _\! \stemDown bes8 \stemDown c8
    \stemDown as8 ) | % 35
    \time 4/4  \stemDown des2. ( _\> \stemDown ces8 \stemDown beses8 )
    _\! _\pp | % 36
    as1 ( ~ _\ppp \pageBreak | % 37
    \stemUp as2 ~ \stemUp as8 \stemUp c,4. ) | % 38
    \stemUp des8 ( _\< \stemUp f8 \stemUp es4 ) \stemUp des4 ( \stemUp
    as'4 ) _\! _\f | % 39
    \stemUp <ges bes>2 ( _\fz _\> \stemUp as2 ) _\! | \barNumberCheck
    #40
    R1 | % 41
    \stemDown es'4. ( _\pp \stemDown des8 \stemDown es4 \stemDown bes4 )
    \pageBreak | % 42
    \stemDown des2 ( \stemUp as2 | % 43
    \stemDown des2 \stemUp as2 ~ | % 44
    \stemUp as4 ) r4 r2 | % 45
    R1 \bar "||"
    \pageBreak | % 46
    \key b \major R1*7 \pageBreak | % 53
    R1 | % 54
    \stemUp e32 ( _\p \stemUp gis32 \stemUp e32 \stemUp gis32 \stemUp e32
    \stemUp gis32 \stemUp e32 \stemUp gis32 \stemUp e16 ) r8. r2 | % 55
    r4 \stemUp fis32 ( \stemUp a32 \stemUp fis32 \stemUp a32 \stemUp fis32
    \stemUp a32 \stemUp fis32 \stemUp a32 \stemUp fis16 ) r8. r4 | % 56
    r2 \stemUp fis32 ( \stemUp gis32 \stemUp fis32 \stemUp gis32 \stemUp
    fis32 \stemUp gis32 \stemUp fis32 \stemUp gis32 \stemUp e16 ) r8.
    \pageBreak | % 57
    \stemUp a32 ( \stemUp cis32 \stemUp a32 \stemUp cis32 \stemUp a32
    \stemUp cis32 \stemUp a32 \stemUp cis32 \stemUp a16 ) r8. r4 \stemUp
    gis32 ( \stemUp bis32 \stemUp gis32 \stemUp bis32 \stemUp gis32 ) r16.
    | % 58
    r4 \stemUp e32 ( _\pp \stemUp gis32 \stemUp e32 \stemUp gis32
    \stemUp e32 \stemUp gis32 \stemUp e32 \stemUp gis32 \stemUp e16 ) r8.
    r4 | % 59
    R1 | \barNumberCheck #60
    \stemUp fis32 ( _\fz _\> \stemUp b32 \stemUp fis32 \stemUp b32
    \stemUp fis32 \stemUp b32 \stemUp fis32 \stemUp b32 \stemUp fis16 )
    r8. _\! \stemUp gis32 ( \stemUp b32 \stemUp gis32 \stemUp b32
    \stemUp gis32 ) r16. r4 \pageBreak | % 61
    \stemUp fis32 ( _\p \stemUp a32 \stemUp fis32 \stemUp a32 \stemUp
    fis32 \stemUp a32 \stemUp fis32 \stemUp a32 \stemUp fis16 ) r8.
    \stemUp e32 ( _\pp \stemUp a32 \stemUp e32 \stemUp a32 \stemUp e32 )
    r16. r4 | % 62
    \stemUp a32 ( \stemUp cis32 \stemUp a32 \stemUp cis32 \stemUp a32
    \stemUp cis32 \stemUp a32 \stemUp cis32 \stemUp a16 ) r8. \stemUp
    fis32 ( \stemUp gis32 \stemUp fis32 \stemUp gis32 \stemUp fis32 ) r16.
    r4 | % 63
    \stemUp e32 ( \stemUp gis32 \stemUp e32 \stemUp gis32 \stemUp e32
    \stemUp gis32 \stemUp e32 \stemUp gis32 \stemUp e32 \stemUp gis32
    \stemUp e32 \stemUp gis32 \stemUp e32 \stemUp gis32 \stemUp e32
    \stemUp gis32 \stemUp e32 \stemUp gis32 \stemUp e32 \stemUp gis32
    \stemUp e32 \stemUp gis32 \stemUp e32 \stemUp gis32 ) \stemUp e32 (
    \stemUp gis32 \stemUp e32 \stemUp gis32 \stemUp e32 \stemUp gis32
    \stemUp cis32 \stemUp dis32 ) \pageBreak | % 64
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( _\pp \stemDown dis8 \stemDown cis8 ) }
    \stemDown cis4 ( ~ \stemDown cis8 \stemDown e8 \stemDown dis8
    \stemDown cis8 ) | % 65
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( \stemDown dis8 \stemDown cis8 ) }
    \stemDown cis4 ( ~ \stemDown cis8 \stemDown e8 \stemDown dis8
    \stemDown cis8 ) | % 66
    \times 2/3  {
        \stemUp b8 ( \stemUp gis8 \stemUp b8 }
    \stemDown cis4 ) \stemDown a16 ( \stemDown cis16 \stemDown b16
    \stemDown a16 \stemDown b4 ) _\> | % 67
    \stemUp gis4 ( \times 2/3 {
        \stemUp b8 \stemUp gis8 \stemUp b8 }
    \stemDown cis2 ) _\! _\pp \pageBreak | % 68
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( \stemDown dis8 \stemDown cis8 ) }
    \stemDown cis4 ( ~ \stemDown cis8 \stemDown e8 \stemDown dis8
    \stemDown cis8 ) | % 69
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 ( \stemDown dis8 _\< \stemDown cis8 ) }
    \stemDown cis4 ( ~ \stemDown cis8 \stemDown e8 \stemDown d8
    \stemDown cis8 ) | \barNumberCheck #70
    \times 2/3  {
        \stemDown fis8 ( _\! \stemDown e8 \stemDown d8 ) }
    \stemDown d4 \stemDown a'8 ( _\f \stemDown fis8 \stemDown e8
    \stemDown d8 ) | % 71
    \stemDown d'8 ( _\ff \stemDown cis8 \stemDown bis8 _\> \stemDown b8
    ) \stemDown ais8 ( \stemDown a8 \stemDown gis8 \stemDown fisis8 )
    \pageBreak | % 72
    \stemDown a8 ( _\! _\mf \stemDown gis8 \stemDown fis8 \stemDown e8
    \stemDown dis8 \stemDown cis8 \stemDown bis8 \stemDown fis'8 ) | % 73
    \stemDown e4 ( _\fp \stemDown dis2 ) _\> \stemDown d4 ( | % 74
    \stemDown dis2. ) _\! \stemDown cis4 ( ~ | % 75
    \stemDown cis4 \stemDown bis4 \stemUp a2 ~ | % 76
    \stemUp a4 ) \stemUp gis4 ( \stemUp fisis2 ~ _\pp | % 77
    \stemUp fisis4 ) \stemUp gis4 ( \stemUp a8 \stemUp gis8 \stemUp dis8
    \stemUp e8 ) | % 78
    \stemUp cis2 ( _\pp ^ "sul G" _\< \stemUp dis4 \stemUp e4 ) _\!
    \pageBreak | % 79
    \stemUp gis4 ( \stemUp fis2 ) _\> \stemUp a4 ( _\! | \barNumberCheck
    #80
    \stemUp a4 ) \stemUp gis4 ( ~ \stemUp gis8 \stemUp fis4 \stemUp e8 )
    | % 81
    \stemUp e4 ( \stemUp dis4 ) \stemUp fis4 ( \stemUp e8 \prall \stemUp
    dis8 ) | % 82
    \stemUp e2. \stemUp cis8 ( \stemUp dis8 ) | % 83
    \stemUp e2 _\< \stemUp fis4 ( \stemUp gis4 ) \pageBreak | % 84
    \stemDown b4. ( _\! _\mf \stemDown cis16 \stemDown b16 ) \stemUp b16
    ( \stemUp gis8. ~ \stemUp gis8 \stemUp e8 ) | % 85
    \stemUp fis4. ( \stemUp gis8 ) \stemUp a4 ( \stemUp e4 ) | % 86
    \stemUp e4 ( _\pp \stemUp dis4 ) \stemUp fis4 ( \stemUp e8 \prall
    \stemUp dis8 ) | % 87
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 ( _\pp \stemUp dis8 \stemUp cis8 }
    \stemUp cis4 ~ \stemUp cis8 ) \stemUp e8 \stemUp dis8 \stemUp cis8 | % 88
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 ( \stemUp dis8 \stemUp cis8 }
    \stemUp cis4 ~ \stemUp cis8 ) \stemUp e8 ( \stemUp dis8 \stemUp cis8
    ) | % 89
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp e8 ( \stemUp dis8 \stemUp cis8 ) }
    \stemUp <cis gis'>2. ~ ~ \pageBreak | \barNumberCheck #90
    \stemUp <cis gis'>8 r8 r4 r2 | % 91
    R1 \pageBreak | % 92
    R1 | % 93
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown eis'16 _\p \stemDown fis16 \stemDown gis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown eis16 \stemDown dis16 \stemDown cis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown dis16 \stemDown eis16 \stemDown fis16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown eis16 \stemDown dis16 \stemDown cis16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown dis16 \stemDown eis16 \stemDown fis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown eis16 \stemDown gis16 r16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis16 \stemDown eis16 \stemDown dis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown eis16 \stemDown cis16 r16 }
    \pageBreak | % 94
    \stemDown gis'8 ( \trill ^ "#" _\mf \stemDown cis16 ) r16 \stemDown
    bis8 ( \trill \stemDown cis16 ) r16 _\< \stemDown fis16 ( \prall
    \stemDown dis16 \stemDown cis16 ) r16 \stemDown bis8 ( \trill
    \stemDown cis16 ) r16 | % 95
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown gis16 ( _\! _\f \stemDown gis'16 ) \stemDown gis16
        \stemDown gis16 \stemDown gis16 \stemDown gis16 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 _\< \stemDown gis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown gis,16 ( \stemDown gis'16 ) \stemDown gis16 -. }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown gis,16 ( \stemDown gis'16 ) \stemDown gis16 -. }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown gis,16 ( \stemDown gis'16 ) \stemDown gis16 -. }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown gis,16 ( \stemDown gis'16 ) \stemDown gis16 -. }
    \pageBreak | % 96
    \acciaccatura { \stemUp a,8 ( } \stemDown a'2. ) _\! ^\ff
    \acciaccatura { \stemUp a,8 ( } \stemDown a'8. ) \stemDown a16 -. | % 97
    \stemDown fis16 \stemDown e8. \acciaccatura { \stemUp a,8 ( }
    \stemDown a'2. ) ~ _\ffz | % 98
    \stemDown a4 \stemDown a8. \stemDown a16 \stemDown fis16 \stemDown e8.
    \stemDown a8. \stemDown a16 | % 99
    \stemDown fis16 _\mp \stemDown e8. \stemDown a8. \stemDown a16
    \stemDown fis16 \stemDown e8. \stemDown a,8. \stemDown a16
    \pageBreak | \barNumberCheck #100
    \stemDown fis16 \stemDown e8. \stemDown a8. _\p \stemDown a16 _\>
    \stemDown fis16 \stemDown e8. \stemUp a,8. \stemUp a16 | % 101
    as1 _\! _\pp ^ "4 Violini" | % 102
    as1 | % 103
    \stemUp as2 ( \stemUp a2 ) | % 104
    \stemDown bes4 ( \stemDown c4 \stemDown des2 ) | % 105
    \stemDown bes8. ( ^ "2 Violini con sordini" \stemDown des16
    \stemDown des4 \stemDown c8 \stemDown as8 \stemDown bes4 ) | % 106
    \stemDown bes8 ( \stemDown des8 \stemDown c8 \stemDown as8 \stemDown
    bes2 ) \pageBreak | % 107
    \stemDown bes8 ( \stemDown des8 \stemDown des4 \stemDown c8
    \stemDown as8 ) r4 ^\fermata | % 108
    \stemDown bes2 r4 ^\fermata \stemDown bes8 ( \stemDown des8 | % 109
    \stemDown c8 \stemDown as8 \stemDown bes2 ) r4 ^\fermata |
    \barNumberCheck #110
    \stemUp f8. ( ^ "Solo" _\pp \stemUp as16 \stemUp as4 \stemUp f8.
    \stemUp es16 \stemUp des4 ) | % 111
    \stemUp es8. ( \stemUp f16 \stemUp as8. \stemUp f16 \stemUp es4
    \stemUp e4 ) | % 112
    \stemUp f8. ( ^ "Tutti [con sord.]" ^\markup{ \italic {molto cresc.}
        } _\< \stemUp as16 ) \stemUp as4 \stemDown des8. ( \stemDown es16
    \stemDown f4 ) _\! _\f \pageBreak | % 113
    \stemDown es8. ( _\> \stemDown des16 \stemDown es8 \stemDown c8
    \stemDown des2 ) _\! _\p | % 114
    r2 \stemDown as8 ( _\p \stemDown des8 \stemDown f8 \stemDown as8 ) | % 115
    \stemDown bes2 ( ~ \stemDown bes8 \stemDown as8 \stemDown des8
    \stemDown bes8 ) | % 116
    \stemDown as8 ( \stemDown f8 \stemDown bes8 \stemDown as8 \stemDown
    f8 \stemDown as8 \stemDown f8 \prall \stemDown es8 ) | % 117
    \stemDown des8 ( _\pp \stemDown f8 \stemDown as8 \stemDown f16
    \stemDown es16 \stemDown des8 \prall \stemDown bes8 \stemDown as8
    \stemDown f8 ) | % 118
    \stemUp f4 ( \stemUp des8 \stemUp es8 \stemUp f8 _\markup{ \italic
        {dim.} } _\< \stemUp as4 _\! _\> \stemUp f8 _\! \pageBreak | % 119
    \stemUp f4 _\ppp \stemUp es4 \stemUp des4 \stemUp bes4 |
    \barNumberCheck #120
    \stemUp des4 ) r4 r2 | % 121
    R1*3 | % 124
    r8 \stemDown des'8 ( _\pp \stemDown f8 \stemDown as8 \stemDown des8
    \stemDown es8 \stemDown f8 \stemDown as8 ) | % 125
    des1 ~ _\ppp | % 126
    \stemDown des4 r4 r2 | % 127
    R1 \bar "|."
    }

PartPTwoOneVoiceTwo =  \relative cis'' {
    \clef "treble" \time 4/4 \key des \major s1*7 \pageBreak s1*6
    \pageBreak s1*6 \pageBreak s1*7 \pageBreak s1*5 \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key b \major \once \override NoteHead.style = ##f \stemNeutral cis2
    s2*9 | % 51
     \once \override NoteHead.style = ##f \stemNeutral cis2 s1.
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*3 \pageBreak s1*4
    \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5 \pageBreak s1*6
    \pageBreak s1 | % 91
     \once \override NoteHead.style = ##f \stemNeutral e,2 s2 \pageBreak
    s1*2 \pageBreak s1*2 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*6
    \pageBreak s1*6 \pageBreak s1*9 \bar "|."
    }

PartPTwoOneVoiceThree =  \relative gis'' {
    \clef "treble" \time 4/4 \key des \major s1*7 \pageBreak s1*6
    \pageBreak s1*6 \pageBreak s1*7 \pageBreak s1*5 \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key b \major s1*7 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak s1*2 \pageBreak | % 94
     \once \override NoteHead.style = ##f \stemNeutral gis32 \once
    \override NoteHead.style = ##f \stemNeutral ais32 \once \override
    NoteHead.style = ##f \stemNeutral gis32 \once \override
    NoteHead.style = ##f \stemNeutral ais32 s8*15 \pageBreak s1*4
    \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*9 \bar
    "|."
    }

PartPTwoTwoVoiceOne =  \relative des' {
    \clef "treble" \time 4/4 \key des \major | % 1
    R1*3 | % 4
    R1 ^ "con sord." | % 5
    \stemUp des4. ( ~ _\ppp \stemUp des8 -- \stemUp des2 ~ | % 6
    \stemUp des8 ) ( -- \stemUp c8 ) -- \stemUp des2. | % 7
    \stemUp des2 ( \stemUp as2 ~ \pageBreak | % 8
    as1 ) | % 9
    \stemUp as2 ( \stemUp a2 ) | \barNumberCheck #10
    \stemUp bes4 ( \stemUp c4 \stemUp des2 ) | % 11
    \stemUp bes2 ( _\pp \stemUp as4 \stemUp bes4 ) | % 12
    \stemUp bes4 ( \stemUp as4 \stemUp bes2 ) | % 13
    \stemUp bes2 ( _\< \stemUp as4 \stemUp bes4 ) \pageBreak | % 14
    \stemUp bes4 _\! \stemUp as4 \stemUp bes2 | % 15
    as1 _\ppp | % 16
    as1 | % 17
    \stemUp as2 ( ^\markup{ \italic {molto cresc.} } _\< \stemUp des2 )
    | % 18
    \stemUp des4. _\! _\f _\markup{ \italic {dim.} } _\> \stemUp bes8
    \stemUp as2 _\! _\p | % 19
    R1 \pageBreak | \barNumberCheck #20
    R1*6 | % 26
    r2 \stemUp as'2 ~ _\ppp \pageBreak | % 27
    as1 | % 28
    f1 | % 29
    as1 | \barNumberCheck #30
    \stemUp f2 ( ~ \stemUp f8 \stemUp f4 ) -- \stemUp f8 ( -- | % 31
    \stemUp f2 ) ~ \stemUp f8 \stemUp f4 -- \stemUp f8 ~ -- \pageBreak | % 32
    f1 ~ | % 33
    f1 _\< | % 34
    \time 2/4  \stemUp f2 _\! | % 35
    \time 4/4  \stemUp f4 ( _\> \stemUp ges4 \stemUp <e g>2 ) _\! _\pp | % 36
    \stemUp as4 ( _\ppp \stemUp f4 \stemUp des2 ) \pageBreak | % 37
    \stemUp c2 ( ~ \stemUp c8 \stemUp ges'8 \stemUp f8 \stemUp es8 ) | % 38
    \stemUp as,2 ( _\< \stemUp des2 ) | % 39
    \stemUp bes2 ( _\! _\fz _\f _\> \stemUp des2 ) _\! | \barNumberCheck
    #40
    R1 | % 41
    \stemDown bes'2. ( _\pp \stemUp es,4 \pageBreak | % 42
    \stemUp f4 ) r4 r2 | % 43
    R1*3 \bar "||"
    \pageBreak | % 46
    \key b \major \stemUp gis2 :32 _\pp \stemUp fis2 :32 | % 47
    \stemUp gis2 :32 \stemUp fis2 :32 | % 48
    \stemUp dis4 :32 _\< \stemUp e2 :32 \stemUp dis4 :32 _\! _\mf | % 49
    \stemUp gis2 :32 \stemUp gis2 :32 _\p _\> | \barNumberCheck #50
    \stemUp gis2 :32 _\! _\pp \stemUp fis2 :32 | % 51
    \stemUp gis2 :32 _\< \stemUp fis2 :32 | % 52
    \stemUp <cis e>2 :32 _\! _\< \stemUp <cis e>2 :32 _\! \pageBreak | % 53
    <cis e gis>1 :32 ^^ ^ "div." _\f | % 54
    \stemUp <cis e gis>8 _\pp r8 r4 r2 | % 55
    R1*2 \pageBreak | % 57
    R1 | % 58
    r4 \stemUp <cis e>4 ^ "pizz." \stemUp <cis e>4 r4 | % 59
    R1*2 \pageBreak | % 61
    R1*3 \pageBreak | % 64
    \stemUp gis'2 :32 _\pp ^ "arco" \stemUp fis2 :32 | % 65
    \stemUp gis2 :32 \stemUp fis2 :32 | % 66
    \stemUp dis4 :32 \stemUp e2 :32 _\f \stemUp dis4 :32 | % 67
    \stemUp e4 :32 \stemUp gis2. :32 _\pp \pageBreak | % 68
    \stemUp gis2 :32 \stemUp <g a>2 :32 | % 69
    \stemUp gis2 :32 _\< \stemUp <g a>2 :32 | \barNumberCheck #70
    \stemUp <fis a>2 :32 _\! \stemUp a2 :32 _\f | % 71
    \stemDown e'2 :32 _\ff \stemDown cis4. :32 _\> \stemDown e32
    \stemDown e32 \stemDown e32 \stemDown e32 \pageBreak | % 72
    \stemDown <bis fis'>8 _\! _\mf r8 r4 r2 | % 73
    \stemDown bis2 ( _\fp _\> \stemUp a2 ) | % 74
    \stemDown b2 _\! \stemUp <g ais>2 | % 75
    \stemUp <fis a>2. ( \stemUp e4 ) | % 76
    dis1 ~ _\pp | % 77
    \stemUp dis8 r8 r4 r2 | % 78
    r4 r8 \stemUp <gis, e'>8 _\pp ^ "pizz." r4 r8 \stemUp <gis e'>8
    \pageBreak | % 79
    r4 r8 \stemUp <a fis'>8 r4 r8 \stemUp <a fis'>8 | \barNumberCheck
    #80
    r4 r8 \stemUp <gis gis'>8 r4 r8 \stemUp <e' cis'>8 | % 81
    r4 r8 \stemUp <cis a'>8 r4 r8 \stemUp <gis gis'>8 | % 82
    r4 r8 \stemUp <cis gis'>8 r4 r8 \stemUp <gis gis'>8 | % 83
    r4 r8 \stemUp <cis gis'>8 _\< r4 r8 \stemUp <gis e'>8 \pageBreak | % 84
    r4 _\! r8 \stemUp <dis' fis>8 _\mf r4 r8 \stemUp <b gis'>8 | % 85
    \stemUp <a a'>8 r8 r8 \stemUp <d d'>8 \stemUp <e cis'>8 r8 \stemUp
    <gis, gis'>8 r8 | % 86
    \stemUp <cis a'>8 _\pp r8 r8 \stemUp <cis a'>8 r4 r8 \stemUp <gis
        gis'>8 | % 87
    \stemUp gis2 ( _\pp ^ "arco" \stemUp a2 ) | % 88
    \stemUp gis2 ( \stemUp a2 ) | % 89
    gis1 ~ \pageBreak | \barNumberCheck #90
    \stemUp gis8 r8 r4 r2 | % 91
    R1 \pageBreak | % 92
    <cis gis'>1 _\pp | % 93
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp eis16 _\p \stemUp fis16 \stemUp gis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp eis16 \stemUp dis16 \stemUp cis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp dis16 \stemUp eis16 \stemUp fis16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp eis16 \stemUp dis16 \stemUp cis16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemUp dis16 \stemUp eis16 \stemUp fis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp eis16 \stemUp gis16 r16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp fis16 \stemUp eis16 \stemUp dis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemUp eis16 \stemUp cis16 r16 }
    \pageBreak | % 94
    \stemUp gis'8 ( \trill ^ "#" _\mf \stemUp cis16 ) r16 \stemDown bis8
    ( \trill \stemDown cis16 ) r16 _\< \stemDown fis16 ( \prall
    \stemDown dis16 \stemDown cis16 ) r16 \stemDown bis8 ( \trill
    \stemDown cis16 ) r16 | % 95
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown gis16 ( _\! _\f \stemDown gis'16 ) \stemDown gis16
        \stemDown gis16 \stemDown gis16 \stemDown gis16 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown gis16 \stemDown gis16 \stemDown gis16 \stemDown gis16
        \stemDown gis16 _\< \stemDown gis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown gis,16 ( \stemDown gis'16 ) \stemDown gis16 -. }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown gis,16 ( \stemDown gis'16 ) \stemDown gis16 -. }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown gis,16 ( \stemDown gis'16 ) \stemDown gis16 -. }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown gis,16 ( \stemDown gis'16 ) \stemDown gis16 -. }
    \pageBreak | % 96
    \acciaccatura { \stemUp a,8 ( } \stemDown a'2. ) _\! ^\ff
    \acciaccatura { \stemUp a,8 ( } \stemDown a'8. ) \stemDown a16 -. | % 97
    \stemDown fis16 \stemDown e8. \acciaccatura { \stemUp a,8 ( }
    \stemDown a'2. ) ~ _\ffz | % 98
    \stemDown a4 \stemDown a8. \stemDown a16 \stemDown fis16 \stemDown e8.
    \stemDown a8. \stemDown a16 | % 99
    \stemDown fis16 _\mp \stemDown e8. \stemDown a8. \stemDown a16
    \stemDown fis16 \stemDown e8. \stemUp a,8. \stemUp a16 \pageBreak |
    \barNumberCheck #100
    \stemUp fis16 \stemUp e8. \stemUp a8. _\p \stemUp a16 _\> \stemUp
    fis16 \stemUp e8. \stemUp a,8. \stemUp a16 | % 101
    as1 _\! _\pp ^ "4 Violini" | % 102
    as1 | % 103
    \stemUp as2 ( \stemUp a2 ) | % 104
    \stemUp bes4 ( \stemUp c4 \stemUp des2 ) | % 105
    \stemUp des8 ^ "2 Violini con sordini" \stemUp des4 \stemUp des4
    \stemUp des4 \stemUp des8 ~ | % 106
    \stemUp des8 \stemUp des4 \stemUp des4 \stemUp des4 \stemUp des8 ~
    \pageBreak | % 107
    \stemUp des8 \stemUp des4 \stemUp des4 \stemUp des8 r4 ^\fermata | % 108
    \stemUp des8 \stemUp des4 \stemUp des8 r4 ^\fermata \stemUp des8
    \stemUp des8 ~ | % 109
    \stemUp des8 \stemUp des8 ~ \stemUp des8 \stemUp des4 \stemUp des8 r4
    ^\fermata | \barNumberCheck #110
    R1*2 | % 112
    \stemUp des4 ( _\pp ^ "Tutti [con sord.]" _\< \stemUp es4
    \stemUp des2 ) \pageBreak | % 113
    \stemUp ges2 ( _\! _\f _\> \stemUp f2 ) _\! _\p | % 114
    R1*5 \pageBreak | % 119
    R1*5 | % 124
    r8 \stemDown f8 ( _\pp \stemDown des'8 \stemDown es8 \stemDown f8
    \stemDown as8 \stemDown des8 \stemDown es8 ) | % 125
    f1 ~ _\ppp | % 126
    \stemDown f4 r4 r2 | % 127
    R1 \bar "|."
    }

PartPTwoTwoVoiceTwo =  \relative f' {
    \clef "treble" \time 4/4 \key des \major s1*7 \pageBreak s1*6
    \pageBreak s1*6 \pageBreak s1*7 \pageBreak s1*5 \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1 | % 36
    \stemDown f4 \stemDown des4 \stemDown des2 \pageBreak s1*5
    \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key b \major s1*7 \pageBreak s1*4 \pageBreak s1*3 | \barNumberCheck
    #60
     \once \override NoteHead.style = ##f \stemNeutral cis'2 s2
    \pageBreak s1 | % 62
     \once \override NoteHead.style = ##f \stemNeutral cis2 s1.
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak s1*2 \pageBreak s1*2
    \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*6 \pageBreak | % 113
    \stemDown beses,2 ( \stemDown as2 ) s1*2 | % 116
     \once \override NoteHead.style = ##f \stemNeutral es'2 s2*5
    \pageBreak s1*9 \bar "|."
    }

PartPTwoTwoVoiceThree =  \relative gis' {
    \clef "treble" \time 4/4 \key des \major s1*7 \pageBreak s1*6
    \pageBreak s1*6 \pageBreak s1*7 \pageBreak s1*5 \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key b \major s1*7 \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*3
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak s1*2 \pageBreak | % 94
     \once \override NoteHead.style = ##f \stemNeutral gis32 \once
    \override NoteHead.style = ##f \stemNeutral ais32 \once \override
    NoteHead.style = ##f \stemNeutral gis32 \once \override
    NoteHead.style = ##f \stemNeutral ais32 s8*15 \pageBreak s1*4
    \pageBreak s1*7 \pageBreak s1*6 \pageBreak s1*6 \pageBreak s1*9 \bar
    "|."
    }

PartPTwoThreeVoiceOne =  \relative as {
    \clef "alto" \time 4/4 \key des \major | % 1
    R1*3 | % 4
    R1 ^ "con sord." | % 5
    \stemUp as4. ( ~ ^ "div." _\ppp \stemUp as8 -- \stemUp as2 ~ | % 6
    \stemUp as8 ) -- \stemUp as8 -- \stemUp as2. | % 7
    \stemUp <f as>2 ( \stemUp f2 ) \pageBreak | % 8
    <es ges>1 | % 9
    \stemUp f2 ( \stemUp f2 ) | \barNumberCheck #10
    \stemUp ges2 ( \stemUp f2 ) | % 11
    des1 ~ _\pp | % 12
    des1 | % 13
    des1 ~ _\< \pageBreak | % 14
    des1 _\! _\> | % 15
    <des f>1 _\! _\ppp | % 16
    \stemUp ges4 ( \stemUp es8. \stemUp f16 \stemUp ges2 ) | % 17
    \stemUp f4 ^\markup{ \italic {molto cresc.} } _\< \stemUp es4
    \stemUp f2 | % 18
    \stemUp <des ges>2 ( _\! _\f _\markup{ \italic {dim.} } _\> \stemUp
    <des f>2 ) _\! _\p | % 19
    R1 \pageBreak | \barNumberCheck #20
    R1*6 | % 26
    r2 \stemUp as'2 ~ _\ppp \pageBreak | % 27
    as1 | % 28
    \stemUp bes8 ( \stemUp des8 \stemUp c8 \stemUp as8 \stemUp bes2 ) | % 29
    as1 | \barNumberCheck #30
    \stemUp bes8 ( \stemUp des8 \stemUp c8 \stemUp as8 \stemUp bes2 ) | % 31
    \stemUp bes8 ( \stemUp des8 \stemUp c8 \stemUp as8 \stemUp bes2 )
    \pageBreak | % 32
    \stemUp bes8 ( \stemUp des8 \stemUp c8 \stemUp as8 \stemUp bes8
    \stemUp ges8 \stemUp as8 \stemUp f8 ) | % 33
    \stemUp bes8 ( _\< \stemUp des8 \stemUp c8 \stemUp as8 \stemUp bes8
    \stemUp ges8 \stemUp as8 \stemUp f8 ) | % 34
    \time 2/4  \stemUp bes8 _\! \stemUp ges8 \stemUp as8 \stemUp f8 | % 35
    \time 4/4  \stemUp bes4 ( _\> \stemUp beses2. ) _\pp | % 36
    <f as>1 _\! _\ppp \pageBreak | % 37
    \stemUp ges4 ( \stemUp bes8. \stemUp as16 \stemUp ges8 \stemUp bes8
    \stemUp as8 \stemUp ges8 ) | % 38
    \stemUp f4 ( _\< \stemUp es4 ) \stemUp f2 | % 39
    \stemUp des2 ( _\! _\f _\fz _\> \stemUp f2 ) _\! | \barNumberCheck
    #40
    R1 | % 41
    des'1 _\pp \pageBreak | % 42
    as1 ~ | % 43
    \stemUp as8 r8 r4 r2 | % 44
    R1*2 \bar "||"
    \pageBreak | % 46
    \key b \major \stemDown cis2 :32 _\pp \stemUp a2 :32 | % 47
    \stemDown cis2 :32 \stemUp a2 :32 | % 48
    \stemUp gis2 :32 _\< \stemUp fis4 :32 _\! _\mf \stemUp b4 :32 | % 49
    \stemDown e2 :32 \stemDown <cis e>2 :32 _\p _\> | \barNumberCheck
    #50
    \stemDown cis2 :32 _\! _\pp \stemUp a2 :32 | % 51
    \stemDown cis2 :32 _\< \stemDown a'2 :32 | % 52
    \stemDown cis,4 :32 _\! _\< \stemUp b4 :32 \stemUp a2 :32 _\!
    \pageBreak | % 53
    \times 2/3  {
        \stemUp cis,8 ( ^^ _\f \stemUp gis'8 \stemUp cis8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown e8 \stemDown gis8 \stemDown cis8 ) }
    \stemDown cis2 ~ | % 54
    \stemDown cis8 _\pp r8 r4 r2 | % 55
    R1*2 \pageBreak | % 57
    R1*4 \pageBreak | % 61
    R1*3 \pageBreak | % 64
    \stemDown cis,2 :32 _\pp \stemUp a2 :32 | % 65
    \stemDown cis2 :32 \stemUp a2 :32 | % 66
    \stemUp gis2 :32 \stemUp fis4 :32 _\f \stemUp b4 :32 | % 67
    \stemDown e2 :32 \stemDown <cis e>2 :32 _\pp \pageBreak | % 68
    \stemDown <cis e>2 :32 \stemDown e2 :32 | % 69
    \stemDown <cis e>2 :32 _\< \stemDown e2 :32 | \barNumberCheck #70
    \stemDown d2 :32 _\! \stemDown fis2 :32 _\f | % 71
    \stemDown gis2 :32 _\ff \stemDown gis2 :32 _\> \pageBreak | % 72
    \stemDown gis8 _\! _\mf r8 r4 r2 | % 73
    \stemDown a2 ( _\fp _\> \stemDown fis2 ) _\! | % 74
    \stemDown g4 ( \stemDown fis4 \stemDown e2 ) | % 75
    \stemDown dis2. ( \stemDown cis4 ) | % 76
    bis1 ~ _\pp | % 77
    \stemUp bis8 r8 r4 r2 | % 78
    r4 \stemUp cis,4 :32 _\pp \stemUp cis16 r8. r4 \pageBreak | % 79
    r4 \stemUp a'4 :32 \stemUp a16 r8. r4 | \barNumberCheck #80
    r4 \stemUp gis4 :32 \stemUp gis16 r8. r4 | % 81
    r4 \stemUp a4 :32 \stemUp a16 r8. \stemUp gis4 :32 | % 82
    \stemUp gis2 :32 \stemUp gis16 r8. r4 | % 83
    r4 \stemUp cis,4 :32 _\< \stemUp cis16 _\! r8. r4 \pageBreak | % 84
    r4 \stemUp a'4 :32 \stemUp a16 r8. r4 | % 85
    \stemUp a4 :32 \stemUp a16 r8. r4 \stemUp gis4 :32 | % 86
    \stemUp a16 _\pp r8. \stemUp a4 :32 \stemUp a16 r8. \stemUp gis4 :32
    | % 87
    \stemUp <cis, e>2 _\pp \stemUp <cis g'>2 | % 88
    \stemUp <cis e>2 \stemUp <cis g'>2 | % 89
    \stemUp <cis e>4 \stemUp <cis eis>2. ~ ~ \pageBreak |
    \barNumberCheck #90
    \stemUp <cis eis>8 r8 r4 r2 | % 91
    <cis gis'>1 ~ ~ _\pp \pageBreak | % 92
    <cis gis'>1 | % 93
    <cis gis'>1 _\p _\< \pageBreak | % 94
    \stemUp gis'16 ( _\! _\mf \stemUp eis16 ) \stemUp gis16 ( \stemUp
    eis16 ) \stemUp fis16 ( \stemUp gis16 ) \stemUp gis16 ( _\< \stemUp
    eis16 ) \stemUp fis16 ( \stemUp gis16 ) \stemUp gis16 ( \stemUp eis16
    ) \stemUp fis16 ( \stemUp gis16 ) \stemUp gis16 ( \stemUp eis16 ) | % 95
    \stemUp ais16. _\! _\f \stemUp bis32 \stemUp gis8 \stemUp ais16.
    \stemUp bis32 \stemUp gis8 _\< \stemUp ais16. \stemUp bis32 \stemUp
    ais16. \stemUp bis32 \stemUp ais16. \stemUp bis32 \stemUp ais16.
    \stemUp bis32 \pageBreak | % 96
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp cis16 _\! ^\ff \stemUp cis16 \stemUp cis16 \stemUp cis16
        \stemUp cis16 \stemUp cis16 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp cis4. :64 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp cis4. :64 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp cis4. :64 }
    | % 97
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp cis4. :64 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp cis4. :64 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp cis4. :64 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp cis4. :64 }
    | % 98
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp cis4. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp cis4. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp cis4. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp cis4. :64 }
    | % 99
    \stemUp cis4 _\mp \stemUp cis8. ( \stemUp e16 \stemUp e4 ) \stemUp
    cis8. ( \stemUp e16 \pageBreak | \barNumberCheck #100
    \stemUp e4 ) \stemUp cis8. ( _\p \stemUp e16 _\> \stemUp e4 )
    \stemUp cis8. ( \stemUp e16 | % 101
    <des f>1 ) _\! ^ "4 Viole" _\pp | % 102
    des1 | % 103
    <des, des'>1 | % 104
    \stemUp des'4 ( ^ "div." \stemUp c4 \stemUp as2 ) | % 105
    \stemUp ges8 ( ^ "2 Viole con sordini" \stemUp bes8 \stemUp bes4
    \stemUp as8 \stemUp f8 \stemUp ges4 ) | % 106
    \stemUp ges8 ( \stemUp bes8 \stemUp as8 \stemUp f8 \stemUp ges2 )
    \pageBreak | % 107
    \stemUp ges8 ( \stemUp bes8 \stemUp bes4 \stemUp as8 \stemUp f8 ) r4
    ^\fermata | % 108
    \stemUp ges2 r4 ^\fermata \stemUp ges8 ( \stemUp bes8 | % 109
    \stemUp as8 \stemUp f8 \stemUp ges2 ) r4 ^\fermata | \barNumberCheck
    #110
    des1 ~ ^ "Solo" _\pp | % 111
    des1 | % 112
    \stemUp f8. ( ^ "Tutti [con sord.]" _\< \stemUp as16 ) \stemUp as4
    \stemDown des8. ( \stemDown es16 \stemDown f4 ) _\! _\f \pageBreak | % 113
    \stemUp es2 ( _\> \stemUp as2 ) _\! _\p | % 114
    R1*5 \pageBreak | % 119
    R1*6 | % 125
    \clef "treble" as'1 ~ _\ppp | % 126
    \stemDown as4 r4 r2 | % 127
    R1 \bar "|."
    }

PartPTwoThreeVoiceTwo =  \relative f {
    \clef "alto" \time 4/4 \key des \major s1*4 | % 5
    \stemDown f4. ( ~ \stemDown f8 -- \stemDown f2 ~ | % 6
    \stemDown f8 ) -- \stemDown es8 -- \stemDown f2. | % 7
    \stemDown des2 ~ \stemDown des2 \pageBreak s1 | % 9
    \stemDown des2 ( \stemDown f2 ) | \barNumberCheck #10
    \stemDown ges2 ( \stemDown des2 ) s1*3 \pageBreak s1*6 \pageBreak
    s1*7 \pageBreak s1*5 \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s1*2 \pageBreak s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key b \major s1*7 \pageBreak s1*4 \pageBreak | % 57
     \once \override NoteHead.style = ##f \stemNeutral cis'2 s2*5 |
    \barNumberCheck #60
     \once \override NoteHead.style = ##f \stemNeutral cis2 s2
    \pageBreak s1 | % 62
     \once \override NoteHead.style = ##f \stemNeutral cis2 s1.
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*5
    \pageBreak s1*6 \pageBreak s1*2 \pageBreak s1*2 \pageBreak s1 | % 95
    \stemDown fis,8 \stemDown eis8 \stemDown fis8 \stemDown eis8
    \stemDown fis8 \stemDown fis8 \stemDown fis8 \stemDown fis8
    \pageBreak | % 96
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown a16 \stemDown a16 \stemDown a16 \stemDown a16
        \stemDown a16 \stemDown a16 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown a4. :64 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown a4. :64 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown a4. :64 }
    | % 97
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown a4. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown a4. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown a4. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown a4. :64 }
    | % 98
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown a4. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown a4. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown a4. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown a4. :64 }
    | % 99
    \stemDown a4 \stemDown a8. ( \stemDown cis16 \stemDown cis4 )
    \stemDown a8. ( \stemDown cis16 \pageBreak | \barNumberCheck #100
    \stemDown cis4 ) \stemDown a8. ( \stemDown cis16 \stemDown cis4 )
    \stemDown a8. ( \stemDown cis16 s1*3 | % 104
    \stemDown es,4 \stemDown as4 \stemDown as2 ) s1*2 \pageBreak s1*6
    \pageBreak | % 113
    \stemDown des2 ( \stemDown as2 ) s1*2 | % 116
     \once \override NoteHead.style = ##f \stemNeutral es'2 s2*5
    \pageBreak s1*6 | % 125
    \clef "treble" s1*3 \bar "|."
    }

PartPTwoFourVoiceOne =  \relative des {
    \clef "bass" \time 4/4 \key des \major | % 1
    R1*3 | % 4
    R1 ^ "con sord." | % 5
    \stemDown des4. ( ~ _\ppp \stemDown des8 -- \stemDown des2 ~ | % 6
    \stemUp des8 ) _- \stemUp as8 _- \stemUp des2. ^ "div." | % 7
    <des, as'>1 \pageBreak | % 8
    <des as'>1 | % 9
    \stemUp as'2 ( \stemUp des2 ) | \barNumberCheck #10
    \stemUp des4 ( \stemUp as4 ) \stemUp as2 | % 11
    ges1 ~ _\pp | % 12
    ges1 | % 13
    ges1 ~ _\< \pageBreak | % 14
    ges1 _\! _\> | % 15
    des1 ~ _\! _\ppp | % 16
    des1 | % 17
    \stemDown des'4 ^\markup{ \italic {molto cresc.} } _\< \stemUp c4
    \stemUp bes4 \stemUp as4 ~ | % 18
    as1 _\! _\f _\markup{ \italic {dim.} } _\> | % 19
    R1 \pageBreak | \barNumberCheck #20
    R1 | % 21
    \once \omit TupletBracket
    \times 2/3  {
        r8 _\! \stemUp des,8 ( _\pp \stemUp as'8 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown des8 \stemDown f8 \stemDown as8 }
    \stemDown des8 ) r8 r4 | % 22
    R1*4 | % 26
    r2 \stemDown des2 ( ~ _\ppp \pageBreak | % 27
    \stemDown des8 \stemDown f8 \stemDown f4 ) \stemDown es8 ( \stemDown
    c8 \stemDown des4 ) | % 28
    \stemDown bes8 ( \stemDown des8 \stemDown c8 \stemDown as8 \stemDown
    bes2 ) | % 29
    \stemDown des8 ( \stemDown f8 \stemDown f4 \stemDown es8 \stemDown c8
    \stemDown des4 ) | \barNumberCheck #30
    \stemDown bes8 ( \stemDown des8 \stemDown c8 \stemDown as8 \stemDown
    bes2 ) | % 31
    \stemDown bes8 ( \stemDown des8 \stemDown c8 \stemDown as8 \stemDown
    bes2 ) \pageBreak | % 32
    \stemDown bes8 ( \stemDown des8 \stemDown c8 \stemDown as8 \stemDown
    bes8 \stemDown ges8 \stemDown as8 \stemDown f8 ) | % 33
    \stemDown bes8 ( _\< \stemDown des8 \stemDown c8 \stemDown as8
    \stemDown bes8 \stemDown ges8 \stemDown as8 \stemDown f8 ) | % 34
    \time 2/4  \stemDown bes8 ( _\! \stemDown ges8 \stemDown as8
    \stemDown f8 ) | % 35
    \time 4/4  \stemDown bes4 ( _\> \stemDown beses2. ) _\pp | % 36
    \stemDown as4 _\! _\ppp \stemUp des,2. ~ ^ "div." \pageBreak | % 37
    <as des>1 | % 38
    \stemUp des'4 ( _\< \stemUp c4 ) \stemUp bes4 ( \stemUp as4 ) _\!
    _\f | % 39
    \stemUp ges2 ( _\fz _\> \stemUp des2 ) _\! | \barNumberCheck #40
    R1 | % 41
    ges1 ( _\pp \pageBreak | % 42
    des1 ) ( | % 43
    des,1 ) | % 44
    des1 ~ | % 45
    \stemUp des4 r4 r2 \bar "||"
    \pageBreak | % 46
    \key b \major R1*6 | % 52
    \clef "tenor" \stemDown gis''2 ( _\p _\< \stemDown cis2 ) _\! _\fz
    \pageBreak | % 53
    \stemDown cis2 ~ _\f _\> \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 _\! \stemDown gis8 \stemDown e8 }
    \clef "bass" \once \omit TupletBracket
    \times 2/3  {
        \stemDown cis8 \stemDown gis8 \stemDown cis,8 ~ }
    | % 54
    \stemUp cis8 _\pp r8 r4 r2 | % 55
    R1*2 \pageBreak | % 57
    R1*4 \pageBreak | % 61
    R1*3 \pageBreak | % 64
    R1*4 \pageBreak | % 68
    R1*4 \pageBreak | % 72
    R1*4 | % 76
    r2 \stemUp bis2 :32 _\ppp | % 77
    bis1 :32 _\> | % 78
    \stemUp cis8 :32 _\! _\ppp \stemUp gis8 :32 \stemUp e8 :32 \stemUp
    cis8 :32 \stemUp fis8 :32 \stemUp a8 :32 \stemUp gis8 :32 \stemUp
    cis,8 :32 \pageBreak | % 79
    \stemUp fis8 :32 \stemUp a8 :32 \stemUp d8 :32 \stemUp e8 :32
    \stemUp fis8 :32 \stemUp d8 :32 \stemUp cis8 :32 \stemUp bis8 :32 |
    \barNumberCheck #80
    \stemUp cis8 :32 \stemUp dis8 :32 \stemUp e8 :32 \stemUp ais,8 :32
    \stemUp bis8 :32 \stemUp gis8 :32 \stemUp cis8 :32 \stemUp a8 :32 | % 81
    \stemUp fis8 :32 \stemUp gis8 :32 \stemUp a8 :32 \stemUp fis8 :32
    \stemUp dis8 :32 \stemUp fis8 :32 \stemUp gis8 :32 \stemUp bis,8 :32
    | % 82
    \stemUp cis8 :32 \stemUp cis'8 :32 \stemUp b8 :32 \stemUp a8 :32
    \stemUp gis8 :32 \stemUp fis8 :32 \stemUp e8 :32 \stemUp dis8 :32 | % 83
    \stemUp cis8 :32 _\< \stemUp gis'8 :32 \stemUp e8 :32 \stemUp cis8
    :32 \stemUp a'8 :32 \stemUp fis8 :32 \stemUp cis8 :32 \stemUp cis'8
    :32 \pageBreak | % 84
    \stemDown b8 :32 _\! \stemDown fis'8 :32 \stemDown dis8 :32
    \stemDown b8 :32 \stemUp e8 :32 \stemUp b8 :32 \stemUp gis8 :32
    \stemUp e8 :32 | % 85
    \stemUp d'8 :32 \stemUp a8 :32 \stemUp fis8 :32 \stemUp b8 :32
    \stemUp a8 :32 \stemUp b8 :32 \stemUp cis8 :32 \stemUp cis,8 :32 | % 86
    \stemUp fis8 :32 _\pp \stemUp gis8 :32 \stemUp a8 :32 \stemUp fis8
    :32 \stemUp dis8 :32 \stemUp fis8 :32 \stemUp gis8 :32 \stemUp bis,8
    :32 | % 87
    \acciaccatura { \stemUp cis8 ( } \stemUp gis'2 ) ( _\pp \stemUp a2 )
    | % 88
    \stemUp gis2 ( \stemUp a2 ) | % 89
    gis1 \pageBreak | \barNumberCheck #90
    <cis, gis'>1 ~ ~ _\pp | % 91
    <cis gis'>1 ~ ~ \pageBreak | % 92
    <cis gis'>1 | % 93
    <cis gis'>1 _\p _\< \pageBreak | % 94
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown eis'16 _\! _\mf \stemDown fis16 \stemDown gis16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown eis16 \stemDown dis16 \stemDown cis16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown dis16 \stemDown eis16 \stemDown fis16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown eis16 \stemDown dis16 _\< \stemDown cis16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown dis16 \stemDown eis16 \stemDown fis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown eis16 \stemDown gis16 r16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown fis16 \stemDown eis16 \stemDown dis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown eis16 \stemDown cis16 r16 }
    _\! | % 95
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis16 _\f \stemDown eis16 \stemDown dis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown eis16 \stemDown cis16 r16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis16 \stemDown eis16 \stemDown dis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown eis16 \stemDown cis16 _\< r16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis16 \stemDown eis16 \stemDown dis16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown fis16 \stemDown eis16 \stemDown dis16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown fis16 \stemDown eis16 \stemDown dis16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown fis16 \stemDown eis16 \stemDown dis16 }
    \pageBreak | % 96
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp e16 _\! ^\ff \stemUp e16 \stemUp e16 \stemUp e16 \stemUp
        e16 \stemUp e16 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp e4. :64 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp e4. :64 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp e4. :64 }
    | % 97
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp e4. :64 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp e4. :64 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp e4. :64 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp e4. :64 }
    | % 98
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp e4. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp e4. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp e4. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp e4. :64 }
    | % 99
    \stemUp e4 _\mp \stemUp e8. ( \stemUp gis16 \stemUp gis4 ) \stemUp e8.
    ( \stemUp gis16 \pageBreak | \barNumberCheck #100
    \stemUp e4 ) \stemUp cis8. ( _\p \stemUp e16 _\> \stemUp e4 )
    \stemUp cis8. ( \stemUp e16 | % 101
    <des f>1 ) _\! ^ "4 Violoncelli" _\pp | % 102
    <des ges>1 | % 103
    \stemUp f2 \stemUp f2 | % 104
    \stemUp ges2 ( \stemUp f2 ) | % 105
    ges,1 ~ ^ "2 Violoncelli" _\pp | % 106
    ges1 ~ \pageBreak | % 107
    \stemUp ges2. r4 ^\fermata | % 108
    \stemUp ges2 r4 ^\fermata \stemUp ges4 ~ | % 109
    \stemUp ges2 ~ \stemUp ges4 r4 ^\fermata | \barNumberCheck #110
    \stemDown des''8. ( _\pp _ "Solo" \stemDown f16 \stemDown f4
    \stemDown des8. \stemDown as16 \stemDown f4 ) | % 111
    \stemDown as8. ( \stemDown des16 \stemDown es8. \stemDown des16
    \stemDown c4 \stemDown bes8 \stemDown beses8 ) | % 112
    \stemDown as2 ^ "Tutti [con sord.]" _\< \stemDown f8. ( \stemDown
    ges16 \stemDown as4 ) _\! _\f \pageBreak | % 113
    des,1 _\> | % 114
    R1*5 \pageBreak | % 119
    R1*4 | % 123
    r8 _\! \stemUp des,8 ( _\mf \stemUp as'8 _\> \stemUp des8 \stemDown
    f8 \stemDown as8 \stemDown des8 \stemDown f8 ) | % 124
    as1 _\! _\p | % 125
    \clef "treble" des1 ~ _\ppp | % 126
    \stemDown des4 r4 r2 | % 127
    R1 \bar "|."
    }

PartPTwoFourVoiceTwo =  \relative as, {
    \clef "bass" \time 4/4 \key des \major s4*21 \stemDown as2. s1
    \pageBreak s1 | % 9
    \stemDown des,2 ( \stemDown f2 ) | \barNumberCheck #10
    \stemDown ges4 ( \stemDown as4 \stemDown des,2 ) s1*3 \pageBreak
    s2*9 s1. _\p \pageBreak s1*7 \pageBreak s1*5 \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s4*5 \stemDown as'2. ~ \pageBreak s1 | % 38
    \stemDown des4 ( \stemDown c4 ) \stemDown bes4 ( \stemDown as4 ) | % 39
    \stemDown ges2 ( \stemDown des2 ) s1*2 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key b \major \once \override NoteHead.style = ##f \stemNeutral cis'2
    s2*11 | % 52
    \clef "tenor" s1 \pageBreak s2. \clef "bass" s4*13 \pageBreak | % 57
     \once \override NoteHead.style = ##f \stemNeutral cis2 s2*5 |
    \barNumberCheck #60
     \once \override NoteHead.style = ##f \stemNeutral cis2 s2
    \pageBreak s1 | % 62
     \once \override NoteHead.style = ##f \stemNeutral cis2 s1.
    \pageBreak | % 64
     \once \override NoteHead.style = ##f \stemNeutral cis2 s2*5 | % 67
     \once \override NoteHead.style = ##f \stemNeutral cis2 s2
    \pageBreak s1*2 | \barNumberCheck #70
     \once \override NoteHead.style = ##f \stemNeutral cis2 s1.
    \pageBreak s1*7 \pageBreak s1*5 \pageBreak s1*6 \pageBreak s1*2
    \pageBreak s1*2 \pageBreak s1*2 \pageBreak | % 96
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown cis16 \stemDown cis16 \stemDown cis16 \stemDown cis16
        \stemDown cis16 \stemDown cis16 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown cis4. :64 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown cis4. :64 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemDown cis4. :64 }
    | % 97
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown cis4. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown cis4. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown cis4. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown cis4. :64 }
    | % 98
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown cis4. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown cis4. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown cis4. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemDown cis4. :64 }
    | % 99
    \stemDown cis4 \stemDown cis8. ( \stemDown e16 \stemDown e4 )
    \stemDown cis8. ( \stemDown e16 \pageBreak | \barNumberCheck #100
    \stemDown cis4 ) \stemDown a8. ( \stemDown cis16 \stemDown cis4 )
    \stemDown a8. ( \stemDown cis16 s1*2 | % 103
    \stemDown des2 \stemDown f,2 | % 104
    \stemDown ges4 \stemDown as4 \stemDown des2 ) s1*2 \pageBreak s1*6
    \pageBreak s2 s2*5 _\p | % 116
     \once \override NoteHead.style = ##f \stemNeutral es2 s2*5
    \pageBreak s4*23 s4 ^ "*)" | % 125
    \clef "treble" s1*3 \bar "|."
    }

PartPTwoFiveVoiceOne =  \relative des' {
    \clef "bass" \time 4/4 \key des \major \transposition c | % 1
    R1*3 | % 4
    R1 ^ "con sord." | % 5
    \stemDown des4. ( ~ _\ppp \stemDown des8 -- \stemDown des2 ~ | % 6
    \stemDown des8 ) ^- \stemDown as8 ^- \stemDown des,2. ~ | % 7
    \stemDown des4 r4 r2 \pageBreak | % 8
    R1*6 \pageBreak | % 14
    R1 | % 15
    as'1 ~ _\ppp | % 16
    as1 | % 17
    \stemDown des,4 ^\markup{ \italic {molto cresc.} } _\< \stemUp c4
    \stemUp bes4 \stemUp as4 ~ | % 18
    \stemUp as2 _\! _\f _\markup{ \italic {dim.} } _\> \stemDown des2
    _\p | % 19
    R1 \pageBreak | \barNumberCheck #20
    R1*6 | % 26
    r2 _\! \stemDown des'2 ~ _\ppp \pageBreak | % 27
    des1 ~ | % 28
    des1 | % 29
    des1 ~ | \barNumberCheck #30
    des1 | % 31
    des1 ~ \pageBreak | % 32
    des1 | % 33
    des1 ~ _\< | % 34
    \time 2/4  \stemDown des2 _\! | % 35
    \time 4/4  des1 _\> | % 36
    des,1 ~ _\ppp \pageBreak | % 37
    des1 | % 38
    \stemDown des4 ( _\< \stemUp c4 ) \stemUp bes4 ( \stemUp as4 ) _\!
    _\f | % 39
    \stemUp ges2 ( _\fz _\> \stemDown des'2 ) _\! | \barNumberCheck #40
    R1*2 \pageBreak | % 42
    R1 | % 43
    as'1 ~ _\ppp | % 44
    as1 ~ | % 45
    \stemDown as4 r4 r2 \bar "||"
    \pageBreak | % 46
    \key b \major R1*7 \pageBreak | % 53
    R1 | % 54
    \stemDown cis,8 _\pp ^ "pizz." \stemDown e8 \stemDown gis8 \stemDown
    cis,8 \stemDown fis8 \stemDown a8 \stemDown gis8 \stemDown cis,8 | % 55
    \stemDown fis8 \stemDown a8 \stemDown d8 \stemDown e8 \stemDown fis8
    \stemDown d8 \stemDown cis8 \stemDown bis8 | % 56
    \stemDown cis8 \stemDown dis8 \stemDown e8 \stemDown ais,8 \stemDown
    bis8 \stemDown gis8 \stemDown cis8 \stemDown a8 \pageBreak | % 57
    \stemDown fis8 \stemDown gis8 \stemDown a8 \stemDown fis8 \stemDown
    dis8 \stemDown fis8 \stemDown gis8 \stemDown gis,8 | % 58
    \stemDown cis8 _\pp \stemDown e8 \stemDown gis8 \stemDown cis8
    \stemDown b8 \stemDown a8 \stemDown gis8 \stemDown e8 | % 59
    \stemDown cis8 \stemDown gis'8 \stemDown e8 \stemDown cis'8
    \stemDown a8 \stemDown cis8 \stemDown e8 \stemDown cis8 |
    \barNumberCheck #60
    \stemDown b8 _\mf \stemDown fis'8 \stemDown dis8 \stemDown b8
    \stemDown e8 _\> \stemDown b8 \stemDown gis8 \stemDown e8 \pageBreak
    | % 61
    \stemDown d'8 _\! _\p \stemDown a8 \stemDown fis8 \stemDown d8
    \stemUp a8 \stemUp b8 \stemUp cis8 \stemUp e8 | % 62
    \stemDown fis8 _\pp \stemDown gis8 \stemDown a8 \stemDown fis8
    \stemDown dis8 \stemDown fis8 \stemDown gis8 \stemDown gis,8 | % 63
    \stemDown cis8 \stemDown cis'8 \stemDown b8 \stemDown a8 \stemDown
    gis8 \stemDown e8 \stemDown cis8 \stemDown gis8 \pageBreak | % 64
    \stemUp cis8 r8 r4 r2 | % 65
    R1*3 \pageBreak | % 68
    R1*4 \pageBreak | % 72
    R1*5 | % 77
    gis1 ( _\ppp ^ "arco" | % 78
    \stemUp cis4 ) r4 r2 \pageBreak | % 79
    R1*5 \pageBreak | % 84
    R1*3 | % 87
    \stemUp cis2 _\pp \stemDown e2 | % 88
    \stemUp cis2 \stemDown e2 | % 89
    cis1 ~ \pageBreak | \barNumberCheck #90
    \stemUp cis8 r8 r4 r2 | % 91
    R1 \pageBreak | % 92
    R1*2 \pageBreak | % 94
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown eis16 _\mf \stemDown fis16 \stemDown gis16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown eis16 \stemDown dis16 \stemDown cis16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown dis16 \stemDown eis16 \stemDown fis16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown eis16 \stemDown dis16 _\< \stemDown cis16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown dis16 \stemDown eis16 \stemDown fis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown eis16 \stemDown gis16 r16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown fis16 \stemDown eis16 \stemDown dis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown eis16 \stemDown cis16 r16 }
    _\! | % 95
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis16 _\f \stemDown eis16 \stemDown dis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown eis16 \stemDown cis16 r16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis16 \stemDown eis16 \stemDown dis16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown eis16 \stemDown cis16 _\< r16 }
    \once \omit TupletBracket
    \times 2/3  {
        \stemDown fis16 \stemDown eis16 \stemDown dis16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown fis16 \stemDown eis16 \stemDown dis16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown fis16 \stemDown eis16 \stemDown dis16 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 2/3  {
        \stemDown fis16 \stemDown eis16 \stemDown dis16 }
    \pageBreak | % 96
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp cis16 _\! ^\ff \stemUp cis16 \stemUp cis16 \stemUp cis16
        \stemUp cis16 \stemUp cis16 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp cis4. :64 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp cis4. :64 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp cis4. :64 }
    | % 97
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp cis4. :64 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp cis4. :64 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp cis4. :64 }
    \once \omit TupletBracket
    \times 4/6  {
        \stemUp cis4. :64 }
    | % 98
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp cis4. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp cis4. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp cis4. :64 }
    \once \omit TupletBracket
    \once \omit TupletNumber
    \times 4/6  {
        \stemUp cis4. :64 }
    | % 99
    \stemUp cis2 ( _\mp \stemUp e,2 \pageBreak | \barNumberCheck #100
    a1 ) ( _\p _\> | % 101
    \stemUp cis4 ) _\! _\pp r4 r2 | % 102
    R1*3 | % 105
    des'1 ~ ^ "2 Contrabassi" _\pp | % 106
    des1 ~ \pageBreak | % 107
    \stemDown des2. r4 ^\fermata | % 108
    \stemDown des2 r4 ^\fermata \stemDown des4 ~ | % 109
    \stemDown des2 ~ \stemDown des4 r4 ^\fermata | \barNumberCheck #110
    R1*2 | % 112
    \stemDown des4 ( _\pp ^\markup{ \italic {molto cresc.} } _\<
    \stemDown c4 ) \stemDown bes4 ( \stemDown as4 ) _\! _\f \pageBreak | % 113
    \stemDown ges2 ( _\> \stemDown des2 ) _\! _\p | % 114
    R1*5 \pageBreak | % 119
    R1*3 | % 122
    R1*4 _ "*) loco" | % 126
    r2 \stemUp <as' f'>4 ^ "div." _\pp r4 | % 127
    \stemUp <as f'>2 ~ ~ \stemUp <as f'>8 r8 r4 \bar "|."
    }

PartPTwoFiveVoiceTwo =  \relative es' {
    \clef "bass" \time 4/4 \key des \major \transposition c s1*7
    \pageBreak | % 8
     \once \override NoteHead.style = ##f \stemNeutral es2 s2*11
    \pageBreak s1*6 \pageBreak s1*7 \pageBreak s1*5 \pageBreak s1*2 | % 34
    \time 2/4  s2 | % 35
    \time 4/4  s2 s1. _\! _\pp \pageBreak s1*5 \pageBreak s1*4 \bar "||"
    \pageBreak | % 46
    \key b \major \once \override NoteHead.style = ##f \stemNeutral cis,2
    s2*9 | % 51
     \once \override NoteHead.style = ##f \stemNeutral cis2 s1.
    \pageBreak s1*4 \pageBreak s1*4 \pageBreak s1*3 \pageBreak s1*3 | % 67
     \once \override NoteHead.style = ##f \stemNeutral cis2 s2
    \pageBreak s1*2 | \barNumberCheck #70
     \once \override NoteHead.style = ##f \stemNeutral cis2 s1.
    \pageBreak s1*7 \pageBreak s1 | \barNumberCheck #80
     \once \override NoteHead.style = ##f \stemNeutral cis2 s2*7
    \pageBreak s1*6 \pageBreak s1 | % 91
     \once \override NoteHead.style = ##f \stemNeutral e2 s2 \pageBreak
    s1*2 \pageBreak s1*2 \pageBreak s1*4 \pageBreak s1*7 \pageBreak s1*6
    \pageBreak s1*3 | % 116
     \once \override NoteHead.style = ##f \stemNeutral es2 s2*5
    \pageBreak s2*15 \stemDown <des des'>4 s4 | % 127
    \stemDown <des des'>2 ~ ~ \stemDown <des des'>8 s4. \bar "|."
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
                        \context Voice = "PartPThreeVoiceTwo" {  \voiceTwo \PartPThreeVoiceTwo }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Oboe 2"
                    \set Staff.shortInstrumentName = "Ob. 2"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPFourVoiceOne" {  \voiceOne \PartPFourVoiceOne }
                        \context Voice = "PartPFourVoiceTwo" {  \voiceTwo \PartPFourVoiceTwo }
                        >>
                    >>
                
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Corno inglese"
                \set Staff.shortInstrumentName = "Cor. ingl."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPFiveVoiceOne" {  \voiceOne \PartPFiveVoiceOne }
                    \context Voice = "PartPFiveVoiceTwo" {  \voiceTwo \PartPFiveVoiceTwo }
                    \context Voice = "PartPFiveVoiceThree" {  \voiceThree \PartPFiveVoiceThree }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Clarinet1"
                \set Staff.shortInstrumentName = "Cl. I. II."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPSixVoiceOne" {  \voiceOne \PartPSixVoiceOne }
                    \context Voice = "PartPSixVoiceTwo" {  \voiceTwo \PartPSixVoiceTwo }
                    \context Voice = "PartPSixVoiceThree" {  \voiceThree \PartPSixVoiceThree }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Clarinet"
                \set Staff.shortInstrumentName = "Cl."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPSevenVoiceOne" {  \voiceOne \PartPSevenVoiceOne }
                    \context Voice = "PartPSevenVoiceTwo" {  \voiceTwo \PartPSevenVoiceTwo }
                    \context Voice = "PartPSevenVoiceThree" {  \voiceThree \PartPSevenVoiceThree }
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
                        \context Voice = "PartPEightVoiceOne" {  \voiceOne \PartPEightVoiceOne }
                        \context Voice = "PartPEightVoiceTwo" {  \voiceTwo \PartPEightVoiceTwo }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Bassoon 2"
                    \set Staff.shortInstrumentName = "Bsn. 2"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPNineVoiceOne" {  \PartPNineVoiceOne }
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
                    \new StaffGroup \with { }
                    
                    <<
                        \new Staff
                        <<
                            \set Staff.instrumentName = \markup { \center-column { \line {"Corni"} \line {"I. II. E"} } }
                            \set Staff.shortInstrumentName = \markup { \center-column { \line {"Cor."} \line {"I. II."} } }
                            
                            \context Staff << 
                                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                                \context Voice = "PartPOneZeroVoiceOne" {  \voiceOne \PartPOneZeroVoiceOne }
                                \context Voice = "PartPOneZeroVoiceTwo" {  \voiceTwo \PartPOneZeroVoiceTwo }
                                \context Voice = "PartPOneZeroVoiceThree" {  \voiceThree \PartPOneZeroVoiceThree }
                                >>
                            >>
                        \new Staff
                        <<
                            \set Staff.instrumentName = "Horn in E 2"
                            \set Staff.shortInstrumentName = "Hn. in E 2"
                            
                            \context Staff << 
                                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                                \context Voice = "PartPOneOneVoiceOne" {  \PartPOneOneVoiceOne }
                                >>
                            >>
                        
                        >>
                    
                    >>
                
                >>
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = \markup { \center-column { \line {"Corni"} \line {"III. E, IV. C"} } }
                    \set Staff.shortInstrumentName = \markup { \center-column { \line {"Cor."} \line {"III. IV."} } }
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneTwoVoiceOne" {  \voiceOne \PartPOneTwoVoiceOne }
                        \context Voice = "PartPOneTwoVoiceTwo" {  \voiceTwo \PartPOneTwoVoiceTwo }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Horn in C 2"
                    \set Staff.shortInstrumentName = "Hn. in C 2"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneThreeVoiceOne" {  \voiceOne \PartPOneThreeVoiceOne }
                        \context Voice = "PartPOneThreeVoiceTwo" {  \voiceTwo \PartPOneThreeVoiceTwo }
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
                        \context Voice = "PartPOneFourVoiceOne" {  \voiceOne \PartPOneFourVoiceOne }
                        \context Voice = "PartPOneFourVoiceTwo" {  \voiceTwo \PartPOneFourVoiceTwo }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Trumpet in E 2"
                    \set Staff.shortInstrumentName = "Tpt. in E 2"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneFiveVoiceOne" {  \PartPOneFiveVoiceOne }
                        >>
                    >>
                
                >>
            \new StaffGroup \with { }
            
            <<
                \new StaffGroup \with { systemStartDelimiter =
                    #'SystemStartBrace }
                
                <<
                    \new StaffGroup \with { }
                    
                    <<
                        \new Staff
                        <<
                            \set Staff.instrumentName = "Trombone1"
                            \set Staff.shortInstrumentName = \markup { \center-column { \line {"Trbni."} \line {"I. II."} } }
                            
                            \context Staff << 
                                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                                \context Voice = "PartPOneSixVoiceOne" {  \voiceOne \PartPOneSixVoiceOne }
                                \context Voice = "PartPOneSixVoiceTwo" {  \voiceTwo \PartPOneSixVoiceTwo }
                                >>
                            >>
                        \new Staff
                        <<
                            \set Staff.instrumentName = "Trombone 3"
                            \set Staff.shortInstrumentName = "Tbn. 3"
                            
                            \context Staff << 
                                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                                \context Voice = "PartPOneSevenVoiceOne" {  \PartPOneSevenVoiceOne }
                                >>
                            >>
                        \new Staff
                        <<
                            \set Staff.instrumentName = \markup { \center-column { \line {"Trombone"} \line {"2"} } }
                            \set Staff.shortInstrumentName = \markup { \center-column { \line {"Trbn."} \line {"III."} } }
                            
                            \context Staff << 
                                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                                \context Voice = "PartPOneEightVoiceOne" {  \voiceOne \PartPOneEightVoiceOne }
                                \context Voice = "PartPOneEightVoiceTwo" {  \voiceTwo \PartPOneEightVoiceTwo }
                                >>
                            >>
                        
                        >>
                    
                    >>
                
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Tuba"
                \set Staff.shortInstrumentName = "Tb."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneNineVoiceOne" {  \voiceOne \PartPOneNineVoiceOne }
                    \context Voice = "PartPOneNineVoiceTwo" {  \voiceTwo \PartPOneNineVoiceTwo }
                    >>
                >>
            
            >>
        \new Staff
        <<
            \set Staff.instrumentName = "Timpani"
            \set Staff.shortInstrumentName = "Timp. Des"
            
            \context Staff << 
                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                \context Voice = "PartPTwoZeroVoiceOne" {  \voiceOne \PartPTwoZeroVoiceOne }
                \context Voice = "PartPTwoZeroVoiceTwo" {  \voiceTwo \PartPTwoZeroVoiceTwo }
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
                    \context Voice = "PartPTwoOneVoiceOne" {  \voiceOne \PartPTwoOneVoiceOne }
                    \context Voice = "PartPTwoOneVoiceTwo" {  \voiceTwo \PartPTwoOneVoiceTwo }
                    \context Voice = "PartPTwoOneVoiceThree" {  \voiceThree \PartPTwoOneVoiceThree }
                    >>
                >>
            \new Staff
            <<
                \set Staff.instrumentName = \markup { \center-column { \line {"Violini"} \line {"II."} } }
                \set Staff.shortInstrumentName = "Viol. II."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPTwoTwoVoiceOne" {  \voiceOne \PartPTwoTwoVoiceOne }
                    \context Voice = "PartPTwoTwoVoiceTwo" {  \voiceTwo \PartPTwoTwoVoiceTwo }
                    \context Voice = "PartPTwoTwoVoiceThree" {  \voiceThree \PartPTwoTwoVoiceThree }
                    >>
                >>
            
            >>
        \new Staff
        <<
            \set Staff.instrumentName = "Violas"
            \set Staff.shortInstrumentName = "Vle"
            
            \context Staff << 
                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                \context Voice = "PartPTwoThreeVoiceOne" {  \voiceOne \PartPTwoThreeVoiceOne }
                \context Voice = "PartPTwoThreeVoiceTwo" {  \voiceTwo \PartPTwoThreeVoiceTwo }
                >>
            >>
        \new Staff
        <<
            \set Staff.instrumentName = "Violoncellos"
            \set Staff.shortInstrumentName = "Vcl."
            
            \context Staff << 
                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                \context Voice = "PartPTwoFourVoiceOne" {  \voiceOne \PartPTwoFourVoiceOne }
                \context Voice = "PartPTwoFourVoiceTwo" {  \voiceTwo \PartPTwoFourVoiceTwo }
                >>
            >>
        \new Staff
        <<
            \set Staff.instrumentName = "Contrabasses"
            \set Staff.shortInstrumentName = "Cb."
            
            \context Staff << 
                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                \context Voice = "PartPTwoFiveVoiceOne" {  \voiceOne \PartPTwoFiveVoiceOne }
                \context Voice = "PartPTwoFiveVoiceTwo" {  \voiceTwo \PartPTwoFiveVoiceTwo }
                >>
            >>
        
        >>
    \layout {}
    % To create MIDI output, uncomment the following line:
    %  \midi {\tempo 4 = 52 }
    }

