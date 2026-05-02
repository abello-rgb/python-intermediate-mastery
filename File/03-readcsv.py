import csv

data_to_write = [
    ['Name','Age','Grade'],
    ['Ana', '14', 'A'],
    ['Luis', '15', 'B'],
    ['María', '13', 'A'],
    ['Diego', '14', 'C'],
    ['Sofía', '15', 'B'],
]


with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(data_to_write)

    