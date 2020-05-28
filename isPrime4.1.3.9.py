def isPrime(num):
    if num <=1:
        return False
    z = num - 1
    while z > 1:
        if (num%z == 0):
            return False
        z -= 1
    return True
    
        
#
# put your code here
#

for i in range(1, 2000):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()