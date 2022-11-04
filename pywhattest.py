from time import sleep
import pandas
import pywhatkit as pw

excel_data = pandas.read_excel('Recipients data.xls', sheet_name='Recipients')

count = 0
for columns in excel_data['Contact'].to_list():
    pw.sendwhatmsg_instantly(
        '+62' + str(excel_data['Contact'][count]),  excel_data['Message'][0], 10, tab_close=True)
    count += 1