import ast
from random import randrange
temporary = open("Dict_data.py", "r")
dictionary_data = temporary.read()
dictionary = ast.literal_eval(dictionary_data)


# gets smaller dictionary based on chosen location
def location_picked_dictionary(big_dictionary, location_list):
    new_dictionary = {}
    for key in list(big_dictionary.keys()):
        if big_dictionary[key][1] in location_list:
            new_dictionary[key] = big_dictionary[key]
    for keym in new_dictionary:
        print(keym)
    return new_dictionary


# Takes a list from sorted_dictionary and sorts it
def quicksort(dictionary_list, start, end):
    if start >= end:
        return
    set_pivot = randrange(start, end+1)
    pivot_value = dictionary_list[set_pivot][1][3]
    dictionary_list[set_pivot], dictionary_list[end] = dictionary_list[end], dictionary_list[set_pivot]

    pointer_location = start

    for i in range(start, end):
        if dictionary_list[i][1][3] > pivot_value:
            dictionary_list[i], dictionary_list[pointer_location] = dictionary_list[pointer_location],\
                                                                    dictionary_list[i]
            pointer_location += 1
    dictionary_list[end], dictionary_list[pointer_location] = dictionary_list[pointer_location], dictionary_list[end]
    quicksort(dictionary_list, start, pointer_location-1)
    quicksort(dictionary_list, pointer_location+1, end)
