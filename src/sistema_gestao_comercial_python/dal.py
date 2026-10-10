from pathlib import Path
import model

class Pessoa:
    arquivo = Path(__file__).parent.parent.parent / "data"/"Pessoa.json"

class Fornecedor:
    arquivo = Path(__file__).parent.parent.parent / "data"/"Fornecedor.json"

class Funcionario:
    arquivo = Path(__file__).parent.parent.parent / "data"/"Funcionario.json"

class Categoria:
    arquivo = Path(__file__).parent.parent.parent / "data"/"Categoria.json"

class Produto:
    arquivo = Path(__file__).parent.parent.parent / "data"/"Produto.json"

class Venda:
    arquivo = Path(__file__).parent.parent.parent / "data"/"Venda.json"