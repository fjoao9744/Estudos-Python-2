class Loja:
    def __init__(self, nome):
        self.__nome = nome.capitalize()
        self.__historico_nome = [nome]
        
        self.estoque = []
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter # Redefine o nome
    def nome(self, novo_nome):
        self.__nome = novo_nome
        self.__historico_nome.append(novo_nome) # Adiciona o novo nome do historico de nomes
        print("O nome da loja foi alterado.")
        
    def restaurar_nome(self):
        print("Historico de nomes: ")
        for i, nome in enumerate(self.__historico_nome):
            print(f"{i}- {nome}")
        
        pergunta = "Para qual nome do histórico de nomes você deseja trocar? (insira o índice): "
        novo_nome = self.perguntar_indice(self.__historico_nome, pergunta, "Por favor, digite um indice valido.")
                
        self.__nome = novo_nome
        self.__historico_nome.append(novo_nome) # Adiciona o novo nome no historico
        
    @staticmethod
    def perguntar_indice(lista, pergunta, exception = ""):
        while True:
            try:
                novo_item = int(input(pergunta))
                novo_item = lista[novo_item]
                return novo_item
            
            except:
                if exception:
                    print(exception)
                continue
    
    def adicionar_produto(self, nome, preco, estoque = 1, detalhes = ""):
        self.estoque.append(Produto(nome, preco, estoque, detalhes))
        
    def vender_produto(self):
        print("Qual item você deseja vender: ")
        for i, produto in enumerate(self.estoque):
            print(f"{i}- {produto._nome}")
            
        pergunta = "Digite o indice do produto que você deseja vender: "
        
        produto = self.perguntar_indice(self.estoque, pergunta, "Por favor, digite um indice valido.")
        
        quantidade = int(input("Qual a quantidade que você deseja vender? "))
        
        if not produto.estoque - quantidade < 0:
            produto.vender(quantidade)
        else:
            print("Não possui essa quantidade no estoque")
            
    def repor_produto(self):
        print("Qual item você deseja repor: ")
        for i, produto in enumerate(self.estoque):
            print(f"{i}- {produto._nome}")
            
        pergunta = "Digite o indice do produto que você deseja repor: "
        
        produto = self.perguntar_indice(self.estoque, pergunta, "Por favor, digite um indice valido.")
        
        quantidade = int(input("Qual a quantidade que você deseja repor? "))
        
        produto.repor(quantidade)
        
    def mostrar_detalhes(self):
        print("Qual item você deseja mostrar detalhes: ")
        for i, produto in enumerate(self.estoque):
            print(f"{i}- {produto._nome}")
            
        pergunta = "Digite o indice do produto que você deseja mostrar detalhes: "
        
        produto = self.perguntar_indice(self.estoque, pergunta, "Por favor, digite um indice valido.")
        
        produto.detalhes()
        
    def alterar_produto(self):
        print("Qual item você deseja alterar: ")
        for i, produto in enumerate(self.estoque):
            print(f"{i}- {produto._nome}")
            
        pergunta = "Digite o indice do produto que você deseja alterar: "
        
        produto = self.perguntar_indice(self.estoque, pergunta, "Por favor, digite um indice valido.")
        
        print("Oque você deseja trocar nesse produto?(digite o indice) ")
        valor = input("1- Nome \n2- preço \n3- estoque \n4- detalhes \nDigite aqui: ")
        
        novo_valor = int(input("Qual vai ser o novo valor? "))
        
        produto.alterar(valor, novo_valor)
        

class Produto:
    def __init__(self, nome, preco, estoque, detalhes):
        self._nome = nome.capitalize()
        self._preco = preco
        self.estoque = estoque
        self._detalhes = detalhes
        
    def vender(self, quantidade = 1):
        if self.estoque:
            self.estoque -= quantidade
        else:
            print("Não possui nenhum desse item no estoque")

    def repor(self, quantidade):
        self.estoque += quantidade

    def detalhes(self):
        print("Detalhes sobre o produto: ")
        print("nome: ", self._nome)
        print("Preço: ", self._preco)
        print("Em estoque: ", self.estoque)
        print("Detalhes: ", self._detalhes)
        
    def alterar(self, valor, novo_valor):
        match valor:
            case 1:
                self._nome = novo_valor
            case 2:
                self._preco = novo_valor
            case 3:
                self.estoque = novo_valor
            case 4:
                self._detalhes = novo_valor

loja = Loja("Atletic")
loja.adicionar_produto("camisa adidas", 4000)
loja.mostrar_detalhes()
