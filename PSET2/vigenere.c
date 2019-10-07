#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    // If no arguments, return error
    if (argc != 2)
    {
        printf("WRONG!\n");
        return 1;
    }
    // declare argument a string
    string argument = (argv[1]);
// create variable for length of argument
    int argLength = strlen(argv[1]);
    bool isInt = true;
// check all characters in argument to ensure they're letters
    for (int n = 0; n < argLength; n++)
    {
        if (argc == 2)
        {
            if (isalpha(argv[1][n]) == false)
            {
                isInt = false;
                printf("Usage: ./caesar key\n");
                return 1;
            }
            
        }
    }
    
    if (isInt)
    {
        string plaintext = get_string("plaintext: ");
		
        printf("ciphertext: ");
        // subtracts ASCII for A from each plaintext letter
        // Adds individual argument letters' modulo of argument length(so number won't exceed length)
        // Modulo 26 to bring high numbers to alphabetical values
        // re-add ASCII for A to bring up to ASCII
        for (int i = 0, j = 0, n = strlen(plaintext); i < n; i++)
        {
            int argPlace = tolower(argument[j % argLength]) - 'a';
			
            if (isupper(plaintext[i]))
            {
                printf("%c", (((plaintext[i] - 'A') + argPlace) % 26) + 'A');
                j++;
            }
			
            if (islower(plaintext[i]))
            {
                printf("%c", (((plaintext[i] - 'a') + argPlace) % 26) + 'a');
                j++;
            }
			
            if (isalpha(plaintext[i]) == false)
            {
                printf("%c", plaintext[i]);
            }
			
        }
        
        printf("\n");
    }
}
