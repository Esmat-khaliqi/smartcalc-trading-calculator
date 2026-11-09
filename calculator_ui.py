# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculate_kh.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        if not Calculator.objectName():
            Calculator.setObjectName(u"Calculator")
        Calculator.resize(1200, 851)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Calculator.sizePolicy().hasHeightForWidth())
        Calculator.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"icon_128.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Calculator.setWindowIcon(icon)
        self.centralwidget = QWidget(Calculator)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_22 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        self.page.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(self.page)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 79))
        self.frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame.setStyleSheet(u"background-color: #101214;\n"
"border:0px;\n"
"border-bottom:1px solid #2E2F32;\n"
"border-right:1px solid #2E2F32;\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setMinimumSize(QSize(40, 40))
        self.label_14.setBaseSize(QSize(0, 0))
        self.label_14.setStyleSheet(u"background-color:#4A8DF5;\n"
"border: 1px solid transparent; \n"
"border-radius: 6px;")
        self.label_14.setPixmap(QPixmap(u":/icons/icons/calculator_white.svg"))
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_14, 1, 1, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border:0px;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(2, 9)

        self.verticalLayout.addWidget(self.frame)

        self.sidebar_widget = QFrame(self.page)
        self.sidebar_widget.setObjectName(u"sidebar_widget")
        sizePolicy.setHeightForWidth(self.sidebar_widget.sizePolicy().hasHeightForWidth())
        self.sidebar_widget.setSizePolicy(sizePolicy)
        self.sidebar_widget.setStyleSheet(u"background-color: #101214;\n"
"border:0px;\n"
"border-right:1px solid #2E2F32;\n"
"")
        self.sidebar_widget.setFrameShape(QFrame.Shape.StyledPanel)
        self.sidebar_widget.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.sidebar_widget)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 15, 0, 0)
        self.label_2 = QLabel(self.sidebar_widget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(8)
        font1.setWeight(QFont.Medium)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(False)
        font1.setHintingPreference(QFont.PreferDefaultHinting)
        self.label_2.setFont(font1)
        self.label_2.setAcceptDrops(False)
        self.label_2.setStyleSheet(u"margin-left:25px;\n"
"color: #9d9ea2;\n"
"border:0px;")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(False)

        self.verticalLayout_4.addWidget(self.label_2)

        self.calculator_widget = QFrame(self.sidebar_widget)
        self.calculator_widget.setObjectName(u"calculator_widget")
        self.calculator_widget.setMinimumSize(QSize(215, 47))
        self.calculator_widget.setMaximumSize(QSize(315, 47))
        self.calculator_widget.setStyleSheet(u"QFrame#calculator_widget {\n"
"    background: rgba(59, 130, 246, 0.15);\n"
"    border: 1px solid transparent; \n"
"    border-radius: 6px;\n"
"    color: #3b82f6;\n"
"    padding: 8px 12px;\n"
"    margin-right: 15px;\n"
"    margin-left: 15px;\n"
"}\n"
"")
        self.calculator_widget.setFrameShape(QFrame.Shape.StyledPanel)
        self.calculator_widget.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.calculator_widget)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.calculator_icon = QLabel(self.calculator_widget)
        self.calculator_icon.setObjectName(u"calculator_icon")
        self.calculator_icon.setMaximumSize(QSize(500, 500))
        self.calculator_icon.setStyleSheet(u"background-color: transparent;\n"
"border:0px;")
        self.calculator_icon.setPixmap(QPixmap(u":/icons/icons/calculator.svg"))

        self.horizontalLayout_6.addWidget(self.calculator_icon)

        self.label_4 = QLabel(self.calculator_widget)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setFamilies([u"Microsoft Sans Serif"])
        font2.setPointSize(11)
        font2.setKerning(True)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"background-color: transparent;\n"
"border:0px;\n"
"padding:5px 0px")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.calculat_arrow = QLabel(self.calculator_widget)
        self.calculat_arrow.setObjectName(u"calculat_arrow")
        self.calculat_arrow.setMaximumSize(QSize(10, 8))
        self.calculat_arrow.setStyleSheet(u"background-color: transparent;\n"
"border:0px;\n"
"")
        self.calculat_arrow.setPixmap(QPixmap(u":/icons/icons/chevron-right.svg"))
        self.calculat_arrow.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.calculat_arrow)

        self.horizontalLayout_6.setStretch(1, 9)

        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addWidget(self.calculator_widget)

        self.trading_widget = QFrame(self.sidebar_widget)
        self.trading_widget.setObjectName(u"trading_widget")
        self.trading_widget.setMinimumSize(QSize(215, 47))
        self.trading_widget.setMaximumSize(QSize(315, 47))
        self.trading_widget.setStyleSheet(u"QFrame#trading_widget {\n"
"    background: rgba(59, 130, 246, 0.15);\n"
"    border: 1px solid transparent; \n"
"    border-radius: 6px;\n"
"    color: #3b82f6;\n"
"    padding: 8px 12px;\n"
"    margin-right: 15px;\n"
"    margin-left: 15px;\n"
"}\n"
"")
        self.trading_widget.setFrameShape(QFrame.Shape.StyledPanel)
        self.trading_widget.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.trading_widget)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.trade_icon = QLabel(self.trading_widget)
        self.trade_icon.setObjectName(u"trade_icon")
        self.trade_icon.setStyleSheet(u"background-color: transparent;\n"
"border:0px;")
        self.trade_icon.setPixmap(QPixmap(u":/icons/icons/trending-up.svg"))

        self.horizontalLayout_5.addWidget(self.trade_icon)

        self.label_8 = QLabel(self.trading_widget)
        self.label_8.setObjectName(u"label_8")
        font3 = QFont()
        font3.setFamilies([u"Microsoft Sans Serif"])
        font3.setPointSize(11)
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"background-color: transparent;\n"
"border:0px;\n"
"padding:5px 0px")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.trade_arrow = QLabel(self.trading_widget)
        self.trade_arrow.setObjectName(u"trade_arrow")
        self.trade_arrow.setMaximumSize(QSize(10, 8))
        self.trade_arrow.setStyleSheet(u"background-color: transparent;\n"
"border:0px;")
        self.trade_arrow.setPixmap(QPixmap(u":/icons/icons/chevron-right.svg"))
        self.trade_arrow.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.trade_arrow)

        self.horizontalLayout_5.setStretch(1, 9)

        self.horizontalLayout_8.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addWidget(self.trading_widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.line = QFrame(self.sidebar_widget)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 1))
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setStyleSheet(u"background-color: rgb(47, 48, 51);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.setting_widget = QFrame(self.sidebar_widget)
        self.setting_widget.setObjectName(u"setting_widget")
        self.setting_widget.setStyleSheet(u"QFrame#setting_widget {\n"
"    background: rgba(59, 130, 246, 0.15);\n"
"    border: 1px solid transparent; \n"
"    border-radius: 6px;\n"
"    color: #3b82f6;\n"
"    padding: 8px  12px;\n"
"    margin-right: 15px;\n"
"    margin-left: 15px;\n"
"	margin-bottom:  20px;\n"
"}\n"
"")
        self.setting_widget.setFrameShape(QFrame.Shape.StyledPanel)
        self.setting_widget.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.setting_widget)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.label_13 = QLabel(self.setting_widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"background-color: transparent;\n"
"border:0px;")
        self.label_13.setPixmap(QPixmap(u":/icons/icons/settings-2.svg"))

        self.horizontalLayout_11.addWidget(self.label_13)

        self.label_12 = QLabel(self.setting_widget)
        self.label_12.setObjectName(u"label_12")
        font4 = QFont()
        font4.setPointSize(11)
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"background-color: transparent;\n"
"border:0px;")

        self.horizontalLayout_11.addWidget(self.label_12)

        self.horizontalLayout_11.setStretch(1, 9)

        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)


        self.verticalLayout_4.addWidget(self.setting_widget)

        self.verticalLayout_4.setStretch(3, 9)

        self.verticalLayout.addWidget(self.sidebar_widget)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 9)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(0, 79))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setStyleSheet(u"background-color: #0a0b0d;\n"
"border:0px;\n"
"border-bottom:1px solid #2E2F32;\n"
"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(20, 10, 20, 10)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(20, -1, -1, -1)
        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"border:0px;\n"
"border-radius:0px;\n"
"color: rgb(157, 158, 162);")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.path_arrow = QLabel(self.frame_3)
        self.path_arrow.setObjectName(u"path_arrow")
        self.path_arrow.setMinimumSize(QSize(5, 5))
        self.path_arrow.setMaximumSize(QSize(10, 8))
        font5 = QFont()
        font5.setPointSize(9)
        self.path_arrow.setFont(font5)
        self.path_arrow.setStyleSheet(u"border:0px;\n"
"border-radius:0px;")
        self.path_arrow.setPixmap(QPixmap(u":/icons/icons/chevron-right_grey.svg"))
        self.path_arrow.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.path_arrow)

        self.path_name = QLabel(self.frame_3)
        self.path_name.setObjectName(u"path_name")
        font6 = QFont()
        font6.setBold(True)
        self.path_name.setFont(font6)
        self.path_name.setStyleSheet(u"border:0px;\n"
"border-radius:0px;")

        self.horizontalLayout_9.addWidget(self.path_name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(10, 11, 13);\n"
"border:0px;")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.frame_4)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.calculator_mashien_section = QWidget()
        self.calculator_mashien_section.setObjectName(u"calculator_mashien_section")
        self.horizontalLayout_21 = QHBoxLayout(self.calculator_mashien_section)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.calculator_mashien_section)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(200, 0, 350, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 40, -1, -1)
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font6)
        self.label_15.setStyleSheet(u"color: rgb(74, 141, 245);")

        self.verticalLayout_3.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")
        font7 = QFont()
        font7.setPointSize(20)
        font7.setBold(True)
        self.label_16.setFont(font7)

        self.verticalLayout_3.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"color:#9d9ea2;\n"
