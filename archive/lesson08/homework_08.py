def massiv_stroc(stroca):
    try:
        st = stroca.split(",")
        numbers = [int(x) for x in st]
        return sum(numbers)
    except ValueError:
        return("Не можу це зробити!")
user_input = input("Введіть кілька рядків з числами через кому, рядки розділіть  крапкою з комою(;) - наприклад: 1,2,3; 3,4,5,5; 4,6,4,6,4,6:")
lines = user_input.split(";")
for line in lines:
    line = line.strip()
    result = massiv_stroc(line)
    print(result)