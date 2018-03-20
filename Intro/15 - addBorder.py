"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
"""

def addBorder(picture):

    r = ['*'*(len(picture[0])+2)]
    for i in picture:
        r.append('*' + i + '*')

    r.append(r[0])

    
    
    return r



'''
===Alternate Solution===

def addBorder(picture):
    l=len(picture[0])+2
    return ["*"*l]+[x.center(l,"*") for x in picture]+["*"*l]
        
   
========================
