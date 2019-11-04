import code_builder
import encode
import decode

def main():
    for i in range(1, 4):
        num_collection = str(i)
        code_builder.main(num_collection)
        encode.main(num_collection)
        decode.main(num_collection)

if __name__== "__main__":
  main()