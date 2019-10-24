print("How many heroes must we gather?")
heroes = int(input())

print("gathering heroes...")
min_heroes = 0 

while(heroes>min_heroes):
   heroes = heroes - 1 
   print(".... found hero," ,heroes,)


print("all heroes have been gathered")