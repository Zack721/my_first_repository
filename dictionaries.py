def Items(car):
    list_of_keys_elements = []
    for key in car:
        element = car.get(key)
        tuple_elements = tuple((key, element))
        list_of_keys_elements.append(tuple_elements)

    return list_of_keys_elements

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": "1964"
}

result = Items(thisdict)
print(result)

