from queue import Queue

with open("input.txt") as f:
	inputLines: list[str] = [line.strip() for line in f.readlines()]
	
map: list[list[str]] = []
for i in range(0, len(inputLines)):
	row: list[str] = []
	for j in range(0, len(inputLines[i])):
		row.append(inputLines[i][j])
		
		if inputLines[i][j] == "S":
			startingPos: tuple = (i, j)
	map.append(row)

numSplitters: int = 0

beamQueue: Queue[tuple] = Queue()
beamQueue.put(startingPos)
while not beamQueue.empty():
	curPos: tuple = beamQueue.get()
	posNewPos: tuple = (curPos[0] + 1, curPos[1])
	
	if posNewPos[0] < len(map):
		if map[posNewPos[0]][posNewPos[1]] == "^":
			numSplitters += 1
			if map[posNewPos[0]][posNewPos[1]-1] == "." and posNewPos[1] - 1 >= 0:
				map[posNewPos[0]][posNewPos[1]-1] = "|"
				beamQueue.put((posNewPos[0], posNewPos[1] - 1))
			
			if map[posNewPos[0]][posNewPos[1]+1] == "." and posNewPos[1] + 1 < len(map[posNewPos[0]]):
				map[posNewPos[0]][posNewPos[1]+1] = "|"
				beamQueue.put((posNewPos[0], posNewPos[1] + 1))
		
		elif map[posNewPos[0]][posNewPos[1]] == ".":
			map[posNewPos[0]][posNewPos[1]] = "|"
			beamQueue.put((posNewPos[0], posNewPos[1]))

print(f"Num Splitters: {numSplitters}")