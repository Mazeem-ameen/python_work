person_name="Eric"
print(f"Hello {person_name}, would you like to learn some python today?")



person_name="Eric"
print(person_name.lower())
print(person_name.upper())
print(person_name.title())


famous_person="Albert Einstein"
message=f"{famous_person} once said, 'A person who never made a mistake never tried anything new.'"
print(message)

print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')


person_name="\t\n  add loveave   \n\t"
print("original name with whitespace")
print(person_name)
print("------")
print("using lstrip()")
print(person_name.lstrip())
print("------")
print("using rstrip()")
print("------")
print("using rstrip()")
print(person_name.rstrip())
print("------")
print("using strip()")
print(person_name.strip())

filename= 'python_notes.txt' 
clean_filename=filename.removesuffix('.txt')

print(clean_filename)


print(5+3)
print(10-2)
print(2*4)
print(16//2)

favorite_number=5
message=f"My favorite number is {favorite_number}."
print(message)