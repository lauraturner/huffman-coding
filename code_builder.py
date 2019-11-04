from collections import OrderedDict
import collections

def write_code_file(code):
    code_file_name = "code.txt"
    with open(code_file_name, 'w') as the_file:
        for ltr in code.keys():
            ltr_code = code[ltr][ : : -1]
            if ltr == '\n':
                ltr = r"\n"
            the_file.write(ltr + '\t' + "".join(ltr_code) + '\n')
    return code_file_name

def add_code(ltr1, ltr2, ltr_code):
    for ltr in ltr1[0]:
        ltr_code[ltr].append('1')
    for ltr in ltr2[0]:
        ltr_code[ltr].append('0')
    return ltr_code

def get_code(ltr_code, ltr_groups):
    if len(ltr_groups) == 1:
        return ltr_code
    ltr1 = ltr_groups.popitem()
    ltr2 = ltr_groups.popitem()
    ltr_code = add_code(ltr1, ltr2, ltr_code)  
    ltr_groups[ltr1[0] + ltr2[0]] = ltr1[1] + ltr2[1]
    ltr_groups = OrderedDict(sorted(ltr_groups.items(), key=lambda x: x[1], reverse=True))
    return get_code(ltr_code, ltr_groups)

def get_frequency(txt_file, asciiDict):
    for line in txt_file:
        for char in line:
            asciiDict[char] += 1
    sorted_ascii = sorted(asciiDict.items(), key=lambda kv: kv[1], reverse=True)
    asciiDict = collections.OrderedDict(sorted_ascii)
    return asciiDict

def get_code_file(file_name):
    asciiDict = {chr(i): 0 for i in range(32, 127)}
    asciiDict['\n'] = 0
    txt_file = open(file_name, "r")
    ltr_frequency = get_frequency(txt_file, asciiDict)
    ltr_code = {x: [] for x in ltr_frequency.keys()}
    code = get_code(ltr_code, ltr_frequency)
    code_file_name = write_code_file(code)
    return code_file_name
