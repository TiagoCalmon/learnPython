year = int(input("Enter a year: "))
if year < 1582:
    print("Not within the Gregorian calendar period")
    exit()
n = year % 4
if n == 0:
    n = year % 100
    if n == 0:
        n = year % 400
        if n == 0:
            print("Leap year")
        else:
            print("Common year")
    else:
        print("Leap year")
else:
    print("Common year")

#
# Put your code here.
#