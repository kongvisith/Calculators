from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

# Set background color
Window.clearcolor = (0, 0, 0, 1)

class Calculator(GridLayout):
    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)
        self.cols = 1
        self.spacing = 10
        self.padding = 10

        # Display area
        self.display = TextInput(
            multiline=False,
            readonly=True,
            font_size=48,
            halign='right',
            background_color=(0, 0, 0, 1),
            foreground_color=(1, 1, 1, 1),
            size_hint=(1, 0.2),
            cursor_blink=False
        )
        self.add_widget(self.display)

        # Define rows of buttons
        buttons = [
            [('AC', self.clear, (0.3, 0.3, 0.3, 1)), ('+/-', self.negate, (0.3, 0.3, 0.3, 1)), ('%', self.percent, (0.3, 0.3, 0.3, 1)), ('÷', self.press, (1, 0.6, 0, 1))],
            [('7', self.press, (0.1, 0.1, 0.1, 1)), ('8', self.press, (0.1, 0.1, 0.1, 1)), ('9', self.press, (0.1, 0.1, 0.1, 1)), ('×', self.press, (1, 0.6, 0, 1))],
            [('4', self.press, (0.1, 0.1, 0.1, 1)), ('5', self.press, (0.1, 0.1, 0.1, 1)), ('6', self.press, (0.1, 0.1, 0.1, 1)), ('-', self.press, (1, 0.6, 0, 1))],
            [('1', self.press, (0.1, 0.1, 0.1, 1)), ('2', self.press, (0.1, 0.1, 0.1, 1)), ('3', self.press, (0.1, 0.1, 0.1, 1)), ('+', self.press, (1, 0.6, 0, 1))],
            [('0', self.press, (0.1, 0.1, 0.1, 1)), ('.', self.press, (0.1, 0.1, 0.1, 1)), ('=', self.calculate, (1, 0.6, 0, 1))]
        ]

        # Add buttons to layout
        for row in buttons:
            h_layout = GridLayout(cols=4 if len(row) == 4 else 3, spacing=10, size_hint=(1, 0.16))
            for label, callback, color in row:
                btn = Button(
                    text=label,
                    font_size=32,
                    background_color=color,
                    color=(1, 1, 1, 1)
                )
                btn.bind(on_press=callback)
                if label == '0':
                    btn.size_hint_x = 2
                    h_layout.add_widget(btn)
                    continue
                h_layout.add_widget(btn)
            self.add_widget(h_layout)

    def press(self, instance):
        text = self.display.text
        if instance.text == '×':
            text += '*'
        elif instance.text == '÷':
            text += '/'
        else:
            text += instance.text
        self.display.text = text

    def clear(self, instance):
        self.display.text = ''

    def calculate(self, instance):
        try:
            self.display.text = str(eval(self.display.text))
        except:
            self.display.text = 'Error'

    def negate(self, instance):
        if self.display.text:
            if self.display.text.startswith('-'):
                self.display.text = self.display.text[1:]
            else:
                self.display.text = '-' + self.display.text

    def percent(self, instance):
        try:
            value = float(self.display.text)
            self.display.text = str(value / 100)
        except:
            self.display.text = 'Error'
class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == '__main__':
    CalculatorApp().run()