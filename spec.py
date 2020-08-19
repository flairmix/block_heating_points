import pandas as pd

PATH_FOR_SAVE = 'G:\\2_work_engineer\\raschet_po'
 
class Data_sheet():
    def __init__(self):

        self.ID_element = [i for i in range(1, 10, 1)]

        self.df_sheet = pd.DataFrame(columns= ['Позиция'] 
                                        + ['Наименование и техническая характеристика'] 
                                        + ['Тип, марка, обозначение документа, опросного листа'] 
                                        + ['Код оборудования, изделия, материала'] 
                                        + ['Завод изготовитель'] 
                                        + ['Единица измерения'] 
                                        + ['Количество'] 
                                        + ['Масса единицы,кг']
                                        + ['Примечания'],
                                        index = self.ID_element)

    def print_sheet(self):
        print(self.df_sheet)

    def sheet_to_csv(self):
        self.df_sheet.to_csv(PATH_FOR_SAVE + '\\sheet' + '.csv', sep=';', encoding="ansi")
    
    def add_element(self, poz, name, type_equip, code, manuf, ed_izm, count, mass, note):
        
        # self.ID_element.append(1)
        i = 1

        self.df_sheet.loc[self.ID_element[i]] = [poz, name, type_equip, code, manuf, ed_izm, count, mass, note]



class Data_sheet_list():
    def __init__(self):

        self.ID_element = [i for i in range(1, 10, 1)]

        self.df_sheet_list = pd.DataFrame(columns= ['Поз.'] 
                                        + ['Наименование'] 
                                        + ['Тип'] 
                                        + ['Завод изготовитель'] 
                                        + ['Ед.изм.'] 
                                        + ['Кол-во'] 
                                        + ['Прим.'],
                                        index = self.ID_element)

    def print_sheet(self):
        print(self.df_sheet_list)

    def sheet_to_csv(self):
        self.df_sheet_list.to_csv(PATH_FOR_SAVE + '\\sheet' + '.csv', sep=';', encoding="ansi")
    
    def add_element(self, poz, name, type_equip, manuf, ed_izm, count, note):
        
        # self.ID_element.append(1)
        i = 1

        self.df_sheet_list.loc[self.ID_element[i]] = [poz, name, type_equip, manuf, ed_izm, count, note]




if __name__ == "__main__":

    sheet = Data_sheet()

    sheet.add_element('poz', 'name', 'type_equip', 'code', 'manuf', 'ed_izm', 'count', 'mass', 'note')

    sheet.print_sheet()

    # sheet.sheet_to_csv()