i=0
numbers = []

while i < 50:
    print 'At the top i is %d' % i
    numbers.append(i)
    
    i += 1
    print 'Number now: %d' % i
    print 'At the bottom i is %d' % i
    
    
print 'The numbers: '

for num in numbers:
    print num 
