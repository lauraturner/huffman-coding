import code_builder

# Function to encode the desiered .txt file with the generated Huffman code
def write_encoded_file(code, txt_file, file_name):
    new_file_name = file_name.replace(".txt", "_encoded.txt") 
    encoded_file = open(new_file_name, "a")
    txt_file = txt_file.read()
    for char in txt_file:
            encoded_file.write(code[char])
    return new_file_name


# Main function to run the encoding module
def main():
    code = code_builder.get_coding(False)
    print("please type the full name of the file you want to encode. ex. test.txt")
    txt_file_name = input() 
    txt_file = open(txt_file_name, "r")
    encoded_file_name = write_encoded_file(code, txt_file, txt_file_name)
    print("The encoded file is called:\t" + encoded_file_name)

if __name__== "__main__":
  main()