type_projection = input().lower()
rows = int(input())
cols = int(input())

income = 0.0
full = rows * cols

if type_projection == 'premiere':
    income = full * 12.00
elif type_projection == 'normal':
    income = full * 7.50
elif type_projection == 'discount':
    income = full * 5.00

print('%.2f leva' % income)
