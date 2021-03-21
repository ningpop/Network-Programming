days = {
    'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30,
    'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31
}

print(days[input('월 입력: ')])
print()

for month in sorted(days):
    print(month)
print()

for month, day in days.items():
    if day == 31:
        print(month)
print()

temp = sorted(days.items(), key=lambda x:x[1])
for month, day in temp:
    print(month, '-', day)
print()

month_name = input('월 3자리 입력: ')
for month, day in days.items():
    if month_name == month[:3]:
        print(day)