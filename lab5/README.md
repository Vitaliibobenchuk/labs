number_dict = { "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine" }

print("Привіт! Я перетворюю номер у словесне представлення.")

number = input("Будь ласка, введіть номер: ")

if not number.isdigit(): print("Ви ввели неправильний номер.") else: # Перетворюємо номер на словесне представлення word_number = "" for digit in number: word_number += number_dict[digit] + " "

print("Ваш номер у словесному представленні: ", word_number)
![photo_5390884444627388285_y](https://user-images.githubusercontent.com/129844781/236915984-351a8749-9b53-4c4e-8c74-192dc3797a2d.jpg)
