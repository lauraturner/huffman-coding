import code_builder

def write_encoded_file(code, txt_file, file_name):
    new_file_name = file_name.replace(".txt", "_encoded.txt") 
    encoded_file = open(new_file_name, "a")
    txt_file = txt_file.read()
    for char in txt_file:
            encoded_file.write(code[char])
    return new_file_name

def get_coding():
    code_file_name = code_builder.get_code_file("File1ASCII.txt")
    txt_file = open(code_file_name, "r")
    code = {}
    for line in txt_file:
        line = line.split('\t')
        if line[0] == '\\n':
            line[0] = '\n'
        code[line[0]] = line[1][:-1] 
    return code

code = get_coding()
print("please type the full name of the file you want to encode. ex. test.txt")
txt_file_name = input() 
txt_file = open(txt_file_name, "r")
encoded_file_name = write_encoded_file(code, txt_file, txt_file_name)
print(encoded_file_name)
