import fitz
from bs4 import BeautifulSoup

def PDFToText(file_name):

    path = f"./inputs/{file_name}.pdf"

    doc = fitz.open(path)

    pagelimit = len(doc)
    # other setup
    pagelimit_converted = pagelimit - 1
    html_pages = ''
    x = 0
    # iterate over each page and get its html, store to "html_pages"
    for pages in doc:
        while x <= pagelimit_converted:
            page = doc[x]
            html_page = page.get_text("html", "html.parser")
            html_pages += str(html_page)  
            x = x + 1

    # stick the html into bs
    html = BeautifulSoup(html_pages, features = 'html.parser')

    # remove images
    for tag in html:
        for img in html('img'):
            img.decompose()
    
    # iterate over each p tag and add its text to var "p_text" to get the entire documents text
    ptag = html.find_all('p')
    p_text = ''
    for ptag in html:   
        p_text += ptag.text

    return(p_text)