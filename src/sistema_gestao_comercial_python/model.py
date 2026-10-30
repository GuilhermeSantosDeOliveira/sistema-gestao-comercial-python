class Pessoa:
    def __init__(self , nome , cpf ):
        self.nome = nome
        self.cpf = cpf

class Fornecedor(Pessoa):
    #fproduto é o produto que o fornecedor fornece
    def __init__(self , nome , cpf , fproduto):
        super().__init__(nome , cpf)
        self.fproduto = fproduto
        
class Funcionario(Pessoa):
    def funcionario(self ,nome , cpf , setor):
        super().__init__(nome , cpf)
        self.setor = setor
        

class Categoria:
    #cid é o id da categoria
    def __init__(self , categoria, cid):
        self.categoria = categoria
        self.cid = cid

class Produto:
    #pid é o id do produto
    #cp é a categoria pertencente
    def __init__(self , produto , quantidade , valor , pid , cp):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor
        self.pid = pid
        self.cp = cp

class venda:
    #vid é o ID da venda 
    #pv é o produto vendido
    #qv é a quantidade vendida
    def __init__(self , data , pv , qv , valor , vid):
        self.data = data
        self.pv = pv
        self.qv = qv
        self.valor = valor
        self.vid = vid

