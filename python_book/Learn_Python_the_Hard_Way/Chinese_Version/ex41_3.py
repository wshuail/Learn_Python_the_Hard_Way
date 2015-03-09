from sys import exit

def fruit():
    print 'How many apples do you have ?'
    apple = raw_input('>')
    print 'Oh, so you have so many apples, %s.' % apple
    print 'How many bananas do you have ?'
    banana = raw_input('>')
    print 'Oh, so you have so many bananas, %s.' % banana
    return 'banana'

def banana():
    print 'Give you some bananas.'
    banana2 = raw_input('>')
    print 'You are generious!'
  
EAT = {'fruit': fruit, 'banana': banana}

def baby(EAT, fruit):
    next = fruit
    while True:
        start = EAT[next]
        return start()
        
baby(EAT, 'fruit')
