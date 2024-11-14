class DataBase:
    def __init__(obj):
        obj.__my_list_ = []
        obj.__my_dict_ = {}

    def AddStrToListNDict(obj, input):
        obj.__my_list_.append(input)
        obj.__my_dict_[input[0]] = len(obj.__my_list_) -1
        
    def GetElemByFirstLetter(obj, letter):
        index_of_element = obj.__my_dict_.get(letter)
        if index_of_element != None:
            return obj.__my_list_[index_of_element]
        return None
def Test1():
    database = DataBase()

    database.AddStrToListNDict("Isaac")
    database.AddStrToListNDict("Yolanda")
    assert database.GetElemByFirstLetter("I") == "Isaac"
    assert database.GetElemByFirstLetter("Y") == "Yolanda"
def main():
    Test1()
main()





