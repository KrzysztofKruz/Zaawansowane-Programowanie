def czyParzysta(liczba: int) -> bool:
    if liczba % 2 == 0:
        return True

    else:
        return False


wynik = czyParzysta(7)
if wynik:
    print('Liczba parzysta')
else:
    print('Liczba nieparzysta')
