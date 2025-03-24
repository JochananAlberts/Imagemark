# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 800)
        MainWindow.setMouseTracking(True)
        MainWindow.setTabletTracking(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.imageLabel = QLabel(self.centralwidget)
        self.imageLabel.setObjectName(u"imageLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setMinimumSize(QSize(400, 400))
        self.imageLabel.setStyleSheet(u"border: 1px solid gray;")

        self.horizontalLayout.addWidget(self.imageLabel)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.LoadImage = QPushButton(self.centralwidget)
        self.LoadImage.setObjectName(u"LoadImage")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LoadImage.sizePolicy().hasHeightForWidth())
        self.LoadImage.setSizePolicy(sizePolicy1)
        self.LoadImage.setMinimumSize(QSize(300, 0))

        self.verticalLayout.addWidget(self.LoadImage)

        self.SaveImage = QPushButton(self.centralwidget)
        self.SaveImage.setObjectName(u"SaveImage")

        self.verticalLayout.addWidget(self.SaveImage)

        self.Spacer = QSpacerItem(300, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.Spacer)

        self.Watermark = QLineEdit(self.centralwidget)
        self.Watermark.setObjectName(u"Watermark")

        self.verticalLayout.addWidget(self.Watermark)

        self.TextSize = QSlider(self.centralwidget)
        self.TextSize.setObjectName(u"TextSize")
        self.TextSize.setMinimum(10)
        self.TextSize.setMaximum(50)
        self.TextSize.setSliderPosition(20)
        self.TextSize.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.TextSize)

        self.UpButton = QPushButton(self.centralwidget)
        self.UpButton.setObjectName(u"UpButton")

        self.verticalLayout.addWidget(self.UpButton)

        self.left_right_buttons = QGridLayout()
        self.left_right_buttons.setObjectName(u"left_right_buttons")
        self.DownButton = QPushButton(self.centralwidget)
        self.DownButton.setObjectName(u"DownButton")

        self.left_right_buttons.addWidget(self.DownButton, 4, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.LeftButton = QPushButton(self.centralwidget)
        self.LeftButton.setObjectName(u"LeftButton")
        icon = QIcon()
        icon.addFile(u"assets/icons/up.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.LeftButton.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.LeftButton)

        self.RightButton = QPushButton(self.centralwidget)
        self.RightButton.setObjectName(u"RightButton")

        self.horizontalLayout_3.addWidget(self.RightButton)


        self.left_right_buttons.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.left_right_buttons)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PictureMark", None))
        self.imageLabel.setText("")
        self.LoadImage.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.SaveImage.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.Watermark.setText("")
        self.Watermark.setPlaceholderText("Watermark")
        self.UpButton.setText("Up")
        self.DownButton.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.LeftButton.setText("Left")
        self.RightButton.setText(QCoreApplication.translate("MainWindow", u"Right", None))
    # retranslateUi

