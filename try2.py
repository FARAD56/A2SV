def remove_duplicates(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    unique_rows = []
    seen_values = set()

    for row in range(num_rows):
        row_values = tuple(matrix[row][col] for col in range(num_cols))

        if row_values not in seen_values:
            seen_values.add(row_values)
            unique_rows.append(matrix[row])

    return unique_rows

matrix = [
    [1, 2, 3],
    [4, 2, 6],
    [7, 8, 2],
    [9, 2, 3],
    [1, 2, 3]  # Duplicate row
]

unique_matrix = remove_duplicates(matrix)
print(unique_matrix)
