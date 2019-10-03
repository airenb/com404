print("Should I do an activity?")
activity = input()
if (activity == "yes"):
    print("What Should we do?")
    what = input()
    if( what == "swimming"):
        print("do I have a towel?")
        towel = input()
        print("Do i have goggles?")
        goggles = input()
        if(towel == "yes") and (goggles == "yes"):
            print("Let's go")
        else:
            print("another time.")
    else:
        print("Maybe another time")        
else:
    print(" Let's stay in")
