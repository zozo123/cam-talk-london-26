.PHONY: all clean

all: talk.pdf

talk.pdf: talk.tex
	pdflatex -halt-on-error -interaction=nonstopmode talk.tex
	pdflatex -halt-on-error -interaction=nonstopmode talk.tex

clean:
	rm -f talk.aux talk.log talk.nav talk.out talk.snm talk.toc talk.vrb talk.pdf
