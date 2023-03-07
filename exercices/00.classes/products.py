class Product:
    def __init__(self, cost, price, marque):
        self.cost = cost
        self.price = price
        self.marque = marque

    def afficher_attributs(self):
        print("Attributs pour le véhicule :")
        print("- Cout :", self.cost)
        print("- Prix :", self.price)
        print("- Marque :", self.marque)

class Meubles(Product):
    def __init__(self, cost, price, marque):
        self.cost = cost
        self.price = price
        self.marque = marque
    


class Canape(Meubles):
    def __init__(self, matériaux, couleur, dimensions, cost, price, marque):
        self.matériaux = matériaux
        self.couleur = couleur
        self.dimensions = dimensions
        self.cost = cost
        self.price = price
        self.marque = marque

    def afficher_attributs(self):
        print()
        print("- matériaux :", self.matériaux)
        print("- couleur :", self.couleur)
        print("- dimensions :", self.dimensions)
        print("- Cout :", self.cost)
        print("- Prix :", self.price)
        print("- Marque :", self.marque)

class Chaise(Meubles):
    def __init__(self, matériaux, couleur, dimensions, cost, price, marque):
        self.matériaux = matériaux
        self.couleur = couleur
        self.dimensions = dimensions
        self.cost = cost
        self.price = price
        self.marque = marque

    def afficher_attributs(self):
        print()
        print("- matériaux :", self.matériaux)
        print("- couleur :", self.couleur)
        print("- dimensions :", self.dimensions)
        print("- Cout :", self.cost)
        print("- Prix :", self.price)
        print("- Marque :", self.marque)

class Table(Meubles):
    def __init__(self, matériaux, couleur, dimensions, cost, price, marque):
        self.matériaux = matériaux
        self.couleur = couleur
        self.dimensions = dimensions
        self.cost = cost
        self.price = price
        self.marque = marque

    def afficher_attributs(self):
        print()
        print("- matériaux :", self.matériaux)
        print("- couleur :", self.couleur)
        print("- dimensions :", self.dimensions)
        print("- Cout :", self.cost)
        print("- Prix :", self.price)
        print("- Marque :", self.marque)

Canape1 = Canape("Cuir", "Blanc", "200x100x80", 1000, 2000, "OKLM")
Canape2 = Canape("Tissu", "Bleu", "150x90x70", 800, 1600, "SIESTA")
Chaise1 = Chaise("Plastique", "Rouge", "50x50x70", 50, 100, "PEPOUSE")
Chaise2 = Chaise("Métal", "Gris", "60x60x80", 75, 150, "PEPOUSE")
Table1 = Table("Verre", "Transparent", "120x60x75", 350, 700, "TEX")
Table2 = Table("Bois", "Chêne", "150x80x75", 250, 500, "TEX")



Canape1.afficher_attributs()
Canape2.afficher_attributs()
Chaise1.afficher_attributs()
Chaise2.afficher_attributs()
Table1.afficher_attributs()
Table2.afficher_attributs()

