class red_tile:
    x: int
    y: int

    def __init__(self, x, y):
        self.x, self.y = x, y

    def calc_area(self, other) -> int:
        l: int = ((self.x - other.x) + 1)
        w: int = ((self.y - other.y) + 1)
        return l*w


#Read input file for the red tiles
with open("input.txt") as f:
    inputLines: list[str] = [line.strip() for line in f.readlines()]

#Make a list of tiles
tileList: list[red_tile] = []
for tile in inputLines:
    tileSplit: list[str] = tile.split(",")
    tileList.append(red_tile(int(tileSplit[0]), int(tileSplit[1])))

#Go through looking for largest area
maxArea: int = 0
for i in range(0, len(tileList)):
    for j in range(i+1, len(tileList)):
        area: int = tileList[i].calc_area(tileList[j])
        if area > maxArea:
            maxArea = area

print(f"Maximum Area: {maxArea}")