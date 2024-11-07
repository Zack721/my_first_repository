class Person:
    def __init__(obj, name):
        obj.__name_ = name
     
    def GetName(obj):
        return obj.__name_
        
    def SetName(obj, name2):
        obj.__name_= name2
        
individual = Person("Nathan")

individual.SetName("Isaac") 
print(individual.GetName())
print(individual._Person__name_)