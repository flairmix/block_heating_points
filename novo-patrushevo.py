import pipe
import module

pipe_heat = pipe.Pipe("pipe_heat")
pipe_hot_water = pipe.Pipe("pipe_hot_water")
pipe_vent = pipe.Pipe("pipe_vent")
pipe_hot_floor = pipe.Pipe("pipe_hot_floor")

#enter system
module_enter = module.Enter_module("module_enter", 2.141, 130, 70, 130, 70, 6., 5.)


#heat
module_heat = module.Heat_module("module_heat", 0.161, 130, 70, 95, 70)

print("pipe_heat_consuption_main - ", module_heat.consumption_main)


#vent
module_vent = module.Vent_module("module_vent", 0.594, 130, 70, 95, 70) 

print("pipe_vent_consuption_main - ", module_vent.consumption_main)


#hot water
pipe_hot_water_consuption_main = pipe_hot_water.pipe_consuption(0.182, 130, 70)
pipe_hot_water_consuption_main_max = pipe_hot_water.pipe_consuption(0.182, 70, 43)

print("pipe_hot_water_consuption_main - ", pipe_hot_water_consuption_main)
print("pipe_hot_water_consuption_main_max - ", pipe_hot_water_consuption_main_max)
print("\n")

print()

