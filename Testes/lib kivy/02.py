# label

from kivy.app import App
from kivy.uix.label import Label

class Page(App):
    def build(self):
        return Label(text="Ola kivy")
    
if __name__ == "__main__":
    Page().run()

