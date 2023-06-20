"""
(c) 2019-2021 Nurul-GC
"""

import os
from configparser import ConfigParser
from random import randint
from sys import argv
from time import sleep

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

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
        GCal().ferramentas.show()


if __name__ == '__main__':
    inifile = ConfigParser()
    if os.path.exists('./gcalculadora.ini'):
        inifile.read('gcalculadora.ini')
        if inifile['MAIN']['tema'] == 'Escuro':
            tema = open('themes/dark.qss').read().strip()
        else:
            tema = open('themes/light.qss').read().strip()
    else:
        with open('gcalculadora.ini', 'w') as INIFILE:
            inifile['MAIN'] = {'tema': 'Claro', 'imagem': 'img/1.png'}
            inifile.write(INIFILE)
        tema = open('themes/light.qss').read().strip()
    fonte = "fonts/AdventPro-Regular.ttf"

    app = Gcal()
    app.gc.exec()
