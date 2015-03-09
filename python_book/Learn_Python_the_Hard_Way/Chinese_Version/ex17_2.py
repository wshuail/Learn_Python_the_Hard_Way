from sys import argv
from os.path import exists

script, file1, file2 = argv

print 'This script %r will cope context of %r to %r.' %(script, file1, file2)

print 'First, open %r, and read its context.' % file1

file_input = open(file1)

file_context = file_input.read()

print 'If %r exists? %r' %(file2, exists(file2))

print 'Hit Enter to execute, click CTRL-C to quit.'

raw_input('> ')

file_copy = open(file2, 'r+')

file_copied = file_copy.write(file_context)

print 'All right, all done.'

file_input.close()
file_copy.close()
