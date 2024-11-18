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
class House:
    #The constructor receives a batch of bricks, if the amount is enough should print "A house was built", otherwise print a error message
    def __init__(hs, brick_batch): #brick_batch is object of the class BrickBatch
        hs.BRICKS_NEEDED_ = 500
        hs.__is_built_ = hs.__CanBuildHouse(brick_batch)

    def __CanBuildHouse(hs, brick_batch):
        if brick_batch.amount_ < hs.BRICKS_NEEDED_:
            return False
        else:
            return True
        
    def IsHouseBuilt(hs):
        return hs.__is_built_

#This class must have one data member: id_ which is a string         
class Builder:
    #Here the constructor is incomplete, make sure you take all the necessary arguments
    def __init__(bd, id):#Done
        #this data member must be private
        bd.__id_ = id
        

    def GetID(bd):
        return bd.__id_

        
    #This method should receive a batch of bricks, if the amount is enough to build the a house must print "Building house..." 
    #and then return a House object, otherwise should print a message error
    def __IsEnoughBricks(bd, needed_amount_bricks):
        pass


    def Build(bd, object):
        if len(object.amount_) >=House().BRICKS_NEEDED_:
            print("Building house...")
            return House()
        else:
            print("Not enough bricks")

        #will take some bricks from the inventory
        #To Josias, the instructions here arent clear, how many bricks exactly do u want here
        for i in range(0, House.BRICKS_NEEDED_):
            Inventory.__bricks_bought_.pop(i)

class Database:
    def __init__(DB):
        
        DB.__builders_ = []  
        DB.__builderID_to_index_ = {}

    def AddBuilder(DB, builder):
        builder_index =  DB.__builderID_to_index_.get(builder.GetID())
        if builder_index == None:
            DB.__builders_.append(builder)
            DB.__builderID_to_index_[builder.GetID()] = len(DB.__builders_) -1
                   
        else:
            print("The ID is already associated with a different builder.")


    def GetBuilderByID(DB, ID):
        list_of_indexes = DB.__builderID_to_index_.get(ID) #when calling this method make sure to put that the argument ID is equal to builder.GetID() 
        if list_of_indexes == None:
            return None
        else:
            return DB.__builders_[list_of_indexes]  



class Inventory:
    #This class should have at least 3 data members: money_ (int), bricks_bought_ (container of Bricks objects), 
    #and authorized_personnel_ (container of Builder objects)
    def __init__(inv, money):#Done
        inv.__money_ = money
        inv.__bricks_bought_ = []



    #Make one private methods: IsAuthorizedPersonnel(id) - return bool

    def __IsAuthorizedPersonnel_(inv, construction_worker):#Done
        id = construction_worker.GetID()
        if id in inv.authorized_personnel_: #Josias, im not sure I should be calling id like this or if i should do it like builder.__id_
            return True
        else:
            return False

        
    
    #def GetBudget(inv):

    def BuyBricks(inv, bunch_of_bricks):
        total = bunch_of_bricks.CalcTotalPrice()
        if inv.__money_ >= total:
            inv.__money_-= total
        else:
            print(f"You dont have enough money come back when u do, you need an extra {total - inv.__money_}")

    #This method takes one argument typed Builder, if the builder is registred as authorized personnel,
    #so assign the necessary bricks to make a house, if you do not have enought bricks, inside the method buy the rest of bricks,
    #but if there is not necessary money, so print as much as you can, and then print a message error telling that there are not enough resources
    def AssignBricks(inv, builder):#To Josias,conflicting requirements with some other parts 
        if inv.__IsAuthorizedPersonnel_() == True:
            if len(inv.__bricks_bought_) <= House.BRICKS_NEEDED_:
                if Brick().VALUE_* (House.BRICKS_NEEDED_ - len(Inventory().__bricks_bought_)) >= #Dont know what to do








def main():
    bricks_wanted = int(input("How many bricks do u want?")) 
    container_of_bricks = BrickBatch(bricks_wanted)
    print(len(container_of_bricks.bricks_))
    print(f"${container_of_bricks.CalcTotalPrice()} ")



#is a class helper with only one property which is public
#has one method that makes the batch
#should receive one argument that is an int saying the number of bricks they want also have a container that holds objects
#have a method that calcs the total value of all the bricks in the container

