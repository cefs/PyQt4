#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import * 

app = QApplication([])

# FontDialog
# ft = QFontDialog.getFont(QFont("Chandas", 10), None, 'Escolha uma fonte')

# PageSetupDialog
# dl = QPageSetupDialog(None)
# dl.setWindowTitle('Seleção de Fonte')
# dl.exec_()
# dl.printer()

#PrintDialog
QPrintDialog(None).exec_()


