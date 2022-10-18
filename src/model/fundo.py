from typing_extensions import Self


class Fundos:

    def __init__(self, nome, segmento) -> None:
        self.__ticker
        self.__nome = nome
        self.__segmento = segmento

    def __init__(self, nome)-> None:
        Self.__nome = nome

    def get_Nome(self):
        return self.__nome
    
    def get_Segmento(self):
        return self.__segmento

    def set_Nome(self, nome):
        self.__nome = nome

    def set_Segmento(self, segmento):
        self.__segmento = segmento

    def toString(self):
        return f'Nome:{self.__nome} Segmento:{self.__segmento}' 