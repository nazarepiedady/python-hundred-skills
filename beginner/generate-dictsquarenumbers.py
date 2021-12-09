def show_dict():
    dictionary = dict()
    
    for number_key in range(1, 21):
        dictionary[number_key] = number_key ** 2
    for (key, value) in dictionary.items():
        print(value)

show_dict()
