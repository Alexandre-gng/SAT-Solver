"""
Stockage de l'instance SAT :

- Une liste des clauses
- Chaque clause possède une longueur variable (la taille de la clause quoi)
- Cette liste est constituée d'entiers, chaque entier correspond à une variable de l'instance
    -> Un entier négatif indique que cette variable est en NOT <!>

On crée une classe "Instance" qui comporte :
- La liste des Clauses (liste de liste)
- nombre de clauses
- nombre de variables

==================
INDICATIONS SUR LE CNF FORMAT :
- c are comments
- p indicates the parameters :
    - n variables
    - m clauses

"""


"""
OBJECTIVES:
- Parser correctement le cnf txt en récupérant une liste de liste propre OK
- Vérificateur de literal OK
- Faire une classe adapté pour chaque instance 
- Développer l'algorithme DPLL

"""
from parser import ccf_parser
from SatSolver import unit_propagation, DPLL

instance = ccf_parser("ccf_files/ccf2.cnf")
print(instance)

print(DPLL(instance))