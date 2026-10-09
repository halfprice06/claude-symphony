\version "2.24.3"
% automatically converted by musicxml2ly from ../xml/Mozart_Sym41_mvt3.musicxml
\pointAndClickOff

\header {
    title =  "Symphony No. 41 in C Major (“Jupiter”)"
    opus =  "K. 551"
    composer =  "Wolfgang Amadeus Mozart"
    encodingsoftware =  "MuseScore 4.1.0"
    encodingdate =  "2023-07-21"
    source =  "https://musescore.com/score/4861738"
    copyright =  "This OpenScore Edition is available for dedication."
    poet =  "Symphony No. 41 – “Jupiter Symphony” – K. 551"
    subtitle =  "III – Menuetto"
    }

#(set-global-staff-size 14.971428571428573)
\paper {
    
    paper-width = 21.01\cm
    paper-height = 29.69\cm
    top-margin = 1.0\cm
    bottom-margin = 2.0\cm
    left-margin = 1.0\cm
    right-margin = 1.0\cm
    indent = 1.6161538461538465\cm
    short-indent = 0.7542051282051283\cm
    }
\layout {
    \context { \Score
        skipBars = ##t
        }
    }
PartPOneVoiceOne =  \relative d''' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key c \major | % 1
        \mark \markup { \musicglyph "scripts.segno" } R2.*6 \pageBreak
        ^\markup{ \bold {Allegretto} } | % 7
        R2.*2 | % 9
        \stemDown d2. ~ _\f | \barNumberCheck #10
        \stemDown d2. ~ | % 11
        \stemDown d2. ~ | % 12
        \stemDown d2. \pageBreak | % 13
        \stemDown d4 \stemDown d4 \stemDown d4 | % 14
        \stemDown c4 \stemDown c4 \stemDown c4 | % 15
        \stemDown a4 \stemDown a4 \stemDown a4 | % 16
        \stemDown g4 r4 r4 }
    \repeat volta 2 {
        | % 17
        R2.*4 \pageBreak | % 21
        r4 r4 \stemDown g4 ( _\p | % 22
        \stemDown a2 \stemDown b4 | % 23
        \stemDown c2 \stemDown es4 | % 24
        \stemDown d4 ) r4 r4 | % 25
        R2. | % 26
        r4 \stemDown g4 _\f \stemDown g4 | % 27
        \stemDown g2 \stemDown e8 \stemDown c8 | % 28
        \stemDown g2 ( \stemDown fis4 \pageBreak | % 29
        \stemDown f4 \stemDown e4 \stemDown d4 | \barNumberCheck #30
        \stemDown c2 ) \stemDown d8 ( \trill \stemDown c16 \stemDown d16
        | % 31
        \stemDown e4 ) \stemDown f4 -. \stemDown g4 -. | % 32
        \stemDown a2 ( \stemDown gis4 | % 33
        \stemDown g4 \stemDown fis4 \stemDown e4 | % 34
        \stemDown d4 ) \stemDown fis4 \stemDown g8 ( \trill \stemDown
        fis16 \stemDown g16 | % 35
        \stemDown a4 ) \stemDown b4 -. \stemDown c4 -. \pageBreak | % 36
        \stemDown d2 ( \stemDown cis4 | % 37
        \stemDown c4 \stemDown b4 \stemDown a4 | % 38
        \stemDown g2 ) \stemDown a8 ( \trill \stemDown g16 \stemDown a16
        | % 39
        \stemDown b4 ) \stemDown c4 -. \stemDown d4 -. | \barNumberCheck
        #40
        \stemDown e4 -. \stemDown b4 ( \stemDown c4 ) | % 41
        \stemDown a4 -. \stemDown e4 ( \stemDown f4 ) | % 42
        \stemDown g8 \stemDown a8 \stemDown g8 \stemDown e8 \stemDown f8
        \stemDown d8 | % 43
        \stemDown c4 r4 r4 \pageBreak | % 44
        R2.*4 | % 48
        \stemDown d'2 ( _\p \stemDown cis4 | % 49
        \stemDown c4 \stemDown b4 \stemDown a4 | \barNumberCheck #50
        \stemDown g4 ) r4 r4 | % 51
        R2. | % 52
        \stemDown g'2 ( _\f \stemDown fis4 \pageBreak | % 53
        \stemDown f8 ) r8 \stemDown d8 -. r8 \stemDown b8 -. r8 | % 54
        \stemDown g'2 ( \stemDown fis4 | % 55
        \stemDown f8 ) r8 \stemDown d8 -. r8 \stemDown b8 -. r8 | % 56
        \stemDown c4 \stemDown c4 \stemDown c4 | % 57
        \stemDown f4 \stemDown f4 \stemDown f4 | % 58
        \stemDown d4 \stemDown d4 \stemDown d4 | % 59
        \stemDown c4 r4 r4 }
    \pageBreak \repeat volta 2 {
        \stemDown b,2. ( ^ "To Coda" ^\markup{ \bold {Trio} } _\p
        \stemDown c4 ) r4 r4 R2.*2 \stemDown b2. ( \stemDown c4 ) r4 r4
        R2.*2 }
    \pageBreak \repeat volta 2 {
        \stemDown gis'2. _\f \stemDown a2. \stemDown c2. \stemDown b2.
        \stemDown d2. \stemDown c2. \pageBreak \stemDown fis2. \stemDown
        e4 r4 r4 R2.*4 \stemDown b,2. ( _\p \pageBreak \stemDown c4 ) r4
        r4 R2.*2 \stemDown b'2. ( \stemDown c4 ) r4 r4 r8 \stemDown g8 (
        \stemDown b8 \stemDown d8 \stemDown f8 \stemDown d8 ) \stemDown
        c4 -. \stemDown e4 ( \stemDown c4 ) }
    ^ "Menuetto D.C." }

PartPOneVoiceTwo =  \relative c'' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key c \major | % 1
         \once \override NoteHead.style = ##f \stemDown c2. s4*15
        \pageBreak s2*9 \pageBreak s1*3 }
    \repeat volta 2 {
        s1*3 \pageBreak s1*6 \pageBreak s4*21 \pageBreak s1*6 \pageBreak
        s4*27 \pageBreak s4*21 }
    \pageBreak \repeat volta 2 {
        s1*6 }
    \pageBreak \repeat volta 2 {
        s2*9 \pageBreak s4*21 \pageBreak s4*21 }
    }

PartPTwoVoiceOne =  \relative d'' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key c \major | % 1
        R2.*6 \pageBreak | % 7
        R2.*2 | % 9
        \stemDown d2. ~ _\f | \barNumberCheck #10
        \stemDown d2. ~ | % 11
        \stemDown d2. ~ | % 12
        \stemDown d2. \pageBreak | % 13
        \stemDown g4 \stemDown g4 \stemDown g4 | % 14
        \stemDown a4 \stemDown a4 \stemDown a4 | % 15
        \stemDown fis4 \stemDown fis4 \stemDown fis4 | % 16
        \stemDown g4 r4 r4 }
    \repeat volta 2 {
        | % 17
        \stemDown d2 ( _\p \stemDown cis4 | % 18
        \stemDown c2 \stemDown b4 ) | % 19
        \stemDown f'2 ( \stemDown e4 | \barNumberCheck #20
        \stemDown es2 \stemDown d4 ) \pageBreak | % 21
        \stemDown a'2 ( \stemDown g4 | % 22
        \stemDown fis2 \stemDown f4 | % 23
        \stemDown e2 \stemDown fis4 | % 24
        \stemDown g4 ) r4 r4 | % 25
        R2. | % 26
        r4 \stemDown g4 _\f \stemDown g4 | % 27
        \stemDown g2 \stemDown e8 ( \stemDown c8 ) | % 28
        \stemDown g'2 ( \stemDown fis4 \pageBreak | % 29
        \stemDown f4 \stemDown e4 \stemDown d4 | \barNumberCheck #30
        \stemDown c2 ) \stemDown d8 ( \trill \stemDown c16 \stemDown d16
        | % 31
        \stemDown e4 ) \stemDown f4 -. \stemDown g4 -. | % 32
        \stemDown a2 ( \stemDown gis4 | % 33
        \stemDown g4 \stemDown fis4 \stemDown e4 | % 34
        \stemDown d4 ) \stemDown fis4 \stemDown g8 ( \trill \stemDown
        fis16 \stemDown g16 | % 35
        \stemDown a4 ) \stemDown b4 -. \stemDown c4 -. \pageBreak | % 36
        \stemDown d2 ( \stemDown cis4 | % 37
        \stemDown c4 \stemDown b4 \stemDown a4 | % 38
        \stemDown g2 ) \stemDown a8 ( \trill \stemDown g16 \stemDown a16
        | % 39
        \stemDown b4 ) \stemDown c4 -. \stemDown b4 -. | \barNumberCheck
        #40
        \stemDown c4 -. \stemDown f,4 ( \stemDown e4 ) | % 41
        r4 \stemDown bes4 ( \stemUp a4 ) | % 42
        \stemDown g'8 \stemDown a8 \stemDown g8 \stemDown e8 \stemDown f8
        \stemDown d8 | % 43
        \stemDown c8 ( \stemDown b8 ) \stemDown c8 -. \stemDown d8 -.
        \stemDown e8 -. \stemDown f8 -. \pageBreak | % 44
        \stemDown g4 r4 r4 | % 45
        R2. | % 46
        \stemDown c2 ( _\p \stemDown b4 | % 47
        \stemDown bes4 \stemDown a4 \stemDown as4 ) ~ | % 48
        \stemDown as4 ( \stemDown g2 ) | % 49
        \stemDown fis4 ( \stemDown f4 \stemDown d4 ) | \barNumberCheck
        #50
        \stemDown g4 ( \stemDown f4 \stemDown e4 ) | % 51
        \stemDown d4 ( \stemDown f4 ) \stemDown b,4 -. | % 52
        \stemDown g'2. ~ _\f \pageBreak | % 53
        \stemDown g2. ~ | % 54
        \stemDown g2. ~ | % 55
        \stemDown g2. | % 56
        \stemDown g4 \stemDown g4 \stemDown g4 | % 57
        \stemDown a4 \stemDown a4 \stemDown a4 | % 58
        \stemDown b4 \stemDown b4 \stemDown b4 | % 59
        \stemDown c4 r4 r4 }
    \pageBreak \repeat volta 2 {
        R2. r4 r4 \stemDown a8 _\p \stemDown g8 \stemDown fis8 (
        \stemDown g8 ) \stemDown f8 \stemDown d8 \stemDown e8 \stemDown
        c8 \stemDown e8 ( \stemDown d8 ) \stemDown c8 \stemDown b8
        \stemDown a8 \stemDown g8 R2. r4 r4 \stemDown a'8 \stemDown g8
        \stemDown fis8 ( \stemDown g8 ) \stemDown f8 \stemDown d8
        \stemDown b8 \stemDown d8 \stemDown c4 -. \stemDown e4 (
        \stemDown c4 ) }
    \pageBreak \repeat volta 2 {
        \stemDown d2. _\f \stemDown e2. \stemDown fis2. \stemDown gis2.
        \stemDown b2. \stemDown a2. \pageBreak \stemDown c2. \stemDown b4
        r4 r4 R2.*5 \pageBreak r4 r4 \stemDown a8 _\p \stemDown g8
        \stemDown fis8 ( \stemDown g8 ) \stemDown f8 \stemDown d8
        \stemDown e8 \stemDown c8 \stemDown e8 ( \stemDown d8 )
        \stemDown c8 \stemDown b8 \stemDown a8 \stemDown g8 \stemDown b2.
        ( \stemDown c4 ) r4 \stemDown a'8 \stemDown g8 \stemDown fis8 (
        \stemDown g8 ) \stemDown f8 \stemDown d8 \stemDown b8 \stemDown
        d8 \stemDown c4 -. \stemDown e4 ( \stemDown c4 ) }
    }

PartPTwoVoiceTwo =  \relative c'' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key c \major | % 1
         \once \override NoteHead.style = ##f \stemDown c2. s4*15
        \pageBreak s2*9 \pageBreak s1*3 }
    \repeat volta 2 {
        s1*3 \pageBreak s1*6 \pageBreak s4*21 \pageBreak s1*6 \pageBreak
        s4*27 \pageBreak s4*21 }
    \pageBreak \repeat volta 2 {
        s1*6 }
    \pageBreak \repeat volta 2 {
        s2*9 \pageBreak s4*21 \pageBreak s4*21 }
    }

PartPThreeVoiceOne =  \relative d' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key c \major | % 1
        R2.*6 \pageBreak | % 7
        R2.*2 | % 9
        \stemUp d2. ~ _\f | \barNumberCheck #10
        \stemUp d2. ~ | % 11
        \stemUp d2. ~ | % 12
        \stemUp d2. \pageBreak | % 13
        \stemDown d'4 \stemDown d4 \stemDown d4 | % 14
        \stemDown e4 \stemDown e4 \stemDown e4 | % 15
        \stemDown c4 \stemDown c4 \stemDown c4 | % 16
        \stemDown b4 r4 r4 }
    \repeat volta 2 {
        | % 17
        \stemDown b2 ( _\p \stemUp ais4 | % 18
        \stemUp a4 \stemUp fis4 \stemUp g4 ) | % 19
        \stemDown d'2 ( \stemDown c4 ~ | \barNumberCheck #20
        \stemDown c4 \stemUp a4 \stemDown b4 ) \pageBreak | % 21
        \stemDown f'2 ( \stemDown e4 ) | % 22
        \stemDown es4 ( \stemDown d2 ) ~ | % 23
        \stemDown d4 ( \stemDown c2 ) | % 24
        \stemDown b4 r4 r4 | % 25
        R2. | % 26
        r4 \stemDown g'4 _\f \stemDown g4 | % 27
        \stemDown g2 \stemDown e8 ( \stemDown c8 ) | % 28
        \stemUp g4 \stemDown g'4 ( \stemDown fis4 \pageBreak | % 29
        \stemDown f4 \stemDown e4 \stemDown d4 | \barNumberCheck #30
        \stemDown c2 ) \stemDown d8 ( \trill \stemDown c16 \stemDown d16
        | % 31
        \stemDown e4 ) \stemDown f4 -. \stemDown g4 -. | % 32
        \stemDown a2 ( \stemDown gis4 | % 33
        \stemDown g4 \stemDown fis4 \stemDown e4 | % 34
        \stemDown d4 ) \stemDown fis4 \stemDown g8 ( \trill \stemDown
        fis16 \stemDown g16 | % 35
        \stemDown a4 ) \stemDown b4 -. \stemDown c4 -. \pageBreak | % 36
        \stemDown d2 ( \stemDown cis4 | % 37
        \stemDown c4 \stemDown b4 \stemDown a4 | % 38
        \stemDown g2 ) \stemDown a8 ( \trill \stemDown g16 \stemDown a16
        | % 39
        \stemDown b4 ) \stemDown c4 -. \stemDown f,4 -. |
        \barNumberCheck #40
        \stemDown g4 -. \stemDown d4 ( \stemDown c4 ) | % 41
        r4 \stemUp g4 ( \stemUp f4 ) | % 42
        \stemDown e'8 \stemDown f8 \stemDown e8 \stemDown c8 \stemDown d8
        \stemDown b8 | % 43
        \stemDown c4 r4 r4 \pageBreak | % 44
        \stemDown g'2 ( _\p \stemDown fis4 | % 45
        \stemDown f4 \stemDown e4 \stemDown es4 ) | % 46
        \stemDown as4 ( \stemDown g2 ~ | % 47
        \stemDown g4 \stemDown fis4 \stemDown es4 ) | % 48
        \stemDown d2 \stemDown e4 | % 49
        \stemDown d2 \stemDown b4 | \barNumberCheck #50
        \stemDown c4 ( \stemDown b4 \stemDown c4 ) | % 51
        \stemUp a4 r4 \stemUp f4 | % 52
        \stemUp g2. ~ _\f \pageBreak | % 53
        \stemUp g2. ~ | % 54
        \stemUp g2. ~ | % 55
        \stemUp g2. | % 56
        \stemDown e'4 \stemDown e4 \stemDown e4 | % 57
        \stemDown d4 \stemDown d4 \stemDown d4 | % 58
        \stemDown f4 \stemDown f4 \stemDown f4 | % 59
        \stemDown e4 r4 r4 }
    \pageBreak \repeat volta 2 {
        R2.*8 }
    \pageBreak \repeat volta 2 {
        \stemDown b2. _\f \stemDown c2. \stemDown dis2. \stemDown e2.
        \stemDown f2. \stemDown e2. \pageBreak \stemDown a2. \stemDown
        gis4 r4 r4 R2.*5 \pageBreak R2.*7 }
    }

PartPThreeVoiceTwo =  \relative c'' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key c \major | % 1
         \once \override NoteHead.style = ##f \stemDown c2. s4*15
        \pageBreak s2*9 \pageBreak s1*3 }
    \repeat volta 2 {
        s1*3 \pageBreak s1*6 \pageBreak s4*21 \pageBreak s1*6 \pageBreak
        s4*27 \pageBreak s4*21 }
    \pageBreak \repeat volta 2 {
        s1*6 }
    \pageBreak \repeat volta 2 {
        s2*9 \pageBreak s4*21 \pageBreak s4*21 }
    }

PartPFourVoiceOne =  \relative b {
    \repeat volta 2 {
        \clef "bass" \time 3/4 \key c \major | % 1
        R2.*6 \pageBreak | % 7
        R2.*2 | % 9
        \stemDown b2 ( _\f \stemDown bes4 | \barNumberCheck #10
        \stemDown a8 ) r8 \stemDown c8 -. r8 \stemDown a8 -. r8 | % 11
        \stemDown b2 ( \stemDown bes4 | % 12
        \stemDown a8 ) r8 \stemDown c8 -. r8 \stemDown a8 -. r8
        \pageBreak | % 13
        \stemDown b4 \stemUp b,4 \stemUp b4 | % 14
        \stemUp c4 \stemUp c4 \stemUp c4 | % 15
        \stemDown d4 \stemDown d4 \stemDown d4 | % 16
        \stemUp g,4 r4 r4 }
    \repeat volta 2 {
        | % 17
        R2. | % 18
        r4 \stemDown a'4 ( _\p \stemDown b4 ) | % 19
        \stemDown d2 ( \stemDown e4 ) | \barNumberCheck #20
        r4 \stemDown c4 ( \stemDown b4 ) \pageBreak | % 21
        \stemDown d2 ( \stemDown e4 ) | % 22
        \stemDown es4 ( \stemDown d2 ) ~ | % 23
        \stemDown d4 ( \stemDown c2 ) | % 24
        \stemDown b4 r4 r4 | % 25
        R2. | % 26
        r4 \stemDown g4 _\f \stemDown g4 | % 27
        \stemDown g2 \stemDown e8 \stemDown c8 | % 28
        \stemDown g'4 r4 r4 \pageBreak | % 29
        R2. | \barNumberCheck #30
        \stemDown c2 ( \stemDown b4 | % 31
        \stemDown bes4 \stemDown a4 \stemDown g4 | % 32
        \stemDown f4 ) r4 r4 | % 33
        R2. | % 34
        \stemDown d'2 ( \stemDown cis4 | % 35
        \stemDown c4 \stemDown b4 \stemDown a4 \pageBreak | % 36
        \stemDown g4 ) r4 r4 | % 37
        R2. | % 38
        \stemDown g'2 ( \stemDown fis4 | % 39
        \stemDown f4 \stemDown e4 \stemDown d4 ) | \barNumberCheck #40
        \stemDown c4 -. \stemDown d4 ( \stemDown e4 ) | % 41
        \stemDown f,4 -. \stemDown g4 ( \stemDown a4 ) | % 42
        \stemDown g4 \stemDown g4 \stemDown g4 | % 43
        \stemUp c,4 r4 r4 \pageBreak | % 44
        R2. | % 45
        \stemDown g''2 ( _\p \stemDown fis4 | % 46
        \stemDown f4 \stemDown e4 \stemDown d4 | % 47
        \stemDown cis4 \stemDown d4 \stemDown c4 ) | % 48
        \stemDown b4 ( \stemDown bes4 \stemDown a4 | % 49
        \stemDown as4 \stemDown g4 \stemDown f4 ) | \barNumberCheck #50
        \stemDown e4 ( \stemDown d4 \stemUp c4 ) | % 51
        \stemDown f4 -. \stemDown d4 -. \stemDown g4 -. | % 52
        \stemDown e2 ( _\f \stemDown es4 \pageBreak | % 53
        \stemDown d8 ) r8 \stemDown g8 -. r8 \stemDown f8 -. r8 | % 54
        \stemDown e2 ( \stemDown es4 | % 55
        \stemDown d8 ) r8 \stemDown g8 -. r8 \stemDown f8 -. r8 | % 56
        \stemDown e4 \stemDown e4 \stemDown e4 | % 57
        \stemDown f4 \stemDown f4 \stemDown f4 | % 58
        \stemDown g4 \stemDown g4 \stemDown g4 | % 59
        \stemUp c,4 r4 r4 }
    \pageBreak \repeat volta 2 {
        \stemDown f'2. ( _\p \stemDown e4 ) r4 r4 R2.*2 \stemDown f2. (
        \stemDown e4 ) r4 r4 R2.*2 }
    \pageBreak \repeat volta 2 {
        \stemDown d2. _\f \stemDown c2. \stemDown fis2. \stemDown b,2.
        \stemDown f'2. \stemDown e2. \pageBreak \stemDown dis2. (
        \stemDown e4 ) r4 r4 R2.*4 \stemDown f2. ( _\p \pageBreak
        \stemDown e4 ) r4 r4 R2.*2 \stemDown f2. ( \stemDown e4 ) r4 r4
        R2.*2 }
    }

PartPFourVoiceTwo =  \relative c' {
    \repeat volta 2 {
        \clef "bass" \time 3/4 \key c \major | % 1
         \once \override NoteHead.style = ##f \stemDown c2. s4*15
        \pageBreak s2*9 \pageBreak s1*3 }
    \repeat volta 2 {
        s1*3 \pageBreak s1*6 \pageBreak s4*21 \pageBreak s1*6 \pageBreak
        s4*27 \pageBreak s4*21 }
    \pageBreak \repeat volta 2 {
        s1*6 }
    \pageBreak \repeat volta 2 {
        s2*9 \pageBreak s4*21 \pageBreak s4*21 }
    }

PartPFiveVoiceOne =  \relative b {
    \repeat volta 2 {
        \clef "bass" \time 3/4 \key c \major | % 1
        R2.*6 \pageBreak | % 7
        R2.*2 | % 9
        \stemDown b2 ( _\f \stemDown bes4 | \barNumberCheck #10
        \stemDown a8 ) r8 \stemDown c8 -. r8 \stemDown a8 -. r8 | % 11
        \stemDown b2 ( \stemDown bes4 | % 12
        \stemDown a8 ) r8 \stemDown c8 -. r8 \stemDown a8 -. r8
        \pageBreak | % 13
        \stemDown b4 \stemUp b,4 \stemUp b4 | % 14
        \stemUp c4 \stemUp c4 \stemUp c4 | % 15
        \stemDown d4 \stemDown d4 \stemDown d4 | % 16
        \stemUp g,4 r4 r4 }
    \repeat volta 2 {
        | % 17
        R2. | % 18
        r4 \stemDown fis'4 ( _\p \stemDown g4 ) | % 19
        \stemDown b2 ( \stemDown c4 ) | \barNumberCheck #20
        r4 \stemDown fis,4 ( \stemDown g4 ) \pageBreak | % 21
        \stemDown b2 ( \stemDown c4 ) | % 22
        r4 \stemDown a4 ( \stemDown b4 | % 23
        \stemDown c4 \stemDown e,4 \stemDown fis4 | % 24
        \stemDown g4 ) r4 r4 | % 25
        R2. | % 26
        r4 \stemUp g,4 _\f \stemUp g4 | % 27
        \stemUp g2 \stemUp e8 \stemUp c8 | % 28
        \stemUp g'4 r4 r4 \pageBreak | % 29
        R2. | \barNumberCheck #30
        \stemDown c'2 ( \stemDown b4 | % 31
        \stemDown bes4 \stemDown a4 \stemDown g4 | % 32
        \stemDown f4 ) r4 r4 | % 33
        R2. | % 34
        \stemDown d'2 ( \stemDown cis4 | % 35
        \stemDown c4 \stemDown b4 \stemDown a4 \pageBreak | % 36
        \stemDown g4 ) r4 r4 | % 37
        R2. | % 38
        \stemDown g'2 ( \stemDown fis4 | % 39
        \stemDown f4 \stemDown e4 \stemDown d4 ) | \barNumberCheck #40
        \stemDown c4 -. \stemDown d4 ( \stemDown e4 ) | % 41
        \stemDown f,4 -. \stemDown g4 ( \stemDown a4 ) | % 42
        \stemDown g4 \stemDown g4 \stemDown g4 | % 43
        \stemUp c,4 r4 r4 \pageBreak | % 44
        R2.*8 | % 52
        \stemDown e2 ( _\f \stemDown es4 \pageBreak | % 53
        \stemDown d8 ) r8 \stemDown g8 -. r8 \stemDown f8 -. r8 | % 54
        \stemDown e2 ( \stemDown es4 | % 55
        \stemDown d8 ) r8 \stemDown g8 -. r8 \stemDown f8 -. r8 | % 56
        \stemDown e4 \stemDown e4 \stemDown e4 | % 57
        \stemDown f4 \stemDown f4 \stemDown f4 | % 58
        \stemDown g4 \stemDown g4 \stemDown g4 | % 59
        \stemUp c,4 r4 r4 }
    \pageBreak \repeat volta 2 {
        \stemDown d'2. ( _\p \stemDown c4 ) r4 r4 R2.*2 \stemDown d2. (
        \stemDown c4 ) r4 r4 R2.*2 }
    \pageBreak \repeat volta 2 {
        \stemDown b2. _\f \stemDown a2. \stemDown c2. \stemDown gis2. ~
        \stemDown gis2. \stemDown a2. \pageBreak \stemDown c2. (
        \stemDown b4 ) r4 r4 R2.*4 \stemDown d2. ( _\p \pageBreak
        \stemDown c4 ) r4 r4 R2.*2 \stemDown d2. ( \stemDown c4 ) r4 r4
        R2.*2 }
    }

PartPFiveVoiceTwo =  \relative c' {
    \repeat volta 2 {
        \clef "bass" \time 3/4 \key c \major | % 1
         \once \override NoteHead.style = ##f \stemDown c2. s4*15
        \pageBreak s2*9 \pageBreak s1*3 }
    \repeat volta 2 {
        s1*3 \pageBreak s1*6 \pageBreak s4*21 \pageBreak s1*6 \pageBreak
        s4*27 \pageBreak s4*21 }
    \pageBreak \repeat volta 2 {
        s1*6 }
    \pageBreak \repeat volta 2 {
        s2*9 \pageBreak s4*21 \pageBreak s4*21 }
    }

PartPSixVoiceOne =  \relative c'' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key c \major \transposition c | % 1
        R2.*2 | % 3
        \stemDown c8 _\p r8 \stemUp g8 r8 \stemDown c8 r8 | % 4
        \stemDown e2 ( \stemDown d8 ) r8 | % 5
        R2.*2 \pageBreak | % 7
        \stemDown d8 r8 \stemDown c8 r8 \stemDown d8 r8 | % 8
        \stemDown f2 ( \stemDown e8 ) r8 | % 9
        \stemDown d2. ~ _\f | \barNumberCheck #10
        \stemDown d4 \stemDown d4 \stemDown d4 | % 11
        \stemDown d2. ~ | % 12
        \stemDown d4 \stemDown d4 \stemDown d4 \pageBreak | % 13
        \stemDown d4 \stemDown d4 \stemDown d4 | % 14
        \stemDown e4 \stemDown e4 \stemDown e4 | % 15
        \stemDown d4 \stemDown d4 \stemDown d4 | % 16
        \stemDown d4 r4 r4 }
    \repeat volta 2 {
        | % 17
        \stemUp g,4 _\p \stemUp g4 \stemUp g4 | % 18
        \stemUp g4 \stemUp g4 \stemUp g4 | % 19
        \stemUp g4 \stemUp g4 \stemUp g4 | \barNumberCheck #20
        \stemUp g4 \stemUp g4 \stemUp g4 \pageBreak | % 21
        \stemUp g4 \stemUp g4 \stemUp g4 | % 22
        \stemUp g4 \stemUp g4 \stemUp g4 | % 23
        \stemUp g4 \stemUp g4 \stemUp g4 | % 24
        \stemUp g4 \stemDown g'4 _\f \stemDown g4 | % 25
        \stemDown g2 \stemDown e8 \stemDown c8 | % 26
        \stemDown g'4 \stemUp g,4 \stemUp g4 | % 27
        \stemUp g2 \stemUp e8 \stemUp c8 | % 28
        \stemUp g'4 r4 r4 \pageBreak | % 29
        R2. | \barNumberCheck #30
        \stemDown c4 \stemDown c4 \stemDown c4 | % 31
        \stemDown c4 \stemDown c4 \stemDown c4 | % 32
        \stemDown c4 r4 r4 | % 33
        R2. | % 34
        \stemDown d2 r4 | % 35
        \stemDown d4 \stemDown d4 \stemDown d4 \pageBreak | % 36
        \stemDown d4 r4 r4 | % 37
        R2. | % 38
        \stemUp g,4 \stemUp g4 \stemUp g4 | % 39
        \stemUp g4 \stemUp g4 \stemUp g4 | \barNumberCheck #40
        \stemDown c4 r4 r4 | % 41
        \stemDown c4 r4 r4 | % 42
        \stemUp g4 \stemUp g4 \stemUp g4 | % 43
        \stemUp g4 r4 r4 \pageBreak | % 44
        R2.*8 | % 52
        \stemUp g2. ~ _\f \pageBreak | % 53
        \stemUp g4 \stemUp g4 \stemUp g4 | % 54
        \stemUp g2. ~ | % 55
        \stemUp g4 \stemUp g4 \stemUp g4 | % 56
        \stemDown c4 \stemDown c4 \stemDown c4 | % 57
        \stemDown c4 r4 r4 | % 58
        \stemDown d4 r4 r4 | % 59
        \stemDown c4 r4 r4 }
    \pageBreak \repeat volta 2 {
        \transposition c R2.*8 }
    \pageBreak \repeat volta 2 {
        \stemUp e,4 _\f r4 \stemUp e8 \stemUp e8 \stemUp e4 r4 \stemUp e8
        \stemUp e8 \stemUp e4 r4 \stemUp e8 \stemUp e8 \stemUp e4 r4
        \stemUp e8 \stemUp e8 \stemUp e4 r4 \stemUp e8 \stemUp e8
        \stemUp e4 r4 \stemUp e8 \stemUp e8 \pageBreak \stemUp e4 r4
        \stemUp e8 \stemUp e8 \stemUp e4 r4 r4 R2.*5 \pageBreak R2.*7 }
    }

PartPSevenVoiceOne =  \relative e' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key c \major \transposition c | % 1
        R2.*2 | % 3
        \stemUp e8 _\p r8 \stemUp g8 r8 \stemUp e8 r8 | % 4
        \stemDown c'2 ( \stemUp g8 ) r8 | % 5
        R2.*2 \pageBreak | % 7
        \stemUp g8 r8 \stemUp g8 r8 \stemUp g8 r8 | % 8
        \stemDown d'2 ( \stemDown c8 ) r8 | % 9
        \stemDown d2. ~ _\f | \barNumberCheck #10
        \stemDown d4 \stemDown d4 \stemDown d4 | % 11
        \stemDown d2. ~ | % 12
        \stemDown d4 \stemDown d4 \stemDown d4 \pageBreak | % 13
        \stemUp g,4 \stemUp g4 \stemUp g4 | % 14
        \stemDown c4 \stemDown c4 \stemDown c4 | % 15
        \stemDown d4 \stemDown d4 \stemDown d4 | % 16
        \stemUp g,4 r4 r4 }
    \repeat volta 2 {
        | % 17
        \stemUp g,4 _\p \stemUp g4 \stemUp g4 | % 18
        \stemUp g4 \stemUp g4 \stemUp g4 | % 19
        \stemUp g4 \stemUp g4 \stemUp g4 | \barNumberCheck #20
        \stemUp g4 \stemUp g4 \stemUp g4 \pageBreak | % 21
        \stemUp g4 \stemUp g4 \stemUp g4 | % 22
        \stemUp g4 \stemUp g4 \stemUp g4 | % 23
        \stemUp g4 \stemUp g4 \stemUp g4 | % 24
        \stemUp g4 \stemUp g'4 _\f \stemUp g4 | % 25
        \stemUp g2 \stemUp e8 \stemUp c8 | % 26
        \stemUp g'4 \stemUp g4 \stemUp g4 | % 27
        \stemUp g2 \stemUp e8 \stemUp c8 | % 28
        \stemUp g'4 r4 r4 \pageBreak | % 29
        R2. | \barNumberCheck #30
        \stemUp c,4 \stemUp c4 \stemUp c4 | % 31
        \stemUp c4 \stemUp c4 \stemUp c4 | % 32
        \stemUp c4 r4 r4 | % 33
        R2. | % 34
        \stemDown d'2 r4 | % 35
        \stemDown d4 \stemDown d4 \stemDown d4 \pageBreak | % 36
        \stemUp g,4 r4 r4 | % 37
        R2. | % 38
        \stemUp g4 \stemUp g4 \stemUp g4 | % 39
        \stemUp g4 \stemUp g4 \stemUp g4 | \barNumberCheck #40
        \stemUp c,4 r4 r4 | % 41
        \stemUp c4 r4 r4 | % 42
        \stemUp g'4 \stemUp g4 \stemUp g4 | % 43
        \stemUp e4 r2 \pageBreak | % 44
        R2.*8 | % 52
        \stemUp g2. ~ _\f \pageBreak | % 53
        \stemUp g4 \stemUp g4 \stemUp g4 | % 54
        \stemUp g2. ~ | % 55
        \stemUp g4 \stemUp g4 \stemUp g4 | % 56
        \stemUp c,4 \stemUp c4 \stemUp c4 | % 57
        \stemUp c4 r4 r4 | % 58
        \stemUp g'4 r4 r4 | % 59
        \stemUp e4 r4 r4 }
    \pageBreak \repeat volta 2 {
        \transposition c \stemUp g2. ( _\p \stemUp c,4 ) r4 r4 R2.*2
        \stemUp g'2. ( \stemUp c,4 ) r4 r4 R2.*2 }
    \pageBreak \repeat volta 2 {
        \stemUp e4 _\f r4 \stemUp e8 \stemUp e8 \stemUp e4 r4 \stemUp e8
        \stemUp e8 \stemUp e4 r4 \stemUp e8 \stemUp e8 \stemUp e4 r4
        \stemUp e8 \stemUp e8 \stemUp e4 r4 \stemUp e8 \stemUp e8
        \stemUp e4 r4 \stemUp e8 \stemUp e8 \pageBreak \stemUp e4 r4
        \stemUp e8 \stemUp e8 \stemUp e4 r4 r4 R2.*4 \stemUp g2. ( _\p
        \pageBreak \stemUp c,4 ) r4 r4 R2.*2 \clef "bass" \stemUp g,2. (
        \stemUp c,4 ) r4 r4 R2.*2 }
    }

PartPEightVoiceOne =  \relative c' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key g \major \transposition f | % 1
        R2.*6 \pageBreak | % 7
        R2.*6 \pageBreak | % 13
        R2.*4 }
    \repeat volta 2 {
        | % 17
        R2.*4 \pageBreak | % 21
        R2.*8 \pageBreak | % 29
        R2.*7 \pageBreak | % 36
        R2.*8 \pageBreak | % 44
        R2.*9 \pageBreak | % 53
        R2.*7 }
    \pageBreak \repeat volta 2 {
        \transposition f R2.*8 }
    \pageBreak \repeat volta 2 {
        R2.*6 \pageBreak R2.*7 \pageBreak R2.*7 }
    }

PartPNineVoiceOne =  \relative c' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key g \major \transposition f | % 1
        R2.*6 \pageBreak | % 7
        R2.*6 \pageBreak | % 13
        R2.*4 }
    \repeat volta 2 {
        | % 17
        R2.*4 \pageBreak | % 21
        R2.*8 \pageBreak | % 29
        R2.*7 \pageBreak | % 36
        R2.*8 \pageBreak | % 44
        R2.*9 \pageBreak | % 53
        R2.*7 }
    \pageBreak \repeat volta 2 {
        \transposition f R2.*8 }
    \pageBreak \repeat volta 2 {
        R2.*6 \pageBreak R2.*7 \pageBreak R2.*7 }
    }

PartPOneZeroVoiceOne =  \relative c'' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key c \major | % 1
        R2.*2 | % 3
        \stemDown c4 _\p r4 r4 | % 4
        \stemUp g4 r4 r4 | % 5
        R2.*2 \pageBreak | % 7
        \stemUp g4 r4 r4 | % 8
        \clef "bass" \stemUp c,,4 r4 r4 | % 9
        \clef "treble" \stemUp g''4 _\f r4 r4 | \barNumberCheck #10
        \stemDown d'4 r4 r4 | % 11
        \stemUp g,4 r4 r4 | % 12
        \stemDown d'4 r4 r4 \pageBreak | % 13
        \stemDown d4 r4 r4 | % 14
        \stemDown e4 r4 r4 | % 15
        \stemDown d4 r4 r4 | % 16
        \stemDown d4 r4 r4 }
    \repeat volta 2 {
        | % 17
        \stemUp g,4 _\p r4 r4 | % 18
        R2. | % 19
        \stemUp g4 r4 r4 | \barNumberCheck #20
        R2. \pageBreak | % 21
        \stemUp g4 r4 r4 | % 22
        \stemUp g4 r4 r4 | % 23
        \stemUp g4 r4 r4 | % 24
        \stemUp g4 r4 r4 | % 25
        R2. | % 26
        r4 \stemUp g4 _\f \stemUp g4 | % 27
        \stemUp g2 \stemUp e8 \stemUp c8 | % 28
        \stemUp g'4 r4 r4 \pageBreak | % 29
        R2. | \barNumberCheck #30
        \stemDown c4 \stemDown c4 \stemDown c4 | % 31
        \stemDown c4 \stemDown c4 \stemDown c4 | % 32
        \stemDown c4 r4 r4 | % 33
        R2. | % 34
        \stemDown d2 r4 | % 35
        \stemDown d4 \stemDown d4 \stemDown d4 \pageBreak | % 36
        \stemDown d4 r4 r4 | % 37
        R2. | % 38
        \stemUp g,4 \stemUp g4 \stemUp g4 | % 39
        \stemUp g4 \stemUp g4 \stemUp g4 | \barNumberCheck #40
        \stemDown c4 r4 r4 | % 41
        \stemDown c4 r4 r4 | % 42
        \stemUp g4 \stemUp g4 \stemUp g4 | % 43
        \stemUp g4 r4 r4 \pageBreak | % 44
        R2.*8 | % 52
        \stemUp g2. ~ _\f \pageBreak | % 53
        \stemUp g4 \stemUp g4 \stemUp g4 | % 54
        \stemUp g2. ~ | % 55
        \stemUp g4 \stemUp g4 \stemUp g4 | % 56
        \stemDown c4 \stemDown c4 \stemDown c4 | % 57
        \stemDown c4 r4 r4 | % 58
        \stemDown d4 r4 r4 | % 59
        \stemDown c4 r4 r4 }
    \pageBreak \repeat volta 2 {
        R2.*8 }
    \pageBreak \repeat volta 2 {
        \stemUp e,4 _\f r4 \stemUp e8 \stemUp e8 \stemUp e4 r4 \stemUp e8
        \stemUp e8 \stemUp e4 r4 \stemUp e8 \stemUp e8 \stemUp e4 r4
        \stemUp e8 \stemUp e8 \stemUp e4 r4 \stemUp e8 \stemUp e8
        \stemUp e4 r4 \stemUp e8 \stemUp e8 \pageBreak \stemUp e4 r4
        \stemUp e8 \stemUp e8 \stemUp e4 r4 r4 R2.*5 \pageBreak R2.*7 }
    }

PartPOneOneVoiceOne =  \relative c' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key c \major | % 1
        R2.*2 | % 3
        \stemUp c4 _\p r4 r4 | % 4
        \stemUp g4 r4 r4 | % 5
        R2.*2 \pageBreak | % 7
        \stemUp g4 r4 r4 | % 8
        \clef "bass" \stemUp c,,4 r4 r4 | % 9
        \clef "treble" \stemUp g'''4 _\f r4 r4 | \barNumberCheck #10
        \stemDown d'4 r4 r4 | % 11
        \stemUp g,4 r4 r4 | % 12
        \stemDown d'4 r4 r4 \pageBreak | % 13
        \stemUp g,4 r4 r4 | % 14
        \stemDown c4 r4 r4 | % 15
        \stemDown d4 r4 r4 | % 16
        \stemUp g,4 r4 r4 }
    \repeat volta 2 {
        | % 17
        \stemUp g,4 _\p r4 r4 | % 18
        R2. | % 19
        \stemUp g4 r4 r4 | \barNumberCheck #20
        R2. \pageBreak | % 21
        \stemUp g4 r4 r4 | % 22
        \stemUp g4 r4 r4 | % 23
        \stemUp g4 r4 r4 | % 24
        \stemUp g4 r4 r4 | % 25
        R2. | % 26
        r4 \stemUp g'4 _\f \stemUp g4 | % 27
        \stemUp g2 \stemUp e8 \stemUp c8 | % 28
        \stemUp g'4 r4 r4 \pageBreak | % 29
        R2. | \barNumberCheck #30
        \stemUp c,4 \stemUp c4 \stemUp c4 | % 31
        \stemUp c4 \stemUp c4 \stemUp c4 | % 32
        \stemUp c4 r4 r4 | % 33
        R2. | % 34
        \stemDown d'2 r4 | % 35
        \stemDown d4 \stemDown d4 \stemDown d4 \pageBreak | % 36
        \stemUp g,4 r4 r4 | % 37
        R2. | % 38
        \stemUp g4 \stemUp g4 \stemUp g4 | % 39
        \stemUp g4 \stemUp g4 \stemUp g4 | \barNumberCheck #40
        \stemUp c,4 r4 r4 | % 41
        \stemUp c4 r4 r4 | % 42
        \stemUp g'4 \stemUp g4 \stemUp g4 | % 43
        \stemUp e4 r2 \pageBreak | % 44
        R2.*8 | % 52
        \stemUp g2. ~ _\f \pageBreak | % 53
        \stemUp g4 \stemUp g4 \stemUp g4 | % 54
        \stemUp g2. ~ | % 55
        \stemUp g4 \stemUp g4 \stemUp g4 | % 56
        \stemUp c,4 \stemUp c4 \stemUp c4 | % 57
        \stemUp c4 r4 r4 | % 58
        \stemUp g'4 r4 r4 | % 59
        \stemUp e4 r4 r4 }
    \pageBreak \repeat volta 2 {
        R2.*8 }
    \pageBreak \repeat volta 2 {
        \stemUp e4 _\f r4 \stemUp e8 \stemUp e8 \stemUp e4 r4 \stemUp e8
        \stemUp e8 \stemUp e4 r4 \stemUp e8 \stemUp e8 \stemUp e4 r4
        \stemUp e8 \stemUp e8 \stemUp e4 r4 \stemUp e8 \stemUp e8
        \stemUp e4 r4 \stemUp e8 \stemUp e8 \pageBreak \stemUp e4 r4
        \stemUp e8 \stemUp e8 \stemUp e4 r4 r4 R2.*5 \pageBreak R2.*7 }
    }

