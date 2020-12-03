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

'''
    basePage()
    :returns: Base URL
'''
def basePage():
    return page

'''
    extInfo()
    :returns: Extension info
'''
def extInfo(stringVal):
    string = "Name: " + name + "\nVersion: " + version + "\nAuthor: " + author
    return stringVal + string

'''
    novelDetails(URL)
    :param URL: Base Link of the webnovel
    :returns: List of strings
        [0] Alt. Names
        [1] Author
        [2] Artist
        [3] Desc
        [4] Year
        [5] Genre
'''
def novelDetails(URL):
    retList = [ '', '', '', '', '', '' ]

    # Download webpage
    page = requests.get(URL)
    if page.status_code != 200:
        print("Unable to download page: " + URL)
        return retList
    # Save webpage to var
    soup = BeautifulSoup(page.text, 'lxml')

    # Check if not Null
    if soup is None:
        return retList
    else:
        for nd in soup.find_all('div', class_='novel-details'):
            # Check if None
            if nd is None:
                continue
            else:
                for item in nd.find_all('div', class_='novel-detail-item'):
                    # Check if None
                    if item is None:
                        continue
                    else:
                        header = item.find('div', class_='novel-detail-header')
                        if header is not None:
                            # Get detail Body (Main contents)
                            body = item.find('div', class_='novel-detail-body')
                            if body is not None:
                            # Switch header
                                if "Alternative Names" in header.text:
                                    retList[0] = body.text
                                elif "Author" in header.text:
                                    retList[1] = body.text
                                elif "Artist" in header.text:
                                    retList[2] = body.text
                                elif "Description" in header.text:
                                    retList[3] = body.text
                                elif "Year" in header.text:
                                    retList[4] = body.text
                                elif "Genre" in header.text:
                                    retList[5] = body.text
                                else:
                                    continue
                        else:
                            continue
                # End of Inner 'For loop'
        # End of Outer 'For Loop'      
    # Return List
    return retList

'''
    chapterLinks()
    :param URL: Base URL of Webnovel
    :returns: List of URLs of Chapter links
'''
def chapterLinks(URL):
    # Get number of Volumes
    vol = input("Number of Volumes: ")
    
    # Get number of Tabs
    tab = input("Number of Tabs: ")
    x = []

    # Download webpage
    page = requests.get(URL)
    if page.status_code != 200:
        print("Unable to download page: " + URL)
        return x

    soup = BeautifulSoup(page.content, 'html.parser')

    # For every volume
    for volCount in range(1, int(vol))
        # For every tab inside a volume
        for tabCount in range(0, int(tab)):

            results = soup.find(id='chapters_'+str(volCount)+'-'+str(tabCount))
            chapters = results.find('ul', class_='chapter-chs')
            chaptersList = chapters.find_all('a', class_='')

            # Get the exact links, inside href
            for ch in chaptersList:
                if ch.has_attr('href'):
                    x.append(ch['href'])
    # Return list of URLs
    return x

'''
    getChapterInfo()
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
        # raise RuntimeError("Chapter has no contents")
        retList.append( "" )
        return retList
    
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