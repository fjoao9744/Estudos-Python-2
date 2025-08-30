# .kv

from kivy.app import App
from kivy.properties import NumericProperty

class ContadorApp(App):
    contador = NumericProperty(0)
        
    def click(self):
        self.contador += 1
    
if __name__ == "__main__":
    ContadorApp().run()

