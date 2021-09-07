"""Restaurant rating lister."""


ratings = open("scores.txt")
# loop through all of the lines in ratings, split on the :, 
# and for each line[1] as the key and line[2] as the value. 

def create_dict(ratings):
    """
    Create a dictionary from a file of restaurant names and ratings.
    Outputs a list of the restaurants and their ratings in alphabetical order.
    """
    rating_dict = {}

    for line in ratings:
        rating_dict[line.split(":")[0]] = line.split(":")[1].rstrip()
    
    add_rest_question(rating_dict)

def add_rest_question(rating_dict):
    """
    Asks user whether they would like to add a restuarant and score to the dictionary.
    Simple yes/no function. "Y" goes to add_restuarant function. "N" shows the current
    dictionary and ends the program. 
    """
    print("Would you like to add a new restaurant rating? y/n")
    rest_quest = input(" > ").lower()
    if rest_quest == "y":
        add_restaurants(rating_dict)
    else: 
        sort_and_print(rating_dict)

def add_restaurants(rating_dict):
    """
    Pulls in the rating_dict from the add_rest_question, which runs
    before this. Asks the user for a new restaurant to add to the
    ratings_dict, followed by a score to add. Adds the new restaurant
    and score, then runs the add_rest_question function to see if they
    would like to add more restaurants & scores.
    """
    
    new_rest = input("Name of restuarant you would like to add? ")
    new_score = input("How would you like to score it? ")
    rating_dict[new_rest] = new_score
    add_rest_question(rating_dict)

def sort_and_print(rating_dict):
    """
    Cycles through the rating_dict, sorts the dictionary on keys,
    and prints out key is rated at value.
    """
    for key, value in sorted(rating_dict.items()):
        print(f"{key} is rated at {value}.")


create_dict(ratings)


