print(" What is your name human?")
name = input()
print("")
print(" How old are you (in years)?")
age = input()
print("")
print("How tall are you (in meters)?")
height = float(input())
print("")
print("How much do you weigh (in kg)?")
weight = float(input())

BMI= weight/ height*height 

print(name, "you are",age, "and your BMI is" ,BMI )