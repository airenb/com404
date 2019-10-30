#first function 
def is_slow_zombie(speed):
    if( speed<5):
        return True 
    else:
        return False 

#second function 
def take_action(mutation, speed):
    if(is_slow_zombie == True):
        print("This" , mutation, "zombie is a slow zombie, you can run around it!")
    else:
        print("this", mutation, " zombie is a fast xombie. you better hide!")

#third function 
def run():
    print("enter the mutation type")
    mutation = input()
    print("what speed?")
    speed = int(input())
    print("pick one:identify or action")
    picked = input()
    
    if(picked == "identify"):
        print("a slow zombie:", is_slow_zombie)
    elif(picked == "action"):
        return take_action
    else:
        print("unknown zombie!")

#run program 
run()
