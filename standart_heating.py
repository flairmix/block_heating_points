from typical_solutions import *

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
        if Dn_hot_max == Dn_hot_min:
            number += 1
            heat_module.ID_element.append(number)

            consuption_min_hot_1 = consumption(Dn_hot_min, heat_module.flowspeed_min_hot)
            consuption_max_hot_1 = consumption(Dn_hot_min, heat_module.flowspeed_max_hot)
            
            Qmin_hot_1 = power(consuption_min_hot_1, heat_module.tempt1, heat_module.tempt2)   
            Qmax_hot_1 = power(consuption_max_hot_1, heat_module.tempt1, heat_module.tempt2)   

            # Qmin_cold_1  =  Qmin_hot_1
            # Qmax_cold_1 = Qmax_hot_1

            heat_module.add_element(number, 
                                Dn_cold, 
                                consuption_min_cold, 
                                consuption_max_cold, 
                                Qmin_cold, 
                                Qmax_cold,
                                Dn_hot_min,
                                Dn_hot_max,
                                consuption_min_hot_1, 
                                consuption_max_hot_1, 
                                Qmin_hot_1, 
                                Qmax_hot_1                       
                                )
            break      

        elif Dn_hot_min < Dn_hot_max :
            number += 1
            heat_module.ID_element.append(number)

            consuption_min_hot_recount = consumption(Dn_hot_min, heat_module.flowspeed_min_hot)
            consuption_max_hot_recount = consumption(Dn_hot_min, heat_module.flowspeed_max_hot)
            
            Qmin_hot_recount = power(consuption_min_hot_recount, heat_module.tempt1, heat_module.tempt2)  
            Qmax_hot_recount = power(consuption_max_hot_recount, heat_module.tempt1, heat_module.tempt2)  
            
            consuption_min_cold_recount = consumption(Dn_cold, heat_module.flowspeed_min_cold) 
            consuption_max_cold_recount = consumption(Dn_cold, heat_module.flowspeed_max_cold) 

            heat_module.add_element(number, 
                                Dn_cold, 
                                consuption_min_cold_recount, 
                                consuption_max_cold_recount, 
                                Qmin_cold, 
                                Qmax_cold,
                                Dn_hot_min,
                                Dn_hot_max,
                                consuption_min_hot_recount, 
                                consuption_max_hot_recount, 
                                Qmin_hot_recount, 
                                Qmax_hot_recount                       
                                )

            Dn_hot_min = DN_pipe[DN_pipe.index(Dn_hot_min) + 1]

        else:
            print("Dn_hot_min > Dn_hot_max")
            break
    

heat_module.print_me()

print(heat_module.ID_element)

heat_module.to_csv()