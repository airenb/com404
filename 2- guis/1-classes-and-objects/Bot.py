class Bot :
   
   # contructor
    def __init__(self, name):
        self.name = name 
        self.age = 0
        self.energy = 10
        self.shield = 10

    #method 
    def display_name(self):
        
        
        print("--------")
        print("|", self.name,   "|")
        print("--------") 
    
    
    
    def display_age(self):
        print(".-----.")
        print("| .-. |")
        print("| ",self.age," |")
        print("| `-' |") 
        print("`-----'")


    
    def display_energy(self):
        print("my energy is", "♦"*self.energy)
   
   
   
    def display_shield(self):
        print("my shield level is", "♦"* self.shield)

    #make some bots 

beep = Bot("Beep")
beep.display_name()
beep.display_age()
beep.display_energy()
beep.display_shield()    



 