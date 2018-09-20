import http.server
import argparse
import json
from pedidos import Pedidos
# Python 3.7 é a mais nova versão, simplificou bastante a maneira de fazer o httpServer.
# Não encontrei nenhum exemplo que realmente fizesse uso das funcionalidades dessa versão
# Os que encontrei utilizam outras bibliotecas para fazer o tratamento das requests como re e cgi
# Porem não é necessario na versão atual(3.7) e demorei um pouquinho para perceber isso :p

pedidos = Pedidos()
class HTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        #Testando a leitura de um post, printando o resultado no terminal
        pedidoj = self.rfile.read(int(self.headers["Content-Lenght"]))
        pedido = json.loads(pedidoj)
        resposta = pedidos.fazer_pedido(pedido)
        if resposta:
            self.send_response(201)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            jstring = json.dumps(resposta)
            self.wfile.write(jstring.encode("utf-8"))
            return
        else:
            formatError()
            return

    def do_GET(self):
        url = self.path.split('/')
        print(url)
        if (url[1] == 'pedido'):
            id = int(url[2])
            if (id > len(pedidos.pedidos)):
                self.__formatError("Id " + url[2] + " invalido, verifique o id do pedido.")
                return
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            pedido = pedidos.pedidos[id - 1]
            for item in pedidos.andamento:
                if (item == id):
                    pedido.append("andamento")
                    break
            if (pedido[-1] != "andamento"):
                pedido.append("pronto")
            resposta = json.dumps(pedido)
            pedido.pop()
            self.wfile.write(resposta.encode("utf-8"))

        if (url[1] == 'pedidos'):
            if (url[2] == 'todos'):
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                resposta = json.dumps(pedidos.pedidos)
                self.wfile.write(resposta.encode("utf-8"))

            elif (url[2] == 'andamento'):
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                resposta = json.dumps(pedidos.andamento)
                self.wfile.write(resposta.encode("utf-8"))

            elif (url[2] == 'prontos'):
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                resposta = json.dumps(pedidos.prontos)
                self.wfile.write(resposta.encode("utf-8"))
            else:
                self.__formatError()
                return
        return

    def do_UPDATE(self):
        # TODO: atualizar o pedido para pronto, remover do dicionario andamento
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        resposta = json.dumps(pedidos.prontos)
        self.wfile.write(resposta.encode("utf-8"))
        return

    def __formatError(self, desc = ""):
        self.send_response(400)
        self.end_headers()
        self.wfile.write(("Request invalida: " + desc).encode('utf_8'))
        return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='HTTP Server')
    parser.add_argument('port', type=int, help='Listening port for HTTP Server')
    parser.add_argument('ip', help='HTTP Server IP')
    args = parser.parse_args()
    print("Starting Server...")
    with http.server.ThreadingHTTPServer((args.ip, args.port), HTTPRequestHandler) as server:
        server.serve_forever()
