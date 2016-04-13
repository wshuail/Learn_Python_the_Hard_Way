# !/usr/bin/env pthon
# -*- coding: utf-8 -*-

from sys import exit

def gold_room ():
    print 'This room is full of gold. How much do you take ?'
    
    next = raw_input ('>')
    
    if '0' in next or '1' in next:
        how_much = int (next) # the obsulute number
    else:
        dead ('Man, learn to type a number.') # what happend if the number do not contain '0' or '1'.
        
    if how_much < 50:
        print 'Nice, you\'re not greedy, you win !'
    else:
        print 'You greedy bastard !'
        
        
def bear_room ():
    print 'There is a bear there.'
    print 'The bear has a bunch of honey.'
    print 'The fat bear is in front of another door.'
    print 'How are you going to move the bear ?'
    bear_moved = False
    
    while True:
        next = raw_input ('>')
        
        if next == 'take honey':   # this should be '==', not '='
            dead ('The bear look at you and then slaps your face off.')
        elif next == 'taunt bear' and not bear_moved: # 'not bear_moved' = True
            print 'The bear was moved from the door. You can go through it now.'
            bear_moved = True
        elif next == 'taunt bear' and bear_moved: # False
            dead ('The bear gets pissed off and chews your leg off.')
        elif next == 'open door' and bear_moved: #False
            gold_room () # this function was defined at the begining of this file.
        else:
            print 'I got no idea what that means.'
            
            
def cthulu_room ():
    print 'Here you see the great evil Cthulu.' # What's this ???
    print 'He, it, what stares at you and you go insane.'
    print 'Do you flee for your life or eat your head?'
    
    next = raw_input ('>')
    
    if 'flee' in next:
        start ()   # what will happen after this ?
    elif 'head' in next:
        dead ('Well that was tasty !')
    else:
        cthulu_room ()
        
            
def dead (why):
    print why, 'Good job !'
    exit(0) # what's this ?
    
def start():
    print 'You\'re in a dark room.'
    print 'There is a door to your right or your left.'
    print 'Which one do you take?'
    
    next = raw_input ('>')
    
    if next == 'left':
        bear_room ()
    elif next == 'right':
        cthulu_room ()
    else:
        dead ('You stumble around the room until you starve.')
        
        
start ()
