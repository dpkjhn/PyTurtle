'''
Created on 31 Dec 2012

@author: djohn
'''

MAXSIZE = [200, 200]

class Screen(object):
    '''
    classdocs
    '''
    
    def clear_screen(self):
        '''
        Clear the drawing area
        '''
        pass


    def __init__(self, maxsize=MAXSIZE):
        '''
        Constructor
        '''
        self._maxsize = maxsize

class Viewport(Screen):
    
        