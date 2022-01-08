import webbrowser
from configparser import ConfigParser
from sys import argv, exit
from time import sleep

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from gcoperacoes import Operacoes


class GCal:
    def __init__(self):
        self.gcOperacoes = Operacoes()

        self.ferramentas = QWidget()
        self.ferramentas.setFixedSize(600, 600)
        self.ferramentas.setWindowTitle('GCalculadora')
        self.ferramentas.setWindowIcon(QIcon('img/favicons/favicon-32x32.png'))

        menu = QMenuBar(self.ferramentas)
        opcoes = menu.addMenu('Opções')
        alterartema = opcoes.addAction(QIcon('img/icons/paint.png'), 'Alterar Tema')
        alterartema.triggered.connect(self.alterarTema)
        instrucoes = opcoes.addAction(QIcon('img/icons/info.png'), 'Instruções')
        instrucoes.triggered.connect(self._instrucoes)
        opcoes.addSeparator()
        sair = opcoes.addAction(QIcon('img/icons/exit.png'), 'Sair')
        sair.triggered.connect(self._sair)
        menu.addSeparator()
        sobre = menu.addAction('Sobre')
        sobre.triggered.connect(self._sobre)

        self.tab = QTabWidget(self.ferramentas)
        self.tab.setGeometry(0, 30, 600, 580)
        self.tab.setDocumentMode(True)

        frame = QFrame()
        layout = QFormLayout()
        layout.setSpacing(10)

        labelInfo = QLabel('<h2>Bem Vindo a calculadora<br><i>Mais Simples e Prática da Atualidade</i></h2>')
        labelInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addRow(labelInfo)

        inifile = ConfigParser()
        inifile.read('gcalculadora.ini')

        labelImagem = QLabel()
        labelImagem.setStyleSheet("border-width:1px;"
                                  "border-style:solid;"
                                  "border-color:white;")
        labelImagem.setPixmap(QPixmap(str(inifile['MAIN']['imagem'])))
        labelImagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addRow(labelImagem)

        progBar = QProgressBar()
        progBar.setMaximum(100)
        progBar.setOrientation(Qt.Orientation.Horizontal)

        def iniciar():
            for valor in range(0, 101, 5):
                progBar.setValue(valor)
                sleep(0.3)
            self.tab.removeTab(self.tab.currentIndex())
            self.janelaOperacional()

        iniciarBtn = QPushButton('Iniciar')
        iniciarBtn.clicked.connect(iniciar)
        layout.addRow(iniciarBtn, progBar)

        link = lambda: webbrowser.open('https://artesgc.home.blog')
        labelTrade = QLabel('<b><a href="#" style="text-decoration:none;">&trade;ArtesGC Inc</a></b>')
        labelTrade.setAlignment(Qt.AlignmentFlag.AlignRight)
        labelTrade.linkActivated.connect(link)
        labelTrade.setToolTip('Abrir website oficial da ArtesGC!')
        layout.addWidget(labelTrade)

        frame.setLayout(layout)
        self.tab.addTab(frame, 'Principal')
        self.tab.setCurrentWidget(frame)

    def alterarTema(self):
        def alterar():
            try:
                config = ConfigParser()
                if escolhaTema.currentText() == 'Escuro':
                    config['MAIN'] = {'tema': escolhaTema.currentText(), 'imagem': 'img/1.png'}
                elif escolhaTema.currentText() == 'Claro':
                    config['MAIN'] = {'tema': escolhaTema.currentText(), 'imagem': 'img/2.png'}
                with open('gcalculadora.ini', 'w') as INIFILE:
                    config.write(INIFILE)
                QMessageBox.information(self.ferramentas, 'Sucessso', 'O tema definido sera aplicado após o reinicio do programa!')
                janelaConfiguracoes.close()
            except Exception as erro:
                QMessageBox.warning(self.ferramentas, 'Aviso', f'Durante o processamento do pedido o seguinte erro foi encontrado:\n- {erro}')

        janelaConfiguracoes = QDialog(self.ferramentas)
        janelaConfiguracoes.setWindowTitle('GCalculadora - Tema')
        janelaConfiguracoes.setFixedSize(QSize(300, 150))
        janelaConfiguracoes.setWindowIcon(QIcon('img/favicons/favicon-32x32.png'))
        layoutConfiguracoes = QVBoxLayout()

        labelInfo = QLabel('<h3>Escolha o tema para o programa:</h3>')
        layoutConfiguracoes.addWidget(labelInfo)

        temas = ['Claro', 'Escuro']
        escolhaTema = QComboBox()
        escolhaTema.addItems(temas)
        layoutConfiguracoes.addWidget(escolhaTema)

        btnSalvar = QPushButton('Salvar')
        btnSalvar.clicked.connect(alterar)
        layoutConfiguracoes.addWidget(btnSalvar)

        janelaConfiguracoes.setLayout(layoutConfiguracoes)
        janelaConfiguracoes.show()

    def _instrucoes(self):
        QMessageBox.information(self.ferramentas, 'Instruções', '''
<h2>Bem Vindo a calculadora<br>
<i>Mais Simples e Prática da Atualidade</i></h2>
<hr>
<p>Ela Te Permite Fazer Cálculos Dos Mais Complexos Aos Mais Simples<br>
De Forma Resumida E Sem Muitos Detalhes, Basta Introduzir:</p>
<ul><li>O [primeiro valor] E O [segundo valor]</li>
<li>Pressionar O Botão Da Operação Desejada</li>
<li>E O [resultado] Surgirá.. Como Que Por Magia!</li></ul>

<p>Ela Também Te Permite Efetuar<br>
Operações Singulares (com Apenas Um Dos Valores)<br>
Basta deixar o outro valor com 0..</p>

<p>Obrigado pelo Apoio!<br>
<b>&trade;ArtesGC Inc</b></p>
''')

    def _sair(self):
        return exit(0)

    def _sobre(self):
        QMessageBox.information(self.ferramentas, 'Sobre o Programa', '''
<h2>Informações Sobre o Programa</h2>
<hr>
<p>Nome: <b>GCalculadora</b><br>
Versão: <b>0.6-082021</b><br>
Designer e Programador: <b>Nurul-GC</b><br>
Empresa: <b>ArtesGC Inc.</b></p>
''')

    def janelaOperacional(self):
        def apagar():
            valor1.clear()
            valor2.clear()
            resultado.clearMask()

        def soma():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setNumDigits(int(self.gcOperacoes.soma()))

        def subt():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setNumDigits(int(self.gcOperacoes.subtracao()))

        def mult():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setNumDigits(int(self.gcOperacoes.multiplicacao()))

        def divi():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setNumDigits(int(self.gcOperacoes.divisao()))

        def exp():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setNumDigits(int(self.gcOperacoes.expoente()))

        def expN():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setNumDigits(int(self.gcOperacoes.expoenteNeg()))

        def razQ():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setNumDigits(int(self.gcOperacoes.raizQuad()))

        def mod():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setNumDigits(int(self.gcOperacoes.modulo()))

        def logB():
            def calcular():
                if not valor1.text() or not valor2.text():
                    QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
                else:
                    self.gcOperacoes.valor1 = int(valor1.text())
                    self.gcOperacoes.valor2 = int(valor2.text())
                    base = int(valorBase.currentText())
                    resultado.setNumDigits(int(self.gcOperacoes.logaritmo(base)))
                    janelaLog.close()

            janelaLog = QDialog(self.ferramentas)
            layoutJ = QVBoxLayout()

            labelInfo = QLabel('<h3>Escolha o Valor da base:</h3>')
            layoutJ.addWidget(labelInfo)

            valores = ['1', '3', '4', '5', '6', '7', '8', '9']
            valorBase = QComboBox()
            valorBase.addItems(valores)
            layoutJ.addWidget(valorBase)

            btnSalvar = QPushButton('Salvar')
            btnSalvar.clicked.connect(calcular)
            layoutOperacoes.addWidget(btnSalvar)

            janelaLog.setLayout(layoutJ)
            janelaLog.show()

        def log2():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setNumDigits(int(self.gcOperacoes.logaritmo2()))

        def log10():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setNumDigits(int(self.gcOperacoes.logaritmo10()))

        def logN():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setNumDigits(int(self.gcOperacoes.logaritmoNat()))

        def seno():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setNumDigits(int(self.gcOperacoes.seno()))

        def cos():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setNumDigits(int(self.gcOperacoes.coseno()))

        def tan():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setNumDigits(int(self.gcOperacoes.tangente()))

        def atan():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setNumDigits(int(self.gcOperacoes.arcTangente()))

        frameOperacoes = QFrame()
        layoutOperacoes = QFormLayout()
        layoutOperacoes.setSpacing(20)
        layoutBtn = QGridLayout()
        layoutValores = QHBoxLayout()

        valor1 = QLineEdit()
        valor1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        valor1.setPlaceholderText('Digite o primeiro valor..')
        layoutValores.addWidget(valor1)

        valor2 = QLineEdit()
        valor2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        valor2.setPlaceholderText('Digite o segundo valor..')
        layoutValores.addWidget(valor2)
        layoutOperacoes.addRow(layoutValores)

        resultado = QLCDNumber()
        layoutOperacoes.addRow(resultado)

        # ***** separador *****
        layoutOperacoes.addRow(QLabel('<hr>'))

        # ***** 1 linha *****
        btnSoma = QPushButton('+')
        btnSoma.clicked.connect(soma)
        btnSoma.setToolTip('Soma')
        layoutBtn.addWidget(btnSoma, 0, 0)

        btnSubt = QPushButton('-')
        btnSubt.clicked.connect(subt)
        btnSubt.setToolTip('Subtração')
        layoutBtn.addWidget(btnSubt, 0, 1)

        btnMult = QPushButton('x')
        btnMult.clicked.connect(mult)
        btnMult.setToolTip('Multiplicação')
        layoutBtn.addWidget(btnMult, 0, 2)

        btnDivi = QPushButton('/')
        btnDivi.clicked.connect(divi)
        btnDivi.setToolTip('Divisão')
        layoutBtn.addWidget(btnDivi, 0, 3)

        # ***** 2 linha *****
        btnExp = QPushButton('^')
        btnExp.clicked.connect(exp)
        btnExp.setToolTip('Exponenciação')
        layoutBtn.addWidget(btnExp, 1, 0)

        btnExpN = QPushButton('^-1')
        btnExpN.clicked.connect(expN)
        btnExpN.setToolTip('Exponenciação Negativa')
        layoutBtn.addWidget(btnExpN, 1, 1)

        btnRazQ = QPushButton('√')
        btnRazQ.clicked.connect(razQ)
        btnRazQ.setToolTip('Raiz Quadrada')
        layoutBtn.addWidget(btnRazQ, 1, 2)

        btnMod = QPushButton('%')
        btnMod.clicked.connect(mod)
        btnMod.setToolTip('Môdulo')
        layoutBtn.addWidget(btnMod, 1, 3)

        # ***** 3 linha *****
        btnLog = QPushButton('logB(v)')
        btnLog.clicked.connect(logB)
        btnLog.setToolTip('Logaritmo de V na base B')
        layoutBtn.addWidget(btnLog, 2, 0)

        btnLog2 = QPushButton('log2(v)')
        btnLog2.clicked.connect(log2)
        btnLog2.setToolTip('Logaritmo de V na base 2')
        layoutBtn.addWidget(btnLog2, 2, 1)

        btnLog10 = QPushButton('log10(v)')
        btnLog10.clicked.connect(log10)
        btnLog10.setToolTip('Logaritmo de V na base 10')
        layoutBtn.addWidget(btnLog10, 2, 2)

        btnLogN = QPushButton('logN(v)')
        btnLogN.clicked.connect(logN)
        btnLogN.setToolTip('Logaritmo Natural de V')
        layoutBtn.addWidget(btnLogN, 2, 3)

        # ***** 4 linha *****
        btnSeno = QPushButton('Seno(v)')
        btnSeno.clicked.connect(seno)
        btnSeno.setToolTip('Seno de V em Radianos')
        layoutBtn.addWidget(btnSeno, 3, 0, 1, 2)

        btnCos = QPushButton('Cos(v)')
        btnCos.clicked.connect(cos)
        btnCos.setToolTip('Coseno de V em Radianos')
        layoutBtn.addWidget(btnCos, 3, 2, 1, 2)

        # ***** 5 linha *****
        btnTan = QPushButton('Tan(v)')
        btnTan.clicked.connect(tan)
        btnTan.setToolTip('Tangente de V em Radianos')
        layoutBtn.addWidget(btnTan, 5, 0, 1, 2)

        btnATan = QPushButton('ArcTan(v)')
        btnATan.clicked.connect(atan)
        btnATan.setToolTip('Arco Tangente de V em Radianos')
        layoutBtn.addWidget(btnATan, 5, 2, 1, 2)
        layoutOperacoes.addRow(layoutBtn)

        btnClr = QPushButton('C')
        btnClr.clicked.connect(apagar)
        btnClr.setToolTip('Apagar Valores e Resultado')
        layoutOperacoes.addRow(btnClr)

        # ***** separador *****
        layoutOperacoes.addRow(QLabel('<hr>'))

        frameOperacoes.setLayout(layoutOperacoes)
        self.tab.addTab(frameOperacoes, 'Operações')
        self.tab.setCurrentWidget(frameOperacoes)
