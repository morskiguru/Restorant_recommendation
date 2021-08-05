from helper_functions import quicksort


def sort_dictionary(dictionary):
    dict_list = []
    keys_list = list(dictionary)
    value_list = list(dictionary.values())
    for i in range(len(keys_list)):
        dict_list.append([keys_list[i], value_list[i]])
    quicksort(dict_list, start=0, end=len(dict_list)-1)
    for i in range(len(dict_list)):
        print(f"{dict_list[i][0]} has a review of: {dict_list[i][1][3]}")
        print(f"Adress: {dict_list[i][1][0]}")
