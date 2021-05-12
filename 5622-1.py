words = input()

alpabet_list = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
times = 0

for i in range(len(words)):
    for alpabet in alpabet_list:
        if (words[i] in alpabet):
            times += alpabet_list.index(alpabet) + 3
print(times)