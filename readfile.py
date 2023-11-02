# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


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
            keepPrinting = False
            continue

        
    
        #Split the line into seperate string to make it easier to compare
        h = x.split()
    
        #This if statement will check the first string in a line of text
        #This is me testing to see if I can find a specific word and start printing the fiel at that word
        #I edit the text file so that each round of research starts with Round-# so I fan find al of them easily 
        #without writting extra lines of code
        if(h[0]=="Round-#"):
            keepPrinting = True
        
        
        #this if will only print out the read line when I am ready to print
        if(keepPrinting):
            print(x)
            
'''
WARNING: IF there are lines in the document that are blank and have multiple spaces the code will break.
        Now that there is more stuff that needs to run this error is important because it will keep the graphs from printing
'''            
        
#open the text file that needs to be read
#utf-8-sig removes a strange set of characters that I found while printing the document
f = open("ENGR-1110 Project.txt", "r", encoding="utf-8-sig") 
printResearch(f)
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

# Data 
countries = ["Afghanistan", "Somalia", "Central African Republic", "Equatorial Guinea", 
         	"Sierra Leone", "Niger", "Chad", "South Sudan", "Mozambique", 
         	"Congo", "Mali", "Guinea-Bissau"] 
  
economic_standing = np.array([14.58, 8.13, 2.38, 11.81, 3.97, 13.97, 12.7, 12, 17.85, 58.07, 18.83, 1.63]) 
physician_density = np.array([0.25, 0.02, 0.07, 0.4, 0.07, 0.04, 0.06, np.nan, 0.09, 0.38, 0.13, 0.2]) 
hospital_bed_density = np.array([0.4, 0.9, 1, np.nan, np.nan, 0.4, np.nan, np.nan, 0.7, np.nan, 0.1, np.nan]) 
  
  
# Plot Economic Standing 
plt.figure(figsize=(10, 6)) 
plt.bar(countries, economic_standing, color='lightgreen') 
plt.xlabel('Countries') 
plt.ylabel('Economic Standing (GDP in billions of USD)') 
plt.xticks(rotation=90) 
plt.title('Economic Standing') 
plt.tight_layout() 
plt.show() 
  
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

'''
So far all graphs are easily printed in Spyder IDE.
They are in "plots" tab instead of printed out on the console.
'''