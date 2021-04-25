from kivymd.uix.screen import Screen
from kivymd.app import MDApp
from kivymd.uix.list import MDList,OneLineListItem,TwoLineIconListItem,TwoLineListItem,ThreeLineListItem
from kivymd.uix.list import IconLeftWidget,ImageLeftWidget #for image
from kivy.uix.scrollview import ScrollView


#from tkinter import Tk     # from tkinter import Tk for Python 3.x
#from tkinter.filedialog import askopenfilename

#Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
#filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
#print(filename)

from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.image import Image



class Lists(MDApp): #MDApp in class is to inherite everything from the library
	
	def build(self):
		screen = Screen()

		scroll = ScrollView()
		list_view = MDList()

		scroll.add_widget(list_view)
		for i in range(20):
			#icon = ImageLeftWidget(source="...")
			icon = IconLeftWidget(icon="android")
			items = TwoLineIconListItem(text='Item '+str(i),secondary_text='Hello')
			items.add_widget(icon)
			list_view.add_widget(items)

		
		
		screen.add_widget(scroll)
		
		return screen


Lists().run()