Writeup 7 - Forensics I
======

Name: Ethan Farkas
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Ethan Farkas

## Assignment 7 writeup

### Part 1 (40 pts)

1. Jpeg File

2. John Hancock Center, Chicago Illinois

3.  2018:08:22 11:33:24

4.  Apple iphone 8

5. 539.537 m

6.

### Part 2 (55 pts)
flag is CMSC389R-{dropping_files_is_fun}

I loaded the binary in a decompiler.  In main, there is a local string '/tmp/.stego'.  A function called reverse_array is then called.  It's arguments are 'w8' , 0, and 'challenge'.  Challange was a pointer to the data section, where there was a bunch of unintelligible data.  0 acts as a counter, and is incremented each loop in reeverse array.  At this point I noticed that in main, after reverse_array is fopen and fwrite.  It's opening in wb mode, which means it is writing a binary file somewhere.  As there was no file in the local directory, I figured that the file was being written in the /tmp directory.  I also took a hint that the flag location might be hidden from the text that is printed with puts in the binary - 'Where is your flag now'.   Going to the /tmp directory, I found the .stego file.

I saw that the .stego file was a binary file.  Taking a hint from the name, I figured the flag must involve some stegonography.  However, the .stego file was not an image itself, as it did not contain any recognizable magic bytes at the beginning.  Trying to open the file with an image viewer thus didn't work.  Running strings on it or using a hex editor also didn't produce any results.  Knowing this, I used binwalk to look for embedded files.  There was a jpeg file embedded in the .stego.  After extracting the jpeg using binwalk, I was able to view it, and saw a stegosaurous.  I then used steghide in extract mode to find the hidden flag.  The password was "stegosaurous", per the image.
