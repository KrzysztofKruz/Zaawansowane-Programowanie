def liczby_a(listaLiczb):
    liczby = []
    for liczba in listaLiczb:
        liczby.append(liczba * 2)
    return liczby


def liczby_b(listaLiczb):
    liczby = [liczby * 2 for liczby in listaLiczb]
    return liczby
