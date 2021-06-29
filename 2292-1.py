room = int(input())

floor = 1
count = 1

while room > count:
    count += 6 * floor
    floor += 1
print(floor)