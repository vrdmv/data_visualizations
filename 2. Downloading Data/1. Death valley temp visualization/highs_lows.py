import csv
from matplotlib import pyplot as plt
from datetime import datetime

# first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')

# Get dates, highs and lows temperatures from file
filename = 'death_valley_2014.csv'
with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)
    # for index, column_header in enumerate(header_row):
        # print(str(index) + ' - ' + column_header)

    dates, highs, lows = [], [], [] # VERY INTERESTING !!!
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(str(current_date) + " - missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# Plot data.
figure = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates,highs,lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=17)
plt.xlabel('', fontsize=16)
figure.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()

