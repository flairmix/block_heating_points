import pipe
import module
import calc
import equipment 

heat_power = 0.12037
vent_power = 0.2337
hot_water_power = 0.02527

POWER = heat_power + vent_power + hot_water_power
temperature_T1_main = 95
temperature_T2_main = 80


#enter
velocity_main_enter = 0.9

pressure_t1 = 7.9      #!!!
pressure_t2 = 5.3      #!!!

dP_min_enter = 1.0
number_valve_dp = 6


#heat _____________________________________________________
velocity_out_heat = 0.6

temperature_T1_out_heat = 80
temperature_T2_out_heat = 60
dp_min_heat = 0.5
static_pressure_heat = 0.85
max_pressure_heat = 6                            #!!!!!!! 

dp_pressure_heat_system = 0.3
number_valve_heat = 4                            #todo 

dp_min_heat_refill = 0.5                         #todo                                                                         
number_valve_heat_refill = 0                     #todo 

heat_pumps_circ_pressure = dp_pressure_heat_system + 0.3

# heat_system_volume = 1600


#vent  _____________________________________________________

velocity_out_vent = 0.6

temperature_T1_out_vent = 90
temperature_T2_out_vent = 70
dP_min_vent = 0.5
static_pressure_vent = 0.8
max_pressure_vent = 6

dp_pressure_vent_system = 0.5

number_valve_vent = 5                              #todo 

dp_min_vent_refill = 0.5                           #todo                                                                         
number_valve_vent_refill = 2                       #todo 

vent_pump_circ_pressure = dp_pressure_vent_system + 0.3

vent_system_volume = 31

#hot_water _____________________________________________________

temperature_T1_out_hot_water = 65 
temperature_T2_out_hot_water = 5
dp_min_hot_water = 0.5

velocity_out_hot_water = 0.5

hot_water_cons_T1_2st = 3.72
number_valve_hot_water = 4



print("--------------------------------------------------------------------")
print("Power (GCal/h) -           ", round(POWER, 4))
print("Power (kW) -               ", round(calc.GCalh_to_kW(POWER), 4))
print("Power_heat (GCal/h) -      ", round(heat_power, 4))
print("Power_vent (GCal/h) -      ", round(vent_power, 4))
print("Power_hot_water (GCal/h) - ", round(hot_water_power, 4))
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
print("valve_control_dp - Dn         ", valve_control_dP.km125f_DN[number_valve_dp],
    ", Kvs", valve_control_dP.km125f_Kvs[number_valve_dp], 
    ", dp ", calc.dp(module_enter.consumption_main, valve_control_dP.km125f_Kvs[number_valve_dp])) 

print("--------------------------------------------------------------------")




#heat

module_heat = module.Heat_module("module_heat", 
    heat_power, 
    temperature_T1_main, 
    temperature_T2_main, 
    temperature_T1_out_heat, 
    temperature_T2_out_heat)

valve_control_heat = equipment.Valve_control("valve_control_heat", 
    module_heat.consumption_main, 
    dp_min_heat)

expansion_tank_heat = equipment.Expansion_tank("expansion_tank_heat", 
    module_heat.power_gcalh, 
    module_heat.temperature_T1_out, 
    module_heat.temperature_T2_out, 
    static_pressure_heat, 
    max_pressure_heat)


print("heat")
print("heat_power -                       ", heat_power)
print("temperature_T1_out_heat -          ", temperature_T1_out_heat, "\n"
      "temperature_T2_out_heat -          ", temperature_T2_out_heat)

print("pipe_heat_consumption_main -       ", module_heat.consumption_main, " t/h")
print("pipe_heat_consumption_out -        ", module_heat.consumption_out, " t/h")
print("velocity_main -                    ", velocity_main_enter)
print("velocity_out -                     ", velocity_out_heat)
print("pipe_dn_main -                     ", module_heat.pipe_dn(module_heat.consumption_main, velocity_main_enter))
print("pipe_dn_out -                      ", module_heat.pipe_dn(module_heat.consumption_out, velocity_out_heat))

print("---")

print("dP_min -                           ", dp_min_heat)
print("Kv valve dP -                      ", calc.kv(module_heat.consumption_main, dp_min_heat))
print("valve_control_vent - Dn            ", valve_control_heat.km125f_DN[number_valve_heat],
    ", Kvs", valve_control_heat.km125f_Kvs[number_valve_heat], 
    ", dp ", calc.dp(module_heat.consumption_main, valve_control_heat.km125f_Kvs[number_valve_heat])) 
print("---")

print("refilling")
print("heat_refilling_consumption (t/h) - ", module_heat.heat_refilling_consumption)
print("heat_refilling_dn -                ", module_heat.heat_refilling_dn)

print("dP_min_refill -                    ", dp_min_heat_refill)

print("Kv valve dP -                      ", calc.kv(module_heat.heat_refilling_consumption, dp_min_heat_refill))
print("valve_control_heat - Dn            ", valve_control_heat.km125f_DN[number_valve_heat_refill],
    ", Kvs", valve_control_heat.km125f_Kvs[number_valve_heat_refill], 
    ", dp ", calc.dp(module_heat.heat_refilling_consumption, valve_control_heat.km125f_Kvs[number_valve_heat_refill])) 
print("---")
print("exp_tank")
print("expansion_tank_heat_l -            ", expansion_tank_heat.tank_volume)
# print("expansion_tank_heat_l_manually -   ", expansion_tank_heat.tank_volume_manually(heat_system_volume))

