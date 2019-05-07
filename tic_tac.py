import os, time, sys
from itertools import chain
list_num = [[0,0,0], [0,0,0], [0,0,0]]
mistake = 0

def examp():
    #for linux
    os.system('clear')
    #for windows
    #os.system('cls')
    print("INPUT THESE NUMBERS TO PLAY!! :D")
    print("    1    |   2   |   3   ")
    print("-------------------------")
    print("    4    |   5   |   6   ")
    print("-------------------------")
    print("    7    |   8   |   9   ")
    time.sleep(3)

examp()

def graph():
    global list_num
    #for linux
    os.system('clear')
    #for windows
    #os.system('cls')
    print("    {}    |   {}   |   {}   ".format('X' if list_num[0][0] == 1 else 'O' if list_num[0][0] != 0 else ' ', 'X' if list_num[0][1] == 1 else 'O' if list_num[0][1] != 0 else ' ', 'X' if list_num[0][2] == 1 else 'O' if list_num[0][2] != 0 else ' '))
    print("-------------------------")
    print("    {}    |   {}   |   {}   ".format('X' if list_num[1][0] == 1 else 'O' if list_num[1][0] != 0 else ' ', 'X' if list_num[1][1] == 1 else 'O' if list_num[1][1] != 0 else ' ', 'X' if list_num[1][2] == 1 else 'O' if list_num[1][2] != 0 else ' '))
    print("-------------------------")
    print("    {}    |   {}   |   {}   ".format('X' if list_num[2][0] == 1 else 'O' if list_num[2][0] != 0 else ' ', 'X' if list_num[2][1] == 1 else 'O' if list_num[2][1] != 0 else ' ', 'X' if list_num[2][2] == 1 else 'O' if list_num[2][2] != 0 else ' '))
    #for each in list_num:
        #print(each)

def change_1(posi):
    global mistake
    
    if posi == 1:
        if(list_num[0][0] != 0):
            temp = int(input("HouseFull Try other place.. : "))
            change_1(temp)
        else:
            list_num[0][0] = 1
    elif posi == 2:
        if(list_num[0][1] != 0):
            temp = int(input("HouseFull Try other place.. : "))
            change_1(temp)
        else:
            list_num[0][1] = 1
    elif posi == 3:
        if(list_num[0][2] != 0):
            temp = int(input("HouseFull Try other place.. : "))
            change_1(temp)
        else:
            list_num[0][2] = 1
    elif posi == 4:
        if(list_num[1][0] != 0):
            temp = int(input("HouseFull Try other place.. : "))
            change_1(temp)
        else:
            list_num[1][0] = 1
    elif posi == 5:
        if(list_num[1][1] != 0):
            temp = int(input("HouseFull Try other place.. : "))
            change_1(temp)
        else:
            list_num[1][1] = 1
    elif posi == 6:
        if(list_num[1][2] != 0):
            temp = int(input("HouseFull Try other place.. : "))
            change_1(temp)
        else:
            list_num[1][2] = 1
    elif posi == 7:
        if(list_num[2][0] != 0):
            temp = int(input("HouseFull Try other place.. : "))
            change_1(temp)
        else:
            list_num[2][0] = 1
    elif posi == 8:
        if(list_num[2][1] != 0):
            temp = int(input("HouseFull Try other place.. : "))
            change_1(temp)
        else:
            list_num[2][1] = 1
    elif posi == 9:
        if(list_num[2][2] != 0):
            temp = int(input("HouseFull Try other place.. : "))
            change_1(temp)
        else:
            list_num[2][2] = 1
    else:
        mistake += 1
        if mistake > 3:
            exit("You are retard to play!! Go home kid!!")
        temp = int(input("ENTER CORRECT OPTION U NOOB!!! : "))
        change_1(temp)

