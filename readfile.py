# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import sys

def printMembers(fileName):
    #Change the document into something printable by reading it line by line
    y = fileName.readlines()

    #This variable can help us figure out when to stop trying to print
    keepPrinting = False

    #loop through the entire document line by line
    for x in y:
        
        #Split the line into seperate string to make it easier to compare
        h = x.split()
        
        #If the only character in the line is a newline character skip it
        #Otherwise the program will throw an error when it tries to compare it
        if (len(x) == 1 and not(keepPrinting)):
            #Using continue will skip past the liens that would cause errors,
            #While allowing the loop to continue to run
            continue
        elif (keepPrinting and len(x) == 1):# and x != "~"):
            print("|" + " "*104 + "|")
            continue
        #If keepPrinting is true but the current line is empty set keep printing to false
        #This will give us a stop point for printing when we find an empty line
        elif (keepPrinting and (h[0] == "~")):
            print("=" * 106)
            print()
            keepPrinting = False
            continue

        #This if statement will check the first string in a line of text
        #This is me testing to see if I can find a specific word and start printing the fiel at that word
        #I edit the text file so that each round of research starts with Round-# so I fan find al of them easily 
        #without writting extra lines of code
        if(h[0]=="Our-Members:"):
            print("=" * 106)
            keepPrinting = True
        
        
        #this if will only print out the read line when I am ready to print
        if(keepPrinting):
            #print(x)
            #Trying to make the output look pretty by putting it in a box
            x = x.strip()
            print(f'|{x:<104}|')

#This function will print both the graphs and the narrative at the same time
def printNarrativeAndGrpahs(fileName):
    #Change the document into something printable by reading it line by line
    y = fileName.readlines()
    
    #Keep track of the order our graphs need to be printed in
    
    graphNum = 0
    
    #This variable can help us figure out when to stop trying to print
    keepPrinting = False

    #loop through the entire document line by line
    for x in y:
        
        #Split the line into seperate string to make it easier to compare
        h = x.split()
        
        #If the only character in the line is a newline character skip it
        #Otherwise the program will throw an error when it tries to compare it
        if (len(x) == 1 and not(keepPrinting)):
            #Using continue will skip past the liens that would cause errors,
            #While allowing the loop to continue to run
            continue
        elif (keepPrinting and len(x) == 1):# and x != "~"):
            print("="*106)
            graphNum += 1
            if (graphNum == 1):
                plotChildcareEffectiveness()
                trash = input()
            elif(graphNum == 2):
                plotEconomicStanding()
                trash = input()
            elif(graphNum == 3):
                plotBedDensity()
                trash = input()
            print("="*106)
            continue
        #If keepPrinting is true but the current line is empty set keep printing to false
        #This will give us a stop point for printing when we find an empty line
        elif (keepPrinting and (h[0] == "~")):
            print("=" * 106)
            print()
            keepPrinting = False
            continue

    
        #This if statement will check the first string in a line of text
        #This is me testing to see if I can find a specific word and start printing the fiel at that word
        #I edit the text file so that each round of research starts with Round-# so I fan find al of them easily 
        #without writting extra lines of code
        if(h[0]=="Narrative:"):
            print("=" * 106)
            keepPrinting = True
        
        
        #this if will only print out the read line when I am ready to print
        if(keepPrinting):
            #print(x)
            #Trying to make the output look pretty by putting it in a box
            x = x.strip()
            print(f'|{x:<104}|')

