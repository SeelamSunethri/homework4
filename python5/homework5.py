def my_range(*args):
    if len(args)==1:
        start, end, step = 0, args[0], 1
    elif len(args)==2:
        start, end, step = args[0], args[1], 1
    else:
        start, end, step = args[0], arg[1], args[2]
    while True:
        if step> 0 and start >= end:
            break
        elif step <0 and start <= end:
            break
        yield('%g'%start)
        start=start+step
for i in my_range(3,9,1):
    print(i)