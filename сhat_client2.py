import socket


s = socket.socket()
s.connect(('localhost', 9000))

while True:
    data = input("Enter some text: ")
    s.send(data.encode())
    data_msg = s.recv(1024).decode()
    print(data_msg)
    if data.lower() == 'exit':
        s.close()
        break