class Pessoa:
    def pessoa(self , nome , cpf ):
        self.nome = nome
        self.cpf = cpf

class Fornecedor(Pessoa):
    def Fornecedor(self , fproduto):
        self.fproduto = fproduto
        

class Funcionario(Pessoa):
    def funcionario(self , setor):
        self.setor = setor
        

class Categoria:
    def categoria(self , categoria, cid):
        self.categoria = categoria
        self.cid = cid

class Produto:
    def produtos(self , produto , quantidade , valor , pid ):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor
        self.pid = pid

class venda:
    def venda(self , data , vendas , vid):
        self.vid = vid
        self.data = data
        self.vendas = vendas

