import datetime
from model.fundos import Fundo

############################################################
#Programa model.Cotacoes
#AUTOR.......: Daniel Marinho 
#DATA........: 18/10/2022
#DESCRICAO...: class Cotacao  
############################################################

class Cotacao():

    def __init__(self, abertura:int=None, fechamento:int=None, 
                       minimo:int=None, maximo:int=None, volume_cotas:int=None, mes:datetime=None, fundo:Fundo=None)  -> None:
        self.set_fundo(fundo) # class Fundos
        self.set_Abertura(abertura)
        self.set_Fechamento(fechamento) 
        self.set_Minimo(minimo) 
        self.set_Maximo(maximo)
        self.set_Volume_Cotas(volume_cotas)
        self.set_Mes(mes)


    def get_Abertura(self) -> int:
        return self.abertura

    def get_Fechamento(self):
        return self.fechamento

    def get_Minimo(self):
        return self.minimo

    def get_Maximo(self):
        return self.maximo
    
    def get_Volume_Cotas(self):
        return self.volume_cotas

    def get_Mes(self):
        return self.mes
    
    def set_Fundo(self, fundo:Fundo) -> Fundo:
        self.fundo = fundo
    
    def set_Abertura(self, abertura):
        self.abertura = abertura

    def set_Fechamento(self, fechamento):
        self.fechamento = fechamento

    def set_Minimo(self, minimo):
        self.minimo = minimo

    def set_Maximo (self, maximo):
        self.maximo = maximo 

    def set_Volume_Cotas(self, volume_cotas):
        self.volume_cotas = volume_cotas

    def set_Mes(self, mes):
        self.mes = mes