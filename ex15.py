from sys import argv # import a module

script, filename = argv

txt = open (filename) # a new command

print 'Here\'s your file %r:' % filename
print txt.read() # When this command is excuted, the file will be open. But what will happen if there are two files.

print 'Type the filename again.'
file_again = raw_input ('*') # This will print what we write down.

txt_again = open(file_again) # This will open the file.

print txt_again.read() # This will print what in the file.