"margin-bottom:10px;")

        self.verticalLayout_3.addWidget(self.label_17)

        self.calculat_section = QFrame(self.frame_2)
        self.calculat_section.setObjectName(u"calculat_section")
        self.calculat_section.setStyleSheet(u"QFrame#calculat_section {\n"
"		background-color: rgb(22, 23, 25);\n"
"		border:1px solid #2f3033;\n"
"		border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton ,QLabel ,QLineEdit{\n"
"		background-color: transparent;\n"
"}\n"
"\n"
"QPushButton  {\n"
"		padding:20px 0px;\n"
"		border:1px solid #2f3033;\n"
"		border-radius: 4px;\n"
"		font-size:15px;\n"
"		font-weight: 900;\n"
"}\n"
"\n"
"QPushButton#btn_plus,#btn_minus,#btn_multiply,#btn_divide,#btn_equal  {\n"
"		background-color:#1e2124;\n"
"		border:0px;\n"
"		color:rgba(74, 141, 245, 1);\n"
"}\n"
"\n"
"\n"
"QPushButton#btn_equal  {\n"
"		background-color:rgba(74, 141, 245, 1);\n"
"		color:	#fff ;\n"
"}")
        self.calculat_section.setFrameShape(QFrame.Shape.StyledPanel)
        self.calculat_section.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.calculat_section)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 15)
        self.label_18 = QLabel(self.calculat_section)
        self.label_18.setObjectName(u"label_18")
        font8 = QFont()
        font8.setPointSize(8)
        font8.setBold(True)
        self.label_18.setFont(font8)
        self.label_18.setStyleSheet(u"padding-top:30px;\n"
"padding-left:30px;\n"
"color: rgb(157, 158, 162);")
        self.label_18.setTextFormat(Qt.TextFormat.AutoText)

        self.verticalLayout_6.addWidget(self.label_18)

        self.result_bar = QLabel(self.calculat_section)
        self.result_bar.setObjectName(u"result_bar")
        self.result_bar.setMinimumSize(QSize(0, 30))
        self.result_bar.setMaximumSize(QSize(16777215, 30))
        font9 = QFont()
        font9.setFamilies([u"Microsoft Sans Serif"])
        font9.setPointSize(12)
        font9.setBold(False)
        self.result_bar.setFont(font9)
        self.result_bar.setStyleSheet(u"padding:0px 20px;")
        self.result_bar.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_6.addWidget(self.result_bar)

        self.user_value = QLineEdit(self.calculat_section)
        self.user_value.setObjectName(u"user_value")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.user_value.sizePolicy().hasHeightForWidth())
        self.user_value.setSizePolicy(sizePolicy3)
        font10 = QFont()
        font10.setPointSize(30)
        font10.setBold(False)
        font10.setKerning(True)
        self.user_value.setFont(font10)
        self.user_value.setStyleSheet(u"padding:0px 20px;\n"
"padding-bottom:20px;")
        self.user_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_6.addWidget(self.user_value)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(15)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(15, -1, 15, -1)
        self.btn_multiply = QPushButton(self.calculat_section)
        self.btn_multiply.setObjectName(u"btn_multiply")
        self.btn_multiply.setStyleSheet(u"#btn_multiply:hover{background: rgba(59, 130, 246, 0.15);}")

        self.gridLayout_4.addWidget(self.btn_multiply, 1, 3, 1, 1)

        self.num_6 = QPushButton(self.calculat_section)
        self.num_6.setObjectName(u"num_6")
        self.num_6.setStyleSheet(u"#num_6:hover{\n"
"background: rgba(59, 130, 246, 0.15);\n"
"}")

        self.gridLayout_4.addWidget(self.num_6, 2, 2, 1, 1)

        self.clear_btn = QPushButton(self.calculat_section)
        self.clear_btn.setObjectName(u"clear_btn")
        font11 = QFont()
        font11.setWeight(QFont.Black)
        self.clear_btn.setFont(font11)
        self.clear_btn.setStyleSheet(u"#clear_btn{\n"
"color: rgb(249, 65, 68);\n"
"}\n"
"#clear_btn:hover{\n"
"background: rgba(59, 130, 246, 0.15);\n"
"}")

        self.gridLayout_4.addWidget(self.clear_btn, 0, 0, 1, 1)

        self.num_5 = QPushButton(self.calculat_section)
        self.num_5.setObjectName(u"num_5")
        self.num_5.setStyleSheet(u"#num_5:hover{\n"
"background: rgba(59, 130, 246, 0.15);\n"
"}")

        self.gridLayout_4.addWidget(self.num_5, 2, 1, 1, 1)

        self.btn_minus = QPushButton(self.calculat_section)
        self.btn_minus.setObjectName(u"btn_minus")
        self.btn_minus.setStyleSheet(u"#btn_minus:hover{background: rgba(59, 130, 246, 0.15);}")

        self.gridLayout_4.addWidget(self.btn_minus, 2, 3, 1, 1)

        self.btn_decimal = QPushButton(self.calculat_section)
        self.btn_decimal.setObjectName(u"btn_decimal")
        self.btn_decimal.setStyleSheet(u"#btn_decimal:hover{\n"
"background: rgba(59, 130, 246, 0.15);\n"
"}")

        self.gridLayout_4.addWidget(self.btn_decimal, 4, 2, 1, 1)

        self.num_2 = QPushButton(self.calculat_section)
        self.num_2.setObjectName(u"num_2")
        self.num_2.setStyleSheet(u"#num_2:hover{\n"
"background: rgba(59, 130, 246, 0.15);\n"
"}")

        self.gridLayout_4.addWidget(self.num_2, 3, 1, 1, 1)

        self.num_1 = QPushButton(self.calculat_section)
        self.num_1.setObjectName(u"num_1")
        self.num_1.setStyleSheet(u"#num_1:hover{\n"
"background: rgba(59, 130, 246, 0.15);\n"
"}")

        self.gridLayout_4.addWidget(self.num_1, 3, 0, 1, 1)

        self.backs_btn = QPushButton(self.calculat_section)
        self.backs_btn.setObjectName(u"backs_btn")
        self.backs_btn.setStyleSheet(u"#backs_btn:hover{\n"
"background: rgba(59, 130, 246, 0.15);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/delete.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backs_btn.setIcon(icon1)

        self.gridLayout_4.addWidget(self.backs_btn, 0, 1, 1, 1)

        self.btn_divide = QPushButton(self.calculat_section)
        self.btn_divide.setObjectName(u"btn_divide")
        self.btn_divide.setFont(font11)
        self.btn_divide.setStyleSheet(u"#btn_divide:hover{background: rgba(59, 130, 246, 0.15);}")

        self.gridLayout_4.addWidget(self.btn_divide, 0, 3, 1, 1)

        self.btn_percent = QPushButton(self.calculat_section)
        self.btn_percent.setObjectName(u"btn_percent")
        self.btn_percent.setFont(font11)
        self.btn_percent.setStyleSheet(u"#btn_percent:hover{\n"
"background: rgba(59, 130, 246, 0.15);\n"
"}")

        self.gridLayout_4.addWidget(self.btn_percent, 0, 2, 1, 1)

        self.btn_minus_plus = QPushButton(self.calculat_section)
        self.btn_minus_plus.setObjectName(u"btn_minus_plus")
        self.btn_minus_plus.setStyleSheet(u"#btn_minus_plus:hover{\n"
"background: rgba(59, 130, 246, 0.15);\n"
"}")

        self.gridLayout_4.addWidget(self.btn_minus_plus, 4, 0, 1, 1)

        self.num_9 = QPushButton(self.calculat_section)
        self.num_9.setObjectName(u"num_9")
        self.num_9.setStyleSheet(u"#num_9:hover{\n"
"background: rgba(59, 130, 246, 0.15);\n"
"}")

        self.gridLayout_4.addWidget(self.num_9, 1, 2, 1, 1)

        self.btn_plus = QPushButton(self.calculat_section)
        self.btn_plus.setObjectName(u"btn_plus")
        self.btn_plus.setStyleSheet(u"#btn_plus:hover{background: rgba(59, 130, 246, 0.15);}")

        self.gridLayout_4.addWidget(self.btn_plus, 3, 3, 1, 1)

        self.num_8 = QPushButton(self.calculat_section)
        self.num_8.setObjectName(u"num_8")
        self.num_8.setStyleSheet(u"#num_8:hover{\n"
"background: rgba(59, 130, 246, 0.15);\n"
"}")

        self.gridLayout_4.addWidget(self.num_8, 1, 1, 1, 1)

        self.num_0 = QPushButton(self.calculat_section)
        self.num_0.setObjectName(u"num_0")
        self.num_0.setStyleSheet(u"#num_0:hover{\n"
"background: rgba(59, 130, 246, 0.15);\n"
"}")

        self.gridLayout_4.addWidget(self.num_0, 4, 1, 1, 1)

        self.num_3 = QPushButton(self.calculat_section)
        self.num_3.setObjectName(u"num_3")
        self.num_3.setStyleSheet(u"#num_3:hover{\n"
"background: rgba(59, 130, 246, 0.15);\n"
"}")

        self.gridLayout_4.addWidget(self.num_3, 3, 2, 1, 1)

        self.num_4 = QPushButton(self.calculat_section)
        self.num_4.setObjectName(u"num_4")
        self.num_4.setStyleSheet(u"#num_4:hover{\n"
"background: rgba(59, 130, 246, 0.15);\n"
"}")

        self.gridLayout_4.addWidget(self.num_4, 2, 0, 1, 1)

        self.btn_equal = QPushButton(self.calculat_section)
        self.btn_equal.setObjectName(u"btn_equal")
        self.btn_equal.setStyleSheet(u"#btn_equal:hover{background: rgba(59, 130, 246, 0.15);}")

        self.gridLayout_4.addWidget(self.btn_equal, 4, 3, 1, 1)

        self.num_7 = QPushButton(self.calculat_section)
        self.num_7.setObjectName(u"num_7")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.num_7.sizePolicy().hasHeightForWidth())
        self.num_7.setSizePolicy(sizePolicy4)
        self.num_7.setStyleSheet(u"#num_7:hover{\n"
"background: rgba(59, 130, 246, 0.15);\n"
"}")

        self.gridLayout_4.addWidget(self.num_7, 1, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_4)

        self.verticalLayout_6.setStretch(3, 4)

        self.horizontalLayout_3.addLayout(self.verticalLayout_6)


        self.verticalLayout_3.addWidget(self.calculat_section)

        self.label_20 = QLabel(self.frame_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"padding-top:10px;\n"
"padding-bottom:30px;\n"
"color:#9d9ea2;")

        self.verticalLayout_3.addWidget(self.label_20)

        self.verticalLayout_3.setStretch(3, 9)

        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.horizontalLayout_21.addWidget(self.frame_2)

        self.stackedWidget_2.addWidget(self.calculator_mashien_section)
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.verticalLayout_22 = QVBoxLayout(self.setting_page)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_29 = QFrame(self.setting_page)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(500, 500))
        self.frame_29.setMaximumSize(QSize(16777215, 16777215))
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_29)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(200, 39, 450, 0)
        self.label_41 = QLabel(self.frame_29)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(0, 0))
        self.label_41.setMaximumSize(QSize(16777215, 50))
        font12 = QFont()
        font12.setFamilies([u"Microsoft Sans Serif"])
        font12.setPointSize(8)
        font12.setBold(True)
        self.label_41.setFont(font12)
        self.label_41.setStyleSheet(u"color: rgb(74, 141, 245);letter-spacing: 2px;")

        self.verticalLayout_34.addWidget(self.label_41)

        self.label_52 = QLabel(self.frame_29)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(0, 48))
        self.label_52.setMaximumSize(QSize(16777215, 37))
        font13 = QFont()
        font13.setPointSize(25)
        font13.setWeight(QFont.DemiBold)
        self.label_52.setFont(font13)
        self.label_52.setStyleSheet(u"")
        self.label_52.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_34.addWidget(self.label_52)

        self.label_40 = QLabel(self.frame_29)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(0, 37))
        self.label_40.setMaximumSize(QSize(16777215, 36))
        font14 = QFont()
        font14.setFamilies([u"Microsoft Sans Serif"])
        font14.setPointSize(10)
        font14.setWeight(QFont.Medium)
        self.label_40.setFont(font14)
        self.label_40.setStyleSheet(u"color: rgb(157, 158, 162);\n"
"letter-spacing: 1px;\n"
"word-spacing: 2px;\n"
"")

        self.verticalLayout_34.addWidget(self.label_40)

        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"#frame_30{\n"
