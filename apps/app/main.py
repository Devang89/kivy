from kivy.app import App
from kivy.lang import Builder
import json, glob
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime
from pathlib import Path
import random
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
import os

os.listdir()
Builder.load_file('design.kv')

class LoginScreen(Screen):
    def soccer(self):
        self.manager.current = "Soccer_screen"

    def tennis(self):
        self.manager.current = "tennis_screen"

    def hockey(self):
        self.manager.current = "Hockey_screen"
    
    def baseball(self):
        self.manager.current = "Baseball_screen"

    def football(self):
        self.manager.current = "Football_screen"
    
    def login(self, uname, pword):
        with open('kivy/apps//users.json') as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = "Login_success"
        else:
            self.ids.login_wrong.text = 'wrong username or password'

class ImageButton(ButtonBehavior, Image):
    pass
  

class RootWidget(ScreenManager):
    pass

class SoccerScreen(Screen):
    pass

class BaseballScreen(Screen):
    pass
        
class TennisScreen(Screen):
    pass

class FootballScreen(Screen):
    pass

class HockeyScreen(Screen):
    pass

      


class LoginSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current  = "Login_Screen"



class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()