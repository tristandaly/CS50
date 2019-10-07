#include <stdio.h>
#include <cs50.h>
#include <math.h>
// variables are declared, and can all be declared on one line
float answer;
int quarter, dime, nickel, penny, cents, coins;
int main(void)
{
    // Program will ask for input until a float that is greater than 0 is entered
    do
	{
	answer = get_float("How much change is owed: ");
    }
    while (answer <= 0) ;
	// variable 'cents' is defined as the answer with decimal place reduced	
	cents = round(answer * 100);
	// for loops assume one quarter is possible if cents are at least 25
	for (quarter = 1; cents >= 25; quarter++)
	{
		cents -= 25;
        // the 'coin' designation (final answer) is added with each applicable currency
		coins += 1;
	}
    // process is repeated for dimes - pennies. Can these coins fit? Add +1 to 'Coins'
	for (dime = 1; cents >= 10; dime++)
	{
        // '-=' is a shortcut for "cents = cents - 10. 10 cents is now gone from total"
		cents -= 10;
		coins += 1;
	}
	
	for (nickel = 1; cents >= 5; nickel++)
	{
		cents -= 5;
		coins += 1;
	}
	for (penny = 1; cents >= 1; penny++)
	{
		cents -= 1;
		coins += 1;
	}
    // final answer is printed: Total number of coins needed for change    
	printf("%i\n", coins);
		
}
