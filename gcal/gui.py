import webbrowser
from configparser import ConfigParser
from sys import argv, exit
from time import sleep

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from gcoperacoes import Operacoes

inifile = ConfigParser()
inifile.read('gcalculadora.ini')
if inifile['MAIN']['tema'] == 'Escuro':
    tema = open('themes/dark.qss').read().strip()
else:
    tema = open('themes/light.qss').read().strip()


class GCal:
    def __init__(self):
        self.gcOperacoes = Operacoes()

        self.ferramentas = QWidget()
        self.ferramentas.setFixedSize(600, 600)
        self.ferramentas.setWindowTitle('GCalculadora')
        self.ferramentas.setStyleSheet(tema)
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

        self.janelaInicial()

    def alterarTema(self):
        def alterar():
            try:
                config = ConfigParser()
                if escolhaTema.currentText() == 'Escuro':
                    config['MAIN'] = {'tema': escolhaTema.currentText(), 'imagem': 'img/2.png'}
                elif escolhaTema.currentText() == 'Claro':
                    config['MAIN'] = {'tema': escolhaTema.currentText(), 'imagem': 'img/1.png'}
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

    def janelaInicial(self):
        frame = QFrame()
        layout = QFormLayout()
        layout.setSpacing(10)

        labelInfo = QLabel('<h2>Bem Vindo a calculadora<br><i>Mais Simples e Prática da Atualidade</i></h2>')
        labelInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addRow(labelInfo)

        labelImagem = QLabel()
        labelImagem.setPixmap(QPixmap(str(inifile['MAIN']['imagem'])).scaled(500, 440))
        labelImagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addRow(labelImagem)

        def iniciar():
            self.tab.removeTab(self.tab.currentIndex())
            self.janelaOperacional()

        iniciarBtn = QPushButton('Iniciar')
        iniciarBtn.clicked.connect(iniciar)
        layout.addRow(iniciarBtn)
        layout.addRow(QLabel("<hr>"))

        link = lambda: webbrowser.open('https://artesgc.home.blog')
        labelTrade = QLabel('<b><a href="#" style="text-decoration:none;">&trade;ArtesGC Inc</a></b>')
        labelTrade.setAlignment(Qt.AlignmentFlag.AlignRight)
        labelTrade.linkActivated.connect(link)
        labelTrade.setToolTip('Abrir website oficial da ArtesGC!')
        layout.addWidget(labelTrade)

        frame.setLayout(layout)
        self.tab.addTab(frame, 'Principal')
        self.tab.setCurrentWidget(frame)

    def janelaOperacional(self):
        def apagar():
            valor1.clear()
            valor2.clear()
            resultado.clear()

        def soma():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setText(str(self.gcOperacoes.soma()))

        def subt():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setText(str(self.gcOperacoes.subtracao()))

        def mult():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setText(str(self.gcOperacoes.multiplicacao()))

        def divi():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setText(str(self.gcOperacoes.divisao()))

        def exp():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setText(str(self.gcOperacoes.expoente()))

        def expN():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setText(str(self.gcOperacoes.expoenteNeg()))

        def razQ():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setText(str(self.gcOperacoes.raizQuad()))

        def mod():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setText(str(self.gcOperacoes.modulo()))

        def logB():
            def calcular():
                if not valor1.text() or not valor2.text():
                    QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
                else:
                    self.gcOperacoes.valor1 = int(valor1.text())
                    self.gcOperacoes.valor2 = int(valor2.text())
                    base = int(valorBase.currentText())
                    resultado.setText(str(self.gcOperacoes.logaritmo(base)))
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
            layoutJ.addWidget(btnSalvar)

            janelaLog.setLayout(layoutJ)
            janelaLog.show()

        def log2():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setText(str(self.gcOperacoes.logaritmo2()))

        def log10():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setText(str(self.gcOperacoes.logaritmo10()))

        def logN():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setText(str(self.gcOperacoes.logaritmoNat()))

        def seno():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setText(str(self.gcOperacoes.seno()))

        def cos():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setText(str(self.gcOperacoes.coseno()))

        def tan():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setText(str(self.gcOperacoes.tangente()))

        def atan():
            if not valor1.text() or not valor2.text():
                QMessageBox.warning(self.ferramentas, 'Aviso', '<b>Não foi possivel processar a operação com os valores não preenchidos!</b>')
            else:
                self.gcOperacoes.valor1 = int(valor1.text())
                self.gcOperacoes.valor2 = int(valor2.text())
                resultado.setText(str(self.gcOperacoes.arcTangente()))

        def selctvalor1():
            selectvalor1.setChecked(True)
            valor1.setFocus(Qt.FocusReason.MouseFocusReason)

        def selctvalor2():
            selectvalor2.setChecked(True)
            valor2.setFocus(Qt.FocusReason.MouseFocusReason)

        frameOperacoes = QFrame()
        layoutOperacoes = QFormLayout()
        layoutOperacoes.setSpacing(10)

        layoutBtnOper = QGridLayout()
        layoutValores = QHBoxLayout()

        layoutvalor1 = QFormLayout()
        valor1 = QLineEdit()
        valor1.setValidator(QIntValidator(-2147483648, 2147483647))
        valor1.setFont(QFont("Courier", 10))
        valor1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        valor1.setPlaceholderText('Digite o 1º valor..')
        valor1.textEdited.connect(selctvalor1)

        selectvalor1 = QRadioButton()
        selectvalor1.clicked.connect(selctvalor1)
        layoutvalor1.addRow(selectvalor1, valor1)
        layoutValores.addLayout(layoutvalor1)

        layoutvalor2 = QFormLayout()
        valor2 = QLineEdit()
        valor2.setValidator(QIntValidator(-2147483648, 2147483647))
        valor2.setFont(QFont("Courier", 10))
        valor2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        valor2.setPlaceholderText('Digite o 2º valor..')
        valor2.textEdited.connect(selctvalor2)

        selectvalor2 = QRadioButton()
        selectvalor2.clicked.connect(selctvalor2)
        layoutvalor2.addRow(selectvalor2, valor2)
        layoutValores.addLayout(layoutvalor2)
        layoutOperacoes.addRow(layoutValores)

        resultado = QLineEdit()
        resultado.setReadOnly(True)
        resultado.setFont(QFont("Courier", 20))
        resultado.setPlaceholderText('Resultado da operaçao..')
        resultado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutOperacoes.addRow(resultado)

        # ***** separador *****
        layoutOperacoes.addRow(QLabel('<hr>'))

        # ***** 1 linha *****
        btnSoma = QPushButton('+')
        btnSoma.clicked.connect(soma)
        btnSoma.setToolTip('Soma')
        layoutBtnOper.addWidget(btnSoma, 0, 0)

        btnSubt = QPushButton('-')
        btnSubt.clicked.connect(subt)
        btnSubt.setToolTip('Subtração')
        layoutBtnOper.addWidget(btnSubt, 0, 1)

        btnMult = QPushButton('x')
        btnMult.clicked.connect(mult)
        btnMult.setToolTip('Multiplicação')
        layoutBtnOper.addWidget(btnMult, 0, 2)

        btnDivi = QPushButton('/')
        btnDivi.clicked.connect(divi)
        btnDivi.setToolTip('Divisão')
        layoutBtnOper.addWidget(btnDivi, 0, 3)

        btnExp = QPushButton('^')
        btnExp.clicked.connect(exp)
        btnExp.setToolTip('Exponenciação')
        layoutBtnOper.addWidget(btnExp, 0, 4)

        btnExpN = QPushButton('^-1')
        btnExpN.clicked.connect(expN)
        btnExpN.setToolTip('Exponenciação Negativa')
        layoutBtnOper.addWidget(btnExpN, 0, 5)

        btnRazQ = QPushButton('√')
        btnRazQ.clicked.connect(razQ)
        btnRazQ.setToolTip('Raiz Quadrada')
        layoutBtnOper.addWidget(btnRazQ, 0, 6)

        btnMod = QPushButton('%')
        btnMod.clicked.connect(mod)
        btnMod.setToolTip('Môdulo')
        layoutBtnOper.addWidget(btnMod, 0, 7)

        # ***** 2 linha *****
        btnLog = QPushButton('logB(v)')
        btnLog.clicked.connect(logB)
        btnLog.setToolTip('Logaritmo do Valor na base B')
        layoutBtnOper.addWidget(btnLog, 1, 0)

        btnLog2 = QPushButton('log2(v)')
        btnLog2.clicked.connect(log2)
        btnLog2.setToolTip('Logaritmo do Valor na base 2')
        layoutBtnOper.addWidget(btnLog2, 1, 1)

        btnLog10 = QPushButton('log10(v)')
        btnLog10.clicked.connect(log10)
        btnLog10.setToolTip('Logaritmo do Valor na base 10')
        layoutBtnOper.addWidget(btnLog10, 1, 2)

        btnLogN = QPushButton('logN(v)')
        btnLogN.clicked.connect(logN)
        btnLogN.setToolTip('Logaritmo Natural do Valor')
        layoutBtnOper.addWidget(btnLogN, 1, 3)

        btnSeno = QPushButton('Seno(v)')
        btnSeno.clicked.connect(seno)
        btnSeno.setToolTip('Seno do Valor em Radianos')
        layoutBtnOper.addWidget(btnSeno, 1, 4)

        btnCos = QPushButton('Cos(v)')
        btnCos.clicked.connect(cos)
        btnCos.setToolTip('Coseno do Valor em Radianos')
        layoutBtnOper.addWidget(btnCos, 1, 5)

        btnTan = QPushButton('Tan(v)')
        btnTan.clicked.connect(tan)
        btnTan.setToolTip('Tangente do Valor em Radianos')
        layoutBtnOper.addWidget(btnTan, 1, 6)

        btnATan = QPushButton('ArcTan(v)')
        btnATan.clicked.connect(atan)
        btnATan.setToolTip('Arco Tangente do Valor em Radianos')
        layoutBtnOper.addWidget(btnATan, 1, 7)

        # ***** separador *****
        layoutBtnOper.addWidget(QLabel('<hr>'), 2, 0, 1, 8)

        # ***** 3 linha *****
        btn9 = QPushButton('9')
        layoutBtnOper.addWidget(btn9, 3, 0, 1, 2)

        btn8 = QPushButton('8')
        layoutBtnOper.addWidget(btn8, 3, 2, 1, 2)

        btn7 = QPushButton('7')
        layoutBtnOper.addWidget(btn7, 3, 4, 1, 2)

        btn6 = QPushButton('6')
        layoutBtnOper.addWidget(btn6, 3, 6, 1, 2)

        # ***** 4 linha *****
        btn5 = QPushButton('5')
        layoutBtnOper.addWidget(btn5, 4, 0, 1, 2)

        btn4 = QPushButton('4')
        layoutBtnOper.addWidget(btn4, 4, 2, 1, 2)

        btn3 = QPushButton('3')
        layoutBtnOper.addWidget(btn3, 4, 4, 1, 2)

        btn2 = QPushButton('2')
        layoutBtnOper.addWidget(btn2, 4, 6, 1, 2)

        # ***** 5 linha *****
        btn1 = QPushButton('1')
        layoutBtnOper.addWidget(btn1, 5, 0, 1, 4)

        btn0 = QPushButton('0')
        layoutBtnOper.addWidget(btn0, 5, 4, 1, 4)
        layoutOperacoes.addRow(layoutBtnOper)

        btnClr = QPushButton('AC')
        btnClr.clicked.connect(apagar)
        btnClr.setToolTip('Apagar Valores e Resultado')
        layoutOperacoes.addRow(btnClr)

        # ***** separador *****
        layoutOperacoes.addRow(QLabel('<hr>'))

        link = lambda: webbrowser.open('https://artesgc.home.blog')
        labelTrade = QLabel('<b><a href="#" style="text-decoration:none;">&trade;ArtesGC Inc</a></b>')
        labelTrade.setAlignment(Qt.AlignmentFlag.AlignRight)
        labelTrade.linkActivated.connect(link)
        labelTrade.setToolTip('Abrir website oficial da ArtesGC!')
        layoutOperacoes.addWidget(labelTrade)

        frameOperacoes.setLayout(layoutOperacoes)
        self.tab.addTab(frameOperacoes, 'Operações')
        self.tab.setCurrentWidget(frameOperacoes)
