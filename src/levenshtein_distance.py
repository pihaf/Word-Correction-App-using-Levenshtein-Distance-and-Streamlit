def levenshtein_distance(source_string, target_string):
    num_rows = len(source_string) + 1
    num_cols = len(target_string) + 1
    matrix = [[0] * num_cols for _ in range(num_rows)]

    for r in range(num_rows):
        matrix[r][0] = r
    for c in range(num_cols):
        matrix[0][c] = c

    for r in range(1, num_rows):
        for c in range(1, num_cols):
            if source_string[r - 1] == target_string[c - 1]:
                cost = 0
            else:
                cost = 1

            ins_cost = matrix[r][c - 1] + 1
            del_cost = matrix[r - 1][c] + 1
            sub_cost = matrix[r - 1][c - 1] + cost
            matrix[r][c] = min(ins_cost, del_cost, sub_cost)

    # Return the levenshtein distance
    return matrix[num_rows - 1][num_cols - 1]
