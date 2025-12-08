import math

class Node:
    x: int
    y: int
    z: int

    def __init__(self, coords: tuple):
        self.x, self.y, self.z = coords

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)
    
    def __hash__(self):
        return hash((self.x, self.y, self.z))


def distance(node1: Node, node2: Node) -> float:
    x1, y1, z1 = node1.x, node1.y, node1.z
    x2, y2, z2 = node2.x, node2.y, node2.z

    #Calculate straight line distance (Euclidean distance)
    distance: float = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    return distance


#Read input values
with open("input.txt") as f:
    inputLines: list[str] = [line.strip() for line in f.readlines()]

#Make a list of nodes with their coordinates in 3D
nodeList: list[Node] = []
for line in inputLines:
    x, y, z = [int(coord) for coord in line.split(",")]
    newNode = Node((x, y, z))
    nodeList.append(newNode)

#Make an edge list with the two nodes, and the distance between them (i.e. [Node1, Node2, distance])
edgeList: list[list] = []
for i in range(0, len(nodeList)):
    for j in range(i + 1, len(nodeList)):
        edgeList.append([nodeList[i], nodeList[j], distance(nodeList[i], nodeList[j])])

#Sort by edges of shortest distance 
distSorted: list[list] = sorted(edgeList, key=lambda x: x[2])

#Intialize Circuits where each node is a "circuit"
circuits: list[set[Node]] = [{n} for n in nodeList]

#Keeps track of the last edge we visited
curEdge: int = -1 

#Keep connecting circuits until the one big circuits (aka len(circuits) == 1)
while len(circuits) != 1:
    #Move to the next edge
    curEdge += 1
    edge: list[Node, Node, float] = distSorted[curEdge]

    circuitsToMerge: list[set[Node]] = []
    for c in circuits:
        for n in c:
            if n == edge[0] or n == edge[1]:
                circuitsToMerge.append(c) #We will merge this circuit with another as the edge has an overlap
                break

    for c in circuitsToMerge:
        circuits.remove(c) #Remove the circuit as we will combine it later and readd it

    #Merge the circuits the edge connects to
    mergedCircuit: set[Node] = set.union(*circuitsToMerge)
    circuits.append(mergedCircuit)

#Total is last two boxes connected's x coords (the last edge needed)
lastEdge: list[Node, Node, float] = distSorted[curEdge]
total: int = lastEdge[0].x * lastEdge[1].x

print(f"Total: {total}")