"background-color: rgb(22, 23, 25);\n"
"border:1px solid #2f3033;\n"
"padding:20px;\n"
"border-radius: 4px;\n"
"margin-top:30px;\n"
"}\n"
"\n"
"\n"
"")
        self.frame_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_30)
        self.verticalLayout_35.setSpacing(10)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_30)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)
        self.label_19.setStyleSheet(u"background-color: transparent;")

        self.verticalLayout_35.addWidget(self.label_19)

        self.label_37 = QLabel(self.frame_30)
        self.label_37.setObjectName(u"label_37")
        font15 = QFont()
        font15.setFamilies([u"Microsoft Sans Serif"])
        font15.setPointSize(10)
        self.label_37.setFont(font15)
        self.label_37.setStyleSheet(u"color: rgb(157, 158, 162);\n"
"margin-bottom:15px ;\n"
"background-color: transparent;\n"
"letter-spacing: 1px;")

        self.verticalLayout_35.addWidget(self.label_37)

        self.line_2 = QFrame(self.frame_30)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 1))
        self.line_2.setMaximumSize(QSize(16777215, 1))
        self.line_2.setStyleSheet(u"background-color: rgb(47, 48, 51);\n"
"\n"
"")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_35.addWidget(self.line_2)

        self.label_39 = QLabel(self.frame_30)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font15)
        self.label_39.setStyleSheet(u"color: rgb(157, 158, 162);\n"
"margin-top:15px ;\n"
"background-color: transparent;\n"
"letter-spacing: 1px;")

        self.verticalLayout_35.addWidget(self.label_39)


        self.verticalLayout_34.addWidget(self.frame_30)

        self.verticalSpacer_7 = QSpacerItem(20, 19, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacer_7)


        self.verticalLayout_22.addWidget(self.frame_29)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_6)

        self.stackedWidget_2.addWidget(self.setting_page)
        self.trading_section = QWidget()
        self.trading_section.setObjectName(u"trading_section")
        self.horizontalLayout_2 = QHBoxLayout(self.trading_section)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.trad_frame = QFrame(self.trading_section)
        self.trad_frame.setObjectName(u"trad_frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.trad_frame.sizePolicy().hasHeightForWidth())
        self.trad_frame.setSizePolicy(sizePolicy5)
        self.trad_frame.setMinimumSize(QSize(0, 0))
        self.trad_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.trad_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.trad_frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.frame_5 = QFrame(self.trad_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(30, 20, 30, 15)
        self.label_21 = QLabel(self.frame_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font15)
        self.label_21.setStyleSheet(u"color: rgb(74, 141, 245);")

        self.verticalLayout_9.addWidget(self.label_21)

        self.label_22 = QLabel(self.frame_5)
        self.label_22.setObjectName(u"label_22")
        font16 = QFont()
        font16.setFamilies([u"Microsoft Sans Serif"])
        font16.setPointSize(20)
        font16.setBold(True)
        self.label_22.setFont(font16)

        self.verticalLayout_9.addWidget(self.label_22)

        self.label_23 = QLabel(self.frame_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font15)
        self.label_23.setStyleSheet(u"color: rgb(157, 158, 162);")

        self.verticalLayout_9.addWidget(self.label_23)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.trad_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(30, -1, 30, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(350, 0))
        self.frame_7.setMaximumSize(QSize(456, 16777215))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 20, 20, 86)
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 400))
        self.frame_9.setMaximumSize(QSize(16777215, 600))
        self.frame_9.setStyleSheet(u"background-color: rgb(22, 23, 25);\n"
"border:1px solid #2f3033;\n"
"border-radius:4px ;")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"border:0px;\n"
"border-bottom:1px solid #2f3033;\n"
"border-radius:0px;")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_15.setSpacing(20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(20, 20, 20, 20)
        self.label_24 = QLabel(self.frame_10)
        self.label_24.setObjectName(u"label_24")
        sizePolicy1.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy1)
        self.label_24.setMinimumSize(QSize(40, 40))
        self.label_24.setMaximumSize(QSize(40, 40))
        self.label_24.setStyleSheet(u"background: rgba(59, 130, 246, 0.15);\n"
"border:0px;\n"
"border-radius:4px;")
        self.label_24.setPixmap(QPixmap(u":/icons/icons/trending-up.svg"))
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_24)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_25 = QLabel(self.frame_10)
        self.label_25.setObjectName(u"label_25")
        font17 = QFont()
        font17.setFamilies([u"Microsoft Sans Serif"])
        font17.setPointSize(11)
        font17.setBold(True)
        self.label_25.setFont(font17)
        self.label_25.setStyleSheet(u"border:0px;")

        self.verticalLayout_11.addWidget(self.label_25)

        self.label_26 = QLabel(self.frame_10)
        self.label_26.setObjectName(u"label_26")
        font18 = QFont()
        font18.setPointSize(10)
        self.label_26.setFont(font18)
        self.label_26.setStyleSheet(u"border:0px;")

        self.verticalLayout_11.addWidget(self.label_26)


        self.horizontalLayout_15.addLayout(self.verticalLayout_11)

        self.horizontalLayout_15.setStretch(1, 1)

        self.verticalLayout_12.addWidget(self.frame_10)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"#frame_12{\n"
