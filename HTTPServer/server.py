import http.server
import argparse
import json
# Python 3.7 é a mais nova versão, simplificou bastante a maneira de fazer o httpServer.
# Não encontrei nenhum exemplo que realmente fizesse uso das funcionalidades dessa versão
# Os que encontrei utilizam outras bibliotecas para fazer o tratamento das requests como re e cgi
# Porem não é necessario na versão atual(3.7) e demorei um pouquinho para perceber isso :p

#Dicionario de pedidos em andamento
pedidos = {}

def fazer_pedido(pedido):
    print(pedido)
    return pedido

def checar_pedido(pedidoID):
    # TODO: Checar se o pedido está nos pedidos em andamento, caso nao esteja informar que o pedido está pronto
    print(pedidoID)
    return False

class HTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        #Testando a leitura de um post, printando o resultado no terminal
        pedido = json.load(self.rfile.read())
        resposta = fazer_pedido(pedido)
        self.send_response(201)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(resposta).encode("utf-8"))
        return

    def do_GET(self):
        if (self.headers["Content-Length"] == None || self.headers["Content-Type"] =! "application/json"):
            formatError()
            return
        #Testando o jsom.dumps passando um dicionario como argumento
        pedidoID = json.load(self.rfile)
        resposta = checar_pedido(pedidoID)
        self.wfile.write(json.dumps(resposta).encode("utf-8"))
        return

    def do_UPDATE(self):
        # TODO: atualizar o pedido para pronto, remover da lista pedidos
        return

    def formatError():
        self.send_response(400)
        self.end_headers()
        self.wfile.write("Request com formato incorreto".encode('utf_8'))
        return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='HTTP Server')
    parser.add_argument('port', type=int, help='Listening port for HTTP Server')
    parser.add_argument('ip', help='HTTP Server IP')
    args = parser.parse_args()
    print("Starting Server...")
    with http.server.ThreadingHTTPServer((args.ip, args.port), HTTPRequestHandler) as server:
        server.serve_forever()
