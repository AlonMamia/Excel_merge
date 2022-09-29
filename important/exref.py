from UIBrowser import *
import sys
from funcEX import *
import os

# browse file ui
root = tk.Tk()
ui = FileSelect(root)
root.mainloop()

if not ui.flag:
    sys.exit()

df1 = ui.originalFileComp.df.copy()
df2 = ui.newFileComp.df.copy()

df2 = nameFormat(df2,
                 ["תז תושב", "מספר מזהה"], ["תאריך תחילת החוב", "ת.פרעוןנטו"], ["ערך חוב עדכני", "סכום במטבע מקומי"],
                 ["מספר חשבון", "חשבון"])

df1['הקצאה'] = df1['הקצאה'].apply(lambda x: FormatAloctaion(x).format(x))
df1 = minimizeRows(df1)

# zero all original debt column values
df1.loc[:, 'סכום במטבע מקומי'] = '0'

df2['הקצאה'] = df2['הקצאה'].apply(lambda x: FormatAloctaion(x).format(x))
df2 = debtSum(df2)

# insert into df2 all of the rows which are in df1 but not in df2 based on the allocation column
df2 = merger(df1, df2)
df2 = removeExeptions(df2)

df2 = df2.sort_values("מספר מזהה")
df2 = formatType(df2)

# remove columns and change order
df2 = df2[['מספר מזהה', "הקצאה", 'ת.פרעוןנטו', 'סכום במטבע מקומי', "חשבון"]]

df2['הקצאה'] = df2['הקצאה'].astype(int)
df2 = nameFormat(df2,
                 ["מספר מזהה", "תז תושב"], ["סכום במטבע מקומי", "ערך חוב עדכני"], ["חשבון", "מספר חשבון"],
                 ["ת.פרעוןנטו", "תאריך תחילת החוב"])

# create a new excel sheet and insert the result
path = os.path.join(os.path.expanduser("~"), "Desktop", "inc_total.xlsx")

writer = pd.ExcelWriter(path, engine='xlsxwriter', date_format='dd/mm/yyyy')
df2.to_excel(writer, sheet_name='גיליון1', index=False)

workbook = writer.book
worksheet = writer.sheets["גיליון1"]

workSheetFormat(df2, worksheet)

# set number format
number_format = workbook.add_format({'num_format': '0'})
worksheet.set_column(0, 4, 18)
worksheet.set_column(1, 1, 11, number_format)

# exit ui
root = tk.Tk()
ui = Process(root)
root.mainloop()

writer.save()
