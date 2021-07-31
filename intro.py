import sys

def intro():
    print("""
        ********************************************
            Hello To The Hungry Traveler        
        ********************************************
    
We will help you choose the a nice place to eat.    """)
    while True:
        ready = input("Are you ready to pick a restaurant?\nPlease anwser with a yes or no (y/n)")
        if ready == "y" or ready == "yes":
            print("Let's get you a restaurant!!")
            return True
        elif ready == "n" or ready == "no":
            print("Return to The Hungry Traveler when you get hungry!!")
            sys.exit("Goodbye")
