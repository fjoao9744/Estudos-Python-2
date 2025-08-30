# teste de widgets simples

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage
from kivy.uix.progressbar import ProgressBar
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class Page(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20)
        
        label = Label(text="label")
        layout.add_widget(label)
        
        button = Button(text="button")
        layout.add_widget(button)
        
        tbutton = ToggleButton(text="tbutton")
        layout.add_widget(tbutton)
        
        image = Image(source='download.png')
        layout.add_widget(image)
        
        asyncImage = AsyncImage(source='https://br.neurochispas.com/wp-content/uploads/2022/08/Vertices-de-um-dodecaedro-600x475.webp')
        layout.add_widget(asyncImage)
        
        progress = ProgressBar(max=100, value=66)
        layout.add_widget(progress)
        
        slider = Slider(min=0, max=100, value=50)
        layout.add_widget(slider)

        switch = Switch()
        layout.add_widget(switch)

        check = CheckBox()
        layout.add_widget(check)
        
        texti = TextInput()
        layout.add_widget(texti)
        
        return layout
    
if __name__ == "__main__":
    Page().run()

