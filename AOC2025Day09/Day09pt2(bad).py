class red_tile:
    x: int
    y: int

    def __init__(self, x, y):
        self.x, self.y = x, y

    def calc_area(self, other) -> int:
        l: int = ((self.x - other.x) + 1)
        w: int = ((self.y - other.y) + 1)
        return l*w
    

def isVerticalEdge(edge) -> bool:
    return edge[0].x == edge[1].x and edge[0].y != edge[1].y


#True = Inside, False = Outside
def raycast(edges:list, x:int, y: int) -> bool:
    numIntersect: int = 0
    for i in range(x, 2000):
        for edge in edges:
            if edge[0].x == i and isVerticalEdge(edge):
                minY: int = min(edge[0].y, edge[1].y)
                maxY: int = max(edge[0].y, edge[1].y)
                if y >= minY and y <= maxY:
                    numIntersect += 1
    print(numIntersect)
    return numIntersect % 2 == 1


#Validates rectangle is within shape
def validate_rect(edges: list, c1: red_tile, c2: red_tile) -> bool:
    minX, maxX, minY, maxY = 0, 0, 0, 0
    minX = min(c1.x, c2.x)
    maxX = max(c1.x, c2.x)
    minY = min(c1.y, c2.y)
    maxY = max(c1.y, c2.y)
    print(f"{minX}, {maxX}, {minY}, {maxY}")

    """#Raycast each row
    goodRect: bool = True
    for i in range(minY, maxY + 1):
        #If the raycast returned false (outside)
        if not raycast(edges, i, minX, maxX):
            goodRect = False
            break"""
    
    #Raycast the corners
    goodRect = (raycast(edges, minX, minY) and raycast(edges, minX, maxY) 
                and raycast(edges, maxX, minY) and raycast(edges, maxX, maxY))

    return goodRect


#Read input file for the red tiles
with open("input.txt") as f:
    inputLines: list[str] = [line.strip() for line in f.readlines()]

#Make a list of tiles
tileList: list[red_tile] = []
for tile in inputLines:
    tileSplit: list[str] = tile.split(",")
    tileList.append(red_tile(int(tileSplit[0]), int(tileSplit[1])))

#list of green tile edges
edges: list[red_tile] = []
for i in range(0, len(tileList)-1):
    edges.append([tileList[i], tileList[i+1]])
edges.append([tileList[len(tileList) - 1], tileList[0]])

#Go through getting areas
areaList: list[list] = []
for i in range(0, len(tileList)):
    for j in range(i+1, len(tileList)):
        area: int = tileList[i].calc_area(tileList[j])
        areaList.append([area, tileList[i], tileList[j]])

#Sort by largest area
sortedAreas = sorted(areaList, key=lambda x: x[0], reverse=True)

#Check if the rectangle is within the inside of the shape
curRect = 0
while curRect < len(sortedAreas) and not validate_rect(edges, sortedAreas[curRect][1], sortedAreas[curRect][2]):
    curRect += 1

print(curRect)
print(sortedAreas[curRect][0])

print(f"Maximum Area: {sortedAreas[0][0]}")