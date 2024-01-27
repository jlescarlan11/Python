import calendar

yy = 2024 #  year
mm = 12 #    months


with open('calendar.txt', 'a') as file:
    #   Display the calendar
    for i in range(1, mm+1):    #   month
        file.write(calendar.month(yy, i) + "\n")
        