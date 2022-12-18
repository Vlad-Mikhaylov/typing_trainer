"""Module with graphical part of the keyboard trainer"""
import kivy
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App

from config import APP_NAME, WINDOW_SIZE, HINT_TEXT, BACKGROUND_COLOR, \
    MINIMUM_WIDTH, MINIMUM_HEIGHT
from utils import log, formSpeed, mostMissButtons

Window.size = WINDOW_SIZE
Window.minimum_width = MINIMUM_WIDTH
Window.minimum_height = MINIMUM_HEIGHT
Window.title = APP_NAME
Window.clearcolor = BACKGROUND_COLOR


class KeyboardTrainApp(App):
    """Main class of gui part of the keyboard trainer"""

    def __init__(self, kt):
        """Initialization of the app.
        Just set the reference to the main logic class of the app.
        """
        super().__init__()
        self.kt = kt
        self.MainLayout = RelativeLayout()
        self.TextLabel = Label(text='',
                               markup=True,
                               color=(.0, .0, .0, 10),
                               font_size=40)
        self.TextInputWidget = TextInput(hint_text=HINT_TEXT, font_size=30)

    def build(self):
        """Start function of the app.
        Draw the start menu.
        """
        self.makeMenu()

        LabelWidget = Label(text=APP_NAME,
                            pos_hint={'top': 1.3},
                            font_size=50,
                            color=(.2, .2, .2, 1))
        self.MainLayout.add_widget(LabelWidget)

        return self.MainLayout

    def newPhrase(self, KeyboardInput, text):
        """Begins a new phase of the letter input"""
        self.MainLayout.clear_widgets()
        self.TextLabel.text = text

        self.MainLayout.add_widget(self.TextLabel)

        menu = BoxLayout(spacing=3,
                         orientation='vertical',
                         size_hint=(.3, .1),
                         pos_hint={'top': 0.3, 'right': 0.65})
        self.MainLayout.add_widget(menu)

        menu.add_widget(Button(text='To menu',
                               font_size=30,
                               on_press=self.kt.interupt))

        self.MainLayout.add_widget(KeyboardInput.listener)

    def addLetter(self, index, text):
        """Change the letter color during the input phase"""
        log(Window.size)
        self.TextLabel.text = '[color=ff0000]' + text[:index] + \
                              '[/color]' + text[index:]
        print(self.TextLabel.text)
        log((self.TextLabel.text,))

    def endMenu(self, speed, mistakes, averageSpeed):
        """Draw the menu of with statistics and buttons start and exit"""
        self.MainLayout.clear_widgets()

        self.makeMenu()

        newText = "Speed: " + formSpeed(speed) + '\nMistakes: ' + str(mistakes)
        newText += '\nAverage speed: ' + formSpeed(averageSpeed)
        newText += '\nMost mistakes buttons: ' + mostMissButtons()
        LabelWidget = Label(text=newText,
                            pos_hint={'top': 1.3},
                            font_size=30,
                            color=(.2, .2, .2, 1))
        self.MainLayout.add_widget(LabelWidget)

    def makeMenu(self):
        """Make menu with buttons and textarea"""
        menu = BoxLayout(spacing=3,
                         orientation='vertical',
                         size_hint=(.5, .5),
                         pos_hint={'top': 0.6, 'right': 0.75})
        self.MainLayout.add_widget(menu)

        self.TextInputWidget = TextInput(hint_text=HINT_TEXT, font_size=30)
        menu.add_widget(self.TextInputWidget)
        start = BoxLayout(spacing=3,
                          orientation='horizontal')
        start.add_widget(Button(text='Start',
                                font_size=30,
                                on_press=self.kt.newInput1))
        text1 = BoxLayout(spacing=3,
                                 orientation='horizontal')
        text2 = BoxLayout(spacing=3,
                                 orientation='horizontal')

        text1.add_widget(Button(text='Easy level Typing',
                                font_size=30,
                                on_press=self.kt.newInput2))
        text2.add_widget(Button(text='Hard level Typing',
                                font_size=30,
                                on_press=self.kt.newInput2))
        menu.add_widget(start)
        menu.add_widget(text1)
        menu.add_widget(text2)
        menu.add_widget(Button(text='Reset statistics',
                               font_size=30,
                               on_press=self.kt.reset))
        menu.add_widget(Button(text='Exit',
                               font_size=30,
                               on_press=exit))

    def insertText(self, text):
        """Change text in text-input widget to given"""
        self.TextInputWidget.text = text


class KeyboardListener(Widget):
    """Make and set a listener object to the keyboard"""

    def __init__(self, triggerFunc):
        """Make keyboard and bind it to the window"""
        super().__init__()
        self.triggerFunc = triggerFunc

        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text')

        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        """Unbind keyboard from the window"""
        log('shutting down keyboard')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        """Activate trigger function and release keyboard if needed"""
        needToRelease = self.triggerFunc(keycode, text, modifiers)
        if needToRelease:
            keyboard.release()

        return True
