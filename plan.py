import project_cust_38.Cust_Functions as F
import datetime as DT
import mosh as MSH
import zagruzka as ZG
import project_cust_38.Cust_SQLite as CSQ
import copy
import project_cust_38.Cust_Excel as CEX
#TODO указывать время работы каждой смены по участкам, каждый участок будет иметь несколько смен
#TODO учитывать резерв загрузки начало и конец смены и между нарядами по каждому рц
#TODO и учесть коэффицет времени -2 это в 2 раза медленнее работает при построении табеля
#TODO не менять праздники и выходные в календаре если они ранее были установлены
#TODO настройка изменения условий с такого то числа
#TODO сравнение вариантов планирования
"""
определить соотношение направлений в % == направление, % *
определить порядок по приоритету мк по направлению, которые еще не зыкрыты == направление, номер мк *
каждую мк разложить на последовательность деталей, которые еще не сделаны  == направление, номер мк, имя детали, рц *
каждую деталь разложить на последовательность операций, которые еще не сделаны  == направление, номер мк, имя детали, рц, операция, время выполнения *
сформировать картину мощностей == направление, РЦ, часы, даты *
каждую операцию рассчитать на параллельное выполнение(сделать две но короче) == направление, номер мк, имя детали, рц, операция + операция, время выполнения
наполнять мощности операциями по порядку, фиксировать время начала операции и время конца
свести операции на диаграмму == направление, номер мк, имя детали, рц, операция , начало , конец

условия предшествования технологических операций;
доступность основных рабочих центров;
транспортировка между рабочими центрами или между подразделениями;
наличие необходимых для выполнения операций товарно-материальных ценностей.
"""

def load_plan(self,delete_cash_plan):
    #zagruzka = ZG.load_zagruzka(self)
    #==================
    imafp = self.files_tmp +F.sep() + 'plan.pickle'
    imafz = self.files_tmp +F.sep() + 'zagruzka.pickle'
    imafm = self.files_tmp +F.sep() + 'mosh.pickle'
    if delete_cash_plan:
        F.udal_file(imafp)
        F.udal_file(imafz)
        F.udal_file(imafm)
    if F.nalich_file(imafp):
        rez_list =  F.load_file_pickle(imafp)
    else:
        if F.nalich_file(imafz):
            zagruzka = F.load_file_pickle(imafz)
        else:
            zagruzka = ZG.load_zagruzka(self)
            F.save_file_pickle(imafz, zagruzka)

        DOSTUPNIE_PLOSHADI = [1, 2, 3, 4, 5]
        if F.nalich_file(imafm):
            dict_moshn = F.load_file_pickle(imafm)
        else:
            dict_moshn = MSH.load_grafic_moshnostey(self, DOSTUPNIE_PLOSHADI)
            F.save_file_pickle(imafm, dict_moshn)

        if dict_moshn == None:
            return
        rez = [['Дата','Код_РЦ', 'Пномер', 'ФИО','Пулл','Время_начала','Время_конца','Раб_мин','напр1','напр2','напр3','напр4','summ']]
        for day in dict_moshn:
            for empl in day['empl']:
                summ = 0
                tmp = [day['date'],empl['Код_РЦ'], empl['Пномер'], empl['ФИО'],empl['Пулл'],empl['Время_начала'],empl['Время_конца'],empl['Раб_час']*60]
                for vid in empl['Пулл'].keys():
                    tmp.append(empl['Пулл'][vid])
                    summ+=empl['Пулл'][vid]
                tmp.append(summ)
                rez.append(tmp)
        now = F.now("%Y-%m-%d")
        try:
            CEX.zap_spis(rez, self.files_tmp , f'mosh_{now}.xlsx', '1', 1, 1)
        except:
            pass

        rez_list = nalogenie(self, dict_moshn,zagruzka)
        name = f'plan_{now}.xlsx'

        self.save_excell_plan(rez_list,self.files_tmp,name)
        F.save_file_pickle(imafp,rez_list)
        if delete_cash_plan:
            try:
                F.otkr_papky(self.files_tmp)
            except:
                pass
    return rez_list

def calc_limit_po_childrens(mk,iter_dse,iter_oper,limit_tmp):
    current_uroven = mk[iter_dse]['Уровень']
    for i in range(iter_dse - 1, -1,-1):
        if mk[i]['Уровень'] <= current_uroven:
            break
        if mk[i]['Уровень'] == current_uroven + 1:
            if 'План_завершение' in mk[i]['Операции'][-1]:
                if limit_tmp < mk[i]['Операции'][-1]['План_завершение']:
                    limit_tmp = mk[i]['Операции'][-1]['План_завершение']
    return limit_tmp