print("---")
print("pumps_main")
print("pumps_cons + 0.15% (t/h) -         ", module_heat.consumption_out * 1.15)
print("pumps_pressure(bar) -              ", heat_pumps_circ_pressure)
print("---")
print("pumps_refill")
print("pumps_cons(t/h) -                  ", module_heat.heat_refilling_consumption)
print("pumps_pressure(bar) -              ", static_pressure_heat - pressure_t2 + dp_min_heat_refill + 0.3)


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
print("pipe_vent_consumption_main -             ", round(module_vent.consumption_main, 3), " t/h")
print("pipe_vent_consumption_out -              ", round(module_vent.consumption_out, 3), " t/h")
print("velocity_main -                          ", velocity_main_enter)
print("velocity_out -                           ", velocity_out_vent)
print("pipe_dn_main -                           ", module_vent.pipe_dn(module_vent.consumption_main, velocity_main_enter))
print("pipe_dn_out -                            ", module_vent.pipe_dn(module_vent.consumption_out, velocity_out_vent))

print("---")
print("dP_min -                                  ", dP_min_vent)
print("Kv valve dP -                             ", round(calc.kv(module_vent.consumption_main, dP_min_vent), 3))
print("valve_control_vent - Dn", valve_control_vent.km125f_DN[number_valve_vent],
    ", Kvs", valve_control_vent.km125f_Kvs[number_valve_vent], 
    ", dp ", calc.dp(module_vent.consumption_main, valve_control_vent.km125f_Kvs[number_valve_vent])) 
print("---")
print("refilling")
print("vent_refilling_consumption (t/h) -         ", round(module_vent.vent_refilling_consumption, 3))
print("vent_refilling_dn -                        ", module_vent.vent_refilling_dn)

print("heat + vent_refilling_consumption (t/h) -  ", round(module_vent.vent_refilling_consumption + module_heat.heat_refilling_consumption, 3))
print("heat + vent_refilling_dn -                 ", calc.pipeDn(module_vent.vent_refilling_consumption + module_heat.heat_refilling_consumption, 0.7))
print("---")
print("dP_min_refill -                            ", dp_min_vent_refill)
print("Kv valve dP -                              ", calc.kv(module_vent.vent_refilling_consumption, dp_min_vent_refill))
print("valve_control_vent - Dn ", valve_control_vent.km125f_DN[number_valve_vent_refill],
    ", Kvs", valve_control_vent.km125f_Kvs[number_valve_vent_refill], 
    ", dp ", calc.dp(module_vent.vent_refilling_consumption, valve_control_vent.km125f_Kvs[number_valve_vent_refill])) 

print("---")
print("exp_tank")
print("expansion_tank_vent_l -                    ", expansion_tank_vent.tank_volume)
print("expansion_tank_vent_l_manually -           ", expansion_tank_vent.tank_volume_manually(vent_system_volume))

print("---")
print("pumps_main")
print("pumps_cons + 0.15% (t/h) -                 ", round(module_vent.consumption_out * 1.15, 3))
print("pumps_pressure(bar) -                      ", vent_pump_circ_pressure)
print("---")
print("pumps_refill")
print("pumps_cons(t/h) -                          ", round(module_vent.vent_refilling_consumption, 3))
print("pumps_pressure(bar) -                      ", static_pressure_vent - pressure_t2 + dp_min_vent_refill + 0.3)
print("--------------------------------------------------------------------")



#hot_water

module_hot_water = module.Heat_module("module_hot_water", 
    hot_water_power, 
    temperature_T1_main, 
    temperature_T2_main, 
    temperature_T1_out_hot_water, 
    temperature_T2_out_hot_water)

valve_control_hot_water = equipment.Valve_control("valve_control_hot_water", 
    module_hot_water.consumption_main, 
    dp_min_hot_water)


print("hot_water")
print("hot_water_power -                  ", hot_water_power)
print("temperature_T1_out_hot_water -     ", temperature_T1_out_hot_water, "\n"
      "temperature_T2_out_hot_water -     ", temperature_T2_out_hot_water)

print("pipe_hot_water_consumption_main -  ", module_hot_water.consumption_main, " t/h")
print("pipe_hot_water_consumption_out -   ", module_hot_water.consumption_out, " t/h")
print("velocity_main -                    ", velocity_main_enter)
print("velocity_out -                     ", velocity_out_hot_water)
print("pipe_dn_main -                     ", module_hot_water.pipe_dn(module_hot_water.consumption_main, velocity_main_enter))
print("pipe_dn_T3 -                      ", module_hot_water.pipe_dn(module_hot_water.consumption_out, velocity_out_hot_water))
print("pipe_dn_B1 -                      ", module_hot_water.pipe_dn(module_hot_water.consumption_out, velocity_out_hot_water))
print("pipe_dn_T1_2st -                  ", module_hot_water.pipe_dn(hot_water_cons_T1_2st, velocity_main_enter))
print("---")

print("dP_min -                           ", dp_min_hot_water)
print("Kv valve dP -                      ", calc.kv(module_hot_water.consumption_main, dp_min_hot_water))
print("valve_control_vent - Dn            ", valve_control_hot_water.km125f_DN[number_valve_hot_water],
    ", Kvs", valve_control_hot_water.km125f_Kvs[number_valve_hot_water], 
    ", dp ", calc.dp(hot_water_cons_T1_2st, valve_control_hot_water.km125f_Kvs[number_valve_hot_water])) 
print("---")


print("--------------------------------------------------------------------")