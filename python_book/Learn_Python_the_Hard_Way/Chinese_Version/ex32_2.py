x1 = ['apple', 'orange', 'banana']
x2 = ['Tom', 'Jim', 'Marry']
x3 = ['tree', 'flower', 'grass']
num = [1, 2, 3, 4, 5, 6]
empty_num = []
empty_num2 = []

for i in x1:
    print 'I have a %s.' % i

for i in x2:
    print 'I have a friend: %s.' % i
    
for i in num:
    print 'how many people are there? %d' % i

print 'Add numbers into the empty list.'
for i in range(1, 6):
    empty_num.append(i * 100)

print empty_num

print 'List numbers in the list.'
for i in empty_num:
    print 'Elements are: %d' % i
    
    
empty_num2.append(range(1, 100))
print empty_num2
