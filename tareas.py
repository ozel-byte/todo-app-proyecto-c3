


import numpy


tarea = [
    ("T1","ST1",3,12),
    ("T2","ST2",5,13),
    ("T3","ST3",4,15),
    ("T4","ST4",3,18)
]

individuos = [
    [4,2,1,3],
    [1,2,3,4],
    [3,1,4,2],
]
def calcularTareaPorIndividuo(lista,num):
    listaTareasChidas = []
    totalHrs = 0
    listaHrs = []
    listaTareas = []
    for x in lista:
        totalHrs += tarea[x-1][3]
        listaHrs.append(totalHrs)
        listaTareas.append(tarea[x-1])
    for i,x in enumerate(listaHrs):
        print(f"|{x}|",end=" ")
        hrsTarea = listaTareas[i][2]*8
        if x <= hrsTarea:
            print(f"{listaTareas[i][0]} Tarea valida")
            listaTareasChidas.append(listaTareas[i])
        else:
            print(f"{listaTareas[i][0]} Tarea Invalida")


    return ("Individuo"+str(num),len(listaTareasChidas),listaTareasChidas)
numIndividuo = 1
print(" ")
listaIndiviudosMejores = []
for i,x in enumerate(individuos):
    listaIndiviudosMejores.append(calcularTareaPorIndividuo(x,i+1))

print(listaIndiviudosMejores)

print(f"Mejor {max([x[1] for x in listaIndiviudosMejores])}")
print(f"Peor  {min([x[1] for x in listaIndiviudosMejores])}") 
print(f"Promedio {numpy.mean([x[1] for x in listaIndiviudosMejores])}")
#print(calcularTareaPorIndividuo(individuos[1],numIndividuo))
#numIndividuo+=1
#print(" ")
#print(calcularTareaPorIndividuo(individuos[0],numIndividuo))
# listaHrsPorIndividuo = []
# for x in individuos:
#     totalHrs = 0
#     for y in x:
#         print(tarea[y-1])
#         totalHrs += tarea[y-1][3]
#     listaHrsPorIndividuo.append(totalHrs)

# for x in range(1,listaHrsPorIndividuo[0]+1):
#     print(x)
#     pass


