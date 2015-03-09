from nose.tools import *
from ex47.game import Room

def test_room():
    gold = Room('GoldRoom',
                '''This room has gold in it you can grab. There's a door 
                to its north.'''
    assert_equal(gold.name, 'GoldRoom')
    assert_equal(gold.paths, [])
    
def test_room_paths():
    center = Room('Certer', 'Test room is center.')
    north = Room('North', 'Test room is north.')
    south = Room('South', 'Test room is south.')
    
    certer.add_paths(['north': north, 'south': south])
    assert_equal(certer.go('north'), north)
    assert_equal(certer.go('south'), south)
    
def test_map():
    start = Room('Start', 'You can go west and down a hole.')
    west = Room('Trees', 'There are threes here, you can go east.')
    east = Room('Denguon', 'It\'s dark down here, you can go up.')
    
    start.add_paths(['west': west, 'down': down])
    west.add_paths(['east': start])
    east.add_paths(['up': start])
    
    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), east)
    assert_equal(start.go('down').go('up'), start)
