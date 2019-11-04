import collections
from collections import OrderedDict

# function to be used by encoding and decoding modules to get a dict of the Huffman Code.
# The decode flag is used to switch the bit code to be the dict keys and the characters to be the 
# values for decoding 
def get_coding(decode):
    code_file_name = "code.txt"
    txt_file = open(code_file_name, "r")
    code = {}
    for line in txt_file:
        line = line.split('\t')
        if line[0] == '\\n':
            line[0] = '\n'
        if decode:
            code[line[1][:-1]] = line[0]
        else:   
            code[line[0]] = line[1][:-1] 
    return code

# Function to format and write the generated Huffman Coding key to a txt file called code.txt
def write_code_file(code):
    code_file_name = "code.txt"
    with open(code_file_name, 'w') as the_file:
        for ltr in code.keys():
            ltr_code = code[ltr][ : : -1]
            if ltr == '\n':
                ltr = r"\n"
            the_file.write(ltr + '\t' + "".join(ltr_code) + '\n')
    return code_file_name

# function used to add bit encoding to each character as the Huffman Coding Tree is created
def add_code(ltr1, ltr2, ltr_code):
    for ltr in ltr1[0]:
        ltr_code[ltr].append('1')
    for ltr in ltr2[0]:
        ltr_code[ltr].append('0')
    return ltr_code

# Recursicve function to find the bit codes of each character using the Huffman Coding algorithm 
def make_code(ltr_code, ltr_groups):
    if len(ltr_groups) == 1:
        return ltr_code
    ltr1 = ltr_groups.popitem()
    ltr2 = ltr_groups.popitem()
    ltr_code = add_code(ltr1, ltr2, ltr_code)  
    ltr_groups[ltr1[0] + ltr2[0]] = ltr1[1] + ltr2[1]
    ltr_groups = OrderedDict(sorted(ltr_groups.items(), key=lambda x: x[1], reverse=True))
    return make_code(ltr_code, ltr_groups)

# Function to read characters from a file and calclate their frequency in a dict
def get_frequency(txt_file, asciiDict):
    for line in txt_file:
        for char in line:
            asciiDict[char] += 1
    sorted_ascii = sorted(asciiDict.items(), key=lambda kv: kv[1], reverse=True)
    asciiDict = collections.OrderedDict(sorted_ascii)
    return asciiDict

# Main function to get the Huffman Coding
def main():
    # Create a dict of ASCII characters and add in the LF character
    asciiDict = {chr(i): 0 for i in range(32, 127)}
    asciiDict['\n'] = 0
    txt_file = open("File1ASCII.txt", "r")
    ltr_frequency = get_frequency(txt_file, asciiDict)
    # make new dict to hole the bit code for each character
    ltr_code = {x: [] for x in ltr_frequency.keys()}
    code = make_code(ltr_code, ltr_frequency)
    code_file_name = write_code_file(code)
    return code_file_name


if __name__== "__main__":
  main()