from helper_functions import location_picked_dictionary


def choose_expenses(dictionary, location_list):
    cost_dictionary = {}
    moderated_dictionary = location_picked_dictionary(dictionary, location_list)
    print("Do you wish to set a price search for the restaurants? y/n")
    while True:
        user_accept_money_filer = input("")
        if user_accept_money_filer == "y":
            print("""
            Choose price range of a restaurant:
            1) 5 to 10 dollars per meal
            2) 10 to 30 dollars per meal
            3) 30 and above dollars per meal
            """)
            cost_input = []
            while True:
                user_cost_input = input("")
                if int(user_cost_input) in range(1, 4, 1):
                    cost_input.append(int(user_cost_input))
                    break
                else:
                    print("Wrong input type a number from 1 to 3")
            for key in moderated_dictionary.keys():
                if moderated_dictionary[key][2] in cost_input:
                    cost_dictionary[key] = moderated_dictionary[key]
            break
        elif user_accept_money_filer == "n":
            cost_dictionary = moderated_dictionary
            break
        print("Wrong input! Please respond with a y or n")
    return cost_dictionary
    
