#include <cs50.h>
#include <stdio.h>

int main(void)

{
    // declare variable
    int height;
    // do-while loop to prompt user while conditions are true
	do
    {
        height = get_int("Height: ");
    }

        while (height < 1 || height > 8);
    {
        // adds spaces and blocks
        for (int rows = 0; rows < height; rows++)
        {
            for (int spaces = height - rows; spaces > 1; spaces--)
            {
                printf(" ");
            }
            for (int bricks = -1; bricks < rows; bricks++)
            {
                printf("#");
            }
            // adds double-space between pyramids
            printf("  ");
			// new pyramid is made using same formula without spaces (not needed on right side)
			for (int bricks = -1; bricks < rows; bricks++)
			{
                printf("#");
            }

			printf("\n");

		}

	}

}
