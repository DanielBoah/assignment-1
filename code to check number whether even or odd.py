def number_checker(start,end):
    for num in range(start,end+1):
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")
print(number_checker(10,30))           