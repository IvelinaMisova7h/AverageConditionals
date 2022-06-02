product = input()
day = input()
quantity = float(input())
result = 0

if day == 'Saturday' or day == 'Sunday':
    if product == 'banana':
        result = quantity * 2.70
    elif product == 'apple':
        result = quantity * 1.25
    #TODO
else:
    if product == 'banana':
        result = quantity * 2.50
    elif product == 'apple':
        result = quantity * 1.20
    #TODO

print(result)
