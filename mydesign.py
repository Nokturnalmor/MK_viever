# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python\MK_viever\mydesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1278, 855)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(self.tab)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cmb_napr = QtWidgets.QComboBox(self.layoutWidget)
        self.cmb_napr.setObjectName("cmb_napr")
        self.verticalLayout.addWidget(self.cmb_napr)
        self.tbl_mk_filtr = QtWidgets.QTableWidget(self.layoutWidget)
        self.tbl_mk_filtr.setMaximumSize(QtCore.QSize(16777215, 66))
        self.tbl_mk_filtr.setObjectName("tbl_mk_filtr")
        self.tbl_mk_filtr.setColumnCount(0)
        self.tbl_mk_filtr.setRowCount(0)
        self.verticalLayout.addWidget(self.tbl_mk_filtr)
        self.tbl_mk = QtWidgets.QTableWidget(self.layoutWidget)
        self.tbl_mk.setObjectName("tbl_mk")
        self.tbl_mk.setColumnCount(0)
        self.tbl_mk.setRowCount(0)
        self.verticalLayout.addWidget(self.tbl_mk)
        self.groupBox_4 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.groupBox_4)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.lbl_curr_mk = QtWidgets.QLabel(self.tab_5)
        self.lbl_curr_mk.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_curr_mk.setFont(font)
        self.lbl_curr_mk.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_curr_mk.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lbl_curr_mk.setText("")
        self.lbl_curr_mk.setObjectName("lbl_curr_mk")
        self.verticalLayout_11.addWidget(self.lbl_curr_mk)
        self.tbl_filtr_dse = QtWidgets.QTableWidget(self.tab_5)
        self.tbl_filtr_dse.setMaximumSize(QtCore.QSize(16777215, 66))
        self.tbl_filtr_dse.setObjectName("tbl_filtr_dse")
        self.tbl_filtr_dse.setColumnCount(0)
        self.tbl_filtr_dse.setRowCount(0)
        self.verticalLayout_11.addWidget(self.tbl_filtr_dse)
        self.tbl_dse = QtWidgets.QTableWidget(self.tab_5)
        self.tbl_dse.setMinimumSize(QtCore.QSize(0, 10))
        self.tbl_dse.setMaximumSize(QtCore.QSize(7215, 7215))
        self.tbl_dse.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tbl_dse.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbl_dse.setShowGrid(True)
        self.tbl_dse.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_dse.setCornerButtonEnabled(True)
        self.tbl_dse.setObjectName("tbl_dse")
        self.tbl_dse.setColumnCount(0)
        self.tbl_dse.setRowCount(0)
        self.tbl_dse.verticalHeader().setDefaultSectionSize(36)
        self.verticalLayout_11.addWidget(self.tbl_dse)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.splitter_2 = QtWidgets.QSplitter(self.tab_6)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tbl_jur_filtr = QtWidgets.QTableWidget(self.layoutWidget1)
        self.tbl_jur_filtr.setMaximumSize(QtCore.QSize(16777215, 66))
        self.tbl_jur_filtr.setObjectName("tbl_jur_filtr")
        self.tbl_jur_filtr.setColumnCount(0)
        self.tbl_jur_filtr.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tbl_jur_filtr)
        self.tbl_jur = QtWidgets.QTableWidget(self.layoutWidget1)
        self.tbl_jur.setObjectName("tbl_jur")
        self.tbl_jur.setColumnCount(0)
        self.tbl_jur.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tbl_jur)
        self.tbl_zadanie = QtWidgets.QTableWidget(self.splitter_2)
        self.tbl_zadanie.setObjectName("tbl_zadanie")
        self.tbl_zadanie.setColumnCount(0)
        self.tbl_zadanie.setRowCount(0)
        self.verticalLayout_6.addWidget(self.splitter_2)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.tab_7)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.tbl_zamech_filtr = QtWidgets.QTableWidget(self.tab_7)
        self.tbl_zamech_filtr.setMaximumSize(QtCore.QSize(16777215, 66))
        self.tbl_zamech_filtr.setObjectName("tbl_zamech_filtr")
        self.tbl_zamech_filtr.setColumnCount(0)
        self.tbl_zamech_filtr.setRowCount(0)
        self.verticalLayout_14.addWidget(self.tbl_zamech_filtr)
        self.tbl_zamech = QtWidgets.QTableWidget(self.tab_7)
        self.tbl_zamech.setMinimumSize(QtCore.QSize(0, 10))
        self.tbl_zamech.setMaximumSize(QtCore.QSize(7215, 7215))
        self.tbl_zamech.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tbl_zamech.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbl_zamech.setShowGrid(True)
        self.tbl_zamech.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_zamech.setCornerButtonEnabled(True)
        self.tbl_zamech.setObjectName("tbl_zamech")
        self.tbl_zamech.setColumnCount(0)
        self.tbl_zamech.setRowCount(0)
        self.tbl_zamech.verticalHeader().setDefaultSectionSize(36)
        self.verticalLayout_14.addWidget(self.tbl_zamech)
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget_2.addTab(self.tab_8, "")
        self.verticalLayout_10.addWidget(self.tabWidget_2)
        self.verticalLayout_3.addWidget(self.splitter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.fr_cal = QtWidgets.QFrame(self.tab_2)
        self.fr_cal.setMaximumSize(QtCore.QSize(16777215, 290))
        self.fr_cal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_cal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_cal.setObjectName("fr_cal")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.fr_cal)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.fr_cal)
        self.calendarWidget.setMaximumSize(QtCore.QSize(16777215, 200))
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout_3.addWidget(self.calendarWidget)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.fr_cal)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_13.addWidget(self.label_5)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.rbut_nach_per = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbut_nach_per.setText("")
        self.rbut_nach_per.setObjectName("rbut_nach_per")
        self.horizontalLayout_13.addWidget(self.rbut_nach_per)
        self.le_nach_per = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_nach_per.setFont(font)
        self.le_nach_per.setObjectName("le_nach_per")
        self.horizontalLayout_13.addWidget(self.le_nach_per)
        self.verticalLayout_13.addLayout(self.horizontalLayout_13)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_13.addWidget(self.label_4)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.rbut_konec_per = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbut_konec_per.setText("")
        self.rbut_konec_per.setObjectName("rbut_konec_per")
        self.horizontalLayout_14.addWidget(self.rbut_konec_per)
        self.le_konec_per = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_konec_per.setFont(font)
        self.le_konec_per.setObjectName("le_konec_per")
        self.horizontalLayout_14.addWidget(self.le_konec_per)
        self.verticalLayout_13.addLayout(self.horizontalLayout_14)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 0, 11, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cmb_vid_otcheta = QtWidgets.QComboBox(self.fr_cal)
        self.cmb_vid_otcheta.setMinimumSize(QtCore.QSize(0, 33))
        self.cmb_vid_otcheta.setMaximumSize(QtCore.QSize(16777215, 33))
        self.cmb_vid_otcheta.setObjectName("cmb_vid_otcheta")
        self.horizontalLayout_2.addWidget(self.cmb_vid_otcheta)
        self.cmb_podrazdelenie = QtWidgets.QComboBox(self.fr_cal)
        self.cmb_podrazdelenie.setMinimumSize(QtCore.QSize(0, 33))
        self.cmb_podrazdelenie.setMaximumSize(QtCore.QSize(16777215, 33))
        self.cmb_podrazdelenie.setMaxVisibleItems(50)
        self.cmb_podrazdelenie.setObjectName("cmb_podrazdelenie")
        self.horizontalLayout_2.addWidget(self.cmb_podrazdelenie)
        self.btn_otchet = QtWidgets.QPushButton(self.fr_cal)
        self.btn_otchet.setMinimumSize(QtCore.QSize(0, 33))
        self.btn_otchet.setMaximumSize(QtCore.QSize(16777215, 33))
        self.btn_otchet.setObjectName("btn_otchet")
        self.horizontalLayout_2.addWidget(self.btn_otchet)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.fr_cal)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.cmb_gant_tochnost_dat = QtWidgets.QComboBox(self.groupBox_3)
        self.cmb_gant_tochnost_dat.setMinimumSize(QtCore.QSize(0, 33))
        self.cmb_gant_tochnost_dat.setMaximumSize(QtCore.QSize(16777215, 33))
        self.cmb_gant_tochnost_dat.setObjectName("cmb_gant_tochnost_dat")
        self.verticalLayout_9.addWidget(self.cmb_gant_tochnost_dat)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cmb_gant_vert = QtWidgets.QComboBox(self.groupBox_3)
        self.cmb_gant_vert.setMinimumSize(QtCore.QSize(0, 33))
        self.cmb_gant_vert.setMaximumSize(QtCore.QSize(16777215, 33))
        self.cmb_gant_vert.setObjectName("cmb_gant_vert")
        self.horizontalLayout_4.addWidget(self.cmb_gant_vert)
        self.cmb_gant_vert_val = QtWidgets.QComboBox(self.groupBox_3)
        self.cmb_gant_vert_val.setMinimumSize(QtCore.QSize(0, 33))
        self.cmb_gant_vert_val.setMaximumSize(QtCore.QSize(16777215, 33))
        self.cmb_gant_vert_val.setObjectName("cmb_gant_vert_val")
        self.horizontalLayout_4.addWidget(self.cmb_gant_vert_val)
        self.cmb_gant_colour = QtWidgets.QComboBox(self.groupBox_3)
        self.cmb_gant_colour.setMinimumSize(QtCore.QSize(0, 33))
        self.cmb_gant_colour.setMaximumSize(QtCore.QSize(16777215, 33))
        self.cmb_gant_colour.setObjectName("cmb_gant_colour")
        self.horizontalLayout_4.addWidget(self.cmb_gant_colour)
        self.btn_grafic_load = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_grafic_load.setMinimumSize(QtCore.QSize(0, 33))
        self.btn_grafic_load.setMaximumSize(QtCore.QSize(16777215, 33))
        self.btn_grafic_load.setObjectName("btn_grafic_load")
        self.horizontalLayout_4.addWidget(self.btn_grafic_load)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.verticalLayout_15.addWidget(self.fr_cal)
        self.btn_udown = QtWidgets.QPushButton(self.tab_2)
        self.btn_udown.setObjectName("btn_udown")
        self.verticalLayout_15.addWidget(self.btn_udown)
        self.tabw_otchet = QtWidgets.QTabWidget(self.tab_2)
        self.tabw_otchet.setObjectName("tabw_otchet")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.tab_12)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.tbl_otchet_filtr = QtWidgets.QTableWidget(self.tab_12)
        self.tbl_otchet_filtr.setMaximumSize(QtCore.QSize(16777215, 66))
        self.tbl_otchet_filtr.setObjectName("tbl_otchet_filtr")
        self.tbl_otchet_filtr.setColumnCount(0)
        self.tbl_otchet_filtr.setRowCount(0)
        self.verticalLayout_16.addWidget(self.tbl_otchet_filtr)
        self.tbl_otchet = QtWidgets.QTableWidget(self.tab_12)
        self.tbl_otchet.setObjectName("tbl_otchet")
        self.tbl_otchet.setColumnCount(0)
        self.tbl_otchet.setRowCount(0)
        self.verticalLayout_16.addWidget(self.tbl_otchet)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.le_path_save = QtWidgets.QLineEdit(self.tab_12)
        self.le_path_save.setMinimumSize(QtCore.QSize(0, 33))
        self.le_path_save.setMaximumSize(QtCore.QSize(16777215, 33))
        self.le_path_save.setObjectName("le_path_save")
        self.horizontalLayout_6.addWidget(self.le_path_save)
        self.btn_save_txt = QtWidgets.QPushButton(self.tab_12)
        self.btn_save_txt.setEnabled(True)
        self.btn_save_txt.setMinimumSize(QtCore.QSize(99, 33))
        self.btn_save_txt.setMaximumSize(QtCore.QSize(99, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_save_txt.setFont(font)
        self.btn_save_txt.setObjectName("btn_save_txt")
        self.horizontalLayout_6.addWidget(self.btn_save_txt)
        self.verticalLayout_16.addLayout(self.horizontalLayout_6)
        self.tabw_otchet.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_13)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.line_2 = QtWidgets.QFrame(self.tab_13)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_8.addWidget(self.line_2)
        self.tabw_otchet.addTab(self.tab_13, "")
        self.verticalLayout_15.addWidget(self.tabw_otchet)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1278, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionexcel = QtWidgets.QAction(MainWindow)
        self.actionexcel.setObjectName("actionexcel")
        self.action_txt = QtWidgets.QAction(MainWindow)
        self.action_txt.setObjectName("action_txt")
        self.menu_2.addAction(self.actionexcel)
        self.menu_2.addAction(self.action_txt)
        self.menu.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabw_otchet.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Состояние"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Структура"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "Журнал"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "Замечания"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("MainWindow", "Аутосорсинг"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Маршрутные карты"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Период"))
        self.label_5.setText(_translate("MainWindow", "Начало периода"))
        self.label_4.setText(_translate("MainWindow", "Конец периода"))
        self.cmb_vid_otcheta.setToolTip(_translate("MainWindow", "Вид отчета"))
        self.cmb_podrazdelenie.setToolTip(_translate("MainWindow", "Подразделение"))
        self.btn_otchet.setToolTip(_translate("MainWindow", "shift - del cache"))
        self.btn_otchet.setText(_translate("MainWindow", "Сформировать"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Парметры планирования"))
        self.cmb_gant_tochnost_dat.setToolTip(_translate("MainWindow", "цвет"))
        self.cmb_gant_vert.setToolTip(_translate("MainWindow", "поле"))
        self.cmb_gant_vert_val.setToolTip(_translate("MainWindow", "поле_значение"))
        self.cmb_gant_colour.setToolTip(_translate("MainWindow", "цвет"))
        self.btn_grafic_load.setText(_translate("MainWindow", "График"))
        self.btn_udown.setText(_translate("MainWindow", "^"))
        self.btn_save_txt.setText(_translate("MainWindow", "Выгрузить"))
        self.tabw_otchet.setTabText(self.tabw_otchet.indexOf(self.tab_12), _translate("MainWindow", "Таблица"))
        self.tabw_otchet.setTabText(self.tabw_otchet.indexOf(self.tab_13), _translate("MainWindow", "График"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Отчеты"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Выгрузить таблицу"))
        self.actionexcel.setText(_translate("MainWindow", "Excel"))
        self.action_txt.setText(_translate("MainWindow", "txt"))
