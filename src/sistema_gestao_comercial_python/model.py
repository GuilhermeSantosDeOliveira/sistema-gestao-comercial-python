class Pessoa:
    def __init__(self , nome , cpf ):
        self.nome = nome
        self.cpf = cpf

class Fornecedor(Pessoa):
    #fproduto é o produto que o fornecedor fornece
    def __init__(self , fproduto):
        self.fproduto = fproduto
        

class Funcionario(Pessoa):
    def funcionario(self , setor):
        self.setor = setor
        

class Categoria:
    #cid é o id da categoria
    def __init__(self , categoria, cid):
        self.categoria = categoria
        self.cid = cid

class Produto:
    #pid é o id do produto
    def __init__(self , produto , quantidade , valor , pid ):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor
        self.pid = pid

class venda:
    #vid é o ID da venda 
    def __init__(self , data , vendas , vid):
        self.vid = vid
        self.data = data
        self.vendas = vendas

