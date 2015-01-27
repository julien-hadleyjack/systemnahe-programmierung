# Einleitung #

Systemnahe Programmierung beschäftigt sich mit der Erstellung beziehungsweise Programmierung von Software, die Teil des Betriebssystemes oder sehr eng mit diesem verbunden ist.

Die Software dient hierbei als Abstraktionsschicht zwischen Hardware und Betriebssystem, welche leichten Zugriff auf einfache Funktionen des Systems bietet. 
Gleichzeitig bietet die Schicht allerdings aus Sicherheitsgründen keinen direkten Zugriff auf das Betriebssystem, weshalb sich der Programmierer selbst um den Austausch von Daten kümmern muss. Gleichzeitig bedeutet dies, dass systemnahe Software fehleranfälliger und umständlicher ist. Was zunächst wie ein Nachteil erscheint, ist gleichzeitig jedoch auch ein Vorteil für die Software. Das Augenmerk des Programmierers muss somit nicht auf Funktionalität liegen sondern legt den Blickpunkt auf Werte wie Robustheit und Effizienz. 
Was wiederum die Entwicklung erschwert, da keine fehlertoleranten und schnellen Schnittstellen zur Verfügung stehen.

Systemnahe Software wird sehr oft in der Programmiersprache C geschrieben. Dies hat unter anderem den Grund, dass übersetzter C Code direkt auf einem Prozessor lauffähig ist und während der Laufzeit keine Überprüfung auf Programmierfehler oder Prüfungen der Datenzugriffe statt finden. Sämtliche Daten und Code lassen sich zudem sehr kompakt ablegen. 
Eine sehr wichtige Eigenschaft für systemnahe Programmierung, die Hardwarenähe durch direkten Zugriff auf Speicher und Register, wird durch C ebenfalls bereitgestellt. 
