def IsVowelInString(caps_string, output, n):
    print(n)
    if capital_string.count(n) < 0:
        output += f"Vowel {n} isnt in string"
    elif capital_string.count(n) > 0:
        output += f"Vowel {n} is in string"
    
    return output



output_to_user = "Jame"
Original_String = input("What would you like to say?")
capital_string = Original_String.casefold()
for i in ["a", "e", "i", "o", "u"]:
    IsVowelInString(capital_string, output_to_user, i)

print(output_to_user)
#doesnt work for some reason

#Josias said to use a set and functions and scrap this attempt, 

