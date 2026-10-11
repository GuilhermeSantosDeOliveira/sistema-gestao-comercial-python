import controller

while True:
    desicao = int(input("digite 1 para pesquisar"))
    if desicao == 1:
        cpf = int(input("pesquise pelo cpf: "))
        r = controller.PessoaController.pesquisar(cpf)
        print(r)
