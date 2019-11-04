
def get_coding(file_name):
    txt_file = open(file_name, "r")
    code = {}
    for line in txt_file:
        line = line.split('\t')
        if line[0] == '\\n':
            line[0] = '\n'
        code["".join(line[1][:-1])] = line[0]
    return code

code_file_name = 'test.txt'
code = get_coding(code_file_name)
text_file_name = "File2ASCII_encoded.txt"
txt_file = open(text_file_name, "r")
txt_file = txt_file.read()
decodes_file_name = text_file_name.replace("_encoded.txt", "_decoded.txt") 
decoded_file = open(decodes_file_name, "a")
num_code = ""
for num in txt_file:
    num_code += num
    if num_code in code.keys():
        decoded_file.write(code[num_code])
        num_code = ""

