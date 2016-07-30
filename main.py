'''
Created on ١٧‏/١١‏/٢٠١٥

@author: Ahmed AbdElrheem
'''
from random import randint, choice
# import pygame
# print(pygame.init())
#print(pygame.display.set_mode((600,600)))
#pygame.camera
#pygame.quit()
 
def listToString(l):
    strI= ""
    for i in l:
        strI += i+" "
    return strI
 
def generateDashesForLines(lines):
    lineLength = len(lines)
    dashesListForLines = []
    for i in range(lineLength):
        if lines[i] == " ":
            dashesListForLines.append("_")
        else:
            dashesListForLines.append("-") 
    return dashesListForLines    

def checkForDahes(dashedList):
    dashed = False
    for i in dashedList:
        if i == "-":
            dashed = True
            break
    return dashed      



############################
print("#####################################################################################################################")
description = "# The word to guess is represented by a row of dashes,                                                              #\n# representing each letter of the word  If the guessing player suggests a letter which occurs in the word,          #\n# the com writes it in all its correct positions. If the suggested letter or number does not occur in the word      #\n# the com tell that the remaining chances is decreased and the missed digits are The game is over when the remaining#\n# chances is zero or the player guessed the word correctly                                                          #."
print(description)
print("#####################################################################################################################")
print("1- Go")
print("2- Exit")
score = 0
hint  = 2
Go = input("Go Or Quit >> ")
while Go != "1" and Go != "2":
                print("Enter a Valid choice ")
                Go = input(">> ")
                
if Go == "1":
    wordsFile = open("words.txt","r+")
        
    trials = 0
    toContinue = 1
    newList = wordsFile.read().splitlines()
    while toContinue == 1:
        for i in range(len(newList)):
            if toContinue == 1:
                print("#########################################")
                
                trials = 6
                rand = randint(0,len(newList)-1)
                lineDashed = generateDashesForLines(newList[rand])
                print(newList[rand])
                #print(lineDashed)
                print(listToString(lineDashed))
                toPrint = 1
                wrongChar = []
                while trials != 0 and checkForDahes(lineDashed) == True:
                        toPrint = 1
                        x = input("Your Guess (letters only): ")
                        newWord = newList[rand]
                        if len(x) > 1:
                            print("Cant Enter More Than one Character")
                            continue
                        
                        if not x.isalpha():
                            print("Not a valid character. Please enter a letter .")
                            toPrint = 0
            
                        if x in newWord:
                            if x in lineDashed:
                                toPrint = 0
                                print("You have already tried this letter or digit. Guess again!" )
                            else:  
                                for j in range(len(newWord)):
                                    if newWord[j] == x:
                                        lineDashed[j] = x 
                                
                        if x.isupper() == True:
                            if x.lower() in newWord:
                                if x.lower() in lineDashed:
                                    #trials += 1
                                    toPrint = 0
                                    print("You have already tried this letter or digit. Guess again!" )
                                elif x.lower() not in lineDashed:  
                                    for j in range(len(newWord)):
                                        if newWord[j] == x.lower():
                                            lineDashed[j] = x.lower()
                                    #print(lineDashed) 
                            elif x not in newWord:
                                if x not in wrongChar and x.lower() not in wrongChar:
                                    trials -= 1
                                    print("This character is not present in the name.")
                                    wrongChar.append(x) 
                                else:
                                    print("You have already tried this Wrong letter or digit. Guess again!")      
            #                         
                        if x.islower() == True:
                            if x.upper() in newWord:
                                if x.upper() in lineDashed:
                                    #trials += 1
                                    toPrint = 0
                                    print("You have already tried this letter or digit. Guess again!" )
                                elif x.upper() not in lineDashed:  
                                    for j in range(len(newWord)):
                                        if newWord[j] == x.upper():
                                            lineDashed[j] = x.upper()
                                    #print(lineDashed) 
                                    
                            elif x not in newWord:
                                if x not in wrongChar and x.upper() not in wrongChar:
                                    trials -= 1
                                    print("This character is not present in the name.")
                                    wrongChar.append(x) 
                                else:
                                    print("You have already tried this Wrong letter or digit. Guess again!")  
                        if toPrint == 1:
                            print("Chances Remaining   :   "+str(trials))
                            if len(wrongChar) != 0 :
                                print("Missed Letters/Digits :  "+listToString( wrongChar)) 
                            else:
                                print("Missed Letters/Digits :  None")    
                            #print(lineDashed)
                            print(listToString(lineDashed))
                               
                                   
                if trials == 0:
                    print("You Lose and Your Score is  "+str(score))
                    print("The Correct Word Is "+"'"+newWord+"'")
                    
                elif checkForDahes(lineDashed) == False:
                    score += 10
                    print("You Won and Your Score is  "+str(score))
                    
                print("Play Again ? y/n ")
                choice = input()
                
                while choice != "y" and choice != "n" and choice != "N" and choice != "Y"  :
                    print("Enter a Valid choice ")
                    choice = input()
                    
                
                if choice == "y" or choice == "Y" :
                    toContinue = 1
                elif choice == "n" or choice == "N":
                    toContinue = 0    
            else:
                break            
elif Go == "2":
            exit            