def change_2(posi):
    global mistake
    if posi == 1:
        if(list_num[0][0] != 0):
            temp = int(input("HouseFull Try other place.. : "))
            change_2(temp)
        else:
            list_num[0][0] = 2
    elif posi == 2:
        if(list_num[0][1] != 0):
            temp = int(input("HouseFull Try other place.. : "))
            change_2(temp)
        else:
            list_num[0][1] = 2
    elif posi == 3:
        if(list_num[0][2] != 0):
            temp = int(input("HouseFull Try other place.. : "))
            change_2(temp)
        else:
            list_num[0][2] = 2
    elif posi == 4:
        if(list_num[1][0] != 0):
            temp = int(input("HouseFull Try other place.. : "))
            change_2(temp)
        else:
            list_num[1][0] = 2
    elif posi == 5:
        if(list_num[1][1] != 0):
            temp = int(input("HouseFull Try other place.. : "))
            change_2(temp)
        else:
            list_num[1][1] = 2
    elif posi == 6:
        if(list_num[1][2] != 0):
            temp = int(input("HouseFull Try other place.. : "))
            change_2(temp)
        else:
            list_num[1][2] = 2
    elif posi == 7:
        if(list_num[2][0] != 0):
            temp = int(input("HouseFull Try other place.. : "))
            change_2(temp)
        else:
            list_num[2][0] = 2
    elif posi == 8:
        if(list_num[2][1] != 0):
            temp = int(input("HouseFull Try other place.. : "))
            change_2(temp)
        else:
            list_num[2][1] = 2
    elif posi == 9:
        if(list_num[2][2] != 0):
            temp = int(input("HouseFull Try other place.. : "))
            change_2(temp)
        else:
            list_num[2][2] = 2
    else:
        mistake += 1
        if mistake > 3:
            exit("You are retard to play!! Go home kid!!")
        temp = int(input("ENTER CORRECT OPTION U NOOB!!! : "))
        change_2(temp)

def check_win():
    #Horizontal First line
    if list_num[0].count(list_num[0][0]) == len(list_num[0]) and list_num[0][0] != 0:
        print()
        print()
        print("Player {} WINS!!!!".format(list_num[0][0]))
        for each in list_num:
            print(each)
        time.sleep(5)
        exit(0)
    #Horizontal Second line
    if list_num[1].count(list_num[1][0]) == len(list_num[1]) and list_num[1][0] != 0:
        print()
        print()
        print("Player {} WINS!!!!".format(list_num[1][0]))
        for each in list_num:
            print(each)
        time.sleep(5)
        exit(0)
    #Horizontal Third line
    if list_num[2].count(list_num[2][0]) == len(list_num[2]) and list_num[2][0] != 0:
        print()
        print()
        print("Player {} WINS!!!!".format(list_num[2][0]))
        for each in list_num:
            print(each)
        time.sleep(5)
        exit(0)
    # Diagonal Line check \
    if list_num[0][0] == list_num[1][1] and list_num[1][1] != 0:
        if list_num[1][1] == list_num[2][2]:
            print()
            print()
            print("Player {} WINS!!!!".format(list_num[1][1]))
            for each in list_num:
                print(each)
            time.sleep(5)
            exit(0)
    # Diagonal line check /
    if list_num[0][2] == list_num[1][1] and list_num[1][1] != 0:
        if list_num[1][1] == list_num[2][0]:
            print()
            print()
            print("Player {} WINS!!!!".format(list_num[1][1]))
            for each in list_num:
                print(each)
            time.sleep(5)
            exit(0)
    if list_num[0][0] == list_num[1][0] and list_num[1][0] != 0:
        if list_num[1][0] == list_num[2][0]:
            print()
            print()
            print("Player {} WINS!!!!".format(list_num[1][0]))
            for each in list_num:
                print(each)
            time.sleep(5)
            exit(0)
    if list_num[0][1] == list_num[1][1] and list_num[1][1] != 0:
        if list_num[1][1] == list_num[2][1]:
            print()
            print()
            print("Player {} WINS!!!!".format(list_num[1][1]))
            for each in list_num:
                print(each)
            time.sleep(5)
            exit(0)
    if list_num[0][2] == list_num[1][2] and list_num[1][2] != 0:
        if list_num[1][2] == list_num[2][2]:
            print()
            print()
            print("Player {} WINS!!!!".format(list_num[1][2]))
            for each in list_num:
                print(each)
            time.sleep(5)
            exit(0)
    if 0 not in chain(*list_num):
        print()
        print()
        print("Its a DRAW!!")
        for each in list_num:
            print(each)
        time.sleep(5)
        exit(0)

while True:
    print("",end="\n\n")
    temp = input("Symbol X || Player 1 :   ")
    temp = int(temp)
    change_1(temp)
    #print(list_num)
    graph()
    check_win()
    print("",end="\n\n")
    temp = input("Symbol O || Player 2 :   ")
    temp = int(temp)
    change_2(temp)
    #print(list_num)
    graph()
    check_win()
