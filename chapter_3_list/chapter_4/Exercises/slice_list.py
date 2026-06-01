my_list=['apple', 'banana', 'cherry', 'date', 'fig','grape','kiwi','mango','orange']
print(my_list[0:3])

print(my_list[3:6])
print(my_list[6:])


my_pizzas=['pepperoni', 'mushrooms', 'green peppers', 'extra cheese']
friend_pizzas=my_pizzas[:]

friend_pizzas.append('pineapple')
my_pizzas.append('olives')

print("My favorite pizzas are:")
print(my_pizzas)

print("\nMy friend's favorit pizzas are:")
print(friend_pizzas)

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f" {pizza.title()}")



print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f" {pizza.title()}")
