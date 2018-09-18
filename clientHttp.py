#implementacao utilizando o http.client
import http.client
import json
import time

client = http.client.HTTPConnection("localhost", 8000)

def enviar_pedido(pedido):
    pedidojson = json.dumps(pedido)
    client.request("POST", "", body=pedidojson, headers={"Content-Type":"application/json", })
    print("client:" + str(type(pedidojson)))
    response = json.load(client.getresponse().read())
    return response

def gerar_pedido():
    pedido = []
    print("Digite os itens do seu pedido, ao finalizar digite 0")
    while True:
        item = input("Item: ")
        if item == '0':
            break
        pedido.append(item)
    return pedido

def acompanhar_pedido():
    while True:
        client.request(method = "GET", url = "")
        response = json.load(client.getresponse())
        print(response)
        time.sleep(5)

if __name__ == '__main__':
    while True:
        print("Digite:")
        print("- 1 Para realizar um pedido")
        print("- 2 Para acompanhar um pedido")
        print("- 0 Para sair")
        opcao = input("")
        if (opcao == '1'):
            pedido = gerar_pedido()
            print(pedido)
            confirma = input("Confirmar pedido? s/n")
            if (confirma == 's'):
                responseX = enviar_pedido(pedido) #modified
                print(responseX) #modified
            else:
                print("Pedido cancelado.")
        elif (opcao == '2'):
            acompanhar_pedido()
        elif (opcao == '0'):
            break
        else:
            print("Opcao invalida")
