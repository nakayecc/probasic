import getopt
import sys


def show():
    print("Your ideabank: ")
    try:
        with open('ideabank.txt', 'r', encoding='utf-8') as f:
            for x in enumerate(f, 1):
                tmp, tmp2 = x
                print('{0}. {1}'.format(tmp, tmp2.strip()))
    except IOError:
        print("Error: File does not appear to exist.")


def add(idea):
    try:
        with open('ideabank.txt', 'a', encoding='utf-8') as f:
            f.write(idea + "\n")
            f.close
    except IOError:

        print("Error: File does not appear to exist.")


def dell(index):
    try:
        counter = 0
        with open('ideabank.txt', 'r', encoding='utf-8') as f:
            buffor = []
            for line in f:
                counter = counter + 1
                # print(line)
                if (counter != index):
                    buffor.append(line)
        f.close()
        with open('ideabank.txt', 'w', encoding='utf-8') as k:
            k.writelines(buffor)
            k.close()
    except IOError:
        print("Error: File does not appear to exist.")


options, arg = getopt.getopt(sys.argv[1:], 'ld', ['list', 'delete'])
if (len(sys.argv) > 1):
    for opt, arg in options:
        if opt in ('-l', '--list'):
            show()
        elif opt in ('-d', '--delete'):
            dell(int(sys.argv[2]))
            show()
else:
    add(input("What is your new idea: "))
    show()
