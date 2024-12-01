inc -> Add 1
dec -> Minus 1

```asm
inc AH // Add 1 to AH value
	inc word [a] // Add 1 to the value in memory

dec AH

ADD AH, 5h // AH += 5
SUB AX, 10h
```

mul -> Takes that is 8 or 16 bit which decides the multiplier
mul DH -> Multiplied by AL -> Value will be 16 bit and saved in AX
mul DX -> Multiplied by AX -> Value wil be saved in = DX, AX (32 bit)

div BL -> AX / BL -> Number saved in AL, remainder saved in AH
div BX -> DX:AX / BX -> Number saved in AX, remainder saved in DX