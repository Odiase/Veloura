import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSplitter, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QSplitter Vertical Example')
        self.setGeometry(300, 300, 300, 400)


        layout = QVBoxLayout(self)

        splitter = QSplitter(Qt.Vertical)

        label1 = QLabel('Top Panel (Resizable)')
        label1.setStyleSheet('background-color: lightblue; border: 1px solid black;')
        label1.setAlignment(Qt.AlignCenter)

        label2 = QLabel('Middle Panel (Resizable)')
        label2.setStyleSheet('background-color: lightgreen; border: 1px solid black;')
        label2.setAlignment(Qt.AlignCenter)

        label3 = QLabel('Bottom Panel (Resizable)')
        label3.setStyleSheet('background-color: lightcoral; border: 1px solid black;')
        label3.setAlignment(Qt.AlignCenter)

        # Adding widgets to the splitter
        splitter.addWidget(label1)
        splitter.addWidget(label2)
        splitter.addWidget(label3)

        # Optional: Set initial sizes (heights in pixels)
        splitter.setSizes([100, 200, 100])

        # 5. Add the splitter to the main layout
        layout.addWidget(splitter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    sys.exit(app.exec_())
