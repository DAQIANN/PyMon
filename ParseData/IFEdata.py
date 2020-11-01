import csv

file_name = "testnew.csv"
data = []
name_value = ["Time", "ID", "Min", "Max", "Value"]
with open(file_name, "r") as f:
    line = f.readline()
    line = f.readline()
    while line:
        datum = {}
        temp = line.split(',')
        datum[name_value[0]] = temp[0]
        datum[name_value[1]] = temp[1]
        datum[name_value[2]] = temp[5]
        datum[name_value[3]] = temp[6]
        datum[name_value[4]] = temp[8]
        data.append(datum)
        line = f.readline()

print(data[10000]["Time"], data[10020])
