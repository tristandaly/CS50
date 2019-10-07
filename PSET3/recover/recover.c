#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define BLOCKSIZE = 512
typedef unsigned char BYTE;

int main(int argc, char *argv[])
{
    // define argument variable
    char *argument = argv[1];

    // remind user to use correct command line argument
    if (argc != 2)
    {
        fprintf(stderr, "Please enter filename for recovery\n");
        return 1;
    }

    // open input file
    FILE *inptr = fopen(argument, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", argument);
        return 2;
    }
    // declare mem location of new image, characters in name (xxx.jpg plus \0), and beginning count of images generated
    FILE *rcvImage;
    char imgName[8];
    int imgCount = 0;
    BYTE block[512];
    // While loop that works as long as the block size is 512
    while (fread(block, sizeof(block), 1, inptr) == 1)
    {
        // loop begins and ends with the jpeg header
        if (block[0] == 0xff && block[1] == 0xd8 && block[2] == 0xff)
        {
            if (imgCount > 0)
            {
                // Close stream of file creation (save file when end of jpeg is reached)
                fclose(rcvImage);
                // Create new image in sequence
                sprintf(imgName, "%03i.jpg", imgCount);
                imgCount += 1;
                // open stream of file creation
                rcvImage = fopen(imgName, "w");
                //write image to 512 block chunks
                fwrite(block, sizeof(block), 1, rcvImage);
            }
            if (imgCount == 0)
            {
                sprintf(imgName, "%03i.jpg", imgCount);
                imgCount += 1;
                rcvImage = fopen(imgName, "w");
                fwrite(block, sizeof(block), 1, rcvImage);
            }
        }
        else if (imgCount > 0)
        {
            fwrite(block, sizeof(block), 1, rcvImage);
        }
    }
}