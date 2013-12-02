#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import * 

app = QApplication(sys.argv)

#dl1 = QInputDialog.getInt(None, 'QInputDialog getInteger', 'Entre com o número de produtos:', 1, 0, 150, 5)
#print dl1

#dl2 = QInputDialog.getDouble(None, 'QInputDialog getInteger', 'Entre com o custo do produto:', 5.58, 5.0, 15.0, 2)
#print dl2

#dl3 = QInputDialog.getText(None,'getText - Normal', 'Entre com seu nome completo', QLineEdit.Normal, "Nome Completo")
#dl4 = QInputDialog.getText(None,'getText - Normal', 'Entre com sua senha', QLineEdit.Password)
#dl5 = QInputDialog.getText(None,'getText - Normal', 'Entre com sua senha', QLineEdit.PasswordEchoOnEdit)
#dl6 = QInputDialog.getItem(None, 'getItem', 'Selecione um item:', 
#                           ['diodo','capacitor','resistor','transformador'])
dl7 = QInputDialog.getItem(None, 'getItem', 'Selecione um item:', 
                           ('diodo','capacitor','resistor','transformador'), 2, False)                           


