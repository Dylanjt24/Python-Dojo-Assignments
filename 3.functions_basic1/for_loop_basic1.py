for count in range(0,151):
    print(count)



for count in range(5,1000001):
    if(count % 5 == 0):
        print(count)



for count in range(1,101):
    if(count % 10 == 0):
        print("Coding Dojo")
    elif(count % 5 == 0):
        print("Coding")
    else:
        print(count)



total = 0
for count in range(0, 500001):
    if(count % 2 != 0):
        total += count
print(total)



for count in range(2018, 0, -4):
    print(count)


def multiples(lowNum, highNum, mult):
    for count in range(lowNum, highNum + 1):
        if(count % mult == 0):
            print(count)


#Each number would be on successive lines, I just put commas to make it easier
# 1. Output: 3, 5, 1, 2

# 2. I don't think this would work because list has 4 parameters and range only accepts 3 maximum

# 3. Output: 0, 1, 2, 3