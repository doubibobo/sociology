from tools.read_csv import read_csv, write_csv
import numpy as np


def compute_env(temp_data):
    rows, cols = temp_data.shape
    pollutions = temp_data[:, 2:].astype(np.float32)
    pollutions_max = pollutions.max(axis=0)
    pollutions_min = pollutions.min(axis=0)
    x = (pollutions - pollutions_min) / (pollutions_max - pollutions_min) * 70 + 30
    g = x / x.sum(axis=0)
    h = (g * np.log(g)).sum(axis=0) * (1 / np.log(rows)) * (-1.0)
    f = 1 - h
    k = f / f.sum()
    env = ((g * 100) * (k * 100)).sum(axis=1)
    result = np.concatenate((temp_data[:, 0:2], env.reshape((rows, -1))), axis=1)
    write_csv(result)


if __name__ == '__main__':
    file_path = '../files/gcss2008.csv'
    cols_name = ['s41', 'province',
                 '废水排放', '二氧化硫排放总量', '碳氮化物排放总理', '烟粉尘排放总量', '一般工业废气悟生产量']
    data = read_csv(file_path, cols_name)
    compute_env(data)
    print(data.shape)
