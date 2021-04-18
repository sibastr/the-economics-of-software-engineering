import matplotlib.pyplot as plt
import numpy as np
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from prettytable import PrettyTable
import sys
from mainwindow import Ui_MainWindow
"""
eaf_table = {
    'RELY': [0.75, 0.88, 1.0, 1.15, 1.39],
    'DATA': [None, 0.93, 1.0, 1.09, 1.19],
    'CPLX': [0.75, 0.88, 1.0, 1.15, 1.3],
    'RUSE': [None, 0.91, 1.0, 1.14, 1.29],
    'DOCU': [0.89, 0.95, 1.0, 1.14, 1.29],
    'TIME': [None, None, 1.0, 1.11, 1.50],
    'STOR': [None, None, 1.0, 1.06, 1.21],
    'PVOL': [None, 0.87, 1.0, 1.15, 1.30],
    'ACAP': [1.5, 1.22, 1.0, 0.83, 0.67],
    'PCON': [1.24, 1.1, 1.0, 0.92, 0.84],
    'AEXP': [1.22, 1.1, 1.0, 0.89, 0.81],
    'PCAP': [1.37, 1.16, 1.0, 0.87, 0.74],
    'PEXP': [1.25, 1.12, 1.0, 0.88, 0.81],
    'LTEX': [1.22, 1.10, 1.0, 0.91, 0.84],
    'TOOL': [1.24, 1.1, 1.0, 0.91, 0.82],
    'SITE': [1.25, 1.1, 1.0, 0.92, 0.84],
    'SCED': [1.23, 1.08, 1.0, 1.04, 1.1]
}
"""
eaf_table = {
    'RELY': [0.75, 0.86, 1.0, 1.15, 1.4],
    'DATA': [None, 0.94, 1.0, 1.08, 1.16],
    'CPLX': [0.7, 0.85, 1.0, 1.15, 1.3],
    'TIME': [None, None, 1.0, 1.11, 1.50],
    'STOR': [None, None, 1.0, 1.06, 1.21],
    'VIRT': [None, 0.87, 1.0, 1.15, 1.30],
    'TURN': [None, 0.87, 1.0, 1.07, 1.15],
    'ACAP': [1.46,1.19,1.0,0.86,0.71],
    'AEXP': [1.29, 1.15, 1.0, 0.91, 0.82],
    'PCAP': [1.42, 1.17, 1.00, 0.86, 0.7],
    'VEXP': [1.21, 1.1, 1.0, 0.9, None],
    'LEXP': [1.14, 1.07, 1.0, 0.95, None],
    'MODP': [1.24, 1.1, 1.0, 0.91, 0.82],
    'TOOL': [1.24, 1.1, 1.0, 0.91, 0.82],
    'SCED': [1.23, 1.08, 1.0, 1.04, 1.1]
}
def get_default_eaf_levels():
    eaf_levels = {
        'RELY': 2,
        'DATA': 2,
        'CPLX': 2,
        'TIME': 2,
        'STOR': 2,
        'VIRT': 2,
        'TURN': 2,
        'ACAP': 2,
        'AEXP': 2,
        'PCAP': 2,
        'VEXP': 2,
        'LEXP': 2,
        'MODP': 2,
        'TOOL': 2,
        'SCED': 2
    }
    return eaf_levels
''
def get_salary():
    salaries = {
        "Programmer": 50000,
        "Analytic" : 70000,
        "Manager" : 60000,
        "Tester" : 45000
    }
    return salaries
#Трудозатраты
def labor_costs(c1: float, eaf: float, size: float, p1: float) -> float:

    return c1 * eaf * (size)**p1
#Время
def time(c2: float, l_c: float, p2: float) -> float:
    return c2 * (l_c)**p2

#Нормальный
def normal_mode(eaf: float, size: float) -> list:
    l_c = labor_costs(3.2, eaf, size, 1.05)
    t = time(2.5, l_c, 0.38)
    return [l_c, t]

#Промежуточный
def inter_mode(eaf: float, size: float) -> list:
    l_c = labor_costs(3.0, eaf, size, 1.12)
    t = time(2.5, l_c, 0.35)
    return [l_c, t]

#Встроенный
def inbuilt_mode(eaf: float, size: float) -> list:
    l_c = labor_costs(2.8, eaf, size, 1.2)
    t = time(2.5, l_c, 0.32)
    return [l_c, t]


