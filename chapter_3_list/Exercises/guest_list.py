guest_list=['Alice', 'Bob', 'Charlie']
message=f"Dear {guest_list[0]}, yor are invited to dinner."
print(message)
message=f"Dear {guest_list[1]}, yor are invited to dinner."
print(message)
message=f"Dear {guest_list[2]}, yor are invited to dinner."
print(message)

print("-------------------------")

guest_list=['Alice', 'Bob', 'Charlie']
print(guest_list)


uninvited_guest=guest_list.pop(1)
print(f"Sorry {uninvited_guest}, you are uninvited to dinner.")

new_guest='David'
guest_list.insert(1,new_guest)
print(guest_list)

message=f"Dear {guest_list[1]}, you are invited to dinner."
print(message)
print("------------------------")

one_more_guest='Eve'
guest_list.insert(0,one_more_guest)
print(guest_list)

one_more_guest= 'Frank'
guest_list.insert(2,one_more_guest)
print(guest_list)

one_more_guest='Grace'
guest_list.append(one_more_guest)
print(guest_list)

message=f"You are invited to dinner, {guest_list[1]} and {guest_list[3]}"
print(message)

message=pop_guest=guest_list.pop(0)
print(f"Sorry {pop_guest}, you are uninvited to dinner.")