def count_frequency(numbers):
    count = {}
    for i in numbers:
        if(i in count):
            count[i] += 1
        else:
            count[i] = 1
    return count
numbers= ["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]
print(count_frequency(numbers))
