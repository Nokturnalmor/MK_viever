import Cust_Functions as F

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWinExtras import QtWin
import os
import time
import subprocess
from mydesign import Ui_MainWindow  # импорт нашего сгенерированного файла
#from mydesign2 import Ui_Dialog  # импорт нашего сгенерированного файла
import sys
    #pyinstaller.exe --onefile --icon=1.ico --noconsole Viever.py
def showDialog(self, msg):
    msgBox = QtWidgets.QMessageBox()
    msgBox.setIcon(QtWidgets.QMessageBox.Information)
    msgBox.setText(msg)
    msgBox.setWindowTitle("Внимание!")
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)  # | QtWidgets.QMessageBox.Cancel)
    returnValue = msgBox.exec()

#class mywindow2(QtWidgets.QDialog):  # диалоговое окно
#    def __init__(self,parent=None,item_o="",p1=0,p2=0):
#        self.item_o = item_o
#        self.p1 = p1
#        self.p2 = p2
#        self.myparent = parent
#        super(mywindow2, self).__init__()
#        self.ui2 = Ui_Dialog()
#        self.ui2.setupUi(self)
#        self.setWindowModality(QtCore.Qt.ApplicationModal)

class mywindow(QtWidgets.QMainWindow):
    resized = QtCore.pyqtSignal()
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setWindowTitle("Просмотр маршрутных карт")


        self.show()

        tabl_sp_mk = self.ui.table_mk
        self.spisok_mk()
        tabl_sp_mk.setSelectionBehavior(1)
        tabl_sp_mk.setSelectionMode(1)
        F.ust_cvet_videl_tab(tabl_sp_mk)
        tabl_sp_mk.clicked.connect(self.vibor_mk)
        tabl_sp_mk.doubleClicked.connect(self.dblclk_sp_mk)

        tabl_mk = self.ui.table_mk_view
        tabl_mk.doubleClicked.connect(self.dblclk_mk)
        tabl_mk.setSelectionBehavior(1)
        tabl_mk.setSelectionMode(1)
        F.ust_cvet_videl_tab(tabl_mk)

        lineEdit_mk = self.ui.lineEdit_mk
        lineEdit_mk.textEdited.connect(self.poisk_mk)

        lineEdit_np = self.ui.lineEdit_np
        lineEdit_np.textEdited.connect(self.poisk_np)

        lineEdit_py = self.ui.lineEdit_py
        lineEdit_py.textEdited.connect(self.poisk_py)

        lineEdit_prim = self.ui.lineEdit_prim
        lineEdit_prim.textEdited.connect(self.poisk_prim)

        imgg = self.ui.label_img
        imgg.setScaledContents(True)
        self.fon = QtGui.QPixmap(os.path.join("icons", "001.jpg"))
        self.radius = 30
        self.width = 5
        self.wind_width = 1870
        self.wind_height = 874

        self.wind_k_width = self.fon.width()/self.wind_width
        self.wind_k_height = self.fon.height() / self.wind_height
        self.wind_k_heighth = 0
        self.ris_fona(self.fon)
        combo = self.ui.comboBox
        combo.activated.connect(self.vibor_dse_ineract)

        combo_tara = self.ui.comboBox_tari_rc
        combo_tara.activated.connect(self.vibor_dse_interact_tara_rc)

        but_obnov = self.ui.pushButton_obnov_mk
        but_obnov.clicked.connect(self.obn_mk)

        check_rezjim = self.ui.checkBox_min_rezhjim
        check_rezjim.clicked.connect(self.clck_check_rezjim)

    def clck_check_rezjim(self):
        check_yprosh = self.ui.checkBox_min_rezhjim
        tabl_mk = self.ui.table_mk_view
        if check_yprosh.checkState() == 0:
            for i in range(tabl_mk.rowCount()):
                tabl_mk.setRowHidden(i, False)
            for i in range(tabl_mk.columnCount()):
                if i != 6:
                    tabl_mk.setColumnHidden(i, False)
        else:
            for i in range(tabl_mk.rowCount()):
                flag_kompl = 0
                for j in range(11, tabl_mk.columnCount(), 4):
                    if tabl_mk.item(i, j + 3).text() != '':
                        arr_tmp = tabl_mk.item(i, j + 3).text().split('\n')
                        for k in range(len(arr_tmp)):
                            arr_tmp2 = arr_tmp[k].split(' ')
                            if arr_tmp2[-1] == '' or arr_tmp2[-1] == 'Неисп-мый':
                                flag_kompl = 1
                                break
                    if tabl_mk.item(i, j).text() != '' and 'Полный' not in tabl_mk.item(i, j + 2).text():
                        flag_kompl = 1
                        break
                if flag_kompl == 0:
                    tabl_mk.setRowHidden(i, True)

            for j in range(3, 11):
                tabl_mk.setColumnHidden(j, True)

            for j in range(11, tabl_mk.columnCount(), 4):
                flag_gotova = 1
                for i in range(tabl_mk.rowCount()):
                    if tabl_mk.isRowHidden(i) == False:
                        if tabl_mk.item(i, j).text() != "":
                            if 'олный компл.' not in tabl_mk.item(i, j + 1).text():
                                flag_gotova = 0
                                break
                            if 'олный компл.' not in tabl_mk.item(i, j + 2).text():
                                flag_gotova = 0
                                break
                            if tabl_mk.item(i, j + 3).text() != "":
                                flag_gotova = 0
                                break
                if flag_gotova == 1:
                    tabl_mk.setColumnHidden(j, True)
                    tabl_mk.setColumnHidden(j + 1, True)
                    tabl_mk.setColumnHidden(j + 2, True)
                    tabl_mk.setColumnHidden(j + 3, True)

            for j in range(11, tabl_mk.columnCount(), 4):
                flag_pust = 1
                for i in range(tabl_mk.rowCount()):
                    if tabl_mk.isRowHidden(i) == False:
                        if tabl_mk.item(i, j).text() != '':
                            flag_pust = 0
                            break
                if flag_pust == 1:
                    tabl_mk.setColumnHidden(j, True)
                    tabl_mk.setColumnHidden(j + 1, True)
                    tabl_mk.setColumnHidden(j + 2, True)
                    tabl_mk.setColumnHidden(j + 3, True)


    def obn_mk(self):
        tabl_mk = self.ui.table_mk_view
        nom = tabl_mk.currentRow()
        self.vibor_mk()
        tabl_mk.setCurrentCell(nom,0)

    def sortBy1el(inputStr):
        return inputStr[0]

    def sp_coord_po_rc(self,rc):
        sp_coord = F.otkr_f(F.tcfg('coord_rc'), separ='|')
        if sp_coord == ['']:
            F.msgbox('Не найден файл с координатами')
            return ['']
        for i in range(len(sp_coord)):
            if sp_coord[i][0] == rc:
                return [sp_coord[i][3],sp_coord[i][4]]
        return ['']

    def vibor_dse_ineract(self):
        #определить ид, номер маршуртки
        combo = self.ui.comboBox
        tabl_sp_mk = self.ui.table_mk
        arr = combo.currentText().split('|')
        id = arr[-1]
        if tabl_sp_mk.currentRow() == -1:
            F.msgbox('Не выбрана МК')
            return
        nom_mk = tabl_sp_mk.item(tabl_sp_mk.currentRow(), 0).text()
        #передать занчение для поиска цепочки движения
            #открыть arh_tar.tx, в список все, которые имеют номер наряда
        bd_arh_tar = F.otkr_f(F.tcfg('arh_tar'), separ='|')
        sp_tar_po_mk = []
        sp_tar_po_mk_i_det = []
        itog_sp = []
        for i in range(len(bd_arh_tar)):
            if bd_arh_tar[i][3] == nom_mk:
                sp_tar_po_mk.append(bd_arh_tar[i][0])

            ##по списку поиск в тарах, ид детали
        for i in range(len(sp_tar_po_mk)):
            sp_det = F.otkr_f(F.scfg('arh_tar') + os.sep + sp_tar_po_mk[i] + '.txt', separ='|')
            for j in range(len(sp_det)):
                if sp_det[j][3] == id:
                    sp_tar_po_mk_i_det.append([sp_tar_po_mk[i],sp_det[j][0]])


            #выгрузить из первго списка арх, путь этих тар и даты
        for i in range(len(bd_arh_tar)):
            for k in range(len(sp_tar_po_mk_i_det)):
                if bd_arh_tar[i][0] == sp_tar_po_mk_i_det[k][0]:
                    arr= bd_arh_tar[i][9].split('-->')
                    for j in range(len(arr)):
                        arr2 = arr[j].split('$')
                        sp_coord = self.sp_coord_po_rc(arr2[3])
                        if sp_coord == ['']:
                            F.msgbox('Не найден файл с координамтами')
                            return
                        if len(sp_coord) < 2:
                            F.msgbox('Не найдена координата для ' + bd_arh_tar[2])
                            return
                        # превратьить строку с --> и $ в список рабочих центров.
                        cord_x = sp_coord[0]
                        cord_y = sp_coord[1]
                        itog_sp.append([arr2[1],bd_arh_tar[i][0],sp_tar_po_mk_i_det[k][1],arr2[3],int(cord_x),int(cord_y)])

        if len(itog_sp) == 0:
            imgg = self.ui.label_img
            pixmap = self.fon.scaled(1870, 874).copy()
            imgg.setPixmap(pixmap)
            F.msgbox('Нет перемещений')
            return

            #отсортировать по времени
        itog_sp.sort()

        for i in range(len(itog_sp)):
            for j in range(i+1,len(itog_sp)):
                if itog_sp[i][3] == itog_sp[j][3]:
                    itog_sp[j][4]+=self.radius/2


        self.ris_fona(self.fon,itog_sp)
        sp1 = []
        for i in range(len(itog_sp)):
            if itog_sp[i][1] not in sp1:
                sp1.append(itog_sp[i][1])
        self.ui.comboBox_tari_rc.clear()
        self.ui.comboBox_tari_rc.addItem('')
        for i in sp1:
            text_tara = i
            for j in itog_sp:
                if j[1] == i:
                    text_tara = i + '|' + j[2] + ' шт.' + '|' + j[0]
            self.ui.comboBox_tari_rc.addItem(text_tara)

        self.itog_sp_per_det = itog_sp


    def vibor_dse_interact_tara_rc(self):
        combo_tara = self.ui.comboBox_tari_rc
        arr_tara = combo_tara.currentText().split('|')
        tara = arr_tara[0]
        itog_sp = self.itog_sp_per_det.copy()
        itog_sp_tmp = []
        for i in range(len(itog_sp)):
            if itog_sp[i][1] == tara:
                itog_sp_tmp.append(itog_sp[i])
        self.ris_fona_tara(self.fon, itog_sp_tmp)




    def ris_krug(self,qp,x,y,r):
        qp.setPen(QtGui.QColor(5, 5, 5))
        qp.setBrush(QtGui.QColor(200, 30, 40))
        qp.drawEllipse(int(x-r/2), int(y-r/2), r, r)

    def ris_line(self,qp,x,y,x2,y2):
        if x2 == 0 or y2 == 0:
            return
        pen = QtGui.QPen(QtGui.QColor(200, 30, 40), 5, QtCore.Qt.DotLine)
        pen.setStyle(QtCore.Qt.DashLine)
        qp.setPen(pen)
        qp.setBrush(QtGui.QColor(200, 30, 40))
        qp.drawLine(int(x),int(y),int(x2),int(y2))

    def ris_cifra(self,qp,x,y,text):
        qp.setPen(QtGui.QColor(255, 225, 55))
        razmer = self.radius/2
        qp.setFont(QtGui.QFont('Decorative', int(razmer),5,True))
        qp.drawText(int(x-razmer/2),int(y+razmer/2),str(int(text)))


    def ris_uchastok(self,qp,x1,y1,text,n,x2=0,y2=0,line=True, all = False):
        if all == True:
            self.ris_line(qp, x1, y1, x2, y2)
            self.ris_krug(qp, x1, y1, self.radius)
            self.ris_cifra(qp, x1, y1, text)
            return

        if line == True:
            if n % 2 != 0:
                self.ris_line(qp, x1 - self.radius/2, y1, x2, y2)
        else:
            if n%2 == 0:
                self.ris_krug(qp, x1, y1, self.radius)
                self.ris_cifra(qp, x1, y1, text)


    def ris_fona_tara(self,fon,sp = ('')):
        imgg = self.ui.label_img
        pixmap = fon.scaled(self.wind_width, self.wind_height).copy()
        qpp = QtGui.QPainter(pixmap)
        nom = 1
        for i in range(len(sp)):
            x = sp[i][4] / self.wind_k_width
            y = sp[i][5] / self.wind_k_height
            x2 = 0
            y2 = 0
            if i < len(sp) - 1:
                x2 = sp[i + 1][4] / self.wind_k_width
                y2 = sp[i + 1][5] / self.wind_k_height
            self.ris_uchastok(qpp, x, y, nom, i, x2, y2, True, all=True)
            nom += 1
        qpp.end()
        imgg.setPixmap(pixmap)


    def ris_fona(self,fon,sp = ('')):
        imgg = self.ui.label_img

        pixmap = fon.scaled(self.wind_width,self.wind_height).copy()
        qpp = QtGui.QPainter(pixmap)
        nom = 1
        for i in range(len(sp)):
            x = sp[i][4] /self.wind_k_width
            y = sp[i][5] /self.wind_k_height
            x2 = 0
            y2 = 0
            if i < len(sp)-1:
                x2 = sp[i + 1][4] /self.wind_k_width
                y2 = sp[i + 1][5] /self.wind_k_height
            self.ris_uchastok(qpp,x,y,nom,i,x2,y2,True)
            nom+=0.5
        nom = 1
        for i in range(len(sp)):
            x = sp[i][4] /self.wind_k_width
            y = sp[i][5] /self.wind_k_height
            x2 = 0
            y2 = 0
            if i < len(sp)-1:
                x2 = sp[i + 1][4] /self.wind_k_width
                y2 = sp[i + 1][5] /self.wind_k_height
            self.ris_uchastok(qpp,x,y,nom,i,x2,y2,False)
            nom+=0.5
        qpp.end()
        imgg.setPixmap(pixmap)

    #def paintEvent(self, e):
    #    qp = QtGui.QPainter()
    #    qp.begin(self)
    #    self.ris_krug(qp)
    #    qp.end()

    def dblclk_sp_mk(self):
        self.spisok_mk()

    def dblclk_mk(self):
        tabl_mk = self.ui.table_mk_view
        r = tabl_mk.currentRow()
        k = tabl_mk.currentColumn()
        if k >10 and (k-11)%4==0:
            self.vigruz_tehkart(r,k)
        if k >10 and (k-12)%4==0:
            self.vigruz_tara(r,k)
        if k >10 and (k-13)%4==0:
            self.vigruz_narad(r,k)
        if k < 11:
            self.vigruz_vizual(r,k)
    def vigruz_vizual(self,r,k):
        tabl_mk = self.ui.table_mk_view
        if tabl_mk.item(r, k).text() == "":
            return
        tabl_sp_mk = self.ui.table_mk
        combobox = self.ui.comboBox
        id = tabl_mk.item(r, 6).text().strip()

        for i in range(combobox.count()):
            arr = combobox.itemText(i).split('|')
            if arr[-1] == id:
                combobox.setCurrentIndex(i)
                self.ui.tabWidget.setCurrentIndex(1)
                self.vibor_dse_ineract()
        return

    def vigruz_narad(self, r, k):
        tabl_mk = self.ui.table_mk_view
        if tabl_mk.item(r, k).text() == "":
            return
        tabl_sp_mk = self.ui.table_mk
        id = tabl_mk.item(r, 6).text().strip()
        arr = tabl_mk.item(r, k).text().split('\n')
        sp_nar = F.otkr_f(F.tcfg('Naryad'), separ='|')
        sp_jur = F.otkr_f(F.tcfg('BDzhurnal'), separ='|')
        s= ''
        for i in range(len(arr)):
            arr2 = arr[i].split(' ')
            nom_nar = arr2[0]
            dop = ''
            if arr2[-1] == "Завершен":
                for k in range(len(sp_jur)-1,-1,-1):
                    if sp_jur[k][2] == nom_nar and sp_jur[k][7] == 'Завершен':
                        dop = sp_jur[k][8] + ' ' + sp_jur[k][9] + '\n'
            for j in range(1,len(sp_nar)):
                if sp_nar[j][0] == nom_nar:
                    s += nom_nar + ' выдан ' + sp_nar[j][2] + ' ' + sp_nar[j][7] + ' на ' + sp_nar[j][9] + \
                         ' для :' + '\n' + '    ' + sp_nar[j][17] + ','+ sp_nar[j][18] + '\n' + dop + '\n'
        showDialog(self, s)
        return

    def vigruz_tara(self, r, k):
        tabl_mk = self.ui.table_mk_view
        if tabl_mk.item(r, k).text() == "":
            return
        tabl_sp_mk = self.ui.table_mk

        id = tabl_mk.item(r, 6).text().strip()

        nom_mk = tabl_sp_mk.item(tabl_sp_mk.currentRow(), 0).text()
        bd_arh_tar = F.otkr_f(F.tcfg('arh_tar'), separ='|')
        s = ''
        for i in bd_arh_tar:
            if i[3] == nom_mk:
                sost = i[6]
                nom = i[0]
                marsh = i[9]
                nazv = i[5]
                det_tmp = F.otkr_f(F.scfg('bd_tara') + os.sep + nom + '.txt', separ='|')
                for i in range(0, len(det_tmp)):
                    if det_tmp[i][3].strip() == id:
                        s += sost + ' ' + nom + ' ' + nazv + '\n' + marsh.replace('$',' ') + '\n' + '\n'
        showDialog(self, s)
        return

    def vigruz_tehkart(self,r,k):
        tabl_mk = self.ui.table_mk_view
        if tabl_mk.item(r, k).text() == "":
            return
        tmp = tabl_mk.item(r, k).text().split('Операции:')
        sp_op = tmp[-1].split(';')
        if F.nalich_file(F.tcfg('BD_dse')) == False:
            showDialog(self, 'Не найден BD_dse')
            return
        sp_dse = F.otkr_f(F.tcfg('BD_dse'), False, '|')
        naim = tabl_mk.item(r, 0).text().strip()
        nn = tabl_mk.item(r, 1).text().strip()
        for i in range(0, len(sp_dse)):
            if sp_dse[i][0] == nn and sp_dse[i][1] == naim:
                nom_tk = sp_dse[i][2]
                if nom_tk == '':
                    showDialog(self, 'Не найден номер ТК')
                    return
                break
        if F.nalich_file(F.scfg('add_docs') + os.sep + nom_tk + '_' + nn + '.pickle') == False:
            showDialog(self, 'Не найден файл ТК')
            return
        sp_tk = F.otkr_f(F.scfg('add_docs') + os.sep + nom_tk + '_' + nn + '.pickle', False, "|")
        msgg = ''
        for o1 in sp_op:
            msgg += str(o1) + ': '
            for i in range(11, len(sp_tk)):
                if sp_tk[i][3].startswith('Т1-' + str(o1).strip()) == True:
                    if sp_tk[i][20] == '1':
                        msgg += sp_tk[i][0] + '\n' + ' Tп.з.=' + sp_tk[i][6] + ' Tшт.=' + sp_tk[i][7] + '\n'
                    else:
                        msgg += sp_tk[i][0] + '\n'
            msgg += '\n'
        showDialog(self, msgg)

    def poisk_mk(self):
        obr = self.ui.lineEdit_mk.text()
        self.poisk_strok(F.nom_kol_po_imen(self.ui.table_mk,'Номер'),obr)
    def poisk_np(self):
        obr = self.ui.lineEdit_np.text()
        self.poisk_strok(F.nom_kol_po_imen(self.ui.table_mk,'Номер проекта'),obr)
    def poisk_py(self):
        obr = self.ui.lineEdit_py.text()
        self.poisk_strok(F.nom_kol_po_imen(self.ui.table_mk,'Номер заказа'),obr)
    def poisk_prim(self):
        obr = self.ui.lineEdit_prim.text()
        self.poisk_strok(F.nom_kol_po_imen(self.ui.table_mk,'Примечание'),obr)

    def poisk_strok(self, kol, obr):
        tabl_sp_mk = self.ui.table_mk
        if obr == "":
            return
        for i in range(0,tabl_sp_mk.rowCount()):
            if obr.upper() in F.cells(i,kol,tabl_sp_mk).upper():
                tabl_sp_mk.selectRow(i)
                return

    def vibor_mk(self):
        tabl_mk = self.ui.table_mk_view
        tabl_sp_mk = self.ui.table_mk
        combo = self.ui.comboBox
        nom = tabl_sp_mk.item(tabl_sp_mk.currentRow(),0).text()
        if F.nalich_file(F.scfg('mk_data') + os.sep + nom + '.txt') == False:
            showDialog(self, 'Не обнаржен файл')
            return
        sp = F.otkr_f(F.scfg('mk_data') + os.sep + nom + '.txt',False,'|')
        if sp == []:
            showDialog(self, 'Некорректное содержимое МК')
            return
        sp = self.oformlenie_sp_pod_mk(sp)
        if sp == False:
            return
        F.zapoln_wtabl(self, sp, tabl_mk, 0, 0, '', '', 200, True, '', 65)
        self.oform_mk(sp,nom)
        combo.clear()
        for i in range(len(sp)):
            combo.addItem(sp[i][0] + '  ' + sp[i][1] + '|' + sp[i][6])
        combo.setMaxVisibleItems(combo.maxCount())



    def uroven(self,strok):
        n = 0
        for i in range(0,len(strok)):
            if strok[i] == " ":
                n+=1
            else:
                break
        return int(n/4)

    def oform_mk(self, sp, nom_mk):
        shag = 15
        tabl_mk = self.ui.table_mk_view
        tabl_sp_mk = self.ui.table_mk

        maxs = set()
        for i in range(1, len(sp)):
            maxs.add(self.uroven(sp[i][0]))
        maxc = max(maxs)
        for i in range(1, len(sp)):
            uroven = self.uroven(sp[i][0])
            for j in range(0, len(sp[i])):
                F.dob_color_wtab(tabl_mk, i - 1, j, 0, 0, shag * maxc - shag * uroven)
        for i in range(1, len(sp)):
            for j in range(11, len(sp[i]), 4):
                F.dob_color_wtab(tabl_mk, i - 1, j, 10, 10, 10)
                if sp[i][j] == '':
                    for k in range(1, 4):
                        F.dob_color_wtab(tabl_mk, i - 1, j + k, 10, 10, 10)
        tabl_mk.setColumnHidden(6, True)
        # komplekt
        for i in range(1, len(sp)):
            for j in range(12, len(sp[i]), 4):
                if tabl_mk.item(i - 1, j).text() != '':
                    if '(полный' in tabl_mk.item(i - 1, j).text():
                        F.dob_color_wtab(tabl_mk, i - 1, j, 0, 127, 0)
                    else:
                        F.dob_color_wtab(tabl_mk, i - 1, j, 37, 17, 0)
                if tabl_mk.item(i - 1, j + 1).text() != '':
                    arr = tabl_mk.item(i - 1, j + 1).text().strip().split('\n')
                    set_sost = set()
                    for k in range(len(arr)):
                        arr2 = arr[k].split(' ')
                        set_sost.add(arr2[1])
                    if 'компл.' in set_sost:
                        F.dob_color_wtab(tabl_mk, i - 1, j + 1, 0, 127, 0)  # зеленый
                    elif len(set_sost) == 1 and 'Выдан' in set_sost:
                        pass
                    elif len(set_sost) == 1 and 'Создан' in set_sost:
                        pass
                    else:
                        F.dob_color_wtab(tabl_mk, i - 1, j + 1, 37, 17, 0)  # оранж
                if tabl_mk.item(i - 1, j + 2).text() != '':
                    arr = tabl_mk.item(i - 1, j + 2).text().strip().split('\n')
                    set_sost = set()
                    for k in range(len(arr)):
                        arr2 = arr[k].split(' ')
                        if len(arr2) == 1:
                            set_sost.add('')
                        else:
                            set_sost.add(arr2[1])
                    if len(set_sost) == 1 and 'Исправлен' in set_sost:
                        F.dob_color_wtab(tabl_mk, i - 1, j + 2, 0, 127, 0)  # зеленый
                    if len(set_sost) == 1 and 'Изгот.вновь' in set_sost:
                        F.dob_color_wtab(tabl_mk, i - 1, j + 2, 0, 127, 0)  # зеленый
                    if len(set_sost) == 2 and 'Изгот.вновь' in set_sost and 'Исправлен' in set_sost:
                        F.dob_color_wtab(tabl_mk, i - 1, j + 2, 0, 127, 0)  # зеленый
                    if 'Неисп-мый' in set_sost:
                        F.dob_color_wtab(tabl_mk, i - 1, j + 2, 200, 10, 10)  # красный
                    else:
                        F.dob_color_wtab(tabl_mk, i - 1, j + 2, 37, 17, 0)  # оранж

    def max_det_skompl(self,nom_op,id_dse):
        tabl_mk = self.ui.table_mk_view
        for j in range(tabl_mk.rowCount()):
            if tabl_mk.item(j,6).text() == id_dse:
                for i in range(11,tabl_mk.columnCount(),4):
                    if tabl_mk.item(j, i).text().strip() != '':
                        obr = tabl_mk.item(j, i).text().strip().split('Операции:\n')
                        obr2 = obr[-1].split(";")
                        if str(nom_op) in obr2:
                            if tabl_mk.item(j, i+1).text().strip() == '':
                                return 0
                            kompl = tabl_mk.item(j, i+1).text().strip().split(' шт.')
                            return int(kompl[0])


    def summ_dost_det_po_nar(self, nom_mar, id_dse, nom_op, zakr=False):
        tabl_mk = self.ui.table_mk_view
        sp_nar = F.otkr_f(F.tcfg('Naryad'), False, '|')
        sp_zhur = F.otkr_f(F.tcfg('BDzhurnal'), False, '|')
        if sp_nar == ['']:
            showDialog(self, 'Не найдена база с нарядами')
            return
        max_det = self.max_det_skompl(nom_op, id_dse)
        summ_det = 0
        for i in range(len(sp_nar)):
            if sp_nar[i][1] == nom_mar and sp_nar[i][25] == id_dse and sp_nar[i][24] == nom_op and sp_nar[i][21] == '':
                if zakr == True:
                    mn = []
                    flag = 1
                    for j in range(len(sp_zhur)):
                        if sp_zhur[j][2] == sp_nar[i][0]:
                            mn.append(sp_zhur[j][3])
                    if len(mn) > 0:
                        mn = set(mn)
                        mn = list(mn)
                        for j in range(len(sp_zhur)):
                            if sp_zhur[j][2] == sp_nar[i][0] and sp_zhur[j][7] == 'Завершен':
                                if sp_zhur[j][3] in mn:
                                    mn.remove(sp_zhur[j][3])
                            if len(mn) == 0:
                                flag = 0
                                break
                        if flag == 0:
                            summ_det += F.valm(sp_nar[i][12].strip())
                else:
                    summ_det += F.valm(sp_nar[i][12].strip())
        if max_det - summ_det < 0:
            return 0
        return max_det - summ_det

    def oformlenie_sp_pod_mk(self,s):
        try:
            for j in s:
                for i in range(11, len(s[0]),4):
                    if '$' in j[i]:
                        vrem, oper1, oper2 = [x for x in j[i].split("$")]
                        j[i] = vrem + '\n' + oper1 + '\n' + oper2
                for i in range(13, len(s[0]),4):
                    if '$' in j[i]:
                        j[i] = j[i].replace('$','\n')
                for i in range(14, len(s[0]), 4):
                    if '$' in j[i]:
                        j[i] = j[i].replace('$', '\n')
            return s
        except:
            F.msgbox('Ошибка формирования МК')
            return False

    def spisok_mk(self):
        tabl_sp_mk = self.ui.table_mk
        if F.nalich_file(F.tcfg('bd_mk')) == False:
            showDialog(self, 'Не найден bd_mk')
            return
        sp = F.otkr_f(F.tcfg('bd_mk'),separ='|')
        F.zapoln_wtabl(self,sp,tabl_sp_mk,0,0,'','',200,True,'',10)


app = QtWidgets.QApplication([])

myappid = 'Powerz.BAG.SustControlWork.0.0.0'  # !!!
QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
app.setWindowIcon(QtGui.QIcon(os.path.join("icons", "icon.png")))

S = F.scfg('Stile').split(",")
app.setStyle(S[1])

application = mywindow()
application.show()

sys.exit(app.exec())