
# User input for number of years
years = int(input("Please enter the number of years: "))

# calculates the number of months based on inputted years
months = years * 12

# initialize variable for total rainfall
total_rain = 0

# Outer loop iterates over years
for year in range (1, years + 1):
    #Inner loop iterates over months
    for month in range(1, 13):
        # user input for inches of rain per month
        month_rain = float(input("How many inches of rain on month {}: ".format(month)))
        # total_rain = total_rain + month_rain
        total_rain += month_rain


# calculates the average rainfall 
avg_rain = total_rain / months

# print number of months, total rainfall, and average rainfall
print("The number of months in {} years is: {}".format(years, months))
print("In {} years there was a total of {} inches of rainfall".format(years, total_rain))
print("The average amount of rainfall per month in {} years is {} inches".format(years, avg_rain))
