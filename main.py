# from PyQt5 import QtCore, QtGui, QtWidgets
# from gui import Ui_MainWindow
#
# import cv2
# import numpy as np
# import face_recognition
# import time
#
#
# def add_face():
#     student_id, name = ui.selected_text()
#
#     ui.update_text(
#         text='please stand infront the Camera without moving', color='yellow')
#
#     time.sleep(5)
#
#     video_capture = cv2.VideoCapture(0)
#     frames = []
#     frames_en = []
#     while True:
#         ret, frame = video_capture.read()
#         small_frame = cv2.resize(
#             frame, (0, 0), fx=0.25, fy=.25, interpolation=None)
#
#         rgb_small_frame = small_frame[:, :, ::-1]
#         face_locations = face_recognition.face_locations(rgb_small_frame)
#
#         if len(face_locations) == 1:
#             # face_encodings = face_recognition.face_encodings(
#             #     rgb_small_frame, face_locations)
#
#             path = 'images\\' + str(student_id) + ".jpg"
#             cv2.imwrite(path, frame)
#
#             ui.set_image(path=frame)
#
#             video_capture.release()
#             # cv2.destroyAllWindows()
#
#         elif len(face_locations) == 0:
#             ui.update_text(
#                 text="THERE IS NO ONE INFRONT CAMERA", color='red')
#         else:
#             ui.update_text(text="There is more than one person infront camer!"
#                            "ONLY ONE PERSON", color='red')
#
#         # print(face_locations)
#
#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#
#     ui.view_stu()
#     ui.Add_Face.clicked.connect(add_face)
#
#     sys.exit(app.exec_())
