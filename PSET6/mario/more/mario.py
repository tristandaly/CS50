from cs50 import get_int


def main():

    # Begin loop - continues until a number from 1-8 is entered
    while True:
        Height = get_int("Height: ")
        if Height >= 1 and Height <= 8:
            break
    # Based on height, spaces are added to the equivalent of height - 1, subtracting with each row from the top
    # Same rule applies to hash symbols, only one is added with each line
    # Double-space is added at the end of each pyramid-half (after hash is printed) before right side is printed with same formula
    for i in range(Height):
        print(" "*(Height-i-1), end="")
        print("#"*(i+1), end="")
        print("  ", end="")
        print("#"*(i+1))


if __name__ == "__main__":
    main()

