from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import Screen,ScreenManager
# from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window

Window.size = (300, 500)

username_helper = """
ScreenManager:
    UserScreen:
    LoginScreen:
    CameraScreen:
    


<UserScreen>:
    name: 'user'
    MDTextField:
        hint_text: "Enter Username"
        helper_text: "or clock on forgot username"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color

        pos_hint: {'center_x':0.5, 'center_y':0.6}
        size_hint_x:None
        width:250
    MDTextField:
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
            root.manager.current = 'login'
            root.manager.transition.direction = 'left'
    MDRectangleFlatButton:
        text:'Sign up'
        pos_hint:{'center_x': 0.7, 'center_y': 0.3}
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
            
"""






class UserScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class CameraScreen(Screen):
    pass

sm=ScreenManager()
sm.add_widget(UserScreen(name='user'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(CameraScreen(name='cam'))
class DemoApp(MDApp):
    def build(self):

        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.theme_style = 'Dark'

        screen = Screen()
        self.username = Builder.load_string(username_helper)

        screen.add_widget(self.username)

        button = MDRectangleFlatButton(text='Submit')
        return screen




DemoApp().run()
