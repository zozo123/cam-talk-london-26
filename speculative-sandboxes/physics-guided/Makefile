.PHONY: check pdf clean
check:
	python3 verify_equations.py
pdf:
	latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -jobname=evidence-frontiers main.tex
clean:
	latexmk -C -jobname=evidence-frontiers main.tex
