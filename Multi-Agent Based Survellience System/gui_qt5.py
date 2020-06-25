from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog
import yolo_setup as YOLO
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 500)
        MainWindow.setMinimumSize(QtCore.QSize(900, 500))
        MainWindow.setMaximumSize(QtCore.QSize(900, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        MainWindow.setIconSize(QtCore.QSize(48, 48))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.leftSideBarWidget = QtWidgets.QWidget(self.centralwidget)
        self.leftSideBarWidget.setGeometry(QtCore.QRect(0, 0, 221, 511))
        self.leftSideBarWidget.setStyleSheet("background-color: rgb(0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font: 75 italic 18pt \"Yu Gothic UI\";")
        self.leftSideBarWidget.setObjectName("leftSideBarWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.leftSideBarWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 224, 404))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.leftSideBarVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.leftSideBarVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftSideBarVerticalLayout.setObjectName("leftSideBarVerticalLayout")
        #self.label_Logo_Image = QtWidgets.QLabel(self.verticalLayoutWidget)
        #self.label_Logo_Image.setText("")
        #self.label_Logo_Image.setPixmap(QtGui.QPixmap("logo1.png"))
        #self.label_Logo_Image.setContentsMargins(0,15,0,0)
        #self.label_Logo_Image.setAlignment(QtCore.Qt.AlignCenter)
        #self.label_Logo_Image.setObjectName("label_Logo_Image")
        #self.leftSideBarVerticalLayout.addWidget(self.label_Logo_Image)
        self.btnOpenVideo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.btnOpenVideo.sizePolicy().hasHeightForWidth())
        #self.btnOpenVideo.setSizePolicy(sizePolicy)
        self.btnOpenVideo.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon1 = QtGui.QIcon()
        #icon1.addPixmap(QtGui.QPixmap(":/icon/video_icon_.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOpenVideo.setIcon(icon1)
        self.btnOpenVideo.setIconSize(QtCore.QSize(40, 40))
        self.btnOpenVideo.setCheckable(False)
        self.btnOpenVideo.setObjectName("btnOpenVideo")
        self.leftSideBarVerticalLayout.addWidget(self.btnOpenVideo)
        #self.btnOpenCamera = QtWidgets.QPushButton(self.verticalLayoutWidget)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.btnOpenCamera.sizePolicy().hasHeightForWidth())
        #self.btnOpenCamera.setSizePolicy(sizePolicy)
        #self.btnOpenCamera.setLayoutDirection(QtCore.Qt.LeftToRight)
        #icon2 = QtGui.QIcon()
        #icon2.addPixmap(QtGui.QPixmap(":/icon/cam_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.btnOpenCamera.setIcon(icon2)
        #self.btnOpenCamera.setIconSize(QtCore.QSize(40, 40))
        #self.btnOpenCamera.setObjectName("btnOpenCamera")
        #self.leftSideBarVerticalLayout.addWidget(self.btnOpenCamera)
        self.btnPredict = QtWidgets.QPushButton(self.verticalLayoutWidget)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.btnPredict.sizePolicy().hasHeightForWidth())
        #self.btnPredict.setSizePolicy(sizePolicy)
        self.btnPredict.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon3 = QtGui.QIcon()
        #icon3.addPixmap(QtGui.QPixmap(":/icon/predict_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPredict.setIcon(icon3)
        self.btnPredict.setIconSize(QtCore.QSize(40, 40))
        self.btnPredict.setObjectName("btnPredict")
        self.leftSideBarVerticalLayout.addWidget(self.btnPredict)
        #self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        #self.pushButton_7.setEnabled(True)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        #self.pushButton_7.setSizePolicy(sizePolicy)
        #self.pushButton_7.setText("")
        #self.pushButton_7.setObjectName("pushButton_7")
        #self.leftSideBarVerticalLayout.addWidget(self.pushButton_7)
        #self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        #self.pushButton_6.setSizePolicy(sizePolicy)
        #self.pushButton_6.setText("")
        #self.pushButton_6.setObjectName("pushButton_6")
        #self.leftSideBarVerticalLayout.addWidget(self.pushButton_6)
        #self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        #self.pushButton_5.setSizePolicy(sizePolicy)
        #self.pushButton_5.setText("")
        #self.pushButton_5.setObjectName("pushButton_5")
        #self.leftSideBarVerticalLayout.addWidget(self.pushButton_5)
        #self.footerWidget = QtWidgets.QWidget(self.centralwidget)
        #self.footerWidget.setGeometry(QtCore.QRect(10, 420, 891, 81))
        #self.footerWidget.setStyleSheet("background-color: rgb(0, 0, 0);\n"
         #   "color: rgb(255, 255, 255);\n"
          #  "font: 75 italic 18pt \"Yu Gothic UI\";\n"
           # "border:2px dashed;\n"
            #"border-top-color: rgb(255, 255, 0);")
        #self.footerWidget.setObjectName("footerWidget")
        #self.horizontalLayoutWidget = QtWidgets.QWidget(self.footerWidget)
        #self.horizontalLayoutWidget.setGeometry(QtCore.QRect(210, 10, 661, 61))
        #self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        #self.footerHorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        #self.footerHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        #self.footerHorizontalLayout.setObjectName("footerHorizontalLayout")
        #self.labelActivity = QtWidgets.QLabel(self.horizontalLayoutWidget)
        #self.labelActivity.setStyleSheet("border:0px;\n"
         #   "font: 63 10pt \"Yu Gothic UI Semibold\";")
        #self.labelActivity.setObjectName("labelActivity")
        #self.footerHorizontalLayout.addWidget(self.labelActivity)
        #self.LabelActivityName = QtWidgets.QLabel(self.horizontalLayoutWidget)
        #self.LabelActivityName.setStyleSheet("border:0px;\n"
         #   "font: 63 10pt \"Yu Gothic UI Semibold\";")
        #self.LabelActivityName.setText("")
        #self.LabelActivityName.setObjectName("LabelActivityName")
        #self.footerHorizontalLayout.addWidget(self.LabelActivityName)
        #self.LabelConfidence = QtWidgets.QLabel(self.horizontalLayoutWidget)
        #font = QtGui.QFont()
        #font.setFamily("Yu Gothic UI Semibold")
        #font.setPointSize(10)
        #font.setBold(False)
        #font.setItalic(False)
        #font.setWeight(7)
        #self.LabelConfidence.setFont(font)
        #self.LabelConfidence.setStyleSheet("border:0px;\n"
        #    "font: 63 10pt \"Yu Gothic UI Semibold\";")
        #self.LabelConfidence.setObjectName("LabelConfidence")
        #self.footerHorizontalLayout.addWidget(self.LabelConfidence)
        #self.LabelConfidenceValue = QtWidgets.QLabel(self.horizontalLayoutWidget)
        #self.LabelConfidenceValue.setStyleSheet("border:0px;\n"
        #    "font: 63 10pt \"Yu Gothic UI Semibold\";")
        #self.LabelConfidenceValue.setText("")
        #self.LabelConfidenceValue.setObjectName("LabelConfidenceValue")
        #self.footerHorizontalLayout.addWidget(self.LabelConfidenceValue)
        self.LabelVideoPlayer = QtWidgets.QLabel(self.centralwidget)
        self.LabelVideoPlayer.setGeometry(QtCore.QRect(240, 10, 631, 391))
        self.LabelVideoPlayer.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelVideoPlayer.setObjectName("LabelVideoPlayer")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnOpenVideo.clicked.connect(self.browse_video)
        self.btnPredict.clicked.connect(self.predict_video)
        #self.btnOpenCamera.clicked.connect(self.open_camera)
        self.video_path = ""
        self.prediction = ""
        self.confidence = 0
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Multi-Agent Based Surveillence System"))
        self.btnOpenVideo.setText(_translate("MainWindow", "Select a Video "))
        #self.btnOpenCamera.setText(_translate("MainWindow", "Open Camera"))
        self.btnPredict.setText(_translate("MainWindow", "Start          "))
        #self.labelActivity.setText(_translate("MainWindow", "Performance:"))
        #self.LabelConfidence.setText(_translate("MainWindow", "Accuracy Rate:"))
        self.LabelVideoPlayer.setText(_translate("MainWindow", "Open Video"))
    def get_prediction(self):
        YOLO.video_prediction(self.video_path)
        # self.prediction, self.confidence = Predictor.test(self.video_path)
        print("Prediction Completed")
    def browse_video(self):
        video_path = QFileDialog.getOpenFileName(None,'Select Video','',"Video file(*.mp4 *.avi *.MOV)", None, QFileDialog.DontUseNativeDialog)
        if not(video_path[0]):
            return
        self.video_path = str(video_path[0])
        print(self.video_path)
        # video_loading_thread = Thread(target=self.get_prediction, args=[])
        # video_loading_thread.start()

        cap = cv2.VideoCapture(self.video_path)
        ret, frame = cap.read()
        cv2.imwrite("./Thumbnail.png", frame)
        cv2.imwrite("./frame.jpg", frame)
        pixmap = QtGui.QPixmap("./Thumbnail.png")
        pixmap = pixmap.scaled(pixmap.width(), pixmap.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.LabelVideoPlayer.setPixmap(pixmap)
        cap.release()
    def predict_video(self):
        if (self.video_path != None or self.videopath != ""):
            video_loading_thread = Thread(target=self.get_prediction, args=[])
            video_loading_thread.start()
        else:
            print("No Video File Selected")
    def open_camera(self):
        video_loading_thread = Thread(target=YOLO.camera_prediction, args=[])
        video_loading_thread.start()
    	# cam = cv2.VideoCapture(0)
    	# while (True):
    	# 	ret_val, img = cam.read()
    	# 	if ret_val:
    	# 		cv2.imshow('Laptop Camera', img)
    	# 	if (cv2.waitKey(1) == 27):
    	# 		break  # esc to quit
    	# cv2.destroyAllWindows()

import resources_pyqt5

# import setup as Predictor
from threading import Thread
import cv2
import time
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    palette = QPalette()
    palette.setColor(QPalette.ButtonText, Qt.red)
    app.setPalette(palette)
    app.setStyle('Windows')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

