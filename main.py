"""
hierarchy: 
    object
        module
            enter_module
            heat_module
            vent_module
            hot_water_module
            YYTE
        pipe
        equipment
            valve      
            pump        
            exchanger  

"""


import module
import pipe
import valve



heat_module_1 = module.Heat_module("heat_module_1", 1000, 130, 70, 95, 70)
pipe_heat_T12 = pipe.Pipe("pipe_heat_T12 ")


print(heat_module_1.consumption_main)
print(heat_module_1.consumption_out)

print(pipe_heat_T12.pipe_dn(40))



