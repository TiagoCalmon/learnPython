def readint(prompt, min, max):
#
# put your code here
    v=None
    while True:
        try:
            v=int(input(prompt))
            assert v > min and v < max
        except ValueError:
            print('Error: wrong input.')
            continue
        except AssertionError:
            print('Error: the value is not within permitted range ( ', min , ' .. ', max, ' )')
            continue
        return v

    
v = readint("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)