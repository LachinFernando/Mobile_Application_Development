from kivymd.app import MDApp
from kivymd.toast import toast
from kivy.lang import Builder

KV = '''
BoxLayout:
    orientation:'vertical'

    MDTopAppBar:
        id: toolbar
        title: 'Test Toast'
        md_bg_color: app.theme_cls.primary_color
        left_action_items: [['menu', lambda x: '']]

    FloatLayout:

        MDRaisedButton:
            text: 'TEST KIVY TOAST'
            on_release: app.show_toast()
            pos_hint: {'center_x': .5, 'center_y': .5}

'''


class Test(MDApp):
    def show_toast(self):
        '''Displays a toast on the screen.'''

        toast('Test Kivy Toast')

    def build(self):
        return Builder.load_string(KV)

Test().run()