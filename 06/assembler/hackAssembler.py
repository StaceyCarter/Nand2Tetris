import sys

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

# input_file = sys.argv[0]

def readFile(file):
    """ Open file and read in contents line by line, ignoring white space and comments.

    Depending on if each line is an A or a C instruction, handle converting it into a binary number.
    """
    with open(file) as open_file:
        for line in open_file:
            line = line.strip()
            if "//" in line:
                index = line.index("//")
                line = line[:index].strip()
            if line != "" and line[0] != "/":
                if line[0] == "@":
                    handleA(line[1:])
                else:
                    handleC(line)

def handleA(line):
    """ Handle an A instruction

    Convert the given number to binary 16 bit representation. Always starts with a 0 for A instructions.
    Parameters:
    line = String of numbers

    Output:
    String - binary representation of input number
    """
    #convertToBinary(num) !!!
    pass

def handleC(line):
    """ Handle C (computation) instruction.

    Break down the instruction string into its separate components and assign binary strings to represent each component.
    Concatenate all binary components together at the end as the result.

    Parameters:
        line (String) = represents instructions of what to do
    
    Output:
        String - binary representation of the instruction to complete.
    """
    pass

def convertToBinary(num):
    binary = []
    while num > 0:
        binary.append(str(num % 2))
        num = num // 2
    binary.reverse()
    return "".join(binary)



            
            


           

readFile("Add.asm")

# if __name__ == "__main__":
    
    