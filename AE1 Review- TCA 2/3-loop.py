#message
print("how many zones must i cross?")
zones = int(input())

print("Crossing zones...")

#loop
min_zones = 0 
while(zones>min_zones):
    print("crossed zones", zones, )
    zones = zones - 1

print("Crossed all zones.  Jumanji!")