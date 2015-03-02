print 'Now choose a num, 1 or 2 ?'

num = raw_input('')

if num == '1':
    print 'You are the best !'
    print 'Now choose another num, 1 or 2 ?'
    num2 = raw_input('')
    
    if num2 == '1':
        print 'I will give you an apple.'
    elif num2 == '2':
        print 'I will give you a banana.'
    else:
        print 'please enter 1 or 2.'
        
elif num == '2':
    print 'You are so 2.'

else:
    print 'Please choose 1 or 2.'      
