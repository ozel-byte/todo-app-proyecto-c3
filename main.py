

from enum import Flag
import random
from re import T
import sys
from typing import Counter
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import cv2
from matplotlib import image
import numpy

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
    ABECEDARIO = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    CALEDARIO = 'dd/mm/yyyy'
    DIASTRABAJDOS = 0

    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("ui.ui",self)
        self.ventanaDos.hide()
        self.btn_siguiente.clicked.connect(self.agregarDias)
        self.btn_agregar.clicked.connect(self.agregarTareas)
        self.btn_siguiente.setEnabled(False)
        self.btn_siguiente.clicked.connect(self.iniciarIteraccion)
        self.PROBABILIDADDESENDENCIA = random.randint(1,100)/100
        self.PROBABILIDADMUTACION = random.randint(1,100)/100
        self.PROBABILIDADMUTACIONGEN = random.randint(1,100)/100
    
    def agregarDias(self):
        print("tareas agregadasa")
        self.ventanaDos.show()

    def validarDatos(self):
        try:
            self.MATERIA = str(self.materia.text())
            self.NOMBRE_TAREA = str(self.nombre_tarea.text())
            self.TIEMPO_TAREA = int(self.tiempo_tarea.text())
            self.HORASDIA = int(self.horas_porDia.text())
            self.TAREASDIA = int(self.tareas_porDia.text())
            self.CALEDARIO = str(self.calendario.text())
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
        #     self.IMPORTANCIATAREA
        # ))
        
        # self.lista_total.addItem("Materia: "+self.MATERIA+"\n Nombre-Tarea: "+str(self.NOMBRE_TAREA)+"\n Tiempo: "+str(self.TIEMPO_TAREA)+"\n Importancia-Tarea: "+str(self.IMPORTANCIATAREA))
        # self.lista_total.addItem("----------------------------------------------------")
        # self.materia.setText("")
        # self.nombre_tarea.setText("")
        # self.tiempo_tarea.setText("")
        print("lista")
        print(self.LISTATAREAS)
        self.btn_siguiente.setEnabled(True)

    def iniciarIteraccion(self):
        listaIndividuos = self.generarIndividuos()
        listaSeleccionIndividuos = self.seleccionIndividuos(listaIndividuos)
        listaCruzaIndividuos     = self.cruzaIndividuos(listaSeleccionIndividuos)
        listaMutacionIndividuos  = self.mutaTareas(listaCruzaIndividuos)
        self.calcularLasMejoresTareas(listaMutacionIndividuos)
        #self.poda()
        
    
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
            #individuo2 = x[1]
            listanew2 = [x for x,y in Counter(individuo1).items() if y > 1]
            #listanew3 = [x for x,y in Counter(individuo2).items() if y > 1]

            for p in listanew2:
                individuo1.remove(p)
            # for p in listanew3:
            #     individuo2.remove(p)
            self.agregandoLosNuevosValoresIndividuos(individuo1)

    def agregandoLosNuevosValoresIndividuos(self,listaIndividuo):
        for x in range(1,len(self.LISTATAREAS)):
            if not x in listaIndividuo:
                listaIndividuo.append(x)

    def mutaTareas(self,listaCruzaIndividuos):
        print("-------Mutacion-------")
        for x in listaCruzaIndividuos:
            if random.randint(1,100)/100 <= self.PROBABILIDADMUTACION:
                self.mutar(x[0])
        for x in listaCruzaIndividuos:
            self.LISTAJOINPADREHIJO.append(x)
        
        print(self.LISTAJOINPADREHIJO)
        return self.LISTAJOINPADREHIJO
        #returnar padre hijo
    
    def mutar(self,listaCruzaIndividuos):
        for x in listaCruzaIndividuos:
            if random.randint(1,100)/100 <= self.PROBABILIDADMUTACIONGEN:
                listaCruzaIndividuos.remove(x)
                randoPosicionNumber = random.randint(0,len(listaCruzaIndividuos))
                listaCruzaIndividuos.insert(randoPosicionNumber,x)
        
        pass
    def calcularLasMejoresTareas(self,listaMutacionIndividuo):
        # for x in listaMutacionIndividuo:

        #     pass
        pass
    def poda(self,listaMutaIndividuos):

        pass




if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ViewTask()
    GUI.show()
    sys.exit(app.exec_())