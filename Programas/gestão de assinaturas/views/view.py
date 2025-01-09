import __init__
from models.database import engine
from models.model import Subscription, Payments
from sqlmodel import Session, select
from datetime import date, datetime

class SubscriptionService:
    def __init__(self, engine):
        self.engine = engine
        
    def create(self, subscription: Subscription):
        with Session(self.engine) as session:
            session.add(subscription)
            session.commit()
            return subscription
        
    def list_all(self):
        with Session(self.engine) as session:
            statement = select(Subscription)
            
            result = session.exec(statement).all()
            
            return result
    
    def _has_pay(self, results):
        for result in results:
            if result.date.month == date.today().month:
                return True
        return False
                
    def pay(self, subscription: Subscription):
        with Session(self.engine) as session:
            statement = select(Payments).join(Subscription).where(Subscription.empresa == subscription.empresa)
            results = session.exec(statement).all()
                    
            if self._has_pay(results=results):
                question = input("Você ja pagou essa conta esse mes, deseja pagar novamente? Y ou N: ")
                
                if not question.upper() == "Y":
                    return
                
            pay = Payments(subscription_id=subscription.id, date=date.today()) # type: ignore
                
            session.add(pay)
            session.commit()
            
    def total_value(self):
        with Session(self.engine) as session:
            statement = select(Subscription)
            results = session.exec(statement).all()
            
        total = 0
        
        for result in results:
            total += result.valor
            
        return float(total)
    
    def delete(self, id):
        with Session(self.engine) as session:
            statement = select(Subscription).where(Subscription.id == id)
            result = session.exec(statement).one()
            session.delete(result)
            
            session.commit()
            
    def _get_last_month(self):
        today = datetime.now()
        year = today.year
        month = today.month
        
        last_months = []
        
        for _ in range(12):
            last_months.append((month, year))
            
            month -= 1
            if month == 0:
                month = 12
                year -= 1
        
        return last_months[::-1]
    
    def _get_values_for_month(self, last_months):
        with Session(self.engine) as session:
            statement = select(Payments)
            results = session.exec(statement).all()
            
            value_for_months = []
            
            for _ in last_months:
                value = 0
                for result in results:
                    if result.date.month == _[0] and result.date.year == _[1]:
                        value += float(result.subscription.valor)
                        
                value_for_months.append(value)
                    
            return value_for_months
            
    def gen_chart(self):
        last_months = self._get_last_month()
        values_for_month = self._get_values_for_month(last_months)
        
        import matplotlib.pyplot as plt
                
        plt.plot([values[0] for values in last_months], values_for_month)
        
        plt.show()
        
        
# ss = SubscriptionService(engine)

# subscription = Subscription(empresa='CursoEmVideo', site='cursoemvideo.com', data_assinatura=date.today(), valor=39) # type: ignore

'''assinaturas = ss.list_all()
for i, value in enumerate(assinaturas):
    print(f"{i} -> {value.empresa}")
    
x = int(input("Qual assinatura você deseja pagar? "))

ss.pay(assinaturas[x])'''
