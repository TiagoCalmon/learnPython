def isYearLeap(year):
    if year < 1582:
        print("Not within the Gregorian calendar period")
        return False
    n = year % 4
    if n == 0:
        n = year % 100
        if n == 0:
            n = year % 400
            if n == 0:
                return True
                #print("Leap year")
            else:
                return False
                #print("Common year")
        else:
            return True
            #print("Leap year")
    else:
        return False
#
# your code from LAB 4.1.3.6
#

def daysInMonth(year, month):
    m_31 = [1, 3, 5, 7, 8, 10, 12]
    m_30 = [4, 6, 9, 11]
    if month in m_31:
        return 31
    elif month in m_30:
        return 30
    else:
        if isYearLeap(year):
            return 29
        else:
            return 28
        
#
# put your new code here
#

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")