import code_builder
import os

# Function to encode the desiered .txt file with the generated Huffman code
def write_encoded_file(code, txt_files, num_collection):
    file_path = ".\\Collection " + num_collection + "\\Encoded"
    print("the following files are encoded and saved in " + file_path)
    for txt_file in txt_files:
        new_file_name = txt_file['name'].replace(".txt", "_encoded.txt") 
        encoded_file = open(file_path + "\\" + new_file_name, "a")
        for line in txt_file['txt']:
            for char in line:
                encoded_file.write(code[char])
        print(new_file_name)
    print("\n")

# Main function to run the encoding module
def main(num_collection):
    data_path = ".\\Data 20191031" 
    code = code_builder.get_coding(False, num_collection)
    txt_files = []
    for filename in os.listdir(data_path):
        file_path = data_path + "\\" + filename
        txt_files.append({'txt': open(file_path, "r"), 'name': filename})
    write_encoded_file(code, txt_files, num_collection)
    
