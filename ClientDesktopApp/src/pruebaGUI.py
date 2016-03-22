import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setGeometry(300,300,800,400)
window.setWindowTitle("PyQt Ini")
window.show()
print("ok")
