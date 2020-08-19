
import object


coef_propilen = 1

coef_refill = 15 #литров / кВт
time_refill = 8 

class Module(object.Object):
    def __init__(self, 
        name, 
        power_gcalh, 
        temperature_T1_main, 
        temperature_T2_main, 
        temperature_T1_out, 
        temperature_T2_out):
            self.name = name
            self.power_gcalh = power_gcalh
            self.temperature_T1_main = temperature_T1_main
            self.temperature_T2_main = temperature_T2_main
            self.temperature_T1_out = temperature_T1_out 
            self.temperature_T2_out = temperature_T2_out

            self.consumption_main = 1000 * power_gcalh / (coef_propilen * (temperature_T1_main - temperature_T2_main)) 
            self.consumption_out = 1000 * power_gcalh / (coef_propilen * (temperature_T1_out - temperature_T2_out))

    def pipe_dn(self, consuption_th, velosity = 1):        
        diameter_range = (20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200, 250, 300)
        diameter_calc = int(1000 * (consuption_th / 2826 / velosity) ** 0.5)
        i = 0
        while diameter_calc > diameter_range[i]:
            i += 1 
        return diameter_range[i]




class Enter_module(Module): 

    def __init__(self, 
        name,
        power_gcalh,
        temperature_T1_main,
        temperature_T2_main,
        temperature_T1_out,  
        temperature_T2_out,
        pressure_t1, 
        pressure_t2):
            super().__init__(name,
                power_gcalh,
                temperature_T1_main,
                temperature_T2_main,
                temperature_T1_out, 
                temperature_T2_out)

            self.pressure_t1 = pressure_t1
            self.pressure_t2 = pressure_t2


class YYTE(Module): # узел учета тепловой энергии 
    pass


class Heat_module(Module):  # ? do i need this 

    def __init__(self, 
        name, 
        power_gcalh, 
        temperature_T1_main, 
        temperature_T2_main, 
        temperature_T1_out, 
        temperature_T2_out):
            super().__init__(name, 
                power_gcalh, 
                temperature_T1_main, 
                temperature_T2_main, 
                temperature_T1_out, 
                temperature_T2_out)
        
            self.heat_refilling_consumption =  self.power_gcalh * 1.163 * (coef_refill / time_refill)
            self.heat_refilling_dn = self.pipe_dn(self.heat_refilling_consumption, 0.6)


class Heat_module_undependent_1system(Heat_module):

    def __init__(self, 
            name, 
            power_gcalh,
            temperature_T1_main, 
            temperature_T2_main, 
            temperature_T1_out, 
            temperature_T2_out, 
            exch_count, 
            exch_percent):
            super().__init__(name, 
                power_gcalh, 
                temperature_T1_main, 
                temperature_T2_main, 
                temperature_T1_out, 
                temperature_T2_out)

            self.exch_count = exch_count
            self.exch_percent = exch_percent 

            exch_one_power = power_gcalh / (exch_percent * 100) 
            consuption_exch_one_main = 1000 * exch_one_power / (temperature_T1_main - temperature_T2_main) 
            consuption_exch_one_out = 1000 * exch_one_power / (temperature_T1_out - temperature_T2_out) 


class Heat_module_dependent(Heat_module):
    
    def __init__(self, 
        name, 
        power_gcalh, 
        temperature_T1_main, 
        temperature_T2_main, 
        temperature_T1_out, 
        temperature_T2_out):
            super().__init__(name, 
                power_gcalh, 
                temperature_T1_main, 
                temperature_T2_main, 

                temperature_T1_out, 
                temperature_T2_out)

                # TODO 





class Vent_module(Module):

    def __init__(self, 
        name, 
        power_gcalh, 
        temperature_T1_main, 
        temperature_T2_main, 
        temperature_T1_out, 
        temperature_T2_out):
            super().__init__(name, 
                power_gcalh, 
                temperature_T1_main, 
                temperature_T2_main, 
                temperature_T1_out, 
                temperature_T2_out)
            
            self.vent_refilling_consumption =  self.power_gcalh * 1.163 * (coef_refill / time_refill)
            self.vent_refilling_dn = self.pipe_dn(self.vent_refilling_consumption, 0.7)




class Hotwater_module(Module): 

    def __init__(self, 
        name, 
        power_gcalh, 
        temperature_T1_main, 
        temperature_T2_main, 
        temperature_T1_out, 
        temperature_T2_out):
            super().__init__(name, 
                power_gcalh, 
                temperature_T1_main, 
                temperature_T2_main, 
                temperature_T1_out, 
                temperature_T2_out)



    
