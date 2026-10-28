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
    def converter():
            funcionario_arquivo = Path(__file__).parent.parent.parent / "data"/"Funcionario.json"
            with open(funcionario_arquivo, "r" ,encoding='utf-8') as arq:
                funcionario = json.load(arq)
                return funcionario

    @classmethod
    def salvar(cls , funcionario:model.Funcionario):
        funcionario_arquivo = Path(__file__).parent.parent.parent / "data"/"Funcionario.json"
        Funcionario = cls.converter()
        f = {"nome":funcionario.nome , "cpf" :funcionario.cpf , "setor":funcionario.setor}
        Funcionario.append(f)
        with open(funcionario_arquivo , "w" ,encoding='utf-8') as arq:
            json.dump(Funcionario,arq,indent=4 ,ensure_ascii=False)

    @classmethod
    def funcionario_pesquisa(cls , cpf:str , lista=None):
        if lista == None:
            lista = cls.converter()
        for i in lista:
            if i["cpf"] == cpf:
                    return i

    @classmethod
    def funcionario_editar(cls , lupa , nome , cpf, setor):
        funcionario = cls.converter()
        i = cls.funcionario_pesquisa(lupa["cpf"] , funcionario)
        if i == None:
            return
        else:
            i["nome"] = nome
            i["cpf"] = cpf
            i["setor"]= setor
        funcionario_arquivo = Path(__file__).parent.parent.parent / "data"/"Funcionario.json"
        with open(funcionario_arquivo , "w" ,encoding='utf-8') as arq:
            json.dump(funcionario , arq , indent=4 ,ensure_ascii=False)

    @classmethod
    def funcionario_excluir(cls , cpf):
        funcionario = cls.converter()
        i = cls.funcionario_pesquisa(cpf, funcionario)
        if i == None:
            return False
        else:
            f= funcionario.index(i)
            del funcionario[f]
        funcionario_arquivo = Path(__file__).parent.parent.parent / "data"/"Funcionario.json"
        with open(funcionario_arquivo , "w" ,encoding='utf-8') as arq:
            json.dump(funcionario , arq , indent=4 ,ensure_ascii=False)
        return True

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
    def categoria_editar(cls , lupa , categoria):
        Categoria = cls.categoria_converter()
        i = cls.categoria_pesquisa(lupa["cid"] , Categoria)
        if i == None:
            return
        else:
            i["categoria"] = categoria
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
    def converter():
            produto_arquivo = Path(__file__).parent.parent.parent / "data"/"Produto.json"
            with open(produto_arquivo , "r" ,encoding='utf-8') as arq:
                produto = json.load(arq)
                return produto
    @classmethod
    def produto_salvar(cls , produto:model.Produto):
        produto_arquivo = Path(__file__).parent.parent.parent / "data"/"Produto.json"
        Produto = cls.converter()
        p = {"produto":produto.produto , "quantidade" :produto.quantidade , "valor" : produto.valor , "pid": produto.pid , "categoria": produto.cp}
        Produto.append(p)
        with open(produto_arquivo , "w" ,encoding='utf-8') as arq:
            json.dump(Produto,arq,indent=4 ,ensure_ascii=False)

    @classmethod
    def produto_pesquisa(cls , pid:str , lista=None):
        if lista == None:
            lista = cls.converter()
        for i in lista:
            if i["pid"] == pid:
                return i

    @classmethod
    def produto_editar(cls , lupa , produto , quantidade, valor ,cp):
        Produto = cls.converter()
        i = cls.produto_pesquisa(lupa["pid"] , Produto)
        if i == None:
            return
        else:
            i["produto"] = produto
            i["quantidade"] = quantidade
            i["valor"]= valor
            i["cp"]=cp
        produto_arquivo = Path(__file__).parent.parent.parent / "data"/"Produto.json"
        with open(produto_arquivo , "w" ,encoding='utf-8') as arq:
            json.dump(Produto , arq , indent=4 ,ensure_ascii=False)

    @classmethod
    def produto_excluir(cls , pid):
        produto = cls.converter()
        i = cls.produto_pesquisa(pid, produto)
        if i == None:
            return False
        else:
            p= produto.index(i)
            del produto[p]
        funcionario_arquivo = Path(__file__).parent.parent.parent / "data"/"Produto.json"
        with open(funcionario_arquivo , "w" ,encoding='utf-8') as arq:
            json.dump(produto , arq , indent=4 ,ensure_ascii=False)
        return True

    #essa é uma parte do codigo da classe produto que remete diretamente a classe categoria e serve para auxilio em uma parte do codigo da controller
    @classmethod
    def lista_exclusao(cls , cp , lista=None):
        if lista == None:
            lista = cls.converter()
        for i in lista:
            if i["cp"] == cp:
                return i
    @classmethod
    def exclusao(cls , cp):
        produto = cls.converter()
        i = cls.lista_exclusao(cp, produto)
        if i == None:
            return False
        else:
            p= produto.index(i)
            del produto[p]
        funcionario_arquivo = Path(__file__).parent.parent.parent / "data"/"Produto.json"
        with open(funcionario_arquivo , "w" ,encoding='utf-8') as arq:
            json.dump(produto , arq , indent=4 ,ensure_ascii=False)
        return True


class VendaDal:
    arquivo = Path(__file__).parent.parent.parent / "data"/"Venda.json"


