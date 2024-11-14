class Person:
    def __init__(obj, name, age, gender):
        obj.__name_ = name
        obj.__age_ = age 
        obj.__gender_ = gender

    def GetName(obj):
        return obj.__name_

    def GetAge(obj):
        return obj.__age_

    def GetGender(obj):
        return obj.__gender_

    def SetName(obj, name):
        obj.__name_ = name

    def SetAge(obj, age):
        obj.__age_ = age 

    def SetGender(obj, gender):
        obj.__gender_ = gender

    def __str__(obj):
        return f"The name is {obj.__name_}; the age is {obj.__age_}; and the gender is {obj.__gender_}"  

class Database:
    def __init__(DB):
        
        DB.__people_ = []  
        DB.__my_dict_ = {}

    def AddPerson(DB, input):
        DB.__people_.append(input)
        indexes =  DB.__my_dict_.get(input.GetName())
        current_index = len(DB.__people_) -1
        if indexes == None:
            DB.__my_dict_[input.GetName()] = [current_index]
                   
        else:
            indexes.append(current_index)



    def GetPersonByName(DB, name):
        list_of_indexes = DB.__my_dict_.get(name)
        
        if list_of_indexes == None:
            return None
        else:
            list_of_objects = []
            for i in list_of_indexes:
                list_of_objects.append(DB.__people_[i])
            return list_of_objects
                


    def GetSize(DB):
        return len(DB.__people_)

    def PrintPeopleName(DB):
        for i in DB.__people_:
            print(i.GetName())

    

def Test():
    mingzi = "Isaac"
    age = 18
    gender = "Male"
    user = Person(mingzi, age, gender) 
    database = Database()
    database.AddPerson(user)
    database.PrintPeopleName()
    database.GetPersonByName(mingzi)
    print(len(database.GetPersonByName(mingzi)))
    
def main():
    Test()
    print("Success")

main()

#Dont know what else u want me to do


