MAIN_DOCUMENT=systemnahe-programmierung
max_print_line=1048576
ditaaEps?=$(where DitaaEps.jar)
ditaa?=$(where ditaa.jar)

.PHONY: default initialize build join word plain latex clean-all clean-bcf

default:  build

special-generated/chapter-template.tex: templates/chapter-template.tex
	@echo "Generating chapter template."
	@python3 scripts/apply_template.py template -i "chapters-markdown" -o "chapters-latex" -t chapter-template.tex "special-generated/chapter-template.tex"

.SECONDEXPANSION:
markdown_output=$(patsubst chapters-markdown/%.md,chapters-latex/%.tex, $(wildcard chapters-markdown/*.md))
$(markdown_output): special-generated/chapter-template.tex $$(patsubst chapters-latex/%.tex,chapters-markdown/%.md,$$@)
	-@filename=`basename $(@F) .tex`; \
	echo "Generating chapter: $$filename."; \
	pandoc --template special-generated/chapter-template.tex \
			-f markdown -t latex \
			--chapters \
			--biblatex \
			--columns=100 \
			--listings \
			chapters-markdown/$$filename.md -o chapters-latex/$$filename.tex;

eps_output=$(patsubst sources/%_ditaa.txt,images/%-eps-converted-to.pdf, $(wildcard sources/*_ditaa.txt))
$(eps_output): $$(patsubst images/%-eps-converted-to.pdf,images/%.eps,$$@)
	@filename=`basename $(@F) -eps-converted-to.pdf`; \
	echo "Generating image pdf: $$filename."; \
	epstopdf images/$$filename.eps --outfile=images/$$filename-eps-converted-to.pdf

transform: $(markdown_output)
	@echo "Transforming chapters."
	@python3 scripts/apply_template.py transform -o "chapters-latex"
	@touch transform

special_output = $(MAIN_DOCUMENT).tex special-generated/customsettings.sty special-generated/erklaerung.tex special-generated/sperrvermerk.tex
special_input = templates/overview.tex templates/customsettings.sty templates/erklaerung.tex templates/sperrvermerk.tex metadata.py $(markdown_output)
$(special_output): $(special_input)
	@echo Generating special pages.
	@python3 scripts/apply_template.py template -i "chapters-markdown" -o "chapters-latex" \
		-t overview.tex "${MAIN_DOCUMENT}.tex" \
		-t customsettings.sty "special-generated/customsettings.sty" \
		-t erklaerung.tex "special-generated/erklaerung.tex" \
		-t sperrvermerk.tex "special-generated/sperrvermerk.tex"

special = special/abstract.tex special/acronyms.tex special/glossary.tex
$(MAIN_DOCUMENT).pdf: transform $(special_output) $(eps_output) $(special) $(wildcard images/*)
	@echo Generating $(MAIN_DOCUMENT).pdf.
	@max_print_line=${max_print_line} latexmk
	@if [ -n "${pplatex}" ]; then \
		echo; echo; echo; \
		echo Formatting pdflatex output.; \
		${pplatex} --input $(MAIN_DOCUMENT).log; \
    fi

initialize:
	@echo Initializing project.
	@python3 scripts/initialize.py

join:
	@echo Joining markdown files.
	@awk 'FNR==1{print ""}1' chapters-markdown/*.md > "${MAIN_DOCUMENT}.md"

word: join
	@echo Creating word document.
	#@pandoc -f latex -t docx "${MAIN_DOCUMENT}.tex" -o "${MAIN_DOCUMENT}.docx" --default-image-extension=png --bibliography="references.bib"
	@pandoc -f markdown -t docx "${MAIN_DOCUMENT}.md" -o "${MAIN_DOCUMENT}.docx" --default-image-extension=png --bibliography="references.bib"

plain: join
	@echo Creating plain document.
	@pandoc -f markdown -t plain "${MAIN_DOCUMENT}.md" -o "${MAIN_DOCUMENT}.txt" --default-image-extension=png --bibliography="references.bib"

clean:
	@latexmk -c
	-rm chapters-latex/*.tex special-generated/*.tex
	
clean-all: clean
	-rm $(eps_output) $(images_output) ${MAIN_DOCUMENT}.md ${MAIN_DOCUMENT}.docx

clean-bcf:
	-rm $(MAIN_DOCUMENT).bcf

latex:
	@echo Generating $(MAIN_DOCUMENT).pdf.
	@max_print_line=${max_print_line} latexmk && test -n "${pplatex}" && echo; echo; echo; echo Formatting pdflatex output.; ${pplatex} --input $(MAIN_DOCUMENT).log;
	

build: $(MAIN_DOCUMENT).pdf
