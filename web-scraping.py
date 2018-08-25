from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
def principal():
    busca=input("Sua busca: ")
    busca=entrada(busca)
    my_url='https://pt.stackoverflow.com/questions/tagged/'+busca
    #opening connection, grabbig the page
    uClient=uReq(my_url)
    #offloads the content into a variable
    page_html = uClient.read()
    #close the content
    uClient.close()
    #htm parser
    page_soup = soup(page_html, 'html.parser')
    #grab each post from the page
    posts = page_soup.findAll("div",{"class":"summary"})

    for i in range(len(posts)):
        title=posts[i].find("a")
        desc = posts[i].find("div",{"class":"excerpt"})
        print(f"------{i}-------")
        print(filtro(title))
        print(filtro(desc))
#filtro de tagas html
def filtro(title):
    title=str(title)
    titulo=[]
    for i in range(len(title)):
        if title[i]==chr(62):
            j=i
            for i in range(j+1,len(title)-1):
                if title[i]==chr(60):
                    break
                else:
                    titulo.append(title[i])
    titulo=''.join(titulo)
    return titulo
#tratamento da entrada para busca
def entrada(n):
    n=n.split()
    n='+'.join(n)
    return n
principal()
