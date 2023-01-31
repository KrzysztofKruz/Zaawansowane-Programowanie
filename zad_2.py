class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Biblioteka znajduje się w {self.city}, na ulicy {self.street}, z kodem pocztowym {self.zip_code}, ' \
               f'dostępne w godzinach: {self.open_hours}. Telefon: {self.phone}'


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Pracownik biblioteki nazywa się {self.first_name} {self.last_name}. Urodził się {self.birth_date} ' \
               f'i zaczął pracować w bibliotece {self.hire_date}. Mieszka w {self.city}, na ulicy {self.street}, ' \
               f'z kodem pocztowym {self.zip_code}. Telefon: {self.phone}'


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Książka znajsuję się w {self.library}, została wydana w {self.publication_date}, przez ' \
               f'{self.author_name} {self.author_surname} i składa się z {self.number_of_pages} stron'


class Order:
    def __init__(self, employee, student, books: List[Book], order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Zamówienie zostało zrobione przez {self.student} i przydzielone {self.employee} na książki' \
               f' {self.books} dnia {self.order_date}'


Biblioteka1 = Library("Katowice", "3 Maja 50", "40-097", "Od 7:00 do 21:00", "782-293-121")
Biblioteka2 = Library("Sosnowiec", "Sokołów 24", "41-200", "Od 8:00 do 22:00", "252-435-567")
Książka1 = Book("Biblioteka1", 15-11-1999, "Michael", "Śmiszny", 256)
Książka2 = Book("Biblioteka2", 31-5-2012, "Albert", "Batman", 176)
Książka3 = Book("Biblioteka2", 5-11-1959, "Tomasz", "Misek", 293)
Książka4 = Book("Biblioteka1", 25-4-2001, "Krzysztof", "Jankowski", 196)
Książka5 = Book("Biblioteka2", 12-2-2011, "Aleksandra", "Michalińska", 356)
Pracownik1 = Employee("Eligiusz", "Jankowski", 8-7-2012, 12-4-1997, "Katowice", "Piłsudzkiego","40-097", "124-543-136")
Pracownik2 = Employee("Angelina", "Jęczak", 16-1-2010, 2-9-1999, "Sosnowiec", "Kukułek","41-200", "421-902-546")
Pracownik3 = Employee("Kalpurnia", "Ślązak", 9-12-2009, 12-4-1989, "Mysłowice", "Wolności","40-357", "975-003-179")
Zamówienie1 = Order(Pracownik1, Student2, [Książka2, Książka4, Książka5], 7-10-2022)
Zamówienie2 = Order(Pracownik3, Student3, [Książka1, Książka3], 16-9-2022)
