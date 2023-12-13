from PIL import Image, ImageDraw, ImageFont, ImageColor
import os

def create_greeting_card(background_option, background_value, text, image_path, output_path, text_color="white", text_size=36, font_path=None):
    # Ініціалізація змінної "card" за межами умовних операторів
    card = None

    if background_option == "color":
        # Створення порожнього зображення із вказаним кольором тла
        card = Image.new("RGB", (800, 600), background_value)
    elif background_option == "image":
        # Використання зображення як фону
        card = Image.open(background_value)
        card = card.resize((800, 600))  # Зміна розміру за потребою

    # Перевірка, чи змінна "card" не залишилась невизначеною
    if card is None:
        print("Помилка: Неможливо створити вітальну листівку.")
        return

    if image_path:
        img = Image.open(image_path)
        img = img.resize((250, 250))
        card.paste(img, (250, 0))

    draw = ImageDraw.Draw(card)
    font_path = "times.ttf"
    # Встановлення шрифту
    if font_path is None:
        # Використання стандартного шрифту, якщо шлях не вказано
        font = ImageFont.load_default()
    else:
        try:
            font = ImageFont.truetype(font_path, text_size)
        except OSError:
            print("Помилка: Неможливо завантажити шрифт.")
            return

    text_bbox = draw.textbbox((0, 0), text, font=font)
    x = (card.width - (text_bbox[2] - text_bbox[0])) // 2
    y = (card.height - (text_bbox[3] - text_bbox[1])) // 2
    draw.text((x, y), text, font=font, fill=text_color)

    card.save(output_path)
def main():
  print("Ласкаво просимо до Конструктора Вітальних Листівок!")

  # Вибір типу фону
  background_option = input("Оберіть тип фону ('color' або 'image'): ".encode('utf-8').decode('utf-8')).lower()

  while background_option not in ['color', 'image']:
      print("Невірний вибір фону. Оберіть 'color' або 'image'.")
      background_option = input("Оберіть тип фону ('color' або 'image'): ").lower()

  # Отримуємо введення користувача для налаштування листівки
  if background_option == 'color':
      while True:
          background_value = input("Введіть колір тла (наприклад, #RRGGBB): ")
          try:
              # Перевірка вірності введеного кольору тла
              ImageColor.getcolor(background_value, "RGB")
              break
          except ValueError:
              print("Невірний формат кольору тла. Будь ласка, використовуйте #RRGGBB.")
  else:
      while True:
          background_value = input("Введіть шлях до зображення: ")
          # Додайте додаткову перевірку шляху до зображення, якщо потрібно

          if os.path.isfile(background_value):
              break
          else:
              print("Файл не знайдено. Будь ласка, введіть правильний шлях до зображення.")

  text = input("Введіть текст вітання: ")

  while True:
      text_color = input("Введіть колір тексту (наприклад, #RRGGBB): ".encode('utf-8').decode('utf-8'))
      try:
          ImageColor.getcolor(text_color, "RGB")
          break
      except ValueError:
          print("Невірний формат кольору тексту. Будь ласка, використовуйте #RRGGBB.")

  while True:
      try:
          text_size = int(input("Введіть розмір тексту: "))
          break
      except ValueError:
          print("Невірний формат розміру тексту. Будь ласка, введіть ціле число.")

  image_path = input("Введіть шлях до зображення (залиште порожнім, якщо без зображення): ")

  while image_path and not os.path.isfile(image_path):
      print("Файл не знайдено. Будь ласка, введіть правильний шлях до зображення.")
      image_path = input("Введіть шлях до зображення (залиште порожнім, якщо без зображення): ")

  output_path = input("Введіть шлях для збереження вітальної листівки: ")

  # Створюємо вітальну листівку
  create_greeting_card(background_option, background_value, text, image_path, output_path, text_color, text_size)
  print(f"Вітальна листівка успішно створена за шляхом {output_path}")

if __name__ == "__main__":
  main()