"border:0px;\n"
"}\n"
"QFrame QLabel ,QLineEdit{\n"
"border:0px;\n"
"border-radius:0px ;\n"
"}\n"
"\n"
"QLineEdit {\n"
"padding-left:5px;\n"
"}")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_12)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(20, 20, 10, 20)
        self.label_28 = QLabel(self.frame_12)
        self.label_28.setObjectName(u"label_28")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy6)
        self.label_28.setStyleSheet(u"border:0px;\n"
"color:#9d9ea2;\n"
"margin-bottom:10px;\n"
"")

        self.verticalLayout_14.addWidget(self.label_28)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"background-color: rgb(12, 13, 15);")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.frame_14)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(50, 0))
        font19 = QFont()
        font19.setFamilies([u"Microsoft Sans Serif"])
        font19.setPointSize(15)
        self.label_29.setFont(font19)
        self.label_29.setStyleSheet(u"color:#9d9ea2;\n"
"background-color: rgb(12, 13, 15);")
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_29)

        self.acc_b = QLineEdit(self.frame_14)
        self.acc_b.setObjectName(u"acc_b")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.acc_b.sizePolicy().hasHeightForWidth())
        self.acc_b.setSizePolicy(sizePolicy7)
        self.acc_b.setMaximumSize(QSize(16777215, 50))
        self.acc_b.setFont(font19)
        self.acc_b.setStyleSheet(u"background-color: rgb(12, 13, 15);")

        self.horizontalLayout_16.addWidget(self.acc_b)

        self.horizontalLayout_16.setStretch(1, 1)

        self.verticalLayout_14.addWidget(self.frame_14)

        self.label_43 = QLabel(self.frame_12)
        self.label_43.setObjectName(u"label_43")
        sizePolicy6.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy6)
        self.label_43.setStyleSheet(u"border:0px;\n"
"color:#9d9ea2;\n"
"margin-top:20px;\n"
"margin-bottom:10px;")

        self.verticalLayout_14.addWidget(self.label_43)

        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"background-color: rgb(12, 13, 15);")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.frame_15)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(50, 0))
        self.label_42.setFont(font19)
        self.label_42.setStyleSheet(u"color:#9d9ea2;background-color: rgb(12, 13, 15);")
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_42)

        self.entry_p = QLineEdit(self.frame_15)
        self.entry_p.setObjectName(u"entry_p")
        sizePolicy7.setHeightForWidth(self.entry_p.sizePolicy().hasHeightForWidth())
        self.entry_p.setSizePolicy(sizePolicy7)
        self.entry_p.setMaximumSize(QSize(16777215, 50))
        self.entry_p.setFont(font19)
        self.entry_p.setStyleSheet(u"background-color: rgb(12, 13, 15);")

        self.horizontalLayout_24.addWidget(self.entry_p)

        self.horizontalLayout_24.setStretch(1, 1)

        self.verticalLayout_14.addWidget(self.frame_15)

        self.label_45 = QLabel(self.frame_12)
        self.label_45.setObjectName(u"label_45")
        sizePolicy6.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy6)
        self.label_45.setStyleSheet(u"border:0px;\n"
"color:#9d9ea2;\n"
"margin-bottom:10px;\n"
"margin-top:20px;")

        self.verticalLayout_14.addWidget(self.label_45)

        self.frame_16 = QFrame(self.frame_12)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"background-color: rgb(12, 13, 15);\n"
