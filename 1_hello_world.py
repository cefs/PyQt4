#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#
# Simples Hello World em PyQt4
#

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# cria o objeto aplicatio
app = QApplication(sys.argv)

# cria um label
label =  QLabel("<font color=blue size=100><b>Hello World</b></font>")

# coloca o label do dialog
label.setWindowFlags(Qt.SplashScreen)

# apresenta o label, SLOT
label.show()

# agenda a execução de um app.quit() em 10 segundos
QTimer.singleShot(10000, app.quit)

# incia aplicativo
app.exec_()