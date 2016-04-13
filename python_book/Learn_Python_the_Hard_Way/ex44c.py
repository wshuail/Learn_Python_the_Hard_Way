# !/usr/bin/env python
# -*- coding: utf-8 -*-

# THis scripts describe the alternative of the class

class Parent(object):
    def altered(self):
        print 'PARENT altered'
        
class Child(Parent):
    def altered(self):
        print 'Child, BEFORE PARENT altered()'
        super(Child, self).altered()
        print 'CHILD,  AFTER PARENT altered()'
        
dad = Parent ()
son = Child ()

dad.altered()
son.altered()
