Open up Dosbox-Options to open dosbox.conf

# CPU
AX, BX, CX, DX -> 4 Registries that are 16bits
Each registry is split into two registries AH, AL etc (A High, A Low)
Each mini-registry is 8bits

# DOS
help to find commands
Files can't be longer than 8 characters (aside from extension)

To assemble -> nasm file_name -o file_name.com
Also to assemble nasm -o file_name.com file_name.asm
# RAM
There's milions of cells that each hold one byte of data and an adress 01, 02 etc

- h / 0x means base 16
# Assembler Commands
org 100h -> Move all RAM instructions from 100 not (h means 16bit)
# Debugging
insight file.com
Ctrl - F4 to reset
F1 - Help
F8 - Continue (move on)