'''
Created on 8 nov. 2016

@author: Camelia
'''
from allOperations import *
def validNumber(number):
    try:
        number[0] = int(number[0])
        number[1] = int(number[1])
        return True
    except ValueError:
        print("The number you entered is invalid")
        
def addNumberToListCommand(numbers, number):
    if validNumber(number) == True:
        addNumber(numbers, number)
    else:
        print("Invalid number, can't be added.")
        
def insertNumberInList(ind, numbers, number):
    try:
        index = int(ind)
        if index > len(numbers)-1 or index < 0:
            print("The index you entered exceeds list's boundaries.")
        else:
            if validNumber(number):
                insertNumberAtIndexGiven(numbers, number, index)
                return
            else:
                print("Invalid number.")
    except ValueError:
        print("Invalid index, must be an integer.")
        
def deleteNumberFromList(index, numbers):
    try:
        if index == int(index):
            if index > len(list)-1 or index < 0:
                print("The index you entered exceeds list's boundaries.")
            else:
                removeAtPIndexGiven(numbers, index)
                return
    except ValueError:
        print("Invalid index, must be an integer")
        
def deleteNumbersBetweenIndexes(index1, index2, numbers):
    try:
        if int(index1) == index1 and index2 == int(index2):
            if index1< 0 or index2 < 0 or index1 > len(numbers)-1 or index2 > len(numbers)-1 or index1 >= index2:
                print("Invalid indexes configuration, try again.")
            else:
                removeFromAnIndexToAnother(numbers, index1, index2)
                return
    except ValueError:
        print("nvalid indexes, must be instances of integer.")

def checkIfEqual(number1, number2):
    if number1[0] == number2[0] and number1[1] == number2[1]:
        return True
    return False        
def replaceValues(numbers, instance, new):
    try:
        if new[0] == int(new[0]) and new[1] == int(new[1]) and instance[0] == int(instance[0]) and instance[1] == int(instance[1]) :
            for i in range(0, len(numbers)):
                if checkIfEqual(numbers[i], instance):
                    replaceAtIndexGiven(numbers, i, new)
            return
    except ValueError:
        print("Invalid instances. The comparable item or the replacing item do not match the list blueprint.")
        
def isReal(number):
    """checks if the number is real"""
    if number[1] == 0:
        return True
    return False

def NumberToString(number):
    """prints the number as a string"""
    if number[1] == 0: #if the imaginary part is 0
        return number
    else:
        n = ""
        n += str(number[0])+"+"+str(number[1])+"i";
        return n

def printList(numbers):
    s=""
    for i in range(0, len(numbers)):
        s += str(NumberToString(numbers[i]))
        s+="\n"
    print(s)

from math import sqrt

def modulo(number):
    m = sqrt(number[0]*number[0] + number[1] * number[1])
    return m
    
def listNumbers(numbers):
    """returns the list of all numbers"""
    l = []
    for i in range(0, len(numbers)):
        l.append(NumberToString(numbers[i]))
    return l
    

def listRealNumbersBetweenIndexes(numbers, index1, index2):
    """this function returns the list of all the real numbers between th given indexes, meaning those numbers which have the imaginary part 0"""
    l = []
    try:
        if index1 == int(index1) and index2 == int(index2):
            if index1 >= index2 or index1 < 0 or index2 < 0 or index1 > len(numbers)-1 or index2 > len(numbers)-1:
                print("Invalid indexes.")
            else:
                for i in range(0, len(numbers)):
                    if isReal(numbers[i]):
                        l.append(NumberToString(numbers[i]))
                return l
    except ValueError:
        print("Invalid indexes, must be integers.")

def listGreaterThan(numbers, mod):
    l = []
    for i in range(0, len(numbers)):
        if modulo(numbers[i]) > float(mod):
            l.append(NumberToString(numbers[i]))
    return l

def listLessThan(numbers, mod):
    l = []
    for i in range(0, len(numbers)):
        if modulo(numbers[i]) < float(mod):
            l.append(NumberToString(numbers[i]))
    return l
        
def listEqualTo(numbers, mod):
    l = []
    for i in range(0, len(numbers)):
        if modulo(numbers[i]) == float(mod):
            l.append(NumberToString(numbers[i]))
    return l        

def listByModulo(numbers, mod, sign):
    l = []
    if sign == ">":
        l = listGreaterThan(numbers, mod)
    elif sign == "=":
        l = listEqualTo(numbers, mod)
    else:
        l = listLessThan(numbers, mod)
    return l

def sumOfTwo(n1, n2):
    """computes the sum of two numbers"""
    n = []
    n[0] = n1[0] + n2[0]
    n[1] = n1[1] + n2[1]
    return n

def sum(numbers, index1, index2):
    """returns the sum between the two given indexes"""
    s = []
    s[0] = 0
    s[1] = 0
    try:
        if index1 == int(index1) and int(index2) == index2:
            if index1 > len(numbers)-1 or index2 > len(numbers)-1 or index1 < 0 or index2 < 0 or index1 >= index2:
                print("Invalid indexing.")
            else:
                for i in range(index1, index2+1):
                    s = sumOfTwo(s, numbers[i])
                return NumberToString(s)
    except ValueError:
        print("Invalid indexing.")
        
def productOfTwo(n1, n2):
    p = []
    p[0] = n1[0] * n2[0] - n1[1] * n2[1]
    p[1] = n1[0] * n2[1] + n2[0] * n1[1]
    return p
                    
def product(numbers, index1, index2):              
    """returns the sum between the two given indexes"""
    p = []
    p[0] = 1
    p[1] = 1
    try:
        if index1 == int(index1) and int(index2) == index2:
            if index1 > len(numbers)-1 or index2 > len(numbers)-1 or index1 < 0 or index2 < 0 or index1 >= index2:
                print("Invalid indexing.")
            else:
                for i in range(index1, index2+1):
                    p = productOfTwo(p, numbers[i])
                return NumberToString(p)
    except ValueError:
        print("Invalid indexing.")
    
def filterLess(numbers, mod):
    for i in range(0, len(numbers)):
        if modulo(numbers[i]) >= float(mod):
            deleteNumberFromList(i, numbers)
            i -= 1
    return numbers    
    
def filterGreater(numbers, mod):
    for i in range(0, len(numbers)):
        if modulo(numbers[i]) <= float(mod):
            deleteNumberFromList(i, numbers)
            i -= 1
    return numbers    
   
def filterEqual(numbers, mod):
    for i in range(0, len(numbers)):
        if modulo(numbers[i]) < float(mod) or modulo(numbers[i]) > float(mod):
            deleteNumberFromList(i, numbers)
            i -= 1
    return numbers    
       
def Filter(numbers, mod, sign):        
    if sign == "=":
        return filterEqual(numbers, mod)
    elif sign == ">":
        return filterGreater(numbers, mod)
    elif sign == "<":
        return filterLess(numbers, mod)
from copy import deepcopy    

def backup(backups, nrOfBackups, numbers):
    l = deepcopy(numbers)
    backups.append(l)
    nrOfBackups += 1
    return l,backups, nrOfBackups

def undo(backups, nrOfBackups, numbers):
    if nrOfBackups == 0:
        print("Can't undo, there is no operation to be undone.")
    else:
        numbers = deepcopy(backups[nrOfBackups-2])
        nrOfBackups -=1
        backups.pop()
        return numbers, backups, nrOfBackups