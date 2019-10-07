// Copies a BMP file

#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: copy infile outfile\n");
        return 1;
    }

    // remember filenames
    int n = atoi(argv[1]);
    char *infile = argv[2];
    char *outfile = argv[3];

    // enter correct argument
    if (n < 1 || n > 100)
    {
        fprintf(stderr, "Please enter a number from 1 - 100\n");
        return 2;
    }

    // open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 3;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 4;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 5;
    }

    // create outfile's BITMAPFILEHEADER
    BITMAPFILEHEADER newBf;
    // create outfile's BITMAPINFOHEADER
    BITMAPINFOHEADER newBi;

    // assign to default headers
    newBf = bf;
    newBi = bi;

    // assign values for new padding
    newBi.biWidth *= n;
    newBi.biHeight *= n;

    // determine padding for scanlines
    int padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    // define new padding
    int newPadding = (4 - (newBi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    // define attributes of outputted BMP
    newBi.biSizeImage = ((sizeof(RGBTRIPLE) * newBi.biWidth) + newPadding) * abs(newBi.biHeight);
    newBf.bfSize = newBi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

    // write outfile's BITMAPFILEHEADER
    fwrite(&newBf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&newBi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // Point to beginning of row which is defined as pixel amount in total width
    RGBTRIPLE *row = malloc(sizeof(RGBTRIPLE) * newBi.biWidth);

    // iterate over infile's scanlines
    for (int i = 0; i < abs(bi.biHeight); i++)
    {
        int pointer = 0;

        // iterate over pixels in scanline
        for (int j = 0; j < bi.biWidth; j++)
        {
            // temporary storage
            RGBTRIPLE triple;

            // read RGB triple from infile
            fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

            for (int k = 0; k < n; k++)
            {
                // Temp storage location moves to beginning of new row after completion of last row width
                *(row + pointer) = triple;
                pointer++;
            }

        }

        // skip over padding, if any
        fseek(inptr, padding, SEEK_CUR);

        // add entire rows using newly defined width/row variables
        for (int m = 0; m < n; m++)
        {
            fwrite(row, sizeof(RGBTRIPLE), newBi.biWidth, outptr);

            // add padding to these new rows
            for (int p = 0; p < newPadding; p++)
            {
                fputc(0x00, outptr);
            }
        }
    }

    // prevent memory leak from malloc
    free(row);

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
