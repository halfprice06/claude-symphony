\version "2.24.0"
%{
  ***********************************************************************
  * Dvořák - Symphony nr 7                                              *
  *                                                                     *
  * encodage par J.F. Lucarelli                                         *
  * 18/11/12 - 01/11/2013                                               *
  * Ver 0.0 : 04/09/2013                                                *
  * Ver 1.0 : 01/11/2013                                                *
  *                                                                     *
  * Symphonie n°7 : mouvement III - Scherzo Vivace                      *
  * Fichier de notes, Violoncello II                                    *
  *                                                                     *
  * Ne pas compiler                                                     *
  *                                                                     *
  ***********************************************************************
%}

\include "Common/Version.ly"


SgMcVioloncelloII = {
  \relative c {

    \include "Common/Properties.ly"

    \tag #'partScore
      \oneMMRNumberOn

    s2 s4

    % partie I, commune

    s1. * 91

    % partie II, séparée

    \bar "||"

    \key g \major

    \tag #'partScore
      \set Staff.shortInstrumentName = "II"
    \elseTag #'partScore
      \set Staff.shortInstrumentName = \markup {\center-column {Vlc. II}}

    \TempoIIIMM

   \tupletSpan 2

    % Les violoncelles se dédoublent - \break forcé
    \break

    \tag #'partScore {
      \tuplet 6/4 {
        cis8 \pp ( d cis d cis d
      }
      \tuplet 6/4 {
        \repeat tremolo 3 {cis8 d} \repeat tremolo 3 {cis8 d )}
      }
    }
    \elseTag #'partScore {
      \tuplet 6/4 {
        cis8 \ppp ([d cis d cis d] cis [d cis d cis d] cis [d cis d cis d])
      }
    }

    \tag #'partScore
      \set Staff.shortInstrumentName = ""

    \tuplet 6/4 {
      \repeat tremolo 3 {cis8 ( d} \repeat tremolo 3 {cis8 d} \repeat tremolo 3 {cis8 d )}
    }
    \tuplet 6/4 {
      \repeat tremolo 3 {cis8 \< ( d} \repeat tremolo 3 {cis8 d} \repeat tremolo 3 {cis8 d ) \bindDynamics}
    }
    \tuplet 6/4 {
      \repeat tremolo 3 {cis8 \> ( d} \repeat tremolo 3 {cis8 d} \repeat tremolo 3 {cis8 d ) \!}
    }
    \tuplet 6/4 {
      \repeat tremolo 3 {cis,8 \pp ( d} \repeat tremolo 3 {cis8 d} \repeat tremolo 3 {cis8 d )}
    }
    \tuplet 6/4 {
      \repeat tremolo 3 {cis8 \< ( d} \repeat tremolo 3 {cis8 d} \repeat tremolo 3 {cis8 d ) \!}
    }
    \tuplet 6/4 {
      \repeat tremolo 3 {cis8 \> ( d} \repeat tremolo 3 {cis8 d} \repeat tremolo 3 {cis8 d ) \!}
    }
    \tuplet 6/4 {
      \repeat tremolo 3 {ais'8 ( \p \< b} \repeat tremolo 3 {ais8 b} \repeat tremolo 3 {ais8 b ) \!}
    }
    \tupletSpan 2.
    \tuplet 9/6 {b8 ( c b c b c b c b )}
    \tuplet 8/6 {gis \f ( a? gis a gis a gis a )}
    \tupletSpan 2
    \tuplet 6/4 {
      \repeat tremolo 3 {ais8 ( \fz \> b} \repeat tremolo 3 {ais8 b} \repeat tremolo 3 {ais8 b ) \!}
    }
    \tuplet 6/4 {
      \repeat tremolo 3 {gis8 ( \p \dim a! \!} \repeat tremolo 3 {gis8 a} \repeat tremolo 3 {gis8 a ) \!}
    }
    \tupletSpan 2.
    \tuplet 9/6 {e8 \pp ( dis e dis e dis e dis e )}
    \tuplet 9/6 {c' ( b c b c b c b c )}

    % Les violoncelles se rejoignent - \break forcé
    \break
  }

  % partie III, commune

  \tag #'partScore
    \set Staff.shortInstrumentName = \markup {\center-column {I+ II}}
  \elseTag #'partScore
      \set Staff.shortInstrumentName = \markup {\center-column {Vlc. I+ II}}
    s1.

    \tag #'partScore
      \set Staff.shortInstrumentName = ""
    \elseTag #'partScore
      \set Staff.shortInstrumentName = "Vlc."

    s1. * 36

    % partie IV, séparée

    \relative c {
      \tag #'partScore
        \set Staff.shortInstrumentName = "II"
      \elseTag #'partScore
        \set Staff.shortInstrumentName = \markup {\center-column {Vlc. II}}
      \tag #'partScore
        \oneMMRNumberOn

      \key g \major

      % Les violoncelles se séparent - \break forcé
      \break
      r2 r4 r e4 \p ( d )
      \tag #'partScore
        \set Staff.shortInstrumentName = ""
      <<{d2. ( c2 bes4 )}{s4 s4 s4 \< s s s \!}>>
      a4 \< ( c4. ees8 ) ees4 ( d4. cis8 ) \!
      cis4 \f ( d f ~ f ) e? ( d )
      e2. \fz ( ~ e2 \dim c!4 ) \!
      d2. \p ( ~ d2 \dim bes4 ) \!
      \tupletSpan 2.
      \tuplet 8/6 {a8 \pp ( d cis d cis d cis d a bes a bes a bes a bes )}
      \tupletSpan 2
      <<{\tuplet 6/4 {\repeat tremolo 3 {b! ( c} \repeat tremolo 3 {b c} \repeat tremolo 3 {b c )}}}{s4 s1 \< s4 \!}>>
      \tuplet 6/4 {
        \repeat tremolo 3 {a8 ( bes \>} \repeat tremolo 3 {a bes} \repeat tremolo 3 {a bes \! )}
      }
      \tuplet 6/4 {
        \repeat tremolo 3 {e, \pp ( f} \repeat tremolo 3 {e f} \repeat tremolo 3 {e f )}
      }
      \tuplet 6/4 {
        \repeat tremolo 3 {a ( bes} \repeat tremolo 3 {a bes} \repeat tremolo 3 {a bes )}
      }
      a8 \mp ([d fis! a]) a,8 ([d fis a]) a, ([d fis a])
      % Les violoncelles se rejoignent - \break forcé
      \break
    }
  }

%{
  ***************************************************************
  * Création des voix                                           *
  ***************************************************************
%}

voiceSgMcVioloncelloII = \new Voice {
  \time 6/4
  % Permet de prendre en compte la levée dans le comptage des mesures 
  \set Timing.measurePosition = #(ly:make-moment 3/4)
  \key d \minor
  \set Staff.instrumentName = \markup {\fontsize #3 "Violoncelli"}
  \tag #'partScore
    \set Staff.shortInstrumentName = ""
  \elseTag #'partScore
    \set Staff.shortInstrumentName = "Vlc."
  \set Staff.midiInstrument = "string ensemble 1"
  \clef bass
  \SgMcVioloncelloII
}
