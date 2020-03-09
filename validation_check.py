# Проверка валидности расстановки скобочек в выражении.
# Алгоритм программы следующий:
# В функцию go_list передаем элемент списка созданного из строки и проверяем является ли скобка открывающей или закрывающей.
# Если скобка открывающая ищем соответствующую ей закрывающую и соединяем два символа.
# Результат заносим в контрольный список.
# Аналогично поступаем если скобка закрывающая.
# Функция go_list возвращает соотвествующий элемент если нашла его в списке созданном из строки,
# в противном случае просто вносит символ в контрольный список.
# Функция change_pattern_list принимает открывающий или закрывающий элемент и заменяет его в списке созданном из строки
# на символ '-'. Это реализованно для отсутствия повторений, далее функция возращает модифицированный список.
# После проверки каждого символа модифицируем контрольный список убирая из него все символы '-'.
# Функция check_all проверяет модифицированный контрольный список, преобразуя его в множество.
# Если расстановка скобок валидная то элемент в модифицированном множестве будет найден в контрольном множестве.
# Например:
# -при вводе ([]) модифицированное множество будет иметь вид: ()[] = true.
# -при вводе {[(]} модифицированное множество будет иметь вид: {}[]( = false.


def go_list(sym=''):
    if sym in list_front:
        i = list_front.index(sym)
        if list_back[i] in pattern_list:
            test_list.append(sym + list_back[i])
        else:
            test_list.append(sym)
        return list_back[i]
    elif sym in list_back:
        i = list_back.index(sym)
        if list_front[i] in pattern_list:
            test_list.append(sym + list_front[i])
        else:
            test_list.append(sym)
        return list_front[i]
    else:
        test_list.append(sym)


def change_pattern_list(pattern_list, sym_change):
    for i in range(len(pattern_list)):
        if pattern_list[i] == sym_change:
            pattern_list[i] = '-'
            break
        else:
            continue
    return pattern_list


def check_all(test_list=[], set_control=set()):
    test_list = set(test_list)
    for element in test_list:
        if element not in set_control:
            print('false')
            return False
        else:
            continue
    return True


if __name__=='__main__':
    pattern = input('Введите последовательность скобок: ').strip()           # Вводим выражение для проверки.
    list_front = ['{', '(', '[']                                             # Список открывающих элементов.
    list_back = ['}', ')', ']']                                              # Список закрывающих элементов.
    set_control = {'{}', '[]', '()'}                                         # Контрольное множество.
    pattern_list = [sym for sym in pattern]                                  # Создаем список из строки.
    test_list = []
    for sym in pattern_list:
        sym_change = go_list(sym)                                            # Проверяем каждый символ.
        pattern_list = change_pattern_list(pattern_list, sym_change)         # Модифицируем список заменяя элементы.
    test_list = [sym for sym in test_list if sym != '-']
    if check_all(test_list, set_control):                                    # проверяем валидность строки
        print('true')                                                        # если расстановка валидная выводим 'true'.