def count_eaf(eaf_l: list):
    eaf = 1
    for factor in eaf_table:
        index = eaf_l[factor]
        eaf *= eaf_table[factor][index]
    return eaf

def cocomo(size: int, eaf_l: list, mode_func):
    eaf = count_eaf(eaf_l)
    return mode_func(eaf, size)


eaf_levels = get_default_eaf_levels()

def RelyImpact(size,eaf_levels):

    eaf_copy = eaf_levels.copy()
    RelyResult = []
    list_of_modes = [normal_mode, inter_mode, inbuilt_mode]
    for i in range(3):
        mode = list_of_modes[i]
        for j in range(5):
            eaf_copy['RELY'] = j
            temp_result = cocomo(size, eaf_copy, mode)
            RelyResult.append(temp_result)
    dict_result = {
        'RELY_Normal': RelyResult[0:5],
        'RELY_Inter': RelyResult[5:10],
        'RELY_Inbuilt': RelyResult[10:15]
    }
    return dict_result

def DataImpact(size,eaf_levels):

    eaf_copy = eaf_levels.copy()
    DataResult = []
    list_of_modes = [normal_mode, inter_mode, inbuilt_mode]
    for i in range(3):
        mode = list_of_modes[i]
        for j in range(1,5):
            eaf_copy['DATA'] = j
            temp_result = cocomo(size, eaf_copy, mode)
            DataResult.append(temp_result)
    dict_result = {
        'DATA_Normal': DataResult[0:4],
        'DATA_Inter': DataResult[4:8],
        'DATA_Inbuilt': DataResult[8:12]
    }
    return dict_result
def CPLXImpact(size,eaf_levels):
    eaf_copy = eaf_levels.copy()

    CPLXResult = []
    list_of_modes = [normal_mode, inter_mode, inbuilt_mode]
    for i in range(3):
        mode = list_of_modes[i]
        for j in range(5):
            eaf_copy['CPLX'] = j
            temp_result = cocomo(size, eaf_copy, mode)
            CPLXResult.append(temp_result)
    dict_result = {
        'CPLX_Normal' : CPLXResult[0:5],
        'CPLX_Inter' : CPLXResult[5:10],
        'CPLX_Inbuilt' : CPLXResult[10:15]
    }
    return dict_result


