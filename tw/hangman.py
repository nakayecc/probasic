import sys
import time
import os
from pygame import mixer
#from termcolor import colored #print (colored("tekst", 'red', 'on_green'))

hashlist = []
passwordlist = []

life = 6
timer = time.time()
nowData = time.strftime("%c")
clear = "\n" * 100
usedlatterbank = []



def handle_used_letter(currentletter):
    if not((currentletter) in usedlatterbank):
        usedlatterbank.append(currentletter)
    return usedlatterbank


def startGame(life,usedlatterbank):
    passwordlist, hashlist = prepare("warszawa") 
    print(hashlist)
    print(len(usedlatterbank))

    while ("_" in hashlist):
        animation(life)
        life,usedlatterbank = contain(passwordlist, hashlist, life)
    #showdebug(passwordlist, hashlist)
    restart(life)


def loadScores():
    pass
 


def credits():
    print(clear)
    f = open("/home/michal/Codecool/probasic/TW/credits.txt", "r")
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
   
    f = open("/home/michal/Codecool/probasic/TW/hangman.txt", 'r')
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
        startGame(life,usedlatterbank)
    elif select == "2":
        loadScores()
    elif select == "3":
        credits()
    elif select == "4":
        quit()
    else:
        print("Try again! Select 1, 2, 3 or 4.")
        menu()


def prepare (string):
    tmplist = []
    tmplist2 = []
    stringtmp = string.upper()
    tmplist += stringtmp
    listlen = len(stringtmp)
    i = 0
    while i < listlen:
        tmplist2.append('_')
        i+=1
    return tmplist, tmplist2


def useletter(bank):
    life
    print("todo")
    return


def restart(life):
 
    counter = 0
 
    while True:
        res = str(input("Do you want to play again? y/n: "))
 
        if res == "y":
            print("Restarting...")
            life = 6
            startGame(life,usedlatterbank)
        elif res == "n":
            print("Ok then... See ya!")
            menu()
        else:
            print("Choose 'y' for yes or 'n' for 'no'!")
            counter += 1
 
        if counter == 5: #rage mode is activated.. xD
            print("CHOOSE Y OR NO! MORON...")\


def contain(passwordlist, hashlist, life):
        i = 0
        wordlen = 0
        counter= 0

        if life <= 0:
            restart(life)

        ask = str(input("Type you letter: "))
        asktmp = ask.upper()
        wordlen = len(ask)
        print(wordlen)

        if(wordlen == 1):
            usedlatterbank = handle_used_letter(asktmp)
            if (asktmp in passwordlist):
                while i<len(passwordlist):
                    if(asktmp == passwordlist[i]):
                        overwrite(hashlist,i,asktmp)
                    i+=1
            else:
                life-=1
        elif( wordlen > 1 and wordlen < len(passwordlist)):
   
            tmp2list = []
            tmp2list +=asktmp

            for k in range(wordlen):
                if(tmp2list[k] in passwordlist):
                    for x in range(wordlen):
                        for y in range(len(passwordlist)):
                            handle_used_letter(tmp2list[k])
                            if(tmp2list[x] == passwordlist[y]):
                                hashlist[y] = tmp2list[x] 
                else:
                    life-=1
        elif( wordlen == len(hashlist)):
            tmp2list = []
            tmp2list +=asktmp

            for k in range(wordlen):
                handle_used_letter(tmp2list[k])
                if(tmp2list[k] in passwordlist):
                    counter += 1
                  
            print("Counter : " + str(counter) )
            if(counter == len(hashlist)):
                for x in range(wordlen):
                    for y in range(len(passwordlist)):
                        if(tmp2list[x] == passwordlist[y]):
                            hashlist[y] = tmp2list[x]
                print("test +")
                return life,usedlatterbank
            else:
                life-=2
            print("test -")
            return life,usedlatterbank

        print("test done")
        print(hashlist)
        return life,usedlatterbank


def animation(life):

    if life == 6:
        f = open("/home/michal/Codecool/probasic/TW/hangman7.txt", 'r')
        print(f.read())
        f.close()
    elif life == 5:
        f = open("/home/michal/Codecool/probasic/TW/hangman2.txt", 'r')
        print(f.read())
        f.close()
    elif life == 4:
        f = open("/home/michal/Codecool/probasic/TW/hangman3.txt", 'r')
        print(f.read())
        f.close()
    elif life == 3:
        f = open("/home/michal/Codecool/probasic/TW/hangman4.txt", 'r')
        print(f.read())
        f.close()
    elif life == 2:
        f = open("/home/michal/Codecool/probasic/TW/hangman5.txt", 'r')
        print(f.read())
        f.close()
    elif life == 1:
        f = open("/home/michal/Codecool/probasic/TW/hangman6.txt", 'r')
        print(f.read())
        f.close()
    elif life == 0:
        f = open("/home/michal/Codecool/probasic/TW/hangman.txt", 'r')
        print(f.read())
        f.close()


def showdebug(passwordlist, hashlist):
    print(passwordlist)
    print(hashlist)


def overwrite(hashlist, index, letter):
    hashlist[index] = letter


def main():
    menu()
    #showdebug(passwordlist, hashlist)


if __name__ == "__main__":
    main()