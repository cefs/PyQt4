#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        
        # criar label
        label = QLabel("Selecione um dos bot�es abaixo \npara abrir o di�logo desejado")
        
        #cria os bot�es
        question_button     = QPushButton("&Question")
        information_button  = QPushButton("&Information")
        warning_button      = QPushButton("&Warning")
        critical_button     = QPushButton("&Critical")
        close_button        = QPushButton("&Close")
        
        # cria uma caixa de layout vertical, para
        # organizar os elementos
        vbox = QVBoxLayout()
        
        # adicionar os elementos a vbox
        vbox.addWidget(label)
        vbox.addWidget(question_button)
        vbox.addWidget(information_button)
        vbox.addWidget(warning_button)
        vbox.addWidget(critical_button)
        vbox.addWidget(close_button)
        
        # adiciona o vbox ao di�logo
        self.setLayout(vbox)
        
        # conecta o evento click do bot�o close ao
        # slot reject(), sa�da do aplicativo
        self.connect(close_button, SIGNAL("clicked()"),
                     self, SLOT("reject()"))
        
        # conecta os bot�es �s devidas fun��es
        self.connect(question_button, SIGNAL("clicked()"),
                     self.question_button_clicked)
        
        self.connect(information_button, SIGNAL("clicked()"),
                     self.information_button_clicked)
        
        self.connect(warning_button, SIGNAL("clicked()"),
                     self.warning_button_clicked)
        
        self.connect(critical_button, SIGNAL("clicked()"),
                     self.critical_button_clicked)
        
        # muda o t�tulo da janela
        self.setWindowTitle('Dialog - 01')
        
    def question_button_clicked(self):
        print "Question pressed..."
        msg = QMessageBox.question(self, "QMessageBox",
                                   "Isto � uma quest�o...", QMessageBox.Yes|QMessageBox.No)
        
    def information_button_clicked(self):
        print "Information pressed..."
        msg = QMessageBox.information(self, "QMessageBox",
                                   "Isto � uma informa��o...", QMessageBox.Close)
        
    def warning_button_clicked(self):
        print "Warning pressed..."
        msg = QMessageBox.warning(self, "QMessageBox",
                                   "Isto � uma informa��o...", QMessageBox.Close)
        
    def critical_button_clicked(self):
        print "Critical pressed..."
        msg = QMessageBox.critical(self, "QMessageBox", \
                                   "Isto � uma Critical...", \
                                   QMessageBox.Apply|QMessageBox.Reset|QMessageBox.Close)
        
if __name__ == "__main__":
    # cria objeto aplicativo
    app = QApplication(sys.argv)
    # cria di�logo
    dlg = Form()
    # executa di�logo
    dlg.exec_()