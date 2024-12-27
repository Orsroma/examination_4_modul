# # #- Практика:
# #
# #     <aside>
# #     🍄
# #
# #     В папке **`integer`**создайте файл `int_conversion.py`
# #
# #     ---
# #
# #     ### Описание темы: Преобразование типов — функция `int()`
# #
# #     Функция `int()` используется для преобразования значений в целочисленный тип. Она принимает на вход строку, дробное число или любое значение, которое может быть преобразовано в целое число, и возвращает целое числ
# #
# #     ---
# #
# #     ### Задания:
# #
# #     ### Задание #1
# #
# #     Создайте переменную `float_num` со значением `12.99`.
# #
# #     1. Примените к `float_num` функцию `int()` и сохраните результат в переменную `int_num`. Проверьте результат, выведя его на экран.
# #     2. Обратите внимание, как дробная часть числа обрабатывается функцией `int()`.
float_num = 12.99
int_num = int(float_num)

print(int_num)
#
# #
# #     ### Задание #2
# #
# #     Создайте переменную `string_num` со значением `"45"` (строковый тип).
# #
# #     1. Преобразуйте `string_num` в целое число, используя функцию `int()`, и сохраните результат в переменную `converted_num`.
# #     2. Проверьте тип переменной `converted_num`, чтобы убедиться, что она теперь целочисленного типа.
string_num = "45"

converted_num = int(string_num)
print(converted_num)
#
#
# #
# #     ### Задание #3
# #
# #     Создайте переменную `invalid_string` со значением `"hello123"`.
# #
# #     1. Попробуйте преобразовать `invalid_string` в целое число с помощью функции `int()`.
# #     2. Обратите внимание на возникшую ошибку и подумайте, почему Python не может преобразовать это значение в целое число.
#
invalid_string = "23"

baba = int(invalid_string)

print(baba)
#
# #- Практика:
#
#     <aside>
#     🍄
#
#     В папке `Data types` —>**`integer`**создайте файл `int_conversion.py`
#
#     ---
#
#     **Описание темы:** Абсолютное значение — функция `abs()`
#
#     Функция `abs()` возвращает абсолютное значение числа, то есть положительное значение величины независимо от знака. Это полезно, если нужно узнать расстояние от числа до нуля, не учитывая направление.
#
#     Пример:
#
#     ```python
#
#     number = -10
#     positive_number = abs(number)
#     print(positive_number)  # Выведет: 10
#
#     ```
#
#     ---
#
#     ### Задания:
#
#     ### **Задание #1**
#
#     Создайте переменную `num1` со значением `-56`.
#
#     1. Примените функцию `abs()` к `num1`, чтобы получить его абсолютное значение. Сохраните результат в переменную `abs_num1`.
#     2. Выведите `abs_num1` на экран.

num1 = -56
abs_num1 = num1.__abs__()

print(abs_num1)

#     ### **Задание #2**
#
#     Создайте переменную `num2` со значением `-4.8`.

num2 = -4.8
abs_num2 = abs(num2)

print(abs_num2)

#     1. Примените функцию `abs()` к `num2` и сохраните результат в переменную `abs_num2`.
#     2. Проверьте результат, выведя `abs_num2` на экран, и убедитесь, что значение положительное.
#     </aside>

num = 10
while num > 0:
    print(num)
    num -= 1
print("Счёт завершён!")
