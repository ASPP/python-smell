import pandas as pd


CSV_COMMENT_PREFIXES = ['# ', '-- ', 'REM ']


def readfiles(filenames):
    """ Generator that yields all lines from multiple files. """
    for filename in filenames:
        for line in open(filename, 'rt'):
            yield line


def filter_comments(lines, comment_prefixes=CSV_COMMENT_PREFIXES):
    """ Generator that yields all lines that do not start with comment prefixes. """
    for line in lines:
        for prefix in comment_prefixes:
            if line.startswith(prefix):
                break
        else:
            yield line


def parse_data(lines):
    """ Generator that parses each line as a list of integers. """
    for line in lines:
        yield [int(x) for x in line.split(',')]

        
filenames = ['../first_commented_data.csv', '../second_commented_data.csv', '../third_commented_data.csv']
data = pd.DataFrame(
    parse_data(filter_comments(readfiles(filenames))),
    columns=['unci', 'dunci', 'trinci', 'quari'],
)
print(data.sum())
