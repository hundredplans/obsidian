	```
jmp place
mov DX, 'j' ; Ignored
int 21h

place:
mov AH, 00h
int 21h
```
cmp AL, 5 ; Checks if AL is == 5 by settings flags
; Jump if
jg koniec ; >
jl koniec ; <
jge koniec ; >=
jle koniec ; <=
je koniec ; ==
jne koniec ; !=
```