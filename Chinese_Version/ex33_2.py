i=10
num = []

while i > 0:
    print 'Add the number %d in the list.' % i
    num.append(i)
    
    i = i - 1
    
    print 'The number at the bottom is %d.' % i 
    
print 'Now let\'s look at the numbers in the list.'
for i in num:
    print i 
