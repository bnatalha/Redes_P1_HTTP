#implementacao utilizando o http.client
import http.client
import json
import time

client = http.client.HTTPConnection("192.168.56.1", 8000)

def update_pedido(id):
    client.request(method = "UPDATE", url = ("/pedido/" + str(id)), body = "")
    response = (client.getresponse().getcode())
    print("Resposta do servidor: {}".format(response))
    return

def verificar_todos():
    client.request(method = "GET", url = "/pedidos/todos")
    response = json.loads(client.getresponse().read())
    for pedido in response:
        print("Id do Pedido: {}".format(pedido[0]))
        print("Itens:")
        for item in pedido[1]:
            print("\t{}, R${}".format(item[0], item[1]))
        print()
        print("Valor Total: R${}\n".format(pedido[2]))
        print()

def verificar_prontos():
    client.request(method = "GET", url = "/pedidos/prontos")
    response = json.loads(client.getresponse().read())
    print("Pedidos Prontos: {}".format(response))

def verificar_andamento():
    client.request(method = "GET", url = "/pedidos/andamento")
    response = json.loads(client.getresponse().read())
    print("Pedidos em andamento: {}".format(response))

def acompanhar_pedido(id):
    client.request(method = "GET", url = "/pedido/" + str(id))
    response = json.loads(client.getresponse().read())
    print("Id do Pedido: {}".format(response[0]))
    print("Itens:")
    for item in response[1]:
        print("\t{}, R${}".format(item[0], item[1]))
    print()
    print("Valor Total: R${}\n".format(response[2]))
    print("Status: {}".format(response[3]))
    print()
    return

if __name__ == '__main__':
    while True:
        print("Digite:")
        print("- 1 Para verificar todos os pedidos realizados")
        print("- 2 Para verificar os pedidos em andamento")
        print("- 3 Para verificar os pedidos prontos")
        print("- 4 Para informar que um pedido está pronto")
        print("- 0 Para sair")
        opcao = input("")
        print ()
        if (opcao == '1'):
            verificar_todos()

        elif (opcao == '2'):
            verificar_andamento()
        elif (opcao == '3'):
            verificar_prontos()
        elif(opcao == '4'):
            id = input("Digite o id do pedido: ")
            update_pedido(id)
        elif(opcao == '0'):
            break
        else:
            print("Opcao invalida")
