import os
import socket 

def call():
    os.system('route.bat')
    os.system('del route.bat')
    os.system('cls')

def CreateFile(IPAddr):
    ip=IPAddr[:11]
    f=open("route.bat","w+")
    f.write("Start http://%s/"%ip)
    f.close()
    call()

if __name__ == "__main__":
    hostname = socket.gethostname() 
    IPAddr = socket.gethostbyname(hostname)   
    CreateFile(IPAddr)  
