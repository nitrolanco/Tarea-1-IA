import random


def getData():
    with open("graph.txt", "r") as file:
        lines = file.readlines()
        initNode = str(lines[0].split(": ")[1].strip())
        finalNode = str(lines[1].split(": ")[1].strip())
        valHeuristica = []
        for i in range(2, 10):
            a, b = lines[i].split(" ")
            valHeuristica.append((str(a).strip(), int(b)))
        arcos = []
        for i in range(10, len(lines)):
            a, b, c = lines[i].split(",")
            arcos.append((str(a).strip(), str(b).strip(), int(c)))
        return [(initNode, finalNode), valHeuristica, arcos]


def dfsNext(current, arcos):
    possibles = []
    for a in arcos:
        if a[0] == current:
            possibles.append(a)
    return possibles[random.randint(0, len(possibles)-1)]


def pathPrinter(path):
    for i in range(0, len(path)):
        if i < len(path)-1:
            print(path[i] + "->", end="")
        else:
            print(path[i])


def onceExpanded(path):
    for i in range(0, len(path)):
        print(path[i] + ": 1", end="\n")


def dfs(initNode, finalNode, arcos):
    totalCost = 0
    visited = []
    current = initNode
    visited.append(current)
    while (current != finalNode):
        next = dfsNext(current, arcos)
        totalCost += next[2]
        current = next[1]
        visited.append(current)
    pathPrinter(visited)
    print("Costo: "+str(totalCost), end=" ")
    onceExpanded(visited)
    if totalCost == 18:
        print("Costo: "+str(totalCost) + ", el costo es óptimo.")
    else:
        print("Costo: "+str(totalCost) + ", el costo no es óptimo")
    return " "


def greedyNext(current, valHeuristica, arcos):
    possibles = []
    for a in arcos:
        if a[0] == current:
            val = 0
            getVal(a[1], valHeuristica)
            possibles.append((a[2]+val, a))
    sortedPossibles = sorted(possibles)
    return sortedPossibles[0][1]


def greedy(initNode, finalNode, valHeuristica, arcos):
    totalCost = 0
    current = initNode
    visited = []
    visited.append(current)
    while (current != finalNode):
        next = greedyNext(current, valHeuristica, arcos)
        totalCost += next[2]
        current = next[1]
        visited.append(current)
    pathPrinter(visited)
    print("Costo: "+str(totalCost), end=' ')
    onceExpanded(visited)
    if totalCost == 18:
        print("Costo: "+str(totalCost) + ", el costo es óptimo.")
    else:
        print("Costo: "+str(totalCost) + ", el costo no es óptimo")
    return " "


def getVal(node, valHeuristica):
    val = 0
    for b in valHeuristica:
        if b[0] == str(node):
            val = b[1]
            return val
    return -100000000000


def avStar(currPath, arcos, valHeuristica):
    avaibles = []
    for a in arcos:
        if a[0] == currPath[-1]:
            val = getVal(a[1], valHeuristica)
            posNext = []
            posNext = currPath[:]
            pastVal = getVal(posNext[-1], valHeuristica)
            posNext.append(a[1])
            posNext[0] = a[2]+val+posNext[0] - pastVal
            avaibles.append(posNext)
    return avaibles


def aStar(initNode, finalNode, valHeuristica, arcos):
    pQ = []
    visited = []
    current = initNode
    currPath = [getVal(current, valHeuristica), current]
    pQ.append(currPath)
    while (current != finalNode):
        avaibles = []
        avaibles = avStar(currPath, arcos, valHeuristica)
        for a in avaibles:
            pQ.append(a)
        visited.append(pQ[0])
        pQ.pop(0)
        pQ = sorted(pQ)
        current = pQ[0][-1]
        currPath = pQ[0]
    visited.append(pQ[0])
    pathPrinter(currPath[1:])
    visitedNodes(visited, valHeuristica)
    if currPath[0] == 18:
        print("Costo: "+str(currPath[0])+", el costo es óptimo.")
    else:
        print("Costo: "+str(currPath[0]) + ", el costo no es óptimo")
    return " "


def visitedNodes(visited, valHeuristica):
    timesVisited = dict()
    for (node, valH) in valHeuristica:
        timesVisited[node] = 0
    for node, value in timesVisited.items():
        for path in visited:
            if (node == path[-2]):
                timesVisited[node] += 1
    for node, value in timesVisited.items():
        for path in visited:
            if (timesVisited[node] == 0 and node == path[-1]):
                timesVisited[node] += 1
    for node, value in timesVisited.items():
        print(str(node)+": "+str(value))


def avUC(currPath, arcos):
    avaibles = []
    for a in arcos:
        if a[0] == currPath[-1]:
            posNext = []
            posNext = currPath[:]
            posNext.append(a[1])
            posNext[0] = a[2]+posNext[0]
            avaibles.append(posNext)
    return avaibles


def uCost(initNode, finalNode, arcos, valHeuristica):
    pQ = []
    visited = []
    current = initNode
    currPath = [0, current]
    pQ.append(currPath)
    while (current != finalNode):
        avaibles = []
        avaibles = avUC(currPath, arcos)
        for a in avaibles:
            pQ.append(a)
        visited.append(pQ[0])
        pQ.pop(0)
        pQ = sorted(pQ)
        current = pQ[0][-1]
        currPath = pQ[0]
    visited.append(pQ[0])
    pathPrinter(currPath[1:])
    visitedNodes(visited, valHeuristica)
    if currPath[0] == 18:
        print("Costo: "+str(currPath[0])+", el costo es óptimo.")
    else:
        print("Costo: "+str(currPath[0]) + ", el costo no es óptimo")
    return " "
