alpabet = input()
count = len(alpabet)

count -= alpabet.count("c=")

count -= alpabet.count("c-")

count -= alpabet.count("dz=")

count -= alpabet.count("d-")

count -= alpabet.count("lj")

count -= alpabet.count("nj")

count -= alpabet.count("s=")

count -= alpabet.count("z=")

print(count)