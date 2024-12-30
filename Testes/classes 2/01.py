# herança multiplas

class A:
    @staticmethod
    def metodoA():
        print("a")
        
    @staticmethod
    def ver():
        print("Estou na classe A")
        
class B:
    @staticmethod
    def metodoB():
        print("b")
    
    @staticmethod
    def ver():
        print("Estou na classe B")
        
class C(A, B): # vai herdar tudo das outras classes
    @staticmethod
    def metodoC():
        print("c")
        
c = C()
c.metodoA() #metodo herdado da classe A
c.metodoB() #metodo herdado da classe B
c.metodoC()

c.ver() # mostra a primeira pq ela vem primeiro na herança