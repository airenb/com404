print("Calculating the sum of the first 100 numbers...")
number = 0
previous_number = 0

while(number <100):
    number = number + 1 
    previous_number = number + previous_number
    number + previous_number

print(previous_number)



