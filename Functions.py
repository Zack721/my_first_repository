


def GetName():
    name = input("What is your name")
    return name 

def PrintName(name):
        print(f"Hello {name}.")
    


break_loop = False
while break_loop ==  False:
    
    PrintName(GetName())
    break_loop = input("Would you like to continue?")




