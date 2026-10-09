\version "2.22.0"				%%% Méhul - Symphonie 1 - mvt 4
\include "Fonctions.lyp"                     
\include "Global.lyp"   

\score {
   \new StaffGroup <<
      \new Staff {
         \set Staff.midiInstrument = "flute"
         \partCombine 
            \relative c'' {\keepWithTag #'score \include "Mvt4/Fl1-4.lyp"}
            \relative c'' {\keepWithTag #'score \include "Mvt4/Fl2-4.lyp"}
      }
      \new Staff {
         \set Staff.midiInstrument = "oboe"
         \partCombine 
            \relative c'' {\keepWithTag #'score \include "Mvt4/Hb1-4.lyp"}
            \relative c'' {\keepWithTag #'score \include "Mvt4/Hb2-4.lyp"}
       }     
      \new Staff {
         \set Staff.midiInstrument = "clarinet"
         \partCombine 
            \relative c'' {\keepWithTag #'score \include "Mvt4/Cl1-4.lyp"}
            \relative c'' {\keepWithTag #'score \include "Mvt4/Cl2-4.lyp"}
      }
      \new Staff {
         \set Staff.midiInstrument = "bassoon"
         \partCombine 
            \relative c {\keepWithTag #'score \include "Mvt4/Bn1-4.lyp"}
            \relative c {\keepWithTag #'score \include "Mvt4/Bn2-4.lyp"}
       }     
      \new Staff {
         \set Staff.midiInstrument = "french horn"
         \partCombine 
            \relative c'' \transpose c g {\keepWithTag #'score \include "Mvt4/C1-4.lyp"}
            \relative c'' \transpose c g {\keepWithTag #'score \include "Mvt4/C2-4.lyp"}
      }
      \new Staff {
         \set Staff.midiInstrument = "timpani"
			\keepWithTag #'score \include "Mvt4/Ti-4.lyp"
      }
      \new Staff {
         \set Staff.midiInstrument = "violin"
			\keepWithTag #'score \include "Mvt4/V1-4.lyp"
         }
      \new Staff {
         \set Staff.midiInstrument = "violin"
			\keepWithTag #'score \include "Mvt4/V2-4.lyp"
         }
      \new Staff {
         \set Staff.midiInstrument = "viola"
			\keepWithTag #'score \include "Mvt4/A-4.lyp"
      }
      \new Staff {
         \set Staff.midiInstrument = "cello"
			\keepWithTag #'score \include "Mvt4/Vc-4.lyp"
      }
      \new Staff {
         \set Staff.midiInstrument = "contrabass"
			\keepWithTag #'score \include "Mvt4/Cb-4.lyp"
      }
   >>

\midi {     \tempo 2 = 90
 }
}
