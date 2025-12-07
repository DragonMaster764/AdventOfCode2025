def solve_problem(problem: list[int], operator: str) -> int:
		if operator == "+":
			answer: int = 0
			for num in problem:
				answer += num
		elif operator == "*":
			answer: int = 1
			for num in problem:
				answer *= num
		
		return answer


with open("input.txt") as f:
	inputLines = f.readlines()

rows: list[list[str]] = []
operators: list[str] = []	
			
for i in range(0, len(inputLines)):
	curLine: str = inputLines[i]
	if i != len(inputLines) - 1:
		curRow: list[str] = [c for c in curLine if c != "\n"]
		rows.append(curRow)
	else:
		operators = curLine.split()
		
grandTotal: int = 0

curOperatorIndex: int = len(operators) - 1
operator: str = operators[curOperatorIndex]

problem: list[int] = []
						
for i in range(len(rows[0]) - 1, -1, -1):
		curNum: str = ""
		
		for row in rows:
				if row[i] != ' ':
					curNum += row[i]
					
		if curNum != "":
				problem.append(int(curNum))
		else:
			#Solve Problem
			grandTotal += solve_problem(problem, operator)
			
			#Next operator
			curOperatorIndex -= 1
			operator = operators[curOperatorIndex]
			
			#Reset the problem (new problem now)
			problem=[]
			
#Solve final problem
grandTotal += solve_problem(problem, operator)
		
print(f"Grand Total: {grandTotal}")