print("How many numbers should I sum up?")
amount_sum = int(input())

numbers = 0 
previous_number = 0
while(numbers< amount_sum):
    print("Suggest a number")
    suggested = int(input())
    numbers = numbers + 1 
    previous_number = suggested + previous_number

print(previous_number)