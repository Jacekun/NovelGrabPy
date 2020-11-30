# imports
import os
import imp
import io

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
    # Open Log
    logFile = io.open("AppLog.log", "a", encoding="utf-8")

    # Get module
    modName = input("Enter module: ")

    module = imp.load_source( modName, os.path.join('ext', modName + ".py") )
    modInit = getattr( module, "extInfo" )
    modChapterLink = getattr( module, "chapterLinks" )
    modCont = getattr( module, "getChapterBody" )

    extInfo = modInit("Package Info:\n")
    print( extInfo )
    logFile.write( extInfo + '\n')

    # Get Webnovel Name, and create Directory
    wnName = input("Get output File Name: ")
    wnFile = wnName + ".txt"
    outputFile = io.open(wnFile, "a", encoding="utf-8")
    logFile.write( "OutputName: " + wnFile + '\n' )

    # Get webnovel url
    wnPage = input("Paste base URL here: ")
    logFile.write( "Base URL: " + wnPage + '\n' )

    # Get Chapter Links, from ext
    listCh = modChapterLink(wnPage)

    # Counters
    count = 0
    countMax = len(listCh)
    status = ""

    # Iterate through chapter links
    for ch in listCh:
        # Clear screen
        clear()

        # Working on...
        count += 1
        status = "Working on ", str(count), " out of ", str(countMax), ".... Percentage: ", str((count/countMax)*100), "%"
        print( status )
        logFile.write( status )

        # Get Body and write to File
        body = modCont(ch)
        if body is None:
            bodyString = "None"
            logFile.write( "Returns a NoneType" )
        else:
            bodyString = body
            logFile.write( "Has contents" )

        # Write to Output File
        try:
            outputFile.write("Source: " + ch + "\nBody:\n" + bodyString + "\n\n")
            logFile.write( "Written to output file!" )
        except:
            logFile.write( "Not written to output! Encountered an error!" )

        # Done
        status = str(count), " out of ", str(countMax), " done! Percentage: ", str((count/countMax)*100), "%"
        print( status )
        logFile.write( status )
    # End of For Loop

    # Close output file
    outputFile.close()
    print("Done!")

    # Close LogFile
    logFile.close()