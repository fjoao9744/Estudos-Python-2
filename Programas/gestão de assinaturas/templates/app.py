import __init__
from views.view import SubscriptionService
from models.database import engine
from models.model import Subscription
from datetime import datetime
from decimal import Decimal

class UI:
    def __init__(self):
        self.subscription_service = SubscriptionService(engine)
        
    def start(self):
        while True:
            print('''
            [1] -> Adicionar assinatura
            [2] -> Remover assinatura
            [3] -> Valor total
            [4] -> Gastos últimos 12 meses
            [5] -> Sair
            ''')

            choice = int(input('Escolha uma opção: '))

            match choice:
                case 1:
                    self.add_subscription()
                case 2:
                    self.delete_subscription()
                case 3:
                    self.total_value()
                case 4:
                    self.subscription_service.gen_chart()
                    #TODO: chamar o metodo pay na interface
                case _:
                    break
                
    def add_subscription(self):
        empresa = str(input("Empresa: "))
        site = str(input("Site: "))
        data_assinatura = datetime.strptime(input("Data de assinatura: "), '%d/%m/%Y')
        valor = Decimal(input("Valor: "))
        
        subscription = Subscription(empresa=empresa, site=site, data_assinatura=data_assinatura, valor=valor) # type: ignore
        self.subscription_service.create(subscription)
        
    def delete_subscription(self):
        subscritions = self.subscription_service.list_all()
        print("Escolha qual assinatura você deseja apagar: ")
        #TODO: quando excluir a assinatura, excluir todos os pagamentos dela
        for value in subscritions:
            print(f"{value.id} -> {value.empresa}")
        choice = int(input("Escolha a assinatura: "))
        
        self.subscription_service.delete(choice)
        print("Assinatura excluida com sucesso")
        
    def total_value(self):
        print(f"seu valor total em assinaturas é: {self.subscription_service.total_value()}")
        
UI().start()