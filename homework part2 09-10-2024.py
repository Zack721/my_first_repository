def UniqueChars(str):  #O(1)
    unique_chars = set(())   #O(1)
    for i in str:       #O(n)
        unique_chars.add(i)   #O(1)

    return unique_chars     #O(1)

user_set = UniqueChars(input("What would you like to input: \n"))  #O(1)
if "1" in user_set and "0" in user_set and len(user_set) == 2:
    print("Yes")
else:
    print("No")