"")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.frame_16)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(50, 0))
        self.label_44.setFont(font19)
        self.label_44.setStyleSheet(u"color:#9d9ea2;background-color: rgb(12, 13, 15);")
        self.label_44.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_44)

        self.tp = QLineEdit(self.frame_16)
        self.tp.setObjectName(u"tp")
        sizePolicy7.setHeightForWidth(self.tp.sizePolicy().hasHeightForWidth())
        self.tp.setSizePolicy(sizePolicy7)
        self.tp.setMaximumSize(QSize(16777215, 50))
        self.tp.setFont(font19)
        self.tp.setStyleSheet(u"background-color: rgb(12, 13, 15);")

        self.horizontalLayout_25.addWidget(self.tp)

        self.horizontalLayout_25.setStretch(1, 1)

        self.verticalLayout_14.addWidget(self.frame_16)


        self.horizontalLayout_14.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"#frame_13{\n"
"border:0px;\n"
"}\n"
"QFrame QLabel ,QLineEdit{\n"
"border:0px;\n"
"border-radius:0px ;\n"
"}\n"
"\n"
"QLineEdit {\n"
"padding-left:5px;\n"
"}")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_13)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 20, 20, 20)
        self.label_47 = QLabel(self.frame_13)
        self.label_47.setObjectName(u"label_47")
        sizePolicy6.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy6)
        self.label_47.setStyleSheet(u"border:0px;\n"
"color:#9d9ea2;\n"
"margin-bottom:10px;\n"
"")

        self.verticalLayout_15.addWidget(self.label_47)

        self.frame_17 = QFrame(self.frame_13)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"background-color: rgb(12, 13, 15);")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.risk_percent = QLineEdit(self.frame_17)
        self.risk_percent.setObjectName(u"risk_percent")
        sizePolicy7.setHeightForWidth(self.risk_percent.sizePolicy().hasHeightForWidth())
        self.risk_percent.setSizePolicy(sizePolicy7)
        self.risk_percent.setMaximumSize(QSize(16777215, 50))
        self.risk_percent.setFont(font19)
        self.risk_percent.setStyleSheet(u"background-color: rgb(12, 13, 15);\n"
"padding-left:15px;")

        self.horizontalLayout_26.addWidget(self.risk_percent)

        self.label_46 = QLabel(self.frame_17)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(50, 0))
        self.label_46.setFont(font19)
        self.label_46.setStyleSheet(u"color:#9d9ea2;\n"
"background-color: rgb(12, 13, 15);")
        self.label_46.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_46)

        self.horizontalLayout_26.setStretch(0, 1)

        self.verticalLayout_15.addWidget(self.frame_17)

        self.label_51 = QLabel(self.frame_13)
        self.label_51.setObjectName(u"label_51")
        sizePolicy6.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy6)
        self.label_51.setStyleSheet(u"border:0px;\n"
"color:#9d9ea2;\n"
"margin-top:20px;\n"
"margin-bottom:10px;")

        self.verticalLayout_15.addWidget(self.label_51)

        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"background-color: rgb(12, 13, 15);")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.frame_18)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(50, 0))
        self.label_49.setFont(font19)
        self.label_49.setStyleSheet(u"color:#9d9ea2;background-color: rgb(12, 13, 15);")
        self.label_49.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_49)

        self.sl = QLineEdit(self.frame_18)
        self.sl.setObjectName(u"sl")
        sizePolicy7.setHeightForWidth(self.sl.sizePolicy().hasHeightForWidth())
        self.sl.setSizePolicy(sizePolicy7)
        self.sl.setMaximumSize(QSize(16777215, 50))
        self.sl.setFont(font19)
        self.sl.setStyleSheet(u"background-color: rgb(12, 13, 15);")

        self.horizontalLayout_27.addWidget(self.sl)

        self.horizontalLayout_27.setStretch(1, 1)

        self.verticalLayout_15.addWidget(self.frame_18)

        self.label_48 = QLabel(self.frame_13)
        self.label_48.setObjectName(u"label_48")
        sizePolicy6.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy6)
        self.label_48.setStyleSheet(u"border:0px;\n"
"color:#9d9ea2;\n"
"margin-bottom:10px;\n"
"margin-top:20px;")

        self.verticalLayout_15.addWidget(self.label_48)

        self.frame_19 = QFrame(self.frame_13)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"background-color: rgb(12, 13, 15);")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.risk_reward_r = QLineEdit(self.frame_19)
        self.risk_reward_r.setObjectName(u"risk_reward_r")
        sizePolicy7.setHeightForWidth(self.risk_reward_r.sizePolicy().hasHeightForWidth())
        self.risk_reward_r.setSizePolicy(sizePolicy7)
        self.risk_reward_r.setMaximumSize(QSize(16777215, 50))
        font20 = QFont()
        font20.setFamilies([u"Microsoft Sans Serif"])
        font20.setPointSize(13)
        self.risk_reward_r.setFont(font20)
        self.risk_reward_r.setStyleSheet(u"background-color: rgb(12, 13, 15);padding-left:15px;")

        self.horizontalLayout_28.addWidget(self.risk_reward_r)

        self.label_50 = QLabel(self.frame_19)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(50, 0))
        self.label_50.setFont(font19)
        self.label_50.setStyleSheet(u"color:#9d9ea2;background-color: rgb(12, 13, 15);")
        self.label_50.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_50)

        self.horizontalLayout_28.setStretch(0, 1)

        self.verticalLayout_15.addWidget(self.frame_19)


        self.horizontalLayout_14.addWidget(self.frame_13)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 1)

        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"#frame_11{\n"
"border:0px;\n"
"}")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_11)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(20, 0, 20, 20)
        self.label_27 = QLabel(self.frame_11)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font15)
        self.label_27.setStyleSheet(u"color:#9d9ea2;\n"
"border:0px;\n"
"margin-bottom:15px;")

        self.verticalLayout_13.addWidget(self.label_27)

        self.trade_calculat_btn = QPushButton(self.frame_11)
        self.trade_calculat_btn.setObjectName(u"trade_calculat_btn")
        self.trade_calculat_btn.setMinimumSize(QSize(0, 50))
        self.trade_calculat_btn.setMaximumSize(QSize(16777215, 50))
        self.trade_calculat_btn.setFont(font19)
        self.trade_calculat_btn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.trade_calculat_btn.setStyleSheet(u"background-color: rgb(74, 141, 245);\n"
"border:0px;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/chevron-right_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.trade_calculat_btn.setIcon(icon2)
        self.trade_calculat_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_13.addWidget(self.trade_calculat_btn)


        self.verticalLayout_12.addWidget(self.frame_11)

        self.verticalLayout_12.setStretch(1, 1)

        self.verticalLayout_10.addWidget(self.frame_9)

        self.verticalLayout_10.setStretch(0, 1)

        self.horizontalLayout_4.addWidget(self.frame_7)

        self.trading_pages = QStackedWidget(self.frame_6)
        self.trading_pages.setObjectName(u"trading_pages")
        self.empty_frame = QWidget()
        self.empty_frame.setObjectName(u"empty_frame")
        self.verticalLayout_21 = QVBoxLayout(self.empty_frame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 20, 0, 0)
        self.frame_em = QFrame(self.empty_frame)
        self.frame_em.setObjectName(u"frame_em")
        sizePolicy.setHeightForWidth(self.frame_em.sizePolicy().hasHeightForWidth())
        self.frame_em.setSizePolicy(sizePolicy)
        self.frame_em.setMinimumSize(QSize(0, 481))
        self.frame_em.setMaximumSize(QSize(500, 493))
        self.frame_em.setStyleSheet(u"background-color: rgb(22, 23, 25);\n"
"border:1px solid #2f3033;\n"
"border-radius:4px ;")
        self.frame_em.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_em.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_em)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(30, 0, 30, 0)
        self.info_label = QLabel(self.frame_em)
        self.info_label.setObjectName(u"info_label")
        sizePolicy.setHeightForWidth(self.info_label.sizePolicy().hasHeightForWidth())
        self.info_label.setSizePolicy(sizePolicy)
        self.info_label.setFont(font15)
        self.info_label.setStyleSheet(u"color: rgb(157, 158, 162);\n"
"border:0px;")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.info_label)


        self.verticalLayout_21.addWidget(self.frame_em)

        self.verticalSpacer_4 = QSpacerItem(40, 87, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_21.addItem(self.verticalSpacer_4)

        self.verticalLayout_21.setStretch(0, 1)
        self.verticalLayout_21.setStretch(1, 1)
        self.trading_pages.addWidget(self.empty_frame)
        self.result_frame = QWidget()
        self.result_frame.setObjectName(u"result_frame")
        self.horizontalLayout_36 = QHBoxLayout(self.result_frame)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.frame_8 = QFrame(self.result_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_8)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_8)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_20)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 15)
        self.label_31 = QLabel(self.frame_20)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font17)
        self.label_31.setStyleSheet(u"border:0px;")

        self.verticalLayout_17.addWidget(self.label_31)

        self.label_30 = QLabel(self.frame_20)
        self.label_30.setObjectName(u"label_30")
        font21 = QFont()
        font21.setFamilies([u"Microsoft Sans Serif"])
        font21.setPointSize(9)
        self.label_30.setFont(font21)
        self.label_30.setStyleSheet(u"color:#9d9ea2;\n"
"border:0px;")

        self.verticalLayout_17.addWidget(self.label_30)


        self.verticalLayout_16.addWidget(self.frame_20)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, -1, -1, 30)
        self.frame_21 = QFrame(self.frame_8)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_21)
        self.verticalLayout_18.setSpacing(15)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 7, 0)
        self.frame_24 = QFrame(self.frame_21)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"background-color: rgb(22, 23, 25);\n"
