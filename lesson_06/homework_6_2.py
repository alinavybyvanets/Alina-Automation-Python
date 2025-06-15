while True:
    world = input("Введіть слово, яке містить літеру h/H:")
    if 'h' in world or 'H' in world:
        print("Слово містить літеру h/H")
        break
    else:
        print("Слово не містить літеру h/H. Спробуйте ще раз")


