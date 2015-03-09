from sys import exit

def start():
    print 'Now you have been in SYSU, please a major.'
    
    major  = raw_input('>')
    
    if major == 'finance':
        finance()
        
    elif major == 'computer' or major == 'software':
        program()
        
    elif major == 'environment':
        environment()
        
    else:
        print 'Choose your major, freshman !'        

def finance():
    print 'This is a great major !'
    print 'Which campus do you like?'
    campus = raw_input('>')
    if campus == 'east':
        print 'You will be rich !' 
    elif campus == 'south':
        print 'You will hunt for a good job !'
    else:
        print 'You want to be a doctor ?'
        
def program():
    print 'program is interesting !'
    print 'Which language do you lile ?'
    language = raw_input('')
    print '%s is interesting !'
    print 'how much language do you want to learn ?'
    language_num = raw_input('')
    lan_num = int(language_num)
    if lan_num <= 3:
        print 'Less languages can make you a aspect !'
    elif lan_num > 3:
        print 'You have to work hard !'
    else:
        print 'Make your day !'
        
        
def environment():
    print 'You make a wrong choice!'
    print 'You\'d better change you major.'
    print 'Do you want ?'
    change_major = False
    next_action = raw_input('>')
    if next_action == 'yes' and change_major:
        print 'Talk is cheap, do it!'
    elif next_action == 'yes' and not change_major:
        print 'You\'re doing the right thing.'
        print 'Now change your major.'
        change_major()

def change_major():
    print 'Which major do you want to change!'
    next = raw_input('>')
    if next == 'finance':
        finance()
    if next == 'computer':
        program()
    else:
        print 'You have no future !'
        exit()

def dead():
    print 'Come again !'
    exit()

start()
