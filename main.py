#Importing necessary modules
import os
import csv


#Creating an object from the CSV file "budget_data"
budget_data = os.path.join("budget_data.csv")
total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []


#opening/reading the CVS file
with open(budget_data, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

#reading header
    csv_header = next(csvreader)

#reading the first row
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    
#going through each row of data after
    for row in csvreader:
        # tracking dates
        dates.append(row[0])    

        #calculate the change, then add it to list of changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #total months
        total_months += 1

        #Profit/Losses over entire period
        total_pl = total_pl + int(row[1])
   #greatest profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #greatest decrease
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #average change
    avg_change = sum(profits)/len(profits)
    
#Displaying information 
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")


#Exporting as .txt file
output = open("output.txt", "w")

lne1 = "Financial Analysis"
lne2 = "---------------------"
lne3 = str(f"Total Months: {str(total_months)}")
lne4 = str(f"Total: ${str(total_pl)}")
lne5 = str(f"Average Change: ${str(round(avg_change,2))}")
lne6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
lne7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(lne1,lne2,lne3,lne4,lne5,lne6,lne7))