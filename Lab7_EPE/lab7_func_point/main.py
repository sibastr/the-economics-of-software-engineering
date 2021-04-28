from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys
from random import randint
from cocomo2 import Ui_MainWindow2


# Класс главного окна
class MyWindow(QMainWindow):
	def __init__(self, code_lines):
		QWidget.__init__(self)

		# Загрузка интерфейса
		#uic.loadUi("cocomo2.ui", self)

		self.ui = Ui_MainWindow2()
		self.ui.setupUi(self)

		# Настройка radiobuttons
		self.ui.rbPERS2.setChecked(True)
		self.ui.rbRCPX4.setChecked(True)
		self.ui.rbRUSE1.setChecked(True)
		self.ui.rbPDIF3.setChecked(True)
		self.ui.rbPREX1.setChecked(True)
		self.ui.rbFCIL4.setChecked(True)
		self.ui.rbSCED0.setChecked(True)

		self.ui.rbRUSE0.setEnabled(False)
		self.ui.rbPDIF0.setEnabled(False)
		self.ui.rbSCED5.setEnabled(False)

		self.ui.rbPREC2.setChecked(True)
		self.ui.rbFLEX4.setChecked(True)
		self.ui.rbRESL1.setChecked(True)
		self.ui.rbTEAM2.setChecked(True)
		self.ui.rbPMAT1.setChecked(True)

		self.groupPREC = [self.ui.rbPREC0, self.ui.rbPREC1, self.ui.rbPREC2, self.ui.rbPREC3, self.ui.rbPREC4, self.ui.rbPREC5]
		self.groupFLEX = [self.ui.rbFLEX0, self.ui.rbFLEX1, self.ui.rbFLEX2, self.ui.rbFLEX3, self.ui.rbFLEX4, self.ui.rbFLEX5]
		self.groupRESL = [self.ui.rbRESL0, self.ui.rbRESL1, self.ui.rbRESL2, self.ui.rbRESL3, self.ui.rbRESL4, self.ui.rbRESL5]
		self.groupTEAM = [self.ui.rbTEAM0, self.ui.rbTEAM1, self.ui.rbTEAM2, self.ui.rbTEAM3, self.ui.rbTEAM4, self.ui.rbTEAM5]
		self.groupPMAT = [self.ui.rbPMAT0, self.ui.rbPMAT1, self.ui.rbPMAT2, self.ui.rbPMAT3, self.ui.rbPMAT4, self.ui.rbPMAT5]

		self.groupPERS = [self.ui.rbPERS0, self.ui.rbPERS1, self.ui.rbPERS2, self.ui.rbPERS3, self.ui.rbPERS4, self.ui.rbPERS5]
		self.groupRCPX = [self.ui.rbRCPX0, self.ui.rbRCPX1, self.ui.rbRCPX2, self.ui.rbRCPX3, self.ui.rbRCPX4, self.ui.rbRCPX5]
		self.groupRUSE = [self.ui.rbRUSE0, self.ui.rbRUSE1, self.ui.rbRUSE2, self.ui.rbRUSE3, self.ui.rbRUSE4, self.ui.rbRUSE5]
		self.groupPDIF = [self.ui.rbPDIF0, self.ui.rbPDIF1, self.ui.rbPDIF2, self.ui.rbPDIF3, self.ui.rbPDIF4, self.ui.rbPDIF5]
		self.groupPREX = [self.ui.rbPREX0, self.ui.rbPREX1, self.ui.rbPREX2, self.ui.rbPREX3, self.ui.rbPREX4, self.ui.rbPREX5]
		self.groupFCIL = [self.ui.rbFCIL0, self.ui.rbFCIL1, self.ui.rbFCIL2, self.ui.rbFCIL3, self.ui.rbFCIL4, self.ui.rbFCIL5]
		self.groupSCED = [self.ui.rbSCED0, self.ui.rbSCED1, self.ui.rbSCED2, self.ui.rbSCED3, self.ui.rbSCED4, self.ui.rbSCED5]

		self.ui.pushButtonCalculate.clicked.connect(lambda: button_calculate_1())
		self.ui.pushButtonCalculate_2.clicked.connect(lambda: button_calculate_2())
		self.code_lines = code_lines
		self.ui.lineEditLines.setText(str(code_lines))


		def button_calculate_1():
			work, time = calculate_cocomo2_model_1(calculate_earch(), calculate_object_points(), calculate_power())
			
			self.ui.label_work.setText(str(round(work, 3)))
			self.ui.label_time.setText(str(round(time, 3)))
			self.ui.label_workers.setText(str(round(work / time, 3)))
			self.ui.label_budget.setText(str(round(work * float(self.ui.lineEditSalary.text()), 3)))


		def button_calculate_2():
			lines = int(self.ui.lineEditLines.text()) / 1000
			work, time = calculate_cocomo2_model_2(calculate_earch(), lines, calculate_power())
			
			self.ui.label_work_2.setText(str(round(work, 3)))
			self.ui.label_time_2.setText(str(round(time, 3)))
			self.ui.label_workers_2.setText(str(round(work / time, 3)))
			self.ui.label_budget_2.setText(str(round(work * float(self.ui.lineEditSalary_2.text()), 3)))


		def calculate_cocomo2_model_1(earch, object_points, power):
			prod_table = [4, 7, 13, 25, 50]
			nop = object_points * (100 - float(self.ui.lineEditRUSE.text())) / 100
			work = nop / prod_table[self.ui.comboBoxXP.currentIndex()]
			time = 3 * work ** (0.33 + 0.2 * (power - 1.01))

			return work, time


		def calculate_cocomo2_model_2(earch, ksloc, power):
			work = 2.45 * earch * ksloc ** power
			time = 3 * work ** (0.33 + 0.2 * (power - 1.01))

			return work, time


		def calculate_object_points():
			forms = int(self.ui.lineEditForms_0.text()) + int(self.ui.lineEditForms_1.text()) * 2 + int(self.ui.lineEditForms_2.text()) * 3
			reports = int(self.ui.lineEditReport_0.text()) * 2 + int(self.ui.lineEditReport_1.text()) * 5 + int(self.ui.lineEditReport_2.text()) * 8
			third_gen_language = int(self.ui.lineEditLanguages.text()) * 10
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




if __name__ == '__main__':
	app = QApplication([])
	application = MyWindow(2568)
	application.show()

	sys.exit(app.exec())