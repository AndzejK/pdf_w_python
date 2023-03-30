from fpdf import FPDF

# at this stage we have an open/blank pdf page
pdf = FPDF(orientation="portrait",unit="pt", format="A4") 
pdf.add_page()

# Adding an img
pdf.image("macbook_uv1b4RPlv7tei9TOd5De_1.jpg", w=51,h=51 ) # the original size of this pic is 512 × 512 pixels thus I'll make 10x smaller

# adding a txt
pdf.set_font(family="Times",style="B",size=24)
# technically txt or all objects are placed in a "cell"
pdf.cell(w=0,h=50,txt="Python Documentation", align="C",border=0,ln=1) #ln breaks the line, the 2nd cell/line will be below it

# adding another cell
pdf.set_font(family="Times",style="B",size=14)
pdf.cell(w=0,h=15,txt="Useful description",ln=2)

# adding another cell
pdf.set_font(family="Times",size=12)
txt_for_descr_1="""
The stats() method is a built-in function in Python's NumPy library that can be used to calculate several statistical properties of an array. Here are some of the most useful properties that the stats() method can calculate:
"""
pdf.multi_cell(w=0,h=15,txt=txt_for_descr_1) #multi_cell breaks for us lines and all text is fit in on the pdf page


# save pdf in this the location the same as the script
pdf.output("outcome_v4.pdf") 

