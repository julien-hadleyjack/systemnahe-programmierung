# coding=utf-8

###############################################################################
# 
#    General Options, Layout
#
###############################################################################

font_size = "12pt"  # Allowed: 8pt, 9pt, 10pt, 11pt, 12pt, 14pt, 17pt, 20pt
language = "german" # options: german, english
font_type = "palatino" # options: palatino, goudysans, lmodern, libertine
toc_depth = 2

# Layout, as strings with specified metric unit.
top_margin, bot_margin, left_margin, right_margin = "2.5cm", "2.5cm", "2.5cm", "2.5cm"

column_spacing = "10pt"
row_spacing = "1.5" 



###############################################################################
# 
#    Custom Packages
#
###############################################################################

"""
Examples:
rotating (Paket um Textteile drehen zu können)
lscape (Paket um Seite im Querformat anzuzeigen)
"""

# Format: {"biblatex": ["backend=biber", "style=alphabetic"], "rotating": []}
custom_packages = {}



###############################################################################
# 
#    Bibliography
#
###############################################################################
# Bibliography.
bib_files = ["references.bib"]
# http://ctan.mirrorcatalogs.com/macros/latex/contrib/biblatex/doc/biblatex.pdf
bibliography_style = "numeric"
sorting_style = None # "none"
autocite = "inline" #footnote


###############################################################################
# 
#    Minted
#
###############################################################################
# other options: "linenos", "numberblanklines=false", "style=bw"
minted_default = ["frame=lines", "breaklines=true", "xleftmargin=30pt", "xrightmargin=30pt", "framesep=5pt", "fontsize=\\footnotesize"]
print_document = False

###############################################################################
# 
#    Title Page
#
###############################################################################

title = "Systemnahe Programmierung"
authors = ["Julien Hadley Jack", "Sebastian Dernbach"]
date = r"\today"

###############################################################################
# 
#    Text Snippets For Translation
#
###############################################################################
deutsch = {"language": "german",
			"deckblattabschlusshinleitung": "für die Prüfung zum",
			"artikelstudiengang": "der",
			"anderdh": "an der Dualen Hochschule Baden-Württemberg",
			"von": "von",
			"dbbearbeitungszeit": "Bearbeitungszeitraum",
			"dbmatriknr": "Matrikelnummer",
			"dbkurs": "Kurs",
			"dbfirma": "Ausbildungsfirma",
			"dbbetreuer": "Betreuer",
			"dbgutachter": "Gutachter",
			"sperrvermerk": "Sperrvermerk",
			"erklaerung": "Erklärung",
			"abkverz": "Abkürzungsverzeichnis",
			"glossar": "Glossar"}

english = {"language": "english",
			"deckblattabschlusshinleitung": "for the}",
			"artikelstudiengang": "at",
			"anderdh": "at the Cooperative State University",
			"von": "by",
			"dbbearbeitungszeit": "Time of Project",
			"dbmatriknr": "Student ID",
			"dbkurs": "Course",
			"dbfirma": "Company",
			"dbbetreuer": "Supervisor in the Company",
			"dbgutachter": "Reviewer",
			"sperrvermerk": "Restriction Notice",
			"erklaerung": "Author's declaration",
			"abkverz": "Acronyms",
			"glossar": "Glossar"}

snippets = deutsch
