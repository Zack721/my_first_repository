class Person:
    def __init__(obj):
        obj.__name_= ""

    def PrintName(obj):
        print(f"Hello, i am {obj.__name_}")

    def GetName(obj):
        return obj.__name_


    def NameInCaps(obj):
        return obj.__name_.upper()

    def SetName(obj, name):
        obj.__name_ = name


    def StrToList(obj):
        list_of_chars = []
        for character in obj.__name_:
            list_of_chars.append(character)
        return  list_of_chars
def TestEmptyName():
    person3 = Person()
    person3.PrintName()
    #assert person3.GetName() == ""
    #assert person3.NameInCaps() == ""
    #assert person3.StrToList() == []


def TestNotEmptyNames():
    person4 = Person()
    person4.SetName("Bartholomew")
    person4.PrintName()
    assert person4.GetName() == "Bartholomew"
    assert person4.NameInCaps() == "BARTHOLOMEW"
    assert person4.StrToList() == ['B','a','r','t','h','o','l','o','m','e','w']


def main():
    
    TestEmptyName()
    TestNotEmptyNames()
    print("\nsuccess")
main()