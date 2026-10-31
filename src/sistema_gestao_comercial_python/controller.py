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
    def cadastrar_categoria(cls , categoria):
        cid = cls.criar_cid()
        dal.CategoriaDal.categoria_salvar(model.Categoria(categoria , cid))
        return True

    @classmethod
    def pesquisa_categoria(cls , cid:str):
        return dal.CategoriaDal.categoria_pesquisa(cid)

    @classmethod
    def editar_categoria(cls ,lupa ,categoria):
        dal.CategoriaDal.categoria_editar(lupa ,categoria)
        return True

    @classmethod
    def excluir_categoria(cls ,cid):
        if dal.CategoriaDal.categoria_excluir(cid) == True:
            while True:
                x = dal.ProdutoDal.exclusao(cid)
                if x == False:
                    break
                else:
                    pass
            return True
        else:return False

class ProdutoController:
    def criar_pid():
        while True:
            pid = utilidades.criar_id()
            if dal.ProdutoDal.produto_pesquisa(pid) == None:
                return pid
            
    @classmethod
    def cadastrar_produto(cls ,  produto , quantidade , valor , cp):
        pid = cls.criar_pid()
        x = dal.CategoriaDal.categoria_pesquisa(cp)
        if x == None:
            return False
        elif x != None:
            dal.ProdutoDal.produto_salvar(model.Produto(produto , quantidade , valor , pid , cp))
            return True

    @classmethod
    def pesquisa_produto(cls , pid:str):
        return dal.ProdutoDal.produto_pesquisa(pid)

    @classmethod
    def editar_produto(cls ,lupa ,produto , quantidade, valor ,cp):
        x=dal.CategoriaDal.categoria_pesquisa(cp)
        if x == None:
            return False
        if x !=None:
            dal.ProdutoDal.produto_editar(lupa ,produto , quantidade, valor ,cp)
            return True

    @classmethod
    def excluir_produto(cls ,pid):
        if dal.ProdutoDal.produto_excluir(pid) == True:  # noqa: SIM103
            return True
        else:return False

class FuncionarioController:

    @classmethod
    def cadastrar_funcionario(cls , nome , cpf , setor):
        if dal.FuncionarioDal.funcionario_pesquisa(cpf) is not None:
            return False
        if utilidades.validar_nome(nome) ==True and utilidades.validar_cpf(cpf) ==True:
            dal.FuncionarioDal.salvar(model.Funcionario(nome , cpf , setor))
            return True
        else: return False

    @classmethod
    def pesquisar_funcionario(cls ,cpf:str):
        return dal.FuncionarioDal.funcionario_pesquisa(cpf)

    @classmethod
    def editar_fornecedor(cls ,lupa ,nome , cpf ,setor):
        if utilidades.validar_nome(nome) == True and utilidades.validar_cpf(cpf) == True:
            dal.FuncionarioDal.funcionario_editar(lupa ,nome , cpf , setor)
            return True
        else: return False

    @classmethod
    def excluir_fornecedor(cls ,cpf):
        if dal.FuncionarioDal.funcionario_excluir(cpf) == True:  # noqa: SIM103
            return True
        else:return False

class VendaController:

    def criar_vid():
        while True:
            vid = utilidades.criar_id()
            if dal.VendaDal.pesquisa_venda(vid) == None:
                return vid
            
    @classmethod
    def cadastrar_venda(cls ,  data , pv , qv):
        vid = cls.criar_vid()
        x = dal.ProdutoDal.produto_pesquisa(pv)
        valor = dal.VendaDal.valor(x , qv)
        if x == None:
            return False
        elif x != None:
            if dal.VendaDal.retirada_estoque(x , qv) ==  True:
                dal.VendaDal.salvar_vendas(model.venda(data , pv , qv , valor , vid))
                return True

VendaController.cadastrar_venda("30|10|2026" , "47312" , "5")