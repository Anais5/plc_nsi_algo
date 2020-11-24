class File1:
    """ File implémentée sur la base d'une liste chainée simple"""
    from algo.struct.liste_simple import Liste

    def __init__(self):
        pass

    def __len__(self):
        pass

    def enfiler(self, valeur):
        """ à faire """
        pass

    def defiler(self):
        """ à faire """
        pass

    def __str__(self):
        pass


class File2:
    """ File implémentée sur la base d'une deque (file double) python """
    from collections import deque

    def __init__(self):
        pass

    def __len__(self):
        pass

    def enfiler(self, valeur):
        """ à faire """
        pass

    def defiler(self):
        """ à faire """
        pass

    def __str__(self):
        pass


class File3:
    """ File implémentée sur la base de deux piles."""
    from algo.struct.piles import Pile1 as Pile

    def __init__(self):
        pass

    def __len__(self):
        pass

    def enfiler(self, valeur):
        """ à faire """
        pass

    def defiler(self):
        """ à faire """
        pass

    def __str__(self):
        pass


class File4:
    """ File implémentée sur la base d'un tableau de taille fixe.
    Pour cela, on prend une list python mais on s'interdit les méthodes
    append, pop, insert. 
    """

    def __init__(self, taille=1024):
        self.__tableau = [None]*taille
        self.__entree = 0
        self.__sortie = 0
        self.__est_pleine = False
        self.__longueur = 0

    def est_vide(self):
        return self.__longueur == 0

    def enfiler(self, valeur):
        if self.__est_pleine:
            raise IndexError("On ne peut pas ajouter de valeur à une file pleine")
        self.__tableau[self.__entree] = valeur
        self.__entree += 1
        if self.__entree >= len(self.__tableau):
            self.__entree = 0
        if self.__entree == self.__sortie:
            self.__est_pleine = True
        self.__longueur += 1

    def defiler(self):
        if self.est_vide():
            raise IndexError("On ne peut pas enlever une valeur à une file vide")
        if self.__est_pleine:
            self.__est_pleine = False
        self.__sortie += 1
        if self.__sortie >= len(self.__tableau):
            self.__sortie = 0
        self.__longueur -= 1
        return self.__tableau[self.__sortie - 1]

    def __len__(self):
        return self.__longueur

    def __str__(self):
        chaine = ""
        if self.__entree <= self.__sortie:
            for i in range(self.__entree, self.__sortie):
                chaine += f"{self.__tableau[self.__entree + i]} -> "
                chaine += str(self.__tableau[self.__sortie])
        else:
            for i in range(self.__entree, len(self.__tableau)):
                chaine += f"{self.__tableau[self.__entree + i]} -> "
            for i in range(self.__sortie):
                chaine += f"{self.__tableau[i]} -> "
            chaine += str(self.__tableau[self.__sortie])
        return chaine