def Impact_Graph(dict_RELY,dict_CPLX,dict_Data):
    work_RELY_Normal = []
    time_RELY_Normal = []
    work_Data_Normal = []
    time_Data_Normal = []
    work_CPLX_Normal = []
    time_CPLX_Normal = []

    work_RELY_Inter = []
    time_RELY_Inter = []
    work_Data_Inter = []
    time_Data_Inter = []
    work_CPLX_Inter = []
    time_CPLX_Inter = []

    work_RELY_Inbuilt = []
    time_RELY_Inbuilt = []
    work_Data_Inbuilt = []
    time_Data_Inbuilt = []
    work_CPLX_Inbuilt = []
    time_CPLX_Inbuilt = []
    for i in range(5):
        work_RELY_Normal.append(dict_RELY['RELY_Normal'][i][0])
        time_RELY_Normal.append(dict_RELY['RELY_Normal'][i][1])

        work_RELY_Inter.append(dict_RELY['RELY_Inter'][i][0])
        time_RELY_Inter.append(dict_RELY['RELY_Inter'][i][1])

        work_RELY_Inbuilt.append(dict_RELY['RELY_Inbuilt'][i][0])
        time_RELY_Inbuilt.append(dict_RELY['RELY_Inbuilt'][i][1])


    for i in range(5):
        work_CPLX_Normal.append(dict_CPLX['CPLX_Normal'][i][0])
        time_CPLX_Normal.append(dict_CPLX['CPLX_Normal'][i][1])

        work_CPLX_Inter.append(dict_CPLX['CPLX_Inter'][i][0])
        time_CPLX_Inter.append(dict_CPLX['CPLX_Inter'][i][1])

        work_CPLX_Inbuilt.append(dict_CPLX['CPLX_Inbuilt'][i][0])
        time_CPLX_Inbuilt.append(dict_CPLX['CPLX_Inbuilt'][i][1])

    for i in range(4):
        work_Data_Normal.append(dict_Data['DATA_Normal'][i][0])
        time_Data_Normal.append(dict_Data['DATA_Normal'][i][1])

        work_Data_Inter.append(dict_Data['DATA_Inter'][i][0])
        time_Data_Inter.append(dict_Data['DATA_Inter'][i][1])

        work_Data_Inbuilt.append(dict_Data['DATA_Inbuilt'][i][0])
        time_Data_Inbuilt.append(dict_Data['DATA_Inbuilt'][i][1])

    # Work graph
    fig, axs = plt.subplots(2, 3)
    axs[0, 0].plot([0,1,2,3,4],work_RELY_Normal,[0,1,2,3,4],work_CPLX_Normal,[1,2,3,4],work_Data_Normal)
    axs[0, 0].set_title('Normal mode')
    axs[0, 0].legend(['RELY', 'CPLX', 'DATA'])
    axs[0, 1].plot([0, 1, 2, 3, 4], work_RELY_Inter, [0, 1, 2, 3, 4], work_CPLX_Inter, [1, 2, 3, 4], work_Data_Inter)
    axs[0, 1].set_title('Inter mode')
    axs[0, 1].legend(['RELY', 'CPLX', 'DATA'])
    axs[0, 2].plot([0, 1, 2, 3, 4], work_RELY_Inbuilt, [0, 1, 2, 3, 4], work_CPLX_Inbuilt, [1, 2, 3, 4], work_Data_Inbuilt)
    axs[0, 2].set_title('Inbuilt mode')
    axs[0, 2].legend(['RELY', 'CPLX', 'DATA'])
    axs[1, 0].plot([0, 1, 2, 3, 4], time_RELY_Normal, [0, 1, 2, 3, 4], time_CPLX_Normal, [1, 2, 3, 4], time_Data_Normal)
    axs[1, 0].set_title('Normal mode')
    axs[1, 0].legend(['RELY', 'CPLX', 'DATA'])
    axs[1, 1].plot([0, 1, 2, 3, 4], time_RELY_Inter, [0, 1, 2, 3, 4], time_CPLX_Inter, [1, 2, 3, 4], time_Data_Inter)
    axs[1, 1].set_title('Inter mode')
    axs[1, 1].legend(['RELY', 'CPLX', 'DATA'])
    axs[1, 2].plot([0, 1, 2, 3, 4], time_RELY_Inbuilt, [0, 1, 2, 3, 4], time_CPLX_Inbuilt, [1, 2, 3, 4], time_Data_Inbuilt)
    axs[1, 2].set_title('Inbuilt mode')
    axs[1, 2].legend(['RELY', 'CPLX', 'DATA'])

    axs[0,0].set(xlabel='Уровень фактора', ylabel='Трудозатраты')
    axs[0, 1].set(xlabel='Уровень фактора', ylabel='Трудозатраты')
    axs[0, 2].set(xlabel='Уровень фактора', ylabel='Трудозатраты')
    axs[1, 0].set(xlabel='Уровень фактора', ylabel='Время')
    axs[1, 1].set(xlabel='Уровень фактора', ylabel='Время')
    axs[1, 2].set(xlabel='Уровень фактора', ylabel='Время')
    plt.show()


