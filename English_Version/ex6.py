# -- coding: utf-8 --

x = "There are %d types of people." % 10 # define x
binary = "binary"
do_not = "don't"
y = "Those who know %s are those who know %s." %(binary, do_not) # define y with "%"

print x # print the string
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that jok so funny?! %r"
print joke_evaluation % hilarious # anoth method to use "%"

w = "This is the left side of ..."
e = "a string with right side."
print w + e # print two strings together, but what will happen to the "..."
