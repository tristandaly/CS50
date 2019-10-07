# Questions

## What's `stdint.h`?

The standard input/output library in C. Allows program to accept input from user and output when prompted.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

Useful when requiring an int that only needs to be x number of bytes (8, 16, 32 etc.)

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

BYTE: 1
DWORD: 4
LONG: 8
WORD: 2

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

0x42, 0x4D

## What's the difference between `bfSize` and `biSize`?

bfSize deals with the BMP image as a whole, whereas biSize contains size info for the BITMAPINFOHEADER

## What does it mean if `biHeight` is negative?

When the image loads, a negative biHeight means the image will load from the top down.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount

## Why might `fopen` return `NULL` in `copy.c`?

Unsupported File Format

## Why is the third argument to `fread` always `1` in our code?

It defines the number of elements being used in the function

## What value does `copy.c` assign to `padding` if `bi.biWidth` is `3`?

3 is assigned to padding, as the 3 triples add to 9. Adding 3 more gives a multiple of 4 (12)

## What does `fseek` do?

Points to a specific location in a file, similar to a pointer.

## What is `SEEK_CUR`?

Shows the current location of the pointer.
