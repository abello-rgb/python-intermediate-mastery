import csv



max_sales = 0
name_bestseller = None

with open('Bestseller - Sheet1.csv', 'r', encoding='utf8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        sales = row[4]
        book_name = row[0]
        sales = float(sales)
        if sales > max_sales:
            max_sales = sales
            name_bestseller = book_name
    print('BestSeller:', name_bestseller ,max_sales)    


with open('output.csv', 'w', newline= '') as file:

    csv_writer = csv.writer(file)
    csv_writer.writerow([name_bestseller, max_sales])

