from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout,
QHBoxLayout, QGridLayout)
from PyQt5.QtGui import QIcon, QFont, QPixmap
import sys
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("M-GPT")
        self.setGeometry(0, 0, 800, 400)
        self.initUI()
        self.setWindowIcon(QIcon("chatgpt.png"))

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label3 = QLabel("#3")
        label4 = QLabel("#4")
        label5 = QLabel("#5")
        label6 = QLabel("#6")
        label7 = QLabel("#7")
        label3.setGeometry(0, 200, 80, 80)
        label4.setGeometry(0, 250, 80, 80)
        label5.setGeometry(0, 300, 80, 80)
        label6.setGeometry(0, 350, 80, 80)
        label7.setGeometry(0, 400, 80, 80)

        label3.setStyleSheet("background-color: red;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;")
        label6.setStyleSheet("background-color: yellow;")
        label7.setStyleSheet("background-color: green;")

        grid = QGridLayout()

        grid.addWidget(label3, 0,0)
        grid.addWidget(label4,0,1)
        grid.addWidget(label5,1,0)
        grid.addWidget(label6,1,1)
        grid.addWidget(label7,2,2)

        central_widget.setLayout(grid)


        
        label2 = QLabel(self)
        label2.setGeometry(0, 50, 80, 80)

        pixmap = QPixmap("chatgpt.png")
        label2.setPixmap(pixmap)

        label2.setScaledContents(True)

        label = QLabel("Hello, Welcome to M-GPT", self)
        label.setFont(QFont("Arial", 15))
        label.setGeometry(0, 0, 800, 50)
        label.setStyleSheet("color: #FFFFFF;"
            "background-color: #000000;"
            "font-weight: bold;"
            "font-style: italic;"
            "text-decoration: underline;")
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        label.setAlignment(Qt.AlignCenter)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) #exec_() is a built-in method of our 'app' object




if __name__ == "__main__":
    main()


