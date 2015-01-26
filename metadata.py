# coding=utf-8

# Global settings.
document_class = "ext" + "article"  # Ext is for extsizes package.
font_size = "12pt"  # Allowed: 8pt, 9pt, 10pt, 11pt, 12pt, 14pt, 17pt, 20pt
language = "de" # options: de, en
font_type = "palatino" # options: palatino, goudysans, lmodern, libertine
bib_files = ["references.bib"]


"""
Packages. Examples:
rotating (Paket um Textteile drehen zu können)
lscape (Paket um Seite im Querformat anzuzeigen)
amsmath, amssymb (Mathematikpakete benutzen)
"""
custom_packages = []


toc_depth = 2


# Bibliography.
bibliography_style = "ieeetr"  # Set to 'ieeetr' for ordered bibliography.
put_bibliography_on_new_page = True


# Layout, as strings with specified metric unit.
top_margin = "2.5cm"
bot_margin = top_margin
left_margin = top_margin
right_margin = left_margin

column_spacing = "10pt"
row_spacing = "1.5" 

# Front page.
## Setting title to None also ignores authors and date.
title = "Systemnahe Programmierung"
authors = ["Julien Hadley Jack", "Sebastian Dernbach"]
date = r"\today"

# Sprache
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
