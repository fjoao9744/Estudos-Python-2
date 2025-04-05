class C:
    x = []
    def add(self, element):
        self.x.append(element)

o1 = C()
o2 = C()
o1.add(1)
o2.add(2)
print(o1.x == [1, 2])
print(o1.x is o2.x)

from dataclasses import dataclass, field

"""@dataclass
class D:
    x: list = []      # This code raises ValueError
    def add(self, element):
        self.x.append(element)
        """
        
#para resolver esse erro tem que o default_factory

@dataclass
class D2:
    x: list = field(default_factory=list) # assim toda vez que a classe for instanciada ela vai criar uma nova instancia

print(D2().x is D2().x)