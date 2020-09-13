Alpa = input().upper()
biggest = 0
a = 0

for j in range(26):
    total = Alpa.count(chr(65 + j))

    if total > biggest:
        biggest = total
        biggest_Alpa = chr(65 + j)

    elif total == biggest:
        a = biggest

if a == biggest:
    print("?")

else:
    print(biggest_Alpa)