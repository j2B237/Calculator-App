"""
    Author : Yossepbb
    Date: 18/08/2022
    Description: Simple calculator application made with Python
    Licence : GNU V2. You are free to copy that code and modify it.
    Kivy version used for this project
    And
    python 3.9.1

"""
import kivy

kivy.require("2.1.0")
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget


class CalculatorWidget(Widget):

    def clear(self) -> None:
        """ Clear screen """
        self.ids.calc_input.text = "0"

    def value(self, instance) -> None:
        """ Get value and display it to textbox """
        prior = self.ids.calc_input.text

        if "Error" in prior:
            prior = ""
        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = str(instance)
        else:
            self.ids.calc_input.text = f'{prior}{instance}'

    def operator(self, instance) -> None:
        """ display operator on textbox """
        self.ids.calc_input.text += instance

    def math(self) -> None:
        """ perform calcul """
        # Get the current content of calc input
        prior = self.ids.calc_input.text
        try:
            res = eval(prior)
            self.ids.calc_input.text = str(res)
        except ZeroDivisionError:
            self.ids.calc_input.text = "Error"

    def pos_or_negative(self) -> None:
        """ Turn textbox input to positive or negative """
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    def dot(self) -> None:
        """ Create a decimal number """
        prior = self.ids.calc_input.text
        # split textbox content by "+"
        numbers = prior.split("+")

        if "+" in prior and "." not in numbers[-1]:
            prior = f'{prior}.'
        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'

        self.ids.calc_input.text = prior

    def remove_last(self) -> None:
        """ delete last character in textbox """
        prior = self.ids.calc_input.text
        if prior == "":
            self.ids.calc_input.text = "0"
        else:
            prior = prior[:-1]
            self.ids.calc_input.text = prior


class CalculatorApp(App):
    def build(self) -> Widget:
        Window.size = (300, 520)
        self.title = "Calculator"

        return CalculatorWidget()


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
