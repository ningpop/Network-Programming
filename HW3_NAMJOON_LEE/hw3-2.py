d = [
    {'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
    {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
    {'name':'Princess', 'phone':'555-3141', 'email':''},
    {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}
]

for i in d:
    if i['phone'][-1] == '8':
        print(i['name'])
print()

for i in d:
    if i['email'] == '':
        print(i['name'])
print()

name = input('사용자 이름 입력: ')
result = False
for i in d:
    if i['name'] == name:
        print(i['phone'], i['email'])
        result = True
if result == False:
    print('이름이 없습니다.')
