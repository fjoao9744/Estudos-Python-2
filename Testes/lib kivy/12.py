# screen manager

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition

manager = ScreenManager(transition=FadeTransition())

class HomeScreen(Screen):
    def on_enter(self):
        lbl = Label(text="Home")
        btn = Button(text="entrar", size_hint=(0.2, 0.1), pos_hint={"center_x":0.5, "center_y":0.4})
        btn.bind(on_release=self.go_to_main)
        
        self.add_widget(lbl)
        self.add_widget(btn)
        
    def go_to_main(self, instance):
        manager.current = "main"
        

manager.add_widget(HomeScreen(name="home"))

class MainScreen(Screen):
    def on_enter(self):
        lbl = Label(text="Bem vindo!")
        self.add_widget(lbl)

manager.add_widget(MainScreen(name="main"))

class app(App):
    def build(self):
        return manager
    
if __name__ == "__main__":
    app().run()