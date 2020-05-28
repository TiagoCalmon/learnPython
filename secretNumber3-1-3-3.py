secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
inp=int(input("type a integer number: "))
while inp != secret_number:
    print("Ha ha! You're stuck in my loop!")
    inp=int(input("type a integer number: "))
print("Well done, muggle! You are free now.")