from cs50 import get_string
import sys


def main():
    # First verify if there are two arguments
    if len(sys.argv) != 2:
        print("Usage: python caesar.py key")
        exit(1)

    else:
        # Declare argument variable as a converted string
        argument = int(sys.argv[1])
        plaintext = get_string("Plaintext: ")
        print("ciphertext:", end="")
        for n in range(len(plaintext)):
            if plaintext[n].isupper():
                # Convert string to int for math
                o = ((ord(plaintext[n]) - 65 + argument) % 26) + 65
                # Convert back to string for print statement
                print(chr(o), end="")

            elif plaintext[n].islower():
                o = ((ord(plaintext[n]) - 97 + argument) % 26) + 97
                print(chr(o), end="")
            # If non-letters are entered, don't convert them. Print as-is
            elif plaintext[n].isalpha() == False:
                print(plaintext[n], end="")
        print()
        exit(0)


if __name__ == "__main__":
    main()