import pipe
import module
import calc
import equipment 

heat_power = 0.0915

POWER = heat_power 
temperature_T1_main = 95
temperature_T2_main = 70


#enter
velocity_main_enter = 0.5

pressure_t1 = 6.0      #!!!
pressure_t2 = 3.0      #!!!

dP_min_enter = 0.5
number_valve_dp = 3



print("--------------------------------------------------------------------")
print("Power_heat (GCal/h) -      ", round(heat_power, 4))
print("---")

module_enter = module.Enter_module("module_enter",
    POWER, 
    temperature_T1_main,
    temperature_T2_main,
    temperature_T1_main, 
    temperature_T2_main, 
    pressure_t1, pressure_t2)

valve_control_dP = equipment.Valve_control("valve_control_dP", module_enter.consumption_main, dP_min_enter)

print("pipe_enter_consumption_main - ", round(module_enter.consumption_main, 3), " t/h")
print("velocity_main -               ", velocity_main_enter)
print("pipe_dn_main -                ", module_enter.pipe_dn(module_enter.consumption_main, 
                                        velocity_main_enter))

print("dP_min -                      ", dP_min_enter)
print("Kv valve dP -                 ", calc.kv(module_enter.consumption_main, dP_min_enter))
print("valve_control_dp - Dn         ", valve_control_dP.kat33_DN[number_valve_dp],
    ", Kvs", valve_control_dP.kat33_Kvs[number_valve_dp], 
    ", dp ", calc.dp(module_enter.consumption_main, valve_control_dP.kat33_Kvs[number_valve_dp])) 

print("--------------------------------------------------------------------")