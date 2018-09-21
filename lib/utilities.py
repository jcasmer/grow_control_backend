import pandas

from django.conf import settings

from api.models import TypeDiagnostic

class Utilites():

    def get_oms_data(gender, char_type, data_lenght):
        '''
        function set the data to oms chart
        '''
        file_name = None
        if gender == 'Femenino':
            file_path = settings.FILE_GIRL_ROOT
        elif gender == 'Masculino':
            file_path = settings.FILE_BOY_ROOT

        sheet = 0
        # 1 == weight
        if int(char_type) == 1 or int(char_type) == 3:
            sheet = 0
        # 1 == height
        elif int(char_type) == 2:
            sheet = 1

        full_data = {}
        label = []
        data = []
        try:
            file_to_read = pandas.read_excel(open(file_path, 'rb'), sheet_name=sheet)
        except:
            pass
        j = 0
        for i in range(0, data_lenght + 2, 2):
            if file_to_read['Day'][i] <= data_lenght:
                data.append({'y': file_to_read['SD0'][i], 'x':file_to_read['Day'][i] })
            elif file_to_read['Day'][i] > data_lenght:
                data.append({'y': file_to_read['SD0'][i], 'x':file_to_read['Day'][i] })
                break

        full_data = {
            # 'label': label,
            'data': data
        }
        return full_data
        

    def get_child_status(gender, char_type, child_detail, week):
        '''
        function calculate child's status
        '''
        file_name = None
        if gender == 'Femenino':
            file_path = settings.FILE_GIRL_ROOT
        elif gender == 'Masculino':
            file_path = settings.FILE_BOY_ROOT

        sheet = 0
        # 1 == weight; 3 == IMC
        if int(char_type) == 1 or int(char_type) == 3:
            sheet = 0
        # 1 == height
        elif int(char_type) == 2:
            sheet = 1   

        try:
            file_to_read = pandas.read_excel(open(file_path, 'rb'), sheet_name=sheet)
        except:
            pass
        
        line_week = None
        for i in range(0, len(file_to_read['Day']) - 1):
            if file_to_read['Day'][i + 1]:
                if file_to_read['Day'][i] <= week and file_to_read['Day'][i + 1] > week:
                    line_week = i + 1
                elif file_to_read['Day'][i] <= week and file_to_read['Day'][i + 1] < week:
                    line_week = i + 1
            else:
                if file_to_read['Day'][i] <= week and file_to_read['Day'][i] > week:
                    line_week = i
                elif file_to_read['Day'][i] <= week and file_to_read['Day'][i] < week:
                    line_week = i
        status = ''
        try:
            if int(char_type) == 1 or int(char_type) == 3:
                if child_detail.weight <= file_to_read['SD4neg'][line_week]:
                    status = 'Bajo Peso Severo'
                elif file_to_read['SD4neg'][line_week] <= child_detail.weight and file_to_read['SD3neg'][line_week] >= child_detail.weight :
                    status = 'Bajo Peso'
                elif file_to_read['SD3neg'][line_week] <=  child_detail.weight and file_to_read['SD2neg'][line_week] >= child_detail.weight :
                    status = 'Bajo Peso'
                elif file_to_read['SD2neg'][line_week] <=  child_detail.weight and file_to_read['SD1neg'][line_week] >= child_detail.weight :
                    status = 'Peso Promedio'
                elif file_to_read['SD1neg'][line_week] <=  child_detail.weight and file_to_read['SD0'][line_week] >= child_detail.weight :
                    status = 'Peso Promedio'
                elif file_to_read['SD0'][line_week] <= child_detail.weight and file_to_read['SD1'][line_week] >= child_detail.weight :
                    status = 'Peso Promedio'
                elif file_to_read['SD1'][line_week] <= child_detail.weight and file_to_read['SD2'][line_week] >= child_detail.weight :
                    status = 'Posible Riesgo de Sobre Peso'
                elif file_to_read['SD2'][line_week] <= child_detail.weight and file_to_read['SD3'][line_week] >= child_detail.weight :
                    status = 'Sobre Peso'
                elif file_to_read['SD3'][line_week] <= child_detail.weight and file_to_read['SD4'][line_week] >= child_detail.weight :
                    status = 'Sobre Peso'
                elif file_to_read['SD4'][line_week] < child_detail.weight :
                    status = 'Sobre Peso'
            elif int(char_type) == 2:
                if child_detail.height <= file_to_read['SD3neg'][line_week]:
                    status = 'Baja Talla Severa'
                elif file_to_read['SD3neg'][line_week] <=  child_detail.height and file_to_read['SD2neg'][line_week] >= child_detail.height :
                    status = 'Baja Talla'
                elif file_to_read['SD2neg'][line_week] <=  child_detail.height and file_to_read['SD1neg'][line_week] >= child_detail.height :
                    status = 'Talla Promedio'
                elif file_to_read['SD1neg'][line_week] <=  child_detail.height and file_to_read['SD0'][line_week] >= child_detail.height :
                    status = 'Talla Promedio'
                elif file_to_read['SD0'][line_week] <= child_detail.height and file_to_read['SD1'][line_week] >= child_detail.height :
                    status = 'Talla Promedio'
                elif file_to_read['SD1'][line_week] <= child_detail.height and file_to_read['SD2'][line_week] >= child_detail.height :
                    status = 'Talla Por Encima Del Promedio'
                elif file_to_read['SD2'][line_week] <= child_detail.height and file_to_read['SD3'][line_week] >= child_detail.height :
                    status = 'Talla Por Encima Del Promedio '
                elif file_to_read['SD3'][line_week] < child_detail.height :
                    status = 'Super Talla'
        except Exception as e:
            pass
        return status