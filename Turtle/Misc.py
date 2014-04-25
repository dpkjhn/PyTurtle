'''
Created on 31 Dec 2012

@author: djohn
'''

class Enum(object):
    def __init__(self, names):
        for number, name in enumerate(names.split()):
            setattr(self, name, number)