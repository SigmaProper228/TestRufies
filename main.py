from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from instructions import *
from ruffier import *

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        label = Label(text=txt_instruction)
        name_txt = Label(text='Введите имя:')
        age_txt = Label(text='Введите возраст:')
        name_input = TextInput(size_hint=(1, None), height='30px', pos_hint={'center_y':0.5}, multiline=False)
        self.age_input = TextInput(size_hint=(1, None), height='30px', pos_hint={'center_y':0.5}, multiline=False)
        button1 = Button(text='Начать', size_hint=(0.30, 0.60), pos_hint={'center_x':0.5})
        layout_v = BoxLayout(orientation='vertical')
        layout_name = BoxLayout()
        layout_age = BoxLayout()
        layout_v.add_widget(label)
        layout_v.add_widget(layout_name)
        layout_v.add_widget(layout_age)
        layout_name.add_widget(name_txt)
        layout_name.add_widget(name_input)
        layout_age.add_widget(age_txt)
        layout_age.add_widget(self.age_input)
        layout_v.add_widget(button1)
        self.add_widget(layout_v)
        button1.on_press = self.next
    def next(self):
        global age
        try:
            age = int(self.age_input.text)
            self.manager.current = 'Экран 2'
        except ValueError:
            self.age_input.text = 'Пиши цифрами :/'

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        txt = Label(text=txt_test1)
        result_txt = Label(text='Введите результат:')
        self.result_amount = TextInput(size_hint=(1, None), height='30px', pos_hint={'center_y':0.5}, multiline=False)
        button = Button(text='Продолжить', size_hint=(0.30, 0.60), pos_hint={'center_x':0.5})
        layout_v = BoxLayout(orientation='vertical')
        layout_result = BoxLayout()
        layout_v.add_widget(txt)
        layout_v.add_widget(layout_result)
        layout_result.add_widget(result_txt)
        layout_result.add_widget(self.result_amount)
        layout_v.add_widget(button)
        self.add_widget(layout_v)
        button.on_press = self.next
    def next(self):
        global res1
        try:
            res1 = int(self.result_amount.text)
            self.manager.current = 'Экран 3'
        except ValueError:
            self.result_amount.text = 'Пиши цифрами :/'


class TheethScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        txt = Label(text=txt_sits)
        button = Button(text='Продолжить', size_hint=(0.30, 0.60), pos_hint={'center_x':0.5})
        layout_v = BoxLayout(orientation='vertical')
        layout_v.add_widget(txt)
        layout_v.add_widget(button)
        self.add_widget(layout_v)
        button.on_press = self.next
    def next(self):
        self.manager.current = 'Экран 4'

class ForthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        txt = Label(text=txt_test3)
        button = Button(text='Завершить', size_hint=(0.30, 0.60), pos_hint={'center_x':0.5})
        txt_result = Label(text='Результат:')
        txt_after = Label(text='Результат после отдыха:')
        self.result = TextInput(size_hint=(1, None), height='30px', pos_hint={'center_y':0.5}, multiline=False)
        self.result_after = TextInput(size_hint=(1, None), height='30px', pos_hint={'center_y':0.5}, multiline=False)
        layout_v = BoxLayout(orientation='vertical')
        layout_result = BoxLayout()
        layout_after = BoxLayout()
        layout_v.add_widget(txt)
        layout_v.add_widget(layout_result)
        layout_result.add_widget(txt_result)
        layout_result.add_widget(self.result)
        layout_v.add_widget(layout_after)
        layout_after.add_widget(txt_after)
        layout_after.add_widget(self.result_after)
        layout_v.add_widget(button)
        self.add_widget(layout_v)
        button.on_press = self.next
    def next(self):
        global res2, res3
        try:
            res2 = int(self.result.text)
        except ValueError:
            self.result.text = 'Пиши цифрами :/'
            return
        try:
            res3 = int(self.result_after.text)
            self.manager.current = 'Экран 5'
        except ValueError:
            self.result_after.text = 'Пиши цифрами :/'


class FivethScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.results = Label(text='')
        layout_v = BoxLayout(orientation='vertical')
        layout_v.add_widget(self.results)
        self.add_widget(layout_v)
        self.on_enter = self.before
    def before(self):
        res = test(res1, res2, res3, age)
        self.results.text = res

class MyApp(App):
    def build(self):
        screeeen = ScreenManager()
        screeeen.add_widget(FirstScreen(name='Экран 1'))
        screeeen.add_widget(SecondScreen(name='Экран 2'))
        screeeen.add_widget(TheethScreen(name='Экран 3'))
        screeeen.add_widget(ForthScreen(name='Экран 4'))
        screeeen.add_widget(FivethScreen(name='Экран 5'))
        return screeeen

app = MyApp()
app.run()