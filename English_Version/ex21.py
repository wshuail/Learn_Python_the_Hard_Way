def add (a, b):
    print 'ADDING %d + %d' % (a, b)
    return a + b
    
def subtract (a, b):
    print 'SUBTRACT %d - %d' % (a, b)
    return a - b
    
def multiply (a, b):
    print 'multiply %d * %d' % (a, b)
    return a * b
    
def divide (a, b):
    print 'divide %d / %d' % (a, b)
    return a / b
    
print 'Let\'s do some math just with functions.'


age = add (30, 5)
height = subtract (78, 4)
weight = multiply (90, 2)
iq = divide (100, 2)

print 'age: %d, height: %d, weight: %d, IQ: %d' % (age, height, weight, iq)


# a puzzle for zredit, type it in any way.
print 'Here\'s a puzzle.'

what = add (age, subtract(height, multiply(weight, divide(iq, 2)))) #-4391

print 'That becomes : ', what, 'Can you do it by hand ?'
