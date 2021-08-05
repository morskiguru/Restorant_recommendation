#import files
import ast
from intro import intro
from location_choice import location_choice, user_location_input
from choose_expenses import choose_expenses
from sorted_dictionary import sort_dictionary

temporary = open("Dict_data.py", "r")
dictionary_data = temporary.read()
dictionary = ast.literal_eval(dictionary_data)
location = []
reset = True

while reset:
    intro()
    location_choice()
    expenses = choose_expenses(dictionary, user_location_input)
    sort_dictionary(expenses)









