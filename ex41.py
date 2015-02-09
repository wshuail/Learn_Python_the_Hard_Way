import random
from urllib import urlopen
import sys

WORD_URL = 'http://learncodethehardway.org/words.txt'
WORDS = []

PHRASES = { # this is a dict
    'class %%%(%%%):':
    'make a class named %%% that is a %%%.',
    'class %%%(object):\n\tdef__init__(self, ***)':
    'class %%% has a __init__ that take self and *** parameters.',
    'class %%%(object):\n\tdef ***(self, @@@)':
    'class %%% has a fuction named *** that takes self and @@@ parameter.',
    '*** = %%% ()':
    'set *** as an instance of class %%%.',
    '***.***(@@@)':
    'from *** get the *** fuction, and call it with parameters self, @@@.'
    "***.*** = '***'":
    'from *** get the *** attribute and set it to \'***\'.'
} # do not forget it ---- }

# do they want to drill phrase first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv [1] == 'english':  #sys.argv means that 'from sys get the argv function
    PHRASE_FIRST = True
    
# load up the words from the website
for word in urlopen(WORD_URL).readlines (): # from 'urlopen() get the readlines function
    WORDS.append(word.strip())     # from the 'WORDS' get the append function, and call it with parameter with 'word.strip()'; for the 'word.strip()', from 'word' get the strip function.
    
def convert (snippet, phrase):
    class_name = [w.capitalize() for w in 
                    random.sample(WORDS, snippet,count('%%%'))]
    other_name = random.sample(WORDS, snippet.count('***'))
    resultes = []
    param_names = []
    

for i in range(0, snippet.count('@@@')):
    param_count = random.randint (1, 3) # from random get the randint, and call it with parameter with '1' and '3'
    param_names.append (','.join(random.sample(WORDS, param_count))) # from param_names get the append, and call it with ...; from random get sample with parameters ....; 
    
    for sentence in snippet, phrance:
        result = sentence [:]
        
        #fake class name
    for word in class_name:
        result = result.replace('%%%', word, 1) # from result get the function 'replace'.
        
    # fake other names
    for word in other_names:
        result = result.replace ('***', word, 1)
        
    # fake parameter lists
    for word in param_names:
        result = result.replace ('@@@', word, 1)
        
    results.append (result)
    
return results



# keep going until they hit CTRL-D

try:
    while True:
        snippets = PHRASES.keys ()
        random.shuffle (snippets)
        
        for snippet in snippets:
            phrase = PHRASE [snippet]
            question, answer = convert (snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer question
                
            print question
            
            raw_input ('>')
            print 'ANSWER: %s\n\n' % answer
            
except EOFError:
    print '\nBye'
    
    
