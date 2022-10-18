from model.fundo import Fundos 


class endrecos(Fundos):

    def __init__(self, emrpeendimento, endereco, bairro, cidade, area_bruta, nome, ticker) -> None:
        super.__init__(nome, ticker)
        self.__empreendimento = emrpeendimento
        self.__endereco = endereco
        self.__bairro = bairro
        self.__cidade = cidade 
        self.__area_bruta = area_bruta
        

    def get_Empreendimento(self):
        return self.__empreendimento

    def get_Endereco(self):
        return self.__endereco

    def get_Bairro(self):
        return self.__bairro

    def get_Cidade(self):
        return self.__cidade
    
    def get_Area_Bruta(self):
        return self.__area_bruta

    def set_Empreendimento(self, empreendimento):
        self.__empreendimento = empreendimento

    def set_Endereco(self, endereco):
        self.__endereco = endereco

    def set_Bairro(self, bairro):
        self.__bairro = bairro

    def set_Cidade(self, cidade):
        self.__cidade = cidade
    
    def set_Area_Bruta(self, area_bruta):
        self.__area_bruta = area_bruta

    def toString(self):
        return f'Empreendimento: {self.__empreendimento} Endereço {self.__endereco} Bairro {self.__bairro} Cidade: {self.__cidade} Area Bruta: {self.__area_bruta}'