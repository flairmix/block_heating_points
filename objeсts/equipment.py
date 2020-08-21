# Classes and functions for equipment

import object

class Equipment(object.Object):

    def __init__(self, name):
        self.name = name


class Exchanger(Equipment):

    def __init__(self, name):
        super().__init__(name)

        self.manufacturer = "Ridan"
    
    def exch_choice(self, power, consuption_main, consuption_out, t1, t2, t11, t21):
        pass



class Pump(Equipment):

    def __init__(self, name):
        super().__init__(name)

        self.manufacturer = " "

    def pump(self, type, consuption, pressure_delta):
        pass

    
class Valve_control(Equipment):
    
    def __init__(self, name, Gmax, dP_min):
        super().__init__(name)

        self.Gmax = Gmax
        self.dP_min = dP_min
        
        self.manufacturer = "Granreg"

    #Granreg
    kat33_DN = [15, 20, 25, 32, 40, 50, 65, 80, 100, 125, 150]
    kat33_Kvs = [3.2, 5, 8, 12.5, 20, 32, 50, 80, 125, 160, 200]

    km125f_DN = [15, 20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200]
    km125f_Kvs = [4, 5, 9, 15, 22, 40, 63, 90, 136, 230, 316, 555]

    def valve_control_d_pressure_choice(self, consuption, pressure_delta):
        pass

    def valve_control_consuption_choice(self, consuption, pressure_delta):
        pass


class Valve_lock(Equipment):
    
    def __init__(self, name):
        super().__init__(name)

        self.manufacturer = " "

    def valve_lock_choise(self, dn, type):
        pass


class Expansion_tank(Equipment):
    def __init__(self, name, power, temp_t1, temp_t2, static_pressure, valve_pressure):
            super().__init__(name)

            self.power = power 
            self.temp_t1 = temp_t1 
            self.temp_t2 = temp_t2 
            self.static_pressure = static_pressure 
            self.valve_pressure = valve_pressure

            self.manufacturer = " "
            
            #expansion water
            temp = [10, 20, 30, 40, 50, 60, 70, 80, 85, 90, 95, 100, 105, 110, 115, 120]
            expansion = [0.0003, 0.0017, 0.0043, 0.0078, 0.0121, 0.0171, 0.228, 0.0292, 0.0326, 0.0361, 0.0398, 0.0434, 0.0477, 0.519, 0.0562, 0.0606]

            i = 0 
            while(temp_t1 > temp[i]):
                i += 1
            self.coef_expansion = expansion[i]

            self.system_volume_l = self.power * 1163 * 15 
            self.expansion_volume = 1.05 * (self.system_volume_l * self.coef_expansion)
            self.tank_volume = int(self.expansion_volume / (1 - (self.static_pressure / self.valve_pressure)))
        
    def tank_volume_manually(self, system_volume_l):
        expansion_volume = 1.05 * (system_volume_l * self.coef_expansion)
        return int(expansion_volume / (1 - (self.static_pressure / self.valve_pressure)))
