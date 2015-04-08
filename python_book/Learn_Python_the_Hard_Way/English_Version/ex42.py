# !/usr/bin/env python
# -*- coding: utf-8 -*-

# animal is-a object (yes, sort of confusing) look at the extra credit

#make a class named Animal, that is a object
class Animal (object):
    pass
    
# make a class named dog, that is an 'Animal'; dog is-a Animal;
class Dog (Animal):
    # class 'dog' has a '__init__' that takes self and name parameters.
    def __init__ (self, name):
        #self has-a name named name.
        self.name = name 

# make a class named cat, that is an 'Animal'; cat is-an animal
class Cat(Animal):
    # class cat has-a __init__ that takes self and name parameters.
    def __init__(self, name):
        #self has-a name named name.
        self.name = name
        
# make a class named Person, that is an object; Person is-an object
class Person (object):
    # class Person has __init__ that takes self and name parameters.
    def __init__(self, name):
        # self has-a name named name.
        self.name = name
        
        #Person has-a pet of some kind.
        self.pet = None
        
# Employee is a Person
class Employee (Person):
    def __init__ (self, name, salary): # the Employee has-a __init__ that tales self, name and salary parameters.
        # The class Employee inherits something from Person
        super(Employee, self).__init__(name)
    
        # Employee has-a salary.
        self.salary = salary
    
# Fish is-a object    
class Fish(object):
    pass
    
# Salmon is-a Fish
class Salmon(Fish):
    pass
    
# Halibut is-a fish
class Halibut(Fish):
    pass
    
# rover is-a Dog
rover = Dog ('Rover') # set rover to an instance of class 'Dog'

#satan is-a cat
satan = Cat ('satan')

# mary is-a person
mary = Person ('Person')

# mary has-a pet named satan
mary.pet = satan

# set frank to an instance of Employee parameters with Frank and 120000
# frank is an Employee
frank = Employee ('Frank', 120000)

# frank has-a pet named rover
frank.pet = rover

#flipper is-a fish
flipper = Fish ()

#crouse is a salmon
crouse = Salmon ()

# harry is-a halibut
harry = Halibut ()
