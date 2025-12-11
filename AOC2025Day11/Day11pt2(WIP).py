class node:
    name: str
    adjList: list

    def __init__(self, name):
        self.name = name


def visit_path(visited: list[str], curNode: node, dac: bool, fft: bool) -> int:
    if curNode.name == "out":
        #Check that "dac" and "fft" have been visited before
        if dac and fft:
            return 1
        else:
            return 0
    elif curNode.name in visited:
        return 0
    else:
        #Add the node as being visited
        visited.append(curNode.name)

        if curNode.name == "dac":
            dac = True

        if curNode.name == "fft":
            fft = True
        
        #Keep track of valid paths going down each device
        valid_paths: int = 0
        for d in curNode.adjList:
            valid_paths += visit_path(visited, d, dac, fft)
        
        #Once we are done visiting this node, we can remove it from being visited
        visited.remove(curNode.name)
        return valid_paths


#Read file input
with open("input.txt") as f:
    inputLines: list[str] = [line.strip() for line in f.readlines()]

deviceStr: list[str] = [line.split(":")[0] for line in inputLines]
connectionsStr: list[str] = [line.split(":")[1] for line in inputLines]

#Make all the nodes into devices, then add the adjList
devices: list[node] = []
svrIndex = -1  #Marks which device is the start (svr)
for i in range(0, len(deviceStr)):
    curDevice = deviceStr[i]
    devices.append(node(curDevice))
    if curDevice == "svr":
        svrIndex = i

#Add an out device
devices.append(node("out"))

#Now add the adjacency lists
for i in range(0, len(devices)-1):
    adjNodes: list[str] = connectionsStr[i].split()
    adjList: list[node] = []
    for d in devices:
        if d.name in adjNodes:
            adjList.append(d)
    
    devices[i].adjList = adjList

#Start with nodes at the "svr" device
paths: int = 0
for d in devices[svrIndex].adjList:
    paths += visit_path(["svr"], d, False, False)

print(f"Paths: {paths}")