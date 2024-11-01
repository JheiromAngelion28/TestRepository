def checkvalue(value,datalist): 
    if(value.casefold() in (name.casefold() for name in datalist)):
        return True
    return False

data = ["Clodsire", "quagsire", "best", "Perfection"]
print(checkvalue("Perfection",data))