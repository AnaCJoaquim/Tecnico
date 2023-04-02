from CadPerfil import *
from Endereco import *
from Veiculo import *
from Document import *
from Seguro import *
import os

os.system("cls")
print("Bem vindo ao sistema do Detran\nRealize seu cadastro para começar:")
P = Cadastro(input("Insira seu nome: "), 
        input("Insira seu cpf: "),
        input("Insira seu rg: "),
        input("Insira sua data de nascimento: "),
        input("Insira seu gênero: "))
    
E = End(input("Insira o logradouro: "),
        input("Insira o numero: "),
        input("Insira o complemento: "),
        input("Insira o bairro: "),
        input("Insira a cidade: "),
        input("Insira o estado: "),
        input("Insira o CEP: "),)

while True:
    choice = input(f"Olá {P.nome}, o que deseja fazer agora?\n[1]Fazer cadastro do carro\n[2]Fazer cadastro do seguro\n[3]Fazer cadastro da documentação\n[4]Calcular IPVA\n[5]Sair")
    choice = int(choice)
    if choice == 1:
        os.system("cls")
        V = Veic(input("Insira a marca do carro:"),
                input("Insira o modelo do carro:"),
                input("Insira o tipo do carro:"),
                input("Insira o valor do carro:"),
                input("Insira o ano de fabricação do carro:"),
                input("Insira o ano do modelo do carro:"),
                input("Insira o combustível do carro:"))
    elif choice == 2:
        os.system("cls")
        S = Seguro(input("Insira o logradouro de trabalho: "),
                   input("Insira o numero: "),
                   input("Insira o complemento: "),
                   input("Insira o bairro: "),
                   input("Insira a cidade: "),
                   input("Insira o estado: "),
                   input("Insira o CEP: "),
                   input("Insira os quilômetro rodados por dia: "),
                   input("Insira a garagem: "))
        print(f"A expectativa do valor de seguro do carro é de: {S.valSeg()}")
    elif choice == 3:
         os.system("cls")
         D = Documentacao(input("Insira sua CNH: "),
                          input("Insira o número do renavam: "),
                          input("Insira o número da placa: "),
                          input("Insira o número do IPVA: "))
    elif choice == 4:
        os.system("cls")
        try: 
            print(f"O valor do IPVA do carro está em R${V.IPVA()}\n")
        except:
            print("Parece que seu carro ainda não está cadastrado, tente fazer isso primeiro :)")
    elif choice == 5:
        os.system("cls")
        print("Deslogando do sistema...")
        break
    else:
        print("Essa opção parece não existir, tente novamente")