def printNarrative(fileName):
    #Change the document into something printable by reading it line by line
    y = fileName.readlines()

    #This variable can help us figure out when to stop trying to print
    keepPrinting = False

    #loop through the entire document line by line
    for x in y:
        
        #Split the line into seperate string to make it easier to compare
        h = x.split()
        
        #If the only character in the line is a newline character skip it
        #Otherwise the program will throw an error when it tries to compare it
        if (len(x) == 1 and not(keepPrinting)):
            #Using continue will skip past the liens that would cause errors,
            #While allowing the loop to continue to run
            continue
        elif (keepPrinting and len(x) == 1):# and x != "~"):
            print("|" + " "*104 + "|")
            continue
        #If keepPrinting is true but the current line is empty set keep printing to false
        #This will give us a stop point for printing when we find an empty line
        elif (keepPrinting and (h[0] == "~")):
            print("=" * 106)
            print()
            keepPrinting = False
            continue

        #This if statement will check the first string in a line of text
        #This is me testing to see if I can find a specific word and start printing the fiel at that word
        #I edit the text file so that each round of research starts with Round-# so I fan find al of them easily 
        #without writting extra lines of code
        if(h[0]=="Narrative:"):
            print("=" * 106)
            keepPrinting = True
        
        
        #this if will only print out the read line when I am ready to print
        if(keepPrinting):
            #print(x)
            #Trying to make the output look pretty by putting it in a box
            x = x.strip()
            print(f'|{x:<104}|')

def plotEconomicStanding():
    # Data 
    countries = ["Afghanistan", "Somalia", "Central African Republic", "Equatorial Guinea", 
         	"Sierra Leone", "Niger", "Chad", "South Sudan", "Mozambique", 
         	"Congo", "Mali", "Guinea-Bissau"] 
  
    economic_standing = np.array([14.58, 8.13, 2.38, 11.81, 3.97, 13.97, 12.7, 12, 17.85, 58.07, 18.83, 1.63]) 
    
  
  
    # Plot Economic Standing 
    plt.figure(figsize=(10, 6)) 
    plt.bar(countries, economic_standing, color='lightgreen') 
    plt.xlabel('Countries') 
    plt.ylabel('Economic Standing (GDP in billions of USD)') 
    plt.xticks(rotation=90) 
    plt.title('Economic Standing') 
    plt.tight_layout() 
    plt.show() 
    
def plotBedDensity():
    #Data
    countries = ["Afghanistan", "Somalia", "Central African Republic", "Equatorial Guinea", 
         	"Sierra Leone", "Niger", "Chad", "South Sudan", "Mozambique", 
         	"Congo", "Mali", "Guinea-Bissau"] 
    physician_density = np.array([0.25, 0.02, 0.07, 0.4, 0.07, 0.04, 0.06, np.nan, 0.09, 0.38, 0.13, 0.2]) 
    hospital_bed_density = np.array([0.4, 0.9, 1, np.nan, np.nan, 0.4, np.nan, np.nan, 0.7, np.nan, 0.1, np.nan]) 
    
    # Plot Physician Density and Hospital Bed Density 
    plt.figure(figsize=(10, 6)) 
    x = np.arange(len(countries)) 
    width = 0.35 
    plt.bar(x - width/2, physician_density, width, label='Physician Density') 
    plt.bar(x + width/2, hospital_bed_density, width, label='Hospital Bed Density') 
    plt.xlabel('Countries') 
    plt.ylabel('Density (per 1,000 people)') 
    plt.xticks(x, countries, rotation=90) 
    plt.legend() 
    plt.title('Physician and Hospital Bed Density') 
    plt.tight_layout() 
    plt.show() 
    

def plotChildcareEffectiveness():
    # Country names and corresponding infant mortality rates
    countries = [
        "Afghanistan",
        "Somalia",
        "Central African Republic",
        "Equatorial Guinea",
        "Sierra Leone",
        "Niger",
        "Chad",
        "South Sudan",
        "Mozambique",
        "Congo",
        "Mali",
        "Guinea-Bissau"
    ]

    infant_mortality_rates = [
        103.06,
        85.06,
        81.74,
        77.85,
        72.3,
        65.53,
        63.99,
        61.63,
        59.77,
        59.12,
        58.99,
        47.69
    ]

    # Create a bar chart
    plt.figure(figsize=(16, 6))
    plt.barh(countries, infant_mortality_rates, color='skyblue')
    plt.xlabel('Infant Mortality Rate per 1,000 Live Births')
    plt.title('Childcare Effectiveness by Country')
    plt.gca().invert_yaxis()  # Invert the y-axis to display the highest rate at the top

    # Display the plot
    plt.show()
    

