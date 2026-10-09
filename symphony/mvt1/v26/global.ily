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
  s1*14
  \break
  \key aes \major \mark \default
  \tempo "Poco meno mosso" 4 = 100
  s1*22
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
  s1*14
  \mark \default
  s1*16
  \break
  \key c \major \mark \default
  \tempo "Poco meno mosso" 4 = 100
  s1*15
  \mark \default
  s1*9
  \break
  \key c \minor \mark \default
  \tempo "Allegro appassionato (Tempo dell'Allegro)" 4 = 126
  s1*4
  \mark \default
  \tempo "Più lento" 4 = 72
  s1*8
  \tempo "Tempo I (Lento)" 4 = 50
  s1*4
  \bar "|."
}
