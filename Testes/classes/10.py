# composição

class Motor:
    def ligar(self):
        print("Motor ligado!")

class Carro:
    def __init__(self):
        self.motor = Motor()  # Composição

    def dirigir(self):
        self.motor.ligar()
        print("Carro está se movendo!")

carro = Carro()
carro.dirigir()

