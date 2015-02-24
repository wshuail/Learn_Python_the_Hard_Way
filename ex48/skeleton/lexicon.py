stuff = raw_input('>')
words = stuff.split()

first_word = ('direction', 'north')
second_word = ('verb', 'go')

sentence = [first_word, second_word]

def conver_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None 


