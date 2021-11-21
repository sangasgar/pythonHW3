#Урок 3
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#1
a = int(input("Введите число 1 "))
b = int(input("Введите число 2 "))

def division_func(a, b):
    return a/b
try:
    print(f"a / b = {division_func(a, b)}")
except ZeroDivisionError as ZD:
     print(ZD)
#2
name = input("Ваше имя ")
surname = input("Ваша фамилия ")
birth_year= input("Год рождения ")
city_of_residence = input("Город проживания ")
email = input("email ")
phone = input("Ваш телефон ")
def info_func(name = "name", surname = "surname", birth_year = "birth_year", city_of_residence = "city_of_residence", email = "email", phone = "phone"):
    print(f"Ваше имя {name}, ваша фамилия  {surname},год рождения  {birth_year}, город проживания  {city_of_residence}, email {email}, ваш телефон {phone}")
info_func(name=name, surname=surname, birth_year=birth_year, city_of_residence = city_of_residence, email=email, phone=phone)
#3

def sum_2_max(a: int, b: int, c: int):
    total = 0
    if a < b and a < c:
        total = b + c
    elif b < a and b < c:
        total = a + c
    elif c < a and c < b:
        total = a + b
    return total
print(sum_2_max(2, 5, 8))

#4

def degree(x: int, y: int):
    return x ** y
def degre1(x: int, y: int):
        с_y = abs(y)
        for i in range(с_y//2):
            x = x * x
        total = 1/x
        return total

print(degree(2, -4))
print(degre1(2, -4))

#5



total_num = 0

list_num = input("Введите числа через пробел или q для завершения работы ").split(" ")
def do(list_num, total_num):
    for i in list_num:
        if i != "q":
            total_num = total_num + int(i)
        else:
           break
    return total_num
total_num1 = do(list_num, total_num)
total_num2 = 0
while "q" not in list_num:
    list_num = input("Введите числа через пробел или q для завершения работы ").split(" ")
    for i in list_num:
        if i != "q":
            total_num2 = total_num2 + int(i)
        else:
            break
print(total_num1 + total_num2)

#6
text = input("Введите слово ")
def int_func(text):
    text_upper = text.capitalize()
    return text_upper
print(int_func(text))

text_list = input("Введите слова через пробелы ").split(" ")

def int_func1(text_list):
    text_finally = ""
    t = ""
    for i in text_list:
        t = str(i).capitalize()
        text_finally = text_finally + t + " "
    return text_finally


print(int_func1(text_list))