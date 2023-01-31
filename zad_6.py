def listy(a: list, b: list) -> list:
    lista = a + b
    return [element ** 3 for element in list(set(lista))]


print(listy([1, 2, 8, 4], [5, 4, 6, 9]))
