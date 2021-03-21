str = 'led=on&motor=off&switch=off'

temp = str.split('&')
result = {}
for i in temp:
    key, value = i.split('=')
    result[key] = value
print(result)