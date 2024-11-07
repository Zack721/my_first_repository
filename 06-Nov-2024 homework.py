class Person:
    def __init__(obj, name, age, gender):
        obj.__name_ = name
        obj.__age_ = age 
        obj.__gender_ = gender

    def GetPersonAttributes(obj):
        return obj.__name_, obj.__age_, obj.__gender_
    
    def SetPersonAttributes(obj, name, age, gender):
        obj.__name_ = name
        obj.__age_ = age 
        obj.__gender_ = gender

class Database:
    def __init__(DB, AddPerson, GetPersonByName):
        DB.AddPerson_ = AddPerson
        DB.GetPersonByName_ = GetPersonByName

    def SetValues(DB, individual):
        DB.AddPerson_ .append(individual)

    def PrintName(DB):
        print(f"The members of the list are{DB.AddPerson_}")


name_ = input("name?")
age_ = int(input("Age?"))
gender_ = input("Gender?")
User = Person(name_, age_ , gender_)
data_b = Database(list(()),"")

#User.SetPersonAttributes(name_, age_, gender_)
data_b.SetValues(User.GetPersonAttributes())
data_b.PrintName()


