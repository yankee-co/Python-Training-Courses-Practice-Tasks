# То что я написал до того как заметил, что условия использовать запрещено

def Bio(name, surname, age, male):
    if isinstance(name, str) == isinstance(surname, str) == isinstance(age, int) == isinstance(male, bool):
        if male == True:
            print('Hi there, {0} {1}, {2} y.o., {3}'.format(
                name, surname, age, "man"))
        else:
            print('Hi there, {0} {1}, {2} y.o., {3}'.format(
                name, surname, age, "girl"))
    else:
        print("Oops, something went wrong...")


Bio("Edward", "Zima", 16, True)
Bio("Alisa", "Sagaz", 18, False)

# GIVING WRONG TYPES OF DATA:

Bio(12, "Sagaz", 18, "Wow")

# Вариант без if, else

print()
print()

x = int(input("How many times run programm?"))

for i in range(x):
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    age = int(input("Enter your age: "))
    male = input("Enter 'yes' if u are man, 'no' - girl: ")
    male = (male == "yes")
    while (male == True):
        print('Hi, {0} {1}, {2} y.o., {3}'.format(name, surname, age, "man"))
        break
    while (male == False):
        print('Hi, {0} {1}, {2} y.o., {3}'.format(name, surname, age, "girl"))
        break
