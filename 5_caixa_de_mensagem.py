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
        label = QLabel("Selecione um dos botões abaixo \npara abrir o diálogo desejado")
        
        #cria os botões
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
        
        # adiciona o vbox ao diálogo
        self.setLayout(vbox)
        
        # conecta o evento click do botão close ao
        # slot reject(), saída do aplicativo
        self.connect(close_button, SIGNAL("clicked()"),
                     self, SLOT("reject()"))
        
        # conecta os botões às devidas funções
        self.connect(question_button, SIGNAL("clicked()"),
                     self.question_button_clicked)
        
        self.connect(information_button, SIGNAL("clicked()"),
                     self.information_button_clicked)
        
        self.connect(warning_button, SIGNAL("clicked()"),
                     self.warning_button_clicked)
        
        self.connect(critical_button, SIGNAL("clicked()"),
                     self.critical_button_clicked)
        
        # muda o título da janela
        self.setWindowTitle('Dialog - 01')
        
    def question_button_clicked(self):
        print "Question pressed..."
        msg = QMessageBox.question(self, "QMessageBox",
                                   "Isto é uma questão...", QMessageBox.Yes|QMessageBox.No)
        
    def information_button_clicked(self):
        print "Information pressed..."
        msg = QMessageBox.information(self, "QMessageBox",
                                   "Isto é uma informação...", QMessageBox.Close)
        
    def warning_button_clicked(self):
        print "Warning pressed..."
        msg = QMessageBox.warning(self, "QMessageBox",
                                   "Isto é uma informação...", QMessageBox.Close)
        
    def critical_button_clicked(self):
        print "Critical pressed..."
        msg = QMessageBox.critical(self, "QMessageBox", \
                                   "Isto é uma Critical...", \
                                   QMessageBox.Apply|QMessageBox.Reset|QMessageBox.Close)
        
if __name__ == "__main__":
    # cria objeto aplicativo
    app = QApplication(sys.argv)
    # cria diálogo
    dlg = Form()
    # executa diálogo
    dlg.exec_()