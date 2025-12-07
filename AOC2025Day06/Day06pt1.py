with open("input.txt") as f:
	inputLines = f.readlines()

problems: list[list[str]] = []
operators: list[str] = []	
			
for i in range(0, len(inputLines)):
	curList: list[str] = inputLines[i].strip().split()
	if i != len(inputLines) - 1:
		problems.append(curList)
	else:
		operators = curList

grandTotal: int = 0
						
for i in range(0, len(problems[0])):
		operator: str = operators[i]
		
		if operator == "+":
			answer: int = 0
			for numList in problems:
				answer += int(numList[i])
		elif operator == "*":
			answer: int = 1
			for numList in problems:
				answer *= int(numList[i])
		
		grandTotal += answer
		
print(f"Grand Total: {grandTotal}")