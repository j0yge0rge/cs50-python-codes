x = input("camelcase:")
snake_case = ""

for char in x:
    if char.isupper():
        snake_case = snake_case + "_" + char.lower()
    else:
        snake_case = snake_case + char

print("sake_case:", snake_case)
