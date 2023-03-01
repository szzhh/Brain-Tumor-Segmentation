# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\AI\Brain-Tumor-Segmentation\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1902, 1120)
        Form.setMouseTracking(False)
        Form.setStyleSheet("#Form{\n"
"    background-color: rgb(231, 246, 255);\n"
"}\n"
"#pushButton {\n"
"    image:url(icon/1.png);\n"
"    background-color:transparent; \n"
"}\n"
"#pushButton:hover{\n"
"    image:url(icon/1_1.png);\n"
"}\n"
"#pushButton_2 {\n"
"    image:url(icon/2.png);\n"
"    background-color:transparent; \n"
"}\n"
"#pushButton_2:hover{\n"
"    image:url(icon/2_1.png);\n"
"}\n"
"#pushButton_3 {\n"
"    image:url(icon/3.png);\n"
"    background-color:transparent; \n"
"}\n"
"#pushButton_3:hover{\n"
"    image:url(icon/3_1.png);\n"
"}\n"
"#pushButton_4 {\n"
"    image:url(icon/5.png);\n"
"    background-color:transparent; \n"
"}\n"
"#pushButton_4:hover{\n"
"    image:url(icon/5_1.png);\n"
"}\n"
"#pushButton_5 {\n"
"    image:url(icon/12.png);\n"
"    background-color:transparent; \n"
"}\n"
"#pushButton_5:hover{\n"
"    image:url(icon/12_1.png);\n"
"}\n"
"#pushButton_6 {\n"
"    image:url(icon/6.png);\n"
"    background-color:transparent; \n"
"}\n"
"#pushButton_6:hover{\n"
"    image:url(icon/6_1.png);\n"
"}\n"
"#pushButton_8 {\n"
"    image:url(icon/6.png);\n"
"    background-color:transparent; \n"
"}\n"
"#pushButton_8:hover{\n"
"    image:url(icon/6_1.png);\n"
"}\n"
"#pushButton_9 {\n"
"    image:url(icon/9.png);\n"
"    background-color:transparent; \n"
"}\n"
"#pushButton_9:hover{\n"
"    image:url(icon/9_1.png);\n"
"}\n"
"#pushButton_10 {\n"
"    color: black;\n"
"    float: left;\n"
"    text-decoration: none;\n"
"    transition: background-color .3s;\n"
"    font-size: 30px;\n"
"}\n"
"#pushButton_10:hover{    \n"
"    background-color: rgb(198, 204, 209);\n"
"    color: black;\n"
"    /*border: 1px solid #ddd;*/\n"
"    font-size: 40px;\n"
"}\n"
"#pushButton_11 {\n"
"    color: black;\n"
"    float: left;\n"
"    text-decoration: none;\n"
"    transition: background-color .3s;\n"
"    font-size: 30px;\n"
"}\n"
"#pushButton_11:hover{    \n"
"    background-color: rgb(198, 204, 209);\n"
"    color: black;\n"
"    /*border: 1px solid #ddd;*/\n"
"    font-size: 40px;\n"
"}\n"
"/*QComboBox::drop-down {\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
"width: 30px;\n"
"border-left-width: 0px;\n"
"border-left-color: gray;\n"
"border-left-style: solid;\n"
"border-top-right-radius: 3px;\n"
"border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(icon/8.png);\n"
"}\n"
"QComboBox::down-arrow:hover {\n"
"    image: url(icon/7.png);\n"
"}*/\n"
"QSlider::add-page:Horizontal\n"
"     {     \n"
"        background-color: rgb(87, 97, 106);\n"
"        height:4px;\n"
"     }\n"
"     QSlider::sub-page:Horizontal \n"
"    {\n"
"        /*background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(231,80,229, 255), stop:1 rgba(7,208,255, 255));*/\n"
"        \n"
"        background-color: rgb(89, 147, 255);\n"
"        height:4px;\n"
"     }\n"
"    QSlider::groove:Horizontal \n"
"    {\n"
"        background:transparent;\n"
"        height:6px;\n"
"    }\n"
"    QSlider::handle:Horizontal \n"
"    {\n"
"        height: 50px;\n"
"        width:30px;\n"
"        border-image: url(icon/10.png);\n"
"        margin: -8 0px; \n"
"    }\n"
"QCheckBox::indicator::unchecked {   \n"
"    image: url(icon/11_1.png);\n"
"    height: 20px;\n"
"    width:20px;\n"
"}\n"
"QCheckBox::indicator::checked { \n"
"    image: url(icon/11.png);\n"
"    height: 20px;\n"
"    width:20px;\n"
"}\n"
"QCheckBox{\n"
"    spacing: 20px;\n"
"}\n"
"QHeaderView                    \n"
"{\n"
"    background:transparent; \n"
"}\n"
"QHeaderView::section          \n"
"{\n"
"    font-size:16px;               \n"
"    font-family:\"微软雅黑\"; \n"
"    color:#FFFFFF;                   \n"
"    background-color: rgb(89, 147, 255);                 \n"
"    border:none;             \n"
"          \n"
"}\n"
"QTableWidget                  \n"
"{\n"
"    background:#FFFFFF;          \n"
"    border:none;                   \n"
" \n"
"    font-size:16px;                \n"
"    font-family:\"微软雅黑\"; \n"
"    color:#666666;               \n"
"}\n"
"QTableWidget::item::selected      \n"
"{                       \n"
"    color: rgb(0, 0, 0); \n"
"    background-color: rgb(227, 227, 227);\n"
"}            ")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(263, 0, 1641, 101))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 271, 101))
        self.label_11.setStyleSheet("font: 25pt \"楷体\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(89, 147, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(1610, 30, 61, 51))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(1520, 30, 61, 51))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(1200, 10, 81, 81))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 100, 271, 51))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(0, 150, 271, 31))
        self.label_4.setStyleSheet("font: 15pt \"华文楷体\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(0, 220, 271, 41))
        self.label_5.setStyleSheet("font: 15pt \"华文楷体\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(1700, 30, 61, 51))
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(0, 380, 271, 811))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(1090, 150, 780, 780))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(290, 150, 141, 61))
        self.label_12.setStyleSheet("background-color: rgb(89, 147, 255);\n"
"color: rgb(255, 255, 255);\n"
"/*border-top-left-radius:30px;\n"
"border-top-right-radius:0;\n"
"border-bottom-right-radius:30px;\n"
"border-bottom-left-radius:0;*/\n"
"font: 12pt \"微软雅黑\";")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(1090, 150, 141, 61))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"微软雅黑\";\n"
"background-color: rgb(89, 147, 255);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(350, 960, 681, 31))
        self.horizontalSlider.setStyleSheet("")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(155)
        self.horizontalSlider.setProperty("value", 1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(590, 1020, 61, 31))
        self.lineEdit_3.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(690, 1020, 121, 31))
        self.label_14.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.label_14.setObjectName("label_14")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(20, 390, 41, 31))
        self.label_17.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border-radius: 10px;")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(20, 430, 41, 31))
        self.label_18.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 10px;")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(30, 510, 231, 41))
        self.checkBox.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_1 = QtWidgets.QCheckBox(Form)
        self.checkBox_1.setGeometry(QtCore.QRect(30, 570, 111, 41))
        self.checkBox_1.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.checkBox_1.setObjectName("checkBox_1")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.checkBox_1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(1070, 150, 20, 780))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(520, 1000, 61, 71))
        self.pushButton_10.setStyleSheet("background-color: rgb(231, 246, 255);")
        self.pushButton_10.setFlat(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(810, 1000, 61, 71))
        self.pushButton_11.setMouseTracking(False)
        self.pushButton_11.setStyleSheet("background-color: rgb(231, 246, 255);")
        self.pushButton_11.setAutoDefault(False)
        self.pushButton_11.setFlat(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(1090, 970, 781, 101))
        self.lineEdit_4.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setFrame(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 730, 261, 391))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(7, 0, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(24)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(0, 680, 271, 41))
        self.label_8.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(20, 470, 41, 31))
        self.label_19.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"border-radius: 10px;")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(10, 670, 251, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_account = QtWidgets.QLabel(Form)
        self.label_account.setGeometry(QtCore.QRect(0, 180, 271, 41))
        self.label_account.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"background-color: rgb(231, 246, 255);")
        self.label_account.setAlignment(QtCore.Qt.AlignCenter)
        self.label_account.setObjectName("label_account")
        self.label_name = QtWidgets.QLabel(Form)
        self.label_name.setGeometry(QtCore.QRect(0, 260, 271, 41))
        self.label_name.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"background-color: rgb(231, 246, 255);")
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.label_uid = QtWidgets.QLabel(Form)
        self.label_uid.setGeometry(QtCore.QRect(0, 340, 271, 41))
        self.label_uid.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"background-color: rgb(231, 246, 255);")
        self.label_uid.setAlignment(QtCore.Qt.AlignCenter)
        self.label_uid.setObjectName("label_uid")
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(0, 300, 271, 41))
        self.label_21.setStyleSheet("\n"
"font: 15pt \"华文楷体\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(10, 550, 251, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(150, 570, 111, 41))
        self.checkBox_2.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.checkBox_2.setObjectName("checkBox_2")
        self.buttonGroup.addButton(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 620, 111, 41))
        self.checkBox_3.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.checkBox_3.setObjectName("checkBox_3")
        self.buttonGroup.addButton(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(150, 620, 111, 41))
        self.checkBox_4.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.checkBox_4.setObjectName("checkBox_4")
        self.buttonGroup.addButton(self.checkBox_4)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 390, 191, 31))
        self.label.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 430, 201, 31))
        self.label_2.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.label_2.setObjectName("label_2")
        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setGeometry(QtCore.QRect(70, 470, 191, 31))
        self.label_22.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.label_22.setObjectName("label_22")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(1310, 20, 71, 61))
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(1800, 30, 51, 51))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(1410, 30, 75, 51))
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_7.raise_()
        self.label_11.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.pushButton_9.raise_()
        self.label_6.raise_()
        self.label_9.raise_()
        self.label_13.raise_()
        self.horizontalSlider.raise_()
        self.lineEdit_3.raise_()
        self.label_14.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.checkBox.raise_()
        self.checkBox_1.raise_()
        self.line.raise_()
        self.pushButton_10.raise_()
        self.pushButton_11.raise_()
        self.lineEdit_4.raise_()
        self.label_12.raise_()
        self.tableWidget.raise_()
        self.label_8.raise_()
        self.label_19.raise_()
        self.line_2.raise_()
        self.label_account.raise_()
        self.label_name.raise_()
        self.label_uid.raise_()
        self.label_21.raise_()
        self.line_3.raise_()
        self.checkBox_2.raise_()
        self.checkBox_3.raise_()
        self.checkBox_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_22.raise_()
        self.pushButton_8.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Brain Dancer Diagnosis"))
        self.label_11.setText(_translate("Form", "云上智脑"))
        self.label_4.setText(_translate("Form", "账户"))
        self.label_5.setText(_translate("Form", "姓名"))
        self.label_12.setText(_translate("Form", "2D切分"))
        self.label_13.setText(_translate("Form", "3D重建"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "1"))
        self.label_14.setText(_translate("Form", "/        155"))
        self.checkBox.setText(_translate("Form", "显示分割结果"))
        self.checkBox_1.setText(_translate("Form", "t1"))
        self.pushButton_10.setText(_translate("Form", "<"))
        self.pushButton_11.setText(_translate("Form", ">"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "账号"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "姓名"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "UID"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "年龄"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "主治医生"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "肿瘤体积"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "肿瘤核心"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "增强肿瘤"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "内容"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("Form", "病例信息"))
        self.label_account.setText(_translate("Form", "2333"))
        self.label_name.setText(_translate("Form", "wxd"))
        self.label_uid.setText(_translate("Form", "d0"))
        self.label_21.setText(_translate("Form", "UID"))
        self.checkBox_2.setText(_translate("Form", "t2"))
        self.checkBox_3.setText(_translate("Form", "t1ce"))
        self.checkBox_4.setText(_translate("Form", "flair"))
        self.label.setText(_translate("Form", "肿瘤区域颜色"))
        self.label_2.setText(_translate("Form", "肿瘤核心区域颜色"))
        self.label_22.setText(_translate("Form", "增强肿瘤区域颜色"))

