x, y = map(int, input('두 수 입력 : ').split())

if x > y:
    big = x
    small = y
else:
    big = y
    small = x

while True:
    temp = big % small
    big = small
    small = temp

    if small == 0:
        break

print(f'최대공약수: {big}')