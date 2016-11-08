'''
Created on 8 nov. 2016

@author: Camelia
'''
from allOperations import *
from commandOperations import *


def readCommand():
    cmd = input("Enter command: ")
    if cmd.find(" ") == -1:
        command = cmd
        parameters = ""
    else:
        command = cmd[0:cmd.find(" ")]
        parameters = cmd[cmd.find(" ")+1:]
        parameters = parameters.split(" ")
        print(len(parameters))
    return command, parameters

def validParameters(command, parameters):
    commandParameters = {"add":[1], "insert":[3], "remove":[1, 3], "replace":[3], "list":[0, 3, 4], "sum":[3], "product":[3], "filter":[3], "undo":[0], "exit":[0]}
    if command in commandParameters and len(parameters) in commandParameters[command]:
        return True
    return False

def addCommand(numbers, cmd):
    n = defineNumber(cmd[0])
    #print(n[0], "   jcecblkvkb  ", n[1])
    addNumberToListCommand(numbers, n)

def defineNumber(numberString):
    n = []
    numberString = numberString.strip()
    
    if numberString.find("+") == -1 and numberString.find("-", 1) == "-1":
        n[1] = 0
        n[0] = numberString
        return n
    if numberString.find("+")!=-1:
        #n[0] = numberString[0:numberString.find("+")]
        
        #n[1] = numberString[numberString.find("+")+1:numberString.find("i")]
        numberString = numberString.strip("i")
        n = numberString.split("+")
        if len(n) == 3:
            n[0] = n[1]
            n[1] = n[2]
            n.pop()
        return n
    elif numberString.find("-", 1) != -1:
        #n[0] = numberString[0:numberString.find("-", 1)]
        #n[1] = numberString[numberString.find("-", 1):numberString.find("i")]
        numberString = numberString.strip("i")
        n = numberString.split("-")
        if len(n) == 3:
            n[0] += n[1]
            n[1] = n[2]
            n.pop()
        return n

def insertCommand(numbers, cmd):
    if cmd[1] == "at":
        number = defineNumber(cmd[0])
        print(len(number))
        insertNumberInList(cmd[2], numbers, number)
    else:
        print("Invalid command.")
        
def remove(numbers, cmd):
    if len(cmd) == 1:
        deleteNumberFromList(cmd[0], numbers)
    elif len(cmd) == 3:
        if cmd[1] == "to":
            deleteNumbersBetweenIndexes(cmd[0], cmd[1], numbers)
        else:
            print("Invalid command.")
            
def replace(numbers, cmd):
    if cmd[1] != "with":
        print("Invalid command.")
    else:
        n = defineNumber(cmd[0])
        new = defineNumber(cmd[2])
        replaceValues(numbers, n, new)
        
def list(numbers, cmd):
    if len(cmd) == 0:
        print(listNumbers(numbers))
    elif len(cmd) == 3:
        if cmd[0] == "modulo" and cmd[1] in ["<", "=", ">"]:
            printList(listByModulo(numbers, cmd[2], cmd[1]))
        else:
            print("Invalid command.")
    elif len(cmd) == 4:
        if cmd[0] == "real" and cmd[2] == "to":
            printList(listRealNumbersBetweenIndexes(numbers, cmd[1], cmd[3]))
        else:
            print("Invalid command.") 

def printSum(numbers, cmd):
    if cmd[1] == "to":
        print(NumberToString(sum(numbers, cmd[0], cmd[2])))
    else:
        print("Invalid command.")
        
def printProduct(numbers, cmd):
    if cmd[1] == "to":
        print(NumberToString(product(numbers, cmd[0], cmd[2])))
    else:
        print("Invalid command.")
        
def filterCommand(numbers, cmd):
    if cmd[0] != "modulo":
        print("Invalid command.")
    elif cmd[1] not in ["<", "=", ">"]:
        print("Invalid command.")
    else:
        m = defineNumber(cmd[2])
        printList(Filter(numbers, m, cmd[1]))
        
      