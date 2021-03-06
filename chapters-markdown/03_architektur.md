# Mikrocontroller-Architektur #

Bei der Intel 8051 Familie handelt es sich um einen 8-Bit Prozessorkern mit einem einheitlichen Befehlssatz. Es werden 128 Byte \ac{RAM} und 4096 Byte \ac{ROM} intern verbaut, wobei die Möglichkeit zum Anschluss von externem \ac{RAM} und \ac{ROM} besteht. Außerdem besitzt er 2 Timer und 4 8-bit \ac{I/O} Ports. Sie besitzt 2 externe Interrupt Quellen sowie 2 verschiedene Interrupt Prioritäten.

Als Datenspeicher dienen die 8 Register, aufgeteilt auf die 4 Registerbänke. Diese sind direkt über ihre Adresse oder als reguläres Register ansprechbar. Als Programmspeicher kann entweder der interne oder der externe Speicher verwendet werden.

Zur Ausführung eines Befehls benötigt der 8051 mindestens 12 Takte. Durch die Trennung von Befehls- und Datenspeicher ist die Harvard Architektur zu erkennen.
