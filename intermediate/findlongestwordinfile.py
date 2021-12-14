import os.path


def find_longest_word_in_file(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    max_length = len(max(words, key=len))
    return [word for word in words if len(word) == max_length]


print(find_longest_word_in_file(os.path.realpath('test.txt')))
