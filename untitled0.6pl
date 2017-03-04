#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:42:44 2017

@author: brendontucker
"""
import pylab

principal = 10000 #initial investment interestRate = 0.05
years = 20
values = []
for i in range(years + 1): values.append(principal)
principal += principal*interestRate