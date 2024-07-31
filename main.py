import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class ScreenOne(Screen):
    def __init__(self, **kwargs):
        super(ScreenOne, self).__init__(**kwargs)
        self.add_widget(Label(text='This is Screen 1'))

class ScreenTwo(Screen):
    def __init__(self, **kwargs):
        super(ScreenTwo, self).__init__(**kwargs)
        self.add_widget(Label(text='This is Screen 2'))

class ScreenThree(Screen):
    def __init__(self, **kwargs):
        super(ScreenThree, self).__init__(**kwargs)
        self.add_widget(Label(text='This is Screen 3'))

class ScreenFour(Screen):
    def __init__(self, **kwargs):
        super(ScreenFour, self).__init__(**kwargs)
        self.add_widget(Label(text='This is Screen 4'))

class ScreenFive(Screen):
    def __init__(self, **kwargs):
        super(ScreenFive, self).__init__(**kwargs)
        self.add_widget(Label(text='This is Screen 5'))

class ImageButton(ButtonBehavior, Image):
    pass

class MyApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        
        # Add screens to the screen manager
        sm.add_widget(ScreenOne(name='screen1'))
        sm.add_widget(ScreenTwo(name='screen2'))
        sm.add_widget(ScreenThree(name='screen3'))
        sm.add_widget(ScreenFour(name='screen4'))
        sm.add_widget(ScreenFive(name='screen5'))

        # Create the main layout
        layout = BoxLayout(orientation='vertical')

        # Create the navigation bar layout
        nav_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='48dp')
        
        # Function to switch screens
        def switch_to_screen(screen_name):
            sm.current = screen_name
        
        # Create buttons for navigation with images
        button1 = ImageButton(source='images/button1_logo.png', on_release=lambda x: switch_to_screen('screen1'))
        button2 = ImageButton(source='images/button2_logo.png', on_release=lambda x: switch_to_screen('screen2'))
        button3 = ImageButton(source='images/button3_logo.png', on_release=lambda x: switch_to_screen('screen3'))
        button4 = ImageButton(source='images/button4_logo.png', on_release=lambda x: switch_to_screen('screen4'))
        button5 = ImageButton(source='images/button5_logo.png', on_release=lambda x: switch_to_screen('screen5'))
        
        # Add buttons to the navigation layout
        nav_layout.add_widget(button1)
        nav_layout.add_widget(button2)
        nav_layout.add_widget(button3)
        nav_layout.add_widget(button4)
        nav_layout.add_widget(button5)

        # Add the screen manager and navigation layout to the main layout
        layout.add_widget(sm)
        layout.add_widget(nav_layout)
        
        return layout

if __name__ == '__main__':
    MyApp().run()
