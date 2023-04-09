from PyQt5 import QtWidgets, QtGui, QtCore,QtWebEngineWidgets
from PyQt5.QtWinExtras import QtWin
import os
import project_cust_38.Cust_Qt as CQT
CQT.conver_ui_v_py()
from mydesign import Ui_MainWindow  # импорт нашего сгенерированного файла
import config
import sys
import project_cust_38.Cust_Functions as F
import project_cust_38.Cust_mes as CMS
import project_cust_38.Cust_SQLite as CSQ
import project_cust_38.Cust_Excel as CEX
import project_cust_38.otcheti as OTCH
from datetime import datetime as DT, timedelta

cfg = config.Config('Config\CFG.cfg')  # файл конфига, находится п папке конфиг

F.test_path()

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.versia = '1.5.3'
        #=================add_ui=========================
        self.parent_for_grafic = self.ui.verticalLayout_8
        #===========================================connects
        self.bd_naryad = F.bdcfg('Naryad')
        self.bd_act = F.bdcfg('BDact')
        self.bd_users = F.bdcfg('BD_users')
        self.bd_mat = F.bdcfg('nomenklatura_erp')
        self.bd_selector = F.bdcfg('BD_selector')
        self.db_dse = F.bdcfg('BD_dse')
        self.db_resxml = F.bdcfg('db_resxml')
        self.db_kplan = F.bdcfg('DB_kplan')
        self.files_tmp = F.scfg('files_tmp')
        #==================BTN
        self.ui.btn_otchet.clicked.connect(lambda _, x=self: OTCH.otchet(x))
        self.ui.btn_grafic_load.clicked.connect(lambda _, x=self: OTCH.create_gant(x))
        self.ui.btn_save_txt.clicked.connect(self.save_txt)
        self.ui.btn_udown.clicked.connect(self.up_down)
        #==================lines

        #==================TABLES
        self.ui.tbl_mk.setSelectionBehavior(1)
        self.ui.tbl_mk.setSelectionMode(1)
        self.ui.tbl_mk.currentItemChanged.connect(self.select_mk)
        self.ui.tbl_jur.setSelectionBehavior(1)
        self.ui.tbl_jur.setSelectionMode(1)
        self.ui.tbl_jur.currentItemChanged.connect(self.select_jur)
        self.ui.tbl_otchet.doubleClicked.connect(lambda _, x=self: OTCH.dbl_clck_otch(x))
        self.ui.tbl_otchet.clicked.connect(lambda: OTCH.clck_otch(self))
        #==================TABS
        self.ui.tabWidget.currentChanged[int].connect(self.tab_click)
        #===================CHECKBOX

        #===================COMBOBOX
        self.ui.cmb_vid_otcheta.activated.connect(lambda _, x=self: OTCH.vibor_vid_otcheta(x))
        self.ui.cmb_napr.activated.connect(self.vibor_napravl)
        self.ui.cmb_gant_vert.activated.connect(lambda _, x=self: OTCH.vibor_pole_gant(x))
        #===================RADIOBOX

        # ================CALENDAR===================================
        self.ui.calendarWidget.clicked.connect(lambda _, x=self: OTCH.calendar_click(x))
        #++++++++++++++++++++++++++++++++++++++++++++

        #==== GLOBALS
        self.plan_for_gant = ''
        #======ACTIONS
        self.ui.actionexcel.triggered.connect(self.export_table)
        self.ui.action_txt.triggered.connect(self.export_table_txt)
        #=======loads
        self.LIST_ED_IZM_MAT = ['Килограмм', 'кг']
        self.LIST_VID_MAT = ['Отводы',
                        'Переходы',
                        'Тройники',
                        'Трубопроводная арматура',
                        'Фланцы',
                        'Штуцера',
                        'Паронит ГОСТ 481-80',
                        'Фторопласт',
                        'Шнуры',
                        'Труба ГОСТ 9941-81 (нерж)',
                        'Труба квадратная (10,01)',
                        'Трубы по ГОСТ (10,01)',
                        'Трубы по ТУ (10,01)',
                        'Шпилька  ГОСТ 22042',
                        'Шпилька ГОСТ 9066 (без шаблона)',
                        'Шпилька для фланцевых соединений ГОСТ 9066',
                        'Шпильки DIN 975',
                        'Двутавр (10,01)',
                        'Зубчатые рейки (10.01)',
                        'Квадрат (10,01)',
                        'Круги (10,01)',
                        'Листовой металл (10,01)',
                        'Прутки (10,01)',
                        'Уголок (10,01)',
                        'Швеллер (10,01)',
                        'Шестигранник (10,01)',
                        ]
        #self.app_icons()
        CMS.dict_etapi(self,self.bd_naryad)
        CMS.dict_emploee_rc(self)
        CMS.dict_rc_po_oper(self,self.bd_naryad)
        CMS.dict_rc(self,self.bd_users)
        CMS.dict_professions(self, self.bd_users)
        CMS.dict_napravl(self, self.db_kplan)
        CMS.dict_opers(self,self.bd_naryad)
        self.DICT_EMPLOEE = CMS.dict_emploee(self.bd_users)
        self.DICT_EMPLOEE_FULL = CMS.dict_emploee_full(self.bd_users)
        self.DICT_MK = CSQ.zapros(self.bd_naryad,f"""SELECT Пномер, Номер_заказа || "$" || Номер_проекта as NPPY FROM mk""",rez_dict=True)
        self.DICT_MK = F.raskrit_dict(self.DICT_MK,'NPPY')
        self.LIST_ZAMECH = self.load_zamech()
        self.DICT_KOD_VP =F.raskrit_dict(CSQ.zapros(self.bd_naryad,f"""SELECT * FROM kod_zamech_vp""",rez_dict=True),'Имя')
        self.setWindowTitle('Просмотр')
        self.ui.cmb_vid_otcheta.addItem('')
        spis_vid_otcheta = ['Трудозатраты',
                            'О выработке сотрудников за месяц',
                            'Текущие работы',
                            'Выработка цеха по виду',
                            'Выработка цеха по направлению',
                            'Журнал работ',
                            'Внеплановые работы',
                            'Выработка сотрудника',
                            'Выработка сотрудников',
                            'Понедельный график выработки и отгрузок',
                            'Выработка цеха понарядно',
                            'Статистика нормо-весовых харктеристик МК',
                            'План-фактный анализ по месяцам',
                            'План работ',
                            'Селекторное',
                            'Неосвоенный_вес_по_созданным_нарядам',
                            'Норматив материалов по завершенным нарядам',
                            'Журнал_техкарт',
                            'Журнал_замечаний']
        for otchet in spis_vid_otcheta:
            self.ui.cmb_vid_otcheta.addItem(otchet)


        spis_napravl = list(self.DICT_NAPRAVL.keys())
        for napravl in spis_napravl:
            self.ui.cmb_napr.addItem(napravl)
        self.ui.btn_save_txt.setDisabled(True)
        self.vid_otcheta = ''
        CQT.load_icons(self)
        CQT.load_css(self)
        #============DB
        #====ВРЕМЕННО


    def up_down(self):
        fr =self.ui.fr_cal
        btn = self.ui.btn_udown
        if fr.isHidden():
            btn.setText('/\\')
            fr.setHidden(False)
        else:
            btn.setText(r'\/')
            fr.setHidden(True)


    def save_txt(self):
        def check_save_txt_trdzt(self):
            count_err = 0
            list = CQT.spisok_iz_wtabl(self.ui.tbl_otchet, sep='', shapka=True, rez_dict=True)
            for item in list:
                val_of_proc = F.valm(item['Соответствие_%'])
                if val_of_proc < self.PROC_OTKL_TRUDOZATRAT[0] or val_of_proc > self.PROC_OTKL_TRUDOZATRAT[1]:
                    count_err += 1
            if count_err:
                CQT.msgbox(
                    f'{count_err} значений выходят за диапазон от {self.PROC_OTKL_TRUDOZATRAT[0]} до {self.PROC_OTKL_TRUDOZATRAT[1]}, необходимо править наряды/табель')
                return False
            return True

        if self.vid_otcheta == 'Трудозатраты':
            if not check_save_txt_trdzt(self):
                return
            rab_centr = self.ui.cmb_podrazdelenie.currentText().split('|')[0]
            list = CQT.spisok_iz_wtabl(self.ui.tbl_otchet, sep='', shapka=True, rez_dict=True)
            list_users = [_['ФИО'] for _ in list]
            CMS.vigruzka_trudozatrat_2(self,self.ui.le_nach_per.text(),self.ui.le_konec_per.text(),list_users,rab_centr,'','')


    def generate_list_plan(self,rez_list):
        plan = []
        if rez_list == None:
            return
        for deistvie in rez_list:
            plan.append([])
            if plan == [[]]:
                for key in deistvie.keys():
                    for key2 in deistvie[key].keys():
                        plan[0].append(key2)
                plan.append([])
                len_shapka = len(plan[0])
            for key in deistvie.keys():
                for key2 in deistvie[key].keys():
                    plan[-1].append(str(deistvie[key][key2]))
                if len(plan[-1]) < len_shapka:
                    for i in range(len_shapka - len(plan[-1])):
                        plan[0].append('')
        return plan

    def save_excell_plan(self,rez_list, path, name):
        if rez_list == None:
            return
        plan = self.generate_list_plan(rez_list)
        CEX.zap_spis(plan,path,name,'1',1,1)


    def keyReleaseEvent(self, e):
        if e.key() == 67 and e.modifiers() == (QtCore.Qt.ControlModifier | QtCore.Qt.ShiftModifier):
            if CQT.focus_is_QTableWidget():
                CQT.copy_bufer_table(QtWidgets.QApplication.focusWidget())
        if self.ui.tbl_filtr_dse.hasFocus():
            if e.key() == 16777220:
                CMS.primenit_filtr(self,self.ui.tbl_filtr_dse,self.ui.tbl_dse)
        if self.ui.tbl_zamech_filtr.hasFocus():
            if e.key() == 16777220:
                CMS.primenit_filtr(self, self.ui.tbl_zamech_filtr, self.ui.tbl_zamech)
        if self.ui.tbl_otchet_filtr.hasFocus():
            if e.key() == 16777220:
                CMS.primenit_filtr(self, self.ui.tbl_otchet_filtr, self.ui.tbl_otchet)
                if self.ui.cmb_vid_otcheta.currentText() == 'Журнал работ':
                    CMS.primenit_summ(self,self.ui.tbl_otchet)
                if self.ui.cmb_vid_otcheta.currentText() == 'Выработка цеха понарядно':
                    CMS.primenit_summ(self,self.ui.tbl_otchet)
                if self.ui.cmb_vid_otcheta.currentText() == 'Выработка сотрудника':
                    CMS.primenit_summ(self, self.ui.tbl_otchet)
                if self.ui.cmb_vid_otcheta.currentText() == 'Понедельный график выработки и отгрузок':
                    CMS.primenit_summ(self, self.ui.tbl_otchet,sredn=True)
                if self.ui.cmb_vid_otcheta.currentText() == 'Статистика нормо-весовых харктеристик МК':
                    CMS.primenit_summ(self, self.ui.tbl_otchet,sredn=True)
                if self.ui.cmb_vid_otcheta.currentText() == 'План работ':
                    CMS.primenit_summ(self, self.ui.tbl_otchet, sredn=True)
                if self.ui.cmb_vid_otcheta.currentText() == 'Норматив материалов по завершенным нарядам':
                    CMS.primenit_summ(self, self.ui.tbl_otchet, sredn=True)
                if self.ui.cmb_vid_otcheta.currentText() == 'Журнал_техкарт':
                    CMS.primenit_summ(self, self.ui.tbl_otchet, sredn=True)
                if self.ui.cmb_vid_otcheta.currentText() == 'Журнал_замечаний':
                    CMS.primenit_summ(self, self.ui.tbl_otchet, sredn=True)
                self.ui.tbl_otchet.isRowHidden(1)
        if self.ui.tbl_mk_filtr.hasFocus():
            if e.key() == 16777220:
                CMS.primenit_filtr(self, self.ui.tbl_mk_filtr, self.ui.tbl_mk)
        if self.ui.tbl_jur_filtr.hasFocus():
            if e.key() == 16777220:
                CMS.primenit_filtr(self, self.ui.tbl_jur_filtr, self.ui.tbl_jur)

    def tab_click(self, ind):
        tab = self.ui.tabWidget
        if tab.tabText(ind) == 'Отчеты':
            dat = F.datetostr(DT.today() - timedelta(days =7))
            konec = F.nach_kon_date(date=dat, vid='n')[1]
            nach = F.nach_kon_date(date=dat, vid='n')[0]
            self.ui.le_konec_per.setText(konec)
            self.ui.le_nach_per.setText(nach)
            CQT.clear_tbl(self.ui.tbl_otchet)
            CQT.clear_tbl(self.ui.tbl_otchet_filtr)

    def OTCH_otchet(self,val):
        pass

    def raschet_etapa(self, fio):
        for key in self.DICT_EMPLOEE_RC:
            if fio in key:
                return self.DICT_EMPLOEE_RC[key]
        return

    def fill_dse(self):
        tbl_mk = self.ui.tbl_mk
        nk_nom_mk = CQT.nom_kol_po_imen(tbl_mk,'Пномер')

        r = tbl_mk.currentRow()
        nom_mk = int(tbl_mk.item(r,nk_nom_mk).text())
        if nom_mk == 0:
            return
        self.glob_nom_mk = nom_mk
        if nom_mk not in self.dict_res:
            CQT.msgbox(f'Ресурная не найдена')
            return
        res = F.from_binary_pickle(self.dict_res[nom_mk])

        if res == '':
            conn_res, cur_res = CSQ.connect_bd(self.db_resxml)
            res = CMS.load_res(nom_mk, conn=conn_res, cur=cur_res)
            CSQ.close_bd(conn_res, cur_res)


        # print(filtr)
        tabl_dse = self.ui.tbl_dse


        spis_shap_mk = [
            ['Чек', "Наименование", "Обозначение", "В работу,шт.", 'Уровень', "Количество,шт.", "Освоено,шт.",
             'Закрыто,шт.',
             'Ном_оп', "Операция",
             "Масса/М1,М2,М3", "Ссылка", "ID",
             "Примечание", "ПКИ", "Тпз", "Тшт", 'РЦ', 'Оборудование', "Профессия", "Вид_работ",
             "КР", "КОИД", "Документы", 'Переходы']]
        spis_shab_mk = []

        set_etapi = set()
        for i, dse in enumerate(res):
            naim = CMS.uroven_oform(dse['Наименование'], dse['Уровень'])
            nn = CMS.uroven_oform(dse['Номенклатурный_номер'], dse['Уровень'])
            kolich = dse['Количество']
            mat = dse['Мат_кд']
            ssil = dse['Ссылка']
            id = dse['Номерпп']
            prim = dse['Прим']
            pki = dse['ПКИ']
            ur = dse['Уровень']

            for j, oper in enumerate(dse['Операции']):
                if 'Освоено,шт.' not in oper:
                    res[i]['Операции'][j]['Освоено,шт.'] = 0
                if 'Закрыто,шт.' not in oper:
                    res[i]['Операции'][j]['Закрыто,шт.'] = 0
                flag_strukturn_dostup = True
                # print(flag_strukturn_dostup)
                if flag_strukturn_dostup:
                    zakrito = oper['Закрыто,шт.']
                    osvoeno = oper['Освоено,шт.']
                    oper_naim = oper['Опер_наименовние']
                    oper_nom = oper['Опер_номер']
                    oper_rc_kod = oper['Опер_РЦ_код']
                    oper_oborud = oper['Опер_оборудование_наименовние']
                    oper_tpz = oper['Опер_Тпз']
                    oper_tst = round(F.valm(oper['Опер_Тшт']) / kolich, 6)
                    oper_prof = oper['Опер_профессия_наименование']

                    oper_vidrab = oper['Опер_профессия_код']
                    if oper_vidrab in self.DICT_PROFESSIONS:
                        oper_vidrab = self.DICT_PROFESSIONS[oper_vidrab]['вид работ']
                    oper_kr = oper['Опер_КР']
                    oper_koid = oper['Опер_КОИД']
                    docs = '; '.join(dse['Документы']) + "; " + '; '.join(oper['Опер_документы'])
                    perehod = '; '.join(oper['Переходы'])
                    v_raboty = kolich - osvoeno
                    spis_shab_mk.append(
                        ['', naim, nn, v_raboty, ur, kolich, osvoeno, zakrito, oper_nom, oper_naim, mat, ssil, id,
                         prim, pki, oper_tpz, oper_tst, oper_rc_kod, oper_oborud,
                         oper_prof, oper_vidrab, oper_kr, oper_koid, docs, perehod])

        spis_shab_mk = sorted(spis_shab_mk, key=lambda ppor: ppor[F.nom_kol_po_im_v_shap(spis_shap_mk, 'ID')],
                              reverse=True)
        spis_shab_mk.insert(0, spis_shap_mk[0])
        set_red = {F.nom_kol_po_im_v_shap(spis_shab_mk, "В работу,шт.")}
        CQT.zapoln_wtabl(self, spis_shab_mk, tabl_dse, 0, set_red, '', '', 600, True, '', 40)
        tabl_dse.setColumnWidth(CQT.nom_kol_po_imen(tabl_dse, 'Наименование'), 350)
        tabl_dse.setColumnWidth(CQT.nom_kol_po_imen(tabl_dse, 'Обозначение'), 350)
        tabl_dse.setColumnWidth(CQT.nom_kol_po_imen(tabl_dse, 'Масса/М1,М2,М3'), 200)
        tabl_dse.setColumnWidth(CQT.nom_kol_po_imen(tabl_dse, 'Ссылка'), 70)
        tabl_dse.setColumnHidden(CQT.nom_kol_po_imen(tabl_dse, 'ID'), True)
        nk_check = CQT.nom_kol_po_imen(tabl_dse, 'Чек')

        CMS.zapolnit_filtr(self, self.ui.tbl_filtr_dse, tabl_dse)
        CMS.load_column_widths(self, tabl_dse)
        self.info_label()
        self.oform_dse()

    @CQT.onerror
    def oform_dse(self):
        tbl = self.ui.tbl_dse
        nk_ur = CQT.nom_kol_po_imen(tbl, 'Уровень')
        nk_v_rab = CQT.nom_kol_po_imen(tbl, 'В работу,шт.')
        max_ur = 0
        for i in range(tbl.rowCount()):
            ur = int(tbl.item(i, nk_ur).text())
            if ur > max_ur:
                max_ur = ur
        if max_ur == 0:
            shag = 55
        else:
            shag = 155 // max_ur
        for i in range(tbl.rowCount()):
            ur = int(tbl.item(i, nk_ur).text())
            ed = 255 - (max_ur - ur) * shag
            CQT.ust_color_row_wtab(tbl, i, 0 + ed, 225, 0 + ed)
            CQT.dob_color_wtab(tbl, i, nk_v_rab, 0, 15, 15)


    @CQT.onerror
    def info_label(self):
        lbl = self.ui.lbl_curr_mk
        tabl_sp_mk = self.ui.tbl_mk
        flag = None
        for i in range(tabl_sp_mk.rowCount()):
            if tabl_sp_mk.item(i, 0) == None:
                break
            if tabl_sp_mk.item(i, 0).text() == str(self.glob_nom_mk):
                tabl_sp_mk.setCurrentCell(i, 0)
                flag = i
                break
        if flag == None:
            lbl.setText('')
        else:
            lbl.setText(
                f'МК {tabl_sp_mk.item(flag, 0).text()} - {tabl_sp_mk.item(flag, 3).text()} '
                f'({tabl_sp_mk.item(flag, 6).text()})')


    def fill_jurnal(self):
        nk_nom_mk = CQT.nom_kol_po_imen(self.ui.tbl_mk, 'Пномер')
        nom_mk = int(self.ui.tbl_mk.item(self.ui.tbl_mk.currentRow(), nk_nom_mk).text())
        zapros = f'''SELECT jurnal.Дата, jurnal.Статус, 
                    jurnal.Номер_наряда, jurnal.Примечание AS "Примеч_журнал", 
                    naryad.ФИО, naryad.Фвремя, naryad.ФИО2, 
                    naryad.Фвремя2, naryad.Задание, 
                    naryad.Внеплан, naryad.Примечание AS "Примеч_наряд" FROM jurnal 
                    INNER JOIN naryad ON jurnal.Номер_наряда == naryad.Пномер 
                    INNER JOIN mk ON naryad.Номер_мк == mk.Пномер 
                    WHERE mk.Пномер == {nom_mk} AND jurnal.Статус == "Завершен"'''
        rez = CSQ.zapros(self.bd_naryad, zapros)
        CQT.zapoln_wtabl(self, rez, self.ui.tbl_jur, separ='', isp_shapka=True)
        CMS.zapolnit_filtr(self, self.ui.tbl_jur_filtr, self.ui.tbl_jur)
        CQT.clear_tbl(self.ui.tbl_zadanie)


    def load_jkzam_excel(self,query):
        list = CEX.read_file('O:\Журналы и графики\Журнал конструкторских замечаний\Журнал конструкторских замечаний.xlsm','Лист1',1,'*',2,17)
        list_dicts = F.list_to_dict(list)
        for item in list_dicts[1:]:
            pr_py = str(item['Заказ']).replace('.0','') + '$' + str(item['Проект'])
            if pr_py not in self.DICT_MK:
                continue
            query.append([str(item['№'])+ "_z",F.datetostr(item['Дата ']) ,self.DICT_MK[pr_py],'',item['Содержание'],item['Отдел'],
                          item['Простой/мин'],item['Трудозатры раб/мин'],item['Материал (брак неиспр)'],
                          '',item['Код замечания'],item['Прим. СГК']])
        return query


    def load_zamech(self):
        query = CSQ.zapros(self.bd_naryad,f"""SELECT * FROM zamech""")
        if F.nalich_file('O:\Журналы и графики\Журнал конструкторских замечаний\Журнал конструкторских замечаний.xlsm'):
            query = self.load_jkzam_excel(query)
        else:
            CQT.msgbox(f'Нет доступа к журналу конструкторскиих замечаний')
        return query


    def fill_zamech(self):
        tbl_mk = self.ui.tbl_mk
        nk_nom_mk = CQT.nom_kol_po_imen(tbl_mk, 'Пномер')
        r = tbl_mk.currentRow()
        nom_mk = int(tbl_mk.item(r, nk_nom_mk).text())
        if nom_mk == 0:
            return
        self.glob_nom_mk = nom_mk
        nk_mk = F.nom_kol_po_im_v_shap(self.LIST_ZAMECH,'МК')
        rez_list = [self.LIST_ZAMECH[0]]
        for i in range(len(self.LIST_ZAMECH)):
            if self.LIST_ZAMECH[i][nk_mk] == nom_mk:
                rez_list.append(self.LIST_ZAMECH[i])
        CQT.fill_wtabl(rez_list,self.ui.tbl_zamech)
        CMS.zapolnit_filtr(self,self.ui.tbl_zamech_filtr,self.ui.tbl_zamech)


    def select_mk(self):
        if self.ui.tbl_mk.currentRow() == -1:
            return

        self.fill_jurnal()
        self.fill_dse()
        self.fill_zamech()


    def select_jur(self):
        if self.ui.tbl_jur.currentRow() == -1:
            return
        nk_zadanie = CQT.nom_kol_po_imen(self.ui.tbl_jur,'Задание')


        zad = self.ui.tbl_jur.item(self.ui.tbl_jur.currentRow(),nk_zadanie).text().split('\n')
        zad = [[_] for _ in zad]
        zad.insert(0,['Задание'])
        CQT.zapoln_wtabl(self,zad,self.ui.tbl_zadanie,separ='',isp_shapka=True)


    def load_mk(self,napr):
        zapros = f'''SELECT DISTINCT mk.Пномер, mk.Статус, mk.Вид, mk.Номенклатура, mk.Номер_заказа, mk.Номер_проекта, 
                            mk.Примечание, mk.Основание, mk.Приоритет, mk.Направление, mk.Вес, mk.Количество, "" as Ресурсная,
                            zagot.Прим_резка, '' as "Прогресс_01",  '' as "Резка",  '' as "Мех_обр", 
                            '' as "Сборка",  '' as "Покрытие" 
                            FROM mk 
                    INNER JOIN zagot ON mk.Пномер = zagot.Ном_МК 
                    WHERE mk.Направление == "{napr}" ORDER BY mk.Приоритет DESC;'''
        spis = CSQ.zapros(self.bd_naryad, zapros, shapka=True)
        nk_nom_mk = F.nom_kol_po_im_v_shap(spis, 'Пномер')
        nk_res = F.nom_kol_po_im_v_shap(spis, 'Ресурсная')
        nk_obsh = F.nom_kol_po_im_v_shap(spis, 'Прогресс_01')
        nk_zag = F.nom_kol_po_im_v_shap(spis, 'Резка')
        nk_meh = F.nom_kol_po_im_v_shap(spis, 'Мех_обр')
        nk_sb = F.nom_kol_po_im_v_shap(spis, 'Сборка')
        nk_mal = F.nom_kol_po_im_v_shap(spis, 'Покрытие')

        list_nom_mk = tuple([_[nk_nom_mk] for _ in spis[1:]])

        dict_res = CSQ.zapros(self.db_resxml,f"""SELECT * FROM res WHERE Номер_мк in {list_nom_mk}""",rez_dict=True)
        self.dict_res = F.raskrit_dict(dict_res, 'Номер_мк')

        for i in range(1, len(spis)):
            if spis[i][nk_nom_mk] not in self.dict_res:
                print(f'МК№ {spis[i][nk_nom_mk]} не найдена ресурсная')
                continue
            res = F.from_binary_pickle(self.dict_res[spis[i][nk_nom_mk]])
            if res == None:
                print(f'МК№ {spis[i][nk_nom_mk]} не корректная ресурсная')
                continue
            spis[i][nk_obsh] = CMS.procent_vip(res, '01')
            spis[i][nk_zag] = CMS.procent_vip(res, '0101')
            spis[i][nk_meh] = CMS.procent_vip(res, '0102')
            spis[i][nk_sb] = CMS.procent_vip(res, '0103')
            spis[i][nk_mal] = CMS.procent_vip(res, '0104')
        red_col = {}
        set_isp_col = {_ for _ in range(len(spis[0])) if _ != nk_res}
        CQT.zapoln_wtabl(self, spis, self.ui.tbl_mk, set_isp_col, red_col, (), '', 200, True, '', )
        nk_obsh_t = CQT.nom_kol_po_imen(self.ui.tbl_mk, 'Прогресс_01')
        nk_zag_t = CQT.nom_kol_po_imen(self.ui.tbl_mk, 'Резка')
        nk_meh_t = CQT.nom_kol_po_imen(self.ui.tbl_mk, 'Мех_обр')
        nk_sb_t = CQT.nom_kol_po_imen(self.ui.tbl_mk, 'Сборка')
        nk_mal_t = CQT.nom_kol_po_imen(self.ui.tbl_mk, 'Покрытие')
        CQT.zapolnit_progress(self, self.ui.tbl_mk, nk_obsh_t)
        CQT.zapolnit_progress(self, self.ui.tbl_mk, nk_zag_t, isp_poc=False)
        CQT.zapolnit_progress(self, self.ui.tbl_mk, nk_meh_t, isp_poc=False)
        CQT.zapolnit_progress(self, self.ui.tbl_mk, nk_sb_t, isp_poc=False)
        CQT.zapolnit_progress(self, self.ui.tbl_mk, nk_mal_t, isp_poc=False)

    def vibor_napravl(self):
        napr = self.ui.cmb_napr.currentText()
        if napr == '':
            CQT.clear_tbl(self.ui.tbl_jur)
            CQT.clear_tbl(self.ui.tbl_jur_filtr)
            CQT.clear_tbl(self.ui.tbl_mk)
            CQT.clear_tbl(self.ui.tbl_mk_filtr)
        else:
            self.load_mk(napr)
            CMS.load_column_widths(self, self.ui.tbl_mk)
            CMS.zapolnit_filtr(self,self.ui.tbl_mk_filtr,self.ui.tbl_mk)
            nk_status = CQT.nom_kol_po_imen(self.ui.tbl_mk_filtr, 'Статус')
            self.ui.tbl_mk_filtr.item(0,nk_status).setText('!Закрыта')
            CMS.primenit_filtr(self, self.ui.tbl_mk_filtr,self.ui.tbl_mk)

    def export_table_txt(self):
        tab = self.ui.tabWidget
        if tab.currentIndex() == CQT.nom_tab_po_imen(tab, 'Отчеты'):
            dir_folder = CMS.load_tmp_folder(self, "export_table")
            if dir_folder == None:
                return
            imaf = f'Отчет_{str(self.ui.cmb_vid_otcheta.currentText())}_{F.now("%d.%m.%Y %H;%M")}.txt'
            spis = CQT.spisok_iz_wtabl(self.ui.tbl_otchet, shapka=True)
            spis = F.spis_txt_table(spis)
            F.save_file(dir_folder + F.sep() + imaf, spis)
            F.otkr_papky(dir_folder)
        if tab.currentIndex() == CQT.nom_tab_po_imen(tab, 'Маршрутные карты'):
            table_name = ''
            if self.ui.tbl_jur.hasFocus():
                table_name = 'Журнал работ'
                spis = CQT.spisok_iz_wtabl(self.ui.tbl_jur, shapka=True, only_visible=True)
            if self.ui.tbl_mk.hasFocus():
                table_name = 'Маршрутные карты'
                spis = CQT.spisok_iz_wtabl(self.ui.tbl_mk, shapka=True, only_visible=True)
            if self.ui.tbl_zadanie.hasFocus():
                table_name = 'Задание'
                spis = CQT.spisok_iz_wtabl(self.ui.tbl_zadanie, shapka=True, only_visible=True)
            if table_name == '':
                CQT.msgbox('Не выбрана таблица для печати')
                return
            dir_folder = CMS.load_tmp_folder(self, "export_table")
            if dir_folder == None:
                return
            imaf = f'Таблица_{table_name}_{F.now("%d.%m.%Y %H;%M")}.txt'
            spis = F.spis_txt_table(spis)
            F.save_file(dir_folder + F.sep() + imaf, spis)
            F.otkr_papky(dir_folder)

    def export_table(self):
        tab = self.ui.tabWidget
        if tab.currentIndex() == CQT.nom_tab_po_imen(tab, 'Отчеты'):
            dir_folder = CMS.load_tmp_folder(self, "export_table")
            if dir_folder == None:
                return
            imaf = f'Отчет_{str(self.ui.cmb_vid_otcheta.currentText())}_{F.now("%d.%m.%Y %H;%M")}.xlsx'
            spis = CQT.spisok_iz_wtabl(self.ui.tbl_otchet, shapka=True, only_visible=True)
            CEX.zap_spis(spis, dir_folder, imaf, '1', 1, 1, True, True, 'g')
            F.otkr_papky(dir_folder)
        if tab.currentIndex() == CQT.nom_tab_po_imen(tab, 'Маршрутные карты'):
            table_name = ''
            if self.ui.tbl_jur.hasFocus():
                table_name = 'Журнал работ'
                spis = CQT.spisok_iz_wtabl(self.ui.tbl_jur, shapka=True, only_visible=True)
            if self.ui.tbl_mk.hasFocus():
                table_name = 'Маршрутные карты'
                spis = CQT.spisok_iz_wtabl(self.ui.tbl_mk, shapka=True, only_visible=True)
            if self.ui.tbl_zadanie.hasFocus():
                table_name = 'Задание'
                spis = CQT.spisok_iz_wtabl(self.ui.tbl_zadanie, shapka=True, only_visible=True)
            if table_name == '':
                CQT.msgbox('Не выбрана таблица для печати')
                return
            dir_folder = CMS.load_tmp_folder(self, "export_table")
            if dir_folder == None:
                return
            imaf = f'Таблица_{table_name}_{F.now("%d.%m.%Y %H;%M")}.xlsx'
            CEX.zap_spis(spis, dir_folder, imaf, '1', 1, 1, True, True, 'g')
            F.otkr_papky(dir_folder)

app = QtWidgets.QApplication(sys.argv)

args = sys.argv[1:]
myappid = 'Powerz.BAG.SystCreateWork.1.0.4'  # !!!
QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
app.setWindowIcon(QtGui.QIcon(os.path.join("icons", "icon.png")))
# ========================================================
application = mywindow()
if CMS.kontrol_ver(application.versia,"Просмотр") == False:
    sys.exit()
# =========================================================

S = cfg['Stile'].split(",")
app.setStyle(S[0])
application = mywindow()
application.show()
sys.exit(app.exec())

