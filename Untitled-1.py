def UniqueChars(str):  #O(1)
    unique_chars = set(())   #O(1)
    for i in str:       #O(n)
        unique_chars.add(i)   #O(1)

    return unique_chars     #O(1)

print(UniqueChars("banana"))   #O(1)