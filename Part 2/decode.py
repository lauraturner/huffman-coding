import code_builder
import os

#  Function to read in the file the user wants to decode (file name is user input from the cmd line)
def get_encoded_file(num_collection):
    encoded_files_path = ".\\Collection " + num_collection + "\\Encoded"
    encoded_files = []
    for filename in os.listdir(encoded_files_path):
        file_path = encoded_files_path + "\\" + filename
        encoded_files.append({'txt': open(file_path, "r"), 'name': filename})
    return encoded_files

#  Function used to decode the desired file and write the decoded file to a new .txt file
def decode_file(encoded_files, code, num_collection):
    file_path = ".\\Collection " + num_collection + "\\Decoded"
    print("the following files are decoded and saved in " + file_path)
    decoded_files_path = ".\\Collection " + num_collection + "\\Decoded" 
    for encoded_file in encoded_files:
        decoded_file_name = encoded_file['name'].replace("_encoded.txt", "_decoded.txt")
        decoded_file = open(decoded_files_path + "\\" + decoded_file_name, "a")
        huff_code = ""
        for line in encoded_file['txt']:
            for num in line:
                huff_code += num
                if huff_code in code.keys():
                    decoded_file.write(code[huff_code])
                    huff_code = ""
        print(decoded_file_name)
    print("\n")

# Main function to run the decoding module 
def main(num_collection):
    code = code_builder.get_coding(True, num_collection)
    encoded_files = get_encoded_file(num_collection)
    decode_file(encoded_files, code, num_collection)
