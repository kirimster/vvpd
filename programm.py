def many_elements(massive):
    """Проверка на несколько одинаковых экземпляров"""
    ans = []

    for element in massive:
        if massive.count(element) > 1 and element not in ans:
            ans.append(element)

    return ans



def element_a_in_b(massive_a, massive_b):
    ans = many_elements(massive_a)
    ans_b = []

    for element in ans:
        if element in massive_b:
            ans_b.append(element)

    return ans_b



def check_int_array(arr):
    return all(isinstance(x, int) for x in arr)

def main():
    """Меню"""
    masive_first = []
    masive_second = []
    while True:
        menu_variable = input(
            "\nДобро пожаловать в меню,что вы хотите сделать?:\n"
            "1. Ввести массив A\n"
            "2. Ввести массив B\n"
            "3. Задание секции 1.2\n"
            "4. Задание секции 2.2\n"
            "5. Задание секции 2.2\n"
            "6. Выход из меню\n"
            "Напишите цифру действия: "
        )
        match menu_variable:
            case "1":
                try:
                    masive_first = list(map(int, input("Введите целые числовые элементы массива A").split()))
                    print(masive_first)
                    check_int_array(masive_first)
                except ValueError:
                    print("Элементы должны быть целыми числами!!")
            case "2":
                try:
                    masive_second = list(map(int, input("Введите целые числовые элементы массива B").split()))
                    check_int_array(masive_second)
                except ValueError:
                    print("Элементы должны быть целыми числами!!")
            case "4":
                print("повторяющиеся элементы массива А,"\
                    f"которые есть в массиве B: {element_a_in_b(masive_first, masive_second)}")
            case "6":
                break

            case _:
                print("Номера такого действия нет в меню")


if __name__ == "__main__":
    main()
