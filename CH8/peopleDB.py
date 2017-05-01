#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 12:08:49 2017

@author: brendontucker
"""
import datetime

class Person(object):

    def __init__(self, name): 
        """Create a person""" 
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:] 
        except:
            self.lastName = name 
        self.birthday = None
        
    def getName(self):
        """Returns self's full name""" 
        return self.name
        
    def getLastName(self):
        """Returns self's last name""" 
        return self.lastName
        
    def setBirthday(self, birthdate):
        """Assumes birthdate is of type datetime.dateSets self's birthday to 
        birthdate""" 
        self.birthday = birthdate
        
    def getAge(self):
        """Returns self's current age in days""" 
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
        
    def __lt__(self, other):
        """Returns True if self's name is lexicographically
        less than other's name, and False otherwise""" 
        if self.lastName == other.lastName:
            return self.name < other.name 
        return self.lastName < other.lastName
    
    def __str__(self):
        """Returns self's name""" 
        return self.name
        
        
You = Person('Hamburg Hello')