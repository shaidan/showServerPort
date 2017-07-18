from tabulate import tabulate

list_header = []
list_data = []

file = open("./server_port.txt")

def trim_tail(inputString):
    return inputString.replace('\n', '')

for line in file:
    #set header
    if line.startswith('#'):
        line = trim_tail(line)
        list_header = line.split(' ')
    else:
        line = trim_tail(line)
        list_temp = line.split(' ')
        list_data.append(list_temp)


print tabulate(list_data, headers=list_header, tablefmt='orgtbl')