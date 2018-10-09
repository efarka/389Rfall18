Writeup 5 - Binaries I
======

Name: *Ethan Farkas*
Section:0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Ethan Farkas

## Assignment 5 Writeup

When I went to code these string functions  I made heavy use of the mov and add commands.  I knew I could manipulate the data of the strings using mov commands, and could increment pointers using the add command.  I also used the add and cmp commands for the loop – I incremented my counter using add, and then used cmp to set a flag to tell the program when the loop condition had been met.  Because I used some of the most basic commands in the assembly language, the code itself is very easy to follow, and makes logical sense.  The most confusing step for me was understanding cmp.  Once I understood that cmp was just doing subtraction, I understood how to avoid off by one errors or infinite loops. 


I quickly ran into a bug that was causing my program to seg fault.  I had mistakenly read the wrong documentation for which registers the parameters are passed into.  Because of this, I was manipulating the wrong bytes and my program seg faulted almost immediately.  It took me a while to figure this out, even though it was a pretty major bug.  Though I attempted to use gdb, I didn’t have enough experience with it to inspect the registers or get anything useful out of it.  I ended up debugging by commenting out each line in the binary until the program didn’t seg fault anymore.


Another issue I ran into was that originally my program didn’t assemble because my Kali was a 32 bit version.  Apparently when I installed Kali linux 2 years ago, I installed a 32 bit version not knowing the difference between that and 64 bit.  This was fixed by installing the 64 bit version of Kali. 

