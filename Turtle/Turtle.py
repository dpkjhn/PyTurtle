'''
Created on 30 Dec 2012

@author: djohn
'''

from Misc import *

class Turtle(object):
    '''
    classdocs
    '''
    def move(self, direction, distance):
        print self._curpos
    
    def _draw_self(self):
        pass
    


    def __init__(self, curpos=[0,0]):
        '''
        Constructor
        '''
        self._curpos = curpos