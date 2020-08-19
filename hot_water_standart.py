import typical_solutions

hot_water_module = typical_solutions.Hot_water_module()
number = 0

for i in range(0, len(typical_solutions.DN_pipe)):


    w1_Dn = typical_solutions.DN_pipe[i]
    w1_consuption_min = hot_water_module.consumption(w1_Dn, hot_water_module.flowspeed_min_cold) 
    w1_consuption_max = hot_water_module.consumption(w1_Dn, hot_water_module.flowspeed_max_cold) 

    w1_Qmin = hot_water_module.power(w1_consuption_min, hot_water_module.temp_t3, hot_water_module.temp_w1)
    w1_Qmax = hot_water_module.power(w1_consuption_max, hot_water_module.temp_t3, hot_water_module.temp_w1) 

    t3_Dn_min = hot_water_module.pipeDn(w1_consuption_min * hot_water_module.circulation, hot_water_module.flowspeed_min_cold)
    t3_Dn_max = hot_water_module.pipeDn(w1_consuption_max * hot_water_module.circulation, hot_water_module.flowspeed_max_cold)

    t4_Dn_min = hot_water_module.pipeDn(w1_consuption_min * (hot_water_module.circulation - 1), hot_water_module.flowspeed_min_cold)
    t4_Dn_max = hot_water_module.pipeDn(w1_consuption_max * (hot_water_module.circulation - 1), hot_water_module.flowspeed_max_cold)


    for i in range(0, len(typical_solutions.DN_pipe)):
        t2_Dn = typical_solutions.DN_pipe[i]

        t2_consumption_min = hot_water_module.dn_to_consumption(t2_Dn, hot_water_module.flowspeed_min_hot)
        t2_consumption_max = hot_water_module.dn_to_consumption(t2_Dn, hot_water_module.flowspeed_max_hot)

        t2_Qmin_part1 = (t2_consumption_min * hot_water_module.t2_delta_t) / 1000
        t2_Qmax_part1 = (t2_consumption_max * hot_water_module.t2_delta_t) / 1000

        part1 = 100 * t2_Qmin_part1 / w1_Qmin
        part2 = 100 - part1

        Qmin_part2 = w1_Qmin - t2_Qmin_part1
        Qmax_part2 = w1_Qmax - t2_Qmax_part1

        for j in range(0, len(typical_solutions.DN_pipe)):
            t12_Dn = typical_solutions.DN_pipe[j]

            t12_consumption_min = hot_water_module.dn_to_consumption(t12_Dn, hot_water_module.flowspeed_min_hot)
            # t12_consumption_max = hot_water_module.dn_to_consumption(t12_Dn, hot_water_module.flowspeed_max_hot)

            t12_delta_min = 1000 * Qmin_part2 / t12_consumption_min
            # t12_delta_max = Qmin_part2 / t12_consumption_max

            if t12_delta_min > 5 and t12_delta_min < 30 and part1 >= 30 and part1 <= 70:
                number += 1
                hot_water_module.ID_element.append(number)
                hot_water_module.add_element(number, 
                                            w1_Dn, 
                                            w1_consuption_min,  
                                            w1_consuption_max,
                                            w1_Qmin, 
                                            w1_Qmax,
                                            t3_Dn_min, 
                                            t4_Dn_min, 
                                            t2_Dn,
                                            hot_water_module.t2_delta_t,
                                            t2_consumption_min,  
                                            t2_consumption_max,
                                            t2_Qmin_part1, 
                                            t2_Qmax_part1,
                                            Qmin_part2,
                                            Qmax_part2,
                                            t12_Dn, 
                                            t12_consumption_min, 
                                            int(t12_delta_min), 
                                            part1, 
                                            part2)
                break 
    number += 1
    hot_water_module.ID_element.append(number)


hot_water_module.print_me()
hot_water_module.to_csv()