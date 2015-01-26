

initialize:
	python scripts/initialize.py

build:
	python scripts/apply_template.py template -i "chapters-latex" -t chapter-template.tex "special-generated/chapter-template.tex"

	for f in chapters-markdown/*.md; do \
		filename=`basename $$f .md`; \
		pandoc -f markdown --chapters --template special-generated/chapter-template.tex -t latex chapters-markdown/$$filename.md -o chapters-latex/$$filename.tex; \
	done
	# Use listings.
	# sed -i -e 's/\\begin{verbatim}/\\begin{minipage}\{0\.95\\textwidth}\\begin{lstlisting}/g' "systemnahe-programmierung"}}.tex
	# sed -i -e 's/\\end{verbatim}/\\end{lstlisting}\\end{minipage}/g' "systemnahe-programmierung"}}.tex

	python scripts/apply_template.py transform -i "chapters-latex"

	python scripts/apply_template.py template -i "chapters-latex" -t overview.tex "systemnahe-programmierung.tex" \
															 	  -t customsettings.sty "special-generated/customsettings.sty" \

	# python scripts/transform_img_eps.py

	latex -shell-escape -interaction=nonstopmode -halt-on-error -file-line-error "systemnahe-programmierung".tex > /dev/null 2>&1 || true
	bibtex "systemnahe-programmierung" || true
	latex -shell-escape -interaction=nonstopmode -halt-on-error -file-line-error "systemnahe-programmierung".tex > /dev/null 2>&1 || true
	latex -shell-escape -interaction=nonstopmode -halt-on-error -file-line-error "systemnahe-programmierung".tex > /dev/null 2>&1 || true
	pdflatex -shell-escape -interaction=nonstopmode -halt-on-error -file-line-error "systemnahe-programmierung".tex

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
