import random

from itertools import combinations

# numbers which user is allowed to input
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# list of winning numbers
winner_list = [
    [1, 2, 3],
    [1, 4, 7],
    [1, 5, 9],
    [2, 5, 8],
    [3, 5, 7],
    [3, 6, 9],
    [4, 5, 6],
    [7, 8, 9],
]

nochance_list = []

reserved_list = []

# user input list
user_list = []

# Computers Turn list
computer_list = []




def print_matrix():
    '''tic-tac-toe matrix the program will print'''
    print()
    for i in range(1, 10):
        if i in user_list:
            print("1", end=" ")
        else:
            if i in computer_list:
                print("0", end=" ")
            else:
                print("-", end=" ")
        if i in [3, 6]:
            print()
    print()
    print()


def sub_list(list):
    temp_list = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            if i == j:
                pass
            else:
                temp_list.append([list[i], list[j]])
    return temp_list


def user_move_analysis():
    '''analyzes the users move'''
    if len(user_list) == 2:
        for i in winner_list:
            check = all(item in i for item in user_list)
            if check is True:
                if i in nochance_list:
                    pass
                else:
                    return i
    if len(user_list) > 2:
        user_move_list = sub_list(user_list)
        for i in user_move_list:
            for j in winner_list:
                check = all(item in j for item in i)
                if check is True:
                    if j in nochance_list:
                        pass
                    else:
                        return j


def user_minus(fav_list):
    for i in fav_list:
        if i in user_list:
            pass
        else:
            return i


def self_analysis_list():
    '''computer analyzes its own list'''
    if len(computer_list) == 1:
        for i in winner_list:
            check = all(item in i for item in computer_list)
            if check is True:
                flag = False
                for j in i:
                    if j in user_list:
                        flag = True
                        break
                if flag is True:
                    pass
                else:
                    return i
    if len(computer_list) > 1:
        com_move_list = sub_list(computer_list)
        for i in com_move_list:
            for j in winner_list:
                check = all(item in j for item in i)
                if check is True:
                    flag = False
                    for k in j:
                        if k in user_list:
                            flag = True
                            break
                    if flag is True:
                        pass
                    else:
                        return j


def self_minus(fav_list):
    for i in fav_list:
        if i in computer_list:
            pass
        else:
            return i


def minus():
    for i in number_list:
        if i in reserved_list:
            pass
        else:
            return i


def self_analysis():
    favourable_list = self_analysis_list()
    if favourable_list is None:
        fav_input = minus()
        computer_list.append(fav_input)
        reserved_list.append(fav_input)
        print("Computers Turn (0) => ", fav_input)
    else:
        fav_input = self_minus(favourable_list)
        computer_list.append(fav_input)
        reserved_list.append(fav_input)
        print("Computers Turn (0) => ", fav_input)


def user_input():
    '''function for user input'''

    temp = ""
    try:
        temp = int(input("Users Turn (1) => \n"))
    except:
        print("*** Invalid input ***")
        return user_input()

    if temp not in number_list:
        print("*** Input Error ***")
        return user_input()
    else:
        if temp in reserved_list:
            print("*** Slot Taken ***")
            return user_input()
        else:
            user_list.append(temp)
            reserved_list.append(temp)


def computer_first_input():
    '''function for computers first move'''
    temp = random.choice([1, 2, 3, 4, 7])
    computer_list.append(temp)
    reserved_list.append(temp)
    print("Computers Turn (0) => ", temp)


def computer_input():
    '''analyzes users moves or computer does self analysis based on case'''
    if len(user_list) > 1:
        favourable_list = user_move_analysis()
        if favourable_list is None:
            self_analysis()
        else:
            fav_input = user_minus(favourable_list)
            if fav_input in reserved_list:
                self_analysis()
            else:
                computer_list.append(fav_input)
                reserved_list.append(fav_input)
                nochance_list.append(favourable_list)
                print("Computers Turn (0) => ", fav_input)
    else:
        self_analysis()


def match_computer():
    comb = list(combinations(computer_list, 3))
    arr = []
    for ii in comb:
        arr.append(list(ii))
    for i in winner_list:
        for j in arr:
            check = all(item in i for item in j)
            if check is True:
                return True
            else:
                pass



def match_user():
    '''checks against the winner list'''
    comb = list(combinations(user_list, 3))
    arr = []
    for ii in comb:
        arr.append(list(ii))
    for i in winner_list:
        for j in arr:
            check = all(item in i for item in j)
            if check is True:
                return True
            else:
                pass



def main():
    '''function for user or Computers Turn with winner print'''
    i = 0
    while i < 9:
        i = i + 1
        if i % 2 == 0:
            user_input()
            print_matrix()
            com_done = match_user()
            if com_done is True:
                print()
                print("*****************************************")
                print()
                print(
                    """
    __ __              _ _ _  _      |  |
    |  |  | ___  _ _   | | | ||_| ___ |  |
    |_   _|| . || | |  | | | || ||   ||__|
    |_|  |___||___|  |_____||_||_|_||__|"""
                )
                print()
                print("*****************************************")
                print()
                break
        else:
            if i == 1:
                computer_first_input()
                print_matrix()
            else:
                computer_input()
                print_matrix()
                com_done = match_computer()
                if com_done is True:
                    print()
                    print("*********************************************************")
                    print()
                    print(
                        """
    _____                        _              _ _ _  _           
    |     | ___  _____  ___  _ _ | |_  ___  ___ | | | ||_| ___  ___ 
    |   --|| . ||     || . || | ||  _|| -_||  _|| | | || ||   ||_ -|
    |_____||___||_|_|_||  _||___||_|  |___||_|  |_____||_||_|_||___|
                    |_|"""
                    )
                    print()
                    print("*********************************************************")
                    print()
                    break


if __name__ == "__main__":
    main()
