from scene import *
import time


class MainMenuScreen(Scene):
	def setup(self):
		self.background=SpriteNode(position=self.size/2,
		                           color= ('#454545'),
		                           parent=self,
		                           size=self.size)
