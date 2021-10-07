from socket import*
l = True
while l:
    a = socket()
    a.bind(("localhost",1234))
    print("Wait for client response:------")
    a.listen(5)
    ip,data = a.accept()
    p = ip.recv(1024).decode()
    print('client',p)
    j = input("Enter your message to response")
    ip.send(j.encode("ascii"))
    if p == "bye":
        l=False
        a.close()
