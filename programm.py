def many_elements(massive):
    """Проверка на несколько одинаковых экземпляров"""
    ans = []
    for element in range(0,len(massive)):
        if massive.count(massive[element]) > 1 and massive[element] not in ans:
            ans.append(massive[element])
    print(ans)


def check_int_array(arr):
    return all(isinstance(x, int) for x in arr)

def main():
    """Меню"""
    while True:
        menu_variable = input(
            "\nДобро пожаловать в меню,что вы хотите сделать?:\n"
            "1. Ввести массив A\n"
            "2. Ввести массив B\n"
            "3. Выход из меню\n"
            "Напишите цифру действия: "
        )
        match menu_variable:
            case "1":
                try:
                    masive_first = map(int, input().split())
                    check_int_array(masive_first)
                except ValueError:
                    print("Элементы должны быть целыми числами")
            case "2":
                print(222)
            case "3":
                break

            case _:
                print("Номера такого действия нет в меню")


if __name__ == "__main__":
    main()
