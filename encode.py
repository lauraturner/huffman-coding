# To encode a .txt file
def encode_file(code, txt_file, file_name):
    new_file_name = file_name.replace(".txt", "_encoded.txt") 
    encoded_file = open(new_file_name, "a")
    txt_file = txt_file.read()
    for char in txt_file:
            encoded_file.write(code[char])

def get_coding(file_name):
    txt_file = open(file_name, "r")
    code = {}
    for line in txt_file:
        print(line)
        line = line.split('\t')
        if line[0] == '\\n':
            line[0] = '\n'
        code[line[0]] = line[1][:-1] 
    return code

file_name = 'test.txt'
code = get_coding(file_name)
txt_file_name = "File2ASCII.txt"
txt_file = open(txt_file_name, "r")
encode_file(code, txt_file, txt_file_name)