def calc_limit_po_oper(mk,iter_dse,iter_oper,limit_tmp):
    for i in range(iter_oper-1,-1,-1):
        if 'План_завершение' in mk[iter_dse]['Операции'][i]:
            if limit_tmp < mk[iter_dse]['Операции'][i]['План_завершение']:
                limit_tmp = mk[iter_dse]['Операции'][i]['План_завершение']
                break
    return limit_tmp

def calculate_start_limit_oper(mk,iter_dse,iter_oper):
    limit_tmp = copy.deepcopy(mk[iter_dse]['Лимит_дата_начала'])
    lim_child = calc_limit_po_childrens(mk,iter_dse,iter_oper,limit_tmp)
    lim_oper = calc_limit_po_oper(mk,iter_dse,iter_oper,lim_child)
    return lim_oper


def nalogenie(self,dict_moshn,zagruzka):
    list_plan = []
    npp = 1
    i =0
    cc = len(zagruzka)
    set_defecit_rc = set()
    for mk in zagruzka:
        i+=1
        print(f'{i} из {cc}')
        for iter_dse, dse in enumerate(mk['Ресурсная']):
            name_dse =f"{dse['Номенклатурный_номер']} {dse['Наименование']}"
            arr_mat_dse = dse['Мат_кд'].split('/')
            ves_dse = 0
            if arr_mat_dse[1] != '' and arr_mat_dse[2] != '':
                ves_dse = round(F.valm(arr_mat_dse[0]) * dse['Количество'],2)

            for iter_oper, oper in enumerate(dse['Операции']):
                start_limit = calculate_start_limit_oper(mk['Ресурсная'],iter_dse,iter_oper)
                rc = oper['Опер_РЦ_код']
                t_pz = round(oper['Опер_Тпз'],2)
                t_sht = round(oper['Опер_Тшт'] / dse['Количество'], 2)

                oper_name = oper['Опер_наименовние']
                oper_nom = oper['Опер_номер']
                oper_prof = oper['Опер_профессия_наименование']
                limit_data_oper = oper['Лимит_дата_начала']
                koef_paral = mk['Коэф_парал']
                list_partiy = generate_partii(dse['Количество'],koef_paral)
                vid_rabot = oper['Опер_профессия_код']
                if oper['Опер_профессия_код'] in self.DICT_PROFESSIONS:
                    vid_rabot = self.DICT_PROFESSIONS[oper['Опер_профессия_код']]['вид работ']
                for dse_part in list_partiy:
                    time_rasch = round((t_sht+t_pz)*dse_part, 2)
                    t_operacionnoe = round(t_sht * dse_part,2)
                    list_plan = nalogenie_operacii(self,list_plan,dict_moshn, t_operacionnoe, t_pz, rc, mk,start_limit,set_defecit_rc,
                                                   name_dse,oper,
                           time_rasch,mk['Вес'],ves_dse,dse,oper_name,oper_nom,limit_data_oper,iter_dse,iter_oper,vid_rabot,dse_part,npp)

    list_plan = start_end_mk(list_plan)
    for item in set_defecit_rc:
        print(item)
    return list_plan

def generate_partii(kol_vo,koef):
    chast = kol_vo//koef
    rez = [chast] * koef
    ost = kol_vo%koef
    if ost > 0:
        rez.append(ost)
    return rez

