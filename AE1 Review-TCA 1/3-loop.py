print("How many miles must I travel before I reach the secret base?")
miles = int(input())

print("I will count the miles...")

#loop
min_miles = 0 
while(miles>min_miles):
    print("i have", miles, "to go before i reach base" )
    miles = miles - 1
print("I have arrived at the secret headquarters of the MIB!")
print("It is time to sneak in.")