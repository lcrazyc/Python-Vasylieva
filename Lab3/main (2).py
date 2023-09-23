def rizni_symvolu(slovo):
    symvolu = set(slovo)  # Перетворюємо слово в множину для визначення унікальних символів
    return len(symvolu)

slovo = input("Введіть слово: ")
result = rizni_symvolu(slovo)

print("Кількість різних символів у слові:", result)
