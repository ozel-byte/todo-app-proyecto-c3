import matplotlib.pyplot as plt 
# IA Algoritmo-Genetico 12 5
# IA Tensorflow 13 10
# IA Redes-Neuronales 15 6 
# Ingles Present-Simple 18 8
# Mantenimiento aws 11 6

lista = [
    ("IA1", "Algoritmo-Genetico", 12, 5,1),
    ("IA2", "Tensorflow", 13, 10,1),
    ("IA3", "Redes-Neuronales", 15, 6,1),
    ("Ingles", "Present-Simple", 18, 8,2),
    ("Mantenimiento", "aws", 11, 6,1)
    ]

fig, gnt = plt.subplots(1,figsize=(16,6)) 
gnt.set_xlim(0, 40) 
gnt.set_xlabel('Dias') 
gnt.set_ylabel('Tareas') 
gnt.grid(True) 
count = 0

for i,x in enumerate(lista):
    gnt.barh(x[0],x[2],left=count)
    count = x[2]
# gnt.barh("Tarea1",1,left=5) 
# gnt.barh("Tarea2",5,left=8)
# gnt.barh("Tarea3",8,left=10)
plt.show()
