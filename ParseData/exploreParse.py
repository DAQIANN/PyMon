#from csv import reader
#from pprint import pprint
#result = []
#with open('data.txt') as in_file:
#    csv_reader = reader(in_file)
#    headers = [x.strip() for x in next(csv_reader)]
#
#    for line in csv_reader:
#        if line:
#            d = dict(zip(headers, map(str.strip, line)))
#            if d['Sect'] == '2-2':
#                result.append(d)
#
#pprint(result)

import pandas as pd
df = pd.read_csv('data.txt')
print(df)
