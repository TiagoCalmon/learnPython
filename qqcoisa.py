#largest=-99999
#n=int(input("type the integer number: "))
#while n != -1:
  #  if n > largest:
  #      largest=n
   # n=int(input("type the integer number: "))
#print(largest)

#for i in range(0, 11):
    # line of code
 #   if (i % 2) != 0:
 #       print(i)

#x = 0
#while x < 11:
 #   if (x % 2) != 0:
 #      print(x)
 #   x += 1
#aux = ""
#for ch in "john.smith@pythoninstitute.org":
#    if ch == "@":
#        break
#    aux += ch
#print(aux)
    # line of code

#for digit in "0165031806510":
#    if digit == "0":
#        print("x", end="")
 #       continue
 #   print(digit, end="")
 #       # line of code
    # line of code

# step 1
beatles = []

print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Step 2:", beatles)

# step 3
for i in range(2):
    beatles.append(str(input("Type b names: ")))
    

print("Step 3:", beatles)

# step 4
del beatles[-1]
del beatles[-1]
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))