import requests
import argparse
import socket
import json
def printReturn(response):
    print response.content
    print response.headers
    print response.status_code

def makeRequest(url):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 9999)
    client_socket.connect(server_address)

    #request_header = 'GET /user/getuser/Vao HTTP/1.1\r\nHost: http://localhost\r\n\r\n'
    client_socket.send(url)
    response = ''
    while True:
        recv = client_socket.recv(1024)
        if not recv:
            break
        response += recv

    print response
    client_socket.close()

def listaUsers():
    url = 'GET /user/getuser/lista HTTP/1.1\r\nHost: http://localhost\r\n\r\n'
    makeRequest(url)
    '''
    URL = "http://localhost:9999/user/getuser/lista"
    r = requests.get(url = URL)
    printReturn(r)
    '''
def getUser(nome):
    url = 'GET /user/getuser/{} HTTP/1.1\r\nHost: http://localhost\r\n\r\n'.format(nome)
    makeRequest(url)

def delUser(nome):
    url = 'DELETE /user/getuser/del/{} HTTP/1.1\r\nHost: http://localhost\r\n\r\n'.format(nome)
    makeRequest(url)

def postUser(dados):
    dados = {
        "nome": dados[0],
        "idade": dados[1],
        "altura": dados[2]
    }

    URL = "http://localhost:9999/user/getuser/post"
    r = requests.post(url = URL, data = dados)
    printReturn(r)
    
def updateUser(dados):
    URL = "http://localhost:9999/user/getuser/put"
    dados = {
        "nome": dados[0],
        "idade": dados[1],
        "altura": dados[2]
    }
    r = requests.put(url = URL, data = dados)
    printReturn(r)

if __name__ == '__main__':
    arg = argparse.ArgumentParser(description="Rest Client")
    arg.add_argument("-p", dest="post", nargs='+', type=str, default="", help="parametros requisicao POST")
    arg.add_argument("-g", dest="get", type=str, default="", help="Parametro Requisicao GET")
    arg.add_argument("-put", dest="put", nargs='+', type=str, default="", help="Parametro Requisicao PUT")
    arg.add_argument("-l", dest="lista", default='', action='store_true',help="Parametro Requisicao listar")
    arg.add_argument("-d", dest="delete", type=str, default="", help="Parametro Requisicao DELETE")

    args = arg.parse_args()

    if (args.post != ""):
        postUser(args.post)
    if (args.get != ""):
        getUser(args.get)
    if (args.lista):
        listaUsers()
    if (args.put != ""):
        updateUser(args.put)
    if (args.delete != ""):
        delUser(args.delete)
#curl -i -H "Content-Type: application/json" -X POST -d '{"nimi":"artistin_nimi"}' http://localhost:5000/artistit
