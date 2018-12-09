# from__future__import division
# import numpy as np
import pandas as pd
# mport matplotlib.pyplot as plt
# from numpy.randomimport randn
# from pandasimport Series, DataFrame
# from datetimeimport datetime
import xlrd, openpyxl

xlsx_file = pd.ExcelFile('test.xlsx')
# print(xlsx_file)
All = xlsx_file.parse('Sheet1')
print(All)

