# Clock para animations

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):
        self.eventos = []
        
        self.root = FloatLayout(size_hint=(1,1))
        self.btn = Button(text="Mover", size_hint=(0.2,0.1), pos_hint={'x':0, 'y':0.5})
        self.stop_btn = Button(text="Parar", size_hint=(0.2,0.1), pos_hint={'x':0, 'y':0.6})
        
        self.root.add_widget(self.btn)
        self.root.add_widget(self.stop_btn)
        
        self.stop_btn.bind(on_release=self.parar_eventos)
        
        self.btn.bind(on_release=lambda dt: self.eventos.append(Clock.schedule_interval(self.move_button, 1/60))) # 60 FPS
         
        return self.root

    def move_button(self, dt):
        x = self.btn.pos_hint['x'] + 0.01
        if x > 1:
            x = 0
        self.btn.pos_hint = {'x': x, 'y': 0.5}
        
    def parar_eventos(self, *args):
        for e in self.eventos:
            e.cancel()
        self.eventos.clear()

MyApp().run()
