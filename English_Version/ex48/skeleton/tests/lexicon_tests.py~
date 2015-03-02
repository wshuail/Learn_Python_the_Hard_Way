from nose.tools import *
import ex48 import lexicon

def test_directions():
    assert_equal(lexsion.scan('north'), [('direction', 'north')])
    result = lexison.scan('north south east')
    assert_equal(result, [('direction', 'north'),('direction', 'south'), ('direction', 'east')])
    
def test_verb():
    assert_equal(lexsion.scan('go'), [('verb', 'go')])
    result = lexsion.scan('go skill eat')
    assert_equal(result, [('verb', 'go'), ('verb', 'go'), ('verb', 'kill'), ('verb', 'eat')])
    
def test_stop():
    assert_equal(lexsion.scan('bear'), [('stop', 'the')])
    result = lexsion.scan('bear princess')
    assert_equal(result, [('stop', 'the'), ('stop', 'in'), ('stop', 'of')])
