"""
(c) 2019-2021 Nurul-GC
"""

from configparser import ConfigParser
import os
import webbrowser
from random import randint
from sys import argv, exit
from time import sleep

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from gcal.gui import GCal


class Gcal:
    def __init__(self):
        self.gc = QApplication(argv)

        QFontDatabase.addApplicationFont(fonte)

        img = QPixmap("img/favicons/favicon-512x512.png")
        self.align = int(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignAbsolute)
        self.janela = QSplashScreen(img)
        self.janela.setStyleSheet(tema)
        self.janela.show()
        self.iniciar()

    def iniciar(self):
        load = 0
        while load < 100:
            self.janela.showMessage(f"Carregando os Modulos do Programa: {load}%", self.align, Qt.GlobalColor.black)
            load += randint(1, 10)
            sleep(0.5)
        self.janela.close()
        GCal().ferramentas.setStyleSheet(tema)
        GCal().ferramentas.show()


if __name__ == '__main__':
    inifile = ConfigParser()
    if os.path.exists('gcalculadora.ini'):
        inifile.read('gcalculadora.ini')
        if inifile['MAIN']['tema'] == 'Escuro':
            tema = open('themes/gcalculadora.qss').read().strip()
        else:
            tema = open('themes/gcalculadora-light.qss').read().strip()
    else:
        inifile['MAIN'] = {'tema': 'Claro', 'imagem': 'img/2.png'}
        with open('gcalculadora.ini', 'w') as INIFILE:
            inifile.write(INIFILE)
        tema = open('themes/gcalculadora-light.qss').read().strip()
    fonte = "fonts/AdventPro-Bold.ttf"

    app = Gcal()
    app.gc.exec()
