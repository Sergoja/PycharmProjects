def get_grade(grade):
    if grade == 2:
        print("Плохо")
    elif grade == 3:
        print("Удовлетворительно")
    elif grade == 4:
        print("Хорошо")
    elif grade == 5:
        print("Отлично")
    else:
        print("Ошибка")

# try:
#     assert get_grade(2) == "Плохо"
#     assert get_grade(3) == "Удовлетворительно"
#     assert get_grade(4) == "Хорошо"
#     assert get_grade(5) == "Отлично"
#     assert get_grade("") == "Ошибка"
# except AssertionError:
#     print("Неверно, проверьте функцию на разных значениях")
# else:
# 
