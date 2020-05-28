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
    #print("Common year")
#
# put your code here
#

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")