"border:1px solid #2f3033;\n"
"border-radius:4px ;")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_24)
        self.verticalLayout_19.setSpacing(20)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(15, 15, 15, 15)
        self.frame_26 = QFrame(self.frame_24)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"border:0px;")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.frame_26)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"color:#9d9ea2;\n"
"border:0px;")

        self.horizontalLayout_19.addWidget(self.label_34)

        self.label_35 = QLabel(self.frame_26)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(16, 16))
        self.label_35.setPixmap(QPixmap(u":/icons/icons/arrow-down-left.svg"))
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_35)

        self.horizontalLayout_19.setStretch(0, 1)

        self.verticalLayout_19.addWidget(self.frame_26)

        self.risk_A_label = QLabel(self.frame_24)
        self.risk_A_label.setObjectName(u"risk_A_label")
        font22 = QFont()
        font22.setFamilies([u"Microsoft Sans Serif"])
        font22.setPointSize(20)
        font22.setWeight(QFont.ExtraBold)
        self.risk_A_label.setFont(font22)
        self.risk_A_label.setStyleSheet(u"color:#f94144;\n"
"border:0px;")

        self.verticalLayout_19.addWidget(self.risk_A_label)


        self.verticalLayout_18.addWidget(self.frame_24)

        self.frame_27 = QFrame(self.frame_21)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"background-color: rgb(22, 23, 25);\n"
"border:1px solid #2f3033;\n"
"border-radius:4px ;")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_27)
        self.verticalLayout_23.setSpacing(20)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(15, 15, 15, 15)
        self.frame_31 = QFrame(self.frame_27)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"border:0px;")
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_56 = QLabel(self.frame_31)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"color:#9d9ea2;\n"
"border:0px;")

        self.horizontalLayout_23.addWidget(self.label_56)

        self.horizontalLayout_23.setStretch(0, 1)

        self.verticalLayout_23.addWidget(self.frame_31)

        self.pot_Loss_label = QLabel(self.frame_27)
        self.pot_Loss_label.setObjectName(u"pot_Loss_label")
        self.pot_Loss_label.setFont(font22)
        self.pot_Loss_label.setStyleSheet(u"color:#f94144;\n"
"border:0px;")

        self.verticalLayout_23.addWidget(self.pot_Loss_label)


        self.verticalLayout_18.addWidget(self.frame_27)

        self.frame_32 = QFrame(self.frame_21)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"background-color: rgb(22, 23, 25);\n"
"border:1px solid #2f3033;\n"
"border-radius:4px ;")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_32)
        self.verticalLayout_24.setSpacing(20)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(15, 15, 15, 15)
        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"border:0px;")
        self.frame_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_59 = QLabel(self.frame_33)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"color:#9d9ea2;\n"
"border:0px;")

        self.horizontalLayout_29.addWidget(self.label_59)

        self.horizontalLayout_29.setStretch(0, 1)

        self.verticalLayout_24.addWidget(self.frame_33)

        self.rr_label = QLabel(self.frame_32)
        self.rr_label.setObjectName(u"rr_label")
        self.rr_label.setFont(font22)
        self.rr_label.setStyleSheet(u"color:#20c45f;\n"
"border:0px;")

        self.verticalLayout_24.addWidget(self.rr_label)


        self.verticalLayout_18.addWidget(self.frame_32)


        self.horizontalLayout_17.addWidget(self.frame_21)

        self.frame_25 = QFrame(self.frame_8)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_25)
        self.verticalLayout_28.setSpacing(15)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(7, 0, 0, 0)
        self.frame_38 = QFrame(self.frame_25)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"background-color: rgb(22, 23, 25);\n"
"border:1px solid #2f3033;\n"
"border-radius:4px ;")
        self.frame_38.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_38)
        self.verticalLayout_27.setSpacing(20)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(15, 15, 15, 15)
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"border:0px;")
        self.frame_39.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_68 = QLabel(self.frame_39)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setStyleSheet(u"color:#9d9ea2;\n"
"border:0px;")

        self.horizontalLayout_32.addWidget(self.label_68)

        self.horizontalLayout_32.setStretch(0, 1)

        self.verticalLayout_27.addWidget(self.frame_39)

        self.pot_Size_label = QLabel(self.frame_38)
        self.pot_Size_label.setObjectName(u"pot_Size_label")
        self.pot_Size_label.setFont(font22)
        self.pot_Size_label.setStyleSheet(u"color:#f5f7f9;\n"
"border:0px;")

        self.verticalLayout_27.addWidget(self.pot_Size_label)


        self.verticalLayout_28.addWidget(self.frame_38)

        self.frame_36 = QFrame(self.frame_25)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"background-color: rgb(22, 23, 25);\n"
"border:1px solid #2f3033;\n"
"border-radius:4px ;")
        self.frame_36.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_36)
        self.verticalLayout_26.setSpacing(20)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(15, 15, 15, 15)
        self.frame_37 = QFrame(self.frame_36)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"border:0px;")
        self.frame_37.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_65 = QLabel(self.frame_37)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setStyleSheet(u"color:#9d9ea2;\n"
"border:0px;")

        self.horizontalLayout_31.addWidget(self.label_65)

        self.label_66 = QLabel(self.frame_37)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMaximumSize(QSize(16, 16))
        self.label_66.setPixmap(QPixmap(u":/icons/icons/arrow-up-right.svg"))
        self.label_66.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_66)

        self.horizontalLayout_31.setStretch(0, 1)

        self.verticalLayout_26.addWidget(self.frame_37)

        self.pot_Profit_label = QLabel(self.frame_36)
        self.pot_Profit_label.setObjectName(u"pot_Profit_label")
        self.pot_Profit_label.setFont(font22)
        self.pot_Profit_label.setStyleSheet(u"color:#20c45f;\n"
"border:0px;")

        self.verticalLayout_26.addWidget(self.pot_Profit_label)


        self.verticalLayout_28.addWidget(self.frame_36)

        self.frame_34 = QFrame(self.frame_25)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"background-color: rgb(22, 23, 25);\n"
