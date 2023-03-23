from restaurantData import restaurant_data, types

def autocomplete(s, words):
    return [word for word in words if word.startswith(s)]

def quicksort(words):
    if len(words) <= 1:
        return words
    pivot = words[0]
    left = []
    right = []
    for word in words[1:]:
        if word < pivot:
            left.append(word)
        else:
            right.append(word)
    return quicksort(left) + [pivot] + quicksort(right)

def order_restaurants(list):
    rdict = {}
    for restaurant in list:
        if restaurant[0] not in rdict.keys():
            rdict[restaurant[0]] = [restaurant[1:]]
            continue
        rdict[restaurant[0]] += [restaurant[1:]]
    return rdict

# sort and order types and restaurants
def prepare_types_and_restaurants(types, restaurants):
    sorted_types = quicksort(types)
    restaurant_dict = order_restaurants(restaurants)
    return sorted_types, restaurant_dict

# Print function
def print_restaurants(list):
    for restaurant in list:
        print("************************************************************", end="\n\n")
        print(f"Name: {restaurant[0]}")
        print(f"Price: {restaurant[1]}/5")
        print(f"Price: {restaurant[2]}/5")
        print(f"Address: {restaurant[3]}")
    print("************************************************************", end="\n\n")

def print_types(types):
    printable_types = ""
    for type in types:
        printable_types += type + "  "
    return printable_types

# recommender function
def recommender():
    sorted_types, restaurant_dict = prepare_types_and_restaurants(types, restaurant_data)
    letters = input("What type of food would you like? Enter one or more letters: ").strip().lower()
    choices = autocomplete(letters, sorted_types)
    if choices == []:
        print(f"No food type that starts with {letters}\n")
        print("Please choose from these food types: " + print_types(sorted_types) + "\n")
        recommender()
    else:
        if len(choices) == 1:
            choice = choices[0]
            print(f"Your only choice for your input is: {choice}\n")
            confirmation = input(f"Would you like to view {choice} restaurants? y/n: ").strip().lower()
            if confirmation == "y":
                print_restaurants(restaurant_dict[choice])
        else:
            print("You have multiple choices: " + print_types(choices))
            choice = input("Which one would you like? Enter name: ").strip().lower()
            if choice in choices:
                confirmation = input(f"Would you like to view {choice} restaurants? y/n: ").strip().lower()
                if confirmation == "y":
                    print_restaurants(restaurant_dict[choice])
            else:
                print("This food type was not listed.\n\n")
    confirmation = input("Would you like to search again? y/n: ").strip().lower()
    if confirmation == "y":
        print("\n")
        recommender()
    else:
        print("Thank you for using this service.\n\n")
        quit()
    

print("\nRESTAURANT RECOMMENDER SYSTEM\n")
recommender()