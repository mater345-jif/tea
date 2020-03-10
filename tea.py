import xlsxwriter
from datetime import datetime
from operator import itemgetter

expenses = []
test = ()

input_from = input('From: ')
input_from_time = input('Time: ')

input_end = input('End: ')
input_end_time = input('Time: ')
input_comment = input('Do you have a comment: ')

append_from = (input_from + ":" + input_from_time)
append_end = (input_end + ":" + input_end_time)
test = ([append_from, append_end, input_comment])

print(test)
#expenses["End"] = input_end
#expenses["Comment"] = input_comment

print(expenses)

"""
#Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Expenses05.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Add a number format for cells with money.
money_format = workbook.add_format({'num_format': '$#,##0'})

date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})

worksheet.set_column(1, 1, 15)


# Write some data headers.
worksheet.write('A1', 'Item', bold)
worksheet.write('B1', 'Cost', bold)

# Some data we want to write to the worksheet.
#expenses = (
#    ['Rent', '2013-01-13', 1000],
#    ['Gas',  '2013-01-14',  100],
#    ['Food', '2013-01-16',  300],
#    ['Gym',  '2013-01-20',   50],
#)


# Start from the first cell below the headers.
row = 1
col = 0

# Iterate over the data and write it out row by row.
start, end, comment = itemgetter('Start', 'End', 'Comment')(expenses)
print(start)
print(end)
print(comment)
for time_from time_end comment in expenses:
    start1 = datetime.strptime(start, "%Y-%m-%d")
    end2 = datetime.strptime(end, "%Y-%m-%d")
    worksheet.write_datetime(row, col, start1, date_format)
    worksheet.write_datetime(row, col + 1, end2, date_format)
    worksheet.write_string  (row, col + 2, comment)
    row += 1


# Write a total using a formula.
worksheet.write(row, 0, 'Elapsed time:',       bold)
worksheet.write(row, 2, '=B2-A2')

workbook.close()
"""