"""
(c) 2019-2021 Nurul-GC
"""
import os
from sys import argv, exit
from PyQt5.Qt import *
from gcoperacoes import Operacoes


class GCal:
    def __init__(self):
        self.gc = QApplication(argv)
        self.fonte = QFontDatabase()
        self.fonte.addApplicationFont(fonte)

        self.ferramentas = QWidget()
        self.ferramentas.setFont(QFont('AdventPro'))
        self.ferramentas.setFixedSize(500, 250)

        self.tab = QTabWidget(self.ferramentas)
        self.tab.setGeometry(0, 30, 500, 230)

        self.janelaPrincipal()

    def janelaPrincipal(self):
        frame = QFrame()
        layout = QFormLayout()

        labelInfo = QLabel('Bem Vindo')
        layout.addRow(labelInfo)

        frame.setLayout(layout)
        self.tab.addTab(frame, 'Principal')
        self.tab.setCurrentWidget(frame)


if __name__ == '__main__':
    tema = open('themes/gcalculadora.qss').read().strip()
    fonte = 'fonts/AdventPro-SemiBold.ttf'

    app = GCal()
    app.ferramentas.show()
    app.gc.exec_()
