import os
import shutil
import  cv2
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageQt, ImageGrab
from Ui_mainwindow import Ui_Form
import vtk_first_try
import vtkmodules.all as vtk
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import numpy as np
import json
from utils import *
import requests


n=0
max_n=155
img=cv2.imread(os.path.split(os.path.realpath(__file__))[0]+r'/imgs/blank.png', cv2.COLOR_BGR2RGB)
imglst=[]


class L(QLabel):
    def __init__(self, parent):
        global path
        global img
        super().__init__(parent=parent)
        self.setStyleSheet('QFrame {background-color:black;}')
        self.setGeometry(QtCore.QRect(290, 150, 780, 780))
        #self.img1 = ImageQt.toqpixmap(Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)))
        #self.scaled_img = self.img1.scaled(self.size())
        self.img1 = QPixmap(cov(img))
        self.scaled_img = self.img1.scaled(self.size())
        #self.scaled_img= ImageQt.toqpixmap(Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)).resize((self.width(), self.height())))
        self.point = QPoint(0, 0)
        self.lastPos= QPoint(self.width()/2,self.height()/2)#十字线复原
    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        self.draw_img(painter)
        self.line(painter)
        painter.end()
        
    def line(self,painter):
        pen=QPen()
        pen.setWidth(2)
        pen.setStyle(Qt.DashDotLine)
        pen.setColor(Qt.blue)
        painter.setPen(pen)
        painter.drawLine(0, self.lastPos.y(), self.width(), self.lastPos.y())
        painter.drawLine(self.lastPos.x(), 0, self.lastPos.x(), self.height())
        
    def draw_img(self, painter):
        painter.drawPixmap(self.point, self.scaled_img)

    def mouseMoveEvent(self, e):  # 重写移动事件
        if self.left_click:
            self._endPos = e.pos() - self._startPos
            self.point = self.point + self._endPos
            self._startPos = e.pos()
            self.lastPos=e.pos()
            self.repaint()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_click = True
            self._startPos = e.pos()
            self.lastPos=e.pos()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.lastPos=e.pos()
            #self.left_click = False
            self.repaint()
        elif e.button() == Qt.RightButton:
            self.point = QPoint(0, 0)
            self.scaled_img = self.img1.scaled(self.size())
            self.lastPos= QPoint(self.width()/2,self.height()/2)
            self.repaint()

    def wheelEvent(self, e):
        if e.angleDelta().y() > 0:
            # 放大图片
            self.scaled_img = self.img1.scaled(self.scaled_img.width()-20, self.scaled_img.height()-20)
            new_w = e.x() - (self.scaled_img.width() * (e.x() - self.point.x())) / (self.scaled_img.width() + 20)
            new_h = e.y() - (self.scaled_img.height() * (e.y() - self.point.y())) / (self.scaled_img.height() + 20)
            self.point = QPoint(new_w, new_h)
            self.repaint()
        elif e.angleDelta().y() < 0:
            # 缩小图片
            self.scaled_img = self.img1.scaled(self.scaled_img.width()+20, self.scaled_img.height()+20)
            new_w = e.x() - (self.scaled_img.width() * (e.x() - self.point.x())) / (self.scaled_img.width() - 20)
            new_h = e.y() - (self.scaled_img.height() * (e.y() - self.point.y())) / (self.scaled_img.height() - 20)
            self.point = QPoint(new_w, new_h)
            self.repaint()

    '''def resizeEvent(self, e):
        if self.parent is not None:
            self.scaled_img = self.img1.scaled(self.size())
            self.point = QPoint(0, 0)
            self.update()'''

