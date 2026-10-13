.PHONY: check pdf clean

check:
	python3 verify_math.py
	python3 -m unittest -v test_reference.py

pdf:
	latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -jobname=acceptance-aware-forkable-compute main.tex

clean:
	latexmk -c -jobname=acceptance-aware-forkable-compute main.tex