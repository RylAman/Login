from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import Screen, ScreenManager
# from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
import mysql.connector

from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window

Window.size = (300, 500)

username_helper = """
ScreenManager:
    UserScreen:
    SignupScreen:
    LoginScreen:
    CameraScreen:



<UserScreen>:
    name: 'user'
    MDTextField:
        id: email
        hint_text: "Enter Username"
        helper_text: "or clock on forgot username"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color

        pos_hint: {'center_x':0.5, 'center_y':0.6}
        size_hint_x:None
        width:250
    MDTextField:
        id: password
        hint_text: "Enter Password"
        helper_text: "or clock on forgot username"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color

        pos_hint: {'center_x':0.5, 'center_y':0.5}
        size_hint_x:None
        width:250
    MDRectangleFlatButton:
        text:'Sign in'
        pos_hint:{'center_x': 0.3, 'center_y': 0.3}
        on_release:
            app.receive_data(email,password)
        #    root.manager.current = 'login'
        #    root.manager.transition.direction = 'left'
    MDRectangleFlatButton:
        text:'Sign up'
        pos_hint:{'center_x': 0.7, 'center_y': 0.3}
        on_release:
            root.manager.current = 'signup'
            root.manager.transition.direction = 'left'

<SignupScreen>:
    name: 'signup'
    MDTextField:
        hint_text: "Enter Name"
        helper_text: "or clock on forgot username"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color

        pos_hint: {'center_x':0.5, 'center_y':0.7}
        size_hint_x:None
        width:250
    MDTextField:
        hint_text: "Enter DOB"
        helper_text: "or clock on forgot username"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color

        pos_hint: {'center_x':0.5, 'center_y':0.6}
        size_hint_x:None
        width:250
    MDTextField:
        hint_text: "Enter E-mail"
        helper_text: "or clock on forgot username"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color

        pos_hint: {'center_x':0.5, 'center_y':0.5}
        size_hint_x:None
        width:250
    MDTextField:
        hint_text: "Enter Password"
        helper_text: "or clock on forgot username"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color

        pos_hint: {'center_x':0.5, 'center_y':0.4}
        size_hint_x:None
        width:250
    MDRectangleFlatIconButton:
        icon: "account-plus"
        icon_color: app.theme_cls.primary_color
        text:'Create'
        pos_hint:{'center_x': 0.5, 'center_y': 0.2}
        on_release:
            root.manager.current = 'login'
            root.manager.transition.direction = 'left'




<LoginScreen>:
    name:'login'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                Screen:
                    MDRectangleFlatButton:
                        text:'Back'
                        pos_hint:{'center_x': 0.3, 'center_y': 0.3}
                        on_release:
                            root.manager.current = 'user'
                            root.manager.transition.direction = 'right'
                    BoxLayout:
                        orientation:'vertical'
                        MDToolbar:
                            title: 'demo'
                            left_action_items: [["menu", lambda x: nav_drawer.set_state('toggle')]]
                            elevation:15

                        ScrollView:
                            MDList: 
                                OneLineIconListItem:
                                    text: 'Camera'
                                    IconLeftWidget:
                                        icon:'camera-enhance'
                                        on_release:
                                            root.manager.current = 'cam'

                                OneLineIconListItem:
                                    text: 'Logout'
                                    IconLeftWidget:
                                        icon:'logout'
                        Widget:

                    MDBottomAppBar:
                        MDToolbar:
                            title: 'demo'
                            left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                            mode: 'end'   
                            icon: 'language-python'
                            type: 'bottom'



            MDNavigationDrawer:
                id: nav_drawer

                BoxLayout:

                    orientation:'vertical'
                    spacing:'8dp'
                    padding:'12dp'
                    Image: 
                        source: 'k.jpg' 
                    MDLabel:
                        text: '   Aman'
                        font_style: 'Subtitle1'
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDLabel:
                        text: '    ar3506245@gmail'
                        font_style: 'Caption'
                        size_hint_y: None
                        height: self.texture_size[1]
                    ScrollView:
                        MDList: 
                            OneLineIconListItem:
                                text: 'Profile'
                                IconLeftWidget:
                                    icon:'face-profile-woman'
                            OneLineIconListItem:
                                text: 'Logout'
                                IconLeftWidget:
                                    icon:'logout'

<CameraScreen>:
    name:'cam'
    orientation: 'vertical'
    Camera:
        id: camera
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'  
    MDFloatingActionButton:
        icon:'language-python'
        pos_hint:{'center_x': 0.1, 'center_y': 0.9}
        on_release:
            root.manager.current = 'login'
            root.manager.transition.direction = 'right' 

"""


class UserScreen(Screen):
    pass


class SignupScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class CameraScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(UserScreen(name='user'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(CameraScreen(name='cam'))
sm.add_widget(CameraScreen(name='signup'))


class DemoApp(MDApp):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    database = mysql.connector.Connect(host="localhost", user="root", password="aman", database="login", port="3306", auth_plugin = "mysql_native_password")
    cursor = database.cursor()
    cursor.execute("select * from logindata")
    for i in cursor.fetchall():
        print(i[0], i[1])

    def build(self):

        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.theme_style = 'Dark'

        screen = Screen()
        self.username = Builder.load_string(username_helper)

        screen.add_widget(self.username)

        button = MDRectangleFlatButton(text='Submit')
        return screen
    def send_data(self, email, password):
        if re.fullmatch(self.regex, email.text):
            self.cursor.execute(f"insert into logindata values('{email.text}','{password.text}')")
            self.database.commit()
            email.text=""
            password.text=""
        #for i in self.cursor.fetchall():
        #        print(i[0], i[1])

    def receive_data(self, email, password):
        self.cursor.execute("select * from logindata")
        email_list=[]
        for i in self.cursor.fetchall():
            email_list.append(i[0])
        if email.text in email_list and email.text != "" :
            self.cursor.execute(f"select password from logindata where email='{email.text}'")
            for j in self.cursor:
                if password.text == j[0]:
                    print("success")
                    self.username.get_screen('login').manager.current = 'login'
                #    sm.add_widget(LoginScreen(name='login'
                #    DemoApp.sm.current='login'
                else:
                    cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
                    self.dialog = MDDialog(title='Invalid Username or Password',
                                           text="Please input a valid username or password", size_hint=(0.7, 0.2),
                                           buttons=[cancel_btn_username_dialogue])
                    self.dialog.open()

        else:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Invalid Username or Password', text="Please input a valid username or password", size_hint=(0.4, 0.1),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

    def close_username_dialogue(self, obj):
        self.dialog.dismiss()
DemoApp().run()
