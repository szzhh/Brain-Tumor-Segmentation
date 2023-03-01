from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
import sys
import os
import requests
import json
from mainwindow import Mainwindow

class Lwindow():
    def __init__(self):
        qfile_stats=QFile(os.path.split(os.path.realpath(__file__))[0]+'/Login.ui')
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()

        self.ui = QUiLoader().load(qfile_stats)

        self.ui.pushButton_1.clicked.connect(self.check)
        self.ui.pushButton_2.clicked.connect(self.register)
        
    def check(self):
        account = self.ui.lineEdit_1.text()
        password = self.ui.lineEdit_2.text()
        account_type = 'doctor'
        r = requests.post('http://172.24.21.239:5000/login', json={'account': account, 'passwd': password, 'account_type': account_type})
        j=json.loads(r.text)
        if j['status']:
            d_uid=j['uid']
            self.open_mainwindow(d_uid)
        elif not j['status']:
            QMessageBox.about(self.ui,'提示','账户或密码错误，请检查后重新输入！')
        
    def open_mainwindow(self,d_uid):
        # 关闭登录
        self.ui.close()
        # 实例化另外一个窗口
        self.mainwindow = Mainwindow(d_uid)
        # 显示新窗口
        self.mainwindow.show()
        QMessageBox.about(self.ui,'提示','登录成功！')
    
    def register(self):
        self.ui.close()
        self.rwindow = Rwindow()
        self.rwindow.ui.show()
        
class Rwindow():
    def __init__(self):
        qfile_stats=QFile(os.path.split(os.path.realpath(__file__))[0]+'/Register.ui')
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()

        self.ui = QUiLoader().load(qfile_stats)

        self.ui.pushButton_1.clicked.connect(self.check)
        self.ui.pushButton_2.clicked.connect(self.back)
        
    def back(self):
        self.ui.close()
        self.lwindow = Lwindow()
        self.lwindow.ui.show()
        
    def check(self):
        account = self.ui.lineEdit_1.text()
        password = self.ui.lineEdit_2.text()
        name = self.ui.lineEdit_3.text()
        account_type = 'doctor'
        r = requests.post('http://172.24.21.239:5000/register', json={'account': account, 'passwd': password,'name':name, 'account_type': account_type})
        j=json.loads(r.text)
        if j['status']:
            QMessageBox.about(self.ui,'提示','注册成功，请返回登录！')
        elif not j['status']:
            QMessageBox.about(self.ui,'提示', j['msg'])

if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon(os.path.split(os.path.realpath(__file__))[0]+r'/imgs/brain.ico'))
    lwindow = Lwindow()
    lwindow.ui.show()
    app.exec_()