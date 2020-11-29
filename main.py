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

    print( modInit("Package Info:\n") )