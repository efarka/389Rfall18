Writeup 3 - OSINT II, OpSec and RE
======

Name: Ethan Farkas
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Ethan Farkas

## Assignment 3 Writeup

### Part 1 (100 pts)
One of the biggest mistakes Fred made in his security policies is probably the easiest to fix.  Fred used a very weak password of ‘pokemon’ to secure his server.  This password is so common that attackers can quickly crack it using a brute force attack.  Fred ought to use a password manager.  Humans are often bad at generating multiple unique passwords, but if he uses a password manager, he only needs to generate one strong password, and his logins will be secure.  As techspective states, “A password manager not only eliminates the need to remember multiple passwords, it also ensures that your passwords are stored safely with using encryption.”

Additionally, Fred should not have completely open ports on his machine.  Having open ports means attackers can connect to the port and attack it.  Fred should use a firewall and a whitelist to specify who can connect to that port.  According to makeuseof, “A firewall is a barrier or shield that is intended to protect your PC, tablet, or phone from the data-based malware dangers that exist on the Internet.”  If Fred used a firewall, chances are most attackers wouldn’t even be able to connect to his port.

Finally, ideally, Fred’s IP address would not be so easily visible.  The IP address being visible allows attackers to scan his IP for open ports and look for vulnerabilities.  His website should not redirect to his IP Address.  As the vpnlab states, it is important to hide your ip-address to reduce your attack surface.  Especially in Fred’s case, the attack would have been much more difficult if he had his ip address lying around in the open on his public website.  

Sources:
https://techspective.net/2018/04/23/what-is-a-password-manager-and-why-do-you-need-it/
https://www.makeuseof.com/tag/5-reasons-use-firewall/
https://www.thevpnlab.com/why-should-you-hide-your-ip-address/

