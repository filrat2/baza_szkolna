# -*- coding: utf-8 -*-

# define global variables
SUBJECTS = ("język polski", "polski", "język niemiecki", "niemiecki",
            "angielski", "język angielski", "matematyka",  "biologia",
            "chemia", "historia", "muzyka", "technika", "plastyka",
            "wf", "wychowanie fizyczne", "wos", "fizyka", "informatyka",
            "religia", "etyka", "geografia")

students = []
tutors = []
class_tutors = []
classes = set()

# define classes

# %% ClassTutor


class ClassTutor:

    def __init__(self):
        self.name = ""
        self.school_class = ""

    def __repr__(self):
        return self.name

    def set_attrs(self):

        while True:
            school_class = input("Podaj oznaczenie klasy: ")
            school_class = ''.join(filter(str.isalnum, school_class)).upper()

            if 1 <= len(school_class) <= 2:
                if len(school_class) == 1:
                    if school_class[0].isnumeric() is False:
                        print("Jednoznakowe oznaczenie klasy musi być cyfrą.")
                        pass
                    else:
                        break
                elif len(school_class) == 2:
                    if (school_class[0].isnumeric() is False or
                            school_class[1].isalpha() is False):
                        print("Dwuznakowe oznaczenie klasy musi być w formacie"
                              " cyfry z literą np. '2A'.")
                        pass
                    else:
                        break
            else:
                print("Oznaczenie klasy musi być w formacie samej liczby "
                      "np. '2' lub liczby z literą np. '2A'.")
                pass

        name = input("Podaj imię i nazwisko wychowawcy "
                     f"klasy {school_class}: ")
        name = name.title()

        self.name = name
        self.school_class = school_class

# %% Tutor


class Tutor:

    def __init__(self):
        self.name = ""
        self.subjects = []
        self.classes = []

    def __repr__(self):
        return self.name

    def set_attrs(self):

        global SUBJECTS

        tutor_subjects = []
        classes = []

        name = input("Podaj imię i nazwisko nauczyciela: ")
        name = name.title()

        while True:
            print("/aby zakończyć wprowadzanie przedmiotów wpisz 'exit'/")
            subject = input("Wprowadź nazwy przedmiotów szkolnych, "
                            f"które prowadzi nauczyciel {name}: ")
            subject = subject.lower()

            if subject == "exit":
                break
            elif subject == "przedmioty":
                print("Dostępne przedmioty:\n"
                      f"{', '.join(SUBJECTS)}")
            elif subject not in SUBJECTS:
                print("Brak przedmiotu na liście dostępnych przedmiotów.\n"
                      "/aby wyświetlić listę dostępnych przedmitów wpisz "
                      "'przedmioty'/")
                pass
            else:
                tutor_subjects.append(subject)

        while True:
            print("/aby zakończyć wprowadzanie klas wpisz 'exit'/")
            class_id = input("Wprowadź oznaczenia klas, "
                             f"które uczy nauczyciel {name}: ")
            class_id = ''.join(filter(str.isalnum, class_id)).upper()

            if class_id == "EXIT":
                break
            elif 1 <= len(class_id) <= 2:
                if len(class_id) == 1:
                    if class_id[0].isnumeric():
                        classes.append(class_id)
                    else:
                        print("Jednoznakowe oznaczenie klasy musi być liczbą.")
                        pass
                elif len(class_id) == 2:
                    if class_id[0].isnumeric() and class_id[1].isalpha():
                        classes.append(class_id)
                    else:
                        print("Dwuznakowe oznaczenie klasy musi być w formacie"
                              " liczby z literą np. '2A'.")
                        pass
            else:
                print("Oznaczenie klasy musi być w formacie samej liczby "
                      "np. '2' lub liczby z literą np. '2A'.")
                pass

        classes = list(set(classes))
        classes.sort()

        self.name = name
        self.subjects = tutor_subjects
        self.classes = classes

# %% Student


class Student:

    def __init__(self):
        self.name = ""
        self.school_class = ""

    def __repr__(self):
        return self.name

    def set_attrs(self):

        while True:
            school_class = input("Podaj oznaczenie klasy do której "
                                 "przypisane zostanie dziecko: ")
            school_class = ''.join(filter(str.isalnum, school_class)).upper()

            if 1 <= len(school_class) <= 2:
                if len(school_class) == 1:
                    if school_class[0].isnumeric() is False:
                        print("Jednoznakowe oznaczenie klasy musi być cyfrą.")
                        pass
                    else:
                        break
                elif len(school_class) == 2:
                    if (school_class[0].isnumeric() is False or
                            school_class[1].isalpha() is False):
                        print("Dwuznakowe oznaczenie klasy musi być w formacie"
                              " cyfry z literą np. '2A'.")
                        pass
                    else:
                        break
            else:
                print("Oznaczenie klasy musi być w formacie samej liczby "
                      "np. '2' lub liczby z literą np. '2A'.")
                pass

        name = input("Podaj imię i nazwisko dziecka, "
                     f"które zostanie przypisane do klasy {school_class}: ")
        name = name.title()

        classes.add(school_class)

        self.name = name
        self.school_class = school_class

