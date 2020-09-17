import os
import csv

cwkdir = os.getcwd()

budget_data = os.path.join(cwkdir, 'Resources', 'budget_data.csv')


total_months = []
total_profit = []
monthly_profit_change = []
 
# Open csv 
with open(budget_data,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    header = next(csvreader)  

    for row in csvreader: 


        total_months.append(row[0])
        total_profit.append(int(row[1]))


    for x in range(len(total_profit)-1):
        

        monthly_profit_change.append(total_profit[x+1]-total_profit[x])
        

max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)


max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Results

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")