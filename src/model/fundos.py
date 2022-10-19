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
        self.set_Segmento(segmento)

    def get_Ticker(self):
        return self.ticker

    def get_Nome(self):
        return self.nome
    
    def get_Segmento(self):
        return self.segmento

    def set_Ticker(self, ticker):
        self.ticker = ticker

    def set_Nome(self, nome):
        self.nome = nome

    def set_Segmento(self, segmento):
        self.segmento = segmento

    def toString(self):
        return f'Nome:{self.nome} Segmento:{self.segmento}' 