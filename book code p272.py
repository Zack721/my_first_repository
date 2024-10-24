def AdjustValuesForNextRow(Spaces, Symbols):
    Spaces = Spaces - 1
    Symbols = Symbols + 2
    return Spaces, Symbols


NumberOfSpaces = int(input())
NumberOfSymbols = int(input())
NumberOfSpaces, NumberOfSymbols = AdjustValuesForNextRow(NumberOfSpaces, NumberOfSymbols)
print(NumberOfSpaces)
print(NumberOfSymbols)

