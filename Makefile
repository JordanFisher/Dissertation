# Mathias Kölsch

LATEX="/cygdrive/c/Program Files/texmf/miktex/bin/latex"
BIBTEX="/cygdrive/c/Program Files/texmf/miktex/bin/bibtex"
DVIPS="/cygdrive/c/Program Files/texmf/miktex/bin/dvips"
GSVIEW="/cygdrive/c/Program Files/ghostscript/GSview/gsview/gsview32.exe"
BIBINPUTS=$(HOMEDRIVE)\\$(HOMEPATH)\\mybibfolder

# these are for example for SIGGRAPH papers:
PS2PDF_FLAGS=-dCompatibilityLevel=1.3 -dMaxSubsetPct=100 -dSubsetFonts=true -dEmbedAllFonts=true -dAutoFilterColorImages=false -dAutoFilterGrayImages=false -dColorImageFilter=/FlateEncode -dGrayImageFilter=/FlateEncode -dMonoImageFilter=/FlateEncode

# Dissertations should have 600dpi or more:
# -dGrayImageResolution=600 -dColorImageResolution=600 -dMonoImageResolution=600

default: Dissertation.dvi

ps:	Dissertation.ps

pdf:	Dissertation.pdf

Dissertation.dvi: Dissertation.tex Title.tex Dedicate.tex Acknowledgements.tex Vitae.tex Abstract.tex Intro.tex ucthesis.cls uct12.clo
	${LATEX} Dissertation
	${BIBTEX} -include-directory=${BIBINPUTS} Dissertation
	${LATEX} Dissertation
	${LATEX} Dissertation

Dissertation.ps: Dissertation.dvi
	${DVIPS} -t letter -Ppdf -G0 Dissertation.dvi -o Dissertation.ps
#	${GSVIEW} Dissertation.ps

Dissertation.pdf: Dissertation.ps
	ps2pdf ${PS2PDF_FLAGS} Dissertation.ps

clean:	
	rm -f *.aux
	rm -f Dissertation.dvi
	rm -f Dissertation.ps
	rm -f Dissertation.pdf
	rm -f Dissertation.bbl
	rm -f Dissertation.blg
	rm -f Dissertation.log
	rm -f Dissertation.lof
	rm -f Dissertation.toc

realclean: clean
	rm -f *~


