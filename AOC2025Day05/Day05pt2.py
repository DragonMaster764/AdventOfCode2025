#Read the input
with open("input.txt") as f:
    inputLines: list[str] = f.readlines()

#Remove newlines
inputLines = [line.strip() for line in inputLines]

#Get ranges (everything before blank line), and make them into tuples (start, end)
ingredientRanges: list[list[int, int]] = []
curLineIndex: int = 0
while inputLines[curLineIndex] != "":
    start: int = int(inputLines[curLineIndex].split("-")[0])
    end: int = int(inputLines[curLineIndex].split("-")[1])
    ingredientRanges.append([start, end])
    curLineIndex += 1

#No need for ingredient IDs for part 2

#Sort ranges by start to merge them together
sortByStart = sorted(ingredientRanges, key=lambda x: x[0])

#Start merging ranges together (initalize with first range)
mergedRanges: list[list[int, int]] = [sortByStart[0]]
curMergeRange: int = 0
for r in sortByStart:
    # New range must start before the end (or equal to the end) of the merge range, 
    # and the end of the new range must be greater than the current end of the merge range
    if r[0] <= mergedRanges[curMergeRange][1] and r[1] > mergedRanges[curMergeRange][1]:
        #Extend the range to the new end
        mergedRanges[curMergeRange][1] = r[1]

        #If the range start is after the end of the current merged range, add a new range we will merge on, and move our efforts to that one
    elif r[0] > mergedRanges[curMergeRange][1]:
        mergedRanges.append(r)
        curMergeRange += 1

#Now go through merged ranges, and total up the IDs (end - start + 1)
freshIDs: int = 0
for r in mergedRanges:
    freshIDs += (r[1] - r[0] + 1)

print(f"Number of fresh IDs: {freshIDs}")