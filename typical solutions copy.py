import pandas as pd 
import calc
from math import sqrt


PATH_FOR_SAVE = 'G:\\2_work_engineer\\raschet_po'
Dn = [50, 65, 80, 100, 125, 150, 200]
DN_pipe = (20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200, 250, 300)

def consumption(Dn, V_ms): 
    return (V_ms * ((Dn / 1000)** 2) * 2826)

def power(consumption, t_max, t_min):
    return consumption * (t_max - t_min) / 1000

def pipeDn(G, v = 1):
    DN = (20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200, 250, 300)
    dn = int(1000 * (G / 2826 / v) ** 0.5)
    i = 0
    while dn > DN[i]:
        i += 1 
    return DN[i]

    
class Enter_module():
    def __init__(self):    
        self.ID_element = []        
        self.tempt1 = 150
        self.tempt2 = 70
        self.flowspeed_min = 0.5
        self.flowspeed_max = 0.8

        self.df_sheet = pd.DataFrame(columns= ['number'] 
                                        + ['Dn'] 
                                        + ['Расход_min, m3\\h '] 
                                        + ['Расход_max, m3\\h'] 
                                        + ['Qmin, gcal / h'] 
                                        + ['Qmax, gcal / h'],
                                        index = self.ID_element)

    def print_me(self):
        print(self.df_sheet)

    def to_csv(self):
        self.df_sheet.to_csv(PATH_FOR_SAVE + 
                            '\\enter_module_{t1}-{t2}, {v1}-{v2}'.format(t1=self.tempt1, t2=self.tempt2, v1=self.flowspeed_min, v2=self.flowspeed_max) + 
                            '.csv', sep=';', encoding="ansi")
    
    def add_element(self, number, Dn, consuption_min, consuption_max, Qmin, Qmax):
        self.df_sheet.loc[self.ID_element[number]] = [number, Dn, consuption_min, consuption_max, Qmin, Qmax]


class Heat_module():
    def __init__(self):    
        self.ID_element = []        
        self.tempt1 = 95
        self.tempt2 = 70
        self.tempt11 = 80
        self.tempt21 = 60
        self.flowspeed_min_hot = 0.5
        self.flowspeed_max_hot = 0.8
        self.flowspeed_min_cold = 0.4
        self.flowspeed_max_cold = 0.6

        self.df_heat_typ_module = pd.DataFrame(columns= ['number'] 
                                                        + ['Dn_cold'] 
                                                        + ['Расход_min_cold, m3/h '] 
                                                        + ['Расход_max_cold, m3/h']
                                                        + ['Qmin_cold, gcal/h'] 
                                                        + ['Qmax_cold, gcal / h']
                                                        + ['Dn_min_hot']
                                                        + ['Dn_max_hot']
                                                        + ['Расход_min_hot, m3/h '] 
                                                        + ['Расход_max_hot, m3/h'] 
                                                        + ['Qmin_hot, gcal/h'] 
                                                        + ['Qmax_hot, gcal/h'],
                                                        index = self.ID_element)


    def print_me(self): 
        print(self.df_heat_typ_module)

    def to_csv(self):
        self.df_heat_typ_module.to_csv(PATH_FOR_SAVE + '\\heat_module_cold({t11}-{t21},{v11}-{v21}), hot({t1}-{t2}, {v1}-{v2})'.format(t11=self.tempt11, 
                                                                                                        t21=self.tempt21,
                                                                                                        v11=self.flowspeed_min_cold, 
                                                                                                        v21=self.flowspeed_max_cold,
                                                                                                        t1=self.tempt1, 
                                                                                                        t2=self.tempt2,
                                                                                                        v1=self.flowspeed_min_hot, 
                                                                                                        v2=self.flowspeed_max_hot) + \
                                                                                                        '.csv', sep=';', encoding="ansi")
    
    def add_element(self, 
                    number, 
                    Dn_cold,
                    consuption_min_cold, 
                    consuption_max_cold, 
                    Qmin_cold, 
                    Qmax_cold,
                    Dn_hot_min,
                    Dn_hot_max,
                    consuption_min_hot, 
                    consuption_max_hot, 
                    Qmin_hot, 
                    Qmax_hot):
        self.df_heat_typ_module.loc[self.ID_element[number]] = [number, 
                                                                Dn_cold, 
                                                                consuption_min_cold, 
                                                                consuption_max_cold, 
                                                                Qmin_cold, 
                                                                Qmax_cold,
                                                                Dn_hot_min,
                                                                Dn_hot_max,
                                                                consuption_min_hot, 
                                                                consuption_max_hot, 
                                                                Qmin_hot, 
                                                                Qmax_hot]



