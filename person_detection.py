import cv2
image = cv2.imread('Zdjecia/Ludzie1.jpg')
image = cv2.resize(image,(300,300))

Czy_czlowiek = cv2.HOGDescriptor()
# To jest: Histogram zorientowanych gradientów
Czy_czlowiek .setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# Ustawiam wspolczynniki dla liniowego klasyfikatora SVM (wprowadzam wspolczynniki klasyfikatora przeszkolonego do wykrywania osob)
(czlowiek, _) = Czy_czlowiek.detectMultiScale(image, winStride = (3,3), padding = (3,3), scale = 1.01)
# Wykrywam obiekty o różnych rozmiarach na obrazie wejściowym. Wykryte obiekty są zwracane jako lista prostokątów

for (x, y, w, h) in czlowiek:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
# Rysuje prostokat na obrazie (image, start_point, end_pointcolor, thickness)
cv2.imshow('Czy_czlowiek', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Liczba ludzi: {len(czlowiek)}")
