"""Travailler avec des variables

En python, les variables sont déclarées au moment de leur utilisation.
On peut tout de même les déclarer vides mais cela ne change pas grand chose :

"""
var_1 = "Bonjour"   # déclaration + affectation (l'usage classique)
var_2 = None        # ressemble à une déclaration sans affectation...
var_4: int          # déclaration avec un typage
var_5: str = "OMG"  # déclaration + typage + affectation (équivalent à var_1)


# On note que le typage est fort, pas de trans-typage implicite :
var_3 = 4
var_4 = 3
print(var_3 + var_4)
# 7
print(var_1 + " " + var_5)
# "Bonjour OMG"

# Réaliser des opérations sur deux types incompatibles entraine une erreur :
# print(var_4 + var_5)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Il faut explicitement trans-typer les variables :
print(str(var_4) + var_5)
# "3OMG"

# Certains trans-typage sont tout de même possible de manière implicite :
print(5 * .5)  # En multipliant un int et un float, on produit un float
# 2.5


# On note aussi que le typage est dynamique :
a = None
a = "Bonjour"  # ne produit pas d'erreur...
print(a)

b: int = 5
b = False  # ...même quand on a tyé explicitement !
print(b)


# On terminera par le plus important, Python est compatible unicode :
player_name = "🐑"
print('Bonjour ' + player_name)
# Bonjour 🐑

# On peut même utiliser les émojis comme noms de variable ❤️, mais comment ?!






"""Constantes & variables

Python n'empêche globalement rien : vous pouvez accéder aux
propriétés cachées d'une classe, vous pouvez modifier des constantes, etc.

Mais pourquoi ?!
Python veut que l'on fasse attention à ce qu'on fait et nous demande de
bien nommer les choses. Il ne nous bloque pas, mais les linters nous
indiqueront que l'on est en train de faire une bêtise, sans nous en 
empêcher.

Pour différencier les variables et constantes, comme la grande majorité
des langages, Python nous dit de jouer sur la casse :
"""

MA_CONSTANTE = "Jean Jean"
ma_variable = "dodo"
print (MA_CONSTANTE, ma_variable)

# Cela ne change rien à l'usage, je dois juste être vigilant à ne pas modifier
# la première :
MA_CONSTANTE = "Toutouille"    # mauvaise idée !
ma_variable = "la fripouille"  # Ok
print (MA_CONSTANTE, ma_variable)






"""Les structures plus complexes

Au delà des types simples, Python embarque évidement un ensemble d'outils
pour structurer nos données de manière plus complexe. Parmi eux, on compte
- les enums
- les dictionnaires (dict)
- les listes (list), équivalent des tableaux pour les développeurs normaux
- les tuples, qui sont des listes ordonnées


Pour mieux afficher à l'écran ces objets plus complexes, on utilisera la 
merveilleurs librairie pprint
"""
from datetime import date  # on importe aussi date, pour jouer avec ce type
from pprint import pprint

player = {
    "name": 'Joe le rigolo',
    "role": 'invited',
    "birth_date": date(2020, 10, 8)
}
pprint(player)                 # pour afficher tout l'objet
print(player['birth_date'])    # pour accéder à sa date de naissance 👶


roles = ['invited', 'user', 'admin']
pprint(roles)  # pour afficher tout l'objet
print('toto' in roles)
# False
print('user' in roles)
# True


# On peut regretter de stocker les rôles dans un tableau, car on pourrait
# malencontreusement des doublons :
roles = ['invited', 'user', 'admin', 'user', 'admin']
pprint(roles)
# ['invited', 'user', 'admin', 'user', 'admin']
pprint('admin' in roles)
# True


# Ce n'est pas dramatique, mais on dispose d'un outil plus pertinent, les sets :
roles = {'invited', 'user', 'admin', 'user', 'admin'}
pprint(roles)
# {'invited', 'user', 'admin'}
pprint('user' in roles)
# True



"""Bon, un peu de pratique !

Il nous reste beaucoup à dire autour de la syntaxe du langage,
mais cela risque de vite devenir soporifique (j'arrive toujours à placer un Pokemon).




"""