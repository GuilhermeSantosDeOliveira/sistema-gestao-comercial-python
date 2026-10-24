import dal
import model
import validar


class PessoaController:

    @classmethod
    def cadastrar(cls , nome , cpf):
        if dal.PessoaDal.pesquisa(cpf) is not None:
            return False
        if validar.validar_cpf(cpf) == True and validar.validar_nome(nome) ==True:
            dal.PessoaDal.salvar(model.Pessoa(nome , cpf))
            return True
        else: return False
        
    @classmethod
    def pesquisar(cls ,cpf:str):
        return dal.PessoaDal.pesquisa(cpf)

    @classmethod
    def editar(cls , lupa , nome , cpf):
        if validar.validar_cpf(cpf) == True and validar.validar_nome(nome) == True:
            dal.PessoaDal.editar(lupa , nome , cpf)
            return True
        else:return False

    @classmethod
    def excluir(cls , cpf):
        if dal.PessoaDal.excluir(cpf) == True:  # noqa: SIM103
            return True
        else:return False

class FornecedorController:
    @classmethod
    def cadastrar_fornecedor(cls , nome , cpf , fproduto):
        if dal.FornecedorDal.fornecedor_pesquisa(cpf) is not None:
            return False
        if validar.validar_nome(nome) ==True and validar.validar_cpf(cpf) ==True:
            dal.FornecedorDal.fornecedor_salvar(model.Fornecedor(nome , cpf , fproduto))
            return True
        else: return False

    @classmethod
    def pesquisar_fornecedor(cls ,cpf:str):
        return dal.FornecedorDal.fornecedor_pesquisa(cpf)

    @classmethod
    def editar_fornecedor(cls ,lupa ,nome , cpf ,fproduto):
        if validar.validar_nome(nome) == True and validar.validar_cpf(cpf) == True:
            dal.FornecedorDal.fornecedor_editar(lupa ,nome , cpf , fproduto)
            return True
        else: return False

    @classmethod
    def excluir_fornecedor(cls ,cpf):
        if dal.FornecedorDal.fornecedor_excluir(cpf) == True:  # noqa: SIM103
            return True
        else:return False

