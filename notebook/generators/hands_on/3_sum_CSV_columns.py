# Script that computes the sum of all the columns in 3 CSV files that contain commented lines
import pandas as pd

comment_prefixes = ['# ', '-- ', 'REM ']

filename1 = '../first_commented_data.csv'
print('Load data from', filename1)
with open(filename1, 'rt') as f:
    valid_lines = []
    for line in f:
        for prefix in comment_prefixes:
            if line.startswith(prefix):
                break
        else:
            data = [int(x) for x in line.split(',')]
            valid_lines.append(data)

data1 = pd.DataFrame(valid_lines, columns=['unci', 'dunci', 'trinci', 'quari'])


filename2 = '../second_commented_data.csv'
print('Load data from', filename2)
with open(filename2, 'rt') as f:
    valid_lines = []
    for line in f:
        for prefix in comment_prefixes:
            if line.startswith(prefix):
                break
        else:
            data = [int(x) for x in line.split(',')]
            valid_lines.append(data)

data2 = pd.DataFrame(valid_lines, columns=['unci', 'dunci', 'trinci', 'quari'])


filename3 = '../third_commented_data.csv'
print('Load data from', filename3)
with open(filename3, 'rt') as f:
    valid_lines = []
    for line in f:
        for prefix in comment_prefixes:
            if line.startswith(prefix):
                break
        else:
            data = [int(x) for x in line.split(',')]
            valid_lines.append(data)

data3 = pd.DataFrame(valid_lines, columns=['unci', 'dunci', 'trinci', 'quari'])

print(data1.sum() + data2.sum() + data3.sum())
