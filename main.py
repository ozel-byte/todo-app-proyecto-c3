

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
    NOMBRE_TAREA = ' '
    TIEMPO_TAREA = 0
    LISTATAREAS = []
    IMPORTANCIATAREA = ""
    CANTIDADTAREA = 0
    HORASDIA = 0
    TAREASDIA = 0
    ABECEDARIO = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("ui.ui",self)
        self.ventanaDos.hide()
        self.ventanaTres.hide()
        self.btn_siguiente.clicked.connect(self.generarIndividuos)
        self.btn_agregar.clicked.connect(self.agregarTareas)
        self.btn_siguiente.setEnabled(False)
        self.btn_comenzar.clicked.connect(self.agregarTareas)
    

    def validarDatos(self):
        try:
            self.MATERIA = str(self.materia.text())
            self.NOMBRE_TAREA = str(self.nombre_tarea.text())
            self.TIEMPO_TAREA = int(self.tiempo_tarea.text())
            self.HORASDIA = int(self.horas_porDia.text())
            self.TAREASDIA = int(self.tareas_porDia.text())
            if self.btn_mayor.isChecked():
                print('si es max')
                self.IMPORTANCIATAREA = "mayor"
            elif self.btn_menor.isChecked():
                print('no es max')
                self.IMPORTANCIATAREA = "menor"
        except ValueError:
            print("Datos mal ingresados")

    def agregarTareas(self):
        self.validarDatos()
        self.LISTATAREAS.append((
            self.MATERIA,
            self.NOMBRE_TAREA,
            self.TIEMPO_TAREA,
            self.IMPORTANCIATAREA
        ))
        
        self.lista_total.addItem("Materia: "+self.MATERIA+"\n Nombre-Tarea: "+str(self.NOMBRE_TAREA)+"\n Tiempo: "+str(self.TIEMPO_TAREA)+"\n Importancia-Tarea: "+str(self.IMPORTANCIATAREA))
        self.lista_total.addItem("----------------------------------------------------")
        self.materia.setText("")
        self.nombre_tarea.setText("")
        self.tiempo_tarea.setText("")
        self.btn_siguiente.setEnabled(True)
        # self.ventanaTres.show()

    def iniciarIteraccion(self):
        listaTareasNumber = [x for x in range(self.LISTATAREAS)]
        pass
    
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
        self.ventanaDos.show()
        return poblacion
        

    def seleccionIndividuos():
        pass

    def cruzaPaquetes():
        pass

    def mutaPaquetes():
        pass

    def limpieza():
        pass

    def poda():
        pass




if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ViewTask()
    GUI.show()
    sys.exit(app.exec_())