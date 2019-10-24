#function_1 
def under():
    print( word )
    print("*******")

#function_2
def over():
    print("********")
    print( word )

#function_3
def both():
    print("********")
    print( word )
    print("********")

#function_4 
def grid():
    print("********         ********")
    print(word,   "|",      word,)
    print("********         ********")
    print("********         ********")
    print(word,   "|",      word,)
    print("********         ********") 



print("What is your word?")
word = input()

print("option 1, 2, 3 or 4")
option = int(input())
if (option == "1"):
    under()
elif(option =="2"):
    over()
elif(option =="3"):
    both()
elif(option== "4"):
    grid()
