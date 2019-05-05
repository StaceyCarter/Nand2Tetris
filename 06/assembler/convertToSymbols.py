SYMBOL_TABLE = {
    'SP' : 0,
    'LCL' : 1,
    'ARG' : 2,
    'THIS' : 3,
    'THAT' : 4,
    'R0' : 0,
    'R1' : 1,
    'R2' : 2,
    'R3' : 3,
    'R4' : 4,
    'R5' : 5,
    'R6' : 6,
    'R7' : 7,
    'R8' : 8,
    'R9' : 9,
    'R10' : 10,
    'R11' : 11,
    'R12' : 12,
    'R13' : 13,
    'R14' : 14,
    'R15' : 15,
    'SCREEN' : 16384,
    'KBD' : 24576
}

def readFile(file):
    """ Open file and read in contents line by line, translate all the contents into something readable by the assembler.

    >>> readFile("Max.asm")
    @0
    D=M
    @1
    D=D-M 
    @11
    D;JGT           
    @1
    D=M              
    @13no_
    0;JMP            
    @0             
    D=M              
    @R2
    M=D              
    @17
    0;JMP
    """
    # binaryFile = open("symbols", "a")
    pass

no_whiteSpace = []

def first_pass(file):
    with open(file) as open_file:
        for line in open_file:
            line = line.strip()
            if "//" in line:
                index = line.index("//")
                line = line[:index].strip()
            if line != "" and line[0] != "/":
                no_whiteSpace.append(line)
                
def convertLabels(arr):
    """Add the labels to the symbol table for look up and delete them from the instruction list"""
    for index, instruction in enumerate(arr):
        if instruction[0] == "(":
            SYMBOL_TABLE[instruction[1:-1]] = index + 1
            no_whiteSpace.pop(index)

def addVariables(arr):
    """Add the variables to the Symbol table."""
    n = 16
    for instruction in arr:
        if instruction[0] == "@" and instruction[1:] not in SYMBOL_TABLE:
            SYMBOL_TABLE[instruction[1:]] = n
            n += 1

def secondPass()

        

first_pass("Max.asm") # Remove comments and white space

convertLabels(no_whiteSpace) # Remove labels and add them to the symbol table

addVariables(no_whiteSpace)