town = input()
s = float(input())
result = 0

if town == 'Sofia':
    if s >= 0 and s <= 500:
        result = s*0.05
    elif s > 500 and s <= 1000:
        result = s*0.07
    elif s > 1000 and s <= 10000:
        result = s*0.08
    elif s > 10000:
        result = s*0.12

elif town == 'Plovdiv':
    if s >= 0 and s <= 500:
        result = s*0.055
    elif s > 500 and s <= 1000:
        result = s*0.08
    elif s > 1000 and s <= 10000:
        result = s*0.12
    elif s > 10000:
        result = s*0.145

elif town == 'Varna':
    if s >= 0 and s <= 500:
        result = s*0.045
    elif s > 500 and s <= 1000:
        result = s*0.075
    elif s > 1000 and s <= 10000:
        result = s*0.1
    elif s > 10000:
        result = s*0.13


if result >= 0:
    print("%.2f" % result)
else:
    print('error')
