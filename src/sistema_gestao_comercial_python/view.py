import controller

while True:
    print("----MENU DE PESSOAS----")
    print("--digite 1 para pesquisar uma pessoa--")
    print("--digite 2 para cadastrar uma pessoa--")
    print("--digite 0 para sair do menu de pessoas--")
    desicao = int(input("digite o numero desejado : "))
    if desicao == 0:
        break
    elif desicao == 1:
        cpf = int(input("pesquise pelo cpf: "))
        r = controller.PessoaController.pesquisar(cpf)
        print(f"o nome é {r["nome"]} e o cpf é {r["cpf"]}")
    elif desicao == 2:
        nome = input("digite o nome que deseja cadastrar: ")
        cpf = int(input("digite o cpf da pessoa que deseja cadastrar: "))
        confirme = int(input(f"verifique as informações:\n o nome é : {nome} \n o cpf é : {cpf} \n digite 1 para confirmar ou 2 para  recusar: "))
        if confirme == 1:
            if controller.PessoaController.cadastrar(nome , cpf):
                print(f"o nome: {nome} pertencente ao cpf: {cpf} foi cadastrado com sucesso")
            else:
                print("o cadastro falhou")
        elif confirme==0:
            print("OK! , você está sendo redirecionado para o Menu pessoas")
            break