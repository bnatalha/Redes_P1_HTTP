import http.server
import argparse
import json
# Python 3.7 é a mais nova versão, simplificou bastante a maneira de fazer o httpServer.
# Não encontrei nenhum exemplo que realmente fizesse uso das funcionalidades dessa versão
# Os que encontrei utilizam outras bibliotecas para fazer o tratamento das requests como re e cgi
# Porem não é necessario na versão atual(3.7) e demorei um pouquinho para perceber isso :p

# Lista de todos os pedidos
pedidos = []
# Ex: ["torrada", "suco", "tapioca"]

# Dicionario de pedidos em andamento
andamento = {}
# Ex: {1 : "torrada", 3:""tapioca", }

# Dicionario de pedidos prontos
prontos = {}
#EX: {2 :"suco"}

def fazer_pedido(pedido):
    # TODO: if pedido invalido return False
    print(pedido)
    return pedido


class HTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        #Testando a leitura de um post, printando o resultado no terminal
        pedido = json.load(self.rfile.read())
        resposta = fazer_pedido(pedido)
        if resposta:
            self.send_response(201)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            jstring = json.dumps(resposta)
            self.wfile.write(jstring.enconde("utf-8"))
            return
        else:
            formatError()
            return

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        resposta = json.dumps(andamento)
        self.wfile.write(resposta.encode("utf-8"))
        return

    def do_UPDATE(self):
        # TODO: atualizar o pedido para pronto, remover do dicionario andamento
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
