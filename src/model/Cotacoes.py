

from model.fundo import Fundos


class Cotacoes ():

    def __init__(self, abertura, fechamento, minimo, maximo, volume_cotas, mes, ticker)  -> None:
        super().__init__(ticker);
        self.__abertura = abertura
        self.__fechamento = fechamento 
        self.__minimo = minimo 
        self.__maximo = maximo
        self.__volume_cotas = volume_cotas
        self.__mes = mes


    def get_Abertura(self):
        return self.__abertura

    def get_Fechamento(self):
        return self.__fechamento

    def get_Minimo(self):
        return self.__minimo

    def get_Maximo(self):
        return self.__maximo
    
    def get_volume_Cotas(self):
        return self.__volume_cotas

    def get_mes(self):
        return self.__mes

    def set_Abertura(self, abertura):
        self.__abertura = abertura

    def set_Fechamento(self, minimo):
        self.__minimo = minimo

    def set_Minimo(self, minimo):
        self.__minimo = minimo

    def set_Maximo (self, maximo):
        self.__maximo = maximo 

    def set_Volume_Cotas(self, volume_cotas):
        self.__volume_cotas = volume_cotas

    def set_Mes(self, mes):
        self.__mes = mes