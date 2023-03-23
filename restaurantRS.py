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

def restaurant_dict(list):
    rdict = {}
    for restaurant in list:
        if restaurant[0] not in rdict.keys():
            rdict[restaurant[0]] = [restaurant[1:]]
            continue
        rdict[restaurant[0]] += [restaurant[1:]]
    return rdict

# Print function
def print_restaurants(list):
    pass

# recommender function
def recommender():
    pass



rd = restaurant_dict(restaurant_data)
print(rd["german"][0])








# JUST FOR TEST


"""
words = ['apple', 'banana', 'orange', 'peach', 'pear']
print(autocomplete('a', words)) # ['apple']
print(autocomplete('pe', words)) # ['peach', 'pear']

words = ['pear', 'banana', 'apple', 'orange', 'peach']
sorted_words = quicksort(types)
print(sorted_words) # ['apple', 'banana', 'orange', 'peach', 'pear']

"""