the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'orange', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quartes']

# this firsr kind of a loop go through a list
for number in the_count:
    print 'This is count %d' % number # d is number
    
# same as above
for fruit in fruits:
    print 'A fruit of type: %s' % fruit # s is string
    
# also, we can go through a mixed lists too
# notice that we have to use %r since we dno't know what's in it.
for i in change:
    print 'I got %r.' % i # r for anything
    
# we can also built a list. First we start with an empety one.
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print 'Adding %d to the list.' % i
    # append is a function that lists undertand
    elements.append(i)
    
# now we can print them out too.
for i in elements:
    print 'Element was : %d' % i
