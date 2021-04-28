import matplotlib.pyplot as plt
import numpy as np
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from prettytable import PrettyTable
import sys
from mainwindow import Ui_MainWindow
from main import MyWindow
class Language:
    def __init__(self, name: str, loc_per_fp: int):
        self.name = name
        self.loc_per_fp = loc_per_fp

class FunctionPointMethod:
    Languages = (
        Language("Ассемблер", 320),
        Language("С", 128),
        Language("Кобол", 106),
        Language("Фортран", 90),
        Language("Паскаль", 53),
        Language("С++", 53),
        Language("Java", 53),
        Language("C#", 53),
        Language("Ada 95", 49),
        Language("Visual Basic 6", 24),
        Language("Visual C++", 34),
        Language("Delphi Pascal", 29),
        Language("Perl", 21),
        Language("Prolog", 54),
        Language("SQL", 46),
        Language("JavaScript", 56),
    )

level_of_rank_ILF = {
    'easy': 7,
    'normal':10,
    'hard' : 15,
    'ftr_1' : range(1,2),
    'ftr_2' : range(2,6),
    'ftr_3' : 5,
    'det_1' : range(1,20),
    'det_2' : range(20,51),
    'det_3' : 50
}
level_of_rank_EIF = {
    'easy': 5,
    'normal':7,
    'hard' : 10,
    'ftr_1' : range(1,2),
    'ftr_2' : range(2,6),
    'ftr_3' : 5,
    'det_1' : range(1,20),
    'det_2' : range(20,51),
    'det_3' : 50
}
level_of_rank_EI = {
    'easy': 3,
    'normal':4,
    'hard' : 6,
    'ftr_1': range(0,2),
    'ftr_2' : range(2,3),
    'ftr_3' : 2,
    'det_1' : range(1,5),
    'det_2' : range(5,16),
    'det_3' : 15
}

level_of_rank_EO = {
    'easy': 4,
    'normal':5,
    'hard' : 7,
    'ftr_1': range(0,2),
    'ftr_2' : range(2,4),
    'ftr_3' : 3,
    'det_1' : range(1,5),
    'det_2' : range(5,20),
    'det_3' : 19
}
level_of_rank_EQ = {
    'easy': 3,
    'normal':4,
    'hard' : 6,
    'ftr_1': range(0,2),
    'ftr_2' : range(2,4),
    'ftr_3' : 3,
    'det_1' : range(1,5),
    'det_2' : range(5,20),
    'det_3' : 19
}



def rankandamount(self, dict,dict_spinBox):
    RET = dict_spinBox['ftr'].value()
    DET = dict_spinBox['det'].value()
    rank = 0
    points_amount = dict_spinBox['amount'].value()
    if RET in dict['ftr_1']:
        if DET in dict['det_1']:
            rank = dict['easy']
        elif DET in dict['det_2']:
            rank = dict['easy']
        elif DET > dict['det_3']:
            rank = dict['normal']

    elif RET in dict['ftr_2']:
        if DET in dict['det_1']:
            rank = dict['easy']
        elif DET in dict['det_2']:
            rank = dict['normal']
        elif DET > dict['det_3']:
            rank = dict['hard']

    elif RET > dict['ftr_3']:
        if DET in dict['det_1']:
            rank = dict['normal']
        elif DET in dict['det_2']:
            rank = dict['hard']
        elif DET > dict['det_3']:
            rank = dict['hard']

    result = points_amount * rank
    if rank == dict['easy']:
        cur_value = dict_spinBox['easy'].value()
        dict_spinBox['easy'].setValue(cur_value+result)
    elif rank == dict['normal']:
        cur_value = dict_spinBox['normal'].value()
        dict_spinBox['normal'].setValue(cur_value + result)
    elif rank == dict['hard']:
        cur_value = dict_spinBox['hard'].value()
        dict_spinBox['hard'].setValue(cur_value + result)

