#Read the file
with open("input.txt") as f:
    bankList: list[str] = f.readlines()

#Go through the list, getting rid of the \n
banks: list[str] = [line.strip() for line in bankList]

#Find Largest Function (start and end (excluded) index to search, and the list)
#Returns [largest (the actual number), largest_index (index of the largest number)]
def findLargest(bank, start, end):
    largest: int = -1
    largest_index: int = -1
    for i in range(start, end):
        if int(bank[i]) > largest:
            largest = int(bank[i])
            largest_index = i
    
    return [largest, largest_index]


#Joltage variable keeping track of joltage
joltage: int = 0

for bank in banks:
    
    #Find the largest. List: [largest, largest_index]
    largest: list[int] = findLargest(bank, 0, len(bank))

    #Check the largest_index is not at the end of the list (no secondary battery to pick!)
    if largest[1] == len(bank) - 1:
        #Check for the next largest by searching everything before the largest
        largest = findLargest(bank, 0, largest[1])

    #Now check for the next largest AFTER the largest_index (second largest)
    secondLargest: list[int] = findLargest(bank, largest[1] + 1, len(bank))
    
    #Now get the number when you combine them, and add it to joltage
    bankJoltage: int = int(str(largest[0]) + str(secondLargest[0]))
    joltage += bankJoltage

print(joltage)