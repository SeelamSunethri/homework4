number1 = [2,7,11,15]
target1 = 9
number2 = [3,2,4]
target2 = 6
number3 = [3,3]
target3 = 6
def targetsum(x,y):
    index_map = {}
    for index, number in enumerate(x):
        if y-number in index_map:
            return index_map[y - number], index
        index_map[number] = index
print(targetsum(number1,target1))
print(targetsum(number2,target2))
print(targetsum(number3,target3))
