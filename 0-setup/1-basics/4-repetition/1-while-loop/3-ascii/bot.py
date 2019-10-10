print("How many bars should be charged?")
max_charged = int(input())

bars_charged = 0 

while(bars_charged < max_charged):
   bars_charged = bars_charged + 1
   print("Charging:", " █"*bars_charged)

print("The battery is fully charged.")

