#!/usr/bin/env python3

#---------------------------------------------------------------------------
#
#   Write a Python program to create and display all combinations of letters,
#   selecting each letter from a different key in a dictionary.
#   Sample data : {'1':['a','b'], '2':['c','d']}
#   Expected Output:
#   ac
#   ad
#   bc
#   bd
#
#---------------------------------------------------------------------------


def generate_combinations(data, current_key_index=0, current_combination=""):
    if current_key_index == len(data):
        print(current_combination)
        return

    current_key = list(data.keys())[current_key_index]
    letters = data[current_key]

    for letter in letters:
        generate_combinations(data, current_key_index + 1, current_combination + letter)


data = {'1': ['a', 'b'], '2': ['c', 'd']}

generate_combinations(data)


    

