import dal
import model

class PessoaController:
    @classmethod
    def pesquisar(cls ,cpf):
        return dal.PessoaDal.pesquisa(cpf)


