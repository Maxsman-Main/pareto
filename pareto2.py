import pandas as pd


def create_parameters():
    excel_data = pd.read_excel('KonstantinovM.xlsx')
    data = excel_data.iloc
    parameters = []
    for i in range(200):
        lststring = data[i].tolist()
        string = lststring[0]
        a = string.split(',')
        name = int(a[0])
        a = a[1:]
        for j in range(len(a)):
            a[j] = float(a[j])
        a.append(name)
        parameters.append(a)
    return parameters

def sorted_by_first_parameter(parameters):
    for i in range(len(parameters)):
        for j in range(len(parameters) - i - 1):
            if parameters[j][0] < parameters[j + 1][0]:
                parameters[j], parameters[j + 1] = parameters[j + 1], parameters[j]
    return parameters

def make_pareto_set(parameters):
    ln = len(parameters)
    i = 0
    while(i < ln - 1):
        indexes = []
        j = i + 1
        while(j < ln):
            if (parameters[i][1] > parameters[j][1] and parameters[i][2] >= parameters[j][2]) or (parameters[i][1] >= parameters[j][1] and parameters[i][2] > parameters[j][2]):
                parameters.pop(j)
                j -= 1
                ln -= 1
            j += 1
        i += 1
    return parameters
            

parameters = create_parameters()
parameters = sorted_by_first_parameter(parameters)
parameters = make_pareto_set(parameters)

for i in range(len(parameters)):
    print(parameters[i])
