import socket
hostname = socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
print("computer name is: "+hostname)
print("your computer ip address :" +IPAddr)
