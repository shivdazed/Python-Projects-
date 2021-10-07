from socket import*
while True:
    a = socket()
    a.bind(("localhost",1234))
    a.listen(5)
    ip,data = a.accept()
    p = ip.recv(1024).decode()
    print('client:',p)
    j = input("Enter you message to response:-")
    ip.send(j.encode('ascii'))
    if p == "bye":
        break
    a.close()
