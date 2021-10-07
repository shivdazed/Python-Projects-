class Client:
    from socket import *
    l = True
    while l:
        a = socket()
        a.connect(("localhost",1234))
        j = input("Enter your message:-")
        a.send(j.encode('ascii'))
        t = (a.recv(1024)).decode()
        print("server:",t)
        if j=='bye' or t =='bye':
            l=False        
            a.close()


                
