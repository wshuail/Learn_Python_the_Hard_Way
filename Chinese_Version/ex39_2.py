fruit = ['apple', 'orange', 'banana']

more_fruit = ['pear', 'lizhi', 'longyan', 'taozi']

while len(fruit) != 5:
    one = more_fruit.pop()
    print 'Now I will add one more fruit to the list.'
    fruit.append(one)
    print 'Loot at the fruit: ', fruit
    
print fruit[0]
print fruit[-1]
print fruit.pop()
print '#'.join(fruit)
print '&'.join(fruit[1:4])