def get_default_fi_levels():
    fi_levels = {
        'Data_trans': 2,
        'Data_proc': 2,
        'Performance': 2,
        'Exp_limit': 2,
        'Rate_trans': 2,
        'Input': 2,
        'Effect_work': 2,
        'Update': 2,
        'Cplx' : 2,
        'Repeat': 2,
        'Easy_inst': 2,
        'Easy_exp': 2,
        'Amount_setup': 2,
        'Agile': 2
    }
    return fi_levels

class mywindow(QMainWindow):
    def __init__(self):

        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_calculate.clicked.connect(self.onTaskBtnClick)
        self.ui.pushButton_ILF.clicked.connect(self.addILFBtnClick)
        self.ui.pushButton_EIF.clicked.connect(self.addEIFBtnClick)
        self.ui.pushButton_EI.clicked.connect(self.addEIBtnClick)
        self.ui.pushButton_EO.clicked.connect(self.addEOBtnClick)
        self.ui.pushButton_EQ.clicked.connect(self.addEQBtnClick)


        self.lang_combos = [self.ui.first_lang_comboBox,
                            self.ui.second_lang_comboBox,
                            self.ui.third_lang_comboBox]

        self.lang_perc_spins = [self.ui.first_lang_perc_spinBox,
                                self.ui.second_lang_perc_spinBox,
                                self.ui.third_lang_perc_spinBox]

        n = len(FunctionPointMethod.Languages)
        m = len(self.lang_combos)
        for i in range(m):
            for j in range(n):
                self.lang_combos[i].addItem(FunctionPointMethod.Languages[j].name)

        self.ui_spinbox_EI = {
            'easy': self.ui.simple_ei_spinBox,
            'normal': self.ui.med_ei_spinBox,
            'hard': self.ui.hard_ei_spinBox,
            'ftr' : self.ui.EI_FTR,
            'det': self.ui.EI_DET,
            'amount': self.ui.EI_Amount
        }
        self.ui_spinbox_EO = {
            'easy': self.ui.simple_eo_spinBox,
            'normal': self.ui.med_eo_spinBox,
            'hard': self.ui.hard_eo_spinBox,
            'ftr': self.ui.EO_FTR,
            'det': self.ui.EO_DET,
            'amount': self.ui.EO_Amount
        }
        self.ui_spinbox_EQ = {
            'easy': self.ui.simple_eq_spinBox,
            'normal': self.ui.med_eq_spinBox,
            'hard': self.ui.hard_eq_spinBox,
            'ftr' : self.ui.EQ_FTR,
            'det' : self.ui.EQ_DET,
            'amount': self.ui.EQ_Amount
        }
        self.ui_spinbox_EIF = {
            'easy': self.ui.simple_eif_spinBox,
            'normal': self.ui.med_eif_spinBox,
            'hard': self.ui.hard_eif_spinBox,
            'ftr' : self.ui.EIF_RET,
            'det' : self.ui.EIF_DET,
            'amount': self.ui.EIF_Amount
        }
        self.ui_spinbox_ILF = {
            'easy': self.ui.simple_ilf_spinBox,
            'normal': self.ui.med_ilf_spinBox,
            'hard': self.ui.hard_ilf_spinBox,
            'ftr' : self.ui.ILF_RET,
            'det' : self.ui.ILF_DET,
            'amount': self.ui.ILF_Amount
        }


    def addILFBtnClick(self):
        rankandamount(self,level_of_rank_ILF, self.ui_spinbox_ILF)
    def addEIFBtnClick(self):
        rankandamount(self,level_of_rank_EIF, self.ui_spinbox_EIF)
    def addEIBtnClick(self):
        rankandamount(self,level_of_rank_EI, self.ui_spinbox_EI)
    def addEOBtnClick(self):
        rankandamount(self,level_of_rank_EO, self.ui_spinbox_EO)
    def addEQBtnClick(self):
        rankandamount(self,level_of_rank_EQ, self.ui_spinbox_EQ)


    def onTaskBtnClick(self):
        fi_levels = get_default_fi_levels()
        fi_levels['Data_trans'] = self.ui.Data_trans.value()
        fi_levels['Data_proc'] = self.ui.Data_proc.value()
        fi_levels['Performance'] = self.ui.Performance.value()
        fi_levels['Exp_limit'] = self.ui.Exp_limit.value()
        fi_levels['Rate_trans'] = self.ui.Rate_trans.value()
        fi_levels['Input'] = self.ui.Input.value()
        fi_levels['Effect_work'] = self.ui.Effect_work.value()
        fi_levels['Update'] = self.ui.Update.value()
        fi_levels['Cplx'] = self.ui.Cplx.value()
        fi_levels['Repeat'] = self.ui.Repeat.value()
        fi_levels['Easy_inst'] = self.ui.Easy_inst.value()
        fi_levels['Easy_exp'] = self.ui.Easy_exp.value()
        fi_levels['Amount_setup'] = self.ui.Amount_setup.value()
        fi_levels['Agile'] = self.ui.Agile.value()
        values = fi_levels.values()
        result = sum(values)
        print(result)
        VAF = result * 0.01 + 0.65
        print(fi_levels)
        print(VAF)
        result = []
        temp = 0
        temp += self.ui.simple_ei_spinBox.value()
        temp += self.ui.med_ei_spinBox.value()
        temp += self.ui.hard_ei_spinBox.value()
        result.append(temp)
        self.ui.total_ei_label_2.setText(str(temp))

        temp = 0
        temp += self.ui.simple_eo_spinBox.value()
        temp += self.ui.med_eo_spinBox.value()
        temp += self.ui.hard_eo_spinBox.value()
        result.append(temp)
        self.ui.total_eo_label_2.setText(str(temp))

        temp = 0
        temp += self.ui.simple_eq_spinBox.value()
        temp += self.ui.med_eq_spinBox.value()
        temp += self.ui.hard_eq_spinBox.value()
        result.append(temp)
        self.ui.total_eq_label_2.setText(str(temp))

        temp = 0
        temp += self.ui.simple_eif_spinBox.value()
        temp += self.ui.med_eif_spinBox.value()
        temp += self.ui.hard_eif_spinBox.value()
        result.append(temp)
        self.ui.total_eif_label_2.setText(str(temp))

        temp = 0
        temp += self.ui.simple_ilf_spinBox.value()
        temp += self.ui.med_ilf_spinBox.value()
        temp += self.ui.hard_ilf_spinBox.value()
        result.append(temp)
        self.ui.total_ilf_label_2.setText(str(temp))

        points_sum = sum(result)
        self.ui.total_label_2.setText(str(points_sum))
        loc = 0
        temp = 0
        perc = self.lang_perc_spins[0].value()
        print('1 perc',perc)
        a = self.lang_combos[0].currentIndex()
        temp = FunctionPointMethod.Languages[a].loc_per_fp
        print(temp)
        loc_temp = temp * VAF * points_sum * perc/100
        loc += loc_temp
        #print(loc)
        perc = self.lang_perc_spins[1].value()
        print('2 perc', perc)
        a = self.lang_combos[1].currentIndex()
        temp = FunctionPointMethod.Languages[a].loc_per_fp
        loc_temp = temp * VAF * points_sum * perc / 100
        loc += loc_temp
        print(temp)
        #print(loc)
        perc = self.lang_perc_spins[2].value()
        a = self.lang_combos[2].currentIndex()
        temp = FunctionPointMethod.Languages[a].loc_per_fp
        loc_temp = temp * VAF * points_sum * perc / 100
        loc += loc_temp
        #print(loc)
        print('3 perc', perc)
        print(temp)
        self.ui.SLOC_lineEdit.setText(str(round(loc)))

        application_2 = MyWindow(round(loc))
        application_2.show()


if __name__ == '__main__':
    app = QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())





