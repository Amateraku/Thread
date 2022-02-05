from threading import Thread
import socket


s = socket.socket()
s.bind(('localhost', 9000))
s.listen(1)

conn, adr = s.accept()
conn2, adr2 = s.accept()


def first_client():
    while 1:
        data = conn.recv(1024)
        if data.decode().lower() == 'exit':
            s.close()
            break
        conn2.send(data)


def second_client():
    while 1:
        data2 = conn2.recv(1024)
        if data2.decode().lower() == 'exit':
            s.close()
            break
        conn.send(data2)


th = Thread(target=first_client())
th2 = Thread(target=second_client())
th.start()
th2.start()