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
    def __init__(inv, money):
        inv.__money_ = money
        inv.__bricks_bought_ = []
    
    def GetBudget(inv):

    def BuyBricks(inv, bunch_of_bricks):
        total = bunch_of_bricks.CalcTotalPrice()
        if inv.__money_ >= total:
            inv.__money_-= total
        else:
            print(f"You dont have enough money come back when u do, you need an extra {total - inv.__money_}")

    def AssignBricks(inv):

    
            
class Builder:
    def __init__(bd):
        bd.ID_ = 

    def Build(bd):
        #will take some bricks from the inventory

class House:
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