class Mainwindow(QWidget):
    def __init__(self,d_uid):
        super().__init__()
        self.label=L(self)
        #self.label.setScaledContents(True)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.phone)
        self.ui.pushButton_2.clicked.connect(self.download)
        self.ui.pushButton_8.clicked.connect(self.deal)
        self.ui.pushButton_3.clicked.connect(self.upload)
        self.ui.pushButton_4.clicked.connect(self.exit)
        self.ui.pushButton_5.clicked.connect(self.edit)
        self.ui.pushButton_9.clicked.connect(self.help)
        self.ui.pushButton_10.clicked.connect(self.left)
        self.ui.pushButton_11.clicked.connect(self.right)
        self.ui.lineEdit_3.returnPressed.connect(self.enter)
        self.ui.horizontalSlider.valueChanged.connect(self.slider)
        self.ui.checkBox.stateChanged.connect(self.check)
        self.ui.checkBox_1.stateChanged.connect(self.check)
        self.ui.checkBox_2.stateChanged.connect(self.check)
        self.ui.checkBox_3.stateChanged.connect(self.check)
        self.ui.checkBox_4.stateChanged.connect(self.check)
        #3d
        self.vtkWindow = QVTKRenderWindowInteractor(self)
        self.vtkWindow.setGeometry(1090, 150, 780, 780)
        self.ui.label_13.raise_()
        self.d_uid=d_uid
        r = requests.post('http://172.24.21.239:5000/query', json={'account_type': 'doctor', 'uid': self.d_uid})
        self.d_info = json.loads(r.text)['user_info']
        self.p_info = json.loads(r.text)['user_info']['patients'][0]
        self.ui.label_account.setText( self.d_info['account'])
        self.ui.label_name.setText( self.d_info['name'])
        self.ui.label_uid.setText(self.d_info['uid'])

    def phone(self):
        QMessageBox.about(self,'联系我们','电话：16680806885\n'
                                                'QQ：23380149114\n'
                                                '微信：szh2338014914\n'
                                                '邮箱：sunzhonghao@csu.edu.cn\n')
    def help(self):
        QMessageBox.about(self,'帮助','1、云端上传功能：将待处理的文件上传至云端数据库。\n'
                                                        '2、云端处理下载功能：将云端数据库中的待处理文件进行分割并缓存到本地显示\n'
                                                        '3、病历导出功能：将病人信息、2D分割图片、3D重建图片及病情描述、医生建议导出为pdf\n'
                                                        '4、联系我们\n'
                                                        '5、使用帮助：客户端使用信息\n'
                                                        '6、退出\n')
    def edit(self):
        items = ['无肿瘤T0','一期T1', '二期T2','三期T3', '四期T4']
        value1, ok1 = QInputDialog.getItem(self, "病症判别", "请选择病症情况", items, 0, True)
        if ok1:
            print(value1)
        value2, ok2 = QInputDialog.getMultiLineText(self, "治疗建议","请输入治疗建议",None)
        if ok2:
            print(value2)
    def upload(self):
        path=(QtWidgets.QFileDialog.getOpenFileNames(None, '浏览', os.path.split(os.path.realpath(__file__))[0]))[0]
        QMessageBox.about(self,'提示','上传处理中······（预计等待20秒）')
        r = requests.post('http://172.24.21.239:5000/query', json={'account_type': 'doctor', 'uid': self.d_uid})
        self.p_info = json.loads(r.text)['user_info']['patients'][0]
        r = requests.post('http://172.24.21.239:5000/uploader', data={'uid': self.p_info['uid']}, files={'t1': open(path[1], 'rb'), 't2': open(path[3], 'rb'), 't1ce': open(path[2], 'rb'), 'flair': open(path[0], 'rb')})
        if json.loads(r.text)['status']:
            QMessageBox.about(self,'提示','文件成功上传至云端！')
    def download(self):
        global imglst

        screen = QtWidgets.QApplication.primaryScreen()
        screenshot = screen.grabWindow( self.label.winId() )
        screenshot.save(os.path.split(os.path.realpath(__file__))[0]+'/imgs/mask_t1.png','png')

        screen = QtWidgets.QApplication.primaryScreen()
        screenshot = screen.grabWindow( self.ui.label_9.winId() )
        screenshot.save(os.path.split(os.path.realpath(__file__))[0]+'/imgs/3D.png', 'png')
        
        r = requests.post('http://172.24.21.239:5000/query', json={'account_type': 'doctor', 'uid': self.d_uid})
        self.p_info = json.loads(r.text)['user_info']['patients'][0]
        
        args = {
            '姓名': self.p_info['name'],
            '年龄': str(self.p_info['age']),
            '性别': '男',
            '编号': '532',
            '住院号': '9452398',
            '床号': '18'
        }
        modulePath = os.path.split(os.path.realpath(__file__))[0]+'/imgs/temp.doc'
        savePath=QtWidgets.QFileDialog.getExistingDirectory(None, '浏览', os.path.split(os.path.realpath(__file__))[0])
        # print(savePath)    
        imagesPath = [os.path.split(os.path.realpath(__file__))[0]+'/imgs/mask_t1.png', os.path.split(os.path.realpath(__file__))[0]+'/imgs/3D.png']
        advicePath = os.path.split(os.path.realpath(__file__))[0]+'/imgs/对策.json' 
        V1 = self.p_info['TumorVolumn_1']
        V2 = self.p_info['TumorVolumn_2']
        V3 = self.p_info['TumorVolumn_3']
        
        pdfpath = generatePDF(modulePath, savePath, imagesPath, advicePath, V1,V2,V3, args)

        reply = QMessageBox.information(self, "提示", "病历成功导出至本地！是否上传至云端", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == 16384:
            r = requests.post('http://172.24.21.239:5000/export_pdf', data={'uid': self.p_info['uid']}, files={'pdf': open(pdfpath, 'rb')})
            if r.json()['status']:
                QMessageBox.about(self,'提示','病历成功上传至云端！')
    def exit(self):
        if os.path.exists(os.path.split(os.path.realpath(__file__))[0]+r'/temp/'):
            shutil.rmtree(os.path.split(os.path.realpath(__file__))[0]+r'/temp/')
        self.close()
    def left(self):
        global n
        n=(n-1)%max_n
        self.ui.lineEdit_3.setText(str(n+1))
        self.ui.horizontalSlider.setValue(n+1)
        
        self.check()
    def right(self):
        global n
        n=(n+1)%max_n
        self.ui.lineEdit_3.setText(str(n+1))
        self.ui.horizontalSlider.setValue(n+1)
        
        self.check()
    def enter(self):
        global n
        n=int(self.ui.lineEdit_3.text())-1
        self.ui.horizontalSlider.setValue(n+1)
        
        self.check()
    def slider(self):
        global n
        n=int(self.ui.horizontalSlider.value())-1
        self.ui.lineEdit_3.setText(str(n+1))
    
        self.check()
    def draw3D(self,path):
        self.vtkWindow.Initialize()
        self.vtkWindow.Start()
        ren = vtk.vtkRenderer()
        self.vtkWindow.GetRenderWindow().AddRenderer(ren)
        coneActor, coneMapper = vtk_first_try.open_nii(path)
        ren.AddVolume(coneActor)
        
    def deal(self):
        global n
        global imglst

        n=0
        QMessageBox.about(self,'提示','处理中······（预计等待15秒）')
        
        #云端查询信息
        r = requests.post('http://172.24.21.239:5000/query', json={'account_type': 'doctor', 'uid': self.d_uid})
        self.p_info = json.loads(r.text)['user_info']['patients'][0]
        p_uid=self.p_info['uid']
        
        #云端分割实例
        r = requests.get('http://172.24.21.239:5000/analyse', json={'uid': p_uid})
        QMessageBox.about(self,'提示','云端分割成功，准备下载！')
        
        path1=req_get(p_uid, 't1')
        path2=req_get(p_uid, 't2')
        path3=req_get(p_uid, 't1ce')
        path4=req_get(p_uid, 'flair')
        path5=req_get(p_uid, 'seg')
        
        imglst.append( gz2np(path1,path5))
        imglst.append( gz2np(path2,path5))
        imglst.append( gz2np(path3,path5))
        imglst.append( gz2np(path4,path5))
        
        self.ui.lineEdit_3.setText(str(n+1))
        self.ui.horizontalSlider.setValue(n+1)
        self.ui.checkBox.setChecked(False)
        self.ui.checkBox_1.setChecked(True)
        self.ui.checkBox_2.setChecked(False)
        self.ui.checkBox_3.setChecked(False)
        self.ui.checkBox_4.setChecked(False)
        
        self.draw3D(path1)#绘制右图
        self.check()#绘制左图
        
        self.ui.tableWidget.item(0,0).setText(self.p_info['account'])
        self.ui.tableWidget.item(1,0).setText(self.p_info['name'])
        self.ui.tableWidget.item(2,0).setText(self.p_info['uid'])
        self.ui.tableWidget.item(3,0).setText(str(self.p_info['age']))
        self.ui.tableWidget.item(4,0).setText(self.p_info['doctor'])
        self.ui.tableWidget.item(5,0).setText(self.p_info['TumorVolumn_1'])
        self.ui.tableWidget.item(6,0).setText(self.p_info['TumorVolumn_2'])
        self.ui.tableWidget.item(7,0).setText(self.p_info['TumorVolumn_3'])
        
        QMessageBox.about(self,'提示','处理完成！')
        self.ui.lineEdit_4.setText('处理完成！')
        
    def check(self):
        global n
        global img
        global imglst

        if not self.ui.checkBox.isChecked() and  self.ui.checkBox_1.isChecked():
            img=imglst[0][0][n]
            self.up()
        elif self.ui.checkBox.isChecked() and  self.ui.checkBox_1.isChecked():
            img=imglst[0][1][n]
            self.up()
        elif not self.ui.checkBox.isChecked() and self.ui.checkBox_2.isChecked():
            img=imglst[1][0][n]
            self.up()
        elif self.ui.checkBox.isChecked() and self.ui.checkBox_2.isChecked():
            img=imglst[1][1][n]
            self.up()
        elif not self.ui.checkBox.isChecked() and  self.ui.checkBox_3.isChecked():
            img=imglst[2][0][n]
            self.up()
        elif self.ui.checkBox.isChecked() and  self.ui.checkBox_3.isChecked():
            img=imglst[2][1][n]
            self.up()
        elif not self.ui.checkBox.isChecked() and self.ui.checkBox_4.isChecked():
            img=imglst[3][0][n]
            self.up()
        elif self.ui.checkBox.isChecked() and self.ui.checkBox_4.isChecked():
            img=imglst[3][1][n]
            self.up()
            
    def up(self):
        global img
        self.label.point = QPoint(0, 0)
        ssize=self.label.size()
        self.label.img1 = QPixmap(cov(img))
        self.label.scaled_img = self.label.img1.scaled(ssize)
        ww=self.label.width()/2
        hh=self.label.height()/2
        self.label.lastPos= QPoint(ww,hh)
        self.label.repaint()

if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon(os.path.split(os.path.realpath(__file__))[0]+r'/imgs/brain.ico'))
    mainwindow=Mainwindow('d0')
    mainwindow.show()
    app.exec_()