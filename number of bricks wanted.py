class Brick:
    def __init__(obj):
        obj.VALUE_ = 5

class BrickBatch:
    def __init__(br, amount):
        br.bricks_= []
        br.amount_ = amount
        br.__BatchMaker()
    
    def __BatchMaker(br):
        for i in range(0, br.amount_):
            br.bricks_.append(Brick())
        
    def CalcTotalPrice(br):
        return br.amount_ * Brick().VALUE_
       
class Inventory:
    #This class should have at least 3 data members: money_ (int), bricks_bought_ (container of Bricks objects), 
    #and authorized_personnel_ (container of Builder objects)
    def __init__(inv, money):
        inv.__money_ = money
        inv.__bricks_bought_ = []

    #Make one private methods: IsAuthorizedPersonnel(id) - return bool
    
    def GetBudget(inv):

    def BuyBricks(inv, bunch_of_bricks):
        total = bunch_of_bricks.CalcTotalPrice()
        if inv.__money_ >= total:
            inv.__money_-= total
        else:
            print(f"You dont have enough money come back when u do, you need an extra {total - inv.__money_}")

    #This method takes one argument typed Builder, if the builder is registred as authorized personnel,
    #so assign the necessary bricks to make a house, if you do not have enought bricks, inside the method buy the rest of bricks,
    #but if there is not necessary money, so print as much as you can, and then print a message error telling that there are not enough resources
    def AssignBricks(inv):

    
#This class must have one data member: id_ which is a string         
class Builder:
    #Here the constructor is incomplete, make sure you take all the necessary arguments
    def __init__(bd):
        #this data member must be private
        bd.ID_ = 
        
    #This method should receive a batch of bricks, if the amount is enough to build the a house must print "Building house..." 
    #and then return a House object, otherwise should print a message error
    def Build(bd):
        #will take some bricks from the inventory

class House:
    #The constructor receives a batch of bricks, if the amount is enough should print "A house was built", otherwise print a error message
    def __init__(hs):
        hs.BRICKS_NEEDED_ = 500
    def AMountOfBricksNeeded(hs):
        #number if bricks needed to build a house
def main():
    bricks_wanted = int(input("How many bricks do u want?")) 
    container_of_bricks = BrickBatch(bricks_wanted)
    print(len(container_of_bricks.bricks_))
    print(f"${container_of_bricks.CalcTotalPrice()} ")



#is a class helper with only one property which is public
#has one method that makes the batch
#should receive one argument that is an int saying the number of bricks they want also have a container that holds objects
#have a method that calcs the total value of all the bricks in the container

