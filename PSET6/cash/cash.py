from cs50 import get_float


def main():
    # If answer given is not a positive number, repeat prompt
    while True:
        answer = get_float("How much change is owed: ")
        if answer > 0:
            break
    # Break input out of decimal by rounding up
    answer = round(answer * 100)
    # This begins our initial count
    coins = 0
    # Subtract value of 25 from input and add 1 to coin counter. A quarter has been added
    while answer > 0:
        if answer >= 25:
            answer -= 25
            coins += 1
        # Do the same for dimes - pennies. As long as the total is at least 10 cents (etc) you can add one more coin to the final print statement
        elif answer >= 10:
            answer -= 10
            coins += 1

        elif answer >= 5:
            answer -= 5
            coins += 1

        elif answer >= 1:
            answer -= 1
            coins += 1

    # Print final coin count
    print(coins)


if __name__ == "__main__":
    main()