import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

with open(filename, 'rt') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    headers = next(reader)
    column = {}
    for h in headers:
        column[h] = []
    for row in reader:
        for h, v in zip(headers, row):
            column[h].append(v)

objects = {}
for idx, objectID in enumerate(column['id']):
        if objectID not in objects.keys():
            objects[objectID] = []
            for key, attributeValue in column.items():
                objects[objectID].append(attributeValue[idx])
        elif objectID in objects.keys():
            objects[objectID].append(column['s_full_link'][idx])

maxLength = 0
for key, value in objects.items():
    if len(value) > maxLength:
        maxLength = len(value)

for key, value in objects.items():
    diff = maxLength - len(value)
    for i in range(diff):
        value.append('NONE')

diff = maxLength - len(headers)
for i in range(diff):
    headers.append("{}_{}".format("s_full_link", i+1))

with open('output.csv', mode='w') as output_file:
    writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(headers)
    for objectID, attributes in objects.items():
        writer.writerow(attributes)