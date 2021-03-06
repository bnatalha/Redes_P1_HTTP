import socket
import sys
from _thread import *

host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

order_list = {0: False, 1: False, 2: True}

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(5)
print('Waiting for a connection.')


def threaded_client(conn):
    conn.send(str.encode('Welcome, type your info\n'))

    while True:
        data = conn.recv(2048)


        try:
            key = int(data.decode('utf-8'))

            if key == -1:
                break

            is_ready = order_list[key]
        except KeyError as e:
            reply = 'Erro: Pedido não cadastrado\n'
            conn.sendall(str.encode(reply))
            continue

        if is_ready:
            reply = 'Seu pedido está pronto\n'
        else:
            reply = 'aguarde mais um pouco\n'

        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()


while True:

    conn, addr = s.accept()
    print('connected to: '+addr[0]+':'+str(addr[1]))

    start_new_thread(threaded_client, (conn,))
