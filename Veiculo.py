class Carro:
    def __init__(self,ano,tipo,modelo,comb,valor): 
        self.ano = ano
        self.tipo = tipo
        self.modelo = modelo
        self.comb = comb
        self.valor = valor
    
    def IPVA(self):
        print(f"O valor do IPVA é: R${float(self.valor)*0.04}")

    def mostrar(self):
        print(f"ano: {self.ano}\ntipo: {self.tipo}\nmodelo: {self.modelo}\ncombustível: {self.comb}\nvalor: {self.valor}\n    ")


c = Carro(input("Digite o ano do carro: "),
        input("Digite o tipo do carro: "),
        input("Digite o modelo do carro: "),
        input("Digite o combustível do carro: "),
        input("Digite o valor do carro: "))

c.mostrar()
c.IPVA()