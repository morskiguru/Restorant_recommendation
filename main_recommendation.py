#import files
import ast
from intro import intro
from location_choice import location_choice, user_location_input
from choose_expenses import choose_expenses
from print_possible_restaurants import give_recommendation

temporary = open("Dict_data.py", "r")
dictionary_data = temporary.read()
dictionary = ast.literal_eval(dictionary_data)
location = []
reset = True

while reset:
    intro()
    location_choice()
    reset = give_recommendation(dictionary, user_location_input)









