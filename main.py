#定时推送消息的app
#基本功能1：读取md文件
#基本功能2：设定时间一到，自动跳出窗口
#基本功能3：可以输入然后保存内容为md文件

import sys
import time
import random
from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QPushButton,QLabel,QFileDialog,QLineEdit
from PySide2.QtCore import Slot


BG_IMG=r'D:\python_project\app1\rose.jpg'
TIME_FILE=r'D:\python_project\app1\talk_files\time_set.txt'


#主窗口
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #确定窗口位置
        self.setGeometry(300, 100, 800, 800)
        self.hello=None
        self.back_image = QLabel(self)
        self.back_image.setText("<center><font>Hello!<br/>"
                                "What talk do you want to have today?</font></center>")
        self.back_image.setObjectName('bg_label')
        self.button = QPushButton("To choose file, Click me!")
        self.break_time = QLineEdit("5")
        self.break_button = QPushButton("To break, Click me!")

        #Create a layout to organize the Widgets
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.back_image)
        self.layout.addWidget(self.break_time)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.break_button)
        self.setLayout(self.layout)

        #click to choose talk file
        self.button.clicked.connect(self.magic)
        self.break_button.clicked.connect(self.take_break)

        #set all style of this widget
        self.setStyleSheet("QLabel#bg_label{background-image: url(planet.jpg);font: bold 70px;color:#FFE699}"+
                           "QPushButton{background-color: #C89595;font: bold 30px;border-width: 1px;border-color: black;}")

    #choose the magical file to light up your day!
    @Slot()
    def magic(self):

        fileName = QFileDialog.getOpenFileName(self)[0]
        with open(fileName, 'r', encoding='utf-8') as f:
            self.hello = f.readlines()

    def take_break(self):
        if self.hello:
            self.hide()
            if self.break_time.text():
                time.sleep(int(self.break_time.text())*60)
            else:
                time.sleep(30*60)
            self.back_image.setText(random.choice(self.hello))
            self.show()


if __name__ == '__main__':

    #先创建窗口进行文件选择
    #create a QApplication instance
    app = QApplication()
    #A QLabel is a widget that can present text (simple or rich, like html), and images
    widget = MyWidget()
    widget.show()
    #enter the Qt main loop and start to execute the Qt code
    sys.exit(app.exec_())






