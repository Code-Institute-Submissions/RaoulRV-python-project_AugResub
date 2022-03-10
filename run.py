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