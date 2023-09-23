from mod import y         #main.py
n = int(input("Введіть натуральне число n: "))
while n < 1:
   n = int(input("n повинно бути натуральним числом. "))

result = у(n)
print(f"Результат обчислення у = 1*3*5*...(2*{n}-1) = {result}")


  def у(n):   #mod.py
    y = 1
    for i in range(1, 2 * n, 2):
        y *= i
    return y
