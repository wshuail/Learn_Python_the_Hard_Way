# !/usr/bin/env python

# This is a script for me to know how 'super' works.

class Fruit(object):
    def __init__(self, red, yellow, say):
        self.red = 'apple'
        self.yellow = 'banana'
        self.say = 'I Love Python.'

class Apple(Fruit):
    def __init__(self, red, say):
        super(Apple, self).__init__(red, say)

f = Fruit('blue', 'green', 'hello')
a = Apple('red', 'hi')
print a.red()
print a.say()
