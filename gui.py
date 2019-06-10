from mailServer import Mail
import cv2
import numpy as np
import face_recognition
import time
from datetime import datetime
import os
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from db import Database

db = Database()

mail = Mail()

# db.insert_course(name='MATH101', day='Sunday', start='10:30', hours=5)
course = 'MATH101'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 630)
        font = QtGui.QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Pause_Camera = QtWidgets.QPushButton(self.centralwidget)
        self.Pause_Camera.setGeometry(QtCore.QRect(1050, 540, 121, 60))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Pause_Camera.setFont(font)
        self.Pause_Camera.setStyleSheet("QPushButton{\n"
                                        "color: rgb(85, 170, 255);\n"
                                        "border:2px solid rgb(85, 170, 255);\n"
                                        "border-radius: 5px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::hover{\n"
                                        "color:  rgb(255, 255, 255);\n"
                                        "border:2px solid rgb(255, 255, 255);\n"
                                        "border-radius: 5px;\n"
                                        "}\n"
                                        "\n"
                                        "")
        self.Pause_Camera.setObjectName("Pause_Camera")
        self.Play_Camera = QtWidgets.QPushButton(self.centralwidget)
        self.Play_Camera.setGeometry(QtCore.QRect(900, 540, 121, 60))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Play_Camera.setFont(font)
        self.Play_Camera.setStyleSheet("QPushButton{\n"
                                       "color: rgb(85, 170, 255);\n"
                                       "border:2px solid rgb(85, 170, 255);\n"
                                       "border-radius: 5px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton::hover{\n"
                                       "color:  rgb(255, 255, 255);\n"
                                       "border:2px solid rgb(255, 255, 255);\n"
                                       "border-radius: 5px;\n"
                                       "}\n"
                                       "\n"
                                       "")
        self.Play_Camera.setObjectName("Play_Camera")
        self.Camera = QtWidgets.QLabel(self.centralwidget)
        self.Camera.setGeometry(QtCore.QRect(790, 150, 510, 370))
        self.Camera.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.Camera.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Camera.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Camera.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Camera.setAutoFillBackground(False)
        self.Camera.setStyleSheet("border:2px solid rgb(85, 170, 255);\n"
                                  "border-radius : 5px;\n"
                                  "color : white;")
        self.Camera.setFrameShape(QtWidgets.QFrame.Box)
        self.Camera.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Camera.setLineWidth(2)
        self.Camera.setMidLineWidth(25)
        self.Camera.setText("")
        self.Camera.setOpenExternalLinks(False)
        self.Camera.setObjectName("Camera")
        self.Record = QtWidgets.QListWidget(self.centralwidget)
        self.Record.setGeometry(QtCore.QRect(50, 150, 650, 171))
        self.Record.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Record.setStyleSheet("border:2px solid rgb(85, 170, 255);\n"
                                  "border-radius : 5px;\n"
                                  "color: white;\n"
                                  "gridline-color: rgb(0, 144, 144);\n"
                                  "selection-background-color: rgb(85, 255, 255);\n"
                                  "selection-color: rgb(0, 0, 0);\n"
                                  "")
        self.Record.setFrameShape(QtWidgets.QFrame.Box)
        self.Record.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Record.setLineWidth(5)
        self.Record.setObjectName("Record")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: rgb(85, 170, 255);\n"
                                   "border-radius : 10px;")
        self.label_2.setObjectName("label_2")
        self.Name_Entry = QtWidgets.QLineEdit(self.centralwidget)
        self.Name_Entry.setGeometry(QtCore.QRect(130, 420, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.Name_Entry.setFont(font)
        self.Name_Entry.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "border:2px solid rgb(85, 170, 255);\n"
                                      "border-radius: 5px;")
        self.Name_Entry.setAlignment(QtCore.Qt.AlignCenter)
        self.Name_Entry.setClearButtonEnabled(True)
        self.Name_Entry.setObjectName("Name_Entry")
        self.Email_Entry = QtWidgets.QLineEdit(self.centralwidget)
        self.Email_Entry.setGeometry(QtCore.QRect(130, 470, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.Email_Entry.setFont(font)
        self.Email_Entry.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "border:2px solid rgb(85, 170, 255);\n"
                                       "border-radius: 5px;")
        self.Email_Entry.setCursorPosition(11)
        self.Email_Entry.setAlignment(QtCore.Qt.AlignCenter)
        self.Email_Entry.setClearButtonEnabled(True)
        self.Email_Entry.setObjectName("Email_Entry")
        self.Database_list = QtWidgets.QListWidget(self.centralwidget)
        self.Database_list.setGeometry(QtCore.QRect(320, 420, 380, 180))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Database_list.setFont(font)
        self.Database_list.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Database_list.setStyleSheet("border:2px solid rgb(85, 170, 255);\n"
                                         "border-radius : 5px;\n"
                                         "color: white;\n"
                                         "gridline-color: rgb(85, 170, 255);\n"
                                         "selection-background-color: rgb(85, 170, 255);\n"
                                         "selection-color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(0,0,0);\n")
        self.Database_list.setFrameShape(QtWidgets.QFrame.Box)
        self.Database_list.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Database_list.setLineWidth(4)
        self.Database_list.setObjectName("Database_list")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(45, 420, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setMouseTracking(False)
        self.label_3.setTabletTracking(False)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("color: rgb(85, 170, 255);\n"
                                   "border-radius : 10px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(45, 470, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_4.setFont(font)
        self.label_4.setMouseTracking(False)
        self.label_4.setTabletTracking(False)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("color: rgb(85, 170, 255);\n"
                                   "border-radius : 10px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 390, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("color: rgb(85, 170, 255);\n"
                                   "border-radius : 3px;")
        self.label_5.setObjectName("label_5")
        self.Add_Student = QtWidgets.QPushButton(self.centralwidget)
        self.Add_Student.setGeometry(QtCore.QRect(130, 520, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Add_Student.setFont(font)
        self.Add_Student.setStyleSheet("QPushButton{\n"
                                       "color: rgb(85, 170, 255);\n"
                                       "border:2px solid rgb(85, 170, 255);\n"
                                       "border-radius: 5px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton::hover{\n"
                                       "color:  rgb(255, 255, 255);\n"
                                       "border:2px solid rgb(255, 255, 255);\n"
                                       "border-radius: 5px;\n"
                                       "}\n"
                                       "\n"
                                       "")
        self.Add_Student.setObjectName("Add_Student")
        self.Add_Face = QtWidgets.QPushButton(self.centralwidget)
        self.Add_Face.setGeometry(QtCore.QRect(130, 570, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Add_Face.setFont(font)
        self.Add_Face.setStyleSheet("QPushButton{\n"
                                    "color: rgb(85, 170, 255);\n"
                                    "border:2px solid rgb(85, 170, 255);\n"
                                    "border-radius: 5px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton::hover{\n"
                                    "color:  rgb(255, 255, 255);\n"
                                    "border:2px solid rgb(255, 255, 255);\n"
                                    "border-radius: 5px;\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.Add_Face.setObjectName("Add_Face")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(790, 110, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("color: rgb(85, 170, 255);\n"
                                   "border-radius : 10px;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 10, 419, 99))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(60)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("color: rgb(85, 170, 255);\n"
                                   "border-radius : 5px;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1000, 40, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "border-radius : 5px;")
        self.label_8.setObjectName("label_8")
        self.Updates = QtWidgets.QLabel(self.centralwidget)
        self.Updates.setGeometry(QtCore.QRect(50, 340, 651, 31))
        self.Updates.setStyleSheet("color: white;\n"
                                   "border: 2px solid rgb(85, 170, 255);\n"
                                   "border-radius: 5px;\n"
                                   "font: 10pt \"NSimSun\";")
        self.Updates.setObjectName("Updates")

        self.Refresh = QtWidgets.QPushButton(self.centralwidget)
        self.Refresh.setGeometry(QtCore.QRect(705, 420, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Refresh.setFont(font)
        self.Refresh.setStyleSheet("QPushButton{\n"
                                   "color: rgb(85, 170, 255);\n"
                                   "border:2px solid rgb(85, 170, 255);\n"
                                   "border-radius: 5px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton::hover{\n"
                                   "color:  rgb(255, 255, 255);\n"
                                   "border:2px solid rgb(255, 255, 255);\n"
                                   "border-radius: 5px;\n"
                                   "}\n"
                                   "\n"
                                   "")
        self.Refresh.setObjectName("Refresh")

        self.Delete_Stu = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_Stu.setGeometry(QtCore.QRect(705, 455, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Delete_Stu.setFont(font)
        self.Delete_Stu.setStyleSheet("QPushButton{\n"
                                      "color: rgb(85, 170, 255);\n"
                                      "border:2px solid rgb(85, 170, 255);\n"
                                      "border-radius: 5px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::hover{\n"
                                      "color:  rgb(255, 255, 255);\n"
                                      "border:2px solid rgb(255, 255, 255);\n"
                                      "border-radius: 5px;\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.Delete_Stu.setObjectName("Delete_Stu")

        self.Destroy = QtWidgets.QPushButton(self.centralwidget)
        self.Destroy.setGeometry(QtCore.QRect(705, 490, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Destroy.setFont(font)
        self.Destroy.setStyleSheet("QPushButton{\n"
                                   "color: rgb(85, 170, 255);\n"
                                   "border:2px solid rgb(85, 170, 255);\n"
                                   "border-radius: 5px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton::hover{\n"
                                   "color:  rgb(255, 255, 255);\n"
                                   "border:2px solid rgb(255, 255, 255);\n"
                                   "border-radius: 5px;\n"
                                   "}\n"
                                   "\n"
                                   "")
        self.Destroy.setObjectName("Destroy")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.StopFlag = False

        self.timerADD = QtCore.QTimer()
        self.timerADD.timeout.connect(self.ADD)

        self.timerCAM = QtCore.QTimer()
        self.timerCAM.timeout.connect(self.CAM)

        self.timerEN = QtCore.QTimer()
        self.timerEN.timeout.connect(self.EN)

        self.timerABS = QtCore.QTimer()
        self.timerABS.timeout.connect(self.ABS)

        self.Play_Camera.clicked.connect(self.encode)
        self.Play_Camera.clicked.connect(self.play)

        self.Pause_Camera.clicked.connect(self.pause)
        self.Add_Student.clicked.connect(self.add_stu)
        self.Add_Student.clicked.connect(self.view_stu)
        self.Database_list.clicked.connect(self.selected_text)
        # self.Add_Face.clicked.connect(self.selected_text)
        self.Add_Face.clicked.connect(self.add_face)

        self.Refresh.clicked.connect(self.R)
        self.Delete_Stu.clicked.connect(self.X)
        self.Destroy.clicked.connect(self.D)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto-Attendance"))
        self.Pause_Camera.setText(_translate("MainWindow", "Pause"))
        self.Play_Camera.setText(_translate("MainWindow", "Play"))
        self.Camera.setWhatsThis(_translate(
            "MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Recorded Attendance"))
        self.Name_Entry.setText(_translate("MainWindow", "Enter name"))
        self.Email_Entry.setText(_translate("MainWindow", "Enter email"))
        self.label_3.setText(_translate("MainWindow", "Name :"))
        self.label_4.setText(_translate("MainWindow", "Email :"))
        self.label_5.setText(_translate("MainWindow", "Database "))
        self.Add_Student.setText(_translate("MainWindow", "Add Person"))
        self.Add_Face.setText(_translate("MainWindow", "Add Face"))
        self.label_6.setText(_translate("MainWindow", "Camera "))
        self.label_7.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\">Auto-Attendance</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "By Othman Ayman"))
        self.Updates.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\">Welcome..</p></body></html>"))
        self.Refresh.setText(_translate("MainWindow", "R"))
        self.Delete_Stu.setText(_translate("MainWindow", "X"))
        self.Destroy.setText(_translate("MainWindow", "D"))

    def add_stu(self):
        name = self.Name_Entry.text()
        self.Name_Entry.clear()
        email = self.Email_Entry.text()
        self.Email_Entry.clear()
        db.insert_student(name=name, email=email)
        db.insert_c_s(student=name, course=course)
        text = f'The student {name} has been added successfuly'
        self.update_text(text=text, color='green')

    def view_stu(self):
        self.Database_list.clear()
        r = db.view_students()
        for s in r:
            id = s[0]
            name = s[1]
            email = s[2]
            self.Database_list.addItem(f'{id} {name} ~{email}')

    def view_att(self):
        self.Record.clear()
        r = db.search()
        for s in r:
            id = s[0]
            name = s[1]
            course = s[2]
            present = s[3]
            time_att = str(s[4])

            self.Record.addItem(
                f'{id} {name} -present: {present}- ({time_att}) ')

    def update_text(self, text, color):
        _translate = QtCore.QCoreApplication.translate

        self.Updates.setStyleSheet(f"color: {color};\n"
                                   "border: 2px solid rgb(85, 170, 255);\n"
                                   "border-radius: 5px;\n"
                                   "font: 10pt \"NSimSun\";")
        self.Updates.setText(_translate(
            "MainWindow", f"<html><head/><body><p align=\"center\">{text}</p></body></html>"))

    def selected_text(self):
        try:
            item = self.Database_list.selectedItems()[0].text()
            item = item.split(' ')
            id = item[0]
            names = item[1:-1]
            name = ""
            for i in names:
                name += str(i) + " "
            self.update_text(
                text=f'THE SELECTED STUDENT IS {name} WITH ID {id}', color='white')

            path = f'images\\{id}.jpg'
            self.set_image(path=path)
            return id, name
        except IndexError:

            self.update_text(
                text=f'Please Select Name', color='yellow')
            return None, None

    def ADD(self):
        try:
            ret, frame = self.video_capture.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]
            face_locations = face_recognition.face_locations(
                rgb_small_frame)

            if len(face_locations) == 1:
                # face_encodings = face_recognition.face_encodings(
                #     rgb_small_frame, face_locations)

                path = f"images\\{self.student_id}.jpg"
                cv2.imwrite(path, frame)

                self.set_image(path=path)
                self.video_capture.release()
                # cv2.destroyAllWindows()
                self.update_text(
                    text=f"face added Successfuly!!  for {self.name}", color='green')
                self.timerADD.stop()

            elif len(face_locations) == 0:
                self.update_text(
                    text="THERE IS NO ONE INFRONT CAMERA", color='red')
            else:
                self.update_text(text="There is more than one person infront camer!"
                                 "ONLY ONE PERSON", color='red')
        except Exception as e:
            self.update_text(text=e, color='red')

    def add_face(self):
        try:
            self.student_id, self.name = self.selected_text()
            if self.student_id is None:
                return None

            self.video_capture = cv2.VideoCapture(0)

            self.timerADD.start()

        except Exception as e:
            self.update_text(text=e, color='red')

    def set_image(self, path):
        # path = "images\\2.jpg"
        if os.path.exists(path=path):
            # Setup pixmap with the provided image
            pixmap = QtGui.QPixmap(path)
            pixmap = pixmap.scaled(self.Camera.width(), self.Camera.height(
            ), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
            self.Camera.setPixmap(pixmap)  # Set the pixmap onto the label
            self.Camera.setAlignment(QtCore.Qt.AlignCenter)
        else:
            _translate = QtCore.QCoreApplication.translate
            self.Camera.setText(_translate(
                "MainWindow", "The image is not exist!"))

    def EN(self):
        try:
            n = self.rows
            s = self.r[n]
            self.ids.append(s[0])
            self.names.append(s[1])
            self.emails.append(s[2])

            path = f"images\\{s[0]}.jpg"
            if os.path.exists(path):
                image = face_recognition.load_image_file(f"images\\{s[0]}.jpg")
                en = face_recognition.face_encodings(image)[0]
                self.encoded.append(en)
                self.rows += 1
            else:
                self.update_text(
                    text=f"please add image for ({s[1]}) then try again", color='yellow')

                self.timerCAM.stop()
                self.StopFlag = True
                self.timerEN.stop()

            k = len(self.r)
            if self.rows == k:
                self.update_text(text="Finished Encoding", color='yellow')
                self.timerEN.stop()
                self.update_text(text="Started!!", color='green')

        except Exception as e:
            self.update_text(text=e, color='red')

    def encode(self):
        self.update_text(text="Encoding Students Faces..", color='yellow')
        self.emails = []
        self.ids = []
        self.names = []
        self.encoded = []
        self.r = db.view_students()
        self.rows = 0
        self.timerEN.start()

    def play(self):
        try:
            self.StopFlag = False

            self.video_capture = cv2.VideoCapture(0)

            self.timerCAM.start()

        except Exception as e:
            self.update_text(text=f"play: {e}", color='red')

    def CAM(self):
        k = len(self.r)
        if self.rows == k:

            # try:
            ret, frame = self.video_capture.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]
            face_locations = face_recognition.face_locations(
                rgb_small_frame)
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)

            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(
                    self.encoded, face_encoding)

                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = self.names[first_match_index]
                    id = self.ids[first_match_index]
                    email = self.emails[first_match_index]

                    self.encoded.pop(first_match_index)
                    self.names.pop(first_match_index)
                    self.ids.pop(first_match_index)
                    self.emails.pop(first_match_index)

                    db.insert_attendance(
                        student=name, course=course, present=1)
                    t = str(datetime.now())
                    mail.send(email=email, student=name,
                              subject=course, time=t)
                    self.update_text(
                        text=f"Attendance added and sent email for {name}", color='green')

            self.view_att()
            path = 'cam\\cam.jpg'
            cv2.imwrite(path, frame)
            self.set_image(path=path)
            if self.StopFlag:
                self.video_capture.release()
                self.timerCAM.stop()
            # except Exception as e:
            #     self.update_text(text=f"CAM: {e}", color='red')

    def pause(self):
        if self.StopFlag:
            pass
        else:
            self.StopFlag = True
            self.timerABS.start()

    def ABS(self):
        if self.emails:
            name = self.names[0]
            id = self.ids[0]
            email = self.emails[0]
            self.encoded.pop(0)
            self.names.pop(0)
            self.ids.pop(0)
            self.emails.pop(0)

            db.insert_attendance(
                student=name, course=course, present=0)
            t = str(datetime.now())
            mail.send_abs(email=email, student=name,
                          subject=course, time=t)
            self.update_text(
                text=f"Sent emails for absents Successfully! ", color='green')
        else:
            self.timerABS.stop()

    def R(self):
        self.view_stu()
        self.view_att()

    def D(self):
        try:
            db.destroy()
            self.R()
        except Exception as e:
            self.update_text(text=f"D: {e}", color='red')

    def X(self):
        try:
            self.student_id, self.name = self.selected_text()
            if self.student_id is None:
                self.update_text(
                    'PLEASE SELECT A STUDENT TO DELETE ', 'yellow')
                return None
            db.delete_student(id=self.student_id)
            self.view_stu()

        except Exception as e:
            self.update_text(text=f"X: {e}", color='red')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.view_stu()
    ui.view_att()
    sys.exit(app.exec_())
