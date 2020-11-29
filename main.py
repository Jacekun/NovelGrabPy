# imports
import os
import imp

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
    modChapterLink = getattr( module, "chapterLinks" )

    print( modInit("Package Info:\n") )

    # Get webnovel url
    wnPage = input("Paste base URL here: ")

    # Get Chapter Links, from ext
    listCh = modChapterLink(wnPage)

    # Print
    for ch in listCh:
        print(ch)

    print("Done!")