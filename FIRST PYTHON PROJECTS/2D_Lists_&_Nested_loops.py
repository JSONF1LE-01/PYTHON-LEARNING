number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[0][2], "ignore wut the hell")
#nested for loop (print all values in the list)

for row in number_grid:
    for column in row:
        print(column)