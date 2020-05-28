
        

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
        
def dayOfYear(year, month, day):
    if (year < 0) or (month < 1 ) or (month > 12 ) or (day < 1) or (day > 31):
        return None
    if month == 2:
        if isYearLeap(year):
            if day > 29:
                return None
        else:
            if day > 28:
                return None
    a = ((12 - month) / 10)
    b = year - a
    c = month + (12 * a)
    d = b / 100
    e = d / 4
    f = 2 - d + e
    g = int(365.25 * b)
    h = int(30.6001 * (c + 1))
    i = int((f + g) + (h + day) + 5)
    j = int(i % 7) #Resto de I por 7, onde 0=SAB, 1=DOM, 2=SEG, 3=TER, 4=QUA, 5=QUI, 6=SEX
    if j == 0: 
        return "SAB"
    elif j == 1: 
        return "DOM"
    elif j == 2: 
        return "SEG"
    elif j == 3:
        return "TER"
    elif j == 4: 
        return "QUA"
    elif j == 5: 
        return "QUI"
    elif j == 6:
        return "SEX" 
    else:   
        return None
    
#
# put your new code here
#

print(dayOfYear(2000, 2, 29))