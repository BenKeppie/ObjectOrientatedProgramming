class VirtualPet:
    """An implementation of a virtual pet"""

    def __init__(self,Name):
        self.name=Name
        self.hunger=50
        self.location="Home"
        print("I have been born! I am called {0}".format(self.name))

    def talk(self):
        print("Hello, I am your pet.")

    def eat(self,food):
        self.hunger=self.hunger+10
        print("Mmmm that {0} was yummy.".format(food))

    def walk(self,location):
        self.location=location
        print("Wow that was a good walk to {0}".format(location))

def DisplayMenu(location):
    print()
    print("Your pets hunger is currently: {}".format(pet_one.hunger))
    print()
    print("You are currently at {0}, what do you wish to do?".format(location))
    print()
    print("1. Talk")
    print("2. Eat")
    print("3. Walk")
    print()

def MenuChoice():
    Choice=int(input(""))
    if Choice==1:
        pet_one.talk()
    elif Choice==2:
        Food=GetFood()
        pet_one.eat(Food)
    elif Choice==3:
        location=GetLocation()
        pet_one.walk(location)
        pet_one.hunger=pet_one.hunger-10
        


def GetLocation():
    Location=0
    LocationID=""
    
    print("Where would you like to walk your pet to?")

    print()
    print("1. Home")
    print("2. Cambridge")
    print("3. Cambourne")
    print("4. Hardwick")
    Location=int(input())
    
    LocationID=LocationBank(Location)
    return LocationID

def LocationBank(Location):
    Valid=False
    while not Valid:
        Valid=True
        if Location==1:
            LocationID="Home"
        elif Location==2:
            LocationID="Cambridge"
        elif Location==3:
            LocationID="Cambourne"
        elif Location==4:
            LocationID="Hardwick"
        else:
            Location=0
            Location=int(input("Invalid input, please enter a number."))
            Valid=False
    return LocationID
    



def GetFood():
    Food=0
    
    print("What would you like to feed your pet?")

    print()
    print("1. Carrot")
    print("2. Cookie")
    print("3. Chocolate")
    print("4. Pizza")
    Food=int(input())
    FoodID=FoodBank(Food)
    return FoodID



    
def FoodBank(Food):
    Valid=False
    while not Valid:
        Valid=True
        if Food==1:
            FoodID="Carrot"
            
        elif Food==2:
            FoodID="Cookie"
            
        elif Food==3:
            FoodID="Chocolate"
        elif Food==4:
            FoodID="Pizza"
        else:
            Food=0
            Food=int(input("Invalid input, please enter a number."))
            Valid=False
    return FoodID
          


if __name__=="__main__":
    Name=input("What would you like to call your pet? ")
    print()
    pet_one=VirtualPet(Name)
    print()
    print("Welcome to the main menu! You are currently at Home, please pick choose a number that corresponds to the action you wish to do.")
    Valid=False
    while not Valid:
        DisplayMenu(pet_one.location)
        MenuChoice()