PartPOneTwoVoiceOne =  \relative c {
    \repeat volta 2 {
        \clef "bass" \time 3/4 \key c \major | % 1
        R2.*2 | % 3
        \stemUp c4 _\p r4 r4 | % 4
        \stemUp g4 r4 r4 | % 5
        R2.*2 \pageBreak | % 7
        \stemUp g4 r4 r4 | % 8
        \stemUp c4 r4 r4 | % 9
        \stemUp g4 _\f r4 r4 | \barNumberCheck #10
        R2. | % 11
        \stemUp g4 r4 r4 | % 12
        R2. \pageBreak | % 13
        \stemUp g4 r4 r4 | % 14
        \stemUp c4 r4 r4 | % 15
        R2. | % 16
        \stemUp g4 r4 r4 }
    \repeat volta 2 {
        | % 17
        \stemUp g4 _\p r4 r4 | % 18
        R2. | % 19
        \stemUp g4 r4 r4 | \barNumberCheck #20
        R2. \pageBreak | % 21
        \stemUp g4 r4 r4 | % 22
        \stemUp g4 r4 r4 | % 23
        \stemUp g4 r4 r4 | % 24
        \stemUp g4 r4 r4 | % 25
        R2. | % 26
        r4 \stemUp g4 _\f \stemUp g4 | % 27
        \stemUp g4 \stemUp g4 \stemUp c4 | % 28
        \stemUp g4 r4 r4 \pageBreak | % 29
        R2. | \barNumberCheck #30
        \stemUp c2 \stemUp c8 \stemUp c8 | % 31
        \stemUp c4 \stemUp c4 \stemUp c4 | % 32
        \stemUp c4 r4 r4 | % 33
        R2.*3 \pageBreak | % 36
        R2.*2 | % 38
        \stemUp g2 \stemUp g8 \stemUp g8 | % 39
        \stemUp g4 \stemUp g4 \stemUp g4 | \barNumberCheck #40
        \stemUp c4 r4 r4 | % 41
        \stemUp c4 r4 r4 | % 42
        \stemUp g4 \stemUp g4 \stemUp g4 | % 43
        \stemUp c4 r4 r4 \pageBreak | % 44
        R2.*8 | % 52
        \stemUp c4 _\f r4 \stemUp c8 \stemUp c8 \pageBreak | % 53
        \stemUp g4 \stemUp g4 \stemUp g4 | % 54
        \stemUp c4 r4 \stemUp c8 \stemUp c8 | % 55
        \stemUp g4 \stemUp g4 \stemUp g4 | % 56
        \stemUp c4 \stemUp c4 \stemUp c4 | % 57
        \stemUp c4 r4 r4 | % 58
        \stemUp g4 r4 r4 | % 59
        \stemUp c4 r4 r4 }
    \pageBreak \repeat volta 2 {
        R2.*8 }
    \pageBreak \repeat volta 2 {
        R2.*6 \pageBreak R2.*7 \pageBreak R2.*7 }
    }

