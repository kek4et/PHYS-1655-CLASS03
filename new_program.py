#----------------------------------------------------------------------------
#    PROGRAM NAME:  Hello.py
#    PURPOSE:       Simple python example
#    CREATED:       Craig Group  2024
#
#    Class02
#    UVA Honor Pledge
#   
#    To run me:  python Hello.py
#____________________________________________________________________________

#------------------------------------------------
#                  IMPORTS
#------------------------------------------------
#None



#------------------------------------------------
#               GLOBAL CONSTANTS
#------------------------------------------------
#None


#------------------------------------------------
#               METHODS
#------------------------------------------------
#None

#------------------------------------------------
#                   MAIN FUNCTION
#------------------------------------------------
def main():

    #To print something to the screen in Python.
    print("\n Hello Python Multiverse!\n\n")

    #Let's try to print something with some variables..  
    year=2024
    semester="Spring"
    
    #I can just add up strings into a single MONSTER string!
    mystr="This is " + " " + semester + " " + "semester" + " " + "of" + " " + str(year) + "!\n"
    #Note that I needed to conver integer, year, into a string with the str function!
    
    print(mystr)
    
    
#Call the main function
main()
