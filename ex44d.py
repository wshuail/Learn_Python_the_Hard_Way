class Parent(object):
    
    def override(self):
        print 'PARENT override ()'
        
    def implicit(self):
        print 'PARENT implicit ()'
    
    def altered (self):
        print 'PARENT altered ()'
        
class Child(Parent):
    
    def override(self):
        print 'CHILD override ()'
        
    def altered(self):
        print 'CHILD, BEFORE PARENT altered ()'     
        super(Child, self).altered()
        print 'CHILD, AFTER PARENT altered ()'
        
        
dad = Parent ()
son = Child ()

#both print 'PARENT implicite()'
dad.implicit()
son.implicit()


dad.override() #print PARENT override
son.override() #print CHILD override

#both print PARENT altered
dad.altered()
son.altered()
