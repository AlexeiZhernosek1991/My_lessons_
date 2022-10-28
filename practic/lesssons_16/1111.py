import csv

with open('example.csv', encoding='UTF-8') as csv_file:
    exampleReader = csv.reader(csv_file)
    for row in exampleReader:
        string = 'Строка #' + str(exampleReader.line_num) + ' '
        for value in row:
            string += value + ' '
        print(string)
