import json
from pathlib import Path

import model


class PessoaDal:
    def converter():
        pessoa_arquivo = Path(__file__).parent.parent.parent / "data"/"Pessoa.json"
        with open(pessoa_arquivo , "r" ,encoding='utf-8') as arq:
            Pessoa = json.load(arq)
            return Pessoa

    @classmethod
    def salvar(cls , pessoa:model.Pessoa):
        pessoa_arquivo = Path(__file__).parent.parent.parent / "data"/"Pessoa.json"
        Pessoa = cls.converter()
        p = {"nome":pessoa.nome , "cpf" :pessoa.cpf}
        Pessoa.append(p)
        with open(pessoa_arquivo , "w" ,encoding='utf-8') as arq:
            json.dump(Pessoa,arq,indent=4 ,ensure_ascii=False)

    @classmethod
    def pesquisa(cls , cpf:str , lista=None):
        if lista == None:
            lista = cls.converter()
        for i in lista:
            if i["cpf"] == cpf:
                    return i

    @classmethod
    def editar(cls , lupa , nome , cpf):
        pessoa = cls.converter()
        i = cls.pesquisa(lupa["cpf"] , pessoa)
        if i == None:
            return
        else:
            i["nome"] = nome
            i["cpf"] = cpf
        pessoa_arquivo = Path(__file__).parent.parent.parent / "data"/"Pessoa.json"
        with open(pessoa_arquivo , "w" ,encoding='utf-8') as arq:
            json.dump(pessoa , arq , indent=4 ,ensure_ascii=False)

    @classmethod
    def excluir(cls , cpf):
        pessoa = cls.converter()
        i = cls.pesquisa(cpf, pessoa)
        if i == None:
            return False
        else:
            p= pessoa.index(i)
            del pessoa[p]
        pessoa_arquivo = Path(__file__).parent.parent.parent / "data"/"Pessoa.json"
        with open(pessoa_arquivo , "w" ,encoding='utf-8') as arq:
            json.dump(pessoa , arq , indent=4 ,ensure_ascii=False)
        return True

            
class FornecedorDal:
    #vou deixar fornecedor assim por hora e mecher nele depois

    def converter():
            fornecedor_arquivo = Path(__file__).parent.parent.parent / "data"/"Fornecedor.json"
            with open(fornecedor_arquivo , "r" ,encoding='utf-8') as arq:
                fornecedor = json.load(arq)
                return fornecedor

    def salvar(cls , fornecedor:model.Fornecedor ):
            fornecedor_arquivo = Path(__file__).parent.parent.parent / "data"/"Fornecedor.json"
            Fornecedor = cls.converter()
            f = {"nome":fornecedor.nome , "cpf" :fornecedor.cpf}
            Fornecedor.append(f)
            with open(fornecedor_arquivo , "w" ,encoding='utf-8') as arq:
                json.dump(Fornecedor,arq,indent=4 ,ensure_ascii=False)
    
class FuncionarioDal:
    arquivo = Path(__file__).parent.parent.parent / "data"/"Funcionario.json"
    

class CategoriaDal:
    def converter():
        categoria_arquivo = Path(__file__).parent.parent.parent / "data"/"Categoria.json"
        with open(categoria_arquivo , "r" ,encoding='utf-8') as arq:
            categoria = json.load(arq)
            return categoria
        
    def salvar(cls , categoria:model.Categoria ):
        categoria_arquivo = Path(__file__).parent.parent.parent / "data"/"Categoria.json"
        Fornecedor = cls.converter()
        f = {"categoria":categoria.categoria , "cid" :categoria.cid}
        Fornecedor.append(f)
        with open(categoria_arquivo , "w" ,encoding='utf-8') as arq:
            json.dump(Fornecedor,arq,indent=4 ,ensure_ascii=False)

class ProdutoDal:
    arquivo = Path(__file__).parent.parent.parent / "data"/"Produto.json"

class VendaDal:
    arquivo = Path(__file__).parent.parent.parent / "data"/"Venda.json"