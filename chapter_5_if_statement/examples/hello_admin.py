user_names= ['admin','orden','michael','florence','eli']
for user_name in user_names:
    if user_name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user_name}, thank you for logging in again.")



user_names = []

if user_names:
    for user in user_names:
        print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")

print("Removing all users from the list...")




current_users= ['admin', 'azeem', 'Ali', 'omar', 'Hassan']
new_users = ['michael', 'florence', 'eli', 'azeem', 'omar']

current_users_lower =[]

for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} is already taken. Please choose a different username.")
    else:
        print(f"{new_user} is available.")


numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")






