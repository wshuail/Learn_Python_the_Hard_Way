color  = {'gd':'red', 'bj':'green','sh':'orange', 'hn':'purple'}

color['sc'] = 'yellow'
color['xz'] = 'blue'

print color

def find(themap, location):
    if location in themap:
        return themap[location]
    else:
        print 'NOT FOUND'

color['area'] = find
       
while True:
    print 'Location?'
    loc = raw_input('>: ')
    
    if not state: break
    
    found = color['area'](color, loc)
    print found
