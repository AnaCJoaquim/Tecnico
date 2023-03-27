class Veic:
    def __init__(self,marca,modelo,tipo,valor,ano_fab, ano_modelo,comb): 
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.valor = valor
        self.ano_fab = ano_fab
        self.ano_modelo = ano_modelo
        self.comb = comb

    def IPVA(self):
        IPVA = int(self.valor) +(int(self.valor)*0.04)
        return IPVA

