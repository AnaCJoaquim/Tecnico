class Cadastro:
    def __init__(self,nome,bairro,cidade,estado):
        self.nome = nome
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado


p = Cadastro(input("Insira seu nome: "), 
            input("Insira seu barirro: "),
            input("Insira sua cidade: "),
            input("Insira seu estado: "))
            