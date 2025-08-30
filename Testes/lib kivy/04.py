# widgets

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp

class Page(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=dp(20), spacing=dp(10))
        
        label = Label(text="smogon")
        button = Button(text="aperte!")
        
        layout.add_widget(label)
        layout.add_widget(button)
        
        return layout
    
if __name__ == "__main__":
    Page().run()

