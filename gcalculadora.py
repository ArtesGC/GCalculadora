"""
(c) 2019-2021 Nurul-GC
"""
import os
from sys import argv, exit
from time import sleep

from PyQt5.Qt import *
from gcoperacoes import Operacoes


class GCal:
    def __init__(self):
        self.gc = QApplication(argv)
        self.gcOperacoes = Operacoes()

        self.fonte = QFontDatabase()
        for fontfile in fonte:
            self.fonte.addApplicationFont(fontfile)

        self.ferramentas = QWidget()
        self.ferramentas.setStyleSheet(tema)
        self.ferramentas.setFixedSize(600, 670)

        self.tab = QTabWidget(self.ferramentas)
        self.tab.setGeometry(0, 30, 600, 640)

        self.janelaPrincipal()

    def janelaPrincipal(self):
        def iniciar():
            for valor in range(0, 101):
                progBar.setValue(valor)
                sleep(0.3)
            self.janelaOperacional()

        frame = QFrame()
        layout = QFormLayout()
        layout.setSpacing(10)

        labelInfo = QLabel('<h2>Bem Vindo a calculadora<br><i>Mais Simples e Completa da Atualidade</i></h2>')
        labelInfo.setAlignment(Qt.AlignCenter)
        layout.addRow(labelInfo)

        labelImagem = QLabel()
        labelImagem.setPixmap(QPixmap('img/2.png'))
        labelImagem.setAlignment(Qt.AlignCenter)
        layout.addRow(labelImagem)

        progBar = QProgressBar()
        progBar.setMaximum(100)
        progBar.setOrientation(Qt.Horizontal)
        iniciarBtn = QPushButton('Iniciar')
        iniciarBtn.clicked.connect(iniciar)
        layout.addRow(iniciarBtn, progBar)

        frame.setLayout(layout)
        self.tab.addTab(frame, 'Principal')
        self.tab.setCurrentWidget(frame)

    def janelaOperacional(self):
        QMessageBox.information(self.ferramentas, 'Sucesso', 'Bem Vindo..')


if __name__ == '__main__':
    tema = open('themes/gcalculadora.qss').read().strip()
    fonte = [f'fonts/{fontFile}' for fontFile in os.listdir('fonts') if fontFile.endswith('.ttf')]

    app = GCal()
    app.ferramentas.show()
    app.gc.exec_()
