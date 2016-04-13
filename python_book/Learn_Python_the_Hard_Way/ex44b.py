# !/usr/bin/env python
# -*- coding: utf-8 -*-

# This script describes the override of the class

class Parent (object):
    
    def override(self):
        print 'PARENT override()'
        
class Child (Parent):
    
    def override (self):
        print 'CHILD override ()'
        
dad = Parent ()
son = Child ()

dad.override()
son.override()
