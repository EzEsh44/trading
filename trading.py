#####################################################################
'''
The goal is to execute trading autonomously based on wanted tickers

Author:
Evan Shults
Creation Date: 8/9/2021



'''
#####################################################################

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
# from kivy_deps import sdl2, glew

class PongGame(Widget):
    pass

class tradingApp(App):
    def build(self):
        return PongGame()

tradingApp().run()


