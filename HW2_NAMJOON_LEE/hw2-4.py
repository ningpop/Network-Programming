result = 0

for i in range(1, 1001):
    sum = 0
    for j in str(i):
        sum += int(j)
    result += sum

print(result)