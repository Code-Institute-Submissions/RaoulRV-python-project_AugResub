import random

from itertools import combinations

# numbers which user is allowed to input
number_list = [1,2,3,4,5,6,7,8,9]

# list of winning numbers
winner_list = [
    [1,2,3],
    [1,4,7],
    [1,5,9],
    [2,5,8],
    [3,5,7],
    [3,6,9],
    [4,5,6],
    [7,8,9]
]

nochance_list = []

reserved_list = []

# user input list
user_list = []

# computer input list
computer_list = []

# tic-tac-toe matrix the program will print

def print_matrix():
    print()
    for i in range(1,10):
        if i in user_list:
            print('1', end=' ')
        else:
            if i in computer_list:
                print('0', end=' ')
            else:
                print('-', end=' ')
        if i in [3,6]:
            print()
    print()
    print()

def subs_list (list):
    temporary_list = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            if i == j:
                pass
            else:
                temporary_list.append([list[i], list[j]])
    return(temporary_list)

# analyzes the users move

def user_move_analysis():
    if len(user_list) == 2:
        for i in winner_list:
            check = all(item in i for item in user_list)
            if check is True:
                if i in nochance_list:
                    pass
                else:
                    return i
    if len(user_list) > 2:
        user_move_list = subs_list(user_list)
        for i in user_move_list:
            for j in winner_list:
                check = all(item in j for item in i)
                if check is True:
                    if j in nochance_list:
                        pass
                    else:
                        return j


def user_minus(favorite_list):
    for i in favorite_list:
        if i in user_list:
            pass
        else:
            return i

# computer analyzes its own list
def self_analysis_list():
    if(len(computer_list) == 1):
        for i in winner_list:
            check = all(item in i for item in computer_list)
            if check is True:
                flag = False
                for j in i:
                    if j in user_list:
                        flag = True
                        break
                if(flag == True):
                    pass
                else:
                    return i
    if len(computer_list) > 1:
        com_move_list = subs_list(computer_list)
        for i in com_move_list:
            for j in winner_list:
                check = all(item in j for item in i)
                if check is True:
                    flag = False
                    for k in j:
                        if k in user_list:
                            flag = True
                            break
                    if(flag == True):
                        pass
                    else:
                        return j