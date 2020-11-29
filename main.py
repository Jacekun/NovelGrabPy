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
    modCont = getattr( module, "getContents" )

    print( modInit("Package Info:\n") )

    # Get Webnovel Name, and create Directory
    wnName = input("Get Folder Name: ")
    wnFile = wnName + ".txt"
    outputFile = open(wnFile, "a")

    # Get webnovel url
    wnPage = input("Paste base URL here: ")

    # Get Chapter Links, from ext
    listCh = modChapterLink(wnPage)
    temp = ""

    # Iterate through chapter links
    for ch in listCh:
        # Get Body and write to File
        bodyString = modCont(ch)
        outputFile.write("Source:" + ch + "\nBody:\n" + bodyString + "\n\n")

    # Close output file
    outputFile.close()
    print("Done!")