day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if year % 4 == 0 and month == 2 and day <= 29:
    print("Date valid.")

elif year % 4 != 0 and month == 2 and day <= 28:
    print("Date valid.")

elif month % 2 != 0 and month in range(1, 8) and day in range(1, 32) and year in range(1, 2021) and (month != 2):
    print("Date valid.")

elif month % 2 == 0 and month in range(1, 8) and day in range(1, 31) and year in range(1, 2021) and (month != 2):
    print("Date valid.")

elif month % 2 != 0 and month in range(8, 13) and day in range(1, 31) and year in range(1, 2021) and (month != 2):
    print("Date valid.")

elif month % 2 == 0 and month in range(8, 13) and day in range(1, 32) and year in range(1, 2021) and (month != 2):
    print("Date valid.")

else:
    print("Invalid date.")

"""
1	January		31 days
2	February	28 days, 29 in leap years
3	March		31 days
4	April		30 days
5	May			31 days
6	June		30 days
7	July		31 days
8	August		31 days
9	September	30 days
10	October		31 days
11	November	30 days
12	December	31 days
"""
