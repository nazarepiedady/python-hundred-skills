def get_file_length(filename):
    with open(filename) as file:
        for line_number, line_content in enumerate(file):
            pass
    return line_number + 1

print('Number of lines in the file: ', get_file_length('test.txt'))
