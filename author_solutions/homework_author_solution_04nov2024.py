class NameHandler:
    def __init__(self, name):
        self.__data_ = name
    
    def SayHello(self):
        print(f"Hello! I am {self.__data_}.")
        
    def GetInCaps(self):
        return self.__data_.upper()
    
    def GeListOfChars(self):
        result = []
        for c in self.__data_:
            result.append(c)
        return result

def Test1():
    print("Test 1 has started")
    
    handler = NameHandler("Josias")
    handler.SayHello()
    assert "JOSIAS" == handler.GetInCaps()
    assert ['J', 'o', 's', 'i', 'a', 's'] == handler.GeListOfChars()
    
    print("Test 1 has finished")
    
def main():
    Test1()
    
    print("\nSuccess!")

main()
