# !/usr/bin/env python
# -*- coding: utf-8 -*- 

from sys import exit
from random import randint

class Game(object):
	
	def __init__(self, start):
		self.quips = [
			'You died, and you kinda suck it.',
			'Your mom would be proud, if she is smarter.',
			'Suck a luser.',
			'I have a small puppy that\'s better at this.']
		self.start = start

	def play(self):
		next = self.start

		while True:
			print '/n----------------'
			room = getattr(self, next)
			next = room()

	def death(self):
		print self.quips[randint(0, len(self.quips) - 1)]
		exit(1)

	def princess_lives_here(self):
		print 'You see a princess here with a beautiful crown.'
		print 'She gives you a piece of cake.'

		eat_it = raw_input('>> ')
		if eat_it  == 'eat it':
			print 'You explore like a pinata full of frogs.'
			return 'death'
		elif eat_it == 'do not eat it':
			print 'She throw the cake at you and the cake cut off your head.'
			return 'death'

		elif eat_it == 'make her eat it':
			print 'she gives you the very last bit of cake and sheoves you in.'
			return 'gold_koi_pond'
		else:
			print 'The princess looks at you confused and just points at the cake.'
			return 'princess_lives_here'

	def gold_koi_pond(self):
		print 'There is a garden with a koi pond in the center.'

		feed_it = raw_input('>> ')
		
		if feed_it == 'feef it':
			print 'The koi jump up, rather than eat the cake, eat you arm.'
			return 'death'

		elif feef_it == 'do not feed it':
			print 'You are then pooped out a week larer.'
			return 'death'

		elif feed_it == 'throw it in':
			print 'You can see it happy, and then ...'
			return 'bear_with_sword'

		else:
			print 'The koi gets anoyyed and wriggles a bit.'
			return 'gold_koi_pond'

	def bear_with_sword(self):
		print 'It holds its raw out and looks at you.'

		give_it = raw_input('>> ')
		if give_it == 'give it':
			print 'The bear swipes at your hand to grab the diamond.'
			return 'death'
		elif give_it == 'say no':
			print 'The bear seem shocked. No body else told it that.'
			return 'big_iron_gate'

	def big_iron_gate(self):
		print 'You walk up to the big iron gate and see a handle.'
		
		open_it  = raw_input('>> ')
		
		if open_it == 'open it':
			print 'You open it and now you are free.'
			return 'death'

		else:
			print 'That\'s doesnot seem sensible.'
			return 'big_iron_gate'

a_game = Game('princess_lives_here')
a_game.play()
