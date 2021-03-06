import sys
from Assignment2a import *
from PyQt4.QtGui import *

SCALE_CONST = 0.95
DAY_IMAGE = "day.jpg"
NIGHT_IMAGE = "night.jpg"

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Question1()
        self.ui.setupUi(self)
        self.setupSysClockLcd()
        self.setupCurrentTimeVisualization()

    def setupSysClockLcd(self):
        def showLCD():
            currentTime = QtCore.QTime.currentTime()
            currentTimeText = currentTime.toString('hh:mm')
            self.ui.sysClockLcd.display(currentTimeText)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(showLCD)
        timer.start(1000)
        showLCD()

    def setupCurrentTimeVisualization(self):
        def getCurrentTimePixmap():
            pixmap = QtGui.QPixmap()
            currentTime = QtCore.QTime.currentTime()
            workStartTime = QtCore.QTime(8,0)
            workEndTime = QtCore.QTime(17,0)
            if workStartTime <= currentTime and currentTime <= workEndTime:
                pixmap.load(DAY_IMAGE)
            else:
                pixmap.load(NIGHT_IMAGE)
            return pixmap

        def formatPixmap(pixmap):
            width = self.ui.currentTimeVisualization.width()
            height = self.ui.currentTimeVisualization.height()
            scaledPixmap = pixmap.scaled(width*SCALE_CONST, height*SCALE_CONST)
            return scaledPixmap

        self.scene = QGraphicsScene(self)
        appropriatePixmap = getCurrentTimePixmap()
        formattedPixmap = formatPixmap(appropriatePixmap)
        self.scene.addPixmap(formattedPixmap)
        self.ui.currentTimeVisualization.setScene(self.scene)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myApp = MyForm()
    myApp.show()
    sys.exit(app.exec_())