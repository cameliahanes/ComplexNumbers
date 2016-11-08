'''
Created on 8 nov. 2016

@author: Camelia
'''
from allOperations import *

def testInit(numbers):
    numbers.append("2 + 5i")
    numbers.append("1 + i")
    numbers.append("3 - i")
    numbers.append("-1 - 8i")
    numbers.append("6 - 3i")
    numbers.append("9 + 14i")
    numbers.append("3 + 10i")
    numbers.append("-4 + 6i")
    numbers.append("7 + 3i")

def testAdd():
    numbers = []
    testInit(numbers)
    number = "7 + 7i"
    assert len(numbers) == 9
    addNumber(numbers, number)
    assert len(numbers) == 10

def testInsert():
    numbers = []
    testInit(numbers)
    number = "2 + 2i"
    index = 3
    insertNumberAtIndexGiven(numbers, number, index)
    assert len(numbers) == 10
    assert numbers[3] == number

def testDelete():
    numbers = []
    testInit(numbers)
    index = 4
    assert len(numbers) == 9
    removeAtPIndexGiven(numbers, index)
    assert len(numbers) == 8
    assert numbers[index] == "9 + 14i"


def testDelete2():
    numbers = []
    testInit(numbers)
    index1 = 2
    index2 = 6
    assert len(numbers) == 9
    removeFromAnIndexToAnother(numbers, index1, index2)
    assert len(numbers) == 4
    assert numbers[2] == "-4 + 6i"
    
testInsert()

testAdd()

testDelete()

testDelete2()