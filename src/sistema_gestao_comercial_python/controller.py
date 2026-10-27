import dal
import model
import utilidades


class PessoaController:

    @classmethod
    def cadastrar(cls , nome , cpf):
        if dal.PessoaDal.pesquisa(cpf) is not None:
            return False
        if utilidades.validar_cpf(cpf) == True and utilidades.validar_nome(nome) ==True:
            dal.PessoaDal.salvar(model.Pessoa(nome , cpf))
            return True
        else: return False
        
    @classmethod
    def pesquisar(cls ,cpf:str):
        return dal.PessoaDal.pesquisa(cpf)

    @classmethod
    def editar(cls , lupa , nome , cpf):
        if utilidades.validar_cpf(cpf) == True and utilidades.validar_nome(nome) == True:
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
        if utilidades.validar_nome(nome) ==True and utilidades.validar_cpf(cpf) ==True:
            dal.FornecedorDal.fornecedor_salvar(model.Fornecedor(nome , cpf , fproduto))
            return True
        else: return False

    @classmethod
    def pesquisar_fornecedor(cls ,cpf:str):
        return dal.FornecedorDal.fornecedor_pesquisa(cpf)

    @classmethod
    def editar_fornecedor(cls ,lupa ,nome , cpf ,fproduto):
        if utilidades.validar_nome(nome) == True and utilidades.validar_cpf(cpf) == True:
            dal.FornecedorDal.fornecedor_editar(lupa ,nome , cpf , fproduto)
            return True
        else: return False

    @classmethod
    def excluir_fornecedor(cls ,cpf):
        if dal.FornecedorDal.fornecedor_excluir(cpf) == True:  # noqa: SIM103
            return True
        else:return False

class CategoriaController:
    def criar_cid():
        while True:
            cid = utilidades.criar_id()
            if dal.CategoriaDal.categoria_pesquisa(cid) == None:
                return cid

    @classmethod
    def cadastrar_categoria(cls , nome , cpf):
        cid = cls.criar_cid()
        dal.CategoriaDal.categoria_salvar(model.Categoria(nome , cpf))
        return cid

    @classmethod
    def pesquisa_categoria(cls , cid:str):
        return dal.CategoriaDal.categoria_pesquisa(cid)

    @classmethod
    def editar_categoria(cls ,lupa ,categoria , cid):
        dal.CategoriaDal.categoria_editar(lupa ,categoria , cid)
        return True

    @classmethod
    def excluir_categoria(cls ,cid):
        if dal.CategoriaDal.categoria_excluir(cid) == True:  # noqa: SIM103
            return True
        else:return False


