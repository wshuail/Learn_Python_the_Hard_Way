# !/usr/bin/env python
# -*- coding: utf-8 -*-

# This is the exercise of chapeter 42 of Learn Python the Hard Way (Chinese Version)


class Myclass(object):
    def __init__(self):
        self.number = 1000
        self.fruit = 'apple'
    
    def eat(self):
        print 'I will eat this apple.'
        
    def eat_more(self, other_fruit):
        self.cloth = 'skirt'
        print 'I will eat apples and %r.' % other_fruit
        
    def eat_less(self, less):
        print 'How many apples are ate ?'
        self.number = self.number - less
        return self.number
        
a = Myclass()

print a.number
print a.fruit
print a.eat()
print a.eat_more('bananas')
print a.eat_less(10)
print a.cloth    
