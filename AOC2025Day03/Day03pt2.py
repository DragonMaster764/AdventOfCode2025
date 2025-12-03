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
    
    batteriesLeft: int = 12
    batteryNums: list[int] = []
    start: int = 0

    for i in range(0, 12):
        #Find the largest number. List: [largest, largest_index]
        largest: list[int] = findLargest(bank, start, len(bank))

        #while there isn't enough batteries after the largest, look before it
        while largest[1] + (batteriesLeft - 1) >= len(bank):
            largest = findLargest(bank, start, largest[1])

        #Add battery to batteryNums
        batteryNums.append(largest[0])
        batteriesLeft -= 1

        #Now look for the next largest with the start being the largest_index + 1
        start = largest[1] + 1

    #Now get the number when you combine them, and add it to joltage
    bankJoltage: str = ""
    for battery in batteryNums:
        bankJoltage += str(battery)
    joltage += int(bankJoltage)

print(joltage)