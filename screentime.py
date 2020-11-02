import csv
import sys
import math

#making sure the comand line has three arguments
if len(sys.argv) != 2:
    print("Error")
    print("Usage: python screentime.py file.csv")
    exit(1)

# initializing the variables
count = []
unlock = 0
screenon = []
path = sys.argv[1]

''' times phone was unlocked'''

#open the csv file into a reader
with open (path,'r') as file:
    reader = csv.DictReader(file)

    #add items to a list
    for row in reader:
        #print(row)
        count.append(row['counter'])

        
        #cast items to ints
        for x in range(0, len(count)):
           count[x] = int(count[x])

''' total time screen was on for'''
    
#open the csv file into a reader
with open (path,'r') as file:
    reader = csv.DictReader(file)
    
    #add items to a list
    for row in reader:
        #print(row)
        screenon.append(row['milis'])
        
        #cast items to ints
        for x in range(0, len(screenon)):
           screenon[x] = int(screenon[x])

    totalmilis = sum(screenon)
    millis = math.floor(totalmilis % 1000)
    second = math.floor((totalmilis / 1000) % 60)
    minute = math.floor((totalmilis / (1000 * 60)) % 60)
    hour = math.floor((totalmilis / (1000 * 60 * 60)) % 24)
    total = (f'{hour:02}:{minute:02}:{second:02}')

    '''show the result'''

    #show screen on time  
    print(f' you unlocked your phone {count[-1]} times yesterday, your screen was on for {total}') 
    
    


