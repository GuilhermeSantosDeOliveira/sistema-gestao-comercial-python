import json
from pathlib import Path

import model


class PessoaDal:
    @classmethod
    def converter(cls):
        arquivo = Path(__file__).parent.parent.parent / "data"/"Pessoa.json"
        with open(arquivo , "r" ,encoding='utf-8') as arq:
            Pessoa = json.load(arq)
            return Pessoa

    @classmethod
    def salvar(cls , pessoa:model.Pessoa):
        arquivo = Path(__file__).parent.parent.parent / "data"/"Pessoa.json"
        with open(arquivo , "w" ,encoding='utf-8') as arq:
            json.dump(arq,indent=4 ,ensure_ascii=False)

    @classmethod
    def pesquisar(cls):
        pessoa = cls.converter()
    

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