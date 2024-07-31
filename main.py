import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button, ButtonBehavior
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

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
        
        # Create a vertical layout for the screen
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Add a heading
        self.layout.add_widget(Label(text='Notifications', font_size='24sp', size_hint_y=None, height=50))
        
        # Create a scrollable view for notifications
        self.scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - 100))
        self.notifications_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.notifications_layout.bind(minimum_height=self.notifications_layout.setter('height'))
        self.scroll_view.add_widget(self.notifications_layout)
        
        self.layout.add_widget(self.scroll_view)
        self.add_widget(self.layout)
    
    def add_notification(self, message):
        notification = BoxLayout(size_hint_y=None, height=50, padding=10)
        notification.add_widget(Label(text=message))
        close_button = Button(text='Close', size_hint_x=None, width=100)
        close_button.bind(on_release=lambda btn: self.notifications_layout.remove_widget(notification))
        notification.add_widget(close_button)
        self.notifications_layout.add_widget(notification)

class ScreenFive(Screen):
    def __init__(self, **kwargs):
        super(ScreenFive, self).__init__(**kwargs)
        
        # Create a vertical layout for the form
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Add a heading
        layout.add_widget(Label(text='Profile', font_size='24sp', size_hint_y=None, height=50))
        
        # Add form fields
        layout.add_widget(Label(text='Name:'))
        layout.add_widget(TextInput(multiline=False))
        
        layout.add_widget(Label(text='Email:'))
        layout.add_widget(TextInput(multiline=False))
        
        layout.add_widget(Label(text='Phone:'))
        layout.add_widget(TextInput(multiline=False))
        
        layout.add_widget(Label(text='Address:'))
        layout.add_widget(TextInput(multiline=True))
        
        self.add_widget(layout)

class ImageButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(ImageButton, self).__init__(**kwargs)
        with self.canvas.before:
            self.bg_color = Color(1, 1, 1, 1)  # Default white background
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
        
    def _update_rect(self, instance, value):
        self.rect.size = self.size
        self.rect.pos = self.pos
        
    def set_color(self, color):
        with self.canvas.before:
            self.bg_color.r, self.bg_color.g, self.bg_color.b, self.bg_color.a = color

class MyApp(App):
    def build(self):
        # Create the screen manager
        self.sm = ScreenManager()
        
        # Add screens to the screen manager
        self.sm.add_widget(ScreenOne(name='screen1'))
        self.sm.add_widget(ScreenTwo(name='screen2'))
        self.sm.add_widget(ScreenThree(name='screen3'))
        self.sm.add_widget(ScreenFour(name='screen4'))
        self.sm.add_widget(ScreenFive(name='screen5'))

        # Create the main layout
        layout = BoxLayout(orientation='vertical')

        # Create the navigation bar layout
        self.nav_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='48dp')
        
        # Create buttons for navigation with images and white background
        self.buttons = {
            'screen1': ImageButton(source='images/button1_logo.png'),
            'screen2': ImageButton(source='images/button2_logo.png'),
            'screen3': ImageButton(source='images/button3_logo.png'),
            'screen4': ImageButton(source='images/button4_logo.png'),
            'screen5': ImageButton(source='images/button5_logo.png')
        }

        # Add buttons to the navigation layout
        for screen_name, button in self.buttons.items():
            button.bind(on_release=lambda btn, name=screen_name: self.switch_to_screen(name))
            self.nav_layout.add_widget(button)

        # Add the screen manager and navigation layout to the main layout
        layout.add_widget(self.sm)
        layout.add_widget(self.nav_layout)
        
        # Set initial button color
        self.update_button_colors('screen1')

        return layout

    def switch_to_screen(self, screen_name):
        self.sm.current = screen_name
        self.update_button_colors(screen_name)

        # Test notification when switching to screen 4
        if screen_name == 'screen4':
            self.sm.get_screen('screen4').add_notification("New Notification")
            self.sm.get_screen('screen4').add_notification("New Notification")
            self.sm.get_screen('screen4').add_notification("New Notification")
            self.sm.get_screen('screen4').add_notification("New Notification")
            self.sm.get_screen('screen4').add_notification("New Notification")
            self.sm.get_screen('screen4').add_notification("New Notification")
            self.sm.get_screen('screen4').add_notification("New Notification")
            self.sm.get_screen('screen4').add_notification("New Notification")
            self.sm.get_screen('screen4').add_notification("New Notification")
            self.sm.get_screen('screen4').add_notification("New Notification")
            self.sm.get_screen('screen4').add_notification("New Notification")
            self.sm.get_screen('screen4').add_notification("New Notification")
            self.sm.get_screen('screen4').add_notification("New Notification")
            self.sm.get_screen('screen4').add_notification("New Notification")

    def update_button_colors(self, active_screen):
        for screen_name, button in self.buttons.items():
            if screen_name == active_screen:
                button.set_color((0.5, 0.5, 0.5, 1))  # Grey color
            else:
                button.set_color((1, 1, 1, 1))  # White color

if __name__ == '__main__':
    MyApp().run()
