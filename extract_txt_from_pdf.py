import fitz
with fitz.open("Introduction_Python_3.11.2_documentation.pdf") as pdf_page:
    #get 1st pdf page 
    page1=pdf_page[0].get_text()
    # find the total number of all pdf pages
    total_pages=len(pdf_page)
    for cur_page in range(total_pages):
        print("#page:",cur_page+1)
         # add page number before displaying text
        print(pdf_page[cur_page].get_text())