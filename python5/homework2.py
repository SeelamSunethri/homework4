def bunnyears2(y):
    if y == 0:
        return 0
        if y%2 == 0:
            return 3+bunnyears2(y-1)
        else:
            return bunnyears2(y-1)+2
print('bunnyears2(0)->',bunnyears2(0))
print('bunnyears2(1)->',bunnyears2(1))
print('bunnyears2(2)->',bunnyears2(5))
