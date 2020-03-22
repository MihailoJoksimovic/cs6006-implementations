# Nullify matrix: given the matrix, if any element is 0, then the whole row and column should be set to 0

# If we iterate one by one, the whole matrix will become 0 ... that's bad.

# We need some way to store the elements to zero out. One option is to use another matrix and to set to 0 elements that
# need to be zeroed out.
# Another way is to just store rows and cols that need to be nullified. That's kind of a better one ...
# The third option is some tricky shit and I still can't figure it out honestly.

def nullify(row, col, m, n, matrix):
    # First nullify the row
    for i in range(n):
        matrix[row][i] = 0

    # Then nullify column
    for i in range(m):
        matrix1[i][col] = 0

    return matrix1

matrix1 = [
    [5, 0, 4],
    [3, 7, 1]
]

zeros_matrix = [[None for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

# Iterate through matrix and set 0s where needed

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        if matrix1[i][j] == 0:
            zeros_matrix[i][j] = 1

# Now iterate through zeros matrix and nullify rows and cols ...

# However, a better solution is to just keep row or col. that needs to be nullified

nullify_rows = []
nullify_cols = []

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        nullify_rows.append(i)
        nullify_rows.append(j)

# Now iterate through nullify rows and nullify cols and ... well, nullify :)

# Now, there was a question -- whether we can do this without EXTRA space?
# This is where it gets tricky. But here's the thing -- we know that if, for example in first row, if any col. has 0,
# then we can set the first el. of that row to 0. Same goes for column -- if at any row the column has 0, we can nullify
# the whole ...

firstRowHasZeros = False
firstColHasZeros = False

# Check if first row and first col have zeros
for i in range(0, len(matrix1[0])):
    if matrix1[0][i] == 0:
        firstRowHasZeros = True
        break

for j in range(0, len(matrix1)):
    if matrix1[j][0] == 0:
        firstColHasZeros = True
        break

# Check for zeros in the rest of the array

for i in range(1, len(matrix1)):
    for j in range(1, len(matrix1[0])):
        if matrix1[i][j] == 0:
            matrix1[i][0] = 0
            matrix1[0][j] = 0

# Now nullify rows and cols

def nullify_row(row):
    pass

def nullify_col(col):
    pass

for i in range(len(matrix1)):
    if matrix1[i][0] == 0:
        nullify_row(i)

for j in range(len(matrix1[0])):
    if matrix1[0][j] == 0:
        nullify_col(j)
