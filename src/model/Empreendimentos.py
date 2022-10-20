from model.fundos import Fundo

############################################################
#Programa model.Empreendimentos
#AUTOR.......: Daniel Marinho 
#DATA........: 18/10/2022
#DESCRICAO...: class Empreendimento  
############################################################

class Empreendimento():

    def __init__(self, segmento, fundo:Fundo=None) -> None:
        self.set_Segmento(segmento)
        self.set_Fundo(fundo)
        
    def get_Nome(self):
        return self.nome

    def get_Segmento(self):
        return self.segmento

    def set_Nome(self, nome):
        self.nome =  nome

    def set_Segmento(self, segmento):
        self.segmento = segmento

    def set_Fundo(self,fundo:Fundo=None) -> Fundo:
        self.fundo = fundo

    def toString (self):
        return f'Nome: {self.__nome} Segmento: {self.__nome}'