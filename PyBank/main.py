import os
import csv

pybankpath = os.path.join("C:\\Users\\dtrob\\repos\\Challenges\\Challenge 3\\python-challenge\\PyBank\\Resources\\budget_data.csv")

found = False

with open(pybankpath, 'r') as file:
    reader = csv.reader(file)
    # Skip the header row
    data = list(reader)

# Calculate the total number of months
# Subtract 1 to exlude the header row
num_months = len(data) - 1 

# Initialize the net total to zero
net_total = 0
# Initialize variables for change calculations
previou_profit_loss = 0
changes = []
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

# Iterate through the data list to calculate the net total and changes
for i in range(1, len(data)):
    row = data[i]
    date = row[0]
    profit_loss = int(row[1])
    # Calculate net total
    net_total += profit_loss
    # Calculate change from previous month
    if i > 1:
        change = profit_loss - previou_profit_loss
        changes.append(change)

        # Check if the current change is the greatest increase
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = date

        # Check if the current change is the greatest decrease
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = date

    # Update previous profit/loss
    previou_profit_loss = profit_loss

# Calculate average change
average_change = sum(changes) / len(changes)

print("Total Months:", num_months)
print("Total:", net_total)
print("Average Change:", average_change)
print("Greatest Increase in Profits:", greatest_increase_date, "($", greatest_increase, ")")
print("Greatest Increase in Profits:", greatest_decrease_date, "($", greatest_decrease, ")")

# Prepare the content to be written to the output file
output_content = f"Financial Analysis\n"
output_content += f"----------------------------\n"
output_content += f"Total Months: {num_months}\n"
output_content += f"Total: ${net_total}\n"
output_content += f"Average Change: ${average_change:.2f}\n"
output_content += f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
output_content += f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"

# Specify the output file name
output_file = "financial_analysis.txt"

# Write the content to the output file
with open(output_file, 'w') as file:
    file.write(output_content)

print("Financial analysis exported to", output_file)
