import http.server
import argparse
import json
# Python 3.7 é a mais nova versão, simplificou bastante a maneira de fazer o httpServer.
# Não encontrei nenhum exemplo que realmente fizesse uso das funcionalidades dessa versão
# Os que encontrei utilizam outras bibliotecas para fazer o tratamento das requests como re e cgi
# Porem não é necessario na versão atual(3.7) e demorei um pouquinho para perceber isso :p
class HTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        #Testando a leitura de um post, printando o resultado no terminal
        a = json.load(self.rfile.read())
        self.send_response(200)
        self.end_headers()
        return

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        #Testando o jsom.dumps passando um dicionario como argumento
        self.wfile.write(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4).encode())
        return

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='HTTP Server')
    parser.add_argument('port', type=int, help='Listening port for HTTP Server')
    parser.add_argument('ip', help='HTTP Server IP')
    args = parser.parse_args()
    print("Starting Server...")
    with http.server.ThreadingHTTPServer((args.ip, args.port), HTTPRequestHandler) as server:
        server.serve_forever()
