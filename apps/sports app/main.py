
from kivy.app import App
from kivy.lang import Builder
import json, glob
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime
from pathlib import Path
import random
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image

Builder.load_file('main.kv')

class LoginScreen(Screen):
    def soccer(self):
        self.manager.current = "Sign_up_screen"
    
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

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("kivy/apps//users.json") as file:
            users = json.load(file)
        users[uname] = {'username': uname, 'password': pword,
        'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        
        with open("kivy/apps//users.json", 'w') as file:
            json.dump(users, file)
        self.manager.current = "Sign_up_success"

class SignUpSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "Login_Screen"

class LoginSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current  = "Login_Screen"
    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob("kivy/apps//quotes/*txt")
        available_feelings  = [Path(filename).stem for filename in 
        available_feelings]
        print(available_feelings)

        if feel in available_feelings:
            with open(f"kivy/apps//quotes//{feel}.txt") as file:
                quotes = file.readlines()
                self.ids.quotes.text = random.choice(quotes)
        else:
            self.quotes.ids.text = "try anouther feeling"


class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()

