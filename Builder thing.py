class Builder:
    #Here the constructor is incomplete, make sure you take all the necessary arguments
    def __init__(bd, id):#Done
        #this data member must be private
        bd.__id_ = id

    def GetID(bd):
        return bd.__id_

        
    #This method should receive a batch of bricks, if the amount is enough to build the a house must print "Building house..." 
    #and then return a
    
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
        

def main():
    database = Database()
    database.AddBuilder(Builder("12hd"))
    database.AddBuilder(Builder("34hg"))
    database.AddBuilder(Builder("56nj"))
    database.AddBuilder(Builder("12hd"))
    result = database.GetBuilderByID("12hd")
    print(result.GetID())
    
main()