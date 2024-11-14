#the class Person have a set/get method for every data member
#in order to get access to an specific value and handle the data members easily
class Person:
    def __init__(obj, name, age, gender):
        obj.__name_ = name
        obj.__age_ = age 
        obj.__gender_ = gender

    #here instead GetPersonAttributes better make 
    #3 different get methods (GetName, GetAge, GetGender)
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


        
    #here instead SetPersonAttributes better make 
    #3 different set methods (SetName, SetAge, SetGender)


#the class Database is aimed to save Person objects
#and provide access to them only through its methods
class Database:
    #the constructor should receive no arguments
    #beside the default argument (DB)
    def __init__(DB):
        #the data members naming is not correct
        DB.__people_ = [] #Isaac: dont think i need this as cannot get name from it in the return value of the method GetPersonByName without getting an error 
        DB.__my_dict_ = {} #the same here

    #the methods names are not correct
    #you should have only two methods: AddPerson(person), GetPersonByName(name)
    #you used those names for the data members but not for the methods
    def AddPerson(DB, input):
        DB.__people_.append(input)
        DB.__my_dict_[input] = len(DB.__people_) -1


    def GetPersonByName(DB, name):
        index_of_person = DB.__my_dict_.get(name)
        if index_of_person != None:
            return User.GetName(),User.GetAge(),User.GetGender()
            
    
        return None

    #the methods GetPersonByName(name) should return a Person object that matches the name
    #otherwise, an error message should be printed
    #example:
    #database.Add(Person("Josias", 23, "Male"))
    #assert database.GetPersonByName("Josias") == Person("Josias", 23, "Male")
    #database.GetPersonByName("Isaac") #error message
    
    #def GetPersonByName(DB):
        #assert 
        
mingzi = "Isaac"
age = 18
Gender = "Male"
User = Person(mingzi, age, Gender) 
database = Database()
database.AddPerson(mingzi)
assert database.GetPersonByName(mingzi) == ("Isaac",18,"Male")
#User.SetPersonAttributes(name_, age_, gender_) given the change in name would be User.AddPerson(name_, age_, gender_)




