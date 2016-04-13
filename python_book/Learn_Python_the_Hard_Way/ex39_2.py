# !/usr/bin/env python

# a test script for me to learn dictionary.

# create a dict
dict = {'apple': 'red', 'orange': 'yellow', 'book': 'squre', 'cup': 'china'}

print 'Print all elements in the dict.'
for things, attributes in dict.items():
    print 'The atrributes of %s is %s.' % (things, attributes)

print 'test if I can get red.'
test_apple = dict.get('apple')
print test_apple
print '\n'
print 'Two arguments.'
test_two_arguments = dict.get('apple', 'book')
print test_two_arguments

print '\n'
print 'Two arguments with None.'
test_two_args_with_None = dict.get('apple', None)
print test_two_args_with_None

print '\n'
print 'Get an element may not in the dict.'
test_not_there = dict.get('diamond')
if not test_not_there:
    print 'There is no diamond.'
print '\n'

print 'Change it to be a function.'
def get_nothing(nothing):
        test_nothing = dict.get(nothing)
        if not test_nothing:
            print 'Sorry, %s does not exit in the dict.' % nothing
get_nothing('diamond')

print '\n'
print 'Get something with default values.'
default_value = dict.get('Anything', 'Does Not Exist')
print default_value

print '\n'
print 'What happens if the first argument is in the dict.'
default_value_2 = dict.get('apple', 'Is the color is red?')
print default_value_2








