\version "2.24.0"
\include "Fonctions.lyp"                     
\include "Global.lyp"                     

#(set-global-staff-size 20)  

\paper{ #(define page-breaking ly:page-turn-breaking)
    top-margin = 5.0
    bottom-margin = 5.0
    obsolete-before-title-space = 10.0  score-markup-spacing.basic-distance = #(/ obsolete-before-title-space staff-space)
    obsolete-after-title-space = 5.0  markup-system-spacing.basic-distance = #(/ obsolete-after-title-space staff-space)
	oddHeaderMarkup = \markup \fill-line { 
				" "
				\unless \on-first-page \fromproperty #'header:instrumentHeader
				\if \should-print-page-number \fromproperty #'page:page-number-string }
	evenHeaderMarkup = \markup \fill-line {
				\if \should-print-page-number \fromproperty #'page:page-number-string
				\unless \on-first-page \fromproperty #'header:instrumentHeader
				" " }
    oddFooterMarkup = \markup \fill-line \teeny { \fromproperty #'header:copyright }
    ragged-last-bottom = ##f
    first-page-number = 2
}	%% fin paper
\book {
\header {
    title = \cTitre
    composer =	\cCompositeur
	copyright = \cCopyright
	poet = \markup \box { \pad-around #1 {"Timbales"}}	%% placé en haut à gauche
	instrumentHeader = \markup {"Timbales"}
}	%% fin header

\markup \fill-line {\bold \huge "I"}
\score {
		\new Staff << 
			\reperes \silencesMulti
			\set Staff.instrumentName = \markup {\bold {"Sol-Ré"}}
		 	\keepWithTag #'partie
			\include "Mvt1/Ti-1.lyp" >>
}	%% fin score I

\markup \fill-line {\bold \huge "II"}
\markup { \fill-line {\huge "tacet"}}
\markup "  "
%% fin score II

\markup \fill-line {\bold \huge "III"}
\score {
		\new Staff { 
			\reperes \silencesMulti
			\set Staff.instrumentName = \markup {\bold {"Sol-Ré"}}
		 	\keepWithTag #'partie
			\include "Mvt3/Ti-3.lyp" }
}	%% fin score III

\markup \fill-line {\bold \huge "IV"}
\score {
		\new Staff { 
			\reperes \silencesMulti
			\set Staff.instrumentName = \markup {\bold {"Sol-Ré"}}
		 	\keepWithTag #'partie
			\include "Mvt4/Ti-4.lyp" }
}	%% fin score IV

}	%% fin book	
