for i in range(1, 21, 2):
    print(i, end=' ')
print()

for x in range(0, 101, 10):
    print(x, end=' ')
print()

for y in range(20, 0, -1):
    print(y, end=' ')
print()

number_of_stars = int(input("Number of stars: "))
for z in range(0, number_of_stars):
    print("*", end='')
print()

for a in range(1, number_of_stars + 1):
    print()
    for b in range(0, a):
        print("*", end='')
print()
