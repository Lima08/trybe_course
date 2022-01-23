import sys

#  Passamos argumentos na hora da chamada pela linha de comando com:
# >>  python3 example_input_sys.py 2 4 "teste"

if __name__ == "__main__":
    for argument in sys.argv:
        print("Received -> ", argument)