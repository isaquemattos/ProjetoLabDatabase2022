
# #
# Falta corrigir essa class 
# #

class endrecos():

    def __init__(self, emrpeendimento, endereco, bairro, cidade, area_bruta, nome, ticker) -> None:
        self.empreendimento = emrpeendimento
        self.endereco = endereco
        self.bairro = bairro
        self.cidade = cidade 
        self.area_bruta = area_bruta
        

    def get_Empreendimento(self):
        return self.empreendimento

    def get_Endereco(self):
        return self.endereco

    def get_Bairro(self):
        return self.bairro

    def get_Cidade(self):
        return self.cidade
    
    def get_Area_Bruta(self):
        return self.area_bruta

    def set_Empreendimento(self, empreendimento):
        self.empreendimento = empreendimento

    def set_Endereco(self, endereco):
        self.endereco = endereco

    def set_Bairro(self, bairro):
        self.bairro = bairro

    def set_Cidade(self, cidade):
        self.cidade = cidade
    
    def set_Area_Bruta(self, area_bruta):
        self.area_bruta = area_bruta

    def toString(self):
        return f'Empreendimento: {self.empreendimento} Endereço {self.endereco} Bairro {self.bairro} Cidade: {self.cidade} Area Bruta: {self.area_bruta}'