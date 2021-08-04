import ast
import json
import random


names = ["Abe's", "Martins Stake-house", "Gatsby's", "Fish and Crisps", "Food Vault", "Tasty Delights", "The Vagabond",
         "Farosh's", "Gstronomish", "Giagantia", "Pork and Stuff", "Lamb Lamb Lamb", "Vila Salad Bar", "Crispy+s",
         "McTavish Diner", "McDonalds", "Wok One", "Wok Two", "Fredoe's", "Wendy's", "Blitz Bar", "Kriger's Shnupies",
         "Quencher", "Waldoe's", "Ernie's", "Restaurant", "Teriaki", "ZigZags", "Ulma's Place", "Indian Food's",
         "Oh My God", "Pork and More Pork", "Aquatico", "Serengeti's Special's", "Devotion To Food",
         "Free Your Hunger", "Greg's", "Holly's", "Joker's", "Khal Of Taste", "Lorein's", "Y U Du Dis", "Xandar's",
         "Crucial Food", "Voluntary Eating", "Barnabus", "Night Out", "Moonlight Share", "Giddy", "Witty",
         "Monochrom Food", "Doddle Food", "Asparagus", "Pesto", "Thought It Was Pesto", "Its Asparagus", "Brunch",
         "Overpriced Eggs", "Glendrim's", "Walihuuu", "Wladoe's", "Kalorom", "Brokulon", "Witcher Pray",
         "Sorcerers Foods", "Tolkien House", "The Hobitton", "The Malevolent Stomach", "Amazing Food", "What What",
         "Addicted To Food", "Where To Hunger Goes", "Tho Whom The Belly Groans", "Me And My Appetite"]

Locations = [["Center", 0], ["West Side", 1], ["East Side", 2], ["North Side", 3], ["South Side", 4], ["Outskirts", 5]]

# Creating Fake Dictionary With key name of
# local and value a list containing [address, location value, cost_value, review]
# location value 1-6 Center, West East North South Outskirts
Dictionary_information = {}
for i in range(len(names)):
    k = random.choice(range(8))
    if k >= 5:
        k = 5
    j = random.randint(1, 3)
    m = random.randint(40, 101) / 10.0

    if j == 1:
        m -= 2.0
    elif j == 2:
        m -= 1.0
    if k == 0:
        m += 1.0
        if m >= 10.0:
            m = 10.0
    elif k == 5:
        m -= 1.00
    m = round(m, 1)

    Dictionary_information[names[i]] = [Locations[k][0]+" "+str(random.choice(range(100))), Locations[k][1]+1,
                                        j, m]
print(Dictionary_information)
Dict_file = open("Dict_data.txt", "w")
json.dump(Dictionary_information, Dict_file)
Dict_file.close()
# Dictionary for restaurants key = name of restaurant, values = [address, location number, expenses score]
test = open("Dict_data.txt", "r")
Dictionary_test = test.read()
Dictionary_test_dict = ast.literal_eval(Dictionary_test)
print(Dictionary_test_dict)
