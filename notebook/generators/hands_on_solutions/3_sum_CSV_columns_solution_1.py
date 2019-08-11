import pandas as pd


CSV_COMMENT_PREFIXES = ['# ', '-- ', 'REM ']


def lines_without_comments(filename, comment_prefixes=CSV_COMMENT_PREFIXES):
    with open(filename, 'rt') as f:
        valid_lines = []
        for line in f:
            for prefix in comment_prefixes:
                if line.startswith(prefix):
                    break
            else:
                data = [int(x) for x in line.split(',')]
                yield data


filenames = ['../first_commented_data.csv', '../second_commented_data.csv', '../third_commented_data.csv']
data = []
for filename in filenames:
    print('Load data from', filename)
    data_chunk = pd.DataFrame(
        lines_without_comments(filename),
        columns=['unci', 'dunci', 'trinci', 'quari'],
    )
    data.append(data_chunk)

data = pd.concat(data)
print(data.sum())
