c0 = int(input("Enter a integer number : "))
steps = 0
if c0 <= 0:
    exit()
while c0 != 1:
    if (c0 % 2) == 0:
        c0 /= 2
    else:
        c0 = 3*c0 + 1
    print(int(c0))
    steps += 1
print("steps = ",steps)
