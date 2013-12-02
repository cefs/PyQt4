#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


# cria o objeto aplicatio
app = QApplication(sys.argv)

dlg = QMessageBox(None)
dlg.setWindowTitle('Message Box')
dlg.setIcon(QMessageBox.Critical)
dlg.setText('Isto é uma mensagem crítica, Deseja continuar?')
dlg.setStandardButtons(QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
resp = dlg.exec_()
