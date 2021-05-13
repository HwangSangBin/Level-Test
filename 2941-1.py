croatia_words = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

words = input()

for i in croatia_words:
    words = words.replace(i, "a")
print(len(words))