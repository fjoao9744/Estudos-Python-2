class Pessoa:
    def __init__(self, nome, idade, sexo = "I"):
        self.nome: str = nome.capitalize()
        self.idade: int = idade
        self.sexo: str = sexo.upper()[0]
        self.livros = []
        
    def apresentar(self):
        match self.sexo:
            case "I":
                print(f"Ola! meu nome é {self.nome} e eu tenho {self.idade} anos!")
                
            case "M":
                print(f"Ola! meu nome é {self.nome} eu sou um homem e eu tenho {self.idade} anos!")
                
            case "F":
                print(f"Ola! meu nome é {self.nome} eu sou uma mulher e eu tenho {self.idade} anos!")
                
    def adicionar_livro(self, livro: object):
        self.livros.append(livro)
        
    def mostrar_livros(self):
        if len(self.livros) == 0:
            print(f"{self.nome} não possui nenhum livro. ")
            return
        
        for i, livro in enumerate(self.livros):
            print(f"Livro {i}: ")
            livro.info()
        

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura

class Livro(Retangulo):
    def __init__(self, titulo, autor, ano_publicacao, medidas = [0, 0]):
        super().__init__(base= medidas[0], altura= medidas[1])
        self.titulo: str = titulo
        self.autor: str = autor
        self.ano_publicacao: int = ano_publicacao
        
    def info(self):
        print(f"""titulo:{self.titulo}
autor: {self.autor} 
ano de publicação: {self.ano_publicacao}""" ) 
        
        if self.base != 0 and self.altura != 0:
            print(f"medidas: {self.base}x{self.altura}")
        
jorge = Pessoa("jorge", 22, "M")

jorge.apresentar()

harry_potter = Livro("harry potter", "J. K. Rowling", 1998)

print(harry_potter.info())
print(harry_potter.area())

pequeno_prince = Livro("Pequeno principe", "Antoine de Saint-Exupéry", 1943, medidas=[14, 21])

print(pequeno_prince.info())
print(pequeno_prince.area())