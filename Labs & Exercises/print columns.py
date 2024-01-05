def collect_column_items(matrix, n):
    if not matrix or n < 0 or n >= len(matrix[0]):
        return []

    final = []
    for row in range(len(matrix)):
        if n < len(matrix[row]):
            final.append(matrix[row][n])
    return final
