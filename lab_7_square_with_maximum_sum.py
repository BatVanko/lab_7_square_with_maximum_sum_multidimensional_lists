import sys


def square_matrix_2_from_coordinates(mat, ro, co):
    result = []
    if 0 <= ro < len(mat)  and 0 <= co < len(mat[0]) :
        result = [[mat[ro][co], mat[ro][co + 1]],
                  [mat[ro + 1][co], mat[ro + 1][co + 1]]
                  ]

    return result


row, col = [int(x) for x in input().split(', ')]

matrix = []
max_matrix = []
max_sum = - sys.maxsize

for _ in range(row):
    matrix.append([int(x) for x in input().split(', ')])
for i in range(len(matrix)-1):
    for j in range(len(matrix[0])-1):
        current_matrix = square_matrix_2_from_coordinates(matrix, i, j)

        sum_matrix = 0
        for k in range(len(current_matrix)):
            for l in range(len(current_matrix[0])):
                sum_matrix += current_matrix[k][l]
                if sum_matrix > max_sum:
                    max_sum = sum_matrix
                    max_matrix = current_matrix

for i in range (len(max_matrix)):
    print(*max_matrix[i], sep=' ')
    # print(' '.join([str(x) for x in max_matrix[i]]))
print(max_sum)

