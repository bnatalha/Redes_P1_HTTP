#implementacao utilizando o http.client
import http.client
import json

client = http.client.HTTPConnection("localhost", 8000)

def enviar_pedido(pedido):
    pedido_encoded = json.dumps(pedido)
    print(type(pedido_encoded)) # DEBUG: Checar o tipo de arquivo que json.dumps está retornando 
    client.request("POST", "", body=pedido_encoded, headers={"Content-Type":"application/json", })

def gerar_pedido():
    pedido = []
    print("Digite os itens do seu pedido, ao finalizar digite 0")
    while True:
        item = input("Item: ")
        if not item:
            break
        pedido.append("item")
    return pedido

def acompanhar_pedido(pedidoID):
    while true:
        client.request(method = "GET", url = pedidoID)
        response = client.getresponse()
        time.sleep(5)

if __name__ == '__main__':
    while True:
        print("Digite:")
        print("- 1 Para realizar um pedido")
        print("- 2 Para acompanhar um pedido")
        print("- 0 Para sair")
        opcao = input("")
        if (opcao == 1):
            pedido = gerar_pedido()
            print(pedido)
            confirma = input("Confirmar pedido? s/n")
            if (confirma == 's')
                enviar_pedido(pedido)
        elif (opcao == 2):
        elif (opcao == 0):
            return
        else:
            print("Opcao invalida")
