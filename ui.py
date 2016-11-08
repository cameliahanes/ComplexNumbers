'''
Created on 8 nov. 2016

@author: Camelia
'''
from commandOperations import *
from Commands import *
from allOperations import *

def displayMenu():
    s = ""
    s += "add <number>; \n"
    s += "insert <number> at <index>; \n"
    s += "remove <index>; \n"
    s += "remove <start index> to <end index>;\n"
    s += "replace <old number> with <new number>;\n"
    s += "list; \n"
    s += "list real; \n"
    s += "list modulo < | = | > <number>;\n" 
    s += "sum <start index> to <end index>;\n"
    s += "product <start index> to <end index>; \n"
    s += "filter modulo < | = | > <number>;\n"
    s += "undo;\n"
    s += "exit;\n"
    print(s)
    
def run():
    numbers = []
    undoList = []
    nrOfUndoes = 0
    commandList = { "add":addCommand, "insert":insertCommand, "remove":remove, "replace":replace, "list":list, "sum":printSum, "product":printProduct, "filter":filterCommand }
    while True:
        displayMenu()
        command, parameters = readCommand()
        if command == "exit":
            break
        elif command == "undo":
            if nrOfUndoes == 0:
                print("There is nothing to be undone.")
            else:
                numbers, undoList, nrOfUndoes = undo(backups, nrOfBackups, numbers)
        else:
            if validParameters(command, parameters) == True:
                commandList[command](numbers, parameters)
                if command in ["add", "remove", "replace", "filter"]:
                    numbers, undoList, nrOfUndoes = backup(undoList, nrOfUndoes, numbers)
            else:
                print("Invalid command.")

run()
        
        
        
        
        