#!/bin/env python                 
#    
# -*- coding: iso-8859-1 -*                             
 
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
 
class MyDialog(QDialog):
  def __init__(self, parent = None):
    super(MyDialog, self).__init__(parent)
 
    label1 = QLabel("&lt;h2&gt;Hello&lt;/h2&gt;")
    label2 = QLabel("&lt;h1 style=\"color: #0000FF\"&gt;World...&lt;/h1&gt;")
 
    vbox = QVBoxLayout()
    vbox.addWidget(label1)
    vbox.addWidget(label2)
 
    self.setLayout(vbox)
 
app = QApplication(sys.argv)
dlg = MyDialog()
dlg.exec_()