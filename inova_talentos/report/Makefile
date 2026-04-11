############################################
# Makefile for thesis
############################################

all:
	TEXMF_OUTPUT_DIRECTORY=. pdflatex -shell-escape main
	bibtex main
	TEXMF_OUTPUT_DIRECTORY=. pdflatex -shell-escape main
	TEXMF_OUTPUT_DIRECTORY=. pdflatex -shell-escape main
	date

clean:
	rm -rf *.gz *.bbl *.bcf *.aux *.log *.blg *.out main.pdf *~