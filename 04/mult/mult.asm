// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

@R0
D=M
@n // Takes whatever is in register 0 and sets n to this value (should be in register 16)
M=D // n = R0

@R1
D=M
@i // Takes whatever is in register 1 and sets i to this value (register 17)
M=D // i = R1

@0
D=A
@total
M=D // Sets total to 0


(LOOP)
    @i 
    D=M // Selects i (the iterator)
    @STOP
    D;JEQ // If i = 0 then got to STOP.

    @n // Get the number currently stored in total and set it to D
    D=M
    @total // Get the value n (what we are adding together)
    M=D+M // Add n onto the current total.

    @i // Select the iterator
    M=M-1 // i = i - 1

    @LOOP
    0;JMP // Go to loop

(STOP)
    @total
    D=M
    @R2
    M=D // Sets RAM[2] = total

(END)
    @END
    0;JMP