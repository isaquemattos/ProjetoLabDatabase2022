from model.fundos import Fundos


# #
# Falta corrigir essa class 
# se não dar tempo retirar o implementação 
# #
class relatorios(Fundos):

    def __init__(self, arquivo, mes, ticker, nome) -> None:
        super().__init__(nome, ticker)
        self.__arquivo = arquivo
        self.__mes = mes


    def get_Arquivo(self):
        return self.__arquivo

    def ger_Mes(self):
        return self.__mes

    def set_Mes(self, mes):
        self.__mes

    def set_Arquivo(self, arquivo):
        self.__arquivo = arquivo

    def toString(self):
        return f'Arquivo: {self.__arquivo} Mês: {self.__mes}'
    