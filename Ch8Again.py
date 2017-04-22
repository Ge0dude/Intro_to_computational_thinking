#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:48:13 2017

@author: brendontucker
"""
class IntSet(object):
    
    def __init__(self):
        self.vals = []
        
    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
            
    def member(self, e):
        return e in self.vals
    
    def remove(self, e):
        try: 
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
            
    def getMembers(self):
        return self.vals[:]
        
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'
        
s = IntSet()
s.insert(1)
s.insert(4)

#s.member = IntSet.insert 
#wowow, that is allowed!? So bad--can't believe that, maybe this is why people
#complain about OOP so much compared to FP

