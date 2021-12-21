# 3x3 matrix
three_columns_matrix = [[12, 7, 3],
                        [4, 5, 6],
                        [7, 8, 9]]

# 3x4 matrix
four_columns_matrix = [[5, 8, 1, 2],
                       [6, 7, 3, 0],
                       [4, 5, 9, 1]]


# result is 3x4
four_columns_result = [[0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0]]


# iterate through rows of three times three
for three_row in range(len(three_columns_matrix)):
    # iterate through columns of three times four
    for four_column in range(len(four_columns_matrix[0])):
        # iterate through rows of three times four
        for four_row in range(len(four_columns_matrix)):
            four_columns_result[three_row][four_column] = \
                  three_columns_matrix[three_row][four_row] * \
                  four_columns_matrix[four_row][four_column]


for row in four_columns_result:
    print(row)
