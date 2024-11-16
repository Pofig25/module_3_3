def print_params(a = 1, b = 'строка', c = True): # Создайте функцию print_params(a = 1, b = 'строка', c = True)
    print(a, b, c)                              # Функция должна выводить эти параметры.
print_params()                                  # Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params(b = 'Urban')
print_params(4, 'обзац')
print_params(5, 'параграф', False)
print_params(b = 25, c = [1, 2, 3])             # Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print('')                                       # печать пустой строки для разделения блоков в отображении результатов

values_list = [6, 'глава', False]                # Создайте список values_list с тремя элементами разных типов.
values_dict = {'a': 7, 'b': 'раздел', 'c': True} # Создайте словарь values_dict с тремя ключами,
                                                 # соответствующими параметрам функции print_params, и значениями разных типов.
print_params(*values_list)                       # Передайте values_list и values_dict в функцию print_params,
print_params(**values_dict)                      # используя распаковку параметров (* для списка и ** для словаря).
print('')                                        # печать пустой строки для разделения блоков в отображении результатов

values_list_2 = [54.32, 'Строка' ]               # Создайте список values_list_2 с двумя элементами разных типов
print_params(*values_list_2, 42)              # Проверьте, работает ли print_params(*values_list_2, 42)
