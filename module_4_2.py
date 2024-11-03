def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()   #  Вызов внутри функции. Ошибки нет, но текст не выводится, т.к. inner-function существует только внутри функции test_function().
#inner_function()   # Вызов вне функции. Ошибка т.к.inner-function существует только внутри функции test_function().
test_function()   # Все успешно работает, т.к. функция inner_function() находится в области видимости функции test_function().