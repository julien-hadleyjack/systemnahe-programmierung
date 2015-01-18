
initialize:
	python scripts/initialize.py

build:
	pandoc -f markdown -t latex "systemnahe-programmierung.md" > "systemnahe-programmierung.tex"
	# Use listings.
	# sed -i -e 's/\\begin{verbatim}/\\begin{minipage}\{0\.95\\textwidth}\\begin{lstlisting}/g' "systemnahe-programmierung"}}.tex
	# sed -i -e 's/\\end{verbatim}/\\end{lstlisting}\\end{minipage}/g' "systemnahe-programmierung"}}.tex

	python scripts/apply_template.py -i "systemnahe-programmierung.tex" -o "systemnahe-programmierung.tex" -t latex.template

	python scripts/transform_img_eps.py

	latex -shell-escape "systemnahe-programmierung".tex
	bibtex "systemnahe-programmierung"
	latex -shell-escape "systemnahe-programmierung".tex
	latex -shell-escape "systemnahe-programmierung".tex
	pdflatex -shell-escape "systemnahe-programmierung".tex

debug:
	$(MAKE) clean
	$(MAKE) build
	xdg-open "systemnahe-programmierung.pdf" &
	$(MAKE) clean

publish:
	$(MAKE) build
	$(MAKE) clean   

clean:
	rm -f *.out *.aux *.dvi *.log *.blg *.bbl *.tex-e *.toc *.pyc