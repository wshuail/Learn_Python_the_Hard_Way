from sys import argv

script, filename = argv

print 'Now I will open the test file %r.' % filename

# open the imput file
text = open(filename, 'r+')

print text.read()

print 'Now we will write some words on this file.'

line1 = raw_input('line 1:')
line2 = raw_input('line 2:')

text.seek(3)
text.write(line1)
text.seek(4)
text.write('\n')
text.seek(5)
text.write(line2)

print text.read()

text.close()
