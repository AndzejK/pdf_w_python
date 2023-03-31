import tabula
import pandas
table=tabula.read_pdf("weather.pdf",pages=1) #pages where is hour table!

type(table) # <class 'list'>
type(table[0]) # <class 'pandas.core.frame.DataFrame'>
# export data/table from pdf to csv
table[0].to_csv("from_pdf_to_csv.csv",index=None)
print(table)
