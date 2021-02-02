import Cust_Functions as F

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWinExtras import QtWin
import os
import time
import subprocess
from mydesign import Ui_MainWindow  # импорт нашего сгенерированного файла
#from mydesign2 import Ui_Dialog  # импорт нашего сгенерированного файла
import sys

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

    def vigruz_narad(self, r, k):
        tabl_mk = self.ui.table_mk_view
        if tabl_mk.item(r, k).text() == "":
            return
        tabl_sp_mk = self.ui.table_mk
        id = tabl_mk.item(r, 6).text().strip()
        nom_mk = tabl_sp_mk.item(tabl_sp_mk.currentRow(), 0).text()
        arr = tabl_mk.item(r, k).text().split('\n')
        sp_nar = F.otkr_f(F.tcfg('Naryad'), separ='|')
        s= ''
        for i in range(len(arr)):
            arr2 = arr[i].split(' ')
            nom_nar = arr2[0]
            for j in range(1,len(sp_nar)):
                if sp_nar[j][0] == nom_nar:
                    s += nom_nar + ' выдан ' + sp_nar[j][2] + ' ' + sp_nar[j][7] + ' на ' + sp_nar[j][9] + \
                         ' для :' + '\n' + '    ' + sp_nar[j][17] + ','+ sp_nar[j][18] + '\n' + '\n'
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
        if F.nalich_file(F.scfg('add_docs') + os.sep + nom_tk + '_' + nn + '.txt') == False:
            showDialog(self, 'Не найден файл ТК')
            return
        sp_tk = F.otkr_f(F.scfg('add_docs') + os.sep + nom_tk + '_' + nn + '.txt', False, "|")
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
        self.poisk_strok(0,obr)
    def poisk_np(self):
        obr = self.ui.lineEdit_np.text()
        self.poisk_strok(3,obr)
    def poisk_py(self):
        obr = self.ui.lineEdit_py.text()
        self.poisk_strok(4,obr)
    def poisk_prim(self):
        obr = self.ui.lineEdit_prim.text()
        self.poisk_strok(5,obr)

    def poisk_strok(self, kol, obr):
        tabl_sp_mk = self.ui.table_mk
        if obr == "":
            return
        for i in range(0,tabl_sp_mk.rowCount()):
            if F.cells(i,kol,tabl_sp_mk).upper().startswith(obr.upper()) == True:
                tabl_sp_mk.selectRow(i)
                return

    def vibor_mk(self):
        tabl_mk = self.ui.table_mk_view
        tabl_sp_mk = self.ui.table_mk
        nom = tabl_sp_mk.item(tabl_sp_mk.currentRow(),0).text()
        if F.nalich_file(F.scfg('mk_data') + os.sep + nom + '.txt') == False:
            showDialog(self, 'Не обнаржен файл')
            return
        sp = F.otkr_f(F.scfg('mk_data') + os.sep + nom + '.txt',False,'|')
        if sp == []:
            showDialog(self, 'Некорректное содержимое МК')
            return
        sp = self.oformlenie_sp_pod_mk(sp)
        F.zapoln_wtabl(self, sp, tabl_mk, 0, 0, '', '', 200, True, '', 65)
        self.oform_mk(sp)



    def uroven(self,strok):
        n = 0
        for i in range(0,len(strok)):
            if strok[i] == " ":
                n+=1
            else:
                break
        return int(n/4)


    def oform_mk(self,sp):
        shag = 15
        tabl_mk = self.ui.table_mk_view
        tabl_sp_mk = self.ui.table_mk

        maxs = set()
        for i in range(1,len(sp)):
            maxs.add(self.uroven(sp[i][0]))
        maxc = max(maxs)
        for i in range(1,len(sp)):
            uroven = self.uroven(sp[i][0])
            for j in range(0, len(sp[i])):
                F.dob_color_wtab(tabl_mk,i-1,j,0,0,shag*maxc-shag*uroven)
        for i in range(1, len(sp)):
            for j in range(11, len(sp[i]),4):
                F.dob_color_wtab(tabl_mk, i - 1, j, 10, 10, 10)
        tabl_mk.setColumnHidden(6,True)
        #komplekt
        for i in range(1, len(sp)):
            for j in range(12, len(sp[i]), 4):
                if tabl_mk.item(i - 1,j).text() != '':
                    if '(полный' in tabl_mk.item(i - 1,j).text():
                        F.dob_color_wtab(tabl_mk, i - 1, j, 0, 127, 0)
                    else:
                        F.dob_color_wtab(tabl_mk, i - 1, j, 37, 17, 0)
                if tabl_mk.item(i - 1, j+1).text() != '':
                    arr = tabl_mk.item(i - 1, j+1).text().strip().split('\n')
                    flag = 0
                    set_sost = set()
                    for k in range(len(arr)):
                        arr2 = arr[k].split(' ')
                        set_sost.add(arr2[1])
                    if len(set_sost) == 1 and 'Завершен' in set_sost:
                        flag = 2
                    elif len(set_sost) == 1 and 'Выдан' in set_sost:
                        flag = 0
                    else:
                        flag = 1

                    if flag == 1:# оранж
                        F.dob_color_wtab(tabl_mk, i - 1, j+1, 37, 17, 0)
                    if flag == 0:
                        if tabl_mk.currentRow() == -1:
                            showDialog(self, 'Не выбрана дсе')
                            return
                        if tabl_sp_mk.currentRow() == -1:
                            showDialog(self, 'Не выбрана мк')
                            return
                    nom_mk = tabl_sp_mk.item(tabl_sp_mk.currentRow(), 0).text()
                    id_dse = tabl_mk.item(i - 1, 6).text()
                    arr_op = tabl_mk.item(i - 1, j - 1).text()
                    arr_op2 = arr_op.split('Операции:\n')
                    obr = arr_op2[-1].split(";")
                    ostatok = 0
                    for op in obr:
                        nom_op = op
                        ostatok += self.summ_dost_det_po_nar(nom_mk, id_dse, nom_op)  # зеленый
                    if ostatok <= 0:
                        F.dob_color_wtab(tabl_mk, i - 1, j + 1, 0, 127, 0)  # зеленый

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
        for j in s:
            for i in range(11, len(s[0]),4):
                if '$' in j[i]:
                    vrem, oper1, oper2 = [x for x in j[i].split("$")]
                    j[i] = vrem + '\n' + oper1 + '\n' + oper2
            for i in range(13, len(s[0]),4):
                if '$' in j[i]:
                    j[i] = j[i].replace('$','\n')
        return s

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