"border:1px solid #2f3033;\n"
"border-radius:4px ;")
        self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_34)
        self.verticalLayout_25.setSpacing(20)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(15, 15, 15, 15)
        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"border:0px;")
        self.frame_35.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_62 = QLabel(self.frame_35)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setStyleSheet(u"color:#9d9ea2;\n"
"border:0px;")

        self.horizontalLayout_30.addWidget(self.label_62)

        self.horizontalLayout_30.setStretch(0, 1)

        self.verticalLayout_25.addWidget(self.frame_35)

        self.pot_SLD_label = QLabel(self.frame_34)
        self.pot_SLD_label.setObjectName(u"pot_SLD_label")
        self.pot_SLD_label.setFont(font22)
        self.pot_SLD_label.setStyleSheet(u"color:#f5f7f9;\n"
"border:0px;")

        self.verticalLayout_25.addWidget(self.pot_SLD_label)


        self.verticalLayout_28.addWidget(self.frame_34)


        self.horizontalLayout_17.addWidget(self.frame_25)

        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 1)

        self.verticalLayout_16.addLayout(self.horizontalLayout_17)

        self.frame_22 = QFrame(self.frame_8)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"QFrame QLabel{\n"
"border:0px;\n"
"}\n"
"\n"
"\n"
"")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_22)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"background-color: rgb(22, 23, 25);\n"
"border:1px solid #2f3033;\n"
"border-radius:4px ;\n"
"")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_23)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 20)
        self.label_33 = QLabel(self.frame_23)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font17)
        self.label_33.setStyleSheet(u"border:0px;")

        self.horizontalLayout_33.addWidget(self.label_33)

        self.label_32 = QLabel(self.frame_23)
        self.label_32.setObjectName(u"label_32")
        font23 = QFont()
        font23.setFamilies([u"Microsoft Sans Serif"])
        font23.setPointSize(8)
        self.label_32.setFont(font23)
        self.label_32.setStyleSheet(u"border:0px;\n"
"color: rgb(157, 158, 162);")

        self.horizontalLayout_33.addWidget(self.label_32)

        self.horizontalLayout_33.setStretch(0, 4)
        self.horizontalLayout_33.setStretch(1, 1)

        self.verticalLayout_30.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_40 = QFrame(self.frame_23)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMaximumSize(QSize(10, 16777215))
        self.frame_40.setStyleSheet(u"border:0px;")
        self.frame_40.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_40)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_73 = QLabel(self.frame_40)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMinimumSize(QSize(10, 10))
        self.label_73.setMaximumSize(QSize(10, 10))
        self.label_73.setStyleSheet(u"background-color: rgb(32, 196, 95);\n"
"border-radius: 4px ;")
        self.label_73.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_73)

        self.label_72 = QLabel(self.frame_40)
        self.label_72.setObjectName(u"label_72")
        sizePolicy.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy)
        self.label_72.setMaximumSize(QSize(12, 16777215))
        font24 = QFont()
        font24.setFamilies([u"Microsoft Sans Serif"])
        font24.setPointSize(20)
        self.label_72.setFont(font24)
        self.label_72.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_72.setStyleSheet(u"\n"
"color: rgb(157, 158, 162);")
        self.label_72.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_72)

        self.label_71 = QLabel(self.frame_40)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMaximumSize(QSize(10, 10))
        self.label_71.setStyleSheet(u"background-color: rgb(74, 141, 245);\n"
"border-radius: 4px ;")
        self.label_71.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_71)

        self.label_75 = QLabel(self.frame_40)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMaximumSize(QSize(12, 16777215))
        font25 = QFont()
        font25.setFamilies([u"Microsoft Sans Serif"])
        font25.setPointSize(21)
        self.label_75.setFont(font25)
        self.label_75.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_75.setStyleSheet(u"color: rgb(157, 158, 162);")
        self.label_75.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_75)

        self.label_74 = QLabel(self.frame_40)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMaximumSize(QSize(10, 10))
        self.label_74.setStyleSheet(u"background-color: rgb(249, 65, 68);\n"
"border-radius: 4px ;")
        self.label_74.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_74)


        self.horizontalLayout_18.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.frame_23)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"border:0px;")
        self.frame_41.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_42 = QFrame(self.frame_41)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"border:0px;")
        self.frame_42.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_42)
        self.verticalLayout_32.setSpacing(27)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(-1, 0, 0, 0)
        self.label_76 = QLabel(self.frame_42)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font15)
        self.label_76.setStyleSheet(u"border:0px;")

        self.verticalLayout_32.addWidget(self.label_76)

        self.label_77 = QLabel(self.frame_42)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font15)
        self.label_77.setStyleSheet(u"border:0px;")

        self.verticalLayout_32.addWidget(self.label_77)

        self.label_78 = QLabel(self.frame_42)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font15)
        self.label_78.setStyleSheet(u"border:0px;")

        self.verticalLayout_32.addWidget(self.label_78)


        self.horizontalLayout_34.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.frame_41)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"border:0px;")
        self.frame_43.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_43)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(-1, 0, 0, 0)
        self.TP_label = QLabel(self.frame_43)
        self.TP_label.setObjectName(u"TP_label")
        font26 = QFont()
        font26.setFamilies([u"Microsoft Sans Serif"])
        font26.setPointSize(15)
        font26.setBold(True)
        self.TP_label.setFont(font26)
        self.TP_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.TP_label.setStyleSheet(u"border:0px;\n"
"color: rgb(32, 196, 95);")
        self.TP_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_33.addWidget(self.TP_label)

        self.Entry_label = QLabel(self.frame_43)
        self.Entry_label.setObjectName(u"Entry_label")
        self.Entry_label.setFont(font26)
        self.Entry_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Entry_label.setStyleSheet(u"border:0px;\n"
"color: rgb(74, 141, 245);")
        self.Entry_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_33.addWidget(self.Entry_label)

        self.Stop_loss_label = QLabel(self.frame_43)
        self.Stop_loss_label.setObjectName(u"Stop_loss_label")
        self.Stop_loss_label.setFont(font26)
        self.Stop_loss_label.setStyleSheet(u"border:0px;\n"
"color: rgb(249, 65, 68);")
        self.Stop_loss_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_33.addWidget(self.Stop_loss_label)


        self.horizontalLayout_34.addWidget(self.frame_43)


        self.horizontalLayout_18.addWidget(self.frame_41)

        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(1, 9)

        self.verticalLayout_30.addLayout(self.horizontalLayout_18)


        self.verticalLayout_29.addWidget(self.frame_23)


        self.verticalLayout_16.addWidget(self.frame_22)

        self.verticalSpacer_5 = QSpacerItem(20, 319, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_16.addItem(self.verticalSpacer_5)

        self.verticalLayout_16.setStretch(2, 1)

        self.horizontalLayout_36.addWidget(self.frame_8)

        self.trading_pages.addWidget(self.result_frame)

        self.horizontalLayout_4.addWidget(self.trading_pages)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)

        self.horizontalLayout_13.addLayout(self.horizontalLayout_4)


        self.verticalLayout_7.addWidget(self.frame_6)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.horizontalLayout_2.addWidget(self.trad_frame)

        self.stackedWidget_2.addWidget(self.trading_section)

        self.horizontalLayout_20.addWidget(self.stackedWidget_2)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 9)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 9)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_22.addWidget(self.stackedWidget)

        Calculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calculator)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(2)
        self.trading_pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Calculator)
    # setupUi

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(QCoreApplication.translate("Calculator", u"MainWindow", None))
        self.label_14.setText("")
        self.label.setText(QCoreApplication.translate("Calculator", u"Smart calc", None))
        self.label_2.setText(QCoreApplication.translate("Calculator", u"WORKSPACE", None))
        self.calculator_icon.setText("")
        self.label_4.setText(QCoreApplication.translate("Calculator", u"Calculator", None))
        self.calculat_arrow.setText("")
        self.label_8.setText(QCoreApplication.translate("Calculator", u"Trading", None))
        self.trade_arrow.setText("")
        self.label_12.setText(QCoreApplication.translate("Calculator", u"Settings", None))
        self.label_11.setText(QCoreApplication.translate("Calculator", u"Workspace", None))
        self.path_arrow.setText("")
        self.path_name.setText(QCoreApplication.translate("Calculator", u"Calculator", None))
        self.label_15.setText(QCoreApplication.translate("Calculator", u"STANDARD", None))
        self.label_16.setText(QCoreApplication.translate("Calculator", u"Calculator", None))
        self.label_17.setText(QCoreApplication.translate("Calculator", u"Everyday calculations, made effortless", None))
        self.label_18.setText(QCoreApplication.translate("Calculator", u"CALCULATIONS", None))
        self.result_bar.setText("")
        self.user_value.setInputMask("")
        self.user_value.setText("")
        self.user_value.setPlaceholderText(QCoreApplication.translate("Calculator", u"0", None))
        self.btn_multiply.setText(QCoreApplication.translate("Calculator", u"x", None))
        self.num_6.setText(QCoreApplication.translate("Calculator", u"6", None))
        self.clear_btn.setText(QCoreApplication.translate("Calculator", u"AC", None))
        self.num_5.setText(QCoreApplication.translate("Calculator", u"5", None))
        self.btn_minus.setText(QCoreApplication.translate("Calculator", u"-", None))
        self.btn_decimal.setText(QCoreApplication.translate("Calculator", u".", None))
        self.num_2.setText(QCoreApplication.translate("Calculator", u"2", None))
        self.num_1.setText(QCoreApplication.translate("Calculator", u"1", None))
        self.btn_divide.setText(QCoreApplication.translate("Calculator", u"\u00f7", None))
        self.btn_percent.setText(QCoreApplication.translate("Calculator", u"%", None))
        self.btn_minus_plus.setText(QCoreApplication.translate("Calculator", u"+/-", None))
        self.num_9.setText(QCoreApplication.translate("Calculator", u"9", None))
        self.btn_plus.setText(QCoreApplication.translate("Calculator", u"+", None))
        self.num_8.setText(QCoreApplication.translate("Calculator", u"8", None))
        self.num_0.setText(QCoreApplication.translate("Calculator", u"0", None))
        self.num_3.setText(QCoreApplication.translate("Calculator", u"3", None))
        self.num_4.setText(QCoreApplication.translate("Calculator", u"4", None))
        self.btn_equal.setText(QCoreApplication.translate("Calculator", u"=", None))
        self.num_7.setText(QCoreApplication.translate("Calculator", u"7", None))
        self.label_20.setText(QCoreApplication.translate("Calculator", u"Keyboard input supported - Esc to clear - Enter for result", None))
        self.label_41.setText(QCoreApplication.translate("Calculator", u"PREFERENCES", None))
        self.label_52.setText(QCoreApplication.translate("Calculator", u"Settings", None))
        self.label_40.setText(QCoreApplication.translate("Calculator", u"SmartCalc workspace information.", None))
        self.label_19.setText(QCoreApplication.translate("Calculator", u"About SmartCalc", None))
        self.label_37.setText(QCoreApplication.translate("Calculator", u"A focused workspace for everyday calculations and trading risk planning", None))
        self.label_39.setText(QCoreApplication.translate("Calculator", u"Version 1.0 - Desktop interface", None))
        self.label_21.setText(QCoreApplication.translate("Calculator", u"TRADING TOOLS", None))
        self.label_22.setText(QCoreApplication.translate("Calculator", u"Trading Calculator", None))
        self.label_23.setText(QCoreApplication.translate("Calculator", u"Plan your position with a clear view of risk and reward.", None))
        self.label_25.setText(QCoreApplication.translate("Calculator", u"Trade parameters", None))
        self.label_26.setText(QCoreApplication.translate("Calculator", u"Enter your trade details", None))
        self.label_28.setText(QCoreApplication.translate("Calculator", u"Account Balance", None))
        self.label_29.setText(QCoreApplication.translate("Calculator", u"$", None))
        self.acc_b.setPlaceholderText(QCoreApplication.translate("Calculator", u"0", None))
        self.label_43.setText(QCoreApplication.translate("Calculator", u"Entry Price", None))
        self.label_42.setText(QCoreApplication.translate("Calculator", u"$", None))
        self.entry_p.setPlaceholderText(QCoreApplication.translate("Calculator", u"0", None))
        self.label_45.setText(QCoreApplication.translate("Calculator", u"Take Profit", None))
        self.label_44.setText(QCoreApplication.translate("Calculator", u"$", None))
        self.tp.setPlaceholderText(QCoreApplication.translate("Calculator", u"0", None))
        self.label_47.setText(QCoreApplication.translate("Calculator", u"Risk  %", None))
        self.risk_percent.setPlaceholderText(QCoreApplication.translate("Calculator", u"0", None))
        self.label_46.setText(QCoreApplication.translate("Calculator", u"%", None))
        self.label_51.setText(QCoreApplication.translate("Calculator", u"Stop Loss", None))
        self.label_49.setText(QCoreApplication.translate("Calculator", u"$", None))
        self.sl.setPlaceholderText(QCoreApplication.translate("Calculator", u"0", None))
        self.label_48.setText(QCoreApplication.translate("Calculator", u"Risk/Reward Ratio", None))
        self.risk_reward_r.setPlaceholderText(QCoreApplication.translate("Calculator", u"Auto from target", None))
        self.label_50.setText(QCoreApplication.translate("Calculator", u":2", None))
        self.label_27.setText(QCoreApplication.translate("Calculator", u"Enter a target price or a ratio. A ratio calculates the target price for you.", None))
        self.trade_calculat_btn.setText(QCoreApplication.translate("Calculator", u"Calculate   ", None))
        self.info_label.setText(QCoreApplication.translate("Calculator", u"Enter your trade parameters and click Calculate to see results", None))
        self.label_31.setText(QCoreApplication.translate("Calculator", u"Results overview", None))
        self.label_30.setText(QCoreApplication.translate("Calculator", u"Your position at a glance", None))
        self.label_34.setText(QCoreApplication.translate("Calculator", u"Risk Amount", None))
        self.risk_A_label.setText(QCoreApplication.translate("Calculator", u"123", None))
        self.label_56.setText(QCoreApplication.translate("Calculator", u"Potential Loss", None))
        self.pot_Loss_label.setText(QCoreApplication.translate("Calculator", u"123", None))
        self.label_59.setText(QCoreApplication.translate("Calculator", u"Risk/Reward", None))
        self.rr_label.setText(QCoreApplication.translate("Calculator", u"132321", None))
        self.label_68.setText(QCoreApplication.translate("Calculator", u"Position Size", None))
        self.pot_Size_label.setText(QCoreApplication.translate("Calculator", u"13", None))
        self.label_65.setText(QCoreApplication.translate("Calculator", u"Potential Profit", None))
        self.pot_Profit_label.setText(QCoreApplication.translate("Calculator", u"123", None))
        self.label_62.setText(QCoreApplication.translate("Calculator", u"Stop Loss Distance", None))
        self.pot_SLD_label.setText(QCoreApplication.translate("Calculator", u"133", None))
        self.label_33.setText(QCoreApplication.translate("Calculator", u"Price levels", None))
        self.label_32.setText(QCoreApplication.translate("Calculator", u"ENTRY - TARGET - STOP", None))
        self.label_72.setText(QCoreApplication.translate("Calculator", u"|", None))
        self.label_75.setText(QCoreApplication.translate("Calculator", u"|", None))
        self.label_76.setText(QCoreApplication.translate("Calculator", u"Take Profit", None))
        self.label_77.setText(QCoreApplication.translate("Calculator", u"Entry Price", None))
        self.label_78.setText(QCoreApplication.translate("Calculator", u"Stop Loss", None))
        self.TP_label.setText(QCoreApplication.translate("Calculator", u"13", None))
        self.Entry_label.setText(QCoreApplication.translate("Calculator", u"3424", None))
        self.Stop_loss_label.setText(QCoreApplication.translate("Calculator", u"4234234", None))
    # retranslateUi

