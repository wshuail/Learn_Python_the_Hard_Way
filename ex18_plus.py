def print_length(*meter): # the * means I can put more than one values.
    wall, river = meter
    print 'wall: %r \nriver: %r' % (wall, river) # if I should put a space after the \n.
    
print_length ('18m', '25km')    
