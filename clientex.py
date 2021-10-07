from socket import*
while True:
    a = socket()
    a.connect(("localhost",1234))
    j = input("Enter your message:-")
    a.send(j.encode('ascii'))
    t = (a.recv(1024)).decode()
    print("server:",t)
    if t == "bye" or j =='bye':
        break
    a.close()