def nalogenie_operacii(self,list_plan,dict_moshn, t_operacionnoe, t_pz, rc, mk,start_limit,set_defecit_rc,name_dse,oper,
                       time_rasch,ves,ves_dse,dse,oper_name,oper_nom,limit_data_oper,iter_dse,iter_oper,vid_rabot,dse_part,npp):
    list_plan_dse = add_time_to_day(dict_moshn, t_operacionnoe, t_pz, rc, mk['Направление'], start_limit,npp)
    if list_plan_dse == []:
        pass
        # print(f'Для {rc} под {oper["Опер_наименовние"]} {oper["Опер_профессия_наименование"]} не найдены мощности')
        #set_defecit_rc.add((
        #                   'Рц найден, но не найдено время', rc, name_dse, oper['Опер_номер'], oper["Опер_наименовние"],
        #                   mk['Пномер']))
        # add_time_to_day(dict_moshn, t_operacionnoe, t_pz, rc, mk['Направление'])
    else:
        if list_plan_dse == False:
            # print(f'Для {rc} под {oper["Опер_наименовние"]} {oper["Опер_профессия_наименование"]} не найдены мощности')
            set_defecit_rc.add(
                ('Рц не найден', rc, name_dse, oper['Опер_номер'], oper["Опер_наименовние"], mk['Пномер']))
            # add_time_to_day(dict_moshn, t_operacionnoe, t_pz, rc, mk['Направление'])
        else:
            for deistvie in list_plan_dse:
                ves_test_sborka = 0

                if rc == '010301' or rc == '010302':
                    ves_test_sborka = round(time_rasch / 480 * 102, 3)
                list_plan.append({deistvie['Начало']: {'#':deistvie['#'], 'ФИОД': deistvie['ФИОД'], 'Начало': deistvie['Начало'],
                                                       'Конец': deistvie['Конец'], 'РЦ': rc, 'РМ': deistvie['РМ'],
                                                       'Должность': deistvie['Должность'], "Направление": mk['Направление'],
                                                       'Номер_заказа': mk['Номер_заказа'],
                                                       'Номер_проекта': mk['Номер_проекта'],
                                                       'Вид': mk['Вид'], 'Примечание': mk['Примечание'],
                                                       'Основание': mk['Основание'],
                                                       'Количество_изд_МК': mk['Количество'], 'Вес_мк': ves,
                                                       'Прим_резка': mk['Прим_резка'], "МК": mk['Пномер'],
                                                       "ДСЕ": name_dse,
                                                       "Вес_ДСЕ(кол)": ves_dse, "Количество_ДСЕ(на_МК)": dse['Количество'],
                                                       'Операция': oper_name, 'Номер_опер': oper_nom, 'Время_пз(мин)': t_pz,
                                                       'Время_шт(мин)': t_operacionnoe,
                                                       'Остаток': deistvie['Остаток'],
                                                       'Дельта': deistvie['Дельта'],
                                                       'Лимит_дата_опер': limit_data_oper,
                                                       'Лимит_дата_дсе': mk['Ресурсная'][iter_dse]['Лимит_дата_начала'],
                                                       'Лимит_по_входящим': start_limit,
                                                       'Время_для_оценки(мин)': time_rasch,
                                                       'Вес_для_оценки_сборка': ves_test_sborka,
                                                       'Вид работ': vid_rabot,
                                                       'Профессия': oper['Опер_профессия_наименование']}})
                time_rasch = 0
                t_operacionnoe = 0
                mk['Ресурсная'][iter_dse]['Операции'][iter_oper]['План_завершение'] = deistvie[
                    'Конец']  # ограничение, запрос идет в
                ves = 0
    return list_plan

def start_end_mk(list_plan):
    dict_sroki_end_proecta = dict()
    dict_sroki_start_proecta = dict()
    for i in range(len(list_plan)):
        day = list(list_plan[i].keys())[0]
        if list_plan[i][day]['МК'] in dict_sroki_end_proecta:
            if list_plan[i][day]['Конец'] > dict_sroki_end_proecta[list_plan[i][day]['МК']]:
                dict_sroki_end_proecta[list_plan[i][day]['МК']] = list_plan[i][day]['Конец']
        else:
            dict_sroki_end_proecta[list_plan[i][day]['МК']] = list_plan[i][day]['Конец']
        if list_plan[i][day]['МК'] in dict_sroki_start_proecta:
            if list_plan[i][day]['Начало'] < dict_sroki_start_proecta[list_plan[i][day]['МК']]:
                dict_sroki_start_proecta[list_plan[i][day]['МК']] = list_plan[i][day]['Начало']
        else:
            dict_sroki_start_proecta[list_plan[i][day]['МК']] = list_plan[i][day]['Начало']
    for i in range(len(list_plan)):
        day = list(list_plan[i].keys())[0]
        list_plan[i][day]['Начало мк'] = dict_sroki_start_proecta[list_plan[i][day]['МК']]
        list_plan[i][day]['Завершение мк'] = dict_sroki_end_proecta[list_plan[i][day]['МК']]
    return list_plan

def find_user_in_day(moshn,ispolnotel,start_limit):
    fl_naid_ispolnitel = False
    if ispolnotel == '':
        fl_naid_ispolnitel = True
    else:
        for j in range(len(moshn['empl'])):
            if ispolnotel == f"{moshn['empl'][j]['ФИО']} {moshn['empl'][j]['Должность']}" \
                    and moshn['empl'][j]['Время'] >= start_limit:
                fl_naid_ispolnitel = True
                break
    if fl_naid_ispolnitel == False:
        ispolnotel = ''
    return ispolnotel

