Memory can be thought of as an array filled with bytes

Directive (Etyketi)
db (define byte) -> Every element will be one byte and stored one after the other
dw (define word) -> Will be stored as two bytes (33 stored as 003)
dd (define doubleword) -> Will be stored as four bytes

tekst db 33h, 55h, 30h -> Store the numbers in memory

mov AX, tekst -> Store pointer
mov BX, \[tekst] -> Store value of pointer
mov CH, \[tekst] -> Since it's only an 8bit registry the value returned will only be 8 bits

mov AL, \[BX] -> Can only be BX inside
mov BX, tekst+2 -> Gets the third byte of tekst
mov AL, \[BX + 2] -> Same as above

mov byte \[tekst], 'a' -> Place 'a' into memory (have to specify size) into first slot
mov byte \[BX], '$' -> Place $ at at the address of BX