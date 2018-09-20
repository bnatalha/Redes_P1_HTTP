#implementacao utilizando o http.client
import http.client
import json
import time

client = http.client.HTTPConnection("localhost", 8000)

def enviar_pedido(pedido):
    pedidojson = json.dumps(pedido)
    pe = pedidojson.encode("utf-8")
    client.request("POST", "", body=pe,
                    headers={   "Content-Type":"application/json",
                                "Content-Lenght":len(pe)
                                })
    response = json.load(client.getresponse())
    print("")
    print("Pedido realizado com sucesso.")
    print("")
    print("Id do Pedido: {}".format(response[0]))
    print("Itens:")
    for item in response[1]:
        print("\t{}, R${}".format(item[0], item[1]))
    print()
    print("Valor Total: R${}\n".format(response[2]))
    return response[0]

def gerar_pedido():
    pedido = []
    print("Digite os itens do seu pedido, ao finalizar digite 0")
    while True:
        item = input("Item: ")
        if item == '0':
            break
        pedido.append(item)
    return pedido

def acompanhar_pedido(id):
    print("Aperte Ctrl+C para voltar ao menu.")
    try:
        while True:
            client.request(method = "GET", url = "/pedido/" + str(id))
            response = client.getresponse().read()
            print(response)
            time.sleep(5)
    except KeyboardInterrupt:
        return

def update_pedido():
    client.request(method = "UPDATE", url = "", body = "")
    response = client.getresponse().read()
    print(response)
    return

if __name__ == '__main__':
    while True:
        print("Digite:")
        print("- 1 Para realizar um pedido")
        print("- 2 Para acompanhar um pedido")
        print("- 3 Para indicar que o pedido esta pronto")
        print("- 0 Para sair")
        opcao = input("")
        print ()
        if (opcao == '1'):
            pedido = gerar_pedido()
            print(pedido)
            confirma = input("Confirmar pedido? s/n\n")
            if (confirma == 's'):
                id = enviar_pedido(pedido)
                print()
                print("Deseja acompanhar o pedido e ser notificado quando estiver pronto? s/n")
                a = input()
                if a == 's':
                    acompanhar_pedido(id)
            else:
                print("Pedido cancelado.")
        elif (opcao == '2'):
            acompanhar_pedido()
        elif (opcao == '3'):
            update_pedido()
        elif (opcao == '0'):
            break
        else:
            print("Opcao invalida")