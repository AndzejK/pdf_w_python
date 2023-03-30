import pandas # with this module  we can read excel file :)
from fpdf import FPDF

dataframe=pandas.read_excel("data.xlsx")

# Standard way of iterrating the data from a file like excel, etc.
for index,row in dataframe.iterrows():
    pdf = FPDF(orientation="portrait",unit="pt", format="A4") 
    pdf.add_page()

    # Adding title
    pdf.set_font(family="Times",style="B",size=24)
    pdf.cell(w=0,h=50,txt=row['name'], align="C",ln=1) # dynamic text

    # Adding content to the pdf files
    for column in dataframe.columns[1:]: # extracting the names of the columns 
        pdf.set_font(family="Times",style='B',size=14)
        pdf.cell(w=60,h=25,txt=f"{column.title()}:")

        pdf.set_font(family="Times",size=12)
        pdf.cell(w=60,h=25,txt=row[column],ln=1) # extracting data for the columns 

    # creates pdf files and in my case 3 of them
    pdf.output(f"{row['name']}.pdf") 

