############################################################
#Programa model.Fundos
#AUTOR.......: Daniel Marinho 
#DATA........: 18/10/2022
#DESCRICAO...: class Fundo  
############################################################

class Fundo:

    def __init__(self, nome:str=None, segmento:str=None, ticker:str=None) -> None:
        self.set_Ticker(ticker)        
        self.set_Nome(nome)

    def get_Ticker(self):
        return self.ticker

    def get_Nome(self):
        return self.nome

    def set_Ticker(self, ticker):
        self.ticker = ticker

    def set_Nome(self, nome):
        self.nome = nome

    def toString(self):
        return f'Nome:{self.nome} Segmento:{self.segmento}' 