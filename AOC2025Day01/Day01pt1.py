#Read the instructions from the file
with open("input.txt") as f:
    instructions: list[str] = [line.strip() for line in f.readlines()]

#Keep track of 0s (the password) and current number on the safe (start at 50)
password: int = 0
safeNum: int = 50

#Go through each step in the safe combo
for step in instructions:
    #Seperate the direction and distance
    direction: str = step[:1]
    distance: int = int(step[1:])

    if direction == "R":
        #Increase the safeNum by the distance (if it goes right of 99, we use mod 100 to keep it 0->99)
        safeNum = (safeNum + distance) % 100
    else:
        #Decrease the safeNum by the distance (if it goes left of 0, we use mod 100 to keep it between 0->99)
        safeNum = (safeNum - distance) % 100

    #If the safeNum is on 0, increase the num
    if safeNum == 0:
        password += 1

print(f"Password: {password}")


    