def add_time_to_day(dict_moshn,t_operacionnoe,t_pz,rc,napravlenie, start_limit,npp):
    list_plan_dse = []
    ispolnotel = ''
    t_pz_tmp = copy.deepcopy(t_pz)
    fl_naiden_rc = False
    for i in range(len(dict_moshn)): #по каждому дню
        if t_operacionnoe <= 0:
            break
        ispolnotel = find_user_in_day(dict_moshn[i],ispolnotel,start_limit)
        for j in range(len(dict_moshn[i]['empl'])): #по каждому рабочему месту
            if ispolnotel != "":
                if f"{dict_moshn[i]['empl'][j]['ФИО']} {dict_moshn[i]['empl'][j]['Должность']}" != ispolnotel: # подбор исполнителя
                    continue
            if dict_moshn[i]['empl'][j]['Код_РЦ'] == rc: # выбор РЦ
                fl_naiden_rc = True
                if dict_moshn[i]['empl'][j]['Пулл'][napravlenie] > 0 and dict_moshn[i]['empl'][j]['Время'] >= start_limit: #Если есть резерв по мощности и дата время начала не ранее лимита
                    KOEF_VREMENI = 1/dict_moshn[i]['empl'][j]['Коэфф_производит']
                    KOEF_BETWEEN_ORDER = round(dict_moshn[i]['empl'][j]['Между_нар_мин']/6,1)
                    t_oper_tmp = (t_operacionnoe + t_pz_tmp)*KOEF_VREMENI + KOEF_BETWEEN_ORDER

                    if t_oper_tmp > dict_moshn[i]['empl'][j]['Пулл'][napravlenie]:
                        t_oper_tmp = dict_moshn[i]['empl'][j]['Пулл'][napravlenie]
                    dict_moshn[i]['empl'][j]['Пулл'][napravlenie] -= t_oper_tmp
                    dt_nachalo = dict_moshn[i]['empl'][j]['Время']
                    dt_konec = dict_moshn[i]['empl'][j]['Время_конца']
                    if dt_nachalo > dt_konec:
                        print(f'ОШибка конец раньше начала')
                        return
                    rez_dt = F.date_add_time(dict_moshn[i]['empl'][j]['Время'], minutes=int(t_oper_tmp))
                    dolgnost = dict_moshn[i]['empl'][j]['Должность']
                    ispolnotel = f"{dict_moshn[i]['empl'][j]['ФИО']} {dolgnost}"
                    if rez_dt > dt_konec: # если предпологаемое время завершения работ позже конца рабочего дня
                        deficit_time_float = (rez_dt - dt_konec).total_seconds() / 60.0  #не помещается минут
                        dict_moshn[i]['empl'][j]['Время'] = dt_konec #переменное время  = концу дня

                        t_operacionnoe -= round(((t_oper_tmp - deficit_time_float - KOEF_BETWEEN_ORDER) / KOEF_VREMENI)-t_pz_tmp,2) #Тшт = операционное время - пз - дефицит
                        t_operacionnoe = round(t_operacionnoe,1)
                        list_plan_dse.append({'#':npp,'РМ':dict_moshn[i]['empl'][j]['Пномер'],'ФИОД':ispolnotel,'Должность':dolgnost,'Начало':dt_nachalo,'Конец':dt_konec,'Остаток':t_operacionnoe,'Дельта':rez_dt-dt_nachalo})
                        npp += 1
                        t_pz_tmp = 0
                        break
                    else:
                        dict_moshn[i]['empl'][j]['Время'] = rez_dt
                        t_operacionnoe -= round(((t_oper_tmp - KOEF_BETWEEN_ORDER) / KOEF_VREMENI)-t_pz_tmp,2)
                        t_operacionnoe = round(t_operacionnoe, 1)
                        list_plan_dse.append({'#':npp,'РМ':dict_moshn[i]['empl'][j]['Пномер'],'ФИОД': ispolnotel,'Должность':dolgnost, 'Начало': dt_nachalo, 'Конец': rez_dt,'Остаток':t_operacionnoe, 'Дельта':rez_dt-dt_nachalo})
                        npp += 1
                        t_pz_tmp = 0
                        break
    if t_operacionnoe > 0 and fl_naiden_rc==False:
        return False
    return list_plan_dse
