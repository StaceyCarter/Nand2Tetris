from hackAssembler import readFile

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


def first_pass(file):
    no_whiteSpace = []
    with open(file) as open_file:
        for line in open_file:
            line = line.strip()
            if "//" in line:
                index = line.index("//")
                line = line[:index].strip()
            if line != "" and line[0] != "/":
                no_whiteSpace.append(line)
    return no_whiteSpace
                
def convertLabels(arr):
    """Add the labels to the symbol table for look up and delete them from the instruction list"""
    no_labels = []
    labels_seen = 0
    for index, instruction in enumerate(arr):
        if instruction[0] == "(":
            SYMBOL_TABLE[instruction[1:-1]] = index - labels_seen
            labels_seen += 1
        else:
            no_labels.append(instruction)
    return no_labels

def addVariables(arr):
    """Add the variables to the Symbol table."""
    n = 16
    for instruction in arr:
        if instruction[0] == "@" and instruction[1:] not in SYMBOL_TABLE and not instruction[1:].isdigit():
            SYMBOL_TABLE[instruction[1:]] = n
            n += 1


def secondPass(arr):
    instruction_file = open("Symbols.asm", "w")
    for instruction in arr:
        if instruction[0] == "@":
            if instruction[1:].isdigit():
                result = instruction[1:]
            else:
                result = SYMBOL_TABLE[instruction[1:]]
            instruction_file.write("@" + str(result) + "\n")
        else:
            instruction_file.write(str(instruction) + "\n")

    instruction_file.close()

        

array_of_instructions = first_pass("Pong.asm") # Remove comments and white space

array_instructions_clean = convertLabels(array_of_instructions) # Remove labels and add them to the symbol table

addVariables(array_instructions_clean)

secondPass(array_instructions_clean)

readFile("Symbols.asm", "Pong.hack")



