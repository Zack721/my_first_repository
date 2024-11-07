class Car:
    def __init__(obj, brand, model, colour, year):
        obj.brand_ = brand
        obj.model_ = model
        obj.colour_ = colour
        obj.year_ = year

    def __str__(obj):
        return f"This is a {obj.brand_} {obj.model_} made in {obj.year_} in {obj.colour_}"
    
    def GetColour(obj):
        return obj.colour_

        

car_info = Car("Ford", "Mustang", "Black and yellow", 1985)
cars_colur = car_info.GetColour()
print(cars_colur)

