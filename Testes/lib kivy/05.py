# label argumentos

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp, sp

class Page(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=dp(20), spacing=dp(10))
        
        label = Label(text="[b]smogon[/b]", 
                      font_size=sp(20), 
                      color=[0, 1, 0, 1], # [R, G, B, A]
                      halign="left", # 'left', 'center', 'right', 'justify', 'auto'
                      valign="top", # 'bottom', 'middle', 'center', 'top'
                      size_hint=(1, 1), # (largura, altura) # controla o tamanho em relação ao pai
                      pos_hint={'center_x':0.5, 'center_y':0.5}, # controla a posição relativa ao pai
                      markup=True # habilita o [b], [i]
                      )
        
        label.bind(size=label.setter('text_size')) # type:ignore
        
        layout.add_widget(label)
        
        return layout
    
if __name__ == "__main__":
    Page().run()

