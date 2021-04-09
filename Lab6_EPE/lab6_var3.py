import matplotlib.pyplot as plt
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

def RelyImpact(size):
    eaf_levels = get_default_eaf_levels()
    RelyResult = []
    list_of_modes = [normal_mode, inter_mode, inbuilt_mode]
    for i in range(3):
        mode = list_of_modes[i]
        for j in range(5):
            eaf_levels['RELY'] = j
            temp_result = cocomo(size, eaf_levels, mode)
            RelyResult.append(temp_result)
    dict_result = {
        'RELY_Normal': RelyResult[0:5],
        'RELY_Inter': RelyResult[5:10],
        'RELY_Inbuilt': RelyResult[10:15]
    }
    return dict_result

def DataImpact(size):
    eaf_levels = get_default_eaf_levels()
    DataResult = []
    list_of_modes = [normal_mode, inter_mode, inbuilt_mode]
    for i in range(3):
        mode = list_of_modes[i]
        for j in range(1,5):
            eaf_levels['DATA'] = j
            #print(eaf_levels['DATA'])

            temp_result = cocomo(size, eaf_levels, mode)
            DataResult.append(temp_result)
    dict_result = {
        'DATA_Normal': DataResult[0:4],
        'DATA_Inter': DataResult[4:8],
        'DATA_Inbuilt': DataResult[8:12]
    }
    return dict_result
def CPLXImpact(size):
    eaf_levels = get_default_eaf_levels()
    CPLXResult = []
    list_of_modes = [normal_mode, inter_mode, inbuilt_mode]
    for i in range(3):
        mode = list_of_modes[i]
        for j in range(5):
            eaf_levels['CPLX'] = j
            temp_result = cocomo(size, eaf_levels, mode)
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
    plt.plot([0,1,2,3,4],work_RELY_Normal,[0,1,2,3,4],work_CPLX_Normal,[1,2,3,4],work_Data_Normal)

    plt.ylabel('Work Normal')
    plt.xlabel('Factors')
    plt.legend(['RELY','CPLX','DATA'])
    plt.show()

    plt.plot([0, 1, 2, 3, 4], work_RELY_Inter, [0, 1, 2, 3, 4], work_CPLX_Inter, [1, 2, 3, 4], work_Data_Inter)
    plt.ylabel('Work Intermediate')
    plt.xlabel('Factors')
    plt.legend(['RELY', 'CPLX', 'DATA'])
    plt.show()

    plt.plot([0, 1, 2, 3, 4], work_RELY_Inbuilt, [0, 1, 2, 3, 4], work_CPLX_Inbuilt, [1, 2, 3, 4], work_Data_Inbuilt)
    plt.ylabel('Work Inbuilt')
    plt.xlabel('Factors')
    plt.legend(['RELY', 'CPLX', 'DATA'])

    plt.show()
    # Time graph
    plt.plot([0, 1, 2, 3, 4], time_RELY_Normal, [0, 1, 2, 3, 4], time_CPLX_Normal, [1, 2, 3, 4], time_Data_Normal)

    plt.ylabel('Time Normal')
    plt.xlabel('Factors')
    plt.legend(['RELY', 'CPLX', 'DATA'])
    plt.show()

    plt.plot([0, 1, 2, 3, 4], time_RELY_Inter, [0, 1, 2, 3, 4], time_CPLX_Inter, [1, 2, 3, 4], time_Data_Inter)
    plt.ylabel('Time Intermediate')
    plt.xlabel('Factors')
    plt.legend(['RELY', 'CPLX', 'DATA'])
    plt.show()

    plt.plot([0, 1, 2, 3, 4], time_RELY_Inbuilt, [0, 1, 2, 3, 4], time_CPLX_Inbuilt, [1, 2, 3, 4], time_Data_Inbuilt)
    plt.ylabel('Time Inbuilt')
    plt.xlabel('Factors')
    plt.legend(['RELY', 'CPLX', 'DATA'])

    plt.show()

def project_tradion():
    eaf_levels = get_default_eaf_levels()
    eaf_levels['RELY'] = 4
    eaf_levels['TIME'] = 4
    eaf_levels['SCED'] = 4
    eaf_levels['PCAP'] = 4
    eaf_levels['ACAP'] = 4
    eaf_levels['CPLX'] = 4
    result_Air = cocomo(430000 / 1000, eaf_levels, inter_mode)

    work_plan_requirements = result_Air[0] * 0.08
    time_plan_requirements = result_Air[1] * 0.36

    work_design_project = result_Air[0] * 0.18
    time_design_project = result_Air[1] * 0.36

    work_details_design = result_Air[0] * 0.25
    time_details_design = result_Air[1] * 0.18

    work_code_test = result_Air[0] * 0.26
    time_code_test = result_Air[1] * 0.18

    work_integration_test = result_Air[0] * 0.31
    time_integration_test = result_Air[1] * 0.28

    print("Трудозатраты в месяцах для проекта:", result_Air[0])
    print("Время проекта в месяцах для проекта:", result_Air[1])

    print("Работа на планирование и определение требований:", work_plan_requirements)
    print("Время на планирование и определение требований:", time_plan_requirements)
    print("Работа по проектироваю проекта:", work_design_project)
    print("Время на проектирование проекта:", time_design_project)
    print("Работа по детальному проектированию:", work_details_design)
    print("Время на детальное проектирование:", time_details_design)
    print("Работа по кодированию и тестированию отдельных модулей:", work_code_test)
    print("Время на кодирование и тестирование отдельных модулей:", time_code_test)
    print("Работа на интеграцию и тестирование:", work_integration_test)
    print("Время на интеграцию и тестирование:", time_integration_test)

    print("Итоговая работа:", result_Air[0] + work_plan_requirements)
    print("Итоговое время:", result_Air[1] + time_plan_requirements)
    print("\n------------------------------------------------------------------------------\n")
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

    print("Анализ требований", analysis)
    print("Проектирование продукта", design_product)
    print("Программирование", programming)
    print("Тестирование", testing)
    print("Верификация и аттестация", verification)
    print("Канцелярия проекта", office)
    print("Управление конфигурацией и обеспечение качества", quality_assurance)
    print("Создание руководств", manuals)


    print("Итоговые человеко-месяцы", summary_work)



if __name__ == '__main__':
    d_Rely = RelyImpact(15000/1000)
    d_Data = DataImpact(15000/1000)
    d_CPLX = CPLXImpact(15000/1000)

    #Impact_Graph(d_Rely,d_CPLX,d_Data)
    project_tradion()





#print(cocomo( 100000, eaf_levels, normal_mode))
#eaf_levels = get_default_eaf_levels()
#print(cocomo(15000, eaf_levels, inter_mode))
#eaf_levels = get_default_eaf_levels()
#print(cocomo(11111, eaf_levels, inbuilt_mode))

