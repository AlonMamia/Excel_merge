import pandas as pd

# Create a Pandas dataframe from some data.
df = pd.DataFrame({'Data': [u'نص عربي / English text'] * 6})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Get the xlsxwriter workbook and worksheet objects.
workbook = writer.book
worksheet = writer.sheets['Sheet1']

# Add the cell formats.
# format_right_to_left = workbook.add_format({'reading_order': 2})

# Change the direction for the worksheet.
worksheet.right_to_left()

# Make the column wider for visibility and add the reading order format.
# worksheet.set_column('B:B', 30, format_right_to_left)

# Close the Pandas Excel writer and output the Excel file.
writer.save()