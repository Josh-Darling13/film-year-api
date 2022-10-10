from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.slider import Slider
import requests

Builder.load_file('slider.kv')



class MyLayout(Widget):
    def slide_it(self, *args):
        # print(args[1])
        self.slide_text.text = str(int(args[1]))
        url = "https://imdb8.p.rapidapi.com/auto-complete"
        querystring = {"q":"y=" + str(int(args[1]))}
        headers = {
            "X-RapidAPI-Key": "ac06a94b3emshd31c62841a131e4p16d231jsnc6cb5f3d5c95",
            "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)

class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()