def project_tradion(eaf,kloc,mode,self):

    eaf_levels = eaf.copy()

    result_Air = cocomo(kloc, eaf_levels,mode)
    amount_of_workers = []
    workers_by_time = []

    work_plan_requirements = result_Air[0] * 0.08
    time_plan_requirements = result_Air[1] * 0.36

    workers_by_time += [math.ceil(work_plan_requirements/time_plan_requirements)]

    amount_of_workers += [math.ceil(work_plan_requirements/time_plan_requirements)]*round(time_plan_requirements)


    work_design_project = result_Air[0] * 0.18
    time_design_project = result_Air[1] * 0.36

    workers_by_time += [math.ceil(work_design_project / time_design_project)]

    amount_of_workers += [math.ceil(work_design_project / time_design_project)] * round(
        time_design_project)

    work_details_design = result_Air[0] * 0.25
    time_details_design = result_Air[1] * 0.18

    workers_by_time += [math.ceil(work_details_design / time_details_design)]
    amount_of_workers += [math.ceil(work_details_design / time_details_design)] * round(
        time_details_design)

    work_code_test = result_Air[0] * 0.26
    time_code_test = result_Air[1] * 0.18

    workers_by_time += [math.ceil(work_code_test / time_code_test)]
    amount_of_workers += [math.ceil(work_code_test / time_code_test)] * round(
        time_code_test)

    work_integration_test = result_Air[0] * 0.31
    time_integration_test = result_Air[1] * 0.28

    workers_by_time += [math.ceil(work_integration_test / time_integration_test)]
    amount_of_workers += [math.ceil(work_integration_test / time_integration_test)] * round(
        time_integration_test)

    # Переносим значения в UI
    self.ui.work.setPlainText(str(round(result_Air[0],2)))
    self.ui.time.setPlainText(str(round(result_Air[1],2)))
    self.ui.work_plan.setPlainText(str(round(result_Air[0] + work_plan_requirements,2)))
    self.ui.time_plan.setPlainText(str(round(result_Air[1] + time_plan_requirements,2)))

    # Заполняем таблицу традиционных трудозатрат в UI
    item = QTableWidgetItem()
    item.setText(str(round(work_plan_requirements,2)))
    self.ui.tableWidget_2.setItem(0, 0, item)

    item = QTableWidgetItem()
    item.setText(str(round(work_design_project,2)))
    self.ui.tableWidget_2.setItem(1, 0, item)

    item = QTableWidgetItem()
    item.setText(str(round(work_details_design,2)))
    self.ui.tableWidget_2.setItem(2, 0, item)

    item = QTableWidgetItem()
    item.setText(str(round(work_code_test,2)))
    self.ui.tableWidget_2.setItem(3, 0, item)

    item = QTableWidgetItem()
    item.setText(str(round(work_integration_test,2)))
    self.ui.tableWidget_2.setItem(4, 0, item)

    # Заполняем таблицу традиционного времени в UI

    item = QTableWidgetItem()
    item.setText(str(round(time_plan_requirements,2)))
    self.ui.tableWidget_2.setItem(0, 1, item)

    item = QTableWidgetItem()
    item.setText(str(round(time_design_project,2)))
    self.ui.tableWidget_2.setItem(1, 1, item)

    item = QTableWidgetItem()
    item.setText(str(round(time_details_design,2)))
    self.ui.tableWidget_2.setItem(2, 1, item)

    item = QTableWidgetItem()
    item.setText(str(round(time_code_test,2)))
    self.ui.tableWidget_2.setItem(3, 1, item)

    item = QTableWidgetItem()
    item.setText(str(round(time_integration_test,2)))
    self.ui.tableWidget_2.setItem(4, 1, item)

    result_Air[0] += work_plan_requirements
    result_Air[1] += time_plan_requirements
    analysis = result_Air[0] * 0.04
    design_product = result_Air[0] * 0.12
    programming = result_Air[0] * 0.44
    testing = result_Air[0] * 0.06
    verification = result_Air[0] * 0.14
    office = result_Air[0] * 0.07
    quality_assurance = result_Air[0] * 0.07
    manuals = result_Air[0] * 0.06
    summary_work = sum([analysis, design_product, programming, testing,
                        verification, office, quality_assurance, manuals])

    # Заполняем таблицу трудозатрат WBS
    item = QTableWidgetItem()
    item.setText(str(round(analysis,2)))
    self.ui.tableWidget.setItem(0, 0, item)

    item = QTableWidgetItem()
    item.setText(str(round(design_product, 2)))
    self.ui.tableWidget.setItem(1, 0, item)

    item = QTableWidgetItem()
    item.setText(str(round(programming, 2)))
    self.ui.tableWidget.setItem(2, 0, item)

    item = QTableWidgetItem()
    item.setText(str(round(testing, 2)))
    self.ui.tableWidget.setItem(3, 0, item)

    item = QTableWidgetItem()
    item.setText(str(round(verification, 2)))
    self.ui.tableWidget.setItem(4, 0, item)

    item = QTableWidgetItem()
    item.setText(str(round(office, 2)))
    self.ui.tableWidget.setItem(5, 0, item)

    item = QTableWidgetItem()
    item.setText(str(round(quality_assurance, 2)))
    self.ui.tableWidget.setItem(6, 0, item)

    item = QTableWidgetItem()
    item.setText(str(round(manuals, 2)))
    self.ui.tableWidget.setItem(7, 0, item)

    item = QTableWidgetItem()
    item.setText(str(round(summary_work, 2)))
    self.ui.tableWidget.setItem(8, 0, item)


    dif_workers = []
    dif_workers.append(amount_of_workers[0])
    for i in range(len(amount_of_workers)):
        if amount_of_workers[i] not in dif_workers:
            dif_workers.append(amount_of_workers[i])

    x = np.arange(1, len(amount_of_workers)+1)
    y = amount_of_workers

    fig, ax = plt.subplots()
    ax.bar(x, y)
    plt.xlabel('Месяцы')
    fig.set_figwidth(12)  # ширина Figure
    fig.set_figheight(6)  # высота Figure
    plt.ylabel('Количество сотрудников')
    plt.show()

    salary = get_salary()
    budget_list = []

    budget_list += [(((salary['Manager'] + salary['Analytic']) / 2) * workers_by_time[0] * time_plan_requirements)]
    budget_list += [(((salary['Programmer'] + salary['Analytic']) / 2) * workers_by_time[1] * time_design_project)]
    budget_list += [(((salary['Programmer'] + salary['Analytic']) / 2) * workers_by_time[2] * time_details_design)]
    budget_list += [(((salary['Programmer'] + salary['Tester']) / 2) * workers_by_time[3] * time_code_test)]
    budget_list += [(((salary['Programmer'] + salary['Tester']) / 2) * workers_by_time[4] * time_integration_test)]

    sum_budget = 0
    for i in range(len(budget_list)):
        sum_budget += budget_list[i]

    self.ui.budget.setPlainText(str(round(sum_budget)))


