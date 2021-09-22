from tools import read_csv, write_csv
import numpy as np
import re

data = read_csv('files/file_2.csv', cols_name=None)
print(data)

new_data = []

for item in data:
    new_data_item = []
    data_string = item[0]
    data_string = re.sub(' +', ' ', data_string)
    data_string_firsts = data_string.split('| ')
    new_data_item.extend([data_string_firsts[0]])
    if len(data_string_firsts) >= 2:
        data_string_seconds = data_string_firsts[1]
        data_string_seconds_list = data_string_seconds.split(' ')
        if len(data_string_seconds_list) >= 2:
            coef = data_string_seconds_list[0]
            std = data_string_seconds_list[1]
            if coef != 'Coef.' and std != 'Std.':
                coef = round(float(coef), 3)
                std = round(float(std), 3)
                p = data_string_seconds_list[1]
                if float(p) <= 0.01:
                    string_p = '***'
                elif 0.01 < float(p) <= 0.05:
                    string_p = '**'
                elif 0.05 < float(p) <= 0.1:
                    string_p = '*'
                else:
                    string_p = ''
                new_data_item.extend(['{0}{2}\n({1})'.format(coef, std, string_p)])
            else:
                new_data_item.extend(['{0}\n{1}'.format(data_string_seconds_list[0], data_string_seconds_list[1])])
        else:
            new_data_item.extend(data_string_seconds_list)
    else:
        new_data_item.extend([' '])
    new_data.append(new_data_item)
print(new_data)
new_data = np.array(new_data)
print(new_data)
write_csv(new_data, file_path='files/result_2.csv')
