import pipe
import module
import calc
import equipment 

heat_power = 0.1794
vent_power = 0.0673
hot_water_power = 0.1865

POWER = heat_power + vent_power + hot_water_power
temperature_T1_main = 95
temperature_T2_main = 70

velocity_enter = 0.7
velocity_out = 0.4


print("--------------------------------------------------------------------")



#enter system

dP_min = 1.5

module_enter = module.Enter_module("module_enter",
    POWER, 
    temperature_T1_main,
    temperature_T2_main,
    95, 
    70, 
    6.,3.)

valve_control_dP = equipment.Valve_control("valve_control_dP", module_enter.consumption_main, dP_min)


print("enter module")
print("Power (GCal/h) - ", POWER)
print("Power (kW) - ", calc.GCalh_to_kW(POWER))
print("pipe_enter_consumption_main - ", module_enter.consumption_main, " t/h")
print("velocity_main - ", velocity_enter)
print("pipe_dn_main - ", module_enter.pipe_dn(module_enter.consumption_main, velocity_enter))

print("dP_min - ", dP_min)
print("Kv valve dP - ", calc.kv(module_enter.consumption_main, dP_min))
print("valve_control_dp - Dn", valve_control_dP.km125f_DN[6],
    ", Kvs", valve_control_dP.km125f_Kvs[6], 
    ", dp ", calc.dp(module_enter.consumption_main, valve_control_dP.km125f_Kvs[6])) 


print("--------------------------------------------------------------------")





#heat

temperature_T1_out_heat = 85
temperature_T2_out_heat = 65
dp_min_heat = 0.5
static_pressure_heat = 0.8
valve_pressure_heat = 6

velocity_out_heat = 0.5

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
    valve_pressure_heat)

print("heat_power - ", heat_power)
print("temperature_T1_out_heat - ", temperature_T1_out_heat, "\n"
    "temperature_T2_out_heat -", temperature_T2_out_heat)

print("pipe_heat_consumption_main - ", module_heat.consumption_main, " t/h")
print("pipe_heat_consumption_out - ", module_heat.consumption_out, " t/h")
print("velocity_main - ", velocity_enter)
print("velocity_out - ", velocity_out_heat)
print("pipe_dn_main - ", module_heat.pipe_dn(module_heat.consumption_main, velocity_enter))
print("pipe_dn_out - ", module_heat.pipe_dn(module_heat.consumption_out, velocity_out_heat))

print("---")
valve_number_heat = 4                                                                            #todo 
print("dP_min - ", dp_min_heat)
print("Kv valve dP - ", calc.kv(module_heat.consumption_main, dp_min_heat))
print("valve_control_vent - Dn", valve_control_heat.km125f_DN[valve_number_heat],
    ", Kvs", valve_control_heat.km125f_Kvs[valve_number_heat], 
    ", dp ", calc.dp(module_heat.consumption_main, valve_control_heat.km125f_Kvs[valve_number_heat])) 
print("---")
print("refilling")
print("heat_refilling_consumption (t/h) - ", module_heat.heat_refilling_consumption)
print("heat_refilling_dn - ", module_heat.heat_refilling_dn)

valve_number_heat_refill = 0                                                                            #todo 
dp_min_heat_refill = 0.5                                                                                #todo                                                                         
print("dP_min_refill - ", dp_min_heat_refill)
print("Kv valve dP - ", calc.kv(module_heat.heat_refilling_consumption, dp_min_heat_refill))
print("valve_control_heat - Dn", valve_control_heat.km125f_DN[valve_number_heat_refill],
    ", Kvs", valve_control_heat.km125f_Kvs[valve_number_heat_refill], 
    ", dp ", calc.dp(module_heat.heat_refilling_consumption, valve_control_heat.km125f_Kvs[valve_number_heat_refill])) 
print("---")
print("exp_tank")
print("expansion_tank_heat_l - ", expansion_tank_heat.tank_volume)

print("---")
print("pumps_main")
print("pumps_cons + 0.15% (t/h) - ", module_heat.consumption_out * 1.15)
print("pumps_pressure(bar) - ", (2.25 + 5 + 3) / 10)
print("---")
print("pumps_refill")
print("pumps_cons(t/h) - ", module_heat.heat_refilling_consumption)
print("pumps_pressure(bar) - ", static_pressure_heat + 0.3)


print("--------------------------------------------------------------------")




#vent
temperature_T1_out_vent = 80
temperature_T2_out_vent = 60
dP_min_vent = 0.5
static_pressure_vent = 0.8
valve_pressure_vent = 6

velocity_out_vent = 0.5

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
    valve_pressure_vent)

print("vent")
print("power_vent (Gcalh) - ", vent_power)
print("pipe_vent_consumption_main - ", module_vent.consumption_main, " t/h")
print("pipe_vent_consumption_out - ", module_vent.consumption_out, " t/h")
print("velocity_main - ", velocity_enter)
print("velocity_out - ", velocity_out_vent)
print("pipe_dn_main - ", module_vent.pipe_dn(module_vent.consumption_main, velocity_enter))
print("pipe_dn_out - ", module_vent.pipe_dn(module_vent.consumption_out, velocity_out_vent))

