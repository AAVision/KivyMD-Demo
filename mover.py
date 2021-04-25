from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen,ScreenManager

Window.size=(300,500)

screen_helper="""
ScreenManager:
	MenuScreen:
	ProfileScreen:

<MenuScreen>:
	name:'one'
	MDRectangleFlatButton:
		text:'Next'
		pos_hint:{'center_x':0.5,'center_y':0.5}
		on_press:root.manager.current='two'

<ProfileScreen>:
	name:'two'
	MDLabel:
		text:'Welcome'
		halign:'center'
	MDRectangleFlatButton:
		text:'Back'
		pos_hint:{'center_x':0.5,'center_y':0.2}
		on_press:root.manager.current='one'

"""

class MenuScreen(Screen):
	pass

class ProfileScreen(Screen):
	pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='one'))
sm.add_widget(ProfileScreen(name='two'))
#mode fo2 momkn tkoun free-end
class Mover(MDApp):
	def build(self):
		self.theme_cls.primary_palette='Purple'
		self.theme_cls.theme_style='Dark'
		screen = Builder.load_string(screen_helper)
		return screen


Mover().run()