def printCitations(fileName):
    #Change the document into something printable by reading it line by line
    y = fileName.readlines()

    #This variable can help us figure out when to stop trying to print
    keepPrinting = False

    #loop through the entire document line by line
    for x in y:
        
        #Split the line into seperate string to make it easier to compare
        h = x.split()
        
        #If the only character in the line is a newline character skip it
        #Otherwise the program will throw an error when it tries to compare it
        if (len(x) == 1 and not(keepPrinting)):
            #Using continue will skip past the liens that would cause errors,
            #While allowing the loop to continue to run
            continue
        elif (keepPrinting and len(x) == 1):# and x != "~"):
            print("|" + " "*104 + "|")
            continue
        #If keepPrinting is true but the current line is empty set keep printing to false
        #This will give us a stop point for printing when we find an empty line
        elif (keepPrinting and (h[0] == "~")):
            print("=" * 106)
            print()
            keepPrinting = False
            continue

        
    
        
    
        #This if statement will check the first string in a line of text
        #This is me testing to see if I can find a specific word and start printing the fiel at that word
        #I edit the text file so that each round of research starts with Round-# so I fan find al of them easily 
        #without writting extra lines of code
        if(h[0]=="Citations:"):
            print("=" * 106)
            keepPrinting = True
        
        
        #this if will only print out the read line when I am ready to print
        if(keepPrinting):
            #print(x)
            #Trying to make the output look pretty by putting it in a box
            x = x.strip()
            print(f'|{x:<104}|')

'''
A function that will print out the vision portion of our file
'''
def printVision(fileName):
    #Change the document into something printable by reading it line by line
    y = fileName.readlines()

    #This variable can help us figure out when to stop trying to print
    keepPrinting = False

    #loop through the entire document line by line
    for x in y:
        
        #Split the line into seperate string to make it easier to compare
        h = x.split()
        
        #If the only character in the line is a newline character skip it
        #Otherwise the program will throw an error when it tries to compare it
        if (len(x) == 1 and not(keepPrinting)):
            #Using continue will skip past the liens that would cause errors,
            #While allowing the loop to continue to run
            continue
        elif (keepPrinting and len(x) == 1):# and x != "~"):
            print("|" + " "*104 + "|")
            continue
        #If keepPrinting is true but the current line is empty set keep printing to false
        #This will give us a stop point for printing when we find an empty line
        elif (keepPrinting and (h[0] == "~")):
            print("=" * 106)
            print()
            keepPrinting = False
            continue

        
    
        
    
        #This if statement will check the first string in a line of text
        #This is me testing to see if I can find a specific word and start printing the fiel at that word
        #I edit the text file so that each round of research starts with Round-# so I fan find al of them easily 
        #without writting extra lines of code
        if(h[0]=="Our-Vision:"):
            print("=" * 106)
            keepPrinting = True
        
        
        #this if will only print out the read line when I am ready to print
        if(keepPrinting):
            #print(x)
            #Trying to make the output look pretty by putting it in a box
            x = x.strip()
            print(f'|{x:<104}|')

'''
Curent iteration of this code is workig on printing out specifically the research collection paragraphs
'''
def printResearch(fileName):
    
    #Change the document into something printable by reading it line by line
    y = fileName.readlines()

    #This variable can help us figure out when to stop trying to print
    keepPrinting = False

    #loop through the entire document line by line
    for x in y:
        
        #If the only character in the line is a newline character skip it
        #Otherwise the program will throw an error when it tries to compare it
        if (len(x) == 1 and not(keepPrinting)):
            #Using continue will skip past the liens that would cause errors,
            #While allowing the loop to continue to run
            continue
        #If keepPrinting is true but the current line is empty set keep printing to false
        #This will give us a stop point for printing when we find an empty line
        elif (keepPrinting and (x == "\n")):
            print("=" * 106)
            print()
            keepPrinting = False
            continue

        
    
        #Split the line into seperate string to make it easier to compare
        h = x.split()
    
        #This if statement will check the first string in a line of text
        #This is me testing to see if I can find a specific word and start printing the fiel at that word
        #I edit the text file so that each round of research starts with Round-# so I fan find al of them easily 
        #without writting extra lines of code
        if(h[0]=="Round-#"):
            print("=" * 106)
            keepPrinting = True
        
        
        #this if will only print out the read line when I am ready to print
        if(keepPrinting):
            #print(x)
            #Trying to make the output look pretty by putting it in a box
            x = x.strip()
            print(f'|{x:<104}|')
            
