```
push 0xFFFF // Push value
push AX // Push registry (only 16b)
push word [a] // a has to be a dw (define word), 2byte

pop AX // Send value into AX, can only be 16b
pop word [y] // 

Registry SP // Points to address at top of stack, moves down as you add FFFD -> FFFC
pusha // Place all registries in stack
popa // Place stack in registries
```

Stacks start at FFFE and address goes down
