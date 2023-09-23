rechennya = input("Введіть речення: ")

okremy_slova = rechennya.split()  # Розбиваємо речення на слова

print("Слова, відмінні від 'привіт':")

for i in okremy_slova:
    if i != 'привіт':
        print(i)
