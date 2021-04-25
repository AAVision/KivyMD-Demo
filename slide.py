from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import PIL


Window.size=(300,500)

screen_helper="""
Screen:
	NavigationLayout:
		ScreenManager:
			Screen:
			    BoxLayout:
			        orientation: 'vertical'
			        MDToolbar:
			            title: 'AAVISION'
			            left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
			            elevation:10

			        Widget:

		MDNavigationDrawer:
			id: nav_drawer

"""


class slide(MDApp):

	def build(self):
		self.theme_cls.primary_palette='Purple'
		self.theme_cls.theme_style='Dark'
		screen = Builder.load_string(screen_helper)
		return screen

	

slide().run()