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

massive_a = [10, 20, 30, 30]
massive_b = [20, 30, 40]

element_a_in_b(massive_a, massive_b)
print(element_a_in_b(massive_a, massive_b))