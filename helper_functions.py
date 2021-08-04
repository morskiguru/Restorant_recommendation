import ast
temporary = open("Dict_data.py", "r")
dictionary_data = temporary.read()
dictionary = ast.literal_eval(dictionary_data)


# gets smaller dictionary based on chosen location
def location_picked_dictionary(big_dictionary, location_list):
    new_dictionary = {}
    for key in list(big_dictionary.keys()):
        print(key)
        if big_dictionary[key][1] in location_list:
            new_dictionary[key] = big_dictionary[key]
    return new_dictionary

def sort_dictionary(dictionary):

