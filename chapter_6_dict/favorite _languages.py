favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }


language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")



favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }


for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite laguage is {language.title()}.")



favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }


for name in favorite_languages.keys():
    print(name.title())


favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }


friends= ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}")


if name in friends:
    language= favorite_languages[name].title()
    print(f"\t{name.title()}, i see you love {language}")

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }


if 'erin' not in favorite_languages.keys():
    print("erin, please take our pool!")


favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()} thank you for taking the pool")




favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }


print("The following languages has been mentioned")

for language in favorite_languages.values():
    print(language.title())



favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }


print("The following languages has been mentioned")

for language in set(favorite_languages.values()):
      print(language.title())