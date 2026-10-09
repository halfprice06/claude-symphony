\version "2.24.0"
pedAflat = \markup \harp-pedal #"^-^|^--^"
pedNat = \markup \harp-pedal #"---|----"
global = {
  \key c \minor \time 4/4
  \tempo "Lento" 4 = 50
  s1*14
  \mark \default
  \tempo "Allegro appassionato" 4 = 126
  s1*18
  \mark \default
  s1*12 \tempo \markup \medium \italic "poco rit." s1*2
  \break
  \key aes \major \mark \default
  \tempo "Poco meno mosso" 4 = 100
  s1*19 \tempo \markup \medium \italic "rit." s1*3
  \mark \default
  \tempo "a tempo" 4 = 126
  s1*4
  \tempo "Poco più tranquillo" 4 = 108
  s1*4
  \break
  \key c \minor \mark \default
  \tempo "a tempo" 4 = 126
  s1*20
  \key b \minor \mark \default
  s1*6
  \key c \minor
  s1*6
  \mark \default
  s1*4 \tempo \markup \medium \italic "allargando" s1*2 \tempo "a tempo" s1*8
  \mark \default
  s1*14 \tempo \markup \medium \italic "poco rit." s1*2
  \break
  \key c \major \mark \default
  \tempo "Poco meno mosso" 4 = 100
  s1*15
  \mark \default
  s1*7 \tempo \markup \medium \italic "rit." s1*2
  \break
  \key c \minor \mark \default
  \tempo "Allegro appassionato (Tempo dell'Allegro)" 4 = 126
  s1*3 \tempo \markup \medium \italic "allargando" s1
  \mark \default
  \tempo "Più lento" 4 = 72
  s1*6 \tempo \markup \medium \italic "rit." s1*2
  \tempo "Tempo I (Lento)" 4 = 50
  s1*4
  \bar "|."
}
