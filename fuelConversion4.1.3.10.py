#1 American mile = 1609.344 metres;
#1 American gallon = 3.785411784 litres.
fator=378.5411784/1.609344
print(fator)
def l100kmtompg(liters):
    gallon = liters/3.785411784
    #print(gallon)
    miles = 100/1.609344
    #print(miles)
    return miles / gallon
# put your code here
#

def mpgtol100km(miles):
    liters = 3.785411784
    _100km = (1/1.609344)*100
    gallon = _100km/miles
    return gallon*liters
    
    
#
# put your code here
#

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))