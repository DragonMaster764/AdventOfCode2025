import math

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

        #If the number in our range can be split in half, and both halves are the same, add it to invalidIDs
        if len(numString) % 2 == 0:
            if numString[:len(numString) // 2] == numString[len(numString) // 2:]:
                invalidIDs += x


print (invalidIDs)

    
    