#This function counts the neighbors with @ and returns the number of "@" neighbors
def count_neighbors(grid: list[list[str]], curRow: int, curCol: int, numRows: int, numCols: int) -> int:
    neighbors: int = 0
    #Check a 3x3 grid starting from the top left corner of the current spot, to the bottom right
    for i in range(curRow - 1, curRow + 2):
        for j in range(curCol - 1, curCol + 2):
            #Check the space is in bounds
            if (i >= 0 and i < numRows) and (j >= 0 and j < numCols):
                #Check if it is also a "@" and it's not the current spot we are checking for neighbors at (the center of our 3x3 grid)
                if (grid[i][j] == "@" and [i, j] != [curRow, curCol]):
                    neighbors += 1

    return neighbors


#Read the file input
with open("input.txt") as f:
    inputLines: list[str] = f.readlines()

#Get rid of the new line characters
inputLines = [line.strip() for line in inputLines]

#Make our grid into a 2D list
grid: list[list[str]] = []
for line in inputLines:
    #Go row by row, and sperate every character, then add the row to the grid
    row: list[str] = []
    for c in line:
        row.append(c)
    grid.append(row)

#Variables for our limits
numRows:int = len(grid)
numCols:int = len(grid[0])

#Count possible rolls
rolls: int = 0

#Keeps track of how many rolls were removed this round (-1 to start the while loop)
rollsRemoved: int = -1

while rollsRemoved != 0:
    rollsRemoved = 0
    #Now go through each row, checking the 8 adjacent neighbors of an '@' symbol, counting up other '@'s
    for i in range(0, numRows):
        for j in range(0, numCols):
            if grid[i][j] == "@":
                numNeighbors: int = count_neighbors(grid, i, j, numRows, numCols)
                
                if numNeighbors < 4:
                    #Remove the roll from the grid, and add to rolls removed
                    grid[i][j] = "."
                    rollsRemoved += 1
    
    #Add the current removed rolls this round to "rolls"
    rolls += rollsRemoved

print(f"Rolls: {rolls}")
