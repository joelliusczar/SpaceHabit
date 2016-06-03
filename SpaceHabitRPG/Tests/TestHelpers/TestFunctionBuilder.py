def build_sort_by_function(sortCriteria,dictOfDicts):
    
    comparisonList = []
    def sortFunction(a,b):
        for c in comparisonList:
            field = c[0]
            comparison = c[1]
            if not comparison(a[field],b[field]):
                return False
        return True

    
    keyAndSubDictPair = dictOfDicts.popitem()
    dictOfDicts[keyAndSubDictPair[0]] = keyAndSubDictPair[1]
    for s in sortCriteria:
        sortByFieldName = s[0]
        sortingDirection = s[1]
        fieldType = type(keyAndSubDictPair[1][sortByFieldName])
        #1 is pymongo.ASCENDING
        if sortingDirection == 1:
            if fieldType == type(0):
                comparisonList.append((sortByFieldName,int.__le__))
            elif fieldType == type(""):
                comparisonList.append((sortByFieldName,str.__le__))
            else:
                raise TypeError("field type was something unexpected")
        elif sortingDirection == -1:
            if fieldType == type(0):
                comparisonList.append((sortByFieldName,int.__ge__))
            elif fieldType == type(""):
                comparisonList.append((sortByFieldName,str.__ge__))
            else:
                raise TypeError("field type was something unexpected")
        else:
            raise TypeError("sorting direction was invalid")

    return sortFunction