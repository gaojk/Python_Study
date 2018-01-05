# Author:Jing Lv
# 读取Excel

# 读2003 excel
import xlrd
# 读2007 excel
import openpyxl


def read03Excel(path):
    data = xlrd.open_workbook(path)
    sheets = data.sheet_names()
    sheet = data.sheet_by_name(sheets[0])
    for i in range(0, sheet.nrows):
        row = sheet.row(i)
        for j in range(0, sheet.ncols):
            print(sheet.cell_value(i, j), "\t", end="")
        print()


def read07Excel(path, sheetname):
    data = openpyxl.load_workbook(path)  # 打开excel文件
    print(data.get_sheet_names())  # 获取工作簿所有工作表名
    sheet = data.get_sheet_by_name(sheetname)  # 获取工作表
    print(sheet.title)

    for row in sheet.rows:
        for cell in row:
            print(cell.value, "\t", end="")
        print()


# path03 = '../dataFile/case1.xls'
# read03Excel(path03)
path07 = '../dataFile/api_case.xlsx'
read07Excel(path07)
