def run():
    print("type a message")
    message = input()
    print(" choose: under, over, both, grid")
    chosen = input()

    if (chosen == "under"):
        print(" Halloween")
        print(" - - - - - - - - -")
        print( message )

    elif(chosen == "over"):
        print( message )
        print(" - - - - - - - - -")
        print(" Halloween")

    elif(chosen == "both"):
        print(" Halloween")
        print(" - - - - - - - - -")
        print( message )
        print(" - - - - - - - - -")
        print(" Halloween")

    elif (chosen == "grid"):
        if(len(message)>5):
            for row in range (0, len(message), 1):
                for collum in range (0, len(message), 1):
                    print(collum, "|", end="")
        print()

run()

