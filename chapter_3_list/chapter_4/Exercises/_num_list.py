for value in range (1,21):
    print(value)


numbers = list(range(1, 1000001))
print(numbers)

print("\n-------------\n")
numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

multiples_of_3 = list(range(3, 31, 3))
print(multiples_of_3)

print("\n--------------------\n")

cubes=[]

for value in range(1,11):
    cube=value**3
    cubes.append(cube)

for cube in cubes:
    print(cube)

print("\n----------------------\n")


cubes =[value**3 for value in range(1,11)]

for cube in cubes:
    print(cube)