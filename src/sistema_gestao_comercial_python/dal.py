import json
from pathlib import Path

import model


class PessoaDal:
    def converter():
        arquivo = Path(__file__).parent.parent.parent / "data"/"Pessoa.json"
        with open(arquivo , "r" ,encoding='utf-8') as arq:
            Pessoa = json.load(arq)
            return Pessoa

    @classmethod
    def salvar(cls , pessoa:model.Pessoa):
        arquivo = Path(__file__).parent.parent.parent / "data"/"Pessoa.json"
        Pessoa = cls.converter()
        p = {"nome":pessoa.nome , "cpf" :pessoa.cpf}
        Pessoa.append(p)
        with open(arquivo , "w" ,encoding='utf-8') as arq:
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
        arquivo = Path(__file__).parent.parent.parent / "data"/"Pessoa.json"
        with open(arquivo , "w" ,encoding='utf-8') as arq:
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
        arquivo = Path(__file__).parent.parent.parent / "data"/"Pessoa.json"
        with open(arquivo , "w" ,encoding='utf-8') as arq:
            json.dump(pessoa , arq , indent=4 ,ensure_ascii=False)
        return True



            
class FornecedorDal:
    arquivo = Path(__file__).parent.parent.parent / "data"/"Fornecedor.json"

class FuncionarioDal:
    arquivo = Path(__file__).parent.parent.parent / "data"/"Funcionario.json"

class CategoriaDal:
    arquivo = Path(__file__).parent.parent.parent / "data"/"Categoria.json"

class ProdutoDal:
    arquivo = Path(__file__).parent.parent.parent / "data"/"Produto.json"

class VendaDal:
    arquivo = Path(__file__).parent.parent.parent / "data"/"Venda.json"