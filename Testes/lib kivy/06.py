# contador

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp

class Page(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=dp(20), spacing=dp(10))
        
        self.cont = 0
        
        self.lbl = Label(text="cliques: ")
        btn = Button(text="aperte!")
        
        btn.bind(on_release=self.click) # type:ignore
        
        layout.add_widget(self.lbl)
        layout.add_widget(btn)
        
        return layout
    
    def click(self, instance): # ou *args
        self.cont += 1
        self.lbl.text = f"cliques: {self.cont}"
    
if __name__ == "__main__":
    Page().run()

