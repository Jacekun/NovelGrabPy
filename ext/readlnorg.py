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

def basePage():
    return page

def extInfo(stringVal):
    string = "Name: " + name + "\nVersion: " + version + "\nAuthor: " + author
    return stringVal + string

'''
    chapterLinks
    :param URL: Base URL of Webnovel
    :returns: List of URLs of Chapter links
'''
def chapterLinks(URL):

    # Get number of Tabs
    tab = input("Number of Tabs: ")
    x = []

    page = requests.get(URL)
    if page.status_code != 200:
        print("Unable to download page: " + URL)
        return x

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

'''
    getChapterInfo
    :param URL: Link of the chapter
    :returns: List
        -[0] Title
        -[1] Content 
'''
def getChapterInfo(URL):
    # Setup vars
    retList = []
    chBody = ""

    # Get Chapter Page, from the Net
    page = requests.get(URL)
    if page.status_code != 200:
        print("Unable to download page: " + URL)
        return retList

    # get the webpage Text
    soup = BeautifulSoup(page.text, 'lxml')

    # Get the Chapter Title, append to resultList
    retList.append(soup.title.text[5:])

    # Find the chapter body contents
    chapter_text = soup.find('div', id='growfoodsmart')
    if chapter_text is None:
        raise RuntimeError("Chapter has no contents")
    
    # Typecast result to string, including tags
    chBody = str(chapter_text)

    # Get string after >
    try:
        target = '>'
        chBody = chBody[chBody.index(target) + len(target):]
    except:
        chBody = chBody
    
    # Remove Last characters, the </div> tag
    try:
        chBody = chBody[:-6]
    except:
        chBody = chBody

    # Append to retList
    retList.append(chBody)

    # Return chapter body string
    return retList