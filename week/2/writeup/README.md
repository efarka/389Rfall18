Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Ethan Farkas
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *PUT YOUR NAME HERE*

## Assignment 2 writeup

### Part 1 (45 pts)

1.	What is kruegster1990's real name?
Fred Krueger

2.	List all personal information (including social media accounts) you can find about him. For each, briefly detail how you discovered them.
Doing a quick google search led me to his twitter account @krugster1990
His email is kruegster@tutanota.com from his website
https://www.instagram.com/kruegster1990/ from namechk
Found that he liked pokemon, and an airline ticket to sfo

he also has a reddit account i found from namechk


3.	What is the IP address of the webserver hosting his company's sie? How did you discover this?
142.93.118.186.  I pinged his website, and saw what ip address responded.

4.	List any hidden files or directories you found on this website. Did you find any flags?
In the robots.txt, I found the directory /secret, where the flag CMSC389R-{fly_th3_sk1es_w1th_u5} was.  I also found the github repo by going to /.git where I found another flag.

5.	Did you find any other IP addresses associated with this website? What do they link to, or where did you find them?
I found an ip address, 142.93.117.193, as the address of the under construction portion of the site.

6.	If you found any associated server(s), where are they located? How did you discover this?
By using shodan.io and entering the ip I found that the servers are located in New York.

7.	Which operating system is running on the associated server(s)? How did you discover this?
Ubuntu  I used browserspy.dk and entered 142.93.117.193

8.	BONUS: Did you find any other flags on your OSINT mission? (Up to 9 pts!)
CMSC389R-{h1dden_fl4g_in_s0urce}
CMSC389R-{fly_th3_sk1es_w1th_u5}
CMSC389R-{y0u_found_th3_g1t_repo}

### Part 2 (55 pts)

*REPLACE THIS TEXT WITH A BRIEF EXPLANATION OF YOUR APPROACH TO SOLVING THIS CHALLENGE, AND THE OUTCOME*

By nmaping the port, I found open ports 80, 1337, 2222, 10010, and a filtered port on 11211.  I nc's on each of these and found a login form on 1337.  I wrote a script to brute force the password to this form, but it ended up being faster to just guess the username and password as kreugster/pokemon.  I gathered the flag by exploring the shell and finding the flight records, and catting the one that matched the ticket on Fred's instagram.  The flag is CMSC389R-{c0rn3rstone-air-27670}