PartPOneThreeVoiceOne =  \relative g'' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key c \major | % 1
        \stemDown g2 ( _\p \stemDown fis4 | % 2
        \stemDown f4 \stemDown e4 \stemDown d4 | % 3
        \stemDown c8 ) r8 \stemDown b8 -. r8 \stemDown c8 -. r8 | % 4
        \stemDown e2 ( \stemDown d8 ) r8 | % 5
        \stemDown a'2 ( \stemDown g4 | % 6
        \stemDown fis4 \stemDown f4 \stemDown e4 \pageBreak | % 7
        \stemDown d8 ) r8 \stemDown c8 -. r8 \stemDown d8 -. r8 | % 8
        \stemDown f2 ( \stemDown e8 ) r8 | % 9
        \stemDown d'2 ( _\f \stemDown cis4 | \barNumberCheck #10
        \stemDown c8 ) r8 \stemDown a8 -. r8 \stemDown fis8 -. r8 | % 11
        \stemDown d'2 ( \stemDown cis4 | % 12
        \stemDown c8 ) r8 \stemDown a8 -. r8 \stemDown fis8 -. r8
        \pageBreak | % 13
        \stemDown d'8 -. r8 \stemDown d8 -. r8 \stemDown d8 -. r8 | % 14
        \stemDown e2 \stemDown c8 ( \stemDown a8 ) | % 15
        \stemDown c2 \stemDown a8 ( \stemDown fis8 ) | % 16
        \stemDown g4 r4 r4 }
    \repeat volta 2 {
        | % 17
        \stemUp d,2 ( _\p \stemUp cis4 | % 18
        \stemUp c2 \stemUp b4 ) | % 19
        \stemUp f'2 ( \stemUp e4 | \barNumberCheck #20
        \stemUp es2 \stemUp d4 ) \pageBreak | % 21
        \stemUp a'2 ( \stemUp g4 ) | % 22
        \stemUp fis4 ( \stemDown d'4 \stemUp f,4 ) | % 23
        \stemUp e4 ( \stemDown c'4 \stemUp es,4 ) | % 24
        \stemUp d4 \stemUp g4 _\f \stemUp g4 | % 25
        \stemUp g2 \stemUp e8 \stemUp c8 | % 26
        \stemUp g'4 r4 r4 | % 27
        R2. | % 28
        \stemDown g'2 ( \stemDown fis4 \pageBreak | % 29
        \stemDown f4 \stemDown e4 \stemDown d4 | \barNumberCheck #30
        \stemDown c4 ) \stemUp c,4 -. \stemDown d'8 ( \trill \stemDown c16
        \stemDown d16 | % 31
        \stemDown e4 ) \stemDown f4 -. \stemDown g4 -. | % 32
        \stemDown a2 ( \stemDown gis4 | % 33
        \stemDown g4 \stemDown fis4 \stemDown e4 | % 34
        \stemDown d4 ) \stemUp d,4 -. \stemDown g'8 ( \trill \stemDown
        fis16 \stemDown g16 | % 35
        \stemDown a4 ) \stemDown b4 -. \stemDown c4 -. \pageBreak | % 36
        \stemDown d2 ( \stemDown cis4 | % 37
        \stemDown c4 \stemDown b4 \stemDown a4 | % 38
        \stemDown g4 ) \stemUp g,4 -. \stemDown a'8 ( \trill \stemDown g16
        \stemDown a16 | % 39
        \stemDown b4 ) \stemDown c4 -. \stemDown d4 -. | \barNumberCheck
        #40
        \stemDown e4 -. \stemDown b4 ( \stemDown c4 ) | % 41
        \stemDown a4 -. \stemDown e4 ( \stemDown f4 ) | % 42
        \stemDown g8 ( \stemDown a8 \stemDown g8 ) \stemDown e8
        \stemDown f8 \stemDown d8 | % 43
        \stemDown c4 r4 r4 \pageBreak | % 44
        R2.*8 | % 52
        \stemDown g'2 ( _\f \stemDown fis4 \pageBreak | % 53
        \stemDown f8 ) r8 \stemDown d8 -. r8 \stemDown b8 -. r8 | % 54
        \stemDown g'2 ( \stemDown fis4 | % 55
        \stemDown f8 ) r8 \stemDown d'8 -. r8 \stemDown b8 -. r8 | % 56
        \stemDown c8 -. r8 \stemDown c8 -. r8 \stemDown c8 -. r8 | % 57
        \stemDown a2 \stemDown f8 ( \stemDown d8 ) | % 58
        \stemDown f2 \stemDown d8 ( \stemDown b8 ) | % 59
        \stemDown c4 r4 r4 }
    \pageBreak \repeat volta 2 {
        R2. r4 r4 \stemUp a8 _\p \stemUp g8 \stemUp fis8 ( \stemUp g8 )
        \stemUp f8 \stemUp d8 \stemUp e8 \stemUp c8 \stemUp e8 ( \stemUp
        d8 ) \stemUp c8 \stemUp b8 \stemUp a8 \stemUp g8 R2. r4 r4
        \stemUp a'8 \stemUp g8 \stemUp fis8 ( \stemUp g8 ) \stemUp f8
        \stemUp d8 \stemUp b8 \stemUp d8 \stemUp c4 -. \stemUp e4 (
        \stemUp c4 ) }
    \pageBreak \repeat volta 2 {
        \stemDown gis''2. -! _\f \stemDown a2. -! \stemDown c2. -!
        \stemDown b2. -! \stemDown d2. -! \stemDown c2. -! \pageBreak
        \stemDown dis,2. -! \stemDown e2. -! \stemDown dis2. ( \stemDown
        e2. \stemDown cis2. \stemDown d2. ) R2. \pageBreak r4 r4 \stemUp
        a8 \stemUp g8 \stemUp fis8 ( \stemUp g8 ) \stemUp f8 \stemUp d8
        \stemUp e8 \stemUp c8 \stemUp e8 ( \stemUp d8 ) \stemUp c8
        \stemUp b8 \stemUp a8 \stemUp g8 R2. r4 r4 \stemUp a'8 \stemUp g8
        \stemUp fis8 ( \stemUp g8 ) \stemUp f8 \stemUp d8 \stemUp b8
        \stemUp d8 \stemUp c4 -. \stemUp e4 ( \stemUp c4 ) }
    }

