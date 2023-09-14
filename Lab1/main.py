a = int(input ("Введіть а: "))

while (a < 1 or a > 100):

    a = int(input ("Спройбуйте ще раз, введіть а: "))

b = int(input ("Введіть b: "))

while (b < 1 or b > 100):

    b = int(input ("Спройбуйте ще раз, введіть b: "))


if a > b:

    r = (a*b-3)

elif a == b:

    r = 2

else:

    r = (a*a*a + 1) / b

print("Результат виразу: " , r)
