class Produtos():
    produtos = None
    def __init__(self, dict):
        self.produtos = dict
        return

    def get_valor(self, nome):
        return self.produtos[nome]
    def addProduto(self, nome, valor):
        self.produtos[nome] = valor


class Pedidos():
    # Lista de todos os pedidos
    pedidos = []
    # Lista de pedidos em andamento
    andamento = []
    # Ex: [3,4]
    # Lista de pedidos prontos
    prontos = []
    #EX: [1,2]
    currentID = 1

    produtos = Produtos({"suco":4, "salgado":2.5, "refrigerante":2, "tapioca":6, "torrada":2.5})

    def __init__(self):
        return

    def fazer_pedido(self, pedido):
        pedido_completo = [self.currentID]
        self.currentID += 1
        valor_total = 0
        itens = []
        for item in pedido:
            itens.append((item, self.produtos.get_valor(item)))
            valor_total += self.produtos.get_valor(item)
        pedido_completo.append(itens)
        pedido_completo.append(valor_total)
        self.pedidos.append(pedido_completo)
        self.andamento.append(pedido_completo[0])
        return pedido_completo

    def update_pedido(self, pedido_id):
        for id in self.andamento:
            if(id == pedido_id):
                self.prontos.append(id)
                self.andamento.remove(id)
                return True
        return False
