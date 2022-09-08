# -*- coding: utf-8 -*-

# define global variables
SUBJECTS = ["język polski", "polski", "język niemiecki", "niemiecki",
            "angielski", "język angielski", "matematyka",  "biologia",
            "historia", "muzyka", "technika", "plastyka", "wf", "wos",
            "informatyka", "religia", "etyka", "geografia"]

# define classes

# %% WYCHOWAWCA


class Wychowawca:

    def __init__(self):
        self.name = None
        self.school_class = None

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

# %% NAUCZYCIEL


class Nauczyciel:

    def __init__(self, name, subjects, classes):
        self.name = None
        self.subjects = []
        self.classes = []

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
                for i in SUBJECTS:
                    print(i)
            elif subject not in SUBJECTS:
                print("Brak przedmiotu na liście dostępnych przedmiotów.\n"
                      "/aby wyświetlić listę dostępnych przedmitów wpisz "
                      "'przedmioty'/")
                pass
            else:
                tutor_subjects.append(subject)

        while True:
            print("/aby zakończyć wprowadzanie klas wpisz 'exit'/")
            user_input = input("Wprowadź oznaczenia klas, "
                               f"które uczy nauczyciel {name}: ")
            user_input = ''.join(filter(str.isalnum, user_input)).upper()

            if user_input == "EXIT":
                break
            elif 1 <= len(user_input) <= 2:
                if len(user_input) == 1:
                    if user_input[0].isnumeric():
                        classes.append(user_input)
                    else:
                        print("Jednoznakowe oznaczenie klasy musi być liczbą.")
                        pass
                elif len(user_input) == 2:
                    if user_input[0].isnumeric() and user_input[1].isalpha():
                        classes.append(user_input)
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

# %% UCZEN


class Uczen:

    def __init__(self, name, school_class):
        self.name = None
        self.school_class = None

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

        self.name = name
        self.school_class = school_class

# %%
