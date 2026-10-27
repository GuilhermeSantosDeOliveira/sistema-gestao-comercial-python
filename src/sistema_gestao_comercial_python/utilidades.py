import random
import re


def validar_cpf(cpf):
    cpf = str(cpf)
    if len(cpf)!=11:
        return False
    if cpf == cpf[0]*11:
        return False
    soma1 = 0
    for i in range(9):
        soma1 += int(cpf[i]) * (10 - i)
    resto1 = soma1%11
    
    digito1 = 0 if resto1 < 2 else 11 - resto1

    soma2 = 0
    
    for i in range(10):
        soma2 += int(cpf[i]) * (11 - i)
    
    resto2 = soma2 % 11
    digito2 = 0 if resto2 < 2 else 11 - resto2

    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:  # noqa: SIM103
        return True
    return False

def validar_nome(nome: str) -> bool:

    nome = nome.strip()

    partes = nome.split()
    if len(partes) < 2:
        return False 
        
    if len(nome) < 5:
        return False

    padrao = r"^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ'\s]+$"
    
    if not re.match(padrao, nome):  # noqa: SIM103
        return False
        
    return True

def criar_id():
    id = f"{random.randint(0 , 99999):05d}"
    return id

