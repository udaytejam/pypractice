import csv
with open('example.csv') as csvfile:
    readCsv = csv.reader(csvfile, delimiter=',')
    print(readCsv)
    columns1 = []
    columns2 = []
    for row in readCsv:
        column1 = row[3]
        column2 = row[0]
        print(row)
        print(row[5])

        columns1.append(column1)
        columns2.append(column2)

    print(columns1)
    print(columns2)
