from socket import *
import os, sys


def main():

    if sys.argv < 3:
        print('Value error')
    HOST = sys.argv[1]
    PORT = int(sys.argv)[2]
    ADDR = (HOST, PORT)
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(10)
    pid = os.fork()
    if pid < 0:
        print("Create process failed")
    elif pid == 0:
        pid1 = os.fork()
        if pid1 < 0:
            print("Create process failed")
        elif pid1 == 1:
            pass
        else:
            sys.exit(1)
    else:
        pass

if __name__ == '__main__':
    main()
