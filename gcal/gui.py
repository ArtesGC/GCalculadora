import webbrowser
from configparser import ConfigParser
from sys import exit

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from gcoperacoes import Operacoes, isempty

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
        self.ferramentas.setWindowTitle('GCalculadora')
        self.ferramentas.setStyleSheet(tema)
        self.ferramentas.setWindowIcon(QIcon('img/favicons/favicon-32x32.png'))

        menu = QMenuBar(self.ferramentas)
        opcoes = menu.addMenu('Opções')
        alterartema = opcoes.addAction(QIcon('img/icons/paint.png'), 'Alterar Tema')
        alterartema.triggered.connect(self.alterar_tema)
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

        self.janela_inicial()

    def alterar_tema(self):
        def alterar():
            try:
                config = ConfigParser()
                if escolha_tema.currentText() == 'Escuro':
                    config['MAIN'] = {'tema': escolha_tema.currentText(), 'imagem': 'img/2.png'}
                elif escolha_tema.currentText() == 'Claro':
                    config['MAIN'] = {'tema': escolha_tema.currentText(), 'imagem': 'img/1.png'}
                with open('gcalculadora.ini', 'w') as INIFILE:
                    config.write(INIFILE)
                QMessageBox.information(
                    self.ferramentas, 'Sucessso',
                    'O tema definido sera aplicado após o reinicio do programa!'
                )
                janela_configuracoes.close()
            except Exception as erro:
                QMessageBox.warning(
                    self.ferramentas, 'Aviso',
                    f'Durante o processamento do pedido o seguinte erro foi encontrado:\n- {erro}'
                )

        janela_configuracoes = QDialog(self.ferramentas)
        janela_configuracoes.setWindowTitle('GCalculadora - Tema')
        janela_configuracoes.setFixedSize(QSize(300, 150))
        janela_configuracoes.setWindowIcon(QIcon('img/favicons/favicon-32x32.png'))
        layout_configuracoes = QVBoxLayout()

        label_info = QLabel('<h3>Escolha o tema para o programa:</h3>')
        layout_configuracoes.addWidget(label_info)

        temas = ['Claro', 'Escuro']
        escolha_tema = QComboBox()
        escolha_tema.addItems(temas)
        layout_configuracoes.addWidget(escolha_tema)

        btn_salvar = QPushButton('Salvar')
        btn_salvar.clicked.connect(alterar)
        layout_configuracoes.addWidget(btn_salvar)

        janela_configuracoes.setLayout(layout_configuracoes)
        janela_configuracoes.show()

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

    @staticmethod
    def _sair():
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

    def janela_inicial(self):
        frame = QFrame()
        layout = QFormLayout()
        layout.setSpacing(10)

        label_info = QLabel('<h2>Bem Vindo a calculadora<br><i>Mais Simples e Prática da Atualidade</i></h2>')
        label_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addRow(label_info)

        label_imagem = QLabel()
        label_imagem.setPixmap(QPixmap(str(inifile['MAIN']['imagem'])).scaled(500, 440))
        label_imagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addRow(label_imagem)

        def iniciar():
            self.tab.removeTab(self.tab.currentIndex())
            self.janela_operacional()

        iniciar_btn = QPushButton('Iniciar')
        iniciar_btn.clicked.connect(iniciar)
        layout.addRow(iniciar_btn)
        layout.addRow(QLabel("<hr>"))

        def link(): webbrowser.open('https://artesgc.home.blog')
        label_trade = QLabel('<b><a href="#" style="text-decoration:none;">&trade;ArtesGC Inc</a></b>')
        label_trade.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_trade.linkActivated.connect(link)
        label_trade.setToolTip('Abrir website oficial da ArtesGC!')
        layout.addRow(label_trade)

        frame.setLayout(layout)
        self.tab.addTab(frame, 'Principal')
        self.tab.setCurrentWidget(frame)

    def janela_operacional(self):
        def apagar():
            valor1.clear()
            valor2.clear()
            resultado.clear()

        def soma():
            setvalores()
            resultado.setText(str(self.gcOperacoes.soma()))

        def subt():
            setvalores()
            resultado.setText(str(self.gcOperacoes.subtracao()))

        def mult():
            setvalores()
            resultado.setText(str(self.gcOperacoes.multiplicacao()))

        def divi():
            setvalores()
            resultado.setText(str(self.gcOperacoes.divisao()))

        def exp():
            setvalores()
            resultado.setText(str(self.gcOperacoes.expoente()))

        def exp_n():
            setvalores()
            resultado.setText(str(self.gcOperacoes.expoente_neg()))

        def raz_q():
            setvalores()
            resultado.setText(str(self.gcOperacoes.raiz_quad()))

        def mod():
            setvalores()
            resultado.setText(str(self.gcOperacoes.modulo()))

        def log_b():
            def calcular():
                setvalores()
                base = int(valor_base.currentText())
                resultado.setText(str(self.gcOperacoes.logaritmo(base)))
                janela_log.close()

            janela_log = QDialog(self.ferramentas)
            layout_j = QVBoxLayout()

            label_info = QLabel('<h3>Escolha o Valor da base:</h3>')
            layout_j.addWidget(label_info)

            valores = ['1', '3', '4', '5', '6', '7', '8', '9']
            valor_base = QComboBox()
            valor_base.addItems(valores)
            layout_j.addWidget(valor_base)

            btn_salvar = QPushButton('Salvar')
            btn_salvar.clicked.connect(calcular)
            layout_j.addWidget(btn_salvar)

            janela_log.setLayout(layout_j)
            janela_log.show()

        def log2():
            setvalores()
            resultado.setText(str(self.gcOperacoes.logaritmo2()))

        def log10():
            setvalores()
            resultado.setText(str(self.gcOperacoes.logaritmo10()))

        def log_n():
            setvalores()
            resultado.setText(str(self.gcOperacoes.logaritmo_nat()))

        def seno():
            setvalores()
            resultado.setText(str(self.gcOperacoes.seno()))

        def cos():
            setvalores()
            resultado.setText(str(self.gcOperacoes.coseno()))

        def tan():
            setvalores()
            resultado.setText(str(self.gcOperacoes.tangente()))

        def atan():
            setvalores()
            resultado.setText(str(self.gcOperacoes.arc_tangente()))

        def setvalores():
            if isempty(valor1.text()):
                Operacoes(valor2=int(valor2.text()))
            elif isempty(valor2.text()):
                Operacoes(valor1=int(valor1.text()))
            else:
                Operacoes(valor1=int(valor1.text()), valor2=int(valor2.text()))

        frame_operacoes = QFrame()
        layout_operacoes = QFormLayout()
        layout_operacoes.setSpacing(10)

        layout_btn_oper = QGridLayout()
        layout_valores = QHBoxLayout()

        layoutvalor1 = QFormLayout()
        valor1 = QLineEdit()
        valor1.setValidator(QIntValidator(-2147483648, 2147483647))
        valor1.setFont(QFont("Courier", 10))
        valor1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        valor1.setPlaceholderText('Digite o 1º valor..')
        layoutvalor1.addRow(valor1)
        layout_valores.addLayout(layoutvalor1)

        layoutvalor2 = QFormLayout()
        valor2 = QLineEdit()
        valor2.setValidator(QIntValidator(-2147483648, 2147483647))
        valor2.setFont(QFont("Courier", 10))
        valor2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        valor2.setPlaceholderText('Digite o 2º valor..')
        layoutvalor2.addRow(valor2)
        layout_valores.addLayout(layoutvalor2)
        layout_operacoes.addRow(layout_valores)

        resultado = QLineEdit()
        resultado.setReadOnly(True)
        resultado.setFont(QFont("Courier", 20))
        resultado.setPlaceholderText('Resultado da operaçao..')
        resultado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_operacoes.addRow(resultado)

        # ***** separador *****
        layout_operacoes.addRow(QLabel('<hr>'))

        # ***** 1 linha *****
        btn_soma = QPushButton('+')
        btn_soma.clicked.connect(soma)
        btn_soma.setToolTip('Soma')
        layout_btn_oper.addWidget(btn_soma, 0, 0)

        btn_subt = QPushButton('-')
        btn_subt.clicked.connect(subt)
        btn_subt.setToolTip('Subtração')
        layout_btn_oper.addWidget(btn_subt, 0, 1)

        btn_mult = QPushButton('x')
        btn_mult.clicked.connect(mult)
        btn_mult.setToolTip('Multiplicação')
        layout_btn_oper.addWidget(btn_mult, 0, 2)

        btn_divi = QPushButton('/')
        btn_divi.clicked.connect(divi)
        btn_divi.setToolTip('Divisão')
        layout_btn_oper.addWidget(btn_divi, 0, 3)

        btn_exp = QPushButton('^')
        btn_exp.clicked.connect(exp)
        btn_exp.setToolTip('Exponenciação: 1-valor elevado ao 2-valor')
        layout_btn_oper.addWidget(btn_exp, 1, 0)

        btn_exp_n = QPushButton('^-1')
        btn_exp_n.clicked.connect(exp_n)
        btn_exp_n.setToolTip('Exponenciação Negativa da soma dos valores')
        layout_btn_oper.addWidget(btn_exp_n, 1, 1)

        btn_raz_q = QPushButton('√')
        btn_raz_q.clicked.connect(raz_q)
        btn_raz_q.setToolTip('Raiz Quadrada')
        layout_btn_oper.addWidget(btn_raz_q, 1, 2)

        btn_mod = QPushButton('%')
        btn_mod.clicked.connect(mod)
        btn_mod.setToolTip('Môdulo')
        layout_btn_oper.addWidget(btn_mod, 1, 3)

        # ***** 2 linha *****
        btn_log = QPushButton('logB(v)')
        btn_log.clicked.connect(log_b)
        btn_log.setToolTip('Logaritmo do Valor na base B')
        layout_btn_oper.addWidget(btn_log, 2, 0)

        btn_log2 = QPushButton('log2(v)')
        btn_log2.clicked.connect(log2)
        btn_log2.setToolTip('Logaritmo do Valor na base 2')
        layout_btn_oper.addWidget(btn_log2, 2, 1)

        btn_log10 = QPushButton('log10(v)')
        btn_log10.clicked.connect(log10)
        btn_log10.setToolTip('Logaritmo do Valor na base 10')
        layout_btn_oper.addWidget(btn_log10, 2, 2)

        btn_log_n = QPushButton('logN(v)')
        btn_log_n.clicked.connect(log_n)
        btn_log_n.setToolTip('Logaritmo Natural do Valor')
        layout_btn_oper.addWidget(btn_log_n, 2, 3)

        btn_seno = QPushButton('Seno(v)')
        btn_seno.clicked.connect(seno)
        btn_seno.setToolTip('Seno do Valor em Radianos')
        layout_btn_oper.addWidget(btn_seno, 3, 0)

        btn_cos = QPushButton('Cos(v)')
        btn_cos.clicked.connect(cos)
        btn_cos.setToolTip('Coseno do Valor em Radianos')
        layout_btn_oper.addWidget(btn_cos, 3, 1)

        btn_tan = QPushButton('Tan(v)')
        btn_tan.clicked.connect(tan)
        btn_tan.setToolTip('Tangente do Valor em Radianos')
        layout_btn_oper.addWidget(btn_tan, 3, 2)

        btn_a_tan = QPushButton('ArcTan(v)')
        btn_a_tan.clicked.connect(atan)
        btn_a_tan.setToolTip('Arco Tangente do Valor em Radianos')
        layout_btn_oper.addWidget(btn_a_tan, 3, 3)
        layout_operacoes.addRow(layout_btn_oper)

        btn_clr = QPushButton('AC')
        btn_clr.clicked.connect(apagar)
        btn_clr.setToolTip('Apagar Valores e Resultado')
        layout_operacoes.addRow(btn_clr)

        # ***** separador *****
        layout_operacoes.addRow(QLabel('<hr>'))

        def link(): webbrowser.open('https://artesgc.home.blog')
        label_trade = QLabel('<b><a href="#" style="text-decoration:none;">&trade;ArtesGC Inc</a></b>')
        label_trade.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_trade.linkActivated.connect(link)
        label_trade.setToolTip('Abrir website oficial da ArtesGC!')
        layout_operacoes.addRow(label_trade)

        frame_operacoes.setLayout(layout_operacoes)
        self.tab.addTab(frame_operacoes, 'Operações')
        self.tab.setCurrentWidget(frame_operacoes)
