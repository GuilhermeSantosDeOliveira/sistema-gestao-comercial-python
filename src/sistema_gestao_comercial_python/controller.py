import dal
import model
import validar


class PessoaController:

    @classmethod
    def cadastrar(cls , nome , cpf):
        if validar.validar_cpf(cpf) == True and validar.validar_nome(nome) ==True:
            dal.PessoaDal.salvar(model.Pessoa(nome , cpf))
            return True
        else: return False
        
    @classmethod
    def pesquisar(cls ,cpf:str):
        return dal.PessoaDal.pesquisa(cpf)

    @classmethod
    def editar(cls , lupa , nome , cpf):
        dal.PessoaDal.editar(lupa , nome , cpf)
        return True