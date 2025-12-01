#Read the instructions from the file
with open("input.txt") as f:
    instructions: list[str] = [line.strip() for line in f.readlines()]

#Keep track of 0s (the password) and current inital number on the safe (start at 50)
password: int = 0
safeInitNum: int = 50

#Go through each step in the safe combo
for step in instructions:
    #Seperate the direction, distance, and if it passed zero
    direction: str = step[:1]
    distance: int = int(step[1:])
    passOrLandedZero: bool = False

    #Number of rotations is how many times it goes around the safe (thus passing 0)
    rotations: int = (distance) // 100

    if direction == "R":
        #Get the final num by the distance (if it goes right of 99, we use mod 100 to keep it 0->99)
        safeFinalNum: int = (safeInitNum + distance) % 100
        #Check if it passed (or landed on) 0 on its journey
        passOrLandedZero = (safeFinalNum < safeInitNum and safeInitNum != 0) or safeFinalNum == 0
    else:
        #Get the final num by the distance (if it goes left of 0, we use mod 100 to keep it between 0->99)
        safeFinalNum: int = (safeInitNum - distance) % 100
        #Check if it passed (or landed on) 0 on its journey
        passOrLandedZero = (safeFinalNum > safeInitNum and safeInitNum != 0) or safeFinalNum == 0

    #Password is rotations (for sure passed zero) + if the number passed or landed on 0 in the last partial rotation
    password += rotations + passOrLandedZero

    #Set the new inital number to the safeFinalNum
    safeInitNum = safeFinalNum

print(f"Password: {password}")


    
