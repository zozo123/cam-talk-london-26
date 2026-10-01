.PHONY: all academic short dist guide present clean

SHORT := $(wildcard slides/*.tex)

all: academic short

academic: talk.pdf guide

guide: talk.tex tools/presenter_guide.py
	python3 tools/presenter_guide.py --check

present: talk.pdf tools/present_copy.py
	python3 tools/present_copy.py

short: talk-30min.pdf

dist: all present
	mkdir -p dist
	cp talk.pdf dist/forkable-sandboxes-cambridge.pdf
	cp talk.pdf dist/forkable-sandboxes-cambridge-40.pdf
	cp talk-present.pdf dist/forkable-sandboxes-cambridge-present.pdf
	cp talk-30min.pdf dist/forkable-sandboxes-30min.pdf

talk.pdf: talk.tex
	pdflatex -halt-on-error -interaction=nonstopmode talk.tex
	pdflatex -halt-on-error -interaction=nonstopmode talk.tex

talk-30min.pdf: talk-30min.tex $(SHORT)
	pdflatex -halt-on-error -interaction=nonstopmode talk-30min.tex
	pdflatex -halt-on-error -interaction=nonstopmode talk-30min.tex

clean:
	rm -f talk.aux talk.log talk.nav talk.out talk.snm talk.toc talk.vrb talk.pdf talk-present.pdf
	rm -f talk-30min.aux talk-30min.log talk-30min.nav talk-30min.out talk-30min.snm talk-30min.toc talk-30min.vrb talk-30min.pdf
