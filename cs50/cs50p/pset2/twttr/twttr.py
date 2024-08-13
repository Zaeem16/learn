user_input = input("Input: ")
for letter in user_input:
    if letter.lower() in [ 'a', 'e', 'i', 'o', 'u']:
        user_input = user_input.replace(letter, '')
print(user_input)
