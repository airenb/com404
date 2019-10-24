#variable 
health = int(100) 

print("Your health is ",health ,",Escape is in progress...")
min = 0 
max = 5
user_response = input()
while(max>min):
    print("…Oh dear, who is that?")
    user_response = input()
    max = max - 1
    if (user_response== "smiler's bot"):
        health = health - 20
        print("Time to jam out of here!")
    elif(user_response == "hacker"):
        health = health + 20
        print("Yay! Better follow this one!")
    else:
        print("Phew, just another emoji!")

print("Escaped! Health is", health, ".")