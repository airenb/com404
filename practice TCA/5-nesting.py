dead_ends = 0
mummie = 0 

print("Escaping the tomb...")
min_loop = 0
max_loop = 4 
while(max_loop > min_loop):
    max_loop = max_loop - 1
    print("")
    print("What lies before me?")
    what = input()
    if(what =="a dead end"):
        dead_ends = dead_ends + 1 
        print("time to turn back")
    elif(what =="a mummy"):
        mummie = mummie + 1
        print("better find another way.")
    else:
        print("lets move around it.")

print("encountered" , dead_ends, "dead ends and", mummie, "mummies.")