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
dlg.setIcon(QMessageBox.Question)
dlg.setText('Este é o dialogo padrão do QMessageBox, com apenas um botão OK')
dlg.exec_()
