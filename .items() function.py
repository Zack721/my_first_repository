def items_function(dict):
    list_of_keys_elements = []
    for key, value in dict.items():
        list_of_keys_elements.append(key)
    list_of_keys_elements.sort()
    return list_of_keys_elements

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": "1964",
  "owner": "Josias"
}

print(items_function(thisdict))



