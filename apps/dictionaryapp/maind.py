from kivy.app import App
from kivy.lang import Builder
import json, glob
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime
from pathlib import Path
import random
import json
from difflib import get_close_matches
import os

os.listdir()

Builder.load_file('maind.kv')

class LoginScreen(Screen):
    def word_meaning(self, word):
        data = json.load(open("kivy/apps//data.json"))
        word = word.lower()
        if word in data:
            self.ids.DWord.text =  str('\n'.join(data[word]))
        elif word.title() in data:
            self.ids.DWord.text = str(data[word.title()])
        elif word.upper() in data:
            self.ids.DWord.text =  str(data[word.upper()])
        elif len(get_close_matches(word, data.keys())) > 0:
            self.ids.DWord.text  = ("did you mean " + get_close_matches(word, data.keys())[0])
        else:
            self.ids.DWord.text = ("this word does not exist please double check it")
        
        



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

