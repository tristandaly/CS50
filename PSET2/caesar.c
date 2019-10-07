#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
// Declare that arguments may be used in Main
int main(int argc, string argv[])
{   
    // If no arguments are used, then Print Error and signal it with return 1 
    if (argc != 2)
    {
        printf("WRONG!\n");
        return 1;
    }
    // Declare variables for argument's conversion to integer and its length
    int argument = atoi(argv[1]);
    int argLength = strlen(argv[1]);
    bool isInt = true;
    // Returns error if a non-digit is included in argument
    for (int n = 0; n < argLength; n++)
    {
        if (argc == 2)
        {
            if (isdigit(argv[1][n]) == false)
            {
                isInt = false;
                printf("Usage: ./caesar key\n");
                return 1;
            }
            
        }
    }
    // With argument entered, program prompts for plaintext
    if (isInt)
    {
        string plaintext = get_string("plaintext: ");
        printf("ciphertext: ");
        // int i examines each character in the string
        for (int i = 0, n = strlen(plaintext); i < n; i++)
        {
            if (isupper(plaintext[i]))
            {   
                // Output of cipher is determined by subtracting the alphabet's first letter ASCII value
                // from the curent letter's ASCII to convert to an alphabetic scale (A is 0, H is 7 etc)
                // Then the argument value is added.
                // The total is %26 in case the argument value is high, in order to bring it back to scale.
                // Finally the Ascii value of A is plugged in so the number is brough back to ASCII scale.
                printf("%c", (((plaintext[i] - 'A') + argument) % 26) + 'A');
            }
			
            if (islower(plaintext[i]))
            {
                printf("%c", (((plaintext[i] - 'a') + argument) % 26) + 'a');
            }
            // Any non-alpha characters (including spaces) are left alone and printed as-is
            if (isalpha(plaintext[i]) == false)
            {
                printf("%c", plaintext[i]);
            }
        }
        
        printf("\n");
    }
}
