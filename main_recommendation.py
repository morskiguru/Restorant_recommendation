#import files
import ast
from intro import intro
from location_choice import location_choice, user_location_input
from choose_expenses import choose_expenses
from sorted_dictionary import sort_dictionary

temporary = open("Dict_data.py", "r")
dictionary_data = temporary.read()
dictionary = ast.literal_eval(dictionary_data)
reset = True
location_reset = True
loc_expand = False

while reset:
    intro()
    while location_reset:
        location_choice(loc_expand)
        expenses = choose_expenses(dictionary, user_location_input)
        sort_dictionary(expenses)
        print("Have you find a restaurant?(y/n)")
        while True:
            user_input_if_finished = input("")
            if user_input_if_finished == "y":
                reset = False
                location_reset = False
                break
            elif user_input_if_finished == "n":
                loc_expand = True
                break
            else:
                print("Wrong input")

