# Entwicklungsumgebung #

Zur Entwicklung wird die MCU 8051 IDE eingesetzt, welche für Windows und Linux kostenlos zum Download zur Verfügung steht. Neben den beiden unterstützten Sprachen C und Assemblar bietet die IDE einen Simulator um eine Programmierung ohne reele Hardware zu ermöglichen. 

![MCU 8051 IDE](images/mcu8051ide_screenshot.png "Übersicht der MCU 8051 IDE")

![MCU 8051 IDE Editor](images/ide-editor.png "Code Editor der MCU 8051 IDE") Zentrales Element der IDE ist der Code Editor, welcher mit üblichen aber auch zusätzlichen Features aufwartet. Er bietet Funktionen wie Syntax Highlighting, Vervollständigung der Befehle während des Tippens, Überprüfung der Code Syntax und der Rechtschreibung in Kommentaren. Neben der Anzeige von Zeilennummern, Lesezeichen und Haltemarken ist es möglich den Code als XHTML oder LaTeX Dokument zu exportieren.

Im unteren Bereich der IDE ist der Simulator untergebracht. Er virtualisiert einen gewählten Microcontroller und gibt dem Benutzer die Möglichkeit genau zu erkennen, wie sich die Kompenenten verhalten, nachdem z.B. der Wert des Registers verändert wird. So wird es möglich bestimmte Fehler im Programm zu finden, was mit reeler Hardware nahezu unmöglich wäre. Der Benutzer hat darüber hinaus die Möglichkeit jegliche Speicher zu editieren und das Verhalten direkt zu beobachten. Ein Abbild des laufenden Programms kann außerdem in einer Datei gespeichert werden und zu einem späteren Zeitpunkt fortgesetzt werden.

Die IDE kann zudem die geöffneten Source Code Dateien samt Konfigurationsparameter in einer XML Datei speichern. Der integrierte wissenschaftliche Rechner bietet unter anderem die Umrechnung von Zahlen zwischen Hexadezimal, Dezimal, Oktal und Binär Zahlensystemen. Rohdaten können direkt im integrierten Hexadezimal Editor bearbeitet werden. Assemblarcode kann mit dem Disassembler wieder zurück in Source Code verwandelt werden. 