enter_module = Enter_module()
for i in range (0, len(Dn)):
    enter_module.ID_element.append(i)
    enter_module.add_element(i, 
                            Dn[i], 
                            consumption(Dn[i], enter_module.flowspeed_min), 
                            consumption(Dn[i], enter_module.flowspeed_max),
                            power((consumption(Dn[i], enter_module.flowspeed_min)), enter_module.tempt1, enter_module.tempt2), 
                            power((consumption(Dn[i], enter_module.flowspeed_max)), enter_module.tempt1, enter_module.tempt2))



enter_module.to_csv()
heat_module = Heat_module()
number = 0
heat_module.ID_element.append(number)

for i in range (0, len(Dn)):
    #cold side 
    Dn_cold = Dn[i]
    consuption_min_cold = consumption(Dn_cold, heat_module.flowspeed_min_cold) 
    consuption_max_cold = consumption(Dn_cold, heat_module.flowspeed_max_cold) 
    Qmin_cold = power((consumption(Dn[i], heat_module.flowspeed_min_cold)), heat_module.tempt11, heat_module.tempt21) 
    Qmax_cold = power((consumption(Dn[i], heat_module.flowspeed_max_cold)), heat_module.tempt11, heat_module.tempt21)

    #hot side
    consuption_min_hot = Qmin_cold * 1000 / (heat_module.tempt1 - heat_module.tempt2) 
    consuption_max_hot = Qmax_cold * 1000 / (heat_module.tempt1 - heat_module.tempt2) 
    Dn_hot_min = pipeDn(consuption_min_hot, heat_module.flowspeed_min_hot)     
    Dn_hot_max = pipeDn(consuption_max_hot, heat_module.flowspeed_min_hot)
    Qmin_hot = Qmin_cold  
    Qmax_hot = Qmax_cold

    while Dn_hot_min <= Dn_hot_max:
        print(heat_module.ID_element)
        if Dn_hot_max == Dn_hot_min:
            number += 1
            heat_module.ID_element.append(number)
            heat_module.add_element(number, 
                                    Dn_cold, 
                                    consuption_min_cold, 
                                    consuption_max_cold, 
                                    Qmin_cold, 
                                    Qmax_cold,
                                    Dn_hot_min,
                                    Dn_hot_max,
                                    consuption_min_hot, 
                                    consuption_max_hot, 
                                    Qmin_hot, 
                                    Qmax_hot                       
                                    )
            break
        else:
            # print(DN_pipe[DN_pipe.index(Dn_hot_min) + 1])
            # while Dn_hot_min < Dn_hot_max:
            number += 1
            heat_module.ID_element.append(number)
            heat_module.add_element(number, 
                                    Dn_cold, 
                                    consuption_min_cold, 
                                    consuption_max_cold, 
                                    Qmin_cold, 
                                    Qmax_cold,
                                    Dn_hot_min,
                                    Dn_hot_max,
                                    consuption_min_hot, 
                                    consuption_max_hot, 
                                    Qmin_hot, 
                                    Qmax_hot                       
                                    )        
                
            Dn_hot_min = DN_pipe[DN_pipe.index(Dn_hot_min) + 1]
            number += 1
            heat_module.ID_element.append(number)

            heat_module.add_element(number, 
                                    Dn_cold, 
                                    consuption_min_cold, 
                                    consuption_max_cold, 
                                    Qmin_cold, 
                                    Qmax_cold,
                                    Dn_hot_min,
                                    Dn_hot_max,
                                    consuption_min_hot, 
                                    consuption_max_hot, 
                                    Qmin_hot, 
                                    Qmax_hot                       
                                    )           

heat_module.print_me()

print(heat_module.ID_element)

heat_module.to_csv()