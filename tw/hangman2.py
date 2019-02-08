import sys
import time
import os
from pygame import mixer

hashlist = []
passwordlist = []
usedLetterList = []
life = 6
timer = time.time()
nowData = time.strftime("%c")
clear = "\n" * 100
usedletterlist = []



def startGame():
    inputWordlen, bigLetterInput = None, None
    separator = "|"

    os.system('clear')
    while( '_' in hashlist):
        animation(life)
        print(hashlist)
        print("Used Letters:")
        print("|".join(usedletterlist))
        inputWordlen, bigLetterInput = changeLetterFunction()
        os.system('clear')
        usedLettersByPlayer(inputWordlen, bigLetterInput)
        playerLife(inputWordlen, bigLetterInput)
        if( life == 0):
            restart()
                    


def loadScores():
    pass
 


def credits():
    print(clear)
    f = open("credits.txt", "r")
    print(f.read())
 
    print("""  
   made by:
       Darek
       Hubert
       Michal
 
   Thanks for the game guys! Cheers.
   """)
   
    while True:
        back = str(input("Press 'b' back: "))
 
        if back == "b":
            menu()
            break
        else:
            print("Press 'b' to back")
            credits()
            break

 
def menu():
    os.system('clear')
    f = open("hangmanMenu.txt", 'r')
    print(f.read())
    f.close()
    '''
    mixer.init()
    mixer.music.load("menu.wav")
    mixer.music.play()
    '''
    select = input("""
           1. Start game
           2. Scoreboard
           3. Credits
           4. Exit
 
           Your choice: """)
 
    if select == "1":
        os.system('clear')
        startGame()
    elif select == "2":
        os.system('clear')
        loadScores()
    elif select == "3":
        os.system('clear')
        credits()
    elif select == "4":
        quit()
    else:
        print("Try again! Select 1, 2, 3 or 4.")
        menu()

def animation(life):

    if life == 6:
        f = open("hangman7.txt", 'r')
        print(f.read())
        f.close()
    elif life == 5:
        f = open("hangman2.txt", 'r')
        print(f.read())
        f.close()
    elif life == 4:
        f = open("hangman3.txt", 'r')
        print(f.read())
        f.close()
    elif life == 3:
        f = open("hangman4.txt", 'r')
        print(f.read())
        f.close()
    elif life == 2:
        f = open("hangman5.txt", 'r')
        print(f.read())
        f.close()
    elif life == 1:
        f = open("hangman6.txt", 'r')
        print(f.read())
        f.close()
    elif life == 0:
        f = open("hangman.txt", 'r')
        print(f.read())
        f.close()


def restart():
 
    counter = 0
    global life
 
    while True:
        res = str(input("Do you want to play again? y/n: "))
 
        if res == "y":
            print("Restarting...")
            life = 6
            prepareListsToGame("warszawa")
            usedletterlist.clear()
            startGame()
        elif res == "n":
            print("Ok then... See ya!")
            menu()
        else:
            print("Choose 'y' for yes or 'n' for 'no'!")
            counter += 1
 
        if counter == 5: #rage mode is activated.. xD
            print("CHOOSE Y OR NO! MORON...")\


def showdebug(passwordlist, hashlist):
    print(passwordlist)
    print(hashlist)


def prepareListsToGame (string):
    preparedPasswordList = []
    prepardedHashList = []
    stringtmp = string.upper()
    preparedPasswordList += stringtmp
    listlen = len(stringtmp)
    i = 0
    while i < listlen:
        prepardedHashList.append('_')
        i+=1
    global passwordlist
    global hashlist
    passwordlist = preparedPasswordList
    hashlist = prepardedHashList


def inputLetterByPlayer():
    inputPlayerLetter = str(input("Type you letter: "))
    bigLetterInput = inputPlayerLetter.upper()
    wordlen = len(inputPlayerLetter)
    return wordlen, bigLetterInput

def passwordContainLetter(wordLenVar, bigLetterInputVar):

    if(wordLenVar == 1):
        if (bigLetterInputVar in passwordlist):
            return True
        else:
            return False


    elif(wordLenVar > 1):
        inputLetterList = []
        inputLetterList +=  bigLetterInputVar
        for x in range(wordLenVar):
            if(inputLetterList[x] in passwordlist):
                return True
            else:
                return False


def overwritteLetterOnHash(wordLenVar,bigLetterInputVar):
    i = 0
    global hashlist

    if(wordLenVar == 1):
        while (i < len(passwordlist)):
            if(bigLetterInputVar == passwordlist[i]):
                hashlist[i] = bigLetterInputVar
            i+=1

    elif(wordLenVar > 1):
        inputLetterList = []
        inputLetterList +=  bigLetterInputVar
    
        for x in range(wordLenVar):
            for y in range(len(passwordlist)):
                if(inputLetterList[x] == passwordlist[y]):
                    hashlist[y] = inputLetterList[x]


def changeLetterFunction():
    inputWordlen, bigLetterInput = inputLetterByPlayer()
    inputWordlenVar = inputWordlen
    bigLetterInputVar = bigLetterInput
    
    if(inputWordlen == 1):
        if(passwordContainLetter(inputWordlen,bigLetterInput)):
            overwritteLetterOnHash(inputWordlen,bigLetterInput)
    if(inputWordlen > 1):
        for x in range(inputWordlen):
            if(passwordContainLetter(inputWordlen,bigLetterInput[x])):
                overwritteLetterOnHash(inputWordlen,bigLetterInput)
    return inputWordlenVar, bigLetterInputVar


def playerLife(inputWordlen, bigLetterInput):
    global life
    counter = 0


    if(inputWordlen == 1):
        if(passwordContainLetter(inputWordlen,bigLetterInput)):
            return
        else:
            life-=1


    elif(inputWordlen > 1 and inputWordlen < len(passwordlist)):
        for x in range(inputWordlen):
            if(passwordContainLetter(inputWordlen,bigLetterInput[x])):
                return
            else:
                life-=1


    elif(inputWordlen == len(passwordlist)):
        for x in range(inputWordlen):
            if(passwordContainLetter(inputWordlen,bigLetterInput[x])):
                counter+=1
                print("chuj dupa chuj")
        if(counter == len(passwordlist)):
            return
        else:
            life-=2

def usedLettersByPlayer(inputWordlenVar, bigLetterInputVar):
    global usedletterlist
    for x in range(inputWordlenVar):
        if not(bigLetterInputVar[x] in usedletterlist):
            usedletterlist.append(bigLetterInputVar[x])


def main():
    os.system('clear')
    prepareListsToGame("warszawa")
    menu()


if __name__ == "__main__":
    main()






