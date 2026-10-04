class Pessoa:
    def pessoa(self , nome , cpf ):
        self.nome = nome
        self.cpf = cpf

class Cliente(Pessoa):
    def cliente(self , compra):
        self.compra = compra

class Fornecedor(Pessoa):
    def Fornecedor(self , fproduto , id_fornecedor):
        self.fproduto = fproduto
        self.id_fornecedor = id_fornecedor

class Funcionario(Pessoa):
    def funcionario(self , setor , id_funcionario):
        self.setor = setor
        self.id_funcionario = id_funcionario

class Categoria:
    def categoria(self , categoria):
        self.categoria = categoria

class Produto(Categoria):
    def produtos(self , produto , quantidade , valor ):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

