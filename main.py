

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

    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("viuw.ui",self)

    
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




if __name__ == "__main__":
    pass