import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        button1 = Button(text='Button 1')
        button2 = Button(text='Button 2')
        layout.add_widget(button1)
        layout.add_widget(button2)
        return layout

if __name__ == '__main__':
    MyApp().run()
