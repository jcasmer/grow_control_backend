import pandas

from django.conf import settings

class Utilites():

    def get_oms_data(gender, char_type, data_lenght):
        '''
        fucntion set the data to oms chart
        '''
        file_name = None
        if gender == 'Femenino':
            file_path = settings.FILE_GIRL_ROOT
        elif gender == 'Masculino':
            file_path = settings.FILE_BOY_ROOT

        sheet = 0
        # 1 == weight
        if char_type == 1:
            sheet = 0
        # 1 == weight
        elif char_type == 2:
            sheet = 1

        full_data = {}
        label = []
        data = []
        try:
            file_to_read = pandas.read_excel(open(file_path, 'rb'), sheet_name=sheet)
        except:
            pass
        for i in range(0, data_lenght):
            label.append(file_to_read['Day'][i])
            data.append(file_to_read['SD0'][i])
        full_data = {
            'label': label,
            'data': data
        }

        return full_data

        

    def get_height(self, gender, max_lenght):
        '''
        fucntion to calcule the child's height 
        '''
        pass

    def get_imc(self, gender, max_lenght):
        '''
        fucntion to calcule the child's imc 
        '''
        pass