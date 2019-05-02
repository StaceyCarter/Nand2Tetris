// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// pointer = points to the start of the screen array
// n = length of the array (8192 since screen is 32x256)
// i = counter

(LOOP)
    @8192 // Number of times we need to loop (ie length of screen array)
    D=A
    @n
    M=D // Stores 8192 in n (length of screen array or # of times we need to iterate)

    @0
    D=A
    @i
    M=D // Sets i to 0

    @16384
    D=A
    @pointer
    M=D // pointer stores the address of the first screen register

    @KBD 
    D=M // Assigns value stored in keyboard register
    @CLEAR
    D;JEQ // if keyboard value is 0 (no key is pressed) jump to CLEAR
    
    (COLOR)
    @i
    D=M
    @n
    D=D-M
    @END
    D;JEQ

    @pointer
    D=M
    @i
    A=D+M
    M=-1

    @i
    M=M+1 // Increment counter (i) by one.

    @COLOR
    0;JMP

    (CLEAR) //Runs same loop as COLOR, but instead sets screen value to 0
    @i
    D=M
    @n
    D=D-M
    @END
    D;JEQ

    @pointer
    D=M
    @i
    A=D+M
    M=0

    @i
    M=M+1 // Increment counter (i) by one.

    @CLEAR
    0;JMP


(END)
    @LOOP // Jump back to loop
    0;JMP