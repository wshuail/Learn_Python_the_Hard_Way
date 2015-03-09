class Parent(object):
    def implicite(self):
        print 'PARENT implicite()'
        
class Child(Parent):
    pass
    
dad = Parent ()
son = Child ()

dad.implicite()
son.implicite()
