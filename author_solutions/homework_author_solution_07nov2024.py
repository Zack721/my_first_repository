class Person:
    def __init__(self, name = "", age = -1, gender = "UNKNOWN"):
        self.__name_ = ""
        self.__age_ = -1
        self.__gender_ = "UNKNOWN"
        
        if name != self.__name_:
            self.SetName(name)
        if age != self.__age_:
            self.SetAge(age)
        if gender != self.__gender_:
            self.SetGender(gender)
        
    def __str__(self):
        return f"name: {self.__name_}, age: {self.__age_}, gender: {self.__gender_}"

#private
    def __ValidateName(self, name):
        if name.isalpha():
            return True
        
        print("ERROR. PLEASE, INTRODUCE A VALID NAME")
        return False
        
    def __ValidateAge(self, age):
        if age >= 0:
            return True
        
        print("ERROR. PLEASE, INTRODUCE A VALID AGE")
        return False
        
    def __ValidateGender(self, gender):
        if gender == "MALE" or gender == "FEMALE":
            return True
        
        print("ERROR. PLEASE, INTRODUCE A VALID GENDER")
        return False
        

#public      
    def SetName(self, name):
        if self.__ValidateName(name):
            self.__name_ = name

    def SetAge(self, age):
        if self.__ValidateAge(age):
            self.__age_ = age
        
    def SetGender(self, gender):
        value = gender.upper()
        
        if self.__ValidateGender(value):
            self.__gender_ = value

    def GetName(self):
        return self.__name_
        
    def GetAge(self):
        return self.__age_
        
    def GetGender(self):
        return self.__gender_
    

class Database:
    def __init__(self):
        self.__persons_ = list(())
        self.__name_to_indexes_ = dict(())

#public
    def GetSize(self):
        return len(self.__persons_)

    def IsEmpty(self):
        return self.GetSize() == 0

    def AddPerson(self, person):
        if type(person) == type(Person()):

            current_index = len(self.__persons_)
            person_name = person.GetName()

            self.__persons_.append(person)

            if self.__name_to_indexes_.get(person_name) == None:
                self.__name_to_indexes_[person_name] = [current_index]
            else:
                self.__name_to_indexes_[person_name].append(current_index)
        else:
            print("ERROR. PLEASE, INTRODUCE A VALID PERSON OBJECT")

    def GetPersonByName(self, name):
        result = list(())
        indexes = self.__name_to_indexes_.get(name)

        if indexes != None:
            for i in indexes:
                result.append(self.__persons_[i])
                
        return result


def TestPersonConstructor():
    print("Test PersonConstructor has started")
    
    person1 = Person()
    assert person1.GetName() == ""
    assert person1.GetAge() == -1
    assert person1.GetGender() == "UNKNOWN"

    person2 = Person("Isaac", 18, "male")
    assert person2.GetName() == "Isaac"
    assert person2.GetAge() == 18
    assert person2.GetGender() == "MALE"

    person3 = Person("1sabell", 88, "feMale") #should print an error message
    assert person3.GetName() != "1sabell"
    assert person3.GetName() == ""
    assert person3.GetGender() != "feMale"
    assert person3.GetGender() == "FEMALE"
    assert person3.GetAge() == 88

    person4 = Person("Isabell", -88, "FEMALE") #should print an error message
    assert person4.GetName() == "Isabell"
    assert person4.GetAge() != -88
    assert person4.GetAge() == -1
    assert person4.GetGender() == "FEMALE"

    person5 = Person("Andy", 23, "BINARY") #should print an error message
    assert person5.GetName() == "Andy"
    assert person5.GetAge() == 23
    assert person5.GetGender() == "UNKNOWN"
    assert person5.GetGender() != "BINARY"

    print("Test PersonConstructor has finished\n")

def TestPersonMethods():
    print("Test PersonMethods has started")
    
    person = Person()
    #Test method Set/Get Name
    person.SetName("Francis1") #should print an error message
    assert person.GetName() == ""
    person.SetName("Francis")
    assert person.GetName() == "Francis"

    #Test method Set/Get Age
    person.SetAge(-10) #should print an error message
    assert person.GetAge() == -1
    person.SetAge(10)
    assert person.GetAge() == 10

    #Test method Set/Get Gender
    person.SetGender("NEUTRAL") #should print an error message
    assert person.GetGender() == "UNKNOWN"
    person.SetGender("FEMALe")
    assert person.GetGender() == "FEMALE"
    person.SetGender("mAle")
    assert person.GetGender() == "MALE"
    
    print("Test PersonMethods has finished\n")
    
def TestDatabaseConstructor():
    print("Test DatabaseConstructor has started")

    database = Database()
    assert database.GetSize() == 0
    assert database.IsEmpty

    print("Test DatabaseConstructor has finished\n")
    
def TestDatabaseMethods():
    print("Test DatabaseMethods has started")

    database = Database()

    assert database.IsEmpty()

    #Test method AddPerson
    database.AddPerson(Person("Josias", 23, "MALE"))
    assert database.GetSize() == 1
    database.AddPerson(Person("Isaac", 18, "MALE"))
    assert database.GetSize() == 2
    database.AddPerson(Person("Abigail", 55, "FEMALE"))
    assert database.GetSize() == 3

    #Test method GetPersonByName
    query1 = database.GetPersonByName("Josias")
    query2 = database.GetPersonByName("Joseph")
    query3 = database.GetPersonByName("Isaac")
    query4 = database.GetPersonByName("Abigail")
    query5 = database.GetPersonByName("Nathan")

    assert len(query1) == 1
    assert len(query2) == 0
    assert len(query3) == 1
    assert len(query4) == 1
    assert len(query5) == 0
    
    assert query1[0].GetAge() == 23
    assert query3[0].GetGender() == "MALE"
    assert query4[0].GetAge() == 55

    print("Test DatabaseMethods has finished\n")

    

def main():
    TestPersonConstructor()
    TestPersonMethods()

    TestDatabaseConstructor()
    TestDatabaseMethods()
    
    print("\nSuccess!")

main()