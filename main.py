# imports
import os
import imp
import requests
from bs4 import BeautifulSoup

# define our clear function 
def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear')

# Main execution
class Main:

    # Get module
    modName = input("Enter module: ")

    module = imp.load_source( modName, os.path.join('ext', modName + ".py") )
    modInit = getattr( module, "extInfo" )

    print( modInit("Package Info:\n") )

    # Get webnovel url
    wnPage = input("Paste base URL here: ")
    page = requests.get(wnPage)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='chapters_1-0')

    chapters = results.find('ul', class_='chapter-chs')
    chaptersList = chapters.find_all('a', class_='')

    for ch in chaptersList:
        if ch.has_attr('href'):
            print(ch.text + " : " + ch['href'])

    print("Done!")