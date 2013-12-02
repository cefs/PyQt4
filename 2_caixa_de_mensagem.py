#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#
# Simples Dialogo PyQt4
#

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        
        # criar um label e o bot�o close_button
        label = QLabel("Tecle em close para fechar")
        close_button = QPushButton("&Close")
        
        # criar uma caixa de layout vertical, para
        # organizar os elementos
        vbox = QVBoxLayout()
        
        # adicionar os elementos a vbox
        vbox.addWidget(label)
        vbox.addWidget(close_button)
        
        # adicionar a vbox ao dialogo
        self.setLayout(vbox)
        
        # conecta o evento click do bot�o close ao
        # slot reject(), s�da do aplicativo
        self.connect(close_button, SIGNAL("clicked()"),
                     self, SLOT("reject()"))
        
        # muda o t�tulo da janela
        self.setWindowTitle("Dialog - 01")
        

if __name__ == "__main__":
    # cria o objeto aplicativo
    app = QApplication(sys.argv)
    # cria o dialogo
    dlg = Form()
    # executa o dialogo
    dlg.exec_()