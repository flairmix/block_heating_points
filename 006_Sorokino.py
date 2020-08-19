import pipe
import module
import calc
import equipment 

heat_power = 0.115
vent_power = 0.410

POWER = heat_power + vent_power
temperature_T1_main = 80
temperature_T2_main = 70


#enter
velocity_main_enter = 1

pressure_t1 = 2.94
pressure_t2 = 2.45



#vent 
#пропиленгликоль 30 %

velocity_out_vent = 0.7

temperature_T1_out_vent = 75
temperature_T2_out_vent = 60
dP_min_vent = 0.5
static_pressure_vent = 1.5
max_pressure_vent = 6

dp_pressure_vent_system = 0.5

number_valve_vent = 8                              #todo 

dp_min_vent_refill = 0.5                           #todo                                                                         
number_valve_vent_refill = 0                       #todo 

vent_pump_circ_pressure = dp_pressure_vent_system + 0.5 + 0.3




print("--------------------------------------------------------------------")
print("Power (GCal/h) -           ", POWER)
print("Power (kW) -               ", calc.GCalh_to_kW(POWER))
print("Power_heat (GCal/h) -      ", heat_power)
print("Power_vent (GCal/h) -      ", vent_power)
print("---")

module_enter = module.Enter_module("module_enter",
    POWER, 
    temperature_T1_main,
    temperature_T2_main,
    temperature_T1_main, 
    temperature_T2_main, 
    pressure_t1, pressure_t2)


print("pipe_enter_consumption_main - ", module_enter.consumption_main, " t/h")
print("velocity_main -               ", velocity_main_enter)
print("pipe_dn_main -                ", module_enter.pipe_dn(module_enter.consumption_main, 
                                        velocity_main_enter))



print("--------------------------------------------------------------------")



#vent

module_vent = module.Vent_module("module_vent", 
    vent_power, 
    temperature_T1_main,
    temperature_T2_main,
    temperature_T1_out_vent,
    temperature_T2_out_vent) 

valve_control_vent = equipment.Valve_control("valve_control_vent", 
    module_vent.consumption_main, 
    dP_min_vent)

expansion_tank_vent = equipment.Expansion_tank("expansion_tank_vent", 
    module_vent.power_gcalh, 
    module_vent.temperature_T1_out, 
    module_vent.temperature_T2_out, 
    static_pressure_vent, 
    max_pressure_vent)



print("vent")
print("power_vent (Gcalh) -                     ", vent_power)
print("pipe_vent_consumption_main -             ", module_vent.consumption_main, " t/h")
print("pipe_vent_consumption_out -              ", module_vent.consumption_out, " t/h")
print("velocity_main -                          ", velocity_main_enter)
print("velocity_out -                           ", velocity_out_vent)
print("pipe_dn_main -                           ", module_vent.pipe_dn(module_vent.consumption_main, velocity_main_enter))
print("pipe_dn_out -                            ", module_vent.pipe_dn(module_vent.consumption_out, velocity_out_vent))

print("---")
print("dP_min -                                  ", dP_min_vent)
print("Kv valve dP -                             ", calc.kv(module_vent.consumption_main, dP_min_vent))
print("valve_control_vent - Dn", valve_control_vent.km125f_DN[number_valve_vent],
    ", Kvs", valve_control_vent.km125f_Kvs[number_valve_vent], 
    ", dp ", calc.dp(module_vent.consumption_main, valve_control_vent.km125f_Kvs[number_valve_vent])) 
print("---")
print("refilling")
print("vent_refilling_consumption (t/h) -         ", module_vent.vent_refilling_consumption)
print("vent_refilling_dn -                        ", module_vent.vent_refilling_dn)

print("---")
print("dP_min_refill -                            ", dp_min_vent_refill)
print("Kv valve dP -                              ", calc.kv(module_vent.vent_refilling_consumption, dp_min_vent_refill))
print("valve_control_vent - Dn ", valve_control_vent.km125f_DN[number_valve_vent_refill],
    ", Kvs", valve_control_vent.km125f_Kvs[number_valve_vent_refill], 
    ", dp ", calc.dp(module_vent.vent_refilling_consumption, valve_control_vent.km125f_Kvs[number_valve_vent_refill])) 

print("---")
print("exp_tank")
print("expansion_tank_vent_l -                    ", expansion_tank_vent.tank_volume)

print("---")
print("pumps_main")
print("pumps_cons + 0.15% (t/h) -                 ", module_vent.consumption_out * 1.15)
print("pumps_pressure(bar) -                      ", vent_pump_circ_pressure)
print("---")
print("pumps_refill")
print("pumps_cons(t/h) -                          ", module_vent.vent_refilling_consumption)
print("pumps_pressure(bar) -                      ", static_pressure_vent + dp_min_vent_refill + 0.3)
print("--------------------------------------------------------------------")
