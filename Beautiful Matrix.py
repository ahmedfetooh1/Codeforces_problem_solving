matrix = []
for i in range(5):
    row = list(map(int,input().split()))
    matrix.append(row)
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1 :
            index_row = i +1
            index_col = j + 1 
            break
print(abs(index_row - 3) + abs(index_col - 3))