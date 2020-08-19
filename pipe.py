# Classes and functions for piping calculation 

import object

# class Pipe(object.Object):

#     def __init__(self, name):
#         self.name = name
    
#     def pipe_dn(self, consuption_th, velosity = 1):        
#         diameter_range = (20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200, 250, 300)
#         diameter_calc = int(1000 * (consuption_th / 2826 / velosity) ** 0.5)
#         i = 0
#         while diameter_calc > diameter_range[i]:
#             i += 1 
#         return diameter_range[i]

#     def pipe_consuption(self, power_gcalh, temperature_hight_T1, temperature_low_T2):
#         return float(1000 * (power_gcalh / (temperature_hight_T1 - temperature_low_T2)))
    



def pipe_dn(consuption_th, velosity = 1):        
    diameter_range = (20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200, 250, 300)
    diameter_calc = int(1000 * (consuption_th / 2826 / velosity) ** 0.5)
    i = 0
    while diameter_calc > diameter_range[i]:
        i += 1 
    return diameter_range[i]



