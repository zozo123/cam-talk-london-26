.PHONY: all deck dist guide clean

all: deck

deck: talk.pdf guide

guide: talk.tex tools/presenter_guide.py
	python3 tools/presenter_guide.py --check

dist: deck
	mkdir -p dist
	cp talk.pdf dist/forkable-sandboxes-cambridge.pdf

talk.pdf: talk.tex
	pdflatex -halt-on-error -interaction=nonstopmode talk.tex
	pdflatex -halt-on-error -interaction=nonstopmode talk.tex

clean:
	rm -f talk.aux talk.log talk.nav talk.out talk.snm talk.toc talk.vrb talk.pdf
