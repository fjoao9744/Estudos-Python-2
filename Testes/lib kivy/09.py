# layout dentro de layout

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp

class Page(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=dp(20), spacing=dp(10))
        for c in range(5):
            sub_layout = BoxLayout(orientation="horizontal")
            
            lbl = Label(text=f"Label {c}")
            btn = Button(text=f"button {c}")
            
            sub_layout.add_widget(lbl)
            sub_layout.add_widget(btn)
            
            layout.add_widget(sub_layout)
            
        return layout
    
if __name__ == "__main__":
    Page().run()

