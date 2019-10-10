print("What phrase do you see?")
phrase = str(input())

print("Reversing...")
num = 0
for position in range (len(phrase),0,-1):
    print("The phrase is:", str(phrase))