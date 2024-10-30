def CalcAverages(list):
    total = 0
    for grade in list:
        total += grade
    
    average = total/len(list)
    return average

list_of_grades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 9, 8]

print(f"The average is:{CalcAverages(list_of_grades)}")
