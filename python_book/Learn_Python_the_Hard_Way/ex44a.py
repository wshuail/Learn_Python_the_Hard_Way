# !/usr/bin/env python
# -*- coding: utf-8 -*-

# This script descrbes the inheritance of the class

class Parent(object):
    def implicite(self):
        print 'PARENT implicite()'
        
class Child(Parent):
    pass
    
dad = Parent ()
son = Child ()

dad.implicite()
son.implicite()
