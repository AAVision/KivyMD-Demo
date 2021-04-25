from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton,MDFlatButton
from kivy.core.window import Window
import PIL


Window.size=(300,500)


usename_helper = """
MDTextField:
	hint_text: "Enter username"
	helper_text:"i'm Here!"
	helper_text_mode:"on_focus"
	icon_right:"key"
	icon_right_color:app.theme_cls.primary_color
	pos_hint:{'center_x':0.5,'center_y':0.5}
	size_hint_x:None
	width:250
"""
class User(MDApp):
	def build(self):
		self.theme_cls.primary_palette='Purple'
		screen = Screen()
		#username = MDTextField(text='Enter username',
		#	pos_hint={'center_x':0.5,'center_y':0.5},
		#	size_hint=(0.5,1))
		
		btn = MDRectangleFlatButton(text='Show',pos_hint={'center_x':0.5,'center_y':0.4},
			on_release=self.show_data)

		self.username = Builder.load_string(usename_helper)

		screen.add_widget(self.username)
		screen.add_widget(btn)
		

		return screen
	#show data is a function on release of button
	def show_data(self,obj):
		if self.username.text is "":
			check_string="Enter name"
		else:
			check_string = self.username.text
		close_btn = MDFlatButton(text='Close',on_release=self.close_dialog)
		#more_btn = MDFlatButton(text='More')
		self.dialog = MDDialog(title='Name',text=check_string,
			size_hint=(0.5,1),buttons=[close_btn])
		self.dialog.open()

	def close_dialog(self,obj):
		self.dialog.dismiss()
User().run()