import sys
from tables import comp, dest, jump

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
                    result = handleA(line[1:]) # Returns the binary conversion padded with 0s to 16 bits, msb is always 0.
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
    binary_num = '0' + convertToBinary(int(line)).zfill(15)
    return binary_num

def handleC(line):
    """ Handle C (computation) instruction.

    Break down the instruction string into its separate components and assign binary strings to represent each component.
    Concatenate all binary components together at the end as the result.

    Parameters:
        line (String) = represents instructions of what to do
    
    Output:
        String - binary representation of the instruction to complete.

    Examples:

        >>> handleC("D=D+M")
        '1111000010010000'

        >>> handleC("D;JLE")
        '1110001100000110'

        >>> handleC("D ; JLE")
        '1110001100000110'

        >>> handleC("D = D+M")
        '1111000010010000'

        >>> handleC("D=D+M;JEQ")
        '1111000010010010'

    """

    instructions = {
        'jump' : None,
        'dest' : None,
        'comp' : None
    }

    if ";" in line:
        index = line.index(";")
        instructions['jump'] = line[index+1:].strip()
        instructions['comp'] = line[:index].strip()

    if "=" in line:
        index = line.index("=")
        instructions['dest'] = line[:index].strip()
        instructions['comp'] = line[index+1:].strip()
    
    if "=" in line and ";" in line:
        indexE = line.index("=")
        indexS = line.index(";")
        instructions['comp'] = line[indexE+1:indexS].strip()

    cInstruction = "111"

    comp_binary = comp[instructions['comp']]
    dest_binary = dest[instructions['dest']]
    jump_binary = jump[instructions['jump']]
    
    return "111" + comp_binary + dest_binary + jump_binary
    

def convertToBinary(num):
    binary = []
    while num > 0:
        binary.append(str(num % 2))
        num = num // 2
    binary.reverse()
    return "".join(binary)



            
            


           

readFile("Add.asm")

if __name__ == "__main__":
    from doctest import testmod
    if testmod().failed == 0:
        print("Success!")
    
    