"Função para validar CPF"

from random import randint

def valida_cpf(cpf):
    if len(cpf) != 11:
        while len(cpf) != 11:
            cpf = input("O tamanho do CPF informado é inválido, digite novamente: ")

    dv_informado = cpf[9:]

    if dv_informado == dv(cpf[:-2]): 
        return True
    else:
        return False


def dv1_bruto(cpf):  
    return sum(((i + 2) * int(d) for i, d in enumerate(cpf[::-1])))

def dv1(cpf):
    resultado = dv1_bruto(cpf) * 10 % 11
    return resultado if resultado < 10 else 0

def dv2_bruto(cpf):
    return sum(((i + 3) * int(d) for i, d in enumerate(cpf[::-1])))

def dv2(cpf):
    resultado = (dv2_bruto(cpf) + dv1(cpf) * 2) * 10 % 11
    return resultado if resultado < 10 else 0 

def dv(cpf):
    return str(dv1(cpf)) + str(dv2(cpf))

if __name__ == "__main__":
    valida_cpf()