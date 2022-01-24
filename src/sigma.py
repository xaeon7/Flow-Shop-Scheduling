import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QStackedWidget

from screens.StartScreen import StartScreen

app = QApplication(sys.argv)
widget = QStackedWidget()
Start = StartScreen(widget = widget)

widget.addWidget(Start)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.setWindowIcon(QtGui.QIcon('src/assets/Sigma.ico'))
widget.setWindowTitle('Sigma - Flow Shop Scheduling')
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting...")