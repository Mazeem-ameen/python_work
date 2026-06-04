car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("Is car == 'Subaru'? I predict False.")
print(car == 'Subaru')


print("\nIs car.lower() == 'subaru'? I predict True. ")
print(car.lower() == 'subaru')


print("\nIs car == 'SUBARU'? I predict False.")
print(car == 'SUBARU')

print("\nIs car.lower() == 'SUBARU'? I predict False.")
print(car.lower() == 'SUBARU')


print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')


print("\n-------------------\n")

name = "Azeem"
age = 22
fruits = ['apple', 'banana', 'cherry']
print(name == "Azeem")

print(name != "Azeem")

print(name.lower() == "azeem")

print(name.lower() != "Ali")


print(age == 22)
print(age != 22)
print(age > 21)
print("_____________")

print(age > 21 and age >21)

print(age > 25 or age > 21)

print('apple' in fruits)

print('apple' not in fruits)


print("-----------------\n")
alien_color = 'green' , 'yellow' , 'red'

if alien_color == 'green':
    print("Player just earned 5 points.")

print("\n-------------------\n")
alien_color = 'red'

if alien_color == 'green':
    print("player just earned 5 points.")


print("==================")



alein_color = 'yellow'

if alein_color == 'green':
    print("player just earned 5 points.")
else:
    print("player just earned 10 points.")

print("\n------------------\n")

alien_color = 'green'

if alien_color == 'green':
    print("player just earned 5 points.")
elif alien_color == 'yellow':
    print("player just earned 10 points.")
else:
    print("player just earned 15 points.")


age = 2

if age < 2:
    print("The person is a baby.")
elif age >= 2 and age < 4:
    print("The person is a toddler.")
elif age >= 4 and age < 13:
    print("The person is a kid.")
elif age >= 13 and age < 20:
    print("The person is a teenager.")
elif age >= 20 and age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")


favorite_fruits = ['apple', 'banana', 'cherry']

if 'apple' in favorite_fruits:
    print("You really like apple!")
if 'banana' in favorite_fruits:
    print("You really like banana!")
if 'cherry' in favorite_fruits:
    print("You really like cherry!")
if 'orange' in favorite_fruits:
    print("You really like orange!")
if 'grape' in favorite_fruits:
    print("You really like grape!")

