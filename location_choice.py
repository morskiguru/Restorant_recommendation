user_location_input = []


def location_choice(expanded_search=False):
    while True:
        print("Lets get started.")
        if not expanded_search:
            user_input = input("""
            Please choose your location where you want to eat:
            1) Center of Town
            2) West Side of Town
            3) East Side of Town
            4) North Side of Town
            5) South Side of Town
            6) Outskirts of town
            """)
            if int(user_input) in list(range(1, 7, 1)):
                user_location_input.append(int(user_input))
                break
        elif expanded_search:
            print("""
            Add in which locations you may want to have a lovely meal
            1) Center of Town
            2) West Side of Town
            3) East Side of Town
            4) North Side of Town
            5) South Side of Town
            6) Outskirts of town
            7) Added all needed locations
            """)
            while True:
                user_expanded_location = input("")
                if int(user_expanded_location) == 7:
                    print("Finished adding locations")
                    break
                elif int(user_expanded_location) in list(range(1, 7, 1)):
                    user_location_input.append(int(user_expanded_location))
            break