# define functions

# %% CREATE_PERSON()


def create_person():

    while True:
        command = input("Podaj komendę (uczen/nauczyciel/wychowawca/exit): ")
        command = ''.join(filter(str.isalpha, command)).lower()

        if command == "exit":
            break
        elif command == "uczen":
            obj = Student()
            obj.set_attrs()
            students.append(obj)
        elif command == "nauczyciel":
            obj = Tutor()
            obj.set_attrs()
            tutors.append(obj)
        elif command == "wychowawca":
            obj = ClassTutor()
            obj.set_attrs()
            class_tutors.append(obj)
        else:
            print("Niepoprawna komenda!\n")
            pass


# %% DISPLAY()


def display():

    while True:
        command = input("Dozwolone komendy: 'klasa', 'wychowawca', "
                        "'nauczyciel', 'uczen', 'exit'.\nWybierz typ obiektu, "
                        "który chcesz wyświetlić: ")
        command = ''.join(filter(str.isalpha, command)).lower()

        if command == "exit":
            break
        elif command == "klasa":

            while True:
                class_id = input("Podaj nazwę klasy: ")
                class_id = ''.join(filter(str.isalnum, class_id)).upper()

                if 1 <= len(class_id) <= 2:
                    if len(class_id) == 1:
                        if class_id[0].isnumeric() is False:
                            print("Jednoznakowe oznaczenie klasy musi "
                                  "być cyfrą.")
                            pass
                        else:
                            break
                    elif len(class_id) == 2:
                        if (class_id[0].isnumeric() is False or
                                class_id[1].isalpha() is False):
                            print("Dwuznakowe oznaczenie klasy musi być "
                                  "w formacie cyfry z literą np. '2A'.")
                            pass
                        else:
                            break
                else:
                    print("Oznaczenie klasy musi być w formacie samej liczby "
                          "np. '2' lub liczby z literą np. '2A'.")
                    pass

            if class_id in classes:
                for tutor in class_tutors:
                    if tutor.school_class == class_id:
                        print(f"Wychowawca: {tutor}")
                for student in students:
                    if student.school_class == class_id:
                        print(f"Uczeń: {student}")
            else:
                print("Ta klasa nie ma określonego wychowawcy.")

        elif command == "wychowawca":
            name = input("Podaj imię i nazwisko wychowowcy: ")
            name = name.title()
            class_name = None

            for class_tutor in class_tutors:
                if class_tutor.name == name:
                    class_name = class_tutor.school_class
                    break

            if not class_name:
                print("Nie znaleziono takiego wychowawcy.")
                continue

            for student in students:
                if student.school_class == class_name:
                    print(f"Uczeń: {student}")

        elif command == "nauczyciel":
            name = input("Podaj imię i nazwisko nauczyciela: ")
            name = name.title()
            tutor_classes = None

            for tutor in tutors:
                if tutor.name == name:
                    tutor_classes = tutor.classes
                    break

            if not tutor_classes:
                print("Nie znaleziono takiego nauczyciela.")
                continue

            for class_tutor in class_tutors:
                if class_tutor.school_class in tutor_classes:
                    print(f"Wychowawca klasy {class_tutor.school_class}: "
                          f"{class_tutor}")

        elif command == "uczen":
            name = input("Podaj imię i nazwisko ucznia: ")
            name = name.title()
            class_name = None

            for student in students:
                if student.name == name:
                    class_name = student.school_class
                    break

            if not class_name:
                print("Nie znaleziono ucznia o takich danych.")
                continue

            for tutor in tutors:
                if class_name in tutor.classes:
                    print(f"Nauczyciel: {tutor}, przedmioty: "
                          f"{', '.join(tutor.subjects)}")
        else:
            print("Niepoprawna komenda!\n")
            pass


# %% MAIN LOOP

while True:
    command = input("Podaj komendę (tworz/wyswietl/exit): ")
    command = ''.join(filter(str.isalpha, command)).lower()

    if command == "exit":
        break
    elif command == "tworz":
        create_person()
    elif command == "wyswietl":
        display()
    else:
        print("Niepoprawna komenda!\n"
              "Dozwolone komendy to 'tworz', 'wyswietl', 'exit'.")
        pass

# %%
