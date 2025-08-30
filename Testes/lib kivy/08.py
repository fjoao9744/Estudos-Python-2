# metodos extras

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp

class Page(App):
    def on_start(self):
        print("abrindo a tela")
        
    def build(self):
        print("na tela")
        
        return ""
    
    def on_stop(self):
        print("fechando a tela")
    
if __name__ == "__main__":
    Page().run()

