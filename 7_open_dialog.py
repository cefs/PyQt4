#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import * 

app = QApplication([])

#fileName = QFileDialog.getOpenFileName(None, 'Open File', '.', 'Texto (*.txt); All (*)')
#fileNames = QFileDialog.getOpenFileNames(None, 'Open File', '.', 'Texto (*.txt); All (*)')
#for name in fileNames: print name

dirName = QFileDialog.getExistingDirectory(None, 'Dir name', '/etc/')
print dirName    