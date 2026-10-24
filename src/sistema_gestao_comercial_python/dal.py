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

    def fornecedor_converter():
        fornecedor_arquivo = Path(__file__).parent.parent.parent / "data"/"Fornecedor.json"
        with open(fornecedor_arquivo , "r" ,encoding='utf-8') as arq:
            fornecedor = json.load(arq)
            return fornecedor
        
    @classmethod
    def fornecedor_salvar(cls , fornecedor:model.Fornecedor ):
        fornecedor_arquivo = Path(__file__).parent.parent.parent / "data"/"Fornecedor.json"
        Fornecedor = cls.fornecedor_converter()
        f = {"nome":fornecedor.nome , "cpf" :fornecedor.cpf , "produto_fornecido": fornecedor.fproduto}
        Fornecedor.append(f)
        with open(fornecedor_arquivo , "w" ,encoding='utf-8') as arq:
            json.dump(Fornecedor,arq,indent=4 ,ensure_ascii=False)

    @classmethod
    def fornecedor_pesquisa(cls , cpf:str , lista=None):
        if lista == None:
            lista = cls.fornecedor_converter()
        for i in lista:
            if i["cpf"] == cpf:
                return i
        
    @classmethod
    def fornecedor_editar(cls , lupa , nome , cpf , fproduto):
        Fornecedor = cls.fornecedor_converter()
        i = cls.fornecedor_pesquisa(lupa["cpf"] , Fornecedor)
        if i == None:
            return
        else:
            i["nome"] = nome
            i["cpf"] = cpf
            i["produto_fornecido"] = fproduto
        fornecedor_arquivo = Path(__file__).parent.parent.parent / "data"/"Fornecedor.json"
        with open(fornecedor_arquivo , "w" ,encoding='utf-8') as arq:
            json.dump(Fornecedor , arq , indent=4 ,ensure_ascii=False)
        
    @classmethod
    def fornecedor_excluir(cls , cpf):
        fornecedor = cls.fornecedor_converter()
        i = cls.fornecedor_pesquisa(cpf, fornecedor)
        if i == None:
            return False
        else:
            f= fornecedor.index(i)
            del fornecedor[f]
        fornecedor_arquivo = Path(__file__).parent.parent.parent / "data"/"Fornecedor.json"
        with open(fornecedor_arquivo , "w" ,encoding='utf-8') as arq:
            json.dump(fornecedor , arq , indent=4 ,ensure_ascii=False)
        return True
        
class FuncionarioDal:
    arquivo = Path(__file__).parent.parent.parent / "data"/"Funcionario.json"

class CategoriaDal:

    
    def categoria_converter():
        categoria_arquivo = Path(__file__).parent.parent.parent / "data"/"Categoria.json"
        with open(categoria_arquivo , "r" ,encoding='utf-8') as arq:
            categoria = json.load(arq)
            return categoria

    @classmethod
    def categoria_salvar(cls , categoria:model.Categoria ):
        categoria_arquivo = Path(__file__).parent.parent.parent / "data"/"Categoria.json"
        Categoria = cls.categoria_converter()
        c = {"categoria":categoria.categoria , "cid" :categoria.cid}
        Categoria.append(c)
        with open(categoria_arquivo , "w" ,encoding='utf-8') as arq:
            json.dump(Categoria,arq,indent=4 ,ensure_ascii=False)

    @classmethod
    def categoria_pesquisa(cls , cid:str , lista=None):
        if lista == None:
            lista = cls.categoria_converter()
        for i in lista:
            if i["cid"] == cid:
                return i
    
    @classmethod
    def categoria_editar(cls , lupa , categoria , cid):
        Categoria = cls.categoria_converter()
        i = cls.categoria_pesquisa(lupa["cid"] , Categoria)
        if i == None:
            return
        else:
            i["categoria"] = categoria
            i["cid"] = cid
        categoria_arquivo = Path(__file__).parent.parent.parent / "data"/"Categoria.json"
        with open(categoria_arquivo , "w" ,encoding='utf-8') as arq:
            json.dump(Categoria , arq , indent=4 ,ensure_ascii=False)
    
    @classmethod
    def categoria_excluir(cls , cid):
        categoria = cls.categoria_converter()
        i = cls.categoria_pesquisa(cid, categoria)
        if i == None:
            return False
        else:
            p= categoria.index(i)
            del categoria[p]
        categoria_arquivo = Path(__file__).parent.parent.parent / "data"/"Categoria.json"
        with open(categoria_arquivo , "w" ,encoding='utf-8') as arq:
            json.dump(categoria , arq , indent=4 ,ensure_ascii=False)
        return True
    
class ProdutoDal:
    arquivo = Path(__file__).parent.parent.parent / "data"/"Produto.json"

class VendaDal:
    arquivo = Path(__file__).parent.parent.parent / "data"/"Venda.json"