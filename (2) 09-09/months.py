index = int(input("Enter number of the month: "))
if index in range(2, 5):
    print("SPRING")
elif index in range(5, 8):
    print("SUMMER")
elif index in range(8, 11):
    print("AUTUMN")
elif index in range(11, 13) or index == 1:
    print("WINTER")
else:
    print("Some data given wrong...")
