# Projektarbeit für Systemnahe Programmierung

In der Vorlesung Systemnahe Programmierung von der Dualen Hochschule Karlsruhe haben wir uns mit dem Mikrocontroller 8051 beschäft. Zum Schluss der Vorlesung mussten alle in Gruppenarbeit ein Projekt machen. Die schriftliche Arbeit dazu sollte zusätzlich eine Einleitung in den Mikrocontroller und die uns zur Verfügung gestellte Entwicklungsumgebung geben. 

In dem vorliegendem Projekt haben wir uns für die Implemntierung einer Alarmsicherung entschieden. Über ein Nummernfeld konnte eine PIN eingeben werden, um den Alarmmodus an- und auszuschalten.

# Resultat

Das Endprodukt kann [hier](https://github.com/julien-hadleyjack/systemnahe-programmierung/releases/download/final/systemnahe-programmierung.pdf) heruntergeladen werden.

# Bauen

Um das Projekt selbst zu bauen, brauchst du:

* LaTeX mit Latexmk
* Pandoc
* Minted
* Python mit jinja2 und docopt

Dann musst du nur noch 

```
make
````

ausführen und die PDF-Datei wird generiert.