'''
Created on 8 nov. 2016

@author: Camelia
'''

def addNumber(numbers, number):
    """this functions simply appends a number in the given list of already existing numbers"""
    numbers.append(number)
    
def insertNumberAtIndexGiven(numbers, number, index):
    """the function inserts a given element in the existing list of elements"""
    numbers.insert(index, number)
    
def removeAtPIndexGiven(numbers, index):
    """removes the entry existing at a certain positon"""
    numbers.pop(index)
    
def removeFromAnIndexToAnother(numbers, index1, index2):
    """removes all entries from an index to another"""
    count = 0
    while count < index2 - index1 + 1:
        numbers.pop(index1)
        count += 1
def replaceAtIndexGiven(numbers, index, new):
    """replaces the entry at index wgiven with new entry given as parameter"""
    numbers[index] = new
    