print("---")
valve_number_vent = 1                                                                            #todo 
print("dP_min - ", dP_min_vent)
print("Kv valve dP - ", calc.kv(module_vent.consumption_main, dP_min_vent))
print("valve_control_vent - Dn", valve_control_vent.km125f_DN[valve_number_vent],
    ", Kvs", valve_control_vent.km125f_Kvs[valve_number_vent], 
    ", dp ", calc.dp(module_vent.consumption_main, valve_control_vent.km125f_Kvs[valve_number_vent])) 
print("---")
print("refilling")
print("vent_refilling_consumption (t/h) - ", module_vent.vent_refilling_consumption)
print("vent_refilling_dn - ", module_vent.vent_refilling_dn)

print("heat + vent_refilling_consumption (t/h) - ", module_vent.vent_refilling_consumption + module_heat.heat_refilling_consumption)
print("heat + vent_refilling_dn - ", calc.pipeDn(module_vent.vent_refilling_consumption + module_heat.heat_refilling_consumption, 0.7))
print("---")
valve_number_vent_refill = 0                                                                            #todo 
dp_min_vent_refill = 0.5                                                                                #todo                                                                         
print("dP_min_refill - ", dp_min_vent_refill)
print("Kv valve dP - ", calc.kv(module_vent.vent_refilling_consumption, dp_min_vent_refill))
print("valve_control_vent - Dn", valve_control_vent.km125f_DN[valve_number_vent_refill],
    ", Kvs", valve_control_vent.km125f_Kvs[valve_number_vent_refill], 
    ", dp ", calc.dp(module_vent.vent_refilling_consumption, valve_control_vent.km125f_Kvs[valve_number_vent_refill])) 

print("---")
print("exp_tank")
print("expansion_tank_vent_l - ", expansion_tank_vent.tank_volume)

print("---")
print("pumps_main")
print("pumps_cons + 0.15% (t/h) - ", module_vent.consumption_out * 1.15)
print("pumps_pressure(bar) - ", (0.5 + 5 + 3) / 10)
print("---")
print("pumps_refill")
print("pumps_cons(t/h) - ", module_vent.vent_refilling_consumption)
print("pumps_pressure(bar) - ", static_pressure_heat + 0.3)
print("--------------------------------------------------------------------")




#hot water
temperature_V1_main = 5
temperature_T3 = 65

consumption_cold_water_max = 3.11 #t/h
circulation = 1.5

module_hotwater = module.Hotwater_module("module_hotwater", 
    hot_water_power,
    temperature_T1_main,
    temperature_T2_main,
    temperature_T3,
    temperature_V1_main)

valve_control_hotwater2st = equipment.Valve_control("valve_control_hotwater2st", 
    5,                                                                                  #!!!!!!!!!
    0.5)

valve_hotwater2st_dp = equipment.Valve_control("valve_control_hotwater_dp", 
    module_heat.consumption_main,                                                        #!!!!!!!!!
    1)

print("hotwater")
print("power_hotwater (Gcalh) - ", hot_water_power)
print("velocity_main - ", velocity_enter)
print("velocity_out - ", velocity_out)
print("consumption cold water - ", consumption_cold_water_max)
print("pipe_dn_V1 - ", module_hotwater.pipe_dn(consumption_cold_water_max, velocity_enter))

print("consumption T3 - ", consumption_cold_water_max * circulation)
print("pipe_dn_T3 - ", module_hotwater.pipe_dn(consumption_cold_water_max * circulation, velocity_out))

print("consumption T4 - ", (consumption_cold_water_max * (circulation - 1)))
print("pipe_dn_T4 - ", module_vent.pipe_dn(consumption_cold_water_max * (circulation - 1), velocity_out))

print("---")

print("pipe_dn_1ст - ", module_hotwater.pipe_dn((12.2), velocity_enter))
print("pipe_dn_2ст - ", module_hotwater.pipe_dn(5, velocity_enter))

print("---")
print("pumps_t4")
print("pumps_cons (t/h) - ", (consumption_cold_water_max * (circulation - 1)))
print("pumps_pressure(bar) - ??" )

print("---")
valve_number_hotwater2st = 3                                                                            #todo 
print("valve_control_hotwater2st")
print("dP_min - ", 0.5)
print("Kv valve dP - ", calc.kv(5, 0.5))
print("valve_control_vent - Dn", valve_control_hotwater2st.km125f_DN[valve_number_hotwater2st],
    ", Kvs", valve_control_vent.km125f_Kvs[valve_number_hotwater2st], 
    ", dp ", calc.dp(5, valve_control_hotwater2st.km125f_Kvs[valve_number_hotwater2st])) 

print("---")
valve_number_horwater_dp = 5                                                                            #todo 
print("valve_horwater_dp ")
print("dP_min - ", 1)
print("Kv valve dP - ", calc.kv(module_heat.consumption_main, 1))
print("valve_control_vent - Dn", valve_hotwater2st_dp.kat33_DN[valve_number_horwater_dp],
    ", Kvs", valve_hotwater2st_dp.kat33_Kvs[valve_number_horwater_dp], 
    ", dp ", calc.dp(module_heat.consumption_main, valve_hotwater2st_dp.kat33_Kvs[valve_number_horwater_dp])) 


print("--------------------------------------------------------------------")
