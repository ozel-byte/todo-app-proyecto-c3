

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
    ABECEDARIO = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("ui.ui",self)
        self.ventanaDos.hide()
        self.ventanaTres.hide()
        self.btn_siguiente.clicked.connect(self.generarIndividuos)
        self.btn_comenzar.clicked.connect(self.prueba)
    

    def validarDatos(self):
        try:
            self.MATERIA = str(self.materia.text())
            self.NOMBRE_TAREA = str(self.nombre_tarea.text())
            self.TIEMPO_TAREA = int(self.tiempo_tarea.text())
            # self.CANTIDADTAREA = int(self.cantidad_tarea_por_materia.text())
            if self.mayor.isChecked():
                print('si es max')
                self.IMPORTANCIATAREA = "mayor"
            elif self.menor.isChecked():
                print('no es max')
                self.IMPORTANCIATAREA = "menor"
        except ValueError:
            print("Datos mal ingresados")
    def prueba(self):
        self.ventanaTres.show()

    def iniciarIteraccion(self):
        listaTareasNumber = [x for x in range(self.LISTATAREAS)]
        pass

    def generarIndividuos(self):
        print("-----Generar Individuo-----")
        self.ventanaDos.show()
        self.LISTATAREAS.append({
            self.MATERIA,
            self.NOMBRE_TAREA,
            self.TIEMPO_TAREA,
            self.IMPORTANCIATAREA
        })

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