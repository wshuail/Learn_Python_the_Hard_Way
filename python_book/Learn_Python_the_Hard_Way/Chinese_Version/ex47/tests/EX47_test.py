from nose.tools import *
from ex47.game import Room

def test_room():
    gold = Room('Goldroom'
    '''This is a room full of gold,
    so from you can get a lots of gold.
    there is a door at the north coner.''')
    assert_equal(gold.name, 'Goldroom')
    assert_equal(gold.path, {})
    
def test_room_path():
    center = Room('Test room in the center.')
    north = Room('Test room in the north.')
    south = Room('Test room in the south.')
    
    center.add_path({'north': north, 'south': south})
    
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room('start', 'You can go west or down.')
    west = Room('Trees', 'There are many trees here, you can go east.')
    down = Room('Lake', 'There is a lake here, you can go up.')
    
    start.add_path({'west': west, 'down':down})
    west.add_path({'east', start})
    down.add_path({'up': start})
    
    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(west.go('down').go('up'), start)
    assert_equal(east.go('down'), down)

