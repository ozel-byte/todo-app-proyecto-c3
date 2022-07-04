

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


    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("ui.ui",self)

    def validarDatos(self):
        try:
            self.MATERIA = str(self.materia.text())
            self.NOMBRE_TAREA = str(self.nombre_tarea.text())
            self.TIEMPO_TAREA = int(self.tiempo_tarea.text())
            if self.mayor.isChecked():
                print('si es max')
            elif self.menor.isChecked():
                print('no es max')
        except ValueError:
            print("Datos mal ingresados")

    def generarIndividuos():
        pass

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