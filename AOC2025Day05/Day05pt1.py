#Read the input
with open("input.txt") as f:
    inputLines: list[str] = f.readlines()

#Remove newlines
inputLines = [line.strip() for line in inputLines]

#Get ranges (everything before blank line)
ingredientRanges: list[str] = []
curLineIndex: int = 0
while inputLines[curLineIndex] != "":
    ingredientRanges.append(inputLines[curLineIndex])
    curLineIndex += 1

#Skip the blank line, the rest are ingredient IDs
curLineIndex += 1
idList: list[int] = []
for i in range(curLineIndex, len(inputLines)):
    idList.append(int(inputLines[i]))

#Go through each ID and check if it is fresh
numFresh: int = 0
for id in idList:
    for r in ingredientRanges:
        minID: int = int(r.split("-")[0])
        maxID: int = int(r.split("-")[1])

        if id >= minID and id <= maxID:
            numFresh += 1
            break

print(f"Number of Fresh Ingredients: {numFresh}")