# imports
import requests
from bs4 import BeautifulSoup
import re
import html

# global vars
page = "https://www.readlightnovel.org/"
name = "ReadLightNovel"
version = "1.0.0"
author = "Jace"

def extInfo(stringVal):
    string = "Name: " + name + "\nVersion: " + version + "\nAuthor: " + author
    return stringVal + string

def chapterLinks(URL):

    # Get number of Tabs
    tab = input("Number of Tabs: ")
    x = []

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    for i in range(0, int(tab)):

        results = soup.find(id='chapters_1-'+str(i))
        chapters = results.find('ul', class_='chapter-chs')
        chaptersList = chapters.find_all('a', class_='')

        # Get the exact links, inside href
        for ch in chaptersList:
            if ch.has_attr('href'):
                x.append(ch['href'])

    return x

def getContents(URL):
    # Setup vars
    retVal = ""

    # Get body
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find("div", {"id": "growfoodsmart"})

    if None in results:
        return ""

    retVal = str(results)

    #bodyP = results.find_all('p', class_='')
    #for p in bodyP:
        #retVal += p.text + "\n"

    # Replace <br /><br />
    #for elem in results.find_all(["a", "p", "div", "h3", "br"]):
        #elem = elem.replace_with(elem.text + "\n\n")
    
    # Get the Text, without other Tags
    # retVal = results.content
        
    # 
    try:
        # Get string after >
        target = '>'
        retVal = retVal[retVal.index(target) + len(target):]
    except:
        retVal = retVal
    
    try:
        # Relace breaks
        retVal = retVal.replace('<br>', '\n')
    except:
        retVal = retVal
    
    try:
        # Relace P tag
        retVal = retVal.replace('<p>', '\n')
    except:
        retVal = retVal

    try:
        # Relace breaks
        retVal = retVal.replace('</p>', '')
    except:
        retVal = retVal
    
    try:
        # Encode to UTF-8
        retVal = str(retVal.encode(encoding='utf-8'))
    except:
        retVal = retVal
    
    print(retVal)

    return retVal 