import re

#Read the input file
with open("input.txt") as f:
    rangeLine: str = f.readline().strip()

#Split the line into ranges by splitting by the ','
ranges: list[str] = rangeLine.split(",")

#Variable keeping track of all invalid ids
invalidIDs: int = 0

for idRange in ranges:
    #Get the start and end of the range by splitting by the '-'
    start: str = idRange.split("-")[0]
    end: str = idRange.split("-")[1]

    #Go through the range looking for possible double sequences
    for x in range(int(start), int(end) + 1):
        numString = str(x)

        #Use a regular expression pattern to detect repeated numbers (may only be repeated once)
        match = re.search(r"^([0-9]+)\1{1}$", numString)

        #If there was a match, add it to invalidIDs
        if match:
            invalidIDs += int(match.group())


print(invalidIDs)

    
    