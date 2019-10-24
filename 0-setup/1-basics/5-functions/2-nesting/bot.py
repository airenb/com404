#function is defined 
def identify():
    print("what do you see?")
    see = input()
    if (see == "a large boulder"):
        print("It's time to run!")
    else:
        print("We will be fine")

#call function 
identify()