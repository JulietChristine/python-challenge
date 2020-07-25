import os
import csv

csvpath = os.path.join("Resources/budget_data.csv")
with open(csvpath, 'r') as csvfile:
    pybank_csv = csv.reader(csvfile, delimiter = ',')
    csv_header = next(pybank_csv)

    month = []
    totals = []
    date_pro = ""
    date_los = ""
    difference = 0
    differences = []

    for row in pybank_csv:
        month.append(row[0])
        months = len(month)
        totals.append(int(row[1]))
        sum_totals = sum(totals)
        totals_max = max(totals)
        totals_min = min(totals)
        if int(row[1]) == totals_max:
            date_pro = row[0]
        if int(row[1]) == totals_min:
            date_los = row[0]

for i in range(1, len(totals)):
    difference = totals[i] - totals[i - 1]
    differences.append(difference)
    average_rate_of_change = sum(differences)/len(differences)
    greatest_increase = max(differences)
    greatest_decrease = min(differences)

print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {months}")
print("Total: $", format(sum_totals, ",.2f"))
print("Average Change: $", format(average_rate_of_change, ",.2f"))
print(f"Greatest Increase in Profits:{date_pro}, $" + format(greatest_increase, ",.2f"))
print(f"Greatest Decrease in Profits:{date_los}, $" + format(greatest_decrease, ",.2f"))

file = open("export.txt", "w")
file.write("Financial Analysis" + "\n")
file.write("----------------------------------------" + "\n")
file.write(f"Total Months: {months}" + "\n")
file.write(f"Total: $ {sum_totals}" + "\n")
file.write(f"Average Change: $ {average_rate_of_change}" + "\n")
file.write(f"Greatest Increase in Profits:{date_pro}, $ {greatest_increase}" + "\n")
file.write(f"Greatest Decrease in Profits:{date_los}, $ {greatest_decrease}" +"\n")
file.close()