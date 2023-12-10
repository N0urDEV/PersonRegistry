from abc import ABC, abstractmethod

class Personne(ABC):
    def __init__(self, code, nom, prenom, age):
        self._code = code
        self._nom = nom
        self._prenom = prenom
        self._age = age

    @property
    def code(self):
        return self._code

    @property
    def nom(self):
        return self._nom

    @property
    def prenom(self):
        return self._prenom

    @property
    def age(self):
        return self._age

    def get_code(self):
        return self._code

    def get_nom(self):
        return self._nom

    def get_prenom(self):
        return self._prenom

    def get_age(self):
        return self._age

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Employe(Personne):
    def __init__(self, code, nom, prenom, age, grade):
        super().__init__(code, nom, prenom, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    def get_grade(self):
        return self._grade

    def __str__(self):
        return f"Employé: {self._nom} {self._prenom}, Code: {self._code}, Age: {self._age}, Grade: {self._grade}"
    
    def __eq__(self, other):
        if isinstance(other, Employe):
            return self._code == other._code
        return False

class Eleve(Personne):
    def __init__(self, code, nom, prenom, age, niveau, moyenne):
        super().__init__(code, nom, prenom, age)
        self._niveau = niveau
        self._moyenne = moyenne

    @property
    def niveau(self):
        return self._niveau

    @property
    def moyenne(self):
        return self._moyenne

    def get_niveau(self):
        return self._niveau

    def get_moyenne(self):
        return self._moyenne

    def __str__(self):
        return f"Élève: {self._nom} {self._prenom}, Code: {self._code}, Age: {self._age}, Niveau: {self._niveau}, Moyenne: {self._moyenne}"

    def __eq__(self, other):
        if isinstance(other, Eleve):
            return self._code == other._code
        return False

class Test:
    @staticmethod
    def run():
        employes = [
            Employe("E001", "Ahmed", "Ezzaoui", 30, "Manager"),
            Employe("E002", "Ali", "Aliati", 25, "Analyste"),
            Employe("E003", "Noureddine", "Achbili", 19, "Developpeur")
        ]

        eleves = [
            Eleve("S001", "Nada", "Elhourri", 18, "Lycee", 16.5),
            Eleve("S002", "Anass", "Aaroui", 17, "College", 14.2),
            Eleve("S003", "Khalid", "Zaizai", 16, "Lycee", 15.8)
        ]

        # Affichage
        for employe in employes:
            print(employe)

        for eleve in eleves:
            print(eleve)

        # Affichage du nombre dobjets crees
        print(f"\nNombre d'objets créés:")
        print(f"Nombre d'employés: {len(employes)}")
        print(f"Nombre d'élèves: {len(eleves)}")

Test.run()
