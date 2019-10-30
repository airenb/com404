def run():
    print("type a message")
    message = input()
    print(" choose: under, over, both, grid")

chosen = input()

def under (message):
    print(" Halloween")
    print(" - - - - - - - - -")
    print( message )

def over (message):
    print( message )
    print(" - - - - - - - - -")
    print(" Halloween")

def both (message):
    print(" Halloween")
    print(" - - - - - - - - -")
    print( message )
    print(" - - - - - - - - -")
    print(" Halloween")

def grid( message):
    if(len(message)>5):
        for row in range (0, len(message), 1):
            for collum in range (0, len(message), 1):
                print(collum, "|", end="")
            print()


run()

