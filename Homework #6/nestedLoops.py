'''
The function creates a grid given the number of rows and columns.
Please note that the dimensions with which the grid sits comfortably
are approximately those of a standard IDLE environment.

Note: If the number of columns is odd or even the function creates the grid
anyway. In contrast, the version from the course material did not correctly
print the grid if the column was an even number.
'''

def grid(rows, columns):
    for row in range(rows):
        if row % 2 == 0:
            for column in range(1, columns + 1):
                if column % 2 == 1:
                    if column != columns:
                        print(" ", end = "")
                    else:
                        print(" ")
                else:
                    if column != columns:
                        print("|", end = "")
                    else:
                        print("|")
        else:
            print("-"*columns)

    if rows > 38 or columns > 80:
        return False
    else:
        return True


grid(38, 80)
