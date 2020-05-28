blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#
auxblk = blocks
height = 1
if auxblk <= 0:	
    print("The height of the pyramid:", 0)
    exit()
while auxblk > 0:
    height += 1
    auxblk -= height
    
    
height -= 1
print("The height of the pyramid:", height)