def printMenu():
    #This is a gui menu giving the user the option to look at specific parts of our project
    print("="*39)
    print("|1. Group Members                     |")
    print("|2. Vision and Goals                  |")
    print("|3. Narrative Graphs                  |")
    print("|4. Research acquisition and citations|")
    print("|5. Narrative by itself               |")
    print("|6. Graphs by themselves              |")
    print("|7. Close Program                     |")
    print("="*39 + "\n")

'''
WARNING: IF there are lines in the document that are blank and have multiple spaces the code will break.
        Now that there is more stuff that needs to run this error is important because it will keep the graphs from printing
'''            
        
#open the text file that needs to be read
#utf-8-sig removes a strange set of characters that I found while printing the document
f = open("ENGR-1110 Project.txt", "r", encoding="utf-8-sig") 



#guiInput will hold which menu option the user wants to go to
guiInput = 0
#print(guiInput)

#We need to check the guiInput
#Use a while loop that will keep going until the user enters 6 to close our program
while guiInput != 7:
    printMenu()
    guiInput = int(input("Enter your menu option: "))
    print("")
    
    #option 1 on the menu should print out our group members
    if(guiInput == 1):
        printMembers(f)
        f.close()
        f = open("ENGR-1110 Project.txt", "r", encoding="utf-8-sig") 
        
    #option 2 on the menu should print out vision and goals
    elif(guiInput == 2):
        printVision(f)
        #There is a problem where if we do not close and reopen the file we can no longer read it line by line
        #So we need to close and reopen the file after we read throough it each time
        f.close()
        f = open("ENGR-1110 Project.txt", "r", encoding="utf-8-sig") 
        
    #option 3 will print the narrativeand the graphs.
    #The graphs will be displayed under the paragraph of the narrative that talks about them.
    elif(guiInput == 3):
        printNarrativeAndGrpahs(f)
        f.close()
        f = open("ENGR-1110 Project.txt", "r", encoding="utf-8-sig")
    
    #Option 4 will print out our research acquisition and then the citations of our sources.
    elif(guiInput == 4):
        printResearch(f)
        #There is a problem where if we do not close and reopen the file we can no longer read it line by line
        #So we need to close and reopen the file after we read throough it each time
        f.close()
        f = open("ENGR-1110 Project.txt", "r", encoding="utf-8-sig")
        printCitations(f)
        f.close()
        f = open("ENGR-1110 Project.txt", "r", encoding="utf-8-sig")
    
    #Option 5 displays the narrative all at once
    elif(guiInput == 5):
        printNarrative(f)
        f.close()
        f = open("ENGR-1110 Project.txt", "r", encoding="utf-8-sig")
    
    #option 6 simply displays the graphs all at once
    elif(guiInput == 6):
        plotChildcareEffectiveness()
        plotEconomicStanding()
        plotBedDensity()
        
    #menu option 7 will print our closing statement and then exit the program.
    elif(guiInput == 7):
        print("="*39)
        print("|We hope that we have made you more   |")
        print("|knoledgeable on this topic, so that  |")
        print("|maybe we can make a difference in    |")
        print("|the world.                           |")
        print("="*39)
        print("|Exiting the program now.             |")
        print("="*39)
        f.close()
        sys.exit(0)
    
    else:
        print("="*39)
        print(f'|The option you have selected, {guiInput:<7}|')
        #print("|The option you have selected,", guiInput, "     |") 
        print("|does not exist. Please try again.    |")
        print("="*39, "\n")

    
'''
So far all graphs are easily printed in Spyder IDE.
They are in "plots" tab instead of printed out on the console.
'''