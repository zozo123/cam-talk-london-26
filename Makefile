.PHONY: all deck dist guide clean short

all: deck

deck: talk.pdf guide

SOURCES := talk.tex $(wildcard preamble/*.tex) $(wildcard acts/*/*.tex) $(wildcard assets/*)

guide: $(SOURCES) tools/presenter_guide.py
	python3 tools/presenter_guide.py --check

dist: deck
	mkdir -p dist
	cp talk.pdf dist/forkable-sandboxes-cambridge.pdf

talk.pdf: $(SOURCES)
	pdflatex -halt-on-error -interaction=nonstopmode talk.tex
	pdflatex -halt-on-error -interaction=nonstopmode talk.tex

# Short 20-slide version: talk-short.tex + short/*.tex, same preamble.
SHORT_SOURCES := talk-short.tex $(wildcard preamble/*.tex) $(wildcard short/*.tex) $(wildcard assets/*)

short: talk-short.pdf talk-short-handout.pdf
	python3 tools/presenter_guide.py --short --check
	mkdir -p dist
	cp talk-short.pdf dist/forkable-sandboxes-cambridge-short.pdf
	cp talk-short-handout.pdf dist/forkable-sandboxes-cambridge-short-handout.pdf

talk-short-handout.pdf: talk-short-handout.tex $(SHORT_SOURCES)
	pdflatex -halt-on-error -interaction=nonstopmode talk-short-handout.tex
	pdflatex -halt-on-error -interaction=nonstopmode talk-short-handout.tex

talk-short.pdf: $(SHORT_SOURCES)
	pdflatex -halt-on-error -interaction=nonstopmode talk-short.tex
	pdflatex -halt-on-error -interaction=nonstopmode talk-short.tex

clean:
	rm -f talk-short-handout.aux talk-short-handout.log talk-short-handout.nav talk-short-handout.out talk-short-handout.snm talk-short-handout.toc talk-short-handout.vrb talk-short-handout.pdf
	rm -f talk-short.aux talk-short.log talk-short.nav talk-short.out talk-short.snm talk-short.toc talk-short.vrb talk-short.pdf
	rm -f talk.aux talk.log talk.nav talk.out talk.snm talk.toc talk.vrb talk.pdf
