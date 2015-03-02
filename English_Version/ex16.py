from sys import argv

script, filename = argv

print 'We\'re going to erase %r.' % filename
print 'If you don\'t want to do that, hit CTRL-C (^C).'
print 'If you do want that, hit RETURN.'

raw_input ('?')

print 'Opening the file ...'
target = open(filename, 'w') # There should be an object.

print 'Truncatting the file. Goodbye!'
target.truncate() # The object is only one, thus there no need par.

print 'Now, I want to ask you for three lines.'

line1 = raw_input('line1: ') # I this writing anyting here is OK.
line2 = raw_input('line2: ')
line3 = raw_input('line3: ')

print 'I\'m going to write to the file.'

target.write(line1) # write what I have wrate.
target.write('\n') # next line.
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print 'And finally, we close it.'
target.close()
