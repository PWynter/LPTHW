from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

	def enter(self):
		pass


class Engine(object):
	"""docstring for ClassName"""
	def __init__(self, scene_map):
		pass
		
	def play(self):
		pass

class Death(Scene):

	def enter(self):
		pass

class CentralCorridoor(Scene):
	
	def enter(self):
		pass

class LaserWeaponArmoury(Scene):
	"""docstring for LaserWeaponArmoury"""
	def enter(self):
		pass

class TheBridge(Scene):
	"""docstring for TheBridge"""
	def enter(self):
		pass

class EscapePod(Scene):
	"""docstring for EscapePod"""
	def enter(self):
		pass
				
		
class Map(object):
	"""docstring for Map"""
	def __init__(self, start_scene):
		pass

	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		pass


a_map = Map("CentralCorridoor")
a_game = Engine(a_map)
a_game.play
		