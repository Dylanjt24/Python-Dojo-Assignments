def countDown(num):
    newList = []
    if num < 0:
        print("Please provide a number greater than or equal to zero")
    else:
        for i in range(num, -1, -1):
            newList.append(i)
    return newList



def printReturn(arr):
    print(arr[0])
    return arr[1]



def firstPlusLength(arr):
    sum = arr[0]
    sum += len(arr)
    return sum



def greaterThanSecond(arr):
    newList = []
    if len(arr) < 2:
        return False
    else:
        for i in range(len(arr)):
            if arr[i] > arr[1]:
                newList.append(arr[i])
    print(len(newList))
    return newList



def lengthAndValue(size, value):
    newList = []
    for i in range(0, size):
        newList.append(value)
    return newList