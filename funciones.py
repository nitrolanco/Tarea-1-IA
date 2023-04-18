import random


# Función para leer el grafo desde el archivo graph.txt, "hardcodeada" para el grafo en cuestión


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

# Función para decidir el siguiente nodo en busqueda de profundidad, de manera random


def dfsNext(current, arcos):
    possibles = []
    for a in arcos:
        if a[0] == current:
            possibles.append(a)
    return possibles[random.randint(0, len(possibles)-1)]


# Función para printear el camino final tomado por el método de busqueda en cuestión
def pathPrinter(path):
    for i in range(0, len(path)):
        if i < len(path)-1:
            print(path[i] + "->", end="")
        else:
            print(path[i])


# funcion para printear las veces expandidas de búsqueda en profundidad y greedy
def onceExpanded(path):
    for i in range(0, len(path)):
        print(path[i] + ": 1", end="\n")


# Búsqueda en profundidad
def dfs(initNode, finalNode, arcos):
    totalCost = 0
    # lista de nodos visitados
    visited = []
    current = initNode
    visited.append(current)
    # while hasta que llego al nodo final
    while (current != finalNode):
        # decide siguiente nodo en base a la funcion
        next = dfsNext(current, arcos)
        # agrego costo del siguiente nodo
        totalCost += next[2]
        # actualizo el current
        current = next[1]
        # agrego el nuevo current a los visitados
        visited.append(current)
    pathPrinter(visited)
    print("Costo: "+str(totalCost), end=" ")
    onceExpanded(visited)
    if totalCost == 18:
        print("Costo: "+str(totalCost) + ", el costo es óptimo.")
    else:
        print("Costo: "+str(totalCost) + ", el costo no es óptimo")
    return " "

# función que retortna el siguiente nodo a expandir en base al nodo actual para greedy search


def greedyNext(current, valHeuristica, arcos):
    possibles = []
    for a in arcos:
        if a[0] == current:
            val = 0
            getVal(a[1], valHeuristica)
            possibles.append((a[2]+val, a))
    sortedPossibles = sorted(possibles)
    return sortedPossibles[0][1]


# búsqueda greedy
def greedy(initNode, finalNode, valHeuristica, arcos):
    totalCost = 0
    current = initNode
    # lista de nodos visitados
    visited = []
    visited.append(current)
    # while hasta que estoy en el nodo final
    while (current != finalNode):
        # decido el siguiente en base a la función que retorna el nodo más barato desde el actual
        next = greedyNext(current, valHeuristica, arcos)
        # agrego el costo del arco desde current a next
        totalCost += next[2]
        current = next[1]
        # actualizo el current y lo agrego a los nodos visitados
        visited.append(current)
    # printeo los resultados
    pathPrinter(visited)
    print("Costo: "+str(totalCost), end=' ')
    onceExpanded(visited)
    if totalCost == 18:
        print("Costo: "+str(totalCost) + ", el costo es óptimo.")
    else:
        print("Costo: "+str(totalCost) + ", el costo no es óptimo")
    return " "


# Función que retorna el valor de heurística de un nodo
def getVal(node, valHeuristica):
    val = 0
    for b in valHeuristica:
        if b[0] == str(node):
            val = b[1]
            return val
    return -100000000000


# Funcion que retorna los posibles nodos a expandir dado un camino y su costo
# dado un camino de la manera  [costo, nodo,..., nodoActual]
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


# Búsquedaa A estrella
def aStar(initNode, finalNode, valHeuristica, arcos):
    # pQ es una lista usada como priority qeue, para decidir que nodo seguir
    pQ = []
    # visited es una lista en la que almaceno los nodos visitados, su camino y costo
    # cada elemento tiene la forma [costoTotal+heuristica(últimoVisitado),nodo,...,nodo]
    visited = []
    current = initNode
    currPath = [getVal(current, valHeuristica), current]
    pQ.append(currPath)
    # while loopea hasta estar en el nodo final
    while (current != finalNode):
        # lista para expandir nodos posibles desde el nodo actual
        avaibles = []
        avaibles = avStar(currPath, arcos, valHeuristica)
        # avStar retorna nodos accesibles desde el nodo current y su camino y costo
        # de la manera [costo, nodo,...,posibleNodoSiguiente]
        for a in avaibles:
            pQ.append(a)
        visited.append(pQ[0])
        pQ.pop(0)
        pQ = sorted(pQ)
        # pQ sorteada con el nodo a expandir con menor costo en el primer lugar
        # se almacena el nuevo nodo current y el nuevo camino actual.
        current = pQ[0][-1]
        currPath = pQ[0]
    # se almacena el último camino
    visited.append(pQ[0])
    # printeamos los resultados
    pathPrinter(currPath[1:])
    visitedNodes(visited, valHeuristica)
    if currPath[0] == 18:
        print("Costo: "+str(currPath[0])+", el costo es óptimo.")
    else:
        print("Costo: "+str(currPath[0]) + ", el costo no es óptimo")
    return " "


# Funcion que printea los nodos y la cantidad de veces que fueron expandidos
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


# Funcion que retorna los posibles nodos a expandir dado un camino y su costo
# dado un camino de la manera  [costo, nodo,..., nodoActual]
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


# Búsqueda de costo uniforme
def uCost(initNode, finalNode, arcos, valHeuristica):
    # pQ es una lista usada como priority qeue, para decidir a qué nodo ir
    pQ = []
    # visited es una lista en la que almaceno los nodos visitados, su camino y costo
    # cada elemento tiene la forma [costo,nodo,...,nodo]
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
        # pQ sorteada con el nodo a expandir con menor costo en el primer lugar
        # se almacena el nuevo nodo current y el nuevo camino actual.
        current = pQ[0][-1]
        currPath = pQ[0]
    # se almacena el último camino
    visited.append(pQ[0])
    # printeamos los resultados
    pathPrinter(currPath[1:])
    visitedNodes(visited, valHeuristica)
    if currPath[0] == 18:
        print("Costo: "+str(currPath[0])+", el costo es óptimo.")
    else:
        print("Costo: "+str(currPath[0]) + ", el costo no es óptimo")
    return " "
