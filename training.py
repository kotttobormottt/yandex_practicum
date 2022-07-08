print("Вычислим сколько дней, минут и секунд Вы живёте:")
name = input("Ваше имя: ")
print("Введите свой возраст: ")
age = int(input("Возраст: "))
days = age * 365
minutes = age * 525948
seconds = age * 31556926
print(f"{name} прожил(а) {days} дней {minutes} минут и {seconds} секунд!")