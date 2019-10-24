#first function 
def is_league_united(hero_1, hero_2):
    if (hero_1 == "superman" and hero_2 == "wonder woman"):
        return True
    elif(hero_1 =="wonder woman" and hero_2 =="superman"):
        return True
    else:
        return False

#secind function 
def decide_plan(hero_1, hero_2):
    if(is_league_united(hero_1,hero_2)== True):
        return "time to save the world"
    else:
        return "we must unite the league"
    
#third function 
def run():
    print("Enter the name of the first hero")
    hero_1 = input()
    print("Enter the name of the second hero ")
    hero_2 = input()
    print("league or plan?")
    pick = input()
    if (pick == "league"):
        return is_league_united
    elif(pick == "plan"):
        return decide_plan
    else:
        print("Invalid command. Please try again!")

#run the program
run()