class mywindow(QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_calculate.clicked.connect(self.onTaskBtnClick)
        self.ui.pushButton_graph.clicked.connect(self.onGraphBtnClick)

    def addItemTableWidget(self, row, column, value):
        item = QTableWidgetItem()
        item.setText(str(value))
        self.ui.tableWidget_2.setItem(row, column, item)

    def onTaskBtnClick(self):
        eaf_levels = get_default_eaf_levels()
        eaf_levels['RELY'] = self.ui.RELY.value()
        eaf_levels['DATA'] = self.ui.DATA.value()
        eaf_levels['CPLX'] = self.ui.CPLX.value()
        eaf_levels['TIME'] = self.ui.TIME.value()
        eaf_levels['STOR'] = self.ui.STOR.value()
        eaf_levels['VIRT'] = self.ui.VIRT.value()
        eaf_levels['TURN'] = self.ui.TURN.value()
        eaf_levels['ACAP'] = self.ui.ACAP.value()
        eaf_levels['AEXP'] = self.ui.AEXP.value()
        eaf_levels['PCAP'] = self.ui.PCAP.value()
        eaf_levels['VEXP'] = self.ui.VEXP.value()
        eaf_levels['LEXP'] = self.ui.LEXP.value()
        eaf_levels['MODP'] = self.ui.MODP.value()
        eaf_levels['TOOL'] = self.ui.TOOL.value()
        eaf_levels['SCED'] = self.ui.SCED.value()

        loc = self.ui.LOC.value()
        kloc = loc / 1000

        if self.ui.normal.isChecked():
            mode = normal_mode
        elif self.ui.inter.isChecked():
            mode = inter_mode
        elif self.ui.inbuilt.isChecked():
            mode = inbuilt_mode

        project_tradion(eaf_levels,kloc,mode,self)

    def addItemTableWidget(self, row, column, value):
        item = QTableWidgetItem()
        item.setText(str(value))
        self.ui.tableWidget.setItem(row, column, item)


    def onGraphBtnClick(self):
        eaf_levels = get_default_eaf_levels()
        eaf_levels['RELY'] = self.ui.RELY.value()
        eaf_levels['DATA'] = self.ui.DATA.value()
        eaf_levels['CPLX'] = self.ui.CPLX.value()
        eaf_levels['TIME'] = self.ui.TIME.value()
        eaf_levels['STOR'] = self.ui.STOR.value()
        eaf_levels['VIRT'] = self.ui.VIRT.value()
        eaf_levels['TURN'] = self.ui.TURN.value()
        eaf_levels['ACAP'] = self.ui.ACAP.value()
        eaf_levels['AEXP'] = self.ui.AEXP.value()
        eaf_levels['PCAP'] = self.ui.PCAP.value()
        eaf_levels['VEXP'] = self.ui.VEXP.value()
        eaf_levels['LEXP'] = self.ui.LEXP.value()
        eaf_levels['MODP'] = self.ui.MODP.value()
        eaf_levels['TOOL'] = self.ui.TOOL.value()
        eaf_levels['SCED'] = self.ui.SCED.value()

        loc = self.ui.LOC.value()
        kloc = loc/1000

        d_Rely = RelyImpact(kloc, eaf_levels)
        d_Data = DataImpact(kloc, eaf_levels)
        d_CPLX = CPLXImpact(kloc, eaf_levels)
        Impact_Graph(d_Rely, d_CPLX, d_Data)





if __name__ == '__main__':
    app = QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())





