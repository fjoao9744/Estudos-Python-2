class Pessoa:
    especie = "Humano" # atributo da classe
    
    def __init__(self, nome, idade, sexo) -> None: # atributos da instancia
        self.nome = nome # atributo normal
        self._idade = idade # atributo protegido
        self.__sexo = sexo # atributo privado

