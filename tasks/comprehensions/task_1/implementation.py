def flatten_list(matrix: list) -> list:
    return [k for i in matrix for k in i]


test = [[1,2], [3,4]]
print(flatten_list(test))