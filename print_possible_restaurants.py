from location_choice import location_choice, user_location_input
from choose_expenses import choose_expenses
from helper_functions import sort_dictionary

def give_recommendation(dictionary, location, reset):
    moderated_dictionary = choose_expenses(dictionary, location)
    sorted_dictionary = sort_dictionary()

