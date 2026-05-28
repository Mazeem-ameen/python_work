visit_places=['Paris', 'Tokyo', 'New York', 'Sydney', 'Rome']
print("Original list of places:")
print(visit_places)

print("\nSorted list of places:")
print(sorted(visit_places))


visit_places=['Paris', 'Tokyo', 'New York', 'Sydney', 'Rome']

print("\nsorted list of places in reverse alphabetical order:")
visit_places.sort(reverse=True)
print(visit_places)

print("--------------------")
visit_places=['Paris', 'Tokyo', 'New York', 'Sydney', 'Rome']
print("Original list of places:")
print(visit_places)
print("\nRevese order of the order")
visit_places.reverse()
print(visit_places)

print("\nReverse the original order again:")
visit_places.reverse()
print(visit_places)

print("\nsorted alphabetically:")
print(sorted(visit_places))
print("\nAgain alphabetically sorted list:")
print(sorted(visit_places, reverse=True))


guest_list=['Alice', 'Bob']
print(len(guest_list))

colors=['red' , 'green', 'blue']
#print(colors[5])

print(colors[1])

print("-------------------")
countries = ['Pakistan', 'Turkey', 'Japan', 'Canada', 'Germany']
#original list:
print("original list:")
print(countries)
#sorted list:
print("\nsorted list:")
print(sorted(countries))
#orginal list again:
print("\noriginal list again:")
print(countries)
#using reverse:
countries.reverse()
print("\nReversed list:")
print(countries)

#reverse again:
print("\nReversed again:")
countries.reverse()
print(countries)
#using sort:
countries.sort()
print("\nparmanently sorted:\n")
print(countries)
#using sort reverse:
countries.sort(reverse=True)
print("\nReverse alphabetically sorted list:\n")
print(countries)

#using len
print("\n Number of countries\n")
print(len(countries))


#using append
countries.append('France')
print("\nAdded new country:\n")
print(countries)

#using insert
countries.insert(2,'Italy')
print("\nAdded new country at index\n")
print(countries)

#using del
del countries[3]
print("\nafter deleting country at index\n")
print(countries)

#using pop
popped_country=countries.pop(4)
print("\nafter popping country at index\n")
print(popped_country)

print("\nFinal list\n")
print(countries)

