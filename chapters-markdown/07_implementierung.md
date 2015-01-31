
# Implementierung #

![Konfiguration des Nummernfeldes](images/keypad-screenshot)

Als erstes muss die Matrix-Keypad der IDE richtig konfiguriert werden. Im Bild kann man sehen, dass es auf Port 1 erreichbar ist. Die Einstellungen können auch importiert werden:
<!--
````
# MCU 8051 IDE: Virtual HW component configuration file
# Project: AlarmKeypadLogin
# Component: Matrix Keypad

MatrixKeyPad {{4 1 0 1 5 1 1 1 6 1 2 1 7 - 3 -} {4 4 0 7 5 3 1 6 6 2 2 5 7 - 3 -} {} {} {0 0 1 0 2 0 3 0 4 0 5 0 6 0 7 0 8 0 9 0 10 0 11 0 12 0 13 0 14 0 15 0} 1 1}
````
-->

````nasm
keypad  equ P1              ;Matrix keypad
col1    equ keypad.3            ;Column 1
col2    equ keypad.4            ;Column 2
col3    equ keypad.5            ;Column 3

value   equ 30H             ;Value of pressed button
pressed bit 00H             ;Was the button just pressed?
secure_mode bit 01h         ;Is the user logiged in?
````

Zusätzlich werden auch noch drei Variablen definiert:
* **Value**: Wert der gedrückten Taste
* **pressed**: Ob schon eine Taste gedrückt wurde (wird zurückgesetzt, wenn auf ein neuen Tastendruck gewartet wird)
* **secure_mode**: In welchem Zustand die Alarmsicherung ist (0 für ausgeschaltet, 1 für angeschaltet)


````nasm
get_button:
    clr pressed

    ;Check first row
    mov value,#1            ;Start value is first number on row
    mov keypad, #11111110B      ;Mark first row
    acall check_col1        ;Check all columns 

    ; If button was pressed in row, jump out of function
    jb pressed, found_button    
 
    mov value,#4
    mov keypad, #11111101B
    acall check_col1
 
    jb pressed, found_button
 
    mov value,#7
    mov keypad, #11111011B
    acall check_col1
 
    jb pressed, found_button

    jmp get_button
````

Die Zeilen des Nummernfeldes werden nacheinander überprüft. Dabei wird zuerst `value` auf den Wert der ersten Taste aus der Reihe gesetzt. Danach werden alle Reihen außer die ausgewählte auf `1` gesetzt und zur Funktion `check_col1` gesprungen, die die Spaltenüberprüfung für die ausgewählte Reihe startet. Nach jeder Reihe wird überprüft, ob schon eine Taste gedrückt wird. Ist dies der Fall, dann wird aus der Funktion gesprungen. Wenn alle Reihen überprüft worden sind und kein Tastendruck erkannt wurde, dann wird die Überprüfung wieder von vorne angefangen.

````nasm
check_col1:
    ;If button wasn't pressed, jump to next colum
    jb col1, check_col2

    ;If button was pressed, wait for end of button press
    jnb col1,$

    ;Set bit that key was pressed
    setb pressed
    ret
````

Wenn in der ersten Spalte kein Tastendruck entdeckt worden ist, wird zu `check_col2` gesprungen, die die nächste Spalte überprüft. Sollte die Taste aber gedrückt sein, dass muss auf das Ende des Tastendruckes gewartet werden. Dafür wird einfach zur Zeile der Überprüfung gesprungen.

````nasm
check_col2:
    jb col2, check_col3
    jnb col2,$
    inc value           ;Increment the start value from row
    setb pressed
    ret
````

In der nächsten Spalte wird ähnlich vorgangen. Der Unterstied ist, dass wenn ein Tastendruck entdeckt wurde, `value` um den Unterschied der Tastenwerte inkrementiert wird (in diesem Fall 1).

````nasm
check_pin:
    ;Check first pin (4)
    acall get_button
    mov A, value
    cjne A, #4, check_pin

    ;Check second pin (2)
    acall get_button
    mov A, value
    cjne A, #2, check_pin

    ;Check third pin (6)
    acall get_button
    mov A, value
    cjne A, #6, check_pin

    ;Check fourth pin (8)
    acall get_button
    mov A, value
    cjne A, #8, check_pin

    ;Toggle secure mode of the system
    cpl secure_mode
````

Die Hauptfunktion ist `check_pin`. Sie ruft viermal die `get_button`-Funktion auf und überprüft, ob der gelieferte Tastendruck dem gewünschtem gleicht. Sollte dies einmal nicht der Fall sein, dann wird die Suche von vorne angefangen. Aber wurde die Ziffernfolge erfolgreich eingegeben, dann wird der Alarm-Modus gewechselt.
