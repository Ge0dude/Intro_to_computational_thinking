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
        
class MITPerson(Person):
    
    nextIdNum = 0 #identification number
    
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum 
        MITPerson.nextIdNum += 1
        
    def getIdNum(self): 
        return self.idNum
        
    def __lt__(self, other):
        return self.idNum < other.idNum
        
        
You = Person('Hamburg Hello')
#p1 = MITPerson('Barbara Beaver')

#print ( str(p1) + '\'s id number is ' + str(p1.getIdNum()))
#'''str() method is found in MITPerson's superclass, Person. getIdNum() is
#of course, found in the MITPerson class'''


#p1 = MITPerson('Mark Guttag')
#p2 = MITPerson('Billy Bob Beaver') 
#p3 = MITPerson('Billy Bob Beaver') 
#p4 = Person('Billy Bob Beaver')
#
#print ('p1 < p2 =', p1 < p2) 
#print ('p3 < p2 =', p3 < p2 )
#print ('p4 < p1 =', p4 < p1 )


class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear 
    def getClass(self):
        return self.year
        
class Grad(Student): 
    pass

#seems hard to keep track of what is a subclass of what... ? I guess it is
#supposed to be natural but I just can't seem to think that it would just
#get complicated and only make sense to the person designing the system. 
#Even then, I doubt I could keep my own designs straight 

class Grades(object): #why is this not a child of Students? 
    
    def __init__(self):
        self.students = [] 
        self.grades = {} 
        self.isSorted = True
        
    def addStudent(self, student):
        if student in self.students:
            raise ValueError('Duplicate student') #why no else statement?
        self.students.append(student) 
        self.grades[student.getIdNum()] = [] 
        self.isSorted = False
        
    









