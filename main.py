

import random

import sys
from typing import Counter
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import plotly.express as px
import pandas as pd
import numpy
import matplotlib.pyplot as plt

class ViewTask(QMainWindow):
    MATERIA = ' '
    PROBABILIDADDESENDENCIA = 0.0
    PROBABILIDADMUTACION = 0.0
    PROBABILIDADMUTACIONGEN = 0.0
    NOMBRE_TAREA = ' '
    TIEMPO_TAREA = 0
    LISTATAREAS = []
    IMPORTANCIATAREA = ""
    CANTIDADTAREA = 0
    HORASDIA = 0
    TAREASDIA = 0
    LISTAJOINPADREHIJO = []
    GENERACIONES = []
    DIASENTREGA = 0
    DIASTRABAJDOS = 0
    POBLACIONMAXIMA = 0
    COUNT = 0
    GENERACIONES = 10

    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("ui.ui",self)
        self.ventanaDos.hide()
        self.btn_siguiente.clicked.connect(self.agregarDias)
        self.btn_agregar.clicked.connect(self.agregarTareas)
        self.btn_siguiente.setEnabled(False)
        self.btn_siguiente.clicked.connect(self.iniciarIteraccion)
        self.PROBABILIDADDESENDENCIA = 0.86
        self.PROBABILIDADMUTACION = 0.1
        self.PROBABILIDADMUTACIONGEN = 0.15
        self.POBLACIONMAXIMA = 8
    
    def agregarDias(self):
        print("tareas agregadasa")
        if not self.calcularMaximoDia():
            self.ventanaDos.show()

    def validarDatos(self):
        try:
            self.MATERIA = str(self.materia.text())
            self.NOMBRE_TAREA = str(self.nombre_tarea.text())
            self.TIEMPO_TAREA = int(self.tiempo_tarea.text())
            self.HORASDIA = int(self.horas_porDia.text())
            self.TAREASDIA = int(self.tareas_porDia.text())
            self.DIASENTREGA = int(self.dias_de_entrega.text())
            self.DIASTRABAJDOS = int(self.dias_trabajados.text())
        except ValueError:
            print("Datos mal ingresados")

    def agregarTareas(self):
        with open("prueba.txt") as archivo:
            for x in archivo.readlines():
                print(x)
                linea = x.split(" ")
                self.LISTATAREAS.append((
                    linea[0],
                    linea[1],
                    linea[2],
                    linea[3].rstrip("\n")
                ))

        # self.validarDatos()

        # self.LISTATAREAS.append((
        #     self.MATERIA,
        #     self.NOMBRE_TAREA,
        #     self.TIEMPO_TAREA,
        #     self.IMPORTANCIATAREA,
        #     self.DIASENTREGA
        # ))
        
        # self.lista_total.addItem("Materia: "+self.MATERIA+"\n Nombre-Tarea: "+str(self.NOMBRE_TAREA)+"\n Tiempo: "+str(self.TIEMPO_TAREA)+"\n Importancia-Tarea: "+str(self.IMPORTANCIATAREA))
        # self.lista_total.addItem("----------------------------------------------------")
        # self.materia.setText("")
        # self.nombre_tarea.setText("")
        # self.tiempo_tarea.setText("")
        print("lista")
        print(self.LISTATAREAS)
        self.btn_siguiente.setEnabled(True)
    def calcularMaximoDia(self):
        status = False
        li = [int(x[3]) for x in self.LISTATAREAS]
        valorMaximo = max(li)
        print(valorMaximo)
        if valorMaximo > int(self.dias_total_trabajo.text()):
            status = True
        else:
            status=False

        return status 

    def iniciarIteraccion(self):
        if not self.calcularMaximoDia():
            listaUltimaGeneracion = []
            listaIndividuosGeneracion = []
            listaIndividuos = self.generarIndividuos()
            for x in range(self.GENERACIONES):
                listaSeleccionIndividuos = self.seleccionIndividuos(listaIndividuos)
                listaCruzaIndividuos     = self.cruzaIndividuos(listaSeleccionIndividuos)
                listaMutacionIndividuos  = self.mutaTareas(listaCruzaIndividuos)
                listaTareasCal = self.calcularLasMejoresTareas(listaMutacionIndividuos)
                listaIndividuosGeneracion.append(self.calcularMayorPeorPromedio(listaTareasCal))
                listaIndividuos = self.poda(listaTareasCal)
                listaUltimaGeneracion = listaIndividuos
                listaIndividuos = [x[2] for x in listaIndividuos]
            #self.poda()
            self.msjMejorIndividuo.addItem(str(listaUltimaGeneracion[0]))
            self.graficar(listaIndividuosGeneracion)
            self.graficarGantt2(listaUltimaGeneracion)
        else:
            print("error de dia")
    
    def graficarGantt2(self,lista):
        fig, ax = plt.subplots(1,figsize=(16,6))
        print(lista[0][4])
        tareasValidas = lista[0][4]
        print(tareasValidas)
        cont = 0
        cont2 = 0
        listaaux = []
        for i in tareasValidas:
            diasValidos = (int(i[2])/8)
            listaaux.append(diasValidos)
            cont2 += diasValidos

        for y,i in enumerate(tareasValidas):
           print(i)
           diasValidos = (int(i[2])/8)
           ax.barh(i[1]+' '+i[3]+" "+str(listaaux[y]),diasValidos,left=cont) 
           cont += diasValidos
        plt.show()
        pass


    # def graficaGantt(self,lista):
    #     fig, ax = plt.subplots(1,figsize=(16,6))
    #     i = 0
    #     numDiaTareas = []
    #     print(lista[0][2])
    #     tareasValidas = lista[0][2]
    #     tareasValidas = [x[3] for x in tareasValidas]
    #     nombreTareas = []
    #     for j in range(len(tareasValidas)):
    #         tareita = tareasValidas[j]
    #         tareita = int(tareita)
    #         diasTareasValidas = tareasValidas[j] / 8
    #         numDiaTareas.append(tareita)
    #         nombreValido = lista[0][4][j][1]
    #         nombreTareas.append(nombreValido)
    #         print(numDiaTareas[j])
    #         ax.barh(nombreTareas[j],i-1,left=numDiaTareas[j])                  
    #     plt.show()
    
    def individuo_unico(self,aux1,aux2):
        unico = True  
        for i in aux2:
            if aux1 == i:
                unico = False
                break
        return unico

    def generarIndividuos(self):
        print("-----Generar Individuo-----")
        cont = 0
        poblacion = []
        array_individuo = []
        for i in range(int(self.cantidad_tarea_por_materia.text())):
            while cont < len(self.LISTATAREAS):
                num_aleatorio = random.randint(0,len(self.LISTATAREAS)-1)
                if self.individuo_unico(num_aleatorio,array_individuo):
                    array_individuo.append(num_aleatorio)
                    cont += 1
            cont = 0
            poblacion.append(array_individuo)
            array_individuo = []
        print(poblacion)
        return poblacion
        

    def seleccionIndividuos(self,listaIndividuos):
        print("--seleccion de paquetes---")
        listaIndividuosSelecion = []
        self.LISTAJOINPADREHIJO = listaIndividuos
        count = 1
        count2 = 0
        while count < len(listaIndividuos):
            listaIndividuosSelecion.append((listaIndividuos[count2],listaIndividuos[count],random.randint(1,100)/100,random.randint(0,len(self.LISTATAREAS)-1)))
            if count == len(listaIndividuos)-1:
                count2+=1
                count = count2
            count+=1
        print(listaIndividuosSelecion)
        return listaIndividuosSelecion

    def cruzaIndividuos(self,listaSeleccionTareas):
        print("-------cruza------")
        listaCruzaIndividuos = []
        listaProbabilidadDesendencia = []
        for x in listaSeleccionTareas:
            if random.randint(1,100)/100 <= self.PROBABILIDADDESENDENCIA:
                listaProbabilidadDesendencia.append(x)
            pass
        for x in listaProbabilidadDesendencia:
            individuosPaquete1 = x[0]
            individuosPaquete2 = x[1]
            corte = x[3]
            listaCruzaIndividuos.append([individuosPaquete1[:corte]+individuosPaquete2[corte:]])
            listaCruzaIndividuos.append([individuosPaquete2[:corte]+individuosPaquete1[corte:]])
        self.eliminarTareasRepetidos(listaCruzaIndividuos)
       
        print(listaCruzaIndividuos)
        return listaCruzaIndividuos

    def eliminarTareasRepetidos(self,listaCruzaIndividuos):
        for x in listaCruzaIndividuos:
            individuo1 = x[0]
            listanew2 = [x for x,y in Counter(individuo1).items() if y > 1]
            for p in listanew2:
                individuo1.remove(p)
            self.agregandoLosNuevosValoresIndividuos(individuo1)

    def agregandoLosNuevosValoresIndividuos(self,listaIndividuo):
        for x in range(0,len(self.LISTATAREAS)):
            if not x in listaIndividuo:
                listaIndividuo.append(x)

    def mutaTareas(self,listaCruzaIndividuos):
        print("-------Mutacion-------")
        listaMutaIndividuo = []
        for x in listaCruzaIndividuos:
            listaMutaIndividuo.append(x[0])
        
        for x in listaMutaIndividuo:
            if random.randint(1,100)/100 <= self.PROBABILIDADMUTACION:
                for y in x:
                    if random.randint(1,100)/100 <= self.PROBABILIDADMUTACIONGEN:
                        x.remove(y)
                        rp = random.randint(0,len(x))
                        x.insert(rp,y)
        #     if random.randint(1,100)/100 <= self.PROBABILIDADMUTACION:
        #         self.mutar(x[0])
        # print(listaCruzaIndividuos)
        for x in listaMutaIndividuo:
            self.LISTAJOINPADREHIJO.append(x)
        
        print(self.LISTAJOINPADREHIJO)
        return self.LISTAJOINPADREHIJO
    
    def mutar(self,listaCruzaIndividuos):
        for x in listaCruzaIndividuos:
            if random.randint(1,100)/100 <= self.PROBABILIDADMUTACIONGEN:
                listaCruzaIndividuos.remove(x)
                randoPosicionNumber = random.randint(0,len(listaCruzaIndividuos))
                listaCruzaIndividuos.insert(randoPosicionNumber,x)
        
        pass

    def calcularLasMejoresTareas(self,listaMutacionIndividuo):
        print("-----calcular mejores tareas----")
        listaTareas = []
        for i,x in enumerate(listaMutacionIndividuo):
            listaTareas.append(self.calcularTareaPorIndividuo(x,i))
        #     pass
        listaTareas.sort(key = lambda tareas: tareas[1],reverse=True)
        
        return listaTareas

    def calcularTareaPorIndividuo(self,lista,num):
        listaTareasChidas = []
        totalHrs = 0
        listaHrs = []
        listaTareas = []
        
        for x in lista:
            totalHrs += int(self.LISTATAREAS[x][2])
            listaHrs.append(totalHrs)
            listaTareas.append(self.LISTATAREAS[x])
        for i,x in enumerate(listaHrs):
            hrsTarea = int(listaTareas[i][3])*8
            if x <= hrsTarea:
                listaTareasChidas.append(listaTareas[i])

        return ("Individuo"+str(num),len(listaTareasChidas),lista,"Tareas Validas: ",listaTareasChidas)
    
    def calcularMayorPeorPromedio(self,listaIndividuos):
       
        mejorPeorPromedio = []
        mejorPeorPromedio.append(max([x[1] for x in listaIndividuos]))
        mejorPeorPromedio.append(min([x[1] for x in listaIndividuos])) 
        mejorPeorPromedio.append(numpy.mean([x[1] for x in listaIndividuos]))

        return mejorPeorPromedio
        
    def poda(self,listaMutaIndividuos):
        print("-----poda-----")
        if len(listaMutaIndividuos) > self.POBLACIONMAXIMA:
            listaMutaIndividuos = listaMutaIndividuos[:self.POBLACIONMAXIMA]
            # diferencia = len(listaMutaIndividuos) - self.POBLACIONMAXIMA
            # for x  in range(diferencia):
            #     listaMutaIndividuos.pop(random.randint(0,len(listaMutaIndividuos)-1))
        listaMutaIndividuos.sort(key = lambda tareas: tareas[1],reverse=True)
        
        self.lista_tarea_2.addItem(f"----Generacion {self.COUNT+1}----")
        print(listaMutaIndividuos)
        for x in listaMutaIndividuos:
            self.lista_tarea_2.addItem(str(x))
        # lista = [x[2] for x in listaMutaIndividuos]
        
        self.COUNT+=1
        return listaMutaIndividuos
        

    def graficar(self,listaIndividuosGeneracion):
        fig = plt.figure(figsize=(12,7))
        fig.tight_layout()
        plt.subplot(1, 1, 1)

        yM = [x[0] for x in listaIndividuosGeneracion]
        yP  = [x[1] for x in listaIndividuosGeneracion]
        yPro = [x[2] for x in listaIndividuosGeneracion]

        plt.plot([x for x in range(self.GENERACIONES)],yM,label="Mejor")
        plt.plot([x for x in range(self.GENERACIONES)],yP,label="Peor")
        plt.plot([x for x in range(self.GENERACIONES)],yPro,label="Promedio")
        plt.scatter(len(yM)-1,listaIndividuosGeneracion[-1][0],label=f"Mejor Individuo",color="red")
        plt.title("Comportamiento") 
        plt.legend()
        plt.show()
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ViewTask()
    GUI.show()
    sys.exit(app.exec_())




# Compiladores Analizador-Sementico 6 4 
# Mantenimiento pipeline-aws 12 5 
# Multimedia unity-2d 11 6
# Ingles Report-speech 9 1