PartPOneThreeVoiceTwo =  \relative c' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key c \major s2*9 \pageBreak s2*9
        \pageBreak s1*3 }
    \repeat volta 2 {
        s1*3 \pageBreak s1*6 \pageBreak s4*21 \pageBreak s1*6 \pageBreak
        s4*27 \pageBreak s4*21 }
    \pageBreak \repeat volta 2 {
        | % 1
        s1*6 }
    \pageBreak \repeat volta 2 {
        s2*9 \pageBreak s1 s4*17 _\p \pageBreak s4*21 }
    }

PartPOneFourVoiceOne =  \relative e' {
    \repeat volta 2 {
        \clef "treble" \time 3/4 \key c \major | % 1
        \stemUp e8 ( _\p \stemUp g8 \stemUp e8 \stemUp g8 \stemUp d8
        \stemUp g8 | % 2
        \stemUp c,8 \stemUp g'8 \stemUp c,8 \stemUp g'8 \stemUp f8
        \stemUp g8 ) | % 3
        \stemUp e8 ( \stemUp g8 \stemUp d8 \stemUp g8 \stemUp e8 \stemUp
        g8 | % 4
        \stemUp c,8 \stemUp g'8 \stemUp c,8 \stemUp g'8 \stemUp b,8
        \stemUp g'8 ) | % 5
        \stemUp f8 ( \stemUp g8 \stemUp f8 \stemUp g8 \stemUp e8 \stemUp
        g8 | % 6
        \stemUp d8 \stemUp g8 \stemUp d8 \stemUp g8 \stemUp c,8 \stemUp
        g'8 ) \pageBreak | % 7
        \stemUp b,8 ( \stemUp g'8 \stemUp a,8 \stemUp g'8 \stemUp b,8
        \stemUp g'8 | % 8
        \stemUp d8 \stemUp g8 \stemUp d8 \stemUp g8 \stemUp c,8 \stemUp
        g'8 ) | % 9
        \stemDown d'2 ( _\f \stemDown cis4 | \barNumberCheck #10
        \stemDown c8 ) r8 \stemUp a8 -. r8 \stemUp fis8 -. r8 | % 11
        \stemDown d'2 ( \stemDown cis4 | % 12
        \stemDown c8 ) r8 \stemUp a8 -. r8 \stemUp fis8 -. r8 \pageBreak
        | % 13
        \stemUp g,8 ( \stemUp g'8 ) \stemUp g,8 ( \stemUp g'8 ) \stemUp
        g,8 ( \stemUp g'8 ) | % 14
        \stemUp a,8 ( \stemUp g'8 ) \stemUp a,8 ( \stemUp g'8 ) \stemUp
        a,8 ( \stemUp g'8 ) | % 15
        \stemUp a,8 ( \stemUp fis'8 ) \stemUp a,8 ( \stemUp fis'8 )
        \stemUp a,8 ( \stemUp fis'8 ) | % 16
        \stemUp <b, g'>4 r4 r4 }
    \repeat volta 2 {
        | % 17
        \stemUp b2 ( _\p \stemUp ais4 | % 18
        \stemUp a2 \stemUp g4 ) | % 19
        \stemUp d'2 ( \stemUp c4 ~ | \barNumberCheck #20
        \stemUp c4 \stemUp a4 \stemUp b4 ) \pageBreak | % 21
        \stemUp f'2 ( \stemUp e4 ) | % 22
        \stemUp a,8 ( \stemUp c8 \stemUp d8 \stemUp c8 \stemUp b8
        \stemUp d8 ) | % 23
        \stemUp g,8 ( \stemUp c8 \stemUp e8 \stemUp c8 \stemUp a8
        \stemUp c8 ) | % 24
        \stemUp b4 \stemUp g'4 _\f \stemUp g4 | % 25
        \stemUp g2 \stemUp e8 \stemUp c8 | % 26
        \stemUp g'4 r4 r4 | % 27
        R2. | % 28
        \stemUp g,8 ( \stemUp g'8 \stemUp g,8 \stemUp g'8 \stemUp a,8
        \stemUp g'8 \pageBreak | % 29
        \stemUp b,8 \stemUp g'8 \stemUp c,8 \stemUp g'8 \stemUp d8
        \stemUp g8 ) | \barNumberCheck #30
        \stemUp e8 ( \stemUp g8 \stemUp e8 \stemUp g8 \stemUp f8 \stemUp
        d8 ) | % 31
        \stemUp g8 ( \stemUp c8 ) \stemUp f,8 ( \stemUp c'8 ) \stemUp e,8
        ( \stemUp c'8 ) | % 32
        \stemUp f,8 ( \stemUp c'8 ) \stemUp f,8 ( \stemUp a8 \stemUp e8
        \stemUp a8 | % 33
        \stemUp cis,8 \stemUp a'8 \stemUp d,8 \stemUp a'8 \stemUp g8
        \stemUp a8 ) | % 34
        \stemDown fis8 ( \stemDown a8 \stemDown d8 \stemDown a8
        \stemDown e'8 \stemDown a,8 ) | % 35
        \stemDown fis'8 ( \stemDown d8 ) \stemDown g8 ( \stemDown d8 )
        \stemDown a'8 ( \stemDown d,8 ) \pageBreak | % 36
        \stemDown b'8 ( \stemDown d,8 ) \stemDown b8 ( \stemDown d8
        \stemDown ais8 \stemDown d8 | % 37
        \stemDown a8 \stemDown d8 \stemDown g,8 \stemDown d'8 \stemDown
        c8 \stemDown d8 ) | % 38
        \stemUp b8 ( \stemUp d8 ) \stemUp b8 ( \stemUp d,8 \stemUp c'8
        \stemUp d,8 ) | % 39
        \stemDown d'8 ( \stemDown g8 ) \stemDown c,8 ( \stemDown g'8 )
        \stemDown b,8 ( \stemDown g'8 ) | \barNumberCheck #40
        \stemDown c,4 -. \stemDown b4 ( \stemDown c4 ) | % 41
        \stemUp a4 -. \stemUp e4 ( \stemUp f4 ) | % 42
        \stemUp e8 ( \stemUp f8 \stemUp e8 ) \stemUp c8 \stemUp d8
        \stemUp b8 | % 43
        \stemUp c4 r4 r4 \pageBreak | % 44
        R2.*8 | % 52
        \stemUp g'2 ( _\f \stemUp fis4 \pageBreak | % 53
        \stemUp f8 ) r8 \stemUp d8 -. r8 \stemUp b8 -. r8 | % 54
        \stemUp g'2 ( \stemUp fis4 | % 55
        \stemUp f8 ) r8 \stemDown d'8 -. r8 \stemDown b8 -. r8 | % 56
        \stemUp e,8 ( \stemUp c'8 ) \stemUp e,8 ( \stemUp c'8 ) \stemUp
        e,8 ( \stemUp c'8 ) | % 57
        \stemUp d,8 ( \stemUp c'8 ) \stemUp d,8 ( \stemUp c'8 ) \stemUp
        d,8 ( \stemUp c'8 ) | % 58
        \stemUp d,8 ( \stemUp b'8 ) \stemUp d,8 ( \stemUp b'8 ) \stemUp
        d,8 ( \stemUp b'8 ) | % 59
        \stemUp <e, c'>4 r4 r4 }
    \pageBreak \repeat volta 2 {
        R2.*2 r4 \stemUp d4 -. _\p \stemUp c4 -. \stemUp b4 -. r4 r4
        R2.*2 r4 r4 \stemUp g4 -. \stemUp g4 -. r4 r4 }
    \pageBreak \repeat volta 2 {
        \stemUp d'4 _\f \stemUp d8 \stemUp d8 \stemUp d4 \stemUp c4
        \stemUp c8 \stemUp c8 \stemUp c4 \stemUp dis4 \stemUp dis8
        \stemUp dis8 \stemUp dis4 \stemUp e4 \stemUp e8 \stemUp e8
        \stemUp e4 \stemUp b4 \stemUp b8 \stemUp b8 \stemUp b4 \stemUp c4
        \stemUp c8 \stemUp c8 \stemUp c4 \pageBreak \stemUp c4 \stemUp c8
        \stemUp c8 \stemUp c4 \stemUp b4 \stemDown b'4 _\p \stemDown b4
        r4 \stemUp a4 \stemUp a4 r4 \stemUp gis4 \stemUp gis4 r4 \stemUp
        g4 \stemUp g4 r4 \stemUp fis4 \stemUp fis4 R2. \pageBreak R2.
        \stemUp d2 ( \stemUp c4 ) \stemUp b4 r4 r4 R2.*2 \stemUp b2
        \stemUp d8 ( \stemUp b8 ) \stemUp c4 r4 r4 }
    }

PartPOneFiveVoiceOne =  \relative c'' {
    \repeat volta 2 {
        \clef "alto" \time 3/4 \key c \major | % 1
        R2.*2 | % 3
        \stemDown c4 _\p r4 r4 | % 4
        \stemDown g4 r4 r4 | % 5
        R2.*2 \pageBreak | % 7
        \stemDown g4 r4 r4 | % 8
        \stemDown c,4 r4 r4 | % 9
        \stemUp b8 ( _\f \stemUp d8 \stemUp b8 \stemUp d8 \stemUp bes8
        \stemUp d8 | \barNumberCheck #10
        \stemUp a8 \stemUp d8 \stemUp c8 \stemUp d8 \stemUp a8 \stemUp d8
        ) | % 11
        \stemUp b8 ( \stemUp d8 \stemUp b8 \stemUp d8 \stemUp bes8
        \stemUp d8 | % 12
        \stemUp a8 \stemUp d8 \stemUp c8 \stemUp d8 \stemUp a8 \stemUp d8
        ) \pageBreak | % 13
        \stemDown b8 ( \stemDown d8 ) \stemDown b8 ( \stemDown d8 )
        \stemDown b8 ( \stemDown d8 ) | % 14
        \stemDown c8 ( \stemDown e8 ) \stemDown c8 ( \stemDown e8 )
        \stemDown c8 ( \stemDown e8 ) | % 15
        \stemDown c8 ( \stemDown d8 ) \stemDown c8 ( \stemDown d8 )
        \stemDown c8 ( \stemDown d8 ) | % 16
        \stemUp d4 r4 r4 }
    \repeat volta 2 {
        | % 17
        R2. | % 18
        r4 \stemUp fis,4 ( _\p \stemUp g4 ) | % 19
        \stemUp b2 ( \stemDown c4 ) | \barNumberCheck #20
        r4 \stemUp fis,4 ( \stemUp g4 ) \pageBreak | % 21
        \stemUp b2 ( \stemDown c4 ) | % 22
        r4 \stemUp a4 ( \stemUp b4 | % 23
        \stemDown c4 \stemUp e,4 \stemUp fis4 | % 24
        \stemUp g4 ) \stemDown g'4 _\f \stemDown g4 | % 25
        \stemDown g2 \stemDown e8 \stemDown c8 | % 26
        \stemDown g'4 r4 r4 | % 27
        R2. | % 28
        \stemUp g,2 ( \stemUp a4 \pageBreak | % 29
        \stemUp b4 \stemDown c4 \stemDown d4 ) | \barNumberCheck #30
        \stemDown e2 ( \stemDown f4 | % 31
        \stemDown g4 \stemDown f4 \stemDown e4 ) | % 32
        \stemDown f2 ( \stemDown e4 | % 33
        \stemDown cis4 \stemDown d4 \stemDown g4 ) | % 34
        \stemDown fis2 \stemDown a4 ~ | % 35
        \stemDown a4 ( \stemDown g4 \stemDown fis4 ) \pageBreak | % 36
        \stemDown g4 ( \stemDown b4 \stemDown ais4 | % 37
        \stemDown a4 \stemDown g4 \stemDown c4 ) | % 38
        \stemDown b4 \stemDown d,2 | % 39
        \stemDown g4 ( \stemDown a4 \stemDown b4 ) | \barNumberCheck #40
        \stemDown c4 -. \stemDown f,4 ( \stemDown g4 ) | % 41
        \stemDown c,4 -. \stemUp bes4 ( \stemUp a4 ) | % 42
        \stemUp g4 \stemUp g4 \stemUp g4 | % 43
        \stemUp e4 r4 r4 \pageBreak | % 44
        R2.*8 | % 52
        \stemUp e8 ( _\f \stemUp g8 \stemUp c8 \stemUp g8 ) \stemUp es8
        ( \stemUp g8 ) \pageBreak | % 53
        \stemUp d8 ( \stemUp g8 \stemUp b8 \stemUp g8 ) \stemUp f8 (
        \stemUp g8 ) | % 54
        \stemUp e8 ( \stemUp g8 \stemUp c8 \stemUp g8 ) \stemUp es8 (
        \stemUp g8 ) | % 55
        \stemUp d8 ( \stemUp g8 \stemUp b8 \stemUp g8 ) \stemUp f8 (
        \stemUp g8 ) | % 56
        \stemUp e4 \stemDown c'8 ( \stemDown g'8 ) \stemDown c,8 (
        \stemDown g'8 ) | % 57
        \stemDown a,8 ( \stemDown f'8 ) \stemDown a,8 ( \stemDown f'8 )
        \stemDown a,8 ( \stemDown f'8 ) | % 58
        \stemDown g,8 ( \stemDown f'8 ) \stemDown g,8 ( \stemDown f'8 )
        \stemDown g,8 ( \stemDown f'8 ) | % 59
        \stemUp <g, e'>4 r4 r4 }
    \pageBreak \repeat volta 2 {
        R2.*2 r4 \stemUp g4 -. _\p \stemUp g4 -. \stemUp g4 -. r4 r4
        R2.*2 r4 r4 \stemUp g4 -. \stemUp f4 -. r4 r4 }
    \pageBreak \repeat volta 2 {
        \stemUp b4 _\f \stemUp b8 \stemUp b8 \stemUp b4 \stemUp a4
        \stemUp a8 \stemUp a8 \stemUp a4 \stemUp a4 \stemUp a8 \stemUp a8
        \stemUp a4 \stemUp gis4 \stemUp gis8 \stemUp gis8 \stemUp gis4
        \stemUp gis4 \stemUp gis8 \stemUp gis8 \stemUp gis4 \stemUp a4
        \stemUp a8 \stemUp a8 \stemUp a4 \pageBreak \stemUp a4 \stemUp a8
        \stemUp a8 \stemUp a4 \stemUp gis4 \stemDown gis'4 _\p \stemDown
        gis4 r4 \stemDown fis4 \stemDown fis4 r4 \stemDown e4 \stemDown
        e4 r4 \stemDown e4 \stemDown e4 r4 \stemDown d4 \stemDown d4 R2.
        \pageBreak R2. \stemUp g,2. ~ \stemUp g4 r4 r4 R2.*2 \stemUp d2
        ( \stemUp f4 ) \stemUp e4 r4 r4 }
    }

PartPOneFiveVoiceTwo =  \relative b {
    \repeat volta 2 {
        \clef "alto" \time 3/4 \key c \major s2*9 \pageBreak s2*9
        \pageBreak s4*9 | % 16
        \stemDown b4 s2 }
    \repeat volta 2 {
        s1*3 \pageBreak s1*6 \pageBreak s4*21 \pageBreak s1*6 \pageBreak
        s4*27 \pageBreak s4*21 }
    \pageBreak \repeat volta 2 {
        s1*6 }
    \pageBreak \repeat volta 2 {
        s2*9 \pageBreak s4*21 \pageBreak s4*21 }
    }

PartPOneSixVoiceOne =  \relative c' {
    \repeat volta 2 {
        \clef "bass" \time 3/4 \key c \major | % 1
        R2.*2 | % 3
        \stemDown c4 _\p r4 r4 | % 4
        \stemDown g4 r4 r4 | % 5
        R2.*2 \pageBreak | % 7
        \stemDown g4 r4 r4 | % 8
        \stemUp c,4 r4 r4 | % 9
        \stemDown b'8 ( _\f \stemDown d8 \stemDown b8 \stemDown d8
        \stemDown bes8 \stemDown d8 | \barNumberCheck #10
        \stemDown a8 \stemDown d8 \stemDown c8 \stemDown d8 \stemDown a8
        \stemDown d8 ) | % 11
        \stemDown b8 ( \stemDown d8 \stemDown b8 \stemDown d8 \stemDown
        bes8 \stemDown d8 | % 12
        \stemDown a8 \stemDown d8 \stemDown c8 \stemDown d8 \stemDown a8
        \stemDown d8 ) \pageBreak | % 13
        \stemDown b4 \stemUp b,4 \stemUp b4 | % 14
        \stemUp c4 \stemUp c4 \stemUp c4 | % 15
        \stemDown d4 \stemDown d4 \stemDown d4 | % 16
        \stemUp g,4 r4 r4 }
    \repeat volta 2 {
        | % 17
        \stemUp g4 _\p r4 r4 | % 18
        R2. | % 19
        \stemUp g4 r4 r4 | \barNumberCheck #20
        R2. \pageBreak | % 21
        \stemUp g4 r4 r4 | % 22
        \stemUp g4 r4 r4 | % 23
        \stemUp g4 r4 r4 | % 24
        \stemUp g4 \stemDown g'4 _\f \stemDown g4 | % 25
        \stemDown g2 \stemDown e8 \stemDown c8 | % 26
        \stemDown g'4 r4 r4 | % 27
        R2.*2 \pageBreak | % 29
        R2. | \barNumberCheck #30
        \stemDown c2 ( \stemDown b4 | % 31
        \stemDown bes4 \stemDown a4 \stemDown g4 | % 32
        \stemDown f4 ) r4 r4 | % 33
        R2. | % 34
        \stemDown d'2 ( \stemDown cis4 | % 35
        \stemDown c4 \stemDown b4 \stemDown a4 \pageBreak | % 36
        \stemDown g4 ) r4 r4 | % 37
        R2. | % 38
        \stemDown g'2 ( \stemDown fis4 | % 39
        \stemDown f4 \stemDown e4 \stemDown d4 ) | \barNumberCheck #40
        \stemDown c4 -. \stemDown d4 ( \stemDown e4 ) | % 41
        \stemDown f,4 -. \stemDown g4 ( \stemDown a4 ) | % 42
        \stemDown g4 \stemDown g4 \stemDown g4 | % 43
        \stemUp c,4 r4 r4 \pageBreak | % 44
        R2.*8 | % 52
        \stemDown e8 ( _\f \stemDown g8 \stemDown c8 \stemDown g8 )
        \stemDown es8 ( \stemDown g8 ) \pageBreak | % 53
        \stemDown d8 ( \stemDown g8 \stemDown b8 \stemDown g8 )
        \stemDown f8 ( \stemDown g8 ) | % 54
        \stemDown e8 ( \stemDown g8 \stemDown c8 \stemDown g8 )
        \stemDown es8 ( \stemDown g8 ) | % 55
        \stemDown d8 ( \stemDown g8 \stemDown b8 \stemDown g8 )
        \stemDown f8 ( \stemDown g8 ) | % 56
        \stemDown e4 \stemDown e4 \stemDown e4 | % 57
        \stemDown f4 \stemDown f4 \stemDown f4 | % 58
        \stemDown g4 \stemDown g4 \stemDown g4 | % 59
        \stemUp c,4 r4 r4 }
    \pageBreak \repeat volta 2 {
        R2.*2 r4 \stemDown b'4 -. _\p \stemDown c4 -. \stemDown g4 -. r4
        r4 R2.*2 r4 r4 \stemDown g4 -. \stemUp c,4 -. r4 r4 }
    \pageBreak \repeat volta 2 {
        \stemDown e4 _\f \stemDown e'8 \stemDown e8 \stemDown e4
        \stemDown e,4 \stemDown e'8 \stemDown e8 \stemDown e4 \stemDown
        e,4 \stemDown e'8 \stemDown e8 \stemDown e4 \stemDown e,4
        \stemDown e'8 \stemDown e8 \stemDown e4 \stemDown e,4 \stemDown
        e'8 \stemDown e8 \stemDown e4 \stemDown e,4 \stemDown e'8
        \stemDown e8 \stemDown e4 \pageBreak \stemDown e,4 \stemDown e'8
        \stemDown e8 \stemDown e4 \stemDown e,4 r4 r4 \stemDown b'4 _\p
        r4 r4 \stemDown e4 r4 r4 \stemDown a,4 r4 r4 \stemDown d4 r4 r4
        R2. \pageBreak R2. \stemDown b2 ( \stemDown c4 ) \stemDown g4 r4
        r4 R2.*2 \stemDown g2. ( \stemUp c,4 ) r4 r4 }
    }

PartPOneSevenVoiceOne =  \relative c' {
    \repeat volta 2 {
        \clef "bass" \time 3/4 \key c \major \transposition c | % 1
        R2.*2 | % 3
        \stemDown c4 _\p r4 r4 | % 4
        \stemDown g4 r4 r4 | % 5
        R2.*2 \pageBreak | % 7
        \stemDown g4 r4 r4 | % 8
        \stemUp c,4 r4 r4 | % 9
        \stemDown g'4 _\f r4 r4 | \barNumberCheck #10
        \stemDown d4 r4 r4 | % 11
        \stemDown g4 r4 r4 | % 12
        \stemDown d4 r4 r4 \pageBreak | % 13
        \stemUp b4 \stemUp b4 \stemUp b4 | % 14
        \stemUp c4 \stemUp c4 \stemUp c4 | % 15
        \stemDown d4 \stemDown d4 \stemDown d4 | % 16
        \stemUp g,4 r4 r4 }
    \repeat volta 2 {
        | % 17
        \stemUp g4 _\p r4 r4 | % 18
        R2. | % 19
        \stemUp g4 r4 r4 | \barNumberCheck #20
        R2. \pageBreak | % 21
        \stemUp g4 r4 r4 | % 22
        \stemUp g4 r4 r4 | % 23
        \stemUp g4 r4 r4 | % 24
        \stemUp g4 \stemDown g'4 _\f \stemDown g4 | % 25
        \stemDown g2 \stemDown e8 \stemDown c8 | % 26
        \stemDown g'4 r4 r4 | % 27
        R2.*2 \pageBreak | % 29
        R2. | \barNumberCheck #30
        \stemDown c2 ( \stemDown b4 | % 31
        \stemDown bes4 \stemDown a4 \stemDown g4 | % 32
        \stemDown f4 ) r4 r4 | % 33
        R2. | % 34
        \stemDown d'2 ( \stemDown cis4 | % 35
        \stemDown c4 \stemDown b4 \stemDown a4 \pageBreak | % 36
        \stemDown g4 ) r4 r4 | % 37
        R2. | % 38
        \stemDown g'2 ( \stemDown fis4 | % 39
        \stemDown f4 \stemDown e4 \stemDown d4 ) | \barNumberCheck #40
        \stemDown c4 -. \stemDown d4 ( \stemDown e4 ) | % 41
        \stemDown f,4 -. \stemDown g4 ( \stemDown a4 ) | % 42
        \stemDown g4 \stemDown g4 \stemDown g4 | % 43
        \stemUp c,4 r4 r4 \pageBreak | % 44
        R2.*8 | % 52
        \stemUp c4 _\f r4 r4 \pageBreak | % 53
        \stemUp g4 r4 r4 | % 54
        \stemUp c4 r4 r4 | % 55
        \stemUp g4 r4 r4 | % 56
        \stemDown e'4 \stemDown e4 \stemDown e4 | % 57
        \stemDown f4 \stemDown f4 \stemDown f4 | % 58
        \stemDown g4 \stemDown g4 \stemDown g4 | % 59
        \stemUp c,4 r4 r4 }
    \pageBreak \repeat volta 2 {
        \transposition c R2.*2 r4 \stemDown b'4 -. _\p \stemDown c4 -.
        \stemDown g4 -. r4 r4 R2.*2 r4 r4 \stemDown g4 -. \stemUp c,4 -.
        r4 r4 }
    \pageBreak \repeat volta 2 {
        \stemDown e4 _\f \stemDown e'8 \stemDown e8 \stemDown e4
        \stemDown e,4 \stemDown e'8 \stemDown e8 \stemDown e4 \stemDown
        e,4 \stemDown e'8 \stemDown e8 \stemDown e4 \stemDown e,4
        \stemDown e'8 \stemDown e8 \stemDown e4 \stemDown e,4 \stemDown
        e'8 \stemDown e8 \stemDown e4 \stemDown e,4 \stemDown e'8
        \stemDown e8 \stemDown e4 \pageBreak \stemDown e,4 \stemDown e'8
        \stemDown e8 \stemDown e4 \stemDown e,4 r4 r4 \stemDown b'4 _\p
        r4 r4 \stemDown e4 r4 r4 \stemDown a,4 r4 r4 \stemDown d4 r4 r4
        R2. \pageBreak R2. \stemDown b2 ( \stemDown c4 ) \stemDown g4 r4
        r4 R2.*2 \stemDown g2. ( \stemUp c,4 ) r4 r4 _ "Menuetto D.C." }
    }


% The score definition
\score {
    <<
        
        \new StaffGroup
        <<
            \new Staff
            <<
                \set Staff.instrumentName = "Flauto"
                \set Staff.shortInstrumentName = "Fl."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneVoiceOne" {  \voiceOne \PartPOneVoiceOne }
                    \context Voice = "PartPOneVoiceTwo" {  \voiceTwo \PartPOneVoiceTwo }
                    >>
                >>
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = "Oboe I"
                    \set Staff.shortInstrumentName = "Ob. I"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPTwoVoiceOne" {  \voiceOne \PartPTwoVoiceOne }
                        \context Voice = "PartPTwoVoiceTwo" {  \voiceTwo \PartPTwoVoiceTwo }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Oboe II"
                    \set Staff.shortInstrumentName = "Ob. II"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPThreeVoiceOne" {  \voiceOne \PartPThreeVoiceOne }
                        \context Voice = "PartPThreeVoiceTwo" {  \voiceTwo \PartPThreeVoiceTwo }
                        >>
                    >>
                
                >>
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = "Fagotto I"
                    \set Staff.shortInstrumentName = "Fgt. I"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPFourVoiceOne" {  \voiceOne \PartPFourVoiceOne }
                        \context Voice = "PartPFourVoiceTwo" {  \voiceTwo \PartPFourVoiceTwo }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Fagotto II"
                    \set Staff.shortInstrumentName = "Fgt. II"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPFiveVoiceOne" {  \voiceOne \PartPFiveVoiceOne }
                        \context Voice = "PartPFiveVoiceTwo" {  \voiceTwo \PartPFiveVoiceTwo }
                        >>
                    >>
                
                >>
            
            >>
        \new StaffGroup
        <<
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = "Corno I in C"
                    \set Staff.shortInstrumentName = "Cn. I"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPSixVoiceOne" {  \PartPSixVoiceOne }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Corno II in C"
                    \set Staff.shortInstrumentName = "Cn. II"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPSevenVoiceOne" {  \PartPSevenVoiceOne }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Corno I in F"
                    \set Staff.shortInstrumentName = "Cn. I"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPEightVoiceOne" {  \PartPEightVoiceOne }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Corno II in F"
                    \set Staff.shortInstrumentName = "Cn. II"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPNineVoiceOne" {  \PartPNineVoiceOne }
                        >>
                    >>
                
                >>
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = "Clarino I in C"
                    \set Staff.shortInstrumentName = "Cln. I"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneZeroVoiceOne" {  \PartPOneZeroVoiceOne }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Clarino II in C"
                    \set Staff.shortInstrumentName = "Cln. II"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneOneVoiceOne" {  \PartPOneOneVoiceOne }
                        >>
                    >>
                
                >>
            
            >>
        \new Staff
        <<
            \set Staff.instrumentName = "Timpani in C–G"
            \set Staff.shortInstrumentName = "Timp."
            
            \context Staff << 
                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                \context Voice = "PartPOneTwoVoiceOne" {  \PartPOneTwoVoiceOne }
                >>
            >>
        \new StaffGroup
        <<
            \new StaffGroup \with { systemStartDelimiter =
                #'SystemStartBrace }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = "Violino I"
                    \set Staff.shortInstrumentName = "Vln. I"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneThreeVoiceOne" {  \voiceOne \PartPOneThreeVoiceOne }
                        \context Voice = "PartPOneThreeVoiceTwo" {  \voiceTwo \PartPOneThreeVoiceTwo }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Violino II"
                    \set Staff.shortInstrumentName = "Vln. II"
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneFourVoiceOne" {  \PartPOneFourVoiceOne }
                        >>
                    >>
                
                >>
            \new Staff
            <<
                \set Staff.instrumentName = "Viola"
                \set Staff.shortInstrumentName = "Vla."
                
                \context Staff << 
                    \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                    \context Voice = "PartPOneFiveVoiceOne" {  \voiceOne \PartPOneFiveVoiceOne }
                    \context Voice = "PartPOneFiveVoiceTwo" {  \voiceTwo \PartPOneFiveVoiceTwo }
                    >>
                >>
            \new StaffGroup \with { }
            
            <<
                \new Staff
                <<
                    \set Staff.instrumentName = "Violoncello"
                    \set Staff.shortInstrumentName = "Vc."
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneSixVoiceOne" {  \PartPOneSixVoiceOne }
                        >>
                    >>
                \new Staff
                <<
                    \set Staff.instrumentName = "Basso"
                    \set Staff.shortInstrumentName = "Bs."
                    
                    \context Staff << 
                        \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                        \context Voice = "PartPOneSevenVoiceOne" {  \PartPOneSevenVoiceOne }
                        >>
                    >>
                
                >>
            
            >>
        
        >>
    \layout {}
    % To create MIDI output, uncomment the following line:
    %  \midi {\tempo 4 = 150 }
    }

