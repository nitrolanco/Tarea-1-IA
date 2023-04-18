import funciones as busquedas


def main():
    (initNode, finalNode), valHeuristica, arcos = busquedas.getData()
    while True:
        metodo = input('Elija el método de busqueda a emplear, ingrese:\n 1 para Búsqueda en produndidad \n 2 para búsqueda de costo uniforme \n 3 para búsqueda greedy \n 4 para A estrella \n 0 para terminar ejecución \n')
        if metodo == '1':
            print("Mostrando búsqueda en profundidad")
            print(busquedas.dfs(initNode, finalNode, arcos))
            input("Presione enter para elegir otro método\n")
        elif metodo == '2':
            print("Mostrando búsqueda costo uniforme")
            print(busquedas.uCost(initNode, finalNode, arcos, valHeuristica))
            input("Presione enter para elegir otro método\n")

        elif metodo == '3':
            print("Mostrando búsqueda greedy")
            print(busquedas.greedy(initNode, finalNode, valHeuristica, arcos))
            input("Presione enter para elegir otro método\n")

        elif metodo == '4':
            print("Mostrando búsqueda A estrella")
            print(busquedas.aStar(initNode, finalNode, valHeuristica, arcos))
            input("Presione enter para elegir otro método\n")
        elif metodo == '0':
            break
        else:
            pass
    return 0


main()
