class Seguro:
    def __init__(self,log_trab,numero,complemento,bairro,cidade,estado,cep,km_dia,garagem):
        self.log_trab = log_trab
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.km_dia = km_dia
        self.garagem = garagem
    def valSeg(self):
        val = 2.780
        return "R$" + val

