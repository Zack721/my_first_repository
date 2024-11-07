#the class Person have a set/get method for every data member
#in order to get access to an specific value and handle the data members easily
class Person:
    def __init__(obj, name, age, gender):
        obj.__name_ = name
        obj.__age_ = age 
        obj.__gender_ = gender
    #here instead GetPersonAttributes better make 
    #3 different get methods (GetName, GetAge, GetGender)
    def GetPersonAttributes(obj):
        return obj.__name_, obj.__age_, obj.__gender_
        
    #here instead SetPersonAttributes better make 
    #3 different set methods (SetName, SetAge, SetGender)
    def SetPersonAttributes(obj, name, age, gender):
        obj.__name_ = name
        obj.__age_ = age 
        obj.__gender_ = gender

#the class Database is aimed to save Person objects
#and provide access to them only through its methods
class Database:
    #the constructor should receive no arguments
    #beside the default argument (DB)
    def __init__(DB, AddPerson, GetPersonByName):
        #the data members naming is not correct
        DB.AddPerson_ = AddPerson #because the constructor does not receive arguments, the assignment should be an empty container (list, set, dict...)
        DB.GetPersonByName_ = GetPersonByName #the same here

    #the methods names are not correct
    #you should have only two methods: AddPerson(person), GetPersonByName(name)
    #you used those names for the data members but not for the methods
    def SetValues(DB, individual):
        DB.AddPerson_ .append(individual)

    #the methods GetPersonByName(name) should return a Person object that matches the name
    #otherwise, an error message should be printed
    #example:
    #database.Add(Person("Josias", 23, "Male"))
    #assert database.GetPersonByName("Josias") == Person("Josias", 23, "Male")
    #database.GetPersonByName("Isaac") #error message
    
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


