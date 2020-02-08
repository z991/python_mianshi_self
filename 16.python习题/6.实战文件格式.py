import csv
import xlsxwriter

def read_file(file_path):
    file = open(file_path)
    file_read = csv.reader(file)
    file_data = list(file_read)
    return file_data

def write_titel(name):
    file_name = name+'.xlsx'
    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, 'open')
    worksheet.write(0, 1, 'high')
    worksheet.write(0, 2, 'low')
    worksheet.write(0, 3, 'close')
    worksheet.write(0, 4, 'amount')
    return worksheet, workbook

def write_body(file_path, name):
    file_data = read_file(file_path)
    worksheet, workbook = write_titel(name)
    n = 1
    for fi in file_data[1:]:
        if float(fi[-1]) > 1000000:
            worksheet.write(n, 0, fi[3])
            worksheet.write(n, 1, fi[4])
            worksheet.write(n, 2, fi[5])
            worksheet.write(n, 3, fi[6])
            worksheet.write(n, 4, fi[-1])
            n += 1
    workbook.close()

if __name__ == '__main__':
    write_body('000001.csv', 'def_amount')