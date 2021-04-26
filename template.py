from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import subprocess
import time

Window.size=(300,500)

screen_helper="""
Screen:
	BoxLayout:
		orientation:'vertical'
		MDToolbar:
			title: 'AAVision'
			left_action_items:[["menu",lambda x: app.navigation_draw()]]
			right_action_items:[["clock",lambda x: app.navigation_draw()]]
			elevation:8
		MDLabel:
			text:'Created by AAVISION'
			halign:'center'

		MDBottomAppBar:
			MDToolbar:
				left_action_items:[["coffee",lambda x: app.navigation_draw()]]
				mode:'end'
				type:'bottom'
				icon:'help-rhombus'
				on_action_button:app.navigation_draw()
				

"""


class temp1(MDApp):

	def build(self):
		self.theme_cls.primary_palette='Purple'
		self.theme_cls.theme_style='Dark'
		screen = Builder.load_string(screen_helper)
		return screen

	def navigation_draw(self):
		print("Clicked")

temp1().run()