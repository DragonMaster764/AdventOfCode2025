from queue import Queue

def add_node(map: list[list[str]], lastNum: str, newPos: tuple, beamQueue: Queue[tuple]):
	#If the node hasn't been visited, just set the the node to the last number
	if map[newPos[0]][newPos[1]] == ".":
		map[newPos[0]][newPos[1]] = lastNum
		#Add it to the queue
		beamQueue.put((newPos[0], newPos[1]))
	else:
		#If the node was visited, add the lastNum to the current number
		map[newPos[0]][newPos[1]] = str(int(map[newPos[0]][newPos[1]]) + int(lastNum))



with open("input.txt") as f:
	inputLines: list[str] = [line.strip() for line in f.readlines()]

#Make the 2D Map of the tachyon manifold
map: list[list[str]] = []
for i in range(0, len(inputLines)):
	row: list[str] = []
	for j in range(0, len(inputLines[i])):
		#If it is the start, make it 1 (only one path to start with)
		if inputLines[i][j] == "S":
			startingPos: tuple = (i, j)
			row.append("1")
		else:
			#Just append the character normally
			row.append(inputLines[i][j])
	map.append(row)

#Make a queue with the beam spaces we need to visit (and start with the starting position)
beamQueue: Queue[tuple] = Queue()
beamQueue.put(startingPos)
while not beamQueue.empty():
	curY, curX = beamQueue.get()
	curNum: str = map[curY][curX]
	newY, newX = (curY + 1, curX)
	
	if newY < len(map):
		if map[newY][newX] == "^":
			if map[newY][newX-1] != "^" and newX - 1 >= 0:
				add_node(map, curNum, (newY, newX-1), beamQueue)
			
			if map[newY][newX+1] == "." and newX + 1 < len(map[newY]):
				add_node(map, curNum, (newY, newX+1), beamQueue)
		
		else:
			add_node(map, curNum, (newY, newX), beamQueue)

#Go through the last row, and add all the numbers together
timelines: int = 0

for c in map[len(map) - 1]:
	if c != "." and c != "^":
		timelines += int(c)

print(f"Timelines: {timelines}")