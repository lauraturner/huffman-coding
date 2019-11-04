import code_builder

#  Function to read in the file the user wants to decode (file name is user input from the cmd line)
def get_encoded_file():
    print("please type the full name of the file you want to decode. ex. test.txt")
    txt_file_name = input() 
    txt_file = open(txt_file_name, "r")
    return [txt_file.read(), txt_file_name]

#  Function used to decode the desired file and write the decoded file to a new .txt file
def decode_file(encoded_file_name, encoded_file, code):
    decoded_file_name = encoded_file_name.replace("_encoded.txt", "_decoded.txt") 
    decoded_file = open(decoded_file_name, "a")
    num_code = ""
    for num in encoded_file:
        num_code += num
        if num_code in code.keys():
            decoded_file.write(code[num_code])
            num_code = ""

# Main function to run the decoding module 
def main():
    code = code_builder.get_coding(True)
    encoded_file, encoded_file_name = get_encoded_file()
    decode_file(encoded_file_name, encoded_file, code)

if __name__== "__main__":
  main()