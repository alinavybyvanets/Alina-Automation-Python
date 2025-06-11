from enum import unique

i = input(" Введіть символи")
unique = set(i)
result = len(unique) > 10
print(result)

