from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys
from random import randint
k = 'hui'

# Класс главного окна
class MyWindow(QMainWindow):
	def __init__(self, code_lines):
		QWidget.__init__(self)

		# Загрузка интерфейса
		uic.loadUi("cocomo2.ui", self)

		# Настройка radiobuttons
		self.rbPERS2.setChecked(True)
		self.rbRCPX2.setChecked(True)
		self.rbRUSE2.setChecked(True)
		self.rbPDIF2.setChecked(True)
		self.rbPREX2.setChecked(True)
		self.rbFCIL2.setChecked(True)
		self.rbSCED2.setChecked(True)

		self.rbRUSE0.setEnabled(False)
		self.rbPDIF0.setEnabled(False)
		self.rbSCED5.setEnabled(False)

		self.rbPREC2.setChecked(True)
		self.rbFLEX2.setChecked(True)
		self.rbRESL2.setChecked(True)
		self.rbTEAM2.setChecked(True)
		self.rbPMAT2.setChecked(True)

		self.groupPREC = [self.rbPREC0, self.rbPREC1, self.rbPREC2, self.rbPREC3, self.rbPREC4, self.rbPREC5]
		self.groupFLEX = [self.rbFLEX0, self.rbFLEX1, self.rbFLEX2, self.rbFLEX3, self.rbFLEX4, self.rbFLEX5]
		self.groupRESL = [self.rbRESL0, self.rbRESL1, self.rbRESL2, self.rbRESL3, self.rbRESL4, self.rbRESL5]
		self.groupTEAM = [self.rbTEAM0, self.rbTEAM1, self.rbTEAM2, self.rbTEAM3, self.rbTEAM4, self.rbTEAM5]
		self.groupPMAT = [self.rbPMAT0, self.rbPMAT1, self.rbPMAT2, self.rbPMAT3, self.rbPMAT4, self.rbPMAT5]

		self.groupPERS = [self.rbPERS0, self.rbPERS1, self.rbPERS2, self.rbPERS3, self.rbPERS4, self.rbPERS5]
		self.groupRCPX = [self.rbRCPX0, self.rbRCPX1, self.rbRCPX2, self.rbRCPX3, self.rbRCPX4, self.rbRCPX5]
		self.groupRUSE = [self.rbRUSE0, self.rbRUSE1, self.rbRUSE2, self.rbRUSE3, self.rbRUSE4, self.rbRUSE5]
		self.groupPDIF = [self.rbPDIF0, self.rbPDIF1, self.rbPDIF2, self.rbPDIF3, self.rbPDIF4, self.rbPDIF5]
		self.groupPREX = [self.rbPREX0, self.rbPREX1, self.rbPREX2, self.rbPREX3, self.rbPREX4, self.rbPREX5]
		self.groupFCIL = [self.rbFCIL0, self.rbFCIL1, self.rbFCIL2, self.rbFCIL3, self.rbFCIL4, self.rbFCIL5]
		self.groupSCED = [self.rbSCED0, self.rbSCED1, self.rbSCED2, self.rbSCED3, self.rbSCED4, self.rbSCED5]

		self.pushButtonCalculate.clicked.connect(lambda: button_calculate_1())
		self.pushButtonCalculate_2.clicked.connect(lambda: button_calculate_2())
		self.code_lines = code_lines


		def button_calculate_1():
			work, time = calculate_cocomo2_model_1(calculate_earch(), calculate_object_points(), calculate_power())
			
			self.label_work.setText(str(round(work, 3)))
			self.label_time.setText(str(round(time, 3)))
			self.label_workers.setText(str(round(work / time, 3)))
			self.label_budget.setText(str(round(work / time * float(self.lineEditSalary.text()), 3)))


		def button_calculate_2():
			work, time = calculate_cocomo2_model_2(calculate_earch(), self.code_lines, calculate_power())
			
			self.label_work_2.setText(str(round(work, 3)))
			self.label_time_2.setText(str(round(time, 3)))
			self.label_workers_2.setText(str(round(work / time, 3)))
			self.label_budget_2.setText(str(round(work / time * float(self.lineEditSalary_2.text()), 3)))


		def calculate_cocomo2_model_1(earch, object_points, power):
			prod_table = [4, 7, 13, 25, 50]
			nop = object_points * (100 - float(self.lineEditRUSE.text())) / 100
			work = nop / prod_table[self.comboBoxXP.currentIndex()]
			time = 3 * work ** (0.33 + 0.2 * (power - 1.01))

			return work, time


		def calculate_cocomo2_model_2(earch, ksloc, power):
			work = 2.45 * earch * ksloc ** power
			time = 3 * work ** (0.33 + 0.2 * (power - 1.01))

			return work, time


		def calculate_object_points():
			forms = int(self.lineEditForms_0.text()) + int(self.lineEditForms_1.text()) * 2 + int(self.lineEditForms_2.text()) * 3
			reports = int(self.lineEditReport_0.text()) * 2 + int(self.lineEditReport_1.text()) * 5 + int(self.lineEditReport_2.text()) * 8
			third_gen_language = int(self.lineEditLanguages.text()) * 10
			return forms + reports + third_gen_language


		def calculate_earch():
			tablePERS = [1.62, 1.26, 1.00, 0.83, 0.63, 0.5]
			tableRCPX = [0.60, 0.83, 1.00, 1.33, 1.91, 2.72]
			tableRUSE = [None, 0.95, 1.00, 1.07, 1.15, 1.24]
			tablePDIF = [None, 0.87, 1.00, 1.29, 1.81, 2.61]
			tablePREX = [1.33, 1.22, 1.00, 0.87, 0.74, 0.62]
			tableFCIL = [1.30, 1.10, 1.00, 0.87, 0.73, 0.62]
			tableSCED = [1.43, 1.14, 1.00, 1.00, 1.00, None]
			result = 1

			result *= tablePERS[get_rb_index(self.groupPERS)]
			result *= tableRCPX[get_rb_index(self.groupRCPX)]
			result *= tableRUSE[get_rb_index(self.groupRUSE)]
			result *= tablePDIF[get_rb_index(self.groupPDIF)]
			result *= tablePREX[get_rb_index(self.groupPREX)]
			result *= tableFCIL[get_rb_index(self.groupFCIL)]
			result *= tableSCED[get_rb_index(self.groupSCED)]

			return result


		def calculate_power():
			tablePREC = [6.2, 4.96, 3.72, 2.48, 1.24, 0]
			tableFLEX = [5.07, 4.05, 3.04, 2.03, 1.01, 0]
			tableRESL = [7, 5.65, 4.24, 2.83, 1.41, 0]
			tableTEAM = [5.48, 4.38, 3.29, 2.19, 1.1, 0]
			tablePMAT = [7, 6.24, 4.68, 1.12, 1.56, 0]
			power = 0

			power += tablePREC[get_rb_index(self.groupPREC)]
			power += tableFLEX[get_rb_index(self.groupFLEX)]
			power += tableRESL[get_rb_index(self.groupRESL)]
			power += tableTEAM[get_rb_index(self.groupTEAM)]
			power += tablePMAT[get_rb_index(self.groupPMAT)]

			power = power / 100 + 1.01

			return power


		def get_rb_index(rb_group):
			for i in range(len(rb_group)):
				if rb_group[i].isChecked():
					return i
			return 2

