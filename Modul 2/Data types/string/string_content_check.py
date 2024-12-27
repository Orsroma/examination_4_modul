# #### Практика
#
#
# 🍄
#
# В папке `string`  создайте файл `string_content_check.py`
#
# ---
#
# ### **Описание темы: Проверка содержимого строки**
#
# Python предоставляет методы для проверки, содержит ли строка определённые символы, слова или соответствует ли определённым условиям. Эти методы помогают понять, что находится внутри строки и позволяют строить логику в зависимости от её содержимого.
#
# **Основные методы:**
#
# - `in` оператор: проверяет наличие подстроки в строке.
# - `startswith()`: проверяет, начинается ли строка с определённой подстроки.
# - `endswith()`: проверяет, заканчивается ли строка на определённую подстроку.
# - `isdigit()`: проверяет, состоит ли строка только из цифр.
# - `isalnum()`: проверяет, состоит ли строка только из букв и цифр.
# - `isspace()`: проверяет, состоит ли строка только из пробелов.
# - Задание#6
#     - Создайте переменную `phrase` со значением `"The quick brown fox jumps over the lazy dog"`.
#     - Проверьте, содержит ли `phrase` слово `"fox"`, используя оператор `in`. Сохраните результат в переменную `contains_fox`. Проверьте результат.
phrase = "The quick brown fox jumps over the lazy dog"
contains_fox = phrase in "fox"

print(contains_fox)


# Создаём переменную phrase
phrase = "The quick brown fox jumps over the lazy dog"

# Проверяем, содержит ли phrase слово "fox"
contains_fox = "fox" in phrase

# Выводим результат
print(contains_fox)



# - Задание#6.1
#     - Создайте переменную `greeting` со значением `"Hello, world!"`.
#     - Используйте метод `startswith()` для проверки, начинается ли `greeting` с `"Hello"`. Сохраните результат в переменную `starts_with_hello`. Проверьте результат.
#     - Используйте метод `endswith()` для проверки, заканчивается ли `greeting` на `"world!"`. Сохраните результат в переменную `ends_with_world`. Проверьте результат.
greeting = "Hello, world!"
starts_with_hello = greeting.startswith("Hello")
ends_with_world = greeting.endswith("world!")

print(starts_with_hello)
print(ends_with_world)
# - Задание#6.2
#     - Создайте переменную `text` со значением `"12345"`.
#     - Проверьте, состоит ли `text` только из цифр, используя метод `isdigit()`. Сохраните результат в переменную `is_digits`. Проверьте результат.
#     - Измените значение `text` на `"abc123"`. Проверьте `is_digits` ещё раз, чтобы увидеть, что изменилось.

text = "abc123"
is_digits = text.isdigit()
print(is_digits)

# - Задание#6.3
#     - Создайте переменную `mixed_text` со значением `"Hello123"`.
#     - Используйте метод `isalnum()` для проверки, состоит ли `mixed_text` только из букв и цифр (без пробелов или специальных символов). Сохраните результат в переменную `is_alphanumeric`. Проверьте результат.
mixed_text = "Hello123"
kek = mixed_text.isalnum()
print(kek)

# - Задание#6.4
#     - Создайте переменную `whitespace_text` со значением `" "`.
#     - Проверьте, состоит ли `whitespace_text` только из пробелов, используя метод `isspace()`. Сохраните результат в переменную `is_space`. Проверьте результат.
#

whitespace_text = " "
l2l2 = whitespace_text.isspace()
print(l2l2)