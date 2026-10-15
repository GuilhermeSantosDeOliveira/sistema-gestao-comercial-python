import controller


def pessoas():
    while True:
        print("----MENU DE PESSOAS----")
        print("--digite 1 para pesquisar uma pessoa--")
        print("--digite 2 para cadastrar uma pessoa--")
        print("--digite 3 para editar uma pessoa--")
        print("--digite 4 para excluir uma pessoa--")
        print("--digite 0 para sair do menu de pessoas--")
        desicao = int(input("digite o numero desejado : "))
        if desicao == 0:
            break
        while True:
            if desicao not in[1 ,2 ,3,4,0]:
                print("numero invalido , você retornara ao menu de pessoas")
                break
            elif desicao == 1:
                cpf = input("pesquise pelo cpf: ")
                r = controller.PessoaController.pesquisar(cpf)
                if r == None:
                    print("não conseguimos encontrar ninguem com esse cpf")
                else:
                    print(f"o nome é {r["nome"]} e o cpf é {r["cpf"]}")
                    break
            elif desicao == 2:
                nome = input("digite o nome que deseja cadastrar: ")
                cpf = (input("digite o cpf da pessoa que deseja cadastrar: "))
                confirme = int(input(f"verifique as informações:\n o nome é : {nome} \n o cpf é : {cpf} \n digite 1 para confirmar ou 2 para  recusar: "))
                if confirme == 1:
                    if controller.PessoaController.cadastrar(nome , cpf) == True:
                        print(f"o nome: {nome} pertencente ao cpf: {cpf} foi cadastrado com sucesso")
                    else:
                        print("o cadastro falhou")
                elif confirme==2:
                    print("OK! , você está sendo redirecionado para o Menu pessoas")
                    break
            elif desicao == 3:
                cpf = str(input("procure a pessoa que deseja fazer a edição pelo cpf: "))
                lupa = controller.PessoaController.pesquisar(cpf)
                desicao = int(input(f"a pessoa que encontramos é {lupa["nome"]} pertencente ao cpf {lupa["cpf"]} é essa mesmo que deseja editar? 1 para sim e 2 para não : "))
                if desicao == 2:
                    break
                elif desicao ==1:
                    nome = input("digite um novo nome: ")
                    cpf = input("digite um novo cpf: ")
                    if controller.PessoaController.editar(lupa , nome , cpf) == True:
                        print("cadastro alterado com sucesso")
                        break
            elif desicao == 4:
                cpf = input("digite um cpf para procurar a pessoa que deseja deletar o cadastro: ")
                lupa = controller.PessoaController.pesquisar(cpf)
                if lupa == None:
                    print("não encontramos a pessoa desejada , você será redirecionado para o Menu pessoas")
                    break
                print(f"a pessoa que achamos é {lupa["nome"]} pertencente ao cpf: {lupa["cpf"]}")
                desicao = int(input("essa é a pessoa que deseja deletar? 1 para Sim e 2 para Não : "))
                if desicao == 1:
                    if controller.PessoaController.excluir(cpf) == True:
                        print("cadastro deletado com sucesso!")
                        break
                elif desicao ==2:
                    print("ok! você será redirecionado para o menu pessoas")
                    break


pessoas()