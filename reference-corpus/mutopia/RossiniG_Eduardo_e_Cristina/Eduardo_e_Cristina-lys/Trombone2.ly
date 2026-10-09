\version "2.24.0"
\include "Fonctions.lyp"                     
\include "Global.lyp"                     

#(set-global-staff-size 20)  

\paper{ #(define page-breaking ly:page-turn-breaking) 	
    top-margin = 5\mm
    bottom-margin = 5\mm
    obsolete-before-title-space = 5\mm  score-markup-spacing.basic-distance = #(/ obsolete-before-title-space staff-space)
    head-separation = 5\mm
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
    subsubtitle = \markup {\fontsize #2 "Ouverture"}
    composer =	\cCompositeur
		copyright = \markup {\concat {
				\char #169  "2008-" \italic {"Le Concert - "} \cRefConcert " / " \cCompositeur " - " \cTitre}}
		poet = \markup \box { \pad-around #1 {"Trombone 2"}}	%% placé en haut à gauche
		instrumentHeader = \markup {"Trombone 2"}
}

\score {
		\new Staff << 
			\reperes \silencesMulti
		 	\keepWithTag #'partie
			\include "Mus/Tb2.lyp"
		>>
}	%% fin score
}	%% fin book	
