import sys


def hello(tmp="World"):
    print("Hello " + tmp)


if(len(sys.argv) > 1):
    hello(sys.argv[1])
else:
    hello()
