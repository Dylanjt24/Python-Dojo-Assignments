def makeItBig(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    return arr



def countPositives(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            count+=1
    arr[len(arr)-1] = count
    return arr



def sumTotal(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum



def multiples(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum/len(arr)



def length(arr):
    return len(arr)



def minimum(arr):
    if not len(arr):
        return False
    else:
        minimum = arr[0]
        for i in range(len(arr)):
            if arr[i] < minimum:
                minimum = arr[i]
    return minimum



def maximum(arr):
    if not len(arr):
        return False
    else:
        maximum = arr[0]
        for i in range(len(arr)):
            if arr[i] > maximum:
                maximum = arr[i]
    return maximum



def ultimate(arr):
    newDict = {
        "sumTotal": sumTotal(arr),
        "average": multiples(arr),
        "minimum": minimum(arr),
        "maximum": maximum(arr),
        "length": length(arr) 
    }
    return newDict



def reverse(arr):
    for i in range(len(arr)//2):
        arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
    return arr