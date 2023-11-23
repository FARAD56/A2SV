# --------------------------------------
# Function to convert Adjacency Matrix to Adjacency List
def adjacency_matrix_to_adjacency_list(adj_matrix):
    adj_list = {}

    # Write your code here to convert the adjacency matrix to an adjacency list
    # Your code goes here

    return adj_list  # Return the adjacency list

# Test case
adj_matrix_sample = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1]
]

# --- Student Section to Write Code ---
from collections import defaultdict

Dict = defaultdict(list)

def adjacency_matrix_to_adjacency_list(adj_matrix_sample):
    for src in range(len(adj_matrix_sample)):
        for dest in range(len(adj_matrix_sample[0])):
            if adj_matrix_sample[src][dest] == 1:
                Dict[src].append(dest)
    return Dict



# Write your code for the conversion here
result_adj_list = adjacency_matrix_to_adjacency_list(adj_matrix_sample)
expected_result = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

# Print the result for verification
print("Result:", result_adj_list)
if result_adj_list == expected_result:
    print("Correct! Your code produced the expected result.")
else:
    print("Incorrect! Please try again")
# --------------------------------------
