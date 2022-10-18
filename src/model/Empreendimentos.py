from model.fundo import Fundos


class empreendimentos(Fundos):

    def __init__(self, segmento, nome) -> None:
        super.__init__(nome, segmento)

    def get_Nome(self):
        return self.__nome

    def get_Segmento(self):
        return self.__segmento

    def set_Nome(self, nome):
        self.__nome =  nome

    def set_Segmento(self, segmento):
        self.__segmento = segmento

    def toString (self):
        return f'Nome: {self.__nome} Segmento: {self.__nome}'