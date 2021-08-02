#import files
from intro import intro
from location_choice import location_choice, user_location_input

temporary = open("Dict_data.py", "r")
dictionary_data = temporary.read()
location=[]
reset = True

while reset:
    intro()
    location_choice()






