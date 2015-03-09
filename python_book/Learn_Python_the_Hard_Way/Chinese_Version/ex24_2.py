def secret_formula (started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
    
    
start_point = 10000
beans, jars, crates = secret_formula(start_point) # the variable bacomes 'beans' from 'jelly_beans'.

print 'With a starting point of: %d' % start_point
print 'We\'d have %d beans, %d jars, and %d crates.' % (beans, jars, crates) # so the variable is 'beans', but not 'jelly_beans'.


def fruit(apple):
    my_apple = apple * 2
    return my_apple

def fruit2(my_apple2):
    my_banana = my_apple2 + 10
    return my_banana

apple2 = raw_input('')
apple == int(apple2)

my_apple = fruit(apple)
my_banana = fruit2(my_apple)

print 'I have %d apple, and %d banana.' % (my_apple, my_banana)
