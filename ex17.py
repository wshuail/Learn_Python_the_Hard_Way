from sys import argv
from os.path import exists # import more than one mudules in this way.

script, from_file, to_file = argv # at least one file should be imput.

print 'copy from %r to %r.' %(from_file, to_file)

#We could do these two on one line too, how ?
in_file = open (from_file)
indata = in_file.read()

print 'The input file is %d bytes long.' % len(indata)

print 'Does the output file exists? %r' %exists(to_file) # '%r' is used to debug.
print 'Ready, hit R to continue, CTRL-C to abort.'
raw_input()

out_file = open (to_file, 'w')
out_file.write(indata)

print 'Alright, all done.'

out_file.close()
in_file.close()
