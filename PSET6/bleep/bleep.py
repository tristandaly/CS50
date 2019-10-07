from cs50 import get_string
import sys


def main():
    # Variable 'words' scans and adds words found in the 2nd argument (txt file) and removes whitespace with strip function
    words = set(line.strip() for line in open(sys.argv[1]))
    # Needs arguments to run. If not, program exits
    if (len(sys.argv) != 2):
        exit(1)

    else:
        message = get_string("Provide a message: ")
        # Seprates all words surrounded by whitespace and re-splits them with a single space
        mess = message.split(" ")
    # Iterates over words in input
    for word in mess:
        # If lowercase version of word (unit of string in message) appears in txt file
        if word.lower() in words:
            # Print asterisk over the length of the word(s) found
            print("*"*len(word), end=" ")
        else:
            print(word, end=" ")

    print()


if __name__ == "__main__":
    main()