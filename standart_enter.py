from typical_solutions import *

enter_module = Enter_module()
for i in range (0, len(Dn)):
    enter_module.ID_element.append(i)
    enter_module.add_element(i, 
                            Dn[i], 
                            consumption(Dn[i], enter_module.flowspeed_min), 
                            consumption(Dn[i], enter_module.flowspeed_max),
                            power((consumption(Dn[i], enter_module.flowspeed_min)), enter_module.tempt1, enter_module.tempt2), 
                            power((consumption(Dn[i], enter_module.flowspeed_max)), enter_module.tempt1, enter_module.tempt2))


enter_module.to_csv()
