
# Befehlssatz #

| Befehl     | Beschreibung                                     |
|------------|--------------------------------------------------|
| `ACALL <addr11>` | Ruft die Subroutine an der Adresse `<addr11>` auf |
| `ADD <A>,<Operand>` | Addiert den `<Operand>` zum Inhalt des Akkumulators `<A>` hinzu |
| `ADDC <A>,<Operand>` | Addiert den `<Operand>` und das Übertragsbit zum Inhalt des Akkumulators `<A>` hinzu |
| `AJMP <addr11>` | Springt zu Adresse `<addr11>` |
| `ANL <Zielbyte>,<Quellenbyte>` | Speichert eine bitweise logische UND-Verknüpfung zwischen dem `<Zielbyte>` und dem `<Quellenbyte>` im `<Zielbyte>` | 
| `CJNE <Operand1>,<Operand2>,<rel>` | Springe zu `<rel>` falls die Werte `<Operand1>` und `<Operand2>` ungleich sind |
| `CLR <bit>,<A>` | Löscht das Bit `<bit>` bzw. den Akkumulator `<A>` |
| `CPL <bit>,<A>` | Komplementiert das Bit `<bit>` bzw. den Akkumulator `<A>` |
| `DA <A>` | Korrigiere den Dezimalwert des Akkumulators `<A>` nach einer Addition |
| `DEC <byte>` | Dekrementiere `<byte>` um 1 |
| `DIV <A>,<B>` | Dividiere Akkumulator `<A>` durch Register `<B>` |
| `DJNZ <byte>,<rel>` | Dekrementiere `<byte>` um 1 und springe zu `<rel>` wenn das `<byte>` nicht Null ist |
| `INC <byte>/<DPTR>` | Inkrementiere `<byte>` bzw. `<DPTR>` um 1 |
| `JB <bit>,<rel>` | Springe zu `<rel>`, wenn `<byte>` gesetzt ist (=1) |
| `JBC <bit>,<rel>` | Springe zu `<rel>`, wenn `<byte>` gesetzt ist (=1) und lösche dieses anschließend |
| `JC <rel>` | Springe zu `<rel>`, wenn das Übertragsbit gesetzt ist (=1) |
| `JMP <A>+<DPTR>` | Addiere den Akkumulator `<A>` zum Datenanzeiger `<DPTR>` und lade das Ergebnis in den Programmzähler |
| `JNB <bit>,<rel>` | Springe zu `<rel>`, wenn `<byte>` nicht gesetzt ist (=0) |
| `JNC <rel>` | Springe zu `<rel>`, wenn das Übertragsbit nicht gesetzt ist (=0) |
| `JNZ <rel>` | Springe zu `<rel>`, wenn der Akkumulator nicht Null ist |
| `JZ <rel>` | Springe zu `<rel>`, wenn der Akkumulator Null ist |
| `LCALL <addr16>` | Ruft bedingungslos Subroutine an der Adresse `<addr16>` auf |


